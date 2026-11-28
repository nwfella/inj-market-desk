# Outreach — Phase 0

Generated 2026-11-28T02:40:59Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **260 of 307 Injective perp markets (84.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **63.2 bps wide** (BTC: 5.2 bps).
- **Median two-sided depth inside 25 bps: $12.8k.** The whole venue holds $1.36M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $547.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDSEK/USDC PERP` | 20 F | — | $0 | $507.9k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `USTECH/USDC PERP` | 18 F | — | $0 | $335.6k | [scorecard](docs/scorecards/ustech-usdc-perp.html) |
| `AAPL/USDC PERP` | 36 D | 20,000.0 | $260 | $272.2k | [scorecard](docs/scorecards/aapl-usdc-perp.html) |
| `XAG/USDC PERP` | 40 D | 19,999.1 | $18 | $379.7k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `FLOKI/USDC PERP` | 40 D | 739.9 | $11 | $51.9k | [scorecard](docs/scorecards/floki-usdc-perp.html) |
| `EURUSD/USDC PERP` | 40 D | 19,999.6 | $100 | $316.8k | [scorecard](docs/scorecards/eurusd-usdc-perp.html) |

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
BTC/USDC PERP: score=95.5A spread=5.2 depth25=$346.4k vol24h=$2.79M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.2A spread=6.0 depth25=$309.8k vol24h=$1.62M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.1A spread=36.7 depth25=$99.9k vol24h=$2.50M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$547.5k url=<site>/scorecards/sici-usdc-perp.html
USDSEK/USDC PERP: score=19.7F spread=— depth25=$0 vol24h=$507.9k url=<site>/scorecards/usdsek-usdc-perp.html
USTECH/USDC PERP: score=17.6F spread=— depth25=$0 vol24h=$335.6k url=<site>/scorecards/ustech-usdc-perp.html
AAPL/USDC PERP: score=35.8D spread=20,000.0 depth25=$260 vol24h=$272.2k url=<site>/scorecards/aapl-usdc-perp.html
XAG/USDC PERP: score=39.9D spread=19,999.1 depth25=$18 vol24h=$379.7k url=<site>/scorecards/xag-usdc-perp.html
FLOKI/USDC PERP: score=40.0D spread=739.9 depth25=$11 vol24h=$51.9k url=<site>/scorecards/floki-usdc-perp.html
EURUSD/USDC PERP: score=40.2D spread=19,999.6 depth25=$100 vol24h=$316.8k url=<site>/scorecards/eurusd-usdc-perp.html
BTC benchmark: spread=5.2 depth25=$346.4k
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
