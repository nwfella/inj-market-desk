# Outreach — Phase 0

Generated 2026-11-16T09:44:12Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **256 of 308 Injective perp markets (83.1%)** had no two-sided quote at snapshot time.
- The median quoted market is **45.7 bps wide** (BTC: 5.9 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.34M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $577.3k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 20 F | — | $0 | $522.6k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `US500/USDC PERP` | 18 F | — | $0 | $355.3k | [scorecard](docs/scorecards/us500-usdc-perp.html) |
| `MU/USDC PERP` | 36 D | 19,999.5 | $10 | $284.7k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `INTC/USDC PERP` | 37 D | 19,993.0 | $10 | $385.0k | [scorecard](docs/scorecards/intc-usdc-perp.html) |
| `DELL/USDC PERP` | 44 D | 19,998.8 | $5 | $362.9k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `HOOD/USDC PERP` | 50 C | 42.0 | $89 | $53.7k | [scorecard](docs/scorecards/hood-usdc-perp.html) |

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
BTC/USDC PERP: score=95.4A spread=5.9 depth25=$322.5k vol24h=$5.82M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=95.4A spread=5.0 depth25=$315.6k vol24h=$4.69M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.0A spread=22.6 depth25=$100.4k vol24h=$3.66M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.3E spread=— depth25=$0 vol24h=$577.3k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=19.8F spread=— depth25=$0 vol24h=$522.6k url=<site>/scorecards/sici-usdc-perp.html
US500/USDC PERP: score=17.9F spread=— depth25=$0 vol24h=$355.3k url=<site>/scorecards/us500-usdc-perp.html
MU/USDC PERP: score=36.1D spread=19,999.5 depth25=$10 vol24h=$284.7k url=<site>/scorecards/mu-usdc-perp.html
INTC/USDC PERP: score=37.1D spread=19,993.0 depth25=$10 vol24h=$385.0k url=<site>/scorecards/intc-usdc-perp.html
DELL/USDC PERP: score=43.6D spread=19,998.8 depth25=$5 vol24h=$362.9k url=<site>/scorecards/dell-usdc-perp.html
HOOD/USDC PERP: score=50.5C spread=42.0 depth25=$89 vol24h=$53.7k url=<site>/scorecards/hood-usdc-perp.html
BTC benchmark: spread=5.9 depth25=$322.5k
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
