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

from docs._tooling.extensions.score_metamodel.checks.id_format_and_length import (
    check_id_format,
    check_id_length,
)
from docs._tooling.extensions.score_metamodel.tests import (
    fake_check_logger,
    verify_log_string,
)


class TestId:
    def test_check_id_format_positive(self):
        """
        Test check_id_length function with a positive case.
        """

        need = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            type="gd_req",
            tags="attribute",
            security="NO",
            complies=[
                "STD_REQ_ISO26262__rq-8-6666",
                "STD_REQ_ISO26262__rq-8-6777",
            ],
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()

        check_id_format(need, logger)
        assert not logger.has_warnings

    def test_check_id_format_two_mendatory_substrings_parts_negative(self):
        """
        Test check_id_length function with a negative case.
        """

        need = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ_attribute_satisfies",
            type="gd_req",
            tags="attribute",
            security="NO",
            complies=[
                "STD_REQ_ISO26262__rq-8-6666",
                "STD_REQ_ISO26262__rq-8-6777",
            ],
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()

        check_id_format(need, logger)

        verify_log_string(
            logger,
            "expected to consisting of at least 2 substrings:`<Req Type>__<Abbreviations>`.",
            expect_location=False,
        )

    def test_check_id_format_three_mendatory_substrings_parts_negative(self):
        """
        Test check_id_length function with a negative case.
        """

        need = NeedsInfoType(
            id="TOOL_REQ__1",
            type="tool_req",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()

        check_id_format(need, logger)

        verify_log_string(
            logger,
            "expected to consisting of 3 substrings: `<Req Type>__<Abbreviations>__<Architectural Element>`.",
            expect_location=False,
        )

    def test_check_id_length_positive(self):
        """
        Test check_id_length function with a positive case.
        """

        need = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="STD_REQ_ISO26262__rq_8_6432",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()

        check_id_length(need, logger)
        assert not logger.has_warnings

    def test_check_id_length_negative(self):
        """
        Test check_id_length function with a positive case.
        """

        need = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="STD_REQ_ISO26262__rq_8_6432_00000000000",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        logger = fake_check_logger()

        check_id_length(need, logger)
        verify_log_string(
            logger,
            f'exceeds the maximum allowed length of 30 characters (current length: {len(need['id'])}).',
            expect_location=False,
        )
