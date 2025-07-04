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

load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@score_docs_as_code//:docs.bzl", "docs")
load("@trlc//:trlc.bzl", "trlc_requirements", "trlc_requirements_test", "trlc_specification")
load("@score_platform//tools/trlc_renderer:trlc_renderer.bzl", "trlc_renderer")

trlc_renderer(
    name = "requirements",
    reqs = [
        "//docs/features/communication/docs/requirements:feat_req_communication",
        "//docs/requirements/stakeholder:stkh_reqs",
    ],
)

# Creates all documentation targets:
# - `docs:incremental` for building docs incrementally at runtime
# - `docs:live_preview` for live preview in the browser without an IDE
# - `docs:ide_support` for creating python virtualenv for IDE support
# - `docs:docs` for building documentation at build-time

trlc_specification(
    name = "mapping_metamodel",
    srcs = ["mapping_model.rsl"],
    visibility = ["//visibility:public"],
)

trlc_specification(
    name = "requirements_metamodel",
    srcs = ["requirements_model.rsl"],
    visibility = ["//visibility:public"],
)

trlc_specification(
    name = "architecture_metamodel",
    srcs = ["architecture_model.rsl"],
    visibility = ["//visibility:public"],
)

trlc_specification(
    name = "score_types",
    srcs = ["score_types.rsl"],
    visibility = ["//visibility:public"],
)

trlc_specification(
    name = "modules",
    srcs = ["modules.rsl"],
    visibility = ["//visibility:public"],
)

test_suite(
    name = "requirements_test",
    tests = [
        "//docs/features/communication/docs/requirements:feat_req_communication_test",
    ],
)

docs(
    conf_dir = "docs",
    docs_targets = [
        {
            "suffix": "latest",  # latest main branch documentation build
            "external_needs_info": [
                {
                    "base_url": "https://eclipse-score.github.io/process_description/main",
                    "json_url": "https://eclipse-score.github.io/process_description/main/needs.json",
                    "id_prefix": "process_",
                },
            ],
        },
        {
            "suffix": "release",  # latest main branch documentation build
            "target": ["@score_process//process:docs_needs_latest"],
            "external_needs_info": [
                {
                    "base_url": "https://eclipse-score.github.io/process_description/main",
                    "json_path": "/score_process~/process/docs_needs_latest/_build/needs/needs.json",
                    "id_prefix": "process_",
                },
            ],
        },
    ],
    source_dir = "docs",
    source_files_to_scan_for_needs_links = [],
)
