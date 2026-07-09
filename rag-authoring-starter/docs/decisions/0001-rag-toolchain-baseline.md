# ADR 0001: RAG authoring toolchain baseline

- Status: accepted
- Date: 2025

## Context

The starter repository defined a roadmap (Phases 0-6) and a directory scaffold,
but the only tool present (`tools/ingest/build_inventory.py`) contained a syntax
error and had never been run, the `rag/corpus/`, `rag/chunks/`, `rag/indexes/`,
and `rag/reports/` folders were empty and untracked by Git, and the downstream
RAG/migration/publication tools did not exist. As a result, automated agents and
new contributors had nothing runnable to act on.

## Decision

Establish a minimal, dependency-light toolchain that runs out of the box and
degrades gracefully:

1. `tools/ingest/build_inventory.py` (fixed) — manifest -> inventory table.
2. `tools/ingest/extract_text.py` — DOCX/PDF/TXT -> `*.extracted.txt` + JSON
   provenance sidecar. Requires `python-docx` / `pypdf` (optional).
3. `tools/rag/chunk.py` — heading-aware chunker -> `rag/chunks/*.jsonl` (stdlib).
4. `tools/rag/build_index.py` — stdlib TF-IDF inverted index (stdlib).
5. `tools/rag/query.py` — ranked, provenance-tagged search with part/status
   filters (stdlib).
6. `tools/migration/delta_report.py` — structural delta between two sources for
   the Part 4 r8/r9 pilot.
7. `tools/publication/check_links.py` — link / duplicate-heading / modal-verb
   checks over `specs/`.

Supporting changes:

- `requirements.txt` lists optional dependencies.
- `.gitignore` protects proprietary corpus binaries and generated artefacts.
- `.gitkeep` and `rag/corpus/README.md` preserve and document the structure.
- The physically present Part 8 draft was added to `rag/sources.yaml` and used
  to validate the full pipeline end-to-end.

## Consequences

- The pipeline runs with stdlib only for chunk/index/query; extraction is the
  only step needing optional packages.
- Proprietary documents stay local by default; the manifest and structure remain
  public.
- The stdlib TF-IDF index is intentionally simple. A future ADR may introduce an
  embedding backend (e.g. scikit-learn or a vector DB) if recall proves
  insufficient.
