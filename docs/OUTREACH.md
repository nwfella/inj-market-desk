# Outreach — Phase 0

Generated 2026-11-10T01:32:01Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **231 of 298 Injective perp markets (77.5%)** had no two-sided quote at snapshot time.
- The median quoted market is **61.4 bps wide** (BTC: 4.3 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.08M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 F | — | $0 | $518.8k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `SKY/USDC PERP` | 19 F | — | $0 | $425.9k | [scorecard](docs/scorecards/sky-usdc-perp.html) |
| `US500/USDC PERP` | 19 F | — | $0 | $419.0k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `NIGHT/USDC PERP` | 49 D | 61.2 | $61 | $54.7k | [scorecard](docs/scorecards/night-usdc-perp.html) |
| `COST/USDC PERP` | 55 C | 63.6 | $5 | $60.0k | [scorecard](docs/scorecards/cost-usdc-perp.html) |
| `NVDA/USDC PERP` | 77 B | 52.1 | $47.0k | $157.9k | [scorecard](docs/scorecards/nvda-usdc-perp.html) |
| `SPX/USDC PERP` | 1 F | — | $0 | $12.4k | [scorecard](docs/scorecards/spx-usdc-perp.html) |

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
BTC/USDC PERP: score=95.9A spread=4.3 depth25=$351.1k vol24h=$8.22M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=86.9A spread=17.4 depth25=$172.5k vol24h=$5.72M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=75.3B spread=29.8 depth25=$20.6k vol24h=$3.45M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=19.8F spread=— depth25=$0 vol24h=$518.8k url=<site>/scorecards/sici-usdc-perp.html
SKY/USDC PERP: score=18.8F spread=— depth25=$0 vol24h=$425.9k url=<site>/scorecards/sky-usdc-perp.html
US500/USDC PERP: score=18.7F spread=— depth25=$0 vol24h=$419.0k url=<site>/scorecards/us500-usdc-perp.html
NIGHT/USDC PERP: score=49.2D spread=61.2 depth25=$61 vol24h=$54.7k url=<site>/scorecards/night-usdc-perp.html
COST/USDC PERP: score=54.7C spread=63.6 depth25=$5 vol24h=$60.0k url=<site>/scorecards/cost-usdc-perp.html
NVDA/USDC PERP: score=76.6B spread=52.1 depth25=$47.0k vol24h=$157.9k url=<site>/scorecards/nvda-usdc-perp.html
SPX/USDC PERP: score=1.1F spread=— depth25=$0 vol24h=$12.4k url=<site>/scorecards/spx-usdc-perp.html
BTC benchmark: spread=4.3 depth25=$351.1k
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
