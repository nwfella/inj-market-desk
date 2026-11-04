# Outreach — Phase 0

Generated 2026-11-04T22:40:58Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **265 of 326 Injective perp markets (81.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **47.3 bps wide** (BTC: 8.5 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.19M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDNOK/USDC PERP` | 20 F | — | $0 | $487.5k | [scorecard](docs/scorecards/usdnok-usdc-perp.html) |
| `MRNA/USDC PERP` | 18 F | — | $0 | $351.7k | [scorecard](docs/scorecards/mrna-usdc-perp.html) |
| `SNOW/USDC PERP` | 17 F | — | $0 | $320.1k | [scorecard](docs/scorecards/snow-usdc-perp.html) |
| `LULU/USDC PERP` | 31 E | 365.7 | $9 | $62.7k | [scorecard](docs/scorecards/lulu-usdc-perp.html) |
| `ORCL/USDC PERP` | 34 E | 739.5 | $10 | $146.4k | [scorecard](docs/scorecards/orcl-usdc-perp.html) |
| `XAG/USDC PERP` | 35 E | 19,999.2 | $100 | $109.0k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `INTC/USDC PERP` | 36 D | 19,993.2 | $10 | $228.5k | [scorecard](docs/scorecards/intc-usdc-perp.html) |

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
BTC/USDC PERP: score=95.0A spread=8.5 depth25=$319.2k vol24h=$7.46M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.4A spread=7.8 depth25=$345.9k vol24h=$5.45M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=87.1A spread=37.5 depth25=$99.9k vol24h=$3.44M url=<site>/scorecards/inj-usdc-perp.html
USDNOK/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$487.5k url=<site>/scorecards/usdnok-usdc-perp.html
MRNA/USDC PERP: score=17.8F spread=— depth25=$0 vol24h=$351.7k url=<site>/scorecards/mrna-usdc-perp.html
SNOW/USDC PERP: score=17.4F spread=— depth25=$0 vol24h=$320.1k url=<site>/scorecards/snow-usdc-perp.html
LULU/USDC PERP: score=31.2E spread=365.7 depth25=$9 vol24h=$62.7k url=<site>/scorecards/lulu-usdc-perp.html
ORCL/USDC PERP: score=33.9E spread=739.5 depth25=$10 vol24h=$146.4k url=<site>/scorecards/orcl-usdc-perp.html
XAG/USDC PERP: score=34.6E spread=19,999.2 depth25=$100 vol24h=$109.0k url=<site>/scorecards/xag-usdc-perp.html
INTC/USDC PERP: score=35.5D spread=19,993.2 depth25=$10 vol24h=$228.5k url=<site>/scorecards/intc-usdc-perp.html
BTC benchmark: spread=8.5 depth25=$319.2k
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
