# Outreach — Phase 0

Generated 2026-10-23T18:22:37Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **182 of 286 Injective perp markets (63.6%)** had no two-sided quote at snapshot time.
- The median quoted market is **74.2 bps wide** (BTC: 8.8 bps).
- **Median two-sided depth inside 25 bps: $10.** The whole venue holds $1.48M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 19 F | — | $0 | $451.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `NZDUSD/USDC PERP` | 14 F | — | $0 | $169.5k | [scorecard](docs/scorecards/nzdusd-usdc-perp.html) |
| `STX/USDC PERP` | 13 F | — | $0 | $125.3k | [scorecard](docs/scorecards/stx-usdc-perp.html) |
| `CRM/USDC PERP` | 32 E | 739.8 | $10 | $85.4k | [scorecard](docs/scorecards/crm-usdc-perp.html) |
| `XAG/USDC PERP` | 34 E | 19,999.3 | $1 | $157.7k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `HBAR/USDC PERP` | 37 D | 179.8 | $70 | $87.1k | [scorecard](docs/scorecards/hbar-usdc-perp.html) |
| `DASH/USDC PERP` | 39 D | 139.2 | $5 | $64.4k | [scorecard](docs/scorecards/dash-usdc-perp.html) |

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
BTC/USDC PERP: score=94.7A spread=8.8 depth25=$316.5k vol24h=$15.72M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=88.5A spread=4.2 depth25=$268.2k vol24h=$12.33M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=86.9A spread=25.3 depth25=$125.8k vol24h=$7.62M url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.1F spread=— depth25=$0 vol24h=$451.4k url=<site>/scorecards/usdsek-usdc-perp.html
NZDUSD/USDC PERP: score=14.2F spread=— depth25=$0 vol24h=$169.5k url=<site>/scorecards/nzdusd-usdc-perp.html
STX/USDC PERP: score=12.7F spread=— depth25=$0 vol24h=$125.3k url=<site>/scorecards/stx-usdc-perp.html
CRM/USDC PERP: score=32.1E spread=739.8 depth25=$10 vol24h=$85.4k url=<site>/scorecards/crm-usdc-perp.html
XAG/USDC PERP: score=34.2E spread=19,999.3 depth25=$1 vol24h=$157.7k url=<site>/scorecards/xag-usdc-perp.html
HBAR/USDC PERP: score=36.7D spread=179.8 depth25=$70 vol24h=$87.1k url=<site>/scorecards/hbar-usdc-perp.html
DASH/USDC PERP: score=38.8D spread=139.2 depth25=$5 vol24h=$64.4k url=<site>/scorecards/dash-usdc-perp.html
BTC benchmark: spread=8.8 depth25=$316.5k
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
