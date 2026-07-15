# 0005: Part status lifecycle, versioning, and feature-based development

Status: Proposed
Date: 2026-07-13

## Context

Each IOP v5 part currently carries only an informal, free-text status in the
top-level README table (e.g. "Bikeshed/Markdown shell; substantive migration
pending"). This does not scale:

- it does not distinguish *how far along* a part is in a consistent way across
  parts,
- it has no version number, so there is no way to say "this is v5.1.0 of Part
  6" versus "this is the in-progress next iteration",
- there is no defined way to keep publishing/maintaining an **approved** part
  while new work continues on top of it,
- there is no place to track cross-cutting **features** (pieces of work that
  touch one or more parts) independently from the parts themselves, even
  though in practice most substantial changes are feature-shaped (e.g. "add
  low-latency chunk signalling", "add immersive audio support") rather than
  whole-part rewrites.

DASH-IF also publishes parts independently (see `rag/corpus/published/*`), so
some parts already have real published versions (e.g. Part 6 v5.1.0, Part 8
v5.1.0, Part 9 v5.0.0 FINAL) while others are still shells. The model below
needs to be compatible with that reality.

## Decision

### 1. Status lifecycle (per part, and per feature)

We adopt a single shared status vocabulary, used both for **parts** and for
**features** (see below):

| Order | Status | Meaning |
|---|---|---|
| 1 | **Skeleton** | Structural shell only (headings, references, ToC). No substantive authored prose yet. |
| 2 | **Draft** | Actively authored. Not yet formally reviewed. May be incomplete. |
| 3 | **WG Review** | Feature-/part-complete draft under Working Group (DASH-IF Technical WG) internal review. |
| 4 | **Community Review** | Opened for broader/external review (public comment period). |
| 5 | **Approved** | Ratified and published. Canonical for its version line. |

Additional terminal/side statuses:

- **Deprecated** — superseded by a later approved version; kept for reference.
- **Withdrawn** — abandoned before approval.

These names are intentionally plain-English and ordered; they replace ad hoc
free text such as "Bikeshed/Markdown shell" or "Drafted and building".

> Naming is deliberately kept generic (not tied to Bikeshed/GitHub mechanics)
> so it also applies to the Metanorma/PDF path if that becomes a supported
> output.

### 2. Versioning

Each **part** carries an independent `MAJOR.MINOR.PATCH` version plus its
current status:

- **MAJOR** — bumped only when a part reaches **Approved** as part of a new
  major IOP v5 line decision (rare; coordinated across parts).
- **MINOR** — bumped when:
  - a part reaches **Approved** for the first time at a given major line, or
  - an already-Approved part re-enters development and a **Feature** (see
    below) is later integrated into it.
- **PATCH** — editorial-only fixes to an Approved part (typos, broken links,
  non-normative clarifications) that do not require re-review.

A part's version and status are shown together, e.g.:

```text
Status: Draft · Version: 0.3.0
Status: Approved · Version: 5.1.0
```

### 3. Re-opening development after Approval ("development lines")

Once a part is **Approved** at version `X.Y.0`:

- the Approved content and version stay published/canonical,
- new work does **not** silently mutate the approved text in place,
- instead, a new **development line** for that part is opened, which restarts
  at **Skeleton or Draft** status (informally "vNext"), while the previous
  Approved version remains the reference until the new line itself reaches
  Approved.

This satisfies the requirement that the same status lifecycle can be re-run
per part after approval, without ever leaving the part in an ambiguous
"half-approved" state.

In practice, a development line is realized as a normal branch/PR cycle in
this repo; the important part is that the **status/version metadata**, not
branch naming, is authoritative for what is "the approved thing" at any time.

### 4. Feature-based development and the feature matrix

Most real change is better modeled as a **Feature** — a discrete, reviewable
unit of work with its own lifecycle — that targets one or more parts, rather
than as ad hoc direct edits to a part's "next version".

A **Feature**:

- has its own id, title, and status (same 5-state lifecycle as parts, plus an
  **Integrated** terminal state),
- declares which part(s) it targets (many-to-many — a feature can span
  multiple parts, e.g. a new event type touching Part 10 and Part 12),
- is tracked independently of the parts it targets until it is **Approved**,
- once **Approved**, is **Integrated** into each target part:
  - the feature's content is merged into the part's current development line,
  - each affected part's **MINOR** version is bumped,
  - each affected part's Change History table gets an entry referencing the
    feature id,
  - the feature's status becomes **Integrated** in the feature registry.

This gives a **matrix**: Features × Parts, where each cell says whether/how a
feature affects a part, and the feature registry is the single place to see
cross-cutting work that doesn't map 1:1 onto a single part.

See `rag-authoring-starter/docs/governance/feature-registry.md` for the
tracked matrix and `rag-authoring-starter/docs/governance/status-lifecycle.md`
for the authoring-facing how-to (metadata block format, table format, and the
rules above spelled out for editors).

## Consequences

- README's part-status table is replaced by a Status + Version table (see
  README update in this change).
- Each part's `.bs` file should carry a status/version metadata block (see
  Part 8 and Part 10 for the first concrete examples) and a small in-document
  "Document Status" table near the top, so status/version is visible both in
  the repo and in the built HTML.
- A feature registry file is introduced to track cross-part work items as a
  matrix rather than only inside individual parts' Open Issues tables.
- Existing per-part "Open Issues and Work Items" tables remain useful for
  part-local editorial tracking, but larger/cross-part items should graduate
  into the feature registry once they have a clear scope.
- This is a **process** decision, not a Bikeshed/tooling change; no build
  behavior changes as a result of this document alone.

## Alternatives considered

- **Git branch name as source of truth** (e.g. `part08/vnext`) — rejected as
  sole mechanism because branch naming is not visible in the published
  document itself and does not generalize to the Metanorma/PDF path.
- **Single repo-wide version number** — rejected because parts are published
  and reviewed independently in practice (confirmed by independently versioned
  published artifacts already in `rag/corpus/published/`).
- **GitHub issue labels only** — useful and complementary, but insufficient
  alone for a multi-part feature matrix or for version bumping rules.
