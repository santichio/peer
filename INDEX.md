# Index

Hand-maintained catalog of every document in this repo. **Update this file whenever
a document is added, renamed, or deprecated.** Each entry's description is copied
from the document's `description` metadata.

> See [README.md](README.md) for the document standard and contribution steps.

## Skills

Skills follow the [SKILL.md format](skills/skill-creator/SKILL.md) (folder per skill,
`name` + `description` frontmatter), so they carry no `version`/`status` — shown as `—`.
Bundled prompts, agents, references, and scripts live inside each skill folder and are
not listed separately.

| Name | Title | Version | Status | Description |
| --- | ----- | ------- | ------ | ----------- |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Skill Creator | — | — | Create new skills, modify and improve existing skills, and measure skill performance with evals. |
| [`gitflow`](skills/gitflow/SKILL.md) | Gitflow Workflow | — | — | Drive a code change end-to-end through gitflow using git and the GitHub CLI; stops at PR-ready. |
| [`prd`](skills/prd/SKILL.md) | PRD Generator | — | — | Generate a Product Requirements Document for a new feature. |
| [`ralph`](skills/ralph/SKILL.md) | Ralph PRD Converter | — | — | Convert a PRD to the prd.json format for the Ralph autonomous agent system. |
| [`peer-intake`](skills/peer-intake/SKILL.md) | Peer Backlog Intake | — | — | Convert GitHub Project 'To Do' tasks into standardized PRDs under peer/prd/. |

## Templates

| ID  | Title | Version | Status | Description |
| --- | ----- | ------- | ------ | ----------- |
| [`base-document`](templates/base-document.md) | Base Document Template | 1.0.0 | active | The canonical template every document in this repo copies from. |

## Automation

Reusable CI workflows, their consumer documentation, and CI helper scripts. Workflows
are YAML — they aren't versioned the same way docs are, so version/status show as `—`.

| Name | Path | Version | Status | Description |
| ---- | ---- | ------- | ------ | ----------- |
| `sync-skills` | [.github/workflows/sync-skills.yml](.github/workflows/sync-skills.yml) | — | — | Reusable `workflow_call` workflow that syncs `skills/<name>/` from this repo into a consumer's destination directory. |
| [`sync-skills-action`](.github/workflows/sync-skills-action.md) | .github/workflows/sync-skills-action.md | 1.0.1 | active | Consumer guide for the reusable sync-skills GitHub Action — inputs, examples, pinning, and troubleshooting. |
| `lint-skills` | [.github/workflows/lint-skills.yml](.github/workflows/lint-skills.yml) | — | — | CI workflow that validates every `skills/<name>/SKILL.md` has valid frontmatter and a matching `name`. |
| `lint-skill.py` | [.github/scripts/lint-skill.py](.github/scripts/lint-skill.py) | — | — | Python helper that validates one `SKILL.md` file; invoked by `lint-skills`. |

## References

Top-level references not yet folded into a specific skill. The repo's long-term
direction is to bundle these inside the skill that consumes them; entries here are
candidates for future relocation or removal.

| ID  | Title | Version | Status | Description |
| --- | ----- | ------- | ------ | ----------- |
| [`tech-stack-overview`](references/engineering/tech-stack-overview.md) | Tech Stack Overview | 1.0.0 | active | Selection criteria, cross-cutting standards, and architecture for the standard application stack. |
| [`tech-stack-frontend`](references/engineering/tech-stack-frontend.md) | Tech Stack — Front-end | 1.0.0 | active | Front-end stack — TanStack framework, PandaCSS + PostCSS styling, and Storybook. |
| [`tech-stack-backend`](references/engineering/tech-stack-backend.md) | Tech Stack — Back-end | 1.0.0 | active | Back-end stack — NestJS + Fastify microservices, Kafka messaging, Jest, and Prisma ORM. |
| [`tech-stack-database`](references/engineering/tech-stack-database.md) | Tech Stack — Database & Documentation | 1.0.0 | active | Data layer — PostgreSQL, Firestore real-time, Redis cache, and Mermaid diagrams-as-code. |
| [`tech-stack-devops`](references/engineering/tech-stack-devops.md) | Tech Stack — DevOps | 1.0.0 | active | DevOps toolchain — GitHub, GitHub Actions, NPM, Docker, Kubernetes, and Helm. |
| [`code-style`](references/engineering/code-style.md) | Code Style — ESLint & Prettier | 1.0.0 | active | The preferred ESLint + Prettier configuration for Node.js / TypeScript projects. |
