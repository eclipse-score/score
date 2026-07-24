# AI Agent Extension Guide — eclipse-score

This document defines the rules for extending AI agent context across all eclipse-score
repositories. Read this before adding any agent customization file.

## Guiding Principles

1. **Single point of truth** — never duplicate information that already exists in code or
   docs. Agent files *point* to sources; they do not repeat them.
2. **Minimal always-on context** — `AGENTS.md` carries only what an agent cannot infer
   from reading the repo. Everything else is on-demand.
3. **Portability** — prefer `.agents/` for cross-tool assets (Copilot, Claude Code,
   Codex, ...). Use `.github/` only for Copilot-specific primitives.

## What goes where

| Asset | Location | Auto-loaded? | Cross-tool? |
|-------|----------|-------------|-------------|
| Repo overview, key facts | `AGENTS.md` (root) | ✅ always | ✅ |
| Module-specific skills | `<module>/.agents/skills/<name>/` | on-demand | ✅ |
| File-scoped coding rules | `.github/instructions/<name>.instructions.md` | via `applyTo` | Copilot only |
| Custom agent personas | `.github/agents/<name>.agent.md` | user-invoked | Copilot only |
| Slash-command prompts | `.github/prompts/<name>.prompt.md` | user-invoked | Copilot only |
| Reference data (IDs, snippets) | `.github/docs/` or `.agents/docs/` | on-demand | depends |

## Hierarchy Between Repos

When working across multiple repos (e.g. `score` + `persistency`):

- **`score/AGENTS.md`** provides org-wide context
- **`<module>/AGENTS.md`** provides module-specific context, references score for the rest
- Module `AGENTS.md` must include:
  ```
  > When working in this repo alongside score, score/AGENTS.md is also active.
  > For standalone use, see: https://github.com/eclipse-score/score/blob/main/AGENTS.md
  ```

## Recommended AGENTS.md Structure

```markdown
# <org>/<repo> — Agent Context

> <standalone note referencing score/AGENTS.md>

<one-line description of the repo's role>

## Key Facts

## Conventions

## On-Demand References
| Topic | File |
|-------|------|
| ...   | ...  |
```

Use `## Conventions` for any rule that changes how an agent should behave — preferred
tools, things to never do, required checks before certain actions. Do not put behavioral
rules in `## Key Facts`.

## Adding a New Skill

1. Create folder: `.agents/skills/<skill-name>/SKILL.md` in the module repo
2. Required frontmatter:
   ```yaml
   ---
   name: skill-name          # must match folder name, lowercase-hyphenated
   description: 'What it does. Use when: ... triggers ...'
   ---
   ```
3. Keep `SKILL.md` under 500 lines; put detail in `./references/` subfolder
4. Do not vendor a skill that already exists in `score/.agents/skills/`

## Adding a New Instruction (Copilot only)

1. Place in `.github/instructions/<name>.instructions.md`
2. Use `applyTo` for file-scoped rules (e.g. `applyTo: "**/*.rs"`)
3. Use `description:` for on-demand task rules (e.g. safety review checklist)
4. Never use `applyTo: "**"` unless truly universal — it loads on every request

## Adding Reference Documentation

- GitHub API IDs, GraphQL snippets, external system IDs → `.github/docs/`
- Anything an agent needs to *act* (procedures, runbooks) → `.agents/docs/`
- Link from `AGENTS.md` — do not repeat content inline

The same rules apply to any domain: git conventions, CI/CD runbooks, release procedures, etc.
If a topic is **org-wide**, the reference doc lives in `score/` and module repos link to it.
If a topic is **module-specific**, the doc lives in the module repo and may reference the score doc for shared context.

When adding a new reference doc:

1. Decide scope: org-wide → `score/`, module-specific → `<module>/`
2. Decide type: static IDs / external data → `.github/docs/`, agent procedures / runbooks → `.agents/docs/`
3. Link to it from `AGENTS.md` under an **On-Demand References** table
4. If a module doc extends an org-wide one, reference the score doc rather than duplicating content

## Module Repo Checklist

When setting up a new module repo for agent use:

- [ ] `AGENTS.md` at repo root with: FT discussion number → score, ASIL level →
      `project_config.bzl`, `reference_integration` relationship
- [ ] `.agents/skills/` — only module-specific skills (created when needed)
- [ ] `.agents/docs/` — module-specific runbooks/procedures (created when needed)
- [ ] `.github/docs/` — module-specific reference data, e.g. `score_github_api.md` (created when needed)
- [ ] `.github/instructions/` — Copilot-only scoped rules (created when needed)
- [ ] `.github/agents/` — Copilot-only custom agents (created when needed)
- [ ] `.github/prompts/` — Copilot-only prompts (created when needed)
