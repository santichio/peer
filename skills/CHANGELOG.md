# Changelog — `skills/`

Skills follow the [SKILL.md format](skill-creator/SKILL.md) (folder per skill, `name` +
`description` frontmatter) and have **no per-document version**, so this log is organized
**by date** rather than by SemVer. Based on [Keep a Changelog](https://keepachangelog.com/).

## 2026-06-30

### Added
- `peer-intake` — convert GitHub Project "To Do" tasks into standardized PRDs
  under `.peer/prd/`. Reads project coordinates and product context from a new
  `.peer/context.md` file (schema bundled at
  `skills/peer-intake/references/context-schema.md`), pulls items via the
  GitHub CLI, asks clarifying questions when a task is thin, and writes one
  PRD per task using the `/prd` skill's section format so the output drops
  straight into `/ralph`.

### Fixed
- `gitflow` — rewrote every external relative link in `SKILL.md` and the bundled
  `agents/*.md` files to fully-qualified `https://github.com/santichio/peer/blob/main/…`
  URLs. The previous `../../…` paths broke when the skill was synced into consumer repos
  by `sync-skills.yml` (which rsyncs the skill folder verbatim, no link rewriting). 19
  links updated across 6 files; sibling links inside the skill folder were left as
  relative paths.

### Changed
- `skill-creator` — added a "Portability — self-contained skills" subsection to
  `SKILL.md` (under Skill Writing Guide) that requires new skills to bundle their
  references and forbids relative links escaping the skill folder. External pointers
  must use the full GitHub URL.

## 2026-06-29

### Changed
- `gitflow` — split each stage of the workflow into a bundled subagent under
  `skills/gitflow/agents/` (`sync-local`, `create-branch`, `commit-changes`, `push-branch`,
  `open-pr`, `cleanup-branch`) and refactored `SKILL.md` into a coordinator that dispatches
  to them. Behavior unchanged — only modularity and reuse improve.

### Added
- `gitflow` — `agents/release-workflow.md` orchestrates a release end-to-end: cut the
  release branch, bump the version, update `CHANGELOG.md`, open the PR, tag on `main`
  after merge, and run the merge-back PR into `develop`. Fills the previous gap where the
  skill referenced versioning but bundled no orchestration.

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
