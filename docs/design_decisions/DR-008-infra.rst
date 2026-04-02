..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-008-Infra: Documentation Modularity
=======================================

.. dec_rec:: Modularize docs
   :id: dec_rec__infra__docs_modularity
   :status: proposed
   :context: Infrastructure
   :decision: tbd

Context and Problem
-------------------

S-CORE aims to provide modules that can be smoothly integrated into safety-relevant
ECU projects. To support this, S-CORE modules must provide their users with well-defined
artifacts that clearly describe the content of a
`dependable element <https://github.com/eclipse-score/process_description/blob/main/process/glossary/index.rst>`_.
The existing documentation build concept does not properly support this.

A solution for overcoming these limitations is shown in
`tooling PR #95 <https://github.com/eclipse-score/tooling/pull/95>`_.
It improves the modularity of documentation and allows modules to be built
hermetically by leveraging the features that Bazel provides as a build system.

Limitations of the Current Approach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current documentation build is driven by ``src/incremental.py`` — a single entry
point shared by multiple ``py_binary`` targets. It deliberately escapes the Bazel
sandbox by reading ``BUILD_WORKSPACE_DIRECTORY`` and writing Sphinx output directly
into the workspace's ``_build/`` directory, including deleting a cache file
(``score_source_code_linker_cache.json``) as a side effect. As a result, these targets
only function via ``bazel run``, never ``bazel build``, and parallel invocations can
race on shared workspace state.

This compromises the following fundamental Bazel features:

- **Hermeticity** — Actions can read and write arbitrary host filesystem state, so
  builds depend on the machine environment rather than only on declared inputs.
- **Reproducibility** — Because outputs land in ``_build/`` (workspace-resident, not
  Bazel-tracked), two identical ``bazel run`` invocations starting from different
  workspace states can produce different results.
- **Action caching** — Bazel cannot cache or invalidate results it does not know
  about; outputs written outside the output tree are invisible to the cache, so
  incremental builds may silently serve stale artifacts.
- **Remote execution** — Remote build systems require all inputs and outputs to be
  declared; workspace-relative reads and writes cannot be shipped to a remote worker.
- **Remote caching** — Results cannot be shared across machines via a remote cache
  because the outputs are never stored in Bazel's Content-Addressable Store (CAS).
- **Parallel safety** — Bazel guarantees that sandboxed actions do not interfere with
  each other; deleting ``_build/score_source_code_linker_cache.json`` is an undeclared
  side effect that races with concurrent builds or actions.
- **bazel build compatibility** — These targets are restricted to ``bazel run`` only,
  since ``BUILD_WORKSPACE_DIRECTORY`` is not set during ``bazel build``, making them
  unusable in CI pipelines that rely on standard build commands.
- **Build graph correctness** — Downstream targets cannot depend on outputs that exist
  only in the workspace; Bazel's dependency graph is incomplete, so it cannot guarantee
  a correct topological execution order.

How PR #95 Improves the Situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Fully sandboxed Sphinx builds** —
   The PR introduces ``sphinx_wrapper.py``, a new Sphinx entry point that accepts
   explicit command-line arguments (``--index_file``, ``--output_dir``, ``--config``,
   ``--builder``) and is invoked through proper ``ctx.actions.run()`` calls inside
   dedicated Bazel rule implementations. All inputs and outputs are declared, so Sphinx
   runs entirely within the Bazel sandbox. This restores hermeticity, action caching,
   remote execution, remote caching, parallel safety, and full ``bazel build``
   compatibility.

2. **Proper JSON serialization for external needs** —
   Rather than embedding label lists as environment variable strings, the PR writes a
   well-formed ``needs_external_needs.json`` file using ``ctx.actions.write()`` with
   ``json.encode_indent()``, and passes it as a declared build input. The generated
   ``conf.py`` reads this file directly with ``json.load()``. This ensures correct
   JSON parsing and reliable cache invalidation when dependencies change.

3. **Provider-based dependency tracking** —
   The PR replaces string-based label manipulation with a set of typed Bazel
   providers — ``SphinxSourcesInfo``, ``SphinxModuleInfo``, ``SphinxNeedsInfo``,
   ``DependableElementInfo``, and others. Dependency information now flows through
   the build graph via properly typed provider fields and transitive ``depset``
   collections, making cross-module references both robust and easy to reason about.

4. **Composable, purpose-built rules** —
   Instead of a single monolithic macro generating many targets at once, the PR offers
   a composable set of Bazel rules — ``sphinx_module``, ``dependable_element``,
   ``feature_requirements``, ``component_requirements``, ``architectural_design``,
   ``safety_analysis``, and more. Each is a proper Bazel rule with well-defined
   attributes, making builds more modular, testable, and easier to extend.

5. **No workspace side effects** —
   All build outputs are written to Bazel-managed directories. The PR includes a
   dedicated ``sphinx_html_merge.py`` tool that merges HTML from multiple modules
   using only declared inputs and outputs, ensuring that no files are created,
   modified, or deleted in the source tree during a build.

6. **Template-driven per-module configuration** —
   Rather than relying on a single shared ``conf.py``, the PR generates a tailored
   Sphinx configuration for each module from a ``conf.template.py`` template using
   ``ctx.actions.expand_template()``. External needs are loaded from the
   build-action-produced JSON file, keeping each module's configuration self-contained
   and reproducible.

Goals
-----

- **Proper support of S-CORE adoption**: Enable teams to structure their documentation
  according to the S-CORE process, with dedicated artifact types for requirements,
  architectural design, safety analysis, and assumptions of use.
- **Proper support of Bazel**: Ensure documentation builds adhere to Bazel's core
  principles — hermeticity, reproducibility, and correct dependency tracking — enabling
  action caching, remote caching, remote execution, and parallel builds.
- **Implementation effort**: The one-time cost of migrating existing repositories from
  the current ``docs()`` macro to the new rule-based approach, including BUILD file
  changes and any necessary restructuring of documentation sources.
- **Maintenance effort**: The ongoing cost of keeping the documentation build
  infrastructure working, including dependency management, debugging build failures,
  and adapting to changes in Bazel, Sphinx, or the S-CORE process.
- **Ease of use**: How straightforward it is for developers to create, build, preview,
  and update documentation as part of their normal development workflow.

Options Considered
------------------

Option S: Single ``docs()`` Only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We keep the current ``docs()`` macro and do not adopt the module-based approach.

- **Proper support of S-CORE adoption** 😡 No dedicated artifact types; teams must
  manually structure documentation to match the S-CORE process.
- **Proper support of Bazel** 😡 Sphinx builds escape the sandbox, breaking
  hermeticity, action caching, remote execution, and parallel safety.
- **Implementation effort** 💚 No additional effort.
- **Maintenance effort** 💛 Known workarounds remain in place, but no new complexity
  is introduced.
- **Ease of use** 💚 No change for developers.

Option M: Module API — Many Bazel Targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We drop the current approach and switch to the module-based approach.

- **Proper support of S-CORE adoption** 💚 Purpose-built rules for each S-CORE
  artifact type (requirements, architectural design, safety analysis, etc.).
- **Proper support of Bazel** 💚 Fully sandboxed builds with declared inputs and
  outputs, enabling caching, remote execution, and reproducibility.
- **Implementation effort** 😡 Requires restructuring all existing documentation into
  per-module BUILD targets.
- **Maintenance effort** 💚 Documentation builds are standard Bazel actions — no
  custom scripts or workspace-escaping workarounds to maintain.
- **Ease of use** 😡 Requires developers to adapt to a new workflow. No VS Code LSP
  integration (Esbonio) available.

Option C: Combine the Best of Both
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We integrate the module-based rules into the existing solution, maintaining the current
developer experience while adding S-CORE structure and Bazel correctness where possible.

- **Proper support of S-CORE adoption** 💛 Possible through gradual adoption, but both
  systems must be kept consistent.
- **Proper support of Bazel** 💛 Module-based targets are fully sandboxed, but the
  ``docs()`` macro path retains its existing sandbox violations.
- **Implementation effort** 😡 Highest effort — requires implementing and maintaining
  both approaches in parallel.
- **Maintenance effort** 😡 Two parallel documentation build paths must be kept working
  and consistent.
- **Ease of use** 💚 No mandatory change for developers initially; module-based rules
  available as an opt-in extension.

Evaluation
----------

Summary of how well each option achieves the goals, in order of importance:

.. csv-table::
   :header: Goal, Option S, Option M, Option C
   :widths: 25, 10, 10, 10

   Proper support of S-CORE adoption, 😡, 💚, 💛
   Proper support of Bazel,           😡, 💚, 💛
   Implementation effort,             💚, 😡, 😡
   Maintenance effort,                💛, 💚, 😡
   Ease of use,                       💚, 😡, 💚

Decision
--------

Option M — adopt the module-based approach and invest in VS Code LSP integration
to restore the developer experience.
