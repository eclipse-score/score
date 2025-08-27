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

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "S-CORE"
project_url = "https://eclipse-score.github.io/score"
project_prefix = "S-CORE_"
author = "S-CORE"
release = "0.1"

version = release
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinx_needs",
    "sphinxcontrib.plantuml",
    "score_plantuml",
    "score_metamodel",
    "score_draw_uml_funcs",
    "score_source_code_linker",
    "score_layout",
    "score_header_service",
]

exclude_patterns = [
    # The following entries are not required when building the documentation
    # via 'bazel build //docs:docs', as that command runs in a sandboxed environment.
    # However, when building the documentation via 'sphinx-build' or esbonio,
    # these entries are required to prevent the build from failing.
]

templates_path = ["_templates"]

# Enable numref
numfig = True


# -- sphinx-needs configuration --------------------------------------------
# Setting the needs layouts
needs_template_folder = "_templates"
html_static_path = ["_assets"]
needs_global_options = {"collapse": True}
needs_string_links: dict[str, dict[str, object]] = {
    "source_code_linker": {
        "regex": r"(?P<value>[^,]+)",
        "link_url": "{{value}}",
        "link_name": "Source Code Link",
        "options": ["source_code_link"],
    },
}
# This ensures all needs that are imported show up in the build 'needs.json'
needs_builder_filter = ""
