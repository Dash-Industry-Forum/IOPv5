# DASH-IF IOP v5 migration next steps and recommendations

Generated: 2026-07-21

This report defines the recommended next migration sequence after the current
project status update and F-0010 Part 5 planning commit.

Current baseline commit:

```text
c9e6d39 Document IOP v5 project status and F-0010 plan
```

## Executive recommendation

Proceed in this order:

1. **Stabilize Part 5 Ad Insertion**, because it now has the richest source
   migration and the clearest conformance project plan.
2. **Complete Part 9 Text conformance alignment**, because Part 9 is already
   active and has a conformance coverage report.
3. **Continue Part 6 Content Protection**, because it is needed by Part 5 IF-9
   clear/encrypted playback work and Part 12 conformance.
4. **Update Part 12 after each substantive Part 5/6/9 change**, so conformance
   mapping does not drift.
5. **Then return to Parts 7, 8, 10, and 11** as structured migrations.
6. **Finally run cross-part harmonization**, especially terminology, anchors,
   bibliography, and modal-strength normalization.

## Recommended implementation phases

## Phase 1: Part 5 source stabilization and F-0010 execution

Priority: highest.

Reason:

Part 5 now has an issue-ready plan, validator matrices, cross-part dependencies,
and a central issue index. It is ready to become the pilot for turning migrated
source text into concrete conformance work.

Primary index:

```text
rag/reports/part05-f0010-issue-index.md
```

### Recommended next actions

1. Create GitHub issues from:
   ```text
   rag/reports/part05-f0010-issue-index.md
   ```
2. Start with:
   - F-0010-H1: Harden Part 5 figures against published DOCX/PDF.
   - F-0010-H2: Reconstruct Part 5 Table 2 row layout from DOCX/PDF.
   - F-0010-H3: Visually review Part 5 Table 4.
   - F-0010-H4: Visually review Part 5 Table 5.
   - F-0010-H5: Decide Table 4/Table 5 canonical reuse strategy.
3. After visual review, implement validator planning:
   - F-0010-B1/B2 for DASH-IF ad content MPD validation.
   - F-0010-C1/C2/C3 for IF-5 multi-Period validation.
   - F-0010-A1/A2/A3 for SCTE-35 MPD Event validation.
4. Keep Part 12 synchronized after each validator/test-asset decision.

### Expected deliverables

- Final status for Part 5 Tables 1–5.
- Final status for Figures 1, 3, 4, 5, 6, and 7.
- Validator issue set for Part 5.
- Test-asset plan for Part 5.
- Part 12 conformance mapping updated from planning to implementation targets.

## Phase 2: Part 9 Text completion

Priority: high.

Reason:

Part 9 already has active source and conformance coverage planning. Completing
Part 9 gives a second end-to-end example of source migration plus conformance
mapping.

Primary files:

```text
specs/part09-text/09-text.inc.md
rag/reports/reconcile-part09-text.md
rag/reports/part09-conformance-coverage.md
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Recommended next actions

1. Review Part 9 current source for remaining shell sections.
2. Convert `part09-conformance-coverage.md` into issue-ready implementation
   buckets.
3. Identify positive and negative text/subtitle test assets.
4. Align Part 9 terminology with Parts 2 and 12.
5. Update Part 12 with final Part 9 conformance mapping.

### Expected deliverables

- Part 9 migration completion report.
- Part 9 issue index.
- Part 9 conformance/test-asset matrix.
- Updated Part 12 text conformance section.

## Phase 3: Part 6 Content Protection completion

Priority: high.

Reason:

Part 6 is a dependency for Part 5 IF-9 and clear/encrypted ad insertion playback
assets. It also interacts with Part 12 reference-client testing.

Primary files:

```text
specs/part06-content-protection/10-general.inc.md
specs/part06-content-protection/80-misc.inc.md
rag/reports/reconcile-part06-content-protection.md
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Recommended next actions

1. Finish Part 6 reconciliation sections currently in progress.
2. Identify all content-protection requirements that affect:
   - MSE/EME playback,
   - encrypted Period transitions,
   - key rotation,
   - common-key versus key-change scenarios,
   - ad insertion IF-9 playback.
3. Create a Part 6 conformance coverage matrix.
4. Cross-link Part 6 requirements to F-0010-F1/F2.

### Expected deliverables

- Part 6 reconciliation report updated to completion or known-gaps status.
- Part 6 conformance matrix.
- Cross-link from Part 5 IF-9 to Part 6 content-protection requirements.
- Updated Part 12 content-protection/reference-player mapping.

## Phase 4: Part 12 conformance integration pass

Priority: continuous, but make a dedicated pass after Phases 1–3.

Reason:

Part 12 should become the authoritative map from source requirements to
validator, dash.js, livesim2, and test-asset coverage.

Primary file:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

### Recommended next actions

1. Convert planning-language sections into structured conformance tables.
2. Add stable references to Part 5, Part 6, and Part 9 issue/test matrices.
3. Identify which checks are:
   - validator checks,
   - reference-client checks,
   - livesim2 checks,
   - manual review,
   - not testable.
4. Add test-asset inventory links.

### Expected deliverables

- Part 12 conformance source upgraded from initial mapping to implementation map.
- Cross-part conformance coverage table.
- Clear gap list for remaining parts.

## Phase 5: Parts 7, 8, 10, and 11 structured migration

Priority: medium.

Reason:

These parts are less mature than Parts 5/6/9/12 but need structured migration to
complete the IOP v5 set.

### Part 7 Video

Primary target:

```text
specs/part07-video/07-video.inc.md
```

Recommended approach:

- inventory current shell/source status,
- migrate published video requirements,
- identify codec/profile/conformance hooks,
- map to Part 12 validator/test coverage.

### Part 8 Audio

Primary target:

```text
specs/part08-audio/08-audio.inc.md
```

Recommended approach:

- identify current draft material,
- reconcile codec/channel/loudness requirements,
- align with Part 5 ad-content audio transition requirements,
- map to Part 12.

### Part 10 Events

Primary target:

```text
specs/part10-events/10-events.inc.md
```

Recommended approach:

- prioritize event model alignment because Part 5 IF-3/IF-6 depends on it,
- align DASH Callback Event, SCTE-35 MPD Events, and remote-resolution events,
- map event conformance checks to Part 12.

### Part 11 Additional Technologies

Primary target:

```text
specs/part11-additional-technologies/11-additional-technologies.inc.md
```

Recommended approach:

- complete trick-mode, thumbnails, metadata-track, and registration-process
  items,
- identify any remote-entity overlap with SGAI,
- map testability into Part 12.

## Phase 6: Cross-part editorial and governance pass

Priority: final integration after substantive migrations.

Primary files:

```text
docs/governance/feature-registry.md
rag/reports/project-status-update-2026-07-21.md
README.md
rag-authoring-starter/README.md
```

### Recommended next actions

1. Normalize terminology across all parts.
2. Normalize bibliography aliases.
3. Normalize anchor naming.
4. Normalize modal keywords.
5. Resolve duplicated requirements across Part 2, Part 5, Part 6, Part 10, and
   Part 12.
6. Update root README and project status report after each major milestone.

## Recommended immediate work package

The next concrete work package should be:

```text
WP-2026-07-Part5-Visual-Review-and-Validator-Start
```

### Scope

- F-0010-H1 through F-0010-H5,
- F-0010-B1,
- F-0010-C1,
- F-0010-A1.

### Why this package first

It turns the current Part 5 planning into executable project work while keeping
scope manageable.

### Acceptance criteria

- Published Part 5 figures and tables have final review status.
- Table 4 and Table 5 visual review is complete.
- Table 2 is reconstructed or formally deferred with reason.
- First validator issue scopes are ready for implementation.
- Part 12 is updated with any changed conformance mapping.

## Recommended second work package

```text
WP-2026-07-Part9-Part6-Conformance-Alignment
```

### Scope

- Part 9 conformance issue index,
- Part 6 conformance matrix,
- Part 12 updates for Parts 6 and 9.

### Acceptance criteria

- Part 9 source and conformance report are aligned.
- Part 6 requirements affecting playback/decryption are identified.
- Part 12 has synchronized conformance rows.

## Recommended third work package

```text
WP-2026-08-Events-and-Remote-Resolution
```

### Scope

- Part 10 events migration,
- Part 5 IF-3/IF-6 alignment,
- Part 5 IF-7 SGAI remote resolution,
- Part 11 remote-entity/additional-technology dependencies.

### Acceptance criteria

- DASH event/callback terminology is consistent.
- SCTE-35 MPD Event and DASH Callback Event scope is clear.
- SGAI remote-resolution behaviour has source and test mapping.

## Commit / PR recommendation

Create one branch/PR per work package:

1. `part5-f0010-visual-validator-start`
2. `part9-part6-conformance-alignment`
3. `events-remote-resolution-alignment`
4. `part7-part8-structured-migration`
5. `cross-part-editorial-harmonization`

Each PR should include:

- source changes,
- reconciliation report updates,
- conformance/test matrix updates,
- `check_links.py` validation output,
- clear next-step list.

## Validation command

Run before every commit/PR:

```powershell
python tools/publication/check_links.py
```

Current known good status:

```text
OK: checked 38 file(s), no issues found.
```
