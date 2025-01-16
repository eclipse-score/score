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
from unittest.mock import ANY, MagicMock, patch

import pytest
from sphinx.util.logging import SphinxLoggerAdapter
from docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability import (
    check_g_reqid_traceability,
    check_linkage_parent,
    check_linkage_safety,
    check_linkage_status,
    get_all_needs,
)
from sphinx_needs.data import NeedsInfoType


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
    def test_check_g_reqid_traceability_positive(self):
        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need = NeedsInfoType(
            target_id="STKH_REQ__001",
            id="STKH_REQ__toolchain_sphinx_needs_build__requirement_linkage_test",
            type="stkh_req",
            reqtype="Functional",
            security="NO",
            status="valid",
            safety="QM",
            satisfies=[],
            docname=None,
            lineno=None,
        )

        assert check_g_reqid_traceability(need, logger) is False

    def test_check_g_reqid_traceability_satisfies_false_value_with_stakeholder(self):
        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need = NeedsInfoType(
            target_id="STKH_REQ__001",
            id="STKH_REQ__toolchain_sphinx_needs_build__requirement_linkage_test",
            type="stkh_req",
            reqtype="Functional",
            security="NO",
            status="valid",
            safety="QM",
            satisfies=[
                "TOOL_REQ_",
            ],
            docname=None,
            lineno=None,
        )

        assert check_g_reqid_traceability(need, logger) is True

        logger.warning.assert_called_with(
            "option 'satisfies' not allowed in 'stkh_req' directives.",
            location=ANY,
        )

    def test_check_g_reqid_traceability_missing_satisfies(self):
        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            docname=None,
            lineno=None,
        )

        assert check_g_reqid_traceability(need, logger) is True

        logger.warning.assert_called_with(
            "option 'satisfies' missing in TOOL_REQ__001. satisfies is requiered in `feat_req, comp_req, tool_req` directives.",
            location=ANY,
        )

    def test_check_g_reqid_traceability_satisfies_positive(self):
        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=["GD_1"],
            docname=None,
            lineno=None,
        )

        assert check_g_reqid_traceability(need, logger) is False

    def test_check_linkage_parent_positive(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="TOOL_REQ__1",
            id="TOOL_REQ__2",
            type="comp_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_B",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__2",
            id="FEAT_REQ__2",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)
            assert check_linkage_parent(need_1, logger) is False

    def test_check_linkage_parent_negative(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="TOOL_REQ__1",
            id="TOOL_REQ__1",
            type="comp_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_B",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__3",
            id="FEAT_REQ__3",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=[
                "FEAT_REQ__4",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)
            assert check_linkage_parent(need_1, logger) is True

            logger.warning.assert_called_with(
                f"Need: {need_1["id"]} have invalid status of parent requirement: {need_1["satisfies"][0]} \n",
                location=None,
            )

    def test_check_linkage_safety_positive(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="COMP_REQ__1",
            id="COMP_REQ__1",
            type="comp_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_B",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__2",
            id="FEAT_REQ__2",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_D",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)
            assert check_linkage_safety(need_1, logger) is False

    def test_check_linkage_safety_negative_ASIL_D(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="COMP_REQ__1",
            id="COMP_REQ__1",
            type="comp_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_D",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__2",
            id="FEAT_REQ__2",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_B",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)

            assert check_linkage_safety(need_1, logger) is True

            logger.warning.assert_called_with(
                "Need: `COMP_REQ__1` with `ASIL_D` has no parent requirement that contains the same or lower ASIL. Alloed ASIL values: 'ASIL_D'. \n",
                location=ANY,
            )

    def test_check_linkage_safety_negative_ASIL_B(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="COMP_REQ__1",
            id="COMP_REQ__1",
            type="comp_req",
            reqtype="Functional",
            security="NO",
            safety="ASIL_B",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__2",
            id="FEAT_REQ__2",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)

            assert check_linkage_safety(need_1, logger) is True

            logger.warning.assert_called_with(
                "Need: `COMP_REQ__1` with `ASIL_B` has no parent requirement that contains the same or lower ASIL. Alloed ASIL values: 'ASIL_B', 'ASIL_D'. \n",
                location=ANY,
            )

    def test_check_linkage_status_positive(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="TOOL_REQ__1",
            id="TOOL_REQ__1",
            type="tool_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=[
                "FEAT_REQ__2",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__2",
            id="FEAT_REQ__2",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)
            assert check_linkage_status(need_1, logger) is False

    def test_check_linkage_status_check_negative(self):
        local_all_needs = {}

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="TOOL_REQ__001",
            id="TOOL_REQ__001",
            type="tool_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=["FEAT_REQ__2", "FEAT_REQ__3"],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="FEAT_REQ__2",
            id="FEAT_REQ__2",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="valid",
            satisfies=[
                "FEAT_REQ__3",
            ],
            docname=None,
            lineno=None,
        )
        need_3 = NeedsInfoType(
            target_id="FEAT_REQ__3",
            id="FEAT_REQ__3",
            type="feat_req",
            reqtype="Functional",
            security="NO",
            safety="QM",
            status="invalid",
            satisfies=[
                "FEAT_REQ__4",
            ],
            docname=None,
            lineno=None,
        )
        local_all_needs[need_1["id"]] = need_1
        local_all_needs[need_2["id"]] = need_2
        local_all_needs[need_3["id"]] = need_3

        with patch(
            "docs._tooling.sphinx_extensions.sphinx_extensions.requirements.checks.traceability.all_needs",
            local_all_needs,
        ):
            # Test get_all_needs and check_linkage_status_check with patched all_needs
            get_all_needs(need_1, logger)
            get_all_needs(need_2, logger)
            get_all_needs(need_3, logger)

            assert check_linkage_status(need_1, logger) is True

            logger.warning.assert_called_with(
                "Need: `TOOL_REQ__001` have a valid status but one of it's parents: `FEAT_REQ__3` have an invalid status. \n",
                location=ANY,
            )
