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

from docs._tooling.extensions.score_metamodel import (
    CheckLogger,
    NeedsInfoType,
    local_check,
)
from docs._tooling.extensions.score_metamodel.metamodel import (
    needs_types as production_needs_types,
)


@local_check
def check_options(
    need: NeedsInfoType,
    log: CheckLogger,
    needs_types=production_needs_types,
):
    """
    Checking if all described and wanted attributes are present and their values follow the described pattern.
    """

    # Find the dictionary where "directive" matches the need's type
    required_options = next(
        (
            item["req_opt"]
            for item in needs_types
            if isinstance(item, dict) and item.get("directive") == need["type"]
        ),
        None,
    )

    if required_options is None:
        msg = 'no type info defined for semantic check.'
        log.warning_for_option(need, "type", msg)
        return

    for option, pattern in required_options:
        regex = re.compile(pattern)
        values = need.get(option, None)

        # TODO: why not simply "not values"?
        if values is None or values in [[], ""]:
            msg = 'missing required option.'
            log.warning_for_option(need, option, msg)
        else:
            # Normalize values (convert to list if it's a single string)
            if not isinstance(values, list):
                values = [values]

            for value in values:
                assert isinstance(value, str)

                if not regex.match(value):
                    msg = f'does not follow pattern `{pattern}`.'
                    log.warning_for_option(need, option, msg)
