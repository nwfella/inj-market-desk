#!/usr/bin/env python3
"""
Injective Market Desk — static site generator.

Reads data/latest.json and emits a fully self-contained dashboard plus one
print-ready scorecard per focus market. No fetch/XHR, no CDN, no fonts, no
external anything: the snapshot is baked into each page as inline JSON so the
site works on locked-down networks (github.io is filtered in some corporate
environments).

Usage:
    python build_site.py                 # -> docs/index.html + docs/scorecards/*
    python build_site.py --out docs
"""

from __future__ import annotations

import argparse
import html
import json
import statistics
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

CONTROLS = ["BTC/USDC PERP", "ETH/USDC PERP", "INJ/USDC PERP"]
FOCUS_N = 10


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def esc(s) -> str:
    return html.escape(str(s), quote=True)


def slug(ticker: str) -> str:
    return ticker.lower().replace("/", "-").replace(" ", "-")


def usd(v, dash="—") -> str:
    if v is None:
        return dash
    a = abs(v)
    if a >= 1_000_000:
        return f"${v/1_000_000:,.2f}M"
    if a >= 1_000:
        return f"${v/1_000:,.1f}k"
    return f"${v:,.0f}"


def bps(v) -> str:
    if v is None:
        return "—"
    return f"{v:,.2f}" if abs(v) < 1 else f"{v:,.1f}"


def pct(v) -> str:
    return "—" if v is None else f"{v:,.1f}%"


def grade_class(g: str) -> str:
    return f"g{g}"


# ---------------------------------------------------------------------------
# focus selection
# ---------------------------------------------------------------------------
def pick_focus(snap: dict) -> list[str]:
    """3 benchmarks + a deliberate mix of two failure modes.

    - 3 worst markets that have 24h volume but NO two-sided quote  -> RWA / integrity pitch
      ("volume is arriving, book is not")
    - 4 worst QUOTED markets with real volume                      -> launch-desk pitch
      ("quoted, but 300 bps wide and $40 deep")

    A market with no volume and no book is not a customer either way.
    """
    rows = {r["ticker"]: r for r in snap["markets"]}
    picks = [c for c in CONTROLS if c in rows]

    empty = [
        r
        for r in snap["markets"]
        if r["ticker"] not in picks and not r.get("two_sided") and (r.get("volume_24h_usd") or 0) >= 50_000
    ]
    empty.sort(key=lambda r: -(r.get("volume_24h_usd") or 0))
    picked_empty, fx_seen = [], False
    for r in empty:
        is_fx = r["ticker"].upper().startswith("USD")
        if is_fx and fx_seen:
            continue  # one FX pair is a pattern; three is redundant outreach
        fx_seen = fx_seen or is_fx
        picked_empty.append(r["ticker"])
        if len(picked_empty) == 3:
            break
    picks += picked_empty

    quoted = [
        r
        for r in snap["markets"]
        if r["ticker"] not in picks and r.get("two_sided") and (r.get("volume_24h_usd") or 0) >= 50_000
    ]
    quoted.sort(key=lambda r: (r["score"], -(r.get("volume_24h_usd") or 0)))
    picks += [r["ticker"] for r in quoted[:4]]

    if len(picks) < FOCUS_N:  # relax the volume floor
        for r in sorted(snap["markets"], key=lambda r: r["score"]):
            if r["ticker"] not in picks and (r.get("volume_24h_usd") or 0) >= 10_000:
                picks.append(r["ticker"])
            if len(picks) >= FOCUS_N:
                break
    return picks[:FOCUS_N]


# ---------------------------------------------------------------------------
# diagnosis + narrative (deterministic, no LLM)
# ---------------------------------------------------------------------------
def diagnose(row: dict, peer: dict) -> list[dict]:
    """Return [{kind, text}] problems found, worst first."""
    out = []
    sp = row.get("spread_bps")
    d25 = (row.get("depth_usd") or {}).get("25") or 0
    vol = row.get("volume_24h_usd") or 0
    hhi = row.get("depth_hhi")
    imb = row.get("imbalance_25")

    if not row.get("two_sided"):
        out.append(
            {
                "kind": "no-book",
                "text": "No two-sided quote at snapshot time. The market could not be traded at any "
                "size without crossing a one-sided book, whatever its 24h volume says.",
            }
        )
    else:
        if sp is not None and sp > 100:
            out.append(
                {
                    "kind": "wide",
                    "text": f"Spread is {sp:,.1f} bps, {(sp / max(peer['spread_bps'] or 1, 0.01)):.0f}× "
                    f"wider than BTC ({peer['spread_bps']:.1f} bps). A round trip costs "
                    f"{row.get('roundtrip_bps') or sp:,.1f} bps before any price move.",
                }
            )
        elif sp is not None and sp > 25:
            out.append(
                {
                    "kind": "wide-mid",
                    "text": f"Spread is {sp:,.1f} bps versus {peer['spread_bps']:.1f} bps on BTC — "
                    f"tradeable for retail size, expensive for anyone hedging.",
                }
            )
        if d25 < 5_000:
            out.append(
                {
                    "kind": "thin",
                    "text": f"Two-sided depth within 25 bps of the touch is {usd(d25)}. "
                    f"BTC holds {usd((peer.get('depth_usd') or {}).get('25'))} in the same band.",
                }
            )
        if hhi is not None and hhi > 0.6:
            out.append(
                {
                    "kind": "concentrated",
                    "text": f"One level holds {hhi*100:,.0f}% of resting notional (HHI {hhi:.2f}). "
                    "The quote is a placeholder, not a market: pull it and the book is empty.",
                }
            )
        if imb is not None and abs(imb) > 0.7:
            side = "bid" if imb > 0 else "ask"
            out.append(
                {
                    "kind": "imbalanced",
                    "text": f"Book is {abs(imb)*100:,.0f}% one-sided toward the {side}. "
                    "Directional resting interest, not market making.",
                }
            )

    if vol >= 100_000 and (not row.get("two_sided") or d25 < 5_000):
        out.append(
            {
                "kind": "vol-gap",
                "text": f"24h volume is {usd(vol)} against {usd(d25)} of two-sided depth. "
                "Volume is arriving without a book to absorb it — the fill quality is not visible "
                "from the volume number alone.",
            }
        )
    if not out:
        out.append(
            {
                "kind": "ok",
                "text": "Two-sided, reasonably tight and deep for its volume tier. "
                "No structural problem detected at this snapshot.",
            }
        )
    return out


def actions(row: dict) -> list[str]:
    acts = []
    if not row.get("two_sided"):
        acts.append(
            "Get a two-sided quote resting before spending on anything else: a market with no bid "
            "and no ask converts zero visitors regardless of listing spend."
        )
        acts.append(
            "Decide whether the market is a trading venue or a listing trophy. If nobody is "
            "obligated to quote it, budget for a maker incentive instead of more marketing."
        )
    else:
        sp = row.get("spread_bps") or 0
        d25 = (row.get("depth_usd") or {}).get("25") or 0
        hhi = row.get("depth_hhi") or 0
        if sp > 100:
            acts.append(f"Tighten the touch below 100 bps (currently {sp:,.1f}).")
        if d25 < 5_000:
            acts.append(f"Put at least $5k of two-sided size within 25 bps (currently {usd(d25)}).")
        if hhi > 0.6:
            acts.append("Split the single resting level into 3+ levels — one level at 80% depth is a quote, not liquidity.")
    acts.append(
        "Re-measure on a fixed cadence. One snapshot is an anecdote; the hourly series is what "
        "tells you whether a maker incentive worked."
    )
    return acts[:4]


def verdict(row: dict) -> str:
    g = row.get("grade")
    s = row.get("score", 0)
    if not row.get("two_sided"):
        return (
            f"<b>Grade {g} ({s}/100) — not tradeable.</b> The book is empty or one-sided, so the "
            f"market's {usd(row.get('volume_24h_usd') or 0)} of 24h volume is not currently "
            "reachable by a taker."
        )
    if s >= 65:
        return (
            f"<b>Grade {g} ({s}/100) — healthy for its tier.</b> Two-sided, "
            f"{bps(row.get('spread_bps'))} bps wide with {usd((row.get('depth_usd') or {}).get('25'))} "
            "of depth inside 25 bps."
        )
    return (
        f"<b>Grade {g} ({s}/100) — quoted but fragile.</b> "
        f"{bps(row.get('spread_bps'))} bps wide, "
        f"{usd((row.get('depth_usd') or {}).get('25'))} of two-sided depth inside 25 bps."
    )


# ---------------------------------------------------------------------------
# HTML: scorecard
# ---------------------------------------------------------------------------
def render_scorecard(row: dict, peer: dict, snap: dict, outdir: Path) -> Path:
    probs = diagnose(row, peer)
    acts = actions(row)
    mk = row.get("market_id", "")
    levels_bid = row.get("levels_bid", 0)
    levels_ask = row.get("levels_ask", 0)
    fees = row.get("taker_fee_bps")

    def cmp_line(label, mine, theirs):
        return (
            f"<tr><td>{esc(label)}</td><td class='num'>{mine}</td>"
            f"<td class='num'>{theirs}</td></tr>"
        )

    def lv(r):
        return f"{r.get('levels_bid', 0)} / {r.get('levels_ask', 0)}"

    def nn(f, v):
        return "—" if v is None else f(v)

    metric_rows = "".join(
        [
            cmp_line("Health score", nn(lambda x: f"{x:.1f}", row.get("score")), nn(lambda x: f"{x:.1f}", peer.get("score"))),
            cmp_line("Spread (bps)", bps(row.get("spread_bps")), bps(peer.get("spread_bps"))),
            cmp_line("Depth ≤25 bps (USD)", usd((row.get("depth_usd") or {}).get("25")), usd((peer.get("depth_usd") or {}).get("25"))),
            cmp_line("Depth ≤100 bps (USD)", usd((row.get("depth_usd") or {}).get("100")), usd((peer.get("depth_usd") or {}).get("100"))),
            cmp_line("Book concentration (HHI)", nn(lambda x: f"{x:.2f}", row.get("depth_hhi")), nn(lambda x: f"{x:.2f}", peer.get("depth_hhi"))),
            cmp_line("Book imbalance", nn(lambda x: f"{x:+.0%}", row.get("imbalance_25")), nn(lambda x: f"{x:+.0%}", peer.get("imbalance_25"))),
            cmp_line("Levels (bid / ask)", lv(row), lv(peer)),
            cmp_line("24h volume (USD)", usd(row.get("volume_24h_usd")), usd(peer.get("volume_24h_usd"))),
            cmp_line("Round trip: spread + 2×taker", bps(row.get("roundtrip_bps")), bps(peer.get("roundtrip_bps"))),
        ]
    )

    prob_html = "".join(f"<li><span class='tag'>{esc(p['kind'])}</span> {esc(p['text'])}</li>" for p in probs)
    act_html = "".join(f"<li>{esc(a)}</li>" for a in acts)

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(row['ticker'])} — Injective market scorecard</title>
<style>
:root{{--bg:#0b0d10;--panel:#14181d;--line:#232a33;--fg:#e8edf3;--dim:#8b98a8;--acc:#37d39b;--warn:#f2b13c;--bad:#ef5f6b;--serif:Georgia,'Times New Roman',serif;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:860px;margin:0 auto;padding:34px 22px 60px}}
.kicker{{font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}}
h1{{font:700 34px/1.1 var(--serif);margin:10px 0 4px;letter-spacing:-.01em}}
.sub{{color:var(--dim);font-size:13px;margin-bottom:22px}}
.verdict{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--acc);padding:16px 18px;border-radius:6px;margin:18px 0 26px}}
.verdict b{{font-size:16px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:0 0 26px}}
.cell{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:12px 14px}}
.cell .k{{font:600 10px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-bottom:7px}}
.cell .v{{font:700 20px/1.1 var(--mono)}}
h2{{font:700 13px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin:30px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line)}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}}
th{{font:600 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--dim)}}
td.num,th.num{{text-align:right;font-family:var(--mono)}}
ul{{margin:0;padding-left:18px}}li{{margin:9px 0}}
.tag{{display:inline-block;font:600 10px/1 var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--bg);background:var(--warn);padding:3px 6px;border-radius:3px;margin-right:6px;vertical-align:1px}}
.tag.no-book,.tag.thin,.tag.concentrated{{background:var(--bad)}}
.tag.ok{{background:var(--acc)}}
.foot{{margin-top:34px;padding-top:14px;border-top:1px solid var(--line);color:var(--dim);font-size:12px}}
.note{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:12px 14px;color:var(--dim);font-size:12.5px}}
@media print{{
 body{{background:#fff;color:#111}}
 .wrap{{max-width:none;padding:0}}
 .cell,.verdict,.note{{background:#fff;border-color:#ccc}}
 h1{{color:#111}} .kicker,h2,.sub,.foot{{color:#555}}
 td,th{{border-color:#ddd}} .verdict{{border-left-color:#111}}
}}
</style></head><body><div class="wrap">
<div class="kicker">Injective Market Desk · market scorecard</div>
<h1>{esc(row['ticker'])}</h1>
<div class="sub">Snapshot {esc(snap['generated_at'])} · oracle {esc(row.get('oracle_type','—'))} · market <code>{esc(mk[:18])}…</code></div>

<div class="verdict">{verdict(row)}</div>

<div class="grid">
  <div class="cell"><div class="k">Health score</div><div class="v">{row.get('score'):.1f}<span style="color:var(--dim);font-size:14px"> /100 · {esc(row.get('grade'))}</span></div></div>
  <div class="cell"><div class="k">Spread</div><div class="v">{bps(row.get('spread_bps'))}<span style="color:var(--dim);font-size:14px"> bps</span></div></div>
  <div class="cell"><div class="k">Depth ≤25 bps</div><div class="v">{usd((row.get('depth_usd') or {}).get('25'))}</div></div>
  <div class="cell"><div class="k">24h volume</div><div class="v">{usd(row.get('volume_24h_usd'))}</div></div>
</div>

<h2>What the book says</h2>
<ul>{prob_html}</ul>

<h2>Versus the benchmark</h2>
<table>
<tr><th>Metric</th><th class="num">{esc(row['ticker'].split('/')[0])}</th><th class="num">BTC/USDC PERP</th></tr>
{metric_rows}
</table>

<h2>What to do next</h2>
<ul>{act_html}</ul>

<div class="note">Taker fee on this market reads {bps(fees)} bps from the market metadata
(<code>taker_fee_rate</code>), so the round-trip column is dominated by spread, not fees. Funding,
open interest and maker identity are not in this snapshot — Phase 1 adds them from the indexer.</div>

<div class="foot">
Measured, not estimated: order books read from Injective's public LCD at
<code>sentry.lcd.injective.network</code> (keyless), prices normalised by 1e6, depth sampled from the
touch. 24h volume is a third-party CoinGecko figure for the same venue. Single-snapshot view —
spreads move, and an empty book at one moment does not prove a market is dead all day.<br><br>
<a href="../index.html" style="color:var(--acc)">← all 286 markets</a>
</div>
</div></body></html>"""
    p = outdir / "scorecards" / f"{slug(row['ticker'])}.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(page, encoding="utf-8")
    return p


# ---------------------------------------------------------------------------
# HTML: dashboard
# ---------------------------------------------------------------------------
def render_index(snap: dict, focus: list[str], outdir: Path) -> Path:
    s = snap["summary"]
    rows = snap["markets"]
    rows_json = json.dumps(rows, separators=(",", ":"))
    focus_cards = ""
    by = {r["ticker"]: r for r in rows}
    for t in focus:
        r = by.get(t)
        if not r:
            continue
        cls = "g" + r["grade"]
        focus_cards += f"""
      <a class="card" href="scorecards/{slug(t)}.html">
        <div class="card-top"><span class="tk">{esc(t)}</span><span class="pill {cls}">{r['score']:.0f} · {esc(r['grade'])}</span></div>
        <div class="card-metrics">
          <div><span>spread</span><b>{bps(r.get('spread_bps'))} bps</b></div>
          <div><span>depth ≤25</span><b>{usd((r.get('depth_usd') or {}).get('25'))}</b></div>
          <div><span>24h vol</span><b>{usd(r.get('volume_24h_usd'))}</b></div>
        </div>
        <div class="card-flag">{'no two-sided quote' if not r.get('two_sided') else ('wide' if (r.get('spread_bps') or 0) > 100 else 'quoted')}</div>
      </a>"""

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Injective Market Desk — liquidity truth for 286 perp markets</title>
<style>
:root{{--bg:#0b0d10;--panel:#14181d;--panel2:#171c22;--line:#232a33;--fg:#e8edf3;--dim:#8b98a8;--acc:#37d39b;--warn:#f2b13c;--bad:#ef5f6b;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--serif:Georgia,'Times New Roman',serif}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}}
.wrap{{max-width:1240px;margin:0 auto;padding:34px 22px 70px}}
.kicker{{font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}}
h1{{font:700 32px/1.12 var(--serif);margin:10px 0 8px;letter-spacing:-.01em}}
.lede{{color:var(--dim);max-width:760px;margin:0 0 26px}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-bottom:14px}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px 16px}}
.stat .k{{font:600 10px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-bottom:8px}}
.stat .v{{font:700 26px/1 var(--mono)}}
.stat .n{{color:var(--dim);font-size:12px;margin-top:6px}}
h2{{font:700 12px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin:34px 0 14px;padding-bottom:9px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:baseline}}
h2 a{{color:var(--acc);text-decoration:none;font-size:11px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(232px,1fr));gap:10px}}
.card{{display:block;background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:13px 14px;text-decoration:none;color:inherit;transition:border-color .12s}}
.card:hover{{border-color:var(--acc)}}
.card-top{{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:10px}}
.tk{{font:600 13px/1.2 var(--mono)}}
.pill{{font:700 10px/1 var(--mono);padding:4px 6px;border-radius:3px;color:#0b0d10;background:var(--dim);white-space:nowrap}}
.pill.gA{{background:var(--acc)}}.pill.gB{{background:#7fd8b4}}.pill.gC{{background:var(--warn)}}.pill.gD{{background:#e08b56}}.pill.gE{{background:var(--bad)}}.pill.gF{{background:#b93d4c;color:#fff}}
.card-metrics{{display:grid;gap:3px;font-size:12.5px}}
.card-metrics div{{display:flex;justify-content:space-between}}
.card-metrics span{{color:var(--dim)}}
.card-metrics b{{font-family:var(--mono);font-weight:600}}
.card-flag{{margin-top:9px;font:600 10px/1 var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--bad)}}
.tools{{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 12px}}
input,select{{background:var(--panel);border:1px solid var(--line);color:var(--fg);padding:8px 10px;border-radius:5px;font:13px var(--mono)}}
input{{flex:1;min-width:200px}}
.tblwrap{{overflow-x:auto;border:1px solid var(--line);border-radius:6px}}
table{{width:100%;border-collapse:collapse;font-size:13px;min-width:940px}}
th,td{{padding:8px 11px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}}
th{{background:var(--panel2);font:600 10.5px/1 var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--dim);cursor:pointer;position:sticky;top:0}}
th:hover{{color:var(--fg)}}
td.num{{text-align:right;font-family:var(--mono)}}
tr:hover td{{background:#11161b}}
.badge{{display:inline-block;font:700 10px/1 var(--mono);padding:3px 5px;border-radius:3px;color:#0b0d10}}
.bA{{background:var(--acc)}}.bB{{background:#7fd8b4}}.bC{{background:var(--warn)}}.bD{{background:#e08b56}}.bE{{background:var(--bad)}}.bF{{background:#b93d4c;color:#fff}}
.empty{{color:var(--bad);font-weight:600}}
.method{{color:var(--dim);font-size:13px;max-width:900px}}
.method code{{color:var(--fg);background:var(--panel);padding:1px 5px;border-radius:3px;font-size:12px}}
.method li{{margin:8px 0}}
.foot{{margin-top:36px;padding-top:14px;border-top:1px solid var(--line);color:var(--dim);font-size:12px}}
a{{color:var(--acc)}}
</style></head><body><div class="wrap">

<div class="kicker">Injective Market Desk · snapshot {esc(snap['generated_at'])}</div>
<h1>Liquidity truth for all {s['markets']} Injective perpetual markets</h1>
<p class="lede">Every market on Injective's on-chain order book, measured from the book itself — not from
volume charts. Depth is sampled from the touch, spread is the live touch, and an empty book is reported
as empty. Refreshed hourly; this page is a static snapshot with the data baked in.</p>

<div class="stats">
  <div class="stat"><div class="k">Markets measured</div><div class="v">{s['markets']}</div><div class="n">{s['two_sided']} with a two-sided quote</div></div>
  <div class="stat"><div class="k">No two-sided quote</div><div class="v" style="color:var(--bad)">{s['empty_or_one_sided']}</div><div class="n">{pct(s['empty_pct'])} of all markets</div></div>
  <div class="stat"><div class="k">Median spread</div><div class="v">{bps(s['median_spread_bps'])}<span style="font-size:14px;color:var(--dim)"> bps</span></div><div class="n">p90 {bps(s['p90_spread_bps'])} bps</div></div>
  <div class="stat"><div class="k">Median depth ≤25 bps</div><div class="v">{usd(s['median_depth_usd_25'])}</div><div class="n">{usd(s['total_depth_usd_25'])} across all books</div></div>
  <div class="stat"><div class="k">Venue 24h volume</div><div class="v">{usd(s['total_volume_24h_usd'])}</div><div class="n">median market {usd(s['median_volume_24h_usd'])}</div></div>
  <div class="stat"><div class="k">Median health score</div><div class="v">{s['median_score']}<span style="font-size:14px;color:var(--dim)"> /100</span></div><div class="n">grades A–F, formula below</div></div>
</div>

<h2>Focus scorecards <a href="#all">jump to full table ↓</a></h2>
<div class="cards">{focus_cards}</div>

<h2 id="all">All markets <span id="count" style="color:var(--fg)"></span></h2>
<div class="tools">
  <input id="q" placeholder="filter ticker (e.g. BTC, MSFT, USDSEK)" autocomplete="off">
  <select id="f">
    <option value="all">all markets</option>
    <option value="empty">no two-sided quote only</option>
    <option value="quoted">quoted only</option>
    <option value="wide">spread &gt; 100 bps</option>
    <option value="vol">volume ≥ $50k but thin book</option>
  </select>
</div>
<div class="tblwrap">
<table id="t">
<thead><tr>
  <th data-k="ticker">Market</th>
  <th data-k="score" class="num">Score</th>
  <th data-k="grade">Grade</th>
  <th data-k="spread_bps" class="num">Spread (bps)</th>
  <th data-k="d25" class="num">Depth ≤25 bps</th>
  <th data-k="d100" class="num">Depth ≤100 bps</th>
  <th data-k="hhi" class="num">HHI</th>
  <th data-k="volume_24h_usd" class="num">24h volume</th>
  <th data-k="roundtrip_bps" class="num">Round trip (bps)</th>
  <th data-k="oracle_type">Oracle</th>
</tr></thead>
<tbody id="tb"></tbody>
</table>
</div>

<h2>Method — so you can argue with it</h2>
<div class="method">
<ul>
<li><b>Source.</b> Order books and market metadata: Injective public LCD, <code>sentry.lcd.injective.network</code>, keyless, no rate-limit account. 24h volume: CoinGecko's <code>injective_futures</code> tickers (third-party, refreshed every 30 min).</li>
<li><b>Price normalisation.</b> Derivative book prices are chain-scaled by 1e6; verified against spot at snapshot time (BTC mid 81,291 vs spot 81,262).</li>
<li><b>Depth.</b> Notional resting within X bps of the <i>touch</i> (best bid / best ask), taking the thinner side — the side a taker can actually use. Measuring from mid would score a 60 bps-wide market as zero-depth, which is misleading.</li>
<li><b>Spread.</b> <code>(ask − bid) / mid × 10,000</code>, live touch only. Round trip = spread + 2 × taker fee from market metadata.</li>
<li><b>Health score</b> (0–100), weighted: two-sided quote 25 · spread 25 · depth ≤25 bps 25 · 24h volume 15 · book balance 10. Sub-scores are linear/log maps with published breakpoints: spread 2 bps→1.0, 200 bps→0; depth $1k→0, $1M→1.0; volume $10k→0, $1M→1.0. Weights renormalise when an input is missing.</li>
<li><b>Known gaps.</b> No funding rate, open interest, maker identity, or historical series yet — those need the indexer's gRPC-web surface, which is Phase 1. One snapshot; spreads move.</li>
</ul>
</div>

<div class="foot">
Built from public chain state. Not investment advice; grades describe book microstructure at one moment,
not the creditworthiness of any issuer. <a href="https://github.com/nwfella/inj-market-desk">source</a>
</div>
</div>
<script>
const SNAP = {rows_json};
const FOCUS = {json.dumps(focus)};
const fmtUSD = v => v==null ? '—' : (Math.abs(v)>=1e6 ? '$'+(v/1e6).toFixed(2)+'M' : Math.abs(v)>=1e3 ? '$'+(v/1e3).toFixed(1)+'k' : '$'+Math.round(v));
const fmtB = v => v==null ? '—' : v.toFixed(1);
let sortK='score', sortD=1, filter='all', q='';
function rowMatches(r){{
  if(q && !r.ticker.toLowerCase().includes(q)) return false;
  if(filter==='empty') return !r.two_sided;
  if(filter==='quoted') return !!r.two_sided;
  if(filter==='wide') return (r.spread_bps||0)>100;
  if(filter==='vol') return (r.volume_24h_usd||0)>=50000 && ((r.depth_usd||{{}})['25']||0)<5000;
  return true;
}}
function val(r,k){{
  if(k==='d25') return (r.depth_usd||{{}})['25']||0;
  if(k==='d100') return (r.depth_usd||{{}})['100']||0;
  if(k==='hhi') return r.depth_hhi==null?-1:r.depth_hhi;
  if(k==='grade') return r.grade;
  const v=r[k];
  return v==null?(k==='score'?-1:-1):v;
}}
function draw(){{
  const el=document.getElementById('tb');
  const rows=SNAP.filter(rowMatches).sort((a,b)=>{{
    const x=val(a,sortK), y=val(b,sortK);
    if(typeof x==='string') return sortD*x.localeCompare(y);
    return sortD*(x-y);
  }});
  el.innerHTML = rows.map(r=>{{
    const sp = r.spread_bps==null ? '<span class="empty">no book</span>' : fmtB(r.spread_bps);
    return '<tr>'+
      '<td><a href="scorecards/'+r.ticker.toLowerCase().replace(/[\\/ ]/g,c=>c==='/'?'-':'-')+'.html" style="color:inherit;text-decoration:none;border-bottom:1px dotted #3a4652">'+r.ticker+'</a></td>'+
      '<td class="num">'+r.score.toFixed(1)+'</td>'+
      '<td><span class="badge b'+r.grade+'">'+r.grade+'</span></td>'+
      '<td class="num">'+sp+'</td>'+
      '<td class="num">'+fmtUSD((r.depth_usd||{{}})['25'])+'</td>'+
      '<td class="num">'+fmtUSD((r.depth_usd||{{}})['100'])+'</td>'+
      '<td class="num">'+(r.depth_hhi==null?'—':r.depth_hhi.toFixed(2))+'</td>'+
      '<td class="num">'+fmtUSD(r.volume_24h_usd)+'</td>'+
      '<td class="num">'+(r.roundtrip_bps==null?'—':fmtB(r.roundtrip_bps))+'</td>'+
      '<td style="color:#8b98a8">'+(r.oracle_type||'—')+'</td>'+
    '</tr>';
  }}).join('');
  document.getElementById('count').textContent = rows.length+' of '+SNAP.length+' shown';
}}
document.querySelectorAll('th[data-k]').forEach(th=>th.addEventListener('click',()=>{{
  const k=th.dataset.k;
  if(sortK===k) sortD*=-1; else {{sortK=k; sortD=(k==='score'||k==='spread_bps')?1:-1;}}
  draw();
}}));
document.getElementById('q').addEventListener('input',e=>{{q=e.target.value.trim().toLowerCase();draw();}});
document.getElementById('f').addEventListener('change',e=>{{filter=e.target.value;draw();}});
draw();
</script>
</body></html>"""
    out = outdir / "index.html"
    out.write_text(page, encoding="utf-8")
    return out


# ---------------------------------------------------------------------------
# outreach asset
# ---------------------------------------------------------------------------
def render_outreach(snap: dict, focus: list[str], outdir: Path) -> Path:
    by = {r["ticker"]: r for r in snap["markets"]}
    s = snap["summary"]
    rows = []
    for t in focus:
        r = by.get(t)
        if not r or t in CONTROLS:
            continue
        rows.append(
            f"| `{t}` | {r['score']:.0f} {r['grade']} | {bps(r.get('spread_bps'))} | "
            f"{usd((r.get('depth_usd') or {}).get('25'))} | {usd(r.get('volume_24h_usd'))} | "
            f"[scorecard](docs/scorecards/{slug(t)}.html) |"
        )
    table = "\n".join(rows)
    ph = []
    for t in focus:
        r = by.get(t)
        if not r:
            continue
        ph.append(
            f"{t}: score={r['score']:.1f}{r['grade']} spread={bps(r.get('spread_bps'))} "
            f"depth25={usd((r.get('depth_usd') or {}).get('25'))} vol24h={usd(r.get('volume_24h_usd'))} "
            f"url=<site>/scorecards/{slug(t)}.html"
        )
    ph.append(f"BTC benchmark: spread={bps(by.get('BTC/USDC PERP',{}).get('spread_bps'))} "
              f"depth25={usd((by.get('BTC/USDC PERP',{}).get('depth_usd') or {}).get('25'))}")
    placeholders = "\n".join(ph)
    head = f"""# Outreach — Phase 0

Generated {snap['generated_at']} from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **{s['empty_or_one_sided']} of {s['markets']} Injective perp markets ({pct(s['empty_pct'])})** had no two-sided quote at snapshot time.
- The median quoted market is **{bps(s['median_spread_bps'])} bps wide** (BTC: {bps(by.get('BTC/USDC PERP',{}).get('spread_bps'))} bps).
- **Median two-sided depth inside 25 bps: {usd(s['median_depth_usd_25'])}.** The whole venue holds {usd(s['total_depth_usd_25'])} within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
{table}

## How to find who to email

The launch message is public. For a given market id, the launcher is the sender of
`MsgInstantPerpetualMarketLaunch` (or `MsgInstantExpiryFuturesMarketLaunch`). Two ways to resolve it:

1. Explorer: search the market id on `explorer.injective.network` -> market page -> "created by".
2. Indexer: `/api/explorer/v1/derivatives/markets/{{market_id}}` returns the market; the creating tx is in
   the exchange module events of the launch block.

Then match the address against Injective BD (they know who launched what) or the project's own
announcement. Never cold-email a generic support inbox; the scorecard is only persuasive to whoever
owns the market's liquidity.

## Fill-in values

```
{placeholders}
```

"""
    template = """## Email A — launch desk (markets with a book but broken microstructure)

Subject: {market} is quoting {spread} bps wide — one-page diagnosis attached

> Hi {first},
>
> I measured every perp market on Injective from the order book this morning — 286 of them.
> {market} came out at {score}/100: {spread} bps wide with {depth} of two-sided size inside 25 bps,
> against {volume} of 24h volume. BTC reads {btc_spread} bps and {btc_depth} in the same band.
>
> Attached is the one-pager (also here: {scorecard_url}). It lists the three specific fixes in order of
> impact — the first one is usually a maker incentive, not more marketing.
>
> If it is useful I can re-run it hourly and send you the series so you can see whether the fix landed.
> That is $750 for the audit plus the first month of monitoring, and the free version costs nothing.
>
> — {name}

## Email B — RWA / institutional integrity (markets with volume but no book)

Subject: {market} shows {volume} of 24h volume against {depth} of resting depth

> Hi {first},
>
> Injective now carries tokenized equities, FX and 130+ RWA perp markets. I publish a monthly integrity
> read on them: depth inside 25 bps, spread, book concentration (HHI), oracle source per market, and
> volume-to-depth gaps.
>
> This month {market} is the clearest example: {volume} of 24h volume, {depth} of two-sided depth and
> {spread} bps of spread. That combination is worth understanding before anyone quotes it to a client.
>
> The free page is here: {site_url}. The paid tier is the per-market series plus the underlying JSON
> ({price}/mo), and bespoke diligence reports are {bespoke}.
>
> — {name}

## Rules

- Send 8 emails, not 80. Track replies in a sheet; the Phase 0 gate is **2 replies**.
- Attach the scorecard HTML (it prints to a clean one-page PDF from the browser).
- Never claim manipulation. State what the book shows, with the timestamp, and let the reader conclude.
- Re-snapshot before every send — a stale spread in an email about freshness kills the pitch.
"""
    body = head + template
    p = outdir / "OUTREACH.md"
    p.write_text(body, encoding="utf-8")
    return p


# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="docs")
    ap.add_argument("--data", default=str(DATA / "latest.json"))
    a = ap.parse_args()

    snap = json.loads(Path(a.data).read_text())
    outdir = ROOT / a.out
    outdir.mkdir(parents=True, exist_ok=True)

    focus = pick_focus(snap)
    by = {r["ticker"]: r for r in snap["markets"]}
    # a previous run's focus list leaves orphan scorecards behind
    sc = outdir / "scorecards"
    if sc.exists():
        for f in sc.glob("*.html"):
            f.unlink()
    btc = by.get("BTC/USDC PERP") or {"spread_bps": 0, "depth_usd": {"25": 0}, "score": 0}

    for t in focus:
        if t in by:
            render_scorecard(by[t], btc, snap, outdir)
    idx = render_index(snap, focus, outdir)
    out = render_outreach(snap, focus, outdir)
    print(f"wrote {idx.relative_to(ROOT)} + {len(focus)} scorecards + {out.relative_to(ROOT)}")
    print("focus:", ", ".join(focus))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
