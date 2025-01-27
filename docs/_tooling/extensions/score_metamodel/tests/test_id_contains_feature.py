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
import os
import sys

from score_metamodel import CheckLogger, NeedsInfoType
from score_metamodel.checks.id_contains_feature import id_contains_feature
from score_metamodel.tests import fake_check_logger, need, verify_log_string

sys.path.insert(0, os.path.abspath("../.."))


def test_feature_ok():
    logger = fake_check_logger()

    id_contains_feature(
        need(id="Req__feature17__Title", docname="path/to/feature17/index"), logger
    )
    logger._log.warning.assert_not_called()


def test_feature_not_ok():
    logger = fake_check_logger()

    id_contains_feature(
        need(id="Req__feature17__Title", docname="path/to/feature15/index"), logger
    )
    verify_log_string(logger, "feature15", expect_location=False)
