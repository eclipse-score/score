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
from unittest.mock import MagicMock

import pytest
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.checks.check_options import check_options
from docs._tooling.extensions.score_metamodel.log import CheckLogger
from docs._tooling.extensions.score_metamodel.tests import fake_check_logger, need

NEED_TYPE_INFO = [
    {
        "directive": "tool_req",
        "req_opt": [
            ("some_option", "^some_value__.*$"),
        ],
    }
]

# @pytest.mark.metadata(
#     Description="It should check if directives have required options and required values.",
#     ASIL="ASIL_B",
#     Priority="1",
#     TestType="Requirements-based test",
#     DerivationTechnique="Analysis of requirements",
# )


@pytest.mark.parametrize(
    "need, expected_warning",
    [
        (
            need(type="tool_req", some_option="some_value__001"),
            None
        ),
        (
            need(type="tool_req", some_option="invalid_value"),
            'does not follow pattern'
        ),
        (
            need(type="tool_req"),
            'missing required option.'
        ),
        (
            need(type="unknown_directive"),
            "no type info defined for semantic check"
        ),
        (
            # Currently there is no warning for unknown options
            need(type="tool_req", some_option="some_value__001",
                 unknown_option="value"),
            None
        ),
    ],
)
def test_check_options(need: NeedsInfoType, expected_warning: str | None):
    # Given the required environment
    logger = fake_check_logger()

    # When the check_options function is called with the given need
    check_options(need, logger, NEED_TYPE_INFO)

    # Then expect that the check prints the expected warning
    if expected_warning:
        assert logger.has_warnings
        verify_log_string(logger, expected_warning)
    else:
        assert not logger.has_warnings
