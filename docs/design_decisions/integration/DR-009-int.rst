..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-009-Int: Public module interfaces and derived Bazel visibility
=================================================================

- **Date:** 2026-11-11

.. dec_rec:: Public module interfaces and derived Bazel visibility
   :id: dec_rec__int__module_interface_visibility
   :status: proposed
   :version: 1
   :context: Integration
   :decision: Option 4 - Interfaces needed to build, configure and integrate target software are Public; module documentation, quality artefacts and the Feature Integration Test harness are Integration-accessible interfaces created in the module context of DR-008-int; development tools are Private

Context / Problem
-----------------

S-CORE modules are consumed in two ways:

1. **Module → module**: A module depends on another module with a regular ``bazel_dep``.
   The consumer can only use targets with matching Bazel
   `visibility <https://bazel.build/concepts/visibility>`_. Each dependency of those targets
   must also resolve in the consumer's context. The consumer never sees a ``bazel_dep``
   or ``use_extension`` that the provider marks with ``dev_dependency = True``.
2. **reference_integration → module**: ``reference_integration`` consumes modules like any other
   module, as in (1). In addition, :need:`dec_rec__int__scope_reference_integration` lets it run
   module verification in the module's own context. For that verification, reference_integration
   does not need public visibility or non-dev dependencies.

Visibility and ``dev_dependency`` are two separate Bazel settings, but they depend on each other:

* If a target is **public**, consumers can build it. All its ``deps``, ``data`` and ``load()``
  statements must therefore come from **non-dev** dependencies.
  Toolchains are an exception: they are registered by the root module. The C++ and Rust toolchain
  modules are therefore dev dependencies, and the consumer provides the toolchains.
* If a target is **private**, it can use dev-only tooling freely, but consumers cannot reach it.

So the set of public interfaces decides which supporting tool modules must be non-dev dependencies.
There is a trade-off:

* **Many public interfaces** add tooling to the dependency graph of every consumer.
  Examples are documentation, test, image and analysis tooling. This tooling is not meant for the
  embedded target, but it takes part in version resolution together with the target software.
  Tooling and target software may depend on the same module, and Minimal Version Selection then selects
  one version for both. If the required versions are incompatible, the root module must resolve the
  conflict with ``single_version_override`` or ``multiple_version_override``.
* **Few public interfaces** prevent consumers from using interfaces they need, for example mocks of a
  dependency in their own unit tests or examples in showcases.

``multiple_version_override`` allows several versions of a module to coexist, including different
major versions, for example 2.2.0 for target software and 3.0.0 for tooling. Bazel selects the version
per dependent module, not per build invocation. A build that reaches both dependency paths therefore
uses both versions. The override is only effective in the root module, so every integrator must maintain it.
Keeping tooling interfaces out of the public interfaces keeps the dependency paths of tooling and target
software separate and avoids most of these overrides.

Tool modules, for example documentation or integration test tooling, are released independently of the
target software modules:

* As **non-dev** dependencies, a tool update in one module is enforced on all downstream modules by
  Minimal Version Selection. Incompatible tool versions must be resolved with overrides in every root module.
* As **dev** dependencies, the tool version is resolved in the module context. reference_integration pins
  the versions of the tools it declares when it builds a module in the module context
  (:need:`dec_rec__int__scope_reference_integration`). Deviations are resolved there, if needed with
  ``multiple_version_override``, and not in every consumer.

S-CORE covers tools and processes as well as target software. A dev dependency does not hide a tool:
it is declared in the module's ``MODULE.bazel`` and used whenever the module is built in its module context.
reference_integration is the place where target software, tools and processes of all modules come together
for a release, with one set of tool versions. Modules that use the same tools as reference_integration can
reuse the tool qualification done for this tool set.

This decision record defines the general categories of module interfaces and the recommended Bazel
visibility for each. A module can derive its ``dev_dependency`` setting from it.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- **Minimal target dependency graph:** A consumer of a target software module only receives dependencies
  that are needed to build, configure and integrate target software.
- **Usable interfaces:** Interfaces that consumers need are usable across modules without patches.
- **Releasable combination:** reference_integration can create all quality artefacts needed to release
  a combination of modules.
- **Consistent tool set:** The tools used to create the release artefacts are defined in one place,
  with one set of versions for a release.
- **Derivable rule:** A module owner can derive ``dev_dependency`` for each ``bazel_dep`` and
  ``use_extension`` from the visibility of its targets.
- **Compatible with DR-008-int:** Module verification that reference_integration runs does not
  require public interfaces (see :need:`dec_rec__int__scope_reference_integration`).

..
   NOTE: Working notes, to be removed before this decision record is accepted.

   Snapshot of the target software modules in reference_integration known_good.json
   (baselibs, communication, persistency, kyron, lifecycle, logging, time, config_management):

   * reference_integration patches modules to restore or add public visibility for mocks,
     examples, runtime configuration files and Assumptions of Use. These are used as
     interfaces but are not public everywhere.
   * reference_integration patches modules to turn test tooling into non-dev dependencies
     (score_itf, rules_oci, score_rules_imagefs, googletest, score_sbom, score_tools).
   * The same tool module is dev in some modules and non-dev in others
     (for example score_tooling, score_itf, aspect_rules_lint, score_devcontainer).
   * Repository maintenance targets are often public (copyright, license check,
     starpls, coverage wrapper, cargo_lock, sbom, test suites).
   * score_communication keeps a golden list of its public targets
     (quality/visibility_guard), which can be used to keep visibility stable.
   * docs-as-code: external_needs and bundles reference docs() / docs_bundle targets of the
     provider. Their needs.json is generated by a Sphinx action loaded from @score_docs_as_code.
     Public documentation targets therefore require score_docs_as_code as non-dev dependency.
   * Companion modules: baselibs examples/integration/MODULE.bazel has no module() declaration yet.
     eclipse-score/bazel_registry reads MODULE.bazel from the repository root only.

Visibility Levels
-----------------

.. list-table:: Visibility levels
   :header-rows: 1
   :widths: 16 36 24 24

   * - Level
     - Definition
     - Reachable by
     - Required dependencies
   * - **Public**
     - ``//visibility:public``
     - All consumers
     - Non-dev
   * - **Integration-accessible**
     - Private visibility. Built and executed in the module context, where the module is built in its own
       repository with its dev dependencies: by the module's own CI, and by reference_integration through
       the tooling of :need:`dec_rec__int__scope_reference_integration` to create the quality artefacts
       of a releasable combination of modules.
     - The module itself, reference_integration in the module context
     - Dev
   * - **Private**
     - Private visibility. Only used during development of the module, no release artefacts.
     - The module itself
     - Dev

Interface Categories
--------------------

The table lists all interface categories with the recommended visibility level.
The comment rates the recommended level against the alternatives:
``+`` benefit, ``-`` drawback.

.. list-table:: Interface categories and recommended visibility
   :header-rows: 1
   :widths: 7 20 13 28 32

   * - ID
     - Interface
     - Visibility
     - Typical targets
     - Comment
   * - I-1
     - Library (API)
     - Public
     - ``cc_library``, ``rust_library`` forming the module API
     - | Mandatory.
       | Implementation details stay Private.
   * - I-2
     - Daemon / application binary
     - Public
     - ``cc_binary``, ``rust_binary`` deployed on the target
     - Mandatory.
   * - I-3
     - Build rules, code and configuration generators, configuration schemas
     - Public
     - Starlark rules and macros (``.bzl``), generator tools invoked by users, ``exports_files`` or
       ``filegroup`` of configuration schemas
     - | Mandatory.
       | Generator runtimes are non-dev; keep them separate from dev tool setup.
       | Runtime configuration files are not public on their own. They are provided together with I-6 or I-9a.
   * - I-4
     - Build configuration flags
     - Public / Private
     - ``bool_flag``, ``string_flag``, ``label_flag``
     - | Public for integration variants.
       | Private for development flags.
       | ``+`` Integrators select variants without patches.
       | ``-`` Each public flag is a supported variant.
   * - I-5
     - Test doubles (mocks, fakes, stubs) for provided interfaces
     - Public
     - ``testonly`` ``cc_library``, ``rust_library``
     - | ``+`` Consumers reuse test doubles maintained with the API.
       | ``-`` The unit test framework (e.g. ``googletest``) becomes a non-dev dependency.
   * - I-6
     - Examples and showcase applications, including their runtime configuration files
     - Public
     - ``cc_binary``, ``rust_binary`` demonstrating the module, ``exports_files`` of their configuration
     - | ``+`` Integrators may reuse examples in showcases.
       | ``-`` Examples must only use non-dev dependencies.
       | A companion module is a good fit: the example then references and uses the module exactly
         as a user does.
   * - I-7
     - (Platform) Stakeholder and feature requirements, architecture, Assumptions of Use
     - Public
     - Needs data of the platform and process documentation modules
     - | Provided by documentation modules, not by target software modules.
       | Target software modules use them as dev dependency.
   * - I-8
     - (Module) Component requirements, architecture, Assumptions of Use
     - Integration-accessible
     - ``docs``, ``docs_bundle`` and their needs data
     - | ``+`` Documentation tooling stays dev; modules may use their own tooling to create the documentation.
       | ``+`` Promotes the use of reference_integration tooling which is intended for full qualification of module combinations.
       | ``-`` A module cannot link to the needs of another target software module in its own documentation build.
   * - I-9a
     - Test applications, including their runtime configuration (Feature Integration Tests)
     - Public
     - | ``testonly`` ``cc_binary``, ``rust_binary`` test applications. ``cc_test``, ``rust_test`` test applications with pass criteria.
       | ``exports_files`` configuration files which are coupled to the implementation of the test applications.
     - | ``+`` Integrators may reuse test applications with their own test harness.
       | ``-`` Test application may pull in further non-dev dependencies.
   * - I-9b
     - Feature Integration Test harness
     - Integration-accessible
     - Test rules, test environments, image creation and image test tooling (e.g. ``score_itf``, ``score_rules_imagefs``)
     - | ``+`` Tooling beyond the standard S-CORE tools does not affect the consumer graph.
       | ``+`` Promotes the use of reference_integration tooling which is intended for full qualification of module combinations.
       | ``-`` Other users than the reference_integration need to provide their own test harness.
   * - I-10
     - Module quality artefacts
     - Integration-accessible
     - ``cc_test``, ``rust_test``, ``py_test``, component integration tests, unit tests and their harness,
       coverage reports, static code analysis results (for example CodeQL), traceability checks
     - | ``+`` Test, coverage and analysis tooling do not affect the consumer graph.
       | ``+`` Promotes the use of reference_integration tooling which is intended for full qualification of module combinations.
       | ``-`` Modules releases are limited to their own quality artefacts. Combination of dependency versions are not fully qualifable in the module context.
   * - I-11
     - SBOM, license scan, software composition analysis
     - Integration-accessible
     - SBOM generation, dependency license and vulnerability scans
     - | ``+`` SBOM and scan tooling do not affect the consumer graph.
   * - I-12
     - Development tools
     - Private
     - Linters (e.g. ``clang-tidy``, ``rust-clippy``), formatters (e.g. ``clang-format``), copyright header checks,
       compiler warning policies (toolchain settings), IDE support, language servers, live preview
     - | ``+`` Clean consumer graph.
       | ``+`` Not rerun by reference_integration, results are not release relevant.

Companion modules
^^^^^^^^^^^^^^^^^

This decision record does not decide whether modules use companion modules. The visibility level is the
decision. A companion module is an optional implementation hint for Public interfaces that need
non-target dependencies.

A companion module is a second Bazel module in the same repository, in a subdirectory with its own
``MODULE.bazel``, named for example ``score_baselibs_examples``. It could be released from the same tag
with the same version as the main module and depends on it with a regular ``bazel_dep``. Consumers that only
use it for testing declare it as a dev dependency. Its non-dev dependencies then stay out of the main
module's dependency graph.

* **Candidates:** I-5 and I-6 are a good fit, see the interface categories table.
* **Feasibility:** Bazel registries support several modules from one repository and release. The
  ``source.json`` of a module version can set ``strip_prefix`` to a subdirectory, as used by the Bazel
  Central Registry for ``rules_python`` and ``rules_python_gazelle_plugin``. The S-CORE Bazel registry
  tooling currently expects ``MODULE.bazel`` at the repository root and would need an extension.
* **Releases:** Companion modules are not released today. Releasing them would require a registry entry
  per companion module and a release process that keeps the versions of both modules identical.
  Bazel does not enforce this: Minimal Version Selection only guarantees that the main module is at
  least the version required by the companion module.

Options Considered
------------------

All options keep I-1 to I-6, I-7 and I-9a **Public** and I-12 **Private**. They differ in which interfaces
required for generating the release quality artefacts are made **Private** (**Integration-accessible**).

Option 1: All release relevant artefacts public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Everything that is relevant for the release is Public, including the Feature Integration
Test harness (I-9b), module documentation (I-8), module quality artefacts (I-10) and SBOM (I-11).
There is no Integration-accessible level.

* ``+`` Every consumer can create all release artefacts of a module without additional tooling
* ``+`` Minimal Version Selection aligns tool versions across all modules automatically
* ``-`` Test, coverage, analysis, SBOM, documentation and Feature Integration Test tooling become non-dev
  dependencies of every target software module, including module-specific test add-ons
* ``-`` A tool update in one module is enforced on all downstream modules
* ``-`` Contradicts :need:`dec_rec__int__scope_reference_integration`

Option 2: Module quality artefacts (I-10, I-11) private
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Module quality artefacts and SBOM (I-10, I-11) are Integration-accessible. The Feature Integration Test harness
(I-9b) and module documentation (I-8) stay Public.

* ``+`` Coverage, static analysis and SBOM tooling stay dev
* ``+`` Every consumer can run the Feature Integration Tests of a module
* ``+`` A module's own documentation build can link to the needs of other target software modules
* ``-`` Because tests can be executed from outside the module, every test add-on used by the Feature
  Integration Tests becomes a non-dev dependency. This is not limited to the standard S-CORE test tools.
* ``-`` Test harness, image and documentation tooling updates are enforced on all downstream modules

Option 3: Module quality artefacts and test harness (I-9b, I-10, I-11) private
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As Option 2, and the Feature Integration Test harness (I-9b) is Integration-accessible as well.
Module documentation (I-8) stays Public.

* ``+`` No test tooling and no module-specific test add-on enters the consumer graph
* ``+`` A module's own documentation build can link to the needs of other target software modules
* ``-`` Documentation tooling updates are enforced on all downstream modules

Option 4: Documentation, module quality artefacts and test harness (I-8, I-9b, I-10, I-11) private
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As Option 3, and module documentation (I-8) is Integration-accessible as well. This matches the interface
categories table.

* ``+`` The consumer graph contains target dependencies, generator runtimes and test libraries only
* ``+`` All tools used for release artefacts are aligned in reference_integration. Tool updates and
  deviations are handled there and not in every consumer (``multiple_version_override``).
* ``+`` Modules can adopt tool updates independently. They become effective for the release when
  reference_integration adopts them.
* ``-`` A module's own documentation build is limited toresolve links to platform needs (I-7).

Other alternatives were discarded:

* **Consumer-side patches** (``single_version_override`` with patches): Every consumer maintains its
  own visibility changes. This does not scale and hides the interface definition from the module owner.

Comparison
----------

.. list-table:: Options comparison
   :header-rows: 1
   :widths: 32 17 17 17 17

   * - Criterion
     - Option 1
     - Option 2
     - Option 3
     - Option 4
   * - Tooling in the consumer dependency graph
     - Documentation, test harness, test, analysis and SBOM tooling
     - Documentation, test harness and image tooling
     - Documentation tooling
     - Generator runtimes and partly test libraries (I-5, I-9a) only
   * - Module-specific test add-ons in the consumer dependency graph
     - Yes
     - Likely
     - No
     - No
   * - Risk of version conflicts between tooling and target software
     - High
     - Medium
     - Medium
     - Low
   * - Where tool version updates and deviations are resolved
     - Every module
     - Every module (test harness, documentation)
     - Every module (documentation)
     - reference_integration
   * - Conflicts with existing module setups
     - High
     - Medium
     - Medium
     - Low
   * - Cross-module documentation links in a module's own documentation build
     - Yes
     - Yes
     - Yes
     - No, only from module to platform needs (I-7)
   * - Effort in reference_integration
     - Low
     - Medium
     - Medium
     - Medium

Decision
--------

..
   NOTE: REMOVE ME before this decision record is accepted.

   In general, there is no preference between Option 3 and Option 4. However,
   score_communication would benefit from Option 4 because it uses a different documentation
   build approach: sphinx_module from score_tooling with rules_python Sphinx support,
   rather than the docs()/docs_bundle interface consumed by reference_integration.
   Option 4 allows this module-context approach to be retained without requiring a Public
   documentation interface. This consideration tips the personal preference towards Option 4;
   it does not remove the need to adapt documentation consumption in reference_integration.

**Option 4** is recommended. **Option 3** is the alternative if links to the needs of other target software
modules must be resolved in each module's own documentation build.

Derived dev_dependency rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each ``bazel_dep`` and ``use_extension`` in a ``MODULE.bazel`` file:

1. If a **Public** target needs the dependency through ``deps``, ``data`` or ``load()``,
   the dependency is **non-dev**.
2. Otherwise, it is ``dev_dependency = True``. This covers all dependencies of **Integration-accessible**
   and **Private** targets.
3. Toolchain modules (for example C++ and Rust toolchains) are always ``dev_dependency = True``.
4. Non-dev dependencies are limited to target dependencies, ``rules_cc``, ``rules_rust``, ``platforms``,
   ``bazel_skylib``, generator runtimes (I-3) and test libraries for I-5 and I-9a.
   Any other non-dev dependency must be justified in the module documentation.
5. If a companion module is used, rules 1 to 4 apply to each module separately.

As a result, documentation, test framework, coverage, analysis, SBOM, development tool and toolchain
modules are dev dependencies, for example ``score_docs_as_code``, ``score_tooling``, ``score_itf``,
``score_coverage`` and ``aspect_rules_lint``.

Consequences
------------

* Modules review their targets against the interface categories, set the default visibility to private
  and set ``dev_dependency`` according to the derived rule.
* reference_integration creates the release artefacts of all Integration-accessible interfaces
  (I-8, I-9b, I-10, I-11), partly through the tooling of :need:`dec_rec__int__scope_reference_integration`.
  Development tools (I-12) are not rerun.
* reference_integration defines the tool versions used for release validation and propagates applicable
  version constraints into module-context builds. Deviations are resolved centrally, using version
  overrides, including ``multiple_version_override`` where needed. Module-local development versions
  may differ.
* The documentation path for cross-module linking is discarded. Module documentation links only to
  platform needs (I-7), not to the needs of other target software modules. The existing module-context
  build and publication of dependable-element documentation remain unchanged. The main documentation
  build in reference_integration currently consumes module ``docs_bundle`` targets as Bazel dependencies;
  making these targets Private requires adapting that consumption path.
