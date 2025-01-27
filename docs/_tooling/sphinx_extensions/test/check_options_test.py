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
import sys
from unittest.mock import ANY, MagicMock

import pytest
from sphinx.util.logging import SphinxLoggerAdapter
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.metamodel import (
    needs_types as production_needs_types,
)
from docs._tooling.sphinx_extensions.sphinx_extensions.check_options import (
    check_options,
)


@pytest.mark.metadata(
    Verifies=["TOOL_REQ__toolchain_sphinx_needs_build__options"],
    Description="It should check if directives have required options and required values.",
    ASIL="ASIL_B",
    Priority="1",
    TestType="Requirements-based test",
    DerivationTechnique="Analysis of requirements",
)
class TestCheckOptions:
    NEED_TYPE_INFO = [
        {
            "directive": "tool_req",
            "req_opt": [
                ("some_option", "^some_value__.*$"),
            ],
        },
    ]

    assert type(NEED_TYPE_INFO) == type(production_needs_types)  # noqa: E721
    assert type(NEED_TYPE_INFO[0]) == type(production_needs_types[0])  # noqa: E721

    LOGGER = MagicMock(spec=SphinxLoggerAdapter)
    LOGGER.warning = MagicMock()

    def test_known_directive_with_mandatory_option_and_allowed_value(self):
        # Given a need with a type that is listed in the required options
        #  and mandatory options present
        #  and with correct values
        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            some_option="some_value__001",
            docname=None,
            lineno=None,
        )

        # Expect that the checks pass
        assert check_options(need, self.LOGGER, self.NEED_TYPE_INFO) is False
        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            some_option="some_value__001",
            docname=None,
            lineno=None,
        )

        # Expect that the checks pass
        assert check_options(need, self.LOGGER, self.NEED_TYPE_INFO) is False

    def test_unknown_option_present(self):
        # Given a need with an option that is not listed in the required options
        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            some_option="some_value__001",
            other_option="some_other_value",
            docname=None,
            lineno=None,
        )

        # Expect that the checks pass
        assert check_options(need, self.LOGGER, self.NEED_TYPE_INFO) is False

    def test_known_option_missing(self):
        # Given a need without an option that is listed in the required options
        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            docname=None,
            lineno=None,
        )

        # Expect that the checks fail and a warning is logged
        assert check_options(need, self.LOGGER, self.NEED_TYPE_INFO) is True
        self.LOGGER.warning.assert_called_with(
            f'Need: {need["id"]} is missing required option: `some_option`.',
            location=ANY,
        )

    def test_value_violates_pattern(self):
        # Given a need with an option that is listed in the required options but the value violates the pattern
        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            some_option="some_value_001",
            docname=None,
            lineno=None,
        )

        # Expect that the checks fail and a warning is logged
        assert check_options(need, self.LOGGER, self.NEED_TYPE_INFO) is True
        self.LOGGER.warning.assert_called_with(
            f'Need: {need["id"]} option `some_option` with value `{need["some_option"]}` does not follow pattern `{self.NEED_TYPE_INFO[0]["req_opt"][0][1]}`.',
            location=ANY,
        )
