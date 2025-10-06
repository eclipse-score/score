<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-003-Infra: Devcontainer Strategy for S-CORE

- **Status:** Proposed
- **Owner:** Infrastructure Community
- **Date:** 2025-10-06

---

## 1. Context / Problem

S-CORE contributors require a consistent, efficient, and reproducible local development environment. Today, individual developers set up their own local tooling, which leads to divergence in dependencies, performance bottlenecks, and onboarding friction. To address this, we want to standardize on [Dev Containers](https://containers.dev/) as the foundation for S-CORE development.

The main question: **Should we adopt a single monolithic devcontainer for the full stack, a multi-container approach (via Docker Compose), or a hybrid strategy?**

Additionally, we must ensure that devcontainers are usable both **locally** and in **CI/CD pipelines**. This introduces the challenge of balancing **developer experience** (rich local environments) with **performance and efficiency** (leaner CI/CD containers).

---

## 2. Requirements

1. **Performance**: Acceptable build/startup times and reasonable resource usage, both locally and in CI/CD.
2. **Maintainability**: Easy updates of dependencies and configurations.
3. **Flexibility**: Support for different developer workflows (frontend, backend, infra).
4. **Isolation**: Clear separation of dependencies between S-CORE modules.
5. **Complexity**: Avoid unnecessary overhead in setup and troubleshooting.
6. **Integration**: IDE support (e.g. [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)) and compatibility with Bazel/CI pipelines.
7. **Consistency Across Environments**: Local devcontainers and CI/CD containers should share a common base to avoid divergence.

---

## 3. Options Considered

### 3.1 Single Monolithic Devcontainer

A single container image includes all tools, dependencies, and services needed across the S-CORE stack.

**Pros**:
- Simple onboarding: one container to run.
- Consistency: uniform tooling across contributors and CI/CD.
- Strong IDE integration.

**Cons**:
- Heavyweight: slow to build and update.
- Wasted resources: contributors working on a subset must still run the full image.
- Harder long-term maintainability due to dependency conflicts.
- Inefficient for CI/CD, where only a subset of tools is needed.

### 3.2 Multi-Container (Docker Compose)

Each S-CORE service (e.g. frontend, backend, infra) runs in its own devcontainer, orchestrated with Docker Compose.

**Pros**:
- Isolation: clear boundaries between components.
- Flexibility: contributors can run only the services they need.
- Easier dependency upgrades per module.

**Cons**:
- More complex setup and orchestration.
- Increased cognitive load for new developers.
- IDE integration can be more challenging than with a single container.
- Higher complexity to align CI/CD with local multi-container setups.

### 3.3 Hybrid Approach with Image Layering

A lightweight **base devcontainer** provides shared tooling (Bazel, git, linters). On top of it, optional **service-specific containers** are layered for richer local development.

Additionally, the base image can be reused in **CI/CD pipelines** as a minimal container (fast to build and run), while developers use extended local containers with additional tooling (debuggers, IDE integrations, documentation generators).

**Pros**:
- Balanced size/performance between local and CI/CD use cases.
- Maintains flexibility without overwhelming complexity.
- Allows efficient CI/CD execution by running a minimal container.
- Developers benefit from richer local tooling without slowing down CI pipelines.
- Aligns with industry practices (see [GitHub Codespaces multi-container](https://docs.github.com/en/enterprise-cloud@latest/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#devcontainerjson)).

**Cons**:
- Requires upfront effort to design a clear layering strategy.
- Slightly more complex CI/CD integration to manage both minimal and rich variants.

---

## 4. Decision

We adopt the **Hybrid Approach with Image Layering**:
- A **base devcontainer** as the foundation for both local and CI/CD environments.
- **Service-specific extensions** for local development, adding richer tooling where needed.
- **CI/CD pipelines** will primarily use the base container to optimize performance and avoid unnecessary dependencies.

---

## 5. Rationale

- Provides a **consistent developer experience** across environments while adapting to their needs.
- Avoids bloat of a single huge container while still keeping core tools unified.
- Developers can selectively enable only the services they need locally.
- Ensures **performance in CI/CD** by running lean containers.
- Ensures **flexibility locally** by providing richer environments.
- Aligns well with S-CORE’s modular multi-repo structure.
- Supports integration with [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) and CI/CD systems.

---

## 6. Consequences & Challenges

- **Image layering** must be carefully designed to avoid duplication and long build times.
- **Documentation & onboarding** must explain when to use the base container versus extended service containers.
- **CI/CD pipelines** must support both the lean base image and richer developer images.
- Requires monitoring of build times and resource usage across both local and CI/CD workflows.

---

## 7. Next Steps

1. Extend the existing [S-CORE central devcontainer](https://github.com/eclipse-score/devcontainer) to serve as the **base container** for both local and CI/CD usage.
2. Define **lightweight CI/CD variants** derived from the base container to optimize build speed and runtime performance.
3. Add **service-specific extensions** (backend, frontend, infra) on top of the base devcontainer for richer local development workflows.
4. Provide Docker Compose orchestration templates to combine base + service containers where needed.
5. Update contributor documentation to clarify:
   - when to use the base container,
   - when to use extensions,
   - how CI/CD leverages the lean variant.
6. Validate the approach with pilot projects across different S-CORE components, refining layering and documentation before broad rollout.
