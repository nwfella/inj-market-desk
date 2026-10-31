# Outreach — Phase 0

Generated 2026-10-31T12:30:02Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **211 of 286 Injective perp markets (73.8%)** had no two-sided quote at snapshot time.
- The median quoted market is **83.3 bps wide** (BTC: 9.2 bps).
- **Median two-sided depth inside 25 bps: $774.** The whole venue holds $1.39M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 F | — | $0 | $492.6k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `XAG/USDC PERP` | 19 F | — | $0 | $417.5k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `DELL/USDC PERP` | 17 F | — | $0 | $308.1k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `PYPL/USDC PERP` | 32 E | 214.2 | $1 | $85.0k | [scorecard](docs/scorecards/pypl-usdc-perp.html) |
| `TRX/USDC PERP` | 32 E | 210.1 | $0 | $84.0k | [scorecard](docs/scorecards/trx-usdc-perp.html) |
| `STRC/USDC PERP` | 33 E | 740.9 | $11 | $97.7k | [scorecard](docs/scorecards/strc-usdc-perp.html) |
| `GME/USDC PERP` | 33 E | 213.3 | $1 | $114.9k | [scorecard](docs/scorecards/gme-usdc-perp.html) |

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
BTC/USDC PERP: score=92.0A spread=9.2 depth25=$271.2k vol24h=$16.76M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=90.1A spread=12.9 depth25=$372.9k vol24h=$12.17M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=88.9A spread=16.8 depth25=$79.9k vol24h=$7.40M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$492.6k url=<site>/scorecards/usdhkd-usdc-perp.html
XAG/USDC PERP: score=18.7F spread=— depth25=$0 vol24h=$417.5k url=<site>/scorecards/xag-usdc-perp.html
DELL/USDC PERP: score=17.2F spread=— depth25=$0 vol24h=$308.1k url=<site>/scorecards/dell-usdc-perp.html
PYPL/USDC PERP: score=32.0E spread=214.2 depth25=$1 vol24h=$85.0k url=<site>/scorecards/pypl-usdc-perp.html
TRX/USDC PERP: score=32.5E spread=210.1 depth25=$0 vol24h=$84.0k url=<site>/scorecards/trx-usdc-perp.html
STRC/USDC PERP: score=32.6E spread=740.9 depth25=$11 vol24h=$97.7k url=<site>/scorecards/strc-usdc-perp.html
GME/USDC PERP: score=33.0E spread=213.3 depth25=$1 vol24h=$114.9k url=<site>/scorecards/gme-usdc-perp.html
BTC benchmark: spread=9.2 depth25=$271.2k
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
