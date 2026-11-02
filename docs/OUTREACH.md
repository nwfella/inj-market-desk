# Outreach — Phase 0

Generated 2026-11-02T06:03:08Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **222 of 286 Injective perp markets (77.6%)** had no two-sided quote at snapshot time.
- The median quoted market is **59.5 bps wide** (BTC: 9.1 bps).
- **Median two-sided depth inside 25 bps: $509.** The whole venue holds $1.12M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 E | — | $0 | $538.5k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDHKD/USDC PERP` | 20 F | — | $0 | $492.5k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `XAU/USDC PERP` | 18 F | — | $0 | $330.4k | [scorecard](docs/scorecards/xau-usdc-perp.html) |
| `MU/USDC PERP` | 38 D | 19,999.6 | $2 | $222.3k | [scorecard](docs/scorecards/mu-usdc-perp.html) |
| `XAG/USDC PERP` | 44 D | 137.4 | $5 | $265.6k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `ORCL/USDC PERP` | 45 D | 739.8 | $10 | $190.5k | [scorecard](docs/scorecards/orcl-usdc-perp.html) |
| `CRCL/USDC PERP` | 49 D | 66.2 | $1.1k | $74.0k | [scorecard](docs/scorecards/crcl-usdc-perp.html) |

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
BTC/USDC PERP: score=92.2A spread=9.1 depth25=$270.8k vol24h=$16.58M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=90.9A spread=14.0 depth25=$200.7k vol24h=$12.47M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=89.5A spread=12.5 depth25=$79.9k vol24h=$7.54M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=20.0E spread=— depth25=$0 vol24h=$538.5k url=<site>/scorecards/sici-usdc-perp.html
USDHKD/USDC PERP: score=19.5F spread=— depth25=$0 vol24h=$492.5k url=<site>/scorecards/usdhkd-usdc-perp.html
XAU/USDC PERP: score=17.5F spread=— depth25=$0 vol24h=$330.4k url=<site>/scorecards/xau-usdc-perp.html
MU/USDC PERP: score=38.2D spread=19,999.6 depth25=$2 vol24h=$222.3k url=<site>/scorecards/mu-usdc-perp.html
XAG/USDC PERP: score=43.6D spread=137.4 depth25=$5 vol24h=$265.6k url=<site>/scorecards/xag-usdc-perp.html
ORCL/USDC PERP: score=44.6D spread=739.8 depth25=$10 vol24h=$190.5k url=<site>/scorecards/orcl-usdc-perp.html
CRCL/USDC PERP: score=49.4D spread=66.2 depth25=$1.1k vol24h=$74.0k url=<site>/scorecards/crcl-usdc-perp.html
BTC benchmark: spread=9.1 depth25=$270.8k
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
