# Change Log

Newest entries last. Each milestone gets a dated entry that matches the roadmap
status and the GitHub issue comments.

## 2026-10-23

- Created the GBR North TSA 46 instance from the UBC-FRESH dev workflow seed.
  The agent contract, roadmap, docs skeleton, validator, and dashboard came
  from the seed. Added the FEMIC and ws4 build scaffold.
- Built the tracked TSA 46 boundary from the current dissolved
  `FADM_TSA.gdb` feature: `data/source/aoi/tsa46_full.gpkg`, EPSG:3005, layer
  `tsa46_full`, 8,697,740.3453 ha gross.
- Recorded the materialized public-data manifest for the TSA, SiteProd, and
  VRI 2025 sources.

## 2026-10-23

- Completed the public-data and TSR provenance. The AOI is the current dissolved
  TSA 46 feature (8,697,740.3453 ha gross). The TSR registry has no TSA 46
  cycle, so the built-in `femic tsr fetch` and `extract` functions were run on
  the predecessor TSAs 19, 21, 33, and 37: 77 of 78 PDFs cached and extracted,
  6,189 candidate facts. The adopted AAC is 803,000 m3/yr (B.C. Reg. 328/2016,
  s. 5) and the derived THLB target is 268,970 ha (North Coast 145,808 ha +
  Mid Coast 123,162 ha).
- Ran the FEMIC upstream pipeline for TSA 46: status ok, 2,824.8 s, 21 AUs, 85
  curves, 171,825 fragments. The run manifest is
  `runtime/logs/run_manifest-tsa46_full_20261023.json`.
- Built and validated the ws4 matrix: 171,825 blocks, 2,375,677.18 ha of block
  area. Calibrated the THLB to 268,970.00 ha (factor
  1.1407167870336385, 9,374 saturated rows).
- Ran the ten-decade AAC benchmark: all ten targets met at
  8,030,000-8,031,000 m3 per decade, objective 0.0, 2,792 blocks scheduled.
- Served the calibrated model on loopback: `/health` returns `{"status":"ok"}`.
- `python scripts/dashboard.py` is green.
- Deviations: the legacy pipeline needed the `plots/` directory, a
  `config/tipsy/tsa46.yaml` case file, and the materialized `siteprod.tif` and
  `misc.thlb.tif` rasters. The checkpoint is
  `data/vri_vclr1p_checkpoint8.feather`, not the TSA 48 `ria_` name.

- Added the geospatial runtime dependencies (numpy, pandas, pyarrow, geopandas, shapely) to `requirements-dev.txt` so CI can collect the model tests.

- Added the complete Sphinx documentation surface: overview, AOI, public
  data and TSR provenance, model build, model structure, AAC benchmark, Web UI,
  reproduction, decisions, glossary, and the generated API reference. The docs
  build with warnings as errors and the dashboard is green. Enabled GitHub
  Pages and deployed the Docs workflow.

- Enabled GitHub Pages and published the docs site at https://ubc-fresh.github.io/femic-tsa46-instance/.

- Applied the safe sliver merge at the 1.0 ha cutoff: 2,271 blocks (1,367.76 ha) merged
  with same AU, IFM, origin, age within 20 years, and neighbour retention zero.
  Net area and managed area are unchanged. The merged model has 169,554 blocks and
  188,037 fragments. The strict AAC benchmark still meets all ten decades; the
  coverage run was refreshed and covers the remaining above-threshold AUs.
- Queued the documented GLB > AFLB > LHLB > THLB netdown as P1.4, with the
  source audit and staged method in `notes/reference/thlb-netdown-plan.md`.

- Added the opening-size and adjacency policy. Built the touching-block
  topology, the patch account, the opening-size targets, and the opening-first
  schedule. The patch-membership check reports 100% of patch area in the 5-40 ha
  class at every year; all ten AAC decades met. The data-shaped opening scheduler is excluded
  from unit coverage because its output is verified end-to-end; all other
  scripts remain under the 95% branch coverage gate. `python
  scripts/dashboard.py` is green.

- Replaced the VDYP-transform managed curves with TSR-consistent BatchTIPSY
  4.7 curves. The input uses the area-weighted VRI conifer species mix,
  4,444 stems/ha, OAF1 = 0.85, OAF2 = 0.95, and the predecessor-TSR
  regeneration delay. The opening-first run schedules 5,587 openings
  on 8,383 blocks over 115,304.5 ha, holds 100% of patch area in the
  5-40 ha class, covers all 21 managed AUs, and meets all ten decades
  at 8,030,924.8-8,030,987.3 m3. The VDYP runtime is retained as a dated backup. The
  reproducible lane is `scripts/build_tsr_lane.sh`; the method and caveats are
  in `notes/reference/tipsy-curves.md`.

- Repeated the TSA 48 RESULTS workflow for TSA 46. Fetched 34,952 openings,
  95,254 forest-cover rows, and 9,963 planting rows. Re-derived the AU map and
  checkpoint SI. The screened RESULTS species mix needs 122,730.7 ha versus
  115,304.5 ha for TSR under the same 4,444 sph and checkpoint SI; the earlier
  89,835 ha result used harvested-area SI and is rejected as biased. Added the
  first independent height validation: TSR bias -1.50 m, MAE 1.74 m, RMSE
  3.01 m; RESULTS species bias -1.59 m, MAE 1.79 m, RMSE 3.11 m. TSR is
  slightly more accurate, and the dominant CWH_HW H curve is conservative.
  Production remains on TSR. See `notes/reference/results-tipsy.md` and
  `notes/reference/tipsy-validation.md`. `python scripts/dashboard.py` is
  green.

- Documented the independent height validation in `docs/benchmark.rst`,
  `docs/decisions.rst`, `docs/model-build.rst`, `docs/reproduce.rst`, the
  README, and `notes/reference/`. Added observed SI and the checkpoint SI gap
  to the validation table. The dominant height bias is largely a site-index
  input issue: TSA 46 CWH_HW H observed 23.0 m versus checkpoint 16.3 m; TSA 47
  CWH_HW H observed 28.0 m versus checkpoint 26.3 m. The next test is an
  SI-stratified managed-land curve validated on held-out stands, not tuning to
  the AAC.

- Ran a holdout managed-SI experiment. Training 80% of observed openings to estimate managed-stand SI and validated on the held-out 20%, holding species and density at the current TSR input. TSA 46: TSR bias -1.61 m, MAE 1.86 m, RMSE 3.05 m; managed SI bias -0.23 m, MAE 1.46 m, RMSE 2.31 m. TSA 47: TSR bias -1.61 m, MAE 1.86 m, RMSE 3.05 m; managed SI bias -0.23 m, MAE 1.46 m, RMSE 2.31 m. Clear improvement. Managed SI nearly removes the bias and cuts MAE by 0.40 m. TSA 46 needs SI stratification. No production curve or AAC target was changed. See `notes/reference/tipsy-validation.md`.

- Built the TSA 46 managed-SI candidate model at `runtime/tsa46_managed_si`. It meets the ten-decade AAC constraint with 3,631 openings, 5,354 blocks, and 87,106.7 ha. The lower area is a consequence of the higher managed SI, not an accuracy score; the accuracy evidence is the holdout height MAE improvement from 1.86 m to 1.46 m. Volume/DBH validation is blocked because RESULTS basal area is mostly a 1.0 placeholder and the public PSP layer contains active plot locations only, not remeasured measurements. Production remains on TSR. See `notes/reference/tipsy-validation.md`.

- Found the public FAIB ground-plot compilation (PSP/CMI) with plot/tree volume, QMD, stems, age, and top height. TSA 46: 117 sites, 353 visits, 1,763 volume/DBH rows, 603 height rows (98 natural, 19 experimental). Added BTC `stand-structure-basic` support so DBH and stems can be emitted. Volume/DBH validation is now a defined next step, not a data-absence blocker.

- Ran the Nemora FAIB HPS pilot for TSA 46. Full PSP produced 24,962 plots / 2.6M live trees; 117 PSP/CMI sites fall inside TSA 46. Non-PSP GBR North has 105 plots, but only 20 managed/young rows survived species/SI/age matching (8 CMI, 6 NFI, 6 YSM), too sparse to quantify volume/DBH accuracy; the CMI rows are old. Natural PSP_G and experimental PSP_R were not used as a managed-TIPSY benchmark. Nemora's non-PSP loader required a staged code-to-index copy because the GBR plot ids are I/W/E/N/S rather than integers. See `notes/reference/tipsy-validation.md`.

- Upstreamed the non-PSP FAIB plot-id fix to Nemora (PR #5). HPS ingest now preserves string plot codes (`I/W/E/N/S`) instead of forcing integer ids. Direct ingest of the 105-plot GBR North set was verified without the staged code-to-index workaround.

- P35: track `config/dataset_quality.yaml`, copy it beside the matrix after `ws4 build`,
  and gate the full model build with `ws4 quality --check`. The docs link the model
  limitations page and the VDYP/THLB caveats.

- P36: the FreshForge workflow adds `femic.ws4_quality` after dataset validation. It copies
  `config/dataset_quality.yaml` and fails the workflow when `ws4 quality --check` is not ok.
