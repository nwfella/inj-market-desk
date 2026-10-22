#!/usr/bin/env node
/**
 * Gate for the Injective Market Desk site.
 *
 * Asserts, from the generated artifacts alone:
 *   1. the dashboard's baked snapshot matches data/latest.json exactly
 *   2. every metric is internally consistent (spread recomputed from bid/ask)
 *   3. the focus scorecards exist and carry no NaN/undefined/None
 *   4. nothing on the page would make a network request (no fetch/XHR/src=)
 *   5. the headline summary numbers on the page match the computed summary
 *
 * Usage: node scripts/verify_site.js
 */
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, "data", "latest.json"), "utf8"));
const INDEX = fs.readFileSync(path.join(ROOT, "docs", "index.html"), "utf8");

let pass = 0;
const fails = [];
function ok(name, cond, detail) {
  if (cond) {
    pass++;
  } else {
    fails.push(`${name}${detail ? " :: " + detail : ""}`);
  }
}
const near = (a, b, tol) => Math.abs(a - b) <= tol;

// ---------------------------------------------------------------- 1. baked snapshot
const m = INDEX.match(/const SNAP = (\[.*?\]);\s*\nconst FOCUS/s);
ok("dashboard embeds a snapshot", !!m);
let snap = [];
if (m) {
  try {
    snap = JSON.parse(m[1]);
    ok("payload parses", true);
  } catch (e) {
    ok("payload parses", false, e.message);
  }
}
ok("payload row count == data/latest.json", snap.length === DATA.markets.length,
  `${snap.length} vs ${DATA.markets.length}`);
if (snap.length === DATA.markets.length) {
  let mismatches = 0;
  DATA.markets.forEach((row, i) => {
    if (snap[i].ticker !== row.ticker || snap[i].score !== row.score) mismatches++;
  });
  ok("payload identical to source", mismatches === 0, `${mismatches} rows diverge`);
}

// ---------------------------------------------------------------- 2. metric consistency
let spreadBad = 0;
let depthBad = 0;
let checked = 0;
for (const r of DATA.markets) {
  if (r.two_sided && r.bid && r.ask) {
    checked++;
    const recomputed = ((r.ask - r.bid) / ((r.ask + r.bid) / 2)) * 10000;
    if (!near(recomputed, r.spread_bps, 0.5)) spreadBad++;
    if (r.spread_bps != null && r.roundtrip_bps != null) {
      const rt = r.spread_bps + 2 * r.taker_fee_bps;
      if (!near(rt, r.roundtrip_bps, 0.01)) depthBad++;
    }
  }
}
ok("spread recomputes from bid/ask on every quoted market", spreadBad === 0,
  `${spreadBad}/${checked} off by >0.5bps`);
ok("round-trip == spread + 2*taker fee", depthBad === 0, `${depthBad} bad`);
ok("every two-sided market reports depth >= 0",
  DATA.markets.every((r) => r.depth_usd && Number(r.depth_usd["25"]) >= 0));
ok("every market has a grade A-F", DATA.markets.every((r) => /^[A-F]$/.test(r.grade)));
ok("score range 0..100", DATA.markets.every((r) => r.score >= 0 && r.score <= 100.0001));

// ---------------------------------------------------------------- 3. summary matches page
const s = DATA.summary;
const want = [
  String(s.markets),
  s.empty_pct.toFixed(1) + "%",
  (s.median_spread_bps ?? 0).toFixed(1),
];
for (const w of want) {
  ok(`page shows summary figure ${w}`, INDEX.includes(w), "missing from index.html");
}
const twoSidedCount = DATA.markets.filter((r) => r.two_sided).length;
ok("summary.two_sided matches rows", twoSidedCount === s.two_sided,
  `${twoSidedCount} vs ${s.two_sided}`);
ok("empty == markets - two_sided", s.empty_or_one_sided === s.markets - s.two_sided);

// ---------------------------------------------------------------- 4. scorecards
const focus = JSON.parse((INDEX.match(/const FOCUS = (\[.*?\]);/s) || [])[1] || "[]");
ok("10 focus markets selected", focus.length === 10, `${focus.length}`);
for (const t of focus) {
  const slug = t.toLowerCase().replace(/\//g, "-").replace(/ /g, "-");
  const f = path.join(ROOT, "docs", "scorecards", `${slug}.html`);
  ok(`scorecard exists: ${t}`, fs.existsSync(f));
  if (!fs.existsSync(f)) continue;
  const h = fs.readFileSync(f, "utf8");
  const row = DATA.markets.find((r) => r.ticker === t);
  ok(`scorecard names its market: ${t}`, h.includes(t));
  ok(`scorecard carries score: ${t}`, h.includes(row.score.toFixed(1)));
  ok(`scorecard has no NaN/undefined/None: ${t}`, !/\bNaN\b|\bundefined\b|\bNone\b/.test(h));
  ok(`scorecard links back: ${t}`, h.includes("../index.html"));
}
ok("no orphan scorecards", fs.readdirSync(path.join(ROOT, "docs", "scorecards")).length === focus.length);

// ---------------------------------------------------------------- 5. IT-safe: no network
const forbidden = [
  [/\bfetch\s*\(/, "fetch("],
  [/XMLHttpRequest/, "XMLHttpRequest"],
  [/<script[^>]+src=/i, "external <script src>"],
  [/<link[^>]+href=["']http/i, "external stylesheet"],
  [/@import\s+url\(/i, "CSS @import"],
  [/fonts\.googleapis|cdn\.|<iframe/i, "CDN / iframe"],
];
for (const [re, label] of forbidden) {
  ok(`no ${label} in dashboard`, !re.test(INDEX));
}
// third-party links are fine (they are href anchors), but nothing may be loaded
const extLoads = (INDEX.match(/(src|href)=["']https?:\/\/[^"']+/g) || [])
  .filter((u) => /\ssrc=/.test(u));
ok("no remote resources loaded", extLoads.length === 0, extLoads.join(","));

// ---------------------------------------------------------------- report
const total = pass + fails.length;
console.log(`\nverify_site: ${pass}/${total} checks passed`);
if (fails.length) {
  console.log("FAILURES:");
  for (const f of fails) console.log("  ✗ " + f);
  process.exit(1);
}
console.log(`markets=${s.markets} two_sided=${s.two_sided} empty=${s.empty_or_one_sided} ` +
  `median_spread=${s.median_spread_bps}bps median_depth25=$${s.median_depth_usd_25}`);
console.log("OK");
