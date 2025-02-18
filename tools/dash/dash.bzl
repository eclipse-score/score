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

load("@rules_java//java:java_binary.bzl", "java_binary")
load("//tools/dash/formatters:dash_format_converter.bzl", "dash_format_converter")

def dash_license_checker(
        name,
        src,
        visibility):
    """
    Defines a Bazel macro for creating a `java_binary` target that integrates the DASH license checker.

    Args:
        name (str):
            The name of the `java_binary` target to be created. This will serve as the identifier
            for the generated Bazel target.
        src (str):
            The path to the dependency list file required by the DASH license checker.
            This file should specify the dependencies to be validated.
        visibility (list[str]):
            A list defining the visibility of the created target. It determines which packages
            can depend on this target.

    This macro simplifies the process of setting up the DASH license checker by creating a reusable
    `java_binary` target that adheres to the Bazel build rules and supports consistent license
    validation across projects.
    """
    dash_format_converter(
        name = "{}2dash".format(name),
        requirement_file = src,
    )

    java_binary(
        name = "license.check.{}".format(name),
        main_class = "org.eclipse.dash.licenses.cli.Main",
        runtime_deps = [
            "@dash_license_tool//jar",
        ],
        args = ["$(location :{}2dash)".format(name)],
        data = [
            ":{}2dash".format(name),
        ],
        visibility = ["//visibility:public"],
    )
