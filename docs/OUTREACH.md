# Outreach — Phase 0

Generated 2026-11-23T09:06:11Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **260 of 307 Injective perp markets (84.7%)** had no two-sided quote at snapshot time.
- The median quoted market is **49.4 bps wide** (BTC: 4.2 bps).
- **Median two-sided depth inside 25 bps: $7.7k.** The whole venue holds $1.30M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 E | — | $0 | $554.5k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `PEP/USDC PERP` | 16 F | — | $0 | $249.9k | [scorecard](docs/scorecards/pep-usdc-perp.html) |
| `BKNG/USDC PERP` | 15 F | — | $0 | $186.7k | [scorecard](docs/scorecards/bkng-usdc-perp.html) |
| `GRAM/USDC PERP` | 53 C | 24.0 | $50 | $50.9k | [scorecard](docs/scorecards/gram-usdc-perp.html) |
| `ZRO/USDC PERP` | 56 C | 73.3 | $5.3k | $84.4k | [scorecard](docs/scorecards/zro-usdc-perp.html) |
| `ARB/USDC PERP` | 57 C | 31.3 | $1.1k | $84.3k | [scorecard](docs/scorecards/arb-usdc-perp.html) |
| `JUP/USDC PERP` | 58 C | 18.9 | $19 | $77.0k | [scorecard](docs/scorecards/jup-usdc-perp.html) |

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
BTC/USDC PERP: score=94.9A spread=4.2 depth25=$311.5k vol24h=$922.1k url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=92.1A spread=12.8 depth25=$319.6k vol24h=$533.3k url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=83.9A spread=38.1 depth25=$102.2k vol24h=$360.3k url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=20.1E spread=— depth25=$0 vol24h=$554.5k url=<site>/scorecards/usdhkd-usdc-perp.html
PEP/USDC PERP: score=16.1F spread=— depth25=$0 vol24h=$249.9k url=<site>/scorecards/pep-usdc-perp.html
BKNG/USDC PERP: score=14.7F spread=— depth25=$0 vol24h=$186.7k url=<site>/scorecards/bkng-usdc-perp.html
GRAM/USDC PERP: score=52.6C spread=24.0 depth25=$50 vol24h=$50.9k url=<site>/scorecards/gram-usdc-perp.html
ZRO/USDC PERP: score=56.3C spread=73.3 depth25=$5.3k vol24h=$84.4k url=<site>/scorecards/zro-usdc-perp.html
ARB/USDC PERP: score=57.1C spread=31.3 depth25=$1.1k vol24h=$84.3k url=<site>/scorecards/arb-usdc-perp.html
JUP/USDC PERP: score=57.7C spread=18.9 depth25=$19 vol24h=$77.0k url=<site>/scorecards/jup-usdc-perp.html
BTC benchmark: spread=4.2 depth25=$311.5k
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
