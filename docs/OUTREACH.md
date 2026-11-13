# Outreach — Phase 0

Generated 2026-11-13T16:24:51Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **258 of 309 Injective perp markets (83.5%)** had no two-sided quote at snapshot time.
- The median quoted market is **39.5 bps wide** (BTC: 7.4 bps).
- **Median two-sided depth inside 25 bps: $4.1k.** The whole venue holds $1.10M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 23 E | — | $0 | $1.14M | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 20 E | — | $0 | $601.9k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `AMD/USDC PERP` | 17 F | — | $0 | $286.8k | [scorecard](docs/scorecards/amd-usdc-perp.html) |
| `XAG/USDC PERP` | 32 E | 19,999.2 | $5 | $65.6k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `MU/USDC PERP` | 34 E | 19,999.5 | $10 | $133.7k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `DELL/USDC PERP` | 34 E | 19,998.8 | $10 | $126.2k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `INTC/USDC PERP` | 34 E | 19,993.1 | $10 | $152.9k | [scorecard](docs/scorecards/intc-usdc-perp.html) |

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
BTC/USDC PERP: score=95.2A spread=7.4 depth25=$319.4k vol24h=$7.44M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=88.3A spread=14.5 depth25=$232.9k vol24h=$5.40M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.4A spread=19.7 depth25=$100.2k vol24h=$3.35M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=23.1E spread=— depth25=$0 vol24h=$1.14M url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=20.5E spread=— depth25=$0 vol24h=$601.9k url=<site>/scorecards/sici-usdc-perp.html
AMD/USDC PERP: score=16.8F spread=— depth25=$0 vol24h=$286.8k url=<site>/scorecards/amd-usdc-perp.html
XAG/USDC PERP: score=32.2E spread=19,999.2 depth25=$5 vol24h=$65.6k url=<site>/scorecards/xag-usdc-perp.html
MU/USDC PERP: score=33.7E spread=19,999.5 depth25=$10 vol24h=$133.7k url=<site>/scorecards/mu-usdc-perp.html
DELL/USDC PERP: score=33.7E spread=19,998.8 depth25=$10 vol24h=$126.2k url=<site>/scorecards/dell-usdc-perp.html
INTC/USDC PERP: score=34.1E spread=19,993.1 depth25=$10 vol24h=$152.9k url=<site>/scorecards/intc-usdc-perp.html
BTC benchmark: spread=7.4 depth25=$319.4k
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
