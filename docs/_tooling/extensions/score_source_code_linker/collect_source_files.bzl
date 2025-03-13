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
"""
Bazel rules and aspects for linking source code to documentation.

This module provides:
- `SourceCodeLinksInfo`: A provider encapsulating parsed source code links.
- `parse_source_files_for_needs_links`: A function to set up the parsing rule.
"""

# -----------------------------------------------------------------------------
# Aspect to Collect Source Files (Internal)
# -----------------------------------------------------------------------------

_CollectedFilesInfo = provider(
    doc = "Internal provider for collecting all source files.",
    fields = {
        "files": "depset of source files",
    },
)

def _extract_files_from_attr(ctx, attr_name):
    """Extracts source files from a given attribute if it exists."""
    return [
        f
        for src in getattr(ctx.rule.attr, attr_name, [])
        for f in src.files.to_list()
        if not f.path.startswith("external")
    ]

def _extract_source_files(ctx):
    # type: (ctx) -> list[File]
    """Extracts source files from the context's attributes."""
    srcs = _extract_files_from_attr(ctx, "srcs")
    hdrs = _extract_files_from_attr(ctx, "hdrs")

    return srcs + hdrs

def _get_transitive_deps(attr, attr_name):
    # type: (struct) -> list[Depset]
    """Extracts previously collected transitive dependencies."""
    return [
        dep[_CollectedFilesInfo].files
        for dep in getattr(attr, attr_name, [])
        if _CollectedFilesInfo in dep
    ]

def _collect_source_files_aspect_impl(_target, ctx):
    """Aspect implementation to collect source files from rules and dependencies."""

    return [
        _CollectedFilesInfo(
            files = depset(
                _extract_source_files(ctx),
                # Follow deps to collect source files from dependencies.
                transitive = _get_transitive_deps(ctx.rule.attr, "deps"),
            ),
        ),
    ]

_collect_source_files_aspect = aspect(
    implementation = _collect_source_files_aspect_impl,
    # Follow deps to collect source files from dependencies.
    attr_aspects = ["deps"],
    doc = "Aspect that collects source files from a rule and its dependencies. (Internal)",
)

# -----------------------------------------------------------------------------
# Rule to Collect and Parse Source Files
# -----------------------------------------------------------------------------

SourceCodeLinksInfo = provider(
    doc = "Provider containing a JSON file with source code links.",
    fields = {
        "file": "Path to JSON file containing source code links.",
    },
)

def _collect_and_parse_source_files_impl(ctx):
    """Implementation of a rule that collects and parses source files."""
    sources_file = ctx.actions.declare_file("%s_sources.txt" % ctx.label.name)

    all_files = depset(
        # Collect source files from the current rule.
        # The rule has an "srcs" attribute.
        transitive = _get_transitive_deps(ctx.attr, "srcs_and_deps"),
    ).to_list()

    ctx.actions.write(sources_file, "\n".join([f.path for f in all_files]))
    parsed_sources_json_file = ctx.actions.declare_file("%s.json" % ctx.label.name)

    args = ctx.actions.args()
    args.add(sources_file)
    args.add("--output", parsed_sources_json_file)

    ctx.actions.run(
        arguments = [args],
        executable = ctx.executable._source_files_parser,
        inputs = [sources_file] + all_files,
        outputs = [parsed_sources_json_file],
    )

    return [
        DefaultInfo(
            files = depset([parsed_sources_json_file]),
            runfiles = ctx.runfiles([parsed_sources_json_file]),
        ),
        SourceCodeLinksInfo(
            file = parsed_sources_json_file,
        ),
    ]

parse_source_files_for_needs_links = rule(
    implementation = _collect_and_parse_source_files_impl,
    attrs = {
        "srcs_and_deps": attr.label_list(
            aspects = [_collect_source_files_aspect],
            allow_files = True,
            doc = "Dependencies and files to scan for links to documentation elements.",
        ),
        "_source_files_parser": attr.label(
            # TODO: rename to source_files_parser in next PR
            default = Label("//docs:parsed_source_files_for_source_code_linker"),
            executable = True,
            cfg = "exec",
        ),
    },
    provides = [
        DefaultInfo,
        SourceCodeLinksInfo,
    ],
    doc = "Rule that collects and parses source files for linking documentation. (Internal)",
)

# -----------------------------------------------------------------------------
# Backwards compatibility
# -----------------------------------------------------------------------------
# This should be removed once all references have been updated.
def collect_source_files_for_score_source_code_linker(deps, name):
    print("DEPRECATED: Use `parse_source_files_for_needs_links` instead.")
    parse_source_files_for_needs_links(srcs_and_deps = deps, name = name)
