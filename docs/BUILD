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

load("@docs-as-code//:docs.bzl", "docs")
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")

# Creates all documentation targets:
# - `docs:incremental` for building docs incrementally at runtime
# - `docs:live_preview` for live preview in the browser without an IDE
# - `docs:ide_support` for creating python virtualenv for IDE support
# - `docs:docs` for building documentation at build-time

docs(
    conf_dir = "docs",
    docs_targets = [
        {
            "suffix": "",  # local without external needs
        },
    ],
    source_dir = "docs",
    source_files_to_scan_for_needs_links = [],
    setup_dependencies = True,
)

# These are only exported because they're passed as files to the //docs.bzl
# macros, and thus must be visible to other packages. They should only be
# referenced by the //docs.bzl macros.

# In order to update the requirements, change the `requirements.txt` file and run:
# `bazel run //docs:requirements`.
# This will update the `requirements_lock.txt` file.
# To upgrade all dependencies to their latest versions, run:
# `bazel run //docs:requirements -- --upgrade`.

# Enables source_code_linker to parse all file types, not just .py

# Used inside //docs.bzl to enable access to the assets (css files etc.)
filegroup(
    name = "assets",
    srcs = glob([
        "_assets/**",
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

# Needed for Dash tool to check python dependency licenses.
# filegroup(
#     name = "requirements_lock",
#     srcs = [
#         "/requirements_lock.txt",
#     ],
#     visibility = ["//visibility:public"],
# )
