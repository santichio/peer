# Changelog — `skills/`

Skills follow the [SKILL.md format](skill-creator/SKILL.md) (folder per skill, `name` +
`description` frontmatter) and have **no per-document version**, so this log is organized
**by date** rather than by SemVer. Based on [Keep a Changelog](https://keepachangelog.com/).

## 2026-07-02

### Changed
- **Standardized all skills on a visible `peer/` directory for AI operation
  artifacts** (tasks, references, context, runtime state). Definition files
  (`SKILL.md`, `prompt.md`, `CLAUDE.md`, `ralph.sh`) and platform config stay put.
- `peer-intake` — renamed its artifact directory from `.peer/` to `peer/`
  (`peer/context.md`, `peer/prd/`); updated `SKILL.md`, `references/context-schema.md`,
  and the `INDEX.md` description to match.
- `prd` — PRDs now save to `peer/prd/prd-[feature-name].md` instead of the
  root-level `tasks/`, aligning with `peer-intake`'s output folder.
- `ralph` — runtime state (`prd.json`, `progress.txt`, `archive/`, `.last-branch`)
  now lives in the repo's `peer/ralph/` instead of inside the skill bundle
  (`$SCRIPT_DIR`). `ralph.sh` bumped to 1.1.0; `SKILL.md` paths updated.
- **Replaced the `gh` CLI with the GitHub MCP server connector** for all
  GitHub-API operations in the skills that touch GitHub. Local `git` is
  unchanged; only GitHub-API calls moved. `gh` is no longer an operational
  dependency — this changelog entry is the only remaining reference to it.
  - `gitflow` — `open-pr`, `cleanup-branch`, `sync-local`, `release-workflow`,
    and `SKILL.md` now use GitHub MCP tools: `gh pr create`/`gh pr ready` →
    `create_pull_request` (`draft: false`, so PRs open ready — no draft phase);
    `gh pr view` → `pull_request_read`; `gh pr merge` → GitHub UI /
    `merge_pull_request`; the MCP-connected check replaces `gh --version`/
    `gh auth status`/`gh auth login`. `gh release create` has no MCP equivalent,
    so releases stop at the pushed `git` tag and the GitHub Release object is
    deferred (manual/follow-up).
  - `peer-intake` — `gh project item-list` → `projects_list`
    (`list_project_items`), `gh issue view` → `issue_read`; preconditions and
    `references/context-schema.md` updated to the MCP tools and response shape.
  - Documents both server options (hosted `api.githubcopilot.com/mcp/`, preferred;
    local `ghcr.io/github/github-mcp-server`). Reusable `.github/workflows/` CI is
    intentionally left on `GITHUB_TOKEN` (out of scope).

## 2026-06-30

### Changed
- **Repo restructure: skills now bundle the artifacts they own.** `gitflow`
  absorbs its supporting references (`git-*.md` moved from
  `references/git/` into `skills/gitflow/references/`), the
  `branch-name-helper` and `commit-message-writer` prompts (from
  `prompts/git/` into `skills/gitflow/prompts/`), and the
  `pr-review-assistant` agent (from `agents/git/` into
  `skills/gitflow/agents/`). `ralph` absorbs `ralph.sh` (from
  `scripts/ralph/`). All in-skill links rewritten to relative paths — the
  full-GitHub-URL pattern previously needed for portability is no longer
  required since every dependency now lives inside the skill folder.
- `ralph` — `SKILL.md` now links to the bundled `ralph.sh` directly instead
  of describing it obliquely as "the ralph.sh script".

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
