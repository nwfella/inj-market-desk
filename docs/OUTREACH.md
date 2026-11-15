# Outreach — Phase 0

Generated 2026-11-15T09:26:43Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **257 of 308 Injective perp markets (83.4%)** had no two-sided quote at snapshot time.
- The median quoted market is **49.4 bps wide** (BTC: 9.3 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.09M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $577.4k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 20 F | — | $0 | $521.2k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `DELL/USDC PERP` | 19 F | — | $0 | $408.9k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `MU/USDC PERP` | 44 D | 19,999.5 | $5 | $350.0k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `COIN/USDC PERP` | 46 D | 76.7 | $5 | $50.6k | [scorecard](docs/scorecards/coin-usdc-perp.html) |
| `GOOGL/USDC PERP` | 47 D | 93.9 | $5 | $156.6k | [scorecard](docs/scorecards/googl-usdc-perp.html) |
| `HOOD/USDC PERP` | 50 C | 73.4 | $5 | $158.9k | [scorecard](docs/scorecards/hood-usdc-perp.html) |

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
BTC/USDC PERP: score=86.4A spread=9.3 depth25=$186.9k vol24h=$7.17M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=88.7A spread=16.4 depth25=$289.5k vol24h=$5.58M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.4A spread=32.7 depth25=$100.4k vol24h=$3.36M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.3E spread=— depth25=$0 vol24h=$577.4k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=19.8F spread=— depth25=$0 vol24h=$521.2k url=<site>/scorecards/sici-usdc-perp.html
DELL/USDC PERP: score=18.6F spread=— depth25=$0 vol24h=$408.9k url=<site>/scorecards/dell-usdc-perp.html
MU/USDC PERP: score=43.5D spread=19,999.5 depth25=$5 vol24h=$350.0k url=<site>/scorecards/mu-usdc-perp.html
COIN/USDC PERP: score=45.8D spread=76.7 depth25=$5 vol24h=$50.6k url=<site>/scorecards/coin-usdc-perp.html
GOOGL/USDC PERP: score=47.4D spread=93.9 depth25=$5 vol24h=$156.6k url=<site>/scorecards/googl-usdc-perp.html
HOOD/USDC PERP: score=50.0C spread=73.4 depth25=$5 vol24h=$158.9k url=<site>/scorecards/hood-usdc-perp.html
BTC benchmark: spread=9.3 depth25=$186.9k
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
