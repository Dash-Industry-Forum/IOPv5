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

## Next steps

1. Populate `rag/sources.yaml` with the available documents.
2. Run `python tools/ingest/build_inventory.py`.
3. Review `docs/document-inventory.md`.
4. Add source material to `rag/corpus/` according to status and access policy.
5. Run the RAG build/query tools once dependencies are installed.