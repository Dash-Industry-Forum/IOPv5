#!/usr/bin/env python3
"""
Query the local RAG index built by tools/rag/build_index.py.

Ranks chunks by a TF-IDF cosine-like score and prints the top matches with
provenance (source id, status, target part, heading). Supports filtering by
target part or status to support cross-document comparison and migration work.

Usage:
    python tools/rag/query.py "addressable resync representation"
    python tools/rag/query.py "segment sequence" --part part04-live-low-latency
    python tools/rag/query.py "cbcs" --status published --top 10
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEXES = ROOT / "rag" / "indexes"
TOKEN = re.compile(r"[A-Za-z0-9]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN.findall(text)]


def load_index() -> dict:
    path = INDEXES / "index.json"
    if not path.exists():
        raise SystemExit(
            "No index found. Run tools/rag/build_index.py first."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def score_query(index: dict, query: str) -> list[tuple[float, int]]:
    idf: dict[str, float] = index["idf"]
    inverted: dict[str, list] = index["inverted"]
    n_docs: int = index["n_docs"]

    q_tokens = tokenize(query)
    q_counts = Counter(q_tokens)
    q_len = max(1, len(q_tokens))

    scores = [0.0] * n_docs
    q_weight_sq = 0.0
    for term, tf in q_counts.items():
        w = (tf / q_len) * idf.get(term, 0.0)
        q_weight_sq += w * w
        for doc_idx, doc_tf in inverted.get(term, []):
            scores[doc_idx] += w * (doc_tf * idf.get(term, 0.0))

    q_norm = math.sqrt(q_weight_sq) or 1.0
    ranked = [
        (score / q_norm, idx) for idx, score in enumerate(scores) if score > 0
    ]
    ranked.sort(reverse=True)
    return ranked


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search query text")
    parser.add_argument("--part", help="Filter by target_part (e.g. part04-live-low-latency)")
    parser.add_argument("--status", help="Filter by status (e.g. draft, published)")
    parser.add_argument("--top", type=int, default=8, help="Number of results")
    args = parser.parse_args()

    index = load_index()
    ranked = score_query(index, args.query)
    doc_meta = index["doc_meta"]

    shown = 0
    for score, idx in ranked:
        meta = doc_meta[idx]
        if args.part and meta.get("target_part") != args.part:
            continue
        if args.status and meta.get("status") != args.status:
            continue
        print(f"\n#{shown + 1}  score={score:.4f}  [{meta.get('status')}] {meta.get('target_part')}")
        print(f"    source: {meta.get('source_id')}  chunk: {meta.get('id')}")
        if meta.get("heading"):
            print(f"    heading: {meta['heading']}")
        print(f"    {meta.get('preview')}")
        shown += 1
        if shown >= args.top:
            break

    if shown == 0:
        print("No matches (after filters). Try a broader query or remove filters.")


if __name__ == "__main__":
    main()
