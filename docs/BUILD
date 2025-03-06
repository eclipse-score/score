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

load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library")
load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("//docs:_tooling/extensions/score_source_code_linker/collect_source_files.bzl","collect_and_parse")
load("//tools/dash:dash.bzl", "dash_license_checker")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")
load("//docs:_tooling/bzl/docs.bzl", "incremental", "plantuml_bzl", "live_preview", "ide_support", "docs")


# creates target //docs:docs
docs()

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
incremental()

#sphinx-autobuild, used for no IDE live preview
live_preview()

# Virtual python environment for working on the documentation (esbonio).
# incl. python support when working on conf.py and sphinx extensions.

# create  :plantuml & :plantuml_for_python targets
plantuml_bzl()

# creates :ide_support target for virtualenv
ide_support()

# Idea: replace glob with 'filegroup' 

score_py_pytest(
    name = "score_metamodel_test",
    size = "small",
    srcs = glob(["_tooling/extensions/score_metamodel/**/*.py"]), 
    visibility = ["//visibility:public"],
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
    srcs = glob(["_tooling/extensions/score_source_code_linker/**/*.py"]),
)

# Needed to make the file parser executeable and findable for the aspect below

# Running this executes the `collect_source_files.bzl` aspect.
# Collects all source files from specified targets in 'deps', and makes them available for parsing for the source_code_linker

# For more information see documentation at _tooling/extensions/score_source_code_linker/README.md

# Creates target for 'collect_source_files_for_score_source_code_linker' aspect
collect_and_parse(
    srcs=glob(["_tooling/extensions/score_metamodel/**/*.py"]),
    deps = [
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
