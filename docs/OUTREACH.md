# Outreach — Phase 0

Generated 2026-11-06T17:30:13Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **278 of 354 Injective perp markets (78.5%)** had no two-sided quote at snapshot time.
- The median quoted market is **83.8 bps wide** (BTC: 3.3 bps).
- **Median two-sided depth inside 25 bps: $119.** The whole venue holds $976.5k within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $535.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $398.3k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `USDSEK/USDC PERP` | 18 F | — | $0 | $373.6k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `CRCL/USDC PERP` | 38 D | 153.8 | $5 | $96.4k | [scorecard](docs/scorecards/crcl-usdc-perp.html) |
| `QCOM/USDC PERP` | 41 D | 141.7 | $9 | $121.9k | [scorecard](docs/scorecards/qcom-usdc-perp.html) |
| `NIGHT/USDC PERP` | 46 D | 156.2 | $5 | $52.4k | [scorecard](docs/scorecards/night-usdc-perp.html) |
| `PFE/USDC PERP` | 46 D | 105.5 | $5 | $166.1k | [scorecard](docs/scorecards/pfe-usdc-perp.html) |

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
BTC/USDC PERP: score=95.5A spread=3.3 depth25=$329.5k vol24h=$9.23M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=90.8A spread=10.8 depth25=$206.5k vol24h=$6.00M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.2A spread=21.6 depth25=$100.2k vol24h=$3.29M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$535.9k url=<site>/scorecards/sici-usdc-perp.html
US500/USDC PERP: score=18.5F spread=— depth25=$0 vol24h=$398.3k url=<site>/scorecards/us500-usdc-perp.html
USDSEK/USDC PERP: score=18.1F spread=— depth25=$0 vol24h=$373.6k url=<site>/scorecards/usdsek-usdc-perp.html
CRCL/USDC PERP: score=38.3D spread=153.8 depth25=$5 vol24h=$96.4k url=<site>/scorecards/crcl-usdc-perp.html
QCOM/USDC PERP: score=40.7D spread=141.7 depth25=$9 vol24h=$121.9k url=<site>/scorecards/qcom-usdc-perp.html
NIGHT/USDC PERP: score=45.9D spread=156.2 depth25=$5 vol24h=$52.4k url=<site>/scorecards/night-usdc-perp.html
PFE/USDC PERP: score=46.3D spread=105.5 depth25=$5 vol24h=$166.1k url=<site>/scorecards/pfe-usdc-perp.html
BTC benchmark: spread=3.3 depth25=$329.5k
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
