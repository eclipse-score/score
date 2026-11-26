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
`project lead circle Slack channel <https://sdvworkinggroup.slack.com/archives/C085F44D2CS>`_
in the Eclipse SDV Slack workspace.

.. note::

   You do not need your own repository to follow this guide: clone the
   `module template <https://github.com/eclipse-score/module_template>`_ and try the steps there.
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
``newDependableElementRepo``: it creates the repository from the module template, enables GitHub Pages for the
documentation and sets up the GitHub environment for the QNX builds. Incubation repositories additionally set
``subcategory = "incubation"``:

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

The ``subcategory`` has no technical effect on the repository: it is stored as a custom property and only groups
the repositories in the auto-generated overview of the GitHub organization. Set ``"incubation"`` for incubator
repositories (prefix ``inc_``), which are created to try out the content of a feature request before it is written
down, see the incubation step in the :ref:`feature request process <feature_request_guideline>`.
A regular module repository doesn't need a ``subcategory``.

Then, create a PR in the `eclipse-score/.eclipsefdn <https://github.com/eclipse-score/.eclipsefdn>`_ repository. The PR must be approved by:

- Eclipse S-CORE project lead
- Eclipse Foundation Security Team, which is the code owner of the otterdog configuration

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
template, its `template information <https://eclipse-score.github.io/module_template/main/template/index.html>`_
shows the complete folder tree, and the rules behind it are described in
:ref:`module folder structure <module_folder_structure>`.
Below is an overview of the most relevant files and folders.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File / folder
     - Content
   * - ``.github/workflows/``
     - CI/CD workflows, based on the reusable workflows of ``cicd-workflows``,
       see :doc:`CI/CD workflows <cicd_workflows>`
   * - ``.devcontainer/``
     - Development container based on the common `S-CORE devcontainer <https://github.com/eclipse-score/devcontainer>`_
       image with all required tools; open the repository in VS Code and select *Reopen in Container*
   * - ``.vscode/``
     - Recommended VS Code settings, extensions and snippets, e.g. code completion for requirements and architecture
   * - ``docs/``
     - Module documentation (rst): feature and module documents, safety and security management, release notes
       and verification report, see :doc:`documentation generation <doc_generation>`
   * - ``score/<component>/``
     - One folder per component, e.g. ``score/component_example``: source code and unit tests in ``src/``,
       component integration tests in ``tests/``, component documentation in ``docs/``,
       see :doc:`build and test <building_source_code>`
   * - ``score/tests/``
     - Feature integration tests of the module
   * - ``examples/``
     - An example of architecture modeling with sphinx-needs and the ``Cargo.lock`` used by the license check
   * - ``.bazelrc``, ``score.bazelrc/``
     - Bazel configuration incl. the S-CORE build configurations per target platform
   * - ``MODULE.bazel``, ``BUILD``
     - Bazel module definition and top-level targets
   * - ``project_config.bzl``
     - Project metadata used by shared Bazel macros
   * - ``LICENSE``, ``NOTICE``, ``REUSE.toml``, ``LICENSES/``
     - License and copyright information

The folder of a test determines its test level, see :ref:`module folder structure <module_folder_structure>`.


Adapting the template
---------------------
The template is a working example, not an empty skeleton: it builds, tests and documents the example component
``component_example`` out of the box. To turn it into your module, go through the following files in this order.
Each section explains what the file is for and what you need to adapt.


.. _first_module_module_bazel:

MODULE.bazel
^^^^^^^^^^^^
**To adapt:** the module name and the dependencies of your code.

This file turns your repository into a Bazel module.
The template starts with a minimal module declaration:

.. code-block:: python
    :linenos:

    module(name = "score_module_template")

Rename the module and replace *score_module_template* by your module name.
According to Eclipse S-CORE's naming convention, all module names must start with the *score\_* prefix,
e.g. *score_my_module*. The version of your module is not maintained in ``MODULE.bazel``: it is taken from the release tag
(``vX.Y.Z``, following `semantic versioning <https://semver.org/>`_) when the release is added to the
Bazel registry. Other modules can depend on a released version of your module with ``bazel_dep`` only after it was
published in the Eclipse S-CORE Bazel registry; before that, they need a ``git_override``.

Next, the template declares dependencies to modules that are publicly available in the Bazel Central Registry,
e.g. GoogleTest for the C++ tests, the C++ and Rust rules, and an LLVM toolchain for builds without an explicit
build configuration:

.. code-block:: python
    :linenos:

    bazel_dep(name = "googletest", version = "...", dev_dependency = True)
    bazel_dep(name = "rules_rust", version = "...")
    bazel_dep(name = "rules_cc", version = "...")
    bazel_dep(name = "toolchains_llvm", version = "...", dev_dependency = True)

Then follow the dependencies to Eclipse S-CORE modules that are used during development (excerpt):

.. code-block:: python
    :linenos:

    bazel_dep(name = "score_tooling", version = "...", dev_dependency = True)
    bazel_dep(name = "score_tools", version = "0.0.5", dev_dependency = True)
    bazel_dep(name = "score_docs_as_code", version = "...")
    bazel_dep(name = "score_process_description", version = "...")
    bazel_dep(name = "score_devcontainer", version = "...", dev_dependency = True)
    bazel_dep(name = "score_cpp_policies", version = "...", dev_dependency = True)

- **score_tooling** enables tooling checks such as formatting and license verification.
- **score_tools** provides the copyright checker.
- **score_docs_as_code** and **score_process_description**: enable documentation builds with Sphinx and sphinx-needs
  and the references to the process description.
- **score_devcontainer**: makes the tools of the devcontainer available to Bazel.
- **score_cpp_policies**: provides the shared C++ quality rules, e.g. compiler warnings, sanitizers and clang-tidy.
  For Rust code, ``score_rust_policies`` provides the shared Clippy configuration.

The template is kept up to date by automated pull requests. Take the versions for its dependencies from its
`MODULE.bazel <https://github.com/eclipse-score/module_template/blob/main/MODULE.bazel>`_.
``dev_dependency = True`` marks dependencies which are only needed to develop the module itself, e.g. for tests
and checks. They are ignored when another module depends on your module.

The last part of the template, marked *S-CORE Toolchains (DO NOT MODIFY)*, registers the S-CORE toolchains
from ``score_bazel_cpp_toolchains`` and ``score_toolchains_rust`` for all supported target platforms.
It is explained in the :doc:`build and test <building_source_code>` chapter.

Finally, add the S-CORE modules your code uses, e.g. ``score_baselibs``:

.. code-block:: python
    :linenos:

    bazel_dep(name = "score_baselibs", version = "<version>")

The available versions can be looked up in the `Bazel registry UI <https://eclipse-score.github.io/bazel_registry_ui/>`_.
Choose versions that fit to each other and to the toolchains of your module. A good starting point is the
`reference integration <https://github.com/eclipse-score/reference_integration>`_: it contains the consolidated state of
all S-CORE modules, which are built and tested together. Its
`known_good.json <https://github.com/eclipse-score/reference_integration/blob/main/known_good.json>`_ lists the
integrated version of each module. The ``MODULE.bazel`` of a module version
in the `registry <https://github.com/eclipse-score/bazel_registry/tree/main/modules>`_ shows which versions it depends on.
If Bazel reports *"the root module requires module version X, but got Y in the resolved dependency graph"*,
another module needs a newer version of this dependency; update the version in your ``MODULE.bazel`` accordingly.
Bazel modules don't make transitive dependencies available to your code: list every module whose targets you use
directly in your ``BUILD`` files.

.. tip::
    Working across multiple modules and repositories can be challenging. Use the following approach during development:

    - use `git_override()  <https://bazel.build/rules/lib/globals/module#git_override>`_
      if you want to use a version of another module that is currently not officially available in the Bazel registry.

    - use `local_path_override()  <https://bazel.build/rules/lib/globals/module#local_path_override>`_
      if you want to use your local version of the module, e.g. during active development.

    - use the command line option ``--override_module=<module>=<path>`` (e.g. with ``bazel build``) to try out a local
      checkout without changing ``MODULE.bazel``.


.bazelrc
^^^^^^^^
**To adapt:** nothing; add own settings to ``user.bazelrc``, which is imported if it exists.

The `.bazelrc <https://github.com/eclipse-score/module_template/blob/main/.bazelrc>`_ file tells Bazel where to
find the modules declared in ``MODULE.bazel`` and how to build for the S-CORE target platforms:

.. code-block:: text
    :linenos:

    common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
    common --registry=https://bcr.bazel.build

    try-import %workspace%/score.bazelrc/score_toolchain.bazelrc

- Line 1 points to the `Eclipse S-CORE Bazel registry <https://github.com/eclipse-score/bazel_registry>`_,
  where all official versions of Eclipse S-CORE modules are published.
- Line 2 points to the Bazel Central Registry, where common Bazel modules are made available for everyone.
- Line 4 imports the S-CORE build configurations, e.g. ``--config=score-linux-x86_64`` or ``--config=score-qnx-x86_64``.
  They select the target platform and the matching toolchains and are explained in the
  :doc:`build and test <building_source_code>` chapter.


.. _first_module_build:

BUILD
^^^^^
**To adapt:** ``project`` and ``project_url`` of the ``docs`` macro, and its ``bundles`` when you rename or add
components.

The Bazel `BUILD <https://github.com/eclipse-score/module_template/blob/main/BUILD>`_ file
contains the main Bazel targets on the top level of the module:

.. code-block:: python
    :linenos:

    load("@score_docs_as_code//:docs.bzl", "docs")
    load("@score_tooling//:defs.bzl", "dash_license_checker", "setup_starpls", "use_format_targets")
    load("@score_tools//cr_checker:cr_checker.bzl", "copyright_checker")
    load("//:project_config.bzl", "PROJECT_CONFIG")

First, we load Bazel rules and macros implemented in the Eclipse S-CORE context from the modules
that we've defined as dependencies in the ``MODULE.bazel`` file, e.g. https://github.com/eclipse-score/docs-as-code.

.. code-block:: python
    :linenos:

    copyright_checker(
        name = "copyright",
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
with the Eclipse Dash license tool and the formatting check (``bazel test //:format.check``).

.. code-block:: python
    :linenos:

    docs(
        bundles = [
            {
                "bundle": "//score/component_example:docs",
                "mount_at": "components/component_example",
            },
            {
                "bundle": "//examples:docs",
                "mount_at": "examples",
            },
        ],
        external_needs = [
            "@score_process_description//:needs_json",
        ],
        project = "Module Template Project",
        project_url = "https://eclipse-score.github.io/module_template/",
        source_dir = "docs",
    )

Finally, the *docs* macro creates all documentation targets for the rst files located in the
``docs`` folder and the documentation bundles of the components, which are mounted into it.
This functionality is implemented in `eclipse-score/docs-as-code <https://github.com/eclipse-score/docs-as-code>`_
and described in the :doc:`documentation generation <doc_generation>` chapter.


project_config.bzl
^^^^^^^^^^^^^^^^^^
**To adapt:** the safety level and the languages of your module.

Every Eclipse S-CORE module provides a ``project_config.bzl`` file in its root directory.
This file declares project-level metadata that is consumed by shared Bazel macros such as ``dash_license_checker``.

A minimal example:

.. code-block:: python
    :linenos:

    PROJECT_CONFIG = {
        "asil_level": "QM",        # Safety level: "QM", "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D"
        "source_code": ["cpp"],    # Languages used: "cpp", "rust", or both
    }

The ``asil_level`` documents the safety level of the module.
The ``source_code`` list is evaluated by ``dash_license_checker``: if no ``file_type`` is given,
it determines which dependency file is scanned (e.g., ``Cargo.lock`` for Rust, ``requirements.txt`` for Python).
The template declares ``["rust"]`` and scans ``examples/Cargo.lock``; set the list to the languages of your module
and point ``dash_license_checker`` to its dependency file.

.. tip::
    Start with ``"asil_level": "QM"`` during initial development.
    The level can be raised once the module's safety concept is established.


Component code and documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**To adapt:** the example component and the documents of the module.

- Rename ``score/component_example/`` to your component, incl. its Bazel targets, include paths and C++ namespace,
  or keep it as a pattern and add your own component next to it. The :doc:`build and test <building_source_code>`
  chapter walks through the example component.
- For every further component, create a folder ``score/<component>/`` with the same structure: ``src/``, ``tests/``,
  ``docs/`` and a ``BUILD`` file with the library, the tests and the ``docs_bundle``. Add the bundle of the component
  to the ``bundles`` of the ``docs`` macro in the top-level ``BUILD`` file. Code shared by several components
  can be placed in ``score/common/src/``.
- Adapt the titles, IDs and contents of the documents in ``docs/`` and ``score/<component>/docs/``.
  IDs of the template contain ``mod_temp`` or ``example_feature``, e.g. ``comp__mod_temp_component_name_template``;
  replace them by IDs of your module. Each document contains ``.. attention::`` boxes which list what needs to be
  adapted; remove them afterwards. The :doc:`documentation generation <doc_generation>` chapter explains the documents.


LICENSE, NOTICE and REUSE.toml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**To adapt:** nothing in ``LICENSE`` and ``NOTICE``; extend ``REUSE.toml`` for files which cannot carry a header.

The license files come with the template, so every S-CORE module is published under the same terms:

- ``LICENSE`` and ``LICENSES/Apache-2.0.txt`` contain the Apache License 2.0, the license of all S-CORE modules.
- ``NOTICE`` contains the notices of the Eclipse S-CORE project: project home, trademarks, copyright, the declared
  license and the cryptography notice.
- Every source file starts with the copyright and license header of the Eclipse Foundation, as in the files of the
  template. Files which cannot contain a comment, e.g. JSON files or lock files, are listed in
  `REUSE.toml <https://github.com/eclipse-score/module_template/blob/main/REUSE.toml>`_ instead.
  When you add such files, add them there as well.

The pre-commit checks and ``bazel run //:copyright.check`` report files without a valid header,
see :doc:`build and test <building_source_code>`.


README.md and CODEOWNERS
^^^^^^^^^^^^^^^^^^^^^^^^
**To adapt:** the description of your module in ``README.md``, and the maintainers in ``.github/CODEOWNERS``,
who review the pull requests of your repository.


Keeping up with the template
----------------------------
The template evolves, e.g. with new tool versions and workflow improvements. The workflow
`sync-template.yml <https://github.com/eclipse-score/module_template/blob/main/.github/workflows/sync-template.yml>`_
in your repository checks for changes of the template once a month (or when started manually in the *Actions* tab)
and opens a pull request *[Template Sync] Upstream template update*. Review it like any other pull request:
it can touch files which you have adapted to your module.
