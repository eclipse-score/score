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

load("@score_cli_helper//:cli_helper.bzl", "cli_helper")
load("@score_cr_checker//:cr_checker.bzl", "copyright_checker")
load("@score_starpls_lsp//:starpls.bzl", "setup_starpls")

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

copyright_checker(
    name = "copyright",
    srcs = [
        ".github",
        "docs",
        "tools",
        "//:BUILD",
        "//:MODULE.bazel",
    ],
    config = "@score_cr_checker//resources:config",
    template = "@score_cr_checker//resources:templates",
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
