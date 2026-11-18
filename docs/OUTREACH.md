# Outreach — Phase 0

Generated 2026-11-18T13:58:44Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **310 of 363 Injective perp markets (85.4%)** had no two-sided quote at snapshot time.
- The median quoted market is **50.0 bps wide** (BTC: 6.1 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.31M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `AFRM/USDC PERP` | 18 F | — | $0 | $342.4k | [scorecard](docs/scorecards/afrm-usdc-perp.html) |
| `BAC/USDC PERP` | 18 F | — | $0 | $339.8k | [scorecard](docs/scorecards/bac-usdc-perp.html) |
| `USDHKD/USDC PERP` | 17 F | — | $0 | $277.9k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `MU/USDC PERP` | 40 D | 19,999.5 | $5 | $139.8k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `HOOD/USDC PERP` | 48 D | 60.3 | $92 | $55.5k | [scorecard](docs/scorecards/hood-usdc-perp.html) |
| `AAPL/USDC PERP` | 51 C | 34.9 | $400 | $51.8k | [scorecard](docs/scorecards/aapl-usdc-perp.html) |
| `CVX/USDC PERP` | 52 C | 57.1 | $5 | $78.2k | [scorecard](docs/scorecards/cvx-usdc-perp.html) |

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
BTC/USDC PERP: score=94.9A spread=6.1 depth25=$305.1k vol24h=$7.99M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.2A spread=7.8 depth25=$326.3k vol24h=$6.14M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.1A spread=34.4 depth25=$100.3k vol24h=$4.48M url=<site>/scorecards/inj-usdc-perp.html
AFRM/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$342.4k url=<site>/scorecards/afrm-usdc-perp.html
BAC/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$339.8k url=<site>/scorecards/bac-usdc-perp.html
USDHKD/USDC PERP: score=16.7F spread=— depth25=$0 vol24h=$277.9k url=<site>/scorecards/usdhkd-usdc-perp.html
MU/USDC PERP: score=40.4D spread=19,999.5 depth25=$5 vol24h=$139.8k url=<site>/scorecards/mu-usdc-perp.html
HOOD/USDC PERP: score=48.3D spread=60.3 depth25=$92 vol24h=$55.5k url=<site>/scorecards/hood-usdc-perp.html
AAPL/USDC PERP: score=51.4C spread=34.9 depth25=$400 vol24h=$51.8k url=<site>/scorecards/aapl-usdc-perp.html
CVX/USDC PERP: score=51.6C spread=57.1 depth25=$5 vol24h=$78.2k url=<site>/scorecards/cvx-usdc-perp.html
BTC benchmark: spread=6.1 depth25=$305.1k
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
