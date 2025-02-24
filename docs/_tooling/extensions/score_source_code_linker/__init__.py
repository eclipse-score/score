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
import json
from copy import deepcopy
from score_source_code_linker.parse_source_files import GITHUB_BASE_URL
from sphinx.application import Sphinx
from sphinx_needs.data import SphinxNeedsData
from sphinx_needs.logging import get_logger

LOGGER = get_logger(__name__)


def setup(app: Sphinx) -> dict:
    """
    Setup function needed to identify this file as a Sphinx-Extension

    Args:
        app: Sphinx app of the current running application. Populated automatically.

    Returns:
        (dict):
            Return extension metadata.

            {
                "version": "0.1",
                "parallel_read_safe": True,
                "parallel_write_safe": True,
            }
    """
    app.connect("env-updated", add_source_link)
    app.add_config_value("source_code_linker_file", "", rebuild="env")
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def find_dir_paths(app: Sphinx) -> list[str]:
    """
    Reading 'requirement_links' config value and returning it as list
    The 'requirement_links' config value contains all source links found that need to be parsed.
    Args:
        app: Sphinx app of the current running application

    Returns:
        (list[str]):
                List of filenames as strings captured from the 'requirement_links' configuration value.

        Example:
            [file-1, file-2]
    """
    return [app.config.source_code_linker_file]


def add_source_link(app: Sphinx, env) -> None:
    """
    'Main' function that facilitates the running of all other functions in correct order.
    This function is also 'connected' to the message Sphinx emits, therefore the one that's called directly.
    Args:
        env: Buildenvironment, this is filled automatically
        app: Sphinx app application, this is filled automatically
    """
    Needs_Data = SphinxNeedsData(env)
    needs = Needs_Data.get_needs_mutable()
    needs_copy = deepcopy(needs)
    json_paths = find_dir_paths(app)
    for path in json_paths:
        try:
            with open(path) as f:
                gh_json = json.load(f)
            for id, link in gh_json.items():
                id = id.strip()
                try:
                    # NOTE: Removing & ading the need is important to make sure the needs gets 're-evaluated'.
                    need = needs_copy[id]  # NeedsInfoType
                    Needs_Data.remove_need(need["id"])
                    need["source_code_link"] = ",".join(link)
                    Needs_Data.add_need(need)
                except KeyError:
                    # NOTE: manipulating link to remove git-hash, making the output file location more readable
                    LOGGER.warning(
                        f"Could not find {id} in the needs id's. Found in file(s): {[x.replace(GITHUB_BASE_URL, "").split("/",1)[-1] for x in link]}",
                        type="score_source_code_linker",
                    )
        except Exception as e:
            LOGGER.warning(
                f"An unexpected error occured while adding source_code_links to needs. Error: {e}",
                type="score_source_code_linker",
            )
            LOGGER.warning(
                f"Reading file: {path} right now", type="score_source_code_linker"
            )
