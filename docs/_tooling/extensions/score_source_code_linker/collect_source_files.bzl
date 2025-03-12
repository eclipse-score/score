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
- `SourceCodeLinksInfo`: A provider encapsulating parsed source code links. (public)
- `parse_source_files_for_needs_links`: A function to set up the parsing rule. (public)

Internal implementations:
- `_collect_source_files_aspect`: An aspect to aggregate source files across dependencies.
- `_collect_and_parse_source_files`: A rule to collect and parse source files.
"""

load("@aspect_rules_py//py:defs.bzl", "py_binary")

# -----------------------------------------------------------------------------
# Providers
# -----------------------------------------------------------------------------

SourceCodeLinksInfo = provider(
    doc = "Provider containing a JSON file with source code links.",
    fields = {
        "file": "Path to JSON file containing source code links.",
    },
)

# -----------------------------------------------------------------------------
# Aspect to Collect Source Files (Internal)
# -----------------------------------------------------------------------------

def _extract_source_files(ctx, attr_name):
    """Extracts source files from a given attribute if it exists."""
    return [
        f
        for src in getattr(ctx.rule.attr, attr_name, [])
        for f in src.files.to_list()
        if not f.path.startswith("external")
    ]

def _collect_source_files_aspect_impl(target, ctx):
    """Aspect implementation to collect source files from rules and dependencies."""
    source_files = _extract_source_files(ctx, "srcs") + _extract_source_files(ctx, "hdrs")
    transitive_files = [
        dep[SourceCodeLinksInfo].file
        for dep in getattr(ctx.rule.attr, "deps", [])
        if SourceCodeLinksInfo in dep
    ]
    return [
        SourceCodeLinksInfo(
            file = depset(source_files, transitive = transitive_files),
        ),
    ]

_collect_source_files_aspect = aspect(
    implementation = _collect_source_files_aspect_impl,
    attr_aspects = ["deps"],
    doc = "Aspect that collects source files from a rule and its dependencies. (Internal)",
)

# -----------------------------------------------------------------------------
# Rule to Collect and Parse Source Files (Internal)
# -----------------------------------------------------------------------------

def _collect_and_parse_source_files_impl(ctx):
    """Implementation of a rule that collects and parses source files."""
    sources_file = ctx.actions.declare_file("%s_sources.txt" % ctx.label.name)

    all_files = depset(
        transitive = [dep[SourceCodeLinksInfo].file for dep in getattr(ctx.attr, "deps", []) if SourceCodeLinksInfo in dep],
    ).to_list()

    ctx.actions.write(sources_file, "\n".join([f.path for f in all_files]))
    parsed_sources_json_file = ctx.actions.declare_file("%s.json" % ctx.label.name)

    args = ctx.actions.args()
    args.add(sources_file)
    args.add("--output", parsed_sources_json_file)

    ctx.actions.run(
        arguments = [args],
        executable = ctx.executable.source_files_parser,
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

_collect_and_parse_source_files = rule(
    implementation = _collect_and_parse_source_files_impl,
    attrs = {
        "deps": attr.label_list(
            aspects = [_collect_source_files_aspect],
            allow_files = True,
            doc = "Dependencies and files to scan for links to documentation elements.",
        ),
        "source_files_parser": attr.label(
            executable = True,
            cfg = "exec",
        ),
    },
    doc = "Rule that collects and parses source files for linking documentation. (Internal)",
)

# -----------------------------------------------------------------------------
# Entry Point for Parsing Source Files (Public)
# -----------------------------------------------------------------------------

def parse_source_files_for_needs_links(
        srcs,
        name = "collected_files_for_score_source_code_linker"):
    """Sets up parsing of source files for linking to documentation.

    args:
        srcs: List of source files and dependencies (labels) to parse.
        name: Name of the rule to create."""

    py_binary(
        name = "_source_files_parser",
        srcs = ["//docs:_tooling/extensions/score_source_code_linker/parse_source_files.py"],
    )

    _collect_and_parse_source_files(
        name = name,
        # TODO: shall we call this `srcs` or `deps`?
        # As it accepts both!
        deps = srcs,
        source_files_parser = Label(":_source_files_parser"),
    )

    return Label("@//" + native.package_name() + ":" + name)

# -----------------------------------------------------------------------------
# Backwards compatibility
# -----------------------------------------------------------------------------
# This should be removed once all references have been updated.
def collect_source_files_for_score_source_code_linker(deps, name):
    print("DEPRECATED: Use `parse_source_files_for_needs_links` instead.")
    parse_source_files_for_needs_links(srcs = deps, name = name)
