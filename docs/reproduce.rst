Reproduce the model
===================

This guide rebuilds the TSA 46 instance from a clean checkout. The
runtime outputs are large and ignored by Git; a fresh checkout has the code,
boundary, configs, and docs but not the model tree.

Prerequisites
-------------

- Linux with Python 3.11 or 3.12.
- ``femic`` and ``ws4`` installed in the active environment.
- Wine with both 64-bit and 32-bit support for VDYP7.
- ``FEMIC_EXTERNAL_DATA_ROOT`` pointing at a materialized
  ``femic-public-data/data`` tree.
- The ``plots/`` directory in the instance root.
- A ``config/tipsy/tsa46.yaml`` case file. The first lane uses the
  VDYP-transform managed curves, so BatchTIPSY is not required.

1. Materialize the public data
------------------------------

.. code-block:: bash

   export FEMIC_EXTERNAL_DATA_ROOT=/path/to/femic-public-data/data
   python scripts/check_public_data.py --out data/source/public_data_manifest.json

The four required geodatabases and the two pre-stacked rasters must resolve to
real files, not annex pointer symlinks.

2. Build the AOI
----------------

.. code-block:: bash

   python scripts/build_aoi.py \
     --source "$FEMIC_EXTERNAL_DATA_ROOT/bc/tsa/FADM_TSA.gdb" \
     --tsa-number 46 \
     --out data/source/aoi/tsa46_full.gpkg

Expected: one feature, EPSG:3005, 8,697,740.35 ha gross.

3. Run FEMIC
------------

.. code-block:: bash

   python -m femic run \
     --run-config config/run_profile.tsa46_full.yaml \
     --run-id tsa46_full_20261023 \
     --log-dir runtime/logs \
     --skip-checks

The run takes tens of minutes. It writes the model-input bundle, VDYP caches,
and ``data/vri_vclr1p_checkpoint8.feather``.

4. Build and benchmark
----------------------

.. code-block:: bash

   MODEL_DIR=runtime/tsa46_full \
   PATCHWORKS_OUT=output/patchworks_tsa46_full \
   CALIBRATE_THLB=1 \
   THLB_TARGET_HA=268970 \
   scripts/build_full_tsa46_model.sh

   scripts/run_aac_benchmark.sh

5. Verify
---------

.. code-block:: bash

   python -m ws4.cli validate --dataset runtime/tsa46_full/matrix
   python scripts/check_runtime_signal.py \
     --dataset runtime/tsa46_full/matrix \
     --bundle data/model_input_bundle \
     --run runtime/tsa46_full/runs/aac_benchmark
   python scripts/check_harvest_coverage.py \
     --dataset runtime/tsa46_full/matrix \
     --schedule runtime/tsa46_full/runs/aac_benchmark_coverage/schedule.csv
   python scripts/dashboard.py

The dashboard runs lint, format, strict types, tests, the workflow validator,
and the docs build.

6. Serve
--------

.. code-block:: bash

   ./serve_tsa46_calibrated.sh

Then check ``http://127.0.0.1:8017/health``.

Known rebuild boundaries
------------------------

- The first run failed when ``plots/`` was absent. Create it before the run.
- The TIPSY case file is required even though the managed lane is a VDYP
  transform.
- The checkpoint is ``data/vri_vclr1p_checkpoint8.feather``, not the TSA 48
  ``ria_`` name.
- The pre-stacked ``siteprod.tif`` and ``misc.thlb.tif`` rasters must be
  materialized.
- The model is volume-only; adjacency, opening size, and green-up are not yet
  applied.
