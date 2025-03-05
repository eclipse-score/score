# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
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
from sphinx.application import Sphinx


def return_html_theme_options(app: Sphinx) -> dict:
    return {
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
        # Enable version switcher
        "switcher": {
            "json_url": (
                f"https://{html_context['github_user']}.github.io/"
                f"{html_context['github_repo']}/versions.json"
            ),  # URL to JSON file, hardcoded for now
            "version_match": app.config.release,
        },
        "navbar_end": ["theme-switcher", "navbar-icon-links", "version-switcher"],
        "logo": {
            "text": "Eclipse S-CORE",
        },
    }


html_theme = "pydata_sphinx_theme"  # "alabaster"
html_static_path = ["_tooling/assets", "_assets"]
html_css_files = [
    "css/score.css",
    "css/score_needs.css",
    "css/score_design.css",
]

# html_logo = "_assets/S-CORE_Logo_white.svg"


html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "eclipse-score",
    "github_repo": "score",
    "github_version": "main",
    "doc_path": "docs",
}
