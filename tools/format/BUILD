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

format_multirun(
    name = "format.fix",
    python = "@score_devcontainer//tools:ruff_binary",
    starlark = "@score_devcontainer//tools:buildifier_binary",
    visibility = [
        "//visibility:public",
    ],
    yaml = "@score_devcontainer//tools:yamlfmt_binary",
)

format_test(
    name = "format.check",
    no_sandbox = True,
    python = "@score_devcontainer//tools:ruff_binary",
    starlark = "@score_devcontainer//tools:buildifier_binary",
    visibility = [
        "//visibility:public",
    ],
    workspace = "//:MODULE.bazel",
    yaml = "@score_devcontainer//tools:yamlfmt_binary",
)
