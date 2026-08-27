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

# Serve files from docs/_assets and load our own CSS overrides last so they win
# over the styles shipped by the score_docs_as_code bundle.
html_static_path = ["_assets"]
html_css_files = [
    "css/custom.css",
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

# docs/features/baselibs/requirements has its own BUILD file (needed for the
# feature_requirements()/TRLC export consumed by baselibs), so the root
# docs() glob no longer picks it up and it must be re-attached via a
# docs_bundle mount (see //BUILD). Because that bundle's mount_at path
# already lives inside this project's own "docs" tree, sphinx-mounts also
# finds it there directly and skips its own (redundant) mount, only warning
# about the harmless duplicate.
suppress_warnings = ["mounts.docname_conflict"]

# bitmanipulation.rst holds the feat_req__baselibs__bitmanipulation directive
# extracted out of features/baselibs/requirements/index.rst, which
# `.. include::`s it back in (so its lone requirement remains part of the
# rendered baselibs feature requirements page and the index.rst toctree,
# while also being available to Bazel as its own standalone RST source for a
# narrower TRLC/feature_requirements() target - see that directory's BUILD
# file). Sphinx must not additionally treat it as its own standalone
# document, or the `feat_req` need defined inside it registers twice
# (needs.duplicate_id) and the file is flagged as an orphan
# (toc.not_included).
exclude_patterns = [
    "features/baselibs/requirements/bitmanipulation.rst",
]
