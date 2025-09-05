# Fork Strategy for the S-CORE Organization

> Early work in progress!

## Table of contents

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Models and decision framework](#2-models-and-decision-framework)
- [3. Deep dive into "Both" model](#3-deep-dive-into-both-model)
- [4. Updating a fork](#4-updating-a-fork)
- [5. Internal-first workflow](#5-internal-first-workflow)
- [6. Transformation / publication pipeline (Copybara)](#6-transformation--publication-pipeline-copybara)

## 1. Purpose and audience

This guide helps companies (tool vendors, integrators, OEMs, suppliers) decide how to structure forks of S-CORE repositories to:

- Contribute efficiently upstream
- Integrate internal compliance / security workflows
- Keep proprietary or distribution-specific assets separate
- Avoid accidental leakage of secrets or internal IP
- Automate promotion of reviewed code to the public community

> S-CORE spans 50+ repositories. You DON'T need a one-size-fits-all approach. Pick the minimal model per repository and evolve when needs grow.

Note that this guide will not address license requirements. We are not lawyers. We do not give any advice. You will need to comply to S-CORE licensing on your own.

## 2. Models and decision framework

### 2.1 Core models (at a glance)

Below are the core fork models explained as short sub-sections so it's easier to expand details and constraints later.

#### Public fork

- Us in case of:
  - Contributions to S-CORE or
  - Creating a real fork of S-CORE.
- Pros:
  - Simple
  - Fast, zero internal infrastructure required.

#### Internal fork

- When to use:
  - Passive consumption of S-CORE (read-only) or
  - Extending S-CORE with internal modules, enhancements, glue code etc.
- Constraints: Requires workflows to keep syncing manageable.

#### Both (public + internal)

- When to use: when both criteria from above apply
- Constraints: Requires clear policies and workflows to avoid accidental leakage and to keep syncing manageable.

#### Transformation / publication pipeline (Copybara, etc.)

- When to use: You need to filter files, rewrite metadata, or enforce policy transformations before publishing upstream.
- Pros: Powerful, auditable, and repeatable; supports strict policy enforcement and selective publishing.
- Constraints: Adds extra tooling and maintenance burden; requires engineering effort to build and operate.

There is no generic recommendation, as it truly depends on your needs. The options are sorted roughly by complexity — pick the first one that fits your needs and evolve from there.

## 3. Deep dive into "Both" model

Depending on company policy and other restrictions different contribution styles are possible.
Again, we'll sort from simple to complex and you need to pick the first one that makes sense for you.

### 3.1 Public-first

All developers work on the public fork, and individually create PRs for S-CORE.
This is suitable for individual contributors and companies with no overhead due to internal policies.

1. Everyone works on short lived feature branches, e.g. `topic` or `<username>/<topic>`
2. Everyone creates individual PRs against S-CORE
3. Once PR is merged, the branch is deleted

Note: the `main` branch could either be intentionally dead or reflect S-CORE main branch. No recommendation on that yet. The main branch could serve as independent backup of the source code if this is required by your company policies.

Note: public-first usually does not hold for BIG contributions. Whatever big means for your company. Those usually need to be whitelisted internally before going public.

### 3.2 Internal-first

Most developers work on the internal fork, and individually create internal PRs before going public.
This is suitable for companies which require this due to internal policies.

Setup:

- 🔒 Internal development is protected and private.
- 🧼 Public forks remain clean, reviewable and stripped of internal tooling.
- 🔁 Pull Requests (PRs) require the source branch to have a common ancestor with the base repository — meaning the fork must share history with the original.

Visual Diagram:

```text
score_internal (private)
  │
  ▼  ➝ publish branch ➝ e.g. feature/myfix
my-company/score (public fork)
  │
  ▼  Pull Request ➝ base: main
 eclipse-score/score (upstream)
```

Con: complex setup. See How-To in the next chapters.

### 3.3 Transformation / filtering layer

Add (Copybara / custom) only if filtering / rewriting is required.

Con: complex setup. See How-To in the next chapters.

## 4. Updating a fork

This is only relevant for real, non-contribution-only forks.

You'll need to create PRs from S-CORE `main` to your forked `main`, and run your workflows (e.g. tests, linting) to decide whether to accept the changes.
Of course if you don't, you are screwed.

## 5. Internal-first workflow

This section describes how to safely publish changes developed internally to a public fork and then upstream, while preserving history and avoiding leakage of internal-only assets.

### 5.1 GitHub App setup

To avoid using personal access tokens (PATs) and to enable secure automation at the org level, use a **GitHub App** (e.g. `qorix-repo-publisher`).

#### Why use a GitHub App?

- Short‑lived tokens (reduced blast radius)
- Scoped installation access (principle of least privilege)
- Works across private + public repos

#### Setup steps

1. GitHub → Developer Settings → GitHub Apps → New GitHub App
2. Name it (e.g. `qorix-repo-publisher`)
3. Grant access to:
   - `qorix-group/inc_orchestrator_internal`
   - `qorix-group/inc_orchestrator`
4. Generate a private key and store as secrets:
   - `GH_APP_ID` (numeric ID)
   - `GH_APP_PRIVATE_KEY` (contents of the `.pem` file)

#### Requesting access

When new repositories are created, request the infrastructure / platform team to install the app on them.

#### Token generation in workflow

Use the [tibdex/github-app-token](https://github.com/tibdex/github-app-token) action:

```yaml
- name: Generate GitHub App token
  id: generate_token
  uses: tibdex/github-app-token@v2
  with:
    app_id: ${{ secrets.GH_APP_ID }}
    private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}
```

### 5.2 Automated publication workflow

This GitHub Action typically:

1. Checks out the internal repo (e.g., `inc_orchestrator_internal`)
2. Fast‑forwards its `main` to match upstream (`eclipse-score/inc_orchestrator`)
3. Creates a feature branch and pushes it to the public fork (`qorix-group/inc_orchestrator`)
4. (Optionally) verifies the branch exists and is PR‑ready

Result: The branch can be used to open a PR into the upstream project.

#### How to run

Triggered manually via GitHub Actions UI.

#### Input parameters

- `repo_slug`: project selector (e.g. `inc_orchestrator`)
- `source_branch`: base branch (e.g. `main`)
- `dest_branch`: feature branch to publish (e.g. `feature/myfix`)

Example trigger UI:

```text
Repo:         [inc_orchestrator ▾ ]
Source:       main
Destination:  feature/myfix
▶ Run Workflow
```

#### Example use case

You finished your work internally and want to contribute upstream:
1. Run workflow with `dest_branch=myfeature`
2. Open PR from public fork branch → base: `eclipse-score/inc_orchestrator/main`
3. Merge after review

### 5.3 Manual workflow (Git only)

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

After pushing, open a Pull Request from `feature/my_branch` in the public fork to the upstream repository.

## 6. Transformation / publication pipeline (Copybara)

### What is Copybara?

[Copybara](https://github.com/google/copybara) is an open-source tool developed by Google that helps synchronize code between repositories. It's built to support workflows where you need to:

- Mirror code across internal and external repos
- Filter out unwanted files
- Transform file content or commit metadata
- Keep histories clean and consistent

---

### Key benefits of Copybara

#### Iterative (non-squash) commits

By default, Copybara supports both **squash** and **iterative** commit models. We use the `ITERATIVE` mode to:

- Retain individual commits
- Preserve commit messages and timestamps
- Avoid compressing change history into one lump commit

#### File filtering

You can configure Copybara to:

- Exclude internal-only files (e.g., `.github/workflows`, `copy.bara.sky`, credentials)
- Include only open-source-relevant content

This ensures your public fork stays clean.

#### Author preservation

Using:

```python
authoring = authoring.pass_thru("Qorix Bot <bot@qorix.dev>")
```

Copybara keeps the **original commit authors** — important for traceability and contribution credit.

#### Transformations

Copybara supports custom transformations such as:

- `core.replace`, `core.move`, `core.transform`
- Injecting headers
- Renaming folders

Example:

```python
transformations = [
  core.replace(
    before = "INTERNAL_PATH",
    after = "PUBLIC_PATH",
  )
]
```

---

### Minimal configuration example

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

---

### CI integration (GitHub Actions)

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

---

### Local usage

You can also run Copybara manually on your local machine:

```bash
java -jar copybara_deploy.jar --init-history --force copy.bara.sky publish_branch
```

Use this to preview migrations or sync new branches outside CI.

Check the `copybara` directory for some configuration examples.

### Challenges and trade-offs

While Copybara works well locally, it's tricky to use in GitHub Actions, which automate tasks when code changes:

❌ It doesn’t support GitHub’s default token system.

❌ It expects stored state (which CI environments don’t persist).

❌ It needs special setup for credentials and Git configuration.

❌ It requires --init-history the first time you push a new branch — and only the first time.

---

### Summary

Copybara offers a powerful, flexible way to control how code moves between repositories. While more complex than plain `git`, it allows full control over filtering, authoring, and commit structure.

It works best when:

- You need to filter out sensitive files
- You want to preserve authorship
- You want to define repeatable sync logic

> We use it to mirror internal development to our public forks while maintaining clean, auditable, and collaborative histories.
