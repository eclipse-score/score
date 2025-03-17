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
load("//docs:_tooling/extensions/score_source_code_linker/collect_source_files.bzl", "parse_source_files_for_needs_links")
load("//tools/dash:dash.bzl", "dash_license_checker")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")

sphinx_requirements = all_requirements + [
    "@rules_python//python/runfiles",
    ":plantuml_for_python",
]

def docs(source_files_to_scan_for_needs_links = None, source_dir = "docs", conf_dir = "docs", build_dir_for_incremental = "_build"):
    """
    Creates all targets related to documentation.
    By using this function, you'll get any and all updates for documentation targets in one place.
    Current restrictions:
    * only callable from 'docs/BUILD'
    """

    # Parse source files for needs links
    parse_source_files_for_needs_links(
        name = "score_source_code_parser",
        srcs_and_deps = source_files_to_scan_for_needs_links if source_files_to_scan_for_needs_links else [],
    )

    # Get the output of source_code_linker
    # Does not work:
    # rule_info = native.existing_rule(source_code_linker.name)
    # source_code_links = rule_info[SourceCodeLinks].file.path
    # Workaround:
    source_code_links = "score_source_code_parser.json"

    # Run-time build of documentation, incl. incremental build support and non-IDE live preview.
    _incremental(":score_source_code_parser", source_code_links, source_dir = source_dir, conf_dir = conf_dir, build_dir = build_dir_for_incremental)

    # Virtual python environment for working on the documentation (esbonio).
    # incl. python support when working on conf.py and sphinx extensions.
    # creates :ide_support target for virtualenv
    _ide_support()

    # creates :docs target for build time documentation
    _docs()

def _incremental(source_code_linker, source_code_links, source_dir = "docs", conf_dir = "docs", build_dir = "_build", extra_dependencies = list()):
    """
    A target for building docs incrementally at runtime, incl live preview.
    Args:
        source_code_linker: The source code linker target to be used for linking source code to documentation.
        source_code_links: The output from the source code linker.
        source_dir: Directory containing the source files for documentation.
        conf_dir: Directory containing the Sphinx configuration.
        build_dir: Directory to output the built documentation.
        extra_dependencies: Additional dependencies besides the centrally maintained "sphinx_requirements".
    """

    dependencies = sphinx_requirements + extra_dependencies

    py_binary(
        name = "incremental",
        srcs = ["//docs:_tooling/incremental.py"],
        data = [source_code_linker, "//docs:docs_assets"],
        deps = dependencies,
        env = {
            "SOURCE_CODE_LINKS": source_code_links,
            "SOURCE_DIRECTORY": source_dir,
            "CONF_DIRECTORY": conf_dir,
            "BUILD_DIRECTORY": build_dir,
            "ACTION": "incremental",
        },
    )

    py_binary(
        name = "live_preview",
        srcs = ["//docs:_tooling/incremental.py"],
        data = ["//docs:docs_assets"],
        deps = dependencies,
        env = {
            "SOURCE_DIRECTORY": source_dir,
            "CONF_DIRECTORY": conf_dir,
            "BUILD_DIRECTORY": build_dir,
            "ACTION": "live_preview",
        },
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
            "--define=source_code_linker_file=$(location :score_source_code_parser)",
        ],
        formats = [
            "html",
        ],
        sphinx = ":sphinx_build",
        tags = [
            "manual",
        ],
        tools = [
            ":score_source_code_parser",
            ":plantuml",
        ],
    )
