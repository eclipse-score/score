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

def _trlc_renderer_impl(ctx):
    rendered_file = ctx.actions.declare_file("{}.rst".format(ctx.attr.name))
    args = ctx.actions.args()
    args.add(ctx.executable._renderer.path)
    args.add("--output", rendered_file.path)


    ctx.actions.run(
        inputs = [ctx.executable._renderer] + ctx.files.reqs,
        outputs = [rendered_file],
        arguments = [args],
        executable = ctx.executable._wrapper,
        tools = [ctx.executable._renderer],
    )

    return [DefaultInfo(files = depset([rendered_file]))]

trlc_renderer = rule(
    implementation = _trlc_renderer_impl,
    attrs = {
        "reqs": attr.label_list(allow_files = True),
        "_renderer": attr.label(
            default = Label("//tools/trlc_renderer"),
            executable = True,
            allow_files = True,
            cfg = "exec",
        ),
        "_wrapper": attr.label(
            default = Label("//tools/trlc_renderer:trlc_wrapper"),
            executable = True,
            allow_files = True,
            cfg = "exec",
        ),
    },
)
