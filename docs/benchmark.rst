AAC benchmark
=============

The benchmark asks whether the model can hold the published AAC across ten
decades. The target account is ``product.Yield.managed.Total`` with a
``period_width`` of 10. Each decade target is ten times the annual AAC.

Targets
-------

.. list-table::
   :header-rows: 1

   * - Item
     - Value
   * - AAC
     - 803,000 m3/yr
   * - Decade target band
     - 8,030,000-8,031,000 m3
   * - Horizon
     - 100 years
   * - Target file
     - ``config/targets.tsa46_full.yaml``
   * - Run
     - ``runtime/tsa46_full/runs/opening_first``

TSR-consistent curves
---------------------

The managed lane uses BatchTIPSY 4.7 curves, not the earlier VDYP transform.
The input follows the predecessor TSRs: the future stand regenerates to the
existing analysis-unit species composition, with 4,444 stems/ha, OAF1 = 0.85,
OAF2 = 0.95, and a one- or two-year regeneration delay. The species mix is
area-weighted from the calibrated VRI checkpoint. The source TSRs are the North
Coast TSA TSR 3 Data Package (2007, Table 5.2) and the Mid Coast TSA TSR 3 Data
Package (2011). The full method is in ``notes/reference/tipsy-curves.md``.

Result
------

.. list-table::
   :header-rows: 1
   :widths: 10 25 14

   * - Decade
     - Realized volume (m3)
     - Band status
   * - 1
     - 8,030,924.8
     - met
   * - 2
     - 8,030,987.3
     - met
   * - 3
     - 8,030,958.2
     - met
   * - 4
     - 8,030,983.1
     - met
   * - 5
     - 8,030,984.6
     - met
   * - 6
     - 8,030,830.4
     - met
   * - 7
     - 8,030,975.2
     - met
   * - 8
     - 8,030,481.2
     - met
   * - 9
     - 8,030,625.8
     - met
   * - 10
     - 8,030,816.6
     - met

All ten decades are inside the band. The opening-first schedule schedules
5,587 openings on 8,383 blocks, covering 115,304.5 ha.

Opening-first policy
--------------------

The opening-size and adjacency policy is applied with a touching-block
topology and a patch account. The account joins only blocks that touch and
uses ``product.Treated.managed.CC`` as the treated-area criterion.

- Topology edges: 244,270
- Opening range: 5.3-40.0 ha
- Patch area: 172,207.3 ha
- Patch classes: **100% in the 5-40 ha class at every year**

The 0-1, 1-5, 40-50 and >50 ha classes are all 0.0%. The opening-first
schedule is a deterministic seed, not a final optimized plan. The full record
is ``notes/reference/opening-policy.md``.

Harvest coverage
----------------

The opening-first schedule covers all 21 managed AUs.
``scripts/check_harvest_coverage.py`` reports no gaps, so the allowlist is
unused. The earlier strict volume-only schedule left three small AUs
unselected; that result is retained with the dated VDYP-transform runtime.

RESULTS sensitivity
-------------------

The TSA 48 RESULTS workflow was repeated for TSA 46. The candidate table has
13 AU/SI rows; five have at least three planting records. The screened input
uses RESULTS only for those five and the checkpoint AU SI, with the TSA 46
natural-regeneration density of 4,444 stems/ha.

.. list-table::
   :header-rows: 1
   :widths: 40 14 14 18

   * - Scenario
     - Openings
     - Blocks
     - Scheduled area
   * - Current TSR
     - 5,587
     - 8,383
     - 115,304.5 ha
   * - RESULTS species, checkpoint SI, 4,444 sph
     - 6,190
     - 9,369
     - 122,730.7 ha

Both meet the ten-decade band with 100% 5-40 ha patches. The RESULTS species mix
needs **more** area under the same SI and density. That is a yield-consequence,
not a model-quality score. An earlier 89,835 ha result used harvested-area SI
and is rejected as biased.

Independent height validation
-----------------------------

Observed RESULTS cover heights (1,083 immature single-species observations)
were compared with TIPSY height at age:

.. list-table::
   :header-rows: 1
   :widths: 30 18 18 18

   * - Curve set
     - Bias
     - MAE
     - RMSE
   * - Current TSR
     - -1.50 m
     - 1.74 m
     - 3.01 m
   * - RESULTS species
     - -1.59 m
     - 1.79 m
     - 3.11 m

The TSR curves are slightly more accurate. The dominant CWH_HW H cell is
conservative: age 5-15 bias -1.08 m (-31%), age 16-30 bias -2.02 m (-26%).
That is an accuracy finding, not a reason to tune the AAC.

Site-index attribution
~~~~~~~~~~~~~~~~~~~~~~

The height bias is largely a site-index input issue. For CWH_HW H, observed
managed-stand SI is **23.0 m** at ages 5-15 and **26.0 m** at ages 31-50, while
the checkpoint AU median is **16.3 m**. The checkpoint median covers the full
THLB; the immature/harvested stands are on better sites. The next test is an
SI-stratified managed-land curve, validated on held-out stands.

Holdout managed-SI test
~~~~~~~~~~~~~~~~~~~~~~~

A deterministic 80/20 opening split estimated managed-stand SI from training
observations and tested it on held-out heights, holding species and density at
the current TSR input.

.. list-table::
   :header-rows: 1
   :widths: 30 16 16 16 16

   * - Curve set
     - n
     - Bias
     - MAE
     - RMSE
   * - Current TSR
     - 369
     - -1.61 m
     - 1.86 m
     - 3.05 m
   * - Managed SI
     - 369
     - -0.23 m
     - 1.46 m
     - 2.31 m

Managed SI clearly improves TSA 46 accuracy, including CWH_HW H at ages 5-15
(bias -1.01 m to -0.21 m). This supports SI stratification, not an AAC tune.

See ``notes/reference/results-tipsy.md`` and
``notes/reference/tipsy-validation.md``.

Candidate managed-SI model
~~~~~~~~~~~~~~~~~~~~~~~~~~

The training-split managed-SI curves were built into a side-by-side model at
``runtime/tsa46_managed_si``. It meets the ten-decade AAC constraint with 3,631
openings, 5,354 blocks, and 87,106.7 ha, all patches in the 5-40 ha class. The
area is lower than TSR, but that is a yield consequence, not an accuracy score.
The accuracy evidence is the holdout height MAE improvement from 1.86 m to
1.46 m.

Volume/DBH validation is stratified in :doc:`ground-plot-validation`. The
20-row sample is too small and the CMI rows are too old to justify a curve
change. Production remains on TSR.
The managed/young pre-registration is data-limited; see
:doc:`ground-plot-preregistration`.

Nemora pilot
~~~~~~~~~~~~

Nemora's FAIB HPS pipeline was run on the public ground-plot data. TSA 46 has
117 PSP/CMI sites and 105 non-PSP GBR North plots, but only **20** managed/young
rows matched a TIPSY AU after species/SI/age filtering (8 CMI, 6 NFI, 6 YSM).
The sample is too sparse to quantify volume/DBH accuracy; the CMI rows are old
(median age 114.9). Natural PSP_G and
experimental PSP_R plots were not used as a managed-TIPSY benchmark.

Nemora's non-PSP HPS loader initially assumed integer plot ids; the GBR files
use `I/W/E/N/S` codes. Fixed upstream in Nemora PR #5; direct ingest was
verified on the GBR North set.

Baseline versus benchmark
-------------------------

The baseline schedule is a deterministic clearcut-at-age-60 reference. It
harvests every block once and dumps mature stands into the first decade, so it
is not an AAC benchmark. Use it to verify that the dataset and simulator run,
not to judge the AAC.

Rerun
-----

The supported lane is:

.. code-block:: bash

   export FEMIC_BTC_WINEPREFIX=/path/to/wineprefix-mono
   export FEMIC_BTC_DISPLAY=:99
   TSA=46 bash scripts/build_tsr_lane.sh

The BatchTIPSY install and Wine prefix are not committed. See
``notes/reference/tipsy-curves.md`` for the one-time setup. To rerun only the
simulation and report:

.. code-block:: bash

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
