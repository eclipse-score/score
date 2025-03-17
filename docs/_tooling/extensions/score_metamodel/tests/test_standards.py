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

from sphinx.application import Sphinx
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.checks import standards
from docs._tooling.extensions.score_metamodel.tests import fake_check_logger


class TestStandards:
    #                    ╭──────────────────────────────────────────────────────────────────────────────╮
    #                    │                             Disabled temporarly                              │
    #                    ╰──────────────────────────────────────────────────────────────────────────────╯
    #   def test_check_all_standard_req_linked_item_via_the_compliance_req_positive(self):
    #        """
    #        Test if check all_standard_req_linked_item_via_the_compliance_req function will give a False value (check is valid) when giving a standar requirement which is linked to at least one of the list of items that have complies tag via the same tag.
    #        """
    #
    #        need_1 = NeedsInfoType(
    #            target_id="Traceability of safety requirements",
    #            id="std_req__iso26262__rq-8-6432",
    #            type="std_req",
    #            reqtype="Functional",
    #            status="valid",
    #            docname=None,
    #            lineno=None,
    #        )
    #
    #        need_2 = NeedsInfoType(
    #            target_id="Requirements attribute satisfies",
    #            id="gd_req__attribute_satisfies",
    #            tags="attribute",
    #            security="NO",
    #            type="gd_req",
    #            complies=[
    #                "std_req__iso26262__rq-8-6432",
    #                "std_req__iso26262__rq-8-6422",
    #            ],
    #            status="valid",
    #            satisfies=[
    #             "gd_req__create_maintain_requirements",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_all_standard_req_linked_item_via_the_compliance_req(
    #         app, needs, logger
    #     )
    #     logger.assert_no_warnings()

    # def test_check_standard_req_linked_item_via_the_compliance_req_negative(self):
    #     """
    #     Test if check all_standard_req_linked_item_via_the_compliance_req function will give a False value (check is invalid) when giving a standar requirement which is not linked to at least one of the list of items that have complies tag via the same tag.
    #     """

    #     need_1 = NeedsInfoType(
    #         target_id="Traceability of safety requirements",
    #         id="std_req__iso26262__rq-8-6432",
    #         type="std_req",
    #         reqtype="Functional",
    #         status="valid",
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_2 = NeedsInfoType(
    #         target_id="Requirements attribute satisfies",
    #         id="gd_req__attribute_satisfies",
    #         type="gd_req",
    #         tags="attribute",
    #         security="NO",
    #         complies=[
    #             "std_req__iso26262__rq-8-0000",
    #             "std_req__iso26262__rq-8-1111",
    #         ],
    #         status="valid",
    #         satisfies=[
    #             "gd_req__create_maintain_requirements",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_all_standard_req_linked_item_via_the_compliance_req(
    #         app, needs, logger
    #     )
    #     logger.assert_warning(
    #         f"Standard requirement `{need_1['id']}` is not linked to at least one item via the complies tag.",
    #         expect_location=False,
    #     )

    # def test_check_all_standard_workproducts_linked_item_via_the_compliance_wp_positive(
    #     self,
    # ):
    #     """
    #     Test if check all_standard_workproducts_linked_item_via_the_compliance_wp function will give a False value (check is valid) when giving a standar workproduct which is linked to at least one of the list of items that have complies tag via the same tag.
    #     """

    #     need_1 = NeedsInfoType(
    #         target_id="Organization-specific rules and processes for functional safety",
    #         id="std_wp__iso26262__wp-2-551",
    #         type="std_wp",
    #         status="valid",
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_2 = NeedsInfoType(
    #         target_id="wp__policies",
    #         id="wp__policies",
    #         type="workproduct",
    #         status="draft",
    #         tags="requirements_management",
    #         relevant="PH_SPR_PLAN",
    #         complies=[
    #             "std_wp__iso26262__wp-2-551",
    #             "std_req__iso26262__wp-05-01",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_all_standard_workproducts_linked_item_via_the_compliance_wp(
    #         app, needs, logger
    #     )
    #     logger.assert_no_warnings()

    # def test_check_standard_workproducts_linked_item_via_the_compliance_wp_negative(
    #     self,
    # ):
    #     """
    #     Test if check all_standard_workproducts_linked_item_via_the_compliance_wp function will give a True value (check is invalid) when giving a standar workproduct which is not linked to at least one of the list of items that have complies tag via the same tag.
    #     """

    #     need_1 = NeedsInfoType(
    #         target_id="Organization-specific rules and processes for functional safety",
    #         id="std_wp__iso26262__wp-2-551",
    #         type="std_wp",
    #         status="valid",
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_2 = NeedsInfoType(
    #         target_id="wp__policies",
    #         id="wp__policies",
    #         type="workproduct",
    #         status="draft",
    #         complies=[
    #             "std_wp__iso26262__wp-2-777",
    #             "std_req__iso21434__wp-05-88",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_all_standard_workproducts_linked_item_via_the_compliance_wp(
    #         app, needs, logger
    #     )

    #     logger.assert_warning(
    #         f"Standard workproduct `{need_1['id']}` is not linked to at least one item via the complies tag.",
    #         expect_location=False,
    #     )

    # def test_check_workproduct_uniqueness_over_workflows_positive(self):
    #     """
    #     Test if check check_workproduct_uniqueness_over_workflows function will give a False value (check is valid) when giving a workproduct which is linked exactly to one workflow least from the list of all workflows via output option.
    #     """
    #     need_1 = NeedsInfoType(
    #         target_id="Module Safety Plan",
    #         type="workproduct",
    #         id="wp__module_safety_plan",
    #         status="valid",
    #         complies=[
    #             "std_wp__iso26262__wp-2-653",
    #             "std_wp__iso26262__wp-8-853",
    #             "std_wp__iso26262__wp-8-1251",
    #             "std_wp__iso26262__wp-8-1252",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_2 = NeedsInfoType(
    #         target_id="Create/Maintain Safety Plan",
    #         type="workflow",
    #         id="wf__cr_mt_safety_plan",
    #         status="draft",
    #         input=["wp__platform_mgmt", "wp__issue_track_system"],
    #         output=["wp__module_safety_plan", "wp__platform_safety_plan"],
    #         contains=[
    #             "std_req__iso26262__rq-2-6461",
    #             "std_req__iso26262__rq-2-6462",
    #             "std_req__iso26262__rq-2-6463",
    #             "std_req__iso26262__rq-2-6465",
    #             "std_req__iso26262__rq-2-6468",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_workproduct_uniqueness_over_workflows(app, needs, logger)
    #     logger.assert_no_warnings()

    # def test_check_workproduct_uniqueness_over_workflows_negative_wprkproduct_not_listed_in_any_workflow(
    #     self,
    # ):
    #     """
    #     Test if check check_workproduct_uniqueness_over_workflows function will give a True value (check is invalid) when giving a workproduct which is linked exactly to no workflow from the list of all workflows via output option.
    #     """

    #     need_1 = NeedsInfoType(
    #         target_id="Module Safety Plan",
    #         type="workproduct",
    #         id="wp__module_safety_plan",
    #         status="valid",
    #         relevant="PH_SPR_PLAN",
    #         complies=[
    #             "std_wp__iso26262__wp-2-653",
    #             "std_wp__iso26262__wp-8-853",
    #             "std_wp__iso26262__wp-8-1251",
    #             "std_wp__iso26262__wp-8-1252",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_2 = NeedsInfoType(
    #         target_id="Create/Maintain Safety Plan",
    #         type="workflow",
    #         id="wf__cr_mt_safety_plan",
    #         status="draft",
    #         input=["wp__platform_mgmt", "wp__issue_track_system"],
    #         output=["wp__platform_safety_plan"],
    #         contains=[
    #             "std_req__iso26262__rq-2-6461",
    #             "std_req__iso26262__rq-2-6462",
    #             "std_req__iso26262__rq-2-6463",
    #             "std_req__iso26262__rq-2-6465",
    #             "std_req__iso26262__rq-2-6468",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_workproduct_uniqueness_over_workflows(app, needs, logger)

    #     logger.assert_warning(
    #         "is not contained in any workflow, which is incorrect.",
    #         expect_location=False,
    #     )

    # def test_check_workproduct_uniqueness_over_workflows_negative_wprkproduct_listed_in_multiple_workflows(
    #     self,
    # ):
    #     """
    #     Test if check check_workproduct_uniqueness_over_workflows function will give a True value (check is invalid) when giving a workproduct which is linked exactly to more then one workflow from the list of all workflows via output option.
    #     """

    #     need_1 = NeedsInfoType(
    #         target_id="Module Safety Plan",
    #         type="workproduct",
    #         id="wp__module_safety_plan",
    #         status="valid",
    #         complies=[
    #             "std_wp__iso26262__wp-2-653",
    #             "std_wp__iso26262__wp-8-853",
    #             "std_wp__iso26262__wp-8-1251",
    #             "std_wp__iso26262__wp-8-1252",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_2 = NeedsInfoType(
    #         target_id="Create/Maintain Safety Plan",
    #         type="workflow",
    #         id="wf__cr_mt_safety_plan",
    #         status="draft",
    #         input=["wp__platform_mgmt", "wp__issue_track_system"],
    #         output=["wp__module_safety_plan", "wp__platform_safety_plan"],
    #         contains=[
    #             "std_req__iso26262__rq-2-6461",
    #             "std_req__iso26262__rq-2-6462",
    #             "std_req__iso26262__rq-2-6463",
    #             "std_req__iso26262__rq-2-6465",
    #             "std_req__iso26262__rq-2-6468",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     need_3 = NeedsInfoType(
    #         target_id="Review/Approve Contribution request",
    #         type="workflow",
    #         id="wf__rv_ap_ContrRequest",
    #         status="valid",
    #         input=["wp__cont_request"],
    #         output=["wp__module_safety_plan", "wp__cont_request"],
    #         contains=[
    #             "std_req__iso26262__rq-8-8411",
    #             "std_req__isoPAS8926__rq-4431",
    #             "std_req__isoPAS8926__rq-44321",
    #             "std_req__isoPAS8926__rq-44322",
    #             "std_req__isoPAS8926__rq-4433",
    #             "std_req__isoPAS8926__rq-44341",
    #             "std_req__isoPAS8926__rq-44342",
    #         ],
    #         docname=None,
    #         lineno=None,
    #     )

    #     needs = [need_1, need_2, need_3]

    #     logger = fake_check_logger()
    #     app = Mock(spec=Sphinx)

    #     standards.check_workproduct_uniqueness_over_workflows(app, needs, logger)

    #     ids = [need_2["id"], need_3["id"]]
    #     workflows_str = ", ".join(f"`{id}`" for id in ids)
    #     logger.assert_warning(
    #         f"is contained in {2} workflows: {workflows_str}, which is incorrect.",
    #         expect_location=False,
    #     )
    #                    ╭──────────────────────────────────────────────────────────────────────────────╮
    #                    │                            END OF TEMP DISABLING                             │
    #                    ╰──────────────────────────────────────────────────────────────────────────────╯

    def test_my_pie_linked_standard_requirements(self):
        """
        Simulate results  for my_pie_linked_standard_requirements function and check if the result parameter after calling this function a special case will give the correct value.
        """
        needs = {}

        need_1 = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="std_req__iso26262__rq-8-6432",
            type="std_req",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Traceability",
            id="std_req__iso26262__rq-8-0000",
            type="std_req",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="gd_req__attribute_satisfies",
            security="NO",
            type="gd_req",
            complies=[
                "std_req__iso26262__rq-8-6432",
                "std_req__iso26262__rq-8-6422",
            ],
            status="valid",
            satisfies=[
                "gd_req__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2, need_3]

        # Initialize results
        results = []

        # Call the function
        standards.my_pie_linked_standard_requirements(needs, results, arg1="iso26262")

        # Check that results are [1, 1]
        assert results == [
            1,
            1,
        ], f"For function my_pie_linked_standard_requirements expected [1, 1] but got {
            results
        }"

    def test_my_pie_linked_standard_workproducts(self):
        """
        Simulate results  for test_my_pie_linked_standard_workproducts function and check if the result parameter after calling this function with a special case will give the correct value.
        """

        need_1 = NeedsInfoType(
            target_id="Organization-specific rules and processes for functional safety",
            id="std_wp__iso26262__wp-2-551",
            type="std_wp",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="specific rules for processes",
            id="std_wp__iso26262__wp-2-0000",
            type="std_wp",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="wp__policies",
            id="wp__policies",
            status="draft",
            type="workproduct",
            complies=[
                "std_wp__iso26262__wp-2-551",
                "std_req__iso21434_wp-05-01",
            ],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2, need_3]

        # Initialize results
        results = []

        # Call the function
        standards.my_pie_linked_standard_workproducts(needs, results, arg1="iso26262")

        # Check that results are [1, 1]
        assert results == [
            1,
            1,
        ], f"For function my_pie_linked_standard_workproducts expected [1, 1] but got {
            results
        }"

    def test_my_pie_workproducts_contained_in_exactly_one_workflow(self):
        """
        Simulate results  for test_my_pie_workproducts_contained_in_exactly_one_workflow function and check if the result parameter after calling this function with a special case will give the correct value.
        """

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="wp__module_safety_plan",
            status="valid",
            complies=[
                "std_wp__iso26262__wp-2-653",
                "std_wp__iso26262__wp-8-853",
                "std_wp__iso26262__wp-8-1251",
                "std_wp__iso26262__wp-8-1252",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="wf__cr_mt_safety_plan",
            status="draft",
            input=["wp__platform_mgmt", "wp__issue_track_system"],
            output=["wp__module_safety_plan", "wp__platform_safety_plan"],
            contains=[
                "std_req__iso26262__rq-2-6461",
                "std_req__iso26262__rq-2-6462",
                "std_req__iso26262__rq-2-6463",
                "std_req__iso26262__rq-2-6465",
                "std_req__iso26262__rq-2-6468",
            ],
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="wp__module",
            status="valid",
            complies=[
                "std_wp__iso26262__wp-2-653",
                "std_wp__iso26262__wp-8-853",
                "std_wp__iso26262__wp-8-1251",
                "std_wp__iso26262__wp-8-1252",
            ],
            docname=None,
            lineno=None,
        )

        need_4 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="wp__module_safety",
            complies=[
                "std_wp__iso26262__wp-2-653",
                "std_wp__iso26262__wp-8-853",
                "std_wp__iso26262__wp-8-1251",
                "std_wp__iso26262__wp-8-1252",
            ],
            docname=None,
            lineno=None,
        )

        need_5 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF__CR_MT_SAFETY",
            status="draft",
            input=["wp__platform_mgmt", "wp__issue_track_system"],
            output=["wp__module_safety", "wp__platform_safety_plan"],
            contains=[
                "std_req__iso26262__rq-2-6461",
                "std_req__iso26262__rq-2-6462",
                "std_req__iso26262__rq-2-6463",
                "std_req__iso26262__rq-2-6465",
                "std_req__iso26262__rq-2-6468",
            ],
            docname=None,
            lineno=None,
        )

        need_6 = NeedsInfoType(
            target_id="Review/Approve Contribution request",
            type="workflow",
            id="wf__rv_ap_ContrRequest",
            status="valid",
            input=["wp__cont_request"],
            output=["wp__module_safety", "wp__cont_request"],
            contains=[
                "std_req__iso26262__rq-8-8411",
                "std_req__isoPAS8926__rq-4431",
                "std_req__isoPAS8926__rq-44321",
                "std_req__isoPAS8926__rq-44322",
                "std_req__isoPAS8926__rq-4433",
                "std_req__isoPAS8926__rq-44341",
                "std_req__isoPAS8926__rq-44342",
            ],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2, need_3, need_4, need_5, need_6]

        # Initialize results
        results = []

        # Call the function
        standards.my_pie_workproducts_contained_in_exactly_one_workflow(needs, results)

        # Check that results are [1, 1]
        assert (
            results == [1, 1, 1]
        ), f"For function my_pie_workproducts_contained_in_exactly_one_workflow expected [1, 1, 1] but got {
            results
        }"

    def test_get_standards_needs(self):
        """
        Test if get_standards_needs works as expected with a positive and negative test.
        """
        need_1 = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="std_req__iso26262__rq-8-6432",
            type="std_req",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Traceability of requirements",
            id="wp__11111111",
            reqtype="Functional",
            status="valid",
            type="std_wp",
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2]
        result = standards.get_standards_needs(needs)

        assert need_1 in result.values()
        assert need_2 not in result.values()

    def test_get_standards_workproducts(self):
        """
        Test if get_standards_workproducts works as expected with a positive and negative test.
        """
        need_1 = NeedsInfoType(
            target_id="Organization-specific rules and processes for functional safety",
            id="std_wp__iso26262__wp-2-551",
            type="std_wp",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Traceability of requirements",
            id="wp__11111111",
            reqtype="Functional",
            status="valid",
            type="std_req",
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2]
        result = standards.get_standards_workproducts(needs)

        assert need_1 in result.values()
        assert need_2 not in result.values()

    def test_get_compliance_req_needs(self):
        """
        Test if get_compliance_req_needs works as expected with a positive and negative test.
        """

        need_1 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="gd_req__attribute_satisfies",
            type="workproduct",
            tags="attribute",
            security="NO",
            complies=[
                "std_req__iso26262__rq-8-6666",
                "std_req__iso26262__rq-8-6777",
            ],
            status="valid",
            satisfies=[
                "gd_req__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="gd_req__attribute_satisfies",
            type="gd_req",
            tags="attribute",
            security="NO",
            complies=[
                "std_wp__iso26262__wp-2-551",
                "std_wp__isosae21434_wp-05-01",
            ],
            status="valid",
            satisfies=[
                "gd_req__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2]
        result = standards.get_compliance_req_needs(needs)

        assert need_1.get("complies", [])[0] not in result
        assert need_2.get("complies", [])[0] in result

    def test_get_compliance_wp_needs(self):
        """
        Test if get_compliance_wp_needs works as expected with a positive and negative test.
        """

        need_1 = NeedsInfoType(
            target_id="Requirements attribute satisfies_1",
            id="gd_req__attribute_satisfies",
            type="gd_req",
            tags="attribute",
            security="NO",
            complies=[
                "std_req__iso26262__rq-8-6432",
                "std_req__iso26262__rq-8-6422",
            ],
            status="valid",
            satisfies=["gd_req__create_maintain_requirements"],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="wp__attribute_satisfies_2",
            type="workproduct",
            tags="attribute",
            security="NO",
            complies=[
                "std_wp__iso26262__rq-8-6666",
                "std_wp__iso26262__rq-8-6777",
            ],
            status="valid",
            satisfies=["gd_req__create_maintain_requirements"],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2]
        result = standards.get_compliance_wp_needs(needs)

        assert need_1.get("complies", [])[0] not in result
        assert need_2.get("complies", [])[0] in result

    def test_get_workflows(self):
        """
        Test if get_workflows works as expected with a positive and negative test.
        """
        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="wp__module_safety_plan",
            status="valid",
            complies=[
                "std_wp__iso26262__wp-2-653",
                "std_wp__iso26262__wp-8-853",
                "std_wp__iso26262__wp-8-1251",
                "std_wp__iso26262__wp-8-1252",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="wf__cr_mt_safety_plan",
            status="draft",
            input=["wp__platform_mgmt", "wp__issue_track_system"],
            output=["wp__module_safety_plan", "wp__platform_safety_plan"],
            contains=[
                "std_req__iso26262__rq-2-6461",
                "std_req__iso26262__rq-2-6462",
                "std_req__iso26262__rq-2-6463",
                "std_req__iso26262__rq-2-6465",
                "std_req__iso26262__rq-2-6468",
            ],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2]
        result = standards.get_workflows(needs)

        assert need_1 not in result.values()
        assert need_2 in result.values()

    def test_get_workproducts(self):
        """
        Test if get_workproducts works as expected with a positive and negative test.
        """

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="wp__module_safety_plan",
            status="valid",
            complies=[
                "std_wp__iso26262__wp-2-653",
                "std_wp__iso26262__wp-8-853",
                "std_wp__iso26262__wp-8-1251",
                "std_wp__iso26262__wp-8-1252",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="wf__cstd_req__mt_safety_plan",
            status="draft",
            input=["wp__platform_mgmt", "wp__issue_track_system"],
            output=["wp__module_safety_plan", "wp__platform_safety_plan"],
            contains=[
                "std_req__iso26262__rq-2-6461",
                "std_req__iso26262__rq-2-6462",
                "std_req__iso26262__rq-2-6463",
                "std_req__iso26262__rq-2-6465",
                "std_req__iso26262__rq-2-6468",
            ],
            docname=None,
            lineno=None,
        )

        needs = [need_1, need_2]
        result = standards.get_workproducts(needs)

        assert need_1 in result.values()
        assert need_2 not in result.values()
