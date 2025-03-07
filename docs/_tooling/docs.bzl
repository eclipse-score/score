# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
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
"""Defines Bazel targets for running docs related actions."""

load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_venv")
load("@pip_sphinx//:requirements.bzl", "all_requirements")
load("@rules_java//java:defs.bzl", "java_binary")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")


# Multiple approaches are available to build the same documentation output:
#
# 1. **Esbonio via IDE support (`ide_support` target)**:
#    - Listed first as it offers the least flexibility in implementation.
#    - Designed for live previews and quick iterations when editing documentation.
#    - Integrates with IDEs like VS Code but requires the Esbonio extension.
#    - Requires a virtual environment with consistent dependencies (see 2).
#
# 2. **Directly running Sphinx in the virtual environment**:
#    - As mentioned above, a virtual environment is required for running esbonio.
#    - Therefore, the same environment can be used to run Sphinx directly.
#    - Option 1: Run Sphinx manually via `.venv_docs/bin/python -m sphinx docs _build --jobs auto`.
#    - Option 2: Use the `incremental` target, which simplifies this process.
#    - Usable in CI pipelines to validate the virtual environment used by Esbonio.
#    - Ideal for quickly generating documentation during development.
#
# 3. **Bazel-based build (`docs` target)**:
#    - Runs the documentation build in a Bazel sandbox, ensuring clean, isolated builds.
#    - Less convenient for frequent local edits but ensures build reproducibility.


sphinx_requirements = all_requirements + ["@rules_python//python/runfiles", ":plantuml_for_python"]

def all_docs_targets():
    """
    Creates all targets related to documentation.

    By using this function, you'll get any and all updates for documentation targets in one place.
    """

    # Run-time build of documentation, incl. incremental build support.
    incremental()

    #sphinx-autobuild, used for no IDE live preview
    live_preview()

    # Virtual python environment for working on the documentation (esbonio).
    # incl. python support when working on conf.py and sphinx extensions.

    # create  :plantuml & :plantuml_for_python targets
    plantuml_bzl()

    # creates :ide_support target for virtualenv
    ide_support()

    # creates :docs target for build time documentation
    docs()

def incremental(name = "incremental", extra_dependencies = list()):
    """
    A target for building docs incrementally at runtime.

    Args:
        name: Optional custom name for the target. Defaults to "incremental".
        extra_dependencies: Additional dependencies besides the centrally maintained "sphinx_requirements".
    """
    dependencies = sphinx_requirements + extra_dependencies

    py_binary(
        name = name,
        srcs = ["_tooling/incremental.py"],
        data = [":collected_files_for_score_source_code_linker"],
        deps = dependencies,
    )

def plantuml_bzl():
    java_binary(
        name = "plantuml",
        jvm_flags = ["-Djava.awt.headless=true"],
        main_class = "net.sourceforge.plantuml.Run",
        runtime_deps = [
            "@plantuml//jar",
        ],
    )

    # Note: this is the old comment. copy pasted here.

    # This makes it possible for py_venv to depend on plantuml.
    # Note: py_venv can only depend on py_library.
    # TODO: Investigate if this can be simplified with a custom bzl rule
    #       which replaces / wraps py_venv.
    #       see https://github.com/aspect-build/rules_py/blob/main/py/private/py_venv.bzl
    #       see https://github.com/bazelbuild/rules_python/blob/main/sphinxdocs/private/sphinx.bzl
    py_library(
        name = "plantuml_for_python",
        srcs = ["_tooling/dummy.py"],
        data = [
            ":plantuml",
        ],
    )

def live_preview():
    py_binary(
        name = "live_preview",
        srcs = ["_tooling/live_preview.py"],
        deps = sphinx_requirements,
    )

def ide_support():
    py_venv(
        name = "ide_support",
        venv_name = ".venv_docs",
        deps = sphinx_requirements,
    )

def docs():
    sphinx_docs(
        name = "docs",
        srcs = native.glob([
            "**/*.png",
            "**/*.svg",
            "**/*.rst",
            "**/*.html",
            "**/*.css",
            "**/*.puml",
            # Include the docs tooling itself
            # Note: we don't use py_library here to make it as close as possible to docs:incremental.
            "**/*.py",
            "**/*.yaml",
            "**/*.json",
        ]),
        config = "conf.py",
        extra_opts = [
            "-W",
            "--keep-going",
            # This is 'overwriting' the configuration parameter inside sphinx. As we only get this information during runtime
            "--define=source_code_linker_file=$(location :collected_files_for_score_source_code_linker)",
        ],
        formats = [
            "html",
        ],
        sphinx = ":sphinx_build",
        tags = [
            "manual",
        ],
        tools = [
            ":collected_files_for_score_source_code_linker",
            ":plantuml",
        ],
    )

    sphinx_build_binary(
        name = "sphinx_build",
        deps = sphinx_requirements,
    )
