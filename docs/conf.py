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

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path
from pprint import pprint

from sphinx_needs import logging

# TODO: if we provide the extensions as py_library, we can remove this...
# Originally the intention was better LSP support. But since we do not "import"
# the extensions, but only use them in the extensions list, this is not needed
# anymore.
runfiles = os.getenv("RUNFILES_DIR")
if not runfiles:
    git_root = Path(__file__).resolve()
    while not (git_root / ".git").exists():
        git_root = git_root.parent
        if git_root == Path("/"):
            sys.exit("Could not find git root.")

    runfiles_dir = git_root / "bazel-bin" / "docs" / "ide_support.runfiles"
    if not runfiles_dir.exists():
        sys.exit(
            f"Could not find ide_support.runfiles at {runfiles_dir}. "
            "Have a look at README.md for instructions on how to build docs."
        )
    runfiles = str(runfiles_dir)

sys.path.insert(0, os.path.join(runfiles, "_main/docs/_tooling/extensions"))

logger = logging.get_logger(__name__)
logger.warning(f"runfiles: {runfiles}")
logger.warning(f"sys.path: {sys.path}")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Score"
author = "Score"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# TODO: consider a score_everything extension?
extensions = [
    "sphinx_design",
    "sphinx_needs",
    "sphinxcontrib.plantuml",
    "score_plantuml", # TODO: implicitly load sphinxcontrib.plantuml
    "score_metamodel",
    "score_draw_uml_funcs",
    "score_layout", # TODO: implicitly load sphinx_design
    "score_source_code_linker",
]

# TODO: move these to some score extension?!
exclude_patterns = [
    # The following entries are not required when building the documentation
    # via 'bazel build //docs:docs', as that command runs in a sandboxed environment.
    # However, when building the documentation via 'sphinx-build' or esbonio,
    # these entries are required to prevent the build from failing.
    "bazel-*",
    ".venv_docs",
]

templates_path = ["_templates"]

# Enable numref
numfig = True


# -- sphinx-needs configuration --------------------------------------------
# Setting the needs layouts
# TODO: move to score_layout extension?!
needs_global_options = {"collapse": True}

# TODO: move to source_code_linker extension?!
needs_string_links = {
    "source_code_linker": {
        "regex": r"(?P<value>[^,]+)",
        "link_url": "{{value}}",
        "link_name": "Source Code Link",
        "options": ["source_code_link"],
    },
}
