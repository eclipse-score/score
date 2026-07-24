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

load("@aspect_rules_lint//format:defs.bzl", "format_multirun", "format_test")

alias(
    name = "yamlfmt_binary",
    actual = "@score_devcontainer//tools:yamlfmt_binary",
    visibility = ["//visibility:public"],
)

alias(
    name = "ruff_binary",
    actual = "@score_devcontainer//tools:ruff_binary",
    visibility = ["//visibility:public"],
)

alias(
    name = "buildifier_binary",
    actual = "@score_devcontainer//tools:buildifier_binary",
    visibility = ["//visibility:public"],
)

format_multirun(
    name = "format.fix",
    python = ":ruff_binary",
    starlark = ":buildifier_binary",
    visibility = [
        "//visibility:public",
    ],
    yaml = ":yamlfmt_binary",
)

format_test(
    name = "format.check",
    no_sandbox = True,
    python = ":ruff_binary",
    starlark = ":buildifier_binary",
    visibility = [
        "//visibility:public",
    ],
    workspace = "//:MODULE.bazel",
    yaml = ":yamlfmt_binary",
)
