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

from unittest.mock import Mock

import pytest
from sphinx.application import Sphinx
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.checks.check_options import (
    check_extra_options,
    check_options,
)
from docs._tooling.extensions.score_metamodel.tests import fake_check_logger


@pytest.mark.metadata(
    Verifies=["tool_req__toolchain_sphinx_needs_build__options"],
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
            "mandatory_options": {
                "id": "^tool_req__.*$",
                "some_required_option": "^some_value__.*$",
            },
        }
    ]
    NEED_TYPE_INFO_WITH_OPT_OPT = [
        {
            "directive": "tool_req",
            "mandatory_options": {
                "id": "^tool_req__.*$",
                "some_required_option": "^some_value__.*$",
            },
            "opt_opt": {
                "some_optional_option": "^some_value__.*$",
            },
        }
    ]

    NEED_TYPE_INFO_WITH_REQ_LINK = [
        {
            "directive": "workflow",
            "mandatory_options": {
                "id": "wf__.*$",
                "status": "^(valid|draft)$",
            },
            "req_link": [
                ("input", "^wp__.*$"),
            ],
        }
    ]

    NEED_TYPE_INFO_WITH_OPT_LINK = [
        {
            "directive": "workflow",
            "mandatory_options": {
                "id": "wf__.*$",
                "status": "^(valid|draft)$",
            },
            "opt_link": [
                ("supported_by", "^rl__.*$"),
            ],
        }
    ]

    def test_known_directive_with_mandatory_option_and_allowed_value(self):
        # Given a need with a type that is listed in the required options
        #  and mandatory options present
        #  and with correct values
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__001",
            type="tool_req",
            some_required_option="some_value__001",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO
        # Expect that the checks pass
        check_options(app, need, logger)
        logger.assert_no_warnings()

    def test_known_directive_with_optional_and_mandatory_option_and_allowed_value(self):
        # Given a need with a type that is listed in the optional options
        #  and optional options present
        #  and with correct values
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__001",
            type="tool_req",
            some_required_option="some_value__001",
            some_optional_option="some_value__001",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO_WITH_OPT_OPT
        # Expect that the checks pass
        check_options(app, need, logger)

        logger.assert_no_warnings()

    def test_unknown_directive(self):
        # Given a need with a an unknown type it should raise an error
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__001",
            type="unknown_type",
            some_required_option="some_value__001",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO
        # Expect that the checks pass
        check_options(app, need, logger)
        logger.assert_warning(
            "no type info defined for semantic check.",
            expect_location=False,
        )

    def test_unknown_option_present_in_req_opt(self):
        # Given a need with an option that is not listed in the required options
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__0011",
            type="tool_req",
            some_required_option="some_value__001",
            other_option="some_other_value",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO
        # Expect that the checks pass
        check_extra_options(app, need, logger)
        logger.assert_warning(
            "has these extra options: `other_option`.",
            expect_location=False,
        )

    def test_unknown_option_present_in_neither_req_opt_neither_opt_opt(self):
        # Given a need with an option that is not listed in the required and optional options
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__0011",
            type="tool_req",
            some_required_option="some_value__001",
            some_optional_option="some_value__001",
            other_option="some_other_value",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO_WITH_OPT_OPT
        # Expect that the checks pass
        check_extra_options(app, need, logger)

        logger.assert_warning(
            "has these extra options: `other_option`.",
            expect_location=False,
        )

    def test_known_required_option_missing(self):
        # Given a need without an option that is listed in the required options
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__001",
            type="tool_req",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO
        # Expect that the checks fail and a warning is logged
        check_options(app, need, logger)
        logger.assert_warning(
            "is missing required option: `some_required_option`.",
            expect_location=False,
        )

    def test_value_violates_pattern_for_required_option(self):
        # Given a need with an option that is listed in the required options but the value violates the pattern
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__001",
            type="tool_req",
            some_required_option="some_value_001",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO
        # Expect that the checks fail and a warning is logged
        check_options(app, need, logger)
        logger.assert_warning(
            f'does not follow pattern `{self.NEED_TYPE_INFO[0]["mandatory_options"]["some_required_option"]}`.',
            expect_location=False,
        )

    def test_value_violates_pattern_for_optional_option(self):
        # Given a need with an option that is listed in the optional options but the value violates the pattern
        need = NeedsInfoType(
            target_id="tool_req__001",
            id="tool_req__001",
            type="tool_req",
            some_required_option="some_value__001",
            some_optional_option="some_value_001",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO_WITH_OPT_OPT
        # Expect that the checks fail and a warning is logged
        check_options(app, need, logger)
        logger.assert_warning(
            f'does not follow pattern `{self.NEED_TYPE_INFO_WITH_OPT_OPT[0]["opt_opt"]["some_optional_option"]}`.',
            expect_location=False,
        )

    def test_known_required_link_missing(self):
        # Given a need without an option that is listed in the required options
        need = NeedsInfoType(
            target_id="wf__p_confirm_rv",
            id="wf__p_confirm_rv",
            status="valid",
            type="workflow",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.needs_types = self.NEED_TYPE_INFO_WITH_REQ_LINK
        # Expect that the checks fail and a warning is logged
        check_options(app, need, logger)
        logger.assert_warning(
            "is missing required link: `input`.",
            expect_location=False,
        )

    # TODO: Remove commented code when re

    # def test_value_violates_pattern_for_optional_link(self):
    #     # Given a need without an option that is listed in the required options
    #     need = NeedsInfoType(
    #         target_id="wf__p_confirm_rv",
    #         id="wf__p_confirm_rv",
    #         status="valid",
    #         type="workflow",
    #         supported_by="rl_process_community",
    #         docname=None,
    #         lineno=None,
    #     )

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)
    #     app.config = Mock()
    #     app.config.needs_types = self.NEED_TYPE_INFO
    #     # Expect that the checks fail and a warning is logged
    #     check_options(app, need, logger, self.NEED_TYPE_INFO_WITH_OPT_LINK)
    #     logger.assert_warning(
    #         "does not follow pattern",
    #         expect_location=False,
    #     )
