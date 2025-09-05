
> ⚠️ **Disclaimer:** This document is a living draft, incorporating community feedback. Scope and details may evolve.

# Forking the SCORE Organization: Public & Private Forks


Partners working with SCORE often use **two forks**:
1. a **public fork** to contribute upstream via PRs
2. a **private/internal fork** to integrate SCORE with company systems (CI/CD, compliance, secrets, proprietary code)

However, for simple or initial contributions, a **public fork alone may be sufficient**. Many organizations start with only a public fork and add an internal fork as needs grow (see below for detailed reasons).

This guide introduces the concept at **three levels of detail**:
- **Executive level:** why both forks matter (and when you might only need one)
- **Normal level:** typical workflows and contribution models
- **Implementation level:** sync, branches, protections, and real-world automation (Qorix example, Copybara)

---


## 1. Executive Level (Why)

- **Public forks** keep contributions visible, upstreamable, and community-friendly.
- **Private/internal forks** allow integration with proprietary code, internal policies, and company-specific workflows.

### When is a public fork enough?
For "public-first" workflows, a public fork may be sufficient—especially for initial or simple contributions. You can always add an internal fork later if your needs grow.

### Why have an internal fork? (More detailed reasons)
- **Control:** You must have control over the source code you use for customers and not depend on external repositories, which could disappear (compliance).
- **Integration:** Add company-specific code, packaging, or system tests that cannot be open sourced.
- **Proprietary code:** Maintain proprietary modules, glue code, or customer-specific modifications.
- **Compliance:** Enforce internal CI/CD, security, and compliance checks before code is made public.
- **Support:** Maintain bug-fixes or support branches for customers, even if not yet up-streamed.
- **Separation:** Keep internal-only files, secrets, or business logic out of the public eye.

### Contribution Models
- **Internal-first (gated):** Private review and compliance before public PR. Safer, but slower and more complex.
- **Public-first (open):** Direct contribution via public fork. Faster, more transparent, but needs guardrails to avoid leaks.

---


## 2. Normal Level (What)

### Fork Types
- **Public Forks**
  - For feature branches and PRs only.
  - Must remain clean and minimal (no secrets, no internal code).

- **Private/Internal Forks**
  - Host mirrored upstream branches (`main`, `release/*`).
  - Contain company-specific branches (`internal/main`, `internal/feature/*`).
  - Enforce internal CI/CD, CODEOWNERS, and compliance.
  - Used for integration, compliance, and proprietary work.

### Contribution Models
- **Internal-first (gated):**
  - Flow: dev → internal PR → internal review → promote branch → public fork → upstream PR.
  - Pros: compliance, confidentiality, control.
  - Cons: slower, more complex.

- **Public-first (open):**
  - Flow: dev → public fork feature branch → upstream PR.
  - Pros: fast, transparent, community-friendly.
  - Cons: needs guardrails to avoid leaks; may not fit all compliance needs.

---


## 3. Implementation Level (How)

### Repo Sync
- **Initial seed:** One-time full mirror into an empty private repo.
- **Ongoing sync:** Explicitly push upstream branches (e.g., `main`, `release/*`) into private fork; avoid overwriting `internal/*`.
- **Avoid `git push --mirror`** except at initial seed or for read-only mirrors.

### Branch Layout
- `main`, `release/*` → upstream mirrors (bot-only updates).
- `internal/*` → private company branches (integration, compliance, proprietary code).
- `feature/*` → short-lived public fork branches for upstream PRs.

### Protections & Policies
- **Public fork:**
  - No secrets or internal code.
  - Basic lint/format/build/test checks.
- **Private fork:**
  - Internal CI with compliance/security.
  - Protect upstream branches.
  - Require CODEOWNERS + review on `internal/*`.

### Promotion Flow
- **Internal-first:**
  - Rebase internal feature branch onto upstream main.
  - Strip internal-only commits/files if needed.
  - Push result into public fork, open PR upstream.

### CI Hooks
- Internal PRs: run full secret-backed compliance checks.
- Public PRs: run open CI checks only.
- Optional: trigger internal CI on public PR head (read-only, no secret leaks).

---

## 4. Real-World Example: Qorix Pseudo-fork Publisher Workflow

Some organizations automate the promotion of internal branches to public forks. For example, Qorix uses a dedicated GitHub Action workflow to publish a development branch from an internal repository to a public fork, enabling secure and auditable contributions to upstream.

### Qorix Model: Three Repositories
- `repo_internal` — private internal repo (development, compliance, secrets)
- `qorix-group/repo` — public fork (clean, reviewable)
- `eclipse-score/repo` — original open-source repo (upstream PRs)

#### Naming Convention
- Private repo: suffix `_internal` (e.g., `inc_orchestrator_internal`)
- Public fork: same name as upstream (e.g., `inc_orchestrator`)

#### Secure Automation with GitHub App
Qorix uses a GitHub App (`qorix-repo-publisher`) for secure, scoped automation. The app generates short-lived tokens for pushing branches from private to public repos.

##### Example GitHub Action Step
```yaml
- name: Generate GitHub App token
  id: generate_token
  uses: tibdex/github-app-token@v2
  with:
    app_id: ${{ secrets.GH_APP_ID }}
    private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}
```

#### Workflow Summary
1. Checkout internal repo
2. Fast-forward main branch to match upstream
3. Create feature branch, push to public fork
4. Open PR from public fork to upstream

##### Manual Git Steps
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

---

## 5. Advanced: Using Copybara for Repo Sync

[Copybara](https://github.com/google/copybara) is an open-source tool for synchronizing code between internal and public repositories, with support for filtering files, preserving authorship, and custom transformations.

### Key Benefits
- **Iterative commits:** Retain individual commit history
- **File filtering:** Exclude internal-only files
- **Author preservation:** Keep original commit authors
- **Transformations:** Rename, move, or modify files/metadata as needed

#### Minimal Copybara Config Example
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

#### Running Copybara in CI
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

---

---


## TL;DR

- For most partners, **two forks** (public + private/internal) are best for compliance, integration, and control.
- For simple or initial contributions, a **public fork alone may be enough**.
- Choose a contribution model:
  - **Internal-first** = safer, more compliant, but slower.
  - **Public-first** = faster, more transparent, but needs guardrails.
- Protect mirrored upstream branches; keep internal work separate.
- Automate syncs, document policies, and define responsibilities.
