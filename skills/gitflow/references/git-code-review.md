---
title: Git Code Review Process
id: git-code-review
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-26
updated: 2026-06-26
tags: [git, policy, code-review, pull-request]
description: Pull-request requirements, review criteria, process, and feedback guidelines.
related: [git-branching-strategy, git-commit-conventions, pr-review-assistant]
---

# Git Code Review Process

> Standards for pull requests and code review before merging into protected branches.

## Purpose

Use this when **opening or reviewing a pull request**. It defines what a PR must
contain, the approval requirements, the criteria reviewers apply, and how to give feedback.

## Content

### Pull request creation

A PR should be focused on a single feature, fix, or improvement; large changes are
broken into smaller PRs. Open early and mark as **Draft** until ready for review.

Every PR must include:

- A descriptive title indicating the purpose of the changes.
- A detailed description: what the changes accomplish, why they're necessary, and key implementation details.
- References to related issue tickets or requirements.
- Screenshots or recordings for UI changes when applicable.
- Any special testing instructions or considerations.

### Review requirements

- Minimum one approval from a qualified reviewer; critical components may require two or more (per repository settings).
- Reviews completed within one business day; if longer, the reviewer communicates this to the author.
- Automated checks (linting, tests, builds) must pass before merge.
- Self-reviews are not permitted for production code — authors cannot approve their own PRs.

### Review criteria

| Aspect | Question the reviewer asks |
| --- | --- |
| Functionality | Does the code correctly implement the feature / fix the issue? |
| Architecture | Is the design sound and consistent with project patterns? |
| Code quality | Does it follow coding standards and best practices? |
| Performance | Will it perform efficiently under expected load? |
| Security | Any vulnerabilities or data-protection concerns? |
| Maintainability | Well-structured, self-documenting, easy to understand? |
| Test coverage | Appropriate unit / integration / e2e tests? |
| Documentation | Comments, inline, and external docs complete and clear? |

### Process

1. Author submits the PR and assigns reviewers based on requirements and code ownership.
2. Automated checks run.
3. Reviewers provide constructive feedback via comments.
4. Author addresses feedback or justifies the current implementation.
5. Reviewers re-review and approve when satisfied.
6. Author merges after required approvals.
7. The branch is deleted after merge.

### Feedback guidelines

Feedback should be **specific**, **actionable**, **prioritized** (required vs optional),
**constructive**, **educational**, and **timely**. Keep discussion professional and
focused on the code; technical leads make the final call when consensus can't be reached.

## Related

- [`pr-review-assistant`](../agents/pr-review-assistant.md) — agent that reviews a PR against these criteria.
- [`git-branching-strategy`](git-branching-strategy.md) — which branches require review before merge.
