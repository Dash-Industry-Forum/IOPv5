# DASH-IF IOP v5 Authoring Status Report

**Date:** 2026-07-28  
**Branch:** `tstockhammer-rag-workflow`  
**Repository:** [Dash-Industry-Forum/IOPv5](https://github.com/Dash-Industry-Forum/IOPv5)  
**Preview:** [https://dashif.org/IOPv5/previews/tstockhammer-rag-workflow/](https://dashif.org/IOPv5/previews/tstockhammer-rag-workflow/)

---

## Executive Summary

All 12 parts of DASH-IF IOP v5 are now in the Bikeshed authoring workspace as
Working Draft documents. The publication infrastructure (CI workflow, `build_all.py`,
shared boilerplate, image copying) is operational. All known hanging paragraphs
have been fixed. The DASH-IF Registries section and review/contribution workflow
have been added to Part 1.

Parts 2, 4, 6, 7, 8, 9, 10, and 12 have substantial content migrated from
published sources. Parts 3, 5, and 11 have structural skeletons with partial
content. Part 1 has been significantly enhanced with architecture, registries,
and workflow documentation.

---

## Part-by-Part Status

### Part 1 — Overview, Architecture and Interfaces (v0.3)

**Status:** Working Draft — substantially complete for Part 1 scope.

**Done:**
- Scope, references, terms, abbreviations, conformance/style conventions
- Architecture and interfaces (baseline architecture, reference client, part descriptions)
- Document Status section: Living Document, workflow (WD → WG Review → Community Review → Approved), stable/dev branch model
- Issue Reporting and Contributing/Reviewing sections (GitHub issues, PR workflow, WD/WG/CR phases)
- DASH-IF Registries section: Identifier Registry, Codec Registry, ISO/IEC 23009-1 identifier types table, registration workflow (Google Forms + GitHub issues)
- All 12 `.bs` files updated: `!Repository:`, `!Issue Tracking:`, `!Document Status:` custom metadata
- `DASHIF-IDENTIFIERS` and `DASHIF-CODECS` biblio entries

**Remaining:**
- [ ] Add cross-references from Parts 7, 8, 9 to the Identifier Registry for specific `@schemeIdUri` values used in those parts
- [ ] Improve the identifier registration workflow (replace Google Forms with a GitHub-based workflow)
- [ ] Add more ISO/IEC 23009-1 identifier types from the published standard (e.g. `@profiles` URI list, `@codecs` registry cross-reference)
- [ ] Review and finalize the Part Descriptions section once all parts reach WG Review

---

### Part 2 — Core Principles and CMAF Mapping (v0.1)

**Status:** Working Draft — substantial content migrated; several open issues remain.

**Done:**
- Scope, references, terms, abbreviations
- CMAF structural data model and CMAF-to-DASH mapping
- DASH timing model: MPD timeline, Period timing, Representation timing, sample timeline, `@presentationTimeOffset`, segment references, clock drift, clock synchronization
- Segment information: three addressing modes (indexed/SegmentBase, explicit/SegmentTimeline, simple/duration), segment list computation
- CMAF-to-DASH mappings: Period connectivity, Period continuity, samples on Period boundaries
- Non-equal length tracks: padding, cutting, Period splitting, mixed strategies
- Period splitting: when/how to split, decoder state, best practices
- Good Multi-Period CMAF content, multi-Period profile signalling
- Common service functions: bandwidth signalling, static/dynamic services, MPD updates, locations, gap handling
- Segment loss handling, stand-alone text track timing, forbidden techniques, timing constraints
- All hanging paragraphs fixed (Period Timing, Segment Information, DASH Timing Model, Period Connectivity, Non-Equal Length Tracks, Period Splitting, Representation Timing, Referencing Media Segments, Clock Drift)
- Images: all 21 PNG files present in `images/` directory

**Remaining:**
- [ ] Reconstruct SegmentTemplate parameter table (Table 5: M/O/defaults for three addressing modes)
- [ ] Complete segment-list computation formulae (carry over from v4.3 where they add value)
- [ ] Complete subsegment information (CMAF chunks, Part 4 low-latency relationship)
- [ ] Complete Good Multi-Period CMAF Content (continuous-boundary requirements, profile signalling)
- [ ] Define exact `@bandwidth` interpretation and validator expectations
- [ ] Consolidate MPD update rules with Part 4 live-service text
- [ ] Add normative client and content-author guidance for Locations/BaseURL
- [ ] Complete gap handling (service-offering and client-processing rules)
- [ ] Reconcile content annotation framework with Parts 7, 8, 9, 10

---

### Part 3 — On-Demand Services (v0.1)

**Status:** Working Draft — structural skeleton with initial content.

**Done:**
- Scope, references, terms
- On-demand services introduction and common MPD requirements
- Segment information derivation, on-demand profile, multi-Period on-demand
- Image: `StaticMpdMustBeCovered.png` present

**Remaining:**
- [ ] Migrate full on-demand service requirements from published IOP v4.3 and v5.0.0
- [ ] Add detailed on-demand profile (`@indexRange`, `sidx`) requirements
- [ ] Add trick-mode and seek requirements for on-demand
- [ ] Add conformance mapping to Part 12
- [ ] Add examples (MPD snippets for on-demand profile, multi-Period on-demand)

---

### Part 4 — Live and Low-Latency Services (v0.3)

**Status:** Working Draft — live services and low-latency content migrated.

**Done:**
- Scope, references, definitions
- Live services clause (migrated from v4.3): MPD-based live service offering, segment-based MPD update signalling, clock synchronization, time shift buffer, MPD snapshot validity, content add/remove rules
- Low-latency live services clause (migrated from Part 4 draft r1): architecture, definitions, service offering requirements, adaptation set types (chunked/segment), legacy setup, DVB LL-DASH, client requirements, guidelines (chunk duration, producer reference time, service description, resync points, fast switching, MPD generation, packager operation, client implementation, bandwidth estimation, multicast)
- All hanging paragraphs fixed
- Images: `MpdUpdate-AddContent.png`, `MpdUpdate-RemoveContent.png` at spec root; `Images/` and `Diagrams/` directories present

**Remaining:**
- [ ] Reconcile Low-Latency CR r8/r9 normative text (see `rag/reports/reconcile-low-latency-r8-r9.md`)
- [ ] Extract/redraw architecture figures (currently Issue placeholders)
- [ ] Reconstruct configuration-parameter tables (Tables 1–4 from source)
- [ ] Add Broadcast TV Profile (deferred to future version per CR r8/r9)
- [ ] Add conformance mapping to Part 12
- [ ] Align with Part 2 timing model for live-service-specific constraints

---

### Part 5 — Ad Insertion and Content Replacement (v0.12)

**Status:** Working Draft — substantial migration from published v5.0.0 Part 5.

**Done:**
- Scope, references, terms, abbreviations
- Use cases (VoD, live, recorded live, pre-roll, obfuscation, transitions)
- Architecture overview (SSAI, SGAI, functional entities)
- Interface overview table (IF-0 through IF-9)
- IF-0 (ABR stream source), IF-1 (packager ingest), IF-2 (content preparation), IF-3 (ad avail signalling with SCTE-35), IF-4 (ad decisioning: IF-4a/b/c/d/e/f), IF-5 (MPD and segments with ad placements, Table 5, MPD proxy guidelines, client playback), IF-6 (ad metadata), IF-7 (remote resolution), IF-8 (tracking/measurement), IF-9 (reference playback)
- All hanging paragraphs fixed

**Remaining:**
- [ ] Add/normalize bibliography aliases in `part05-ad-insertion.bs`
- [ ] Extract/redraw architecture figures (Figures 1, 3, 4, 5)
- [ ] Reconstruct Table 2 (DASH-IF Main live content MPD) from published source
- [ ] Visual DOCX/PDF review of Tables 4 and 5
- [ ] Align IF-7c (Remote Periods) with current DASH remote entity model
- [ ] Align IF-6 (DASH Callback Event) with Part 10 event guidance
- [ ] Add conformance mapping to Part 12

---

### Part 6 — Content Protection and Security (v0.x)

**Status:** Working Draft — substantial content from Guidelines-Security repository.

**Done:**
- Core concepts, client reference architecture, content encryption and DRM
- DRM system configuration, MPD signalling (`dashif:laurl`, `dashif:authzurl`)
- Key hierarchy and `default_KID` handling
- DASH-IF interoperable license request model (authorization tokens, proof of authorization, deployment architectures, content ID)
- DRM client workflows (capability detection, DRM selection algorithm, activation, license request workflow, unavailable keys, changing keys, protection policies)
- Periodic re-authorization, key hierarchy, W3C Clear Key, XML schema
- Enhanced Clear Key Content Protection (ECCP)
- All hanging paragraphs fixed (license request model, client workflows, ECCP)
- Images: `Diagrams/` directory with all diagrams; `Images/` directory

**Remaining:**
- [ ] Reconcile against published IOP v5.1.0 Part 6 (see `rag/reports/reconcile-part06-content-protection.md`)
- [ ] Verify/migrate certificate acquisition URL (`dashif:certurl`) from published v5.1.0
- [ ] Verify/migrate HDCP output control clause from published v5.1.0
- [ ] Normalize references and terminology against Parts 1, 2, 12
- [ ] Add conformance mapping to Part 12
- [ ] Evaluate PDF publication path (DASH-IF specs builder container)

---

### Part 7 — Video (v0.x)

**Status:** Working Draft — substantial content migrated.

**Done:**
- Scope, references, terms
- Video codec profiles: H.264/AVC, H.265/HEVC, AV1
- CMAF media profiles and DASH signalling for video tracks
- `@codecs` string requirements, CMAF profile identifiers
- Reference to DASH-IF Codec Registry
- All hanging paragraphs fixed

**Remaining:**
- [ ] Add explicit cross-references to DASH-IF Identifier Registry for video-specific `@schemeIdUri` values (e.g. `SupplementalProperty` for HDR/WCG)
- [ ] Add HDR/WCG signalling requirements (PQ, HLG, Dolby Vision)
- [ ] Add frame rate and resolution signalling requirements
- [ ] Add conformance mapping to Part 12
- [ ] Verify codec registry entries against current DASH-IF Codec Registry

---

### Part 8 — Audio (v0.x)

**Status:** Working Draft — substantial content migrated.

**Done:**
- Scope, references, terms
- Audio codec profiles: HE-AACv2, E-AC-3, AC-4, MPEG-H 3D Audio
- CMAF media profiles and DASH signalling for audio tracks
- `AudioChannelConfiguration@schemeIdUri` requirements
- Reference to DASH-IF Codec Registry and Identifier Registry
- All hanging paragraphs fixed

**Remaining:**
- [ ] Add explicit cross-references to DASH-IF Identifier Registry for `AudioChannelConfiguration@schemeIdUri` values
- [ ] Add loudness normalling requirements (ITU-R BS.1770)
- [ ] Add accessibility descriptor requirements (`Accessibility@schemeIdUri`)
- [ ] Add conformance mapping to Part 12
- [ ] Verify codec registry entries against current DASH-IF Codec Registry

---

### Part 9 — Text (Subtitle) (v0.x)

**Status:** Working Draft — reconciled against published IOP v5.0.0 Part 9.

**Done:**
- Scope, references, terms
- CMAF media profiles for IMSC1, WebVTT, closed captions (CEA-608/708)
- DASH signalling for text tracks
- Open captions (in-video)
- Conformance mapping

**Remaining:**
- [ ] Complete clause-by-clause reconciliation against published Part 9 FINAL (see `rag/reports/reconcile-part09-text.md`)
- [ ] Verify table/reference items from reconciliation crosswalk
- [ ] Add explicit cross-references to DASH-IF Identifier Registry for text-track `@schemeIdUri` values
- [ ] Add conformance mapping to Part 12

---

### Part 10 — Events (v0.4)

**Status:** Working Draft — general events model and timed metadata migrated.

**Done:**
- Scope, references, terms
- DASH events overview (MPD events, inband events, user-defined events)
- In-band MPD validity signalling (`urn:mpeg:dash:event:2012`)
- MPD events, DASH Callback events
- Timed metadata tracks (signalling, timing, ownership boundary with Part 9)
- Cross-references to Part 4 (MPD update timing) and Part 5 (SCTE-35, ad tracking)

**Remaining:**
- [ ] Add normative requirements for MPD Patch events (ISO/IEC 23009-1 Amendment 3)
- [ ] Define ownership boundary between Part 10 (timed metadata) and Part 11 (additional technologies)
- [ ] Add conformance mapping to Part 12
- [ ] Create `tools/validation/validate_part10_events_mpd.py`

---

### Part 11 — Additional Functionalities (v0.1)

**Status:** Working Draft — structural skeleton only; no substantive content yet.

**Done:**
- Scope, references, terms
- Issue placeholders for trick mode, thumbnail tracks, specific metadata tracks, registration process

**Remaining:**
- [ ] Migrate trick-mode requirements from v4.3 (clause 3.2.9 and live trick-mode)
- [ ] Migrate thumbnail track requirements from v4.3
- [ ] Define specific metadata track scope (coordinate with Part 10)
- [ ] Define registration and documentation process for additional technologies
- [ ] Add conformance mapping to Part 12

---

### Part 12 — Conformance and Reference Tools (v0.6)

**Status:** Working Draft — substantially complete for Part 12 scope.

**Done:**
- Scope, terms (DASH-IF Conformance Validator, dash.js, livesim2)
- Conformance interpretations (content authoring, client processing)
- Conformance and reference tools overview (validator, dash.js, livesim2, test assets)
- Initial conformance mappings for Parts 2, 3, 4, 5, 6, 7, 8, 9, 10
- Mermaid diagram of tool relationships

**Remaining:**
- [ ] Reconcile conformance mappings against actual DASH-IF Conformance Validator coverage
- [ ] Reconcile against dash.js sample coverage
- [ ] Reconcile against DASH-IF Test Assets Database
- [ ] Add conformance mapping for Part 11 (once Part 11 has normative content)
- [ ] Add conformance mapping for Part 1 (registries, document status)

---

## Infrastructure Status

### Publication Infrastructure

| Component | Status | Notes |
|-----------|--------|-------|
| `tools/publication/build_all.py` | ✅ Operational | Builds all 12 parts; copies images (`images/`, `Images/`, `figures/`, `Figures/`, `Diagrams/`, `diagrams/`, root-level PNGs) |
| `.github/workflows/preview-bikeshed.yml` | ✅ Operational | Builds preview on manual dispatch; deploys to GitHub Pages |
| `.github/workflows/publish-bikeshed.yml` | ✅ Operational | Official publication from `main` branch |
| Shared boilerplate (`specs/_boilerplate/`) | ✅ Operational | IPR notice, diagram style |
| Bikeshed metadata (all 12 `.bs` files) | ✅ Updated | `!Repository:`, `!Issue Tracking:`, `!Document Status:` |

### Tooling

| Tool | Status | Notes |
|------|--------|-------|
| `tools/update_bs_metadata.py` | ✅ Created | Bulk update of `.bs` metadata fields |
| `tools/fix_hanging_paragraphs.py` | ✅ Created | Detects and fixes hanging paragraphs |
| `tools/validation/validate_part2_core_cmaf_mpd.py` | ✅ Created | Part 2 MPD validation |
| `tools/validation/validate_part3_on_demand_mpd.py` | ✅ Created | Part 3 MPD validation |
| `tools/env/install_dashif_boilerplate.py` | ✅ Operational | Installs DASH-IF Bikeshed group boilerplate |

---

## Remaining Cross-Cutting Tasks

### High Priority

- [ ] **Identifier Registry cross-references**: Add explicit `[[DASHIF-IDENTIFIERS]]` cross-references in Parts 7, 8, 9, 10 for the specific `@schemeIdUri` values used in those parts (e.g. `AudioChannelConfiguration`, `Role`, `Accessibility`, `EventStream`)
- [ ] **Identifier registration workflow**: Replace the Google Forms submission workflow with a GitHub-based workflow (file issue at [Dash-Industry-Forum/Identifiers](https://github.com/Dash-Industry-Forum/Identifiers/issues))
- [ ] **Part 6 reconciliation**: Complete clause-by-clause reconciliation against published IOP v5.1.0 Part 6 (certificate acquisition URL, HDCP output control)
- [ ] **Part 5 figures**: Extract/redraw architecture figures from published Part 5 DOCX

### Medium Priority

- [ ] **Part 2 tables**: Reconstruct SegmentTemplate parameter table (Table 5) and segment-list computation formulae
- [ ] **Part 4 figures/tables**: Extract/redraw architecture figures and reconstruct configuration-parameter tables
- [ ] **Part 9 reconciliation**: Complete clause-by-clause reconciliation against published Part 9 FINAL
- [ ] **Part 11 content**: Migrate trick mode, thumbnail tracks, and metadata track content from v4.3
- [ ] **Conformance validator alignment**: Reconcile Part 12 conformance mappings against actual validator coverage

### Lower Priority

- [ ] **PDF publication path**: Evaluate DASH-IF specs builder container for Part 6 PDF output
- [ ] **Part 12 conformance mapping for Part 11**: Add once Part 11 has normative content
- [ ] **Metanorma evaluation**: Assess Metanorma as long-term PDF/DOC generation path
- [ ] **Codec registry verification**: Verify all `@codecs` strings in Parts 7, 8, 9 against current DASH-IF Codec Registry
- [ ] **Accessibility descriptors**: Add `Accessibility@schemeIdUri` requirements in Part 8 (audio description, sign language)

---

## Recent Changes (This Session)

1. **Part 1 (v0.3)**: Added DASH-IF Registries section (Identifier Registry, Codec Registry, ISO/IEC 23009-1 identifier types table, registration workflow). Added Contributing and Reviewing section (WD/WG/CR phases, PR workflow). Updated Document Status to v0.3.
2. **All 12 `.bs` files**: Replaced `Repository:` with `!Repository:` (custom HTML link), added `!Issue Tracking:` and `!Document Status:` custom metadata entries.
3. **Hanging paragraphs fixed**: Part 2 (Period Timing, Segment Information), Part 4 (Low-Latency intro), Part 5 (Use Cases, Architectures), Part 6 (license request model, client workflows, ECCP).
4. **`build_all.py`**: Added `Diagrams/` and `diagrams/` to image directory list; added root-level image file copying.