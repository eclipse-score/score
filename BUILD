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
load("@score_tooling//:defs.bzl", "cli_helper", "copyright_checker", "setup_starpls")

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
    config = "@score_tooling//cr_checker/resources:config",
    template = "@score_tooling//cr_checker/resources:templates",
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
    bundles = [
        {
            "bundle": "//docs/features/ai_platform:docs",
            "mount_at": "features/ai_platform",
        },
        {
            "bundle": "//docs/features/baselibs:docs",
            "mount_at": "features/baselibs",
        },
        {
            "bundle": "//docs/features/code_generation:docs",
            "mount_at": "features/code_generation",
        },
        {
            "bundle": "//docs/features/communication:docs",
            "mount_at": "features/communication",
        },
        {
            "bundle": "//docs/features/configuration:docs",
            "mount_at": "features/configuration",
        },
        {
            "bundle": "//docs/features/diagnostics:docs",
            "mount_at": "features/diagnostics",
        },
        {
            "bundle": "//docs/features/frameworks:docs",
            "mount_at": "features/frameworks",
        },
        {
            "bundle": "//docs/features/lifecycle:docs",
            "mount_at": "features/lifecycle",
        },
        {
            "bundle": "//docs/features/log_and_trace:docs",
            "mount_at": "features/log_and_trace",
        },
        {
            "bundle": "//docs/features/orchestration:docs",
            "mount_at": "features/orchestration",
        },
        {
            "bundle": "//docs/features/persistency:docs",
            "mount_at": "features/persistency",
        },
        {
            "bundle": "//docs/features/security_crypto:docs",
            "mount_at": "features/security_crypto",
        },
        {
            "bundle": "//docs/features/time:docs",
            "mount_at": "features/time",
        },
    ],
    data = [
        "@score_process_description//:needs_json",
    ],
    source_dir = "docs",
)
