<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-005-Infra: Polyrepo Release Process with SemVer, Manifest Repository, and Continuous Integration Tracking

- **Status:** Proposed
- **Owner:** Infrastructure Community
- **Date:** 2026-01-08

---

## 1. Context

This project consists of multiple independently developed modules stored in separate repositories (polyrepo setup).
Each module evolves independently and is versioned using Semantic Versioning (SemVer).

This ADR **builds on DR-002 (Infrastructure Architecture)**, which establishes:
- the polyrepo structure,
- centralized responsibility for cross-repository integration,
- and infrastructure-owned integration tooling and processes.

Within that context, this ADR defines **how coordinated product releases are produced** from independently developed and versioned modules, while allowing continuous integration to reduce the gap between development and release.

The project delivers a **coordinated product release** that integrates a specific, tested combination of module states. This requires:

- reproducible and auditable release snapshots,
- explicit stabilization phases,
- continuous integration before formal releases,
- independent module lifecycles without blocking development,
- and a process that scales across many repositories and teams.

Commonly referenced workflows do not fully address this problem space:
- **Trunk-Based Development** assumes continuous deployment and does not define coordinated product releases.
- **Gitflow** introduces coordinated release branching across repositories and lacks a central integration manifest.

This ADR defines a release process explicitly designed for **polyrepo systems with coordinated integration releases and continuous verification**.

---

## 2. Goals and Requirements

- Reproducible and auditable release snapshots
- Explicit stabilization phases
- Continuous integration before formal releases
- Independent module lifecycles without blocking development
- A process that scales across many repositories and teams

**Out of scope**
- This ADR does **not** prescribe:
  - module-internal branching models,
  - commit workflows,
  - or team-specific development practices.
- This ADR is **not Gitflow**:
  - stabilization is centralized in the manifest repository,
  - modules are not required to align release branches.
- This ADR does **not** assume a monorepo or continuous deployment model.

---

## 3. Options Considered

### 3.1 Trunk-Based Development Only

Assumes continuous deployment and does not define coordinated product releases.

**Pros**:
- Simplifies development workflow.
- Encourages frequent integration.

**Cons**:
- Does not address the need for coordinated product releases.
- Lacks explicit stabilization phases.
- Not suitable for polyrepo systems requiring integration snapshots.

### 3.2 Gitflow Across Repositories

Introduces coordinated release branching across repositories but lacks a central integration manifest.

**Pros**:
- Well-known branching model.
- Provides release branches for stabilization.

**Cons**:
- Requires coordination of release branches across all repositories.
- Lacks a single source of truth for integration state.
- Does not scale well with increasing module count.

### 3.3 SemVer-Based Polyrepo Release Process with Manifest Repository

A dedicated manifest repository defines integration state, with independent module versioning and two integration modes (tracking and pinned).

**Pros**:
- Single source of truth for product integration.
- Supports continuous verification via tracking mode.
- Provides reproducible releases via pinned mode.
- Scales with module count and team autonomy.
- Clear separation between development, integration, and stabilization.

**Cons**:
- Requires explicit integration governance.
- Introduces additional coordination effort compared to single-repo workflows.
- Relies on strict SemVer discipline in modules.

---

## 4. Decision

We adopt a **SemVer-based polyrepo release process with a dedicated manifest repository, continuous integration tracking, and release trains identified by tags**.

The solution is based on four core principles:

1. **Independent module versioning with strict SemVer guarantees**
2. **A manifest repository as the single source of truth for integration**
3. **Two integration modes: tracking (continuous verification) and pinned (release/stabilization)**
4. **Release stabilization via immutable tags (and an optional manifest release branch)**

### 4.1 Module Versioning (SemVer)

- Each module repository publishes releases following [Semantic Versioning 2.0.0](https://semver.org/).
- Version numbers are **global, linear, and unique per module**.
- Once a version is released, it is immutable and must never be reused.
- There is no automatic or periodic major version bump tied to product releases.

**Compatibility rule:**
- A PATCH release must be produced from a code line that is compatible with the previous release.
- Modules must not include incompatible changes in PATCH releases.

> **Explicitly out of scope:**
> Module-internal development workflows (e.g. trunk-based development, feature branches, rebasing strategies) are intentionally not prescribed by this ADR.

### 4.2 Manifest Repository

A dedicated **manifest (integration) repository** defines which exact module states form a product snapshot.

Responsibilities of the manifest repository:
- Define the complete product composition.
- Pin module states either as:
  - released module versions, or
  - explicit commit hashes (for tracking mode).
- Contain integration-specific artifacts such as:
  - end-to-end tests,
  - integration configuration,
  - packaging or distribution logic.
- Act as the **single source of truth** for product integration.

Any change to module references in the manifest repository is made via a pull request and reviewed as an integration change.

### 4.3 Integration Modes

The manifest repository operates in two distinct modes.

#### 4.3.1 Tracking Mode (Continuous Verification)

- Used on manifest `main`.
- The manifest may track module branches or “next release” branches by automatically updating pinned commit hashes.
- Goal:
  - continuously verify that the *current development state* of modules can be integrated,
  - reduce the gap between development and release,
  - detect integration issues early.
- Tracking references are **not considered release-ready** and are not used for formal release stages.

#### 4.3.2 Pinned Mode (Release and Stabilization)

- Used for release preparation and formal stages.
- The manifest pins **immutable identifiers only**:
  - released module versions, or
  - fixed commit hashes.
- Pinned mode guarantees full reproducibility and auditability.
- All release stages and final releases must use pinned mode.

### 4.4 Product Release Identification and Structure

Product releases are identified using **train-style tags**:

- `vX.Y.0-alpha.N`
- `vX.Y.0-beta.N`
- `vX.Y.0-rc.N`
- `vX.Y.0` (final)

Product versions reuse SemVer-compatible notation for clarity and tooling compatibility, but they represent **integration snapshots**, not API stability guarantees for individual modules.

### 4.5 Release Stabilization Line

To allow iteration without disturbing ongoing integration:

- A stabilization line may be introduced **in the manifest repository only**, e.g.:
  - an optional branch `release/vX.Y`, or
  - an equivalent agreed stabilization mechanism.
- Stabilization happens **only** in the manifest repository.
- Module repositories are not required to coordinate release branches.

This allows:
- continuous tracking on manifest `main`,
- controlled stabilization for a given product release.

### 4.6 Release Stages

#### Alpha
- Goal: early system-level integration.
- Allowed changes:
  - compatible bug fixes (PATCH),
  - compatible features (MINOR) if strictly required.

#### Beta
- Goal: feature freeze and stabilization.
- Allowed changes:
  - bug fixes only (PATCH).

#### Release Candidate (RC)
- Goal: final validation.
- Allowed changes:
  - critical bug or security fixes only (PATCH).

#### Final
- Tag `vX.Y.0` marks the final release.
- Optional product patch releases (`vX.Y.1`, `vX.Y.2`, …) follow the same rules.

### 4.7 Backports

- Fixes are applied first on the appropriate module code line.
- Compatible PATCH releases are created if required.
- The manifest is updated to reference the new immutable version or commit.
- A new stage or patch tag is created.

### 4.8 Breaking Changes During Stabilization

- Breaking changes during stabilization are strongly discouraged.
- If required (e.g. priority or organizational decisions), they must:
  - be explicitly declared,
  - include a documented mitigation strategy (compatibility layer, coordinated upgrades, scope reduction, or deferral),
  - and be recorded in the manifest repository.

### 4.9 Module Release-Line Strategies (Non-Normative Examples)

Modules may choose any internal strategy that preserves SemVer guarantees. Common compliant patterns include:

1. **Disciplined mainline releases**
   PATCH releases are cut before incompatible changes are merged.
2. **Temporary release branches**
   Short-lived branches cut from the last release tag to produce compatible PATCH releases.
3. **Persistent release branches**
   Long-lived branches for maintained version lines or LTS support.

The choice is module-local and does not affect the integration model.

### 4.10 Ownership and Governance

- The manifest repository is owned by the infrastructure/integration team, as defined in DR-002.
- As release stages progress (beta, rc), changes to the manifest require increasing scrutiny and justification.
- Governance applies only to the manifest repository and does not constrain module-internal workflows.

---

## 5. Rationale

This approach reflects established industry practice for large-scale polyrepo systems using
manifest-based integration and release trains (e.g. Android/AOSP, Chromium-style roll-ups),
while remaining explicit, flexible, and compatible with Semantic Versioning.

Option 3.1 (Trunk-Based Development Only) has been rejected because it does not address the need for coordinated product releases or explicit stabilization phases.

Option 3.2 (Gitflow Across Repositories) has been rejected because it requires coordinating release branches across all repositories and lacks a central integration manifest, which does not scale well.

Option 3.3 (SemVer-Based Polyrepo Release Process with Manifest Repository) has been selected as it provides a single source of truth for integration, supports both continuous verification and reproducible releases, and scales with module count and team autonomy.

---
