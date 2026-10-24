# TSR-consistent BatchTIPSY curves: TSA 46

Date: 2026-10-24
Status: production managed-curve lane; VDYP-transform run retained as a dated
backup at `runtime/tsa46_full_vdyp_20261023`.

## Why this lane exists

The first lane used `managed_curve_mode: vdyp_transform`. That transform scaled
the natural VDYP curves and was not an accepted TIPSY yield. It also carried
the VRI volume-adjustment factor into the BatchTIPSY `OAF1` field. The
predecessor TSRs use OAF1 = 0.85, and that correction alone changes managed
volume by about one third.

## TSR assumptions

- Source TSRs: North Coast TSA TSR 3 Data Package (2007, Table 5.2) and Mid Coast TSA TSR 3 Data Package (2011).
- Future stands regenerate to the existing analysis-unit species composition.
  The mix is area-weighted from the calibrated VRI checkpoint and restricted to
  conifers. Up to three species are carried.
- Stem density: 4,444 stems/ha. This is the TIPSY cap for North Coast
  natural regeneration (TSA 46) and the Kingcome planted density (TSA 47).
- OAF1 = 0.85 and OAF2 = 0.95.
- Regeneration delay: 1 year for cedar/yellow-cedar leading AUs, 2 years otherwise.
- The AU-level inventory site index is applied to every planted species, because
  the AU table has one site-index value per AU rather than species-specific
  values.

These are **predecessor-TSR assumptions**, not a reviewed GBR yield table. TSA
46 has no dedicated provincial TSR cycle.

## Lane

1. `scripts/build_tsr_tipsy_input.py` derives the species mix and writes the
   BatchTIPSY input.
2. `scripts/run_tsr_tipsy.py` runs BatchTIPSY 4.7 under the Wine/Xvfb lane and
   parses the transposed output. The 21 AUs produce 756 long
   curve rows (ages 0-350 in ten-year steps).
3. `scripts/build_tsr_bundle.py` interpolates the curves to annual ages 1-300
   and replaces only the treated curves in a bundle copy.
4. `scripts/build_full_tsa46_model.sh` exports Patchworks, merges safe
   slivers, compiles the ws4 matrix, and writes the UI geometry.
5. The opening-first schedule is built with the touching-block topology and
   simulated with the patch account.

Command:

```bash
export FEMIC_BTC_WINEPREFIX=/path/to/wineprefix-mono
export FEMIC_BTC_DISPLAY=:99
TSA=46 bash scripts/build_tsr_lane.sh
```

The BatchTIPSY install and Wine prefix are not committed. See
`runbooks/tipsy-btc-linux-wine.md` in the North Island instance for the
one-time setup.

## Result

- Managed AUs: 21
- Topology edges: 244,270
- Openings: 5,587
- Scheduled blocks: 8,383
- Scheduled area: 115,304.5 ha
- Opening range: 5.3-40.0 ha
- Patch area: 172,207.3 ha
- Patch classes: 100% in the 5-40 ha class at every year
- Ten-decade AAC: 8,030,924.8-8,030,987.3 m3, all ten inside 8,030,000-8,031,000 m3
- Calibrated managed area: 268,970 ha
- Harvest coverage: all 21 managed AUs covered

## Caveats

- The species mix is a VRI-derived regeneration assumption, not an operational
  prescription.
- The uniform site index across species is a simplification.
- Genetic gain is not applied.
- The opening-first schedule is a deterministic seed, not an optimized plan.
- The BatchTIPSY output is only as good as the AU definitions and TSR
  assumptions above.

## Related

- `notes/reference/opening-policy.md`
- `notes/reference/tsr.md`
- `notes/reference/ws4-build.md`
- `config/tipsy/tsa46.yaml`
