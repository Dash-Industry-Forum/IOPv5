# DASH-IF IOP v5

This repository is used for DASH-IF IOP v5 issue tracking and document-authoring
experiments.

The active Bikeshed/RAG authoring work currently happens on the branch:

```text
tstockhammer-rag-workflow
```

The workflow files in this branch are intentionally bootstrapped onto `main` so
that GitHub shows them in the **Actions** tab. GitHub only lists manually runnable
workflows after the workflow files exist on the repository's default branch.

## GitHub Actions bootstrap

The following workflows are available once this README/workflow bootstrap is
merged to `main`:

```text
.github/workflows/build-pr.yml
.github/workflows/preview-bikeshed.yml
.github/workflows/publish-bikeshed.yml
```

### Preview workflow

Use this for publication-style review of a non-main authoring branch.

1. Go to **Actions**.
2. Select **Preview Bikeshed Specs**.
3. Click **Run workflow**.
4. In the branch selector, choose the branch to preview, for example:

   ```text
   tstockhammer-rag-workflow
   ```

5. Optionally set `preview_name`; if omitted, the branch name is used.
6. Keep `noindex` enabled.
7. Run the workflow.

Expected preview URL pattern:

```text
https://dash-industry-forum.github.io/IOPv5/previews/tstockhammer-rag-workflow/
```

or, for a custom preview name:

```text
https://dash-industry-forum.github.io/IOPv5/previews/<preview_name>/
```

A landing page is also generated at:

```text
https://dash-industry-forum.github.io/IOPv5/preview.html
```

Important notes:

- The preview is unadvertised and marked `noindex,nofollow`, but it is **not
  private**.
- GitHub Pages has one live deployment per repository. A preview deployment may
  temporarily replace the currently visible Pages deployment until the main
  publication workflow is run again.
- Do not use preview deployments for confidential drafts or access-controlled
  source material.

### Pull-request build workflow

`Build Pull Request` builds all specs for pull requests to `main` and uploads the
`dist` folder as a workflow artifact. It is mainly useful after the authoring
branch content is present in the PR.

### Publication workflow

`Publish Bikeshed Specs` is intended to publish the official GitHub Pages site
from `main` once the Bikeshed authoring content is merged. Until the
`rag-authoring-starter/` authoring tree is merged to `main`, this workflow is a
bootstrap placeholder and should not be expected to publish the full site from
`main`.

For preview or publication deployment to work, repository administrators need to
enable GitHub Pages with:

```text
Settings → Pages → Build and deployment → Source: GitHub Actions
```

If this is not enabled, the build job may succeed but the deploy job will fail
with a 404/error similar to "Failed to create deployment" or "Ensure GitHub Pages
has been enabled".


## Issue tracking

See Projects for document parts, titles, editors and assigned issues:

```text
https://github.com/Dash-Industry-Forum/IOPv5/projects
```

In issue titles, please indicate the part number in brackets, for example:

```text
[9] Subtitle profile migration
```

or assign the issue to the relevant project during creation.
