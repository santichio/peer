---
title: Git Repository Standards
id: git-repository-standards
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-26
updated: 2026-06-26
tags: [git, policy, repository, naming]
description: Naming conventions and baseline requirements for creating Git repositories.
related: [git-branching-strategy, git-commit-conventions, git-code-review, git-versioning-releases]
---

# Git Repository Standards

> Naming conventions and baseline requirements for creating and configuring Git repositories.

## Purpose

Use this when **creating a new repository** or auditing an existing one. It defines
the prefix-based naming scheme and the minimum files every repository must contain.

## Content

### Creation rules

- All new repositories must be created through the organization's central Git platform administration process.
- Names follow `prefix-name`: a prefix indicating purpose, then a concise, descriptive name (e.g. `service-payment-processor`, `web-customer-portal`).
- The `name` portion is kebab-case, concise, and descriptive of the repository's function.

### Prefix catalog

| Category | Prefix | Use for |
| --- | --- | --- |
| Applications & services | `app-` | Standalone application codebase (mobile app, executable software) |
| | `api-` | Standalone API codebase |
| | `service-` | Microservice codebase |
| Infrastructure & deployment | `infra-` | CI/CD pipelines, IaC files, build scripts |
| | `chart-` | Charts codebase (Helm, Argo) |
| Reusable components | `lib-` | Library reusable by other projects |
| | `pack-` | Generic reusable code parts that can't run/build alone (e.g. webpack) |
| Specialized | `script-` | Scripts codebase |
| | `etl-` | ETL services codebase |
| | `web-` | Web-based application (webpage, portal, blog) |
| Documentation | `docs-` | Documentation repository |
| | `oas-` | OpenAPI (OAS) specification — DSL or raw file(s); suffix with the API repo name |
| | `template-` | Template repositories |

### Baseline requirements

- A `README.md` explaining the project's purpose, setup instructions, and primary contributors.
- A `.gitignore` appropriate for the technology stack.
- Private repositories for all internal projects; public repositories require explicit approval from the security team.

## Related

- [`git-branching-strategy`](git-branching-strategy.md) — branches that must exist at creation time.
- [`git-versioning-releases`](git-versioning-releases.md) — required `CHANGELOG.md`.
