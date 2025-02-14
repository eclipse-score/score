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

"""Defines Bazel rules for running copyright checks and fixes."""

def copyright_checker(
        name,
        srcs,
        visibility,
        template = "//tools/cr_checker/resources:templates",
        config = "//tools/cr_checker/resources:config",
        extensions = [],
        offset = 0,
        remove_offset = 0,
        debug = False,
        use_memory_map = False,
        fix = False):
    """
    Defines a custom build rule for checking and optionally fixing files for compliance
    with specific requirements, such as copyright headers.

    Args:
        name (str): The name of the rule, used as an identifier in the build system.
        srcs (list): A list of source file paths to check.
        visibility (list): A list defining the visibility of the rule, specifying which
                           targets can use this rule.
        template (str, optional): Path to the template resource used for validation.
                                  Defaults to "//tools/cr_checker/resources:templates".
        config (str, optional): Path to the config resource used for project variables.
                                Defaults to "//tools/cr_checker/resources:config".
        extensions (list, optional): A list of file extensions to filter the source files.
                                     Defaults to an empty list, meaning all files are checked.
        offset (int, optional): The line offset for applying checks or modifications.
                                Defaults to 0.
        remove_offset (int, optional): The line offset for removing chars from begining of file.
                                Defaults to 0.
        debug (bool, optional): Whether to enable debug mode, providing additional logs.
                                Defaults to False.
        use_memory_map (bool, optional): Whether to use memory mapping for large files to
                                         improve performance. Defaults to False.
        fix (bool, optional): Whether to apply fixes to files instead of just reporting issues.
                                         Defaults to False.

    Returns:
        None: This function defines a rule for a build system and does not return a value.
    """
    t_names = [
        "{}.check".format(name),
        "{}.fix".format(name),
    ]

    args = [
        "-t $(location {})".format(template),
        "-c $(location {})".format(config),
    ]
    data = []
    if len(extensions):
        args.append("-e {exts}".format(
            exts = " ".join([exts for exts in extensions]),
        ))

    if offset:
        args.append("--offset {}".format(offset))

    if debug:
        args.append("-v")

    if use_memory_map:
        args.append("--use_memory_map")

    for src in srcs:
        args.append("$(locations {})".format(src))

    for t_name in t_names:
        if t_name == "{}.fix".format(name):
            args.insert(0, "--fix")
            if remove_offset:
                args.append("--remove_offset {}".format(remove_offset))

        native.py_binary(
            name = t_name,
            main = "cr_checker.py",
            srcs = [
                "//tools/cr_checker/tool:cr_checker_lib",
            ],
            args = args,
            data = srcs + [
                template,
                config,
            ],
            visibility = visibility,
        )
