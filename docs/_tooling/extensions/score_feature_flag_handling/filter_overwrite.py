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
from sphinx_needs.views import NeedsView
from sphinx_needs.data import NeedsInfoType, NeedsFilteredBaseType
from sphinx_needs.config import NeedsSphinxConfig
from sphinx_needs.views import NeedsAndPartsListView
from docutils import nodes
from sphinx_needs.debug import measure_time


#                    ╭──────────────────────────────────────────────────────────────────────────────╮
#                    │             Wrapping filter funcs to enable 'hide' to be respected           │
#                    ╰──────────────────────────────────────────────────────────────────────────────╯


def wrap_filter_common():
    """
    Wrapper function to avoid circular imports by importing filter_common at runtime instead of module level.

    This wraps two functions used by sphinx_needs directives 'needtable' etc. in order to ensure that the
    hidden requirements are not showing up in the results.
    """
    from sphinx_needs import filter_common

    orig_common = filter_common.process_filters
    orig_parts = filter_common.filter_needs_parts

    @measure_time("filtering")
    def common_wrapper(
        app: Sphinx,
        needs_view: NeedsView,
        filter_data: NeedsFilteredBaseType,
        origin: str,
        location: nodes.Element,
        include_external: bool = True,
    ):  # Used by needlist, needtable and needflow.
        needs_view = needs_view._copy_filtered(
            i["id"] for i in needs_view.Values() if i["hide"] != True
        )
        return orig_common(
            app, needs_view, filter_data, origin, location, include_external
        )

    @measure_time("filtering")
    def parts_wrapper(
        needs: NeedsAndPartsListView,
        config: NeedsSphinxConfig,
        filter_string: None | str = "",
        current_need: NeedsInfoType | None = None,
        *,
        location: tuple[str, int | None] | nodes.Node | None = None,
        append_warning: str = "",
        strict_eval: bool = False,
    ):  # Used by needpie
        if filter_string is not None and filter_string != "":
            filter_string += " and hide != True"
        else:
            filter_string = "hide != True"
        return orig_parts(
            needs,
            config,
            filter_string,
            current_need,
            location=location,
            append_warning=append_warning,
            strict_eval=strict_eval,
        )

    # Patch the original module
    filter_common.process_filters = common_wrapper
    filter_common.filter_needs_parts = parts_wrapper
