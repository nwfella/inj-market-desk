# Outreach — Phase 0

Generated 2026-11-19T13:07:39Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **308 of 363 Injective perp markets (84.8%)** had no two-sided quote at snapshot time.
- The median quoted market is **47.4 bps wide** (BTC: 5.3 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.25M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 23 E | — | $0 | $1.41M | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `DELL/USDC PERP` | 19 F | — | $0 | $460.8k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `EURUSD/USDC PERP` | 19 F | — | $0 | $455.7k | [scorecard](docs/scorecards/eurusd-usdc-perp.html) |
| `FIL/USDC PERP` | 35 E | 212.2 | $1 | $180.7k | [scorecard](docs/scorecards/fil-usdc-perp.html) |
| `XAG/USDC PERP` | 38 D | 19,999.1 | $5 | $433.5k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `ANT/USDC PERP` | 38 D | 1,646.1 | $28 | $79.9k | [scorecard](docs/scorecards/ant-usdc-perp.html) |
| `FLOKI/USDC PERP` | 43 D | 740.1 | $11 | $149.2k | [scorecard](docs/scorecards/floki-usdc-perp.html) |

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
BTC/USDC PERP: score=95.5A spread=5.3 depth25=$326.4k vol24h=$4.26M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.1A spread=10.0 depth25=$346.1k vol24h=$3.73M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=87.7A spread=38.6 depth25=$120.8k vol24h=$4.18M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=23.1E spread=— depth25=$0 vol24h=$1.41M url=<site>/scorecards/usdhkd-usdc-perp.html
DELL/USDC PERP: score=19.2F spread=— depth25=$0 vol24h=$460.8k url=<site>/scorecards/dell-usdc-perp.html
EURUSD/USDC PERP: score=19.1F spread=— depth25=$0 vol24h=$455.7k url=<site>/scorecards/eurusd-usdc-perp.html
FIL/USDC PERP: score=34.9E spread=212.2 depth25=$1 vol24h=$180.7k url=<site>/scorecards/fil-usdc-perp.html
XAG/USDC PERP: score=38.3D spread=19,999.1 depth25=$5 vol24h=$433.5k url=<site>/scorecards/xag-usdc-perp.html
ANT/USDC PERP: score=38.5D spread=1,646.1 depth25=$28 vol24h=$79.9k url=<site>/scorecards/ant-usdc-perp.html
FLOKI/USDC PERP: score=43.4D spread=740.1 depth25=$11 vol24h=$149.2k url=<site>/scorecards/floki-usdc-perp.html
BTC benchmark: spread=5.3 depth25=$326.4k
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
