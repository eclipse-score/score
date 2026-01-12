<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-005-Infra: Development, Release and Bugfix workflows

- **Status:** Proposed
- **Owner:** Infrastructure Community
- **Date:** 2026-01-08

---

## 1. Context

This project consists of multiple independently developed modules stored in separate repositories (polyrepo setup).

This ADR builds on [DR-002 (Integration Testing in a Distributed Monolith)](./DR-002-infra.md), which establishes:
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
- Working on the main branch should be always possible
- Working on a release branch should be always possible and not harm the development on the main branch (resp. Vice versa)
- Working on a bugfix should always be possible (for any old release)
- Module developers must know how to name their released versions
- It must be clear how to do the integration, means what to reference (e.g. „extended“ semver as 1.2.3-etas-r1.0)

---

## 3. Options Considered

### 3.1 Trunk-Based Development with SemVer

Uses trunk-based development where modules develop on `main` branches and release with standard SemVer tags. The manifest repository (per DR-002) continuously tracks the latest module versions. When a product release is needed, release branches are created in the manifest and affected module repositories. Module bugfixes on release branches are tagged with standard SemVer, and the manifest's release branch references these versions.

**Pros**:
- Simplifies development workflow.
- Encourages frequent integration.
- Well-understood versioning convention.

**Cons**:
- Standard SemVer cannot represent parallel release streams. When a bugfix is needed on a release branch while `main` has advanced, version numbering becomes ambiguous (see diagram below).
- Versioning conflicts arise when merging bugfixes back to `main`.

```{mermaid}
gitGraph
    commit id: "1.2.3"

    branch release
    checkout release
    commit id: "1.2.3-r1.0"

    checkout main
    branch bugfix
    checkout main

    commit
    commit id: "1.2.4"
    commit
    commit id: "1.2.6"

    checkout bugfix
    commit id: "bugfix-work"

    checkout release
    merge bugfix
    commit id: "1.2.5"

    checkout main
    merge bugfix
```
> *Explanation:* Using SemVer quickly reaches its limits.
If branching off from version 1.2.3 and needing a bugfix while development on `main` continues (creating 1.2.4), the release branch would need version 1.2.5 for the bugfix. The next version on `main` must then be 1.2.6, even though its logical predecessor is 1.2.4. This violates SemVer since backward compatibility could be broken.

### 3.2 Gitflow Across Repositories

The manifest repository creates release branches (e.g., `release/v1.0`), and each participating module repository creates corresponding release branches. Since Bazel requires either version tags or commit hashes in `MODULE.bazel`, the manifest must be updated manually each time a module's release branch is tagged or advanced. This creates a workflow where teams coordinate to stabilize their module release branches, tag them, and then update the manifest's release branch to reference those tags or commits.

**Pros**:
- Well-known branching model.
- Provides release branches for stabilization.

**Cons**:
- Requires manual updates to the manifest whenever module release branches are tagged or advanced.
- Manual coordination across all module repositories to create, maintain, and tag release branches.
- Frequent manual manifest updates during stabilization increase coordination overhead.
- Does not scale well with increasing module count.

### 3.3 Polyrepo Release Process with Manifest Repository and relaxed version of SemVer

As described in [DR-002 (Integration Testing in a Distributed Monolith)](./DR-002-infra.md) there is a dedicated manifest repository containing the "known goods sets". There is a known good set for the latest version, but also known good sets for release(d) versions. Because of the earlier described limitations of SemVer, the correct module versions should not be referenced in the `MODULE.bazel` (in the manifest repository) as e.g., `1.2.3` but either by referencing the git commit hash directly or using a relaxed SemVer string, e.g. as `1.2.3-v1.0` where the string after the hyphen represents the respective S-CORE release.

With that approach releases are possible, e.g. by creating a release branch in the integration repository as well as in the affected module repositories. Also bugfixes of "old" releases are possible by checking out the repective release branch in the reference integration and if necessary to also created bugfixes in the affected modules.

**Pros**:
- Single source of truth for product integration.
- Supports continuous verification.
- Provides reproducible releases.
- Scales with module count and team autonomy.
- Clear separation between development, integration, and stabilization.

**Cons**:
- Requires explicit integration governance.
- Introduces additional coordination effort compared to single-repo workflows.

---

## 4. Decision

We decided for **Option 3.3**.

**Rationale**

This approach reflects established industry practice for large-scale polyrepo systems using
manifest-based integration and release trains (e.g. Android/AOSP, Chromium-style roll-ups),
while remaining explicit, and flexible.

It provides a single source of truth for integration, supports both continuous verification and reproducible releases, and scales with module count and team autonomy.

Option 3.1 (Trunk-Based Development Only) has been rejected because it does not address the need for coordinated product releases or explicit stabilization phases in a poly repo environment.

Option 3.2 (Gitflow Across Repositories) has been rejected because it requires coordinating release branches across all repositories and lacks a central integration manifest, which does not scale well.
