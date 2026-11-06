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

First Eclipse S-CORE Module
=================================

Before starting, ensure you are an official contributor to the Eclipse S-CORE project.
Otherwise, you will not have the required permissions. Instructions can be found in
:ref:`Actions to ensure Proper Contribution Attribution in Eclipse S-CORE <contribution_attribution>`.

Once you have created an Eclipse account,
accepted the Eclipse Contributor Agreement (ECA), and linked your GitHub account with your Eclipse account,
contact one of the Eclipse S-CORE Project Leads (listed at the official `Eclipse SDV S-CORE webpage <https://projects.eclipse.org/projects/automotive.score/who>`_).
They will add you to the list of the official contributors of the Eclipse S-CORE GitHub organization.

The recommended communication channel to approach Eclipse S-CORE project leads is the
`eclipse sdv slack channel <https://sdv.eclipse.org/get-engaged/>`_.

.. note::

   You do not need an own repository to follow this guide: the running example, the platform info service and
   its consumer, lives in the `reference integration <https://github.com/eclipse-score/reference_integration>`_.
   The following sections describe what you need when you contribute your own module.


Creating a Repository for Your Module
------------------------------------------
After becoming part of the Eclipse S-CORE GitHub organization, you can request a repository for your module.
Repository creation follows Eclipse organizational rules.
Most configuration is handled via `otterdog configuration <https://otterdog.readthedocs.io/en/latest/>`_ located in:

- `eclipse-score/.eclipsefdn <https://github.com/eclipse-score/.eclipsefdn>`_

Create a fork of this repository and modify the file:

- `otterdog/eclipse-score.jsonnet <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_

Add your repository definition next to the existing ones. Module repositories are declared with
``newDependableElementRepo``; incubation repositories additionally set ``subcategory = "incubation"``:

.. code-block:: text
    :emphasize-lines: 5, 6, 7

    newDependableElementRepo('lifecycle') {
      description: "Repository for the lifecycle feature",
    },

    newDependableElementRepo('my_module') {
      description: "Repository for my module",
    },

    newDependableElementRepo('inc_someip_gateway', subcategory = "incubation") {
      description: "Incubation repository for SOME/IP gateway feature",
    },

Then, create a PR in the `eclipse-score/.eclipsefdn <https://github.com/eclipse-score/.eclipsefdn>`_ repository. The PR must be approved by:

- Eclipse S-CORE project lead
- Eclipse Foundation Security Team

.. tip::

    To speed up approval, mention both groups in your PR comment:

    .. code-block:: text

        @eclipse-score/automotive-score-project-leads
        @eclipse-score/eclipsefdn-security

        Please approve.


Repository Layout
^^^^^^^^^^^^^^^^^^
Once merged, your new repository will appear in the Eclipse S-CORE GitHub organization repositories overview.

New repositories are based on the `Eclipse S-CORE module template <https://github.com/eclipse-score/module_template>`_.
Its `README.md <https://github.com/eclipse-score/module_template/blob/main/README.md>`_ explains how to build and test the
template; the expected folder structure is described in :ref:`module folder structure <module_folder_structure>`.
Below is an overview of the most relevant files and folders.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File / folder
     - Content
   * - ``.github/workflows/``
     - CI/CD workflows, based on the reusable workflows of ``cicd-workflows``
   * - ``.devcontainer/``
     - Development container based on the common S-CORE devcontainer image
   * - ``.vscode/``
     - Recommended VS Code settings, extensions and snippets
   * - ``docs/``
     - Module documentation (rst), e.g. module, feature and component documents, release notes and verification report
   * - ``score/``
     - Source code, unit tests and component integration tests, e.g. ``score/component_example``
   * - ``examples/``
     - Examples and their documentation
   * - ``.bazelrc``, ``score.bazelrc/``
     - Bazel configuration incl. the S-CORE build configurations per target platform
   * - ``MODULE.bazel``, ``BUILD``
     - Bazel module definition and top-level targets
   * - ``project_config.bzl``
     - Project metadata used by shared Bazel macros
   * - ``LICENSE``, ``NOTICE``, ``REUSE.toml``, ``LICENSES/``
     - License and copyright information


.github/workflows/
------------------
Contains the CI/CD workflows, e.g. pre-commit checks, license check and documentation build.
They are described in the :doc:`CI/CD workflows <cicd_workflows>` chapter.


.devcontainer and .vscode
-------------------------
``.devcontainer/`` references the common `S-CORE devcontainer <https://github.com/eclipse-score/devcontainer>`_ image,
which contains all required tools pre-installed. Open the repository with the
`VS Code Dev Containers extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>`_
and select *Reopen in Container* to skip manual toolchain setup entirely.

``.vscode/`` provides the Eclipse S-CORE recommended VS Code setup, including code completion patterns for requirements
and architecture in
`.vscode/restructuredtext.code-snippets <https://github.com/eclipse-score/module_template/blob/main/.vscode/restructuredtext.code-snippets>`_.


docs
-----
Place all module documentation here in `rst format <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.
The :doc:`documentation generation <doc_generation>` chapter shows how it is built.

.. tip::
    We try to describe the most :ref:`common workflows <contribute_contribution_guideline>`
    for developers. It is worth checking them.

score/
-------
Source files, unit tests and component integration tests of the module, one folder per component,
e.g. ``score/<component_name>/``. Feature integration tests of the module are placed in ``score/tests/``.
The folder determines the test level, see :ref:`module folder structure <module_folder_structure>`.


.bazelrc
--------
Defines the Bazel configuration of the module. Important entries in the
`.bazelrc <https://github.com/eclipse-score/module_template/blob/main/.bazelrc>`_ file include:

.. code-block:: text
    :linenos:
    :emphasize-lines: 1, 2, 5

    common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
    common --registry=https://bcr.bazel.build

    # Import toolchain bazelrc file
    try-import %workspace%/score.bazelrc/score_toolchain.bazelrc

- Line 1 points to the `Eclipse S-CORE Bazel registry <https://github.com/eclipse-score/bazel_registry>`_,
  where all official versions of Eclipse S-CORE modules are published.
- Line 2 points to the Bazel Central Registry, where common Bazel modules are made available for everyone.
- Line 5 imports the S-CORE build configurations, e.g. ``--config=score-linux-x86_64`` or ``--config=score-qnx-x86_64``.
  They select the target platform and the matching toolchains and are explained in the
  :doc:`building source code <building_source_code>` chapter.

This means, once we reference a dependency in our module,
Bazel will search for it in one of these two registries.


MODULE.bazel
-------------
This file turns your repository into a Bazel module.
The template starts with a minimal module declaration:

.. code-block:: python
    :linenos:

    module(name = "score_module_template")

Rename the module and replace *score_module_template* by your module name.
According to Eclipse S-CORE's naming convention, all module names must start with the *score\_* prefix,
e.g. *score_my_module*. The version is not maintained in ``MODULE.bazel``: it is taken from the release tag
(``vX.Y.Z``, following `semantic versioning <https://semver.org/>`_) when the release is added to the
Bazel registry. Only after your module was published in the Eclipse S-CORE Bazel registry, other modules can access it.

Next, the template declares dependencies to modules that are publicly available in the Bazel Central Registry,
e.g. for unit test execution with GoogleTest:

.. code-block:: python
    :linenos:

    # Add GoogleTest dependency
    bazel_dep(name = "googletest", version = "1.17.0.bcr.2", dev_dependency = True)

    # Rust rules for Bazel
    bazel_dep(name = "rules_rust", version = "0.70.0")

    # C/C++ rules for Bazel
    bazel_dep(name = "rules_cc", version = "0.2.18")

Then follow the dependencies to Eclipse S-CORE modules that are used during development:

.. code-block:: python
    :linenos:

    # tooling
    bazel_dep(name = "score_tooling", version = "1.3.1", dev_dependency = True)

    # docs-as-code
    bazel_dep(name = "score_docs_as_code", version = "8.6.0")
    bazel_dep(name = "score_process_description", version = "2.2.1")

    # Provide the tools from the devcontainer to Bazel
    bazel_dep(name = "score_devcontainer", version = "1.11.4", dev_dependency = True)
    bazel_dep(name = "score_cpp_policies", version = "0.1.2", dev_dependency = True)

- **score_tooling**: enables tooling checks such as copyright, formatting and license verification.
- **score_docs_as_code** and **score_process_description**: enable documentation builds with Sphinx and sphinx-needs
  and the references to the process description.
- **score_devcontainer**: makes the tools of the devcontainer available to Bazel.
- **score_cpp_policies**: provides the shared C++ quality rules, e.g. compiler warnings, sanitizers and clang-tidy.
  For Rust code, ``score_rust_policies`` provides the shared Clippy configuration.

The last part of the template, marked *S-CORE Toolchains (DO NOT MODIFY)*, registers the S-CORE toolchains
from ``score_bazel_cpp_toolchains`` and ``score_toolchains_rust`` for all supported target platforms.
It is explained in the :doc:`building source code <building_source_code>` chapter.

Finally, add the S-CORE modules your code uses. The platform info example uses mw::com from ``score_communication``
and the CRC32 calculation and argument handling from ``score_baselibs``:

.. code-block:: python
    :linenos:

    bazel_dep(name = "score_communication", version = "0.6.0")
    bazel_dep(name = "score_baselibs", version = "0.2.17")

The available versions can be looked up in the `Bazel registry UI <https://eclipse-score.github.io/bazel_registry_ui/>`_.
Bazel modules don't make transitive dependencies available to your code: list every module whose targets you use
directly in your ``BUILD`` files.

.. tip::
    Working across multiple modules and repositories can be challenging. Use the following approach during development:

    - use `git_override()  <https://bazel.build/rules/lib/globals/module#git_override>`_
      if you want to use a version of another module that is currently not officially available in the Bazel registry.

    - use `local_path_override()  <https://bazel.build/rules/lib/globals/module#local_path_override>`_
      if you want to use your local version of the module, e.g. during active development.

    - use ``bazel run --override_module=<module>=<path>`` to try out a local checkout without changing ``MODULE.bazel``.


BUILD
-----
The Bazel `BUILD <https://github.com/eclipse-score/module_template/blob/main/BUILD>`_ file
contains the main Bazel targets on the top level of the module:

.. code-block:: python
    :linenos:

    load("@score_docs_as_code//:docs.bzl", "docs")
    load("@score_tooling//:defs.bzl", "copyright_checker", "dash_license_checker", "setup_starpls", "use_format_targets")
    load("//:project_config.bzl", "PROJECT_CONFIG")

First, we load Bazel rules and macros implemented in the Eclipse S-CORE context from the modules
that we've defined as dependencies in the ``MODULE.bazel`` file, e.g. https://github.com/eclipse-score/docs-as-code.

.. code-block:: python
    :linenos:

    copyright_checker(
        name = "copyright",
        srcs = [
            "score",
            "//:BUILD",
            "//:MODULE.bazel",
        ],
        config = "@score_tooling//cr_checker/resources:config",
        template = "@score_tooling//cr_checker/resources:templates",
        visibility = ["//visibility:public"],
    )

    dash_license_checker(
        src = "//examples:cargo_lock",
        file_type = "",  # let it auto-detect based on project_config
        project_config = PROJECT_CONFIG,
        visibility = ["//visibility:public"],
    )

    # Add target for formatting checks
    use_format_targets()

Second, we define the targets for the copyright check (``bazel run //:copyright.check``), the license check
with the Eclipse Dash license tool and the formatting check (``bazel test //:format.check``),
based on Bazel rules implemented in the https://github.com/eclipse-score/tooling module.

.. code-block:: python
    :linenos:

    docs(
        project = "Module Template Project",
        project_url = "https://eclipse-score.github.io/module_template/",
        source_dir = "docs",
    )

Finally, the *docs* macro creates all documentation targets for the rst files located in the
``docs`` folder and all its subfolders.
This functionality is implemented in `eclipse-score/docs-as-code <https://github.com/eclipse-score/docs-as-code>`_
and described in the :doc:`documentation generation <doc_generation>` chapter.


project_config.bzl
------------------
Every Eclipse S-CORE module provides a ``project_config.bzl`` file in its root directory.
This file declares project-level metadata that is consumed by shared Bazel macros such as ``dash_license_checker``.

A minimal example:

.. code-block:: python
    :linenos:

    PROJECT_CONFIG = {
        "asil_level": "QM",        # Safety level: "QM", "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D"
        "source_code": ["cpp"],    # Languages used: "cpp", "rust", or both
    }

The ``asil_level`` is used by tooling to apply the appropriate quality and compliance checks.
The ``source_code`` list determines which license file types are scanned by ``dash_license_checker``
(e.g., ``Cargo.lock`` for Rust, ``requirements.txt`` for Python).

.. tip::
    Start with ``"asil_level": "QM"`` during initial development.
    The level can be raised once the module's safety concept is established.
