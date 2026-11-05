# Outreach — Phase 0

Generated 2026-11-05T20:40:44Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **279 of 341 Injective perp markets (81.8%)** had no two-sided quote at snapshot time.
- The median quoted market is **98.2 bps wide** (BTC: 3.8 bps).
- **Median two-sided depth inside 25 bps: $635.** The whole venue holds $1.32M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `DELL/USDC PERP` | 20 F | — | $0 | $532.2k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `RUNE/USDC PERP` | 19 F | — | $0 | $478.1k | [scorecard](docs/scorecards/rune-usdc-perp.html) |
| `SNDK/USDC PERP` | 19 F | — | $0 | $460.5k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `MU/USDC PERP` | 36 D | 19,999.4 | $10 | $282.4k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `INTC/USDC PERP` | 38 D | 19,992.6 | $10 | $470.5k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `XAG/USDC PERP` | 39 D | 19,999.2 | $100 | $479.3k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `IBM/USDC PERP` | 41 D | 739.7 | $10 | $63.9k | [scorecard](docs/scorecards/ibm-usdc-perp.html) |

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
BTC/USDC PERP: score=95.5A spread=3.8 depth25=$312.9k vol24h=$7.59M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=91.1A spread=9.8 depth25=$205.0k vol24h=$5.74M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=85.4A spread=36.6 depth25=$80.2k vol24h=$4.18M url=<site>/scorecards/inj-usdc-perp.html
DELL/USDC PERP: score=19.9F spread=— depth25=$0 vol24h=$532.2k url=<site>/scorecards/dell-usdc-perp.html
RUNE/USDC PERP: score=19.4F spread=— depth25=$0 vol24h=$478.1k url=<site>/scorecards/rune-usdc-perp.html
SNDK/USDC PERP: score=19.2F spread=— depth25=$0 vol24h=$460.5k url=<site>/scorecards/sndk-usdc-perp.html
MU/USDC PERP: score=36.1D spread=19,999.4 depth25=$10 vol24h=$282.4k url=<site>/scorecards/mu-usdc-perp.html
INTC/USDC PERP: score=37.9D spread=19,992.6 depth25=$10 vol24h=$470.5k url=<site>/scorecards/intc-usdc-perp.html
XAG/USDC PERP: score=39.4D spread=19,999.2 depth25=$100 vol24h=$479.3k url=<site>/scorecards/xag-usdc-perp.html
IBM/USDC PERP: score=41.0D spread=739.7 depth25=$10 vol24h=$63.9k url=<site>/scorecards/ibm-usdc-perp.html
BTC benchmark: spread=3.8 depth25=$312.9k
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
