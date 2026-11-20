# Outreach — Phase 0

Generated 2026-11-20T11:50:38Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **307 of 363 Injective perp markets (84.6%)** had no two-sided quote at snapshot time.
- The median quoted market is **48.6 bps wide** (BTC: 4.9 bps).
- **Median two-sided depth inside 25 bps: $4.8k.** The whole venue holds $1.24M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 20 F | — | $0 | $504.0k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `AFRM/USDC PERP` | 18 F | — | $0 | $342.4k | [scorecard](docs/scorecards/afrm-usdc-perp.html) |
| `BAC/USDC PERP` | 18 F | — | $0 | $339.9k | [scorecard](docs/scorecards/bac-usdc-perp.html) |
| `XAG/USDC PERP` | 36 D | 19,999.1 | $18 | $126.9k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `TSLA/USDC PERP` | 52 C | 35.4 | $500 | $68.0k | [scorecard](docs/scorecards/tsla-usdc-perp.html) |
| `AMZN/USDC PERP` | 54 C | 31.2 | $500 | $83.1k | [scorecard](docs/scorecards/amzn-usdc-perp.html) |
| `ZRO/USDC PERP` | 59 C | 72.5 | $7.1k | $107.6k | [scorecard](docs/scorecards/zro-usdc-perp.html) |

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
BTC/USDC PERP: score=95.3A spread=4.9 depth25=$333.4k vol24h=$3.93M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.5A spread=6.9 depth25=$341.3k vol24h=$2.63M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=82.0A spread=27.9 depth25=$80.2k vol24h=$256.2k url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.6F spread=— depth25=$0 vol24h=$504.0k url=<site>/scorecards/usdsek-usdc-perp.html
AFRM/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$342.4k url=<site>/scorecards/afrm-usdc-perp.html
BAC/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$339.9k url=<site>/scorecards/bac-usdc-perp.html
XAG/USDC PERP: score=36.4D spread=19,999.1 depth25=$18 vol24h=$126.9k url=<site>/scorecards/xag-usdc-perp.html
TSLA/USDC PERP: score=52.2C spread=35.4 depth25=$500 vol24h=$68.0k url=<site>/scorecards/tsla-usdc-perp.html
AMZN/USDC PERP: score=53.5C spread=31.2 depth25=$500 vol24h=$83.1k url=<site>/scorecards/amzn-usdc-perp.html
ZRO/USDC PERP: score=58.9C spread=72.5 depth25=$7.1k vol24h=$107.6k url=<site>/scorecards/zro-usdc-perp.html
BTC benchmark: spread=4.9 depth25=$333.4k
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
