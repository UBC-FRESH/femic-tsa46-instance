# Runtime provenance refresh

Date: 2026-10-25
Phase: P50

The current TSA 46 production matrix was refreshed so its sidecar matches the
tracked provenance. The matrix tables were not rewritten.

| Item | Value |
| --- | --- |
| Matrix | `runtime/tsa46_full/matrix` |
| Sidecar | `runtime/tsa46_full/matrix/data_quality.yaml` |
| Pre-refresh sidecar | absent |
| Post-refresh sidecar SHA-256 | `50a48f25c515d0a17f231574ba79b9235af5067bd51e61fcda42baf58d30a13e` |
| Manifest SHA-256 | `8f0c11de84c32c02e6ff9254cb2d6765cb78beeaa456eb33f546ebbe183d4487` |
| Quality report | `runtime/tsa46_full/quality/p50/quality.json` |
| Quality report SHA-256 | `fb704a305879bdf04aa0c734be5fe91c937a909dff28d283f94d8a1cf13b635c` |
| Status | ok |
| Tables | 12 |
| Warnings | none |

## Command

```bash
python -m ws4.cli quality \
  --dataset runtime/tsa46_full/matrix \
  --sidecar config/dataset_quality.yaml \
  --out runtime/tsa46_full/quality/p50 \
  --check
```

Exit status: 0.

## Checks

- metadata: ok
- tables: ok (12 tables have rows)
- provenance: ok (`data_quality.yaml` loaded)
- target_coverage: not-applicable (no targets supplied)

## Notes

- The runtime quality report is local and untracked.
- The dated VDYP-transform backup matrix was not refreshed.
- No curve, target, or AAC input changed.
