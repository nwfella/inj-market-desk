# Injective Market Desk

Measures the live order book of **every perpetual market on Injective** and publishes the result as a
static dashboard plus one print-ready scorecard per focus market.

Not a volume chart. A market's volume tells you people traded; it does not tell you whether anyone is
quoting *now*. This project reads the book itself and reports:

- **no two-sided quote** — the market cannot be traded at any size, whatever its 24h volume
- **spread** — live touch, in bps
- **depth** — notional resting within 25 / 100 / 500 bps of the touch, thinner side
- **book concentration (HHI)** — one level holding 80% of notional is a placeholder, not liquidity
- **volume-to-depth gap** — volume arriving without a book to absorb it
- **health score 0–100, grades A–F** — documented formula, renormalised when an input is missing

Headline from the first run (2026-10-22): **176 of 286 markets (61.5%) had no two-sided quote**, the
median quoted market was **65 bps wide** (BTC: 8.7 bps), and **median two-sided depth inside 25 bps was
$10** — for the whole venue, $1.5M of resting size inside 25 bps.

## Run it

Stdlib Python 3.9+ only. No keys, no packages, no accounts.

```bash
python engine/injdesk.py sweep        # 286 markets, ~40s, writes data/latest.json
python engine/injdesk.py table -n 20  # worst 20
python engine/injdesk.py check "BTC/USDC PERP"
python build_site.py                  # -> docs/index.html + docs/scorecards/*.html + OUTREACH.md
node scripts/verify_site.js           # 73-check gate
```

Refresh hourly with the included GitHub Action (`.github/workflows/refresh.yml`), or any cron:

```
17 * * * * cd /path/to/inj-market-desk && python engine/injdesk.py sweep && python build_site.py
```

## Data sources

| What | Where | Cost |
|---|---|---|
| Order books + market metadata | `sentry.lcd.injective.network` (public LCD, keyless) | $0 |
| 24h volume per market | CoinGecko `injective_futures` tickers (third-party) | $0, cached 30 min |
| Hosting | GitHub Pages, static | $0 |

Prices from the derivative book are chain-scaled; the engine divides by `1e6`, verified against spot at
snapshot time (BTC mid 81,291 vs spot 81,262 — a 3.5 bp difference, i.e. the basis).

## Scoring

Weights: two-sided quote 25 · spread 25 · depth ≤25 bps 25 · 24h volume 15 · book balance 10.
Sub-scores: spread 2 bps → 1.0, 200 bps → 0; depth $1k → 0, $1M → 1.0; volume $10k → 0, $1M → 1.0
(log). Missing inputs are dropped and the remaining weights renormalise. **A market with no two-sided
quote is capped at 25** so a busy-but-unquoted market can never grade above E.

## Known gaps (Phase 1)

- **Funding rate, open interest, maker identity** — not exposed by the LCD gateway (it answers
  `501 Not Implemented` for `funding_rates` and `positions`). These live on the indexer's gRPC-web
  surface: `sentry.exchange.grpc-web.injective.network`. Roughly 6h of work.
- **History** — the site ships one snapshot. Each cron run appends to `data/history/`, so a trend
  column is a small addition once a few days exist.
- **Volume** is third-party and 24h-aggregated; it is not derived from this project's own trades.

## Honesty rules baked into the code

- An empty book is reported as empty, never as a low score with a caveat.
- Depth is measured from the touch, not from mid — measuring from mid would score a 60 bps-wide market
  as zero-depth, which is misleading.
- No claim of manipulation anywhere. Wash-trade and concentration metrics are reported as HHI numbers,
  not as accusations.
- Every page carries the snapshot timestamp and the caveat that spreads move.

## Deploy

```bash
git push origin main          # Pages serves /docs
gh api repos/<owner>/inj-market-desk/pages -X POST --input - <<'EOF'
{"source":{"branch":"main","path":"/docs"}}
EOF
```

MIT.
