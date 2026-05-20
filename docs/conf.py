# *******************************************************************************
# Copyright (c) 2026 Contributors to the Eclipse Foundation
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

# Hide both sidebars on the users_guide landing page (left: html_sidebars, right: secondary_sidebar_items)
html_sidebars = {
    "users_guide/index": [],
}

html_theme_options = {
    "secondary_sidebar_items": {
        "users_guide/index": [],
        "**": ["page-toc", "edit-this-page", "sourcelink"],
    },
}
