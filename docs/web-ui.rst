Web UI
======

The ws4 web UI serves the compiled dataset and its runs. It binds loopback by
default and has no authentication.

Launch
------

.. code-block:: bash

   ./serve_tsa46_calibrated.sh

The script expands to:

.. code-block:: bash

   python -m ws4.cli serve \
     --dataset runtime/tsa46_full/matrix \
     --runs runtime/tsa46_full/runs \
     --geometry runtime/tsa46_full/fragments.geojson \
     --land-base runtime/tsa46_full/land_base.geojson \
     --targets config/targets.tsa46_full.yaml \
     --crs EPSG:3005 \
     --allow-runs \
     --allow-agent \
     --port 8017

``PORT=...`` overrides the default. Open
``http://127.0.0.1:8017/``. Under a JupyterHub code-server proxy the path
is the proxied port.

Geometry scale
--------------

.. list-table::
   :header-rows: 1

   * - File
     - Role
     - Size
   * - ``fragments.geojson``
     - 100 m simplified overview, served by default
     - 54.4 MiB
   * - ``fragments_full.geojson``
     - Unsimplified block layer, retained for detail
     - 232.7 MiB
   * - Map response
     - Full-map GeoJSON at the overview scale
     - about 74 MB, about 9.5 s

The 100 m overview keeps the initial payload manageable. It is not a substitute
for viewport or tiled serving. A production deployment should serve vector tiles
at zoom-dependent detail: dissolved units at low zoom, simplified blocks at
middle zoom, and full blocks at high zoom. See ``docs`` and the ws4 roadmap for
the tiling work.

Checks
------

.. code-block:: bash

   curl http://127.0.0.1:8017/health
   # {"status":"ok"}

- The map shows the full TSA 46 AOI.
- The run list contains ``baseline`` and ``opening_first``.
- The target table shows ten decade targets and their realized values.
- The block detail panel shows ``block_id`` and treatment state.

Security
--------

The service has no authentication. Keep it on loopback. Do not use
``--allow-remote`` without a trusted proxy. Pass ``--crs EPSG:3005`` for the GBR
geometry; MapLibre projects it to WGS84 in the browser.
