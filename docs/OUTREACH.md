# Outreach — Phase 0

Generated 2026-11-22T19:40:39Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **257 of 307 Injective perp markets (83.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **55.0 bps wide** (BTC: 9.6 bps).
- **Median two-sided depth inside 25 bps: $7.7k.** The whole venue holds $1.34M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.4k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `NEAR/USDC PERP` | 16 F | — | $0 | $248.7k | [scorecard](docs/scorecards/near-usdc-perp.html) |
| `NVDA/USDC PERP` | 54 C | 240.9 | $34.6k | $71.0k | [scorecard](docs/scorecards/nvda-usdc-perp.html) |
| `LINK/USDC PERP` | 62 C | 50.7 | $5.0k | $100.9k | [scorecard](docs/scorecards/link-usdc-perp.html) |
| `AVAX/USDC PERP` | 63 C | 42.5 | $5.0k | $200.2k | [scorecard](docs/scorecards/avax-usdc-perp.html) |
| `ATOM/USDC PERP` | 63 C | 36.0 | $5.6k | $72.8k | [scorecard](docs/scorecards/atom-usdc-perp.html) |

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
BTC/USDC PERP: score=92.4A spread=9.6 depth25=$282.7k vol24h=$716.9k url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=87.2A spread=9.3 depth25=$328.6k vol24h=$159.1k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=81.3A spread=35.5 depth25=$104.6k vol24h=$368.1k url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.4k url=<site>/scorecards/usdhkd-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
NEAR/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$248.7k url=<site>/scorecards/near-usdc-perp.html
NVDA/USDC PERP: score=54.2C spread=240.9 depth25=$34.6k vol24h=$71.0k url=<site>/scorecards/nvda-usdc-perp.html
LINK/USDC PERP: score=61.5C spread=50.7 depth25=$5.0k vol24h=$100.9k url=<site>/scorecards/link-usdc-perp.html
AVAX/USDC PERP: score=62.9C spread=42.5 depth25=$5.0k vol24h=$200.2k url=<site>/scorecards/avax-usdc-perp.html
ATOM/USDC PERP: score=63.0C spread=36.0 depth25=$5.6k vol24h=$72.8k url=<site>/scorecards/atom-usdc-perp.html
BTC benchmark: spread=9.6 depth25=$282.7k
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
