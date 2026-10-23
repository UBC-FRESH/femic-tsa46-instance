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
     - ``runtime/tsa46_full/runs/aac_benchmark``

Strict benchmark result
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 10 25 14

   * - Decade
     - Realized volume (m3)
     - Band status
   * - 1
     - 8,030,998.942
     - met
   * - 2
     - 8,030,998.803
     - met
   * - 3
     - 8,030,994.445
     - met
   * - 4
     - 8,030,987.469
     - met
   * - 5
     - 8,030,983.938
     - met
   * - 6
     - 8,030,999.755
     - met
   * - 7
     - 8,030,991.308
     - met
   * - 8
     - 8,030,958.203
     - met
   * - 9
     - 8,030,989.593
     - met
   * - 10
     - 8,030,995.988
     - met

All ten decades are inside the band. The search starts from the target-driven
greedy seed, schedules 2,792 blocks, and records
3,885 events. The objective is 0.0.

Coverage run
------------

The strict volume-only search leaves three small managed AUs unselected. A
separate coverage run starts from the strict schedule, adds one event for each
AU above the 100 ha threshold, and re-optimizes. It is a diagnostic, not the
benchmark of record.

- Coverage run: ``runtime/tsa46_full/runs/aac_benchmark_coverage``
- Blocks scheduled: 2,892
- AUs covered: 4601004 (41.1 ha), 4602003 (128.8 ha), and 4601005 (15.3 ha)

.. list-table::
   :header-rows: 1
   :widths: 10 28 16

   * - Decade
     - Coverage-run volume (m3)
     - Band status
   * - 1
     - 8,030,648.817
     - met
   * - 2
     - 8,030,858.321
     - met
   * - 3
     - 8,030,753.466
     - met
   * - 4
     - 8,031,370.905
     - 371 above
   * - 5
     - 8,030,198.684
     - met
   * - 6
     - 8,030,606.636
     - met
   * - 7
     - 8,030,171.550
     - met
   * - 8
     - 8,030,771.204
     - met
   * - 9
     - 8,030,409.735
     - met
   * - 10
     - 8,031,007.723
     - 7.7 above

Nine decades meet the strict band. Decade 4 is 371 m3 above the upper bound and decade 10 is 7.7 m3 above. The strict benchmark remains the benchmark of record.

Baseline versus benchmark
-------------------------

The baseline schedule is a deterministic clearcut-at-age-60 reference. It
harvests every block once and dumps mature stands into the first decade, so it
is not an AAC benchmark. Use it to verify that the dataset and simulator run,
not to judge the AAC.

Rerun
-----

.. code-block:: bash

   scripts/run_aac_benchmark.sh
   # optional: change the search budget
   ITERATIONS=8000 PATIENCE=1000 THREADS=8 scripts/run_aac_benchmark.sh

The watcher is observational and does not persist a run:

.. code-block:: bash

   scripts/watch_aac_benchmark.sh
   PLAIN=1 scripts/watch_aac_benchmark.sh
