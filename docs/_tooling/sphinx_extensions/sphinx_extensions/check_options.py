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
import re

from sphinx.util.logging import SphinxLoggerAdapter
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.metamodel import (
    needs_types as production_needs_types,
)
from docs._tooling.sphinx_extensions.sphinx_extensions.utils.util import (
    log_custom_warning,
)


def get_need_type(needs_types: list[dict], directive: str):
    for need_type in needs_types:
        assert isinstance(need_type, dict), need_type
        if need_type["directive"] == directive:
            return need_type
    raise ValueError(f"Need type {directive} not found in needs_types")


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__options
def check_options(
    need: NeedsInfoType,
    log: SphinxLoggerAdapter,
    needs_types=production_needs_types,
) -> bool:
    """
    Checking if all described and wanted attributes are present and their values follow the described pattern.
    ---
    Returns 'True' if an option is not present or a value violates its pattern
    """

    need_options = get_need_type(needs_types, need["type"])
    required_options: list[tuple[str, str]] = need_options.get("req_opt", [])
    optional_options: list[tuple[str, str]] = need_options.get("opt_opt", [])

    if required_options is None:
        msg = f'Need: {need["id"]} with type {need["type"]}: no type info defined for semantic check.'
        log_custom_warning(need, log, msg)
        return True

    result = False
    for option, pattern in required_options:
        values = need.get(option, None)

        if values is None or values in [[], ""]:
            msg = f'Need: {need["id"]} is missing required option: `{option}`.'
            log_custom_warning(need, log, msg)
            result = True
            continue

        # Normalize values, which can be a list or a string, to a list of strings
        if type(values) is not list:
            values = [values]

        for value in values:
            assert type(value) is str
            regex = re.compile(pattern)

            if not regex.match(value):
                msg = f'Need: {need["id"]} required option `{option}` with value `{value}` does not follow pattern `{pattern}`.'
                log_custom_warning(need, log, msg)
                result = True

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
                    msg = f'Need: {need["id"]} optional option `{option}` with value `{value}` does not follow pattern `{pattern}`.'
                    log_custom_warning(need, log, msg)
                    result = True

    return result


def check_extra_options(
    need: NeedsInfoType,
    log: SphinxLoggerAdapter,
    needs_types=production_needs_types,
) -> bool:
    """
    This function checks if the user specified attributes in the need which are not defined for this element in the metamodel or by default system attributes.
    ---
    Returns 'True' if one of more extra option exist
    """

    need_options = get_need_type(needs_types, need["type"])
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
        ]
    )

    extra_options = [
        option
        for option in list(need.keys())
        if option not in allowed_options
        and need[option] not in [None, {}, "", []]
        and not option.endswith("_back")
    ]

    if extra_options:
        extra_options_str = ", ".join(f"`{option}`" for option in extra_options)
        msg = f'Need: {need["id"]} have these extra options: {extra_options_str}.'
        log_custom_warning(need, log, msg)
        return True

    return False
