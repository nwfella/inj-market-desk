# Outreach — Phase 0

Generated 2026-10-29T20:18:26Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **188 of 286 Injective perp markets (65.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **86.0 bps wide** (BTC: 4.4 bps).
- **Median two-sided depth inside 25 bps: $35.** The whole venue holds $1.42M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 F | — | $0 | $485.0k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `INTC/USDC PERP` | 14 F | — | $0 | $151.8k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `BYND/USDC PERP` | 14 F | — | $0 | $147.0k | [scorecard](docs/scorecards/bynd-usdc-perp.html) |
| `NEAR/USDC PERP` | 31 E | 220.9 | $5 | $69.1k | [scorecard](docs/scorecards/near-usdc-perp.html) |
| `SNDK/USDC PERP` | 32 E | 19,999.7 | $10 | $74.0k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `STRK/USDC PERP` | 34 E | 177.4 | $4 | $56.5k | [scorecard](docs/scorecards/strk-usdc-perp.html) |
| `SNOW/USDC PERP` | 36 D | 219.6 | $5 | $249.7k | [scorecard](docs/scorecards/snow-usdc-perp.html) |

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
BTC/USDC PERP: score=95.6A spread=4.4 depth25=$326.0k vol24h=$16.36M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.3A spread=10.4 depth25=$368.7k vol24h=$12.76M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.6A spread=17.9 depth25=$99.9k vol24h=$7.42M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$485.0k url=<site>/scorecards/usdhkd-usdc-perp.html
INTC/USDC PERP: score=13.6F spread=— depth25=$0 vol24h=$151.8k url=<site>/scorecards/intc-usdc-perp.html
BYND/USDC PERP: score=13.5F spread=— depth25=$0 vol24h=$147.0k url=<site>/scorecards/bynd-usdc-perp.html
NEAR/USDC PERP: score=31.4E spread=220.9 depth25=$5 vol24h=$69.1k url=<site>/scorecards/near-usdc-perp.html
SNDK/USDC PERP: score=31.6E spread=19,999.7 depth25=$10 vol24h=$74.0k url=<site>/scorecards/sndk-usdc-perp.html
STRK/USDC PERP: score=33.6E spread=177.4 depth25=$4 vol24h=$56.5k url=<site>/scorecards/strk-usdc-perp.html
SNOW/USDC PERP: score=35.5D spread=219.6 depth25=$5 vol24h=$249.7k url=<site>/scorecards/snow-usdc-perp.html
BTC benchmark: spread=4.4 depth25=$326.0k
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
