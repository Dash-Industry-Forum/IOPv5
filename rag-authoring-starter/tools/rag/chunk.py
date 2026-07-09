#!/usr/bin/env python3
"""
Chunk extracted text files into heading-aware, provenance-tagged JSONL chunks.

Reads every *.extracted.txt (plus its .json sidecar) under rag/corpus/ and
writes rag/chunks/<id>.jsonl, one JSON object per chunk with fields:

    id, chunk_index, text, source_id, title, status, target_part,
    source_path, heading, tags

Chunking strategy (stdlib only):
- Split on blank-line paragraphs.
- Track the most recent heading-like line (short, title-ish, or numbered).
- Accumulate paragraphs into chunks up to ~MAX_CHARS, breaking on heading
  boundaries so a chunk stays within a single section where possible.

Usage:
    python tools/rag/chunk.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "rag" / "corpus"
CHUNKS = ROOT / "rag" / "chunks"

MAX_CHARS = 1200
OVERLAP_CHARS = 150

# Matches "1", "1.2", "A.3.1", optionally followed by a title.
NUMBERED_HEADING = re.compile(r"^(?:[A-Z]?\d+(?:\.\d+)*)\s+\S")


def is_heading(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if NUMBERED_HEADING.match(stripped):
        return True
    # Short, non-sentence lines that look like titles.
    if len(stripped) <= 80 and not stripped.endswith((".", ",", ";", ":")):
        words = stripped.split()
        if 1 <= len(words) <= 10 and stripped[0].isupper():
            return True
    return False


def paragraphs(text: str) -> list[str]:
    blocks = re.split(r"\n\s*\n", text)
    return [b.strip() for b in blocks if b.strip()]


def chunk_text(text: str) -> list[tuple[str, str]]:
    """Return list of (heading, chunk_text)."""
    chunks: list[tuple[str, str]] = []
    current_heading = ""
    buffer: list[str] = []
    buffer_len = 0

    def flush() -> None:
        nonlocal buffer, buffer_len
        if buffer:
            chunks.append((current_heading, "\n\n".join(buffer)))
            buffer = []
            buffer_len = 0

    for para in paragraphs(text):
        first_line = para.splitlines()[0].strip()
        if is_heading(first_line) and len(para) <= 120:
            # Heading boundary: start a new section.
            flush()
            current_heading = first_line
            buffer.append(para)
            buffer_len += len(para)
            continue

        if buffer_len + len(para) > MAX_CHARS and buffer:
            flush()
            # Simple overlap: carry the tail of the previous chunk.
            if chunks and OVERLAP_CHARS:
                tail = chunks[-1][1][-OVERLAP_CHARS:]
                buffer.append(tail)
                buffer_len += len(tail)

        buffer.append(para)
        buffer_len += len(para)

    flush()
    return chunks


def process_sidecar(sidecar_path: Path) -> int:
    meta = json.loads(sidecar_path.read_text(encoding="utf-8"))
    txt_path = ROOT / meta["extracted_path"]
    if not txt_path.exists():
        print(f"[skip] extracted text missing for {meta.get('id')}")
        return 0

    text = txt_path.read_text(encoding="utf-8", errors="replace")
    source_id = meta.get("id") or txt_path.stem
    out_path = CHUNKS / f"{source_id}.jsonl"

    written = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for index, (heading, chunk) in enumerate(chunk_text(text)):
            record = {
                "id": f"{source_id}#{index}",
                "chunk_index": index,
                "text": chunk,
                "heading": heading,
                "source_id": source_id,
                "title": meta.get("title", ""),
                "status": meta.get("status", ""),
                "target_part": meta.get("target_part", ""),
                "source_path": meta.get("source_path", ""),
                "tags": meta.get("tags", []),
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

    print(f"[ok]   {source_id:<32} {written} chunks -> {out_path.relative_to(ROOT)}")
    return written


def main() -> None:
    CHUNKS.mkdir(parents=True, exist_ok=True)
    sidecars = sorted(CORPUS.rglob("*.extracted.json"))
    if not sidecars:
        print(
            "No extracted sources found. Run tools/ingest/extract_text.py first, "
            "after adding documents under rag/corpus/."
        )
        return

    total = 0
    for sidecar in sidecars:
        total += process_sidecar(sidecar)
    print(f"\nWrote {total} chunks from {len(sidecars)} sources.")


if __name__ == "__main__":
    main()
