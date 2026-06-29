# Changelog — `skills/`

Skills follow the [SKILL.md format](skill-creator/SKILL.md) (folder per skill, `name` +
`description` frontmatter) and have **no per-document version**, so this log is organized
**by date** rather than by SemVer. Based on [Keep a Changelog](https://keepachangelog.com/).

## 2026-06-27

### Added
- `skill-creator` — canonical skill for creating, improving, and evaluating skills.
- `gitflow` — drives a change through gitflow with `git` + `gh`; stops at PR-ready.
- `prd` — generates a Product Requirements Document for a new feature.
- `ralph` — converts a PRD to the `prd.json` format for the Ralph agent system.

### Changed
- Skills now follow the SKILL.md convention (flat `skills/<name>/SKILL.md` folders,
  `name`/`description` frontmatter) instead of the base-document template. `gitflow`
  was restructured into this format and renamed from `gitflow-workflow`.

### Removed
- The previous base-template skill `skills/meta/skill-creator.md` (superseded by
  `skills/skill-creator/`) and the `skills/git/` and `skills/meta/` topic subfolders.
