---
title: Tech Stack — Database & Documentation
id: tech-stack-database
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-27
updated: 2026-06-27
tags: [tech-stack, database, postgresql, firestore, redis, mermaid]
description: Data layer — PostgreSQL, Firestore real-time, Redis cache, and Mermaid diagrams-as-code.
related: [tech-stack-overview, tech-stack-backend]
---

# Tech Stack — Database & Documentation

> The data layer focuses on reliability, real-time capabilities, and clear schema
> documentation.

## Purpose

Use this when choosing where data lives or how to document schemas. Cross-cutting
rules are in the [overview](tech-stack-overview.md).

## Content

### Primary database: PostgreSQL

- The source of truth for all business data; chosen for robustness and SQL compliance.

### Real-time database: Google Firebase (Firestore)

- For features requiring real-time data synchronization (live order tracking, chat,
  notifications). Its NoSQL nature pushes data instantly to connected clients.

### Cache: Redis

- Caches frequently accessed data to optimize performance.

### Documentation: Mermaid

- Diagrams-as-code (ERD, flowcharts) directly within the documentation, so database
  structures and flows are easily maintained and versioned.

## Related

- [`tech-stack-overview`](tech-stack-overview.md) — criteria, cross-cutting standards, glossary.
- [`tech-stack-backend`](tech-stack-backend.md) — services and Prisma ORM that access these stores.
