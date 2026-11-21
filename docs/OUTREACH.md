# Outreach — Phase 0

Generated 2026-11-21T23:16:30Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **310 of 363 Injective perp markets (85.4%)** had no two-sided quote at snapshot time.
- The median quoted market is **74.7 bps wide** (BTC: 10.0 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.16M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.3k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `STX/USDC PERP` | 18 F | — | $0 | $392.1k | [scorecard](docs/scorecards/stx-usdc-perp.html) |
| `XAG/USDC PERP` | 18 F | — | $0 | $374.2k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `COIN/USDC PERP` | 33 E | 255.5 | $711 | $98.6k | [scorecard](docs/scorecards/coin-usdc-perp.html) |
| `MU/USDC PERP` | 36 D | 19,999.3 | $10 | $319.9k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `NEIRO/USDC PERP` | 41 D | 740.0 | $13 | $71.2k | [scorecard](docs/scorecards/neiro-usdc-perp.html) |
| `ANT/USDC PERP` | 41 D | 3,972.0 | $46 | $93.5k | [scorecard](docs/scorecards/ant-usdc-perp.html) |

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
BTC/USDC PERP: score=87.4A spread=10.0 depth25=$141.6k vol24h=$2.44M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=92.0A spread=7.7 depth25=$397.4k vol24h=$1.84M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=81.6A spread=25.2 depth25=$80.1k vol24h=$142.1k url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.3k url=<site>/scorecards/usdhkd-usdc-perp.html
STX/USDC PERP: score=18.4F spread=— depth25=$0 vol24h=$392.1k url=<site>/scorecards/stx-usdc-perp.html
XAG/USDC PERP: score=18.2F spread=— depth25=$0 vol24h=$374.2k url=<site>/scorecards/xag-usdc-perp.html
COIN/USDC PERP: score=32.8E spread=255.5 depth25=$711 vol24h=$98.6k url=<site>/scorecards/coin-usdc-perp.html
MU/USDC PERP: score=36.5D spread=19,999.3 depth25=$10 vol24h=$319.9k url=<site>/scorecards/mu-usdc-perp.html
NEIRO/USDC PERP: score=41.0D spread=740.0 depth25=$13 vol24h=$71.2k url=<site>/scorecards/neiro-usdc-perp.html
ANT/USDC PERP: score=41.1D spread=3,972.0 depth25=$46 vol24h=$93.5k url=<site>/scorecards/ant-usdc-perp.html
BTC benchmark: spread=10.0 depth25=$141.6k
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
