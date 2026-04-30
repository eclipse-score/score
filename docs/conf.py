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

project = "S-CORE"
project_url = "https://eclipse-score.github.io/score"
version = "0.1"

extensions = [
    # TODO: remove plantuml here once
    # https://github.com/useblocks/sphinx-needs/pull/1508 is merged and docs-as-code
    # is updated with new sphinx-needs version
    "sphinxcontrib.plantuml",
    "score_sphinx_bundle",
]

# Hide both sidebars on the handbook landing page (left: html_sidebars, right: secondary_sidebar_items)
html_sidebars = {
    "handbook/index": [],
}

html_theme_options = {
    "secondary_sidebar_items": {
        "handbook/index": [],
        "**": ["page-toc", "edit-this-page", "sourcelink"],
    },
}

# Make _assets available as Sphinx static files root
html_static_path = ["_assets"]


def setup(app):
    # Load handbook card styling after score_layout CSS (priority 500)
    app.add_css_file("css/score_handbook.css", priority=600)
    # Collapsible right-sidebar TOC
    app.add_js_file("js/toc_collapse.js")
