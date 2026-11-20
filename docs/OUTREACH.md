# Outreach — Phase 0

Generated 2026-11-20T20:20:10Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **306 of 363 Injective perp markets (84.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **62.6 bps wide** (BTC: 6.5 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.32M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.5k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `AFRM/USDC PERP` | 18 F | — | $0 | $342.3k | [scorecard](docs/scorecards/afrm-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `PLTR/USDC PERP` | 32 E | 20,000.0 | $10 | $76.4k | [scorecard](docs/scorecards/pltr-usdc-perp.html) |
| `INTC/USDC PERP` | 36 D | 19,992.4 | $10 | $143.3k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `XAG/USDC PERP` | 39 D | 19,999.0 | $18 | $259.9k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `MU/USDC PERP` | 42 D | 19,999.3 | $10 | $184.9k | [scorecard](docs/scorecards/mu-usdc-perp.html) |

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
BTC/USDC PERP: score=95.7A spread=6.5 depth25=$353.0k vol24h=$4.30M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.6A spread=18.0 depth25=$335.3k vol24h=$944.5k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=81.7A spread=39.1 depth25=$100.4k vol24h=$524.4k url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.5k url=<site>/scorecards/usdhkd-usdc-perp.html
AFRM/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$342.3k url=<site>/scorecards/afrm-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
PLTR/USDC PERP: score=31.7E spread=20,000.0 depth25=$10 vol24h=$76.4k url=<site>/scorecards/pltr-usdc-perp.html
INTC/USDC PERP: score=35.5D spread=19,992.4 depth25=$10 vol24h=$143.3k url=<site>/scorecards/intc-usdc-perp.html
XAG/USDC PERP: score=38.7D spread=19,999.0 depth25=$18 vol24h=$259.9k url=<site>/scorecards/xag-usdc-perp.html
MU/USDC PERP: score=41.5D spread=19,999.3 depth25=$10 vol24h=$184.9k url=<site>/scorecards/mu-usdc-perp.html
BTC benchmark: spread=6.5 depth25=$353.0k
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
