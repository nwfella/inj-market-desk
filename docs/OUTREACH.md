# Outreach — Phase 0

Generated 2026-11-27T09:40:54Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **262 of 307 Injective perp markets (85.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **50.9 bps wide** (BTC: 6.5 bps).
- **Median two-sided depth inside 25 bps: $9.5k.** The whole venue holds $1.40M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `STX/USDC PERP` | 18 F | — | $0 | $392.3k | [scorecard](docs/scorecards/stx-usdc-perp.html) |
| `MU/USDC PERP` | 18 F | — | $0 | $351.6k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $344.0k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `EURUSD/USDC PERP` | 36 D | 19,999.6 | $100 | $120.3k | [scorecard](docs/scorecards/eurusd-usdc-perp.html) |
| `XAG/USDC PERP` | 40 D | 19,999.1 | $18 | $343.4k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `DELL/USDC PERP` | 43 D | 19,998.7 | $10 | $318.7k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `COIN/USDC PERP` | 53 C | 45.9 | $734 | $113.4k | [scorecard](docs/scorecards/coin-usdc-perp.html) |

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
BTC/USDC PERP: score=95.3A spread=6.5 depth25=$346.4k vol24h=$1.10M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=92.9A spread=6.3 depth25=$309.8k vol24h=$1.08M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=85.3A spread=30.6 depth25=$100.2k vol24h=$2.18M url=<site>/scorecards/inj-usdc-perp.html
STX/USDC PERP: score=18.4F spread=— depth25=$0 vol24h=$392.3k url=<site>/scorecards/stx-usdc-perp.html
MU/USDC PERP: score=17.8F spread=— depth25=$0 vol24h=$351.6k url=<site>/scorecards/mu-usdc-perp.html
US500/USDC PERP: score=17.7F spread=— depth25=$0 vol24h=$344.0k url=<site>/scorecards/us500-usdc-perp.html
EURUSD/USDC PERP: score=36.4D spread=19,999.6 depth25=$100 vol24h=$120.3k url=<site>/scorecards/eurusd-usdc-perp.html
XAG/USDC PERP: score=39.6D spread=19,999.1 depth25=$18 vol24h=$343.4k url=<site>/scorecards/xag-usdc-perp.html
DELL/USDC PERP: score=43.4D spread=19,998.7 depth25=$10 vol24h=$318.7k url=<site>/scorecards/dell-usdc-perp.html
COIN/USDC PERP: score=52.8C spread=45.9 depth25=$734 vol24h=$113.4k url=<site>/scorecards/coin-usdc-perp.html
BTC benchmark: spread=6.5 depth25=$346.4k
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
