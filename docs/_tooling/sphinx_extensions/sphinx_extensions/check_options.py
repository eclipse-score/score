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
from docs._tooling.sphinx_extensions.sphinx_extensions.model import (
    need_type_info as production_need_type_info,
)
from docs._tooling.sphinx_extensions.sphinx_extensions.utils.util import (
    log_custom_warning,
)
from sphinx_needs.data import NeedsInfoType


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__options
def check_options(
    need: NeedsInfoType,
    log: SphinxLoggerAdapter,
    need_type_info=production_need_type_info,
) -> bool:
    """
    Checking if all described and wanted attributes are present and their values follow the described pattern.
    ---
    Returns 'True' if an option is not present or a value violates its pattern
    """

    required_options = need_type_info.get(need["type"], dict()).get("req_opt", None)

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
