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
#
# **Consistency**:
# When modifying Sphinx extensions or configuration, ensure all methods of building documentation
# (Esbonio, incremental, and Bazel) work as expected to avoid discrepancies.
#
# For user-facing documentation, refer to `/README.md`.

load("@aspect_rules_py//py:defs.bzl", "py_library")
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("//docs:_tooling/bzl/docs.bzl", "all_docs_targets")
load("//docs:_tooling/extensions/score_source_code_linker/collect_source_files.bzl", "collect_and_parse")
load("//tools/dash:dash.bzl", "dash_license_checker")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")

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

# Creates all documentation targets:
# - `docs:incremental` for building docs incrementally at runtime
# - `docs:live_preview` for live preview in the browser without an IDE
# - `docs:ide_support` for creating python virtualenv for IDE support
# - `docs:docs` for building documentation at build-time
# - `docs:plantuml` and `:plantuml_for_python` targets, to be used as dependencies for plantuml generation
all_docs_targets()

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
    deps = [
        ":score_metamodel_test", # score_metamodel incl tests
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
