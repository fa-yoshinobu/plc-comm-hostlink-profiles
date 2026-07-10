# Host Link Device Range Live Verification 2026-07-10

## Scope

Verification of the KEYENCE KV Host Link device range rows in
`device-ranges/kv_device_ranges.json` against live PLC hardware and the KEYENCE
simulator. Ten range cells were corrected as a result.

## Method

The maintainer exercised each device range boundary on real PLC hardware and on
the KEYENCE simulator, and compared the accepted address bounds against the
catalog.

**The printed manuals contain errata for the corrected cells.** Where the manual
and the observed device behaviour disagreed, the observed behaviour was adopted.
This supersedes the manual-derived and implementation-derived values recorded in
`evidence/hostlink_device_ranges_source_20260705.md`, which bootstrapped the
catalog from `plc-comm-hostlink-python` without live verification.

## Corrections

| Device | Profiles | Previous | Verified |
| --- | --- | --- | --- |
| `VM` | `keyence:kv-nano`, `keyence:kv-nano-xym` | `VM0-9499` | `VM0-9999` |
| `VM` | `keyence:kv-3000`, `keyence:kv-3000-xym`, `keyence:kv-5000`, `keyence:kv-5000-xym` | `VM0-49999` | `VM0-59999` |
| `Z` | `keyence:kv-8000`, `keyence:kv-8000-xym` | `Z1-12` | `Z1-23` |
| `CTH` | `keyence:kv-3000-xym`, `keyence:kv-5000-xym` | `CTH0-3` | `CTH0-1` |

## Notes

The `CTH` correction also removes an internal inconsistency in the catalog. The
`-xym` profiles are notation variants of their base profiles and must expose the
same device ranges, but `keyence:kv-3000` and `keyence:kv-5000` already declared
`CTH0-1` while their `-xym` twins declared `CTH0-3`. The verified value is
`CTH0-1` for all four.

`CTH` is the only device whose range narrows. Addresses `CTH2` and `CTH3` were
previously accepted on `keyence:kv-3000-xym` and `keyence:kv-5000-xym` and are
now rejected, matching the base profiles and the observed hardware behaviour.

The `keyence:kv-x500` and `keyence:kv-x500-xym` rows are unchanged.

Range semantics are unchanged: ranges remain catalog data for profile selection,
UI address pickers, and application-layer checks, and are not a guarantee that
every address can be read or written on a connected PLC.
