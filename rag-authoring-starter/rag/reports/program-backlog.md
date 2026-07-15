# IOP v5 program backlog (consolidated status)

This is the single consolidated view of remaining work across the whole IOP v5
program, not just spec content. It complements (does not replace):

- per-part "Open Issues and Work Items" tables (part-local),
- `rag-authoring-starter/docs/governance/feature-registry.md` (cross-part
  feature matrix),
- `rag-authoring-starter/docs/decisions/` (architectural/process decisions).

Last updated: 2026-07-13.

## A. Content migration backlog

| Part | Status | Version | Main gap |
|---|---|---|---|
| 1 | Draft/building | — | Largely drafted; confirm alignment with later parts. |
| 2 | Draft | — | Substantive draft; many open technical issues tracked in-part. |
| 3 | Draft | — | Initial draft from v4.3 on-demand clauses; needs v5 reconciliation. |
| 4 | Draft/building | — | More v4.3 live/low-latency detail remains to migrate. |
| 5 | Skeleton→Draft | — | Shell; major substantive migration pending. Published `DASH-IF-IOP-Part5-v5.0.0` is extracted and much larger than the current source (see `published-content-reconciliation-sprint.md`). |
| 6 | Draft/reconciliation | — | Substantive Bikeshed source exists; reconcile clause-by-clause against published `v5.1.0` rather than treating as a blank shell. |
| 7 | Skeleton→Draft | — | Shell; substantive migration pending. Draft update doc exists in corpus (`Part-7-Video-updates`). |
| 8 | Draft | 0.3.0 | Scaffolded source exists, but published `v5.1.0` has additional CMAF/media-profile/NGA structure; published source now extracted manually and needs manifest entry + crosswalk. |
| 9 | Skeleton→Draft | — | Compact published `FINAL v5.0.0` now extracted manually; current source is a scaffold and needs published-document-first migration. |
| 10 | Draft | 0.2.0 | Scaffolded this session (event taxonomy, examples). No published corpus doc found yet — likely genuinely new for v5. |
| 11 | Draft | — | Shell seeded with trick-mode, thumbnails, metadata-track, registration-process items. |
| 12 | Draft/building | — | Drafted and building; keep as target for conformance mapping (see Feature F-0006). |

Key risk: several parts (5, 6, 8, 9) already have **published v5.0.0/v5.1.0
corpus documents** (`rag/corpus/published/`) that are not yet reconciled with
the in-repo Bikeshed source. This is higher priority than fresh authoring for
those parts — the repo should not diverge from already-approved content.

Initial reconciliation evidence is captured in
`rag/reports/published-content-reconciliation-sprint.md`. Recommended order:
Part 6 clause crosswalk first, then Part 9, Part 5, and Part 8.

## B. Editorial/spec consistency backlog

- Cross-part anchor harmonization (tracked as F-0007).
- Terminology harmonization across parts (F-0007).
- Duplicate/overlapping requirements between Part 2 and topic-specific parts —
  needs a dedicated pass once more parts have substantive content.
- Modal-keyword normalization — run `tools/publication/wrap_modals.py` after
  broad edits (already documented in README; needs to become routine, e.g. a
  pre-merge check).
- Table/example style consistency — Part 8 and Part 10 now follow a consistent
  pattern (signalling table → considerations → examples → backlog table);
  worth propagating to Parts 5, 6, 7, 9, 11 as they get scaffolded.

## C. Governance backlog (new, this session)

- Status/version metadata format defined
  (`docs/governance/status-lifecycle.md`) — needs to be applied to **all**
  parts, not just 8 and 10.
- Feature registry created (`docs/governance/feature-registry.md`) — currently
  seeded with 8 candidate features from Part 8/10 work; needs real owners and
  tracking issues.
- README part-status table needs Status+Version columns (done this session —
  verify it stays in sync as other parts adopt the convention).
- Decide who/what updates the feature registry on Integration (manual for now;
  candidate for a `tools/publication/` check later).

## D. Conformance / Part 12 linkage backlog

- No systematic mapping yet from part requirements to:
  - validators,
  - test vectors,
  - reference-player expectations.
- Tracked as feature F-0006 (spans nearly every part).
- Part 8 and Part 10 both explicitly flag "Conformance mapping" as an open
  issue in-part; this is the first concrete pull-through candidate for F-0006.

## E. Publication path backlog (PDF / DOC)

- Bikeshed HTML is the only reliable output today.
- No supported PDF generation path yet.
- No supported DOC/DOCX generation path yet (published corpus docs are
  `.docx`/`.pdf` produced outside this repo's current toolchain).
- Decision needed (tracked as feature F-0008): stay HTML-only, or invest in
  Metanorma (see section F) or another converter for DOC/PDF.
- Until decided, do not assume generated PDF/DOC artifacts are authoritative.

## F. Metanorma / AsciiDoc experiment backlog

- PoC converter exists: `tools/metanorma/bikeshed_to_adoc.py`.
- **Confirmed missing from this workspace** (checked directly, not just
  referenced): the three status/decision files the README pointed to —
  `docs/decisions/0004-bikeshed-vs-metanorma.md`,
  `rag/reports/metanorma-part12-poc-status.md`, and
  `docs/metanorma-dashif-template-plan.md` — do not exist here. README has
  been corrected to say so explicitly rather than link to non-existent files.
- Current target: Part 12 (small, self-contained).
- Planned next step: ISO-flavoured Metanorma/PDF experiment with DASH-IF
  branding.
- Policy reminder: Bikeshed Markdown remains canonical; generated AsciiDoc
  must not become a second edited source of truth.

Action item: restore these three files from wherever they were previously
authored (another branch/machine/export), or re-author them from scratch
capturing the actual PoC findings, before further Metanorma work continues —
the README currently pointed at them as if they were canonical, which was
incorrect for this workspace.

## G. Tooling / RAG / migration backlog

- Source inventory and extraction tooling exist (`tools/ingest/`) and corpus
  already contains extracted text/json for most published/draft/legacy/MPEG
  sources.
- Chunking/indexing exist (`tools/rag/`), with chunks already built for most
  corpus sources (`rag/chunks/*.jsonl`).
- Gaps:
  - Published Parts 8 and 9 exist in `rag/corpus/published/` but are not yet
    represented in `rag/sources.yaml`; they were manually extracted during the
    published-content reconciliation sprint and should be added to the manifest
    before chunking/indexing.
  - No chunks yet for: Part 6 v5.1.0, Part 8 v5.1.0, Part 9 FINAL, Part 10 IPR
    review docx, external-examples, website corpus, change-requests r9 vs r8
    reconciliation.
  - `rag/reports/` was **confirmed empty** in this workspace (checked
    directly) even though README previously referenced status/backlog reports
    living there (`part02-part03-all-parts-status.md`, `editorial-backlog.md`).
    This program backlog file (`program-backlog.md`) is now the first file in
    that directory and is intended to supersede those two references; README
    has been updated accordingly. If the original two files exist elsewhere,
    fold any content not already covered here back in.
  - Initial published-content reconciliation sprint report exists at
    `rag/reports/published-content-reconciliation-sprint.md`.
  - Next required artifact is a dedicated Part 6 clause crosswalk from published
    `DASH-IF-IOPv5.1.0-Part6` to the current Bikeshed source.

## H. Suggested near-term priority order

1. Complete the published-content reconciliation sprint:
   - Part 6 clause crosswalk first,
   - Part 9 compact migration second,
   - Part 5 major migration map third,
   - Part 8 published v5.1.0 crosswalk after manifest/chunking is fixed.
2. Restore or re-author the missing Metanorma status/decision docs referenced
   by README (section F), or correct README if they're intentionally gone.
3. Apply the new status/version metadata (section C) to all parts, not just 8
   and 10.
4. Start Feature F-0006 (conformance mapping) once at least 2–3 parts have
   real requirement text to map.
5. Only after 1–4: continue expanding Parts 8/10 style scaffolding to Parts 5,
   6, 7, 9, 11.
