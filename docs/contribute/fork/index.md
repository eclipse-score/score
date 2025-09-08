# Fork Strategy for the S-CORE Organization

> Single-page guide: purpose, fork models, and practical workflows.

- [Fork Strategy for the S-CORE Organization](#fork-strategy-for-the-s-core-organization)
  - [1. Purpose \& Context](#1-purpose--context)
    - [1.1 Audience](#11-audience)
    - [1.2 Goals](#12-goals)
    - [1.3 Out of Scope](#13-out-of-scope)
    - [1.4 Private vs Public Forks](#14-private-vs-public-forks)
    - [Public Fork](#public-fork)
    - [Internal Fork](#internal-fork)
    - [Hybrid (Both)](#hybrid-both)
  - [2. How To work with forks](#2-how-to-work-with-forks)
    - [Flow of a feature](#flow-of-a-feature)
      - [Opinionated Alternative: change main reference](#opinionated-alternative-change-main-reference)
  - [3. Hybrid Implementation](#3-hybrid-implementation)
    - [3.1 Public-first Workflow](#31-public-first-workflow)
    - [3.2 Internal-first Workflow](#32-internal-first-workflow)
      - [Workflow Overview](#workflow-overview)
    - [3.3 Transformation / Filtering Pipeline (Copybara Implementation)](#33-transformation--filtering-pipeline-copybara-implementation)
      - [Overview](#overview)
      - [Key Benefits](#key-benefits)
      - [Minimal Configuration Example](#minimal-configuration-example)
      - [CI Integration](#ci-integration)
      - [Local Usage](#local-usage)
      - [Challenges \& Trade-offs](#challenges--trade-offs)
      - [Summary](#summary)
  - [Rest, unsorted](#rest-unsorted)
    - [Keeping Your Fork Updated](#keeping-your-fork-updated)
    - [Prefer GitHub Apps instead of (Fine Grained) Personal Access Tokens](#prefer-github-apps-instead-of-fine-grained-personal-access-tokens)

---

## 1. Purpose & Context

This guide helps companies (tool vendors, integrators, OEMs, suppliers) decide how to structure forks of S-CORE repositories to:

- Contribute efficiently upstream
- Integrate internal compliance / security workflows
- Keep proprietary or distribution-specific assets separate
- Avoid accidental leakage of secrets or internal IP
- Automate promotion of reviewed code to the public community

> S-CORE spans 50+ repositories. You DON'T need a one-size-fits-all approach. Pick the minimal model per repository and evolve when needs grow.

### 1.1 Audience
Engineering orgs managing both internal and external code flows; platform / DevEx teams formalizing contribution and publication pipelines; compliance/security stakeholders.

### 1.2 Goals
Provide a decision and execution framework that reduces friction and risk while keeping the path to upstream contribution short.

### 1.3 Out of Scope
License interpretation, export control, internal HR / policy approvals. You must comply with S-CORE licensing independently.

### 1.4 Private vs Public Forks

Each model description focuses on WHEN to use it and inherent CONSTRAINTS. Implementation details are in Section 3.

### Public Fork

- Use when: You only need to contribute upstream or maintain a long-lived divergence openly.
- Pros: Simple; no internal infra.
- Constraints: No internal-only code separation; risk of accidental leakage if you try to “hide” things manually.

### Internal Fork

- Use when: You passively consume S-CORE (read-only) or maintain internal extensions not (yet) publishable.
- Pros: Freedom to experiment internally; shield proprietary assets.
- Constraints: Requires disciplined syncing from upstream to avoid drift.

Note that internal forks can use any infrastructure and do not need to be on GitHub.

### Hybrid (Both)

- Use when: You both maintain internal-only additions AND contribute upstream regularly.
- Core need: Clear policy to prevent leakage and friction.
- Variants (see Section 3):
  - Public-first
  - Internal-first
  - With transformation layer

---

## 2. How To work with forks

First and foremost see [GitHub's guide to working with forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

Note that in enterprise environments forks will usually be created by forking into an company organization (e.g. `my_company/score`) rather than a personal account. And those will be created by infrastructure administrators rather than individual developers.

Such a fork can be created by e.g. [`gh repo fork eclipse-score/score`](https://cli.github.com/manual/gh_repo_fork) or some infrastructure as code approach.

The default remote names will be:

- `origin`: your fork (e.g. `my_company/score`)
- `upstream`: the original repo (e.g. `eclipse-score/score`)

### Flow of a feature

There is a number of ways to achieve the same result in git, and it comes down to personal/team preference. Here is one possible approach.

```bash
# Update main
git switch main
git pull upstream main

# Create branch
git switch -c `<feature-branch>`

# Commit changes...
...
git push
```


Now you can create PRs from `<feature-branch>` to `upstream/main` directly. See [GitHub Docs - Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) for details.
Alternatively you can use `gh pr create` to create PRs from the command line.


#### Opinionated Alternative: change main reference

The flow can be simplified by making your local `main` track `upstream/main` directly. Since typically `my_company/main` is not relevant. This way you can always fast-forward `main` to the latest upstream state. And keeping `my_company/main` in sync is not needed.

Setup:

```bash
git switch main
git branch --set-upstream-to=upstream/main
git reset --hard upstream/main
```

The daily flow is then the same as without a fork:

```bash
git switch main
git pull
git switch -c `<feature-branch>`
...
git push
```

---

## 3. Hybrid Implementation

As public and internal forks are rather trivial, this section focuses on hybrid workflows.
It provides implementation guidance for updating forks, contributing from hybrids, and operating transformation pipelines.

Depending on policy and compliance constraints, pick the simplest viable variant.

### 3.1 Public-first Workflow

Before a branch is started, it is known whether the target is internal or public domain.
All S-CORE targeting contributions happen on the public fork.

Recommendations:

1. Short-lived feature branches (e.g., `topic` or `<username>/<topic>`)
2. Individual PRs upstream
3. Delete merged branches

Notes:

- `main` in your public fork may either track upstream or remain unused (can serve as a backup copy if required by policy).
- Large contributions may need internal pre-approval before public exposure.

### 3.2 Internal-first Workflow

Most development occurs internally; publication is an explicit step. This ensures internal compliance checks before public exposure. Each pull request is reviewed internally before being pushed to the public fork for upstream submission.
This results in significantly more setup & process overhead.
We have seen examples where this is mandated by policy.
We have seen examples where this makes collaboration impossible due to long delays on every PR.

#### Workflow Overview

Just an example, obviously adapt to your needs.

- Development happens in `internal/feature_unverfied`.
- PR to `internal/feature_verified`.
- Transfer to `public_fork/feature` (manual or automated).
- PR to `eclipse-score/feature` (manual or automated).



### 3.3 Transformation / Filtering Pipeline (Copybara Implementation)

Adds controlled publication with filtering & metadata normalization.

#### Overview

[Copybara](https://github.com/google/copybara) synchronizes code between repositories where you need to:

- Mirror internal → public
- Filter files
- Transform content / metadata
- Preserve coherent history

#### Key Benefits

Iterative (non-squash) commits:

- Retain individual commits
- Preserve messages & timestamps
- Avoid history compression

File filtering:

- Exclude internal-only assets (e.g., `.github/workflows`, `copy.bara.sky`)
- Publish only OSS-relevant content

Author preservation:

```python
authoring = authoring.pass_thru("Qorix Bot <bot@qorix.dev>")
```

Preserves original commit authors for traceability.

Transformations:
Supports `core.replace`, `core.move`, `core.transform`, header injection, folder renames.

Example:

```python
transformations = [
  core.replace(
    before = "INTERNAL_PATH",
    after = "PUBLIC_PATH",
  )
]
```

#### Minimal Configuration Example

```python
origin = git.origin(
    url = "https://github.com/qorix-group/inc_orchestrator_internal.git",
    ref = "main",
)

destination = git.destination(
    url = "https://github.com/qorix-group/inc_orchestrator.git",
    fetch = "refs/heads/main",
    push = "refs/heads/{{BRANCH}}",
)

core.workflow(
    name = "publish_branch",
    mode = "ITERATIVE",
    origin = origin,
    origin_files = glob(
        ["**"],
        exclude = [
            "copy.bara.sky",
            "sync.sky",
            ".github/workflows/copybara.yml",
            ".github/workflows/sync.yml",
        ],
    ),
    destination = destination,
    authoring = authoring.pass_thru("Qorix Bot <bot@qorix.dev>"),
    transformations = [],
)
```

#### CI Integration

```yaml
- name: Generate GitHub App token
  id: generate_token
  uses: tibdex/github-app-token@v2
  with:
    app_id: ${{ secrets.GH_APP_ID }}
    private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

- name: Configure Git
  run: |
    git config --global user.name  "Qorix Bot"
    git config --global user.email "bot@qorix.dev"
    echo "https://x-access-token:${{ steps.generate_token.outputs.token }}@github.com" > ~/.git-credentials

- name: Run Copybara
  run: |
    sed -i "s/{{BRANCH}}/${{ github.event.inputs.branch_name }}/g" copy.bara.sky
    curl -LO https://github.com/qorix-group/copybara/releases/download/v20250508/copybara_deploy.jar
    java -jar copybara_deploy.jar migrate copy.bara.sky publish_branch
```

#### Local Usage

```bash
java -jar copybara_deploy.jar --init-history --force copy.bara.sky publish_branch
```
Use this to preview migrations or sync new branches outside CI.

#### Challenges & Trade-offs

| Challenge | Impact |
|-----------|--------|
| No native GH default token support | Extra auth setup |
| Requires state for first branch push | One-time `--init-history` nuance |
| Credential & Git config ceremony | Boilerplate in CI |
| Additional maintenance | Long-term ownership needed |

#### Summary

Copybara offers controlled, scriptable synchronization with filtering and author preservation. Choose it only when manual git workflows no longer scale or policy filtering is mandatory.

## Rest, unsorted

### Keeping Your Fork Updated

Relevant for real (non-contribution-only) forks. Periodically create PRs (or fast-forward merges) from S-CORE `main` into your fork `main`, running internal workflows (tests, linting, compliance) before acceptance. Neglecting this increases integration cost over time.

### Prefer GitHub Apps instead of (Fine Grained) Personal Access Tokens

TODO
