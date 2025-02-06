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

import os
import sys

from sphinx_autobuild.__main__ import main as sphinx_autobuild_main

# sphinx will print relative paths to the current directory.
# Change to the workspace root so that the paths are readable and clickable.
workspace = os.getenv("BUILD_WORKSPACE_DIRECTORY")
if workspace:
    os.chdir(workspace)

sphinx_autobuild_main(
    [
        "docs",  # source directory
        "_build/html",  # output directory
    ]
)
