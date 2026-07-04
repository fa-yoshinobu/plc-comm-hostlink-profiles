#!/usr/bin/env python3
"""Generate Markdown comparison tables from the canonical Host Link JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "device-ranges" / "kv_device_ranges.json"
TABLE_DIR = ROOT / "tables"


def load_catalog() -> dict[str, Any]:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def cell(value: object) -> str:
    text = "" if value is None else str(value)
    text = text.replace("|", "\\|")
    return text if text == "-" else f"`{text}`"


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell(value) for value in row) + " |")
    return "\n".join(lines)


def profile_table(payload: dict[str, Any]) -> str:
    rows: list[list[object]] = []
    for profile_id, profile in payload["profiles"].items():
        rows.append(
            [
                profile_id,
                profile["display_name"],
                profile["source_label"],
                profile["address_notation"],
                profile.get("base_profile", ""),
            ]
        )
    body = markdown_table(
        ["Profile ID", "Display name", "Source label", "Notation", "Base profile"],
        rows,
    )
    return (
        "# KEYENCE KV Host Link Profiles\n\n"
        "Generated from `device-ranges/kv_device_ranges.json`.\n\n"
        f"{body}\n"
    )


def range_table(payload: dict[str, Any]) -> str:
    profiles = list(payload["profiles"])
    headers = ["Device", "Notation"] + [payload["profiles"][profile]["source_label"] for profile in profiles]
    rows: list[list[object]] = []
    for row in payload["device_range_rows"]:
        rows.append(
            [row["device_type"], row["notation"]]
            + [row["ranges"][profile] for profile in profiles]
        )
    body = markdown_table(headers, rows)
    return (
        "# KEYENCE KV Host Link Device Ranges\n\n"
        "Generated from `device-ranges/kv_device_ranges.json`.\n\n"
        "A `-` value means the device row is not available in that catalog profile.\n\n"
        f"{body}\n"
    )


def write_or_check(path: Path, content: str, check: bool) -> bool:
    if check:
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            print(f"stale generated table: {path.relative_to(ROOT)}")
            return False
        print(f"fresh generated table: {path.relative_to(ROOT)}")
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated tables are stale")
    args = parser.parse_args()

    payload = load_catalog()
    outputs = {
        TABLE_DIR / "kv_profile_parameters.md": profile_table(payload),
        TABLE_DIR / "kv_device_ranges.md": range_table(payload),
    }
    ok = all(write_or_check(path, content, args.check) for path, content in outputs.items())
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

