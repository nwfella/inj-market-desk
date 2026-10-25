# Outreach — Phase 0

Generated 2026-10-25T11:30:05Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **184 of 286 Injective perp markets (64.3%)** had no two-sided quote at snapshot time.
- The median quoted market is **84.9 bps wide** (BTC: 9.9 bps).
- **Median two-sided depth inside 25 bps: $10.** The whole venue holds $1.42M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDSEK/USDC PERP` | 19 F | — | $0 | $451.4k | [scorecard](docs/scorecards/usdsek-usdc-perp.html) |
| `UNI/USDC PERP` | 17 F | — | $0 | $309.6k | [scorecard](docs/scorecards/uni-usdc-perp.html) |
| `STX/USDC PERP` | 17 F | — | $0 | $283.3k | [scorecard](docs/scorecards/stx-usdc-perp.html) |
| `DASH/USDC PERP` | 33 E | 190.7 | $5 | $73.1k | [scorecard](docs/scorecards/dash-usdc-perp.html) |
| `DELL/USDC PERP` | 36 D | 180.4 | $1 | $71.1k | [scorecard](docs/scorecards/dell-usdc-perp.html) |
| `XAG/USDC PERP` | 37 D | 19,999.3 | $1 | $344.3k | [scorecard](docs/scorecards/xag-usdc-perp.html) |
| `KAS/USDC PERP` | 37 D | 3,361.8 | $10 | $148.4k | [scorecard](docs/scorecards/kas-usdc-perp.html) |

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
BTC/USDC PERP: score=93.7A spread=9.9 depth25=$293.7k vol24h=$13.13M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=89.6A spread=9.4 depth25=$340.6k vol24h=$5.69M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=81.1A spread=9.3 depth25=$30.9k vol24h=$7.57M url=<site>/scorecards/inj-usdc-perp.html
USDSEK/USDC PERP: score=19.1F spread=— depth25=$0 vol24h=$451.4k url=<site>/scorecards/usdsek-usdc-perp.html
UNI/USDC PERP: score=17.2F spread=— depth25=$0 vol24h=$309.6k url=<site>/scorecards/uni-usdc-perp.html
STX/USDC PERP: score=16.8F spread=— depth25=$0 vol24h=$283.3k url=<site>/scorecards/stx-usdc-perp.html
DASH/USDC PERP: score=32.9E spread=190.7 depth25=$5 vol24h=$73.1k url=<site>/scorecards/dash-usdc-perp.html
DELL/USDC PERP: score=36.3D spread=180.4 depth25=$1 vol24h=$71.1k url=<site>/scorecards/dell-usdc-perp.html
XAG/USDC PERP: score=36.8D spread=19,999.3 depth25=$1 vol24h=$344.3k url=<site>/scorecards/xag-usdc-perp.html
KAS/USDC PERP: score=37.0D spread=3,361.8 depth25=$10 vol24h=$148.4k url=<site>/scorecards/kas-usdc-perp.html
BTC benchmark: spread=9.9 depth25=$293.7k
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
