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
        external_needs = [
            "@score_process_description//:needs_json",
        ],
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
  the process description, whose guidelines and work products the documents of the template reference.
  The template still uses the label ``@score_process_description//:needs_json``; *docs-as-code* accepts it, but
  recommends the public ``:docs`` target of the module instead, e.g. ``"@score_process_description//:docs"``.
  The module must also be declared with ``bazel_dep`` in ``MODULE.bazel``. See
  `Reference Other Modules <https://eclipse-score.github.io/docs-as-code/main/how-to/other_modules.html>`_ for details.
- ``bundles``: further documentation bundles which are mounted into your documentation, e.g. the documentation
  of each component in ``score/<component_name>``. The template mounts ``//score/component_example:docs``
  and ``//examples:docs`` this way, see `Component documentation`_ below.

The `index.rst <https://github.com/eclipse-score/module_template/blob/main/docs/index.rst>`_ file in ``source_dir``
is the main entry point for your documentation. In the template, it is structured as follows:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Folder in ``docs/``
     - Content
   * - ``template/``
     - Information about the template itself, e.g. the folder structure; remove it in your module
   * - ``features/``
     - Feature architecture, safety and security analysis and planning of the features implemented by the module
   * - ``module/``
     - Module documents, e.g. user, safety and security manuals, safety and security management, release note
   * - ``components/``
     - Mount point of the component documentation
   * - ``verification_report/``
     - Module verification report
   * - ``release_notes/``
     - Release notes of the module versions

The documents implement the work products of the
`S-CORE process description <https://eclipse-score.github.io/process_description/>`_. Each document declares the
work product it realizes, e.g. ``:realizes: wp__requirements_comp``, and contains ``.. attention::`` boxes which
describe how to adapt it to your module.


Component documentation
-----------------------
The documentation of a component is located next to its code, in
`score/component_example/docs <https://github.com/eclipse-score/module_template/tree/main/score/component_example/docs>`_:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File / folder
     - Content
   * - ``index.rst``
     - Component request: purpose of the component and the ``comp`` need ``comp__mod_temp_component_name_template``
   * - ``requirements/``
     - Component requirements and assumptions of use, and the inspection checklist
   * - ``architecture/``
     - Component architecture and the inspection checklist
   * - ``detailed_design/``
     - Detailed design with static and dynamic PlantUML diagrams, and the implementation inspection checklist
   * - ``safety_analysis/``, ``security_analysis/``
     - FMEA, DFA, component classification and assumptions of use from the safety and security analysis

The component ``BUILD`` file turns this folder into a documentation bundle:

.. code-block:: python
    :linenos:

    load("@score_docs_as_code//:docs.bzl", "docs_bundle")

    docs_bundle(
        name = "docs",
        code_targets = [
            ":component_example",
        ],
        primary_need_id = "comp__mod_temp_component_name_template",
        source_dir = "docs",
        visibility = ["//visibility:public"],
    )

- ``source_dir`` is the folder with the rst files of the component.
- ``code_targets`` lists the Bazel targets whose source files are scanned for links to requirements, see
  `Linking requirements, code and tests`_ below.
- ``primary_need_id`` is the need which represents the component, here the ``comp`` need from ``index.rst``.

The top-level ``docs`` macro mounts the bundle with ``"mount_at": "components/component_example"``, so the component
documentation appears under *Components* in the generated documentation.


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


Linking requirements, code and tests
------------------------------------
The documentation does not only contain the rst files: *docs-as-code* also scans the source code and reads the
results of the Bazel tests, and links both to the requirements. This makes the traceability from requirements to
code and tests visible in the generated documentation. In the template, the chain looks like this:

1. **Requirement**: the component requirement is defined in
   `requirements/requirements.rst <https://github.com/eclipse-score/module_template/blob/main/score/component_example/docs/requirements/requirements.rst>`_:

   .. code-block:: rst

      .. comp_req:: Some Title
         :id: comp_req__mod_temp_component_name__some_title
         :reqtype: Functional
         :security: YES
         :safety: ASIL_B
         :derived_from: feat_req__example_feature__example_req
         :status: valid
         :version: 1
         :satisfied_by: comp__mod_temp_component_name_template

         The component shall return the greeting "Hello, <name>!" for a given name through make_hello_message.

2. **Code**: the implementation references the requirement in a comment starting with ``req-traceability:``
   (or ``req-Id:``):

   .. code-block:: cpp

      // req-traceability: comp_req__mod_temp_component_name__some_title
      std::string make_hello_message(const std::string& name) {

   The files of the ``code_targets`` of the ``docs_bundle`` are scanned for these comments.
   The requirement gets the attribute ``source_code_link`` with a link to the file and line on GitHub.

3. **Test**: the component integration test declares the requirement it verifies with
   ``RecordProperty("PartiallyVerifies", ...)``, together with ``TestType``, ``DerivationTechnique`` and
   ``Description``, see :doc:`build and test <building_source_code>`. GoogleTest writes these properties into
   ``test.xml``. The documentation build reads all ``test.xml`` files in ``bazel-testlogs/``, creates a test case
   need for each test and links it to the requirement.

Test results only appear in the documentation if the tests were executed before the documentation build:

.. code-block:: bash

    bazel test --config=score-linux-x86_64 //score/...
    bazel run //:docs

The live preview does not show test results. Which requirement types a test may verify depends on its test level,
see the :ref:`software verification plan <software_verification_plan>`. The docs-as-code how-tos
`Link Source Code to Requirements <https://eclipse-score.github.io/docs-as-code/main/how-to/source_to_doc_links.html>`_ and
`Link Tests to Requirements <https://eclipse-score.github.io/docs-as-code/main/how-to/test_to_doc_links.html>`_
describe the details, e.g. for Python and Rust tests.
