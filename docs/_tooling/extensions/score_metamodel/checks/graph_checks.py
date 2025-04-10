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
from collections.abc import Callable
from typing import Any, Literal

from sphinx.application import Sphinx
from sphinx_needs.data import NeedsInfoType

from score_metamodel import (
    CheckLogger,
    graph_check,
)


def eval_need_check(need: NeedsInfoType, check: str, log: CheckLogger) -> bool:
    """
    Perform a single check on a need:
    1. Split the check into its parts
       (e.g. "status == valid" -> ["status", "==", "valid"])
    2. Perform the check with the operator specified in the yaml file.
    """
    oper: dict[str, Callable[[Any, Any], bool]] = {
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

    if parts[1] not in oper:
        raise ValueError(f"Binary Operator not defined: {parts[1]}")

    if parts[0] not in need:
        msg = f"Attribute not defined: {parts[0]}"
        log.warning_for_need(need, msg)
        return False

    return oper[parts[1]](need[parts[0]], parts[2])


def eval_need_condition(
    need: NeedsInfoType, condition: str | dict[str, list[Any]], log: CheckLogger
) -> bool:
    """Evaluate a condition on a need:
    1. Check if the condition is only a simple check (e.g. "status == valid")
       If so call the check function.
    2. If the condition is a combination of multiple checks
       (e.g. "and: [check1, check2]")
       Recursively call the eval_need_function for each check and combine the
       results with the binary operation which was specified in the yaml file.
    """

    oper: dict[str, Any] = {
        "and": operator.and_,
        "or": operator.or_,
        "not": operator.not_,
        "xor": operator.xor,
    }

    if not isinstance(condition, dict):
        return eval_need_check(need, condition, log)

    cond: str = list(condition.keys())[0]
    vals: list[Any] = list(condition.values())[0]

    if cond in ["and", "or", "xor", "not"]:
        for i in range(len(vals) - 1):
            return oper[cond](
                eval_need_condition(need, vals[i], log),
                eval_need_condition(need, vals[i + 1], log),
            )
    else:
        raise ValueError(f"Binary Operator not defined: {vals}")

    return True


def get_need_selection(
    needs: list[NeedsInfoType], selection: dict[str, str], log: CheckLogger
) -> list[NeedsInfoType]:
    """Create a list of needs that match the selection criteria.:
    - If it is an include selection add the include to the pattern
    - If it is an exclude selection add a "^" to the pattern
    """

    selected_needs: list[NeedsInfoType] = []
    pattern = []
    need_pattern: str = list(selection.keys())[0]
    # Verify Inputs
    if need_pattern in ["include", "exclude"]:
        for pat in list(selection.values())[0].split(","):
            pattern.append(pat.lstrip())
    else:
        raise ValueError(f"Invalid need selection: {selection}")

    if "condition" in selection:
        condition = selection["condition"]
    else:
        raise ValueError(f"Invalid selection: {selection}")

    for need in needs:
        if need_pattern == "include":
            sel = need["type"] in pattern
        else:
            sel = need["type"] not in pattern

        if sel and (eval_need_condition(need, condition, log)):
            selected_needs.append(need)

    return selected_needs


@graph_check
def check_metamodel_graph(
    app: Sphinx,
    all_needs: list[NeedsInfoType],
    log: CheckLogger,
):
    graph_checks_global = app.config.graph_checks
    # Convert list to dictionary for easy lookup
    needs_dict = {need["id"]: need for need in all_needs}

    # Iterate over all graph checks
    for check in graph_checks_global.items():
        apply, eval = check[1].values()

        # Get all needs that match the selection criteria
        selected_needs = get_need_selection(all_needs, apply, log)

        for need in selected_needs:
            for parent_relation in list(eval.keys()):
                if parent_relation not in need:
                    msg = f"Attribute not defined: {parent_relation}"
                    log.warning_for_need(need, msg)
                    continue
                parent_ids = need[parent_relation]

                for parent_id in parent_ids:
                    parent_need = needs_dict.get(parent_id)
                    if parent_need is None:
                        msg = f"Parent need `{parent_id}` not found in needs_dict."
                        log.warning_for_need(need, msg)
                        continue

                    if not eval_need_condition(parent_need, eval[parent_relation], log):
                        msg = (
                            f"parent need `{parent_id}` does not fulfill "
                            f"condition `{eval[parent_relation]}`."
                        )
                        log.warning_for_need(need, msg)
