# Release Workflow Agent

Orchestrate a release end-to-end: cut the release branch, bump the version, update the
changelog, open the PR, tag the release on `main`, and merge back into `develop`.

## Role

Chain the per-step agents for a release. This is the only gitflow agent that owns
**versioning** (SemVer bump) and **changelog maintenance** in addition to the standard
branch / commit / PR cycle. Always follows
[`git-versioning-releases`](https://github.com/santichio/peer/blob/main/references/git/git-versioning-releases.md).

## Inputs

- **version**: target SemVer (e.g. `1.5.0`). If the user gives a release type
  (`major` | `minor` | `patch`), derive it from the current tag with `git describe --tags
  --abbrev=0` and apply the bump.
- **release-notes source**: usually the commits since the last `v*` tag
  (`git log v<prev>..HEAD --oneline`); ask the user if non-obvious.

## Process

### Stage 1 — Sync local

Run [`sync-local`](sync-local.md) with base `develop`. Abort the release if the working
tree isn't clean or origin isn't reachable.

### Stage 2 — Cut the release branch

Run [`create-branch`](create-branch.md) with `flow=release` and `version=<X.Y.Z>`. Branch:
`release/<X.Y.Z>`, origin `develop`.

### Stage 3 — Bump the version

Update the project's canonical version source. Common shapes (pick the one(s) that apply):

- `package.json` (Node) — `npm version <X.Y.Z> --no-git-tag-version`
- `pyproject.toml` (Python) — bump `[project] version = "<X.Y.Z>"`
- `Cargo.toml` (Rust) — bump `[package] version = "<X.Y.Z>"`
- `<module>/__init__.py` `__version__`, `VERSION`, etc.

If unclear, grep the repo for the previous version and update every occurrence; verify with
`grep -r "<prev-version>" --include='*.json' --include='*.toml' --include='*.py'`.

### Stage 4 — Update CHANGELOG.md

Per [`git-versioning-releases`](https://github.com/santichio/peer/blob/main/references/git/git-versioning-releases.md):

- Newest version on top.
- Categorize under: **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**.
- Reference issue / PR numbers.
- Clearly mark breaking changes.

Use this template:

```markdown
## [<X.Y.Z>] — <YYYY-MM-DD>

### Added
- ...

### Changed
- ...

### Fixed
- ...
```

Generate the bullet candidates from `git log v<prev>..HEAD --oneline` and bucket them by
commit type (`feat` → Added/Changed, `fix` → Fixed, `BREAKING CHANGE` → mark prominently).

### Stage 5 — Commit the bump + changelog

Run [`commit-changes`](commit-changes.md). Two commits (atomic):

```text
chore(release): bump version to <X.Y.Z>
docs(changelog): record <X.Y.Z>
```

### Stage 6 — Push and open the PR

Run [`push-branch`](push-branch.md), then [`open-pr`](open-pr.md) with `flow=release`
(PR base `main`). Title: `release: <X.Y.Z>`. Body must list the changelog section verbatim.

**Stop for human review.** The release manager (not this agent) merges the PR.

### Stage 7 — Tag the release on `main` (after merge)

After the human merges the release PR into `main`:

```bash
git switch main && git pull --ff-only origin main
git tag -a v<X.Y.Z> -m "Release <X.Y.Z>"   # add -s if release manager signs tags
git push origin v<X.Y.Z>
```

Tag format is `v<SemVer>` per
[`git-versioning-releases`](https://github.com/santichio/peer/blob/main/references/git/git-versioning-releases.md). Tags are
**never deleted or moved** once pushed — to withdraw, ship a new release.

### Stage 8 — Publish release notes

```bash
gh release create v<X.Y.Z> \
  --title "v<X.Y.Z>" \
  --notes-file <(awk "/^## \\[<X.Y.Z>\\]/,/^## \\[/{print}" CHANGELOG.md | sed '$d')
```

Adjust if release notes should differ from the changelog section.

### Stage 9 — Merge-back into `develop`

Run [`cleanup-branch`](cleanup-branch.md) with `flow=release`. It will:

- Delete the merged `release/<X.Y.Z>` branch.
- Open the second PR `main → develop` (title: `chore: merge main back into develop after <X.Y.Z>`).
- Stop for human review of the merge-back PR.

The release is only complete once both the tag and the merge-back PR have landed.

## Output

Report at each handoff. Final report:
- Released version: `v<X.Y.Z>`.
- Release PR URL (merged).
- Tag SHA on `main`.
- GitHub release URL.
- Merge-back PR URL (open or merged).

## Guardrails

- Never tag from `develop` or a release branch — always tag the merged commit on `main`.
- Never move or delete a released tag. To withdraw, ship a follow-up release.
- Never skip the merge-back PR. Hotfixes and releases must both flow back to `develop`.
- Never self-merge the release PR or the merge-back PR — both need human approval.
- If the previous tag isn't reachable from `develop`, stop and investigate before computing
  the changelog diff — the history is likely fractured.
- Pre-releases (`1.0.0-alpha.1`) and build metadata (`1.0.0+sha`) follow the same flow but
  do **not** trigger a merge-back unless the user explicitly asks.
