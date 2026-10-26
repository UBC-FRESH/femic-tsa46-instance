TSA 46 AOI
==========

The model AOI is the full Great Bear Rainforest North Timber Supply Area, TSA 46. The
tracked boundary is ``data/source/aoi/tsa46_full.gpkg`` (EPSG:3005,
layer ``tsa46_full``).

Boundary
--------

.. list-table::
   :header-rows: 1

   * - Item
     - Value
   * - Source
     - ``FEMIC_EXTERNAL_DATA_ROOT/bc/tsa/FADM_TSA.gdb``
   * - Source layer
     - ``WHSE_ADMIN_BOUNDARIES_FADM_TSA``
   * - Selection
     - ``TSA_NUMBER = 46``, ``TSB_NUMBER`` null, ``RETIREMENT_DATE`` null
   * - Output
     - ``data/source/aoi/tsa46_full.gpkg``, layer ``tsa46_full``
   * - CRS
     - EPSG:3005
   * - Gross area
     - 8,697.7 thousand ha
   * - Bounds
     - 634372.03, 684898.80, 1029161.54, 1222796.50

The layer also carries supply-block rows and retired historical versions. The
selection above keeps the single current dissolved TSA feature. Supply blocks
are components, not the build boundary.

TSA 46 is the union of the former North Coast and Mid Coast boundaries; the symmetric difference is 5,269 ha (0.06%).

Legal framework
---------------

The Great Bear Rainforest (Forest Management) Act and B.C. Reg. 328/2016 came
into effect on January 1, 2017. They replaced the former North Coast, Mid
Coast, Kingcome, and Strathcona TSAs with the GBR North, GBR South, and North
Island TSAs.

.. list-table::
   :header-rows: 1

   * - Item
     - Value
   * - Current AAC
     - 803,000 m3/yr
   * - Legal source
     - B.C. Reg. 328/2016, section 5
   * - Effective date
     - 2017-01-01

Why the full TSA
----------------

The published AAC is a TSA-wide legal determination. The full dissolved TSA is
therefore the only defensible benchmark boundary. District, tenure, or
supply-block clips are overlays or planning sub-units, not the AAC boundary.

Decision record
---------------

The review record is ``notes/reference/aoi.md``. The numeric check is
``data/source/aoi/tsa46_full.summary.json``. A change to
``selection.boundary_path`` or ``boundary_code`` needs a new recorded decision.
