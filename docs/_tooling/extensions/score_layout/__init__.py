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
from typing import Any

from sphinx.application import Sphinx

from score_layout import html_options, sphinx_options


def setup(app: Sphinx) -> dict[str, str | bool]:
    app.connect("config-inited", update_config)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def update_config(app: Sphinx, _config: Any):
    app.config.needs_layouts = sphinx_options.needs_layouts
    app.config.needs_global_options = sphinx_options.needs_global_options
    app.config.html_theme = html_options.html_theme
    app.config.html_context = html_options.html_context
    app.config.html_theme_options = html_options.return_html_theme_options(app)

    app.add_css_file("css/score.css", priority=500)
    app.add_css_file("css/score_needs.css", priority=500)
    app.add_css_file("css/score_design.css", priority=500)
