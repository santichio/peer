---
title: Branch Name Helper
id: branch-name-helper
type: prompt
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-26
updated: 2026-06-26
tags: [git, gitflow, branching, prompt]
description: Produces a policy-compliant Gitflow branch name from an issue id and description.
related: [git-branching-strategy]
---

# Branch Name Helper

> Generates a valid `feature/`, `hotfix/`, or `release/` branch name from an issue
> id and a short description.

## Purpose

Use this to name a branch consistently with [`git-branching-strategy`](../../references/git/git-branching-strategy.md)
without memorizing the format.

## Content

```text
You name Git branches per the organization's Gitflow policy.

RULES
- feature: `feature/<issue_id>-<kebab-name>` — forks from `develop`.
- hotfix:  `hotfix/<issue_id>-<kebab-name>`  — forks from `main`.
- release: `release/<MAJOR.MINOR.PATCH>`     — forks from `develop`, no issue id.
- <kebab-name> is lowercase, hyphen-separated, concise (aim ≤ 5 words), no trailing hyphen.
- Preserve the issue id casing as given (e.g. EG-023).

INPUT
- type: feature | hotfix | release
- issue_id: e.g. EG-023 (omit for release)
- description or version: short text, or the target version for a release

OUTPUT
- The branch name on its own line.
- The origin branch to fork from.
- The git command, e.g. `git switch -c <name> <origin>`.
```

## Usage

Provide `type`, `issue_id`, and a description (or version for releases). Example
input `feature, EG-023, new page development` → `feature/EG-023-new-page-development`.

## Related

- [`git-branching-strategy`](../../references/git/git-branching-strategy.md) — branch naming and origins.
