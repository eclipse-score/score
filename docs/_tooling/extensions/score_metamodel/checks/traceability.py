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
from sphinx.application import Sphinx
from sphinx_needs.data import NeedsInfoType

from score_metamodel import CheckLogger, graph_check


@graph_check
def check_linkage_parent(app: Sphinx, needs: list[NeedsInfoType], log: CheckLogger):
    """
    Checking if all linked parent requirements have status valid.
    """
    # Convert list to dictionary for easy lookup
    needs_dict = {need["id"]: need for need in needs}

    for need in needs:
        parents_not_correct = []
        for satisfie_need in need.get("satisfies", []):
            if needs_dict.get(satisfie_need, {}).get("status") != "valid":
                parents_not_correct.append(satisfie_need)

        if parents_not_correct:
            formatted_parents_not_correct = ", ".join(
                f"`{parent}`" for parent in parents_not_correct
            )
            msg = f"has a parent requirement(s): {formatted_parents_not_correct} with an invalid status."
            log.warning_for_need(need, msg)


@graph_check
def check_linkage_safety(app: Sphinx, needs: list[NeedsInfoType], log: CheckLogger):
    """
    Checking if for feature, component and tool requirements it shall be checked if at least one parent requirement
    contains the same or lower ASIL compared to the ASIL of the current requirement then it will return False.
    """
    # Convert list to dictionary for easy lookup
    needs_dict = {need["id"]: need for need in needs}

    for need in needs:
        allowed_values = ["QM"]
        parents_have_safety = False

        if need["safety"] == "QM":
            return
        elif need["safety"] == "ASIL_B":
            for satisfie_need in need.get("satisfies", []):
                safety = needs_dict.get(satisfie_need, {}).get(
                    "safety"
                )  # Lookup parent need safely
                allowed_values = ["ASIL_B", "ASIL_D"]
                if safety:
                    parents_have_safety = True
                if safety in ["ASIL_B", "ASIL_D"]:
                    continue
        elif need["safety"] == "ASIL_D":
            for satisfie_need in need.get("satisfies", []):
                safety = needs_dict.get(satisfie_need, {}).get(
                    "safety"
                )  # Lookup parent need safely
                if safety:
                    parents_have_safety = True
                allowed_values = ["ASIL_D"]
                if safety == "ASIL_D":
                    continue

        # Checking if the requirement has satisfies field before logging
        if need.get("satisfies") and parents_have_safety:
            msg = (
                f"with `{need['safety']}` has no parent requirement that contains the same or lower ASIL. "
                f"Allowed ASIL values: {', '.join(f'`{value}`' for value in allowed_values)}. \n"
            )
            log.warning_for_need(need, msg)


@graph_check
def check_linkage_status(app: Sphinx, needs: list[NeedsInfoType], log: CheckLogger):
    """
    Checking if for valid feature, component and tool requirements it shall be checked if the status of the parent requirement is also valid.
    """
    needs_dict = {need["id"]: need for need in needs}

    for need in needs:
        if need["status"] == "valid":
            for satisfie_need in need.get("satisfies", []):
                parent_need = needs_dict.get(satisfie_need)  # Get parent requirement

                if not parent_need or parent_need.get("status") != "valid":
                    msg = f"has a valid status but one of its parents: `{satisfie_need}` has an invalid status. \n"
                    log.warning_for_need(need, msg)
