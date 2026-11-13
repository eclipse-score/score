..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

Documentation generation
==========================

Introduction
---------------
As described in the :ref:`Overview of technologies <technology_overview>` chapter,
Eclipse S-CORE uses the Sphinx and sphinx-needs toolchain to generate documentation from rst files.
Elements of the Eclipse S-CORE metamodel, e.g. requirements, architecture elements and test cases,
are represented as sphinx-needs objects.

The integration of Sphinx, sphinx-needs, and the Eclipse S-CORE-specific extensions is implemented in the repository:

- `eclipse-score/docs-as-code <https://github.com/eclipse-score/docs-as-code>`_

The `docs-as-code how-to documentation <https://eclipse-score.github.io/docs-as-code/main/how-to/index.html>`_
describes in detail how documentation is created and built. Here, we focus on a simple example.


Defining a Bazel Documentation Target
-----------------------------------------
To generate HTML documentation from *.rst* files, S-CORE provides the ``docs`` Bazel macro.
In the top-level `BUILD <https://github.com/eclipse-score/module_template/blob/main/BUILD>`_ file of your module,
you find a call of this macro. Without the bundles explained below, it looks like this:

.. code-block:: python
    :linenos:

    load("@score_docs_as_code//:docs.bzl", "docs")

    docs(
        project = "Module Template Project",
        project_url = "https://eclipse-score.github.io/module_template/",
        source_dir = "docs",
    )

The most important parameters are:

- ``source_dir``: the directory that is given to Sphinx as source directory. Sphinx does not rely on Bazel dependencies
  to decide which files are included, but on its own
  `toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_ mechanism,
  starting from ``index.rst``.
- ``project`` and ``project_url``: the name and the published URL of your documentation.
  With both set, no own ``conf.py`` is needed; all S-CORE Sphinx extensions and the metamodel checks are configured
  by *docs-as-code*. Replace the template values by the name and URL of your module.
- ``external_needs``: documentation of other modules whose sphinx-needs objects you want to reference, e.g.
  ``"@score_process_description//:docs"`` for the process description or ``"@score_platform//:docs"``
  for the feature requirements and architecture of the S-CORE platform. The module must also be declared with
  ``bazel_dep`` in ``MODULE.bazel``. See
  `Reference Other Modules <https://eclipse-score.github.io/docs-as-code/main/how-to/other_modules.html>`_ for details.
- ``bundles``: further documentation bundles which are mounted into your documentation, e.g. the documentation
  of each component in ``score/<component_name>``. The template mounts ``//score/component_example:docs``
  and ``//examples:docs`` this way.

The `index.rst <https://github.com/eclipse-score/module_template/blob/main/docs/index.rst>`_ file in ``source_dir``
is the main entry point for your documentation. It includes all other rst files that should be part of the documentation build.


Building documentation
-----------------------
The ``docs`` macro creates the following targets:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Command
     - Purpose
   * - ``bazel run //:docs``
     - Builds the HTML documentation into the ``_build`` folder
   * - ``bazel run //:docs_check``
     - Checks the documentation, incl. the metamodel and traceability checks, without creating HTML
   * - ``bazel run //:docs_link_check``
     - Checks all external links
   * - ``bazel run //:live_preview``
     - Starts a local server which rebuilds the documentation on every change
   * - ``bazel run //:ide_support``
     - Creates the virtual environment ``.venv_docs`` for IDE support (e.g. the Esbonio extension)

The first execution of a Bazel command may take longer, because Bazel needs to download toolchains and dependencies.
Subsequent runs will be much faster.

.. code-block:: text
  :emphasize-lines: 1, 8

  $ bazel run //:docs
  ...
  reading sources... [100%] index
  ...
  Needs successfully exported
  build succeeded.

  The HTML pages are in _build.

After a successful build, open ``_build/index.html`` in a web browser.

When working on the documentation, it is helpful to see the current status directly in the web browser.
Use the *live preview* for this:

.. code-block:: text
  :emphasize-lines: 1, 5

  $ bazel run //:live_preview
  ...
  build succeeded.

  [sphinx-autobuild] Serving on http://127.0.0.1:8000
  [sphinx-autobuild] Waiting to detect changes...

A local server is started on http://127.0.0.1:8000. Open it in your web browser to view the current version
of the documentation. The live preview:

- rebuilds automatically
- updates on every file change
- stays active until you stop the Bazel process (Ctrl+C).

The published documentation of the `module template <https://eclipse-score.github.io/module_template/>`_
shows what the result looks like.


Linking tests to requirements
-----------------------------
The documentation does not only contain the rst files: *docs-as-code* also reads the results of the Bazel tests
and links each test case to the requirements it verifies. This is how the traceability from requirements to tests
becomes visible in the generated documentation.

The platform integration test of the running example shows how this works. The test function is annotated with the
requirement it verifies and the applied test methods
(`test_platform_info_showcase.py <https://github.com/eclipse-score/reference_integration/blob/main/platform_integration_tests/platform_info/test_platform_info_showcase.py>`_):

.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    from attribute_plugin import add_test_properties

    @add_test_properties(
        partially_verifies=["stkh_req__communication__inter_process"],
        test_type="interface-test",
        derivation_technique="requirements-analysis",
    )
    def test_platform_version(target):
        output = run_showcases(target, "Platform Version Check")
        assert "platform_info_consumer: S-CORE version check passed" in output

The attribute plugin writes these properties into the JUnit XML result of the test.
During the documentation build, they become a test case need which is linked to the stakeholder requirement
``stkh_req__communication__inter_process``. The allowed requirement types depend on the test level, see the
:ref:`software verification plan <software_verification_plan>`.
