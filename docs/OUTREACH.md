# Outreach — Phase 0

Generated 2026-11-01T23:35:50Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **224 of 286 Injective perp markets (78.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **66.4 bps wide** (BTC: 10.0 bps).
- **Median two-sided depth inside 25 bps: $1.1k.** The whole venue holds $1.32M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $538.6k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDHKD/USDC PERP` | 20 F | — | $0 | $492.5k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `XAU/USDC PERP` | 17 F | — | $0 | $311.7k | [scorecard](docs/scorecards/xau-usdc-perp.html) |
| `MU/USDC PERP` | 38 D | 19,999.6 | $2 | $222.3k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `RENDER/USDC PERP` | 40 D | 158.2 | $5 | $177.5k | [scorecard](docs/scorecards/render-usdc-perp.html) |
| `CRCL/USDC PERP` | 43 D | 120.5 | $1.1k | $74.7k | [scorecard](docs/scorecards/crcl-usdc-perp.html) |
| `ORCL/USDC PERP` | 45 D | 740.1 | $10 | $190.6k | [scorecard](docs/scorecards/orcl-usdc-perp.html) |

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
BTC/USDC PERP: score=92.0A spread=10.0 depth25=$270.8k vol24h=$16.50M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=88.8A spread=16.3 depth25=$335.7k vol24h=$12.05M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=83.4A spread=30.6 depth25=$80.6k vol24h=$7.52M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$538.6k url=<site>/scorecards/sici-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$492.5k url=<site>/scorecards/usdhkd-usdc-perp.html
XAU/USDC PERP: score=17.2F spread=— depth25=$0 vol24h=$311.7k url=<site>/scorecards/xau-usdc-perp.html
MU/USDC PERP: score=38.2D spread=19,999.6 depth25=$2 vol24h=$222.3k url=<site>/scorecards/mu-usdc-perp.html
RENDER/USDC PERP: score=39.7D spread=158.2 depth25=$5 vol24h=$177.5k url=<site>/scorecards/render-usdc-perp.html
CRCL/USDC PERP: score=42.6D spread=120.5 depth25=$1.1k vol24h=$74.7k url=<site>/scorecards/crcl-usdc-perp.html
ORCL/USDC PERP: score=44.6D spread=740.1 depth25=$10 vol24h=$190.6k url=<site>/scorecards/orcl-usdc-perp.html
BTC benchmark: spread=10.0 depth25=$270.8k
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
