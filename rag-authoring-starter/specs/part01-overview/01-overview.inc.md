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

The following normative references apply to this document set:
[[!MPEGDASH]], [[!ISOBMFF]], [[!MPEGCMAF]], [[!RFC9110]], [[!RFC9111]],
[[!RFC9112]], [[!RFC6265]], [[!RFC8446]].
