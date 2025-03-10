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

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from pprint import pprint

import debugpy
from python.runfiles import Runfiles
from sphinx.cmd.build import main as sphinx_main

parser = argparse.ArgumentParser()
parser.add_argument(
    "-dp", "--debug_port", help="port to listen to debugging client", default=5678
)
parser.add_argument("--debug", help="Enable Debugging via debugpy", action="store_true")
args = parser.parse_args()
if args.debug:
    debugpy.listen(("0.0.0.0", args.debug_port))
    print("Waiting for client to connect on port: " + str(args.debug_port))
    debugpy.wait_for_client()
    pass

# sphinx will print relative paths to the current directory.
# Change to the workspace root so that the paths are readable and clickable.

logger = logging.getLogger(__name__)


def get_runfiles_dir() -> Path:
    if r := Runfiles.Create():
        # Runfiles are only available when running in Bazel.
        # bazel build and bazel run are both supported.
        # i.e. `bazel build //docs:docs` and `bazel run //docs:incremental`.
        logger.debug("Using runfiles to determine plantuml path.")

        runfiles_dir = Path(r.EnvVars()["RUNFILES_DIR"])

        if not runfiles_dir.exists():
            sys.exit(
                f"Could not find runfiles at {runfiles_dir}. Have a look at "
                "README.md for instructions on how to build docs."
            )

    else:
        # The only way to land here is when running from within the virtual
        # environment created by the `docs:ide_support` rule in the BUILD file.
        # i.e. esbonio or manual sphinx-build execution within the virtual
        # environment.
        # We'll still use the plantuml binary from the bazel build.
        # But we need to find it first.
        logger.debug("Running outside bazel.")

        git_root = Path(__file__).resolve().parents[3]
        assert (git_root / ".git").exists(), (
            f"Could not find git root. Assumed path: {git_root}"
        )

        runfiles_dir = git_root / "bazel-bin" / "docs" / "ide_support.runfiles"
        if not runfiles_dir.exists():
            sys.exit(
                f"Could not find ide_support.runfiles at {runfiles_dir}. "
                "Have a look at README.md for instructions on how to build docs."
            )

    return runfiles_dir


# Initialize with a default value
source_code_linker_file = ""


def get_env(name):
    val = os.environ.get(name, None)
    print(f"Env: {name} = {val}")
    if val is None:
        raise ValueError(f"Environment variable {name} is not set")
    return val


# e.g. /absolute_path/bazel-out/k8-fastbuild/bin/docs2/incremental.runfiles/
runfiles_dir = get_runfiles_dir()
print(f"{runfiles_dir=}")
# runfiles_dir points to a cache directory which has a new hash every time.
# Use the relative path that is available from workspace root.
relative_path = Path("bazel-out") / str(runfiles_dir).split('/bazel-out/', 1)[-1]
print(f"{relative_path=}") # TODO

workspace = os.getenv("BUILD_WORKSPACE_DIRECTORY")
if workspace:
    os.chdir(workspace)

# SOURCE_CODE_LINKER = //docs2:all_module_source_files
filename = get_env("SOURCE_CODE_LINKER").split(":")[-1] + ".txt"
source_code_linker_file = str(relative_path.parent) + "/" + filename

# Asset_dir is interpreted by sphinx. Paths are relative conf.py (conf_dir)

assets_dir_prefix = str(Path("..") / relative_path) + "/" + "_main/docs"

print(f"{source_code_linker_file=}") # TODO
print(f"{assets_dir_prefix=}")

# TODO
# if not source_code_linker_file.exists():
#     raise FileNotFoundError(
#         f"Source code linker file not found: {source_code_linker_file}"
#     )
# if not assets_dir_prefix.exists():
#     raise FileNotFoundError(f"Assets directory not found: {assets_dir_prefix}")

arguments = [
    get_env("SOURCE_DIRECTORY"),
    get_env("BUILD_DIRECTORY"),
    "-W",  # treat warning as errors
    "--keep-going",  # do not abort after one error
    "-T",  # show details in case of errors in extensions
    "--jobs",
    "auto",
    "--conf-dir",
    get_env("CONF_DIRECTORY"),
    f"--define=source_code_linker_file={source_code_linker_file}",
    f"--define=html_static_path={assets_dir_prefix}/_assets,{assets_dir_prefix}/_tooling/assets",
]

pprint(arguments)

sphinx_main(arguments)
