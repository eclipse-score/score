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
import docs._tooling.extensions.score_metamodel.tests as tests
from docs._tooling.extensions.score_metamodel.checks.traceability import (
    check_linkage_parent,
    check_linkage_safety,
    check_linkage_status,
)


# @pytest.mark.metadata(
#     Verifies=[
#         "TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_status_check"
#     ],
#     Description="It should check the traceability like linkage of attributes.",
#     ASIL="ASIL_D",
#     Priority="1",
#     TestType="Requirements-based test",
#     DerivationTechnique="Analysis of requirements",
# )
class TestTraceability:
    def test_check_linkage_parent_positive(self):
        local_all_needs = {}

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
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        # Test get_all_needs and check_linkage_status_check with patched all_needs
        check_linkage_parent(local_all_needs, logger)
        assert not logger.has_warnings

    def test_check_linkage_parent_negative(self):
        local_all_needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="TOOL_REQ__1",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__3",
            status="valid",
            satisfies=[
                "FEAT_REQ__4",
            ],
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        # Test get_all_needs and check_linkage_status_check with patched all_needs
        check_linkage_parent(local_all_needs, logger) is True

        tests.verify_log_string(logger,
                                f"invalid status of parent requirement: {
                                    need_1["satisfies"][0]}",
                                )

    def test_check_linkage_safety_positive(self):
        local_all_needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="COMP_REQ__1",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        check_linkage_safety(local_all_needs, logger)
        assert not logger.has_warnings

    def test_check_linkage_safety_negative_ASIL_D(self):
        local_all_needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="COMP_REQ__1",
            safety="ASIL_D",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            safety="ASIL_B",
            satisfies=[
                "FEAT_REQ__3",
            ],
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        check_linkage_safety(local_all_needs, logger)
        tests.verify_log_string(logger, "lower ASIL")

    def test_check_linkage_safety_negative_ASIL_B(self):

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="COMP_REQ__1",
            safety="ASIL_B",
            satisfies=[
                "FEAT_REQ__2",
            ],
        )

        need_2 = tests.need(
            id="FEAT_REQ__2",
            safety="QM",
            satisfies=[
                "FEAT_REQ__3",
            ],
        )
        local_all_needs = {}
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        check_linkage_safety(local_all_needs, logger)
        tests.verify_log_string(logger, "lower ASIL")

    def test_check_linkage_status_positive(self):
        local_all_needs = {}

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
                "FEAT_REQ__3",
            ],
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        check_linkage_status(local_all_needs, logger)
        assert not logger.has_warnings

    def test_check_linkage_status_check_negative(self):
        local_all_needs = {}

        logger = tests.fake_check_logger()

        need_1 = tests.need(
            id="TOOL_REQ__001",
            status="valid",
            satisfies=["FEAT_REQ__2", "FEAT_REQ__3"],
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
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2
        local_all_needs[need_3["id"]] = need_3

        check_linkage_status(local_all_needs, logger)

        tests.verify_log_string(logger,
                                "valid status but one of it's parents: `FEAT_REQ__3` have an invalid status.",
                                )
