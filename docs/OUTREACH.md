# Outreach — Phase 0

Generated 2026-11-24T06:03:48Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **258 of 307 Injective perp markets (84.0%)** had no two-sided quote at snapshot time.
- The median quoted market is **56.2 bps wide** (BTC: 7.8 bps).
- **Median two-sided depth inside 25 bps: $5.0k.** The whole venue holds $1.22M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 19 F | — | $0 | $482.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `NEAR/USDC PERP` | 16 F | — | $0 | $265.1k | [scorecard](docs/scorecards/near-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $250.0k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `INTC/USDC PERP` | 34 E | 19,993.1 | $10 | $157.4k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `AAPL/USDC PERP` | 52 C | 40.8 | $1.1k | $64.6k | [scorecard](docs/scorecards/aapl-usdc-perp.html) |
| `TSLA/USDC PERP` | 55 C | 40.4 | $579 | $192.4k | [scorecard](docs/scorecards/tsla-usdc-perp.html) |
| `AAVE/USDC PERP` | 57 C | 28.7 | $100 | $259.1k | [scorecard](docs/scorecards/aave-usdc-perp.html) |

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
BTC/USDC PERP: score=94.0A spread=7.8 depth25=$310.9k vol24h=$816.4k url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.4A spread=8.8 depth25=$243.4k vol24h=$822.1k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.4A spread=38.1 depth25=$103.7k vol24h=$421.6k url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.4F spread=— depth25=$0 vol24h=$482.4k url=<site>/scorecards/usdsek-usdc-perp.html
NEAR/USDC PERP: score=16.4F spread=— depth25=$0 vol24h=$265.1k url=<site>/scorecards/near-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$250.0k url=<site>/scorecards/pep-usdc-perp.html
INTC/USDC PERP: score=34.2E spread=19,993.1 depth25=$10 vol24h=$157.4k url=<site>/scorecards/intc-usdc-perp.html
AAPL/USDC PERP: score=52.0C spread=40.8 depth25=$1.1k vol24h=$64.6k url=<site>/scorecards/aapl-usdc-perp.html
TSLA/USDC PERP: score=55.0C spread=40.4 depth25=$579 vol24h=$192.4k url=<site>/scorecards/tsla-usdc-perp.html
AAVE/USDC PERP: score=57.3C spread=28.7 depth25=$100 vol24h=$259.1k url=<site>/scorecards/aave-usdc-perp.html
BTC benchmark: spread=7.8 depth25=$310.9k
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
