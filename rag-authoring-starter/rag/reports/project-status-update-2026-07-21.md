# DASH-IF IOP v5 project status update

Date: 2026-07-21

Repository/worktree:

```text
IOPv5-tstock-worktree
```

Workspace:

```text
rag-authoring-starter
```

## Executive summary

The repository has moved beyond the original Part 4 pilot scaffold into a
broader DASH-IF IOP v5 source-authoring and reconciliation workspace.

Major progress has been made on:

- Part 5 Ad Insertion source migration and conformance planning,
- Part 6 content-protection reconciliation,
- Part 9 text/subtitle migration and conformance coverage,
- Part 12 conformance/reference-tool mapping,
- cross-part governance via the feature registry,
- issue-ready project planning for Part 5 ad-insertion conformance.

The most complete new project-plan package is:

```text
F-0010 Part 5 ad-insertion conformance and cross-part indexing
```

This package now includes source migration, cross-part indexing, validator
matrices, runtime/test planning, and a final GitHub issue index.

The agreed migration execution plan is tracked at:

```text
rag/reports/project-migration-execution-plan.md
```

## Current authored-source status by part

| Part | Title | Current status |
|---:|---|---|
| 1 | Overview, Architecture and Interfaces | Drafted and building. |
| 2 | Core Principles and CMAF Mapping | Initial substantive draft; open technical issues remain. |
| 3 | On-Demand Services | Initial draft from v4.3 on-demand clauses. |
| 4 | Live and Low-Latency Live Services | Drafted and building; further v4.3 live detail and LL alignment remain. |
| 5 | Ad Insertion and Content Replacement | Major source migration completed at initial/hardened draft level; F-0010 conformance/cross-part plan created. |
| 6 | Content Protection and Security | Active reconciliation in progress; general/miscellaneous sections updated and tracked. |
| 7 | Video | Shell / migration pending. |
| 8 | Audio | Draft material exists from prior work; feature candidates in governance registry. |
| 9 | Text | Active source migration and conformance coverage planning in progress. |
| 10 | Events | Shell plus event taxonomy/timing feature candidates. |
| 11 | Additional Technologies | Shell seeded with additional-technology work items. |
| 12 | Conformance and Reference Tools | Drafted and building; now includes initial Part 5 and Part 9 conformance mappings. |

## Part 5 Ad Insertion status

Primary source:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md
```

Part 5 now has initial source-level coverage for:

- use cases and scenarios,
- architecture overview,
- interface overview,
- IF-0 ABR stream source,
- IF-1 packager ingest,
- IF-2 content preparation,
- IF-3 ad avail signalling,
- IF-4 ad decisioning and exchange,
- IF-5 MPD and segments with ad placements,
- IF-6 ad metadata signalling,
- IF-7 decisioning parameters and remote resolution,
- IF-8 ad tracking and measurement,
- IF-9 reference playback and decryption.

Hardened areas include:

- IF-0 / IF-1 splice-point and CMAF preparation model,
- IF-2 content preparation,
- IF-3 SCTE-35 opportunity signalling baseline,
- IF-4 DASH-IF ad content Table 4 reconstruction,
- IF-5 Table 5 reconstruction,
- F-0010 conformance/cross-part planning.

Important Part 5 reports:

```text
rag/reports/reconcile-part05-ad-insertion.md
rag/reports/part05-cross-reference-index.md
rag/reports/part05-f0010-issue-index.md
rag/reports/part05-f0010-implementation-plan.md
rag/reports/part05-f0010-table-figure-hardening.md
rag/reports/part05-f0010-table2-reconstruction.md
rag/reports/part05-f0010-table4-validator-matrix.md
rag/reports/part05-f0010-table5-validator-matrix.md
rag/reports/part05-f0010-scte35-validator-matrix.md
rag/reports/part05-f0010-runtime-test-planning.md
```

## F-0010 project plan

Feature:

```text
F-0010 Part 5 ad-insertion conformance and cross-part indexing
```

Tracked in:

```text
docs/governance/feature-registry.md
```

Target parts:

```text
Part 1, Part 2, Part 5, Part 6, Part 10, Part 12
```

Central index:

```text
rag/reports/part05-f0010-issue-index.md
```

The F-0010 issue index defines the final issue set in implementation order.

### Phase 1: source tables and figures

- F-0010-H1: Harden Part 5 figures against published DOCX/PDF.
- F-0010-H2: Reconstruct Part 5 Table 2 row layout from DOCX/PDF.
- F-0010-H3: Visually review Part 5 Table 4 DASH-IF ad content MPD.
- F-0010-H4: Visually review Part 5 Table 5 IF-5 multi-Period ad insertion.
- F-0010-H5: Decide Table 4/Table 5 canonical table reuse strategy.

### Phase 2: structural validator coverage

- F-0010-B1: Implement DASH-IF ad content MPD structural validator checks.
- F-0010-B2: Add DASH-IF ad content MPD positive and negative test vectors.
- F-0010-C1: Implement IF-5 multi-Period structural validator checks.
- F-0010-C2: Reuse Table 4 checks for source ad-content MPDs used by IF-5.
- F-0010-C3: Add IF-5 SSAI scenario test vectors.

### Phase 3: SCTE-35 opportunity-event coverage

- F-0010-A1: Implement MPD-level SCTE-35 EventStream checks.
- F-0010-A2: Add SCTE-35 payload-aware checks.
- F-0010-A3: Add IF-3 SCTE-35 positive and negative test vectors.

### Phase 4: runtime/reference-client/test-assets coverage

- F-0010-D1: Document livesim2 SGAI scenario mapping.
- F-0010-D2: Add or identify dash.js SGAI sample coverage.
- F-0010-D3: Add SGAI remote-resolution test-asset entries.
- F-0010-F1: Define Part 6 alignment points for IF-9 clear/encrypted transitions.
- F-0010-F2: Add dash.js clear/encrypted ad insertion playback test assets.
- F-0010-E1: Define VAST tracking callback timeline assets.
- F-0010-E2: Define Open Measurement integration sample.

### Phase 5: cross-part integration

- F-0010-G1: Harmonize Part 5 cross-part anchors with Parts 1, 2, 6, 10, and 12.
- F-0010-G2: Normalize Part 5 terminology and bibliography across parts.
- F-0010-G3: Update Part 12 conformance mapping after validator/test planning stabilizes.

## Part 9 status

Part 9 text/subtitle work is now active and includes a conformance coverage
report:

```text
rag/reports/part09-conformance-coverage.md
rag/reports/reconcile-part09-text.md
```

Part 12 contains an initial Part 9 text-track conformance mapping.

## Part 12 status

Part 12 remains one of the more mature authored parts and now includes
additional cross-part conformance mappings for:

- Part 9 text/caption/subtitle requirements,
- Part 5 ad-insertion requirements.

Primary source:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md
```

## Governance status

The feature registry now tracks cross-part features, including the new F-0010:

```text
docs/governance/feature-registry.md
```

Relevant feature entries include:

- F-0006: conformance mapping pass across parts,
- F-0007: cross-part anchor and terminology harmonization,
- F-0009: Part 9 text-track conformance coverage,
- F-0010: Part 5 ad-insertion conformance and cross-part indexing.

## Validation status

Latest validation command:

```powershell
python "c:\Users\tsto\OneDrive - Qualcomm\Projects\DASH-IF\IOP\IOPv5-tstock-worktree\rag-authoring-starter\tools\publication\check_links.py"
```

Latest result:

```text
OK: checked 38 file(s), no issues found.
```

The validation reports modal keyword counts and checks authored sources for link
and heading issues.

Bikeshed HTML build validation remains subject to the known corporate
TLS/Bikeshed remote-data update setup. The recommended local setup remains to
use the corporate CA bundle tooling before running Bikeshed update/build.

## Proposed next steps

The detailed execution plan for the agreed migration sequence is:

```text
rag/reports/project-migration-execution-plan.md
```

Recommended priority order:

1. stabilize Part 5 Ad Insertion / F-0010,
2. complete Part 9 Text conformance alignment,
3. continue Part 6 Content Protection,
4. keep Part 12 synchronized after each substantive Part 5/6/9 change,
5. return to Parts 7, 8, 10, and 11 as structured migrations,
6. run cross-part harmonization.

### Immediate next steps

1. Create GitHub issues from:
   ```text
   rag/reports/part05-f0010-issue-index.md
   ```
2. Start F-0010-H1 through F-0010-H5 to stabilize Part 5 tables and figures.
3. Visually inspect the published DOCX/PDF for:
   - Figure 1,
   - Figure 3,
   - Figure 4,
   - Figure 5,
   - Figure 6,
   - Figure 7,
   - Table 2,
   - Table 4,
   - Table 5.
4. Convert F-0010-B/C/A validator matrices into validator/test-asset issues.
5. Continue Part 6 and Part 9 reconciliation in parallel, keeping Part 12
   conformance mapping synchronized.

### Medium-term plan

1. Complete Part 5 source hardening and table/figure review.
2. Implement or scope Part 5 validator checks and test assets.
3. Align Part 5 IF-6/IF-7 with Part 10 event and remote-resolution work.
4. Align Part 5 IF-9 with Part 6 content protection and Part 12 dash.js/MSE/EME
   coverage.
5. Extend F-0006 conformance mapping across all substantive parts.
6. Normalize cross-part anchors and terminology under F-0007.

### Publication/review plan

1. Keep Bikeshed Markdown as canonical source.
2. Use `check_links.py` before commits and pull requests.
3. Use GitHub pull-request build artifacts for review.
4. Use manual branch preview workflow only for non-confidential review builds.
5. Avoid committing access-controlled source documents or private extracted
   binary assets.

## Commit scope

This status update is intended to be committed together with:

- Part 5 migration and F-0010 planning reports,
- Part 12 conformance mapping updates,
- governance feature-registry updates,
- Part 6 and Part 9 reconciliation updates already present in the worktree,
- README/status updates.