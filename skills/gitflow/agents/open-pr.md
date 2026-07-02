# Open PR Agent

Open the pull request via the GitHub MCP server, fill the template, link the issue, and stop for review.

## Role

Take a pushed branch and produce a review-ready PR that satisfies
[`git-code-review`](../references/git-code-review.md). **Never** approve or merge
the PR — end at "ready for review" and surface the URL to the user.

## Inputs

- The pushed branch (from [`push-branch`](push-branch.md)).
- The flow (`feature` | `hotfix` | `release`) to pick the PR base.
- The issue id (if any) and a short summary of what shipped.

## Process

### Step 1 — Resolve the PR base

| Flow | PR base |
| --- | --- |
| Feature | `develop` |
| Hotfix | `main` |
| Release | `main` |

For hotfix/release, a second PR `main → develop` is required after merge — see
[`cleanup-branch`](cleanup-branch.md).

### Step 2 — Draft title and body

- **Title**: Match the lead commit (`<type>(scope): <description>`). Keep it ≤ 70 chars.
- **Body** must include:
  - What the change accomplishes and why.
  - Linked issue (`Closes EG-023` or `Refs: EG-023`).
  - Testing notes (commands run, screenshots/recordings for UI changes).
  - Any reviewer-facing context (risk, rollout, follow-ups).

If the repo has a PR template (`.github/pull_request_template.md`), fill that template
verbatim — do not invent a new structure.

### Step 3 — Create the PR via the GitHub MCP server

Resolve `owner`/`repo` from the origin remote (`git remote get-url origin`), then
call the GitHub MCP tool **`create_pull_request`**:

- `owner`, `repo` — from the origin remote.
- `base` — the PR base from Step 1.
- `head` — the current branch (`git rev-parse --abbrev-ref HEAD`).
- `title` — `<type>(<scope>): <description>`.
- `body` — the filled template, e.g.:

  ```
  ## What & why
  <one or two paragraphs>

  ## Testing
  - <command run>
  - <screenshot or recording for UI>

  Closes EG-023
  ```
- `draft` — `false` (open ready for review directly).

### Step 4 — Report and stop

Report the PR URL from the `create_pull_request` result and **STOP**. The merge is
performed by a human reviewer after approval — do **not** merge from this agent.
The reviewer merges from the GitHub PR UI (`Merge pull request`, no fast-forward,
delete branch), or an automated flow may call the `merge_pull_request` MCP tool.

For a first-pass reviewer perspective, the [`pr-review-assistant`](../agents/pr-review-assistant.md)
agent can preview likely review feedback before a human takes over.

## Output

Report:
- PR URL.
- PR base and head.
- Confirmation the PR opened ready for review (not draft).
- Reminder: hotfix/release requires merge-back to `develop` after merge.

## Guardrails

- Never approve your own PR.
- Never merge a PR you authored.
- Never set `--base develop` for a hotfix or release.
- If CI fails, fix and push — do not bypass required checks.
- If the PR template fields are empty, fill them — empty PRs get bounced.
