#!/usr/bin/env python3
"""Validate the canonical KEYENCE KV Host Link profile JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "device-ranges" / "kv_device_ranges.json"


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_catalog() -> dict[str, Any]:
    return json.loads(CATALOG.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_catalog(payload: dict[str, Any]) -> None:
    require(payload.get("schema_version") == 1, "schema_version must be 1")
    require(payload.get("scope") == "keyence-kv-hostlink", "unexpected scope")

    profiles = payload.get("profiles")
    require(isinstance(profiles, dict) and profiles, "profiles must be a non-empty object")
    profile_ids = list(profiles)
    require(len(profile_ids) == len(set(profile_ids)), "profile IDs must be unique")

    for profile_id, profile in profiles.items():
        require(profile_id.startswith("keyence:"), f"{profile_id}: invalid vendor prefix")
        require(profile.get("display_name"), f"{profile_id}: display_name is required")
        notation = profile.get("address_notation")
        require(notation in {"native", "xym"}, f"{profile_id}: invalid address_notation")
        base = profile.get("base_profile")
        if notation == "xym":
            require(base in profiles, f"{profile_id}: base_profile must reference an existing profile")
            require(profiles[base].get("address_notation") == "native", f"{profile_id}: base must be native")
        else:
            require(base is None, f"{profile_id}: native profile must not set base_profile")

    rows = payload.get("device_range_rows")
    require(isinstance(rows, list) and rows, "device_range_rows must be a non-empty array")
    seen_devices: set[str] = set()
    for row in rows:
        device_type = row.get("device_type")
        require(isinstance(device_type, str) and device_type, "device_type is required")
        device_name = row.get("device_name")
        require(isinstance(device_name, str) and device_name, f"{device_type}: device_name is required")
        require(device_type not in seen_devices, f"duplicate device_type {device_type}")
        seen_devices.add(device_type)
        require(row.get("notation") in {"decimal", "hexadecimal"}, f"{device_type}: invalid notation")
        ranges = row.get("ranges")
        require(isinstance(ranges, dict), f"{device_type}: ranges must be an object")
        require(list(ranges) == profile_ids, f"{device_type}: range profile keys must match profile order")
        for profile_id, range_text in ranges.items():
            require(isinstance(range_text, str) and range_text, f"{device_type}/{profile_id}: empty range")


def main() -> int:
    validate_catalog(load_catalog())
    print(f"validated {CATALOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
