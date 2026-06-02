<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-001-Arch: Rust Readiness for Safety-Critical Components

* **Date:** 2026-03-06

```{dec_rec} Rust Readiness for Safety-Critical Components
:id: dec_rec__arch__rust_safety_critical
:status: accepted
:context: Architecture
:decision: Rust is ready for use in ASIL-B safety-critical components
```

---

## Context / Problem

At the [Architecture F2F in November 2025](https://github.com/orgs/eclipse-score/discussions/1922#discussioncomment-14891648), the project deferred the Rust readiness decision to individual modules with a February 2026 assessment deadline. Key gaps included coverage, compiler qualification, and libcore/libstd qualification.

The [Technical Lead Circle meeting on 2026-03-06](https://github.com/orgs/eclipse-score/discussions/2662) reviewed evidence and concluded that Rust is ready for ASIL-B safety-critical use in S-CORE 1.0.

## Decision

Rust is approved for use in ASIL-B safety-critical components.

## Rationale

Critical tooling (compiler, linting, formatting) is complete. Remaining mandatory gaps (coverage qualification, libcore/libstd extensions) have commercial mitigation paths available.

### Evidence Basis
The evidence was gathered by the S-CORE Rust Community and documented in [Weekly RUST Meeting, 2026-03-04](https://github.com/orgs/eclipse-score/discussions/236#discussioncomment-15997719):

```markdown
# Rust ASIL-B end of 2026 - feasibility overview

Overall tracking board: https://github.com/orgs/eclipse-score/projects/34/views/7
Mandatory scope: https://github.com/orgs/eclipse-score/projects/34/views/8

## Mandatory Scope

### ✅ Code formatting 
Bazel integration + CI/CD integration ready and rolled out in few Rust repositories that ensures code is aligned by same S-CORE wide configuration

- Verification report (https://eclipse-score.github.io/score/main/score_tools/tools_static_analysis_code_quality/clippy.html#doc_tool__clippy)

### ✅ Static code analysis - linting

- Bazel integration + CI/CD integration ready and rolled out in few Rust repositories that ensures code is aligned by same S-CORE wide configuration
- tool have available report verification with confidence HIGH, meaning no qualification needed. (https://eclipse-score.github.io/score/main/score_tools/> ols_static_analysis_code_quality/clippy.html#doc_tool__clippy)


### 📈 Code coverage
Bazel integration + CI/CD integration ready and rolled out in few Rust repositories

- Using build in Rust test framework for writing and running TC
- Tool for coverage calculation used from Ferrocene 
    - Ferrocene provided offer for tool qualification  - ✅  offer available at https://github.com/eclipse-score/score/issues/2020

### 📈 Certified `libcore` and `libstd` subset

- `libcore` certified as ASIL-B in quite big scope already
- Ferrocene provided commercial offer for extension of those two in required timeline. - https://github.com/eclipse-score/score/issues/2020

### ✅ Qualified Rust compiler

- Ferrocene and QNX announced qualified compiler being available at Q3 2025 (QNX Funded)
- OEM/TIER1 can contact ferrocene for compiler offer with maintenance (around ~~25euro/mth/seat)

### Good to have

#### 📈 Coding guidelines

- Plan to use SCRCG (https://github.com/rustfoundation/safety-critical-rust-coding-guidelines)
- Planned availability of first version mid 2026 (not confirmed but there is good progress there)


### Dynamic analysis
`Miri` tool can be used, requires integration with bazel (some repos run it via cargo already) - planned to be done soon (**weeks**), currently no chnical > blockers
```

## Consequences

Feature teams can use Rust for safety-critical components without additional project-level approval. Module-level architecture decisions should document language choice rationale but don't need to re-justify Rust's safety-critical readiness.

## Remaining Risks

- Qualification timeline: Coverage and libcore/libstd work must be ordered latest by July 2026 to make the referenced timeline
- Assessment is specific to QNX 8 with Ferrocene compiler; other platforms need to be evaluated via the [OS onboarding process](https://eclipse-score.github.io/score/main/modules/os/operating_systems/docs/index.html) when promoting to the Certifiable Level
