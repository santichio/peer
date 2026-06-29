# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A documentation repository that standardizes and centralizes AI-related documents —
**skills, prompts, agents, templates, and references**. There is no build system, no
package manager, and no tests: every "artifact" is a Markdown document that conforms to
a shared standard. Work here is authoring and maintaining those documents and keeping
the catalog consistent.

## Non-negotiable document standard

Every **non-skill** document (reference, prompt, agent, template) is a copy of
[`templates/base-document.md`](templates/base-document.md) and must have:

- **YAML frontmatter** with: `title`, `id` (kebab-case, **matches the filename stem**),
  `type` (`prompt|agent|template|reference`), `version` (SemVer), `status`
  (`draft|active|deprecated`), `owner`, `created`, `updated`, `tags`, `description`
  (one line, reused verbatim in `INDEX.md`), and optional `related` (list of doc ids).
  Deprecated docs also carry `deprecated_on` / `replaced_by`.
- **No per-document changelog section.** History lives in a per-directory `CHANGELOG.md`
  (see below). This was a deliberate change — do not reintroduce `## Changelog` sections.
- GitHub-flavored Markdown; **all diagrams in Mermaid** (renders natively on GitHub).

**Skills are the exception** — they do NOT use the base template or this frontmatter. A
skill is a folder `skills/<name>/SKILL.md` in the [SKILL.md format](skills/skill-creator/SKILL.md):
`name` + `description` frontmatter (no version/status/owner), imperative body, optional
bundled `scripts/ references/ assets/`. Authored via the `skill-creator` skill. Don't
modify anything under `skills/skill-creator/`.

**Scripts are also an exception** — files under `scripts/<topic>/` are executable helpers
(bash, python, etc.), not Markdown. Metadata lives in a **header comment** at the top of
the file (`id` matches the filename stem, `description`, `version` SemVer, `owner`); they
do not use YAML frontmatter or the base template. List them in `INDEX.md` (Scripts section)
and log changes in `scripts/CHANGELOG.md` by `id` like other categories.

## Layout

- **Non-skill docs:** `<category>/<topic>/<id>.md` — categories `prompts/ agents/
  references/`; documents grouped in **topic** subfolders (e.g. `references/git/`,
  `references/engineering/`). `templates/` holds the base template directly.
- **Skills:** flat `skills/<name>/SKILL.md` — one self-contained folder per skill, no
  topic subfolder.
- **Scripts:** `scripts/<topic>/<id>.{sh,py,...}` — executable helpers; metadata in a
  header comment, not YAML frontmatter.

## Creating a new document

> **Exception — skills.** To create a skill, use the
> [`skill-creator`](skills/skill-creator/SKILL.md) skill — it produces a
> `skills/<name>/SKILL.md` in the SKILL.md format (not the base template). Then register it
> in `INDEX.md` (Skills table, version/status `—`) and `skills/CHANGELOG.md` (by date). The
> steps below are for non-skill documents.

1. **Copy the template.** `cp templates/base-document.md <category>/<topic>/<id>.md`.
   Pick the category (`skills/ prompts/ agents/ references/`) and a topic subfolder
   (e.g. `git`, `engineering`). Create the topic folder if it's new. The filename stem
   **is** the `id` (kebab-case).
2. **Fill the frontmatter.** All required fields; `version: 1.0.0`; `created` and
   `updated` = today (ISO `YYYY-MM-DD`); `status` usually `active` (or `draft`); set
   `related` ids. Write the body in GFM (Mermaid for diagrams), remove unused optional
   sections, and **do not add a `## Changelog` section**.
3. **Register in `INDEX.md`.** Add one row under the matching category table:
   `| [\`<id>\`](<category>/<topic>/<id>.md) | <Title> | <version> | <status> | <description> |`.
   The description must match the frontmatter `description` verbatim.
4. **Log in the directory `CHANGELOG.md`** (`<category>/CHANGELOG.md`, one level above the
   topic folder). Add a block grouped by id:
   ```markdown
   ## `<id>`

   ### [1.0.0] — <today>
   #### Added
   - <one-line summary of what the document provides>
   ```
   **First doc in a category?** That `CHANGELOG.md` won't exist yet — create it by copying
   the header from an existing one (e.g. `references/CHANGELOG.md`), and delete the
   category's `.gitkeep` placeholder.
5. **Update `README.md` only if the structure changed** — i.e. you added a **new category**
   or a **new topic subfolder**. Add it to the "Repository structure" table and the Mermaid
   diagram (mirror how `references/git/` is shown). Adding a doc to an *existing* topic needs
   no README change.
6. **Verify links** with the checker in the [Cross-links](#cross-links) section.

## Changing an existing document

1. **Edit the file**, then bump `version` (SemVer: MAJOR = breaking/meaning change,
   MINOR = additive, PATCH = wording/typo) and set `updated` to today.
2. **Add a new version entry** at the top of that document's `## \`<id>\`` block in the
   directory `CHANGELOG.md` (newest first), under the right category — Added / Changed /
   Deprecated / Removed / Fixed / Security.
3. **Sync `INDEX.md`** if the row's visible fields changed (`version`, `title`, `status`,
   or `description`).
4. **Renaming / moving** (id change): rename the file and `id` together, update every
   inbound relative link and `related` reference, fix the `INDEX.md` path, and note it in
   the `CHANGELOG.md`. Then run the link checker.
5. **Deprecating:** set `status: deprecated`, add `deprecated_on` and (if applicable)
   `replaced_by`; update the `INDEX.md` status; log under **Deprecated** in the changelog.

> The repo-root `CHANGELOG.md` is only for repo-level changes (README, INDEX structure,
> governance files) — not for individual document edits, which go in the category changelog.

## Reconciling a user-edited document

When the **user** edits a document directly (in their editor, by renaming a file, by
moving a folder) and asks you to "tidy up" or "register" it, your job is
**reconciliation, not authoring**. Treat the user's content as authoritative.

**Hard rule — do not modify the body of the document.** Leave headings, prose, code
blocks, and diagrams exactly as the user wrote them. The only edits you may make to the
file itself are the minimum frontmatter fixes required by repo policy (see step 4 below).

1. **Read the file and understand what changed.** Compare against `git diff` if a prior
   version is on disk. Note: content edits, frontmatter edits, filename change, folder
   move, or any combination.
2. **Verify directory placement.** The file must live under the correct category and
   topic:
   - `references/<topic>/`, `prompts/<topic>/`, `agents/<topic>/` — non-skill docs
     grouped by topic.
   - `templates/` — base template only.
   - `skills/<name>/SKILL.md` — flat, no topic subfolder.
   - `scripts/<topic>/<id>.{sh,py,...}` — executable helpers.

   If the file is in the wrong place, `git mv` it to the right path. Confirm with the
   user before moving if the correct topic is ambiguous.
3. **Verify `id` ↔ filename match.** For non-skill docs the `id` frontmatter field must
   equal the filename stem. If the user changed one without the other, reconcile —
   prefer keeping the user's evident intent and ask when ambiguous.
4. **Minimum frontmatter fix-ups (only if required).** If the user changed the body but
   didn't bump `version` or update `updated`, do so per SemVer (MAJOR/MINOR/PATCH) and
   set `updated` to today. Do not touch any other frontmatter field unless the user's
   change made it inconsistent (e.g. they deprecated a doc but forgot `deprecated_on`).
5. **Update the registry — `INDEX.md`.** Sync the row's visible fields (`version`,
   `title`, `status`, `description`, path). The description must remain verbatim from
   the frontmatter. Add/remove the row if a doc was added/removed.
6. **Update `README.md` only if the structure changed** — a new category or topic
   subfolder appeared, or one disappeared. Add/remove it in the structure table and the
   Mermaid diagram.
7. **Log the change in the directory `CHANGELOG.md`.** Add a new version entry at the
   top of that document's `` ## `<id>` `` block (newest first), under the right category
   — Added / Changed / Deprecated / Removed / Fixed / Security. Summarize what the user
   changed in one line. For governance file edits (`README.md`, `INDEX.md`, `CLAUDE.md`,
   `CONTRIBUTING.md`) log in the repo-root `CHANGELOG.md` instead.
8. **Verify cross-links.** If the file moved or was renamed, run the link checker from
   the [Cross-links](#cross-links) section and fix any `BROKEN:` paths in *other* files
   (still not the user-edited file's body unless a link there now points nowhere).

If a step would require editing the user's body to keep things consistent (e.g. the user
moved a referenced doc but didn't update an in-body link), surface it to the user and
ask before touching the body.

## Cross-links

Documents reference each other with **relative Markdown links** and via the `related`
frontmatter (which uses ids, not paths). Because of the two-deep layout, links between
categories use `../../` (e.g. a `skills/<name>/SKILL.md` links a reference as
`../../references/git/<id>.md`). After moving or adding files, verify every link resolves
(the checker below — the `skills/skill-creator/` bundle's internal links are out of scope):

```bash
# from repo root — prints BROKEN lines for any unresolved relative .md link
grep -rEn "\]\([^)]+\.md[^)]*\)" --include='*.md' . | while IFS= read -r line; do
  file="${line%%:*}"; rest="${line#*:}"; rest="${rest#*:}"
  echo "$rest" | grep -oE "\]\([^)#]+\.md" | sed -E 's/^\]\(//' | while IFS= read -r t; do
    [ "$t" = "../references/other-doc-id.md" ] && continue   # template placeholder
    [ -e "$(dirname "$file")/$t" ] || echo "BROKEN: $file -> $t"
  done
done
```

## This repo follows its own git policy

The git references under `references/git/` are the policy this repo is governed by, and
`skills/gitflow/SKILL.md` is the operational procedure. When making changes here:

- Branch from `develop` (not `main`); both are default branches. Name branches
  `feature/<issue_id>-<name>` (or `hotfix/`). See `references/git/git-branching-strategy.md`.
- Commits follow Conventional Commits, **header ≤ 50 chars**, standard types only
  (the custom `cleanup`/`remove`/`raw` types were removed). See
  `references/git/git-commit-conventions.md`. `docs(...)` is the usual type for content here.
- **Do not self-merge.** Open a PR (base `develop`) and stop for review —
  `references/git/git-code-review.md` requires ≥1 approval; `.github/CODEOWNERS` routes it.

## Reusable workflows

`.github/workflows/` ships two reusable workflows that consumer repos use:

- **`sync-skills.yml`** — reusable `workflow_call` workflow that syncs selected
  `skills/<name>/` folders from this repo into a consumer's destination dir
  (default `.claude/skills`). Modes: `pull-request` (default) or `commit`. Inputs
  documented in [`references/automation/sync-skills-action.md`](references/automation/sync-skills-action.md).
- **`lint-skills.yml`** — CI guard. Runs on every PR and push touching `skills/`; calls
  `.github/scripts/lint-skill.py` to assert each `skills/<name>/SKILL.md` has YAML
  frontmatter, a `name:` matching the folder, and a non-empty `description:`.

Until a release is tagged, consumers pin to `@develop` or a commit sha — the
`@v1` form will work after the first tag.

## Conventions quick reference

- `id` and filenames are kebab-case; `id` == filename stem.
- Dates are ISO `YYYY-MM-DD`.
- `temp/` holds raw, un-standardized source material that gets converted into documents;
  it is not part of the catalog. Leave its files unless asked to clean up.
- See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full "add a document" procedure and
  [`README.md`](README.md) for the metadata reference and status lifecycle.
