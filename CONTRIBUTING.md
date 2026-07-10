# Contributing

This repository is the canonical source for KEYENCE KV Host Link profile data.

## Add Or Change A Profile

1. Add an evidence file under `evidence/`.
2. Update `device-ranges/kv_device_ranges.json` with one profile entry or one
   device-range row change, including a `display_name` and evidence reference.
3. Run:

   ```powershell
   python -m pip install -r requirements-dev.txt
   python tools/validate_profiles.py
   python tools/validate_schema.py
   python tools/generate_profile_tables.py
   ```

4. Confirm `python tools/generate_profile_tables.py --check` passes.
5. Create a new tag for the data update, then update downstream fixture sync
   scripts to that tag in the same release wave.

Do not move or replace a published tag. Field additions are compatible and keep
`schema_version` unchanged. Rename, remove, or semantic changes require a
schema version increment.

## Evidence Rules

Range changes need manual, vendor, or live-device evidence before adoption.
Implementation guard failures are implementation evidence, not PLC evidence.

Keep verification logs and decision records in `evidence/`, not in generated
user tables.

Generated user-facing profile tables follow the shared style defined by the
SLMP profile repository:
https://github.com/fa-yoshinobu/plc-comm-slmp-profiles/blob/main/docs/tables_style.md

Keep style changes in `tools/generate_profile_tables.py`; do not hand-edit
files under `tables/`.
