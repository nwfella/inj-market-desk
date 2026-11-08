# Outreach — Phase 0

Generated 2026-11-08T15:13:22Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **283 of 354 Injective perp markets (79.9%)** had no two-sided quote at snapshot time.
- The median quoted market is **68.9 bps wide** (BTC: 2.4 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.30M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 F | — | $0 | $501.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `SKY/USDC PERP` | 19 F | — | $0 | $425.9k | [scorecard](docs/scorecards/sky-usdc-perp.html) |
| `US500/USDC PERP` | 19 F | — | $0 | $418.9k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `MU/USDC PERP` | 31 E | 19,999.4 | $10 | $66.1k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `INTC/USDC PERP` | 39 D | 19,993.1 | $1 | $324.7k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `WLD/USDC PERP` | 41 D | 141.1 | $5 | $136.7k | [scorecard](docs/scorecards/wld-usdc-perp.html) |
| `ORCL/USDC PERP` | 45 D | 740.4 | $10 | $211.5k | [scorecard](docs/scorecards/orcl-usdc-perp.html) |

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
BTC/USDC PERP: score=96.1A spread=2.4 depth25=$350.7k vol24h=$7.39M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=92.6A spread=2.2 depth25=$227.2k vol24h=$5.28M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.1A spread=22.2 depth25=$100.4k vol24h=$3.63M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=19.6F spread=— depth25=$0 vol24h=$501.9k url=<site>/scorecards/sici-usdc-perp.html
SKY/USDC PERP: score=18.8F spread=— depth25=$0 vol24h=$425.9k url=<site>/scorecards/sky-usdc-perp.html
US500/USDC PERP: score=18.7F spread=— depth25=$0 vol24h=$418.9k url=<site>/scorecards/us500-usdc-perp.html
MU/USDC PERP: score=31.3E spread=19,999.4 depth25=$10 vol24h=$66.1k url=<site>/scorecards/mu-usdc-perp.html
INTC/USDC PERP: score=38.8D spread=19,993.1 depth25=$1 vol24h=$324.7k url=<site>/scorecards/intc-usdc-perp.html
WLD/USDC PERP: score=41.1D spread=141.1 depth25=$5 vol24h=$136.7k url=<site>/scorecards/wld-usdc-perp.html
ORCL/USDC PERP: score=44.9D spread=740.4 depth25=$10 vol24h=$211.5k url=<site>/scorecards/orcl-usdc-perp.html
BTC benchmark: spread=2.4 depth25=$350.7k
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
