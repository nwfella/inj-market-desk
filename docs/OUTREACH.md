# Outreach — Phase 0

Generated 2026-10-30T14:09:21Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **203 of 286 Injective perp markets (71.0%)** had no two-sided quote at snapshot time.
- The median quoted market is **72.9 bps wide** (BTC: 16.2 bps).
- **Median two-sided depth inside 25 bps: $80.** The whole venue holds $1.27M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 F | — | $0 | $485.0k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 17 F | — | $0 | $314.8k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `HBAR/USDC PERP` | 17 F | — | $0 | $280.1k | [scorecard](docs/scorecards/hbar-usdc-perp.html) |
| `TSM/USDC PERP` | 30 E | 739.9 | $10 | $53.5k | [scorecard](docs/scorecards/tsm-usdc-perp.html) |
| `COIN/USDC PERP` | 37 D | 394.2 | $458 | $95.0k | [scorecard](docs/scorecards/coin-usdc-perp.html) |
| `AR/USDC PERP` | 44 D | 140.6 | $1 | $96.8k | [scorecard](docs/scorecards/ar-usdc-perp.html) |
| `RUNE/USDC PERP` | 46 D | 101.1 | $10 | $123.5k | [scorecard](docs/scorecards/rune-usdc-perp.html) |

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
BTC/USDC PERP: score=92.6A spread=16.2 depth25=$270.9k vol24h=$17.52M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=89.6A spread=6.3 depth25=$312.2k vol24h=$15.67M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.2A spread=14.1 depth25=$80.4k vol24h=$7.45M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$485.0k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=17.3F spread=— depth25=$0 vol24h=$314.8k url=<site>/scorecards/sici-usdc-perp.html
HBAR/USDC PERP: score=16.7F spread=— depth25=$0 vol24h=$280.1k url=<site>/scorecards/hbar-usdc-perp.html
TSM/USDC PERP: score=30.5E spread=739.9 depth25=$10 vol24h=$53.5k url=<site>/scorecards/tsm-usdc-perp.html
COIN/USDC PERP: score=37.2D spread=394.2 depth25=$458 vol24h=$95.0k url=<site>/scorecards/coin-usdc-perp.html
AR/USDC PERP: score=43.8D spread=140.6 depth25=$1 vol24h=$96.8k url=<site>/scorecards/ar-usdc-perp.html
RUNE/USDC PERP: score=45.7D spread=101.1 depth25=$10 vol24h=$123.5k url=<site>/scorecards/rune-usdc-perp.html
BTC benchmark: spread=16.2 depth25=$270.9k
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
