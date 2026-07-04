[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# KEYENCE KV Host Link Profiles

Canonical KEYENCE KV Host Link profile data shared by the `plc-comm-hostlink-*`
libraries.

The canonical device-range catalog is [kv_device_ranges.json](device-ranges/kv_device_ranges.json).
Downstream libraries should import a fixed tag from this repository and keep
fixture tests that compare their embedded data against the canonical JSON.

## Profile Data

The catalog defines the supported canonical PLC profile IDs, short
`display_name` values for UI selectors, the native/XYM notation relationship,
and the device range rows for each profile.

Ranges are catalog data for profile selection, UI address pickers, and
application-layer checks. They are not a production guarantee that every
address can be read or written on a connected PLC.

## Supported PLC Profiles

- `keyence:kv-nano`
- `keyence:kv-nano-xym`
- `keyence:kv-3000`
- `keyence:kv-3000-xym`
- `keyence:kv-5000`
- `keyence:kv-5000-xym`
- `keyence:kv-7000`
- `keyence:kv-7000-xym`
- `keyence:kv-8000`
- `keyence:kv-8000-xym`
- `keyence:kv-x500`
- `keyence:kv-x500-xym`

## Documentation

| Page | Use it for |
| --- | --- |
| [Profile list](tables/kv_profile_parameters.md) | Compare canonical IDs, display names, and native/XYM relationships. |
| [Device ranges](tables/kv_device_ranges.md) | Compare device ranges across the supported KEYENCE KV profiles. |
| [Evidence](evidence/) | Review source notes used to adopt profile data. |

## Generate

Do not edit generated table files by hand.

```powershell
python tools/validate_profiles.py
python tools/generate_profile_tables.py
```

Use `--check` in CI to fail when generated tables are stale.

```powershell
python tools/generate_profile_tables.py --check
```

## Downstream Use

Implementation repositories should import a fixed tag and keep fixture tests
that compare their embedded profile/range data against this repository.

If a JSON schema changes, increment `schema_version` and keep the old tag
available until all downstream libraries have migrated.

## License

| Item | Value |
| --- | --- |
| License | [MIT](LICENSE) |
| Canonical data tag | `v1.0.0` or later |

