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

## Caveats

- Height only. Volume, DBH, and mortality are not validated.
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
