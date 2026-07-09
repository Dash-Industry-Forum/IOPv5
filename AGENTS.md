# AGENTS.md — conventions for AI agents working on IOPv5

This workspace makes `Dash-Industry-Forum/IOPv5` the canonical place to author,
migrate, and RAG-assist DASH-IF IOP v5. This file tells an agent **how to act**
here. For *what* the project is, see `rag-authoring-starter/README.md`; for the
plan, see `rag-authoring-starter/docs/roadmap.md`; for decisions, see
`rag-authoring-starter/docs/decisions/`.

Conventions here are adapted from proven RAG-authoring workflows (e.g. Qualabs
`sgai-for-mpeg-dash`), tailored to a **local, offline-first** environment behind
a TLS-intercepting corporate proxy.

## Golden rule: act, then report

Do not stop at analysis. The prior failure mode of this repo was "the agent does
not act". When a next step is concrete and runnable, **run it**, verify the
output, and only then summarise. Prefer small, verified increments.

## Directory layering (one-directional dependency arrow)

```
rag/corpus/      inputs — source documents (many gitignored per access policy)
   ↓ extract
rag/corpus/*.extracted.txt + .json   derived text + provenance
   ↓ chunk
rag/chunks/*.jsonl                    heading-aware chunks
   ↓ index
rag/indexes/index.json                local TF-IDF index (grounding)
   ↓ query / delta
rag/reports/*.md                      delta + analysis artefacts
specs/<part>/                         authored Bikeshed sources (the deliverable)
```

Never hand-edit a derived artefact (`*.extracted.*`, `rag/chunks/`,
`rag/indexes/`, generated `rag/reports/`). Fix the input or the tool and
regenerate.

## The toolchain (run in this order)

```bash
pip install -r rag-authoring-starter/requirements.txt   # optional deps
cd rag-authoring-starter
python tools/ingest/build_inventory.py       # manifest -> docs/document-inventory.md
python tools/ingest/extract_text.py          # corpus -> *.extracted.txt + .json
python tools/ingest/extract_images.py        # DOCX images -> specs/<part>/Images/ + manifest
python tools/rag/chunk.py                    # -> rag/chunks/*.jsonl
python tools/rag/build_index.py              # -> rag/indexes/index.json
python tools/rag/query.py "<q>" --part <p>   # grounded search
python tools/migration/delta_report.py A B   # structural delta between two sources
python tools/publication/check_links.py      # specs/ link/heading/modal checks
```

Every tool degrades gracefully: chunk/index/query run on stdlib alone;
extraction needs `python-docx` / `pypdf`.

## Grounding (local RAG = our NotebookLM)

Before writing normative prose, **ground it** by querying the local index and
citing the source id + chunk. When you assert a fact from a source, note the
provenance (`source_id#chunk`) so reviewers can trace it. This mirrors the
`[GROUNDED_BY=...]` audit tag used in comparable projects; here grounding is
local and offline.

## Authoring convention (reused from DASH-IF-IOP)

We **reuse the DASH-IF-IOP authoring workflow, not its content**. Per part:

```
specs/<partNN-name>/
  <partNN-name>.bs      one Bikeshed file: metadata + includes only (Group: dashif)
  NN-<name>.inc.md      prose (Bikeshed-flavoured markdown)
  Images/               static images + extracted-DOCX originals (triage)
  Diagrams/             Mermaid / PlantUML text sources (preferred, diffable)
```

Diagrams: prefer **Mermaid** (renders in Bikeshed + GitHub), use **PlantUML**
(`.wsd`) for UML per DASH-IF convention, **draw.io** (`*.drawio.svg`) for bespoke
figures, keep original raster only for screenshots/photos.

## Building specs with Bikeshed (local, no Docker)

The environment sits behind a corporate TLS-intercepting proxy. This is fully
solved with a one-time setup; use the wrapper thereafter.

One-time setup:
```powershell
pip install -r requirements.txt              # includes wincertstore on Windows
python tools/env/build_ca_bundle.py          # -> build-tools/corp-ca-bundle.pem (from the OS trust store)
$env:REQUESTS_CA_BUNDLE = "$PWD\build-tools\corp-ca-bundle.pem"
$env:SSL_CERT_FILE      = $env:REQUESTS_CA_BUNDLE
python -m bikeshed update                    # now works through the proxy
python tools/env/install_dashif_boilerplate.py   # installs the `dashif` group boilerplate
```

Build (sets the CA env vars for you):
```powershell
./build.ps1                       # build all specs/<part> with a .bs file
./build.ps1 part04-live-low-latency
./build.ps1 part04-live-low-latency -Watch
```

The generated `build-tools/corp-ca-bundle.pem` and `specs/**/*.html` are
gitignored (machine-specific / build output).

## Environment caveats (important)

- **Proxy/TLS (resolved)**: a corporate proxy re-signs TLS, so `requests`/Bikeshed
  fail with `self-signed certificate in certificate chain`. Fixed by
  `tools/env/build_ca_bundle.py`, which exports the OS trust store (incl. the
  proxy root) into a merged bundle that `REQUESTS_CA_BUNDLE`/`SSL_CERT_FILE`
  point at. Never disable verification. Document, don't hide.
- **`Group: dashif`** is a custom Bikeshed group, not built in. Installed locally
  via `tools/env/install_dashif_boilerplate.py` (reuses the DASH-IF-IOP
  boilerplate assets; registers the org in bikeshed's `doctypes.kdl`).
- **No Docker** on this machine currently → local `bikeshed` is the build path.
- **Windows/PowerShell**: quote paths with spaces (several corpus files have
  spaces/parentheses in their names).

## Decisions

Record non-trivial choices as ADRs in `rag-authoring-starter/docs/decisions/`
(`NNNN-title.md`). Keep them short: context, decision, consequences.

## Public/private policy

Do not commit proprietary MPEG or unpublished DASH-IF binaries to public Git.
`.gitignore` already excludes `rag/corpus/{drafts,change-requests,legacy-v4,mpeg}`
binaries and extracted images; the manifest and folder structure stay public.
