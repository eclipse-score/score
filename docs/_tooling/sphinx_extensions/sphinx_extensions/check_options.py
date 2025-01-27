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

    required_options = get_need_type(needs_types, need["type"]).get("req_opt", None)

    if required_options is None:
        msg = f'Need: {need["id"]} with type {need["type"]}: no type info defined for semantic check.'
        log_custom_warning(need, log, msg)
        return True

    result = False
    for option, pattern in required_options:
        regex = re.compile(pattern)
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

            if not regex.match(value):
                msg = f'Need: {need["id"]} option `{option}` with value `{value}` does not follow pattern `{pattern}`.'
                log_custom_warning(need, log, msg)
                result = True

    return result
