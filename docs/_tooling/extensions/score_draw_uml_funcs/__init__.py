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
"""
This 'sphinx-extension' is responsible to allow for functional drawings of UML diagrams

    - Features
    - Logical Interfaces
    - Modules
    - Components
    - Component Interfaces

and all applicable linkages between them.

It provides this functionality by adding classes to `needs_render_context`,
which then can be invoked inside 'needarch' and 'needuml' blocks in rst files.
"""

import hashlib
import time
from functools import cache
from pathlib import Path

from sphinx.application import Sphinx
from sphinx_needs.logging import get_logger

from score_draw_uml_funcs.helpers import (
    gen_alias,
    gen_header,
    gen_interface_element,
    gen_link_text,
    gen_struct_element,
    get_impl_comp_from_real_iface,
    get_interface,
    get_logical_interface_real,
    get_real_interface_logical,
)

logger = get_logger(__file__)


def setup(app: Sphinx) -> dict:
    app.config.needs_render_context = draw_uml_function_context
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


@cache
def scripts_directory_hash():
    start = time.time()
    all = ""
    for file in Path(".devcontainer/sphinx_conf").glob("**/*.py"):
        with open(file) as f:
            all += f.read()
    hash_object = hashlib.sha256(all.encode("utf-8"))
    directory_hash = hash_object.hexdigest()
    logger.info(
        "calculate directory_hash = "
        + directory_hash
        + " within "
        + str(time.time() - start)
        + " seconds."
    )
    return directory_hash


#       ╭──────────────────────────────────────────────────────────────────────────────╮
#       │                           Actual drawing functions                           │
#       ╰──────────────────────────────────────────────────────────────────────────────╯


def draw_component(
    need: dict,
    all_needs: dict,
    proc_real_interfaces: dict[str, str] | None = None,
    proc_logical_interfaces: dict[str, str] | None = None,
) -> tuple[str, str, dict[str, str], dict[str, str]]:
    """
    Drawing and parsing function of a component.

    Example:
        input:
            need: component_1
            all_needs: all_needs_dict
            processed_interfaces: set()
        return:
            # Part 1 Structure Text
            component "Component 1" as C1 {
            }
            interface "Component Interface 1" as CI1 {
            real operation 1 ()
            real operation 2 ()
            }

            interface "Logical Interface 1" as LI1 {
            Logical Operation 1
            Logical Operation 2
            }

            interface "Component Interface 3" as CI3 {
            real operation 5 ()
            real operation 6 ()
            }

            # Part 2 Linkage Text
            CI1 --> LI1: implements
            C1 --> CI1: implements
            C1 --> CI3: uses

            # Part 3 processed_interfaces
            {
             'real_interface_1',
             'real_interface_2',
             'logical_interface_1'
            }

            # Part 4 processed_interfaces
            {
             'logical_interface_1',
             'logical_interface_2'
            }

            Note: part 1 and 2 are returned as one text item separated by '\n'.
            They are interpreted and names are shortened here to aid readability.
    Returns:
        Tuple of 4 parts.
        (Structure Text, Linkage Text, Processed (Real Interfaces),
        Processed Logical Interfaces)
    """
    proc_real_interfaces = proc_real_interfaces or dict()
    proc_logical_interfaces = proc_logical_interfaces or dict()
    linkage_text = ""

    # Draw outer component
    structure_text = f"{gen_struct_element('component', need)}  {{\n"

    # Process includes: Draw inner (sub)components recursively
    for need_inc in need.get("includes", []):
        curr_need = all_needs[need_inc]

        if "comp_arc_sta" in curr_need["type"]:
            sub_structure, sub_links, proc_real_interfaces, proc_logical_interfaces = (
                draw_component(
                    curr_need, all_needs, proc_real_interfaces, proc_logical_interfaces
                )
            )
        else:
            continue

        structure_text += sub_structure
        linkage_text += sub_links

    # close component
    structure_text += f"}} /' {need['title']} '/ \n\n"

    local_interfaces = dict()
    # Fill proc_real_interfaces with relation to implements and uses
    for interface in need.get("implements", []):
        iface = get_interface(interface, all_needs)
        if iface not in local_interfaces:
            local_interfaces[iface] = "implements"

    for interface in need.get("uses", []):
        iface = get_interface(interface, all_needs)
        if iface not in local_interfaces:
            local_interfaces[iface] = "uses"

    for iface in local_interfaces:
        # Draw interfaces
        if iface not in proc_real_interfaces:
            structure_text += gen_interface_element(iface, all_needs, True)
            proc_logical_interfaces[iface] = get_logical_interface_real(
                iface, all_needs
            )
            proc_real_interfaces[iface] = local_interfaces[iface]

        # Draw connection between real components and interfaces
        linkage_text += f"{
            gen_link_text(
                need['title'], '-->', all_needs[iface]['title'], local_interfaces[iface]
            )
        } \n"

        # Draw connection between real interfaces and logical interfaces
        # if link exists
        if interfaces := proc_logical_interfaces[iface]:
            linkage_text += f"{
                gen_link_text(
                    all_needs[iface]['title'],
                    '-->',
                    all_needs[interfaces]['title'],
                    'implements',
                )
            } \n"

    # Remove duplicate links
    linkage_text = "\n".join(set(linkage_text.split("\n"))) + "\n"

    return structure_text, linkage_text, proc_real_interfaces, proc_logical_interfaces


#       ╭──────────────────────────────────────────────────────────────────────────────╮
#       │                    Classes with hashing to enable caching                    │
#       ╰──────────────────────────────────────────────────────────────────────────────╯


class draw_full_feature:
    def __repr__(self):
        return "draw_full_feature" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs: dict) -> str:
        interfacelist = []
        impl_comp = dict()

        structure_text = "allowmixing\n"
        structure_text += f'actor "Feature User" as {gen_alias("Feature User")} \n'

        # Define Feature as a package
        structure_text += f"{gen_struct_element('package', need)} {{\n"

        # Add logical Interfaces / Interface Operations (aka includes)
        for need_inc in need.get("includes", []):
            # Generate list of interfaces since both interfaces
            # and interface operations can be included
            iface = get_interface(need_inc, all_needs)
            interfacelist.append(iface) if iface not in interfacelist else None

        for iface in interfacelist:
            structure_text += gen_interface_element(iface, all_needs, True)

            # Determine Components which implement the interfaces
            real_iface = get_real_interface_logical(iface, all_needs)
            impl_comp[iface] = get_impl_comp_from_real_iface(real_iface[0], all_needs)

            if imcomp := impl_comp[iface]:
                structure_text += (
                    f"{gen_struct_element('component', all_needs[imcomp[0]])}\n"
                )

        # Close Package
        structure_text += f"}} /' {need['title']}  '/ \n\n"

        link_text = ""

        for iface in interfacelist:
            # Add relation between Actor and Interfaces
            link_text += f"{
                gen_link_text('Feature User', '-d->', all_needs[iface]['title'], 'use')
            } \n"

            # Add relation between interface and component
            if imcomp := impl_comp[iface]:
                link_text += f"{
                    gen_link_text(
                        all_needs[imcomp[0]]['title'],
                        '-->',
                        all_needs[iface]['title'],
                        'implements',
                    )
                } \n"
            else:
                print(f"Interface {iface} is not implemented by any component")

        return gen_header() + structure_text + link_text


class draw_full_component:
    def __repr__(self):
        return "draw_full_component" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs) -> str:
        structure_text, linkage_text, processed_interfaces, logical_interfacelist = (
            draw_component(need, all_needs, dict(), dict())
        )

        # Draw Logical Interfaces
        for iface in logical_interfacelist:
            if log_int := logical_interfacelist[iface]:
                structure_text += gen_interface_element(log_int, all_needs, True)

        return gen_header() + structure_text + linkage_text


class draw_full_interface:
    def __repr__(self):
        return "draw_full_interface" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs) -> str:
        structure_text = gen_interface_element(need["id"], all_needs, True)

        return structure_text + "\n"


draw_uml_function_context = {
    "draw_interface": draw_full_interface(),
    "draw_component": draw_full_component(),
    "draw_feature": draw_full_feature(),
}
