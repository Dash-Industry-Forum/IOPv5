## Summary

<!-- One-paragraph description of what this PR does and why. -->

## Parts affected

<!-- List the parts this PR touches, e.g.:
- Part 2 — Core Principles and CMAF Mapping
- Part 4 — Live and Low-Latency Services
-->

## Type of change

- [ ] Editorial (typo, formatting, cross-reference fix)
- [ ] Content migration (porting text from published source or v4.3)
- [ ] New content (new section, new requirement)
- [ ] Infrastructure (build scripts, CI, tooling)
- [ ] Metadata / `.bs` file update

## Related issues

<!-- Reference the GitHub issues this PR addresses, e.g.:
Closes #42
Addresses [Part 2] Complete SegmentTemplate parameter table
-->

## Source material

<!-- If migrating content, cite the source document and clause/chunk IDs, e.g.:
- DASH-IF IOP v5.0.0 Part 5 clause 5.7 (IF-5 MPD requirements)
- dashif-iop-v4-3#75..#80 (segment-list computation)
-->

## Checklist

### Content

- [ ] Content is accurate and consistent with ISO/IEC 23009-1 and ISO/IEC 23000-19
- [ ] Content does not conflict with existing IOP v5 text in other parts
- [ ] Source provenance is noted in comments or `Issue:` notes where applicable
- [ ] Modal keywords (`shall`, `should`, `may`) are wrapped in `<span class=modal-keyword>` tags
- [ ] No hanging paragraphs (text between a section heading and its first subsection)
- [ ] New sections have stable Bikeshed anchors (`{#anchor-id}`)
- [ ] Cross-references to other parts use plain-text section references (not `[[#anchor]]` across documents)

### Identifiers and registries

- [ ] `@schemeIdUri` values reference the [DASH-IF Identifier Registry](https://dashif.org/identifiers/introduction/)
- [ ] `@codecs` strings reference the [DASH-IF Codec Registry](https://dashif.org/codecs/introduction/)
- [ ] New identifiers or codecs are registered or have a registration issue filed

### Build

- [ ] Bikeshed builds without errors (`python tools/publication/build_all.py --out ../dist`)
- [ ] Images are present in the correct directory (`images/`, `Images/`, or `Diagrams/`)
- [ ] No broken local links (`python tools/publication/check_links.py`)

### Review

- [ ] PR title uses `[Part N]:` prefix if applicable (e.g. `[Part 2]: Add SegmentTemplate table`)
- [ ] Related GitHub issue(s) are assigned to the appropriate **per-part GitHub Project** (e.g. `Part 2: Core Principles and CMAF Mapping`) under the [Dash-Industry-Forum organization](https://github.com/orgs/Dash-Industry-Forum/projects)

## Preview

<!-- After the PR CI build completes, the built HTML is available as a workflow
artifact. For a full publication-style preview, ask a maintainer to run the
preview-bikeshed workflow on this branch. The preview URL will be:
https://dashif.org/IOPv5/previews/<branch-name>/
-->