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
from sphinx.util.logging import SphinxLoggerAdapter
from docs._tooling.sphinx_extensions.sphinx_extensions.utils.util import (
    check_option,
    log_custom_warning,
)
from sphinx_needs.data import NeedsInfoType

all_needs = {}


def get_all_needs(need: NeedsInfoType, log: SphinxLoggerAdapter) -> bool:
    """
    Collecting all requirement values to use it in other functions.
    """
    if need["id"] not in all_needs:
        all_needs[need["id"]] = need
    return False


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_status
def check_linkage_parent(need: NeedsInfoType, log: SphinxLoggerAdapter) -> bool:
    """
    Checking if all links to parent requirements are valid then return False.
    """
    global all_needs
    parents_not_correct = []

    for satisfie_need in need["satisfies"]:
        if all_needs.get(satisfie_need, {}).get("status") != "valid":
            parents_not_correct.append(satisfie_need)

    if parents_not_correct:
        for parent in parents_not_correct:
            msg = f"Need: {need["id"]} have invalid status of parent requirement: {parent} \n"
            log_custom_warning(need, log, msg)
        return True

    return False


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_safety_check
def check_linkage_safety(need: NeedsInfoType, log: SphinxLoggerAdapter) -> bool:
    """
    Checking if for feature, component and tool requirements it shall be checked if at least one parent requirement contains the same or lower ASIL compared to the ASIL of the current requirement then it will return False.
    """
    global all_needs
    if need["id"].startswith("TOOL_REQ") or need["id"].startswith(
        "GD"
    ):  ##TO REMOVE. when safety is defined for TOOL_REQ requirements
        return False  ##TO REMOVE. when safety is defined for TOOL_REQ requirements

    allowed_values = ["QM"]

    if need["safety"] == "QM":
        return False
    elif need["safety"] == "ASIL_B":
        for satisfie_need in need["satisfies"]:
            status = all_needs.get(satisfie_need, {}).get("safety")
            allowed_values = ["ASIL_B", "ASIL_D"]
            if status in ["ASIL_B", "ASIL_D"]:
                return False
    elif need["safety"] == "ASIL_D":
        for satisfie_need in need["satisfies"]:
            status = all_needs.get(satisfie_need, {}).get("safety")
            allowed_values = ["ASIL_D"]
            if status == "ASIL_D":
                return False

    # checking if the requirememt is stakeholder so we need to skip the check as it doesn't have a satisfies field
    if need["satisfies"]:
        msg = f"Need: `{need['id']}` with `{need['safety']}` has no parent requirement that contains the same or lower ASIL. Alloed ASIL values: {', '.join(f'\'{value}\'' for value in allowed_values)}. \n"
        log_custom_warning(need, log, msg)
        return True
    else:
        return False


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_status_check
def check_linkage_status(need: NeedsInfoType, log: SphinxLoggerAdapter) -> bool:
    """
    Checking if for valid feature, component and tool requirements it shall be checked if the status of the parent requirement is also valid then it will retun False.
    """
    global all_needs
    if need["status"] == "valid":
        for satisfie_need in need["satisfies"]:
            if all_needs.get(satisfie_need, {}).get("status") != "valid":
                msg = f"Need: `{need["id"]}` have a valid status but one of it's parents: `{satisfie_need}` have an invalid status. \n"
                log_custom_warning(need, log, msg)
                return True

    return False


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_attributes_uid
def check_g_reqid_traceability(need: NeedsInfoType, log: SphinxLoggerAdapter) -> bool:
    """
    Checking if all described and wanted attributes and restrictions in 'G_Req_Traceability' are followed and adhered to.
    Returns 'True' if guidance has not been followed.
    """

    ## Actual checking logic.
    if need["type"] == "stkh_req" and need["satisfies"] != []:
        msg = "option 'satisfies' not allowed in 'stkh_req' directives."
        log_custom_warning(need, log, msg)
        return True
    if need["type"] in ["feat_req", "comp_req", "tool_req"]:
        msg = f"option 'satisfies' missing in {need['id']}. satisfies is requiered in `feat_req, comp_req, tool_req` directives."
        if check_option(
            need=need, option="satisfies", log=log, msg=msg, allow_empty=False
        ):
            return True
    return False
