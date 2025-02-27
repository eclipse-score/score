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
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("//docs:_tooling/extensions/score_source_code_linker/collect_source_files.bzl", "collect_source_files_for_score_source_code_linker")
load("//tools/dash:dash.bzl", "dash_license_checker")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")

config_setting(
    name = "ci_build",
    values = {
        # Matches when user passes --define=CI_BUILD=true
        "define": "CI_BUILD=true",
    },
)

sphinx_requirements = all_requirements + [
    "@rules_python//python/runfiles",
    ":plantuml_for_python",
]

sphinx_docs(
    name = "docs",
    srcs = glob([
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

sphinx_build_binary(
    name = "sphinx_build",
    deps = sphinx_requirements,
)

# In order to update the requirements, change the `requirements.txt` file and run:
# `bazel run //docs:requirements`.
# This will update the `requirements_lock.txt` file.
# To upgrade all dependencies to their latest versions, run:
# `bazel run //docs:requirements -- --upgrade`.
compile_pip_requirements(
    name = "requirements",
    src = "_tooling/requirements.txt",
    requirements_txt = "_tooling/requirements_lock.txt",
    tags = [
        "manual",
    ],
)

filegroup(
    name = "html",
    srcs = [":docs"],
    output_group = "html",
)

pkg_files(
    name = "html_files",
    srcs = [":html"],
    renames = {"html": ""},
)

pkg_tar(
    name = "github-pages",
    srcs = [":html_files"],
)

# Run-time build of documentation, incl. incremental build support.
py_binary(
    name = "incremental",
    srcs = ["_tooling/incremental.py"],
    data = [":collected_files_for_score_source_code_linker"],
    deps = sphinx_requirements,
)

#sphinx-autobuild, used for no IDE live preview
py_binary(
    name = "live_preview",
    srcs = ["_tooling/live_preview.py"],
    deps = sphinx_requirements,
)

# Virtual python environment for working on the documentation (esbonio).
# incl. python support when working on conf.py and sphinx extensions.
py_venv(
    name = "ide_support",
    venv_name = ".venv_docs",
    deps = sphinx_requirements,
)

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

# Dedicated metamodel target only for pytest.
# It's required to define the imports for bazel pytest, so that python/pytest can
# import "from score_metamodel" without issues.
py_library(
    name = "score_metamodel",
    srcs = glob(["_tooling/extensions/score_metamodel/**/*.py"]),
    imports = ["_tooling/extensions"],
    visibility = ["//visibility:public"],
)

score_py_pytest(
    name = "score_metamodel_test",
    size = "small",
    srcs = glob(["_tooling/extensions/score_metamodel/tests/**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [":score_metamodel"],
)

# ───────────────────────── Source code linker ────────────────────────
# For more information see documentation at _tooling/extensions/score_source_code_linker/README.md
py_library(
    name = "score_source_code_linker",
    srcs = glob(
        ["_tooling/extensions/score_source_code_linker/**/*.py"],
        exclude = ["_tooling/extensions/score_source_code_linker/tests/*.py"],
    ),
    imports = ["_tooling/extensions"],
    visibility = ["//visibility:public"],
)

score_py_pytest(
    name = "score_source_code_linker_test",
    size = "small",
    srcs = glob(["_tooling/extensions/score_source_code_linker/tests/**/*.py"]),
    deps = [
        ":score_source_code_linker",
    ],
)

# Needed to make the file parser executeable and findable for the aspect below
py_binary(
    name = "parsed_source_files_for_source_code_linker",
    srcs = ["_tooling/extensions/score_source_code_linker/parse_source_files.py"],
    visibility = ["//visibility:public"],
)

# Running this executes the `collect_source_files.bzl` aspect.
# Collects all source files from specified targets in 'deps', and makes them available for parsing for the source_code_linker

# For more information see documentation at _tooling/extensions/score_source_code_linker/README.md
collect_source_files_for_score_source_code_linker(
    name = "collected_files_for_score_source_code_linker",
    deps = [
        ":score_metamodel",
        ":score_source_code_linker",
    ],
)

# Needed for Dash tool to check python dependency licenses.
filegroup(
    name = "requirements_lock",
    srcs = [
        "_tooling/requirements_lock.txt",
    ],
    visibility = ["//visibility:public"],
)

dash_license_checker(
    name = "python",
    src = "//docs:requirements_lock",
    visibility = ["//visibility:public"],
)
