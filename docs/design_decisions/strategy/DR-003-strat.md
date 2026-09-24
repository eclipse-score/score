<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-003-Strat: Module Maturity Classification (Release / Experimental / Preview)

- **Date:** 2026-07-27

```{dec_rec} Module Maturity Classification
:id: dec_rec__strat__module_maturity_levels
:status: proposed
:context: Strategy
:decision: Classify every module into one of three maturity levels — Release, Experimental, or Preview — based on requirement coverage and S-CORE process artifact completeness.
:version: 1
```

---

## Context / Problem

DR-001-Strat established S-CORE as a **continuously consistent stack** in which all modules
are integrated and released together. This raises a practical question: modules within the
stack differ significantly in how far they have progressed along the S-CORE developer process.
Some implement all their requirements with full verification evidence; others are still early
work in progress with few or no process artifacts.

Today there is no agreed, uniform way to express a module's **maturity** and its degree of
**S-CORE process compliance**. As a consequence:

- We cannot include immature modules in a platform release without implicitly signalling a
  quality level they do not have.
- Excluding immature modules from releases prevents users from discovering and trying them and
  fragments the "consistent stack" promise.
- Users have no clear, comparable indicator of what a given module actually offers, how well it
  is tested, and whether it is suitable for their intended usage.

We need a small, well-defined set of maturity classifications that lets us **include all
modules in platform releases** while giving users **clear guidance on each module's maturity
and intended usage**.

## Decision

Introduce **three maturity classifications** for S-CORE modules. Every module included in a
platform release is assigned exactly one of them. The classification is derived from two
dimensions:

1. **Requirement coverage** — to what extent the current feature and component requirements are
   implemented and verified (covered/tested).
2. **Artifact completeness** — to what extent the module provides the artifacts mandated by the
   current state of the S-CORE developer process (e.g. verification and traceability reports,
   inspection checklists).

### Classifications

**Release**

- The module implements **all** currently existing feature and component requirements, unless excluded by the valid_from / valid_until attributes
- All feature and component requirements are **fully covered / tested**.
- The module provides **all artifacts** mandated by the current state of the S-CORE developer
  process (e.g. verification and traceability reports, inspection checklists), possibly with a
  few **minor deviations**.

**Experimental**

- The module provides **all artifacts** mandated by the current state of the S-CORE developer
  process.
- **Major deviations** still exist — for example, not all requirements are implemented or
  thoroughly tested.
- The artifacts make it **clear what the module offers and what it does not**, so users can
  make an informed decision.

**Preview**

- **None or not all** of the artifacts required by the S-CORE process are present.
- Therefore the current status of the module **cannot be determined** and **no statement about
  the module's quality** can be made.

### Summary

| Aspect | Preview | Experimental | Release |
|---|:---:|:---:|:---:|
| S-CORE process artifacts present | none / incomplete | complete | complete (minor deviations allowed) |
| Deviations from process | undetermined | major, but transparent | minor only |
| Requirements implemented | undetermined | not necessarily all | all currently existing |
| Requirements covered / tested | undetermined | not necessarily all | fully |
| Quality statement possible (code quality, code coverage)| no | yes (with known gaps) | yes |

This makes it possible to **include all modules in platform releases** while giving users a
clear, comparable indicator of each module's maturity and intended usage.

## Rationale

- **Consistent stack, honest signalling.** DR-001-Strat wants all modules integrated and
  released together. A maturity label lets us keep that promise without overstating the quality
  of early modules.
- **Two independent dimensions matter.** A module can have complete process artifacts yet still
  be functionally incomplete (Experimental), or be functionally advanced yet lack the artifacts
  needed to *prove* it (which keeps it at Preview). The classification deliberately gates on
  **artifact completeness first**, because without artifacts no quality statement is possible
  at all.
- **Transparency over exclusion.** Experimental explicitly requires that the artifacts make the
  gaps visible. Users are guided, not surprised.
- **Minor vs. major deviations** distinguish Release from Experimental. The precise threshold
  between "minor" and "major" is left to the process/quality governance to define (see Open
  Points) rather than hard-coded here.

## Consequences

- Every module in a platform release carries exactly one maturity classification, surfaced to
  users (e.g. in module documentation and release notes).
- The classification must be **derivable from existing S-CORE process artifacts** (verification
  and traceability reports, inspection checklists, requirement coverage) so it can be assessed
  objectively and, ideally, largely automatically.
- The definition of "minor" vs. "major" deviation, and the exact list of mandated artifacts,
  are owned by the S-CORE developer process and may evolve; this DR references the *current*
  state of that process rather than freezing it.
- Follow-up work is required to define **who assigns and reviews** the classification, **when**
  it is (re-)evaluated in the lifecycle, and **how** it is represented in tooling and release
  metadata.

## Open Points

- Precise, checkable criteria separating **minor** from **major** deviations.
- Governance: who assigns/approves a module's classification and at which point in the process.
- Representation: where and how the classification is stored and displayed (module metadata,
  release notes, documentation badges).
- Whether and how a module can be **downgraded** (e.g. Release → Experimental) when the process
  requirements evolve and new mandatory artifacts appear.
