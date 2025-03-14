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
#
# **Consistency**:
# When modifying Sphinx extensions or configuration, ensure all three methods
# (Esbonio, incremental, and Bazel) work as expected to avoid discrepancies.
#
# For user-facing documentation, refer to `/README.md`.

load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_venv")
load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("@rules_java//java:defs.bzl", "java_binary")
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("//docs:_tooling/extensions/score_source_code_linker/collect_source_files.bzl", "collect_source_files_for_score_source_code_linker")
load("//tools/dash:dash.bzl", "dash_license_checker")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")

sphinx_requirements = all_requirements + [
    "@rules_python//python/runfiles",
    ":plantuml_for_python",
]

def docs():
    """
    Creates all targets related to documentation.
    By using this function, you'll get any and all updates for documentation targets in one place.
    Current restrictions:
    * only callable from 'docs/BUILD'
    """
    collect_source_files_for_score_source_code_linker(
        name = "collected_files_for_score_source_code_linker",
        deps = [
            ":score_metamodel",
            ":score_source_code_linker",
        ],
    )

    # Run-time build of documentation, incl. incremental build support and non-IDE live preview.
    _incremental()

    # Virtual python environment for working on the documentation (esbonio).
    # incl. python support when working on conf.py and sphinx extensions.
    # creates :ide_support target for virtualenv
    _ide_support()

    # creates :docs target for build time documentation
    _docs()

def _incremental():
    """
    A target for building docs incrementally at runtime, incl live preview.
    """

    py_binary(
        name = "incremental",
        srcs = ["_tooling/incremental.py"],
        data = [":collected_files_for_score_source_code_linker"],
        deps = sphinx_requirements,
    )

    py_binary(
        name = "live_preview",
        srcs = ["_tooling/live_preview.py"],
        deps = sphinx_requirements,
    )

def _ide_support():
    py_venv(
        name = "ide_support",
        venv_name = ".venv_docs",
        deps = sphinx_requirements,
    )

def _docs():
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
            "**/*.csv",
        ]),
        config = ":conf.py",
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
