# Changelog — `references/`

All notable changes to documents in this directory. Based on
[Keep a Changelog](https://keepachangelog.com/); documents use [SemVer](https://semver.org/).
Entries are grouped by document `id`, newest version first.

## `sync-skills-action`

> **2026-06-30 — Moved.** Relocated to `.github/workflows/sync-skills-action.md`
> next to the workflow it documents. No content change; the doc is now adjacent
> to `sync-skills.yml`. Future entries for this id should be added to the repo-root
> `CHANGELOG.md` (no per-directory changelog at the new location).

### [1.0.1] — 2026-06-29
#### Changed
- Added a "How the sync works" section explaining the pull-based model, when consumers
  see updates, and how `ref` selects which commit of `peer` is read. Includes a
  `sequenceDiagram` of a single run.

### [1.0.0] — 2026-06-27
#### Added
- Consumer guide for the reusable `sync-skills` GitHub Action: inputs table, scheduled
  and on-demand examples, pinning strategy, mode comparison, and troubleshooting.

## `tech-stack-overview`

### [1.0.0] — 2026-06-27
#### Added
- Selection criteria, white-label note, cross-cutting standards, a Mermaid
  architecture diagram, and the consolidated glossary.

## `tech-stack-frontend`

### [1.0.0] — 2026-06-27
#### Added
- Front-end stack: TanStack framework, PandaCSS + PostCSS styling, Storybook.

## `tech-stack-backend`

### [1.0.0] — 2026-06-27
#### Added
- Back-end stack: NestJS + Fastify, Config Module, OpenAPI, Kafka, Jest, Prisma ORM.

## `tech-stack-database`

### [1.0.0] — 2026-06-27
#### Added
- Data layer: PostgreSQL, Firestore real-time, Redis cache, Mermaid diagrams-as-code.

## `tech-stack-devops`

### [1.0.0] — 2026-06-27
#### Added
- DevOps toolchain: GitHub, GitHub Actions, NPM, Docker, Kubernetes, Helm.

## `code-style`

### [1.0.0] — 2026-06-27
#### Added
- Preferred ESLint + Prettier configuration (verbatim configs) with rationale.

## `git-repository-standards`

> **2026-06-30 — Moved.** Now bundled inside the `gitflow` skill at
> `skills/gitflow/references/git-repository-standards.md`. No content change.
> Future entries for this id should be logged in `skills/CHANGELOG.md` by date.

### [1.0.0] — 2026-06-26
#### Added
- Repository creation rules, the prefix catalog, and baseline file requirements.

## `git-branching-strategy`

> **2026-06-30 — Moved.** Now bundled inside the `gitflow` skill at
> `skills/gitflow/references/git-branching-strategy.md`. No content change.
> Future entries for this id should be logged in `skills/CHANGELOG.md` by date.

### [1.0.0] — 2026-06-26
#### Added
- Gitflow default/support branches, naming, and workflow; HTML tables replaced with
  GFM and a Mermaid `gitGraph` diagram.

## `git-commit-conventions`

> **2026-06-30 — Moved.** Now bundled inside the `gitflow` skill at
> `skills/gitflow/references/git-commit-conventions.md`. No content change.
> Future entries for this id should be logged in `skills/CHANGELOG.md` by date.

### [1.0.0] — 2026-06-26
#### Added
- Conventional Commits structure, the standard type library (with SemVer mapping),
  scope, description rules, and atomicity guidance. Header limit 50 characters.

## `git-code-review`

> **2026-06-30 — Moved.** Now bundled inside the `gitflow` skill at
> `skills/gitflow/references/git-code-review.md`. No content change.
> Future entries for this id should be logged in `skills/CHANGELOG.md` by date.

### [1.0.0] — 2026-06-26
#### Added
- Pull-request requirements, review criteria (GFM table), process, and feedback rules.

## `git-versioning-releases`

> **2026-06-30 — Moved.** Now bundled inside the `gitflow` skill at
> `skills/gitflow/references/git-versioning-releases.md`. No content change.
> Future entries for this id should be logged in `skills/CHANGELOG.md` by date.

### [1.0.0] — 2026-06-26
#### Added
- SemVer scheme, Git tags, release process, `CHANGELOG.md` rules, version alignment,
  and automated versioning.
