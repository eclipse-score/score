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
load("@custom_extra_pip//:requirements.bzl", "all_requirements", "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# In order to update the requirements, change the `custom_extra_requirements.in` file and run:
# `bazel run //:requirements.update`.
# This will update the `requirements.txt` file.
# To upgrade all dependencies to their latest versions, run:
# `bazel run //:requirements.update -- --upgrade`.
compile_pip_requirements(
    name = "requirements",
    srcs = [
        "custom_extra_requirements.in",
        "@score_docs_as_code//src:requirements.txt",
    ],
    requirements_txt = "requirements.txt",
    tags = [
        "manual",
    ],
)

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
    data = [
        "@score_process//:needs_json",
    ],
    deps = [
        requirement("sphinxemoji"),
    ],
    source_dir = "docs",
)
