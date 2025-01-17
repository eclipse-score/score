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
load("@aspect_rules_py//py:defs.bzl", "py_library")
load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")

py_library(
    name = "sphinx_extensions",
    srcs = glob(["sphinx_extensions/**/*.py"]),
    imports = ["."],
    visibility = [
        "//visibility:public",
    ],
    deps = [
        requirement("sphinx"),
        requirement("sphinx-needs"),
        requirement("sphinxcontrib-plantuml"),
    ],
)

compile_pip_requirements(
    name = "requirements",
    src = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)
