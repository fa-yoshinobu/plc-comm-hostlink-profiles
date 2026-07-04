# Host Link Device Range Source Notes 2026-07-05

## Scope

Initial canonicalization of KEYENCE KV Host Link profile IDs, display names,
XYM notation variants, and device range rows.

## Source Implementations

| Repository | File | Role |
| --- | --- | --- |
| `plc-comm-hostlink-python` | `src/hostlink/device_ranges.py` | Seed source. Contains the maintained profile labels, canonical IDs, and full device range table. |
| `plc-comm-hostlink-dotnet` | `src/PlcComm.KvHostLink/KvHostLinkDeviceRanges.cs` | Cross-check source for the same full device range table. |
| `plc-comm-hostlink-rust` | `src/device_ranges.rs` | Cross-check source for the same full device range table. |
| `node-red-contrib-plc-comm-kvhostlink` | `lib/hostlink/plc-profile.js` | Cross-check source for canonical PLC profile IDs. |

## Decision

Adopt the Python table as the bootstrap source because it already stores each
profile as a `(display label, canonical ID)` pair. Downstream fixture tests in
the implementation repositories compare their embedded data against
`device-ranges/kv_device_ranges.json`.

No live PLC communication was performed for this canonicalization step.

