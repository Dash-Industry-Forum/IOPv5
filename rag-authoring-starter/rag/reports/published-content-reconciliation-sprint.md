# Published-content reconciliation sprint

Generated: 2026-07-15

This report starts the reconciliation sprint for IOP v5 parts whose current
Bikeshed source may diverge from already-published DASH-IF IOP v5 documents.

The immediate goal is not to produce an authoritative redline. The goal is to
turn the current uncertainty into concrete editorial work packages: identify the
published source, identify the current in-repo source, estimate the size of the
gap, and define the next reconciliation action.

## Scope

Initial sprint scope:

| Part | Published input | Current repository source |
|---|---|---|
| Part 5 | `rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx` | `specs/part05-ad-insertion/` |
| Part 6 | `rag/corpus/published/DASH-IF-IOPv5.1.0-Part6.pdf` | `specs/part06-content-protection/` |
| Part 8 | `rag/corpus/published/DASH-IF-IOP-Part8-v5.1.0.docx` | `specs/part08-audio/` |
| Part 9 | `rag/corpus/published/DASH-IF-IOPv5.0.0-Part9-FINAL.docx` | `specs/part09-text/` |

## Execution performed

1. Confirmed published corpus files for Parts 5, 6, 8, and 9.
2. Installed the optional extraction dependencies from `requirements.txt`.
3. Re-ran `tools/ingest/extract_text.py` for manifest-managed sources.
4. Manually extracted the published Part 8 and Part 9 DOCX files because they are
   present in `rag/corpus/published/` but not yet represented in `rag/sources.yaml`.
5. Compared current Bikeshed source size and heading samples against published
   extracted text.

## Extraction status

| Part | Extraction status | Notes |
|---|---|---|
| Part 5 | Extracted | Manifest source `dashif-iop-v5-part5`; DOCX extracted by `extract_text.py`. |
| Part 6 | Extracted | Manifest source `dashif-iop-v5-part6-v5-1`; PDF extracted by `extract_text.py`. |
| Part 8 | Extracted manually | Published DOCX exists but is not currently in `rag/sources.yaml`; extracted using `python-docx`. |
| Part 9 | Extracted manually | Published FINAL DOCX exists but is not currently in `rag/sources.yaml`; extracted using `python-docx`. |

Generated extraction artifacts:

- `rag/corpus/published/DASH-IF-IOP-Part8-v5.1.0.docx.extracted.txt`
- `rag/corpus/published/DASH-IF-IOP-Part8-v5.1.0.docx.extracted.json`
- `rag/corpus/published/DASH-IF-IOPv5.0.0-Part9-FINAL.docx.extracted.txt`
- `rag/corpus/published/DASH-IF-IOPv5.0.0-Part9-FINAL.docx.extracted.json`

## Current gap estimate

| Part | Current Bikeshed source | Published extracted source | Initial assessment |
|---|---:|---:|---|
| Part 5 | 1 include file, 56 lines, 6 headings | 941 extracted lines | Current repo source is a shell. Major migration required. |
| Part 6 | 6 include files, 1184 lines, 45 headings | 1240 extracted lines | Current repo source is substantially populated. Needs detailed clause-by-clause reconciliation, not a wholesale migration. |
| Part 8 | 1 include file, 175 lines, 17 headings | 407 extracted paragraphs, 56 headings | Current repo source is a scaffold and likely omits substantial published v5.1.0 text. |
| Part 9 | 1 include file, 132 lines, 9 headings | 155 extracted paragraphs, 20 headings | Current repo source is a scaffold and likely omits published FINAL v5.0.0 structure/content. |

## Heading evidence

### Part 5: Ad Insertion

Current repository headings:

- Scope
- References
- Terms and Definitions
- Requirements and Recommendations
- Open Issues and Work Items
- Change History

Published source heading/sample structure:

- Scope
- References
- Normative references
- Informative references
- Definition of terms, symbols and abbreviations
- Introduction
- Use Cases and Scenarios
- VoD
- Live
- Recorded Live
- Pre-Roll into Live
- Obfuscation of Inserted Ads
- Architectures
- Overview on Interfaces and Functions
- Interfaces
- IF-0: ABR Stream Source
- IF-1 and following interface clauses

Assessment:

Part 5 is not reconciled. The current Bikeshed source is only a high-level shell
and does not yet contain the published document's substantive architecture,
interfaces, workflow, and ad-insertion material.

Next action:

Create a migration map from the published Part 5 document into the Bikeshed
structure, then migrate one major section at a time:

1. front matter and terminology,
2. Introduction/use cases,
3. architecture/interface overview,
4. interface clauses,
5. requirements/recommendations,
6. examples/figures/tables,
7. open issues/change history.

### Part 6: Content Protection and Security

Current repository headings include:

- Purpose
- Scope
- Interpretation
- Disclaimer
- Migration Notes
- Open Issues and Work Items
- Change History
- Core concepts of content protection and security
- Client reference architecture for encrypted content playback
- Content encryption and DRM
- Robustness
- W3C Encrypted Media Extensions
- Content protection constraints for CMAF
- Content protection data in CMAF containers
- Encryption and DRM signaling in the MPD
- Signaling presence of encrypted content
- `default_KID` handling
- DRM system configuration
- License request model
- Client workflows
- Miscellaneous constraints

Published source heading/sample structure:

- Scope
- References
- Definition of terms, symbols and abbreviations
- Core concepts of content protection and security
- Introduction
- Client reference architecture for content playback
- Compliances and robustness rules
- W3C Encrypted Media Extensions
- DASH-IF XML schema
- License acquisition URL
- Authorization server URL
- Certificate acquisition URL
- Content protection constraints for CMAF
- Content protection data
- Content protection data constraints
- Content encryption
- Content protection constraints for the MPD

Assessment:

Part 6 is the most advanced of the reconciliation targets. The in-repo source is
roughly comparable in size to the extracted published document and already covers
many of the same conceptual areas. However, headings are not one-to-one:

- The repo appears to have reorganized and possibly expanded the text.
- Published sections such as "DASH-IF XML schema" and URL-specific schema
  clauses need explicit traceability to the current source.
- The current repo source uses newer editorial framing such as Purpose,
  Interpretation, Disclaimer, and Migration Notes that may not map directly to
  the published document.
- This part needs clause-level comparison rather than a simple migration.

Next action:

Produce a Part 6 clause crosswalk:

| Published clause | Current Bikeshed location | Status |
|---|---|---|
| Scope | TBD | confirm migrated |
| References | TBD | confirm migrated |
| Terms/symbols/abbreviations | TBD | confirm migrated |
| Core concepts | TBD | compare text |
| DASH-IF XML schema | TBD | verify present |
| License acquisition URL | TBD | verify present |
| Authorization server URL | TBD | verify present |
| Certificate acquisition URL | TBD | verify present |
| CMAF constraints | TBD | compare text |
| MPD constraints | TBD | compare text |

Recommended order: start Part 6 first because it is close enough to reconcile
quickly and can establish the reconciliation pattern for the remaining parts.

### Part 8: Audio

Current repository headings include:

- Scope
- References
- Terms and Definitions
- Audio Adaptation Set Constraints
- Audio Codecs
- HE-AACv2 audio (stereo)
- HE-AACv2 audio (multichannel)
- Enhanced AC-3
- Dolby TrueHD
- AC-4
- DTS-HD
- MPEG Surround
- MPEG-H 3D Audio
- MPEG-D Unified Speech and Audio Coding
- Requirements and Recommendations
- Open Issues and Work Items
- Change History

Published source heading/sample structure:

- Scope
- References
- Normative references
- Informative references
- Definition of terms, symbols and abbreviations
- CMAF Media Profiles
- Media Profiles
- CMAF Audio Adaptation Sets
- NGA and Preselections
- Overview
- Signalling of Preselections
- Media Profile Specific Information
- MPEG High Efficiency AAC, Stereo
- DASH-specific aspects for HE-AACv2 audio Level 2
- AAC Audio Metadata
- ISO/IEC 23009-1 audio data
- MPEG-4 High Efficiency AAC Profile v2, Multichannel
- Dolby Multichannel Technologies

Assessment:

Part 8 has a useful codec-oriented scaffold, but the published v5.1.0 document
contains additional structure around CMAF media profiles, NGA/preselections, and
media-profile-specific information. The current source is likely not a faithful
representation of the published document yet.

Next action:

Do not continue speculative new Part 8 authoring until published v5.1.0 content
is mapped. Add the published Part 8 document to `rag/sources.yaml`, chunk it, and
prepare a section migration/crosswalk.

### Part 9: Text/Subtitles

Current repository headings:

- Scope
- References
- Terms and Definitions
- Text Adaptation Set Constraints
- CEA-608/708 Digital Television (DTV) Closed Captioning
- Timed Text (IMSC1)
- Requirements and Recommendations
- Open Issues and Work Items
- Change History

Published source heading/sample structure:

- Executive Summary
- Introduction
- Scope
- References
- Normative references
- Informative references
- Definition of terms, symbols and abbreviations
- CMAF Media Profiles
- Adaptation Set requirements and recommendations
- Content requirements
- Text tracks
- Video tracks
- CTA 608/708
- Chunks and gaps
- Client recommendations
- Annex A
- Change History

Assessment:

Part 9 is a compact but real published document. The current repository source
captures only the broad topic outline. It likely misses published structural
material around CMAF media profiles, adaptation-set requirements, content
requirements, chunks/gaps, client recommendations, annexes, and change history.

Next action:

Part 9 is a good second reconciliation target after Part 6 because the published
document is relatively compact.

## Cross-cutting findings

1. `rag/sources.yaml` is incomplete for published Parts 8 and 9.
   - The files exist in `rag/corpus/published/`.
   - They are not represented as manifest sources.
   - As a result, the standard `extract_text.py`, chunking, indexing, and query
     flow does not manage them yet.

2. Part 6 source appears more mature than the older backlog wording suggests.
   - It should be reclassified from "shell" language to "substantive draft under
     reconciliation" once clause crosswalk confirms coverage.

3. Part 5 remains a large migration task.
   - It should not be treated as ready for review.

4. Parts 8 and 9 need published-document-first reconciliation before further
   editorial expansion.

## Recommended sprint sequence

1. **Part 6 clause crosswalk**
   - Highest return because the repository source is already substantial.
   - Goal: confirm whether the current source preserves all published v5.1.0
     content.

2. **Part 9 migration**
   - Compact published FINAL source.
   - Good candidate for a full migration/reconciliation pass.

3. **Part 5 migration**
   - Larger published source.
   - Requires structured migration into Bikeshed sections.

4. **Part 8 reconciliation**
   - More complex due to codec/media-profile structure and current scaffold
     differences.
   - Should follow after the Part 6/9 process is proven.

## Immediate follow-up tasks

- Add published Part 8 and Part 9 to `rag/sources.yaml`.
- Run `tools/rag/chunk.py` after manifest update so all four parts are queryable
  through the standard RAG workflow.
- Create a dedicated `reconcile-part06-content-protection.md` clause crosswalk.
- Update `program-backlog.md` to reflect:
  - Part 6 is substantive but unreconciled, not merely a shell.
  - Part 8 and Part 9 published sources need manifest entries.
  - Part 5 remains major migration.
- After each migration/reconciliation pass, run:
  - `python tools/publication/check_links.py`
  - `python tools/publication/build_all.py --out ../dist`