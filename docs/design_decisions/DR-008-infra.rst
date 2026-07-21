..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-008-Infra: Generating documentation sources via Bazel
========================================================

- **Date:** 2026-06-29

.. dec_rec:: Generating documentation sources via Bazel
   :id: dec_rec__infra__docs_src_dir
   :status: accepted
   :context: Infrastructure
   :decision: Option M because of slight IDE usability edge over Option B

Context / Problem
-----------------

The docs-as-code system builds documentation by reading from a static ``source_dir`` (default ``"docs/"``) on the workspace filesystem.
Three build paths coexist:

1. **Live preview** — Local development via `sphinx-autobuild <https://github.com/sphinx-doc/sphinx-autobuild>`_.
2. **Direct Sphinx** — Sphinx invoked in the same venv for fast iteration or CI.
3. **Bazel sandbox** — ``needs_json`` and similar targets run Sphinx in a hermetic sandbox.

We have no generic solution for generating parts of the documentation source directory via Bazel.
See `docs-as-code issue #423 <https://github.com/eclipse-score/docs-as-code/issues/423>`_ for an open feature request
to implement "Extra docs pages from artifacts".

Workarounds we already have in place are:

* Use ``.`` as source directory to place sources anywhere.
  This implies a careful maintenance of include/exclude patterns in ``conf.py``.
  It is limited because a rule in the root ``BUILD`` file cannot cover files in subdirectories with another ``BUILD`` file.
* Generate json files for special inputs like source links.
  This is limiting because we cannot generate whole pages or directories with this approach.
* Implicitly read files from bazel folders.
  TestLinks in documentation appear if a ``test.xml`` file exists under ``bazel-testlogs/``.
* Reference integration overwrites documentation sources in a workflow.
  `See 'Publish build summary' step <https://github.com/eclipse-score/reference_integration/blob/07e75c498545b2eef8116f1aff3f006646f90f93/.github/workflows/test_and_docs.yml#L74>`_.
* The ``:docs_combo`` does compose a sources directory via `sphinx-collections <https://sphinx-collections.readthedocs.io/>`_.
  It allows no control over the folder hierarchy
  and symlinks in the git workspace can be confusing.

We look for a solution which is simpler and easier to maintain,
so we don't have to keep adding more and more workarounds for each new use case.

Additionally, we repeatedly has issues with caching.
Since we don't rely on Bazel sandbox for docs building, Bazel cannot help with hermeticity and determinism.
We need incremental builds locally and determinism with caching in CI.
See `rules_python sphinxdocs <https://rules-python.readthedocs.io/en/latest/sphinxdocs+/docs/#optimization>`_
how an idea how to achieve this using Bazel.

The "Module API" proposal
(somewhat implemented in `tooling PR 95 <https://github.com/eclipse-score/tooling/pull/95>`_)
fully relies on Bazel.
It is not compatible with the docs-as-code live preview as of now.
`Another exploration by Useblocks <https://github.com/useblocks/bazel-drives-sphinx/tree/main>`_
is available but does not cover live preview either.

We want dashboards generated automatically to be included in the documentation.
See `infrastructure discussion 2026-05-18 <https://github.com/orgs/eclipse-score/discussions/236#discussioncomment-16906461>`_.

Cross-repository composed builds via ``:docs_combo`` must keep working for integrator repositories.

When composing doc sources from multiple places with the same repository,
we need tracking such that errors and warnings point to the original source files.
However, there is no need to provide that for generated or transformed files
(as is common for Javascript or CSS assets in web development with
`source maps <https://developer.mozilla.org/en-US/docs/Glossary/Source_map>`_).

Status quo
^^^^^^^^^^

.. mermaid::

   graph LR
       docs@{ shape: docs, label: "docs/" }
       docs --> :docs
       docs --> :live_preview
       :live_preview -- watch --> docs

While ``sphinx-autobuild --pre-build`` is available to trigger some build steps before each rebuild,
this does not work with Bazel:
If you ``bazel run :live_preview`` and do a ``bazel build`` inside,
that build will wait for the run to finish, thus deadlock.

Requirements (all options satisfy these)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Allow to generate parts of the documentation via Bazel (including whole pages or directories).
- Access file from anywhere in the workspace (e.g. cpp sources in ``src/``).
- Live preview with fast edit-preview cycles.
- Errors and warnings point to the original source files if they are in the repo.
- Combo build can include full sources from multiple repositories.
- Intentionally separate test execution from docs generation.

Goals (optimize these with this decision)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Maintainability**: Minimise the effort for potential future extensions.
- **Effort**: Minimise one-time implementation and ongoing maintenance cost.
- **Speed**: Minimise the build time for documentation builds, especially for live preview.
- **UX**: Minimize efforts necessary to documentation work.

Non-Goals
^^^^^^^^^

- Replacing Sphinx or Sphinx-Needs as documentation tools.
- Keep Esbonio language server alive as we assume nobody is using it.

Options Considered
------------------


Option B: Introduce ``:docs_src_dir`` Bazel target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In short: sphinx-autobuild from a Bazel target that re-materializes the sources continuously via
`ibazel / bazel-watcher <https://github.com/bazelbuild/bazel-watcher>`_.

We add an ``extra_docs`` attribute to the ``docs()`` macro
for additional sources specified via `sphinx_docs_library <https://rules-python.readthedocs.io/en/1.0.0/api/sphinxdocs/sphinxdocs/sphinx_docs_library.html#sphinx_docs_library>`_,
which allows to adapt path prefixes.
The source tree is materialized using hardlinks (``ln``) inside a Bazel ``declare_directory`` action.
Symlinks fail Bazel's output tree validation (dangling link detection),
while copies are unnecessarily expensive for large doc sets.

.. mermaid::

   graph LR
       docs@{ shape: docs, label: "docs/" }
       extradocs@{ shape: docs, label: "extra_srcs" }
       preview@{ shape: subproc, label: "live_preview" }
       allsrc@{ label: ":docs_src_dir" }
       docs --> allsrc --> :docs --> preview
       extradocs --> allsrc
       preview -- rebuild --> :docs
       allsrc --> :needs_json

The live preview is replaced by a custom implementation.
This live preview cannot be executed via ``bazel run`` because of the need to rebuild via Bazel internally.
Thus, there is no ``:live_preview`` target but a ``live_preview`` script.
We cannot rely on watching file system changes to trigger rebuilds because the source directory is composed by Bazel
and may contain generated files.

The ``live_preview`` script runs two concurrent processes:

1. ``ibazel build :docs_src_dir`` — watches workspace sources and re-materializes the tree on change.
2. ``sphinx-autobuild`` — watches the materialized tree and serves HTML with websocket-based browser reload.

The ``score_sync_toml`` extension writes a ``ubproject.toml`` file to the source directory
but Bazel sandboxing makes this fail.
The ``score_sync_toml`` extension's write to the source directory is redirected via
``--define=needscfg_outpath=<workspace>/docs/ubproject.toml``,
which works without modifications to the extension itself.

Because Sphinx sees the materialized tree rather than the original workspace files,
warnings would normally cite ``bazel-out/…`` paths.
In the PoC, this is addressed by a ``_sourcemap.json`` sidecar emitted by the ``docs_src_dir``
Bazel action alongside the declared directory.
The sidecar maps each materialized path back to its original workspace-relative path.
A ``score_sourcemap`` Sphinx extension reads the sidecar on ``builder-inited``,
then installs a ``logging.Filter`` on every Sphinx log handler that rewrites
materialized paths in warning/error records before they are emitted.
The filter runs after Sphinx's own ``WarningLogRecordTranslator``, which has already
converted ``(docname, lineno)`` tuples to strings, so the rewrite is purely textual.
The extension is a no-op when no sidecar is present
(direct Sphinx invocations via ``esbonio`` or ``.venv_docs`` are unaffected).
The sidecar travels with the materialized tree, so path rewriting works inside
the Bazel sandbox (``bazel build``) as well as under ``bazel run`` and ``live_preview``.

Maintainability 💚: Generic solution for all build paths and future extensions.

Effort 💛: Some implementation effort but prototype already works.

Speed 💛: Overall latency is comparable to the status quo for edit-preview cycles, but the initial cold start is a little slower due to the extra Bazel invocation.

UX 😡: Requires a two-step setup: ``bazel run //:ide_support`` (venv) then
``bazel run //:gen_live_preview`` (script).
The generated script is workspace-specific and should be gitignored.

The generally idea is also described in `the rules_python documentation <https://github.com/bazel-contrib/rules_python/blob/5511aaf1e95fbf6b3eeca64ad503b26d712f50aa/docs/README.md#generating-docs-for-development>`_:

.. code-block:: bash

   bazel run //docs:docs.serve  # Run in separate terminal
   ibazel build //docs:docs  # Automatically rebuilds docs

This ``docs.serve`` target implemented in `rules_python` does not have
auto-refresh in the browser though.

Option M: Mount external source bundles via ``sphinx-mounts``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In short: keep source files where they are and mount them into the Sphinx project
using ``[[mounts]]`` entries written to ``ubproject.toml``.

This option has been explored as a proof of concept in
`docs-as-code PR #554 <https://github.com/eclipse-score/docs-as-code/pull/554>`_.
The PoC adds a ``mounts`` attribute to ``docs()``
and wires it through all relevant paths,
including ``:docs_combo`` / ``:docs_sources`` and sandboxed builds.

In contrast to option B, the source files are not re-materialized.
This uses the external `sphinx-mounts <https://sphinx-mounts.useblocks.com/>`_ extension.
`The extension modifies Sphinx internal data structures <https://github.com/useblocks/sphinx-mounts/blob/294526a010dfd8c3be022d154cc8974defd7c7c7/src/sphinx_mounts/mounter.py#L13>`_
to integrate files outside of the source directory.


.. mermaid::

   graph LR
       docs@{ shape: docs, label: "docs/" }
       bundle@{ shape: docs, label: "src/docs/ or generated dir" }
       mounts@{ label: "[[mounts]]" }
       docs --> :docs
       bundle --> mounts --> :docs

The approach avoids copying/symlinking documentation trees into ``docs/``
and aims to keep IDE tooling aligned by reading the same ``ubproject.toml`` as Sphinx.

Known constraints from the PoC:

* Each mount currently expects a directory-shaped Bazel output
  (e.g. via a helper like ``files_to_dir``).
* Per-bundle ``ubproject.toml`` generation is workspace-only (``bazel run``),
  while sandboxed ``bazel build`` skips those workspace writes by design.
* Nested mounts are not supported.

The live_preview implementation would have to be similar to Option B.
However, it is less critical because rst files elsewhere in the same repository
are watched by the existing ``sphinx-autobuild`` setup.
The ``ibazel`` part is only necessary for generated artifacts.

Maintainability 💚: Equivalent to option B.

Effort 💛: Similar order of magnitude as Option B prototype work.

Speed 💛: Comparable iterative speed; initial setup and mount resolution add some overhead.

UX 💛: Slight edge in IDE usability. The two step are still necessary for a comprehensive live preview.

Evaluation
----------

Options B and M are nearly equivalent across the evaluated goals.
Option M has a small edge in IDE usability because it avoids re-materializing sources
and keeps IDE tooling aligned by reading the same ``ubproject.toml`` as Sphinx.

A hybrid of B and M was not sufficiently explored and may be reconsidered later.

In order of importance, most important first.

.. csv-table::
  :header: Goals, Option B, Option M
  :widths: 2, 1, 1

  Maintainability, 💚, 💚
  Effort,          💛, 💛
  Speed,           💛, 💛
  UX,              😡, 💛

**Decision: Option M** because of its slight edge in IDE usability.

Appendix: any_folder experiment
-------------------------------

For a brief moment, we had an ``any_folder`` extension but removed it before the docs-as-code release.
It breaks when using such documentation in ``:docs_combo``:
It relied on configuration in ``conf.py`` but with ``:docs_combo``
the modules' ``conf.py`` is ignored and only the root ``conf.py`` is used.

More information can be found in `PR #450 <https://github.com/eclipse-score/docs-as-code/pull/450>`_.
