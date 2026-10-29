# Outreach — Phase 0

Generated 2026-10-29T14:20:28Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **215 of 286 Injective perp markets (75.2%)** had no two-sided quote at snapshot time.
- The median quoted market is **58.9 bps wide** (BTC: 7.2 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.40M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 F | — | $0 | $485.0k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `INTC/USDC PERP` | 14 F | — | $0 | $151.7k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `PYTH/USDC PERP` | 13 F | — | $0 | $143.1k | [scorecard](docs/scorecards/pyth-usdc-perp.html) |
| `SNOW/USDC PERP` | 33 E | 215.3 | $5 | $113.7k | [scorecard](docs/scorecards/snow-usdc-perp.html) |
| `LDO/USDC PERP` | 36 D | 162.6 | $5 | $60.0k | [scorecard](docs/scorecards/ldo-usdc-perp.html) |
| `CRM/USDC PERP` | 36 D | 153.6 | $5 | $54.5k | [scorecard](docs/scorecards/crm-usdc-perp.html) |
| `VRT/USDC PERP` | 41 D | 240.9 | $5 | $74.7k | [scorecard](docs/scorecards/vrt-usdc-perp.html) |

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
BTC/USDC PERP: score=95.3A spread=7.2 depth25=$326.0k vol24h=$16.52M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.9A spread=6.0 depth25=$369.3k vol24h=$12.85M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.9A spread=16.2 depth25=$99.9k vol24h=$7.40M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$485.0k url=<site>/scorecards/usdhkd-usdc-perp.html
INTC/USDC PERP: score=13.6F spread=— depth25=$0 vol24h=$151.7k url=<site>/scorecards/intc-usdc-perp.html
PYTH/USDC PERP: score=13.3F spread=— depth25=$0 vol24h=$143.1k url=<site>/scorecards/pyth-usdc-perp.html
SNOW/USDC PERP: score=33.0E spread=215.3 depth25=$5 vol24h=$113.7k url=<site>/scorecards/snow-usdc-perp.html
LDO/USDC PERP: score=35.7D spread=162.6 depth25=$5 vol24h=$60.0k url=<site>/scorecards/ldo-usdc-perp.html
CRM/USDC PERP: score=36.4D spread=153.6 depth25=$5 vol24h=$54.5k url=<site>/scorecards/crm-usdc-perp.html
VRT/USDC PERP: score=41.4D spread=240.9 depth25=$5 vol24h=$74.7k url=<site>/scorecards/vrt-usdc-perp.html
BTC benchmark: spread=7.2 depth25=$326.0k
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
