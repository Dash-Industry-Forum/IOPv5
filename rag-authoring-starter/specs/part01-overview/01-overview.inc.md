<!--
  Part 1: Overview, Architecture and Interfaces.
  Migrated from DASH-IF IOP-1 v5.0.0 (2022-06) and updated for currency.
  Provenance: dashif-iop-v5-part1 (published PDF) chunks #5..#13.
  Editorial updates (outdated -> current):
    - HTTP/1.1 RFC 7230-7235 -> RFC 9110/9111/9112 (which obsolete them).
    - TLS RFC 5246 (TLS 1.2) -> RFC 8446 (TLS 1.3); TLS 1.2 retained as minimum.
    - ISO editions refreshed where a newer edition is in force.
    - Issue tracker URL points at the IOPv5 repository.
-->

# Scope # {#scope}

The present document provides an overview of the different features in the
DASH-IF Interoperability Guidelines (IOP). In particular, it provides a reference
architecture together with the relevant interfaces and functional blocks, and
describes how the multi-part IOP document set fits together.

Note: DASH-IF IOP v5 is published as a multi-part document set. The parts and
their summaries are described in [[#part-descriptions]].

# References # {#doc-references}

## Normative references ## {#normative-references}

References are either specific (identified by date of publication and/or edition
number or version number) or non-specific. For specific references, only the
cited version applies. For non-specific references, the latest version of the
referenced document (including any amendments) applies.

Note: While any hyperlinks included in this clause were valid at the time of
publication, DASH-IF cannot guarantee their long-term validity.

The following referenced documents are necessary for the application of the
present document:

- ISO/IEC 23009-1, *Dynamic adaptive streaming over HTTP (DASH) — Part 1: Media
    presentation description and segment formats* [[!MPEGDASH]] (latest edition
    applies).
- ISO/IEC 14496-12, *Coding of audio-visual objects — Part 12: ISO base media
    file format* [[!ISOBMFF]]. The 8th edition (ISO/IEC FDIS 14496-12:2024) is the
    current edition; the latest edition applies.
- ISO/IEC 23000-19, *Common media application format (CMAF) for segmented media*
    [[!MPEGCMAF]].
- DASH-IF IOP v5, Part 12, *Conformance and reference tools*.
- DASH-IF IOP v5, Part 2, *Core principles and CMAF mapping*.
- DASH-IF IOP v5, Part 6, *Content protection*.
- IETF RFC 9110, *HTTP Semantics*.
- IETF RFC 9111, *HTTP Caching*.
- IETF RFC 9112, *HTTP/1.1*.
- IETF RFC 6265, *HTTP State Management Mechanism*.
- IETF RFC 8446, *The Transport Layer Security (TLS) Protocol, Version 1.3*.

Note: This clause replaces the following references from earlier editions, which
have since been obsoleted: the HTTP/1.1 series RFC 7230–7235 (obsoleted by
RFC 9110/9111/9112) and RFC 5246 (TLS 1.2, obsoleted by RFC 8446 / TLS 1.3).
TLS 1.2 remains acceptable as a minimum where TLS 1.3 is not available.

## Informative references ## {#informative-references}

The following referenced documents are not necessary for the application of the
present document but assist the user with regard to a particular subject area:

- CTA-5003-C, *Web Application Video Ecosystem (WAVE) — Device Playback
    Capabilities* (revision C).
- DASH-IF, *Content Protection Information Exchange (CPIX)*.
- DASH-IF Guidelines for Implementation: *DASH-IF Interoperability Point for
    ATSC 3.0*.
- DASH-IF Identifier Registry [[DASHIF-IDENTIFIERS]].
- DASH-IF Codec Registry [[DASHIF-CODECS]].

# Terms, Definitions, Symbols and Abbreviations # {#terms}

## Terms and Definitions ## {#terms-definitions}

For the purposes of the present document, the terms and definitions given in
ISO/IEC 23009-1 [[!MPEGDASH]] and the other referenced parts of DASH-IF IOP v5
apply.

## Symbols ## {#symbols}

For the purposes of the present document, the symbols defined in the individual
parts apply where used.

## Abbreviations ## {#abbreviations}

For the purposes of the present document, the following abbreviations apply:

<table class="data">
  <caption>Abbreviations used in DASH-IF IOP v5.</caption>
  <thead>
    <tr><th>Abbreviation<th>Meaning
  <tbody>
    <tr><td>BMFF<td>Base Media File Format
    <tr><td>CMAF<td>Common Media Application Format
    <tr><td>DASH<td>Dynamic Adaptive Streaming over HTTP
    <tr><td>DRM<td>Digital Rights Management
    <tr><td>HTTP<td>HyperText Transfer Protocol
    <tr><td>IOP<td>InterOperability Point
    <tr><td>ISO<td>International Organization for Standardization
    <tr><td>MPD<td>Media Presentation Description
    <tr><td>MPEG<td>Moving Picture Experts Group
    <tr><td>RFC<td>Request for Comments
    <tr><td>TLS<td>Transport Layer Security
    <tr><td>URL<td>Uniform Resource Locator
    <tr><td>XML<td>Extensible Markup Language
</table>

# Conformance and Style # {#conformance-style}

For detailed guidance on conformance and additional interpretation of the
conformance key words (such as "<span class=modal-keyword>shall</span>"), see DASH-IF IOP v5 Part 12,
*Conformance and reference tools*.

The key words *<span class=modal-keyword>shall</span>*, *<span class=modal-keyword><span class=modal-keyword>shall</span> not</span>*, *<span class=modal-keyword>should</span>*, *<span class=modal-keyword><span class=modal-keyword>should</span> not</span>*, *<span class=modal-keyword>may</span>*, *need not*,
*will*, *will not*, *can*, and *cannot* are to be interpreted as described in the
ETSI Drafting Rules. The words *must* and *must not* are not used to express
normative requirements.

The following naming conventions apply in this document set:

- **Elements** in an XML document are identified by an upper-case first letter
    and in bold face, as `Element`. To express that an element `Element1` is
    contained in another element `Element2`, the notation `Element2.Element1` is
    used. Combined-word names use camel casing, e.g. `ImportantElement`.
- **Attributes** in an XML document are identified by a lower-case first letter
    and preceded by an `@` sign, e.g. `@attribute`. To reference an attribute of a
    specific element, the notation `Element@attribute` is used.
- **List** values, XML data types, and conditions follow the conventions of
    ISO/IEC 23009-1 [[!MPEGDASH]].

# Annex A: Document Status # {#document-status}

## Living Document ## {#living-document}

This document is published as a **Living Document** (LD). A Living Document is
continuously updated as new content is added, issues are resolved, and the
technical community provides feedback. It does not represent a final, approved
specification.

The current status of each part is indicated by its version number in the Change
History table:

- **Working Draft (0.x)**: Content is being drafted and reviewed by the DASH-IF
    Technical Working Group. The document is open for community feedback but has
    not yet been formally approved.
- **WG Review (0.8.x-wgr)**: The Working Group has completed its internal review
    and the document is open for broader community review.
- **Community Review (0.9.x-pr)**: The document is open for public comment before
    final approval (public review).
- **Approved (1.x)**: The document has been formally approved by DASH-IF and
    represents a stable, normative specification. Only approved versions use
    version numbers 1.0 and above.


## Document Workflow ## {#document-workflow}

The DASH-IF IOP v5 document set follows this publication workflow:

1. **Working Draft**: Editors draft content in the `main` development branch.
    Issues and pull requests are tracked at
    [https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).
    Use the label or title prefix `[Part N]` (e.g. `[Part 2]`) to associate an
    issue with a specific part.
2. **WG Review**: The Working Group reviews the draft and resolves open issues.
    A release candidate is tagged on the `main` branch.
3. **Community Review**: The release candidate is published for public comment.
    A `stable` branch is created to maintain the approved version independently
    of ongoing development.
4. **Approved**: After community review, the document is formally approved and
    published as a stable release. The `stable` branch is updated; the `main`
    branch continues development of the next version.

## Stable and Development Versions ## {#stable-dev-branches}

DASH-IF IOP v5 uses a **two-branch model** to allow simultaneous maintenance of
a stable approved version and ongoing development of the next version:

- **`main` branch** — the development branch. All Working Draft content is
    authored here. The preview publication at
    [https://dashif.org/IOPv5/previews/](https://dashif.org/IOPv5/previews/)
    is built from `main`. Version numbers are `0.x` (Working Draft).
- **`stable` branch** — the approved/stable branch. When a version is formally
    approved, it is tagged (e.g. `v1.0`) and the `stable` branch is updated to
    that tag. The official publication at
    [https://dashif.org/Guidelines/iop-v5/](https://dashif.org/Guidelines/iop-v5/)
    is built from `stable`. Version numbers are `1.x` or higher.

**Typical workflow for a new version:**

1. Development continues on `main` (Working Draft, version `0.x`).
2. When ready for WG Review, a release candidate is tagged on `main`
    (e.g. `v1.0-rc1`).
3. After WG and Community Review, the approved version is tagged (e.g. `v1.0`)
    and the `stable` branch is fast-forwarded to that tag.
4. The official publication is updated from `stable`.
5. Development of the next version (`0.x` → `2.0-wip`) continues on `main`.

**Working on a new major version while maintaining a stable one:**

If a new major version (e.g. v2) needs to be developed while v1 remains stable:

1. Create a `v2-dev` branch from `main` for the new major version.
2. The `stable` branch continues to track the approved v1 content.
3. When v2 is approved, `stable` is updated to the v2 tag.

This model ensures that the official publication always reflects the latest
approved content, while editors can freely develop the next version without
affecting the stable publication.

## Issue Reporting ## {#issue-reporting}

All issues, bugs, and feature requests for DASH-IF IOP v5 <span class=modal-keyword>shall</span> be submitted
through the single DASH-IF IOPv5 issue tracker at
[https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).

To associate an issue with a specific part, use one of the following conventions:

- **Label**: Apply the GitHub label `Part 1`, `Part 2`, etc. to the issue.
- **Title prefix**: Begin the issue title with `[Part N]:`, for example
    `[Part 2]: Clarify @timescale requirement for SegmentTemplate`.

## Contributing and Reviewing ## {#contributing}

### General ### {#contributing-general}

DASH-IF IOP v5 is developed openly on GitHub. Contributions and reviews are
welcome at all stages of the publication workflow. The primary mechanisms are
GitHub issues (for feedback and discussion) and pull requests (for editorial
contributions).

### During the Working Draft Phase ### {#contributing-wd}

While a part is at Working Draft status:

- **File an issue** at
    [https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues)
    to report errors, raise technical questions, or propose new content. Use the
    title prefix `[Part N]:` to identify the relevant part.
- **Assign the issue** to the appropriate per-part GitHub Project under the
    [Dash-Industry-Forum organization](https://github.com/orgs/Dash-Industry-Forum/projects)
    (e.g. `Part 2: Core Principles and CMAF Mapping`). Each part has a dedicated
    project for tracking its open issues and work items.
- **Submit a pull request** against the `main` branch to propose editorial
    corrections, add missing content, or improve existing text. Pull requests
    <span class=modal-keyword>should</span> reference the issue they address.
- **Discuss** open issues in the GitHub issue tracker. The DASH-IF Technical
    Working Group reviews issues and pull requests on a regular basis.

### During WG Review ### {#contributing-wg-review}

When a part reaches WG Review status (release candidate tagged on `main`):

- **WG members** review the release candidate and file issues or pull requests
    for any remaining technical or editorial concerns.
- **Substantive changes** require a new release candidate; editorial corrections
    <span class=modal-keyword>may</span> be applied directly.
- The WG chair coordinates the review schedule and announces the review period
    via the DASH-IF mailing list and GitHub.

### During Community Review ### {#contributing-community-review}

When a part reaches Community Review status:

- **Anyone** <span class=modal-keyword>may</span> submit feedback by filing a GitHub issue at
    [https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).
    Use the label `Community Review` or the title prefix `[CR]:` to identify
    community review comments.
- **Pull requests** for editorial corrections are also welcome during this phase.
- The review period is announced on the DASH-IF website and mailing list. At the
    end of the review period, the WG resolves all open issues and, if no
    substantive changes are required, approves the document.

### How to Submit a Pull Request ### {#contributing-pr}

1. **Fork** the IOPv5 repository at
    [https://github.com/Dash-Industry-Forum/IOPv5](https://github.com/Dash-Industry-Forum/IOPv5).
2. **Create a branch** from `main` with a descriptive name (e.g.
    `fix-part2-timescale-clarification`).
3. **Make your changes** to the relevant `.inc.md` or `.bs` files in the
    `rag-authoring-starter/specs/` directory.
4. **Build locally** (optional but recommended) using
    `python tools/publication/build_all.py --out ../dist` to verify the changes
    compile without errors.
5. **Submit a pull request** against the `main` branch of the IOPv5 repository.
    Reference the issue(s) the PR addresses in the PR description.
6. **Assign the related issue(s)** to the appropriate per-part GitHub Project
    under the [Dash-Industry-Forum organization](https://github.com/orgs/Dash-Industry-Forum/projects).
7. The DASH-IF Technical Working Group reviews and merges approved pull requests.
