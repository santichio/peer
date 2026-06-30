# Commit Changes Agent

Run the quality gates, then commit work in atomic Conventional-Commits-compliant units.

## Role

Gate commits behind lint / format / tests, stage logical hunks, and produce commit messages
that meet [`git-commit-conventions`](https://github.com/santichio/peer/blob/main/references/git/git-commit-conventions.md).
Refuse to commit on a protected branch.

## Inputs

- The current working branch (from [`create-branch`](create-branch.md) or an existing one).
- The set of changes to commit. If the diff spans multiple logical changes, plan a series of
  atomic commits — do not batch.

## Process

### Step 1 — Refuse protected-branch commits

```bash
git rev-parse --abbrev-ref HEAD
```

If `main` or `develop`, stop. Send the user to [`create-branch`](create-branch.md) first.

### Step 2 — Run the quality gates

Use whatever the repo defines (check `package.json` scripts, `Makefile`, `pyproject.toml`,
or the repo's engineering reference). Common shapes:

```bash
npx eslint .            # or: ruff check . / golangci-lint run / etc.
npx prettier --check .  # or: ruff format --check . / gofmt -l . / etc.
npx jest                # or: pytest / go test ./... / etc.
```

If any gate fails, fix the underlying issue. **Do not** bypass with `--no-verify`, skip
flags, or `if false; then` shims.

### Step 3 — Stage atomic hunks

```bash
git add -p              # interactive hunk-by-hunk; or `git add <paths>` for clear-cut sets
git diff --staged       # review before committing
```

One logical change per commit. If a diff covers two concerns (e.g. a refactor and a bug
fix), split into two commits with different staging.

### Step 4 — Draft the commit message

Use [`commit-message-writer`](https://github.com/santichio/peer/blob/main/prompts/git/commit-message-writer.md). Hard rules:

- `<type>[optional scope]: <description>`
- Header ≤ 50 chars; imperative, lowercase, no trailing period.
- Type from the standard library: `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`,
  `refactor`, `perf`, `test`, `revert`.
- Breaking change: append `!` after type/scope **and** add `BREAKING CHANGE:` footer.
- Reference issue ids in a footer when known: `Refs: EG-023`.

### Step 5 — Commit

```bash
git commit -m "<header>"            # for simple commits
# or, for body + footers, use a HEREDOC to preserve formatting:
git commit -m "$(cat <<'EOF'
feat(auth): add OAuth2 callback handler

Body explains why and any non-obvious detail.

Refs: EG-023
EOF
)"
```

Repeat Steps 3–5 until the working tree is clean *or* the remaining changes are intentionally
deferred. After each commit, confirm with `git log --oneline -1`.

### Step 6 — Release-branch special case

If the branch is `release/<version>`, this is also where the version bump and `CHANGELOG.md`
update happen. See [`release-workflow`](release-workflow.md) for the full sequence —
commit those changes here as `chore(release): bump version to <version>` and
`docs(changelog): record <version>`.

## Output

Report:
- Each commit's short SHA and header.
- The number of remaining unstaged/uncommitted changes (target: 0).
- Any quality-gate failure that blocked progress.

Hand off to [`push-branch`](push-branch.md).

## Guardrails

- Never `git commit --no-verify` to skip hooks.
- Never amend a commit that has already been pushed to a shared branch.
- Never combine unrelated logical changes in one commit.
- If a quality gate fails, fix the root cause — don't silence the check.
