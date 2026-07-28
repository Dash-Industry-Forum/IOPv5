# DASH-IF IOP v5 Authoring Workspace — `rag-authoring-starter`

This directory is the canonical authoring workspace for the multi-part
**DASH-IF Interoperability Guidelines, Version 5 (IOP v5)**. It contains all
Bikeshed/Markdown source files, tooling, and status reports.

For the top-level repository overview, see [`../README.md`](../README.md).

---

## Directory structure

```text
specs/
  _boilerplate/              shared IPR notice and diagram/table CSS
  part01-overview/           Part 1: Overview, Architecture and Interfaces
  part02-core-cmaf/          Part 2: Core Principles and CMAF Mapping
  part03-on-demand/          Part 3: On-Demand Services
  part04-live-low-latency/   Part 4: Live and Low-Latency Services
  part05-ad-insertion/       Part 5: Ad Insertion and Content Replacement
  part06-content-protection/ Part 6: Content Protection and Security
  part07-video/              Part 7: Video
  part08-audio/              Part 8: Audio
  part09-text/               Part 9: Text (Subtitle)
  part10-events/             Part 10: Events
  part11-additional-technologies/  Part 11: Additional Functionalities
  part12-conformance-reference-tools/  Part 12: Conformance and Reference Tools

tools/
  env/                       Bikeshed and DASH-IF boilerplate setup
  ingest/                    source inventory and text/image extraction
  rag/                       offline chunk/index/query tools
  migration/                 source delta/migration helpers
  publication/               build_all.py, check_links.py, wrap_modals.py
  validation/                per-part MPD validation scripts
  metanorma/                 experimental Bikeshed-to-AsciiDoc tooling

rag/
  sources.yaml               source manifest
  corpus/                    local source documents (mostly gitignored)
  chunks/, indexes/          derived RAG artifacts (gitignored/generated)
  reports/                   migration and status reports

authoring/                   DASH-IF boilerplate, templates, style guide
docs/                        roadmap, decisions, migration maps
website/                     website integration stubs
```

---

## Part status (2026-07-28)

| Part | Title | WD | Status |
|------|-------|----|--------|
| 1 | Overview, Architecture and Interfaces | 0.3 | Substantially complete |
| 2 | Core Principles and CMAF Mapping | 0.1 | Substantial content |
| 3 | On-Demand Services | 0.1 | Skeleton |
| 4 | Live and Low-Latency Services | 0.3 | Substantial content |
| 5 | Ad Insertion and Content Replacement | 0.12 | Substantial content |
| 6 | Content Protection and Security | — | Substantial content |
| 7 | Video | — | Substantial content |
| 8 | Audio | — | Substantial content |
| 9 | Text (Subtitle) | — | Reconciled |
| 10 | Events | 0.4 | Substantial content |
| 11 | Additional Functionalities | 0.1 | Skeleton |
| 12 | Conformance and Reference Tools | 0.6 | Substantially complete |

Full per-part status with done/remaining checklists:

```text
rag/reports/iop-v5-authoring-status.md
```

---

## Building

Build all 12 parts into `../dist/`:

```powershell
python tools/publication/build_all.py --out ../dist
```

Build one part in place:

```powershell
./build.ps1 part02-core-cmaf
```

---

## Local setup

```powershell
pip install -r requirements.txt
pip install bikeshed
python tools/env/build_ca_bundle.py
$env:REQUESTS_CA_BUNDLE = "$PWD\build-tools\corp-ca-bundle.pem"
$env:SSL_CERT_FILE      = $env:REQUESTS_CA_BUNDLE
python -m bikeshed update
python tools/env/install_dashif_boilerplate.py
```

---

## Authoring rules

- Edit `.bs` and `.inc.md` source files, not generated HTML.
- Every `.bs` file must have `!Repository:`, `!Issue Tracking:`, and
  `!Document Status:` custom metadata fields.
- Every section that has subsections must **not** have hanging paragraphs.
  Add `### General ### {#section-id-general}` if needed.
- Modal keywords (`shall`, `should`, `may`) must be wrapped in
  `<span class=modal-keyword>` tags.
- `@schemeIdUri` values must reference the
  [DASH-IF Identifier Registry](https://dashif.org/identifiers/introduction/).
- `@codecs` strings must reference the
  [DASH-IF Codec Registry](https://dashif.org/codecs/introduction/).
- Images go in `images/`, `Images/`, or `Diagrams/` inside the part folder.
  Root-level PNGs in the part folder are also copied by `build_all.py`.

---

## Issue tracking

File issues at: https://github.com/Dash-Industry-Forum/IOPv5/issues

Use label `Part N` or title prefix `[Part N]:` (e.g. `[Part 2]: Add SegmentTemplate table`).

---

## Status reports

```text
rag/reports/iop-v5-authoring-status.md          ← primary status (2026-07-28)
rag/reports/project-status-update-2026-07-21.md
rag/reports/editorial-backlog.md
rag/reports/part05-f0010-issue-index.md
```

---

## Public/private content policy

Many corpus documents are access-controlled and intentionally gitignored.
Do **not** commit:

- Unpublished DASH-IF drafts
- Proprietary MPEG documents
- Extracted binary images unless publication rights are confirmed

Published DASH-IF documents and MPEG publicly available documents may be
committed to `rag/corpus/published/` if their licence permits redistribution.