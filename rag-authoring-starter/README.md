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

## Recommended pilot

The first pilot should focus on **Part 4: Live and Low-Latency Services** because it has:

- existing v5 draft material,
- the Low-Latency r8/r9 change-request inputs,
- dependencies on MPEG DASH and CMAF updates,
- clear migration and reconciliation needs.

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
5. For the Part 4 pilot, add the r8/r9 CR inputs and run `delta_report.py`.