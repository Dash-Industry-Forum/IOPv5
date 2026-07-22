# Document porting status map

Generated: 2026-07-22

This map tracks the porting status of DASH-IF IOP v5 content from the original DOCX drafts to the current Bikeshed/Markdown source structure.

## Porting status legend

```text
✓ Complete: Content ported, reconciled, and synchronized with current source
◐ Partial: Content ported but requires reconciliation or additional work
○ Not started: Content not yet ported or placeholder only
⊗ Deferred: Content intentionally deferred or deprecated
```

## Part-by-part porting status

| Part | Status | Source provenance | Current location | Reconciliation report | Notes |
|---|---|---|---|---|---|
| Part 1 Overview | ✓ | DASH-IF-IOPv5.0-Part01-DRAFT.docx | `specs/part01-overview/` | N/A | Architecture and scope ported. |
| Part 2 Core CMAF | ◐ | DASH-IF-IOPv5.0-Part02-DRAFT.docx | `specs/part02-core-cmaf/01-core-cmaf.inc.md` | `rag/reports/reconcile-part02-core-cmaf.md` | Core CMAF requirements ported; Phase 1 Guidelines-TimingModel integration complete (timing model, addressing modes, terminology). Phases 2-3 pending. |
| Part 3 On-Demand | ◐ | DASH-IF-IOPv5.0-Part03-DRAFT.docx | `specs/part03-on-demand/01-on-demand.inc.md` | Needed | On-demand service requirements ported; timing model cross-references require Guidelines-TimingModel integration. |
| Part 4 Live/Low-Latency | ◐ | DASH-IF-IOPv5.0-Part04-DRAFT.docx | `specs/part04-live-low-latency/00-live-services.inc.md`; `specs/part04-live-low-latency/02-low-latency.inc.md` | Needed | Live and low-latency requirements ported; timing model and availability window discussion requires Guidelines-TimingModel integration. |
| Part 5 Ad Insertion | ◐ | DASH-IF-IOPv5.0-Part05-DRAFT.docx | `specs/part05-ad-insertion/05-ad-insertion.inc.md` | `rag/reports/reconcile-part05-ad-insertion.md` | IF-3 through IF-9 ported; M1 visual review and validator-start work in progress. |
| Part 6 Content Protection | ◐ | DASH-IF-IOPv5.0-Part06-DRAFT.docx | `specs/part06-content-protection/06-content-protection.inc.md`; `specs/part06-content-protection/90-enhanced-clear-key.inc.md` | `rag/reports/reconcile-part06-content-protection.md` | Core DRM and Enhanced Clear Key ported; IF-9 cross-references with Part 5 require synchronization. |
| Part 7 Video | ○ | DASH-IF-IOPv5.0-Part07-DRAFT.docx | `specs/part07-video/07-video.inc.md` | Needed | Video codec and profile requirements ported but require reconciliation and validator planning. |
| Part 8 Audio | ○ | DASH-IF-IOPv5.0-Part08-DRAFT.docx | `specs/part08-audio/08-audio.inc.md` | Needed | Audio codec and profile requirements ported but require reconciliation and validator planning. |
| Part 9 Text | ◐ | DASH-IF-IOPv5.0-Part09-DRAFT.docx | `specs/part09-text/09-text.inc.md` | `rag/reports/reconcile-part09-text.md` | Text, subtitle, and caption requirements ported; validator-start and test-vector inventory in progress. |
| Part 10 Events | ○ | DASH-IF-IOPv5.0-Part10-DRAFT.docx | `specs/part10-events/10-events.inc.md` | Needed | Event signalling requirements ported but require reconciliation and validator planning. |
| Part 11 Additional Technologies | ○ | DASH-IF-IOPv5.0-Part11-DRAFT.docx | `specs/part11-additional-technologies/11-additional-technologies.inc.md` | Needed | Additional technology requirements ported but require reconciliation. |
| Part 12 Conformance and Reference Tools | ◐ | DASH-IF-IOPv5.0-Part12-DRAFT.docx | `specs/part12-conformance-reference-tools/01-conformance.inc.md` | N/A | Conformance, dash.js, livesim2, and test-asset sections ported and updated; validator-start coverage table added. |

## Cross-cutting porting work

### Guidelines-TimingModel integration

**Repository:** https://github.com/Dash-Industry-Forum/Guidelines-TimingModel

**Target parts:** Part 2 (primary), Part 3, Part 4

**Status:** Phase 1 complete (Part 2 core timing model and addressing modes)

**Integration artifacts:**

- `rag/reports/guidelines-timing-model-integration-plan.md` - Overall integration plan
- `rag/reports/part02-timing-model-integration-status.md` - Part 2 integration tracking
- `rag/reports/reconcile-part02-core-cmaf.md` - Part 2 reconciliation report
- `rag/reports/guidelines-timing-model-integration-session-summary.md` - Session summary

**Phase 1 completed (2026-07-22):**

- Phase 1A: MPD timeline and period timing expansion (commit e78bf8c)
- Phase 1B: Segment addressing modes expansion (commit c3716da)
- Phase 1C: Terminology cross-reference (commit 4263c1c)

**Content integrated:**

- MPD Timeline subsection with BasicMpdElements.png diagram
- Period Timing subsection with PeriodsMakeTheMpd.png diagram
- First and Last Period Timing subsection
- Indexed Addressing subsection with IndexedAddressing.png diagram
- Explicit Addressing subsection
- Simple Addressing subsection
- Terminology Cross-Reference table

**Remaining phases:**

- Phase 2: Part 3 On-Demand timing constraints
- Phase 3: Part 4 Live/Low-Latency timing constraints

**Precedence rule:**

```text
ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel
```

All integrated content follows this precedence rule. No conflicts identified.

### Table and figure porting

Many parts include tables and figures from the original DOCX drafts. The porting status for these visual elements is tracked separately:

- **Part 5:** `rag/reports/part05-f0010-table-figure-hardening.md`
- **Part 9:** Implicit in `rag/reports/part09-conformance-coverage.md`
- **Other parts:** Require dedicated table/figure porting reports.

### Conformance keyword and modal verb usage

All parts use conformance keywords (`shall`, `should`, `may`, etc.). The modal verb counts are tracked by `tools/publication/check_links.py` and reported in Part 12.

## Recommended next porting steps

1. **Clone Guidelines-TimingModel locally** and create `rag/reports/guidelines-timing-model-integration-plan.md`.
2. **Reconcile Parts 7 and 8** (video and audio) with validator planning similar to Parts 2, 3, 4, 5, and 9.
3. **Reconcile Part 10** (events) and align with Part 5 ad-insertion event signalling.
4. **Reconcile Part 11** (additional technologies) and identify any deprecated or deferred content.
5. **Create table/figure porting reports** for Parts 2, 3, 4, 6, 7, 8, 10, and 11.
6. **Synchronize Part 6 IF-9 cross-references** with Part 5 ad-insertion encrypted playback requirements.

## Current porting metrics

| Metric | Count |
|---|---|
| Parts with complete porting | 1 (Part 1) |
| Parts with partial porting | 6 (Parts 2, 3, 4, 5, 6, 9, 12) |
| Parts requiring reconciliation | 5 (Parts 7, 8, 10, 11, and timing model integration for Parts 2-4) |
| Parts with validator-start coverage | 5 (Parts 2, 3, 4, 5, 9) |
| Parts with reconciliation reports | 4 (Parts 2, 5, 6, 9) |
| Parts requiring Guidelines-TimingModel integration | 3 (Parts 2, 3, 4) |