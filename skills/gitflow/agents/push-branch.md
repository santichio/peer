# Push Branch Agent

Push the working branch to `origin` with upstream tracking.

## Role

Publish the local support branch so a pull request can be opened. Confirm the push landed
and the branch is tracking `origin/<branch>`.

## Inputs

- The current working branch (must not be `main` or `develop`).

## Process

### Step 1 — Sanity-check the branch

```bash
branch=$(git rev-parse --abbrev-ref HEAD)
case "$branch" in
  main|develop) echo "refusing to push from $branch"; exit 1 ;;
esac
git status --porcelain   # warn if uncommitted changes remain
```

### Step 2 — Push with upstream tracking

```bash
git push -u origin "$branch"
```

If the remote already has the branch and rejects a non-fast-forward push, **stop**. Do not
force-push. Investigate whether someone else pushed to the same branch and resolve with the
user (typically rebase + force-with-lease, but only with explicit approval).

### Step 3 — Confirm tracking

```bash
git rev-parse --abbrev-ref --symbolic-full-name @{u}   # should print origin/<branch>
```

## Output

Report:
- Branch name and the commit it now points at.
- The `origin/<branch>` URL (derived from `git remote get-url origin`).

Hand off to [`open-pr`](open-pr.md).

## Guardrails

- Never `git push --force` on a shared branch.
- `git push --force-with-lease` only with explicit user approval and only on a personal
  feature branch.
- Never push from `main` or `develop`.
