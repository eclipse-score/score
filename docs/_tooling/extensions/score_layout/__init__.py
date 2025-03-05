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
from score_layout import html_options, sphinx_options


def setup(app: Sphinx) -> dict[str, str | bool]:
    app.config.needs_layouts = sphinx_options.needs_layouts
    app.config.needs_global_options = sphinx_options.needs_global_options
    app.config.html_theme = html_options.html_theme
    app.config.html_context = html_options.html_context
    app.config.html_css_files = html_options.html_css_files
    app.config.html_static_path = html_options.html_static_path
    app.config.html_theme_options = html_options.return_html_theme_options(app)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
