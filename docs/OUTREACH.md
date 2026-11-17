# Outreach — Phase 0

Generated 2026-11-17T03:54:16Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **255 of 307 Injective perp markets (83.1%)** had no two-sided quote at snapshot time.
- The median quoted market is **49.4 bps wide** (BTC: 7.4 bps).
- **Median two-sided depth inside 25 bps: $5.1k.** The whole venue holds $1.30M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $557.5k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 20 F | — | $0 | $522.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $250.0k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `XAG/USDC PERP` | 32 E | 19,999.2 | $5 | $65.4k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `INTC/USDC PERP` | 35 E | 19,992.8 | $10 | $188.9k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `MU/USDC PERP` | 40 D | 19,999.5 | $5 | $146.2k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `DELL/USDC PERP` | 41 D | 19,998.8 | $5 | $145.2k | [scorecard](docs/scorecards/dell-usdc-perp.html) |

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
BTC/USDC PERP: score=95.3A spread=7.4 depth25=$327.3k vol24h=$7.08M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.1A spread=8.7 depth25=$326.9k vol24h=$5.30M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=83.4A spread=40.2 depth25=$100.4k vol24h=$3.72M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$557.5k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=19.8F spread=— depth25=$0 vol24h=$522.5k url=<site>/scorecards/sici-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$250.0k url=<site>/scorecards/pep-usdc-perp.html
XAG/USDC PERP: score=32.1E spread=19,999.2 depth25=$5 vol24h=$65.4k url=<site>/scorecards/xag-usdc-perp.html
INTC/USDC PERP: score=34.8E spread=19,992.8 depth25=$10 vol24h=$188.9k url=<site>/scorecards/intc-usdc-perp.html
MU/USDC PERP: score=40.5D spread=19,999.5 depth25=$5 vol24h=$146.2k url=<site>/scorecards/mu-usdc-perp.html
DELL/USDC PERP: score=40.6D spread=19,998.8 depth25=$5 vol24h=$145.2k url=<site>/scorecards/dell-usdc-perp.html
BTC benchmark: spread=7.4 depth25=$327.3k
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
