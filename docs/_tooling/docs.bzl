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
load("//docs:_tooling/extensions/score_source_code_linker/collect_source_files.bzl", "parse_source_files_for_needs_links", "SourceCodeLinks")

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

def docs(source_files_to_scan_for_needs_links = None, source_dir = "docs", conf_dir = "docs", build_dir_for_incremental = "_build"):
    """
    Creates all targets related to documentation.

    By using this function, you'll get any and all updates for documentation targets in one place.

    Current restrictions:
    * only one docs() call per BUILD file is supported, as name mangling is not implemented yet.

    Args:
        source_files_to_scan_for_needs_links: The source files to scan for documentation links and requirements.
        source_dir: Directory containing the source files for documentation. Defaults to "docs".
        conf_dir: Directory containing the Sphinx configuration. Defaults to "docs".
        build_dir_for_incremental: Directory to output the built documentation for incremental builds. Defaults to "_build".
    """

    # Parse source files for needs links
    source_code_linker = parse_source_files_for_needs_links(
        name = "score_source_code_parser",
        srcs = source_files_to_scan_for_needs_links if source_files_to_scan_for_needs_links else [],
    )

    # Get the output of source_code_linker
    # Does not work:
    # rule_info = native.existing_rule(source_code_linker.name)
    # source_code_links = rule_info[SourceCodeLinks].file.path
    # Workaround:
    source_code_links = source_code_linker.name + ".json"

    # Run-time build of documentation, incl. incremental build support and non-IDE live preview.
    _incremental(source_code_linker, source_code_links, source_dir = source_dir, conf_dir = conf_dir, build_dir = build_dir_for_incremental)

    # create  :plantuml & :plantuml_for_python targets
    _plantuml_bzl()

    # Virtual python environment for working on the documentation (esbonio).
    # incl. python support when working on conf.py and sphinx extensions.
    # creates :ide_support target for virtualenv
    _ide_support()

    # creates :docs target for build time documentation
    _docs(source_code_linker, source_code_links)

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
        data = [source_code_linker, "//docs:docs_assets", "//docs:docs_stuff"],
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
        data = ["//docs:docs_assets", "//docs:docs_stuff"],
        deps = dependencies,
        env = {
            "SOURCE_DIRECTORY": source_dir,
            "CONF_DIRECTORY": conf_dir,
            "BUILD_DIRECTORY": build_dir,
            "ACTION": "live_preview",
        },
    )

def _plantuml_bzl():
    java_binary(
        name = "plantuml",
        jvm_flags = ["-Djava.awt.headless=true"],
        main_class = "net.sourceforge.plantuml.Run",
        runtime_deps = [
            "@plantuml//jar",
        ],
    )

    # This makes it possible for py_venv to depend on plantuml.
    # Note: py_venv can only depend on py_library.
    # TODO: Investigatee simplified with a custom bzl rule
    #       which replaces / wraps py_venv.
    #       see https://github.com/aspect-build/rules_py/blob/main/py/private/py_venv.bzl
    #       see https://github.com/bazelbuild/rules_python/blob/main/sphinxdocs/private/sphinx.bzl
    py_library(
        name = "plantuml_for_python",
        srcs = ["//docs:_tooling/dummy.py"],
        data = [
            ":plantuml",
            "//docs:docs_assets",
            "//docs:docs_stuff"
        ],
    )

def _ide_support():
    py_venv(
        name = "ide_support",
        venv_name = ".venv_docs",
        deps = sphinx_requirements,
        # data is avialable in next release after 12.03.2025
        # until then we inject data into plantuml_for_python
        # data = ["//docs:docs_assets", "//docs:docs_stuff"]
    )

def _docs(source_code_linker, _source_code_links):
    sphinx_docs(
        name = "docs",
        srcs = native.glob([
            "**/*.png",
            "**/*.svg",
            "**/*.rst",
            "**/*.html",
            "**/*.css",
            "**/*.puml",
        ]),
        config = "conf.py",
        extra_opts = [
            "-W",
            "--keep-going",
            # This is 'overwriting' the configuration parameter inside sphinx. As we only get this information during runtime
            "--define=source_code_linker_file=$(location {})".format(source_code_linker),
        ],
        formats = [
            "html",
        ],
        sphinx = ":sphinx_build",
        tags = [
            "manual",
        ],
        tools = [
            source_code_linker,
            ":plantuml",
        ],
    )

    sphinx_build_binary(
        name = "sphinx_build",
        deps = sphinx_requirements,
        data = ["//docs:docs_assets", "//docs:docs_stuff"],
    )
