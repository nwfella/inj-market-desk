# Outreach — Phase 0

Generated 2026-11-08T23:43:42Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **279 of 354 Injective perp markets (78.8%)** had no two-sided quote at snapshot time.
- The median quoted market is **82.6 bps wide** (BTC: 8.3 bps).
- **Median two-sided depth inside 25 bps: $500.** The whole venue holds $1.16M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 F | — | $0 | $501.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `SKY/USDC PERP` | 19 F | — | $0 | $425.9k | [scorecard](docs/scorecards/sky-usdc-perp.html) |
| `US500/USDC PERP` | 19 F | — | $0 | $419.0k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `MU/USDC PERP` | 35 D | 19,999.4 | $10 | $211.5k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `CRCL/USDC PERP` | 37 D | 192.4 | $1.1k | $250.9k | [scorecard](docs/scorecards/crcl-usdc-perp.html) |
| `MSFT/USDC PERP` | 46 D | 108.8 | $6 | $165.0k | [scorecard](docs/scorecards/msft-usdc-perp.html) |
| `WLD/USDC PERP` | 48 D | 89.6 | $5 | $136.7k | [scorecard](docs/scorecards/wld-usdc-perp.html) |

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
BTC/USDC PERP: score=95.4A spread=8.3 depth25=$350.7k vol24h=$8.29M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=89.1A spread=18.2 depth25=$251.4k vol24h=$5.48M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=64.8C spread=3.7 depth25=$228 vol24h=$3.66M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=19.6F spread=— depth25=$0 vol24h=$501.9k url=<site>/scorecards/sici-usdc-perp.html
SKY/USDC PERP: score=18.8F spread=— depth25=$0 vol24h=$425.9k url=<site>/scorecards/sky-usdc-perp.html
US500/USDC PERP: score=18.7F spread=— depth25=$0 vol24h=$419.0k url=<site>/scorecards/us500-usdc-perp.html
MU/USDC PERP: score=35.1D spread=19,999.4 depth25=$10 vol24h=$211.5k url=<site>/scorecards/mu-usdc-perp.html
CRCL/USDC PERP: score=37.3D spread=192.4 depth25=$1.1k vol24h=$250.9k url=<site>/scorecards/crcl-usdc-perp.html
MSFT/USDC PERP: score=45.7D spread=108.8 depth25=$6 vol24h=$165.0k url=<site>/scorecards/msft-usdc-perp.html
WLD/USDC PERP: score=47.6D spread=89.6 depth25=$5 vol24h=$136.7k url=<site>/scorecards/wld-usdc-perp.html
BTC benchmark: spread=8.3 depth25=$350.7k
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
