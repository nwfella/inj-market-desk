# Outreach — Phase 0

Generated 2026-10-26T23:54:05Z from `data/latest.json`. Do not hand-edit; regenerate with
`python build_site.py`.

## The three numbers to lead with

- **182 of 286 Injective perp markets (63.6%)** had no two-sided quote at snapshot time.
- The median quoted market is **79.1 bps wide** (BTC: 10.0 bps).
- **Median two-sided depth inside 25 bps: $10.** The whole venue holds $1.34M within 25 bps.

## Target list — volume is arriving, book is not

| Market | Score | Spread bps | Depth ≤25 bps | 24h volume | Scorecard |
|---|---|---|---|---|---|
| `USDHKD/USDC PERP` | 20 F | — | $0 | $514.2k | [scorecard](docs/scorecards/usdhkd-usdc-perp.html) |
| `SICI/USDC PERP` | 17 F | — | $0 | $302.4k | [scorecard](docs/scorecards/sici-usdc-perp.html) |
| `NZDUSD/USDC PERP` | 15 F | — | $0 | $191.2k | [scorecard](docs/scorecards/nzdusd-usdc-perp.html) |
| `PYPL/USDC PERP` | 30 E | 741.5 | $11 | $52.2k | [scorecard](docs/scorecards/pypl-usdc-perp.html) |
| `CRM/USDC PERP` | 31 E | 740.2 | $10 | $64.2k | [scorecard](docs/scorecards/crm-usdc-perp.html) |
| `STRK/USDC PERP` | 36 D | 169.8 | $5 | $96.5k | [scorecard](docs/scorecards/strk-usdc-perp.html) |
| `XAG/USDC PERP` | 37 D | 19,999.3 | $1 | $351.6k | [scorecard](docs/scorecards/xag-usdc-perp.html) |

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
BTC/USDC PERP: score=92.4A spread=10.0 depth25=$270.8k vol24h=$20.60M url=<site>/scorecards/btc-usdc-perp.html
ETH/USDC PERP: score=90.0A spread=6.0 depth25=$337.2k vol24h=$12.43M url=<site>/scorecards/eth-usdc-perp.html
INJ/USDC PERP: score=87.7A spread=17.4 depth25=$100.7k vol24h=$7.79M url=<site>/scorecards/inj-usdc-perp.html
USDHKD/USDC PERP: score=19.7F spread=— depth25=$0 vol24h=$514.2k url=<site>/scorecards/usdhkd-usdc-perp.html
SICI/USDC PERP: score=17.1F spread=— depth25=$0 vol24h=$302.4k url=<site>/scorecards/sici-usdc-perp.html
NZDUSD/USDC PERP: score=14.8F spread=— depth25=$0 vol24h=$191.2k url=<site>/scorecards/nzdusd-usdc-perp.html
PYPL/USDC PERP: score=30.5E spread=741.5 depth25=$11 vol24h=$52.2k url=<site>/scorecards/pypl-usdc-perp.html
CRM/USDC PERP: score=31.1E spread=740.2 depth25=$10 vol24h=$64.2k url=<site>/scorecards/crm-usdc-perp.html
STRK/USDC PERP: score=36.3D spread=169.8 depth25=$5 vol24h=$96.5k url=<site>/scorecards/strk-usdc-perp.html
XAG/USDC PERP: score=36.8D spread=19,999.3 depth25=$1 vol24h=$351.6k url=<site>/scorecards/xag-usdc-perp.html
BTC benchmark: spread=10.0 depth25=$270.8k
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
