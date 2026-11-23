# Outreach — Phase 0

Generated 2026-11-23T00:53:53Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **258 of 307 Injective perp markets (84.0%)** had no two-sided quote at snapshot time.
- The median quoted market is **50.8 bps wide** (BTC: 2.3 bps).
- **Median two-sided depth inside 25 bps: $5.4k.** The whole venue holds $1.22M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.4k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `NEAR/USDC PERP` | 17 F | — | $0 | $297.1k | [scorecard](docs/scorecards/near-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `NVDA/USDC PERP` | 32 E | 354.3 | $1.2k | $62.9k | [scorecard](docs/scorecards/nvda-usdc-perp.html) |
| `TAIKO/USDC PERP` | 47 D | 71.0 | $18 | $53.8k | [scorecard](docs/scorecards/taiko-usdc-perp.html) |
| `POPCAT/USDC PERP` | 52 C | 49.3 | $70 | $50.9k | [scorecard](docs/scorecards/popcat-usdc-perp.html) |
| `ZRO/USDC PERP` | 52 C | 39.8 | $591 | $83.8k | [scorecard](docs/scorecards/zro-usdc-perp.html) |

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
BTC/USDC PERP: score=94.2A spread=2.3 depth25=$320.5k vol24h=$666.5k url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=89.6A spread=5.2 depth25=$200.7k vol24h=$376.2k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=84.3A spread=35.6 depth25=$104.6k vol24h=$368.3k url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.4k url=<site>/scorecards/usdhkd-usdc-perp.html
NEAR/USDC PERP: score=17.0F spread=— depth25=$0 vol24h=$297.1k url=<site>/scorecards/near-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
NVDA/USDC PERP: score=32.5E spread=354.3 depth25=$1.2k vol24h=$62.9k url=<site>/scorecards/nvda-usdc-perp.html
TAIKO/USDC PERP: score=47.4D spread=71.0 depth25=$18 vol24h=$53.8k url=<site>/scorecards/taiko-usdc-perp.html
POPCAT/USDC PERP: score=51.5C spread=49.3 depth25=$70 vol24h=$50.9k url=<site>/scorecards/popcat-usdc-perp.html
ZRO/USDC PERP: score=52.5C spread=39.8 depth25=$591 vol24h=$83.8k url=<site>/scorecards/zro-usdc-perp.html
BTC benchmark: spread=2.3 depth25=$320.5k
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
