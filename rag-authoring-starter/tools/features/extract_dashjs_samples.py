#!/usr/bin/env python3
"""Extract dash.js sample catalog into a normalized YAML-like listing.

The script reads dash.js `samples.json` and emits a compact list that can be used
to map dash.js sample coverage into `rag/features/feature-inventory.yaml`.

Usage:
  python tools/features/extract_dashjs_samples.py \
    --input path/to/samples.json

If no input is supplied, the current public dash.js samples catalog is fetched.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_URL = "https://reference.dashif.org/dash.js/latest/samples/samples.json"


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def load_samples(path: Path | None) -> list[dict[str, Any]]:
    if path:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    request = urllib.request.Request(
        DEFAULT_URL,
        headers={"User-Agent": "IOPv5-dashjs-sample-extractor/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="Local dash.js samples.json")
    args = parser.parse_args()

    sections = load_samples(args.input)
    print("# Normalized dash.js samples")
    print("# Source:", str(args.input) if args.input else DEFAULT_URL)
    print("dashjs_samples:")

    for section in sections:
        section_name = section.get("section", "")
        for sample in section.get("samples", []):
            title = sample.get("title", "")
            sample_id = f"dashjs-{slug(section_name)}-{slug(title)}"
            print(f"  - id: {sample_id}")
            print(f"    section: {json.dumps(section_name, ensure_ascii=False)}")
            print(f"    title: {json.dumps(title, ensure_ascii=False)}")
            if sample.get("href"):
                print(f"    href: {json.dumps(sample['href'], ensure_ascii=False)}")
            labels = sample.get("labels") or []
            if labels:
                print("    labels:")
                for label in labels:
                    print(f"      - {json.dumps(label, ensure_ascii=False)}")
            description = (sample.get("description") or "").strip()
            if description:
                print(f"    description: {json.dumps(description, ensure_ascii=False)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())