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

load("@trlc_renderer_dependencies//:requirements.bzl", "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

sh_binary(
    name = "trlc_wrapper",
    srcs = ["trlc_wrapper.sh"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "trlc_renderer",
    srcs = [
        "trlc_renderer.py",
        ],
    visibility = ["//visibility:public"],
    deps = [
        "@trlc//trlc",
        requirement("bigtree"),
        requirement("pydot"),
        requirement("debugpy"),
    ],
)

# Run bazel run //tools/trlc_renderer:requirements.update
compile_pip_requirements(
    name = "requirements",
    src = "requirements.txt.in",
    requirements_txt = "requirements.txt",
)
