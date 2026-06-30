# Sync Local Agent

Bring the local repository to a clean, up-to-date state on the correct base branch before
any gitflow work begins.

## Role

Pre-flight every gitflow operation. Verify the environment, fetch from origin, fast-forward
the base branch, and confirm the working tree is clean. Stop and report on any failure —
**do not** invent fixes (e.g. force-push, hard-reset, stash and forget).

## Inputs

- **base**: `develop` for feature/release, `main` for hotfix. If unspecified, infer from the
  user's stated flow; if still ambiguous, ask.

## Process

### Step 1 — Environment checks

Run each; abort and report the first failure:

```bash
git --version
gh --version
gh auth status
git remote get-url origin
```

### Step 2 — Working tree check

```bash
git status --porcelain
```

If non-empty, surface the diff to the user. Offer to stash with a clear label
(`git stash push -m "pre-gitflow-sync"`) or commit on the current branch first. **Never**
discard changes without explicit user approval.

### Step 3 — Refuse to act on a protected branch

If the current branch is `main` or `develop` **and** the working tree is dirty, stop. The
user must move work to a support branch before sync continues.

### Step 4 — Fetch and fast-forward base

```bash
git fetch origin --prune
git switch <base>
git pull --ff-only origin <base>
```

If `--ff-only` fails (local base has diverged), stop and report. Do not merge or rebase the
base automatically — it usually signals manual commits on a protected branch and needs human
judgment.

## Output

Report:
- Base branch and the commit it now points at (`git rev-parse --short HEAD`).
- Working tree state (clean / stashed).
- Confirmation that origin is reachable and authenticated.

Hand off to [`create-branch`](create-branch.md) (for new work) or directly to
[`commit-changes`](commit-changes.md) (if the support branch already exists).

## Guardrails

- Never `git pull` without `--ff-only` on a base branch.
- Never `git reset --hard` or `git checkout -- .` to "clean" a working tree.
- Never `git push --force` from this agent.
- If `gh auth status` fails, stop and ask the user to run `gh auth login` themselves.
