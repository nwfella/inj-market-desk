# Outreach — Phase 0

Generated 2026-11-24T17:45:23Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **257 of 307 Injective perp markets (83.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **61.2 bps wide** (BTC: 54.0 bps).
- **Median two-sided depth inside 25 bps: $13.4k.** The whole venue holds $886.4k within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $540.1k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDSEK/USDC PERP` | 19 F | — | $0 | $482.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `NEAR/USDC PERP` | 19 F | — | $0 | $463.5k | [scorecard](docs/scorecards/near-usdc-perp.html) |
| `RAY/USDC PERP` | 32 E | 634.9 | $11 | $75.3k | [scorecard](docs/scorecards/ray-usdc-perp.html) |
| `INTC/USDC PERP` | 36 D | 19,992.8 | $10 | $277.3k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `XAG/USDC PERP` | 36 D | 19,999.0 | $18 | $133.2k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `CVX/USDC PERP` | 38 D | 1,029.7 | $10 | $69.1k | [scorecard](docs/scorecards/cvx-usdc-perp.html) |

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
BTC/USDC PERP: score=84.6A spread=54.0 depth25=$87.6k vol24h=$990.0k url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=87.0A spread=28.5 depth25=$100.8k vol24h=$659.7k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=70.6B spread=8.4 depth25=$10.6k vol24h=$70.1k url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$540.1k url=<site>/scorecards/sici-usdc-perp.html
USDSEK/USDC PERP: score=19.4F spread=— depth25=$0 vol24h=$482.4k url=<site>/scorecards/usdsek-usdc-perp.html
NEAR/USDC PERP: score=19.2F spread=— depth25=$0 vol24h=$463.5k url=<site>/scorecards/near-usdc-perp.html
RAY/USDC PERP: score=32.0E spread=634.9 depth25=$11 vol24h=$75.3k url=<site>/scorecards/ray-usdc-perp.html
INTC/USDC PERP: score=36.0D spread=19,992.8 depth25=$10 vol24h=$277.3k url=<site>/scorecards/intc-usdc-perp.html
XAG/USDC PERP: score=36.5D spread=19,999.0 depth25=$18 vol24h=$133.2k url=<site>/scorecards/xag-usdc-perp.html
CVX/USDC PERP: score=38.4D spread=1,029.7 depth25=$10 vol24h=$69.1k url=<site>/scorecards/cvx-usdc-perp.html
BTC benchmark: spread=54.0 depth25=$87.6k
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
