---
title: Code Style — ESLint & Prettier
id: code-style
type: reference
version: 1.0.0
status: active
owner: gabriel@santich.io
created: 2026-06-27
updated: 2026-06-27
tags: [code-style, eslint, prettier, typescript, standards]
description: The preferred ESLint + Prettier configuration for Node.js / TypeScript projects.
related: [tech-stack-overview, tech-stack-frontend, tech-stack-backend]
---

# Code Style — ESLint & Prettier

> The preferred lint and format configuration for the Node.js / TypeScript stack.
> ESLint and Prettier are [mandatory](tech-stack-overview.md#cross-cutting-standards).

## Purpose

Use this when setting up a new project or aligning an existing one. Copy the two
configuration files verbatim, then install the referenced dev dependencies.

## Content

### `eslint.config.mjs`

```mjs
// @ts-check
import eslint from '@eslint/js';
import eslintPluginPrettierRecommended from 'eslint-plugin-prettier/recommended';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  {
    ignores: ['eslint.config.mjs'],
  },
  eslint.configs.recommended,
  ...tseslint.configs.recommendedTypeChecked,
  eslintPluginPrettierRecommended,
  {
    languageOptions: {
      globals: {
        ...globals.node,
        ...globals.jest,
      },
      ecmaVersion: 5,
      sourceType: 'module',
      parserOptions: {
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
  {
    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-floating-promises': 'warn',
      '@typescript-eslint/no-unsafe-argument': 'warn',
      '@typescript-eslint/no-unused-vars': ['error', {
        'argsIgnorePattern': '^_',
        'varsIgnorePattern': '^_',
        'caughtErrorsIgnorePattern': '^_'
      }]
    },
  },
);
```

### `.prettierrc`

```json
{
  "singleQuote": true,
  "trailingComma": "none",
  "semi": false,
  "tabWidth": 4
}
```

### Key choices

- **Type-checked linting** — extends `typescript-eslint`'s `recommendedTypeChecked`
  using `projectService`, so rules can reason about types.
- **Prettier as an ESLint rule** — `eslint-plugin-prettier/recommended` runs Prettier
  through ESLint, so formatting issues surface as lint errors.
- **Node + Jest globals** — both global sets are enabled for source and tests.
- **Unused vars** — error, but anything prefixed with `_` (args, vars, caught errors)
  is intentionally ignored.
- **Relaxed rules** — `no-explicit-any` is off; `no-floating-promises` and
  `no-unsafe-argument` are warnings rather than errors.
- **Formatting** — single quotes, no semicolons, no trailing commas, 4-space indent.

### Dependencies

Install as dev dependencies: `@eslint/js`, `typescript-eslint`,
`eslint-plugin-prettier`, `prettier`, `globals` (and `eslint` itself).

## Related

- [`tech-stack-overview`](tech-stack-overview.md) — where ESLint + Prettier are mandated.
- Layer docs: [front-end](tech-stack-frontend.md), [back-end](tech-stack-backend.md).
