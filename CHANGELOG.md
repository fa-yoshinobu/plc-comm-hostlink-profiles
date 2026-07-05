# Changelog

## v1.1.0 - 2026-07-06

- Added official English `device_name` labels to every device-range row
  (Relay, Work relay, Index register, Digital trimmer, etc.), sourced from the
  KV-XLE02 and KV-8000/7000 series manuals (evidence: `evidence/kv_device_master_20260705.md`).
- Added `TC`/`TS`/`CC`/`CS` (timer/counter current and set value) device rows,
  mirroring the `T`/`C` per-model ranges. A single timer/counter instance is
  addressed by contact (`T`/`C`), current value (`TC`/`CC`), and set value
  (`TS`/`CS`).

## Unreleased

- Shortened XYM profile display names from `(XYM notation)` to `(XYM)` for
  UI selector labels.
- Added the initial canonical KEYENCE KV Host Link profile and device-range
  catalog for `v1.0.0` preparation.
