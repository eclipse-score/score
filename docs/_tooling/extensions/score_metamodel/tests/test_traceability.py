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


#          ╭──────────────────────────────────────╮
#          │  TEST DISABLED DUE TO CHECKS BEING   │
#          │               DISABLED               │
#          ╰──────────────────────────────────────╯


# from unittest.mock import Mock
#
# import pytest
# from sphinx.application import Sphinx
# from sphinx_needs.data import NeedsInfoType
#
# import score_metamodel.tests as tests
# from score_metamodel.checks.traceability import (
#     check_linkage_parent,
#     check_linkage_safety,
#     check_linkage_status,
# )
#
#
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
# class TestTraceability:
#     def test_check_linkage_parent_positive(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="TOOL_REQ__1",
#             status="valid",
#             satisfies=[
#                 "feat_req__2",
#             ],
#         )
#
#         need_2 = NeedsInfoType(
#             id="feat_req__2",
#             status="valid",
#             satisfies=[
#                 "TOOL_REQ__1",
#             ],
#         )
#         needs = [need_1, need_2]
#
#         check_linkage_parent(app, needs, logger)
#         logger.assert_no_warnings()
#
#     def test_check_linkage_parent_negative(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="TOOL_REQ__1",
#             status="valid",
#             satisfies=[
#                 "feat_req__2",
#             ],
#         )
#
#         needs = [need_1]
#
#         check_linkage_parent(app, needs, logger)
#
#         logger.assert_warning(
#             f"has a parent requirement(s): `{need_1['satisfies'][0]}` with an "
#             f"invalid status.",
#             expect_location=False,
#         )
#
#     def test_check_linkage_safety_positive(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="COMP_REQ__1",
#             status="valid",
#             safety="QM",
#             satisfies=[
#                 "feat_req__2",
#             ],
#         )
#
#         need_2 = NeedsInfoType(
#             id="feat_req__2",
#             status="valid",
#             safety="QM",
#             satisfies=[
#                 "stkh_req__communication__intra_process",
#             ],
#         )
#
#         need_3 = NeedsInfoType(
#             id="stkh_req__communication__intra_process",
#             status="valid",
#             safety="QM",
#         )
#
#         needs = [need_1, need_2, need_3]
#
#         check_linkage_safety(app, needs, logger)
#         logger.assert_no_warnings()
#
#     def test_check_linkage_safety_negative_ASIL_D(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="feat_req__1",
#             safety="ASIL_D",
#             satisfies=[
#                 "stkh_req__communication__inter_process",
#             ],
#         )
#
#         need_2 = NeedsInfoType(
#             id="stkh_req__communication__inter_process",
#             status="valid",
#             safety="ASIL_B",
#         )
#
#         needs = [need_1, need_2]
#
#         check_linkage_safety(app, needs, logger)
#         logger.assert_warning(
#             f"with `{need_1['safety']}` has no parent requirement that contains "
#             f"the same or lower ASIL. Allowed ASIL values: `ASIL_D`.",
#             expect_location=False,
#         )
#
#     def test_check_linkage_safety_negative_ASIL_B(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="feat_req__1",
#             safety="ASIL_B",
#             satisfies=[
#                 "stkh_req__communication__inter_process",
#             ],
#         )
#
#         need_2 = NeedsInfoType(
#             id="stkh_req__communication__inter_process",
#             safety="QM",
#         )
#         needs = [need_1, need_2]
#
#         check_linkage_safety(app, needs, logger)
#         logger.assert_warning(
#             f"with `{need_1['safety']}` has no parent requirement that contains "
#             f"the same or lower ASIL. Allowed ASIL values: `ASIL_B`, `ASIL_D`.",
#             expect_location=False,
#         )
#
#     def test_check_linkage_status_positive(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="TOOL_REQ__1",
#             status="valid",
#             satisfies=[
#                 "feat_req__2",
#             ],
#         )
#
#         need_2 = NeedsInfoType(
#             id="feat_req__2",
#             status="valid",
#         )
#         needs = [need_1, need_2]
#
#         check_linkage_status(app, needs, logger)
#         logger.assert_no_warnings()
#
#     def test_check_linkage_status_negative(self):
#         logger = tests.fake_check_logger()
#         app = Mock(spec=Sphinx)
#
#         need_1 = NeedsInfoType(
#             id="TOOL_REQ__001",
#             status="valid",
#             satisfies=["feat_req__2"],
#         )
#
#         need_2 = NeedsInfoType(
#             id="feat_req__2",
#             status="valid",
#             satisfies=[
#                 "feat_req__3",
#             ],
#         )
#         need_3 = NeedsInfoType(
#             id="feat_req__3",
#             status="invalid",
#             satisfies=[
#                 "feat_req__4",
#             ],
#         )
#         needs = [need_1, need_2, need_3]
#         check_linkage_status(app, needs, logger)
#
#         logger.assert_warning(
#             "has a valid status but one of its parents: `feat_req__3` has an "
#              "invalid status.",
#             expect_location=False,
#         )
