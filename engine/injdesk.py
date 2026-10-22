#!/usr/bin/env python3
"""
Injective Market Desk — Phase 0 engine.

Measures live perp market microstructure across every derivative market on
Injective mainnet using only the public, keyless LCD endpoint.

Stdlib only (urllib + threads). No API keys, no node, no third-party packages.

Usage:
    python engine/injdesk.py sweep            # full sweep -> data/latest.json
    python engine/injdesk.py sweep --threads 4
    python engine/injdesk.py table            # print the 20 worst markets
    python engine/injdesk.py check BTC/USDC PERP

Data contract (what the rest of the pipeline consumes): data/latest.json
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LCD = "https://sentry.lcd.injective.network"
CG_DERIV = "https://api.coingecko.com/api/v3/derivatives/exchanges/injective_futures?include_tickers=all"

# Orderbook prices on Injective derivatives are scaled by 10^6 relative to the
# human quote price. Verified 2026-10-22 against spot: BTC mid/1e6 = 81,291
# (spot 81,262), ETH 2,383.70 (2,382.32), DOGE 0.0785 (0.078658).
PRICE_SCALE = 1_000_000.0

# Bands used for depth measurement, in basis points from mid.
BANDS = (25, 100, 500)

HTTP_TIMEOUT = 30
UA = "inj-market-desk/0.1 (+https://github.com/nwfella)"


# ----------------------------------------------------------------------------
# HTTP
# ----------------------------------------------------------------------------
def get_json(url: str, tries: int = 3) -> dict:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"user-agent": UA, "accept": "application/json"})
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
                return json.loads(r.read())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            time.sleep(0.6 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url} :: {last}")


# ----------------------------------------------------------------------------
# Market metadata
# ----------------------------------------------------------------------------
def fetch_markets() -> list[dict]:
    d = get_json(f"{LCD}/injective/exchange/v1beta1/derivative/markets")
    out = []
    for wrap in d.get("markets", []):
        m = wrap["market"]
        out.append(
            {
                "ticker": m["ticker"],
                "market_id": m["market_id"],
                "quote_denom": m.get("quote_denom", ""),
                "oracle_type": m.get("oracle_type", ""),
                "initial_margin_ratio": _f(m.get("initial_margin_ratio")),
                "maintenance_margin_ratio": _f(m.get("maintenance_margin_ratio")),
                "maker_fee_bps": round(_f(m.get("maker_fee_rate")) * 10_000, 2),
                "taker_fee_bps": round(_f(m.get("taker_fee_rate")) * 10_000, 2),
            }
        )
    return out


def _f(v) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


# ----------------------------------------------------------------------------
# Orderbook measurement
# ----------------------------------------------------------------------------
def fetch_book(market_id: str) -> dict:
    return get_json(f"{LCD}/injective/exchange/v1beta1/derivative/orderbook/{market_id}")


def measure_book(book: dict) -> dict:
    """Scale-invariant spread/imbalance + scaled depth. Never raises."""
    buys = book.get("buys_price_level") or []
    sells = book.get("sells_price_level") or []

    def levels(side):
        out = []
        for lv in side:
            p = _f(lv.get("p")) / PRICE_SCALE
            q = _f(lv.get("q"))
            if p > 0 and q > 0:
                out.append((p, q))
        out.sort(key=lambda x: x[0], reverse=(side is buys))
        return out

    bids, asks = levels(buys), levels(sells)
    res = {
        "levels_bid": len(bids),
        "levels_ask": len(asks),
        "bid": None,
        "ask": None,
        "mid": None,
        "spread_bps": None,
        "depth_usd": {},
        "imbalance_25": None,
        "depth_hhi": None,
        "two_sided": bool(bids and asks),
    }
    for b in BANDS:
        res["depth_usd"][str(b)] = 0.0

    if bids:
        res["bid"] = bids[0][0]
    if asks:
        res["ask"] = asks[0][0]

    if not (bids and asks):
        return res

    best_bid, best_ask = bids[0][0], asks[0][0]
    mid = (best_bid + best_ask) / 2.0
    res["mid"] = mid
    if best_ask > best_bid > 0:
        res["spread_bps"] = round((best_ask - best_bid) / mid * 10_000, 2)

    for band in BANDS:
        # Depth is measured from the TOUCH (best bid / best ask), not from mid:
        # a market quoting 60 bps wide would otherwise register zero depth even
        # though size is resting at the touch. Spread is a separate metric.
        bid_floor = best_bid * (1 - band / 10_000.0)
        ask_ceiling = best_ask * (1 + band / 10_000.0)
        bid_usd = sum(p * q for p, q in bids if p >= bid_floor)
        ask_usd = sum(p * q for p, q in asks if p <= ask_ceiling)
        # Two-sided depth: the thinner side is what a taker can actually use.
        res["depth_usd"][str(band)] = round(min(bid_usd, ask_usd), 2)
        if band == 25:
            total = bid_usd + ask_usd
            if total > 0:
                res["imbalance_25"] = round((bid_usd - ask_usd) / total, 4)

    notionals = [p * q for p, q in bids + asks]
    total = sum(notionals)
    if total > 0:
        res["depth_hhi"] = round(sum((n / total) ** 2 for n in notionals), 4)
    return res


# ----------------------------------------------------------------------------
# External volume reference (free, cached, optional)
# ----------------------------------------------------------------------------
def fetch_volume_map(max_age_s: int = 1800) -> dict:
    cache = DATA / "cg_volume.json"
    if cache.exists() and (time.time() - cache.stat().st_mtime) < max_age_s:
        try:
            return json.loads(cache.read_text())
        except json.JSONDecodeError:
            pass
    try:
        d = get_json(CG_DERIV, tries=2)
    except RuntimeError:
        if cache.exists():
            try:
                stale = json.loads(cache.read_text())
                stale["_stale"] = True
                return stale
            except json.JSONDecodeError:
                pass
        return {}
    m: dict[str, float] = {}
    for t in d.get("tickers", []):
        base = (t.get("base") or "").upper()
        try:
            v = float(t.get("converted_volume", {}).get("usd") or 0)
        except (TypeError, ValueError):
            continue
        if base and v > 0:
            m[base] = max(m.get(base, 0.0), v)
    m["_fetched_at"] = int(time.time())
    DATA.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(m))
    return m


def base_symbol(ticker: str) -> str:
    return ticker.split("/")[0].split("-")[0].upper()


# ----------------------------------------------------------------------------
# Scoring — documented, reproducible, renormalised when inputs are missing
# ----------------------------------------------------------------------------
WEIGHTS = {"two_sided": 25, "spread": 25, "depth": 25, "volume": 15, "balance": 10}


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def score_market(row: dict) -> tuple[float, str]:
    parts: dict[str, tuple[float, int]] = {}

    parts["two_sided"] = (1.0 if row.get("two_sided") else 0.0, WEIGHTS["two_sided"])

    sp = row.get("spread_bps")
    if sp is not None:
        # 2 bps or tighter = perfect; 200 bps or wider = zero.
        parts["spread"] = (clamp(1 - (sp - 2) / 198), WEIGHTS["spread"])

    d25 = (row.get("depth_usd") or {}).get("25") or 0.0
    # $1k two-sided depth (from the touch) -> 0; $1M -> 1 (three decades).
    parts["depth"] = (clamp(math.log10(max(d25, 1) / 1_000.0) / 3), WEIGHTS["depth"])

    vol = row.get("volume_24h_usd")
    if vol:
        # $10k/day -> 0; $1M/day -> 1 (two decades).
        parts["volume"] = (clamp(math.log10(max(vol, 1) / 10_000.0) / 2), WEIGHTS["volume"])

    imb = row.get("imbalance_25")
    if imb is not None:
        parts["balance"] = (1 - abs(imb), WEIGHTS["balance"])

    wsum = sum(w for _, w in parts.values())
    if wsum == 0:
        return 0.0, "F"
    score = 100 * sum(v * w for v, w in parts.values()) / wsum
    # A market with no two-sided quote cannot be "healthy" whatever its volume:
    # cap it so a busy-but-unquoted market never grades above E.
    if not row.get("two_sided"):
        score = min(score, 25.0)
    score = round(score, 1)
    if score >= 80:
        g = "A"
    elif score >= 65:
        g = "B"
    elif score >= 50:
        g = "C"
    elif score >= 35:
        g = "D"
    elif score >= 20:
        g = "E"
    else:
        g = "F"
    return score, g


# ----------------------------------------------------------------------------
# Sweep
# ----------------------------------------------------------------------------
def sweep(threads: int = 6) -> dict:
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "history").mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    markets = fetch_markets()
    vol = fetch_volume_map()

    def work(m: dict) -> dict:
        row = dict(m)
        try:
            book = fetch_book(m["market_id"])
            row.update(measure_book(book))
        except Exception as e:  # noqa: BLE001 — a dead market must not kill the sweep
            row.update(
                {
                    "levels_bid": 0,
                    "levels_ask": 0,
                    "two_sided": False,
                    "spread_bps": None,
                    "depth_usd": {str(b): 0.0 for b in BANDS},
                    "imbalance_25": None,
                    "depth_hhi": None,
                    "error": f"{type(e).__name__}",
                }
            )
        b = base_symbol(m["ticker"])
        row["base"] = b
        row["volume_24h_usd"] = round(vol[b], 2) if b in vol else None
        row["score"], row["grade"] = score_market(row)
        if row.get("spread_bps") is not None:
            row["roundtrip_bps"] = round(row["spread_bps"] + 2 * row.get("taker_fee_bps", 0.0), 2)
        else:
            row["roundtrip_bps"] = None
        return row

    with ThreadPoolExecutor(max_workers=threads) as ex:
        rows = list(ex.map(work, markets))

    rows.sort(key=lambda r: (r["score"], r["ticker"]))
    two_sided = [r for r in rows if r.get("two_sided")]
    spreads = [r["spread_bps"] for r in two_sided if r.get("spread_bps") is not None]
    d25 = [r["depth_usd"]["25"] for r in two_sided]
    vols = [r["volume_24h_usd"] for r in rows if r.get("volume_24h_usd")]

    snap = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": {
            "orderbook": LCD + "/injective/exchange/v1beta1/derivative/orderbook/{market_id}",
            "markets": LCD + "/injective/exchange/v1beta1/derivative/markets",
            "volume": "coingecko injective_futures tickers (24h, third-party)",
            "price_scale": PRICE_SCALE,
            "volume_fetched_at": vol.get("_fetched_at"),
            "volume_stale": bool(vol.get("_stale")),
        },
        "summary": {
            "markets": len(rows),
            "two_sided": len(two_sided),
            "empty_or_one_sided": len(rows) - len(two_sided),
            "empty_pct": round((len(rows) - len(two_sided)) / max(len(rows), 1) * 100, 1),
            "median_spread_bps": round(statistics.median(spreads), 2) if spreads else None,
            "p90_spread_bps": round(sorted(spreads)[int(len(spreads) * 0.9)], 2) if spreads else None,
            "median_depth_usd_25": round(statistics.median(d25), 2) if d25 else None,
            "total_depth_usd_25": round(sum(d25), 2),
            "median_volume_24h_usd": round(statistics.median(vols), 2) if vols else None,
            "total_volume_24h_usd": round(sum(vols), 2) if vols else None,
            "median_score": round(statistics.median([r["score"] for r in rows]), 1),
            "elapsed_s": round(time.time() - t0, 1),
        },
        "markets": rows,
    }
    (DATA / "latest.json").write_text(json.dumps(snap, indent=1))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H")
    (DATA / "history" / f"{stamp}.json").write_text(
        json.dumps(
            {
                "generated_at": snap["generated_at"],
                "summary": snap["summary"],
                "markets": [
                    {
                        "ticker": r["ticker"],
                        "score": r["score"],
                        "grade": r["grade"],
                        "spread_bps": r.get("spread_bps"),
                        "depth_usd_25": r["depth_usd"]["25"],
                        "two_sided": r["two_sided"],
                        "volume_24h_usd": r.get("volume_24h_usd"),
                    }
                    for r in rows
                ],
            }
        )
    )
    return snap


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def cmd_table(n: int = 20) -> None:
    snap = json.loads((DATA / "latest.json").read_text())
    s = snap["summary"]
    print(f"snapshot {snap['generated_at']}  markets={s['markets']}  "
          f"empty/one-sided={s['empty_or_one_sided']} ({s['empty_pct']}%)  "
          f"median spread={s['median_spread_bps']}bps  sweep={s['elapsed_s']}s")
    hdr = f"{'ticker':<22}{'score':>6}{'g':>3}{'spread':>8}{'depth25$':>12}{'vol24h$':>13}{'rt bps':>8}"
    print(hdr)
    print("-" * len(hdr))
    for r in snap["markets"][:n]:
        spread = "—" if r.get("spread_bps") is None else f"{r['spread_bps']:.1f}"
        rt = "—" if r.get("roundtrip_bps") is None else f"{r['roundtrip_bps']:.1f}"
        print(
            f"{r['ticker']:<22}{r['score']:>6.1f}{r['grade']:>3}{spread:>8}"
            f"{r['depth_usd']['25']:>12,.0f}"
            f"{(r['volume_24h_usd'] or 0):>13,.0f}"
            f"{rt:>8}"
        )


def cmd_check(ticker: str) -> None:
    snap = json.loads((DATA / "latest.json").read_text())
    for r in snap["markets"]:
        if r["ticker"].lower() == ticker.lower():
            print(json.dumps(r, indent=2))
            return
    print(f"not found: {ticker}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("sweep")
    sp.add_argument("--threads", type=int, default=6)
    t = sub.add_parser("table")
    t.add_argument("-n", type=int, default=20)
    c = sub.add_parser("check")
    c.add_argument("ticker")
    a = ap.parse_args(argv)

    if a.cmd == "sweep":
        snap = sweep(threads=a.threads)
        s = snap["summary"]
        print(
            f"swept {s['markets']} markets in {s['elapsed_s']}s | "
            f"{s['empty_or_one_sided']} empty/one-sided ({s['empty_pct']}%) | "
            f"median spread {s['median_spread_bps']} bps | median score {s['median_score']}"
        )
    elif a.cmd == "table":
        cmd_table(a.n)
    elif a.cmd == "check":
        cmd_check(a.ticker)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
