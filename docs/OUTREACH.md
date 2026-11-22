# Outreach — Phase 0

Generated 2026-11-22T11:35:32Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **256 of 307 Injective perp markets (83.4%)** had no two-sided quote at snapshot time.
- The median quoted market is **68.9 bps wide** (BTC: 6.9 bps).
- **Median two-sided depth inside 25 bps: $1.1k.** The whole venue holds $1.17M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.4k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `NEAR/USDC PERP` | 16 F | — | $0 | $239.7k | [scorecard](docs/scorecards/near-usdc-perp.html) |
| `NVDA/USDC PERP` | 36 D | 246.0 | $1.8k | $121.7k | [scorecard](docs/scorecards/nvda-usdc-perp.html) |
| `ATOM/USDC PERP` | 51 C | 39.7 | $80 | $56.6k | [scorecard](docs/scorecards/atom-usdc-perp.html) |
| `PEPE/USDC PERP` | 53 C | 32.1 | $50 | $71.2k | [scorecard](docs/scorecards/pepe-usdc-perp.html) |
| `AVAX/USDC PERP` | 54 C | 48.9 | $60 | $201.8k | [scorecard](docs/scorecards/avax-usdc-perp.html) |

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
BTC/USDC PERP: score=94.2A spread=6.9 depth25=$282.7k vol24h=$1.55M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.4A spread=8.8 depth25=$303.9k vol24h=$1.13M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=55.6C spread=11.2 depth25=$1 vol24h=$79.3k url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.4k url=<site>/scorecards/usdhkd-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
NEAR/USDC PERP: score=15.9F spread=— depth25=$0 vol24h=$239.7k url=<site>/scorecards/near-usdc-perp.html
NVDA/USDC PERP: score=36.4D spread=246.0 depth25=$1.8k vol24h=$121.7k url=<site>/scorecards/nvda-usdc-perp.html
ATOM/USDC PERP: score=51.0C spread=39.7 depth25=$80 vol24h=$56.6k url=<site>/scorecards/atom-usdc-perp.html
PEPE/USDC PERP: score=52.6C spread=32.1 depth25=$50 vol24h=$71.2k url=<site>/scorecards/pepe-usdc-perp.html
AVAX/USDC PERP: score=53.9C spread=48.9 depth25=$60 vol24h=$201.8k url=<site>/scorecards/avax-usdc-perp.html
BTC benchmark: spread=6.9 depth25=$282.7k
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
