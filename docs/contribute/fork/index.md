> This document defines recommended fork strategies for companies contributing to S-CORE. It is public, vendor-neutral and evolves with community feedback.

# Fork Strategy for the S-CORE Organization

## 1. Purpose & Audience

This guide helps companies (tool vendors, integrators, OEMs, suppliers) decide how to structure forks of S-CORE repositories to:

- Contribute efficiently upstream
- Integrate internal compliance / security workflows
- Keep proprietary or distribution-specific assets separate
- Avoid accidental leakage of secrets or internal IP
- Automate promotion of reviewed code to the public community

> S-CORE spans 50+ repositories. You DON'T need a one-size-fits-all approach. Pick the minimal model per repository and evolve when needs grow.

## 2. Models & Decision Framework

### 2.1 Core Models (At a Glance)
| Model | When to use | Pros | Constraints |
|-------|-------------|------|-------------|
| Single Public Fork (individual or shared org) | Early exploration, doc fixes, small features | Fast, zero internal infra needed | No internal CI with secrets, no private adaptations |
| Dual Fork (Internal + Public) | Compliance gates, internal packaging, secret-backed tests | Separation of concerns, audit trail, safe reviews | Needs automation & policy, slight latency |
| Internal Mirror Only (read-only) | Passive consumers tracking upstream state | Simplifies dependency pinning | Not for contributing unless paired with public fork |
| Transformation/Pub Pipeline (Copybara etc.) | Need to filter files / rewrite metadata | Powerful, auditable, repeatable | Extra tooling & maintenance |

Recommendation: Most corporate contributors benefit long-term from the Dual Fork model (Internal authoritative workspace + Public publishing fork).

### 2.2 Decision Checklist
Answer these to pick a starting model:
1. Secrets / licenses in tests? → Internal fork needed.
2. Proprietary integration code? → Internal fork.
3. Only docs / small fixes? → Start public-only.
4. Need audit-grade traceability? → Internal-first promotion.
5. Need file filtering / rewriting? → Add transformation pipeline.

## 3. Roles, Topology & Branching

### 3.1 Roles & Responsibilities
| Role | Owns | Responsibilities |
|------|------|------------------|
| Upstream (eclipse-score/*) | Canonical open source history | Reviews public PRs, enforces project guidelines |
| Company Internal Repo | Integration & gated development | Compliance scans, secret-backed CI, internal code retention |
| Public Company Fork | Clean staging for upstream PRs | Holds publish-ready feature branches only |
| Automation (Bot / App) | Sync & publish operations | Keeps mirrors up to date, strips internal-only assets |

### 3.2 Repository & Branch Topology
Internal Repository (authoritative workspace):
- Mirrors (FF-only): `upstream/main`, `upstream/release/*`
- Integration branches: `internal/main`, `internal/release/*`
- Features: `internal/feat/<topic>`
- Optional support: `support/<customer|version>`

Public Fork (minimal surface):
- Short-lived `feature/<topic>` branches only
- No secrets, internal configs, or generated artifacts

Naming Guidance:
- Lower-case, hyphen or slash separated
- Avoid internal ticket IDs in public branch names

## 4. Workflows & Promotion

### 4.1 Public-First (Simple)
1. Fork → branch `feature/<topic>` → develop → PR → merge → delete.
Use When: No secrets, fast iteration, minimal process.

### 4.2 Internal-First (Regulated / Commercial)
1. Fast-forward internal mirror
2. Branch `internal/feat/<topic>`
3. Internal CI & compliance
4. (Optional) Tag snapshot
5. Rebase & publish sanitized branch to public fork `feature/<topic>`
6. Open upstream PR
7. After merge, sync back & reconcile

### 4.3 Transformation / Filtering Layer
Add (Copybara / custom) only if filtering / rewriting is required.

### 4.4 Sync & Promotion Mechanics
Essentials:
- Avoid routine `git push --mirror` after seeding
- Upstream → Internal: controlled fast-forward
- Internal → Public: audited promotion

Initial Seed:
```bash
git clone https://github.com/eclipse-score/<repo>.git upstream_tmp
git clone git@github.com:your-org/<repo>_internal.git internal
cd internal
git remote add upstream ../upstream_tmp/.git
git fetch upstream
git push origin refs/remotes/upstream/main:refs/heads/upstream/main
```

Fast-Forward Sync:
```bash
git fetch upstream main
git checkout upstream/main
git reset --hard upstream/main
git push origin HEAD:upstream/main
```

Promotion (example):
```bash
git fetch upstream main
git checkout internal/feat/my-topic
git rebase upstream/main
git push public HEAD:feature/my-topic --force-with-lease
```

## 5. CI, Compliance & Governance

### 5.1 Separation of Checks
| Check Type | Internal Repo | Public Fork | Upstream PR |
|------------|---------------|-------------|-------------|
| License / key-based tests | Yes | No | No |
| Deep security scanning | Yes | Optional summary | Project policy |
| Lint / format / unit tests | Yes | Yes | Yes |
| Binary provenance / SBOM | Yes | No (sanitized) | Optional attachment |

Best Practice: Re-run a secret-free subset publicly.

### 5.2 Governance Artifacts (Internal)
- Fork Ownership Matrix
- Data Classification Matrix
- Promotion Checklist
- Exception / Override Log

## 6. Automation & Tooling

### 6.1 GitHub App (Scoped Token) Publisher
Example action step:
```yaml
- name: App Token
  id: app_token
  uses: tibdex/github-app-token@v2
  with:
    app_id: ${{ secrets.FORK_PUBLISHER_APP_ID }}
    private_key: ${{ secrets.FORK_PUBLISHER_APP_KEY }}
```
Push published branch:
```bash
git push "https://x-access-token:${TOKEN}@github.com/your-org/<repo>.git" HEAD:feature/my-topic
```

### 6.2 Copybara (Advanced)
Minimal illustrative config:
```python
origin = git.origin(url = "git@github.com:your-org/<repo>_internal.git", ref = "internal/feat/my-topic")
destination = git.destination(url = "git@github.com:your-org/<repo>.git", push = "refs/heads/feature/my-topic")
core.workflow(
  name = "publish_feature",
  mode = "ITERATIVE",
  origin = origin,
  origin_files = glob(["**"], exclude=["internal_scripts/**", "docs/internal/**"]),
  destination = destination,
  authoring = authoring.pass_thru("Your Bot <bot@your-org.example>")
)
```

### 6.3 Lightweight Alternative
Shell + rsync + sanitize script; upgrade to Copybara when complexity grows.

## 7. Security & Risk Management

| Risk | Mitigation |
|------|------------|
| Secret leakage | Pre-publish scan (regex + entropy), allow-list, CI fail on match |
| Overwritten mirrors | Protect `upstream/*`; automation-only pushes |
| Branch drift | Enforce rebase window; stale report bot |
| Untracked manual promotions | All promotions via workflow logging SHA mapping |
| Internal-only files published | Classification list + deny/allow checks |

## 8. Adoption Roadmap & Metrics

### 8.1 Incremental Adoption
1. Public fork → first PRs
2. Add internal mirror for key repos
3. Add internal CI & scans
4. Formalize branch protections
5. Automate promotion (GitHub App)
6. Introduce transformation pipeline (if needed)
7. Add dashboards (latency, drift, scan health)

### 8.2 Operational Metrics
- Median: internal ready → PR opened
- Rebase drift (commit delta at promotion)
- Secret scan FP / TP ratio
- Promotion failure categories
- Feature branch upstream merge rate

## 9. Reference (Cheat Sheet, FAQ, Glossary)

### 9.1 Quick Commands
```bash
# Sync upstream into internal mirror
git fetch upstream main
git push origin refs/remotes/upstream/main:refs/heads/upstream/main

# Start feature (internal)
git checkout -b internal/feat/my-topic upstream/main

# Rebase before publish
git rebase upstream/main

# Publish sanitized branch
git push public HEAD:feature/my-topic --force-with-lease
```

### 9.2 FAQ
**Do we need two forks for every repo?** Only where internal integration or compliance adds value.

**Can engineers push directly to the public fork?** Yes (Public-First). In Internal-First restrict to automation.

**How do we handle hotfixes?** Branch from upstream tag internally → fix → publish → PR → backport.

**How to keep authorship?** Avoid unnecessary squashes; use iterative promotion.

**How to remove internal-only files?** Allow-list publishable paths; fail build on unclassified additions.

### 9.3 Glossary
- Promotion: Moving vetted internal branch to public fork for PR.
- Mirror: Fast-forward copy of upstream branch internally.
- Sanitization: Removing / transforming internal-only content before publishing.
- Drift: Commits difference between upstream main and working branch.

## 10. Summary

Start simple; add structure only as risk and scale justify it. A disciplined Dual Fork plus automated promotion balances safety, compliance, and upstream velocity.

Contributions to improve this guide are welcome—open a PR with additional patterns or automation examples.
