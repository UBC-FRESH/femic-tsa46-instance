Ground-plot validation
======================

Purpose
-------

This page reports the independent FAIB/Nemora ground-plot check for TSA 46. It
tests whether the public plots support a correction to the production
TSR-consistent BatchTIPSY curves. It does not tune the curves to the AAC.

The accepted decision is ADR 0002: the sample is too small and too uneven to
justify a curve change, so production remains on the TSR-consistent lane.

Sample frame
------------

The validation lane is ``scripts/validate_tipsy_ground_plots.py``. It keeps one
leading species per visit (at least 50% of basal area), requires a single-species
stand, uses the 12.5 cm utilization limit, and matches the plot to a model AU
by BEC zone, leading species, and checkpoint site-index class.

.. list-table::
   :header-rows: 1
   :widths: 18 10 10 16 46

   * - Sample type
     - Rows
     - Sites
     - Median age (yr)
     - Role
   * - CMI
     - 8
     - 8
     - 114.9
     - Old managed inventory plots; not a managed-young sample.
   * - NFI
     - 6
     - 3
     - 49.0
     - National forest inventory plots.
   * - YSM
     - 6
     - 6
     - 37.3
     - Young-stand survey plots.
   * - **Total**
     - **20**
     - **17**
     - **63.6**
     - **20 clusters; 105 non-PSP plots before matching.**

The 20 rows are the entire matched sample. The lane does not persist a reason
code for non-matches, so it reports them as unmatched rather than as a single
exclusion reason. Of the 105 candidate non-PSP plots, 17 sites contributed 20
matched rows; the remaining 88 candidate plots did not contribute a matched row.
Natural and experimental PSP plots were not used: PSP_G is unmanaged old growth
and PSP_R is experimental, not a managed-clearcut benchmark. The separate
PSP/CMI set (117 sites, 353 visits; 125 natural and 52 experimental PSP rows)
was excluded for the same reason. This is a small, non-random sample, not an
operational audit.

Results
-------

The signed bias is predicted minus observed. A negative volume bias means the
model underpredicted the plot.

.. list-table::
   :header-rows: 1
   :widths: 18 8 14 14 12 12 12

   * - Metric
     - n
     - Observed
     - Predicted
     - Bias
     - MAE
     - Relative
   * - Volume (m3/ha)
     - 19
     - 216.7
     - 145.7
     - -71.1
     - 108.0
     - -32.8%
   * - DBH (cm)
     - 20
     - 21.8
     - 10.6
     - -11.2
     - 11.2
     - -51.6%
   * - Height (m)
     - 20
     - 16.4
     - 14.3
     - -2.1
     - 4.1
     - -12.9%
   * - Stems (sph)
     - 19
     - 656.7
     - 701.4
     - +44.7
     - 352.6
     - +6.8%

By sample type
~~~~~~~~~~~~~~

The ``n`` column is volume/DBH. Height and stems can have one fewer valid pair;
the full counts are in the CSV.

.. list-table::
   :header-rows: 1
   :widths: 12 10 14 14 14 14 14 14

   * - Sample
     - n
     - Volume bias
     - Volume MAE
     - Volume rel.
     - DBH bias
     - Height bias
     - Stems bias
   * - CMI
     - 8/8
     - -122.1
     - 123.0
     - -37.6%
     - -13.7
     - -2.5
     - +85.4
   * - NFI
     - 5/6
     - -51.2
     - 61.3
     - -41.2%
     - -9.9
     - -1.7
     - +214.8
   * - YSM
     - 6/6
     - -19.5
     - 126.8
     - -13.0%
     - -9.3
     - -2.0
     - -151.5

By species
~~~~~~~~~~

The ``n`` column is volume/DBH/height/stems. All cells are small; they are
descriptive, not estimates of population accuracy.

.. list-table::
   :header-rows: 1
   :widths: 10 16 16 12 12 12

   * - Species
     - n
     - Volume bias (rel.)
     - DBH bias
     - Height bias
     - Stems bias
   * - Cw
     - 5/5/5/5
     - -58.9 (-40%)
     - -10.6
     - -0.4
     - +44.4
   * - Hm
     - 3/3/3/3
     - -133.2 (-65%)
     - -13.7
     - +1.0
     - +86.9
   * - Hw
     - 11/12/12/11
     - -59.6 (-24%)
     - -10.9
     - -3.6
     - +33.3

By age class
~~~~~~~~~~~~

The ``n`` column is volume/DBH/height/stems. A negative volume bias is an
underprediction.

.. list-table::
   :header-rows: 1
   :widths: 12 16 16 12 12 12

   * - Age class
     - n
     - Volume bias (rel.)
     - DBH bias
     - Height bias
     - Stems bias
   * - 16-30
     - 2/3/3/2
     - -44.1 (-99%)
     - -11.7
     - -4.0
     - -518.0
   * - 31-50
     - 6/6/6/6
     - -90.0 (-77%)
     - -10.8
     - -5.7
     - -282.8
   * - 51-80
     - 3/3/3/3
     - -55.6 (-26%)
     - -11.2
     - -2.0
     - +383.1
   * - 81-200
     - 8/8/8/8
     - -69.4 (-21%)
     - -11.5
     - +1.2
     - +304.0

Interpretation
--------------

- Volume, DBH, and height are underpredicted in the aggregate and in every
  sample type. The stems result is mixed.
- The sample cannot quantify accuracy. Most species and age cells contain one
  to five observations, and the CMI component is old (median age 114.9 years).
- Several young rows have predicted volume near zero while observed volume is
  substantial. That is an age/curve-alignment warning, not evidence for a
  global multiplier.
- The TSA 46 result is directionally consistent with the TSA 47 audit, but the
  magnitudes are not comparable because the TSA 46 sample is so much smaller
  and older.

Decision
--------

ADR 0002 retains the production TSR-consistent BatchTIPSY curves. No volume,
DBH, height, stems, or AAC change follows from this sample. The next test needs
more managed/young Cw and Hw plots in the 16-80 age range, with an independent
remeasured sample.

Reproduce
---------

The observations are ``config/tsr/tipsy_ground_plot_validation.tsa46.csv``.
The stratified table is regenerated from them:

.. code-block:: bash

   python scripts/summarize_ground_plot_validation.py \
     --tsa 46 \
     --observations config/tsr/tipsy_ground_plot_validation.tsa46.csv \
     --out config/tsr/tipsy_ground_plot_validation_stratified.tsa46.csv

The full matching lane and its raw inputs are documented in
``notes/reference/tipsy-validation.md``.
