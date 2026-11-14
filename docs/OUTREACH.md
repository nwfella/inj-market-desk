# Outreach — Phase 0

Generated 2026-11-14T10:36:25Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **253 of 309 Injective perp markets (81.9%)** had no two-sided quote at snapshot time.
- The median quoted market is **47.0 bps wide** (BTC: 6.0 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.20M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $577.3k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 20 F | — | $0 | $503.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $250.0k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `XAG/USDC PERP` | 36 D | 19,999.2 | $5 | $183.3k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `MU/USDC PERP` | 39 D | 19,999.5 | $5 | $85.8k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `DELL/USDC PERP` | 40 D | 19,998.8 | $5 | $127.1k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `SNDK/USDC PERP` | 42 D | 19,999.5 | $10 | $96.3k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |

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
BTC/USDC PERP: score=95.3A spread=6.0 depth25=$318.1k vol24h=$9.18M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.1A spread=5.2 depth25=$288.7k vol24h=$5.92M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=85.1A spread=25.2 depth25=$100.5k vol24h=$3.39M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.3E spread=— depth25=$0 vol24h=$577.3k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=19.6F spread=— depth25=$0 vol24h=$503.5k url=<site>/scorecards/sici-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$250.0k url=<site>/scorecards/pep-usdc-perp.html
XAG/USDC PERP: score=35.5D spread=19,999.2 depth25=$5 vol24h=$183.3k url=<site>/scorecards/xag-usdc-perp.html
MU/USDC PERP: score=39.0D spread=19,999.5 depth25=$5 vol24h=$85.8k url=<site>/scorecards/mu-usdc-perp.html
DELL/USDC PERP: score=40.1D spread=19,998.8 depth25=$5 vol24h=$127.1k url=<site>/scorecards/dell-usdc-perp.html
SNDK/USDC PERP: score=42.1D spread=19,999.5 depth25=$10 vol24h=$96.3k url=<site>/scorecards/sndk-usdc-perp.html
BTC benchmark: spread=6.0 depth25=$318.1k
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
