from unittest.mock import ANY, MagicMock

from sphinx.util.logging import SphinxLoggerAdapter
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel.checks import standards
from docs._tooling.extensions.score_metamodel.tests import fake_check_logger


class TestStandards:
    def test_check_all_standard_req_linked_item_via_the_compliance_gd_positive(self):
        """
        Test if check all_standard_req_linked_item_via_the_compliance_gd function will give a False value (check is valid) when giving a standar requirement which is linked to at least one of the list of items that have complience-gd tag via the same tag.
        """

        need_1 = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="R_ISO26262_RQ-8-6432",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-gd": ["R_ISO26262_RQ-8-6432", "R_ISO26262_RQ-8-6422"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        standards.check_all_standard_req_linked_item_via_the_compliance_gd(
            needs, logger
        )
        assert not logger.has_warnings

    def test_check_standard_req_linked_item_via_the_compliance_gd_negative(self):
        """
        Test if check all_standard_req_linked_item_via_the_compliance_gd function will give a False value (check is invalid) when giving a standar requirement which is not linked to at least one of the list of items that have complience-gd tag via the same tag.
        """

        need_1 = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="R_ISO26262_RQ-8-6432",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-gd": ["R_ISO26262_RQ-8-0000", "R_ISO26262_RQ-8-1111"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        standards.check_all_standard_req_linked_item_via_the_compliance_gd(
            needs, logger
        )
        assert logger.has_warnings
        logger._log.assert_called_with(
            f"Standard requirement `{
                need_1['id']}` is not linked to at least one item via the compliance-gd tag. \n",
            location=ANY,
        )

    def test_check_all_standard_workproducts_linked_item_via_the_compliance_wp_positive(
        self,
    ):
        """
        Test if check all_standard_workproducts_linked_item_via_the_compliance_wp function will give a False value (check is valid) when giving a standar workproduct which is linked to at least one of the list of items that have complience-wp tag via the same tag.
        """

        need_1 = NeedsInfoType(
            target_id="Organization-specific rules and processes for functional safety",
            id="R_ISO26262_WP-2-551",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="WP_POLICIES",
            id="WP_POLICIES",
            status="draft",
            tags="requirements_management",
            relevant="PH_SPR_PLAN",
            **{"compliance-wp": ["R_ISO26262_WP-2-551", "R_ISO21434_WP-05-01"]},
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        assert (
            standards.check_all_standard_workproducts_linked_item_via_the_compliance_wp(
                app, logger
            )
            is False
        )

    def test_check_standard_workproducts_linked_item_via_the_compliance_wp_negative(
        self,
    ):
        """
        Test if check all_standard_workproducts_linked_item_via_the_compliance_wp function will give a True value (check is invalid) when giving a standar workproduct which is not linked to at least one of the list of items that have complience-wp tag via the same tag.
        """

        need_1 = NeedsInfoType(
            target_id="Organization-specific rules and processes for functional safety",
            id="R_ISO26262_WP-2-551",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="WP_POLICIES",
            id="WP_POLICIES",
            status="draft",
            **{"compliance-wp": ["R_ISO26262_WP-2-777", "R_ISO21434_WP-05-88"]},
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        assert (
            standards.check_all_standard_workproducts_linked_item_via_the_compliance_wp(
                app, logger
            )
            is True
        )
        logger.warning.assert_called_with(
            f"Standard workproduct `{
                need_1['id']}` is not linked to at least one item via the compliance-wp tag. \n",
            location=ANY,
        )

    def test_check_workproduct_uniqueness_over_workflows_positive(self):
        """
        Test if check check_workproduct_uniqueness_over_workflows function will give a False value (check is valid) when giving a workproduct which is linked exactly to one workflow least from the list of all workflows via output option.
        """
        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY_PLAN",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY_PLAN",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_MODULE_SAFETY_PLAN", "WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        assert (
            standards.check_workproduct_uniqueness_over_workflows(
                app, logger) is False
        )

    def test_check_workproduct_uniqueness_over_workflows_negative_wprkproduct_not_listed_in_any_workflow(
        self,
    ):
        """
        Test if check check_workproduct_uniqueness_over_workflows function will give a True value (check is invalid) when giving a workproduct which is linked exactly to no workflow from the list of all workflows via output option.
        """

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY_PLAN",
            status="valid",
            relevant="PH_SPR_PLAN",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY_PLAN",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        assert (
            standards.check_workproduct_uniqueness_over_workflows(
                app, logger) is True
        )
        logger.warning.assert_called_with(
            f"Workproduct `{
                need_1['id']}` is not contained in any workflow, which is incorrect. \n",
            location=ANY,
        )

    def test_check_workproduct_uniqueness_over_workflows_negative_wprkproduct_listed_in_multiple_workflows(
        self,
    ):
        """
        Test if check check_workproduct_uniqueness_over_workflows function will give a True value (check is invalid) when giving a workproduct which is linked exactly to more then one workflow from the list of all workflows via output option.
        """

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY_PLAN",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY_PLAN",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_MODULE_SAFETY_PLAN", "WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="Review/Approve Contribution request",
            type="workflow",
            id="WF_RV_AP_ContrRequest",
            status="valid",
            input=["WP_CONT_REQUEST"],
            output=["WP_MODULE_SAFETY_PLAN", "WP_CONT_REQUEST"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-8-8411",
                    "R_ISOPAS8926_RQ-4431",
                    "R_ISOPAS8926_RQ-44321",
                    "R_ISOPAS8926_RQ-44322",
                    "R_ISOPAS8926_RQ-4433",
                    "R_ISOPAS8926_RQ-44341",
                    "R_ISOPAS8926_RQ-44342",
                ]
            },
            docname=None,
            lineno=None,
        )

        needs = {need_1["id"]: need_1, need_2["id"]: need_2}

        logger = fake_check_logger()

        assert (
            standards.check_workproduct_uniqueness_over_workflows(
                app, logger) is True
        )
        ids = [need_2["id"], need_3["id"]]
        workflows_str = ", ".join(f"`{id}`" for id in ids)
        logger.warning.assert_called_with(
            f"Workproduct `{need_1['id']}` is contained in {
                2} workflows: {workflows_str}, which is incorrect. \n",
            location=ANY,
        )

    def test_my_pie_linked_standard_requirements(self):
        """
        Simulate results  for my_pie_linked_standard_requirements function and check if the result parameter after calling this function a special case will give the correct value.
        """
        needs = {}

        need_1 = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="R_ISO26262_RQ-8-6432",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Traceability",
            id="R_ISO26262_RQ-8-0000",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-gd": ["R_ISO26262_RQ-8-6432", "R_ISO26262_RQ-8-6422"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        needs[need_1["id"]] = need_1
        needs[need_2["id"]] = need_2
        needs[need_3["id"]] = need_3

        # Initialize results
        results = []

        # Call the function
        standards.my_pie_linked_standard_requirements(needs, results)

        # Check that results are [1, 1]
        assert results == [1, 1], (
            f"For function my_pie_linked_standard_requirements expected [1, 1] but got {
                results}"
        )

    def test_my_pie_linked_standard_workproducts(self):
        """
        Simulate results  for test_my_pie_linked_standard_workproducts function and check if the result parameter after calling this function with a special case will give the correct value.
        """
        needs = {}

        need_1 = NeedsInfoType(
            target_id="Organization-specific rules and processes for functional safety",
            id="R_ISO26262_WP-2-551",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="specific rules for processes",
            id="R_ISO26262_WP-2-0000",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="WP_POLICIES",
            id="WP_POLICIES",
            status="draft",
            **{"compliance-wp": ["R_ISO26262_WP-2-551", "R_ISO21434_WP-05-01"]},
            docname=None,
            lineno=None,
        )

        needs[need_1["id"]] = need_1
        needs[need_2["id"]] = need_2
        needs[need_3["id"]] = need_3

        # Initialize results
        results = []

        # Call the function
        standards.my_pie_linked_standard_workproducts(needs, results)

        # Check that results are [1, 1]
        assert results == [1, 1], (
            f"For function my_pie_linked_standard_workproducts expected [1, 1] but got {
                results}"
        )

    def test_my_pie_workproducts_contained_in_exactly_one_workflow(self):
        """
        Simulate results  for test_my_pie_workproducts_contained_in_exactly_one_workflow function and check if the result parameter after calling this function with a special case will give the correct value.
        """
        needs = {}

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY_PLAN",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY_PLAN",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_MODULE_SAFETY_PLAN", "WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_3 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_4 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_5 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_MODULE_SAFETY", "WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_6 = NeedsInfoType(
            target_id="Review/Approve Contribution request",
            type="workflow",
            id="WF_RV_AP_ContrRequest",
            status="valid",
            input=["WP_CONT_REQUEST"],
            output=["WP_MODULE_SAFETY", "WP_CONT_REQUEST"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-8-8411",
                    "R_ISOPAS8926_RQ-4431",
                    "R_ISOPAS8926_RQ-44321",
                    "R_ISOPAS8926_RQ-44322",
                    "R_ISOPAS8926_RQ-4433",
                    "R_ISOPAS8926_RQ-44341",
                    "R_ISOPAS8926_RQ-44342",
                ]
            },
            docname=None,
            lineno=None,
        )

        needs[need_1["id"]] = need_1
        needs[need_2["id"]] = need_2
        needs[need_3["id"]] = need_3
        needs[need_4["id"]] = need_4
        needs[need_5["id"]] = need_5
        needs[need_6["id"]] = need_6

        # Initialize results
        results = []

        # Call the function
        standards.my_pie_workproducts_contained_in_exactly_one_workflow(
            needs, results)

        # Check that results are [1, 1]
        assert results == [1, 1, 1], (
            f"For function my_pie_workproducts_contained_in_exactly_one_workflow expected [1, 1, 1] but got {
                results}"
        )

    def test_get_standards_needs(self):
        """
        Test if get_standards_needs works as expected with a positive and negative test.
        """
        app = MagicMock()
        app.env = MagicMock()

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="Traceability of safety requirements",
            id="R_ISO26262_RQ-8-6432",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Traceability of requirements",
            id="R_11111111",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        app.env.needs_all_needs = {}
        app.env.needs_all_needs[need_1["id"]] = need_1
        app.env.needs_all_needs[need_2["id"]] = need_2
        needs = app.env.needs_all_needs
        result = standards.get_standards_needs(needs)

        assert need_1 in result.values()
        assert need_2 not in result.values()

    def test_get_standards_workproducts(self):
        """
        Test if get_standards_workproducts works as expected with a positive and negative test.
        """
        app = MagicMock()
        app.env = MagicMock()

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="Organization-specific rules and processes for functional safety",
            id="R_ISO26262_WP-2-551",
            status="valid",
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Traceability of requirements",
            id="R_11111111",
            reqtype="Functional",
            status="valid",
            docname=None,
            lineno=None,
        )

        app.env.needs_all_needs = {}
        app.env.needs_all_needs[need_1["id"]] = need_1
        app.env.needs_all_needs[need_2["id"]] = need_2
        needs = app.env.needs_all_needs
        result = standards.get_standards_workproducts(needs)

        assert need_1 in result.values()
        assert need_2 not in result.values()

    def test_get_compliance_gd_needs(self):
        """
        Test if get_compliance_gd_needs works as expected with a positive and negative test.
        """
        app = MagicMock()
        app.env = MagicMock()

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-wp": ["R_ISO26262_RQ-8-6666", "R_ISO26262_RQ-8-6777"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-gd": ["R_ISO26262_WP-2-551", "R_ISO21434_WP-05-01"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        app.env.needs_all_needs = {}
        app.env.needs_all_needs[need_1["id"]] = need_1
        app.env.needs_all_needs[need_2["id"]] = need_2
        needs = app.env.needs_all_needs
        result = standards.get_compliance_gd_needs(needs)

        assert need_1.get("compliance-wp", [])[0] not in result
        assert need_2.get("compliance-gd", [])[0] in result

    def test_get_compliance_wp_needs(self):
        """
        Test if get_compliance_wp_needs works as expected with a positive and negative test.
        """
        app = MagicMock()
        app.env = MagicMock()

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-gd": ["R_ISO26262_RQ-8-6432", "R_ISO26262_RQ-8-6422"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Requirements attribute satisfies",
            id="GD_REQ__attribute_satisfies",
            tags="attribute",
            security="NO",
            **{"compliance-wp": ["R_ISO26262_RQ-8-6666", "R_ISO26262_RQ-8-6777"]},
            status="valid",
            satisfies=[
                "GD__create_maintain_requirements",
            ],
            docname=None,
            lineno=None,
        )

        app.env.needs_all_needs = {}
        app.env.needs_all_needs[need_1["id"]] = need_1
        app.env.needs_all_needs[need_2["id"]] = need_2
        needs = app.env.needs_all_needs
        result = standards.get_compliance_wp_needs(needs)

        assert need_1.get("compliance-gd", [])[0] not in result
        assert need_2.get("compliance-wp", [])[0] in result

    def test_get_workflows(self):
        """
        Test if get_workflows works as expected with a positive and negative test.
        """
        app = MagicMock()
        app.env = MagicMock()

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY_PLAN",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY_PLAN",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_MODULE_SAFETY_PLAN", "WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        app.env.needs_all_needs = {}
        app.env.needs_all_needs[need_1["id"]] = need_1
        app.env.needs_all_needs[need_2["id"]] = need_2
        needs = app.env.needs_all_needs
        result = standards.get_workflows(needs)

        assert need_1 not in result.values()
        assert need_2 in result.values()

    def test_get_workproducts(self):
        """
        Test if get_workproducts works as expected with a positive and negative test.
        """
        app = MagicMock()
        app.env = MagicMock()

        logger = MagicMock(spec=SphinxLoggerAdapter)
        logger.warning = MagicMock()

        need_1 = NeedsInfoType(
            target_id="Module Safety Plan",
            type="workproduct",
            id="WP_MODULE_SAFETY_PLAN",
            status="valid",
            **{
                "compliance-wp": [
                    "R_ISO26262_WP-2-653",
                    "R_ISO26262_WP-8-853",
                    "R_ISO26262_WP-8-1251",
                    "R_ISO26262_WP-8-1252",
                ]
            },
            docname=None,
            lineno=None,
        )

        need_2 = NeedsInfoType(
            target_id="Create/Maintain Safety Plan",
            type="workflow",
            id="WF_CR_MT_SAFETY_PLAN",
            status="draft",
            input=["WP_PLATFORM_MGMT", "WP_ISSUE_TRACK_SYSTEM"],
            output=["WP_MODULE_SAFETY_PLAN", "WP_PLATFORM_SAFETY_PLAN"],
            **{
                "compliance-wf": [
                    "R_ISO26262_RQ-2-6461",
                    "R_ISO26262_RQ-2-6462",
                    "R_ISO26262_RQ-2-6463",
                    "R_ISO26262_RQ-2-6465",
                    "R_ISO26262_RQ-2-6468",
                ]
            },
            docname=None,
            lineno=None,
        )

        app.env.needs_all_needs = {}
        app.env.needs_all_needs[need_1["id"]] = need_1
        app.env.needs_all_needs[need_2["id"]] = need_2
        needs = app.env.needs_all_needs
        result = standards.get_workproducts(needs)

        assert need_1 in result.values()
        assert need_2 not in result.values()
