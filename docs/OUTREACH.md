# Outreach — Phase 0

Generated 2026-11-04T17:17:02Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **261 of 326 Injective perp markets (80.1%)** had no two-sided quote at snapshot time.
- The median quoted market is **52.1 bps wide** (BTC: 7.2 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.21M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDNOK/USDC PERP` | 20 F | — | $0 | $487.4k | [scorecard](docs/scorecards/usdnok-usdc-perp.html) |
| `MRNA/USDC PERP` | 18 F | — | $0 | $351.6k | [scorecard](docs/scorecards/mrna-usdc-perp.html) |
| `SNOW/USDC PERP` | 17 F | — | $0 | $320.0k | [scorecard](docs/scorecards/snow-usdc-perp.html) |
| `XAG/USDC PERP` | 33 E | 19,999.2 | $100 | $76.4k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `INTC/USDC PERP` | 35 E | 19,993.2 | $10 | $181.1k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `AMD/USDC PERP` | 42 D | 740.0 | $10 | $84.2k | [scorecard](docs/scorecards/amd-usdc-perp.html) |
| `FIL/USDC PERP` | 42 D | 136.8 | $160 | $66.9k | [scorecard](docs/scorecards/fil-usdc-perp.html) |

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
BTC/USDC PERP: score=95.2A spread=7.2 depth25=$319.2k vol24h=$7.46M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.7A spread=5.8 depth25=$345.0k vol24h=$5.41M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.5A spread=34.8 depth25=$99.9k vol24h=$3.40M url=<site>/scorecards/inj-usdc-perp.html
USDNOK/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$487.4k url=<site>/scorecards/usdnok-usdc-perp.html
MRNA/USDC PERP: score=17.8F spread=— depth25=$0 vol24h=$351.6k url=<site>/scorecards/mrna-usdc-perp.html
SNOW/USDC PERP: score=17.4F spread=— depth25=$0 vol24h=$320.0k url=<site>/scorecards/snow-usdc-perp.html
XAG/USDC PERP: score=33.4E spread=19,999.2 depth25=$100 vol24h=$76.4k url=<site>/scorecards/xag-usdc-perp.html
INTC/USDC PERP: score=34.7E spread=19,993.2 depth25=$10 vol24h=$181.1k url=<site>/scorecards/intc-usdc-perp.html
AMD/USDC PERP: score=41.8D spread=740.0 depth25=$10 vol24h=$84.2k url=<site>/scorecards/amd-usdc-perp.html
FIL/USDC PERP: score=41.9D spread=136.8 depth25=$160 vol24h=$66.9k url=<site>/scorecards/fil-usdc-perp.html
BTC benchmark: spread=7.2 depth25=$319.2k
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
