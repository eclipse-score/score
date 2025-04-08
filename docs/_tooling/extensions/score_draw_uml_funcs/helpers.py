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


def gen_need_link(need: dict[str, str]) -> str:
    """Generate the link to the need element from the PlantUML Diagram"""
    link = ".." + "/" + need["docname"] + ".html#" + need["id_parent"]
    if "int_op" in need["type"]:
        return f"[[[{link}]]]"
    else:
        return f"[[{link}]]"


def gen_alias(need: dict[str, str]) -> str:
    """Generate a Unique ID for referencing in PlantUML"""
    return need["id"]


def gen_format(need: dict[str, str]) -> str:
    """Determine Layout for Need"""

    style = ""

    if "comp_arc_sta" in need["type"] and need["safety"] == "ASIL_B":
        style = "<<asilb>>"

    if "comp_arc_int" in need["type"]:
        if need["language"] == "rust":
            style = "<Rust>"
        else:
            style = "<C++>"

    return style


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


def gen_struct_element(UMLelement: str, need: dict[str, str]) -> str:
    """Generate a Structural Element inside the PlantUML Diagram"""
    return (
        f'{UMLelement} "{need["title"]}" as {gen_alias(need)} '
        f"{gen_format(need)} {gen_need_link(need)}"
    )


def gen_interface_element(
    need_id: str, all_needs: dict[str, dict[str, Any]], incl_ops: bool = False
) -> str:
    """Generate interface text and include all operations if selected."""

    text = f"{gen_struct_element('interface', all_needs[need_id])} {{\n\n"
    if incl_ops:
        for op in all_needs[need_id].get("included_by_back", []):
            raw_text = all_needs[op]["title"]
            if raw_text.endswith("()"):
                text += f"+ {raw_text} {gen_need_link(all_needs[op])}\n"
            else:
                text += f"+ {raw_text} () {gen_need_link(all_needs[op])}\n"

    text += f"\n}} /' {all_needs[need_id]['title']} '/ \n\n"
    return text


def gen_link_text(
    from_need: dict[str, str], link_type: str, to_need: dict[str, str], link_text: str
) -> str:
    """
    Helper function that generates link text to be appended to the end
    of a UML diagram to display linkages.

    Example:
        input:
            from_id: Component Interface 1
            to_id: Logical Interface 1
            link_type: -->
            link_text: uses
        return:
            CI1 --> LI1: uses

        Note: The actual string contains '\n' characters between lines,
        shown here as visual line breaks for readability
    """
    return f"{gen_alias(from_need)} {link_type} {gen_alias(to_need)}: {link_text}"


def get_module(
    component: str, all_needs: dict[str, dict[str, Any]]
) -> tuple[str, str, str, str]:
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
            retval = get_module(parent_need_str[0], all_needs)
            open_text += retval[0]
            open_text += f"{gen_struct_element('component', need)}  {{\n"
            close_text += f"}} /' {need['title']} '/ \n\n"
            close_text += retval[1]
            open_mod_text = retval[2]
            close_mod_text = retval[3]

        else:
            # If Top Level Leaf is not a Module
            print(f"{need['id']}: not contained in any module")
            open_text += f"{gen_struct_element('component', need)}  {{\n"
            close_text += f"}} /' {need['title']} '/ \n\n"
    else:
        # Create Module
        open_mod_text += f"{gen_struct_element('package', need)}  {{\n"
        close_mod_text += f"}} /' {need['title']} '/ \n\n"

    return open_text, close_text, open_mod_text, close_mod_text


def get_interface_from_component(
    component: dict[str, str], relation: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    local_interfaces = []

    for interface in component.get(relation, []):
        iface = get_interface_from_int(interface, all_needs)
        if iface not in local_interfaces:
            local_interfaces.append(iface)

    return local_interfaces


def get_interface_from_int(need_id: str, all_needs: dict[str, dict[str, Any]]) -> str:
    """Get Interface for a provided Interface or Interface Operation"""
    if "_int_op" in all_needs[need_id]["type"]:
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
    real_ifaces = []
    real_ifops = []
    logical_ops = all_needs[logical_interface_id]["included_by_back"]

    for logical_op in logical_ops:
        real_ifop = all_needs[logical_op]["implements_back"][0]
        real_ifops.append(real_ifop) if real_ifop not in real_ifops else None

        real_iface = all_needs[real_ifop]["included_by"][0]
        real_ifaces.append(real_iface) if real_iface not in real_ifaces else None

    return real_ifaces


def get_logical_interface_real(
    real_interface_id: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    """Get logical interface based on real interface"""
    logical_ifaces = list()

    real_ifops = all_needs[real_interface_id].get("included_by_back", [])

    for real_ifop in real_ifops:
        logical_ifop = all_needs[real_ifop].get("implements", [])

        if logical_ifop:
            logical_iface = all_needs[logical_ifop[0]].get("included_by", [])[0]

            if logical_iface:
                logical_ifaces.append(
                    logical_iface
                ) if not logical_iface in logical_ifaces else logical_ifaces
            else:
                print(f"{logical_ifop}: Logical Interface not specified!")

        else:
            print(f"{real_ifop}: Logical Interface Operation not specified!")

    return logical_ifaces


def get_impl_comp_from_real_iface(
    real_iface: str, all_needs: dict[str, dict[str, Any]]
) -> str:
    """Get implementing component of the interface"""

    implcomp = all_needs[real_iface].get("implements_back", [])

    if not implcomp:
        print(f"{all_needs[real_iface]['id']}: Implementing Component not specified!")
    else:
        implcomp = implcomp[0]

    return implcomp


def get_use_comp_from_real_iface(
    real_iface: str, all_needs: dict[str, dict[str, Any]]
) -> list[str]:
    """Get components which use the interface"""
    usecomp = all_needs[real_iface].get("uses_back", [])

    if usecomp:
        print(f"{all_needs[real_iface]}: Interface not used by component!")

    return usecomp
