Runtime provenance refresh
==========================

The current production matrix was refreshed on 2026-10-25 so its
`data_quality.yaml` sidecar matches the provenance published in the current
provenance records. The quality gate passes. This page records the matrix path, hashes, and gate
result.

Scope
-----

This is a provenance refresh, not a rebuild. The matrix tables were not
rewritten, and no curve, target, or AAC input changed. The dated VDYP-transform
backup matrices were not refreshed.

Current matrix
--------------

TSA 46
~~~~~~

- Matrix: ``runtime/tsa46_full/matrix``
- Sidecar: ``runtime/tsa46_full/matrix/data_quality.yaml``
- Sidecar SHA-256: ``50a48f25c515d0a17f231574ba79b9235af5067bd51e61fcda42baf58d30a13e``
- Manifest SHA-256: ``8f0c11de84c32c02e6ff9254cb2d6765cb78beeaa456eb33f546ebbe183d4487``
- Quality report: under ``runtime/tsa46_full/quality/``
- Quality report SHA-256: ``fb704a305879bdf04aa0c734be5fe91c937a909dff28d283f94d8a1cf13b635c``
- Status: **ok**; provenance supplied; 12 tables; no warnings.

Quality checks
--------------

.. list-table::
   :header-rows: 1
   :widths: 24 22 54

   * - Check
     - Status
     - Detail
   * - metadata
     - ok
     - Sidecar supplies the provenance metadata.
   * - tables
     - ok
     - 12 tables have rows.
   * - provenance
     - ok
     - Sidecar loaded: ``data_quality.yaml``.
   * - target_coverage
     - not-applicable
     - No active targets were supplied. This is not a target-coverage pass.

The report carries the current limitations, including:

- natural VDYP curves and TSR-consistent BatchTIPSY managed curves;
- predecessor-derived THLB;
- the data-limited managed/young validation in ADR 0003;
- the sparse ground-plot validation in ADR 0002;
- the deterministic opening-first seed and the AAC-as-ceiling caveat.

Refresh command
---------------

The command copies the tracked sidecar beside the matrix and runs the gate:

.. code-block:: bash

   python -m ws4.cli quality \
     --dataset runtime/tsa46_full/matrix \
     --sidecar config/dataset_quality.yaml \
     --out runtime/tsa46_full/quality/p50 \
     --check

The pre-refresh matrix had no ``data_quality.yaml``. The post-refresh sidecar
hash equals the tracked ``config/dataset_quality.yaml`` hash. The runtime
quality report is local and untracked; this page and
``notes/reference/runtime-provenance.md`` are the tracked evidence.

Limits
------

- The runtime artifacts are local and not committed; the hashes are a snapshot.
- No target file was supplied, so target coverage is not asserted.
- The dated VDYP-transform backups are separate comparison artifacts.
- This is not a release tag or a new model version.
