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
load("@score_pytest//:defs.bzl", "py_pytest")

py_pytest(
    name = "test",
    size = "small",
    srcs = [
        "check_options_test.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//docs/_tooling/sphinx_extensions",
    ],
)
