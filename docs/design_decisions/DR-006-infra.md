<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-006-Infra: Clippy Integration via rules_lint

- **Date:** 2026-01-19

```{dec_rec} Clippy Integration via rules_lint
:id: dec_rec__infra__clippy_rules_lint
:status: accepted
:context: Infrastructure
:decision: Use rules_lint for Clippy in S-CORE modules
```

---

## 1. Context / Problem

S-CORE needs a consistent, Bazel-native way to run Rust Clippy across modules. We
initially aligned on rules_rust for Clippy integration, but rules_lint added native
Clippy support while that work was ongoing. We must choose one approach to reduce
divergence and keep lint workflows maintainable.

Key constraints:
- Avoid running Clippy across the entire tree by default.
- Avoid maintaining long, manual target lists.
- Keep lint rules centralized and versioned.
- Allow CI-friendly lint runs without additional tooling requirements.

## 2. Decision

We adopt rules_lint for Clippy integration in S-CORE modules.

## 3. Rationale

rules_lint fits better with the linting workflow:
- It is designed for linting (output groups, lint tests, lint-oriented UX).
- It avoids whole-tree runs and manual target lists by linting only the build graph
  of requested targets.
- Clippy support is released and tested, which reduces risk.

rules_rust remains a valid option, but it requires manual target enumeration for
lint-only runs and is harder to scope for incremental linting.

## 4. Integration Approach

Each module integrates Clippy through a rules_lint aspect:
- Use the shared aspect from `@score_rust_policies//clippy:linters.bzl`
  (repo-local aspects remain an option if needed).
- Reference the centralized Clippy configuration from the policies repo:
  `@score_rust_policies//clippy/strict:clippy.toml`.
- Enable the aspect in `.bazelrc` via `build --aspects=...%clippy` and request
  output groups `rules_lint_human` (and optionally `rules_lint_machine`).
- Skip linting for specific targets using the `no-lint` tag.
- For CI, add `--@aspect_rules_lint//lint:fail_on_violation=true` to fail on findings.
- Use `aspect_rules_lint` >= `2.0.0-rc0` to support `fail_on_violation` with Clippy.

This keeps configuration and behavior consistent while allowing each module to scope
linting to the targets it builds.

## 5. Consequences

- Clippy runs on the Rust targets in the build graph of the requested Bazel targets,
  not the whole repository by default.
- Lint rules are centralized in `score_rust_policies`, reducing duplication and drift.
- The Aspect CLI is not required for Clippy execution; standard `bazel build` works.
- rules_lint uses Aspect telemetry; this can be disabled via repo environment
  variables if required by policy.

## 6. Future Considerations

We may integrate the Aspect CLI in the future to enable the `bazel lint` command and
additional lint UX (interactive output, filtering, reporting). This is optional and
separate from the Bazel-based execution path.
