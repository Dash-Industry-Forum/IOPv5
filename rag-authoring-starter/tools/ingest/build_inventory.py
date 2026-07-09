#!/usr/bin/env python3
"""
Build a Markdown inventory from rag/sources.yaml.

The script intentionally uses only the Python standard library plus optional
PyYAML. If PyYAML is unavailable, it falls back to a small parser that supports
the simple manifest shape used by this starter.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "rag" / "sources.yaml"
OUT = ROOT / "docs" / "document-inventory.md"


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value.startswith('"') and value.endswith('""):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [part.strip().strip('"').strip("'") for part in inner.split(",")]
    return value


def _fallback_yaml_sources(text: str) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped or stripped.startswith("#") or stripped == "sources:":
            continue

        if stripped.startswith("- "):
            if current:
                sources.append(current)
            current = {}
            rest = stripped[2:].strip()
            if rest:
                key, value = rest.split(":", 1)
                current[key.strip()] = _parse_scalar(value)
            continue

        if current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = _parse_scalar(value)

    if current:
        sources.append(current)

    return sources


def load_sources() -> list[dict[str, Any]]:
    text = SOURCES.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text) or {}
        return list(data.get("sources", []))
    except Exception:
        return _fallback_yaml_sources(text)


def guess_local_status(corpus_path: str) -> str:
    if not corpus_path:
        return "not specified"
    path = ROOT / corpus_path
    return "present" if path.exists() else "missing"


def build_inventory(sources: list[dict[str, Any]]) -> str:
    rows = []
    for source in sources:
        tags = source.get("tags", [])
        if isinstance(tags, list):
            tag_text = ", ".join(str(t) for t in tags)
        else:
            tag_text = str(tags)

        rows.append(
            [
                source.get("id", ""),
                source.get("title", ""),
                source.get("type", ""),
                source.get("status", ""),
                source.get("target_part", ""),
                guess_local_status(str(source.get("corpus_path", ""))),
                str(source.get("corpus_path", "")),
                tag_text,
            ]
        )

    headers = [
        "ID",
        "Title",
        "Type",
        "Status",
        "Target part",
        "Local file",
        "Corpus path",
        "Tags",
    ]

    def esc(value: Any) -> str:
        return re.sub(r"\s+", " ", str(value)).replace("|", "\\|").strip()

    lines = [
        "# DASH-IF IOP v5 Document Inventory",
        "",
        "Generated from `rag/sources.yaml`.",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for row in rows:
        lines.append("| " + " | ".join(esc(cell) for cell in row) + " |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `Local file` reports whether the manifest path currently exists under this starter project.",
            "- Missing files may be intentionally excluded from Git because of publication or access restrictions.",
            "- Use this inventory as the first review checkpoint before building a RAG index.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    sources = load_sources()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_inventory(sources), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(sources)} sources")


if __name__ == "__main__":
    main()