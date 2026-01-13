<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

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

This project consists of multiple independently developed modules stored in separate
repositories (polyrepo setup).

This ADR builds on
[DR-002 (Integration Testing in a Distributed Monolith)](./DR-002-infra.md), which
establishes:
- the polyrepo structure,
- centralized responsibility for cross-repository integration,
- and infrastructure-owned integration tooling and processes.

Within that context, this ADR defines **how coordinated product releases are produced**
from independently developed and versioned modules, while allowing continuous
integration to reduce the gap between development and release.

Commonly referenced workflows do not fully address this problem space:
- **Trunk-Based Development** with standard SemVer cannot represent parallel
release streams needed for supporting multiple product versions simultaneously.
- **Gitflow** adds branching complexity without solving the versioning problem
for parallel releases in a polyrepo setup.

This ADR evaluates branching and versioning strategies explicitly designed for
**polyrepo systems with coordinated integration releases and continuous verification**.

---

## 2. Requirements and Goals

### 2.1 Requirements

Options that do not satisfy these requirements are not viable and will be rejected:

- Reproducible and auditable release snapshots
- During working on a release, working on the main branch should still be possible
- Working on a release branch should be always possible and not harm the development on the main branch (resp. vice versa)
- Working on a bugfix should always be possible (for any old release)
- Module developers must know how to name their released versions
- The versioning scheme must clearly indicate which product release a module version
belongs to, enabling parallel release, which essentially means the ability to
maintain previous releases.
- Explicit stabilization phases
- Continuous integration before formal releases

### 2.2 Optimization Goals

Among viable options, we optimize for:

- Independent module lifecycles without blocking development
- A process that scales across many repositories and teams
- Minimal integration governance to coordinate releases across repositories

---

## 3. Options Considered

### 3.1 Trunk-Based Development

Trunk-based development is a branching model where all developers work on a single main
branch ("trunk"), integrating changes frequently—ideally daily. Feature and bugfix
development happens directly on the trunk or in very short-lived branches that are
merged back quickly. Long-lived release branches and parallel release streams are
explicitly avoided. Releases are created directly from the trunk, and if a release
branch is needed for final stabilization or a hotfix, it is kept as short-lived
as possible. Bugfixes are made on the trunk and only cherry-picked to a release
branch in rare cases where a hotfix for an older release is required. Versioning
is linear, and the model does not support parallel maintenance of multiple
product versions.

**Pros**:
- Very simple and lightweight branch structure.
- Maximizes integration and fast feedback through continuous integration.
- Minimizes merge conflicts and versioning issues.

**Cons**:
- Parallel maintenance of multiple product versions (e.g., for long-term support) is
not feasible.
- Not suitable for polyrepo setups that require parallel support of several releases,
as parallel release streams are not supported by design.

> Note: The versioning and merge conflicts described in the diagram below typically
arise when deviating from strict trunk-based development and introducing long-lived
release branches. This is no longer considered state-of-the-art trunk-based development.

```{mermaid}
gitGraph
    commit id: "1.2.3"

    branch release
    checkout release
    commit id: "1.2.3-v1.0"

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

### 3.2 Gitflow Across Repositories

Uses the Gitflow branching model where modules maintain both `main` and `develop` branches, with release branches created for stabilization. The manifest repository (per DR-002) creates release branches (e.g., `release/v1.0`), and each participating module repository creates corresponding release branches. Modules tag bugfixes on release branches with standard SemVer, and the manifest's release branch references these versions.

**Pros**:
- Well-known branching model.
- Explicit `develop` branch separates ongoing work from release stabilization.
- Release branches provide clear stabilization phases.

**Cons**:
- Standard SemVer suffers from the same parallel release stream problem as Option 3.1 (version numbering conflicts).
- Additional overhead of maintaining separate `develop` branches across all repositories.
- More complex branching model increases coordination complexity in a polyrepo setup.
- Does not scale well with increasing module count.

### 3.3 Polyrepo Release Process with Manifest Repository and relaxed version of SemVer

As described in [DR-002 (Integration Testing in a Distributed Monolith)](./DR-002-infra.md) there is a dedicated manifest repository containing the "known goods sets". There is a known good set for the latest version, but also known good sets for released versions. Because of the earlier described limitations of SemVer, the correct module versions should not be referenced in the `MODULE.bazel` (in the manifest repository) as e.g., `1.2.3` but either by referencing the git commit hash directly or using a relaxed SemVer string, e.g. as `1.2.3-v1.0` where the string after the hyphen represents the respective S-CORE release.

With that approach releases are possible, e.g. by creating a release branch in the
manifest repository as well as in the affected module repositories. Bugfixes for
previous releases are handled by checking out the corresponding release branch
in the manifest and affected modules, applying the fix, and updating the manifest
to reference the new module version.

**Pros**:
- Single source of truth for product integration.
- Supports continuous verification.
- Provides reproducible releases.
- Scales with module count and team autonomy.
- Clear separation between development, integration, and stabilization.

**Cons**:
- Requires explicit integration governance.

## 4. Decision

We decided for **Option 3.3**.

**Rationale**

Options 3.1 and 3.2 both violate the requirement for a versioning scheme that clearly indicates which product release a module version belongs to. Standard SemVer cannot represent parallel release streams - when a bugfix is needed on a release branch while `main` has advanced, version numbering becomes ambiguous and conflicts arise (as demonstrated in the diagram in Option 3.1). This makes both options non-viable.

Option 3.3 is the only viable option as it satisfies all requirements through relaxed SemVer (e.g., `1.2.3-v1.0`) where the suffix indicates the product release. Additionally, it optimizes for our goals by:
- Providing a single source of truth for product integration
- Supporting continuous verification through the manifest repository
- Scaling with module count and team autonomy
- Enabling clear separation between development, integration, and stabilization

This approach reflects established industry practice for large-scale polyrepo systems using manifest-based integration and release trains (e.g., Android/AOSP, Chromium-style roll-ups).
