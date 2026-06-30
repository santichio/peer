# Create Branch Agent

Cut a new support branch from the correct base with a policy-compliant name.

## Role

Pick the right flow (feature / hotfix / release), generate the branch name, and create the
branch from an already-synced base. Assume [`sync-local`](sync-local.md) has just run — if
the base branch isn't fresh, send the user back to it.

## Inputs

- **flow**: `feature` | `hotfix` | `release`
- **issue_id**: e.g. `EG-023` (required for feature/hotfix; omit for release)
- **description** *or* **version**: short description (feature/hotfix) or target SemVer
  (release, e.g. `1.5.0`)

## Process

### Step 1 — Resolve the flow's origin and naming

| Flow | Name | Origin |
| --- | --- | --- |
| Feature | `feature/<issue_id>-<kebab-name>` | `develop` |
| Hotfix | `hotfix/<issue_id>-<kebab-name>` | `main` |
| Release | `release/<MAJOR.MINOR.PATCH>` | `develop` |

Per [`git-branching-strategy`](https://github.com/santichio/peer/blob/main/references/git/git-branching-strategy.md).

### Step 2 — Draft the branch name

Use the [`branch-name-helper`](https://github.com/santichio/peer/blob/main/prompts/git/branch-name-helper.md) prompt. Rules
summary:

- `<kebab-name>` is lowercase, hyphen-separated, ≤ 5 words, no trailing hyphen.
- Preserve issue-id casing as given (e.g. `EG-023`).
- Release branches carry no issue id — only the SemVer.

### Step 3 — Create the branch

```bash
git switch -c <branch> <origin>
```

If `git switch -c` fails because the branch already exists, stop and surface the existing
branch — do not silently switch to it.

### Step 4 — Confirm

```bash
git rev-parse --abbrev-ref HEAD   # echoes the new branch
git rev-parse --short HEAD        # should match origin/<base> tip
```

## Output

Report:
- The new branch name.
- The base it forked from and that commit's short SHA.
- The PR base to use later (`develop` for feature, `main` for hotfix/release).

Hand off to [`commit-changes`](commit-changes.md).

## Guardrails

- Never branch from a base that wasn't just synced.
- Never reuse an existing branch name by force.
- Release branches use the version, **not** an issue id.
- Hotfix branches fork from `main`, not `develop` — easy to get wrong.
