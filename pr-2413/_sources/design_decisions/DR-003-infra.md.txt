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

## 2. Goals and Requirements

1. **Performance**: Acceptable build/startup times and reasonable resource usage, both locally and in CI/CD.
1a. **Startup Performance**: Fast container initialization for productive development workflows.
2. **Maintainability**: Easy updates of dependencies and configurations.
3. **Flexibility**: Support for different developer workflows (e.g. development of modules communication, lifecycle, persistency, etc.).
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

Each S-CORE module (e.g. communication, lifecycle, persistency) runs in its own devcontainer, orchestrated with Docker Compose.

**Pros**:
- Isolation: clear boundaries between components.
- Flexibility: contributors can run only the modules they need.
- Easier dependency upgrades per module.

**Cons**:
- More complex setup and orchestration.
- Increased cognitive load for new developers.
- IDE integration can be more challenging than with a single container.
- Higher complexity to align CI/CD with local multi-container setups.
- Performance overhead from container orchestration and inter-container communication.
- Using different devcontainers can introduce friction for collaboration (e.g. "Works in my devcontainer")

### 3.3 Hybrid Approach with Devcontainer Features

A comprehensive **base devcontainer** provides all tooling needed for both development and CI/CD (Bazel, git, linters, build tools). On top of it, optional **devcontainer features** can be added for specialized local development workflows without rebuilding the base image.

The base image serves both **local development** and **CI/CD pipelines** to ensure consistency. Additional development tools (debuggers, IDE integrations, documentation generators) are added via devcontainer features only when needed locally. Developers can customize locally by devcontainer.json (may cause issues since devcontainer.json is under version control - mitigation: code reviews).

**Pros**:
- Perfect consistency between local and CI/CD environments (same base image).
- Flexibility through devcontainer features without base image complexity.
- Leverages existing devcontainer ecosystem and VS Code integration.
- Reduces maintenance overhead compared to multiple specialized images.
- Fast container startup: All tools pre-installed, no runtime feature installation.
- Predictable performance: No dependency on network speed or external service availability during container startup.

**Cons**:
- Base image may be larger than minimal CI requirements.
- Need to carefully evaluate which tools justify separate features vs. inclusion in base image.

---

## 4. Decision

We adopt the **Hybrid Approach with Devcontainer Features**:
- A **comprehensive base devcontainer** includes all tools needed for both development and CI/CD.
- **Devcontainer features** add specialized tooling for local development when justified by significant size/complexity.
- **Same base image** used in both local development and CI/CD pipelines for maximum consistency.

---

## 5. Rationale

Option 3.1 has been rejected because the probability that the container grows big is very high (with the growing necessity of features inside the container).
Option 3.2 (multi repo approach) has been rejected because the container orchestration would not be trivial and would cause several problems (see cons). Additionally, the multi repo approach is a poor fit to the design of the Bazel integration.
Option 3.3 is a compromise of 3.1 and 3.2 and has been selected therefore.

---

## 6. Consequences & Challenges

- **Supply chain security**: Devcontainer features from external sources introduce potential security and availability risks.
- **Feature evaluation**: Clear criteria needed for when tools justify separate features vs. base image inclusion.
- **Base image size**: May be larger than minimal CI requirements, but ensures consistency.
- **Feature maintenance**: Need to monitor and potentially archive critical external devcontainer features.
- **Runtime performance**: Feature-based approaches may cause delays at first container startup due to on-the-fly installation.
- **Network dependency**: Features require internet connectivity for initial installation, potentially limiting offline development workflows.
- **Documentation**: Must explain when and how to use devcontainer features safely.
- **Interim**: As long as we do not have hermetic builds in Bazel, the devontainer approach is a feasably interim step to ensure the right tools in the correct version are available (e.g. gcc_x.y.z, python_a.b.c, etc.)

---

## 7. Next Steps

1. Extend the existing [S-CORE central devcontainer](https://github.com/eclipse-score/devcontainer) to include **all tools needed for CI/CD** as the comprehensive base image.
2. Evaluate and create **devcontainer features** only for tools that add significant size/complexity and are not needed in CI/CD.
3. Establish **supply chain security guidelines** for evaluating, auditing, and potentially archiving external devcontainer features.
4. Use the **same base image** for both local development and CI/CD pipelines to ensure consistency.
5. Update contributor documentation to clarify:
   - when to use the base container,
   - when to use extensions,
   - how CI/CD leverages the lean variant.
6. Validate the approach with pilot projects across different S-CORE components, refining layering and documentation before broad rollout.
