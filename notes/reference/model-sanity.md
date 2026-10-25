# Model sanity audit

Date: 2026-10-24
Dataset: `runtime/tsa46_full/matrix`
Benchmark: `runtime/tsa46_full/runs/opening_first`

## Species composition

The compiled `feature.Area.og1.*` accounts match the coastal CWH/MH mix. Every
species with area has a nonzero account and a resolved curve. The
runtime-signal gate passes.

## Managed area

- Block area: 2,375,677.18 ha.
- Managed area: 268,970 ha.
- Managed area is preserved by the safe sliver merge.

## Benchmark

- Openings: 5,587.
- Scheduled blocks: 8,383.
- All ten decade targets met at the published 803,000 m3/yr AAC.
- The opening-first schedule fills the 5-40 ha class and covers every managed
  AU.

## Zero-harvest AUs

The opening-first schedule covers every managed AU. There are no zero-harvest
AUs and `config/harvest_coverage.allowlist.json` is empty. The earlier strict
volume-only schedule left small AUs unselected; that result is retained with
the dated VDYP-transform runtime.

## Accuracy validation

- Current TSR height bias -1.50 m, MAE 1.74 m, RMSE 3.01 m against observed immature single-species RESULTS cover heights.
- RESULTS species are not more accurate.
- Volume/DBH/mortality are not yet validated.

## Status

Pass. The compiled runtime signal is complete, the safe merge preserves area and
managed area, and the strict and coverage benchmarks both meet the AAC.
