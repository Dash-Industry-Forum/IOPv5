# RAG corpus

Drop source documents here, organised by provenance. Paths must match
`rag/corpus_path` entries in `rag/sources.yaml`.

| Folder | Contents |
|---|---|
| `published/` | Officially published DASH-IF IOP v5 parts |
| `drafts/` | Working drafts not yet published |
| `change-requests/` | CR inputs (e.g. Low-Latency r8/r9) |
| `legacy-v4/` | DASH-IF IOP v4.x for migration mapping |
| `mpeg/` | External standards (ISO/IEC DASH, CMAF) |
| `external-examples/` | Third-party example content |
| `website/` | Website-sourced text |

## Access policy

Do **not** commit private MPEG or unpublished DASH-IF documents to public Git
unless publication rights are confirmed. The default `.gitignore` excludes
`drafts/`, `change-requests/`, `legacy-v4/`, and `mpeg/` binaries so they can be
kept locally while the folder structure and manifest stay public.

## Workflow

1. Add files matching the `corpus_path` entries in `rag/sources.yaml`.
2. `python tools/ingest/extract_text.py`  -> `*.extracted.txt` + `.json`
3. `python tools/rag/chunk.py`            -> `rag/chunks/*.jsonl`
4. `python tools/rag/build_index.py`      -> `rag/indexes/index.json`
5. `python tools/rag/query.py "..."`      -> ranked, provenance-tagged results
