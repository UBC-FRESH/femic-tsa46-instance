# Independent TIPSY height validation: TSA 46

Date: 2026-10-24
Status: first independent accuracy check; production unchanged.

## Why this exists

Area-to-AAC is not a measure of model accuracy. This check compares TIPSY
height-age predictions with observed RESULTS forest-cover heights at the same
age. The AAC target is not used.

## Data and matching

- Observed source: RESULTS forest cover, 95,254 rows for the TSA 46 AOI.
- Filter: immature single-species stands, leading species >=80%, age 5-80,
  observed height >=1.3 m.
- Matched observations: 1,083.
- AU assignment: BEC + leading species + checkpoint-derived SI class.
- Prediction: linear interpolation of the TIPSY height curve at the observed
  age.

## Result

Current TSR curves:

- n = 1,083
- bias = **-1.50 m**
- MAE = **1.74 m**
- RMSE = **3.01 m**

RESULTS-species curves:

- bias = **-1.59 m**
- MAE = **1.79 m**
- RMSE = **3.11 m**

Dominant CWH_HW H under the TSR curves:

- age 5-15: n=619, observed 3.49 m, predicted 2.41 m, bias **-1.08 m (-31%)**
- age 16-30: n=147, observed 7.67 m, predicted 5.65 m, bias **-2.02 m (-26%)**
- age 31-50: n=45, observed 18.85 m, predicted 12.45 m, bias **-6.40 m (-34%)**
- age 51-80: n=12, observed 22.24 m, predicted 17.82 m, bias -4.42 m

The TSR curve is systematically conservative for TSA 46 hemlock, especially at
young and medium ages. This is a genuine accuracy signal, not a reason to raise
yield until the AAC fits.

## Site-index attribution

The height bias is largely explained by the site-index input, not by the shape
of the TIPSY curve. For the dominant CWH_HW H cell:

| Age class | n | Observed SI | Checkpoint SI | Gap | Height bias |
| --- | ---: | ---: | ---: | ---: | ---: |
| 5-15 | 619 | 23.0 m | 16.3 m | +6.7 m | -1.08 m |
| 16-30 | 147 | 23.0 m | 16.3 m | +6.7 m | -2.02 m |
| 31-50 | 45 | 26.0 m | 16.3 m | +9.7 m | -6.40 m |
| 51-80 | 12 | 25.5 m | 16.3 m | +9.2 m | -4.42 m |

The checkpoint AU median SI includes the full THLB, while the observed
immature/harvested stands are on better sites. A single AU median therefore
understates the managed-stand SI. That is a structural issue, not a reason to
raise the AAC. The next test should be an SI-stratified managed-land curve,
validated on held-out stands.

## Holdout managed-SI test

A deterministic opening-id split (80% training, 20% holdout) was used to
estimate a managed-stand SI for each AU/SI cell. Species and density were held
at the current TSR input; only SI changed. The holdout observations were not
used to estimate SI.

| Curve set | n | Bias | MAE | RMSE |
| --- | ---: | ---: | ---: | ---: |
| Current TSR | 369 | -1.61 m | 1.86 m | 3.05 m |
| Managed SI | 369 | -0.23 m | 1.46 m | 2.31 m |

Clear improvement. Managed SI nearly removes the bias and cuts MAE by 0.40 m. TSA 46 needs SI stratification.

This is an accuracy experiment only; no production curve or AAC target was
changed.

## Candidate model

The training-split managed-SI curves were built into a side-by-side ws4 model at
`runtime/tsa46_managed_si`. It meets the ten-decade AAC constraint with 3,631
openings, 5,354 blocks, and 87,106.7 ha. The area is lower than TSR, but that is
a consequence of the higher managed SI, not evidence of correctness. The
accuracy evidence is the holdout height result above. Production remains on
TSR.

## Volume and DBH data limitation

Volume/DBH validation could not be completed from the available public data:

- RESULTS `I_BASAL_AREA` is mostly a 1.0 placeholder and has only 570 non-null
  rows out of 95,254, so observed quadratic-mean DBH cannot be computed.
- The public PSP layer is `WHSE_FOREST_VEGETATION.ISMC_PSP_ACTIVE_SITES_SP`,
  which is active plot locations only, not remeasured tree measurements.
- No CMI or PSP measurement table is materialized in the public-data tree.

Volume, DBH, and mortality validation therefore require a separate PSP/CMI
data-acquisition task. The candidate model is not a production replacement.

## Public PSP/CMI data

The volume/DBH blocker is now a data-acquisition gap, not a data-absence gap.
BC FAIB publishes plot- and tree-level ground-plot compilations at:

``https://www.for.gov.bc.ca/ftp/HTS/external/!publish/ground_plot_compilations/psp/``

Available tables include:

- `faib_header.csv` — site coordinates, BEC, TSA, sample type.
- `faib_sample_byvisit.csv` — visit years and projected ages.
- `faib_compiled_smries.csv` — plot-level volume, basal area, QMD, stems by
  utilization limit.
- `faib_compiled_spcsmries.csv` — species-level volume/BA/QMD/stems.
- `faib_compiled_spcsmries_siteage.csv` — species age, top height, and SI.

For TSA 46:

- 117 PSP/CMI sites, 353 visits
- 1,763 visit rows with merchantable volume and QMD
- 603 rows with leading-species top height
- sample types: 98 natural-growth PSP, 19 experimental PSP

This unblocks a real volume/DBH validation table, but not a clean one: TIPSY is
a managed-stand model, natural-growth PSP is unmanaged, and experimental PSP
may carry treatments. The validation must report sample type separately and
use the 12.5 cm utilization limit consistently.

## Nemora pilot

Nemora's FAIB HPS pipeline was run on the public data:

- Full PSP: 24,962 plots / 2.6M live trees; 117 PSP/CMI sites inside TSA 46.
- Non-PSP GBR North: 105 plots / 4,215 live trees.
- After AU matching, 20 managed/young-stand rows remained:
  8 CMI, 6 NFI, 6 YSM.

The small sample shows the same directional underprediction as TSA 47:

- CMI: volume bias -122.1 m3/ha, DBH -13.7 cm, height -2.5 m, stems +85.4 sph.
- NFI: volume bias -51.2 m3/ha, DBH -9.9 cm, height -1.7 m, stems +214.8 sph.
- YSM: volume bias -19.5 m3/ha, DBH -9.3 cm, height -2.0 m, stems -151.5 sph.

The CMI rows are old (median age 114.9), so this is not a clean managed-young
sample. It is not large enough to quantify TSA 46 volume/DBH accuracy. The 125
natural and 52 experimental PSP rows were not used as a managed-TIPSY
benchmark; PSP_G is unmanaged old growth and PSP_R is experimental, not a
clearcut managed stand.

Nemora's non-PSP HPS loader initially assumed integer plot ids; the GBR files
use `I/W/E/N/S` codes. This was fixed upstream in Nemora PR #5, and direct
ingest was verified on the 105-plot GBR North set. The staged code-to-index
copy is no longer required.

## Caveats

- Volume/DBH are only available from the sparse Nemora ground-plot pilot; mortality is not validated.
- RESULTS cover is an inventory observation, not a remeasured PSP/CMI plot.
- Single-species filter excludes mixed stands.
- TIPSY age and observed total age are assumed comparable; regeneration delay
  is not adjusted.
- The sample is weighted toward CWH_HW H; sparse AU cells are not conclusive.

## Files

- `scripts/validate_tipsy_height.py`
- `tests/test_validate_tipsy_height.py`
- `config/tsr/tipsy_height_validation.tsa46.csv`
- `config/tsr/tipsy_height_validation_summary.tsa46.csv`
- `config/tsr/tipsy_height_validation_results.tsa46.csv`
- `config/tsr/tipsy_height_validation_results_summary.tsa46.csv`
