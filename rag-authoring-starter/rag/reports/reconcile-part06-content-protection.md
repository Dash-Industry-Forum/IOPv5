# Part 6 content-protection reconciliation crosswalk

Generated: 2026-07-15

This report maps the published DASH-IF IOP v5.1.0 Part 6 source against the
current Bikeshed source in `specs/part06-content-protection/`.

Source inputs:

- Published source: `rag/corpus/published/DASH-IF-IOPv5.1.0-Part6.pdf`
- Extracted text: `rag/corpus/published/DASH-IF-IOPv5.1.0-Part6.pdf.extracted.txt`
- Current Bikeshed source:
  - `specs/part06-content-protection/01-intro.inc.md`
  - `specs/part06-content-protection/06-content-protection.inc.md`
  - `specs/part06-content-protection/10-general.inc.md`
  - `specs/part06-content-protection/40-license-request-model.inc.md`
  - `specs/part06-content-protection/60-client-workflows.inc.md`
  - `specs/part06-content-protection/80-misc.inc.md`

## Summary

Part 6 is not a blank shell. The current Bikeshed source is substantial and
already contains most of the published document's major conceptual areas, but it
has been reorganized and extended. Therefore the correct migration action is
**clause-level reconciliation**, not wholesale replacement.

Key findings:

- Published clauses 4, 6, 7, 8, 10, and part of 9 have clear current-source
  counterparts.
- Published clause 5, "DASH-IF XML schema", appears partially represented by the
  newer license-request model and schema material, but needs explicit crosswalk.
- Published clause 11, "Enhanced Clear Key Content Protection (ECCP)", does not
  have an obvious top-level counterpart in current headings and should be treated
  as a high-priority missing/unknown item.
- Current Bikeshed source contains additional/newer material not obviously
  present in the published document, especially interoperable license request
  model, DRM client workflows, authorization-token handling, and periodic
  re-authorization. These may be useful forward-looking additions but must be
  clearly distinguished from published v5.1.0 content.

## Published heading structure

The extracted published Part 6 heading candidates are:

- 1 Scope
- 2 References
- 2.1 Normative references
- 2.2 Informative references
- 3 Definition of terms, symbols and abbreviations
- 3.1 Terms
- 3.2 Symbols
- 3.3 Abbreviations
- 4 Core concepts of content protection and security
- 4.1 Introduction
- 4.2 Client reference architecture for content playback
- 4.3 Compliances and robustness rules
- 4.4 W3C Encrypted Media Extensions
- 5 DASH-IF XML schema
- 5.1 Introduction
- 5.2 License acquisition URL
- 5.3 Authorization server URL
- 5.4 Certificate acquisition URL
- 6 Content protection constraints for CMAF
- 6.1 Introduction
- 6.2 Content protection data
- 6.3 Content protection data constraints
- 6.4 Content encryption
- 7 Content protection constraints for the MPD
- 7.1 Introduction
- 7.2 Signaling encrypted content
- 7.3 Signaling DRM system information
- 7.4 Signaling HDCP output control information
- 7.5 Using a content ID
- 8 Use of W3C Clear Key with DASH
- 9 Key rotation
- 9.1 Introduction
- 9.2 Manifest based key rotation signalling
- 9.3 In-band key rotation signalling
- 9.4 In-band key hierarchy
- 10 HTTPS and DASH
- 11 Enhanced Clear Key Content Protection (ECCP)
- 11.1 Background
- 11.2 Constraints on DASH content generation
- 11.3 Constraints on content protection
- 11.4 Constraints on transport
- 11.5 Constraints on access control
- 11.6 Client requirements
- 11.7 Examples

## Current Bikeshed heading structure

Current Part 6 source headings include:

### `01-intro.inc.md`

- Purpose
- Scope
- Interpretation
- Disclaimer

### `06-content-protection.inc.md`

- Migration Notes
- Open Issues and Work Items
- Change History

### `10-general.inc.md`

- Core concepts of content protection and security
- Client reference architecture for encrypted content playback
- Content encryption and DRM
- Robustness
- W3C Encrypted Media Extensions
- Content protection constraints for CMAF
- Content protection data in CMAF containers
- Encryption and DRM signaling in the MPD
- Signaling presence of encrypted content
- `default_KID` defines the scope of DRM system interactions
- `default_KID` in hierarchical/derived/variant key scenarios
- Providing default DRM system configuration
- Delivering updates to DRM system internal state

### `40-license-request-model.inc.md`

- DASH-IF interoperable license request model
- Proof of authorization
- Obtaining authorization tokens
- Issuing authorization tokens
- Embedding secrets in authorization tokens
- Attaching authorization tokens to license requests
- Problem signaling and handling
- Problem type: not authorized to access content
- Problem type: insufficient proof of authorization
- Possible deployment architectures
- Passing a content ID to services

### `60-client-workflows.inc.md`

- DRM workflows in DASH clients
- Capability detection
- Selecting the DRM system
- Activating the DRM system
- Handling unavailability of content keys
- Handling changes in required and available content keys
- Content protection policies
- Performing license requests
- Efficient license acquisition

### `80-misc.inc.md`

- Periodic re-authorization
- Controlling access rights with a key hierarchy
- Use of W3C Clear Key with DASH
- XML Schema for DASH-IF MPD extensions
- HTTPS and DASH

## Clause crosswalk

| Published clause | Published heading | Current Bikeshed location | Status | Action |
|---|---|---|---|---|
| 1 | Scope | `01-intro.inc.md` / `#what-is-in-this-document` | Present, reorganized | Compare published scope text against current scope; ensure exclusions/additions are intentional. |
| 2 | References | `.bs` bibliography and/or missing front-matter prose | Partial/unknown | Verify all published normative/informative references are represented in `.bs` metadata/bibliography. |
| 2.1 | Normative references | `.bs` bibliography | Partial/unknown | Cross-check published normative references against Bikeshed references. |
| 2.2 | Informative references | `.bs` bibliography | Partial/unknown | Cross-check published informative references against Bikeshed references. |
| 3 | Definition of terms, symbols and abbreviations | Not obvious in current include headings | Missing/unknown | Locate in `.bs` or add a terms/symbols/abbreviations section if absent. |
| 3.1 | Terms | Not obvious in current include headings | Missing/unknown | Verify whether terms are imported globally or need Part 6-specific definitions. |
| 3.2 | Symbols | Not obvious in current include headings | Missing/unknown | Verify whether published symbols are still required. |
| 3.3 | Abbreviations | Not obvious in current include headings | Missing/unknown | Verify whether abbreviations are represented locally or globally. |
| 4 | Core concepts of content protection and security | `10-general.inc.md` / `#security` | Present | Compare text and normative statements. |
| 4.1 | Introduction | `10-general.inc.md` / `#security`; possibly `01-intro.inc.md` | Present, reorganized | Confirm published introduction content is preserved or intentionally replaced. |
| 4.2 | Client reference architecture for content playback | `10-general.inc.md` / `#drm-client-components` | Present, renamed/reorganized | Compare component naming and architecture description. |
| 4.3 | Compliances and robustness rules | `10-general.inc.md` / `#CPS-robustness` | Present, renamed | Compare "compliance" and "robustness" requirements. |
| 4.4 | W3C Encrypted Media Extensions | `10-general.inc.md` / `#CPS-EME` | Present | Compare references and requirements. |
| 5 | DASH-IF XML schema | `80-misc.inc.md` / `#CPS-schema`; related model in `40-license-request-model.inc.md` | Partial/reorganized; reconciliation started | Current schema section now records the clause 5 reconciliation issue and explicitly lists `laurl`, `authzurl`, and a provisional `certurl` placeholder. |
| 5.1 | Introduction | `80-misc.inc.md` / `#CPS-schema` | Partial | Published introduction says clause 5 defines MPD elements for license acquisition and authorization servers; current source now includes a reconciliation note but still needs final normative wording. |
| 5.2 | License acquisition URL | `80-misc.inc.md` / `#CPS-schema`; Clear Key example in `#CPS-AdditionalConstraints-W3C`; related workflows in `40-license-request-model.inc.md` | Partial | Current source has `dashif:laurl` schema/example and a general description. Need final review of published `Laurl` casing, optional `@licenseType`, and examples. |
| 5.3 | Authorization server URL | `80-misc.inc.md` / `#CPS-schema`; authorization-token model in `40-license-request-model.inc.md` | Partial/reorganized | Current source has `dashif:authzurl` schema and a richer authorization-token model. Need explicit mapping to published `Authzurl` and optional `@authzType`. |
| 5.4 | Certificate acquisition URL | `80-misc.inc.md` / `#CPS-schema` | Reconciliation placeholder added | Current source now includes provisional `dashif:certurl` schema placeholder and explanatory text. Need final review against published `Certurl`, optional `@certType`, and certificate-before-license semantics. |
| 6 | Content protection constraints for CMAF | `10-general.inc.md` / `#CPS-cmaf` | Present | Compare all subclauses. |
| 6.1 | Introduction | `10-general.inc.md` / `#CPS-cmaf` | Present/reorganized | Compare text. |
| 6.2 | Content protection data | `10-general.inc.md` / `#CPS-cmaf-structure` | Present, renamed | Compare CENC/CMAF box/signaling constraints. |
| 6.3 | Content protection data constraints | `10-general.inc.md` / `#CPS-cmaf-structure` | Partial/unknown | Verify published constraints are all retained. |
| 6.4 | Content encryption | `10-general.inc.md` / `#CPS-encryption-and-drm`; `#CPS-cmaf` | Present/reorganized | Compare encryption requirements. |
| 7 | Content protection constraints for the MPD | `10-general.inc.md` / `#CPS-mpd` | Present, renamed | Compare all subclauses. |
| 7.1 | Introduction | `10-general.inc.md` / `#CPS-mpd` | Present/reorganized | Compare text. |
| 7.2 | Signaling encrypted content | `10-general.inc.md` / `#CPS-mpd-scheme` | Present, renamed | Compare `ContentProtection`/scheme semantics. |
| 7.3 | Signaling DRM system information | `10-general.inc.md` / `#CPS-mpd-drm-config`; `#CPS-mpd-moof-pssh` | Present/reorganized | Compare MPD vs in-band DRM configuration rules. |
| 7.4 | Signaling HDCP output control information | Unknown | Missing/unknown | Search for HDCP; add or mark intentional omission. |
| 7.5 | Using a content ID | `40-license-request-model.inc.md` / `#CPS-lr-model-contentid` | Present/reorganized | Compare published content-ID semantics. |
| 8 | Use of W3C Clear Key with DASH | `80-misc.inc.md` / `#CPS-AdditionalConstraints-W3C` | Present | Compare constraints and examples. |
| 9 | Key rotation | `10-general.inc.md` / `#CPS-default_KID-hierarchy`; `60-client-workflows.inc.md` key-change handling; `80-misc.inc.md` key hierarchy | Partial/reorganized | Needs dedicated comparison because current text splits key rotation across key hierarchy and client workflows. |
| 9.1 | Introduction | Multiple current locations | Partial/reorganized | Identify canonical current location. |
| 9.2 | Manifest based key rotation signalling | `10-general.inc.md`; maybe `60-client-workflows.inc.md` | Partial/unknown | Verify explicit manifest-based signaling text. |
| 9.3 | In-band key rotation signalling | `10-general.inc.md` / `#CPS-mpd-moof-pssh`; maybe client workflows | Partial/unknown | Verify explicit in-band signaling text. |
| 9.4 | In-band key hierarchy | `80-misc.inc.md` / `#CPS-KeyHierarchy`; `10-general.inc.md` / hierarchy section | Present/reorganized | Compare hierarchy semantics. |
| 10 | HTTPS and DASH | `80-misc.inc.md` / `#CPS-HTTPS` | Present | Compare published requirements. |
| 11 | Enhanced Clear Key Content Protection (ECCP) | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP` | Migrated; needs editorial review | Published clause 11 baseline migrated into a new include and wired into `part06-content-protection.bs`. Review cross-references and relation to newer license request model. |
| 11.1 | Background | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-background` | Migrated; adapted | Background migrated and adapted for Bikeshed source. |
| 11.2 | Constraints on DASH content generation | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-content-generation` | Migrated; adapted | Preserves CMAF/IOP packaging requirement with generic cross-references. |
| 11.3 | Constraints on content protection | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-content-protection` | Migrated; adapted | Preserves Clear Key requirement and note that ECCP is not separately signaled. |
| 11.4 | Constraints on transport | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-transport` | Migrated | Preserves HTTPS and TLS 1.2-or-higher requirements. |
| 11.5 | Constraints on access control | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-access-control` | Migrated | Preserves access-control requirements and token/client-certificate/proxy examples. |
| 11.6 | Client requirements | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-client-requirements` | Migrated | Preserves client requirements for Clear Key and HTTPS. |
| 11.7 | Examples | `90-enhanced-clear-key.inc.md` / `#CPS-ECCP-examples` | Migrated; adapted | Example shortened/adapted from published clause 11; review against final schema-casing decision. |

## Current-source additions not obviously in published Part 6

The current Bikeshed source includes several larger sections that do not map
directly to the published v5.1.0 heading list:

| Current section | File | Initial classification | Action |
|---|---|---|---|
| DASH-IF interoperable license request model | `40-license-request-model.inc.md` | New/reorganized material | Determine whether this supersedes published schema URL clauses or is post-v5.1.0 work. |
| Proof of authorization / authorization tokens | `40-license-request-model.inc.md` | New/reorganized material | Confirm intended status and provenance. |
| Problem signaling and handling | `40-license-request-model.inc.md` | New/reorganized material | Confirm whether related to published schema behavior or new feature work. |
| DRM workflows in DASH clients | `60-client-workflows.inc.md` | New/reorganized material | Decide whether normative, informative, or future-version content. |
| Capability detection / DRM selection / DRM activation | `60-client-workflows.inc.md` | New/reorganized material | Confirm source/provenance. |
| Periodic re-authorization | `80-misc.inc.md` | New/reorganized material | Determine whether published v5.1.0 contains equivalent text. |

These additions are not necessarily wrong. They should remain visible in the
crosswalk because they may represent valuable post-publication development, but
they must not obscure the obligation to preserve published v5.1.0 content.

## High-priority gaps to verify

Targeted source search was run against `specs/part06-content-protection/*.md`
for:

```text
ECCP|Enhanced Clear Key|certificate|Certificate|HDCP|output control|LAURL|ASURL|CURL|Clear Key
```

Result: **0 matches**.

This confirms that the high-priority published-clause gaps are not obviously
present in the current Markdown source under those terms. The Part 6 open-issues
table has been updated to record this verification result.

1. **ECCP / Enhanced Clear Key**
   - Published clause 11 is not visible in current top-level headings.
   - Search terms `ECCP`, `Enhanced Clear Key`, `clear key`, and `access control`
     did not produce matches in the current Markdown source.
   - Status: confirmed missing/unknown pending published-text migration decision.

2. **Certificate acquisition URL**
   - Published clause 5.4 has no obvious current heading.
   - Search terms `certificate`, `certificate acquisition`, and `CURL` did not
     produce matches in the current Markdown source.
   - Status: confirmed missing/unknown pending published-text migration decision.

3. **HDCP output control**
   - Published clause 7.4 has no obvious current heading.
   - Search terms `HDCP` and `output control` did not produce matches in the
     current Markdown source.
   - Status: confirmed missing/unknown pending published-text migration decision.

4. **License/authorization URL terminology**
   - Search terms `LAURL`, `ASURL`, and `CURL` did not produce matches in the
     current Markdown source.
   - Status: current license-request model may be conceptually related, but the
     published Part 6 schema terminology is not explicitly preserved.

5. **Terms/symbols/abbreviations**
   - Published clause 3 is not obvious in current include headings.
   - `part06-content-protection.bs` does not define a terms/symbols/abbreviations
     include; it only defines metadata, bibliography aliases, and content
     includes.
   - Status: local Part 6 terms/symbols/abbreviations are missing/unknown unless
     inherited from shared boilerplate.

6. **References**
   - Published clause 2 should map to `.bs` bibliography and references.
   - `part06-content-protection.bs` currently defines bibliography aliases for
     `DASH`, `CMAF`, `CENC`, `jws`, `jwe`, `MSPR-EncryptionModes`, and
     `HLS-LowLatency`.
   - Status: partial/unknown. A normative/informative reference cross-check
     against the published Part 6 v5.1.0 document is still required.

## Recommended first concrete Part 6 edits

Do not start by rewriting the whole part. Use small, auditable edits:

1. Add a Part 6 migration/open-issue item listing the high-priority gaps:
   - ECCP,
   - certificate acquisition URL,
   - HDCP output control,
   - terms/symbols/abbreviations,
   - reference cross-check.

   Status: completed. `06-content-protection.inc.md` now includes open-issue rows
   for published v5.1.0 reconciliation, published-clause gap verification, and
   references/terminology mapping.

2. If searches confirm absence, add placeholder subsections or open issue rows
   rather than immediately inserting large migrated text.

3. Reconcile clause 5 first because it is structurally important and appears
   partially superseded/reorganized by the newer license-request model.

   Status: substantially advanced. `80-misc.inc.md` now includes a clause 5
   reconciliation note, explicit `laurl`, `authzurl`, and `certurl`
   explanations, a shared typed URL schema type with optional `@licenseType`,
   `@authzType`, and `@certType` attributes, and an example showing certificate,
   authorization, and license URLs under `ContentProtection`. Remaining work is
   to resolve canonical element-name casing (`Laurl`/`Authzurl`/`Certurl` in the
   published prose versus lowercase `dashif:laurl`/`dashif:authzurl`/
   `dashif:certurl` in current examples and schema) before marking the text as
   fully reconciled.

4. Reconcile clause 11 second because it appears most likely missing.

   Status: migrated. Published clause 11 ECCP content has been added as
   `90-enhanced-clear-key.inc.md` and included from `part06-content-protection.bs`.
   The migrated text preserves the ECCP baseline requirements and examples in
   Bikeshed form. Remaining work is editorial review of cross-references, schema
   element casing in examples, and interaction with the newer license request
   model.

5. Reconcile clause 7.4 and 5.4 third because they are narrow targeted items.

6. Finally, compare the already-present major sections:
   - clause 4 core concepts,
   - clause 6 CMAF constraints,
   - clause 7 MPD constraints,
   - clause 8 Clear Key,
   - clause 9 key rotation,
   - clause 10 HTTPS.

## Proposed status after crosswalk

Recommended status label for Part 6:

```text
Draft/reconciliation
```

Recommended README/backlog wording:

```text
Substantive Bikeshed source exists. Clause-level reconciliation against
published v5.1.0 is in progress; high-priority verification items are ECCP,
certificate acquisition URL, HDCP output control, terms/symbols/abbreviations,
and reference mapping.
```

## Validation checklist for the next Part 6 implementation pass

- [x] Search current source for ECCP / Enhanced Clear Key.
- [x] Search current source for certificate acquisition URL.
- [x] Search current source for HDCP output control.
- [x] Read `part06-content-protection.bs` for references/metadata mapping.
- [x] Update open-issues table with confirmed missing/unknown published clauses.
- [x] If adding headings, ensure anchors are stable and non-conflicting.
  - No new headings/anchors were added during the initial clause 5 source edit;
    existing `#CPS-schema` was reused.
- [ ] Run `python tools/publication/check_links.py`.
- [ ] Build Part 6 or all specs after source edits.
