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

# sys.path extension for local files is needed, because the conf.py file is not
# executed, but imported by Sphinx
# sys.path.insert(0, "../docs") # TODO

# -- Project information -----------------------------------------------------

project = "Score Module Example (docs2)"
release = "0.1"

# -- General configuration ---------------------------------------------------

sys.path.insert(0, os.path.abspath("../docs_tooling/extensions")) # TODO
extensions = [
    "sphinx_design", # -> TODO: can we hide this in score_layout?
    "sphinx_needs", # -> TODO: can we hide this in score_metamodel?
    "sphinxcontrib.plantuml", # -> TODO: can we hide this in score_plantuml?
    "score_plantuml", # -> TODO: make this a generic bazel_plantuml?
    "score_metamodel",
    "score_draw_uml_funcs",
    "score_source_code_linker",
    "score_layout",
]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    "**/_template",
    # The following entries are not required when building the documentation
    # via 'bazel build //docs:docs', as that command runs in a sandboxed environment.
    # However, when building the documentation via 'sphinx-build' or esbonio,
    # these entries are required to prevent the build from failing.
    # TODO: can we add this via an extension?
    "bazel-*",
    ".venv_docs",
]

# -- sphinx-needs configuration --------------------------------------------
# Setting the needs layouts
needs_global_options = {"collapse": True}
needs_string_links = {
    "source_code_linker": {
        "regex": r"(?P<value>[^,]+)",
        "link_url": "{{value}}",
        "link_name": "Source Code Link",
        "options": ["source_code_link"],
    },
}

# TODO: external needs
