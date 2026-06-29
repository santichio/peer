---
title: Git Commit Conventions
id: git-commit-conventions
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-26
updated: 2026-06-26
tags: [git, policy, commits, conventional-commits]
description: Conventional Commits structure, the allowed type library, scope, and description rules.
related: [git-branching-strategy, git-versioning-releases, commit-message-writer]
---

# Git Commit Conventions

> All commits, on all branches, follow Conventional Commits v1.0.0.

## Purpose

Use this when **writing a commit message**. It defines the required structure, the
allowed commit types, scope rules, and how descriptions must be phrased.

## Content

### Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

- **Header** — mandatory single line summarizing the change, max 50 characters.
- **Body** — optional detailed explanation, separated from the header by a blank line.
- **Footer** — optional; references issue trackers, breaking changes, or contributors.

A breaking change is signalled by a `!` after the type/scope **or** a `BREAKING CHANGE:`
footer, and correlates with a `MAJOR` version bump. Other footers follow the git
trailer format.

### Type library

| Type | Use for | SemVer |
| --- | --- | --- |
| `feat` | A new feature | MINOR |
| `fix` | A bug fix | PATCH |
| `build` | Build files and dependencies | — |
| `chore` | Build/admin config, package tasks (no code change) | — |
| `ci` | Continuous integration changes | — |
| `docs` | Documentation only (no code change) | — |
| `style` | Formatting, whitespace, visual-only changes | — |
| `refactor` | Code change that keeps behavior (incl. perf from review) | — |
| `perf` | Performance-related code changes | — |
| `test` | Adding/modifying/deleting tests (no code change) | — |
| `revert` | Revert a previous commit; body: `This reverts commit <hash>.` | — |

### Scope

Optional, a noun in parentheses naming a section of the codebase — e.g. `fix(parser):`.
Common scopes: UI components (`button`, `form`), backend services (`auth`, `api`, `db`),
config areas (`webpack`, `docker`, `k8s`), or features (`login`, `checkout`).

### Description rules

- Imperative, present tense ("change", not "changed"/"changes").
- Do not capitalize the first letter.
- Do not end with a period.
- Communicate the change without assuming prior context.

### Atomicity

Each commit is one logical change. Break large changes into a series of smaller
atomic commits — this improves reviews, history, troubleshooting, rollbacks, and cherry-picking.

## Usage

Good:

```
feat(auth): implement OAuth2 authentication flow
fix(payment): resolve transaction timeout error
docs(api): document rate-limit headers
refactor(db): speed up user search query
test(checkout): cover discount calculation
```

Avoid: `Fixed bug`, `Updated code`, `WIP`, `Made changes requested in PR`.

## Related

- [`commit-message-writer`](../../prompts/git/commit-message-writer.md) — prompt that drafts messages to this spec.
- [`git-versioning-releases`](git-versioning-releases.md) — how `feat`/`fix`/`BREAKING CHANGE` map to SemVer.
