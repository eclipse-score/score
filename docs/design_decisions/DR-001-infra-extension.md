<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->


# DR-001-Infra-Extension: S-CORE Build Execution Contract


* **Date:** 2026-01-20

```{dec_rec} S-CORE Build Execution Contract
:id: dec_rec__infra__execution_contract
:status: accepted
:context: Infrastructure
:decision: Adopt a layered execution contract

```

---

## Purpose

This document defines the execution contract for S-CORE builds across developer machines
and CI infrastructure.
Its goal is to ensure **long-term reproducibility (≥10 years)**, **traceability** and
**practical hermeticity**, despite changes in underlying infrastructure such as
GitHub-hosted runners.

It builds on [DR-001], which was concerned about the same topics, but was focused on tools only. This adds details where the original description was too fuzzy.

The contract is intentionally **layered**, because different parts of the system control
different capabilities and failure modes.

---

## Core Requirements

### R1 — Long-Term Reproducibility
S-CORE builds must be reproducible for **at least 10 years** after creation, given:
- the source revision
- archived execution context
- archived toolchains
- recorded build metadata

This must remain possible even if:
- GitHub runner images change or are retired
- upstream toolchains are no longer available
- external services are unavailable

---

### R2 — Traceability
For every build artifact, it must be possible to determine **exactly**:
- which sources were used
- which toolchains and tool versions were used
- which Bazel version and flags were used
- which execution context (container image) was used
- which host baseline constraints applied

This information must be recorded in a **build manifest** and stored alongside the build
outputs.

---

### R3 — Hermeticity (Practical)
Build actions must not depend on **undeclared inputs**.

In practice:
- Tools affecting build outputs must either be:
  - managed by Bazel, or
  - explicitly injected as Bazel action inputs, or
  - reflected in cache partitioning
- Reliance on host state must be minimized and documented where unavoidable.

Perfect hermeticity is not required, but **undeclared variability is not acceptable**.

---

## Three-Layer Execution Contract

### Layer 1 — Host Platform Contract

This layer defines the **non-virtualized constraints** imposed by the machine running
the build.

#### Scope
- GitHub-hosted runners
- self-hosted runners (VM or bare metal)
- kernel-level features shared with containers

#### Responsibilities
- Linux kernel version and configuration
- Security mechanisms (AppArmor / LSM)
- Filesystems, networking, namespaces
- Support for:
  - Bazel `linux-sandbox`
  - QEMU / `binfmt`
  - privileged operations where required

#### Requirements
- Linux host OS (Ubuntu LTS for reference integration)
- Kernel must support:
  - unprivileged user namespaces
  - mount operations required by Bazel sandboxing
- Host security policies must not block Bazel `linux-sandbox` unless explicitly documented

#### Known Constraints
- Ubuntu 24.04+ AppArmor may block Bazel sandbox mount operations
- Containers **cannot** mitigate host-kernel restrictions

#### Policy
- A **Reference Integration Host Baseline** must be defined (e.g. Ubuntu 22.04).
- Deviations (e.g. privileged runners, sandbox disabled) must be explicit and isolated.

---

### Layer 2 — Execution Context Contract (Devcontainer)

This layer defines the **default user-space environment** in which builds are executed.

#### Purpose
- Provide consistent runtime ABI (`glibc`, `libstdc++`)
- Ensure tool binaries (e.g. rustc) can execute reliably
- Eliminate “works on my machine” discrepancies
- Enable local reproduction of CI builds

#### Definition
- A **versioned devcontainer image** is the default execution context.
- The container image must be:
  - built from a known OS baseline (Ubuntu LTS)
  - referenced by immutable digest
  - archived for long-term reproducibility

#### Responsibilities
- User-space runtime libraries
- Bootstrap tooling (git, bash, coreutils, python, etc.)
- Bazel entrypoint (preferably Bazelisk)
- Development UX tooling (optional)

#### Non-Goals
- The devcontainer must **not silently override** repository-declared Bazel versions.
- The devcontainer must **not be the only place** where critical tool versions are defined.

#### Policy
- The devcontainer defines the **default** environment, not the **only** supported one.
- Builds should still be possible on compatible bare-metal hosts.

---

### Layer 3 — Bazel Contract

This layer defines **what Bazel controls and guarantees**.

#### Bazel Versioning
- Each repository must contain `.bazelversion`.
- S-CORE uses a **single Bazel version** across repositories.
- CI enforces version consistency.

#### Toolchains and Tools
- Toolchains (e.g. Rust/Ferrocene, C/C++) must be:
  - versioned
  - immutable
  - built against a documented baseline
- Tools affecting outputs must be known to Bazel or reflected in action inputs.

#### Hermeticity Guarantees
- Bazel sandboxing provides reproducibility **given runnable tools**.
- Bazel does **not** virtualize:
  - kernel
  - `glibc`
  - host security configuration

These constraints must be handled in Layer 1 and Layer 2.

---

## Minimum Supported Baselines

### OS and Runtime Baseline
- Minimum supported baseline: **Ubuntu 20.04 LTS** (subject to revision)
- Toolchains must be built against this baseline
- Older environments are **not supported**

### Rationale
We explicitly do **not** support all historical `glibc` or kernel versions.
Portability is achieved by choosing and documenting a baseline, not by unlimited
backward compatibility. Layer 2 can easily be virtualized as needed, for future reproducibility.

---

## Build Provenance and Archiving

Each CI build must produce and archive:
- build manifest (metadata)
- container image digest
- toolchain identifiers
- source revision(s)

These artifacts form the basis for:
- long-term reproducibility
- forensic analysis
- compliance and auditing

---

## Summary

- **Layer 1** defines what the host *must* provide.
- **Layer 2** defines the default execution environment.
- **Layer 3** defines how Bazel achieves reproducibility and caching.
- Reproducibility, traceability, and hermeticity are enforced through
**explicit contracts**, not assumptions.

This separation allows S-CORE to scale infrastructure, evolve toolchains, and still
reproduce builds years into the future.
