# peer

**peer** is the single, standardized home for all AI-related documents — skills,
prompts, agents, templates, and reference material. The goal is consistency: every
document follows one shared structure, carries versioned metadata, and records its
own history in a changelog. That makes the collection easy to browse, reuse, and
trust.

## Purpose

- **Centralize** AI matters documents that would otherwise be scattered.
- **Standardize** their structure so any document is predictable to read and edit.
- **Version** every document with [Semantic Versioning](https://semver.org/) and a
  changelog, so changes are traceable.

## Repository structure

Most documents are organized as `<category>/<topic>/<id>.md`. Each **category** is a
top-level folder; within it, documents are grouped into **topic** subfolders (e.g.
`references/git/`). The per-directory `CHANGELOG.md` lives at the category root and
covers all of that category's topics.

**Skills are the exception** (see [Document standard](#document-standard)): each skill is
a self-contained folder `skills/<name>/SKILL.md` (no topic subfolder), following the
[SKILL.md format](skills/skill-creator/SKILL.md).

| Path                       | Holds                                                            |
| -------------------------- | --------------------------------------------------------------- |
| `templates/`               | Document templates, including the canonical base template.      |
| `skills/<name>/SKILL.md`   | Skills (SKILL.md format) + optional bundled `scripts/ references/ assets/`. |
| `prompts/<topic>/`         | Standalone prompts and prompt templates.                        |
| `agents/<topic>/`          | Agent definitions and configurations.                           |
| `references/<topic>/`      | Lists, catalogs, and preferences.                               |
| `scripts/<topic>/`         | Executable helper scripts (bash, python, etc.) — not Markdown docs. |
| `INDEX.md`                 | Hand-maintained catalog of every document.                      |
| `CONTRIBUTING.md`          | How to add documents and follow the git workflow.               |
| `CHANGELOG.md`             | Repo-level history; each category also has its own.             |
| `.github/`                 | PR template, `CODEOWNERS`, reusable workflows, and CI helper scripts. |
| `.github/workflows/`       | Reusable GitHub Actions (`sync-skills`, `lint-skills`).         |
| `templates/base-document.md` | The template all **non-skill** documents copy from.           |

```mermaid
flowchart TD
    root["repo root"]
    root --> readme["README.md"]
    root --> index["INDEX.md"]
    root --> contributing["CONTRIBUTING.md"]
    root --> changelog["CHANGELOG.md"]
    root --> github[".github/"]
    root --> templates["templates/"]
    root --> skills["skills/"]
    skills --> scl["CHANGELOG.md"]
    skills --> sc["skill-creator/SKILL.md"]
    skills --> sgf["gitflow/SKILL.md"]
    skills --> sprd["prd/SKILL.md"]
    skills --> sralph["ralph/SKILL.md"]
    root --> prompts["prompts/"]
    root --> agents["agents/"]
    root --> references["references/"]
    root --> scripts["scripts/"]
    scripts --> sccl["CHANGELOG.md"]
    github --> pr["pull_request_template.md"]
    github --> owners["CODEOWNERS"]
    github --> ghwf["workflows/"]
    ghwf --> ghsync["sync-skills.yml"]
    ghwf --> ghlint["lint-skills.yml"]
    github --> ghscripts["scripts/"]
    ghscripts --> ghlintpy["lint-skill.py"]
    templates --> base["base-document.md"]
    templates --> tcl["CHANGELOG.md"]
    references --> rcl["CHANGELOG.md"]
    references --> rgit["git/"]
    rgit --> rdocs["git-*.md"]
    references --> reng["engineering/"]
    reng --> rengdocs["tech-stack-*.md · code-style.md"]
    references --> rauto["automation/"]
    rauto --> rautodocs["sync-skills-action.md"]
    prompts --> pcl["CHANGELOG.md"]
    prompts --> pgit["git/"]
    agents --> acl["CHANGELOG.md"]
    agents --> agit["git/"]
```

## Document standard

Every **non-skill** document (reference, prompt, agent, template) **must**:

1. Be a copy of [`templates/base-document.md`](templates/base-document.md).
2. Start with **YAML frontmatter** carrying the metadata below.
3. Have a SemVer `version` field.
4. Record its changes in its directory's `CHANGELOG.md` (not a per-document section).

> **Skills are the exception.** Skills follow the **SKILL.md format** instead — a folder
> `skills/<name>/SKILL.md` with `name` + `description` frontmatter (no `version`/`status`/
> `owner`), an imperative body, and optional bundled `scripts/ references/ assets/`. Create
> them with the [`skill-creator`](skills/skill-creator/SKILL.md) skill, not the base
> template. They are still listed in `INDEX.md` and logged in `skills/CHANGELOG.md` (by
> date, since they have no version). The metadata reference below does **not** apply to skills.
>
> **Scripts are also an exception.** Files under `scripts/<topic>/` are executable helpers
> (bash, python, etc.), not Markdown documents — they do not use the base template. Each
> script carries a header comment with `id` (filename stem), `description`, `version`
> (SemVer), and `owner`. They are listed in `INDEX.md` and logged in `scripts/CHANGELOG.md`
> by `id`.

### Metadata reference

| Field          | Required | Meaning                                                              |
| -------------- | -------- | ------------------------------------------------------------------- |
| `title`        | yes      | Human-readable title.                                               |
| `id`           | yes      | Stable kebab-case identifier; matches the filename stem.            |
| `type`         | yes      | One of `skill`, `prompt`, `agent`, `template`, `reference`.         |
| `version`      | yes      | SemVer `MAJOR.MINOR.PATCH`; matches the top changelog entry.        |
| `status`       | yes      | `draft`, `active`, or `deprecated`.                                 |
| `owner`        | yes      | Person or handle responsible for the document.                     |
| `created`      | yes      | ISO date `YYYY-MM-DD` the document was created.                    |
| `updated`      | yes      | ISO date `YYYY-MM-DD` of the last meaningful change.               |
| `tags`         | yes      | List of kebab-case tags for discovery.                             |
| `description`  | yes      | One-line summary; reused verbatim in `INDEX.md`.                   |
| `deprecated_on`| if deprecated | ISO date the document was deprecated.                         |
| `replaced_by`  | if deprecated | `id` of the document that supersedes this one.                |
| `related`      | optional | List of related document `id`s.                                   |

## Versioning

Documents use [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR** — a breaking change to the document's behavior, interface, or meaning.
- **MINOR** — an additive, backward-compatible change.
- **PATCH** — wording, typo, or clarification; no behavior change.

When you change a document: bump `version`, update `updated`, and add an entry to
the directory's `CHANGELOG.md` (see [Changelogs](#changelogs)).

## Changelogs

Documents do **not** carry a per-document changelog section. Instead, each top-level
directory keeps one `CHANGELOG.md` (plus a repo-level `CHANGELOG.md` at the root for
`README.md`, `INDEX.md`, and structural changes). This avoids duplicating history
inside every file.

Each `CHANGELOG.md` follows the [Keep a Changelog](https://keepachangelog.com/) style
— entries grouped **by document `id`**, newest version first, using the categories
**Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**. Keep the
top version entry in sync with the document's `version` metadata.

## Status lifecycle

```mermaid
stateDiagram-v2
    [*] --> draft
    draft --> active: reviewed & ready
    active --> deprecated: replaced or retired
    draft --> deprecated: abandoned
    deprecated --> [*]
```

A `deprecated` document keeps `deprecated_on` and (when applicable) `replaced_by`
in its metadata so readers know where to go next.

## Adding a new document

> **Creating a skill?** Skills don't use these steps or the base template. Use the
> [`skill-creator`](skills/skill-creator/SKILL.md) skill — it produces a
> `skills/<name>/SKILL.md` in the SKILL.md format. Then add it to `INDEX.md` and
> `skills/CHANGELOG.md`.

1. Copy [`templates/base-document.md`](templates/base-document.md) into the right
   `<category>/<topic>/` folder (create the topic subfolder if it doesn't exist).
2. Rename it to `<id>.md` (kebab-case, matching the `id` field).
3. Fill in all required metadata.
4. Write the body; remove optional sections you don't need.
5. Add an initial entry for it in the directory's `CHANGELOG.md`.
6. Register the document in [`INDEX.md`](INDEX.md) under its category.

## Conventions

- **GitHub-flavored Markdown** throughout (tables, fenced code, task lists).
- **All diagrams in [Mermaid](https://mermaid.js.org/)** so they render on GitHub.
- `id` and filenames are **kebab-case**; the `id` matches the filename stem.
- Dates are ISO `YYYY-MM-DD`.
- Changes are logged in each directory's `CHANGELOG.md`, newest version first — not in a per-document section.
