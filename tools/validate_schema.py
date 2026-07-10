#!/usr/bin/env python3
"""Validate public Host Link JSON instances against their published schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema" / "kv_device_ranges.schema.json"
CATALOG = ROOT / "device-ranges" / "kv_device_ranges.json"
NEGATIVE_FIXTURE = ROOT / "tests" / "fixtures" / "kv_device_ranges.invalid-property.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def format_errors(validator: Draft202012Validator, instance: Any) -> list[str]:
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    return [f"/{'/'.join(str(part) for part in error.absolute_path)}: {error.message}" for error in errors]


def main() -> int:
    schema = load_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    canonical_errors = format_errors(validator, load_json(CATALOG))
    if canonical_errors:
        raise ValueError("canonical catalog failed schema validation:\n" + "\n".join(canonical_errors))

    negative_errors = format_errors(validator, load_json(NEGATIVE_FIXTURE))
    if not negative_errors:
        raise ValueError("negative fixture unexpectedly passed schema validation")
    if not any("unexpected_property" in error and "Additional properties" in error for error in negative_errors):
        raise ValueError("negative fixture failed for an unexpected reason:\n" + "\n".join(negative_errors))

    print(f"validated {CATALOG.relative_to(ROOT)} against {SCHEMA.relative_to(ROOT)}")
    print(f"confirmed negative fixture rejection: {NEGATIVE_FIXTURE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
