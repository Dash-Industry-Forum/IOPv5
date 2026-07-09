#!/usr/bin/env python3
"""
Build a local search index over the chunks in rag/chunks/*.jsonl.

Two backends:
- If scikit-learn is installed, build a TF-IDF matrix and save it.
- Otherwise, build a stdlib inverted index (term -> postings) with document
  frequencies so query.py can compute a TF-IDF-like score with no dependencies.

Output: rag/indexes/index.json (always) and, if available,
rag/indexes/tfidf.pkl for the sklearn backend.

Usage:
    python tools/rag/build_index.py
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHUNKS = ROOT / "rag" / "chunks"
INDEXES = ROOT / "rag" / "indexes"

TOKEN = re.compile(r"[A-Za-z0-9]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN.findall(text)]


def load_chunks() -> list[dict]:
    records: list[dict] = []
    for path in sorted(CHUNKS.glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def build_stdlib_index(records: list[dict]) -> dict:
    inverted: dict[str, list[list]] = defaultdict(list)  # term -> [[doc_idx, tf], ...]
    doc_meta: list[dict] = []

    for doc_idx, record in enumerate(records):
        tokens = tokenize(record["text"] + " " + record.get("heading", ""))
        counts = Counter(tokens)
        length = max(1, len(tokens))
        for term, tf in counts.items():
            inverted[term].append([doc_idx, tf / length])
        doc_meta.append(
            {
                "id": record["id"],
                "heading": record.get("heading", ""),
                "title": record.get("title", ""),
                "status": record.get("status", ""),
                "target_part": record.get("target_part", ""),
                "source_id": record.get("source_id", ""),
                "source_path": record.get("source_path", ""),
                "preview": record["text"][:280].replace("\n", " "),
            }
        )

    n_docs = len(records)
    idf = {
        term: math.log((1 + n_docs) / (1 + len(postings))) + 1.0
        for term, postings in inverted.items()
    }

    return {
        "backend": "stdlib-tfidf",
        "n_docs": n_docs,
        "idf": idf,
        "inverted": inverted,
        "doc_meta": doc_meta,
    }


def main() -> None:
    INDEXES.mkdir(parents=True, exist_ok=True)
    records = load_chunks()
    if not records:
        print(
            "No chunks found. Run tools/rag/chunk.py first "
            "(which needs extracted corpus text)."
        )
        return

    index = build_stdlib_index(records)
    out = INDEXES / "index.json"
    out.write_text(json.dumps(index), encoding="utf-8")
    print(
        f"[ok] Built {index['backend']} index over {index['n_docs']} chunks "
        f"-> {out.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
