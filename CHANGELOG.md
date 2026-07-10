# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [1.2.0] - 2026-07-10

### Fixed

- Catalog: Corrected ten device range cells against live PLC hardware and the
  KEYENCE simulator. `VM` widens to `VM0-9999` on `keyence:kv-nano` and to
  `VM0-59999` on `keyence:kv-3000` / `keyence:kv-5000`; `Z` widens to `Z1-23` on
  `keyence:kv-8000`. `CTH` narrows to `CTH0-1` on `keyence:kv-3000-xym` and
  `keyence:kv-5000-xym`, which also removes an internal inconsistency with their
  base profiles. The `-xym` notation variants track their base profiles in every
  case. The printed manuals contain errata for these cells, so the observed
  device behaviour was adopted. See
  `evidence/kv_device_ranges_live_verification_20260710.md`.
- Tooling: Reject duplicate JSON object keys during profile validation.
- Schema: Define the additive `device_name` row property used by the canonical
  catalog and validate the public catalog plus a negative fixture in CI.

## [1.1.1] - 2026-07-06

### Changed
- Restyled generated profile-reference tables to match the shared SLMP manual
  style, including generated headers, purpose text, verified-model status,
  plain table cells, and cell-reading appendices.

## [1.1.0] - 2026-07-06

### Added
- Added official English `device_name` labels to every device-range row
  (Relay, Work relay, Index register, Digital trimmer, etc.), sourced from the
  KV-XLE02 and KV-8000/7000 series manuals (evidence: `evidence/kv_device_master_20260705.md`).
- Added `TC`/`TS`/`CC`/`CS` (timer/counter current and set value) device rows,
  mirroring the `T`/`C` per-model ranges. A single timer/counter instance is
  addressed by contact (`T`/`C`), current value (`TC`/`CC`), and set value
  (`TS`/`CS`).

## [1.0.1] - 2026-07-05

### Changed
- Shortened XYM profile display names from `(XYM notation)` to `(XYM)` for
  UI selector labels.

## [1.0.0] - 2026-07-05

### Added
- Added the initial canonical KEYENCE KV Host Link profile and device-range
  catalog for `v1.0.0` preparation.
