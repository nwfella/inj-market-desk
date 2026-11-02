# Outreach — Phase 0

Generated 2026-11-02T23:30:35Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **218 of 298 Injective perp markets (73.2%)** had no two-sided quote at snapshot time.
- The median quoted market is **74.2 bps wide** (BTC: 9.0 bps).
- **Median two-sided depth inside 25 bps: $105.** The whole venue holds $1.18M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `SICI/USDC PERP` | 20 F | — | $0 | $505.3k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `USDSEK/USDC PERP` | 19 F | — | $0 | $411.8k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `XAG/USDC PERP` | 16 F | — | $0 | $218.8k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `ETC/USDC PERP` | 34 E | 719.8 | $10 | $113.7k | [scorecard](docs/scorecards/etc-usdc-perp.html) |
| `ETHFI/USDC PERP` | 38 D | 142.4 | $5 | $50.1k | [scorecard](docs/scorecards/ethfi-usdc-perp.html) |
| `AERO/USDC PERP` | 40 D | 128.3 | $5 | $62.7k | [scorecard](docs/scorecards/aero-usdc-perp.html) |
| `V/USDC PERP` | 41 D | 740.2 | $10 | $66.4k | [scorecard](docs/scorecards/v-usdc-perp.html) |

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
BTC/USDC PERP: score=88.1A spread=9.0 depth25=$270.7k vol24h=$17.71M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=85.9A spread=11.6 depth25=$200.7k vol24h=$13.18M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=90.8A spread=1.4 depth25=$79.9k vol24h=$7.22M url=<site>/scorecards/inj-usdc-perp.html
SICI/USDC PERP: score=19.7F spread=— depth25=$0 vol24h=$505.3k url=<site>/scorecards/sici-usdc-perp.html
USDSEK/USDC PERP: score=18.6F spread=— depth25=$0 vol24h=$411.8k url=<site>/scorecards/usdsek-usdc-perp.html
XAG/USDC PERP: score=15.5F spread=— depth25=$0 vol24h=$218.8k url=<site>/scorecards/xag-usdc-perp.html
ETC/USDC PERP: score=33.9E spread=719.8 depth25=$10 vol24h=$113.7k url=<site>/scorecards/etc-usdc-perp.html
ETHFI/USDC PERP: score=37.6D spread=142.4 depth25=$5 vol24h=$50.1k url=<site>/scorecards/ethfi-usdc-perp.html
AERO/USDC PERP: score=40.1D spread=128.3 depth25=$5 vol24h=$62.7k url=<site>/scorecards/aero-usdc-perp.html
V/USDC PERP: score=41.1D spread=740.2 depth25=$10 vol24h=$66.4k url=<site>/scorecards/v-usdc-perp.html
BTC benchmark: spread=9.0 depth25=$270.7k
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
