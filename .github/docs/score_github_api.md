# Eclipse Score GitHub API Notes

Useful IDs and GraphQL snippets for automating tasks against the eclipse-score GitHub organization.

> **Repo-specific notes** (category IDs, discussion lists per feature team, etc.) live in the
> `.github/docs/score_github_api.md` of each respective repository and reference this file.

## Organization

- Login: `eclipse-score`
- Node ID: `O_kgDOCy9hXw`
- Org-level discussion URLs: `https://github.com/orgs/eclipse-score/discussions/<number>`
- Org discussions are physically stored in the **`eclipse-score/score`** repository

## Discussion Categories

| Feature Team | Category ID |
|--------------|-------------|
| Persistency FT | `DIC_kwDONP32A84ClSxX` |

## GraphQL Notes

> Org discussions are stored in `eclipse-score/score`, not under an org-level field.
> Use `repository(owner: "eclipse-score", name: "score") { discussions(...) }` — the intuitive
> `organization { discussions }` path does not exist in the GitHub GraphQL API.

```bash
gh api graphql -f query='
{
  repository(owner: "eclipse-score", name: "score") {
    discussions(first: 100, categoryId: "<CATEGORY_ID>") {
      nodes { number title closed id }
    }
  }
}'
```
