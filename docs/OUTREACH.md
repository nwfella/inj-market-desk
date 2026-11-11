# Outreach — Phase 0

Generated 2026-11-11T06:21:20Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **250 of 308 Injective perp markets (81.2%)** had no two-sided quote at snapshot time.
- The median quoted market is **58.5 bps wide** (BTC: 7.6 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.20M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $561.0k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 20 F | — | $0 | $512.4k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `MA/USDC PERP` | 18 F | — | $0 | $403.7k | [scorecard](docs/scorecards/ma-usdc-perp.html) |
| `WLD/USDC PERP` | 40 D | 138.3 | $9 | $75.8k | [scorecard](docs/scorecards/wld-usdc-perp.html) |
| `NIGHT/USDC PERP` | 43 D | 120.7 | $100 | $72.0k | [scorecard](docs/scorecards/night-usdc-perp.html) |
| `CRDO/USDC PERP` | 43 D | 739.4 | $10 | $124.9k | [scorecard](docs/scorecards/crdo-usdc-perp.html) |
| `SNDK/USDC PERP` | 45 D | 19,999.6 | $9 | $260.8k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |

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
BTC/USDC PERP: score=94.9A spread=7.6 depth25=$302.8k vol24h=$7.10M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=94.8A spread=5.8 depth25=$272.9k vol24h=$5.68M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=87.1A spread=37.8 depth25=$100.2k vol24h=$3.40M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.2E spread=— depth25=$0 vol24h=$561.0k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=19.7F spread=— depth25=$0 vol24h=$512.4k url=<site>/scorecards/sici-usdc-perp.html
MA/USDC PERP: score=18.5F spread=— depth25=$0 vol24h=$403.7k url=<site>/scorecards/ma-usdc-perp.html
WLD/USDC PERP: score=39.6D spread=138.3 depth25=$9 vol24h=$75.8k url=<site>/scorecards/wld-usdc-perp.html
NIGHT/USDC PERP: score=43.1D spread=120.7 depth25=$100 vol24h=$72.0k url=<site>/scorecards/night-usdc-perp.html
CRDO/USDC PERP: score=43.2D spread=739.4 depth25=$10 vol24h=$124.9k url=<site>/scorecards/crdo-usdc-perp.html
SNDK/USDC PERP: score=45.2D spread=19,999.6 depth25=$9 vol24h=$260.8k url=<site>/scorecards/sndk-usdc-perp.html
BTC benchmark: spread=7.6 depth25=$302.8k
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
