# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Fixed

- Tooling: Reject duplicate JSON object keys during profile validation.

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
