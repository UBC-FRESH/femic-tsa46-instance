Decisions and limitations
=========================

This page records the model decisions that matter to a reviewer. The detailed
records are in ``notes/reference/`` and ``notes/reports/``.

1. Full TSA boundary
--------------------

The benchmark uses the full current dissolved TSA 46 boundary. The AAC is
a TSA-wide legal determination, so a district or tenure clip would not answer
the AAC question. Record: ``notes/reference/aoi.md``.

2. Predecessor-derived THLB
---------------------------

The GBR order replaced the predecessor TSAs. TSA 46 has no dedicated TSR
cycle, so the THLB target is derived from the former North Coast TSA (145,808 ha current THLB) and Mid Coast TSA (123,162 ha current effective THLB).

This is a **predecessor-value derivation**, not a reviewed GBR netdown. Record:
``config/tsr/overlay.yaml`` and ``notes/reference/tsr.md``.

3. TSR-consistent BatchTIPSY curves
-----------------------------------

The production bundle uses BatchTIPSY 4.7 curves built by
``scripts/build_tsr_lane.sh``. The FEMIC data-prep profile stays
``managed_curve_mode: vdyp_transform`` because the lane replaces the treated
curves after the checkpoint and input table are materialized. The input follows the
predecessor TSRs: the future stand regenerates to the existing analysis-unit
species composition, with 4,444 stems/ha, OAF1 = 0.85, OAF2 = 0.95, and
a one- or two-year regeneration delay. The sources are the North Coast TSA TSR 3 Data Package (2007, Table 5.2) and the Mid Coast TSA TSR 3 Data Package (2011). The full
method, caveats, and run results are in ``notes/reference/tipsy-curves.md``.

The earlier VDYP transform is retained as a dated backup at
``runtime/tsa46_full_vdyp_20261023``. It is not the benchmark of record.

4. Harvest coverage
-------------------

The opening-first schedule covers all 21 managed AUs, so
``scripts/check_harvest_coverage.py`` reports no gaps and the allowlist is
unused. The earlier strict volume-only schedule left three small AUs unselected; that result is retained with the dated VDYP-transform runtime. The benchmark of record is the opening-first run, not the
volume-only seed.

5. Accuracy is not AAC fit
---------------------------

The AAC band is a policy constraint, not a validation statistic. A curve set
that needs fewer hectares is not thereby more accurate. The independent height
check compares TIPSY height at age with observed RESULTS cover heights. The
current TSR curves are slightly more accurate than the RESULTS species mix
(TSR bias -1.50 m, MAE 1.74 m, RMSE 3.01 m; RESULTS bias
-1.59 m, MAE 1.79 m). The height bias is largely a site-index issue: the checkpoint AU median SI
understates the managed/harvested stand SI (TSA 46 CWH_HW H: 23.0 m observed
versus 16.3 m checkpoint). The next test is an SI-stratified managed-land
curve, not a higher AAC. Volume, DBH, and mortality remain unvalidated.
Record: ``notes/reference/tipsy-validation.md``.

6. UI geometry scale
--------------------

The served map uses a 100 m overview. The full layer is retained. This is an
interim payload fix; production serving needs viewport and tiled detail. Record:
``notes/reference/ws4-build.md``.

7. Independent sibling instance
-------------------------------

This repository and `Great Bear Rainforest South TSA 47 <https://github.com/UBC-FRESH/femic-tsa47-instance>`_
are related but independent. Neither imports the other. Record:
``notes/reference/related-instances.md``.
