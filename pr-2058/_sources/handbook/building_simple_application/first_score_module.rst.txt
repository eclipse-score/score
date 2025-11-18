..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

.. toctree::
   :maxdepth: 1
   :glob:

Before starting, please make sure that you are an official contributor to the Eclipse S-CORE project,
otherwise you will not have required permissions. An introduction how to do so, you can find in
`Actions to ensure Proper Contribution Attribution in Eclipse Eclipse S-CORE <https://eclipse-score.github.io/score/main/contribute/general/contribution_attribution.html#>`_.
 
Once you’ve created an Eclipse account/accepted Eclipse Contributor Agreement (ECA)/connected your GitHub account
with your Eclipse Account, you should contact one of the Eclipse S-CORE Project Leads
(listed at the official `Eclipse SDV S-Core webpage <https://projects.eclipse.org/projects/automotive.score/who>`_  )
to add you to the list of the official contributors of the Eclipse S-CORE GitHub organization.
The best way to approach Eclipse S-CORE project leads would be via the `eclipse sdv slack channel <https://sdv.eclipse.org/get-engaged/>`_.
 
Now since you are a part of Eclipse S-CORE GitHub organization, you are able to create a repository for your application.
In the Eclipse S-CORE project, this is done according to the rules of the Eclipse organization.
A vast majority of configurations for the GitHub organization is done using `otterdog configuration <https://otterdog.readthedocs.io/en/latest/>`_
in the following repository: https://github.com/eclipse-score/.eclipsefdn.
Create a private fork of this repository and modify otterdog configuration
in `otterdog/eclipse-score.jsonnet <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_ file,
by adding a new repository. In our case it´s the scrample repository:

.. code-block:: python
    :emphasize-lines: 4, 5, 6

    newModuleRepo('logging') {
        description: "Repository for logging framework",
    },
    newModuleRepo('scrample') {
        description: "Repository for example component",
    },  
    newModuleRepo('inc_abi_compatible_datatypes') {
        description: "Incubation repository for ABI compatible data types feature",
    },

Then, create a PR in the original  https://github.com/eclipse-score/.eclipsefdn repository and wait for its approval
by Eclipse S-CORE project lead and eclipse security team.


.. tip::
    To get your PR approved sooner, it is a good idea to make sure that score project leads and eclipse security team
    are aware of your PR, therefore you can put smth. like this into PR's comment:
    
    .. code-block:: python
        
        @eclipse-score/automotive-score-project-leads
        @eclipse-score/eclipsefdn-security

        Please approve.

As soon as your PR is approved and merged (normally done by either security team or project lead),
you will be able to find your repo in the Eclipse S-CORE GitHub organization repositories overview.


.. image:: ../_assets/repository_layout.png
   :alt: repository layout
   :width: 500
   :align: center

By opening the repository, you will see, it´s not empty.
All repositories in Eclipse S-CORE are created based on `Eclipse S-CORE repository template <https://github.com/eclipse-score/module_template>`.
The `README.md <https://github.com/eclipse-score/module_template/blob/main/README.md>`_ file
of the repository already gives a good explanation regarding the structure of the repository.
However, let us have a more detailed look to some files and folders.


.github/workflows/
------------------
This is the place where we define various CI/CD workflows for the repository, e.g.
building of the source code or execution of the unit-tests by every PR or as part of the integration gate
:ref:`integration gate <integration_process>` during release tag creation.


.vscode
------------------
Provides Eclipse S-CORE recommended configuration for your VS Code setup,
including the code completion patterns for requirements and architecture in
`.vscode/restructuredtext.code-snippets <https://github.com/eclipse-score/module_template/blob/main/.vscode/restructuredtext.code-snippets>`_.


docs
-----
This is the appropriate folder to put all documentation for your module in
`rst format <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.
Later on. we will have an example how to do this.

.. tip::
    We try to describe most `common workflows <https://eclipse-score.github.io/score/main/contribute/contribution_request/index.html#doc__contr_guideline>`_ 
    for developers. It is worth checking it.

src
-----
self explaining


test
-----
self explaining


.bazelrc 
--------
With `.bazelrc <https://github.com/eclipse-score/scrample/blob/main/.bazelrc>`_ file you can set-up the bazel configuration
for your bazel module. We will further extend the .bazelrc file in the upcoming chapters, e.g., with toolchain configuration.
Here, we just want to highlight following config items:

.. code-block:: python
    :linenos:
    :emphasize-lines: 8, 9

    build --java_language_version=17
    build --tool_java_language_version=17
    build --java_runtime_version=remotejdk_17
    build --tool_java_runtime_version=remotejdk_17

    test --test_output=errors

    common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
    common --registry=https://bcr.bazel.build

The line number 8 points to the Eclipse S-CORE https://github.com/eclipse-score/bazel_registry,
where all official versions of Eclipse S-CORE modules are published.
The line number 9 points to the common bazel registry, where common bazel modules are made available for everyone.
This means, once we´re referencing a depending module with our scrample application,
bazel will start searching it in one of these two locations.


MODULE.bazel 
-------------
This is actually the file, that makes our repository to the bazel module.
Let us check `MODULE.bazel <https://github.com/eclipse-score/scrample/blob/main/MODULE.bazel>`_ initial content:

.. code-block:: python
    :linenos:

    module(
        name = "cpp_rust_template_repository",
        version = "1.0",
    )

Here, we´re making the first declaration of our module by defining a name and a version.
Please be aware, that only after our module was published in the Eclipse S-CORE bazel registry, other modules can access it.

Now we need to give a reasonable name to our module, so let us replace *cpp_rust_template_repository* with *score_scrample*.

.. code-block:: python
    :linenos:

    module(
        name = "score_scrample",
        version = "1.0",
    )

Please be aware, based on Eclipse S-CORE´s naming convention all names must start with *score\_* prefix.
 
.. code-block:: python
    :linenos:

    bazel_dep(name = "rules_python", version = "1.4.1")

    PYTHON_VERSION = "3.12"

    python = use_extension("@rules_python//python/extensions:python.bzl", "python")
    python.toolchain(
        is_default = True,
        python_version = PYTHON_VERSION,
    )
    use_repo(python)

    # Add GoogleTest dependency
    bazel_dep(name = "googletest", version = "1.17.0")

    # Rust rules for Bazel
    bazel_dep(name = "rules_rust", version = "0.63.0")

    # C/C++ rules for Bazel
    bazel_dep(name = "rules_cc", version = "0.2.1")

In the code snippet above, we declare dependencies to modules, that are publicly available in common bazel registry, e.g.
for unit test execution with gtest.

.. code-block:: python
    :linenos:

    # LLVM Toolchains Rules - host configuration
    bazel_dep(name = "toolchains_llvm", version = "1.4.0")

    llvm = use_extension("@toolchains_llvm//toolchain/extensions:llvm.bzl", "llvm")
    llvm.toolchain(
        cxx_standard = {"": "c++17"},
        llvm_version = "19.1.0",
    )
    use_repo(llvm, "llvm_toolchain")
    use_repo(llvm, "llvm_toolchain_llvm")

    register_toolchains("@llvm_toolchain//:all")

Here we add a llvm toolchain and register its usage in our module, so that we can build our source code.
In upcoming chapters, we will talk about this in more detail.    

.. code-block:: python
    :linenos:

    # tooling
    bazel_dep(name = "score_tooling", version = "1.0.1")

    #docs-as-code
    bazel_dep(name = "score_docs_as_code", version = "1.1.0")

Finally, we add a dependency to Eclipse S-CORE native modules “*score_tooling*” and “*score_docs_as_code*”,
which will enable us to build documentation and execute different kinds of checks (e.g. license checker).

.. tip::
    Please be aware that working with multiple modules located in various repositories can be really challenging,
    especially if you need to do the changes in multiple modules in parallel. You can use the following approach
    to make your life a little bit easier:

    use `git_override()  <https://bazel.build/rules/lib/globals/module#git_override>`_ if you want to use a version of another module, that is currently not officially availabe
    in the bazel registry.

    use `local_path_override()  <https://bazel.build/rules/lib/globals/module#local_path_override>`_ if you want to use the local version of the module, e.g. during active development.    

BUILD 
-----
Last but not least, the bazel `BUILD <https://github.com/eclipse-score/scrample/blob/main/BUILD>`_ file
contains main bazel targets on the top level of the scrample project:

.. code-block:: python
    :linenos:

    load("@score_docs_as_code//:docs.bzl", "docs")
    load("@score_tooling//:defs.bzl", "copyright_checker", "dash_license_checker", "setup_starpls", "use_format_targets")
    load("//:project_config.bzl", "PROJECT_CONFIG")

First, we load bazel rules and macros, implemented in Eclipse S-CORE context from the modules,
that we’ve defined as dependencies in the MODULE.bazel file, e.g. https://github.com/eclipse-score/docs-as-code.

.. code-block:: python
    :linenos:

    copyright_checker(
        name = "copyright",
        srcs = [
            "src",
            "tests",
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

Second, we define bazel targets for *copyright_checker* and *dash_license_checker*,
based on bazel rules implemented and imported from https://github.com/eclipse-score/tooling module.

.. code-block:: python
    :linenos:

    docs(
        source_dir = "docs",
    )

Finally, we define the target to build all documentation in the rst format, which is located in the 
`docs <https://github.com/eclipse-score/docs-as-code/tree/main/docs>`_ folder and all its subfolders.
This functionality is implemented in https://github.com/eclipse-score/docs-as-code module.
