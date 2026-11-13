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

The problem has a structural subtlety that any solution must respect: **a
considerable number of S-CORE modules are libraries**, not long-running services. A library's
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
  that **fails the build with a descriptive message**. Inside the test module
  the binding point and its fail-closed default look like this:

  ```python
  # @score_compatibility_test_suite//time/BUILD.bazel

  load("@score_compatibility_test_suite//:unbound.bzl", "unbound_binding")

  # Fail-closed default: errors at build time until the root module binds it.
  unbound_binding(
      name = "time_api.unbound",
      message = "SCTS binding 'time_api' is unbound. Bind it in your root " +
                "MODULE.bazel: compliance.bind(time_api = \"@<impl>//time:api\").",
  )

  # The binding point the distribution overrides.
  label_flag(
      name = "time_api",
      build_setting_default = ":time_api.unbound",
  )

  # Conformance program compiled + linked against whatever 'time_api' resolves
  # to. Compiling proves the source API; linking proves the symbols/ABI.
  cc_test(
      name = "time_api_conformance",
      srcs = ["time_api_conformance.cc"],
      deps = [":time_api"],  # the label_flag is consumed as a normal dependency
  )
  ```

  ```python
  # @score_compatibility_test_suite//:unbound.bzl

  def _unbound_impl(ctx):
      # Any attempt to build an unbound binding stops the build.
      fail(ctx.attr.message)

  unbound_binding = rule(
      implementation = _unbound_impl,
      attrs = {"message": attr.string(mandatory = True)},
  )
  ```

- The distribution binds each point to its own target, e.g. in its root
  `MODULE.bazel`:

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
