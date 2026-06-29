---
title: Tech Stack — Back-end
id: tech-stack-backend
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-27
updated: 2026-06-27
tags: [tech-stack, backend, nestjs, fastify, kafka, prisma, jest]
description: Back-end stack — NestJS + Fastify microservices, Kafka messaging, Jest, and Prisma ORM.
related: [tech-stack-overview, tech-stack-database, code-style]
---

# Tech Stack — Back-end

> The back-end follows a microservice design pattern, using NestJS for structure and
> Kafka for asynchronous communication.

## Purpose

Use this when building or reviewing back-end services. It defines the framework,
server, configuration, API documentation, messaging, testing, and data-access
choices. Cross-cutting rules are in the [overview](tech-stack-overview.md).

## Content

### Main framework: NestJS

- Modular architecture that supports the microservice design.
- **Server:** [Fastify](tech-stack-overview.md#glossary) for high-performance HTTP processing.
- **Configuration:** a strict **Config Module** manages environment variables and
  white-label configurations.
- **API docs:** every service must provide **OpenAPI** specifications to ensure clear
  contract definitions.

### Messaging: Kafka

- Asynchronous communication between services, ensuring decoupling and resilience in
  the microservices architecture.

### Testing: Jest

- The standard testing framework for the stack — unit and integration tests for reliability.

### Data access: Prisma ORM

- Type-safe database client that simplifies data access and migrations, reducing
  runtime errors. See the [database](tech-stack-database.md) doc for the data stores.

## Related

- [`tech-stack-overview`](tech-stack-overview.md) — criteria, cross-cutting standards, glossary.
- [`tech-stack-database`](tech-stack-database.md) — the data stores Prisma and services use.
- [`code-style`](code-style.md) — mandatory ESLint + Prettier setup.
