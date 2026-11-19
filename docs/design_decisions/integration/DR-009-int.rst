..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-009-Int: Need for a reference_integration repository
=======================================================

- **Date:** 2026-10-06

.. dec_rec:: Need for a reference_integration repository
   :id: dec_rec__int__need_reference_integration
   :status: accepted
   :version: 1
   :context: Integration
   :decision: reference_integration is required

Context / Problem
-----------------

S-CORE is a platform, not a marketplace of independently shipped modules
(:need:`dec_rec__strat__consistent_stack_vs_reference`). A platform must prove that its
modules work together as one stack. Without a single place that integrates all modules,
there is no evidence that a consistent, consumable stack exists at any point in time.

:need:`dec_rec__int__scope_reference_integration` defines *what* runs in
``reference_integration``. This record states *why* the repository must exist at all.

Decision
--------

S-CORE maintains a ``reference_integration`` repository that integrates all modules
together. It is the single place where the full stack is resolved, built, tested, and
documented as one artifact.

Rationale
---------

Consistent stack, not a module marketplace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A marketplace ships modules in isolation and leaves integration to the consumer. S-CORE
instead delivers a validated full stack. This requires one integration point that owns
the combined state of all modules. This applies not only to functional modules but
equally to the tooling modules S-CORE provides: tooling and functional modules go hand in
hand and must be resolved, built, and validated together as one consistent stack.

Avoid dependency hell
^^^^^^^^^^^^^^^^^^^^^^^

Without a common integration, an integrator or distribution creator must discover by hand
which module versions are mutually compatible. Modules migrate across breaking changes at
different times: module A moves to a new major of a shared dependency while module B stays
on the old one. The result is contradictory, unsatisfiable dependency sets.
``reference_integration`` pins one known-good set of module versions, so a matching
combination always exists and is published.

One tooling and infrastructure baseline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All modules using the same tooling and infrastructure in the same version is a key idea
of S-CORE. ``reference_integration`` also enforces that modules use the same tooling and
infrastructure provided by S-CORE. If modules diverge on build, test, analysis, or
documentation tooling, or their version, the integrator and any downstream stack must
understand, maintain, and qualify multiple tools that serve the same purpose. A shared
baseline removes this duplicated overhead.

Modules expose a public interface for re-verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bazel recomputes the final dependency set from the combined requirements of all modules.
The versions resolved in the integrated stack can differ from those a module resolved in
isolation. A changed dependency version can break feature tests, integration tests, and
even unit tests. Modules must therefore provide a public interface that lets the
integrator re-execute unit, component, and integration tests in the integrated
environment and confirm they still hold against the actually resolved dependencies.

Consequences
------------

- Every module is reachable and buildable from ``reference_integration``.
- Modules keep their public dependency footprint minimal and expose re-runnable tests.
- Module-local tooling choices are subordinate to the shared S-CORE baseline.
