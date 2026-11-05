# Outreach — Phase 0

Generated 2026-11-05T12:21:57Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **262 of 326 Injective perp markets (80.4%)** had no two-sided quote at snapshot time.
- The median quoted market is **58.0 bps wide** (BTC: 3.9 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.25M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SNDK/USDC PERP` | 21 E | — | $0 | $721.0k | [scorecard](docs/scorecards/sndk-usdc-perp.html) |
| `USTECH/USDC PERP` | 21 E | — | $0 | $684.6k | [scorecard](docs/scorecards/ustech-usdc-perp.html) |
| `US500/USDC PERP` | 21 E | — | $0 | $633.6k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `LULU/USDC PERP` | 31 E | 223.3 | $9 | $60.7k | [scorecard](docs/scorecards/lulu-usdc-perp.html) |
| `COST/USDC PERP` | 34 E | 671.6 | $10 | $136.0k | [scorecard](docs/scorecards/cost-usdc-perp.html) |
| `DELL/USDC PERP` | 38 D | 740.0 | $10 | $578.9k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `INTC/USDC PERP` | 39 D | 19,993.1 | $10 | $697.7k | [scorecard](docs/scorecards/intc-usdc-perp.html) |

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
BTC/USDC PERP: score=95.3A spread=3.9 depth25=$318.7k vol24h=$7.07M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=92.2A spread=4.6 depth25=$225.6k vol24h=$5.63M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=87.5A spread=34.8 depth25=$100.1k vol24h=$3.98M url=<site>/scorecards/inj-usdc-perp.html
SNDK/USDC PERP: score=21.4E spread=— depth25=$0 vol24h=$721.0k url=<site>/scorecards/sndk-usdc-perp.html
USTECH/USDC PERP: score=21.2E spread=— depth25=$0 vol24h=$684.6k url=<site>/scorecards/ustech-usdc-perp.html
US500/USDC PERP: score=20.8E spread=— depth25=$0 vol24h=$633.6k url=<site>/scorecards/us500-usdc-perp.html
LULU/USDC PERP: score=31.0E spread=223.3 depth25=$9 vol24h=$60.7k url=<site>/scorecards/lulu-usdc-perp.html
COST/USDC PERP: score=33.9E spread=671.6 depth25=$10 vol24h=$136.0k url=<site>/scorecards/cost-usdc-perp.html
DELL/USDC PERP: score=38.4D spread=740.0 depth25=$10 vol24h=$578.9k url=<site>/scorecards/dell-usdc-perp.html
INTC/USDC PERP: score=39.1D spread=19,993.1 depth25=$10 vol24h=$697.7k url=<site>/scorecards/intc-usdc-perp.html
BTC benchmark: spread=3.9 depth25=$318.7k
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
