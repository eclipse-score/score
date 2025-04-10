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

from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx_needs.data import SphinxNeedsData
from sphinx_needs.logging import get_logger

from score_source_code_linker.parse_source_files import GITHUB_BASE_URL

LOGGER = get_logger(__name__)


def setup(app: Sphinx) -> dict[str, str | bool]:
    app.add_config_value("source_code_linker_file", "", rebuild="env")
    if app.config.source_code_linker_file:
        LOGGER.info("Loading source code linker...", type="score_source_code_linker")
        app.connect("env-updated", add_source_link)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


# req-Id: gd_req__req__attr_impl
def add_source_link(app: Sphinx, env: BuildEnvironment) -> None:
    """
    'Main' function that facilitates the running of all other functions
    in correct order.
    This function is also 'connected' to the message Sphinx emits,
    therefore the one that's called directly.
    Args:
        env: Buildenvironment, this is filled automatically
        app: Sphinx app application, this is filled automatically
    """
    Needs_Data = SphinxNeedsData(env)
    needs = Needs_Data.get_needs_mutable()
    needs_copy = deepcopy(needs)
    json_paths = [app.config.source_code_linker_file]
    for path in json_paths:
        try:
            with open(path) as f:
                gh_json = json.load(f)
            for id, link in gh_json.items():
                id = id.strip()
                try:
                    # NOTE: Removing & adding the need is important to make sure
                    # the needs gets 're-evaluated'.
                    need = needs_copy[id]  # NeedsInfoType
                    Needs_Data.remove_need(need["id"])
                    # extra_options are only available at runtime
                    need["source_code_link"] = ",".join(link)  # type: ignore
                    Needs_Data.add_need(need)
                except KeyError:
                    # NOTE: manipulating link to remove git-hash,
                    # making the output file location more readable
                    files = [
                        x.replace(GITHUB_BASE_URL, "").split("/", 1)[-1] for x in link
                    ]
                    LOGGER.warning(
                        f"Could not find {id} in the needs id's. "
                        f"Found in file(s): {files}",
                        type="score_source_code_linker",
                    )
        except Exception as e:
            LOGGER.warning(
                f"An unexpected error occurred while adding source_code_links to needs."
                f"Error: {e}",
                type="score_source_code_linker",
            )
            LOGGER.warning(
                f"Reading file: {path} right now", type="score_source_code_linker"
            )
