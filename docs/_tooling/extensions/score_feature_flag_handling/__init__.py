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
from pprint import pprint
from sphinx.application import Sphinx
from sphinx_needs.data import SphinxNeedsData
from sphinx_needs.config import NeedsSphinxConfig
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
from .filter_overwrite import wrap_filter_common
import os
import json


logger = logging.getLogger(__name__)


def read_filter_tags(app: Sphinx) -> list:
    """
    Helper function to read in the 'filter_tags' provided by `feature_flag.bzl`.

    Args:
        app: The current running Sphinx-Build application

    Returns:
       - List of tags e.g. ['some-ip','another-tag']

    Errors:
        - If 'filter_tags_file_path' can't be found in the config
        - If something goes wrong when reading the file
    """
    # asserting our worldview
    assert hasattr(
        app.config, "filter_tags_file_path"
    ), "Config missing filter_tags_file_path, this is mandatory."
    filter_file = app.config.filter_tags_file_path
    logger.debug(f"Found the following filter_tags_file_path: {filter_file}")
    try:
        with open(filter_file, "r") as f:
            content = f.read().strip()
            filter_tags = [tag.strip() for tag in content.split(",")] if content else []
            logger.debug(f"found: {len(filter_tags)} filter tag.")
            logger.debug(f"filter tags found: {filter_tags}")
            return filter_tags
    except Exception as e:
        logger.error(f"could not read file: {filter_file}. Error: {e}")
        raise e


def hide_needs(app: Sphinx, env: BuildEnvironment) -> None:
    """
    Function that hides needs (requirements) if *all* of their tags are in the specified tags to hide.
    Also deletes any references to hidden requirements, e.g. in 'satisfies' option.

    Args:
        app: The current running Sphinx-Build application, this will be supplied automatically
        env: The current running BuildEnvironment, this will be supplied automatically
    """
    filter_tags = read_filter_tags(app)

    # Early return if no work needs to be done
    if not filter_tags:
        logger.debug("filter_tags was empty, no work to be done.")
        return
    need_data = SphinxNeedsData(env)
    needs = need_data.get_needs_mutable()
    extra_links = [x["option"] for x in NeedsSphinxConfig(env.config).extra_links]
    rm_needs = []
    for need_id, need in needs.items():
        if need["hide"]:
            rm_needs.append(need_id)
        if (
            need["tags"]
            and all(tag in filter_tags for tag in need["tags"])
            and not need["hide"]
        ):
            rm_needs.append(need_id)
            need["hide"] = True

    needs_to_disable = set(rm_needs)

    logger.debug(f"found {len(needs_to_disable)} requirements to be disabled.")
    logger.debug(f"requirements found: {needs_to_disable}")

    # Remove references
    for need_id in needs:
        for opt in extra_links:
            needs[need_id][opt] = [
                x for x in needs[need_id][opt] if x not in needs_to_disable
            ]
            needs[need_id][opt + "_back"] = [
                x for x in needs[need_id][opt + "_back"] if x not in needs_to_disable
            ]


def setup(app):
    logger.debug("score_feature_flag_handling extension loaded")
    app.add_config_value("filter_tags_file_path", None, "env")
    app.connect("env-updated", hide_needs)

    wrap_filter_common()
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
