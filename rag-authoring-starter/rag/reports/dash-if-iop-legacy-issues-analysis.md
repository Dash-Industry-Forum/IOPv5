# DASH-IF-IOP Legacy Issues Analysis for IOP v5

**Date:** 2026-07-28  
**Source:** https://github.com/Dash-Industry-Forum/DASH-IF-IOP/issues (open issues)  
**Purpose:** Review legacy open issues and determine disposition for IOP v5.

---

## Summary

| Category | Count |
|----------|-------|
| ✅ Addressed in IOP v5 — can close with pointer | 18 |
| 🔄 Partially addressed — migrate as open issue to IOPv5 | 20 |
| 📋 Not yet addressed — migrate as new issue to IOPv5 | 38 |
| 🗑️ Stale / meta / out of scope — close | 7 |
| **Total** | **83** |

---

## ✅ Addressed in IOP v5 — Close with pointer to IOP v5

These issues are resolved by content already in the IOP v5 workspace.

| # | Title | IOP v5 resolution |
|---|-------|-------------------|
| #392 | CMAF fragment mapped to DASH segment or subsegment? | Part 2 §2.2 (Terminology Choices) explicitly resolves this: CMAF segment = DASH segment/subsegment depending on addressing mode |
| #387 | Period connectivity - all representations required or only some allowed? | Part 2 §4.2 (Period Connectivity) defines the rules |
| #415 | Ambiguity on `urn:mpeg:dash:period-continuity:2015` | Part 2 §4.2.3 (Period Continuity) clarifies the signalling |
| #270 | Clarify guidelines for the case of missing segments | Part 2 §8 (Segment Loss Handling) with Period splitting and placeholder strategies |
| #261 | Define static MPDs as always available | Part 3 §3.2 (Common MPD Requirements): `MPD@type="static"` means all media is available |
| #232 | Is it correct that IOP v4.3 says to use SegmentTemplate for on-demand? | Part 3 (On-demand) and Part 2 §3.2 (Segment Information) clarify all three addressing modes |
| #300 | Uniform client workflow for multi-DRM scenarios | Part 6 §4 (DRM client workflows): full selection, activation, license request workflow |
| #338 | How to enable acquisition of content keys for periods not yet in MPD? | Part 6 §4.6 (Handling changes in required and available content keys) |
| #344 | Add support for the AV1 video codec | Part 7 (Video) includes AV1 codec profiles |
| #268 | Updates for E-AC-3 and AC-4 for v5 | Part 8 (Audio) covers E-AC-3 and AC-4 |
| #289 | WebVTT: yay or nay? | Part 9 (Text) includes WebVTT as a supported format |
| #342 | v4.3 3.2.13 subtitle @codecs misleading | Part 9 (Text) defines `@codecs` for text tracks |
| #264 | Fix Event Message example | Part 10 §3 (Update Signaling via In-Band Events) has corrected examples |
| #259 | What is the MPD in emsg with value=3 | Part 10 §3: `value=3` carries the updated MPD snapshot in the event's `mpd` field |
| #233 | emsg in file and mpd | Part 10 §2 (DASH Events Overview) and §3 (In-Band Events) |
| #239 | Update Conformance software location and source URLs | Part 12 §2 (Conformance and Reference Tools) has current URLs |
| #297 | Broken URL links in Table 3 | Part 12 has updated URLs for all tools |
| #430 | Editing workflow - Github | Part 1 §1.4 (Contributing and Reviewing) defines the full GitHub workflow |

---

## 🔄 Partially addressed — Migrate as open issue to IOPv5

These issues have related content in IOP v5 but are not fully resolved.

| # | Title | IOP v5 status | Suggested IOPv5 part |
|---|-------|---------------|---------------------|
| #443 | Add contentId and intendedTrackType to ContentProtection | Part 6 has content ID in license request model; `intendedTrackType` not yet addressed | Part 6 |
| #400 | Simplifying representation of multi-key encrypted video tracks | Part 6 §2 (Content encryption and DRM) covers `default_KID` per adaptation set | Part 6 |
| #384 | ContentProtection descriptor usage in conflict with CENC | Part 6 §2 covers `cenc:default_KID` and `pssh` usage | Part 6 |
| #395 | Handling of multiple AvailabilityTimeOffset | Part 4 (live services) covers `@availabilityTimeOffset` but multiple values not fully addressed | Part 4 |
| #389 | Representation@availabilityTimeOffset conflict with MPEG DASH 4th edition | Part 4 (live services) | Part 4 |
| #419 | Confusion around $Time$ value to use in SegmentTemplate | Part 2 §3.2.2 (Explicit Addressing) addresses this but could be clearer | Part 2 |
| #394 | AssetIdentifier extensions in v5 | Part 5 §4.2 (IF-2) and §4.4 (IF-4d) use AssetIdentifier | Part 5 |
| #215 | Separate purposes of AssetIdentifier and period continuity/connectivity | Part 2 §4.2 (Period Connectivity) and Part 5 (AssetIdentifier) | Part 2, Part 5 |
| #279 | Be prescriptive and specific in ad insertion chapter | Part 5 has substantial content but some areas still need normative text | Part 5 |
| #208 | Deployment guidelines for CMFC and CMF2 | Part 2 §2 (CMAF-to-DASH mapping) covers CMAF profiles | Part 2 |
| #290 | What is `@codecs` for metadata adaptation set? | Part 10 §4 (Timed Metadata Tracks) covers `@mimeType` but `@codecs` needs clarification | Part 10 |
| #283 | Subtitle adaptation set should not be restricted to role=subtitle | Part 9 (Text) covers role descriptors | Part 9 |
| #214 | Proposal for simplified IOP profile signaling in v5 | Part 1 §4 (DASH-IF Registries) covers profile URIs | Part 1 |
| #353 | MPD URL Resolution | Part 2 §6.4 (MPD and Segment Locations) covers BaseURL but URL resolution rules need more detail | Part 2 |
| #333 | Client requirement for multiple MPD Location elements | Part 2 §6.4 (Locations) mentions `MPD.Location` but client behaviour is not fully specified | Part 2 |
| #352 | Clause 5.1 Seamless Switching | Part 2 §4.2 (Period Connectivity) and §4.3 (Period Continuity) | Part 2 |
| #306 | Any reason we don't require the client to support multiple periods? | Part 2 §4 (CMAF-to-DASH Mappings) covers multi-Period | Part 2 |
| #216 | Does IOP specify handling of "video+audio -> video-only" transitions? | Part 2 §4.4 (Non-Equal Length Tracks) and §4.5 (Period Splitting) | Part 2 |
| #402 | Audio Section of v5 draft incorrectly pulled | Part 8 (Audio) has been migrated; verify against published v5.0.0 | Part 8 |
| #391 | Broaden the purpose | Part 1 §2 (Scope) | Part 1 |

---

## 📋 Not yet addressed — Migrate as new issue to IOPv5

These issues have no corresponding content in IOP v5 and should be filed as new issues.

### Part 2 — Core Principles and CMAF Mapping

| # | Title | Notes |
|---|-------|-------|
| #416 | `#t=xxx` conflict with period @start | Media fragment URI timing vs MPD Period start |
| #417 | ffmpeg timescale issue | Timescale constraints (Part 2 §9.1 covers 2^53 limit but not ffmpeg-specific) |
| #295 | Deprecate startsWithSAP | Should be deprecated in Part 2 (Forbidden Techniques) |
| #258 | "Extended Segment Information" proposal to deprecate | Part 2 Forbidden Techniques |
| #260 | Deprecate DASH Annex E byte-range addressing | Part 2 Forbidden Techniques |
| #235 | How to determine correct value for `subsegmentStartsWithSAP`? | Part 2 Segment Information |
| #357 | Adaptation Set Contents | Part 2 Representation Structures |
| #275 | What is a "version" in Content Selection? | Part 2 |
| #229 | Remove IOP section 3.3 | Part 2 (already removed in v5 restructuring) |
| #228 | Remove sections dealing with backward-compatibility | Part 2 |
| #206 | Exclude xlink references only from AdaptationSet? | Part 2 |

### Part 3 — On-Demand Services

| # | Title | Notes |
|---|-------|-------|
| #234 | "On-demand with live profile" section is too permissive | Part 3 needs clearer constraints |
| #288 | Encourage/discourage restarting a presentation on the same URL? | Part 3 |

### Part 4 — Live and Low-Latency Services

| # | Title | Notes |
|---|-------|-------|
| #442 | Seekable live sliding window | Time shift buffer and seek behaviour |
| #421 | How to interpret MPD@timeShiftBufferDepth | Part 4 live services |
| #371 | Dynamic MPD support by client | Part 4 client requirements |
| #340 | last-segment-number: Clarify where it can be placed | Part 4 |
| #345 | Discussion: lmsg (in-band last segment message) | Part 4 or Part 10 |
| #276 | What role does lmsg have in 2019 and onwards? | Part 4 or Part 10 |
| #225 | What does it mean to "not offer the last segment that is signaled in the MPD"? | Part 4 |
| #205 | Can we be smarter than 404s? | Part 4 error handling |
| #438 | Improved Broadcast Operation with Modern Media Players | Part 4 |

### Part 5 — Ad Insertion

| # | Title | Notes |
|---|-------|-------|
| #396 | IOP v4.3 typo for event @schemeIdUri | Part 5 or Part 10 |

### Part 6 — Content Protection

| # | Title | Notes |
|---|-------|-------|
| #422 | Test and Conformance for Protected Content | Part 6 + Part 12 |

### Part 7 — Video

| # | Title | Notes |
|---|-------|-------|
| #441 | VVC-related omissions and proposed edits | Part 7 (VVC codec not yet in Part 7) |
| #294 | Why does IOP UHD require square pixels? | Part 7 |
| #286 | Color Primaries, Transfer Characteristics, Matrix Coefficients signalling | Part 7 HDR/WCG |
| #285 | Separate HEVC 4K from HEVC HD requirements? | Part 7 |
| #284 | Visual glitches at representation switches | Part 7 + Part 2 |
| #274 | Get rid of @maxWidth and family | Part 7 |
| #227 | Annex D Signaling Dolby Vision Profiles and Levels | Part 7 |
| #212 | Default video Role is not 'main' | Part 7 |

### Part 8 — Audio

| # | Title | Notes |
|---|-------|-------|
| #293 | USAC chapter: profiles mime sub-parameter conflict | Part 8 |
| #292 | What defines Dolby TrueHD signaling | Part 8 |
| #280 | Audio codecs: what do the "addition formulas" mean? | Part 8 |
| #266 | Signalling AC-3. What should it be? | Part 8 |

### Part 9 — Text

| # | Title | Notes |
|---|-------|-------|
| #287 | 608/708 -> "strongly discouraged" to firm "SHALL NOT" | Part 9 |
| #390 | Correct 4.3 to reference 2010 version of SMPTE-TT for IMSC | Part 9 |

### Part 10 — Events

| # | Title | Notes |
|---|-------|-------|
| #264 | Fix Event Message example | Part 10 (already addressed but verify) |

### Part 11 — Additional Functionalities

| # | Title | Notes |
|---|-------|-------|
| #282 | Thumbnails feature uses backwards definition of "tile" | Part 11 (Thumbnail Tracks) |
| #281 | Only image tiles refer to "@contentType" | Part 11 |
| #277 | How exactly do I use `@maxPlayoutRate` with trick mode? | Part 11 (Trick Mode) |

### Part 12 — Conformance and Reference Tools

| # | Title | Notes |
|---|-------|-------|
| #429 | Conformance tool warning: no duration, but SegmentTimeline exists | Part 12 conformance mapping |
| #278 | Consider role of hypothetical reference implementations | Part 12 |

### Cross-cutting / Part 1

| # | Title | Notes |
|---|-------|-------|
| #307 | Core features vs Basic constraints | Part 1 Scope |
| #366 | 5. Interoperability requirements | Part 1 Scope |
| #348 | Formal Intro | Part 1 |
| #291 | Content selection chapter: optional vs mandatory conflict | Part 2 |
| #230 | Collect URL/HTTP topics into a single chapter | Part 2 |
| #406 | Content steering mechanism for DASH compatible with HLS RSS | New feature — Part 11 or new part |
| #440 | Reporting schema for CMCD v2 | New feature — Part 11 or new part |
| #393 | Create a JSON manifest format for DASH MPDs | Out of scope for IOP v5 (normative DASH only) |
| #385 | Media Capabilities data dictionary | Part 1 or Part 12 |
| #241 | Multistream Use cases for MPEG | Part 1 Architecture |

---

## 🗑️ Stale / meta / out of scope — Close

| # | Title | Reason |
|---|-------|--------|
| #423 | Topics for f2f Meeting in June 2024 | Meeting agenda — stale |
| #420 | f2f June 23 Agenda Topics and Discussion | Meeting agenda — stale |
| #436 | Disclaimers | Meta — handled by IPR boilerplate in IOP v5 |
| #426 | Metadata for documentation | Meta — handled by Bikeshed metadata in IOP v5 |
| #439 | Update patch with reference to MPEG specification | Specific patch — verify if applied |
| #296 | Comments on current iop document | General comments — stale |
| #207 | Conformance Software: Does DASH-IF need/allow HLS format? | Out of scope for IOP v5 |

---

## Recommended Actions

### Immediate (high value, easy)

1. **Close stale/meta issues** (#423, #420, #436, #426, #296, #207) with a comment pointing to IOP v5.
2. **Close addressed issues** (18 issues listed above) with a comment pointing to the specific IOP v5 part and section.
3. **File new IOPv5 issues** for the highest-priority unaddressed items:
   - `[Part 7]: Add VVC codec support` (#441)
   - `[Part 7]: HDR/WCG signalling — Color Primaries, Transfer Characteristics` (#286)
   - `[Part 7]: Dolby Vision signalling` (#227)
   - `[Part 8]: Dolby TrueHD signalling` (#292)
   - `[Part 8]: USAC profiles mime sub-parameter` (#293)
   - `[Part 4]: Seekable live sliding window` (#442)
   - `[Part 2]: Deprecate startsWithSAP` (#295)
   - `[Part 11]: Thumbnails tile definition` (#282)
   - `[Part 11]: Trick mode @maxPlayoutRate` (#277)

### Medium priority

4. **Migrate partially-addressed issues** to IOPv5 with `[Part N]:` prefix and assign to the appropriate per-part project.
5. **File IOPv5 issues** for the remaining unaddressed items grouped by part.

### Notes

- Issues #393 (JSON manifest) and #207 (HLS conformance) are out of scope for IOP v5 and should be closed.
- Issue #406 (Content steering) and #440 (CMCD v2) are new features that could go into Part 11 or a future part.
- Issues #229, #228 (remove backward-compatibility sections) are already resolved by the IOP v5 restructuring.