# Document porting status map

Generated: 2026-07-28 (updated from 2026-07-22)

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
| Part 2 Core CMAF | ✓ | DASH-IF-IOPv5.0-Part02-DRAFT.docx + Guidelines-TimingModel | `specs/part02-core-cmaf/01-core-cmaf.inc.md` | `rag/reports/reconcile-part02-core-cmaf.md` | Guidelines-TimingModel integration complete (Phases 1-13, 2026-07-28). ~1,200 lines added, 29 diagrams, validator updated. Open issues remain (SegmentTemplate table, segment-list formulae). |
| Part 3 On-Demand | ◐ | DASH-IF-IOPv5.0-Part03-DRAFT.docx | `specs/part03-on-demand/01-on-demand.inc.md` | Needed | On-demand requirements ported; static coverage diagram added; open issues: profile URIs, sidx constraints, trick modes. |
| Part 4 Live/Low-Latency | ◐ | DASH-IF-IOPv5.0-Part04-DRAFT.docx + Guidelines-TimingModel | `specs/part04-live-low-latency/00-live-services.inc.md`; `specs/part04-live-low-latency/02-low-latency.inc.md` | Needed | Live service timing complete (availability window, TSB, MPD updates). Low-latency (`02-low-latency.inc.md`) needs review. |
| Part 5 Ad Insertion | ◐ | DASH-IF-IOPv5.0-Part05-DRAFT.docx | `specs/part05-ad-insertion/05-ad-insertion.inc.md` | `rag/reports/reconcile-part05-ad-insertion.md` | IF-3 through IF-9 ported; M1 visual review and validator-start work in progress. |
| Part 6 Content Protection | ◐ | DASH-IF-IOPv5.0-Part06-DRAFT.docx | `specs/part06-content-protection/06-content-protection.inc.md`; `specs/part06-content-protection/90-enhanced-clear-key.inc.md` | `rag/reports/reconcile-part06-content-protection.md` | Core DRM and Enhanced Clear Key ported; IF-9 cross-references with Part 5 require synchronization. |
| Part 7 Video | ◐ | DASH-IF-IOPv5.0-Part07-DRAFT.docx | `specs/part07-video/07-video.inc.md` | Needed | H.264/AVC and H.265/HEVC ported (187 lines). HDR, UHD 4K, Dolby Vision dual-stream, VP9 clauses not yet migrated. No validator or conformance mapping. |
| Part 8 Audio | ◐ | DASH-IF-IOPv5.0-Part08-DRAFT.docx | `specs/part08-audio/08-audio.inc.md` | Needed | Audio codec requirements ported but require reconciliation and validator planning. |
| Part 9 Text | ◐ | DASH-IF-IOPv5.0-Part09-DRAFT.docx | `specs/part09-text/09-text.inc.md` | `rag/reports/reconcile-part09-text.md` | Text, subtitle, and caption requirements ported; validator-start and test-vector inventory in progress. |
| Part 10 Events | ◐ | DASH-IF-IOPv5.0-Part10-DRAFT.docx | `specs/part10-events/10-events.inc.md` | Needed | Event signalling requirements ported but require reconciliation and alignment with Part 5 ad-insertion event signalling. |
| Part 11 Additional Technologies | ◐ | DASH-IF-IOPv5.0-Part11-DRAFT.docx | `specs/part11-additional-technologies/11-additional-technologies.inc.md` | Needed | Additional technology requirements ported but require reconciliation. |
| Part 12 Conformance and Reference Tools | ✓ | DASH-IF-IOPv5.0-Part12-DRAFT.docx | `specs/part12-conformance-reference-tools/01-conformance.inc.md` | N/A | Conformance mappings complete for Parts 2, 3, 4, 5, 9 (v0.5). Validator-start coverage table complete. |

## Cross-cutting porting work

### Guidelines-TimingModel integration ✅ COMPLETE

**Repository:** https://github.com/Dash-Industry-Forum/Guidelines-TimingModel

**Target parts:** Part 2 (primary), Part 3, Part 4

**Status:** All phases complete (Phases 1-13, 2026-07-22 to 2026-07-28)

**Coverage:** ~95% of Guidelines-TimingModel integrated

**Phases completed:**
- Phase 1A-D: Core timing model, addressing modes, terminology (Part 2)
- Phase 2: Static presentation timing (Part 3)
- Phase 3: Dynamic presentation timing (Part 4)
- Phase 4: Core timing expansion — clock drift, clock sync, segment references (Part 2)
- Phase 5A: Period connectivity and boundary timing (Part 2)
- Phase 5B: Non-equal length tracks and period splitting (Part 2)
- Phase 6: Live service timing — availability window, TSB, presentation delay (Part 4)
- Phase 7: Timing constraints — ECMAScript 2⁵³ limit, xs:duration (Part 2)
- Phase 8: MPD updates, period continuity, segment loss handling (Parts 2 + 4)
- Phase 9: Stand-alone text timing, forbidden techniques (Part 2)
- Phase 10: Terminology choices (Part 2)
- Phase 11: Part 12 conformance mappings for Parts 2 and 4
- Phase 12: Part 12 conformance mapping for Part 3; Part 3 enhancement
- Phase 13: Part 2 validator updated with 14 new timing model check codes

**Precedence rule:**
```text
ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel
```

### Table and figure porting

Many parts include tables and figures from the original DOCX drafts. The porting status for these visual elements is tracked separately:

- **Part 5:** `rag/reports/part05-f0010-table-figure-hardening.md`
- **Part 9:** Implicit in `rag/reports/part09-conformance-coverage.md`
- **Other parts:** Require dedicated table/figure porting reports.

### Conformance keyword and modal verb usage

All parts use conformance keywords (`shall`, `should`, `may`, etc.). The modal verb counts are tracked by `tools/publication/check_links.py` and reported in Part 12.

## Recommended next porting steps

### High Priority

1. **Part 7 Video — complete migration** (HDR, UHD 4K, Dolby Vision, VP9 clauses)
   - Source: `v5-old-draft/80-Codecs.inc.md` and `v5-old-draft/27-AdaptationSets.inc.md`
   - Add Part 12 conformance mapping for Part 7
   - Add validator-start tool

2. **Part 8 Audio — reconciliation**
   - Review current content against source DOCX
   - Add Part 12 conformance mapping for Part 8
   - Add validator-start tool

3. **Part 10 Events — reconciliation**
   - Align with Part 5 ad-insertion event signalling
   - Add Part 12 conformance mapping for Part 10

### Medium Priority

4. **Part 4 Low-Latency** (`02-low-latency.inc.md`) — review and enhance
5. **Part 6 IF-9 cross-references** — synchronize with Part 5 encrypted playback
6. **Part 11 Additional Technologies** — reconciliation and deferred content review
7. **Part 3 open issues** — profile URIs, sidx constraints, trick modes

### Lower Priority

8. **Example MPDs** — add concrete examples to `specs/*/examples/` directories
9. **Part 2 open issues** — SegmentTemplate parameter table, segment-list formulae
10. **PR review and merge** — merge `tstockhammer-rag-workflow` into `main`

## Current porting metrics (2026-07-28)

| Metric | Count |
|---|---|
| Parts with complete porting | 3 (Parts 1, 2, 12) |
| Parts with partial porting | 9 (Parts 3, 4, 5, 6, 7, 8, 9, 10, 11) |
| Parts with validator-start coverage | 5 (Parts 2, 3, 4, 5, 9) |
| Parts with reconciliation reports | 4 (Parts 2, 5, 6, 9) |
| Parts with Part 12 conformance mappings | 5 (Parts 2, 3, 4, 5, 9) |
| Guidelines-TimingModel integration | ✅ Complete (~95%) |
| Open GitHub PRs | 1 (`tstockhammer-rag-workflow`) |