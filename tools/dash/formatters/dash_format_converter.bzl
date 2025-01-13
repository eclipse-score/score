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

""" Bazel rule for generating dash formatted requirements file
"""

def _impl(ctx):
    """ The implementation function of the rule.
    """

    output = ctx.actions.declare_file("formatted.txt")
    args = ctx.actions.args()
    args.add("-i", ctx.file.requirement_file)
    args.add("-o", output)

    ctx.actions.run(
        inputs = [ctx.file.requirement_file],
        outputs = [output],
        arguments = [args],
        progress_message = "Generating Dash formatted dependency file ...",
        mnemonic = "DashFormat",
        executable = ctx.executable._tool,
    )
    return DefaultInfo(files = depset([output]))

dash_format_converter = rule(
    implementation = _impl,
    attrs = {
        "requirement_file": attr.label(
            mandatory = True,
            allow_single_file = True,
            doc = "The requirement (requirement_lock.txt) input file which holds deps",
        ),
        "_tool": attr.label(
            default = Label("//tools/dash/formatters:dash_format_converter"),
            executable = True,
            cfg = "exec",
            doc = "",
        ),
    },
)
