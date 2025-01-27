# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
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
"""Bazel interface for running pytest"""

load("@pip_sphinx//:requirements.bzl", "all_requirements")
load("@rules_python//python:defs.bzl", "py_test")

def py_pytest(name, srcs, args = [], data = [], deps = [], plugins = [], pytest_ini = None, **kwargs):
    pytest_bootstrap = Label("//tools/testing/pytest:main.py")

    if not pytest_ini:
        pytest_ini = Label("//tools/testing/pytest:pytest.ini")

    if not srcs:
        fail("No source files provided for %s! (Is your glob empty?)" % name)

    plugins = ["-p %s" % plugin for plugin in plugins]

    py_test(
        name = name,
        srcs = [
            pytest_bootstrap,
        ] + srcs,
        main = pytest_bootstrap,
        args = args +
               ["-c $(location %s)" % pytest_ini] +
               [
                   "-p no:cacheprovider",
                   "--show-capture=no",
               ] +
               plugins +
               ["$(location %s)" % x for x in srcs],
        deps = all_requirements + deps,
        data = [
            pytest_ini,
        ] + data,
        env = {
            "PYTHONDONOTWRITEBYTECODE": "1",
        },
        **kwargs
    )
