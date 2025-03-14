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

load("//docs:_tooling/docs.bzl", "docs")


# Creates all documentation targets:
# - `:docs` for building documentation at build-time
# - `:incremental` for building docs incrementally at runtime
# - `:live_preview` for live preview in the browser without an IDE
# - `:ide_support` for creating python virtualenv for IDE support
filegroup(
    name = "files",
    srcs = ["test.py"],
)
docs(
    build_dir_for_incremental = "_build2",
    conf_dir = "docs2",
    source_dir = "docs2",
    source_files_to_scan_for_needs_links = [":files"],
)
