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
from unittest.mock import MagicMock

from sphinx.util.logging import SphinxLoggerAdapter

from docs._tooling.extensions.score_metamodel import CheckLogger, NeedsInfoType


def fake_check_logger():
    """Creates a CheckLogger with a mocked backend."""

    LOGGER = MagicMock(spec=SphinxLoggerAdapter)
    LOGGER.warning = MagicMock()
    return CheckLogger(LOGGER)


def need(**kwargs):
    """Convinience function to create a NeedsInfoType object with some defaults."""

    kwargs.setdefault("id", "test_need")
    kwargs.setdefault("docname", "docname")
    kwargs.setdefault("doctype", "rst")
    kwargs.setdefault("lineno", "42")

    return NeedsInfoType(**kwargs)


def verify_log_string(logger: CheckLogger, expected_substring, expect_location=True):
    """
    Assert that the logger was called exactly once with a message containing a specific substring.

    This also verifies that the defaults from need() are used correctly.
    So you must use need() to create the need object that is passed to the checks.
    """
    logger._log.warning.assert_called_once()

    # Retrieve the call arguments
    args, kwargs = logger._log.warning.call_args
    log_message = args[0]

    assert expected_substring in log_message, f"Expected substring '{
            expected_substring}' not found in log message: '{log_message}'"

    assert kwargs["type"] == "score_metamodel"

    if expect_location:
        assert kwargs["location"] == "docname.rst:42"
