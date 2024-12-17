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

import os
import sys

try:
    from sphinx.cmd.build import main as sphinx_main
except ImportError:
    sys.exit(
        "This script must be run from Bazel via `bazel run //docs:incremental`"
        " (sphinx not installed)."
    )

workspace = os.getenv("BUILD_WORKSPACE_DIRECTORY")
if not workspace:
    sys.exit(
        "This script must be run from Bazel via `bazel run //docs:incremental`"
        " (BUILD_WORKSPACE_DIRECTORY not set)."
    )

# sphinx will print relative paths to the current directory.
# Change to the workspace root so that the paths are readable and clickable.
os.chdir(workspace)
sphinx_main(
    [
        "docs",
        "_build",
        "--jobs",
        "auto",
    ]
)
