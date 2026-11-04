# Outreach — Phase 0

Generated 2026-11-04T09:13:21Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **228 of 312 Injective perp markets (73.1%)** had no two-sided quote at snapshot time.
- The median quoted market is **76.6 bps wide** (BTC: 6.4 bps).
- **Median two-sided depth inside 25 bps: $220.** The whole venue holds $1.22M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDNOK/USDC PERP` | 20 E | — | $0 | $582.9k | [scorecard](docs/scorecards/usdnok-usdc-perp.html) |
| `SICI/USDC PERP` | 16 F | — | $0 | $229.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USTECH/USDC PERP` | 15 F | — | $0 | $194.3k | [scorecard](docs/scorecards/ustech-usdc-perp.html) |
| `INTC/USDC PERP` | 31 E | 19,993.3 | $10 | $63.0k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `ETHFI/USDC PERP` | 32 E | 199.8 | $5 | $75.0k | [scorecard](docs/scorecards/ethfi-usdc-perp.html) |
| `SNDK/USDC PERP` | 33 E | 19,999.7 | $10 | $98.2k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `ARM/USDC PERP` | 39 D | 150.6 | $5 | $93.3k | [scorecard](docs/scorecards/arm-usdc-perp.html) |

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
BTC/USDC PERP: score=85.0A spread=6.4 depth25=$299.1k vol24h=$50.3k url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=84.1A spread=7.3 depth25=$325.3k vol24h=$179.8k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=83.8A spread=15.7 depth25=$100.0k vol24h=$153.1k url=<site>/scorecards/inj-usdc-perp.html
USDNOK/USDC PERP: score=20.4E spread=— depth25=$0 vol24h=$582.9k url=<site>/scorecards/usdnok-usdc-perp.html
SICI/USDC PERP: score=15.7F spread=— depth25=$0 vol24h=$229.9k url=<site>/scorecards/sici-usdc-perp.html
USTECH/USDC PERP: score=14.9F spread=— depth25=$0 vol24h=$194.3k url=<site>/scorecards/ustech-usdc-perp.html
INTC/USDC PERP: score=31.3E spread=19,993.3 depth25=$10 vol24h=$63.0k url=<site>/scorecards/intc-usdc-perp.html
ETHFI/USDC PERP: score=31.7E spread=199.8 depth25=$5 vol24h=$75.0k url=<site>/scorecards/ethfi-usdc-perp.html
SNDK/USDC PERP: score=32.7E spread=19,999.7 depth25=$10 vol24h=$98.2k url=<site>/scorecards/sndk-usdc-perp.html
ARM/USDC PERP: score=38.6D spread=150.6 depth25=$5 vol24h=$93.3k url=<site>/scorecards/arm-usdc-perp.html
BTC benchmark: spread=6.4 depth25=$299.1k
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
