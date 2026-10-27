# Outreach — Phase 0

Generated 2026-10-27T16:40:07Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **186 of 286 Injective perp markets (65.0%)** had no two-sided quote at snapshot time.
- The median quoted market is **69.7 bps wide** (BTC: 9.4 bps).
- **Median two-sided depth inside 25 bps: $10.** The whole venue holds $1.46M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 20 E | — | $0 | $543.1k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `SICI/USDC PERP` | 17 F | — | $0 | $323.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `SNOW/USDC PERP` | 16 F | — | $0 | $222.8k | [scorecard](docs/scorecards/snow-usdc-perp.html) |
| `STRC/USDC PERP` | 31 E | 719.4 | $10 | $62.7k | [scorecard](docs/scorecards/strc-usdc-perp.html) |
| `XAG/USDC PERP` | 33 E | 19,999.3 | $2 | $112.7k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `QCOM/USDC PERP` | 35 E | 192.2 | $1 | $66.7k | [scorecard](docs/scorecards/qcom-usdc-perp.html) |
| `SNDK/USDC PERP` | 37 D | 190.6 | $1 | $147.4k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |

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
BTC/USDC PERP: score=93.9A spread=9.4 depth25=$300.3k vol24h=$20.86M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=96.0A spread=5.5 depth25=$380.0k vol24h=$12.55M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.3A spread=22.0 depth25=$127.3k vol24h=$7.62M url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$543.1k url=<site>/scorecards/usdsek-usdc-perp.html
SICI/USDC PERP: score=17.4F spread=— depth25=$0 vol24h=$323.5k url=<site>/scorecards/sici-usdc-perp.html
SNOW/USDC PERP: score=15.6F spread=— depth25=$0 vol24h=$222.8k url=<site>/scorecards/snow-usdc-perp.html
STRC/USDC PERP: score=31.1E spread=719.4 depth25=$10 vol24h=$62.7k url=<site>/scorecards/strc-usdc-perp.html
XAG/USDC PERP: score=33.2E spread=19,999.3 depth25=$2 vol24h=$112.7k url=<site>/scorecards/xag-usdc-perp.html
QCOM/USDC PERP: score=34.7E spread=192.2 depth25=$1 vol24h=$66.7k url=<site>/scorecards/qcom-usdc-perp.html
SNDK/USDC PERP: score=37.2D spread=190.6 depth25=$1 vol24h=$147.4k url=<site>/scorecards/sndk-usdc-perp.html
BTC benchmark: spread=9.4 depth25=$300.3k
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
