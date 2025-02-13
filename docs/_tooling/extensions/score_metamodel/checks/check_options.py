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
import re

from sphinx_needs.data import NeedsInfoType

from score_metamodel import (
    CheckLogger,
    local_check,
)
from score_metamodel.metamodel import (
    needs_types as production_needs_types,
)


def get_need_type(needs_types: list[NeedsInfoType], directive: str):
    for need_type in needs_types:
        assert isinstance(need_type, dict), need_type
        if need_type["directive"] == directive:
            return need_type
    raise ValueError(f"Need type {directive} not found in needs_types")


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__options
@local_check
def check_options(
    need: NeedsInfoType,
    log: CheckLogger,
    needs_types=production_needs_types,
):
    """
    Checking if all described and wanted attributes are present and their values follow the described pattern.
    """

    try:
        need_options = get_need_type(needs_types, need["type"])
    except ValueError:
        msg = f"with type `{need['type']}`: no type info defined for semantic check."
        log.warning_for_option(need, log, msg)
        return

    required_options: list[tuple[str, str]] = need_options.get("req_opt", [])
    optional_options: list[tuple[str, str]] = need_options.get("opt_opt", [])

    if len(required_options) == 0:
        msg = "no type info defined for semantic check."
        log.warning_for_option((need, "type", msg))

    for option, pattern in required_options:
        values = need.get(option, None)

        if values is None or values in [[], ""]:
            msg = f"is missing required option: `{option}`."
            log.warning_for_need(need, msg)
            continue

        # Normalize values, which can be a list or a string, to a list of strings
        if type(values) is not list:
            values = [values]

        for value in values:
            assert type(value) is str
            regex = re.compile(pattern)

            if not regex.match(value):
                msg = f"does not follow pattern `{pattern}`."
                log.warning_for_option(need, option, msg)

    if optional_options:
        for option, pattern in optional_options:
            values = need.get(option, None)

            if values is None or values in [[], ""]:  # Skip if no values
                continue

            # Normalize values, which can be a list or a string, to a list of strings
            if not isinstance(values, list):
                values = [values]

            for value in values:
                assert isinstance(value, str)
                regex = re.compile(pattern)  # Compile regex only if a value exists

                if not regex.match(value):
                    msg = f"does not follow pattern `{pattern}`."
                    log.warning_for_option(need, option, msg)


@local_check
def check_extra_options(
    need: NeedsInfoType,
    log: CheckLogger,
    needs_types=production_needs_types,
):
    """
    This function checks if the user specified attributes in the need which are not defined for this element in the metamodel or by default system attributes.
    """

    try:
        need_options = get_need_type(needs_types, need["type"])
    except ValueError:
        msg = f"with type `{need['type']}`: no type info defined for semantic check."
        log.warning_for_option(need, log, msg)
        return

    required_options: list[tuple[str, str]] = need_options.get("req_opt", [])
    optional_options: list[tuple[str, str]] = need_options.get("opt_opt", [])

    allowed_options = (
        [key for key, _ in required_options]
        + [key for key, _ in optional_options]
        # list of default system attributes to ignore
        + [
            "target_id",
            "docname",
            "lineno",
            "type",
            "lineno_content",
            "doctype",
            "content",
            "type_name",
            "type_color",
            "type_style",
            "title",
            "full_title",
            "layout",
            "id_parent",
            "id_complete",
            "external_css",
            "sections",
            "section_name",
            "type_prefix",
            "constraints_passed",
            "collapse",
            "hide",
            "delete",
            "jinja_content",
            "is_part",
            "is_need",
            "is_external",
            "is_modified",
            "modifications",
            "has_dead_links",
            "has_forbidden_dead_links",
        ]
    )

    extra_options = [
        option
        for option in list(need.keys())
        if option not in allowed_options and need[option] not in [None, {}, "", []]
    ]

    if extra_options:
        extra_options_str = ", ".join(f"`{option}`" for option in extra_options)
        msg = f"has these extra options: {extra_options_str}."
        log.warning_for_need(need, msg)
