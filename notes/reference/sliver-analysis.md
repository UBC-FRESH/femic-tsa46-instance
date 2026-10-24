# Sliver and small-fragment analysis: TSA 46

Date: 2026-10-24
Dataset: `runtime/tsa46_full/matrix`
Source geometry: `output/patchworks_tsa46_full/fragments/fragments.shp`

## Headline

- **Block-level small polygons are a modest problem.** 5,980 blocks
  are below 1 ha (3.5% of blocks, 3,612.7 ha,
  0.15% of area).
- **Fragment-level small fragments are a larger problem.** 9,543
  fragments are below 1 ha (5.0% of fragments,
  6,233.7 ha, 0.26% of area).
- **Most of the extra small fragments are not VRI slivers.** 3,575
  small fragments sit in multi-fragment blocks, and **100% of them carry
  RETENTION > 0**. They are the unmanaged/retention remainder of the IFM
  proportional split. Merging them would erase the retention signal.
- A blanket <1 ha merge would change the AU/species of 37.6% of
  the moved area and the IFM state of 9.5%. That is not a safe
  cleanup.

## Block-level size distribution

| Bin (ha) | Blocks | Share of blocks | Area (ha) | Share of area |
| --- | ---: | ---: | ---: | ---: |
| 0-0.1 | 245 | 0.1% | 12.2 | 0.00% |
| 0.1-0.25 | 469 | 0.3% | 85.5 | 0.00% |
| 0.25-0.5 | 1,130 | 0.7% | 428.3 | 0.02% |
| 0.5-0.75 | 2,099 | 1.2% | 1,306.1 | 0.05% |
| 0.75-1 | 2,037 | 1.2% | 1,780.6 | 0.07% |
| 1-1.25 | 3,854 | 2.2% | 4,323.7 | 0.18% |
| 1.25-1.5 | 3,400 | 2.0% | 4,657.6 | 0.20% |
| 1.5-2 | 6,244 | 3.6% | 10,895.9 | 0.46% |
| 2-5 | 33,306 | 19.4% | 115,276.7 | 4.85% |
| 5-10 | 42,559 | 24.8% | 311,864.7 | 13.13% |
| 10-20 | 43,102 | 25.1% | 612,220.6 | 25.77% |
| 20-50 | 28,123 | 16.4% | 833,263.5 | 35.07% |
| 50-1e+07 | 5,257 | 3.1% | 479,561.7 | 20.19% |

The block-level mode is **0.56-0.58 ha (205 blocks)**, not a low-end spike. The
distribution rises toward 1 ha and then jumps across the VRI minimum-mapping
edge.

## Fragment-level size distribution

The low-end fragment mode is **0.98-1.0 ha (442 fragments)**. The exact edge at 1 ha is
sharp: **0.98-1.0 ha: 442; 1.0-1.02 ha: 587**. That is a genuine cutoff flip point: 1.0 ha is the VRI
minimum-mapping-unit edge, and the population just above it is larger than the
population just below it.

| Bin (ha) | Fragments | Share of fragments | Area (ha) | Share of area |
| --- | ---: | ---: | ---: | ---: |
| 0-0.1 | 293 | 0.2% | 14.9 | 0.00% |
| 0.1-0.25 | 559 | 0.3% | 101.4 | 0.00% |
| 0.25-0.5 | 1,511 | 0.8% | 579.3 | 0.02% |
| 0.5-0.75 | 3,168 | 1.7% | 1,988.3 | 0.08% |
| 0.75-1 | 4,012 | 2.1% | 3,549.8 | 0.15% |
| 1-1.25 | 6,080 | 3.2% | 6,766.1 | 0.28% |
| 1.25-1.5 | 4,129 | 2.2% | 5,655.2 | 0.24% |
| 1.5-2 | 8,052 | 4.2% | 14,109.4 | 0.59% |
| 2-5 | 40,148 | 21.1% | 137,303.0 | 5.78% |
| 5-10 | 46,434 | 24.4% | 338,713.3 | 14.26% |
| 10-20 | 44,002 | 23.1% | 622,908.5 | 26.22% |
| 20-50 | 27,066 | 14.2% | 798,281.3 | 33.60% |
| 50-1e+07 | 4,854 | 2.6% | 445,706.6 | 18.76% |

## Threshold table

| Cutoff | Blocks below | Block area (ha) | Fragments below | Fragment area (ha) |
| --- | ---: | ---: | ---: | ---: |
| <0.1 ha | 245 | 12.2 | 293 | 14.9 |
| <0.25 ha | 714 | 97.7 | 852 | 116.4 |
| <0.5 ha | 1,844 | 526.0 | 2,363 | 695.7 |
| <0.75 ha | 3,943 | 1,832.1 | 5,531 | 2,683.9 |
| <1 ha | 5,980 | 3,612.7 | 9,543 | 6,233.7 |

## What is in the small fragments?

| Attribute | Finding |
| --- | --- |
| RETENTION > 0 | **100%** of small fragments in multi-fragment blocks; 42.2% of all small-fragment area |
| Managed (THLB) | 113.5 ha (3.1%) |
| Old growth (>250 years) | 43.5% of small-block area |
| Species unique to small fragments | None; every species also occurs above 1 ha |
| AU/species unique in block | Blocks are AU-specific, so a small block is the block's AU by construction |
| No touching neighbour | 1,215 blocks, 761.5 ha |

The retention result is the important one. These are not stray VRI polygons.
They are the unmanaged remainder created when the IFM proportional split assigns
a share of a stand to retention. They carry model semantics.

## Merge simulation

For each small block, the analysis found touching neighbours and selected the
neighbour with the longest shared boundary. The "safe" merge requires the same
AU, same IFM, same origin, age difference at most 20 years, and a neighbour with
RETENTION = 0.

| Measure | Value |
| --- | ---: |
| Small blocks | 5,980 |
| With a touching neighbour | 4,765 (78.9% of area) |
| Same AU + IFM | 2,794 (1,678.4 ha, 58.9% of merged area) |
| Different AU | 1,070.7 ha (37.6%) |
| Different IFM | 272.1 ha (9.5%) |
| Same age | 61.1% of merged area |
| Mean age difference | 33.4 years |
| No touching neighbour | 1,215 blocks (761.5 ha) |

Safe merge candidates:

| Cutoff | Safe blocks | Safe area (ha) | Block reduction | Fragment reduction |
| --- | ---: | ---: | ---: | ---: |
| <0.25 ha | 325 | 43.4 | 0.19% | 0.17% |
| <0.5 ha | 740 | 197.9 | 0.43% | 0.39% |
| <1.0 ha | 2,486 | 1,488.5 | 1.45% | 1.3% |

An aggressive merge of every small block with a touching neighbour would remove
4,765 blocks (2.8% of blocks)
and 4,765 fragments
(2.5% of fragments), but it would relabel
37.6% of the moved area to a different AU/species and
9.5% to a different IFM state. That is not recommended.

## Recommendation

1. **Do not use a blanket <1 ha merge.** The 1.0 ha edge is real, but it is the
   VRI minimum-mapping edge, not a sliver-only edge. A blanket cutoff would
   remove legitimate small stands and retention fragments.
2. **Use a two-threshold policy.**
   - **0.25 ha**: mandatory geometric sliver cleanup. Merge only into a
     touching neighbour with the same AU, IFM, origin, and similar age. This
     removes 325/131 blocks and 43.4/17.9 ha.
   - **0.5 ha**: upper bound for the same safe merge. This removes 740/283
     blocks and 197.9/73.3 ha.
   - **1.0 ha**: do not merge by default; only merge if the full safe rule holds.
     That removes 2,486/564 blocks and 1,488.5/279.0 ha.
3. **Never merge the retention/IFM split fragments.** They are
   3,575 fragments (1.9% of all fragments)
   and 100% RETENTION > 0. If the goal is model size, change how retention is
   represented (block-level area share/account) rather than deleting the
   fragments.
4. **Keep isolated small blocks.** 1,215 blocks (761.5 ha)
   have no touching neighbour. Do not delete them; they are real area.
5. **Do not tune the 0-1 ha opening weights to hide this.** The 0-1 ha openings
   may be dominated by retention fragments. Fix the geometry where it is safe,
   and represent retention explicitly.

## Expected gain

The safe geometric cleanup at 1.0 ha removes 2,486 blocks
(1.45%) and roughly 1.3% of fragments. The
larger opportunity is the retention representation: 3,575
fragments (1.9%) are retention/IFM splits, not slivers.

## MKRF cross-check

The MKRF PoC shapefile has 1,763 fragments; 35.6% are <1 ha and 5.8% of the area. It is PoC-scale, not the production inventory.

## Reproduction

The analysis uses the compiled `fragments.parquet` and `blocks.parquet`, joins
the track names for `IFM`/`ORIGIN`/`RETENTION`, and uses the fragment shapefile
for adjacency.

```bash
python - <<'PY'
import pandas as pd
f = pd.read_parquet("runtime/tsa46_full/matrix/fragments.parquet")
print((f.area_ha < 1.0).mean())
print(f.area_ha[f.area_ha < 1.0].sum())
PY
```

The spatial merge analysis reads
`output/patchworks_tsa46_full/fragments/fragments.shp`, builds the block
attributes, and queries touching neighbours with the GeoPandas spatial index.
