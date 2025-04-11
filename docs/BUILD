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

load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_venv")
load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("//docs:_tooling/docs.bzl", "docs")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")

sphinx_requirements = all_requirements + [
    "@rules_python//python/runfiles",
    ":plantuml_for_python",
]

# Creates all documentation targets:
# - `docs:incremental` for building docs incrementally at runtime
# - `docs:live_preview` for live preview in the browser without an IDE
# - `docs:ide_support` for creating python virtualenv for IDE support
# - `docs:docs` for building documentation at build-time
docs(source_files_to_scan_for_needs_links = [
    # Note: you can add filegroups, globs, or entire targets here.
    ":score_metamodel_files",
    ":score_source_code_linker",
])

sphinx_build_binary(
    name = "sphinx_build",
    deps = sphinx_requirements,
)

# These are only exported because they're passed as files to the //docs.bzl
# macros, and thus must be visible to other packages. They should only be
# referenced by the //docs.bzl macros.
exports_files(
    glob(
        [
            "_tooling/**/*.py",
        ],
    ) + ["_tooling/requirements_lock.txt"],
    visibility = ["//visibility:public"],
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

# Enables source_code_linker to parse all file types, not just .py
filegroup(
    name = "score_metamodel_files",
    srcs = glob(
        ["_tooling/extensions/score_metamodel/**"],
        exclude = ["**/__pycache__/**"],
    ),
    visibility = ["//visibility:public"],
)

# Used inside //docs.bzl to enable access to the assets (css files etc.)
filegroup(
    name = "docs_assets",
    srcs = glob([
        "_assets/**",
        "_tooling/assets/**",
    ]),
    visibility = ["//visibility:public"],
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
# TODO: This can be removed with the next
# upgrade of `aspect_rules_py` since the py_venv rule now supports a data field
py_library(
    name = "plantuml_for_python",
    srcs = ["_tooling/dummy.py"],
    data = [
        ":plantuml",
    ],
)

filegroup(
    name = "test_rst_files",
    srcs = glob([
        "_tooling/extensions/score_metamodel/tests/rst/**/*.rst",
        "_tooling/extensions/score_plantuml.py",
        "_tooling/extensions/score_draw_uml_funcs/**/*.py",
        "_tooling/extensions/score_source_code_linker/**/*.py",
        "_tooling/extensions/score_layout/**/*.py",
        "_tooling/extensions/score_header_service/**/*.py",
        "conf.py",
    ]),
    visibility = ["//visibility:public"],
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
    data = [
        ":test_rst_files",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":score_metamodel",
    ],
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

# Needed to make the file parser executeable and findable for the source_code_linker aspect
py_binary(
    name = "parsed_source_files_for_source_code_linker",
    srcs = ["_tooling/extensions/score_source_code_linker/parse_source_files.py"],
    visibility = ["//visibility:public"],
)

# Running this executes the `collect_source_files.bzl` aspect.
# Collects all source files from specified targets in 'deps', and makes them available for parsing for the source_code_linker

# Needed for Dash tool to check python dependency licenses.
filegroup(
    name = "requirements_lock",
    srcs = [
        "_tooling/requirements_lock.txt",
    ],
    visibility = ["//visibility:public"],
)

# Dedicated metamodel target only for pytest.
# It's required to define the imports for bazel pytest, so that python/pytest can
# import "from header_service" without issues.
py_library(
    name = "header_service",
    srcs = glob(["_tooling/extensions/score_header_service/**/*.py"]),
    imports = ["_tooling/extensions"],
    visibility = ["//visibility:public"],
)

score_py_pytest(
    name = "header_service_test",
    size = "small",
    srcs = glob(["_tooling/extensions/score_header_service/test/**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [":header_service"],
)
