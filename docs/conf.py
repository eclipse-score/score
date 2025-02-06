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
sys.path.insert(0, ".")

from _tooling.conf_extras import layouts
from sphinx.application import Sphinx

from docs._tooling.sphinx_extensions.sphinx_extensions import checks

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Score"
author = "Score"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath("_tooling/extensions"))
extensions = [
    "sphinx_design",
    "sphinx_needs",
    "sphinxcontrib.plantuml",
    "score_plantuml",
    "score_metamodel",
]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    "**/_template",
    "docs/architecture",
    # The following entries are not required when building the documentation
    # via 'bazel build //docs:docs', as that command runs in a sandboxed environment.
    # However, when building the documentation via 'sphinx-build' or esbonio, these entries
    # are required to prevent the build from failing.
    "bazel-*",
    ".venv_docs",
    "modules/cb2needs",
    "modules/index_bazel.rst",
    "platform_integration_tests",
    "_tooling/sphinx_extensions/test",
]

templates_path = ["_templates"]

# Enable numref
numfig = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"  # "alabaster"
html_static_path = ["_tooling/assets"]
html_css_files = [
    "css/score.css",
    "css/score_needs.css",
    "css/score_design.css",
]

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "eclipse-score",
    "github_repo": "score",
    "github_version": "main",
    "doc_path": "docs",
}

html_theme_options = {
    "navbar_align": "content",
    "header_links_before_dropdown": 5,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/eclipse-score",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#add-an-edit-button
    "use_edit_page_button": True,
    "collapse_navigation": True,
    "logo": {
        "text": "Eclipse SCORE Docs",
    },
    # Enable version switcher
    "switcher": {
        "json_url": f"https://{html_context['github_user']}.github.io/{html_context['github_repo']}/versions.json",  # URL to JSON file, hardcoded for now
        "version_match": release,
    },
    "navbar_end": ["version-switcher", "navbar-icon-links"],
}

# -- sphinx-needs configuration --------------------------------------------

# Setting the needs layouts
needs_layouts = layouts.needs_layouts
needs_global_options = {"collapse": True}
needs_global_options = needs_global_options | layouts.needs_global_options


def setup(app: Sphinx):
    checks.add_warnings(app)
