# TSR and AAC provenance

Status: the GBR North TSA 46 has no dedicated TSR cycle in the provincial TSR
folder. The current AAC comes from the Great Bear Rainforest (Forest
Management) Act and B.C. Reg. 328/2016. The predecessor TSA TSR packages are
the available public netdown evidence.

## Current AAC

| Item | Value | Source |
| --- | ---: | --- |
| GBR North TSA AAC | 803,000 m3/yr | B.C. Reg. 328/2016, s. 5; effective 2017-01-01 |
| GBR South TSA AAC | 830,500 m3/yr | B.C. Reg. 328/2016, s. 10; effective 2017-01-01 |

The provincial TSR pages report the same current AAC values as of January 1,
2017:
`https://www2.gov.bc.ca/.../allowable-annual-cut-timber-supply-areas/great-bear-rainforest-north`
and `.../great-bear-rainforest-south`.

## TSR document materialization

The canonical FEMIC TSR index (`femic tsr index`) records 0 documents under
`TSA/Great_Bear_Rainforest_North_46/` and 0 under
`TSA/Great_Bear_Rainforest_South_47/`.

The built-in fetch and extract functions were run against the predecessor TSAs
that the GBR order replaced:

```bash
python -m femic tsr fetch --tsa 19 --tsa 21 --tsa 33 --tsa 37
python -m femic tsr extract --tsa 19 --tsa 21 --tsa 33 --tsa 37
```

Result: 77 of 78 selected PDFs were cached and extracted (one fetch failure),
producing 6,189 candidate facts. The corpus is cached under `~/.femic/tsr/` and
is not committed.

## Adopted THLB facts

| Fact | Value | Provenance |
| --- | ---: | --- |
| Former North Coast TSA current THLB | 145,808 ha | TSR 2007 rationale, p. 21 |
| Former Mid Coast TSA current effective THLB | 123,162 ha | TSR 2011 rationale, p. 5 |
| Derived GBR North THLB target | 268,970 ha | sum of the two predecessor current THLBs |

TSA 46 is the union of the former North Coast and Mid Coast boundaries. The
symmetric difference is 5,268.5 ha (0.06%), so the predecessor THLB sum is the
defensible first target.

This is a predecessor-value derivation, not a reviewed GBR netdown. Replace it
when a GBR land-base netdown is available. The adopted facts are in
`config/tsr/overlay.yaml`.

## Predecessor mapping

| GBR TSA | Predecessor TSAs |
| --- | --- |
| GBR North TSA 46 | North Coast (21), Mid Coast (19) |
| GBR South TSA 47 | Kingcome (33), Strathcona (37) |
