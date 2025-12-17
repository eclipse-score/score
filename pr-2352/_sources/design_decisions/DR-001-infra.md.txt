<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->


# DR-001-Infra: Integration Strategy for External Development Tools

* **Status:** Agreed within Community
* **Owner:** Infrastructure Community
* **Date:** 2025-09-01

---

## 1. Context / Problem

We use a broad set of tools (formatters, linters, static analyzers, code generators, license/SBOM and security scanners, doc builders) across multiple repositories. Today, tools are invoked via Bazel, IDEs, and CI with varying levels of pinning and caching. We need a standard approach that runs **identically** in CI, local CLI, and IDE/editor integrations, and that fits ISO 26262/ASPICE constraints (version pinning, determinism, long-term retention, offline path).

## 2. Requirements

1. **Version Pinning**: Identical tool versions across CLI/CI/IDE; no hidden network during execution; artifacts hash-pinned.
2. **Config Consistency**: Central baseline config; explicit, reviewable local overrides with drift detection.
3. **Performance**: Fast full and incremental runs; leverage remote cache/execution for heavy, Bazel-config-dependent tools.
4. **Offline & Retention**: Prefetch & store artifacts for ≥10 years; fully offline execution path.
5. **Platforms**: Ubuntu x86_64 + additional to be defined, e.g. Alpine, arm64 etc.
6. **Low Friction**: Minimal per-repo boilerplate; single invocation pattern; easy upgrades.
7. **Maintenance Effort**: Keep the system simple; avoid bespoke per-tool frameworks.

### Assumptions

- SCORE keeps the multirepo approach, therefore almost all tools only need to run on a single module at a time.


## 3. Options Considered

### 3.1 Bazel Aspects
Graph-aware aspects perform analysis/formatting per target, running only on affected targets (others are cached).

**Pros:**
- Efficient: Only runs on affected targets; remote execution possible.
- Config-aware: Linters run on correct configuration as selected via Bazel.

**Cons:**
- Complexity: Limited know-how, higher maintenance.
- Performance: Slow in rare cases (large targets, per-target Python venvs, duplicate analysis).
- Coverage: Not all tools are packagable (e.g., `dot`, PlantUML); alternatives needed.
- IDE Integration: Aspects lack IDE/editor support; must be supplemented by other methods.

### 3.2 Bazel Multitool
Centrally pinned binaries executed via `bazel run`.

**Pros:**
- Simple and compatible with IDE use cases.

**Cons:**
- No centralized config sharing or caching for slow tools.
- Not all tools are packagable (e.g., `dot`).
- Requires pre-execution setup (environment, dependencies).

### 3.3 Bazel Rules & Other Bazel Integrations
Custom Bazel rules encapsulate tool invocations/configurations for deeper integration.

**Pros:**
- Leverages Bazel caching and remote execution.
- Useful where aspects/multitool are unsuitable.

**Cons:**
- Increased complexity in rule management.
- Typically not compatible with IDE usage.

### 3.4 Devcontainer
Container image as authoritative tool distribution.

**Pros:**
- Straightforward onboarding; well-known concept.
- IDE support out of the box.

**Cons:**
- Large images can be slow on CI.
- Tools may implicitly use container content, not explicit dependencies.

### 3.5 Native Host Installs
Rely on developer/CI host environment package managers.

**Pros:**
- Fastest invocation; no wrapper overhead.

**Cons:**
- No version pinning; unenforceable consistency and high drift.
- Requires native setup.

## 4. Deep Dives

### 4.1 Bazel Multitool

We've invested enough time and energy into a solution with multitool to state that it is
a viable option. However, it requires significant effort and workarounds for tools that need
to be called directly from the IDE (for example, the Python binary).

We cannot set Bazel commands as executable paths; editor integrations usually expect a direct executable, so a small local wrapper script per repository is required. Examples: `python`, `ruff`, `starpls`, `spellcheck`, `yamlfmt`.

As multitool does not handle tool configuration, an additional solution is required per tool, which adds complexity.

### 4.2 Tool Versioning

For some tools keeping the version exactly the same is less important. Especially
extensions within VS Code typically come with their own bundled binaries. As long as
those are roughly the same version, slight inconsistencies between IDE and CI are
quite acceptable.

Especially in language servers which are only available within the IDE and are not
strictly safety relevant, this is viable.

### 4.3 Native Tools in CI

As using bazel and devcontainer introduces significant overhead, it seems natural to use certain tools natively in CI.
e.g. using the same installation scripts in devcontainers and CI has proven viable in other projects. Or providing a smaller and more dedicated CI image. These approaches will be detailed in a follow-up DR.

More interestingly there are cases where the exact version is less important (python) or
is managed outside bazel anyway (python requirements.txt files). In such cases native
installs have no disadvantages and are significantly easier (development) and faster (runtime).


## 5. Conclusion

- **Devcontainer** is the primary distribution for all tools, ensuring consistency and ease of onboarding.
- The same devcontainer (possibly stripped down) is used in CI for reproducibility.
- **Bazel aspects** are used for tools that benefit from Bazel-config-dependent analysis or caching. Custom Bazel rules are possible but not actively pursued.
- For small/fast CI jobs, **native installs** are preferred due to speed, especially when version pinning is less critical (see Deep Dive 4.3).
- **Bazel multitool** is a viable alternative for those not using devcontainer, but maintaining it requires significant effort and is not currently feasible for SCORE.



## Appendix: Tool Categories

**Bazel-config-dependent & cacheable**
_Provided via Bazel aspects and devcontainer for IDE support_
- Compilers (LLVM/Clang/GCC/… via toolchains)
- `clang-tidy`, `clang-analyzer`

**Independent & Fast Code Analysis**
_Provided via devcontainer (pre-commit, IDE, CI)_
- `ruff` (Python)
- `basedpyright` (Python)
- `actionlint` (GitHub Actions)
- `yamlfmt` (YAML)
- `spellcheck` (text)
- `buildifier` (Bazel)

**Independent Tools**
_Provided via devcontainer_
- IDE language servers: `rust-analyzer`, `clangd`, `starpls`
- `buildifier`, `bazel-compile-commands`
- `curl`, `qemu-system-aarch64`, `sshpass` (??)
- `protoc`
- `gcovr`

**Not Natively Cacheable in Bazel**
_Provided via devcontainer_
- Sphinx (incl. `sphinx-needs`, `PlantUML`, `graphviz`, and many dependencies)
- GraphQL (static code analysis)
- Eclipse Dash (license analysis)

**System Dependencies**
_Must be provided via devcontainer_
- `bazelisk` / `bazel`
- `git`
- `dot`
