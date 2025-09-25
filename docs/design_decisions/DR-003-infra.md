<!--
Copyright (c) 2025 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-003-Infra: Integration Testing in a Distributed Monolith - Extension for Non-CI Components

* **Status**: Submitted for Review
* **Owners**: Infrastructure Community
* **Date**: 2025-09-25
* **Supersedes / Extends**: Builds on the integration approach of [DR-002](./DR-002-infra.md)

---

## 1. Context / Problem Statement

[DR-002](./DR-002-infra.md) established that S-CORE applies strict
[Continuous Integration (CI)](https://martinfowler.com/articles/continuousIntegration.html):
every change to any component must pass integration tests before merge.

Two gaps were not considered:
1. Some components are external (no direct control over their workflow cadence or branching model).
2. Some internal components are temporarily not operating with per-change pull requests (e.g. early incubation).

We still need fast, reliable integration feedback across the composed system ("distributed monolith") without freezing progress or leaving pipelines permanently red.

The challenge: How do we extend the CI discipline to components that cannot (yet) provide pre-merge integration signals, while minimizing friction, avoiding long-lived breakages, and keeping a path to full CI?

---

## 2. Decision

Introduce a **tiered integration model** defined by when a component receives system-level integration feedback relative to its change lifecycle.

We formalize three tiers (ordered by desirability):

| Tier | When Integration Tests Run (relative to component change) | Primary Use Case | CI Gate Effect | Target State |
|------|-----------------------------------------------------------|------------------|----------------|--------------|
| 1 | Pre-merge (per PR) | Fully CI-enabled internal (and some external) components | Blocks merge on failure | Default & permanent |
| 2 | Post-merge (continuous against main branch) | Transitional internal components, external components which operate without PRs | Blocks promotion / release tags; failures trigger rollback or hotfix | Temporary on path to Tier 1 |
| 3 | Pre-integration of released artifact (version bump PR in S-CORE) | External components with independent release cadence | Blocks adoption of new version into registry | Accepted only for external components, and only if Tier 1/2 infeasible |

All **internal** components must plan migration to Tier 1. Tier 2 is explicitly transitional.

All **external** components can fall under any tier, depending on how closely they cooperate with S-CORE.

---

## 3. Detailed Tier Definitions

### Tier 1 (Pre-merge CI)
Characteristics:
* Every PR triggers integration validation as per DR-002.
* Failures block merge; must be resolved before proceeding.
* May include external repos that are willing to adopt our CI contract (webhooks, shared pipeline, or mirrored gated PR flow). For externals, feedback can be non-blocking if they prefer (e.g. advisory only).

### Tier 2 (Post-merge CI on Main)
Rationale / when allowed:
* Temporary: tooling or refactoring still pending; legacy systems lacking PR granularity.
Behavior:
* Integration suite runs on latest main (e.g. scheduled, or on each merge event via polling/mirroring).
* Failures block further release tagging or dependency promotion; owning team must react with highest priority.
* Participates in the "known-good" process of DR-002: if red, S-CORE cannot consume new versions until resolved.
* Migration plan required: target date for Tier 1, gaps to close, risk assessment if delayed.

### Tier 3 (Pre-integration CI on Released Artifacts)
Rationale:
* Upstream project cadence or governance prevents earlier visibility.
* We cannot enforce their branching/PR discipline.
* No strict up-to-dateness required — otherwise Tier 2 should be preferred.
Behavior:
* New upstream versions are proposed via an update PR (version bump) in S-CORE.
* Full integration tests run before the bump merges.
* If failing: we either (a) defer update, (b) contribute a fix upstream, or (c) add a compatibility shim internally.

---

## 4. Handling Breaking Changes

Breaking interface changes are only allowed when **all impacted Tier 1 components** have green adaptation PRs.

In addition, a mitigation plan for Tier 2 and 3 must exist (included in a shim layer, compatibility facade, or dual-version period).
Since no real synchronization with Tier 2 is possible, close collaboration with owning teams is required to ensure they can adapt promptly.

If not feasible, the change is postponed or introduced behind an opt-in feature flag with a deprecation timeline.

---

## 5. Alternatives Considered

1. Accept broken integration during coordinated waves of change.
   * Rejected: Encourages long red periods; compounds unrelated failures; extremely costly reintegration.
2. Separate, isolated integration pipelines per tier.
   * Rejected: Splits focus, increases maintenance, hides systemic readiness.
3. Force immediate universal Tier 1 adoption.
   * Rejected: Not reasonable due to external ecosystems.
4. Abandon strict CI for the entire system.
   * Rejected: Increases risk of production incidents, violates modern software engineering practices.

---

## 6. Consequences

**Positive:**
* S-CORE sticks to its CI principles while accommodating real-world constraints.
* Predictable system stability; controlled ingestion of third-party updates.
* Transparent technical debt ledger (list of non-Tier 1 components).
* Encourages upstream collaboration (move externals toward Tier 1 where possible).

**Negative:**
* Additional classification + reporting overhead.
* Tier 3 introduces release-based integration, with all its shortcomings like longer feedback loops and risk of surprise integration failures.
* Requires disciplined ownership to avoid Tier 2 stagnation.
