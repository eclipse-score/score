# *******************************************************************************
# Copyright (c) 2024 Contributors to the Eclipse Foundation
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

from sphinx.util.logging import SphinxLoggerAdapter
from docs._tooling.sphinx_extensions.sphinx_extensions.utils.util import (
    log_custom_warning,
)
from sphinx_needs.data import NeedsInfoType


# req-Id: TOOL_REQ__toolchain_sphinx_needs_build__requirement_attributes_uid
def check_id_title_part(need: NeedsInfoType, log: SphinxLoggerAdapter) -> bool:
    """
    Checking if the title is included in the requirement id or not.
    ---
    Returns 'True' if  the prefix is not correct
    """
    # Filter out types that should not be checked
    if not (
        (need["type"].endswith("_req") and not need["type"].endswith("gd_req"))
        or need["type"].endswith("aou")
    ):
        return False

    # Comment out stakeholder check for now
    if need["type"].startswith("stkh_req"):
        return False

    # Accept new ID Format
    if need["id"].endswith("_[0-9a-zA-Z]{8,8}"):
        return False

    # Split the string by underscores
    parts = need["id"].split("__")

    # Ensure we have at least 3 parts (after first two underscores)
    if len(parts) < 3:
        msg = f"\n Need: `{need['id']}` incorrect 'id'\n expected ID consisting of 3 substrings '<Req Type>__<Directory Tree>__<Title>'\n"
        log_custom_warning(need, log, msg)
        return True

    # Get the part of the string after the first two underscores: the path
    directory_tree = parts[1]
    path = os.path.dirname(need["docname"])
    path = path.replace("/", "_")
    path = path.replace("-", "_")

    if need["type"].startswith("feat_req") or need["type"].startswith("tool_req"):
        path = path.replace("features_", "")
        path = path.replace("_docs_requirements", "")
        path = path.replace("_requirements", "")

    if need["type"].startswith("comp_req"):
        path = path.replace("modules_", "")
        path = path.replace("dependix_json_al~", "json_al")
        path = path.replace("dependix_kvstorage~", "kvstorage")

    if need["type"].startswith("aou"):
        path = path.replace("modules_", "")
        path = path.replace("_docs_manual", "")
        path = path.replace("_docs", "")
        path = path.replace("dependix_json_al~", "json_al")

    if directory_tree != path:
        msg = f"\n Need: {need['id']} incorrect 'id': '\n expected {path}\n {os.path.dirname(need["docname"])}. \n ID should consist of: '<Title>'\n"
        log_custom_warning(need, log, msg)
        return True

    # Get the part of the string after the first two underscores: the title
    title = parts[2]

    # Check if the substring consists only of lowercase letters and underscores
    if not all(char.islower() or char == "_" for char in title):
        msg = f"\n Need: {need['id']} incorrect 'id': '<Title>' not composed from snake case\n expected:{title}. \n ID should consist of: '<Title>'\n"
        log_custom_warning(need, log, msg)
        return True

    title = title.replace("_", " ")
    if title != need["title"].lower():
        msg = f"\n Need: `{need['id']}` has an incorrect 'id':\n expected {need["title"].lower()}\n"
        log_custom_warning(need, log, msg)
        return True

    return False
