# Model sanity audit

Date: 2026-10-24
Dataset: `runtime/tsa46_full/matrix`
Benchmark: `runtime/tsa46_full/runs/aac_benchmark`

## Species composition

The compiled `feature.Area.og1.*` accounts match the coastal CWH/MH mix. Every
species with area has a nonzero account and a resolved curve. The
runtime-signal gate passes.

## Managed area

- Block area: 2,375,677.18 ha.
- Managed area: 268,970 ha.
- Managed area is preserved by the safe sliver merge.

## Benchmark

- Unique blocks harvested: 2,792.
- Events: 3,890.
- All ten decade targets met at the published AAC.
- Coverage run: 2,920 blocks, 4,025 events, ten decades
  met.

## Zero-harvest AUs

The strict volume-only benchmark leaves these managed AUs unselected:

- 4601002 (718.2 ha), 4601005 (204.0 ha), 4601006 (413.1 ha)

They are allowlisted in `config/harvest_coverage.allowlist.json` with the reason
that the coverage run harvests them. The coverage gate passes on the coverage
run with no allowlist.

## Status

Pass. The compiled runtime signal is complete, the safe merge preserves area and
managed area, and the strict and coverage benchmarks both meet the AAC.
