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
from typing import Any

from sphinx_needs.logging import get_logger

logger = get_logger(__file__)


########################################################################
# Functions which generate elements
########################################################################
def gen_format(need: dict[str, str]) -> str:
    """Define Layout for Need:
    - Set Background Color for Safety Components
    - Set Language for component interfaces
    """

    style = ""

    if "comp_arc_sta" in need["type"] and need["safety"] == "ASIL_B":
        style = "<<asilb>>"

    if "comp_arc_int" in need["type"]:
        style = "<Rust>" if need["language"] == "rust" else "<C++>"

    return style


def gen_struct_element(UMLelement: str, need: dict[str, str]) -> str:
    """Generate a plantUML element"""
    return (
        f'{UMLelement} "{need["title"]}" as {get_alias(need)} '
        f"{gen_format(need)} {get_need_link(need)}"
    )


def gen_interface_element(
    need_id: str, all_needs: dict[str, dict[str, str]], incl_ops: bool = False
) -> str:
    """Generate architectural interface element and
    include all operations if selected."""

    text = f"{gen_struct_element('interface', all_needs[need_id])} {{\n\n"
    if incl_ops:
        for op in all_needs[need_id].get("included_by_back", []):
            raw_text = all_needs[op]["title"]
            if raw_text.endswith("()"):
                text += f"+ {raw_text} {get_need_link(all_needs[op])}\n"
            else:
                text += f"+ {raw_text} () {get_need_link(all_needs[op])}\n"

    text += f"\n}} /' {all_needs[need_id]['title']} '/ \n\n"
    return text


def gen_link_text(
    from_need: dict[str, str], link_type: str, to_need: dict[str, str], link_text: str
) -> str:
    """
    This function generates a PlantUML link between PlantUML elements

    Example:
        input:
            from_id: Component Interface 1
            to_id: Logical Interface 1
            link_type: -->
            link_text: uses
        return:
            CI1 --> LI1: uses

    """
    return f"{get_alias(from_need)} {link_type} {get_alias(to_need)}: {link_text}"


### Generate PlantUML Headers
def gen_header() -> str:
    """Create PlantUML document header"""
    return (
        "allow_mixing\n"
        + "top to bottom direction\n"
        + "hide stereotype\n"
        + "hide empty attributes\n"
        + gen_sytle_header()
        + "\n"
    )


def gen_sytle_header() -> str:
    """Create PlantUML Header for Style definition"""
    return (
        """<style>\n.asilb {\nLineColor blue\nLineThickness 2.0\n}\n</style>""" + "\n"
    )


########################################################################
# Functions determine relations between needs
########################################################################
def get_alias(need: dict[str, str]) -> str:
    """Generate a Unique ID for referencing in PlantUML"""
    return need["id"]


def get_need_link(need: dict[str, str]) -> str:
    """Generate the link to the need element from the PlantUML Diagram"""
    link = ".." + "/" + need["docname"] + ".html#" + need["id_parent"]

    # Reminder: Link is displayed via triple braces inside a interface
    if "int_op" in need["type"]:
        return f"[[[{link}]]]"

    return f"[[{link}]]"


def get_hierarchy_text(
    component: str, all_needs: dict[str, dict[str, str]]
) -> tuple[str, str, str, str]:
    """This function determines the corresponding module of any component

    :param str component: component to determine the module
    :param dict all_needs: dictionary containing all processed needs

    :return: Tuple of 4 strings:
    open_text: Text to place before the component
    close_text: Text to place after the component
    open_mod_text: Text to open the module
    close_mod_text: Text to close the module
    """
    need = all_needs[component]

    open_text = ""
    close_text = ""
    open_mod_text = ""
    close_mod_text = ""
    parent_need = {}

    if "mod_" not in need["type"]:
        parent_need_str = need.get("includes_back", [])

        if parent_need_str:
            parent_need = all_needs.get(parent_need_str[0], [])

        if parent_need:
            # If Parent Exist and not Module -> Call Function Recursively
            retval = get_hierarchy_text(parent_need_str[0], all_needs)
            open_text += retval[0]
            open_text += f"{gen_struct_element('component', need)}  {{\n"
            close_text += f"}} /' {need['title']} '/ \n\n"
            close_text += retval[1]
            open_mod_text = retval[2]
            close_mod_text = retval[3]

        else:
            # If Top Level Leaf is not a Module
            logger.info(f"{need['id']}: not contained in any module")
            open_text += f"{gen_struct_element('component', need)}  {{\n"
            close_text += f"}} /' {need['title']} '/ \n\n"
    else:
        # Create Module Text
        open_mod_text += f"{gen_struct_element('package', need)}  {{\n"
        close_mod_text += f"}} /' {need['title']} '/ \n\n"

    return open_text, close_text, open_mod_text, close_mod_text


def get_interface_from_component(
    component: dict[str, str], relation: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    """
    Returns a list of interfaces which are related to the component
    """
    local_interfaces: list[str] = []

    for interface in component.get(relation, ""):
        iface = get_interface_from_int(interface, all_needs)
        if iface not in local_interfaces:
            local_interfaces.append(iface)

    return local_interfaces


def get_interface_from_int(need_id: str, all_needs: dict[str, dict[str, Any]]) -> str:
    """Get Interface for a provided Interface or Interface Operation"""

    int_need = all_needs.get(need_id)

    if not int_need:
        logger.warning(f"{need_id}: not defined, misspelled?")
        return ""

    if "_int_op" in int_need["type"]:
        iface = all_needs[need_id]["included_by"][0]
    else:
        iface = need_id

    return iface


def get_real_interface_logical(
    logical_interface_id: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    """Get real interface for provided logical interface
    The relation is traced via the interface operations
    """
    real_ifaces: list[str] = []
    real_ifops: list[str] = []
    logical_ops = all_needs[logical_interface_id]["included_by_back"]

    for logical_op in logical_ops:
        real_ifop = all_needs[logical_op].get("implements_back")
        if not real_ifop:
            logger.info(f"{logical_op}: not implemented by any logical operation")
            continue

        real_ifops.extend(real_ifop) if real_ifop not in real_ifops else None

        # Per definition a operation can only be included by one interface
        real_iface = all_needs[real_ifop[0]].get("included_by")

        if not real_iface:
            logger.info(f"{real_ifop[0]}: not included in any interface")
            continue

        real_ifaces.extend(real_iface) if real_iface not in real_ifaces else None

    return real_ifaces


def get_logical_interface_real(
    real_interface_id: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    """Get logical interface based on real interface"""
    logical_ifaces: list[str] = list()

    real_ifops = all_needs[real_interface_id].get("included_by_back", [])

    for real_ifop in real_ifops:
        logical_ifop = all_needs[real_ifop].get("implements", [])

        if not logical_ifop:
            logger.info(f"{real_ifop}: Logical Interface Operation not specified!")
            continue

        # One real operation can only implement one logical operation
        logical_ifop_need = all_needs.get(logical_ifop[0])
        if not logical_ifop_need:
            logger.info(
                f"{real_ifop}: Logical Interface Operation Need not defined, probably misspelled!"
            )
            continue

        logical_iface = logical_ifop_need.get("included_by", [])

        if not logical_iface:
            logger.info(f"{logical_ifop[0]}: Not included by any Logical Interface!")
            continue

        logical_ifaces.extend(logical_iface) if logical_iface[
            0
        ] not in logical_ifaces else logical_ifaces

    return logical_ifaces


def get_impl_comp_from_real_iface(
    real_iface: str, all_needs: dict[str, dict[str, str]]
) -> list[str]:
    """Get implementing component of the interface"""
    implcomp: list[str] = all_needs[real_iface].get("implements_back", [])

    if not implcomp:
        logger.info(
            f"{all_needs[real_iface]['id']}: Implementing Component not specified!"
        )

    return implcomp


def get_use_comp_from_real_iface(
    real_iface: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    """Get components which use the interface"""
    usecomp: list[str] = all_needs[real_iface].get("uses_back", [])

    if usecomp:
        logger.info(f"{all_needs[real_iface]}: Interface not used by component!")

    return usecomp
