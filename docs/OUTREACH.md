# Outreach — Phase 0

Generated 2026-11-07T02:49:01Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **302 of 354 Injective perp markets (85.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **60.9 bps wide** (BTC: 8.9 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.12M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $535.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $398.3k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `USDSEK/USDC PERP` | 18 F | — | $0 | $373.6k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `MU/USDC PERP` | 31 E | 19,999.4 | $10 | $64.1k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `CRCL/USDC PERP` | 34 E | 19,999.7 | $999 | $100.0k | [scorecard](docs/scorecards/crcl-usdc-perp.html) |
| `HOOD/USDC PERP` | 40 D | 19,995.1 | $260 | $291.7k | [scorecard](docs/scorecards/hood-usdc-perp.html) |
| `AMZN/USDC PERP` | 54 C | 41.6 | $1.0k | $139.8k | [scorecard](docs/scorecards/amzn-usdc-perp.html) |

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
BTC/USDC PERP: score=94.1A spread=8.9 depth25=$302.9k vol24h=$8.82M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=88.8A spread=16.5 depth25=$333.3k vol24h=$5.94M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=88.3A spread=28.4 depth25=$100.2k vol24h=$3.18M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$535.9k url=<site>/scorecards/sici-usdc-perp.html
US500/USDC PERP: score=18.5F spread=— depth25=$0 vol24h=$398.3k url=<site>/scorecards/us500-usdc-perp.html
USDSEK/USDC PERP: score=18.1F spread=— depth25=$0 vol24h=$373.6k url=<site>/scorecards/usdsek-usdc-perp.html
MU/USDC PERP: score=31.2E spread=19,999.4 depth25=$10 vol24h=$64.1k url=<site>/scorecards/mu-usdc-perp.html
CRCL/USDC PERP: score=34.3E spread=19,999.7 depth25=$999 vol24h=$100.0k url=<site>/scorecards/crcl-usdc-perp.html
HOOD/USDC PERP: score=40.1D spread=19,995.1 depth25=$260 vol24h=$291.7k url=<site>/scorecards/hood-usdc-perp.html
AMZN/USDC PERP: score=54.1C spread=41.6 depth25=$1.0k vol24h=$139.8k url=<site>/scorecards/amzn-usdc-perp.html
BTC benchmark: spread=8.9 depth25=$302.9k
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
