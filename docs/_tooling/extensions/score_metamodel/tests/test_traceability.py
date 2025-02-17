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
import pytest
from sphinx_needs.data import NeedsInfoType

import score_metamodel.tests as tests
from score_metamodel.checks.traceability import (
    check_linkage_parent,
    check_linkage_safety,
    check_linkage_status,
)


@pytest.mark.metadata(
    Verifies=[
        "TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_status_check"
    ],
    Description="It should check the traceability like linkage of attributes.",
    ASIL="ASIL_D",
    Priority="1",
    TestType="Requirements-based test",
    DerivationTechnique="Analysis of requirements",
)
class TestTraceability:
    def test_check_linkage_parent_positive(self):
        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="TOOL_REQ__1",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            status="valid",
            satisfies=[
                "TOOL_REQ__1",
            ],
        )
        needs = [need_1, need_2]

        check_linkage_parent(needs, logger)
        logger.assert_no_warnings()

    def test_check_linkage_parent_negative(self):
        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="TOOL_REQ__1",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        needs = [need_1]

        check_linkage_parent(needs, logger)

        logger.assert_warning(
            f"has a parent requirement(s): `{need_1['satisfies'][0]}` with an invalid status.",
            expect_location=False,
        )

    def test_check_linkage_safety_positive(self):
        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="COMP_REQ__1",
            status="valid",
            safety="QM",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            status="valid",
            safety="QM",
            satisfies=[
                "STKH_REQ__3",
            ],
        )

        need_3 = tests.need(
            id="STKH_REQ__3",
            status="valid",
            safety="QM",
        )

        needs = [need_1, need_2, need_3]

        check_linkage_safety(needs, logger)
        logger.assert_no_warnings()

    def test_check_linkage_safety_negative_ASIL_D(self):
        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="FEAT_REQ__1",
            safety="ASIL_D",
            satisfies=[
                "STKH_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="STKH_REQ__2",
            status="valid",
            safety="ASIL_B",
        )

        needs = [need_1, need_2]

        check_linkage_safety(needs, logger)
        logger.assert_warning(
            f"with `{need_1['safety']}` has no parent requirement that contains the same or lower ASIL. Allowed ASIL values: `ASIL_D`.",
            expect_location=False,
        )

    def test_check_linkage_safety_negative_ASIL_B(self):
        needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="FEAT_REQ__1",
            safety="ASIL_B",
            satisfies=[
                "STKH_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="STKH_REQ__2",
            safety="QM",
        )
        needs = [need_1, need_2]

        check_linkage_safety(needs, logger)
        logger.assert_warning(
            f"with `{need_1['safety']}` has no parent requirement that contains the same or lower ASIL. Allowed ASIL values: `ASIL_B`, `ASIL_D`.",
            expect_location=False,
        )

    def test_check_linkage_status_positive(self):
        needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="TOOL_REQ__1",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            status="valid",
        )
        needs = [need_1, need_2]

        check_linkage_status(needs, logger)
        logger.assert_no_warnings()

    def test_check_linkage_status_negative(self):
        needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="TOOL_REQ__001",
            status="valid",
            satisfies=["FEAT_REQ__2"],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
        )
        need_3 = tests.need(
            id="FEAT_REQ__3",
            status="invalid",
            satisfies=[
                "FEAT_REQ__4",
            ],
        )
        needs = [need_1, need_2, need_3]
        check_linkage_status(needs, logger)

        logger.assert_warning(
            "has a valid status but one of its parents: `FEAT_REQ__3` has an invalid status.",
            expect_location=False,
        )
