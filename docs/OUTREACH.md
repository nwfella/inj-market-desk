# Outreach — Phase 0

Generated 2026-11-12T11:10:47Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **244 of 309 Injective perp markets (79.0%)** had no two-sided quote at snapshot time.
- The median quoted market is **56.3 bps wide** (BTC: 3.5 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.15M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 F | — | $0 | $511.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDSEK/USDC PERP` | 18 F | — | $0 | $344.1k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `PFE/USDC PERP` | 44 D | 104.2 | $9 | $66.7k | [scorecard](docs/scorecards/pfe-usdc-perp.html) |
| `TSM/USDC PERP` | 45 D | 96.2 | $5 | $87.9k | [scorecard](docs/scorecards/tsm-usdc-perp.html) |
| `NBIS/USDC PERP` | 46 D | 109.6 | $9 | $85.9k | [scorecard](docs/scorecards/nbis-usdc-perp.html) |
| `QCOM/USDC PERP` | 48 D | 70.0 | $5 | $61.4k | [scorecard](docs/scorecards/qcom-usdc-perp.html) |

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
BTC/USDC PERP: score=95.7A spread=3.5 depth25=$318.7k vol24h=$7.21M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.0A spread=4.4 depth25=$274.3k vol24h=$5.05M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=88.0A spread=15.8 depth25=$80.3k vol24h=$3.16M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=19.7F spread=— depth25=$0 vol24h=$511.5k url=<site>/scorecards/sici-usdc-perp.html
USDSEK/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$344.1k url=<site>/scorecards/usdsek-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
PFE/USDC PERP: score=43.6D spread=104.2 depth25=$9 vol24h=$66.7k url=<site>/scorecards/pfe-usdc-perp.html
TSM/USDC PERP: score=45.3D spread=96.2 depth25=$5 vol24h=$87.9k url=<site>/scorecards/tsm-usdc-perp.html
NBIS/USDC PERP: score=45.7D spread=109.6 depth25=$9 vol24h=$85.9k url=<site>/scorecards/nbis-usdc-perp.html
QCOM/USDC PERP: score=47.5D spread=70.0 depth25=$5 vol24h=$61.4k url=<site>/scorecards/qcom-usdc-perp.html
BTC benchmark: spread=3.5 depth25=$318.7k
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
