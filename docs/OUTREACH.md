# Outreach — Phase 0

Generated 2026-10-28T21:05:41Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **201 of 286 Injective perp markets (70.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **56.6 bps wide** (BTC: 4.9 bps).
- **Median two-sided depth inside 25 bps: $50.** The whole venue holds $1.27M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 20 E | — | $0 | $543.3k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `UNI/USDC PERP` | 14 F | — | $0 | $177.4k | [scorecard](docs/scorecards/uni-usdc-perp.html) |
| `AMD/USDC PERP` | 14 F | — | $0 | $173.3k | [scorecard](docs/scorecards/amd-usdc-perp.html) |
| `CRM/USDC PERP` | 40 D | 740.4 | $10 | $51.5k | [scorecard](docs/scorecards/crm-usdc-perp.html) |
| `COST/USDC PERP` | 40 D | 740.0 | $11 | $54.8k | [scorecard](docs/scorecards/cost-usdc-perp.html) |
| `V/USDC PERP` | 40 D | 740.2 | $10 | $56.3k | [scorecard](docs/scorecards/v-usdc-perp.html) |
| `AVGO/USDC PERP` | 41 D | 739.8 | $10 | $61.1k | [scorecard](docs/scorecards/avgo-usdc-perp.html) |

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
BTC/USDC PERP: score=94.6A spread=4.9 depth25=$290.8k vol24h=$16.51M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=91.0A spread=3.0 depth25=$368.7k vol24h=$12.54M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=86.4A spread=24.7 depth25=$100.3k vol24h=$7.33M url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$543.3k url=<site>/scorecards/usdsek-usdc-perp.html
UNI/USDC PERP: score=14.4F spread=— depth25=$0 vol24h=$177.4k url=<site>/scorecards/uni-usdc-perp.html
AMD/USDC PERP: score=14.3F spread=— depth25=$0 vol24h=$173.3k url=<site>/scorecards/amd-usdc-perp.html
CRM/USDC PERP: score=40.3D spread=740.4 depth25=$10 vol24h=$51.5k url=<site>/scorecards/crm-usdc-perp.html
COST/USDC PERP: score=40.4D spread=740.0 depth25=$11 vol24h=$54.8k url=<site>/scorecards/cost-usdc-perp.html
V/USDC PERP: score=40.5D spread=740.2 depth25=$10 vol24h=$56.3k url=<site>/scorecards/v-usdc-perp.html
AVGO/USDC PERP: score=40.7D spread=739.8 depth25=$10 vol24h=$61.1k url=<site>/scorecards/avgo-usdc-perp.html
BTC benchmark: spread=4.9 depth25=$290.8k
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
