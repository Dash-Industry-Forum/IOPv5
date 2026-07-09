#!/usr/bin/env python3
"""
Extract embedded images from corpus DOCX files into the matching
specs/<target_part>/Images/ folder, and write an image manifest per source.

A .docx is a zip; embedded images live under word/media/. This tool copies them
out (preserving order where possible), names them <source_id>-imgNN.<ext>, and
records a Markdown manifest so editors can decide, per image, whether to:

  - keep the original raster (PNG/JPG), or
  - redraw as Mermaid / PlantUML / draw.io (recommended for EMF/WMF vector art
    and for simple boxes-and-arrows diagrams).

EMF/WMF images are flagged as "redraw recommended" because they are Office
vector drawings that do not render in HTML and are best re-authored as text
diagrams (Mermaid/PlantUML) for a diffable, tool-independent source.

Usage:
    python tools/ingest/extract_images.py                 # all DOCX sources
    python tools/ingest/extract_images.py --id dashif-iop-v5-part4-draft-r1
"""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "rag" / "sources.yaml"
SPECS = ROOT / "specs"

RASTER = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"}
VECTOR_OFFICE = {".emf", ".wmf"}  # not web-renderable; redraw recommended


def load_sources() -> list[dict[str, Any]]:
    text = SOURCES.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        return list((yaml.safe_load(text) or {}).get("sources", []))
    except Exception:
        from build_inventory import _fallback_yaml_sources  # type: ignore

        return _fallback_yaml_sources(text)


def media_sort_key(name: str) -> tuple[int, str]:
    # word/media/image10.png -> sort by the numeric suffix when present.
    stem = Path(name).stem
    digits = "".join(ch for ch in stem if ch.isdigit())
    return (int(digits) if digits else 0, name)


def extract_images(source: dict[str, Any]) -> str:
    corpus_path = str(source.get("corpus_path", "")).strip()
    src = ROOT / corpus_path
    if not corpus_path or not src.exists() or src.suffix.lower() != ".docx":
        return "skip"

    source_id = source.get("id", src.stem)
    target_part = str(source.get("target_part", "")).strip()
    if not target_part or target_part == "multiple":
        images_dir = ROOT / "rag" / "reports" / "images" / source_id
    else:
        images_dir = SPECS / target_part / "Images"
    images_dir.mkdir(parents=True, exist_ok=True)

    manifest_lines = [
        f"# Image manifest: {source_id}",
        "",
        f"Source: `{corpus_path}`",
        "",
        "| # | File | Type | Action | Notes |",
        "|---|---|---|---|---|",
    ]

    count = 0
    with zipfile.ZipFile(src) as zf:
        media = sorted(
            (n for n in zf.namelist() if n.startswith("word/media/")),
            key=media_sort_key,
        )
        for name in media:
            ext = Path(name).suffix.lower()
            count += 1
            out_name = f"{source_id}-img{count:02d}{ext}"
            out_path = images_dir / out_name
            out_path.write_bytes(zf.read(name))

            if ext in VECTOR_OFFICE:
                action = "redraw (Mermaid/PlantUML/draw.io)"
                notes = "Office vector art; not web-renderable"
            elif ext in RASTER:
                action = "keep or redraw"
                notes = "raster; keep if a screenshot/photo"
            else:
                action = "review"
                notes = f"unhandled type {ext}"

            manifest_lines.append(
                f"| {count} | `{out_name}` | {ext.lstrip('.')} | {action} | {notes} |"
            )

    manifest_lines += [
        "",
        "## Guidance",
        "",
        "- **Mermaid** (`<pre class=mermaid>` in Bikeshed) for flow/sequence/"
        "architecture diagrams; renders on GitHub too.",
        "- **PlantUML** (`Diagrams/*.wsd`) matches the DASH-IF convention for UML.",
        "- **draw.io** exported as `*.drawio.svg` for complex bespoke figures.",
        "- Keep original raster only for screenshots/photos not worth redrawing.",
        "",
    ]

    manifest = images_dir / f"{source_id}-images.md"
    manifest.write_text("\n".join(manifest_lines), encoding="utf-8")
    print(f"[ok]   {source_id:<32} {count} image(s) -> {images_dir.relative_to(ROOT)}")
    return "ok"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", help="Extract images from a single source id")
    args = parser.parse_args()

    sources = load_sources()
    if args.id:
        sources = [s for s in sources if s.get("id") == args.id]

    handled = 0
    for source in sources:
        if extract_images(source) == "ok":
            handled += 1
    print(f"\nExtracted images from {handled} DOCX source(s).")


if __name__ == "__main__":
    main()
