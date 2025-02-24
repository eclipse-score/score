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
import os

from sphinx.application import Sphinx
from sphinx_needs.data import NeedsInfoType

from score_metamodel import CheckLogger, local_check


# req-Id: TOOL_REQ__toolchain_sphinx_needs_build__requirement_attributes_uid
@local_check
def check_id_format(app: Sphinx, need: NeedsInfoType, log: CheckLogger):
    """
    Checking if the title, directory and feature are included in the requirement id or not.
    ---
    """
    # Split the string by underscores
    parts = need["id"].split("__")

    if need["id"].startswith(("gd_", "wf__", "wp__", "rl__", "tool_req__", "doc__")):
        if len(parts) != 2 and len(parts) != 3:
            msg = "expected to consisting of one of these 2 formats:`<Req Type>__<Abbreviations>` or `<Req Type>__<Abbreviations>__<Architectural Element>`."
            log.warning_for_option(need, "id", msg)
    else:
        if len(parts) != 3:
            msg = "expected to consisting of this format: `<Req Type>__<Abbreviations>__<Architectural Element>`."
            log.warning_for_option(need, "id", msg)


@local_check
def check_id_length(app: Sphinx, need: NeedsInfoType, log: CheckLogger):
    """
    Validates that the requirement ID does not exceed the hard limit of 45 characters.
    While the recommended limit is 30 characters, this check enforces a strict maximum of 45 characters.
    If the ID exceeds 45 characters, a warning is logged specifying the actual length.
    ---
    """
    if len(need["id"]) > 45:
        msg = f"exceeds the maximum allowed length of 45 characters (current length: {len(need['id'])})."
        log.warning_for_option(need, "id", msg)
