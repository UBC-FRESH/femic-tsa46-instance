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
| Fragments exported | 171,825 |
| Blocks compiled | 171,825 |
| Block area | 2,375,677.18 ha |
| Managed area, uncalibrated | 238,963.49 ha |
| Managed area, calibrated | 268,970.00 ha |
| Calibration factor | 1.1407167870336385 |
| Saturated rows | 9,374 |

The calibrated THLB is the derived predecessor-value target in
`config/tsr/overlay.yaml`: the former North Coast (145,808 ha) and Mid Coast
(123,162 ha) current THLBs. TSA 46 is the union of the two retired TSA
boundaries (symmetric difference 5,268.5 ha, 0.06%).

## Benchmark

`scripts/run_aac_benchmark.sh` runs the ten-decade benchmark with the
target-driven greedy seed. `config/targets.tsa46_full.yaml` asks for
8,030,000-8,031,000 m3 per decade at 803,000 m3/yr.

The baseline schedule is a clearcut-at-age-60 reference, not the benchmark. It
dumps all mature stands in the first decade and is reported only as a
reproducible starting point.

## Validation

- `ws4 build` and `ws4 validate` pass on the full matrix.
- The UI geometry has one feature per block and the land base is the TSA 46 AOI.
- `runtime/tsa46_full/evidence/thlb_calibration.json` records the calibration.
- The benchmark report is `runtime/tsa46_full/runs/aac_benchmark/report_targets.csv`.

## Related dataset

The GBR South TSA 47 model is built independently in
`UBC-FRESH/femic-tsa47-instance`. See
`notes/reference/related-instances.md`.
