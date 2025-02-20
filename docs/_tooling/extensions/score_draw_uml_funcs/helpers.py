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
from itertools import chain


def gen_alias(title: str) -> str:
    return "".join(word[0] for word in title.split())


def gen_link_text(alias_from: str, alias_to: list[str], link_text: str) -> str:
    """
    Helper function that generates link text to be appened to the end of a UML diagramm to display linkages.

    Example:
        input:
            alias_from: CI1
            alias_to: [LI1, LI2]
            link_text: uses
        return:
            CI1 --> LI1: uses
            CI1 --> LI2: uses

        Note: The actual string contains '\n' characters between lines, shown here as visual line breaks for readability

    Args:
        alias_from: The alias from what you want to link
        alias_to: A list of aliases to which you want to link
        link_text: What text to use to link those things together. (Text that will be written by the arrow)

    Returns:
        link_text (str): Text with each link from alias_from to alias_to via link_text seperated via '\n'
    """
    return "\n".join(f"{alias_from} --> {al_to}: {link_text}" for al_to in alias_to)


def find_interfaces_of_operations(needs: dict, needs_inc: list[str]) -> set[str]:
    """
    Helper function to find 'interfaces' that operations belong to.

    Example:
        input:
            needs: all_needs_dict
            needs_inc: ["logical_operation_1", "logical_operation_2"]
        output:
            set: ("Logical_interface_1")

    Args:
        needs: Dictionary of all needs
        needs_inc: List of 'operation ids' that the interface they belong to should be found for

    Returns:
        set: Id's of interfaces the `needs_inc` belong to.

    """
    if not needs_inc:
        return set()

    needs_implements = set(chain(*(needs[id]["implements"] for id in needs_inc)))
    upper_interfaces = set(
        chain(*(needs[id]["includes_back"] for id in needs_implements))
    )
    return upper_interfaces
