---
source:
  issue_url: https://github.com/santichio/peer/issues/7
  project_item_id: PVTI_lAHOBx7hJc4BcG1EzgxUtDE
  project_number: 10
generated_at: 2026-07-02
generator: peer-intake
---

# PRD: Change push method — GitHub MCP connector instead of `gh` CLI

## Introduction

Every skill in this repo that talks to GitHub does so through the `gh` CLI —
`gitflow` opens/merges PRs and cuts releases, and `peer-intake` reads Projects
and issues. The `gh` path requires `gh` to be installed and interactively
authenticated with the right OAuth scopes (the `read:project` scope friction is
a live example), and it is unavailable in sandboxed/headless runs. This PRD
replaces those **GitHub-API** operations with the official **GitHub MCP server**
connector, so Claude drives GitHub through structured MCP tools instead of
shelling out to `gh`. Local `git` operations (branch, commit, rebase) are **not**
in scope and remain plain `git`.

## Goals

- Replace all `gh`-based GitHub-API operations in `gitflow` and `peer-intake`
  with GitHub MCP server tool calls.
- Remove `gh` as an operational dependency of these skills — no `gh` command
  remains in skill instructions; the only surviving mention of `gh` is the
  historical record in `CHANGELOG.md`.
- Keep the skills usable both locally and when synced into consumer repos,
  documenting the MCP prerequisite clearly.
- Leave local `git` usage untouched.

## User Stories

### US-001: Open a PR without `gh`
**Description:** As a developer running the `gitflow` skill, I want the PR to be
opened via the GitHub MCP connector so that I don't need `gh` installed or an
interactive `gh auth` session.
**Acceptance Criteria:**
- [ ] `gitflow`'s open-pr step creates the PR through a GitHub MCP tool (e.g.
  `create_pull_request`), not `gh pr create`.
- [ ] PR title, body, base, and head are passed through unchanged from the
  current behavior.
- [ ] No `gh pr create` / `gh pr view` / `gh pr ready` remains in
  `skills/gitflow/agents/open-pr.md`.

### US-002: Merge / mark-ready and cleanup without `gh`
**Description:** As a developer completing a change, I want merge, ready, and
branch-cleanup steps to use the connector so the whole PR lifecycle is `gh`-free.
**Acceptance Criteria:**
- [ ] `gh pr merge` / `gh pr ready` in `cleanup-branch.md` and `sync-local.md`
  are replaced with the equivalent MCP tools.
- [ ] Branch cleanup logic (delete merged branch) is preserved.

### US-003: Cut a release without `gh`
**Description:** As a maintainer, I want release tagging/creation to use the
connector instead of `gh release create`.
**Acceptance Criteria:**
- [ ] `gh release create` in `release-workflow.md` is replaced with the MCP
  release-creation tool (or documented git-tag + MCP path if no release tool).
- [ ] The version-bump/CHANGELOG/tag sequence is otherwise unchanged.

### US-004: Intake the backlog without `gh`
**Description:** As a user running `peer-intake`, I want project and issue reads
to go through the connector so intake works without `gh` and its `read:project`
scope dance.
**Acceptance Criteria:**
- [ ] `gh project item-list` is replaced with the MCP project-items tool.
- [ ] `gh issue view` is replaced with the MCP issue-read tool.
- [ ] The `gh auth status` / `gh --version` preconditions are replaced with an
  MCP-availability precondition (see FR-6).
- [ ] `references/context-schema.md`'s status-lookup semantics still hold against
  the MCP tool's response shape.

## Functional Requirements

- FR-1: Replace `gh pr create|view|ready|merge` in `skills/gitflow/` with GitHub
  MCP tool calls, preserving arguments and output semantics.
- FR-2: Replace `gh release create` in `skills/gitflow/agents/release-workflow.md`
  with the MCP equivalent (or git-tag + MCP if unavailable).
- FR-3: Replace `gh project item-list` and `gh issue view` in
  `skills/peer-intake/SKILL.md` with GitHub MCP tools; update the JSON-shape
  assumptions in the surrounding prose and `references/context-schema.md`.
- FR-4: Remove every remaining `gh <command>` from skill instructions in
  `gitflow` and `peer-intake`. Leave `git` commands as-is.
- FR-5: Do **not** modify `skills/skill-creator/` (out of scope per CLAUDE.md) or
  the `prd` skill (it has no real `gh` usage — its matches are false positives).
- FR-6: Add a preconditions/prerequisite note to each affected skill stating the
  GitHub MCP server must be connected (and how to connect it), replacing the old
  `gh auth status` check. Note the caveat that MCP servers may be absent in
  headless/cron runs and what the skill should do then (report and stop).
- FR-7: Record the change in `skills/CHANGELOG.md` (dated entry, grouped by skill)
  — this is the only place `gh` should still be named after the change.

## Non-Goals

- Replacing local `git` operations (branch, commit, rebase, tag creation itself).
- Migrating CI in `.github/workflows/` to a connector (this task targets the
  skills; the reusable workflows keep using `GITHUB_TOKEN`/`gh` as they are).
- Touching `skill-creator` or `prd`.
- Introducing the Claude GitHub App/Action (option B) or raw REST (option C) —
  the decision is the MCP server for the interactive skills.
- Building any new MCP server; this consumes the existing official
  `github-mcp-server`.

## Design Considerations

- Skills are prose-with-commands. "Using the connector" means the SKILL.md
  instructs Claude to call the named GitHub MCP tool with specific arguments,
  rather than embedding a `gh` shell command in a fenced block.
- Keep instructions tool-name-specific but resilient: reference the MCP tool by
  its capability (create PR, merge PR, list project items, read issue) so the
  skill still reads clearly if a tool name shifts.
- Preserve the existing stage/agent structure of `gitflow`; only the GitHub-touch
  steps change.

## Technical Considerations

- **In-scope files (representative):**
  `skills/gitflow/agents/open-pr.md` (`gh pr create`),
  `skills/gitflow/agents/cleanup-branch.md` & `sync-local.md` (`gh pr merge/ready`),
  `skills/gitflow/agents/release-workflow.md` (`gh release create`),
  `skills/gitflow/SKILL.md`, and
  `skills/peer-intake/SKILL.md` (`gh project item-list`, `gh issue view`,
  `gh auth status`, `gh --version`) plus
  `skills/peer-intake/references/context-schema.md`.
- **MCP tool mapping (to confirm against the connected server's toolset):**
  `gh pr create` → `create_pull_request`; `gh pr merge` → `merge_pull_request`;
  `gh issue view` → issue-get tool; `gh project item-list` → project-items tool;
  `gh release create` → release-create tool (verify it exists; else git tag + MCP).
- **Auth:** MCP server authenticates via its own token/OAuth config, removing the
  per-user `gh auth refresh -s read:project` step from `peer-intake`.
- **Portability:** because these skills sync into consumer repos, the MCP
  prerequisite must be documented in each skill so a consumer knows to connect
  the GitHub MCP server before use.
- **Governance:** follow this repo's own gitflow — feature branch, Conventional
  Commits (`docs(skills):`, header ≤ 50), PR to `develop`, no self-merge.

## Success Metrics

- `grep -rE "gh (pr|issue|project|release|auth) " skills/gitflow skills/peer-intake`
  returns nothing.
- The only `gh` reference remaining in the repo's skills area is in
  `skills/CHANGELOG.md`.
- The complete implementation lands in a single PR to `develop` that is
  review-ready (green lint, links intact).

## Open Questions

- Which concrete GitHub MCP server will consumers connect (the official remote
  `api.githubcopilot.com/mcp/` vs. a self-hosted/local one), and does its toolset
  include a release-creation tool? If not, `release-workflow` uses `git tag` +
  an MCP push/ref tool.
- Should the reusable `.github/workflows/` remain on `gh`/`GITHUB_TOKEN`
  indefinitely, or is a follow-up task wanted to align CI too? (Currently a
  Non-Goal.)
- Do any consumer repos rely on `peer-intake` working in a headless/cron context
  where MCP is unavailable? If so, define the fallback behavior explicitly.
