---
title: Tech Stack — DevOps
id: tech-stack-devops
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-27
updated: 2026-06-27
tags: [tech-stack, devops, docker, kubernetes, helm, github-actions]
description: DevOps toolchain — GitHub, GitHub Actions, NPM, Docker, Kubernetes, and Helm.
related: [tech-stack-overview]
---

# Tech Stack — DevOps

> The DevOps toolchain automates the lifecycle from code commit to production deployment.

## Purpose

Use this when setting up CI/CD, containerization, or deployment. Cross-cutting rules
are in the [overview](tech-stack-overview.md).

## Content

| Concern | Tool |
| --- | --- |
| Version control | GitHub |
| CI/CD | GitHub Actions |
| Package manager | NPM |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Deployment management | Helm Charts |

Production deployment uses **Helm** to manage **Docker** images and **Kubernetes**
configurations, with **GitHub Actions** driving the CI/CD pipeline.

## Related

- [`tech-stack-overview`](tech-stack-overview.md) — criteria, cross-cutting standards, glossary.
