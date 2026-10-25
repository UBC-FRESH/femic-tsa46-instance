# ADR 0002: Ground-plot validation does not justify a curve change

Status: accepted
Date: 2026-10-25
Issues: UBC-FRESH/ws4#324

## Context

P48 reconciles the independent FAIB/Nemora ground-plot compilation against the
production TSR-consistent BatchTIPSY curves. The purpose is to test whether the
public plots support a volume, DBH, height, or stems correction, not to tune the
curves to the AAC.

TSA 46 has a small sample:

- 20 matched rows from 17 sites and 20 clusters.
- 8 CMI, 6 NFI, and 6 YSM rows.
- Median age 63.6 years; the CMI rows have a median age of 114.9 years.
- 105 non-PSP GBR North plots were available before matching; natural and
  experimental PSP plots were excluded because they are not managed-clearcut
  benchmarks.

The overall matched sample has a volume bias of -71.1 m3/ha (-32.8%), a DBH bias
of -11.2 cm (-51.6%), a height bias of -2.1 m (-12.9%), and a stems bias of
+44.7 sph (+6.8%). Many species and age cells contain only one to five
observations. Young-age predicted volumes are close to zero in several rows,
which is an age/curve-alignment warning, not evidence for a multiplier.

## Decision

Retain the production TSR-consistent BatchTIPSY curves. Do not apply a global
or species-level correction from this sample, and do not change the AAC.

The TSA 46 sample is too small, too old in its CMI component, and too unevenly
distributed to quantify managed-stand accuracy. The directional underprediction
of volume, DBH, and height is consistent with the TSA 47 audit, but the
magnitude is not estimable here. The stems results are mixed and include
near-zero predicted values at young ages.

Treat the stratified table as a monitoring and triage signal. A future curve
change requires an independent remeasured managed/young sample large enough to
separate species, age, site index, and management origin, plus a new ADR.

## Consequences

- Production remains reproducible on the accepted curve lane.
- The model's volume and DBH uncertainty is documented rather than hidden.
- The sample is not strong enough to support an accuracy claim or an
  operational correction.
- More managed/young Cw and Hw plots in the 16-80 age range are the priority for
  a future test.
- No optimality or AAC-sustainability claim follows from this decision.

## Alternatives considered

- **Apply a global volume multiplier.** Rejected: the sample is not random, the
  CMI rows are old, and a multiplier would not separate origin, density, and
  site index.
- **Apply a species-specific correction.** Rejected: most cells have n < 5 and
  the species composition is dominated by Hw.
- **Switch to managed-site-index curves.** Rejected for production: the earlier
  height evidence is not a volume/DBH validation, and the sibling audit shows
  the correction overcorrects some samples.
- **Wait for a perfect sample.** Rejected: the limitation is recorded now, and
  the production lane remains the accepted benchmark until stronger evidence
  arrives.
