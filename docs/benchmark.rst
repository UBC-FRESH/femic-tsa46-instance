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

See ``notes/reference/results-tipsy.md`` and
``notes/reference/tipsy-validation.md``.

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
