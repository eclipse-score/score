First S-Core Module
=====================

The very first step would be to create a repository, where the future application should be located. Before you can do this,
you need to ensure that you are an official contributor in the S-Core project, otherwise you will not have any power in the project.
How to do this is described in
`Actions to ensure Proper Contribution Attribution in Eclipse S-Core <https://eclipse-score.github.io/score/main/contribute/general/contribution_attribution.html#>`_.

After you've created an Eclipse account, accepted Eclipse Contributor Agreement (ECA) and connected you GitHub
account with your Eclipse Account, you should approach one of the S-Core Project Leads, that are listed at the official
`Eclipse SDV S-Core webpage <https://projects.eclipse.org/projects/automotive.score/who>`_ and ask them to add you
to the list of the official contributors in the S-Core GitHub organization. The best way to approach S-Core
project leads would be over the `eclipse sdv slack channel <https://sdv.eclipse.org/get-engaged/>`_.

Once you are part of S-Core GitHub organization, you can request a repository for your application.
In the S-Core project this is done according to the rules of the Eclipse organization.
The majority of the configuration for the GitHub organization is done using `otterdog configuration <https://otterdog.readthedocs.io/en/latest/>`_
in the following repository: https://github.com/eclipse-score/.eclipsefdn. Create a private fork of this repository and modify
otterdog configuration in `otterdog/eclipse-score.jsonnet <https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet>`_
file by adding a new repository, in our case we do it for scrample repository like this:

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

Afterwards create a PR in the original https://github.com/eclipse-score/.eclipsefdn repository and wait till it will be approved
by S-Core project lead and eclipse security team.

.. tip::
    To get your PR approved sooner, it is a good idea to make sure that score project leads and eclipse security team
    are aware of your PR, therefore you can put smth. like this into PR's comment:
    
    .. code-block:: python
        
        @eclipse-score/automotive-score-project-leads
        @eclipse-score/eclipsefdn-security

        Please approve.

As soon as your PR is approved and merged (normally done by either security team or project lead),
you will be able to find your repo in the S-Core GitHub organization repositories overview.

.. image:: ../_assets/repository_layout.png
   :alt: repository layout
   :width: 500
   :align: center

If you will open the repository, you will see, that it is not empty. All repositories in S-Core are created based on
`S-Core repository template <https://github.com/eclipse-score/module_template>`_.
The `README.md <https://github.com/eclipse-score/module_template/blob/main/README.md>`_ file of the repository already
gives a good explanation regarding the structure of the repository, but let us have a
more detailed look at some of the files and folders.

.github/workflows/
------------------
This is the place where we define various CI/CD workflows for the repository, e.g. building of the source code or execution of the unit-tests
by every PR or as part of the integration gate :ref:`integration gate <integration_process>` during release tag creation.


.vscode
------------------
Provides S-Core recommended configuration for your VS Code setup including the code completion patterns for requirements and architecture 
in `.vscode/restructuredtext.code-snippets <https://github.com/eclipse-score/module_template/blob/main/.vscode/restructuredtext.code-snippets>`_.


docs
-----
This is the right folder to put all your documentation for your module in `rst format <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.
We will have later on an example how to do this.

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
`.bazelrc <https://github.com/eclipse-score/scrample/blob/main/.bazelrc>`_ file provides you the possibility to set-up the bazel configuration for your bazel module. We will extend the .bazelrc file
in the upcoming chapters with e.g. toolchains configuration, but here we just want to point out to the following config items:

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

The line number 8 points to the S-Core https://github.com/eclipse-score/bazel_registry, where all official versions of S-Core modules are published.
The line number 9 points to the common bazel registry, with common bazel modules are made available for everyone.

That means, that when we will reference a module as a dependency to our scrample application, bazel will search for the
modules in one of these two locations.

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

Here, we first declare our module, by giving it the name and its current version. Please be aware, that only after our module was published
in the S-Core bazel registry, other modules can access it.

We need to give our module now a reasonable name, so let us replace *cpp_rust_template_repository* with *score_scrample*.

.. code-block:: python
    :linenos:

    module(
        name = "score_scrample",
        version = "1.0",
    )

Please be aware, that there is a naming convention, that all modules names in S-Core should start with *score\_* prefix.     

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

In the code snippet above, we declare dependendencies to the modules, that are publically available in common bazel registry,
e.g. for unit test execution with gtest.

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

Here we add a llvm toolchain and register its usage in our module, so that we can build our source code. We will
talk about these in more details later in the upcoming chapters.    

.. code-block:: python
    :linenos:

    # tooling
    bazel_dep(name = "score_tooling", version = "1.0.1")

    #docs-as-code
    bazel_dep(name = "score_docs_as_code", version = "1.1.0")

Finally, we add dependency to S-Core native modules, *score_tooling* and *score_docs_as_code*, that enables us
building documentation and execute different kinds of checks, e.g. license checker.

.. tip::
    Please be aware that working with multiple modules located in various repositories can be really challenging,
    especially if you need to do the changes in multiple modules in parallel. You can use the following approach
    to make your life a little bit easier:

    use `git_override()  <https://bazel.build/rules/lib/globals/module#git_override>`_ if you want to use a version of another module, that is currently not officially availabe
    in the bazel registry.

    use `local_path_override()  <https://bazel.build/rules/lib/globals/module#local_path_override>`_ if you want to use the local version of the module, e.g. during active development.    

BUILD 
-----
Last but not least the bazel `BUILD <https://github.com/eclipse-score/scrample/blob/main/BUILD>`_ file
contains main bazel targets on the top level of the scrample project:

.. code-block:: python
    :linenos:

    load("@score_docs_as_code//:docs.bzl", "docs")
    load("@score_tooling//:defs.bzl", "copyright_checker", "dash_license_checker", "setup_starpls", "use_format_targets")
    load("//:project_config.bzl", "PROJECT_CONFIG")

First of all, we load bazel rules and macros, implemented in S-Core context from the modules, that we've defined as dependencies
in the MODULE.bazel file, e.g. https://github.com/eclipse-score/docs-as-code.

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


Finally, we define the target to build all documentation in the rst format, that is located in the
`docs <https://github.com/eclipse-score/docs-as-code/tree/main/docs>`_  folder and all its subfolders.
This functionality is implemented in https://github.com/eclipse-score/docs-as-code module.