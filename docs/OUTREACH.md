# Outreach — Phase 0

Generated 2026-11-04T01:22:06Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **230 of 312 Injective perp markets (73.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **77.3 bps wide** (BTC: 7.9 bps).
- **Median two-sided depth inside 25 bps: $153.** The whole venue holds $1.27M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDNOK/USDC PERP` | 20 E | — | $0 | $582.9k | [scorecard](docs/scorecards/usdnok-usdc-perp.html) |
| `SICI/USDC PERP` | 20 F | — | $0 | $508.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USTECH/USDC PERP` | 15 F | — | $0 | $194.3k | [scorecard](docs/scorecards/ustech-usdc-perp.html) |
| `AERO/USDC PERP` | 32 E | 231.3 | $6 | $86.2k | [scorecard](docs/scorecards/aero-usdc-perp.html) |
| `SNDK/USDC PERP` | 32 E | 19,999.6 | $10 | $91.6k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `XAUT/USDC PERP` | 33 E | 182.3 | $5 | $53.4k | [scorecard](docs/scorecards/xaut-usdc-perp.html) |
| `ARM/USDC PERP` | 35 E | 181.5 | $5 | $90.5k | [scorecard](docs/scorecards/arm-usdc-perp.html) |

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
BTC/USDC PERP: score=89.5A spread=7.9 depth25=$321.1k vol24h=$7.60M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=89.4A spread=12.4 depth25=$338.8k vol24h=$5.46M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.1A spread=22.4 depth25=$99.9k vol24h=$3.52M url=<site>/scorecards/inj-usdc-perp.html
USDNOK/USDC PERP: score=20.4E spread=— depth25=$0 vol24h=$582.9k url=<site>/scorecards/usdnok-usdc-perp.html
SICI/USDC PERP: score=19.7F spread=— depth25=$0 vol24h=$508.5k url=<site>/scorecards/sici-usdc-perp.html
USTECH/USDC PERP: score=14.9F spread=— depth25=$0 vol24h=$194.3k url=<site>/scorecards/ustech-usdc-perp.html
AERO/USDC PERP: score=32.1E spread=231.3 depth25=$6 vol24h=$86.2k url=<site>/scorecards/aero-usdc-perp.html
SNDK/USDC PERP: score=32.4E spread=19,999.6 depth25=$10 vol24h=$91.6k url=<site>/scorecards/sndk-usdc-perp.html
XAUT/USDC PERP: score=32.8E spread=182.3 depth25=$5 vol24h=$53.4k url=<site>/scorecards/xaut-usdc-perp.html
ARM/USDC PERP: score=34.6E spread=181.5 depth25=$5 vol24h=$90.5k url=<site>/scorecards/arm-usdc-perp.html
BTC benchmark: spread=7.9 depth25=$321.1k
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
