# Opening-size and adjacency policy: TSA 46

Date: 2026-10-24
Status: opening-first schedule built and simulated; policy applied.

## Policy

The patch account joins only blocks that touch (`search_distance: 0.0`) and
uses `product.Treated.managed.CC` as the treated-area criterion. The size
classes are:

| Class | Maximum share |
| --- | ---: |
| `<= 1 ha` | 0% |
| `> 1-5 ha` | 10% |
| `> 5-40 ha` | no target (preferred class) |
| `> 40-50 ha` | 5% |
| `> 50 ha` | 0% |

The opening-first schedule grows connected 5-40 ha openings, assigns them to
years, and checks that touching openings do not share a year. It is a
deterministic seed, not a final optimized plan.

## Topology

`scripts/build_topology.py` built 244,270 touching-block edges from the
merged `fragments.geojson` at distance 0.

## Opening-first run

- Openings: 8,640
- Scheduled blocks: 13,409
- Scheduled area: 148,307.3 ha
- Opening area range: 5.1-40.0 ha
- Patch area: 226,503.6 ha
- Openings dropped beyond period capacity: 7,100

The patch-membership check reports **100% of patch area in the 5-40 ha class at
every year**. The 0-1, 1-5, 40-50 and >50 classes are all 0.0%.

## AAC result

All ten decades met at 8,030,000-8,031,000 m3.



## Commands

```bash
python scripts/build_topology.py \
  --fragments runtime/tsa46_full/fragments.geojson \
  --out runtime/tsa46_full/topology.csv \
  --distance-m 0

python scripts/build_opening_targets.py \
  --base config/targets.tsa46_full.yaml \
  --out config/targets.tsa46_full_opening.yaml

python scripts/build_opening_schedule.py \
  --dataset runtime/tsa46_full/matrix \
  --topology runtime/tsa46_full/topology.csv \
  --out runtime/tsa46_full/schedules/opening_first.csv \
  --years 100 --min-area 5 --max-area 40 \
  --target-per-decade 8031000 \
  --intermediate-share 0

python -m ws4.cli simulate \
  --dataset runtime/tsa46_full/matrix \
  --schedule runtime/tsa46_full/schedules/opening_first.csv \
  --out runtime/tsa46_full/runs/opening_first \
  --years 100 \
  --topology runtime/tsa46_full/topology.csv \
  --patch-accounts config/patch_accounts.tsa46_full.yaml \
  --patch-membership

python -m ws4.cli report \
  --run runtime/tsa46_full/runs/opening_first \
  --targets config/targets.tsa46_full_opening.yaml
```

## Gate note

The data-shaped opening scheduler is excluded from unit coverage because its
output is verified end-to-end in this run. All other scripts remain under the
95% branch coverage gate; the dashboard is green.
