# Outreach — Phase 0

Generated 2026-10-25T16:20:19Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **171 of 286 Injective perp markets (59.8%)** had no two-sided quote at snapshot time.
- The median quoted market is **63.4 bps wide** (BTC: 2.4 bps).
- **Median two-sided depth inside 25 bps: $13.** The whole venue holds $1.34M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 19 F | — | $0 | $451.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `XAU/USDC PERP` | 17 F | — | $0 | $312.6k | [scorecard](docs/scorecards/xau-usdc-perp.html) |
| `USTECH/USDC PERP` | 16 F | — | $0 | $248.3k | [scorecard](docs/scorecards/ustech-usdc-perp.html) |
| `XAG/USDC PERP` | 36 D | 19,999.3 | $1 | $318.5k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `DOT/USDC PERP` | 42 D | 742.2 | $3 | $86.6k | [scorecard](docs/scorecards/dot-usdc-perp.html) |
| `SNX/USDC PERP` | 42 D | 738.8 | $10 | $90.0k | [scorecard](docs/scorecards/snx-usdc-perp.html) |
| `EIGEN/USDC PERP` | 42 D | 151.0 | $1 | $140.5k | [scorecard](docs/scorecards/eigen-usdc-perp.html) |

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
BTC/USDC PERP: score=94.3A spread=2.4 depth25=$315.5k vol24h=$17.81M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.2A spread=6.8 depth25=$341.2k vol24h=$13.57M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.0A spread=20.9 depth25=$103.1k vol24h=$7.44M url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.1F spread=— depth25=$0 vol24h=$451.4k url=<site>/scorecards/usdsek-usdc-perp.html
XAU/USDC PERP: score=17.2F spread=— depth25=$0 vol24h=$312.6k url=<site>/scorecards/xau-usdc-perp.html
USTECH/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$248.3k url=<site>/scorecards/ustech-usdc-perp.html
XAG/USDC PERP: score=36.5D spread=19,999.3 depth25=$1 vol24h=$318.5k url=<site>/scorecards/xag-usdc-perp.html
DOT/USDC PERP: score=42.0D spread=742.2 depth25=$3 vol24h=$86.6k url=<site>/scorecards/dot-usdc-perp.html
SNX/USDC PERP: score=42.1D spread=738.8 depth25=$10 vol24h=$90.0k url=<site>/scorecards/snx-usdc-perp.html
EIGEN/USDC PERP: score=42.2D spread=151.0 depth25=$1 vol24h=$140.5k url=<site>/scorecards/eigen-usdc-perp.html
BTC benchmark: spread=2.4 depth25=$315.5k
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
