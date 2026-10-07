<!--
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
-->

# DR-010-Strat: S-CORE Compatibility Test Suite (SCTS) — Overview

- **Date:** 2026-10-07

```{dec_rec} S-CORE Compatibility Test Suite (SCTS) — Overview
:id: dec_rec__strat__scts_overview
:status: draft
:tracking: <GitHub issue URL — required once a Shepherd is confirmed>
:context: There is no portable, reusable way for a distribution other than reference_integration to prove that it is "S-CORE compliant" — that the expected modules, public APIs and functional workflows are actually present and behave as specified.
:decision: Establish the S-CORE Compatibility Test Suite (SCTS) as a separately versioned Bazel test module that a distribution consumes as a dependency and runs in two stages — Stage 1 build/link + label-binding conformance, Stage 2 runtime conformance on a deployed image.
:version: 1
```

---

## Context / Problem

`reference_integration` is the canonical S-CORE integration, but it is only *one*
distribution. Commercial and downstream distributions that are comparable to
`reference_integration` (their own images, possibly their own certified or
optimized module builds) currently have **no portable way to demonstrate S-CORE
compliance**. "Compliance" here means three concrete, testable claims:

1. **Presence** — the expected set of S-CORE modules is part of the distribution
   at the expected versions/capabilities.
2. **API surface** — the expected public APIs of those modules exist and are
   source/ABI compatible with the S-CORE contract.
3. **Behavior** — the expected functional workflows behave as specified.

The problem has a structural subtlety that any solution must respect: **most
S-CORE modules are libraries**, not long-running services. A library's
compatibility is a *build/link-time* property, not something that can be observed
by deploying a binary and watching it call APIs across a process boundary — a
missing or changed symbol prevents the consumer from *linking* in the first
place. Only a subset of modules (communication/IPC, datarouter, lifecycle,
SOME/IP) expose a genuine runtime/wire boundary.

A second structural subtlety concerns Bzlmod: in a Bazel module graph, only the
**root module** governs resolved module versions and overrides. A test suite that
declares the modules-under-test as its own `bazel_dep`s and is built standalone
would silently test the *registry* versions it pulls in itself — not the
distribution's integrated set. Any solution must make it impossible to pass
*vacuously* through misconfiguration.

## Decision

Introduce the **S-CORE Compatibility Test Suite (SCTS)** as a dedicated,
separately versioned **Bazel test module** (`score_compatibility_test_suite`,
hosted in its own repository and published to the S-CORE registry). A
distribution proves compliance by adding SCTS as a dependency of its **root**
module and running a well-known set of test targets. SCTS owns the normative
contract; the distribution supplies its implementation through a small, explicit,
**fail-closed** binding surface.

SCTS is organized in **two stages** that map onto the two kinds of compatibility:

### Stage 1 — Build & Bind conformance (static)

Proves **presence** and **API surface** without needing a running target.

- For **library** modules, the suite ships conformance programs/targets written
  against the *normative* public API. The compatibility check **is** whether
  those programs compile and link against the distribution's modules:
  compiling proves the source API; linking proves the symbols/ABI.
- The suite **never names a module-under-test with its own `bazel_dep`**.
  Instead it exposes **binding points** (Bazel `label_flag`s, e.g.
  `time_api`, `kvs_api`, `logging_api`) whose default is an `unbound` target
  that **fails the build with a descriptive message**. The distribution binds
  each point to its own target, e.g. in its root `MODULE.bazel`:

  ```python
  compliance = use_extension("@score_compatibility_test_suite//:bind.bzl", "compliance")
  compliance.bind(
      time_api    = "@score_time//time:api",
      kvs_api     = "@acme_persistency//kvs:api",   # a fork is allowed
      logging_api = "@score_logging//log:api",
  )
  ```

- Because apparent repo names resolve **only** in the root module's repository
  mapping, a binding to a module the distribution has not declared as a
  dependency (or overridden) is a **hard Bazel error**, never a silent registry
  fetch. Misconfiguration therefore **fails closed** instead of passing
  vacuously.
- A presence/provenance check (derived from a normative compatibility baseline,
  itself generated from the S-CORE known-good module set) asserts that the
  distribution's **root** graph actually provides each required module, and
  records the *actually resolved* artifact (repo + version/commit) each
  conformance target bound to, so a vacuous or mis-pointed run is **visible in
  the report** rather than silently green.

### Stage 2 — Runtime conformance on an image (dynamic)

Proves **behavior**. The distribution builds a target image (as
`reference_integration` does today). SCTS conformance applications — the same
ones that already linked successfully in Stage 1 for libraries, plus black-box
clients for the service/wire modules — are deployed to that image and executed
(including on QNX via the existing QEMU/ITF flow). They assert observable
behavior and, for service modules, exercise the IPC/SOME-IP **wire contract**
across the process boundary.

Each conformance test links to the stakeholder requirement(s) it verifies
(`stkh_req__…`) using the established `@add_test_properties(partially_verifies=…)`
mechanism, so results aggregate into a per-requirement **conformance report** —
the distribution's compatibility evidence.

The contract is defined at the **artifact boundary** (named libraries/headers and
images bound via the injection surface), *not* at the build-method boundary: a
distribution does **not** have to reproduce `reference_integration`'s
`known_good.json`/override topology. How it produces the bound artifacts is its
own concern.

## Backwards Compatibility

SCTS is additive and introduces no breaking change to existing modules or to
`reference_integration`. `reference_integration` becomes the **first consumer**
(reference binding) of SCTS, which doubles as the suite's own self-test. SCTS is
semantically versioned as an independent contract: adding conformance tests is a
minor bump; changing or removing a contract point is a major bump. A distribution
claims compliance against a specific SCTS version.

## Alternatives Considered

- **Keep compliance implicit in `reference_integration`.** Rejected: it only
  validates `reference_integration` itself and provides no portable, reusable
  conformance artifact for other distributions.
- **Suite declares the modules-under-test as its own `bazel_dep`s and is built
  standalone.** Rejected: the suite would be the Bazel *root* and would test the
  registry versions it pulls in, not the distribution's integrated set — a
  vacuous pass (the core failure mode this DR must prevent).
- **Pure runtime/black-box testing for all modules** ("deploy an app that calls
  everyone's APIs"). Rejected as the sole mechanism: it cannot detect
  library-level API/ABI incompatibility, which manifests at link time, not at
  runtime.
- **ABI-baseline diffing (`abidiff`) as the primary API check.** Deferred: only
  relevant if distributions ship *prebuilt binaries* linked by third parties
  without recompilation. In the current from-source Bzlmod model, compilation of
  the conformance programs already proves source/API compatibility.

## Rationale

- **Two stages because there are two kinds of compatibility.** Build/link-time
  for libraries (the majority), runtime/wire for services. One mechanism cannot
  cover both; conflating them is the root of the "how do I test a library?"
  confusion.
- **Root-module governance makes the test real.** By relying on Bzlmod diamond
  unification (the root distribution wins version/override), the conformance
  programs are forced to build against the distribution's actual modules — but
  only when SCTS runs *embedded in the distribution as root*, which is exactly
  how it is consumed.
- **Fail-closed by construction over trust in discipline.** The suite names no
  module; unbound = build error. This removes the "test downloaded something past
  the root" failure mode without relying on the distributor configuring overrides
  correctly, and keeps the manual binding surface minimal and self-enforcing (you
  can only *claim* to provide `time` if `time` is genuinely in your root graph).
- **Contract at the artifact boundary** decouples conformance from a
  distributor's internal build methodology, which a compatibility program must
  not dictate.
- **Reuse of existing machinery.** Stakeholder-requirement traceability
  (`partially_verifies` → `testlink` → verification report), the multi-toolchain
  images, and the QEMU/ITF runtime harness already exist and are adopted directly.

## Consequences

### Effective on acceptance

- S-CORE commits to a portable compatibility contract delivered as an independent,
  versioned Bazel test module, with `reference_integration` as its reference
  consumer and self-test.
- The normative compatibility baseline (required module set + public-API manifest)
  becomes an owned S-CORE artifact, derived from the known-good module set, and is
  governed separately from any single distribution.
- Compliance verdicts are defined against the **actually resolved artifacts**
  (recorded provenance), not against configuration intent.

### Implementation (tracked as issues after acceptance)

None of the following block acceptance of this overview DR; they are tracked as
follow-up issues and, where they fix a mechanism, as dedicated follow-up DRs.

| Work item | Description |
|---|---|
| SCTS module skeleton | New repository + `score_compatibility_test_suite` module, registry entry, `//bindings` package with `label_flag`s and the fail-closed `unbound` target. |
| `compliance.bind()` extension | Module extension providing a single binding surface with a completeness assertion over all required contract points. |
| Stage 1 baseline generator | Tool deriving the normative compatibility baseline (module set + min versions) from the known-good set; presence + provenance check. |
| Stage 1 library conformance targets | Per-module compile/link conformance programs against the normative public API (start with one library module, e.g. persistency KVS). |
| Stage 2 runtime harness | Lift the existing `platform_integration_tests` into SCTS behind the binding surface; wire into the image/ITF flow. |
| Service/wire conformance | Black-box clients for communication/IPC, lifecycle, SOME/IP exercising the wire contract. |
| Conformance report / certificate | Per-`stkh_req` pass/fail report with recorded artifact provenance as the distribution's compatibility evidence. |
| Governance | Define how a distribution submits a signed, reproducible conformance report and the terms under which it may claim "S-CORE compliant". |

## Rejected Ideas

- **A single monolithic conformance application linking every module.** Too
  brittle; one unrelated API change breaks the whole suite. SCTS uses per-module
  conformance targets instead.
- **Forcing distributions to adopt `known_good.json` / the `reference_integration`
  override topology.** Rejected: the contract is at the artifact boundary, not the
  build-method boundary.
- **Relying purely on technical means to prevent a *malicious* distributor from
  binding a doctored implementation.** Out of scope for the technical design;
  addressed through governance (signed, reproducible reports and trademark/claim
  terms), as is standard for compatibility kits.
