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
    external_needs = [
        "@score_docs_as_code//:needs_json_file",
        "@score_process_description//:needs_json_file",
    ],
)

# Expose the requirements for cross-repository use without a nested BUILD file,
# which would exclude them from //:docs' root-level glob.
exports_files(
    ["docs/features/log_and_trace/requirements/index.rst"],
    visibility = ["//visibility:public"],
)

# Preserve the previously published file label after flattening Log and Trace.
# Needs traceability is maintained separately through stable requirement IDs.
alias(
    name = "docs/features/log_and_trace/logging/requirements/index.rst",
    actual = ":docs/features/log_and_trace/requirements/index.rst",
    visibility = ["//visibility:public"],
)
