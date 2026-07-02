# Changelog — repository

Repo-level changes: root documents (`README.md`, `INDEX.md`), structure, and
governance. Per-category document history lives in each directory's `CHANGELOG.md`.
Based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Changed
- **Repo focus narrowed to agents, prompts, and skills (2026-06-30).** Supporting
  references and scripts now bundle inside the skill that owns them so each skill
  folder is self-contained and copyable into a consumer repo without external
  dependencies. Specifically:
  - `references/git/*.md` → `skills/gitflow/references/`
  - `prompts/git/*.md` → `skills/gitflow/prompts/`
  - `agents/git/pr-review-assistant.md` → `skills/gitflow/agents/`
  - `scripts/ralph/ralph.sh` → `skills/ralph/`
  - `references/automation/sync-skills-action.md` →
    `.github/workflows/sync-skills-action.md` (adjacent to the workflow it documents)
  - The now-empty top-level `prompts/`, `agents/`, and `scripts/` directories were
    removed along with their per-directory `CHANGELOG.md` files.
  - `references/engineering/*.md` is deferred — these stay at the top level for now
    and will be addressed in a follow-up.
  All inbound links across `INDEX.md`, `README.md`, `CONTRIBUTING.md`, `CLAUDE.md`,
  and `.github/pull_request_template.md` were rewritten to point at the new
  locations.

### Added
- Initial repository scaffolding: `README.md`, `INDEX.md`, base template, and the
  `templates/ skills/ prompts/ agents/ references/` structure.
- Governance: `CONTRIBUTING.md`, `.github/pull_request_template.md`, `.github/CODEOWNERS`,
  and `CLAUDE.md` (guidance for Claude Code).
- One `CHANGELOG.md` per top-level directory (Keep a Changelog style).
- Git `develop` branch alongside `main`.

### Changed
- Document changes are now tracked in per-directory `CHANGELOG.md` files instead of a
  per-document `## Changelog` section.
- Documents are organized into topic subfolders (`<category>/<topic>/`); existing git
  documents moved under `references/git/`, `prompts/git/`, and `agents/git/`.
  `CHANGELOG.md` remains at each category root.
- **Skills adopted the SKILL.md format** (flat `skills/<name>/SKILL.md`, `name`/`description`
  frontmatter) as an exception to the base-document standard. `README.md`, `CLAUDE.md`,
  `CONTRIBUTING.md`, `templates/base-document.md`, and `INDEX.md` updated accordingly;
  `skills/CHANGELOG.md` switched to by-date entries.
- Added top-level `scripts/` category for executable helpers (bash, python, etc.) — not
  Markdown docs; metadata lives in a header comment, not YAML frontmatter. Registered in
  `README.md`, `INDEX.md`, `CLAUDE.md`, and seeded `scripts/CHANGELOG.md`.
- Added reusable `sync-skills` `workflow_call` workflow that syncs `skills/<name>/`
  folders from this repo into a consumer's destination directory (default
  `.claude/skills`), with `pull-request` (default) or `commit` modes.
- Added CI `lint-skills` workflow that validates every `skills/<name>/SKILL.md` has YAML
  frontmatter, `name` matching the folder, and a non-empty `description`. Backed by
  `.github/scripts/lint-skill.py`.
- Added `sync-skills-action` consumer reference guide under `references/automation/`
  (new topic subfolder) — inputs table, examples, pinning strategy, troubleshooting.
- `CLAUDE.md`: documented the "reconciling a user-edited document" workflow — Claude's
  housekeeping responsibilities (placement, INDEX/README/CHANGELOG sync, cross-link
  verification) when the user edits a doc directly, with an explicit "do not modify the
  body" rule.
