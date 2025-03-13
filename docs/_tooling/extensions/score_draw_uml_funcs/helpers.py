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
import re


def gen_alias(title: str) -> str:
    return "".join(word[0] for word in title.split())


def gen_format(need: dict) -> str:
    if need["safety"] == "ASIL_B":
        color = "<<asilb>>" if "comp_arc_sta" in need["type"] else ""
    else:
        color = ""

    return color


def gen_struct_element(element: str, need: dict) -> str:
    return (
        f'{element} "{need["title"]}" as {gen_alias(need["title"])} {gen_format(need)}'
    )


def gen_link_text(from_need: str, link_type: str, to_need: str, link_text: str) -> str:
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


def gen_interface_element(need_id: str, all_needs: dict, incl_ops: bool = False) -> str:
    """Generate interface text and include all operations if selected."""
    if "_int" not in all_needs[need_id]["type"]:
        return ""
    text = f"{gen_struct_element('interface', all_needs[need_id])} {{\n"
    if incl_ops:
        for op in all_needs[need_id].get("includes"):
            raw_text = all_needs[op]["title"]
            if re.match(".*'()'$", raw_text):
                text += f"{raw_text}\n"
            else:
                text += f"{raw_text} ()\n"

    text += f"\n}} /' {all_needs[need_id]['title']} '/ \n\n"
    return text


def get_interface(need_id: str, all_needs: dict) -> str:
    if "_int_op" in all_needs[need_id]["type"]:
        iface = all_needs[need_id]["includes_back"][0]
    else:
        iface = need_id

    return iface


def get_real_interface_logical(need_id: str, all_needs: dict) -> list[str]:
    real_ifaces = []
    real_ifops = []
    logical_ops = all_needs[need_id]["includes"]

    for logical_op in logical_ops:
        real_ifop = all_needs[logical_op]["implements_back"][0]
        real_ifops.append(real_ifop) if real_ifop not in real_ifops else None

        real_iface = all_needs[real_ifop]["includes_back"][0]
        real_ifaces.append(real_iface) if real_iface not in real_ifaces else None

    return real_ifaces


def get_logical_interface_real(need_id: str, all_needs: dict) -> str:
    logical_ifaces = ""

    real_ifops = all_needs[need_id].get("includes")

    for real_ifop in real_ifops:
        logical_ifop = (
            all_needs[real_ifop].get("implements")[0]
            if all_needs[real_ifop].get("implements") != []
            else ""
        )

        tmp = all_needs[logical_ifop].get("includes_back")
        logical_ifaces = tmp[0] if len(tmp) else ""

    return logical_ifaces


def get_impl_comp_from_real_iface(real_iface: str, all_needs: dict) -> list[str]:
    return all_needs[real_iface]["implements_back"]


def get_use_comp_from_real_iface(real_iface: str, all_needs: dict) -> list[str]:
    return all_needs[real_iface]["uses_back"]


def gen_header() -> str:
    return (
        "allow_mixing\n"
        + "left to right direction\n"
        + "hide stereotype\n"
        + gen_sytle_header()
        + "\n"
    )


def gen_sytle_header() -> str:
    return (
        """<style>
        .asilb {
        LineColor blue
        LineThickness 3.0
        }
    </style>"""
        + "\n"
    )
