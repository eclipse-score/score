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

from score_metamodel.checks.id_contains_feature import id_contains_feature
from score_metamodel.tests import fake_check_logger, need


def test_feature_ok():
    logger = fake_check_logger()
    app = Mock(spec=Sphinx)

    id_contains_feature(
        app, need(id="req__feature17__title", docname="path/to/feature17/index"), logger
    )
    logger._log.warning.assert_not_called()  # type: ignore


def test_feature_not_ok():
    logger = fake_check_logger()
    app = Mock(spec=Sphinx)

    id_contains_feature(
        app, need(id="req__feature17__title", docname="path/to/feature15/index"), logger
    )
    logger.assert_warning("feature15", expect_location=False)
