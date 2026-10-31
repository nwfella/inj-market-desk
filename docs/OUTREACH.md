# Outreach — Phase 0

Generated 2026-10-31T21:35:33Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **216 of 286 Injective perp markets (75.5%)** had no two-sided quote at snapshot time.
- The median quoted market is **73.8 bps wide** (BTC: 9.2 bps).
- **Median two-sided depth inside 25 bps: $386.** The whole venue holds $984.5k within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 F | — | $0 | $492.8k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 18 F | — | $0 | $326.6k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `XAG/USDC PERP` | 13 F | — | $0 | $137.8k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `GBPUSD/USDC PERP` | 32 E | 19,999.7 | $100 | $61.0k | [scorecard](docs/scorecards/gbpusd-usdc-perp.html) |
| `SNDK/USDC PERP` | 34 E | 249.3 | $1 | $75.1k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `FIL/USDC PERP` | 40 D | 279.0 | $732 | $102.2k | [scorecard](docs/scorecards/fil-usdc-perp.html) |
| `ORCL/USDC PERP` | 42 D | 740.5 | $10 | $85.0k | [scorecard](docs/scorecards/orcl-usdc-perp.html) |

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
BTC/USDC PERP: score=64.1C spread=9.2 depth25=$500 vol24h=$16.30M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=94.7A spread=5.8 depth25=$313.7k vol24h=$12.03M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.5A spread=12.5 depth25=$79.9k vol24h=$7.29M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$492.8k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=17.5F spread=— depth25=$0 vol24h=$326.6k url=<site>/scorecards/sici-usdc-perp.html
XAG/USDC PERP: score=13.1F spread=— depth25=$0 vol24h=$137.8k url=<site>/scorecards/xag-usdc-perp.html
GBPUSD/USDC PERP: score=32.1E spread=19,999.7 depth25=$100 vol24h=$61.0k url=<site>/scorecards/gbpusd-usdc-perp.html
SNDK/USDC PERP: score=33.6E spread=249.3 depth25=$1 vol24h=$75.1k url=<site>/scorecards/sndk-usdc-perp.html
FIL/USDC PERP: score=40.2D spread=279.0 depth25=$732 vol24h=$102.2k url=<site>/scorecards/fil-usdc-perp.html
ORCL/USDC PERP: score=41.9D spread=740.5 depth25=$10 vol24h=$85.0k url=<site>/scorecards/orcl-usdc-perp.html
BTC benchmark: spread=9.2 depth25=$500
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
