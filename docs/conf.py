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

# from process.process_model_configuration import *
# from _extensions import metamodel, layouts

class metamodel:
    needs_types = [
    # Requirements
    dict(
        directive="stkh_req",
        title="Stakeholder requirements",
        prefix="STKH_REQ__",
        color="#BFD8D2",
        style="node",
    ),
    dict(
        directive="tool_req",
        title="Tool Requirements",
        prefix="TOOL_REQ__",
        color="#BFD8D2",
        style="node",
    ),
    ]

    # Define extra options for needs object
    needs_extra_options = [
        "security",
        "safety",
        "level",
        "rationale",
        "mitigated_by",
        "reqtype",
        "codelink",
        "testlink",
        "reqcovered",
        "testcovered",
    ]

    needs_extra_links = [
        # TODO: Refer process document for the usage of links
        {
            "option": "satisfies",
            "incoming": "is satisfied by",
            "outgoing": "satisfies",
            "style_start": "-up",
            "style_end": "->",
        },
        {"option": "implements", "incoming": "implements by", "outgoing": "implements"},
    ]

class layouts:
    needs_layouts = {
    "score": {
        "grid": "complex",
        "layout": {
            "head_left": [
                '<<meta("title")>>',
            ],
            "head": [
                'status: **<<meta("status")>>**',
                'security: **<<meta("security")>>**',
                'safety: **<<meta("safety")>>**',
            ],
            "head_right": [
                '<<collapse_button("meta",collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>> '
            ],
            "meta_left": [
                '<<meta_all(no_links=True, exclude=["layout","style"])>>',
                "<<meta_links_all()>>",
            ],
            "meta_right": [],
            "footer_left": ["<<meta_id()>>"],
            "footer": ['<<meta("type_name")>>'],
            "footer_right": [],
        },
    },
    }

    needs_global_options = {"layout": "score"}



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Score"
author = "Score"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinx_needs",
]

templates_path = ["_templates"]

suppress_warnings = ["config.cache"]

# Enable numref
numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"  #  "alabaster"
html_static_path = ["_assets"]
html_css_files = [
    "css/score.css",
    "css/score_needs.css",
    "css/score_design.css",
]

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
    "use_edit_page_button": True,  # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#add-an-edit-button
    "collapse_navigation": True,
    "logo": {
        "text": "Eclipse SCORE Docs",
    },
}

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "eclipse-score",
    "github_repo": "score",
    "github_version": "main",
    "doc_path": "docs",
}

# -- sphinx-needs configuration --------------------------------------------

needs_types = metamodel.needs_types
needs_extra_options = metamodel.needs_extra_options
needs_extra_links = metamodel.needs_extra_links

# Setting the needs layouts
needs_layouts = layouts.needs_layouts
needs_global_options = {"collapse": True}
needs_global_options = needs_global_options | layouts.needs_global_options


# sphinx_needs configuration
needs_id_required = True
needs_id_regex = "^[A-Za-z0-9_-]{6,}"
