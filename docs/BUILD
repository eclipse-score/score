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

# Multiple approaches are available to build the same documentation output:
#
# 1. **Esbonio via IDE support (`ide_support` target)**:
#    - Listed first as it offers the least flexibility in implementation.
#    - Designed for live previews and quick iterations when editing documentation.
#    - Integrates with IDEs like VS Code but requires the Esbonio extension.
#    - Requires a virtual environment with consistent dependencies (see 2).
#
# 2. **Directly running Sphinx in the virtual environment**:
#    - As mentioned above, a virtual environment is required for running esbonio.
#    - Therefore, the same environment can be used to run Sphinx directly.
#    - Option 1: Run Sphinx manually via `.venv_docs/bin/python -m sphinx docs _build --jobs auto`.
#    - Option 2: Use the `incremental` target, which simplifies this process.
#    - Usable in CI pipelines to validate the virtual environment used by Esbonio.
#    - Ideal for quickly generating documentation during development.
#
# 3. **Bazel-based build (`docs` target)**:
#    - Runs the documentation build in a Bazel sandbox, ensuring clean, isolated builds.
#    - Less convenient for frequent local edits but ensures build reproducibility.
#
# **Consistency**:
# When modifying Sphinx extensions or configuration, ensure all three methods
# (Esbonio, incremental, and Bazel) work as expected to avoid discrepancies.
#
# For user-facing documentation, refer to `/README.md`.

load("@aspect_rules_py//py:defs.bzl", "py_venv")
load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("@rules_pkg//pkg:mappings.bzl", "pkg_files")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@rules_python//python:defs.bzl", "py_library")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")

# all_requirements include esbonio which we don't need most of the time.
# Hint: the names are e.g. "@@rules_python~~pip~pip_sphinx//esbonio:pkg"
sphinx_requirements = [name for name in all_requirements if not "esbonio" in name] + [":extensions"]

sphinx_docs(
    name = "docs",
    srcs = glob([
        "**/*.png",
        "**/*.svg",
        "**/*.rst",
        "**/*.html",
        "**/*.css",
    ]),
    config = ":conf.py",
    extra_opts = [
        "-W",
        "--keep-going",
    ],
    formats = [
        "html",
    ],
    sphinx = ":sphinx_build",
    tags = [
        "manual",
    ],
)

sphinx_build_binary(
    name = "sphinx_build",
    deps = sphinx_requirements,
)

py_library(
    name = "extensions",
    srcs = [
        "_extensions/layouts.py",
        "_extensions/metamodel.py",
    ],
    imports = ["."],
)

# In order to update the requirements, change the `requirements.txt` file and run:
# `bazel run //docs:requirements`.
# This will update the `requirements_lock.txt` file.
# To upgrade all dependencies to their latest versions, run:
# `bazel run //docs:requirements -- --upgrade`.
compile_pip_requirements(
    name = "requirements",
    src = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
    tags = [
        "manual",
    ],
)

filegroup(
    name = "html",
    srcs = [":docs"],
    output_group = "html",
)

pkg_files(
    name = "html_files",
    srcs = [":html"],
    renames = {"html": ""},
)

pkg_tar(
    name = "github-pages",
    srcs = [":html_files"],
)

# Run-time build of documentation, incl. incremental build support.
py_binary(
    name = "incremental",
    srcs = ["incremental.py"],
    deps = sphinx_requirements,
)

# Virtual python environment for working on the documentation (esbonio).
# incl. python support when working on conf.py and sphinx extensions.
py_venv(
    name = "ide_support",
    venv_name = ".venv_docs",
    # Until release of esbonio 1.x, we need to install it ourselves so the VS Code extension can find it.
    deps = sphinx_requirements + [requirement("esbonio")],
)
