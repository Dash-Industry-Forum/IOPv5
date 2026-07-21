# DASH-IF IOP v5 migration execution plan

Generated: 2026-07-21

This execution plan turns the agreed migration sequence into concrete work
packages, deliverables, dependencies, and acceptance criteria.

Agreed priority order:

1. Stabilize Part 5 Ad Insertion / F-0010.
2. Complete Part 9 Text conformance alignment.
3. Continue Part 6 Content Protection.
4. Keep Part 12 synchronized after each substantive Part 5/6/9 change.
5. Then return to Parts 7, 8, 10, and 11 as structured migrations.
6. Finally run cross-part harmonization.

## Program-level milestones

| Milestone | Scope | Primary output |
|---|---|---|
| M1 | Part 5 / F-0010 stabilization | Part 5 tables/figures reviewed; validator-start issues ready |
| M2 | Part 9 conformance completion | Part 9 issue index and conformance/test matrix |
| M3 | Part 6 content-protection completion | Part 6 conformance matrix and Part 5 IF-9 alignment |
| M4 | Part 12 synchronization | Conformance map reflects Parts 5/6/9 decisions |
| M5 | Parts 7/8/10/11 structured migration | Migration maps and source baselines for remaining parts |
| M6 | Cross-part harmonization | Stable terminology, anchors, bibliography, and modal policy |

## M1: Stabilize Part 5 Ad Insertion / F-0010

### Goal

Turn the current Part 5 migration and F-0010 planning package into executable
project work.

### Primary source files

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md
specs/part05-ad-insertion/part05-ad-insertion.bs
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Primary planning reports

```text
rag/reports/part05-f0010-issue-index.md
rag/reports/part05-f0010-table-figure-hardening.md
rag/reports/part05-f0010-table2-reconstruction.md
rag/reports/part05-f0010-table4-validator-matrix.md
rag/reports/part05-f0010-table5-validator-matrix.md
rag/reports/part05-f0010-scte35-validator-matrix.md
rag/reports/part05-f0010-validator-implementation-issues.md
rag/reports/part05-f0010-runtime-test-planning.md
rag/reports/reconcile-part05-ad-insertion.md
```

### Work items

| Order | Work item | Deliverable |
|---:|---|---|
| 1 | Create GitHub issues from `part05-f0010-issue-index.md` | GitHub issue set F-0010-H/B/C/A/D/F/E/G |
| 2 | F-0010-H1: review/extract/redraw Figures 1, 3, 4, 5, 6, 7 | Figure status table and source updates |
| 3 | F-0010-H2: reconstruct Table 2 from DOCX/PDF | Bikeshed Table 2 or formal deferral |
| 4 | F-0010-H3/H4: visually review Tables 4 and 5 | Confirmed table rows/modal strength |
| 5 | F-0010-H5: decide Table 4/Table 5 reuse | Canonical table strategy |
| 6 | F-0010-B1/B2: start Table 4 validator/test vectors | Validator issue/test-vector package |
| 7 | F-0010-C1/C2/C3: start Table 5 validator/test vectors | IF-5 validator issue/test-vector package |
| 8 | F-0010-A1/A2/A3: start SCTE-35 EventStream validation | SCTE-35 validator issue/test-vector package |
| 9 | Update Part 12 | Conformance mapping synchronized |

### Acceptance criteria

- Part 5 table/figure status is explicit for every published item.
- Table 2 is reconstructed or explicitly deferred with documented reason.
- Tables 4 and 5 are visually reviewed against DOCX/PDF.
- Initial validator scopes for F-0010-A/B/C are implementation-ready.
- Part 12 references the current Part 5 conformance/test-asset plan.
- `python tools/publication/check_links.py` passes.

## M2: Complete Part 9 Text conformance alignment

### Goal

Finish Part 9 migration/conformance planning and make it a second complete
source-to-conformance example.

### Primary source files

```text
specs/part09-text/09-text.inc.md
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Primary reports

```text
rag/reports/reconcile-part09-text.md
rag/reports/part09-conformance-coverage.md
```

### Work items

| Order | Work item | Deliverable |
|---:|---|---|
| 1 | Review Part 9 source for remaining shell/open sections | Gap list |
| 2 | Convert Part 9 conformance coverage into issue buckets | `part09-issue-index.md` |
| 3 | Classify Part 9 requirements | Validator/manual/not-testable matrix |
| 4 | Identify positive/negative test assets | Text/subtitle test-asset plan |
| 5 | Synchronize Part 12 | Updated Part 9 conformance mapping |

### Acceptance criteria

- Part 9 reconciliation has final known-gaps status.
- Part 9 conformance matrix classifies all major requirements.
- Part 12 Part 9 mapping points to concrete issue/test-asset buckets.
- `check_links.py` passes.

## M3: Continue Part 6 Content Protection

### Goal

Complete the active Part 6 reconciliation path and align it with Part 5 IF-9 and
Part 12 conformance/reference-client coverage.

### Primary source files

```text
specs/part06-content-protection/10-general.inc.md
specs/part06-content-protection/80-misc.inc.md
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Primary report

```text
rag/reports/reconcile-part06-content-protection.md
```

### Work items

| Order | Work item | Deliverable |
|---:|---|---|
| 1 | Finish Part 6 reconciliation in active sections | Updated source/reconciliation report |
| 2 | Identify content-protection requirements affecting playback | Requirement inventory |
| 3 | Create Part 6 conformance matrix | `part06-conformance-coverage.md` |
| 4 | Cross-link to Part 5 IF-9/F-0010-F | Part 5/6 alignment notes |
| 5 | Synchronize Part 12 | Updated content-protection/reference-client mapping |

### Acceptance criteria

- Part 6 requirements affecting MSE/EME, encryption, key rotation, and Period
  transitions are identified.
- F-0010-F1/F2 can reference Part 6 requirements directly.
- Part 12 has synchronized rows for Part 6 and Part 5 IF-9.
- `check_links.py` passes.

## M4: Keep Part 12 synchronized

### Goal

Prevent conformance mapping drift while Parts 5/6/9 evolve.

### Primary source file

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Work items

| Order | Work item | Deliverable |
|---:|---|---|
| 1 | After each Part 5/6/9 source update, update Part 12 | Part 12 synchronized mapping |
| 2 | Convert planning text into structured tables | Conformance implementation map |
| 3 | Mark each item by test mechanism | validator / dash.js / livesim2 / manual / not-testable |
| 4 | Link test assets and issue IDs | Traceable conformance map |

### Acceptance criteria

- Part 12 contains no stale Part 5/6/9 references.
- Each conformance row has a test mechanism or explicit deferral.
- Links to issue matrices are stable.
- `check_links.py` passes.

## M5: Return to Parts 7, 8, 10, and 11

### Goal

Create structured migration baselines for the less mature parts.

### Work items by part

| Part | First deliverable | Second deliverable |
|---|---|---|
| Part 7 Video | `reconcile-part07-video.md` | Part 7 source migration baseline |
| Part 8 Audio | `reconcile-part08-audio.md` | Part 8 codec/channel/loudness conformance matrix |
| Part 10 Events | `reconcile-part10-events.md` | Event model alignment with Part 5 IF-3/IF-6 |
| Part 11 Additional Technologies | `reconcile-part11-additional-technologies.md` | Trick-mode/thumbnails/metadata/remote-entity issue index |

### Acceptance criteria

- Each part has a reconciliation report.
- Each part has source gaps classified.
- Dependencies into Parts 2/5/6/10/12 are identified.
- Part 12 has initial placeholders for each conformance area.

## M6: Cross-part harmonization

### Goal

Normalize the whole IOP v5 source set after substantive migrations.

### Primary files

```text
docs/governance/feature-registry.md
README.md
rag-authoring-starter/README.md
rag/reports/project-status-update-2026-07-21.md
```

### Work items

| Order | Work item | Deliverable |
|---:|---|---|
| 1 | Anchor audit | Cross-part anchor index |
| 2 | Terminology audit | Shared glossary recommendations |
| 3 | Bibliography audit | Shared/local bibliography normalization |
| 4 | Modal audit | Modal keyword consistency pass |
| 5 | Duplicate requirement audit | De-duplication recommendations |
| 6 | Project status refresh | Updated status report and README |

### Acceptance criteria

- Cross-part references are stable.
- Shared terms are defined once or intentionally duplicated with reason.
- Bibliography aliases are consistent.
- Modal keyword usage is normalized.
- README/status reports reflect current project reality.

## Recommended next branch

Create a new branch for the immediate work package:

```text
part5-f0010-visual-validator-start
```

Base it on the current branch or on the upstream target branch after the current
status-plan commit is reviewed.

## Recommended next commit contents

For the next commit after this planning report:

- add `project-migration-execution-plan.md`,
- update `project-status-update-2026-07-21.md` to link it,
- optionally update root/starter README to point to it,
- validate with `check_links.py`.

## Validation command

Run before every commit or pull request:

```powershell
python tools/publication/check_links.py
```
