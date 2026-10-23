# Outreach — Phase 0

Generated 2026-10-23T22:11:36Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **180 of 286 Injective perp markets (62.9%)** had no two-sided quote at snapshot time.
- The median quoted market is **67.9 bps wide** (BTC: 6.9 bps).
- **Median two-sided depth inside 25 bps: $10.** The whole venue holds $1.15M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 19 F | — | $0 | $451.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `NZDUSD/USDC PERP` | 14 F | — | $0 | $169.5k | [scorecard](docs/scorecards/nzdusd-usdc-perp.html) |
| `STX/USDC PERP` | 13 F | — | $0 | $125.3k | [scorecard](docs/scorecards/stx-usdc-perp.html) |
| `CRM/USDC PERP` | 32 E | 740.2 | $10 | $86.0k | [scorecard](docs/scorecards/crm-usdc-perp.html) |
| `XAG/USDC PERP` | 34 E | 19,999.3 | $1 | $157.7k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `XLM/USDC PERP` | 36 D | 273.2 | $1 | $79.6k | [scorecard](docs/scorecards/xlm-usdc-perp.html) |
| `DASH/USDC PERP` | 36 D | 159.2 | $5 | $63.2k | [scorecard](docs/scorecards/dash-usdc-perp.html) |

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
BTC/USDC PERP: score=94.0A spread=6.9 depth25=$281.2k vol24h=$15.80M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=88.9A spread=1.2 depth25=$153.3k vol24h=$12.86M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=83.7A spread=7.7 depth25=$40.5k vol24h=$7.78M url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.1F spread=— depth25=$0 vol24h=$451.4k url=<site>/scorecards/usdsek-usdc-perp.html
NZDUSD/USDC PERP: score=14.2F spread=— depth25=$0 vol24h=$169.5k url=<site>/scorecards/nzdusd-usdc-perp.html
STX/USDC PERP: score=12.7F spread=— depth25=$0 vol24h=$125.3k url=<site>/scorecards/stx-usdc-perp.html
CRM/USDC PERP: score=32.1E spread=740.2 depth25=$10 vol24h=$86.0k url=<site>/scorecards/crm-usdc-perp.html
XAG/USDC PERP: score=34.2E spread=19,999.3 depth25=$1 vol24h=$157.7k url=<site>/scorecards/xag-usdc-perp.html
XLM/USDC PERP: score=36.2D spread=273.2 depth25=$1 vol24h=$79.6k url=<site>/scorecards/xlm-usdc-perp.html
DASH/USDC PERP: score=36.2D spread=159.2 depth25=$5 vol24h=$63.2k url=<site>/scorecards/dash-usdc-perp.html
BTC benchmark: spread=6.9 depth25=$281.2k
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
