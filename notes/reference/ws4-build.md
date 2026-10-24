# Full TSA 46 ws4 build evidence

The model is built by `scripts/build_full_tsa46_model.sh` from the FEMIC
export. The Patchworks XML/fragments pair is an interchange input to
`ws4 build`; Patchworks is not the runtime lane.

## Command

```bash
MODEL_DIR=runtime/tsa46_full \
PATCHWORKS_OUT=output/patchworks_tsa46_full \
CALIBRATE_THLB=1 \
THLB_TARGET_HA=268970 \
scripts/build_full_tsa46_model.sh
```

## Dataset

| Table | Value |
| --- | ---: |
| AU count | 21 |
| Curves | 85 |
| Input fragments | 171,825 |
| Blocks after safe merge | 169,554 |
| Compiled fragments | 188,037 |
| Block area | 2,375,677.18 ha |
| Managed area | 268,970 ha |

## Safe sliver cleanup

`scripts/merge_slivers.py` merges only small blocks that preserve model
semantics: same AU, same IFM, same origin, area-weighted age within 20 years,
and both blocks with `RETENTION = 0`. Retention/IFM split fragments are never
merged, and isolated small blocks are kept.

| Measure | Value |
| --- | ---: |
| Small-block cutoff | 1.0 ha |
| Blocks merged | 2,271 |
| Area merged | 1,367.76 ha |
| Net area change | 0.0 ha |
| Skipped | age 257, different AU 1,771, different IFM 200, different origin 32, host-is-candidate 213, no touching neighbour 1,215, retention 21 |

## Benchmark

`scripts/run_aac_benchmark.sh` runs the ten-decade benchmark with the
target-driven greedy seed. `config/targets.tsa46_full.yaml` asks for the
published 803,000 m3/yr.

The strict benchmark schedules 2,792 blocks with
3,890 events and meets all ten decades with objective 0.0.

The coverage run schedules 2,920 blocks with 4,025
events, meets all ten decades, and covers the remaining above-threshold AUs:
4601002 (718.2 ha), 4601005 (204.0 ha), 4601006 (413.1 ha).

## Validation

- `ws4 build` and `ws4 validate` pass on the merged matrix.
- `scripts/check_runtime_signal.py` passes.
- `scripts/check_harvest_coverage.py` passes on the coverage run.
- The UI geometry is rendered from the merged fragments.

## UI geometry levels

The build writes two UI geometry files:

- `fragments.geojson` — 100 m simplified block layer, served by default.
- `fragments_full.geojson` — unsimplified block layer, retained for detail.

The overview is 54.4 MiB; the full layer is 232.7 MiB. The 100 m
overview is an interim scale fix, not a substitute for viewport or tiled
serving.

## Related dataset

The sibling instance is documented in
`notes/reference/related-instances.md`.
