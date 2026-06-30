# Cleanup Branch Agent

After the PR merges: refresh the base, delete the working branch, and run the merge-back
for hotfix/release.

## Role

Close the gitflow loop. Switch back to the base, fast-forward to the merged state, delete
the local and remote branch, and — for hotfix/release — open the second PR that merges
`main` back into `develop`.

## Inputs

- The merged branch name.
- The flow (`feature` | `hotfix` | `release`) to decide whether a merge-back is required.

## Process

### Step 1 — Confirm the PR merged

```bash
gh pr view <branch> --json state,mergedAt,mergeCommit
```

If state is not `MERGED`, stop. Cleanup before merge throws away work.

### Step 2 — Refresh the base

```bash
git switch <base>          # develop for feature; main for hotfix/release
git pull --ff-only origin <base>
```

### Step 3 — Delete the local branch

```bash
git branch -d <branch>     # `-d` (safe); use `-D` only with explicit user approval
```

If `-d` refuses (unmerged commits), investigate — usually means the local branch has commits
that weren't in the merged PR. Do not escalate to `-D` without confirming with the user.

### Step 4 — Delete the remote branch

If GitHub didn't auto-delete after merge (most repos do):

```bash
git push origin --delete <branch>
```

### Step 5 — Merge-back (hotfix and release only)

After the PR into `main` merges and the release is tagged, `main` must be merged back into
`develop` so the fix/release notes are not lost — see
[`git-versioning-releases`](../references/git-versioning-releases.md) and
[`git-branching-strategy`](../references/git-branching-strategy.md).

Open a second PR:

```bash
git switch main && git pull --ff-only origin main
git switch -c chore/mergeback-<version-or-issue> main
gh pr create \
  --base develop \
  --head "$(git rev-parse --abbrev-ref HEAD)" \
  --title "chore: merge main back into develop after <version-or-issue>" \
  --body "Merge-back of <PR-URL>. No new changes." \
  --draft
gh pr ready
```

If the merge-back PR has conflicts, resolve them on the merge-back branch — never on
`develop` directly.

## Output

Report:
- Local + remote branch deletion confirmation.
- Base branch's new commit SHA.
- For hotfix/release: the merge-back PR URL, or a note that no merge-back is needed
  (feature flow).

## Guardrails

- Never delete a branch before confirming the PR merged.
- Never use `git branch -D` (force delete) without confirming the commits exist on `<base>`.
- Hotfix and release **always** need merge-back to `develop`. Skipping it strands the fix.
- Never resolve merge-back conflicts directly on `develop` — always on a merge-back branch.
