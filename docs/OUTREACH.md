# Outreach — Phase 0

Generated 2026-11-07T16:27:05Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **300 of 354 Injective perp markets (84.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **61.2 bps wide** (BTC: 2.1 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.22M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 F | — | $0 | $504.4k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $398.4k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `USDSEK/USDC PERP` | 18 F | — | $0 | $373.6k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `XAG/USDC PERP` | 33 E | 423.8 | $10 | $114.7k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `INTC/USDC PERP` | 39 D | 19,993.1 | $1 | $326.8k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `MU/USDC PERP` | 39 D | 19,999.4 | $1 | $374.7k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `NVDA/USDC PERP` | 47 D | 86.0 | $1.5k | $63.1k | [scorecard](docs/scorecards/nvda-usdc-perp.html) |

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
BTC/USDC PERP: score=96.1A spread=2.1 depth25=$345.7k vol24h=$7.37M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=92.7A spread=0.89 depth25=$225.9k vol24h=$5.25M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=88.6A spread=25.8 depth25=$99.9k vol24h=$3.37M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=19.6F spread=— depth25=$0 vol24h=$504.4k url=<site>/scorecards/sici-usdc-perp.html
US500/USDC PERP: score=18.5F spread=— depth25=$0 vol24h=$398.4k url=<site>/scorecards/us500-usdc-perp.html
USDSEK/USDC PERP: score=18.1F spread=— depth25=$0 vol24h=$373.6k url=<site>/scorecards/usdsek-usdc-perp.html
XAG/USDC PERP: score=33.2E spread=423.8 depth25=$10 vol24h=$114.7k url=<site>/scorecards/xag-usdc-perp.html
INTC/USDC PERP: score=38.8D spread=19,993.1 depth25=$1 vol24h=$326.8k url=<site>/scorecards/intc-usdc-perp.html
MU/USDC PERP: score=39.3D spread=19,999.4 depth25=$1 vol24h=$374.7k url=<site>/scorecards/mu-usdc-perp.html
NVDA/USDC PERP: score=47.4D spread=86.0 depth25=$1.5k vol24h=$63.1k url=<site>/scorecards/nvda-usdc-perp.html
BTC benchmark: spread=2.1 depth25=$345.7k
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
