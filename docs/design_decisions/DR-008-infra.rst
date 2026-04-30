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

- **Date:** 2026-04-23

.. dec_rec:: Generating documentation sources via Bazel
   :id: dec_rec__infra__docs_src_dir
   :status: proposed
   :context: Infrastructure
   :decision: Option B because Option N loses wrt flexibility

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
* Generate json files for special inputs like source links or test reports.
  This is limiting because we cannot generate whole pages or directories with this approach.
* The ``:docs_combo`` does compose a sources directory via `sphinx-collections <https://sphinx-collections.readthedocs.io/>`_.
  It allows no control over the folder hierarchy
  and symlinks in the git workspace can be confusing.

We look for a solution which is simpler and easier to maintain.

Additionally, we repeatedly has issues with caching.
Since we don't rely on Bazel sandbox for docs building, Bazel cannot help with hermeticity and determinism.
We need incremental builds locally and determinism with caching in CI.
See `rules_python sphinxdocs <https://rules-python.readthedocs.io/en/latest/sphinxdocs+/docs/#optimization>`_
how an idea how to achieve this using Bazel.

The "Module API" proposal
(somewhat implemented in `tooling PR 95 <https://github.com/eclipse-score/tooling/pull/95>`_)
fully relies on Bazel.
It is not compatible with the docs-as-code live preview as of now.

Goals
^^^^^

- **Effort**: Minimise one-time implementation and ongoing maintenance cost.
- **Flexibility**: Minimise the effort for potential future extensions.
- **Speed**: Minimise the build time for documentation builds, especially for live preview.
- **UX**: Minimize efforts necessary to documentation work.

Non-Goals
^^^^^^^^^

- Replacing Sphinx or Sphinx-Needs as documentation tools.
- Keep Esbonio language server alive as we assume nobody is using it.

Options Considered
------------------

Option N: No change (status quo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Keep the current architecture.
The ``docs()`` macro in ``docs.bzl`` accepts a ``source_dir`` parameter and reads
documentation sources directly from that directory on the workspace filesystem.

.. mermaid::

   graph LR
       docs@{ shape: docs, label: "docs/" }
       docs --> :docs
       docs --> :live_preview
       :live_preview -- watch --> docs


Effort 💚: No implementation work required.

Flexibility 😡: More workarounds instead of generic solution.

Speed 💚: Fast but only covers source updates (not test result updates, for example).

UX 💚: Status quo


Option B: Introduce ``:docs_src_dir`` Bazel target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We add an ``extra_docs`` attribute to the ``docs()`` macro
for additional sources specified via `sphinx_docs_library <https://rules-python.readthedocs.io/en/1.0.0/api/sphinxdocs/sphinxdocs/sphinx_docs_library.html#sphinx_docs_library>`_,
which allows to adapt path prefixes.
The we materialize a composed folder for the actual sphinx-build.

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

For the implementation we can rely on `ibazel / bazel-watcher <https://github.com/bazelbuild/bazel-watcher>`_
to trigger rebuilds of the ``:docs_src_dir`` target and then still use sphinx-autobuild for the browser auto-reload.
As a side-effect, ibazel is a new tool in S-CORE which could be reused for other auto-rebuild use cases like unit tests.

The ``score_sync_toml`` extension writes a ``ubproject.toml`` file to the source directory
but Bazel sandboxing makes this fail.
As a workaround, ``needscfg_outpath`` can be used to redirect it somewhere else.
Alternatively, ``remove score_sync_toml`` and ``needs_config_writer`` extensions and create the ubproject.toml file in a different way?

Effort 😡: Some implementation effort.

Flexibility 💚: Generic solution for all build paths and future extensions.

Speed ?: unclear

UX 😡: Live-preview requires a setup step to generate the script.


Evaluation
----------

In order of importance, most important first.

.. csv-table::
   :header: Goals, Option N, Option B
   :widths: 2, 1, 1

   Flexibility, 😡, 💚
   Effort,   💚, 😡
   Speed,    💚, ?
   UX,   💚, 😡

**Decision:** Option B because Option N loses wrt flexibility

Appendix: any_folder experiment
-------------------------------

For a brief moment, we had an ``any_folder`` extension but removed it before the docs-as-code release.
It breaks when using such documentation in ``:docs_combo``:
It relied on configuration in ``conf.py`` but with ``:docs_combo``
the modules' ``conf.py`` is ignored and only the root ``conf.py`` is used.
