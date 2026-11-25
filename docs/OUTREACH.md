# Outreach — Phase 0

Generated 2026-11-25T12:55:56Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **259 of 307 Injective perp markets (84.4%)** had no two-sided quote at snapshot time.
- The median quoted market is **55.4 bps wide** (BTC: 7.3 bps).
- **Median two-sided depth inside 25 bps: $13.0k.** The whole venue holds $1.34M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 23 E | — | $0 | $1.06M | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDSEK/USDC PERP` | 19 F | — | $0 | $482.3k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `EURUSD/USDC PERP` | 34 E | 19,999.6 | $100 | $64.8k | [scorecard](docs/scorecards/eurusd-usdc-perp.html) |
| `XAG/USDC PERP` | 36 D | 19,999.0 | $18 | $129.7k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `ZK/USDC PERP` | 38 D | 500.3 | $10 | $58.4k | [scorecard](docs/scorecards/zk-usdc-perp.html) |
| `TAIKO/USDC PERP` | 39 D | 371.3 | $10 | $79.2k | [scorecard](docs/scorecards/taiko-usdc-perp.html) |

## How to find who to email

The launch message is public. For a given market id, the launcher is the sender of
`MsgInstantPerpetualMarketLaunch` (or `MsgInstantExpiryFuturesMarketLaunch`). Two ways to resolve it:

1. Explorer: search the market id on `explorer.injective.network` -> market page -> "created by".
2. Indexer: `/api/explorer/v1/derivatives/markets/{market_id}` returns the market; the creating tx is in
   the exchange module events of the launch block.

Then match the address against Injective BD (they know who launched what) or the project's own
announcement. Never cold-email a generic support inbox; the scorecard is only persuasive to whoever
owns the market's liquidity.

## Fill-in values

```
BTC/USDC PERP: score=94.8A spread=7.3 depth25=$309.6k vol24h=$10.25M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=94.8A spread=10.9 depth25=$327.6k vol24h=$3.43M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=63.9C spread=10.6 depth25=$0 vol24h=$2.86M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=23.1E spread=— depth25=$0 vol24h=$1.06M url=<site>/scorecards/sici-usdc-perp.html
USDSEK/USDC PERP: score=19.4F spread=— depth25=$0 vol24h=$482.3k url=<site>/scorecards/usdsek-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
EURUSD/USDC PERP: score=34.4E spread=19,999.6 depth25=$100 vol24h=$64.8k url=<site>/scorecards/eurusd-usdc-perp.html
XAG/USDC PERP: score=36.4D spread=19,999.0 depth25=$18 vol24h=$129.7k url=<site>/scorecards/xag-usdc-perp.html
ZK/USDC PERP: score=37.9D spread=500.3 depth25=$10 vol24h=$58.4k url=<site>/scorecards/zk-usdc-perp.html
TAIKO/USDC PERP: score=38.9D spread=371.3 depth25=$10 vol24h=$79.2k url=<site>/scorecards/taiko-usdc-perp.html
BTC benchmark: spread=7.3 depth25=$309.6k
```

## Email A — launch desk (markets with a book but broken microstructure)

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
