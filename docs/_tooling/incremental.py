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
from sphinx.cmd.build import main as sphinx_main
from python.runfiles import runfiles

r = runfiles.Create()
workspace = os.getenv("BUILD_WORKSPACE_DIRECTORY")
if workspace:
    os.chdir(workspace)

# Look for the file in runfiles
flags_file = r.Rlocation("_main/docs/feature_flags.txt")

if not os.path.exists(flags_file):
    raise RuntimeError("Could not find feature_flags.txt")

sphinx_main(
    [
        "docs",  # src dir
        "_build",  # out dir
        "-T",  # show details in case of errors in extensions
        "--jobs",
        "auto",
        "--conf-dir",
        "docs",
        "-D",
        f"filter_tags_file_path={flags_file}",
    ]
)
