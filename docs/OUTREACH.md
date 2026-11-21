# Outreach — Phase 0

Generated 2026-11-21T09:54:51Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **311 of 363 Injective perp markets (85.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **82.7 bps wide** (BTC: 4.2 bps).
- **Median two-sided depth inside 25 bps: $4.5k.** The whole venue holds $1.27M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.3k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `XAG/USDC PERP` | 18 F | — | $0 | $385.9k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $342.3k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `COIN/USDC PERP` | 31 E | 250.4 | $679 | $62.4k | [scorecard](docs/scorecards/coin-usdc-perp.html) |
| `HOOD/USDC PERP` | 33 E | 210.9 | $76 | $127.1k | [scorecard](docs/scorecards/hood-usdc-perp.html) |
| `MU/USDC PERP` | 36 D | 19,999.3 | $10 | $306.7k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `ANT/USDC PERP` | 39 D | 3,972.0 | $48 | $53.6k | [scorecard](docs/scorecards/ant-usdc-perp.html) |

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
BTC/USDC PERP: score=95.7A spread=4.2 depth25=$329.9k vol24h=$4.49M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.5A spread=11.0 depth25=$356.9k vol24h=$1.75M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=85.3A spread=36.3 depth25=$80.1k vol24h=$3.57M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.3k url=<site>/scorecards/usdhkd-usdc-perp.html
XAG/USDC PERP: score=18.3F spread=— depth25=$0 vol24h=$385.9k url=<site>/scorecards/xag-usdc-perp.html
US500/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$342.3k url=<site>/scorecards/us500-usdc-perp.html
COIN/USDC PERP: score=31.3E spread=250.4 depth25=$679 vol24h=$62.4k url=<site>/scorecards/coin-usdc-perp.html
HOOD/USDC PERP: score=33.3E spread=210.9 depth25=$76 vol24h=$127.1k url=<site>/scorecards/hood-usdc-perp.html
MU/USDC PERP: score=36.3D spread=19,999.3 depth25=$10 vol24h=$306.7k url=<site>/scorecards/mu-usdc-perp.html
ANT/USDC PERP: score=39.4D spread=3,972.0 depth25=$48 vol24h=$53.6k url=<site>/scorecards/ant-usdc-perp.html
BTC benchmark: spread=4.2 depth25=$329.9k
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
