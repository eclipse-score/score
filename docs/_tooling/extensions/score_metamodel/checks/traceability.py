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
from sphinx_needs.data import NeedsInfoType

from docs._tooling.extensions.score_metamodel import (
    CheckLogger,
    NeedsInfoType,
    graph_check,
)
from docs._tooling.extensions.score_metamodel.checks.util import check_option


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_status
@graph_check
def check_linkage_parent(needs: dict[str, NeedsInfoType], log: CheckLogger) -> bool:
    """
    Checking if all links to parent requirements are valid then return False.
    """
    parents_not_correct = []

    for need in needs.values():
        for satisfie_need in need["satisfies"]:
            if needs.get(satisfie_need, {}).get("status") != "valid":
                parents_not_correct.append(satisfie_need)

        if parents_not_correct:
            for parent in parents_not_correct:
                msg = f"Need: {need['id']} have invalid status of parent requirement: {parent} \n"
                log.warning_for_option(need, "satisfies", msg)


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_safety_check
@graph_check
def check_linkage_safety(needs: dict[str, NeedsInfoType], log: CheckLogger) -> bool:
    """
    Checking if for feature, component and tool requirements it shall be checked if at least one parent requirement contains the same or lower ASIL compared to the ASIL of the current requirement then it will return False.
    """
    for need in needs.values():
        if need["id"].startswith("TOOL_REQ") or need["id"].startswith(
            "GD"
        ):  ##TO REMOVE. when safety is defined for TOOL_REQ requirements
            continue  ##TO REMOVE. when safety is defined for TOOL_REQ requirements

        allowed_values = ["QM"]

        if need["safety"] == "QM":
            continue
        elif need["safety"] == "ASIL_B":
            for satisfie_need in need["satisfies"]:
                status = needs.get(satisfie_need, {}).get("safety")
                allowed_values = ["ASIL_B", "ASIL_D"]
                if status in ["ASIL_B", "ASIL_D"]:
                    continue
        elif need["safety"] == "ASIL_D":
            for satisfie_need in need["satisfies"]:
                status = needs.get(satisfie_need, {}).get("safety")
                allowed_values = ["ASIL_D"]
                if status == "ASIL_D":
                    continue

        # checking if the requirememt is stakeholder so we need to skip the check as it doesn't have a satisfies field
        if need["satisfies"]:
            msg = f"Need: `{need['id']}` with `{need['safety']}` has no parent requirement that contains the same or lower ASIL. Alloed ASIL values: {', '.join(f"'{value}'" for value in allowed_values)}. \n"
            log.warning_for_option(need, "satisfies", msg)


# req-traceability: TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_status_check
@graph_check
def check_linkage_status(needs: dict[str, NeedsInfoType], log: CheckLogger) -> bool:
    """
    Checking if for valid feature, component and tool requirements it shall be checked if the status of the parent requirement is also valid then it will retun False.
    """
    for need in needs.values():
        if need["status"] == "valid":
            for satisfie_need in need["satisfies"]:
                if needs.get(satisfie_need, {}).get("status") != "valid":
                    msg = f"Need: `{need['id']}` have a valid status but one of it's parents: `{satisfie_need}` have an invalid status. \n"
                    log.warning_for_option(need, "satisfies", msg)
