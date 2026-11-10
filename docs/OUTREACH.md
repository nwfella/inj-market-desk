# Outreach — Phase 0

Generated 2026-11-10T09:50:43Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **232 of 298 Injective perp markets (77.9%)** had no two-sided quote at snapshot time.
- The median quoted market is **59.1 bps wide** (BTC: 7.1 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.16M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $572.8k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `SKY/USDC PERP` | 19 F | — | $0 | $425.9k | [scorecard](docs/scorecards/sky-usdc-perp.html) |
| `US500/USDC PERP` | 19 F | — | $0 | $419.0k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `WLFI/USDC PERP` | 42 D | 112.8 | $5 | $53.0k | [scorecard](docs/scorecards/wlfi-usdc-perp.html) |
| `CRDO/USDC PERP` | 47 D | 149.5 | $5 | $62.5k | [scorecard](docs/scorecards/crdo-usdc-perp.html) |
| `ATOM/USDC PERP` | 59 C | 43.1 | $4.1k | $55.1k | [scorecard](docs/scorecards/atom-usdc-perp.html) |
| `HYPE/USDC PERP` | 72 B | 26.9 | $18.9k | $51.8k | [scorecard](docs/scorecards/hype-usdc-perp.html) |

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
BTC/USDC PERP: score=94.9A spread=7.1 depth25=$302.8k vol24h=$11.37M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=94.5A spread=8.6 depth25=$271.8k vol24h=$5.48M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.8A spread=28.9 depth25=$100.2k vol24h=$6.14M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.3E spread=— depth25=$0 vol24h=$572.8k url=<site>/scorecards/sici-usdc-perp.html
SKY/USDC PERP: score=18.8F spread=— depth25=$0 vol24h=$425.9k url=<site>/scorecards/sky-usdc-perp.html
US500/USDC PERP: score=18.7F spread=— depth25=$0 vol24h=$419.0k url=<site>/scorecards/us500-usdc-perp.html
WLFI/USDC PERP: score=41.6D spread=112.8 depth25=$5 vol24h=$53.0k url=<site>/scorecards/wlfi-usdc-perp.html
CRDO/USDC PERP: score=47.3D spread=149.5 depth25=$5 vol24h=$62.5k url=<site>/scorecards/crdo-usdc-perp.html
ATOM/USDC PERP: score=58.8C spread=43.1 depth25=$4.1k vol24h=$55.1k url=<site>/scorecards/atom-usdc-perp.html
HYPE/USDC PERP: score=71.9B spread=26.9 depth25=$18.9k vol24h=$51.8k url=<site>/scorecards/hype-usdc-perp.html
BTC benchmark: spread=7.1 depth25=$302.8k
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
