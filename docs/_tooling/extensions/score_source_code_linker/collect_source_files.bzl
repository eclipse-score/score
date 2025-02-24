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
CollectedFilesInfo = provider(
    fields = {
        "files": "depset of source files",
    },
)

def _extract_source_files(rule, attr):
    collected_source_files = []
    if hasattr(rule.attr, attr):
        for src in getattr(rule.attr, attr):
            for f in src.files.to_list():
                if not f.path.startswith("external"):
                    collected_source_files.append(f)
    return collected_source_files

def _collected_source_files_aspect_impl(target, ctx):
    collected_source_files = []
    collected_source_files += _extract_source_files(ctx.rule, "srcs")
    collected_source_files += _extract_source_files(ctx.rule, "hdrs")
    collected_source_files_deps = [dep[CollectedFilesInfo].files for dep in ctx.rule.attr.deps]
    return [CollectedFilesInfo(files = depset(collected_source_files, transitive = collected_source_files_deps))]

collected_source_files_aspect = aspect(
    implementation = _collected_source_files_aspect_impl,
    attr_aspects = ["deps"],
)

def _requirement_links_impl(ctx):
    sources_filename = ctx.label.name
    sources = ctx.actions.declare_file("%s_sources.txt" % sources_filename)

    accumulated = []
    for dep in ctx.attr.deps:
        accumulated.append(dep[CollectedFilesInfo].files)

    all_files = depset(transitive = accumulated).to_list()

    content = ""
    for filename in all_files:
        content += "%s\n" % filename.path

    ctx.actions.write(sources, content)

    out_filename = ctx.label.name
    out = ctx.actions.declare_file("%s.txt" % out_filename)

    args = ctx.actions.args()
    args.add(sources)
    args.add("--output", out)

    ctx.actions.run(
        arguments = [args],
        executable = ctx.executable._tool,
        inputs = [sources] + all_files,
        outputs = [out],
    )

    return [DefaultInfo(files = depset([out]), runfiles = ctx.runfiles([out]))]

collect_source_files_for_score_source_code_linker = rule(
    implementation = _requirement_links_impl,
    attrs = {
        "deps": attr.label_list(
            aspects = [collected_source_files_aspect],
        ),
        "_tool": attr.label(
            default = "//docs:parsed_source_files_for_source_code_linker",
            executable = True,
            cfg = "exec",
        ),
    },
)
