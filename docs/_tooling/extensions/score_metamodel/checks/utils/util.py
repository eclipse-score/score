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
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.log import CheckLogger


def check_option(
    need: NeedsInfoType,
    option: str,
    log: CheckLogger,
    allowed_values: list[str | int | bool] = None,
    allow_empty: bool = False,
    msg: str = "",
):
    """
    Checks if a specified option exists in the given need and validates its value.
    """
    empty_values = [[], "", None]

    # Check if option exists in need
    if option not in need:
        if msg == "":
            msg = f'Need: {need["id"]} is missing required option: `{option}`.'

        log.warning_for_option(need, option, msg)

    if need[option] in empty_values and not allow_empty:
        if msg == "":
            msg = f'Need: {need["id"]} is missing required option: `{option}`.'
        log.warning_for_option(need, option, msg)

    if allowed_values:
        if need[option] not in allowed_values:
            if msg == "":
                msg = f'Need: {need["id"]} has `{option}` option wrongly set. Got: `{need[option]}` wanted one of: `{allowed_values}`\n'

            log.warning_for_option(need, option, msg)
