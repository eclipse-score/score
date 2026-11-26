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

load("@score_docs_as_code//:docs.bzl", "docs")

# Load the developer tools from their own packages to keep Dash's Starlark
# dependencies out of the Score root package.
load("@score_tooling//cli_helper:cli_helper.bzl", "cli_helper")
load("@score_tooling//starpls:starpls.bzl", "setup_starpls")
load("@score_tools//cr_checker:cr_checker.bzl", "copyright_checker")

test_suite(
    name = "format.check",
    tags = [
        "cli_help=Check formatting:\n" +
        "bazel test //:format.check",
    ],
    tests = ["//tools/format:format.check"],
)

alias(
    name = "format.fix",
    actual = "//tools/format:format.fix",
    tags = [
        "cli_help=Fix formatting:\n" +
        "bazel run //:format.fix",
    ],
)

# The shared PR workflow runs //:copyright.check. The macro discovers its
# inputs through Git at the workspace root and exposes //:copyright.fix too.
copyright_checker(
    name = "copyright",
    visibility = ["//visibility:public"],
)

cli_helper(
    name = "cli-help",
    visibility = ["//visibility:public"],
)

exports_files([
    "MODULE.bazel",
    "BUILD",
])

setup_starpls(
    name = "starpls_server",
    visibility = ["//visibility:public"],
)

docs(
    external_needs = [
        "@score_docs_as_code//:needs_json_file",
        "@score_process_description//:needs_json_file",
    ],
)

# Exposed (without a nested BUILD file, to avoid excluding it from //:docs'
# root-level glob) for cross-repo consumption by score_logging for trlc import.
exports_files(
    ["docs/features/log_and_trace/logging/requirements/index.rst"],
    visibility = ["//visibility:public"],
)
