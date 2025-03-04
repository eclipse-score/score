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
import operator
import re

from sphinx.application import Sphinx
from sphinx_needs.data import NeedsInfoType

from score_metamodel import (
    CheckLogger,
    graph_check,
)


def eval_need_check(need, check):
    """
    Perform a single check on a need:
    1. Split the check into its parts
       (e.g. "status == valid" -> ["status", "==", "valid"])
    2. Perform the check with the operator specified in the yaml file.
    """
    oper = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
    }

    parts = check.split(" ")

    if len(parts) != 3:
        raise ValueError(f"Invalid check defined: {check}")

    if not (parts[1] in oper):
        raise ValueError(f"Binary Operator not defined: {parts[1]}")

    return oper[parts[1]](need[parts[0]], parts[2])


def eval_need_condition(need, condition):
    """Evaluate a condition on a need:
    1. Check if the condition is only a simple check (e.g. "status == valid")
       If so call the check function.
    2. If the condition is a combination of multiple checks
       (e.g. "and: [check1, check2]")
       Recursively call the eval_need_function for each check and combine the
       results with the binary operation which was specified in the yaml file.
    """

    oper = {
        "and": operator.and_,
        "or": operator.or_,
        "not": operator.not_,
        "xor": operator.xor,
    }

    if not isinstance(condition, dict):
        return eval_need_check(need, condition)

    cond = list(condition.keys())[0]
    vals = list(condition.values())[0]

    if cond in ["and", "or", "xor", "not"]:
        for i in range(len(vals) - 1):
            return oper[cond](
                eval_need_condition(need, vals[i]),
                eval_need_condition(need, vals[i + 1]),
            )
    else:
        raise ValueError(f"Binary Operator not defined: {vals}")

    return True


def get_need_selection(needs, selection):
    """Create a list of needs that match the selection criteria.:
    - If it is an include selection add the include to the pattern
    - If it is an exclude selection add a "^" to the pattern
    """

    selected_needs = []

    if "include" in selection:
        pattern = selection["include"]
    elif "exclude" in selection:
        pattern = "^" + selection["exclude"]
    else:
        raise ValueError(f"Invalid selection: {selection}")

    for need in needs:
        if (re.match(pattern, need["type"])) and (
            eval_need_condition(need, selection["condition"])
        ):
            selected_needs.append(need)

    return selected_needs


@graph_check
def check_metamodel_graph(
    app: Sphinx,
    all_needs: NeedsInfoType,
    log: CheckLogger,
):
    graph_checks_global = app.config.graph_checks
    # Convert list to dictionary for easy lookup
    needs_dict = {need["id"]: need for need in all_needs}

    # Iterate over all graph checks
    for check in graph_checks_global.items():
        apply, eval = check[1].values()

        # Get all needs that match the selection criteria
        selected_needs = get_need_selection(all_needs, apply)

        for need in selected_needs:
            for parent_relation in list(eval.keys()):
                parent_ids = need[parent_relation]

                for parent_id in parent_ids:
                    parent_need = needs_dict.get(parent_id, {})

                    if not eval_need_condition(parent_need, eval[parent_relation]):
                        msg = (
                            f"parent need `{parent_id}` does not fulfill "
                            f"condition `{eval[parent_relation]}`."
                        )
                        log.warning_for_need(need, msg)
