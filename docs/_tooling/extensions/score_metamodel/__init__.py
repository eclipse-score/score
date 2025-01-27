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
import importlib
import pkgutil
from typing import Callable

from sphinx.application import Sphinx
from sphinx_needs import logging
from sphinx_needs.data import NeedsInfoType, SphinxNeedsData

from . import metamodel
from .log import CheckLogger

logger = logging.get_logger(__name__)

local_checks: list[Callable[[NeedsInfoType, CheckLogger], None]] = []
graph_checks: list[Callable[[dict[str, NeedsInfoType], CheckLogger], None]] = []


def discover_checks():
    """
    Dynamically import all checks.
    They will self-register with the decorators below.
    """

    package_name = ".checks"  # load ./checks/*.py
    package = importlib.import_module(package_name, __package__)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        logger.debug(f"Importing check module: {module_name}")
        importlib.import_module(f"{package_name}.{module_name}", __package__)


def local_check(func: Callable[[NeedsInfoType, CheckLogger], None]):
    """Use this decorator to mark a function as a local check."""
    logger.debug(f"new local_check: {func}")
    local_checks.append(func)
    return func


def graph_check(func: Callable[[dict[str, NeedsInfoType], CheckLogger], None]):
    """Use this decorator to mark a function as a graph check."""
    logger.debug(f"new graph_check: {func}")
    graph_checks.append(func)
    return func


def _run_checks(app: Sphinx, exception: Exception | None) -> None:
    # Do not run checks if an exception occurred during build
    if exception:
        return

    needs_all_needs = SphinxNeedsData(app.env).get_needs_view()

    logger.debug(f"Running checks for {len(needs_all_needs)} needs")

    log = CheckLogger(logger)

    # Need-Local checks: checks which can be checked file-local, without a
    # graph of other needs.
    for need in needs_all_needs.values():
        for check in local_checks:
            check(need, log)

    # Graph-Based checks: These warnings require a graph of all other needs to
    # be checked.
    needs = needs_all_needs.values()
    for check in graph_checks:
        check(needs, log)

    if log.has_warnings:
        log.warning("Some needs have issues. See the log for more information.")
        # TODO: exit code


def setup(app: Sphinx):
    app.config.needs_id_required = True
    app.config.needs_id_regex = "^[A-Za-z0-9_-]{6,}"
    app.config.needs_types = metamodel.needs_types
    app.config.needs_extra_links = metamodel.needs_extra_links
    app.config.needs_extra_options = metamodel.needs_extra_options

    discover_checks()

    app.connect("build-finished", _run_checks)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
