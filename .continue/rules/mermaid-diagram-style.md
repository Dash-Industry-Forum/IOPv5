---
globs: rag-authoring-starter/specs/**/*.inc.md
alwaysApply: false
---

Diagrams and figure/table captions in Bikeshed .inc.md:

1. FIGURE CAPTIONS: Do NOT hardcode "Figure 1:" / "Figure N:" in a <figcaption> — Bikeshed auto-numbers figures. Write only the caption text, e.g. <figcaption>DASH-based distribution architecture.</figcaption>.

2. DATA TABLES ARE NOT FIGURES: Never wrap a data table (abbreviations, references, change history, etc.) in <figure>/<figcaption> — that makes it an auto-numbered "Figure". Use a plain table with a caption: <table class="data"><caption>Title.</caption><thead>...</table>. Reserve <figure> for actual diagrams/images.

3. MERMAID FLOWCHARTS: Wrap in <figure class="diagram"> and begin <pre class=mermaid> with an init directive. Use native SVG labels (`htmlLabels:false`) rather than HTML/foreignObject labels; the HTML-label path clips/truncates text in Bikeshed output. Use straight edges (`curve:'linear'`), neutral theme, readable font, and automatic SVG sizing. Flowchart example:
`%%{init: {'theme':'neutral','themeVariables':{'fontSize':'18px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':55,'rankSpacing':80,'padding':14,'htmlLabels':false,'useMaxWidth':true}}}%%`
Add `classDef box fill:#eef3f8,stroke:#33475b,stroke-width:1.4px,color:#1a2733;` and apply to all nodes.

4. AVOID TEXT CUT-OFF: prefer plain quoted labels and `htmlLabels:false`; do not use `<br/>`-based HTML labels in flowcharts unless the output is visually checked, because they can clip text at the node edge. Quote labels with special chars, e.g. PKG["ISO BMFF / CMAF Packager (Encryption)"]. Do NOT use HTML entities like &nbsp; inside mermaid source (they get mangled) — use a plain space.

5. Each spec's .bs must include _shared-diagram-style.inc.md (staged by build.ps1/build_all.py) which overrides the shrink-to-content boilerplate CSS and styles table.data > caption.