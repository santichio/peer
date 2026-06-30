---
title: Git Versioning & Releases
id: git-versioning-releases
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-26
updated: 2026-06-26
tags: [git, policy, semver, releases, changelog]
description: Semantic Versioning, Git tags, release management, and CHANGELOG.md maintenance.
related: [git-branching-strategy, git-commit-conventions]
---

# Git Versioning & Releases

> Version numbering, tagging, release management, and changelog rules for all repositories.

## Purpose

Use this when **cutting a release**, **tagging**, or **updating a changelog**. It
defines the SemVer scheme and the release process tied to the branching strategy.

## Content

### Semantic Versioning

All projects follow [SemVer 2.0.0](https://semver.org/): `MAJOR.MINOR.PATCH` (e.g. `1.4.2`).

| Segment | Increment when | Example |
| --- | --- | --- |
| MAJOR | Incompatible API / significant breaking changes | `1.4.2 → 2.0.0` |
| MINOR | New backward-compatible functionality | `1.4.2 → 1.5.0` |
| PATCH | Backward-compatible bug fixes or small improvements | `1.4.2 → 1.4.3` |

Pre-releases use a hyphen and identifiers (`1.0.0-alpha.1`, `2.3.0-beta.2`); build
metadata uses a plus sign (`1.0.0+20230501`).

### Git tags

- Format `v{SemVer}` — e.g. `v1.4.2`.
- Created from `main` after release branches merge.
- Include detailed release notes summarizing changes since the previous release.
- Signed by the release manager when applicable.
- Never deleted or moved once pushed. To withdraw a release, ship a new one that fixes the issue.

### Release process

1. Cut `release/<version>` from `develop` (e.g. `release/1.5.0`).
2. Run final testing, documentation updates, and version-number adjustments on the release branch.
3. Merge the release branch into both `main` and `develop`.
4. Tag the release point on `main`.
5. Generate release artifacts from the tagged commit.
6. Publish release notes: features, improvements, fixes, and breaking changes.

### CHANGELOG.md

Every repository keeps a `CHANGELOG.md` in its root that:

- Is ordered by version, newest first.
- Categorizes changes as **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, or **Security**.
- References relevant issue / PR numbers.
- Clearly marks breaking changes.
- Is updated with each release.

> Note: this describes the root `CHANGELOG.md` of a **software** repository (one file,
> Keep a Changelog style). Documentation repositories sometimes apply the same style
> but keep one `CHANGELOG.md` per top-level directory, grouped by document id; the
> Keep-a-Changelog format itself is identical either way.

### Version alignment

Related microservices/components that form one logical release should share aligned
version numbers to simplify dependency management, compatibility, and holistic testing.

### Automated versioning

Where possible, derive version bumps from Conventional Commit history. For TypeScript
/ Node.js, `standard-version` or `semantic-release` are recommended.

## Related

- [`git-commit-conventions`](git-commit-conventions.md) — commit types that drive automated SemVer bumps.
- [`git-branching-strategy`](git-branching-strategy.md) — branches releases are cut from and tagged on.
