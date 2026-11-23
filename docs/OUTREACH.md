# Outreach — Phase 0

Generated 2026-11-23T21:25:53Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **249 of 307 Injective perp markets (81.1%)** had no two-sided quote at snapshot time.
- The median quoted market is **49.6 bps wide** (BTC: 7.7 bps).
- **Median two-sided depth inside 25 bps: $4.3k.** The whole venue holds $1.12M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 19 F | — | $0 | $482.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $250.0k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `MA/USDC PERP` | 14 F | — | $0 | $180.0k | [scorecard](docs/scorecards/ma-usdc-perp.html) |
| `MU/USDC PERP` | 31 E | 19,999.4 | $10 | $59.7k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `INTC/USDC PERP` | 34 E | 19,993.3 | $10 | $145.6k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `FET/USDC PERP` | 52 C | 38.8 | $6 | $58.1k | [scorecard](docs/scorecards/fet-usdc-perp.html) |
| `QCOM/USDC PERP` | 53 C | 34.0 | $18 | $77.0k | [scorecard](docs/scorecards/qcom-usdc-perp.html) |

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
BTC/USDC PERP: score=94.7A spread=7.7 depth25=$310.9k vol24h=$1.35M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.3A spread=11.6 depth25=$233.9k vol24h=$1.15M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=81.7A spread=32.5 depth25=$101.0k vol24h=$404.8k url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.4F spread=— depth25=$0 vol24h=$482.4k url=<site>/scorecards/usdsek-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$250.0k url=<site>/scorecards/pep-usdc-perp.html
MA/USDC PERP: score=14.5F spread=— depth25=$0 vol24h=$180.0k url=<site>/scorecards/ma-usdc-perp.html
MU/USDC PERP: score=31.0E spread=19,999.4 depth25=$10 vol24h=$59.7k url=<site>/scorecards/mu-usdc-perp.html
INTC/USDC PERP: score=33.9E spread=19,993.3 depth25=$10 vol24h=$145.6k url=<site>/scorecards/intc-usdc-perp.html
FET/USDC PERP: score=52.0C spread=38.8 depth25=$6 vol24h=$58.1k url=<site>/scorecards/fet-usdc-perp.html
QCOM/USDC PERP: score=52.9C spread=34.0 depth25=$18 vol24h=$77.0k url=<site>/scorecards/qcom-usdc-perp.html
BTC benchmark: spread=7.7 depth25=$310.9k
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
