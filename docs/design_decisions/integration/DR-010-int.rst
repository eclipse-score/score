..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-010-Int: Standard umbrella targets for S-CORE modules
========================================================

- **Date:** 2026-10-09

.. dec_rec:: Standard umbrella targets for S-CORE modules
   :id: dec_rec__int__module_umbrella_targets
   :status: proposed
   :version: 1
   :context: Integration
   :decision: Option 1

Context / Problem
-----------------

An S-CORE module (e.g. ``score_baselibs``, ``score_communication``, ``score_logging``) consists of
many Bazel packages and targets; ``score_baselibs`` alone has on the order of 150 ``cc_library``
rules. There is no convention that tells a consumer which of those targets are shipping libraries,
shipping executables, unit tests or integration tests. As a consequence:

* ``reference_integration`` enumerates module targets by hand to build the stack and to run the
  module-scoped validation stage of :need:`dec_rec__int__scope_reference_integration`.
* Platform-specific targets (QNX-only, Linux-only, ``select()``-guarded) are reconstructed by each
  consumer.
* Without an explicit list of shipping targets, it is hard to check whether a coverage figure
  covers all shipping code.
* A newcomer cannot tell from the build files what a module provides.

This decision record defines **where** and **how** a module declares its shipping C++ libraries,
C++ binaries, C++ unit tests and C++ component integration tests, so that consumers reach each set
through one well-defined entry point.

Motivation
^^^^^^^^^^

- **Unified entry to a module.** One label per set, identical in every module, instead of
  enumerating sub-targets. This is the Bazel equivalent of using a package as a whole, as in
  Python ``import os`` or a CMake ``Foo::Foo`` target.
- **Variants handled once.** Platform-specific targets are resolved in the module, not in every
  consumer.
- **Table of contents.** Reading the umbrella shows what the module ships and what it deliberately
  does not.
- **Generic CI.** ``bazel build //score:libs //score:bins`` and ``bazel test //score:unit_tests``
  work the same for every module. Wildcards such as ``//...`` also pick up examples, tooling and
  mocks.
- **Separate test levels.** Distinct unit and integration test suites allow separate CI stages and
  per-level results and coverage, the granularity at which verification evidence is collected.
- **Auditable coverage scope.** The coverage setup in ``reference_integration`` (``code_root_path``,
  excluded tests) selects what is instrumented, but is not an authoritative list of shipping code.
  The umbrellas provide that reference set; they do not by themselves guarantee full coverage.
- **Stable across refactorings.** Internal packages can move or split without breaking consumers
  of the umbrellas.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- **Single entry point**: Each of the four sets is reachable in the same way in every module.
- **Explicit shipping surface**: It is auditable which targets ship and which do not (mocks, fakes,
  examples, tooling).
- **Platform variants**: Consumers do not re-implement platform selection.
- **Ownership**: The sets are maintained by the module team, in sync with the module's BUILD files.
- **Reusability**: Usable by ``reference_integration``, other consumers and the module's own CI.
- **Low maintenance**: Changing a target requires as few changes in as few repositories as
  possible.
- **Extensibility**: A later decision on module-level shared libraries is not blocked.

Non-Goals
~~~~~~~~~

- **Shared libraries** (e.g. one ``cc_shared_library`` per module) are left to a separate decision
  record; the options are only evaluated on whether they enable it.
- **Rust** targets need a separate decision, which may extend the labels defined here or introduce
  separately named targets. Coverage claims for a whole module must still account for shipping Rust
  code outside these umbrellas.
- Packaging of third-party dependencies, Feature Integration Tests (they remain in
  ``reference_integration`` per :need:`dec_rec__int__scope_reference_integration`), and changes to
  build flags, toolchains or existing module targets.

Options Considered
------------------

Option 1: Standard umbrella targets in each module's ``score/BUILD`` (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every S-CORE module adds four targets with **fixed names** to ``score/BUILD``, so any module can be
addressed generically, e.g. ``@score_baselibs//score:libs``:

.. list-table:: Standard umbrella targets
   :header-rows: 1
   :widths: 30 25 45

   * - Label
     - Rule
     - Content
   * - ``//score:libs``
     - ``filegroup`` or ``cc_library``
     - All shipping C++ libraries (component ``cc_library`` targets).
   * - ``//score:bins``
     - ``filegroup``
     - All shipping C++ executables (``cc_binary``).
   * - ``//score:unit_tests``
     - ``test_suite``
     - All C++ unit tests.
   * - ``//score:integration_tests``
     - ``test_suite``
     - All C++ component integration tests.

The form of ``libs`` follows the shape of the module:

* **filegroup** for a collection of independent components (e.g. ``score_baselibs``,
  ``score_time``). It bundles the components for building, CI and review, but provides no
  ``CcInfo``: consumers that link still depend on the component libraries, which stay visible to
  them. In this form the umbrella mainly serves CI and auditability, not linking.
* **cc_library** for one cohesive library that needs a linkable entry point usable in ``deps``. If
  ``layering_check`` is enabled, consumers may only include headers of direct dependencies, so the
  umbrella has to export the public headers itself (e.g. an umbrella header in ``hdrs``).

Example ``score_baselibs`` (excerpt):

.. code-block:: python

   # Standard umbrella targets, see DR-010-int.
   # A target ships if it is listed here or is a transitive dependency of a
   # listed target within this module. Mocks, fakes, examples and tooling are
   # intentionally excluded.

   filegroup(
       name = "libs",
       srcs = [
           "//score/bitmanipulation:bitmanipulation",
           "//score/bitmanipulation:bitmask_operators",
           # :concurrency pulls the rest of score/concurrency transitively.
           "//score/concurrency:concurrency",
           "//score/result:result",
           # ...
       ],
       visibility = ["//visibility:public"],
   )

   filegroup(
       name = "bins",
       srcs = [],  # Intentionally empty: no shipping executables.
       visibility = ["//visibility:public"],
   )

   test_suite(
       name = "unit_tests",
       tests = [
           "//score/bitmanipulation:unit_test_suite_host",
           "//score/concurrency:unit_test_suite_host",
           # ...
       ],
   )

   test_suite(
       name = "integration_tests",
       # Intentionally empty. tests = [] would expand to all tests in //score,
       # so a tag that no test carries is used instead.
       tags = ["score_no_tests"],
   )

Rules:

* **Shipping set**: everything listed in ``libs`` or ``bins`` plus its transitive dependencies
  within the module. Anything else in the module does not ship.
* **Platforms**: libraries and binaries are added behind ``select()``. ``test_suite.tests`` cannot
  contain a ``select()``, so the test suites list all tests, and platform-specific tests use
  ``target_compatible_with``; ``bazel test`` skips incompatible tests in a suite.
* **Empty sets**: an empty ``libs`` or ``bins`` is a ``filegroup`` with ``srcs = []``; an empty test
  suite uses a tag filter that matches no test (see example). ``bazel test`` on an empty suite exits
  with code 4, which generic CI treats as "no tests".
* **Aggregate only**: umbrellas compile no code of their own (except an umbrella header required by
  ``layering_check``). Fine-grained component targets keep Bazel caching effective and let
  consumers depend on parts of a module.
* **Drift check (mandatory)**: module CI fails if a library or binary in the module is neither in
  the shipping set nor on an explicit list of non-shipping targets, e.g. by checking that
  ``bazel query 'kind("cc_(library|binary)", //score/...) except deps(//score:libs + //score:bins)'``
  only returns listed non-shipping targets. ``query`` covers all ``select()`` branches; use
  ``cquery`` for a per-platform check. Without this check the hand-maintained lists drift, and the
  shipping-surface and coverage claims above no longer hold.
* **Test dependencies**: tests usually depend on ``dev_dependency`` repositories (e.g. GoogleTest),
  which are not visible when the module is not the root module. The test suites therefore mainly
  run in the module's own CI.

Modules without a ``score`` package create ``score/BUILD``. If ``score/`` already contains files
owned by a parent package, this adds a package boundary: labels such as ``//:score/...``, globs and
``exports_files`` reaching into ``score/`` must move into the new package once. Otherwise the change
is additive and can be reverted by deleting the four targets.

Pros:

* One uniform label per set and module for ``bazel build`` and ``bazel test``, and in the
  ``cc_library`` form also for ``deps``
* The list lives next to the code and is updated in the same pull request
* Explicit, reviewable shipping surface, with platform variants resolved once in the module
* Usable by the module's own CI, ``reference_integration`` and every other consumer
* No build or caching overhead
* Enables a later ``cc_shared_library`` on ``//score:libs`` or its components

Cons:

* Requires a change and agreement in every module repository, plus a package migration where
  ``score/BUILD`` does not exist yet
* Lists are maintained by hand, and every module has to run the drift check in CI
* The ``filegroup`` form mainly helps CI and auditing: linking consumers still depend on component
  libraries and are not shielded from internal restructuring
* The generic names cover only C++ for now; a later Rust decision must extend or avoid them

Option 2: Module teams maintain their umbrella targets in ``reference_integration``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The same four sets are defined in ``reference_integration``, one package per module (e.g.
``modules/score_baselibs/BUILD``), owned by the module team via ``CODEOWNERS`` and referencing
external labels such as ``@score_baselibs//score/concurrency:concurrency``.

Pros:

* No change in the module repositories and no agreement of module teams needed, so it can start
  immediately
* All definitions in one place, adaptable independently of module releases

Cons:

* The list lives in another repository; drift is only detected when ``reference_integration``
  updates the module, and adding a target needs pull requests in two repositories
* All referenced component targets must be public
* Not usable in the module's own CI; other consumers would have to depend on
  ``reference_integration``
* A later shared library would be owned by ``reference_integration``, not by the module

Option 3: Tag targets in the module and collect them with ``bazel query``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no aggregate target. Each target carries a classifying tag (``score-lib``, ``score-bin``,
``score-unit-test``, ...), and consumers collect the sets, e.g.:

.. code-block:: bash

   bazel query 'attr(tags, "\bscore-lib\b", @score_baselibs//score/...)'
   bazel test --test_tag_filters=score-unit-test @score_baselibs//score/...

Pros:

* No central list; a tagged target is picked up automatically
* Uses existing Bazel features only

Cons:

* A query result is not a label and cannot be used in ``deps``; consumers need a generation step
* Platform-specific sets require ``cquery`` per platform
* Without a CI check, missing or misspelled tags silently drop targets (the same applies to
  forgotten entries in Option 1 lists; both need a check)
* The shipping surface is only visible by running a query
* Every target has to be tagged once (macros can set defaults)
* Shared libraries are only possible via generated targets

Comparison
----------

.. list-table:: Umbrella target options comparison
   :header-rows: 1
   :widths: 28 24 24 24

   * - Criterion
     - Option 1 (in module)
     - Option 2 (in reference_integration)
     - Option 3 (tags + query)
   * - Dependable Bazel label
     - Yes (in ``deps`` only as ``cc_library``)
     - Only inside ``reference_integration``
     - No, needs generation
   * - Drift risk
     - Low (same PR, mandatory CI check)
     - High (cross-repository)
     - Low with a CI check, silent loss without
   * - Platform variants
     - Resolved once in the module
     - Resolved once
     - ``cquery`` per platform
   * - Usable in module CI / by other consumers
     - Yes / Yes
     - No / Via ``reference_integration``
     - Yes / With own tooling
   * - Component visibility
     - Unchanged (``filegroup``: linked components stay public)
     - Public
     - Public for generated targets
   * - Effort
     - Low, one-time plus list upkeep
     - Upkeep in a second repository
     - Tag every target, plus tooling
   * - Enables shared libraries
     - Yes, owned by the module
     - Yes, owned by ``reference_integration``
     - Only via generated targets

Evaluation
----------

Option 1 puts the definition of what a module ships where that knowledge exists, and is the only
option that meets all goals: one uniform entry point for ``reference_integration``, other consumers
and the module's own CI, platform variants resolved once, and a ``libs`` form that fits each
module's shape. Its main cost, keeping the lists up to date, is limited because they change in the
same pull request as the code and the mandatory drift check catches forgotten targets. Its main
risk is adoption: it needs agreement and a change in every module repository.

Option 2 needs no module team agreement and can start immediately, but moves the list away from the
code, which reintroduces drift, forces targets to become public and helps only
``reference_integration``.

Option 3 can detect drift as well as Option 1 when combined with a CI check. The deciding difference
is that a query result is not a label: it cannot be built, tested or linked as one target, and
platform variants need ``cquery``. Tags or queries remain useful to implement the Option 1 drift
check.

**Rollout:** Modules adopt Option 1 one by one. Until a module provides its umbrella targets,
``reference_integration`` may keep an interim definition for it in the style of Option 2. That
definition is removed once the module ships its own ``score/BUILD`` umbrellas, so there is never
more than one authoritative list per module.

**Recommendation:** Option 1. Each S-CORE module provides the standard C++ targets ``//score:libs``,
``//score:bins``, ``//score:unit_tests`` and ``//score:integration_tests`` in ``score/BUILD``.
Shared libraries will be addressed in a separate decision record that builds on ``//score:libs``.
