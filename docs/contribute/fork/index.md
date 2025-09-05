# Fork Strategy for the S-CORE Organization

> Single-page guide structured as: 1. WHY (context & goals) → 2. WHAT (models & decisions) → 3. HOW (workflows & tooling).

- [Fork Strategy for the S-CORE Organization](#fork-strategy-for-the-s-core-organization)
  - [1. Why – Purpose \& Context](#1-why--purpose--context)
    - [1.1 Audience](#11-audience)
    - [1.2 Goals](#12-goals)
    - [1.3 Out of Scope](#13-out-of-scope)
    - [1.4 Principles](#14-principles)
  - [2. What – Fork Models \& Decision Framework](#2-what--fork-models--decision-framework)
    - [2.1 Model Overview (At a Glance)](#21-model-overview-at-a-glance)
      - [Models](#models)
    - [2.2 Selection Criteria](#22-selection-criteria)
    - [2.3 Model Details](#23-model-details)
      - [2.3.1 Public Fork](#231-public-fork)
      - [2.3.2 Internal Fork](#232-internal-fork)
      - [2.3.3 Hybrid (Both)](#233-hybrid-both)
  - [3. How – Implementation \& Workflows](#3-how--implementation--workflows)
    - [3.1 Keeping Your Fork Updated](#31-keeping-your-fork-updated)
    - [3.2 Hybrid Contribution Workflows](#32-hybrid-contribution-workflows)
      - [3.2.1 Public-first Workflow](#321-public-first-workflow)
      - [3.2.2 Internal-first Workflow](#322-internal-first-workflow)
        - [Optional: GitHub App Setup](#optional-github-app-setup)
        - [Automated Publication Workflow](#automated-publication-workflow)
        - [Manual Publication Workflow (Git only)](#manual-publication-workflow-git-only)
    - [3.3 Transformation / Filtering Pipeline (Copybara Implementation)](#33-transformation--filtering-pipeline-copybara-implementation)
      - [Overview](#overview)
      - [Key Benefits](#key-benefits)
      - [Minimal Configuration Example](#minimal-configuration-example)
      - [CI Integration](#ci-integration)
      - [Local Usage](#local-usage)
      - [Challenges \& Trade-offs](#challenges--trade-offs)
      - [Summary](#summary)

---

## 1. Why – Purpose & Context

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

### 1.4 Principles

- Minimize complexity until required
- Prefer reversible choices
- Keep sensitive assets out of public history
- Preserve authorship and traceability
- Automate repeatable publication steps

---

## 2. What – Fork Models & Decision Framework

### 2.1 Model Overview (At a Glance)

Below are the core fork models in increasing complexity. Pick the first that satisfies your needs and evolve only when forced by requirements.

#### Models

- Public Fork
- Internal Fork
- Hybrid (Both: public + internal)
- Transformation / Publication Layer (Copybara / custom)

### 2.2 Selection Criteria
Consider the following when choosing a model:

- Contribution frequency & size
- Need to keep internal-only extensions
- Security / compliance gating before publication
- File / metadata filtering requirements
- Desire to preserve granular commit history externally
- Automation maturity (manual → scripted → policy-enforced)


### 2.3 Model Details

Each model description focuses on WHEN to use it and inherent CONSTRAINTS. Implementation lives in Section 3 (How).

#### 2.3.1 Public Fork

- Use when: You only need to contribute upstream or maintain a long-lived divergence openly.
- Pros: Simple; no internal infra.
- Constraints: No internal-only code separation; risk of accidental leakage if you try to “hide” things manually.

#### 2.3.2 Internal Fork

- Use when: You passively consume S-CORE (read-only) or maintain internal extensions not (yet) publishable.
- Pros: Freedom to experiment internally; shield proprietary assets.
- Constraints: Requires disciplined syncing from upstream to avoid drift.

#### 2.3.3 Hybrid (Both)

- Use when: You both maintain internal-only additions AND contribute upstream regularly.
- Core need: Clear policy to prevent leakage and friction.
- Variants (see Section 3.2):
  - Public-first
  - Internal-first
  - With transformation layer

---

## 3. How – Implementation & Workflows

Implementation guidance for updating forks, contributing from hybrids, and operating transformation pipelines.

### 3.1 Keeping Your Fork Updated

Relevant for real (non-contribution-only) forks. Periodically create PRs (or fast-forward merges) from S-CORE `main` into your fork `main`, running internal workflows (tests, linting, compliance) before acceptance. Neglecting this increases integration cost over time.

### 3.2 Hybrid Contribution Workflows

Depending on policy and compliance constraints, pick the simplest viable variant.

#### 3.2.1 Public-first Workflow

All developers work on the public fork and create PRs directly against S-CORE.

Steps:

1. Short-lived feature branches (e.g., `topic` or `<username>/<topic>`)
2. Individual PRs upstream
3. Delete merged branches


Notes:

- `main` in your public fork may either track upstream or remain unused (can serve as a backup copy if required by policy).
- Large contributions may need internal pre-approval before public exposure.

#### 3.2.2 Internal-first Workflow

Most development occurs internally; publication is an explicit step.

Characteristics:

- 🔒 Internal repo private
- 🧼 Public fork stays clean (only intended contributions)
- 🔁 Branches must share history with upstream for straightforward PRs

Diagram:

```text
score_internal (private)
  │
  ▼  ➝ publish branch ➝ e.g. feature/myfix
my-company/score (public fork)
  │
  ▼  Pull Request ➝ base: main
eclipse-score/score (upstream)
```

Con: More setup & process overhead.

##### Optional: GitHub App Setup

Optional. Start without this if you're experimenting: a fine‑grained PAT (scoped to needed repos: contents + pull requests) stored as a secret (e.g. `GH_TOKEN`) is enough. Migrate to a **GitHub App** when you need org‑wide automation, stronger auditability, or to avoid long‑lived personal tokens.

You can adopt a **GitHub App** (e.g., `qorix-repo-publisher`) to replace PATs for more secure, scalable automation.

Why adopt a GitHub App (benefits over PAT):

- Short‑lived tokens
- Scoped repo access
- Works across private + public

Setup Steps (only if/when you choose to adopt):

1. GitHub → Developer Settings → GitHub Apps → New GitHub App
1. Name it (e.g. `qorix-repo-publisher`)
1. Grant access to:

- `qorix-group/inc_orchestrator_internal`
- `qorix-group/inc_orchestrator`

1. Generate private key → store as secrets:

- `GH_APP_ID`
- `GH_APP_PRIVATE_KEY`

Requesting Access: Ask platform/infrastructure team to install on new repos.

Token Generation (workflow snippet):

```yaml
- name: Generate GitHub App token
  id: generate_token
  uses: tibdex/github-app-token@v2
  with:
    app_id: ${{ secrets.GH_APP_ID }}
    private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}
```

##### Automated Publication Workflow

Typical automation:

1. Checkout internal repo (`inc_orchestrator_internal`)
2. Fast‑forward `main` to match upstream
3. Create feature branch & push to public fork (`qorix-group/inc_orchestrator`)
4. (Optional) Validate branch state for PR readiness

Trigger: Manually through GitHub Actions.

Inputs:

- `repo_slug` (e.g. `inc_orchestrator`)
- `source_branch` (e.g. `main`)
- `dest_branch` (e.g. `feature/myfix`)

Example UI:

```text
Repo:         [inc_orchestrator ▾ ]
Source:       main
Destination:  feature/myfix
▶ Run Workflow
```

Example Use Case:

1. Run workflow with `dest_branch=myfeature`
2. Open PR from public fork branch → base: `eclipse-score/inc_orchestrator/main`
3. Merge after review

##### Manual Publication Workflow (Git only)

For developers preferring local control:

```bash
# 1. Clone the internal repo
git clone git@github.com:qorix-group/inc_orchestrator_internal.git
cd inc_orchestrator_internal

# 2. Add upstream and fork remotes
git remote add upstream https://github.com/eclipse-score/inc_orchestrator.git
git remote add fork https://github.com/qorix-group/inc_orchestrator.git

# 3. Sync internal/main with upstream/main
git fetch upstream
git checkout main
git merge --ff-only upstream/main

# 4. Create and push your branch to the public fork
git checkout -b feature/my_branch
git push fork HEAD:feature/my_branch
```
After pushing: open a Pull Request from `feature/my_branch` in the public fork to upstream.


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
