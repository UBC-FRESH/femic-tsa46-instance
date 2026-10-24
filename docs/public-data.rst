Public data and TSR provenance
==============================

FEMIC reads its public inputs from ``FEMIC_EXTERNAL_DATA_ROOT``. The canonical
tree is the ``data`` directory of ``UBC-FRESH/femic-public-data``. Large layers
are annex-backed; a pointer symlink is not a usable input until ``datalad get``
or ``git annex get`` materializes it.

Required inputs
---------------

.. list-table::
   :header-rows: 1
   :widths: 55 40

   * - Relative path
     - Use
   * - bc/tsa/FADM_TSA.gdb
     - TSA boundary source
   * - bc/siteprod/Site_Prod_BC.gdb
     - Site productivity lookup
   * - bc/vri/2025/VEG_COMP_LYR_R1_POLY_2025.gdb
     - Current VRI layer
   * - bc/vri/2025/VEG_COMP_VDYP7_INPUT_POLY_AND_LAYER_2025.gdb
     - VDYP input layer and polygon
   * - misc.thlb.tif
     - Pre-stacked THLB raster
   * - bc/siteprod/siteprod.tif
     - Pre-stacked site-productivity raster
   * - bc/siteprod/siteprod.bandmap.json
     - Site-productivity band map

Manifest
--------

``data/source/public_data_manifest.json`` records the key-table SHA-256 and
entry count for each file geodatabase. It stores the root as
``${FEMIC_EXTERNAL_DATA_ROOT}``, so the manifest is portable and safe to
commit.

.. code-block:: bash

   export FEMIC_EXTERNAL_DATA_ROOT=/path/to/femic-public-data/data
   python scripts/check_public_data.py \
     --out data/source/public_data_manifest.json

TSR documents
-------------

The canonical FEMIC TSR index has **no dedicated TSR cycle** for TSA 46:
the provincial folder ``TSA/Great_Bear_Rainforest_North_46/``
contains no documents. The current AAC is a legal order, not a TSR product.

The built-in FEMIC TSR functions were run against the predecessor TSAs that the
GBR order replaced:

.. code-block:: bash

   python -m femic tsr index
   python -m femic tsr fetch --tsa 19 --tsa 21 --tsa 33 --tsa 37
   python -m femic tsr extract --tsa 19 --tsa 21 --tsa 33 --tsa 37

Result: 77 of 78 selected PDFs were cached and extracted (one fetch failure),
producing 6,189 candidate facts. The corpus lives under ``~/.femic/tsr/`` and is
not committed.

AAC and THLB facts
------------------

.. list-table::
   :header-rows: 1

   * - Fact
     - Value
     - Source
   * - Current AAC
     - 803,000 m3/yr
     - B.C. Reg. 328/2016, section 5
   * - Calibrated THLB target
     - 268,970 ha
     - derived from the predecessor TSRs

The THLB derivation uses the former North Coast TSA (145,808 ha current THLB) and Mid Coast TSA (123,162 ha current effective THLB).

.. list-table::
   :header-rows: 1
   :widths: 20 10 20 30

   * - Predecessor TSA
     - Code
     - Current THLB (ha)
     - Source
   * - North Coast
     - 21
     - 145,808
     - TSR 2007 rationale, p. 21
   * - Mid Coast
     - 19
     - 123,162
     - TSR 2011 rationale, p. 5

TSA 46 is the union of the former North Coast and Mid Coast boundaries; the symmetric difference is 5,268.5 ha (0.06%).

The adopted facts are recorded in ``config/tsr/overlay.yaml``. This is a
predecessor-value derivation, not a reviewed GBR land-base netdown. Replace it
when a reviewed netdown is available.

Caveats
-------

- The gross TSA area includes ocean and foreshore; the VRI block area is the
  forested subset.
- The TSR corpus is cached outside the repository. A fresh machine must refetch
  it or mount a shared corpus.
- The managed-curve lane uses TSR-consistent BatchTIPSY curves. The BatchTIPSY
  install and Wine prefix are host-local and are not committed.
