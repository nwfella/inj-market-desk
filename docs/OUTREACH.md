# Outreach — Phase 0

Generated 2026-11-19T21:34:51Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **311 of 363 Injective perp markets (85.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **49.0 bps wide** (BTC: 10.2 bps).
- **Median two-sided depth inside 25 bps: $6.0k.** The whole venue holds $1.28M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 22 E | — | $0 | $860.1k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `AFRM/USDC PERP` | 18 F | — | $0 | $342.4k | [scorecard](docs/scorecards/afrm-usdc-perp.html) |
| `BAC/USDC PERP` | 18 F | — | $0 | $339.8k | [scorecard](docs/scorecards/bac-usdc-perp.html) |
| `MU/USDC PERP` | 39 D | 19,999.4 | $10 | $94.8k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `INTC/USDC PERP` | 43 D | 19,992.8 | $10 | $273.3k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `HOOD/USDC PERP` | 48 D | 57.1 | $97 | $52.1k | [scorecard](docs/scorecards/hood-usdc-perp.html) |
| `MSFT/USDC PERP` | 52 C | 41.4 | $200 | $82.8k | [scorecard](docs/scorecards/msft-usdc-perp.html) |

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
BTC/USDC PERP: score=94.3A spread=10.2 depth25=$306.9k vol24h=$2.49M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.7A spread=17.3 depth25=$325.7k vol24h=$5.00M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=87.5A spread=35.9 depth25=$103.5k vol24h=$4.19M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=22.3E spread=— depth25=$0 vol24h=$860.1k url=<site>/scorecards/usdhkd-usdc-perp.html
AFRM/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$342.4k url=<site>/scorecards/afrm-usdc-perp.html
BAC/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$339.8k url=<site>/scorecards/bac-usdc-perp.html
MU/USDC PERP: score=39.4D spread=19,999.4 depth25=$10 vol24h=$94.8k url=<site>/scorecards/mu-usdc-perp.html
INTC/USDC PERP: score=42.9D spread=19,992.8 depth25=$10 vol24h=$273.3k url=<site>/scorecards/intc-usdc-perp.html
HOOD/USDC PERP: score=48.5D spread=57.1 depth25=$97 vol24h=$52.1k url=<site>/scorecards/hood-usdc-perp.html
MSFT/USDC PERP: score=52.1C spread=41.4 depth25=$200 vol24h=$82.8k url=<site>/scorecards/msft-usdc-perp.html
BTC benchmark: spread=10.2 depth25=$306.9k
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
