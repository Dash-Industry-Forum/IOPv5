<!--
  Part 6: Content Protection and Security.
  Imported from the standalone Guidelines-Security Bikeshed repository and
  normalized into the IOPv5 part structure.
-->

# Migration Notes # {#migration-notes}

This Part 6 draft is seeded from the DASH-IF `Guidelines-Security` repository,
which is treated as the migration source for the current content-protection text.
The immediate objective is to preserve the existing technical chapter structure
and published content while aligning metadata, publication paths, and part-level
editorial management with the IOP v5 multi-part publication.

The standalone repository currently uses the DASH-IF specs builder container for
HTML publication and GitHub Pages deployment. Its publication workflow builds via
`make -f /tools/Makefile spec SRC=Guidelines-Security.bs.md NAME=Guidelines-Security`
in the shared DASH-IF container image. The published standalone site also exposes
an accompanying PDF output, indicating that PDF generation is likely provided by
that shared builder environment rather than a repository-local script alone. That
build path should be evaluated as an intermediate PDF option for Part 6 while
Metanorma remains under investigation as the preferred long-term PDF/DOC
generation path.


# Open Issues and Work Items # {#open-issues}


<table class="data">
  <caption>Part 6 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
        <tr><td>Source migration<td>In progress<td>Imported the current Guidelines-Security Bikeshed content and assets into the IOP Part 6 folder structure.
    <tr><td>Published v5.1.0 reconciliation<td>In progress<td>Use <code>rag/reports/reconcile-part06-content-protection.md</code> to reconcile this Bikeshed source clause-by-clause against the published Part 6 v5.1.0 document.
    <tr><td>Published-clause gap verification<td>Open<td>Targeted source search did not find ECCP / Enhanced Clear Key, certificate acquisition URL, HDCP output control, LAURL, ASURL, or CURL terms in the current Markdown source. Verify against the published document and migrate or explicitly defer these clauses.
    <tr><td>References and terminology mapping<td>Open<td>Cross-check published clauses 2 and 3 (references, terms, symbols, and abbreviations) against the Part 6 Bikeshed metadata, bibliography, and shared terminology conventions.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology, references, and any duplicated guidance with Parts 1, 2, and 12.
        <tr><td>PDF publication path<td>In progress<td>The standalone Security workflow has been traced to the shared DASH-IF specs builder container; adapt that environment for Part 6 publication and confirm how the PDF artifact is emitted.

    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.

</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 6 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
        <tr><td>0.2<td>Imported<td>Imported the standalone Guidelines-Security Bikeshed chapters, bibliography, and image assets into the IOP v5 Part 6 structure.
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 6.

</table>
