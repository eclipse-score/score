# eclipse-score/score — Agent Context

This is the **parent documentation and org-level repository** of the
[eclipse-score](https://github.com/eclipse-score) automotive middleware OSS project.
Feature implementations live in separate repos (e.g. `persistency`, `communication`,
`logging`, ...) as individual Bazel modules. This repo holds org-wide documentation,
process definitions, and contribution guidelines.

## Key Facts

- **Org discussions** are physically hosted in *this* repository even though they appear
  at `https://github.com/orgs/eclipse-score/discussions/`. Each feature team has its
  own discussion category.
- **`reference_integration`** is where all feature modules are integrated and tested
  end-to-end. Changes here that affect module APIs or process requirements may need to
  be reflected there.
- **Documentation toolchain**: Sphinx + sphinx-needs. RST files using `.. req::`,
  `.. spec::`, `.. needflow::` etc. carry formal requirements-traceability implications.
  Do not delete or rename need IDs — they may be referenced across repos.
- **Single point of truth rule**: never duplicate information that already exists in
  docs or code. AGENTS.md files point to sources; they do not repeat them.

## Conventions

- **GitHub queries**: always use `gh` CLI with GraphQL, never fetch discussion pages via browser/HTTP

## On-Demand References

| Topic | File |
|-------|------|
| GitHub org/API IDs, GraphQL snippets | `.github/docs/score_github_api.md` |
| Agent extension rules & how to add skills/instructions | `.agents/docs/extension_guide.md` |

## Agent Extension (this repo)

Generic skills shared across all module repos live in `.agents/skills/`.
Module-specific skills live in the respective repo's `.agents/skills/`.
See `.agents/docs/extension_guide.md` for the full rules.
