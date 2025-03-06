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
from pathlib import Path
from typing import Callable

from ruamel.yaml import YAML
from sphinx.application import Sphinx
from sphinx_needs import logging
from sphinx_needs.data import NeedsInfoType, SphinxNeedsData

from .log import CheckLogger

logger = logging.get_logger(__name__)

local_checks: list[Callable[[Sphinx, NeedsInfoType, CheckLogger], None]] = []
graph_checks: list[Callable[[Sphinx, dict[str, NeedsInfoType], CheckLogger], None]] = []


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


def local_check(func: Callable[[Sphinx, NeedsInfoType, CheckLogger], None]):
    """Use this decorator to mark a function as a local check."""
    logger.debug(f"new local_check: {func}")
    local_checks.append(func)
    return func


def graph_check(func: Callable[[Sphinx, dict[str, NeedsInfoType], CheckLogger], None]):
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
            check(app, need, log)

    # Graph-Based checks: These warnings require a graph of all other needs to
    # be checked.
    needs = needs_all_needs.values()
    for check in graph_checks:
        check(app, needs, log)

    if log.has_warnings:
        log.warning("Some needs have issues. See the log for more information.")
        # TODO: exit code


def load_metamodel_data():
    """
    Load and process metamodel.yaml.

    Returns:
        dict: A dictionary with keys:
            - 'needs_types': A list of processed need types.
            - 'needs_extra_links': A list of extra link definitions.
            - 'needs_extra_options': A sorted list of all option keys.
    """
    yaml_path = Path(__file__).resolve().parent / "metamodel.yaml"

    yaml = YAML()
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.load(f)

    types_dict = data.get("needs_types", {})
    links_dict = data.get("needs_extra_links", {})
    graph_check_dict = data.get("graph_checks", {})

    global_base_options = data.get("needs_types_base_options", {})
    global_base_options_optional_opts = global_base_options.get("optional_options", {})

    # Default options by sphinx, sphinx-needs or anything else we need to account for
    default_options_list = default_options()

    # Convert "types" from {directive_name: {...}, ...} to a list of dicts
    needs_types_list = []

    all_options = set()
    for directive_name, directive_data in types_dict.items():
        # Build up a single "needs_types" item
        one_type = {
            "directive": directive_name,
            "title": directive_data.get("title", ""),
            "prefix": directive_data.get("prefix", ""),
        }

        if "color" in directive_data:
            one_type["color"] = directive_data["color"]
        if "style" in directive_data:
            one_type["style"] = directive_data["style"]

        # Store mandatory_options and optional_options directly as a dict
        mandatory_options = directive_data.get("mandatory_options", {})
        one_type["mandatory_options"] = mandatory_options

        optional_options = directive_data.get("optional_options", {})
        optional_options.update(global_base_options_optional_opts)
        one_type["opt_opt"] = optional_options

        all_options.update(list(mandatory_options.keys()))
        all_options.update(list(optional_options.keys()))

        # mandatory_links => "req_link"
        mand_links_yaml = directive_data.get("mandatory_links", {})
        if mand_links_yaml:
            one_type["req_link"] = [(k, v) for k, v in mand_links_yaml.items()]

        # optional_links => "opt_link"
        opt_links_yaml = directive_data.get("optional_links", {})
        if opt_links_yaml:
            one_type["opt_link"] = [(k, v) for k, v in opt_links_yaml.items()]

        needs_types_list.append(one_type)

    # Convert "links" dict -> list of {"option", "incoming", "outgoing"}
    needs_extra_links_list = []
    for link_option, link_data in links_dict.items():
        needs_extra_links_list.append(
            {
                "option": link_option,
                "incoming": link_data.get("incoming", ""),
                "outgoing": link_data.get("outgoing", ""),
            }
        )

    # We have to remove all 'default options' from the extra options.
    # As otherwise sphinx errors, due to an option being registered twice.
    # They are still inside the extra options we extract to enable constraint checking via regex
    needs_extra_options = sorted(all_options - set(default_options_list))

    return {
        "needs_types": needs_types_list,
        "needs_extra_links": needs_extra_links_list,
        "needs_extra_options": needs_extra_options,
        "needs_graph_check": graph_check_dict,
    }


def default_options() -> list[str]:
    "Helper function to get a list of all default options defined by sphinx, sphinx-needs etc."
    return [
        "target_id",
        "id",
        "status",
        "docname",
        "lineno",
        "type",
        "lineno_content",
        "doctype",
        "content",
        "type_name",
        "type_color",
        "type_style",
        "title",
        "full_title",
        "layout",
        "id_parent",
        "id_complete",
        "external_css",
        "sections",
        "section_name",
        "type_prefix",
        "constraints_passed",
        "collapse",
        "hide",
        "delete",
        "jinja_content",
        "is_part",
        "is_need",
        "is_external",
        "is_modified",
        "modifications",
        "has_dead_links",
        "has_forbidden_dead_links",
        "tags",
        "arch",
    ]


def setup(app: Sphinx):
    app.config.needs_id_required = True
    app.config.needs_id_regex = "^[A-Za-z0-9_-]{6,}"

    # load metamodel.yaml via ruamel.yaml
    metamodel = load_metamodel_data()

    # Assign everything to Sphinx config
    app.config.needs_types = metamodel["needs_types"]
    app.config.needs_extra_links = metamodel["needs_extra_links"]
    app.config.needs_extra_options = metamodel["needs_extra_options"]
    app.config.graph_checks = metamodel["needs_graph_check"]

    discover_checks()

    app.connect("build-finished", _run_checks)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
