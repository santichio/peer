# Contributing

This repository standardizes AI-related documents — skills, prompts, agents,
templates, and references. Read the [README](README.md) for the document standard
before contributing.

## Adding or changing a document

> **Creating a skill?** Skills don't use the base template or the generic steps below.
> Use the [`skill-creator`](skills/skill-creator/SKILL.md) skill — it produces a
> `skills/<name>/SKILL.md` (folder per skill, `name`/`description` frontmatter, no
> version/status). Then add it to `INDEX.md` and `skills/CHANGELOG.md` (by date).

> **Adding a script?** Scripts bundled inside a skill (e.g.
> `skills/ralph/ralph.sh`) are executables, not Markdown documents. Put metadata in
> a header comment (`id`, `description`, `version` SemVer, `owner`). They're tracked
> as part of the owning skill — no separate INDEX or changelog entry.

1. Copy [`templates/base-document.md`](templates/base-document.md) into the right
   `references/<topic>/` folder (e.g. `references/engineering/`). Create the topic
   subfolder if it doesn't exist. Most new artifacts now belong inside an existing
   skill — only top-level engineering references use this flow.
2. Rename it to `<id>.md` — kebab-case, matching the `id` in the frontmatter.
3. Fill in all required metadata (see the [metadata reference](README.md#metadata-reference)).
4. Write the body in GitHub-flavored Markdown; use [Mermaid](https://mermaid.js.org/)
   for any diagrams. Remove optional sections you don't need.
5. Register the document in [`INDEX.md`](INDEX.md) under its category.
6. Add an entry to the directory's `CHANGELOG.md`
   (see [Changelogs](README.md#changelogs)). Do **not** add a per-document changelog
   section.
7. When changing an existing document, bump its `version` (SemVer) and `updated` date,
   and add a matching `CHANGELOG.md` entry.

## Git workflow

This repo follows the organization's git policy:

- **Branching** — [`git-branching-strategy`](skills/gitflow/references/git-branching-strategy.md).
  Branch from `develop`; name as `feature/<issue_id>-<name>` (or `hotfix/…`).
  The [branch-name-helper](skills/gitflow/prompts/branch-name-helper.md) prompt can generate names.
- **Commits** — [`git-commit-conventions`](skills/gitflow/references/git-commit-conventions.md).
  Conventional Commits, header ≤ 50 characters, atomic commits. The
  [commit-message-writer](skills/gitflow/prompts/commit-message-writer.md) prompt can draft messages.
- **Pull requests & review** — [`git-code-review`](skills/gitflow/references/git-code-review.md).
  Open a Draft PR early, fill in the PR template, and get at least one approval. Self-
  approval is not permitted. `CODEOWNERS` routes reviews to the repository owner.
- **Versioning & releases** — [`git-versioning-releases`](skills/gitflow/references/git-versioning-releases.md).

## Conventions

- GitHub-flavored Markdown; Mermaid for all diagrams.
- `id` and filenames in kebab-case; `id` matches the filename stem.
- ISO dates (`YYYY-MM-DD`).
