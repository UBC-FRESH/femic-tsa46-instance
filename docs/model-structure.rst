Model structure
===============

The compiled ws4 dataset is a fragment-level columnar store. Blocks aggregate
fragments at runtime; the schedule, simulator, optimizer, and reports operate on
blocks.

Dataset tables
--------------

.. list-table::
   :header-rows: 1

   * - Table
     - Rows
     - Role
   * - ``fragments.parquet``
     - 190,308
     - Fragment geometry and age, keyed to a block and track
   * - ``blocks.parquet``
     - 190,308
     - Block/track/offset/area join used by simulation
   * - ``tracks.parquet``
     - 14,826
     - AU, IFM, origin, silviculture, retention, and treatment state
   * - ``treatments.parquet``
     - 9,491
     - Treatment timeline per track
   * - ``features.parquet``
     - 88,956
     - Feature labels and curve references
   * - ``products.parquet``
     - 28,473
     - Product labels and curve references
   * - ``accounts.parquet``
     - 51
     - Account definitions
   * - ``curves.parquet``
     - 4,667
     - Curve points
   * - ``strata.parquet``
     - 14,826
     - Track/offset age transitions

Blocks and area
---------------

.. list-table::
   :header-rows: 1

   * - Quantity
     - Value
   * - Unique blocks
     - 171,825
   * - Fragment rows
     - 190,308
   * - Block area
     - 2,375,677.18 ha
   * - Gross AOI area
     - 8,697,740.35 ha
   * - Managed area
     - 268,970 ha
   * - Managed share of block area
     - 11.3%

Tracks
------

A track name carries the model semantics explicitly:

.. code-block:: text

   AU(<code>)+IFM(managed|unmanaged)+ORIGIN(natural|treated)
     +SILV_STATE(<state>)+RETENTION(<share>)+treatment(<code>)

- ``AU`` is the analysis unit.
- ``IFM`` is treatment eligibility, not origin.
- ``ORIGIN`` is curve provenance.
- ``RETENTION`` moves area from managed to unmanaged without changing origin.

Species composition
-------------------

The initial ``feature.Area.og1.*`` accounts give the compiled species mix:

.. list-table::
   :header-rows: 1
   :widths: 18 22 12

   * - Species
     - Initial area (ha)
     - Share
   * - CWH_CW
     - 579,570.3
     - 35.3%
   * - CWH_HW
     - 489,493.4
     - 29.8%
   * - CWH_H
     - 244,714.7
     - 14.9%
   * - MH_H
     - 145,864.2
     - 8.9%
   * - CWH_YC
     - 110,608.7
     - 6.7%
   * - CWH_BA
     - 41,870.5
     - 2.5%
   * - CWH_FDC
     - 31,215.5
     - 1.9%

Every species above has a nonzero area account and a resolved curve. The
runtime-signal gate checks this on each build.

Accounts
--------

The model carries ``feature.Area``, ``feature.Yield``, ``product.Yield``,
``product.Treated``, and ``product.HarvestedVolume`` accounts. The AAC target
uses ``product.Yield.managed.Total``. The managed area account is
``feature.Area.managed``.

Geometry
--------

``fragments.geojson`` is the 100 m simplified UI layer.
``fragments_full.geojson`` is the unsimplified layer. The source fragments
shapefile is an interchange artifact under ``output/patchworks_tsa46_full/fragments/``.
