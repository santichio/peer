# `peer/context.md` — schema

`peer/context.md` is the per-repo configuration the `peer-intake` skill reads
to know **which GitHub Project** to pull from and **how to describe the
product** in every PRD it generates. One file, one repo, checked into source
control alongside the project it describes.

It has two parts:

- **YAML frontmatter** — strictly typed coordinates and output settings.
- **Markdown body** — free-form product context. Audience, tone, stack
  conventions, program-level non-goals. The intake skill prefixes this to its
  drafting context for every task, so anything you write here biases every
  PRD generated from this backlog.

## Field reference

| Path | Required | Type | Meaning |
| --- | --- | --- | --- |
| `github.owner` | yes | string | The user or organization that owns the GitHub Project (e.g. `santichio`). |
| `github.repo` | optional | string | Repository name. Only set if you want issue-hydration limited to one repo; omit for organization-wide projects. |
| `github.project_number` | yes | integer | The Projects v2 number from the project URL (`github.com/<owner>/projects/<N>`). |
| `github.status_field` | yes | string | Display name of the single-select status field on the project (e.g. `Status`). The skill matches this name literally. |
| `github.todo_value` | yes | string | The option value that means "ready for PRD" (e.g. `To Do`, `Ready`, `Backlog ✅`). Matched literally — copy it exactly as it appears in the project. |
| `prd.output_dir` | optional | string | Directory PRDs are written to. Default `peer/prd`. Relative to repo root. |
| `prd.filename_pattern` | optional | string | Filename template. Default `{issue_number}-{slug}.md`. Tokens: `{issue_number}`, `{slug}`, `{short_id}` (first 7 chars of the project item id, used for draft items with no linked issue). |

### Status-field lookup, in detail

GitHub Projects v2 exposes each project field by its **display name**. The intake
skill lists items with the GitHub MCP tool `projects_list` (its
`list_project_items` operation) and reads each item's single-select **status**
field named by `status_field`, comparing its value against `todo_value`
**literally**. Match the exact string, including case and any emoji.

If you renamed the status field (e.g. `Stage`), set `status_field: Stage`.
If your "To Do" option is labelled with an emoji (e.g. `📋 To Do`), set
`todo_value: "📋 To Do"` — copy the exact glyph.

## Paste-ready template

Save this as `peer/context.md` at the repo root and fill in the placeholders:

```markdown
---
github:
  owner: <github-user-or-org>
  repo: <repo-name>             # optional
  project_number: <N>
  status_field: Status
  todo_value: "To Do"
prd:
  output_dir: peer/prd
  filename_pattern: "{issue_number}-{slug}.md"
---

# Product context

<!-- One paragraph: what is this product, who uses it, what problem does it solve. -->

## Primary users

<!-- Bullet list of personas. Concrete role + context. -->

## Program-level non-goals

<!-- Things the product as a whole will not do. These bias every PRD's Non-Goals section. -->

## Conventions to respect

<!-- Tech stack, framework choices, terminology, naming conventions, tone.
     Anything you'd otherwise have to repeat in every PRD's Technical Considerations. -->
```

## Why this file lives in `peer/` (not the repo root)

`peer/` collects every artifact the `peer-*` skills produce or consume:
`context.md` here, generated PRDs under `prd/`, future skills may add more.
Keeping the convention scoped to one directory makes the contract obvious to
collaborators and easy to `.gitignore` selectively (e.g. ignore
`peer/prd/draft-*` but commit reviewed PRDs).

## Changing the schema

This schema is owned by the `peer-intake` skill. If you find yourself wanting a
new field (e.g. an `assignee_filter`, a `priority_field`), prefer adding it to
the existing `github:` or `prd:` blocks rather than introducing a new top-level
key — that keeps the parser simple and the contract stable.
