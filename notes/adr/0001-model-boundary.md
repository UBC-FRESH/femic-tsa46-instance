# ADR 0001: Accepted model boundary for the TSA 46 benchmark

Status: accepted
Date: 2026-10-25
Issues: UBC-FRESH/ws4#311

## Context

The Great Bear Rainforest North Timber Supply Area (TSA 46) has a legal
allowable annual cut (AAC) of 803,000 m3/yr and a full dissolved boundary of
8,697,740.35 ha. The GBR order replaced the predecessor TSAs, and TSA 46 has no
dedicated provincial timber supply review (TSR) cycle. A strategic benchmark is
still needed to test whether the public inventory, the predecessor land base, and
the TSR-consistent yield assumptions can support the published AAC.

The model is built with FEMIC from public inventory and site data and compiled
with ws4. It uses the full TSA boundary, a calibrated managed land base, and a
deterministic opening-first schedule. It is a benchmark, not an operational
plan.

## Decision

We accept the following model boundary for the TSA 46 benchmark:

1. **Boundary.** Use the full current dissolved TSA 46 boundary (8,697,740.35 ha
   gross), not a district, tenure, or watershed clip.
2. **Land base.** Calibrate the managed land base to 268,970 ha, derived from
   the former North Coast TSA (145,808 ha current THLB) and Mid Coast TSA
   (123,162 ha current effective THLB). This is a predecessor-value derivation,
   not a reviewed GBR netdown.
3. **Yield curves.** Keep natural curves on VDYP. Replace treated curves with
   BatchTIPSY 4.7 output from the TSR-consistent lane, following the North Coast
   TSA TSR 3 Data Package (2007, Table 5.2) and the Mid Coast TSA TSR 3 Data
   Package (2011). The lane assumes regeneration to the existing AU species mix,
   4,444 stems/ha, OAF1 = 0.85, OAF2 = 0.95, a regeneration delay of one year for
   cedar/yellow-cedar leading AUs and two years otherwise, and the AU-level
   inventory site index applied to every species. It does not apply genetic gain.
   The `managed_curve_mode: vdyp_transform` profile flag describes the FEMIC
   data-preparation lane only; it is not the production managed-curve source.
4. **AAC treatment.** Treat 803,000 m3/yr as a policy ceiling. The benchmark of
   record is the opening-first run, whose ten-decade volumes are inside the
   8,030,000-8,031,000 m3 band. The AAC is not a validation statistic and not a field
   operability guarantee.
5. **Use.** Use the model for strategic sensitivity analysis, provenance review,
   and method development. Do not use it for cutblock layout, tenure decisions,
   investment cases, certification, or legal determinations.

The opening-first schedule covers all 21 managed AUs (5,587
openings, 115,304.5 ha scheduled, 172,207.3 ha patch area). It is a
deterministic seed, not an optimized plan.

## Consequences

- The benchmark is reproducible from public data and explicitly records its
  unknowns.
- Results remain conditional on the predecessor THLB and TSR assumptions. A
  different reviewed netdown or yield table could change the area and volume
  conclusions.
- Height accuracy has been checked against independent RESULTS cover heights.
  Volume, DBH, and mortality remain incompletely validated, so the model must not
  be presented as a calibrated growth-and-yield audit.
- Any later reviewed GBR netdown, TSR cycle, or validation result should trigger
  a new ADR rather than a silent profile change.
- No optimality claim is made for deterministic seeds, bounded searches, or
  heuristic schedules.

## Alternatives considered

- **Clip to a district or tenure.** Rejected: the AAC is a TSA-wide legal
  determination, so a clip would not answer the benchmark question.
- **Wait for a reviewed GBR netdown.** Rejected for this phase: none is
  available. The predecessor derivation is recorded as a limit.
- **Keep the VDYP-transform managed curves.** Rejected for production: the
  transform is not accepted TIPSY output and carried a VRI volume-adjustment
  factor into OAF1. The dated VDYP-transform run is retained as a backup.
- **Adopt a managed-site-index curve on height evidence alone.** Rejected for
  production: height is only one dimension, and volume/DBH/mortality validation
  remains incomplete.
