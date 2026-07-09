---
globs: rag-authoring-starter/specs/**/*.inc.md
alwaysApply: false
---

For every Mermaid diagram in a Bikeshed .inc.md, wrap it in `<figure class="diagram">` and start the `<pre class=mermaid>` block with this init directive so engineering diagrams render cleanly (straight orthogonal edges, readable fonts, natural size — never the default curvy tiny look):

For flowcharts:
`%%{init: {'theme':'neutral','themeVariables':{'fontSize':'16px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':55,'rankSpacing':70,'padding':12,'htmlLabels':true,'useMaxWidth':false}}}%%`

For sequence diagrams use the `'sequence'` config with `'useMaxWidth':false` and larger `messageFontSize`/`actorFontSize`.

Add a `classDef box fill:#eef3f8,stroke:#33475b,stroke-width:1.4px,color:#1a2733;` and apply it to nodes for a consistent boxed look. Number figures ("Figure N: ...") in the figcaption. Each spec's .bs must include `_shared-diagram-style.inc.md` (staged by build.ps1/build_all.py) so the shrink-to-content boilerplate CSS is overridden.