# Model sanity audit

Date: 2026-10-23
Dataset: `runtime/tsa46_full/matrix`
Benchmark: `runtime/tsa46_full/runs/aac_benchmark`

## Species composition

Initial `feature.Area.og1.*` area by species:

| Species | Area (ha) | Share |
| --- | ---: | ---: |
| CWH_CW | 579,570.3 | 35.3% |
| CWH_HW | 489,493.4 | 29.8% |
| CWH_H | 244,714.7 | 14.9% |
| MH_H | 145,864.2 | 8.9% |
| CWH_YC | 110,608.7 | 6.7% |
| CWH_BA | 41,870.5 | 2.5% |
| CWH_FDC | 31,215.5 | 1.9% |

The mix is coastal CWH/MH, consistent with the GBR North inventory. The
compiled species areas sum to the og1 area, and every species has a nonzero
area account.

## Managed area

- Block area: 2,375,677.18 ha.
- Managed area: 268,970.00 ha (11.3% of block area).
- Managed share of og1 area: 16.4%.

## Benchmark

- Unique blocks harvested: 2,792.
- Harvested area: 117,736.7 ha over 100 years (44% of the managed area).
- Events: 3,885 across offsets 0-99.
- All ten decade targets met at 8,030,000-8,031,000 m3.

## Finding: zero-harvest AUs

Three AUs have managed area but no benchmark harvest:

| AU | Managed area (ha) | Total area (ha) |
| --- | ---: | ---: |
| 4601004 | 417.5 | 75,182.3 |
| 4602003 | 1,862.5 | 42,747.1 |
| 4601005 | 204.0 | 27,405.9 |

Total managed area with no harvest: **2,483.9 ha (0.92% of the managed area)**.

The benchmark is volume-feasible without these AUs. The zero signal is recorded
as a known limitation, not a build failure. A follow-up should either schedule
a minimum share of these AUs or document why they are economically or
operationally excluded.

## Coverage run

`runtime/tsa46_full/runs/aac_benchmark_coverage/` is a coverage diagnostic, not
the benchmark of record. It starts from the strict benchmark and adds one
harvest event for each of the three AUs above, then re-optimizes.

- All three AUs are covered: 4601004 (41.1 ha), 4602003 (128.8 ha), 4601005
  (15.3 ha).
- Nine decades meet the strict band.
- Decade 4 is 371 m3 above the upper bound and decade 10 is 7.7 m3 above.
- The objective is 378.63; the strict `aac_benchmark` remains 10/10 met.

The small overage is a real trade-off, not a reason to widen the band. The
strict benchmark stays the benchmark of record; the coverage run answers the
AU-coverage question separately.

## Status

Pass with a recorded limitation. The compiled runtime signal is complete. The
strict benchmark leaves three small AUs unselected; the coverage run selects
them and records the 371 m3 decade-4 overage.
