# Changelog — repository

Repo-level changes: root documents (`README.md`, `INDEX.md`), structure, and
governance. Per-category document history lives in each directory's `CHANGELOG.md`.
Based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

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
