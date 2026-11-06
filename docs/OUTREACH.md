# Outreach — Phase 0

Generated 2026-11-06T23:08:58Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **304 of 354 Injective perp markets (85.9%)** had no two-sided quote at snapshot time.
- The median quoted market is **56.8 bps wide** (BTC: 7.2 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.08M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $535.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $398.3k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `USDSEK/USDC PERP` | 18 F | — | $0 | $373.6k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `CRCL/USDC PERP` | 34 E | 19,999.7 | $998 | $97.4k | [scorecard](docs/scorecards/crcl-usdc-perp.html) |
| `HOOD/USDC PERP` | 40 D | 19,995.1 | $260 | $285.9k | [scorecard](docs/scorecards/hood-usdc-perp.html) |
| `SUI/USDC PERP` | 55 C | 48.3 | $240 | $244.2k | [scorecard](docs/scorecards/sui-usdc-perp.html) |
| `AVAX/USDC PERP` | 57 C | 71.9 | $4.1k | $157.9k | [scorecard](docs/scorecards/avax-usdc-perp.html) |

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
BTC/USDC PERP: score=94.3A spread=7.2 depth25=$302.9k vol24h=$8.90M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=91.2A spread=11.6 depth25=$220.6k vol24h=$5.96M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=88.4A spread=27.6 depth25=$100.2k vol24h=$3.19M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$535.9k url=<site>/scorecards/sici-usdc-perp.html
US500/USDC PERP: score=18.5F spread=— depth25=$0 vol24h=$398.3k url=<site>/scorecards/us500-usdc-perp.html
USDSEK/USDC PERP: score=18.1F spread=— depth25=$0 vol24h=$373.6k url=<site>/scorecards/usdsek-usdc-perp.html
CRCL/USDC PERP: score=34.2E spread=19,999.7 depth25=$998 vol24h=$97.4k url=<site>/scorecards/crcl-usdc-perp.html
HOOD/USDC PERP: score=40.0D spread=19,995.1 depth25=$260 vol24h=$285.9k url=<site>/scorecards/hood-usdc-perp.html
SUI/USDC PERP: score=55.0C spread=48.3 depth25=$240 vol24h=$244.2k url=<site>/scorecards/sui-usdc-perp.html
AVAX/USDC PERP: score=57.3C spread=71.9 depth25=$4.1k vol24h=$157.9k url=<site>/scorecards/avax-usdc-perp.html
BTC benchmark: spread=7.2 depth25=$302.9k
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
