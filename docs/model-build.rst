Model build
===========

The model is built by ``scripts/build_full_tsa46_model.sh``. The script
records every command and artifact path. The Patchworks XML/fragments pair is an
interchange input to ``ws4 build``, not the runtime lane.

Chain
-----

.. code-block:: text

   femic run
     -> femic export patchworks
     -> ws4 build
     -> ws4 validate
     -> build_baseline_schedule
     -> ws4 simulate + report
     -> ws4 optimize (AAC benchmark)
     -> prepare_ws4_ui
     -> prepare_land_base

Upstream run
------------

.. list-table::
   :header-rows: 1

   * - Item
     - Value
   * - Run ID
     - ``tsa46_full_20261023``
   * - Status
     - ok, exit 0
   * - Duration
     - 2,824.821 s
   * - Started / finished
     - 2026-10-23T20:06:34Z / 2026-10-23T20:53:39Z
   * - AUs / curves
     - 21 / 85
   * - Exported fragments
     - 171,825
   * - Manifest
     - ``runtime/logs/run_manifest-tsa46_full_20261023.json``

The run uses the full TSA boundary in ``config/run_profile.tsa46_full.yaml``
and the public data root. It writes the model-input bundle, VDYP caches, and the
checkpoint under ``data/`` (all ignored by Git).

Build and validation
--------------------

.. code-block:: bash

   MODEL_DIR=runtime/tsa46_full \
   PATCHWORKS_OUT=output/patchworks_tsa46_full \
   CALIBRATE_THLB=1 \
   THLB_TARGET_HA=268970 \
   scripts/build_full_tsa46_model.sh

The script runs ``femic export patchworks``, ``ws4 build``, ``ws4 validate``,
the baseline schedule and simulation, and the UI geometry preparation.

.. list-table::
   :header-rows: 1

   * - Dataset fact
     - Value
   * - Blocks
     - 171,825
   * - Fragments in the compiled dataset
     - 190,308
   * - Block area
     - 2,375,677.18 ha
   * - Tracks
     - 14,826
   * - Treatments
     - 9,491
   * - Feature rows
     - 88,956
   * - Product rows
     - 28,473
   * - Accounts
     - 51
   * - Curve rows
     - 4,667

THLB calibration
----------------

The calibration scales each stand's ``thlb_raw / 100`` by one factor, capped at
1.0. The factor is solved so the capped proportional area hits the target.

.. list-table::
   :header-rows: 1

   * - Item
     - Value
   * - Uncalibrated managed area
     - 238,963.49 ha
   * - Target
     - 268,970 ha
   * - Factor
     - 1.1407167870336385
   * - Saturated rows
     - 9,374
   * - Evidence
     - ``runtime/tsa46_full/evidence/thlb_calibration.json``

The calibration is a proportional rescale, not a reviewed GBR netdown.

Baseline
--------

The baseline schedule harvests every block once when it reaches age 60. It is a
reproducible reference, not the AAC benchmark: it dumps mature stands into the
first decade and then declines. The baseline run is
``runtime/tsa46_full/runs/baseline``.

AAC benchmark
-------------

The benchmark is a separate search from the baseline:

.. code-block:: bash

   scripts/run_aac_benchmark.sh

The target band is 8,030,000-8,031,000 m3 per decade at
803,000 m3/yr. The recorded run schedules 2,792 blocks with
3,885 events and meets all ten decades. See :doc:`benchmark` for
the decade table and the coverage run.

Signal and coverage gates
-------------------------

.. code-block:: bash

   python scripts/check_runtime_signal.py \
     --dataset runtime/tsa46_full/matrix \
     --bundle data/model_input_bundle \
     --run runtime/tsa46_full/runs/aac_benchmark

   python scripts/check_harvest_coverage.py \
     --dataset runtime/tsa46_full/matrix \
     --schedule runtime/tsa46_full/runs/aac_benchmark/schedule.csv \
     --allowlist config/harvest_coverage.allowlist.json

The runtime-signal gate fails on a missing species/SI label, an orphan track,
or a missing curve. The coverage gate fails when an AU with at least 100 ha of
managed area has no harvest event, unless the allowlist names it with a reason.

Runtime boundary
----------------

VDYP7 is a 32-bit Windows executable. On Linux it runs under Wine, including the
32-bit loader. The first lane sets ``vdyp_sampling_mode: auto`` because larger
``all`` batches exceeded the short VDYP console timeout in the TSA 48 reference
run. Auto sampling fits from fewer stands, so it is a provisional workaround.

The first lane also sets ``managed_curve_mode: vdyp_transform`` and therefore
does not require BatchTIPSY. That transform is a provisional managed curve lane,
not accepted TIPSY yield curves.

The legacy pipeline also needs ``plots/`` to exist, a
``config/tipsy/tsa46.yaml`` case file, and the materialized
``siteprod.tif`` and ``misc.thlb.tif`` rasters. ArcRasterRescue is only needed
when the pre-stacked SiteProd raster is absent.
