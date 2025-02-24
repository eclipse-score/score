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

from score_metamodel import (
    CheckLogger,
    local_check,
)


@local_check
def id_contains_feature(app: Sphinx, need: NeedsInfoType, log: CheckLogger):
    """
    The ID is expected to be in the format '<Req Type>__<feature>__<Title>'.
    Most of this is ensured via regex in the metamodel.
    However the feature part is checked here.
    """

    parts = need["id"].split("__")

    if len(parts) != 3 or need["id"].startswith("stkh_req__"):
        # No warning needed here, as this is already checked in the metamodel.
        return

    # Get the part of the string after the first two underscores: the path
    feature = parts[1]

    docname = os.path.dirname(need["docname"])
    if feature not in docname:
        log.warning_for_option(
            need, "id", f"Feature '{feature}' not in path '{docname}'."
        )
