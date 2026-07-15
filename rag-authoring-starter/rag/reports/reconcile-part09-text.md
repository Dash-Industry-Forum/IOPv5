# Part 9 text reconciliation crosswalk

Generated: 2026-07-15

This report maps the published DASH-IF IOP v5.0.0 Part 9 source against the
current Bikeshed source in `specs/part09-text/`.

Source inputs:

- Published source: `rag/corpus/published/DASH-IF-IOPv5.0.0-Part9-FINAL.docx`
- Extracted text: `rag/corpus/published/DASH-IF-IOPv5.0.0-Part9-FINAL.docx.extracted.txt`
- Current Bikeshed source:
  - `specs/part09-text/part09-text.bs`
  - `specs/part09-text/09-text.inc.md`

## Summary

Part 9 is compact and suitable for migration in a single first pass. The current
Bikeshed source already contains CEA-608/708 and IMSC1 material migrated from an
older DASH-IF IOP draft, but it is missing the explicit published v5.0.0
structure for CMAF media profiles, text/video adaptation-set tables, chunks and
gaps, and client-selection recommendations.

Recommended status label for Part 9:

```text
Draft/reconciliation
```

## Published heading structure

The extracted published Part 9 heading candidates are:

- Executive Summary
- Introduction
- Scope
- References
- Normative references
- Informative references
- Definition of terms, symbols and abbreviations
- Terms
- Symbols
- Abbreviations
- CMAF Media Profiles
- Adaptation Set requirements and recommendations
- Content requirements
- Text tracks
- Video tracks
- General
- CTA 608/708
- Chunks and gaps
- Client recommendations
- Annex A (informative): Change History

## Current Bikeshed heading structure

Current Part 9 source headings before this reconciliation pass include:

- Scope
- References
- Terms and Definitions
- Text Adaptation Set Constraints
- CEA-608/708 Digital Television (DTV) Closed Captioning
- Timed Text (IMSC1)
- Requirements and Recommendations
- Open Issues and Work Items
- Change History

## Clause crosswalk

| Published heading | Current Bikeshed location | Status | Action |
|---|---|---|---|
| Executive Summary | `09-text.inc.md` / overview text | Added/reconciled | Preserve published summary in introduction. |
| Introduction | `09-text.inc.md` / `#part9-introduction` | Added/reconciled | Add multipart context and scope summary. |
| Scope | `09-text.inc.md` / `#scope` | Present; updated | Add published exclusion of sidecar files. |
| References | `part09-text.bs` bibliography and `09-text.inc.md` references | Added/reconciled; needs final citation policy review | Added bibliography entries for ISO/IEC 14496-30, SCTE 214-1, SCTE 128-1, IMSC1, WebVTT, CTA-608-E, CTA-708-E, DASH-IF IOP v4.3, Part 7 Video, and SMPTE 2052-10/11. |
| Normative references | `.bs` biblio | Added/reconciled; needs final citation policy review | Added ISO/IEC 14496-30 and SCTE 214-1 citations. |
| Informative references | `.bs` biblio | Added/reconciled; needs final citation policy review | Added IOP v4.3, Part 7 Video, IMSC1, WebVTT, CTA and SCTE references. |
| Terms | `09-text.inc.md` / `#terms` | Added/reconciled | Added published term set for captions/subtitles and retained text adaptation set definition. |
| Symbols | `09-text.inc.md` / `#symbols-abbreviations` | Added/reconciled | Published symbols section was empty; local abbreviations table now covers extracted abbreviations. |
| Abbreviations | `09-text.inc.md` / `#symbols-abbreviations` | Added/reconciled | Added published abbreviation set. |
| CMAF Media Profiles | `09-text.inc.md` / `#text-cmaf-media-profiles` | Added/reconciled | Table with IMSC1 Text, IMSC1 Image, WebVTT, and CTA 608/708 now matches extracted published table values. |
| Adaptation Set requirements and recommendations | `09-text.inc.md` / `#adaptation-set-requirements` | Added/reconciled | Add overview and table-based requirements. |
| Content requirements | `09-text.inc.md` / `#content-requirements` | Added/reconciled | Add text track, video track, chunks/gaps substructure. |
| Text tracks | `09-text.inc.md` / `#text-tracks` | Added/reconciled | Add published annotation requirements. |
| Video tracks | `09-text.inc.md` / `#video-tracks` | Added/reconciled | Add CTA 608/708 video-track signaling. |
| CTA 608/708 | `09-text.inc.md` / `#codecs-cea608` | Present; updated | Current source mostly matches; align language-only/multi-channel recommendations. |
| Chunks and gaps | `09-text.inc.md` / `#chunks-and-gaps` | Added/reconciled | Add text non-chunking and empty-document guidance. |
| Client recommendations | `09-text.inc.md` / `#client-recommendations` | Added/reconciled | Add selection algorithm baseline. |
| Annex A Change History | `09-text.inc.md` / `#change-history` | Present; updated | Add published v5.0.0 row. |

## High-priority remaining review items

1. Verify exact table values against the published Part 9 DOCX/PDF:
   - Table 1 CMAF Media Profile parameters.
   - Table 2 Text track Adaptation Set attributes and elements.
   - Table 3 Video track Adaptation Set attributes and elements.

   Status: initial table stabilization completed against extracted text. Remaining
   review should compare generated HTML to the published PDF/DOCX for formatting
   and any DOCX table extraction artifacts.

2. Confirm bibliographic aliases in `part09-text.bs`:
   - MPEG DASH
   - CMAF
   - ISO/IEC 14496-30
   - SCTE 214-1
   - IMSC1 / TTML references
   - DASH-IF IOP v4.3
   - Part 7 Video

   Status: bibliography aliases added. Remaining review is citation policy and
   whether any entries should use shared Bikeshed reference names instead of
   local biblio aliases.

3. Decide whether symbols and abbreviations should be local or shared.

   Status: local terms and abbreviations added for the published Part 9 baseline.

4. Align client recommendation wording with Part 2 selection behavior.

5. Link testable Part 9 requirements to Part 12 conformance inventory.

## Recommended next implementation pass

After this first migration pass:

1. Build/validate the current source.
2. Create focused issues for exact table verification.
3. Compare Part 9 generated HTML against published Part 9 for missing tables,
   anchors, and references.
4. Start Part 9 conformance mapping once table values are stable.