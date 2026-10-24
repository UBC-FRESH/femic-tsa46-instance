# RESULTS-derived TIPSY inputs: TSA 46

Date: 2026-10-24
Status: analysis complete; production TSR lane unchanged.

## Purpose

Repeat the TSA 48 RESULTS workflow for TSA 46. The TSA 48 script/tests are the
template; the TSA 46 AOI, AU table, site-index medians, species mix, density,
and genetic-worth assumptions are re-derived.

## Data

Fetched with `femic data bcdc-fetch` for the TSA 46 AOI:

- RESULTS openings: 34,952
- RESULTS forest cover: 95,254
- RESULTS planting: 9,963

## Method

- Filter openings to the TSA 46 AOI.
- Select the latest/most complete cover row per opening.
- Map to the TSA 46 AU by leading species and checkpoint-derived SI class.
- Aggregate species, planting density, SI, genetic worth, and regeneration
  context.
- Do not use overstory total stems as regeneration density.
- Use the checkpoint AU SI, not the harvested-area cover SI, to avoid selection
  bias.
- Keep the TSA 46 natural-regeneration density assumption (4,444 stems/ha) for
  the species/SI comparison.

Genetic worth is 0 for all species because the predecessor North Coast/Mid
Coast TSR does not adopt a genetic-gain allowance. OAF1 = 0.85, OAF2 = 0.95.

## Coverage

- 13 `(stratum, SI)` candidate rows.
- 5 rows with at least three planting records:
  CWH_BA H, CWH_CW H/M, CWH_FDC H, CWH_HW H.
- CWH_H and MH_H have no RESULTS candidate rows and retain the TSR input.
- Several sparse rows have no planting record; their species/SI are not used in
  the screened input.

## Results

All scenarios meet the ten-decade 8,030,000-8,031,000 m3 band with 100% of patch
area in the 5-40 ha class.

| Scenario | Openings | Blocks | Scheduled area |
| --- | ---: | ---: | ---: |
| Current TSR | 5,587 | 8,383 | 115,304.5 ha |
| RESULTS species, checkpoint SI, 4,444 sph | 6,190 | 9,369 | 122,730.7 ha |

The RESULTS-screened species mix needs **more** area than TSR under the same
checkpoint SI and density. That is not a model-quality score; it means the
RESULTS species mix is less productive than the TSR mix at the AU SI values.
The earlier 89,835 ha result used harvested-area SI and is rejected as biased.

## Accuracy check

Independent TIPSY height validation (see `tipsy-validation.md`):

- Current TSR: bias -1.50 m, MAE 1.74 m, RMSE 3.01 m.
- RESULTS species: bias -1.59 m, MAE 1.79 m, RMSE 3.11 m.

TSR is slightly more accurate; there is no evidence to switch.

## Files

- `scripts/build_results_tipsy_inputs.py`
- `config/tsr/tipsy_au_results_candidates.tsa46.csv`
- `config/tsr/tipsy_au_results_candidates.tsa46_screened.csv`
- `config/tsr/tipsy_au_results_tsr_comparison.tsa46.csv`
- `tipsy_io/runs/03_input-tsa46_results_species.csv`
- `runtime/tsa46_results_species/runs/opening_first`
