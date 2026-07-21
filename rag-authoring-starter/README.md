# DASH-IF IOP v5 RAG Authoring Starter

This starter project is a proposed repository scaffold for making `Dash-Industry-Forum/IOPv5` the canonical workspace for DASH-IF IOP v5 source authoring, migration, publication, and RAG-assisted development.

## Goals

- Maintain the multipart DASH-IF IOP v5 documents as structured source files.
- Keep published, draft, legacy, change-request, MPEG, and website sources clearly separated.
- Build a RAG corpus with provenance-aware metadata.
- Support a Bikeshed-first authoring workflow, with a Metanorma proof-of-concept available for evaluation.
- Provide repeatable tooling for document extraction, inventory, chunking, indexing, query, and publication checks.

## Proposed structure

```text
authoring/       DASH-IF boilerplate, templates, style guide, terminology
specs/           one folder per IOP v5 part
rag/             source manifest, corpus, chunks, indexes, reports
tools/           ingestion, RAG, publication, and migration scripts
website/         website integration stubs
docs/            roadmap, decisions, migration maps, open questions
.github/         optional GitHub workflows and templates
```

## Current active project plan

The starter has moved beyond the original Part 4 pilot into a broader IOP v5
authoring and reconciliation workspace.

The current consolidated status update is:

```text
rag/reports/project-status-update-2026-07-21.md
```

The most complete active project-plan package is:

```text
F-0010 Part 5 ad-insertion conformance and cross-part indexing
```

Central index:

```text
rag/reports/part05-f0010-issue-index.md
```

F-0010 defines the proposed implementation order for:

- Part 5 table/figure stabilization,
- DASH-IF ad content MPD validator checks,
- IF-5 multi-Period ad insertion validator checks,
- SCTE-35 MPD Event checks,
- SGAI remote-resolution coverage with dash.js and livesim2,
- clear/encrypted ad insertion playback assets,
- VAST/Open Measurement tracking sample coverage,
- cross-part anchor and terminology harmonization.

## Public/private content policy

Do not commit private MPEG or unpublished DASH-IF documents to a public repository unless their publication status and license permit it. The `rag/corpus/` tree is designed so that private corpora can be maintained locally while public source stubs remain in Git.

## Toolchain

All tools live under `tools/` and are designed to degrade gracefully. The
inventory, chunking, index, and query tools run with the Python standard library
only; text extraction needs the optional packages in `requirements.txt`.

```bash
pip install -r requirements.txt   # optional: enables DOCX/PDF extraction + YAML

python tools/ingest/build_inventory.py     # rag/sources.yaml -> docs/document-inventory.md
python tools/ingest/extract_text.py        # corpus DOCX/PDF -> *.extracted.txt + .json
python tools/rag/chunk.py                  # extracted text -> rag/chunks/*.jsonl
python tools/rag/build_index.py            # chunks -> rag/indexes/index.json
python tools/rag/query.py "segment sequence" --part part04-live-low-latency
python tools/migration/delta_report.py cr-low-latency-live-r8 cr-low-latency-live-r9
python tools/publication/check_links.py    # link / heading / modal-verb checks on specs/
```

## Next steps

1. Install optional dependencies: `pip install -r requirements.txt`.
2. Add source material to `rag/corpus/` according to status and access policy
   (see `rag/corpus/README.md`). Paths must match `corpus_path` in `rag/sources.yaml`.
3. Run `python tools/ingest/build_inventory.py` and review `docs/document-inventory.md`.
4. Run the extract -> chunk -> index -> query pipeline shown above.
5. Create GitHub issues from `rag/reports/part05-f0010-issue-index.md`.
6. Start F-0010-H1 through F-0010-H5 to stabilize Part 5 tables and figures.
7. Continue Part 6 and Part 9 reconciliation while keeping Part 12 conformance
   mapping synchronized.
8. Run `python tools/publication/check_links.py` before commits and pull requests.
