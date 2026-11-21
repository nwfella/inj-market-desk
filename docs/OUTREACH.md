# Outreach — Phase 0

Generated 2026-11-21T02:15:33Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **312 of 363 Injective perp markets (86.0%)** had no two-sided quote at snapshot time.
- The median quoted market is **50.7 bps wide** (BTC: 8.2 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $927.3k within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.2k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `AFRM/USDC PERP` | 18 F | — | $0 | $342.2k | [scorecard](docs/scorecards/afrm-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.8k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `INTC/USDC PERP` | 34 E | 19,992.5 | $10 | $148.8k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `XAG/USDC PERP` | 39 D | 19,999.0 | $18 | $259.8k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `NVDA/USDC PERP` | 49 D | 62.6 | $500 | $69.7k | [scorecard](docs/scorecards/nvda-usdc-perp.html) |
| `ARB/USDC PERP` | 52 C | 60.6 | $449 | $116.6k | [scorecard](docs/scorecards/arb-usdc-perp.html) |

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
BTC/USDC PERP: score=85.9A spread=8.2 depth25=$161.7k vol24h=$4.76M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=93.4A spread=1.9 depth25=$254.8k vol24h=$1.24M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=88.8A spread=9.5 depth25=$80.3k vol24h=$3.62M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.2k url=<site>/scorecards/usdhkd-usdc-perp.html
AFRM/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$342.2k url=<site>/scorecards/afrm-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.8k url=<site>/scorecards/pep-usdc-perp.html
INTC/USDC PERP: score=34.0E spread=19,992.5 depth25=$10 vol24h=$148.8k url=<site>/scorecards/intc-usdc-perp.html
XAG/USDC PERP: score=38.7D spread=19,999.0 depth25=$18 vol24h=$259.8k url=<site>/scorecards/xag-usdc-perp.html
NVDA/USDC PERP: score=49.0D spread=62.6 depth25=$500 vol24h=$69.7k url=<site>/scorecards/nvda-usdc-perp.html
ARB/USDC PERP: score=51.5C spread=60.6 depth25=$449 vol24h=$116.6k url=<site>/scorecards/arb-usdc-perp.html
BTC benchmark: spread=8.2 depth25=$161.7k
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
