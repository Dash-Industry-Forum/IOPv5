#!/usr/bin/env python3
"""Validate executable DASH example registry entries.

The checker intentionally verifies only URL-level properties:
- MPD URLs are reachable and return a DASH-like content type or XML body.
- dash.js launch URLs use the current reference-player query parameters:
  stream=<MPD>, autoLoad=true.
- dash.js stream parameter matches the MPD URL.

It does not verify browser playback success, codec support, DRM license
availability, or application-level event behavior.
"""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ImportError:
        return load_minimal_registry(path)

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a mapping")
    return data


def load_minimal_registry(path: Path) -> dict[str, Any]:
    """Small fallback parser for this registry shape if PyYAML is unavailable."""
    examples: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_examples = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "examples:":
            in_examples = True
            continue
        if not in_examples:
            continue
        if stripped.startswith("candidate_backlog:"):
            break
        if stripped.startswith("- id:"):
            if current:
                examples.append(current)
            current = {"id": stripped.split(":", 1)[1].strip()}
            continue
        if current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip()
    if current:
        examples.append(current)
    return {"examples": examples}


def fetch_head_or_get(url: str, timeout: float) -> tuple[int, str, bytes]:
    headers = {"User-Agent": "IOPv5-executable-example-checker/1.0"}
    request = urllib.request.Request(url, method="HEAD", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.headers.get("Content-Type", ""), b""
    except Exception:
        request = urllib.request.Request(url, method="GET", headers=headers)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(4096)
            return response.status, response.headers.get("Content-Type", ""), body


def validate_dashjs(example: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mpd = str(example.get("mpd", "")).strip()
    dashjs = str(example.get("dashjs", "")).strip()
    if not dashjs:
        return errors

    parsed = urllib.parse.urlparse(dashjs)
    params = urllib.parse.parse_qs(parsed.query)
    stream = params.get("stream", [""])[0]
    autoload = params.get("autoLoad", [""])[0]

    if not stream:
        errors.append("dashjs URL is missing stream=<MPD>")
    elif stream != mpd:
        errors.append(f"dashjs stream parameter does not match mpd: {stream!r} != {mpd!r}")

    if autoload.lower() != "true":
        errors.append("dashjs URL is missing autoLoad=true")

    if "url" in params:
        errors.append("dashjs URL uses obsolete url= parameter")

    return errors


def validate_mpd(example: dict[str, Any], timeout: float) -> list[str]:
    errors: list[str] = []
    url = str(example.get("mpd", "")).strip()
    if not url:
        return ["missing mpd URL"]

    try:
        status, content_type, body = fetch_head_or_get(url, timeout)
    except urllib.error.HTTPError as e:
        return [f"HTTP error for MPD: {e.code} {e.reason}"]
    except Exception as e:
        return [f"failed to fetch MPD: {e}"]

    if status < 200 or status >= 300:
        errors.append(f"unexpected HTTP status for MPD: {status}")

    normalized_type = content_type.lower()
    if body:
        normalized_body = body.lower()
        looks_like_mpd = b"<mpd" in normalized_body or b":mpd" in normalized_body
    else:
        looks_like_mpd = False

    if (
        "application/dash+xml" not in normalized_type
        and "xml" not in normalized_type
        and not looks_like_mpd
    ):
        errors.append(f"MPD response does not look like DASH XML: Content-Type={content_type!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", type=Path)
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    data = load_yaml(args.registry)
    examples = data.get("examples", [])
    if not isinstance(examples, list):
        print("ERROR: registry 'examples' must be a list", file=sys.stderr)
        return 2

    failures = 0
    for example in examples:
        if not isinstance(example, dict):
            print("ERROR: example entry is not a mapping", file=sys.stderr)
            failures += 1
            continue
        example_id = example.get("id", "<missing-id>")
        errors = []
        errors.extend(validate_dashjs(example))
        errors.extend(validate_mpd(example, args.timeout))

        if errors:
            failures += 1
            print(f"FAIL {example_id}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {example_id}")

    if failures:
        print(f"{failures} example(s) failed validation", file=sys.stderr)
        return 1

    print(f"All {len(examples)} executable example(s) passed URL validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())