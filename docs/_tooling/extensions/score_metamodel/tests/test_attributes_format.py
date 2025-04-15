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

from docs._tooling.extensions.score_metamodel.checks.attributes_format import (
    check_description,
    check_id_format,
    check_id_length,
    check_title,
)
from docs._tooling.extensions.score_metamodel.tests import fake_check_logger, need


class TestId:
    STOP_WORDS = ["shall", "must", "will"]
    WEAK_WORDS = ["just", "that", "about", "really", "some", "thing", "absolutely"]

    def test_check_id_format_positive(self):
        """
        Test check_id_length function with a positive case.
        """

        need_1 = need(
            id="gd_req__attribute_satisfies",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)

        check_id_format(app, need_1, logger)
        assert not logger.has_warnings

    def test_check_id_format_two_mendatory_substrings_parts_negative(self):
        """
        Test check_id_length function with a negative case.
        """

        need_1 = need(
            id="gd_req_attribute_satisfies",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)

        check_id_format(app, need_1, logger)

        logger.assert_warning(
            "expected to consisting of one of these 2 formats:"
            "`<Req Type>__<Abbreviations>` or "
            "`<Req Type>__<Abbreviations>__<Architectural Element>`.",
            expect_location=False,
        )

    def test_check_id_format_three_mendatory_substrings_parts_negative(self):
        """
        Test check_id_length function with a negative case.
        """

        need_1 = need(
            id="feat_req__1",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)

        check_id_format(app, need_1, logger)

        logger.assert_warning(
            "expected to consisting of this format: "
            "`<Req Type>__<Abbreviations>__<Architectural Element>`.",
            expect_location=False,
        )

    def test_check_id_length_positive(self):
        """
        Test check_id_length function with a positive case.
        """

        need_1 = need(
            id="std_req__iso26262__rq_8_6432",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)

        check_id_length(app, need_1, logger)
        assert not logger.has_warnings

    def test_check_id_length_negative(self):
        """
        Test check_id_length function with a negative case.
        """

        need_1 = need(
            id="std_req__iso26262__rq_8_6432_0000000000000000000000",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)

        check_id_length(app, need_1, logger)
        logger.assert_warning(
            f"exceeds the maximum allowed length of 45 characters "
            f"(current length: {len(need_1["id"])}).",
            expect_location=False,
        )

    def test_check_title_positive(self):
        need_1 = need(
            id="std_req__iso26262__rq_8_6432",
            title="std_req  iso26262",
            type="feat_req",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.stop_words = self.STOP_WORDS

        check_title(app, need_1, logger)
        assert not logger.has_warnings

    def test_check_title_negative(self):
        """
        Test check_title function with a negative case.
        """

        need_1 = need(
            id="gd_req__doc_shall_approver",
            title="gd_req doc shall approver",
            type="feat_req",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.stop_words = self.STOP_WORDS

        check_title(app, need_1, logger)
        logger.assert_warning(
            (
                "contains a stop word: `shall`. The title is meant to provide a short "
                "summary, not to repeat the requirement statement. Please revise "
                "the title for clarity and brevity."
            ),
            expect_location=False,
        )

    def test_check_description_positive(self):
        need_1 = need(
            id="std_req__iso26262__rq_8_6432",
            content="This is the description of the requirement",
            type="feat_req",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.weak_words = self.WEAK_WORDS

        check_description(app, need_1, logger)
        assert not logger.has_warnings

    def test_check_description_negative(self):
        """
        Test check_description function with a negative case.
        """

        need_1 = need(
            id="gd_req__doc_shall_approver",
            content="This is just the description of the requirement",
            type="feat_req",
        )

        logger = fake_check_logger()
        app = Mock(spec=Sphinx)
        app.config = Mock()
        app.config.weak_words = self.WEAK_WORDS

        check_description(app, need_1, logger)
        logger.assert_warning(
            "contains a weak word: `just`. Please revise the description.",
            expect_location=False,
        )
