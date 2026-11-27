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
load("@score_tools//cr_checker:cr_checker.bzl", "copyright_checker")

test_suite(
    name = "format.check",
    tests = ["//tools/format:format.check"],
)

alias(
    name = "format.fix",
    actual = "//tools/format:format.fix",
)

# The shared PR workflow runs //:copyright.check. The macro discovers its
# inputs through Git at the workspace root and exposes //:copyright.fix too.
copyright_checker(
    name = "copyright",
    visibility = ["//visibility:public"],
)

exports_files([
    "MODULE.bazel",
    "BUILD",
])

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
            "bundle": "//docs/features/daal:docs",
            "mount_at": "features/daal",
        },
        {
            "bundle": "//docs/features/diagnostics:docs",
            "mount_at": "features/diagnostics",
        },
        {
            "bundle": "//docs/features/feo:docs",
            "mount_at": "features/feo",
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
    external_needs = [
        "@score_docs_as_code//:needs_json_file",
        "@score_process_description//:needs_json_file",
    ],
)
