# Outreach — Phase 0

Generated 2026-10-30T01:00:29Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **198 of 286 Injective perp markets (69.2%)** had no two-sided quote at snapshot time.
- The median quoted market is **67.5 bps wide** (BTC: 3.6 bps).
- **Median two-sided depth inside 25 bps: $52.** The whole venue holds $612.9k within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 19 F | — | $0 | $484.8k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `HBAR/USDC PERP` | 16 F | — | $0 | $266.4k | [scorecard](docs/scorecards/hbar-usdc-perp.html) |
| `TRX/USDC PERP` | 14 F | — | $0 | $176.6k | [scorecard](docs/scorecards/trx-usdc-perp.html) |
| `RKLB/USDC PERP` | 31 E | 278.2 | $1 | $61.2k | [scorecard](docs/scorecards/rklb-usdc-perp.html) |
| `SNDK/USDC PERP` | 32 E | 19,999.7 | $10 | $81.2k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `GBPUSD/USDC PERP` | 32 E | 19,999.7 | $100 | $60.7k | [scorecard](docs/scorecards/gbpusd-usdc-perp.html) |
| `MU/USDC PERP` | 33 E | 740.0 | $11 | $123.4k | [scorecard](docs/scorecards/mu-usdc-perp.html) |

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
BTC/USDC PERP: score=82.7A spread=3.6 depth25=$20.6k vol24h=$17.47M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=91.5A spread=6.3 depth25=$111.0k vol24h=$12.92M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=64.0C spread=9.8 depth25=$168 vol24h=$7.52M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.4F spread=— depth25=$0 vol24h=$484.8k url=<site>/scorecards/usdhkd-usdc-perp.html
HBAR/USDC PERP: score=16.4F spread=— depth25=$0 vol24h=$266.4k url=<site>/scorecards/hbar-usdc-perp.html
TRX/USDC PERP: score=14.4F spread=— depth25=$0 vol24h=$176.6k url=<site>/scorecards/trx-usdc-perp.html
RKLB/USDC PERP: score=30.9E spread=278.2 depth25=$1 vol24h=$61.2k url=<site>/scorecards/rklb-usdc-perp.html
SNDK/USDC PERP: score=31.9E spread=19,999.7 depth25=$10 vol24h=$81.2k url=<site>/scorecards/sndk-usdc-perp.html
GBPUSD/USDC PERP: score=32.1E spread=19,999.7 depth25=$100 vol24h=$60.7k url=<site>/scorecards/gbpusd-usdc-perp.html
MU/USDC PERP: score=33.3E spread=740.0 depth25=$11 vol24h=$123.4k url=<site>/scorecards/mu-usdc-perp.html
BTC benchmark: spread=3.6 depth25=$20.6k
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
