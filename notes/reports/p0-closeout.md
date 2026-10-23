# Phase close-out report: P0 Build the GBR North TSA 46 instance

Phase: P0, Build the instance
Parent issue: #1
Pull request: not opened yet
Evidence head: `678002e`
Report commit: the commit that adds this report. Its CI run is posted on the pull request.
Date: 2026-10-23
Status: queued for approval. Not merged.

## Recommendation

Approve these actions. The agent carries them out in this order, and reads back each result.

1. Squash-merge the phase pull request, and delete the branch `feature/p0-build`.
2. Close parent issue #1 with a closeout comment that cites the merge commit.
3. Launch the next phase: accepted TIPSY curves, a reviewed GBR land-base netdown, and the opening-size policy.

Settings changes: none. This phase changes no repository setting, tag, release, or external account.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| `python scripts/dashboard.py` is green. | Lint, format, types, tests, validator, and docs are green at `678002e`. | Met |
| The tracked AOI is `data/source/aoi/tsa46_full.gpkg`, EPSG:3005, 8,697,740.35 ha gross. | `data/source/aoi/tsa46_full.summary.json`: one dissolved feature, EPSG:3005, 8,697,740.3453 ha. | Met |
| The FEMIC run manifest records a successful TSA 46 run. | `runtime/logs/run_manifest-tsa46_full_20261023.json`: status ok, exit 0, 2,824.821 s, tsa_list `["46"]`. | Met |
| `ws4 build` and `ws4 validate` pass on the full matrix. | 171,825 blocks, 2,375,677.18 ha block area; `ws4 validate` passes. | Met |
| The calibrated managed area matches the derived 268,970 ha THLB target. | `runtime/tsa46_full/evidence/thlb_calibration.json`: 268,970.000 ha, factor 1.1407167870336385, 9,374 saturated rows. | Met |
| The ten decade targets hold the published 803,000 m3/yr AAC. | `runs/aac_benchmark/report_targets.csv`: all ten decades `met`, 8,030,000-8,031,000 m3, objective 0.0, 2,792 blocks scheduled. | Met |
| `/health` returns `{"status":"ok"}` and the UI shows the TSA 46 AOI. | `curl http://127.0.0.1:8017/health` returns `{"status":"ok"}`; `/` returns 200; `/api/targets` returns 200. | Met |
| No private data, credentials, or machine-specific paths are tracked. | The workflow validator scans the committed files and reports 0 errors. | Met |

## 2. Workflow compliance

- Parent issue before the branch: #1 was created before `feature/p0-build`.
- Branch from `main`: `feature/p0-build` starts at the initial repository commit.
- Commit messages start with task IDs: `P0.1`, `P0.2-P0.6`.
- Gates for each commit: the dashboard is green at the evidence head.
- Roadmap and changelog in step: both record the completed tasks and the evidence.
- Child issues closed with closeout evidence: pending the closeout comments in the recommendation.
- Approval gates: repository creation was explicitly approved. No tag, release, settings change, or private data was touched.

## 3. Gate evidence

| Gate | Result at `678002e` |
| --- | --- |
| lint | green |
| format | green |
| types | green |
| tests | green (167 tests, coverage gate 95 percent) |
| validator | green |
| docs | green |

## 4. CI evidence

The pull request is not open yet. Its first CI run is posted on the pull request.

## 5. Deviations

| Deviation | Cause | Remedy |
| --- | --- | --- |
| The first FEMIC run failed because `plots/` did not exist. | The ignore rules keep `plots/` out of git, so the directory was absent. | Created `plots/` and resumed the run. |
| The second FEMIC run failed because `config/tipsy/tsa46.yaml` was absent. | The seed ships only the TIPSY template. | Added a provisional coastal case file; the first lane uses VDYP-transform managed curves. |
| The public data root had unresolved `siteprod.tif` and `misc.thlb.tif` annex pointers. | The annex payload was not materialized. | Materialized both rasters from the sibling annex copy. |
| The checkpoint is `data/vri_vclr1p_checkpoint8.feather`, not the TSA 48 `ria_` name. | The legacy pipeline names the new checkpoint without the `ria_` prefix. | Updated the build script and FreshForge workflow. |

## 6. Next phase

Goal: replace the provisional managed-curve lane and the predecessor-value THLB derivation with accepted evidence.

Tasks:

- P1.1 Accepted TIPSY curve handoff for TSA 46.
- P1.2 Reviewed GBR North land-base netdown and THLB target.
- P1.3 Opening-size and adjacency policy for the benchmark.

Recommended defaults:

- Keep the current VDYP-transform lane as the comparison baseline.
- Keep the derived 268,970 ha target until a reviewed netdown replaces it.
- Add the opening policy only after the TSA-level benchmark is accepted.

## 7. Decision

- [ ] Approve as written.
- [ ] Approve with the changes stated here: <changes>.
