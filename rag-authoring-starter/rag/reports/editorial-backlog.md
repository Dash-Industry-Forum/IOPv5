# Editorial and migration backlog

This report captures repository-wide work items that should become GitHub issues.
The GitHub CLI is not available in the current local environment, so these are
provided as ready-to-copy issue seeds.

## Issue seeds

### [Repo] Improve cross-part references and stable anchors

**Problem:** The current parts refer to other parts mostly as prose ("Part 2",
"Part 12") rather than stable Bikeshed cross-references.

**Tasks:**

- Define anchor naming conventions for all parts.
- Add stable anchors for common clauses (scope, references, conformance, timing,
  service types, examples, open issues).
- Replace prose-only cross-part references with links where Bikeshed supports the
  reference cleanly.
- Avoid duplicate anchor names inside individual generated HTML documents.

**Notes:** This can be done after the first migration pass. Do not block content
migration on perfect cross-part references.

### [Repo] Add examples across all parts

**Problem:** Many requirements will be easier to review and validate with short
examples, but examples are currently sparse.

**Tasks:**

- For each part, identify at least one minimal MPD/media/signalling example.
- Add examples as diffable text where possible, not screenshots.
- Link examples to validator/reference-player expectations in Part 12.
- Keep examples small and focused; larger test vectors belong in test assets.

### [Repo] Improve diagram rendering and authoring conventions

**Problem:** Mermaid diagrams still vary in size, line breaking, and node label
formatting. Some diagrams remain too small or visually inconsistent.

**Tasks:**

- Re-check all diagrams after current CSS changes.
- Standardize Mermaid flowchart settings per orientation (LR/TB).
- Prefer native SVG labels (`htmlLabels:false`) to avoid clipping.
- Use explicit label wording that fits boxes naturally; avoid long function names
  in narrow nodes.
- Consider replacing complex Mermaid figures with PlantUML or draw.io SVG where
  Mermaid layout cannot produce readable output.

### [Repo] Convert newly uploaded Word/PDF sources part by part

**Problem:** Additional Word/PDF sources for other parts have been uploaded and
need gradual conversion.

**Tasks:**

- Update `rag/sources.yaml` for any new inputs.
- Run inventory/extract/chunk/index tools.
- Create per-part migration reports identifying source chunks and deltas.
- Convert one part at a time to `.bs` + `.inc.md` source.
- Preserve access policy: do not commit unpublished or proprietary binaries.

### [Part 11] Draft Additional Technologies

**Problem:** Part 11 has not yet been substantively started.

**Initial scope:**

- Move v4.3 clause 3.2.9 trick mode to Part 11.
- Move thumbnail tracks from v4.3 to Part 11.
- Define specific metadata tracks, coordinating with Part 10 where metadata is
  event-like or timed.
- Define a registration and documentation process for additional DASH-IF
  technologies.

**Tasks:**

- Ground trick-mode text from v4.3 and any uploaded Part 11 sources.
- Identify thumbnail-track source clauses and examples.
- Decide Part 10 vs Part 11 ownership for metadata tracks.
- Draft a registration template covering signalling scheme, content examples,
  validator checks, reference-player behaviour, and public documentation.

### [Repo] Modal keyword presentation

**Problem:** Modal keywords should be readable without making the document heavy.

**Decision to trial:** Use the shared CSS class `.modal-keyword` for selected
introductory/explanatory uses of `shall`, `should`, and `may`, especially in
keyword interpretation lists. Do not aggressively wrap every occurrence in dense
normative prose.

**Tasks:**

- Apply the style in conformance/modal-verb clauses first.
- Review visual output in generated HTML.
- Decide whether to add a small helper script for controlled wrapping in selected
  clauses only.

### [Metanorma] Continue Part 12 proof of concept

**Problem:** Part 12 AsciiDoc generation has started, but the installed
Metanorma Generic renderer on Windows currently produces XML/presentation XML and
then fails during HTML/DOC rendering due to local package/runtime issues.

**Tasks:**

- Keep Bikeshed Markdown canonical.
- Finish the generated AsciiDoc cleanup for Part 12.
- Test Metanorma Generic in CI/Linux or a full Ruby/gem environment.
- Test ISO flavour for PDF generation if Generic remains HTML/DOC only.
- Compare output fidelity against Bikeshed HTML.
