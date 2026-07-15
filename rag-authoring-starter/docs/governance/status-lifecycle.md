# Part status lifecycle and versioning — authoring guide

This is the practical, authoring-facing companion to
`rag-authoring-starter/docs/decisions/0005-status-lifecycle-and-feature-branches.md`.
Read that decision record for rationale; this file defines the concrete format
editors and tools should use.

## 1. Status values

Use exactly one of these values (case as shown) for a part or a feature:

1. `Skeleton`
2. `Draft`
3. `WG Review`
4. `Community Review`
5. `Approved`
6. `Deprecated` (part only; terminal, replaces an older Approved version)
7. `Withdrawn` (terminal; abandoned before Approved)
8. `Integrated` (feature only; terminal, successfully merged into target parts)

Statuses 1–5 are the normal forward lifecycle. A part or feature should only
move forward, except that an Approved part can be re-opened into a **new
development line** that restarts at `Skeleton` or `Draft` (see decision
record §3) while the previously Approved version stays canonical.

## 2. Version format

`MAJOR.MINOR.PATCH`, independent per part. Rules:

- `0.x.y` — pre-Approval (Skeleton/Draft/WG Review/Community Review).
  Increment `MINOR` for each meaningfully new round of substantive content
  (e.g. 0.1 shell → 0.2 first substantive draft → 0.3 expanded draft).
  Increment `PATCH` for small fixes within the same round.
- First Approval sets `MAJOR.MINOR.0` (typically aligned to the IOP major line,
  e.g. `5.0.0` or `5.1.0`, matching already-published parts).
- After Approval, editorial-only fixes bump `PATCH` (e.g. `5.1.0` → `5.1.1`)
  and do **not** change Status.
- After Approval, integrating an Approved **feature** bumps `MINOR` and resets
  `PATCH` to 0 (e.g. `5.1.1` → `5.2.0`), and Status moves back to `Draft` for
  that new development line until it is re-Approved.

## 3. Required metadata in each part's `.bs` file

Add a `Status Text` and version fields near the top of the `.bs` metadata
block (Bikeshed passes unknown custom keys through as plain metadata; we also
add a rendered "Document Status" table right after the title so the
information is visible in the built HTML without relying on Bikeshed
internals).

Minimal pattern (see `part08-audio.bs` / `part10-events.bs` for the concrete
example already applied):

```text
<pre class=metadata>
Work Status: Living Document
Text Macro: copyright Copyright © DASH-IF. This document is made available under the DASH-IF policies.
Text Macro: PARTSTATUS Draft
Text Macro: PARTVERSION 0.3.0
</pre>
```

And, right after Scope (or right after the title), a rendered status table:

```html
<table class="data">
  <caption>Document status.</caption>
  <thead>
    <tr>
      <th scope="col">Status</th>
      <th scope="col">Version</th>
      <th scope="col">Development line</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Draft</td>
      <td>0.3.0</td>
      <td>Initial v5 authoring (pre-Approval)</td>
    </tr>
  </tbody>
</table>
```

Keep this table's Status/Version values in sync with the Change History
table's latest row — Change History is the audit trail, the Document Status
table is the current snapshot.

## 4. Required metadata in the README overview table

The top-level part overview table (`README.md`, "Current part status")
should show **Status** and **Version** as separate columns rather than free
text, e.g.:

| Part | Title | Status | Version |
|---|---|---|---|
| 8 | Audio | Draft | 0.3.0 |
| 10 | Events | Draft | 0.2.0 |

## 5. Features vs. part-local issues

Use the **part-local** "Open Issues and Work Items" table for:

- small, single-part editorial/technical gaps,
- things with no cross-part impact,
- anything not yet scoped enough to be a tracked feature.

Use the **feature registry**
(`rag-authoring-starter/docs/governance/feature-registry.md`) for:

- anything touching more than one part,
- anything that should be reviewable/approvable as a unit before merging into
  the parts it affects,
- anything that should trigger a version bump on Approval/Integration.

When a part-local issue grows into something with cross-part scope, promote it
to the feature registry and remove/close the part-local row, leaving a note
pointing at the feature id.

## 6. Worked example (what we did for Part 8 and Part 10)

Both parts were set to:

- Status: `Draft`
- Version: `0.3.0` (Part 8) / `0.2.0` (Part 10)
- Development line note: "Initial v5 authoring (pre-Approval)"

This reflects that both went from `Skeleton` (shell-only, as found) to `Draft`
(substantive scaffolding, examples, and tables added), and is the first
concrete application of this lifecycle — earlier Change History rows for both
parts predate the status/version convention and are left as-is for history.
