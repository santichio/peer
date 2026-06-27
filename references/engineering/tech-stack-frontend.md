---
title: Tech Stack — Front-end
id: tech-stack-frontend
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-27
updated: 2026-06-27
tags: [tech-stack, frontend, tanstack, pandacss, storybook]
description: Front-end stack — TanStack framework, PandaCSS + PostCSS styling, and Storybook.
related: [tech-stack-overview, code-style]
---

# Tech Stack — Front-end

> The front-end architecture, built on the TanStack ecosystem for type safety,
> performance, and modern state management.

## Purpose

Use this when building or reviewing front-end code. It defines the framework,
styling, and component-documentation choices. Cross-cutting rules (Node/TS, lint)
are in the [overview](tech-stack-overview.md).

## Content

### Framework: TanStack

- Uses the TanStack suite (Query, Router, etc.) as the core framework foundation.
- First-class TypeScript support, efficient data fetching, and robust routing for
  complex applications.

### Styling: PandaCSS with PostCSS

- **PandaCSS** — a build-time CSS-in-JS solution: the developer experience of dynamic
  styling with the performance of static CSS.
- **PostCSS** — processes styles for browser compatibility and optimization.

### Component documentation: Storybook

- Documents and registers UI components, ensuring a consistent visual library.
- Facilitates white-label theming and reuse across the application.

## Related

- [`tech-stack-overview`](tech-stack-overview.md) — criteria, cross-cutting standards, glossary.
- [`code-style`](code-style.md) — mandatory ESLint + Prettier setup.
