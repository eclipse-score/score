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
from collections.abc import Callable
from functools import cache
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx
from sphinx_needs.logging import get_logger

from score_draw_uml_funcs.helpers import (
    gen_header,
    gen_interface_element,
    gen_link_text,
    gen_struct_element,
    get_alias,
    get_hierarchy_text,
    get_impl_comp_from_real_iface,
    get_interface_from_component,
    get_interface_from_int,
    get_logical_interface_real,
    get_real_interface_logical,
)

logger = get_logger(__file__)


def setup(app: Sphinx) -> dict[str, object]:
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


def draw_comp_incl_impl_int(
    need: dict[str, str],
    all_needs: dict[str, dict[str, str]],
    proc_impl_interfaces: dict[str, str],
    proc_used_interfaces: dict[str, list[str]],
) -> tuple[str, str, dict[str, str], dict[str, list[str]]]:
    """This function draws a component including any interfaces which are implemented
    by the component

    :param dict[str,str] need: Component which should be drawn
    :param dict all_needs: Dictionary containing all needs
    :param dict[str,dict] proc_impl_interfaces: Dictionary containing all implemented
      interfaces which were already processed during this cycle
    :param dict[str,dict] proc_used_interfaces: Dictionary containing
        all used interfaces which were already processed during this cycle
    """
    # Draw outer component
    structure_text = f"{gen_struct_element('component', need)}  {{\n"
    linkage_text = ""

    # Draw inner (sub)components recursively
    for need_inc in need.get("includes", []):
        curr_need = all_needs.get(need_inc, {})

        # check for misspelled include
        if not curr_need:
            logger.info(f"{need}: include {need_inc} could not be found")
            continue

        if curr_need["type"] != "comp_arc_sta":
            continue

        sub_structure, sub_linkage, proc_impl_interfaces, proc_used_interfaces = (
            draw_comp_incl_impl_int(
                curr_need, all_needs, proc_impl_interfaces, proc_used_interfaces
            )
        )

        structure_text += sub_structure
        linkage_text += sub_linkage

    # close outer component
    structure_text += f"}} /' {need['title']} '/ \n\n"

    # Find implemented real interfaces inside the module/component
    local_impl_interfaces = get_interface_from_component(need, "implements", all_needs)
    local_used_interfaces = get_interface_from_component(need, "uses", all_needs)

    # Add all interfaces which are implemented by component to global list
    # and provide implementation
    for iface in local_impl_interfaces:
        # check for misspelled implements
        if not all_needs.get(iface, []):
            logger.info(f"{need}: implements {iface} could not be found")
            continue

        if not proc_impl_interfaces.get(iface, []):
            structure_text += gen_interface_element(iface, all_needs, True)
            linkage_text += f"{
                gen_link_text(
                    need,
                    '-u->',
                    all_needs[iface],
                    'implements',
                )
            } \n"
            proc_impl_interfaces[iface] = need["id"]

    # Add all elements which are used by component to global list
    for iface in local_used_interfaces:
        # check for misspelled used
        if not all_needs.get(iface, []):
            logger.info(f"{need}: uses {iface} could not be found")
            continue

        if not proc_used_interfaces.get(iface, []):
            proc_used_interfaces[iface] = [need["id"]]
        else:
            proc_used_interfaces[iface].append(need["id"])

    return structure_text, linkage_text, proc_impl_interfaces, proc_used_interfaces


def draw_module(
    need: dict[str, str],
    all_needs: dict[str, dict[str, str]],
) -> tuple[str, str]:
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
    # Store all Elements which have already been processed
    proc_impl_interfaces: dict[str, str] = dict()
    proc_used_interfaces: dict[str, list[str]] = dict()
    proc_logical_interfaces: dict[str, str] = dict()

    structure_text = f"{gen_struct_element('package', need)}  {{\n"
    linkage_text = ""

    structure_text, linkage_text, proc_impl_interfaces, proc_used_interfaces = (
        process_included_components(
            need,
            all_needs,
            structure_text,
            linkage_text,
            proc_impl_interfaces,
            proc_used_interfaces,
        )
    )
    structure_text += f"}} /' {need['title']} '/ \n\n"

    structure_text, linkage_text, proc_logical_interfaces = add_logical_interfaces(
        proc_impl_interfaces,
        proc_logical_interfaces,
        all_needs,
        structure_text,
        linkage_text,
    )
    structure_text, linkage_text = add_used_interfaces(
        proc_used_interfaces,
        proc_impl_interfaces,
        all_needs,
        structure_text,
        linkage_text,
    )
    linkage_text = "\n".join(set(linkage_text.split("\n"))) + "\n"

    return structure_text, linkage_text


def process_included_components(
    need: dict[str, str],
    all_needs: dict[str, dict[str, str]],
    structure_text: str,
    linkage_text: str,
    proc_impl_interfaces: dict[str, str],
    proc_used_interfaces: dict[str, list[str]],
) -> tuple[str, str, dict[str, str], dict[str, list[str]]]:
    for need_inc in need.get("includes", []):
        curr_need = all_needs.get(need_inc, {})
        if not curr_need:
            logger.info(f"{need}: include with id {need_inc} could not be found")
            continue
        if curr_need["type"] not in ["comp_arc_sta", "mod_view_sta"]:
            continue
        sub_structure, sub_linkage, proc_impl_interfaces, proc_used_interfaces = (
            draw_comp_incl_impl_int(
                curr_need,
                all_needs,
                proc_impl_interfaces,
                proc_used_interfaces,
            )
        )
        structure_text += sub_structure
        linkage_text += sub_linkage

    return structure_text, linkage_text, proc_impl_interfaces, proc_used_interfaces


def add_logical_interfaces(
    proc_impl_interfaces: dict[str, str],
    proc_logical_interfaces: dict[str, str],
    all_needs: dict[str, dict[str, str]],
    structure_text: str,
    linkage_text: str,
) -> tuple[str, str, dict[str, str]]:
    for iface in proc_impl_interfaces:
        if not proc_logical_interfaces.get(iface, []):
            logical_iface_tmp = get_logical_interface_real(iface, all_needs)
            if len(logical_iface_tmp) > 1:
                logger.warning(
                    f"{logical_iface_tmp}: only one logical interface per real "
                    "interface supported"
                )
            if logical_iface_tmp:
                logical_iface = logical_iface_tmp[0]
                proc_logical_interfaces[logical_iface] = iface
                structure_text += gen_interface_element(logical_iface, all_needs, True)
                linkage_text += f"{gen_link_text(all_needs[iface], '-u->',
                                    all_needs[logical_iface],
                                    'implements')}\n"
            else:
                print(f"{iface}: Not connected to any virtual interface")
    return structure_text, linkage_text, proc_logical_interfaces


def add_used_interfaces(
    proc_used_interfaces: dict[str, list[str]],
    proc_impl_interfaces: dict[str, str],
    all_needs: dict[str, dict[str, str]],
    structure_text: str,
    linkage_text: str,
) -> tuple[str, str]:
    for iface, comps in proc_used_interfaces.items():
        if iface not in proc_impl_interfaces:
            impl_comp_str = get_impl_comp_from_real_iface(iface, all_needs)
            impl_comp = all_needs.get(impl_comp_str[0], {}) if impl_comp_str else ""

            if impl_comp:
                retval = get_hierarchy_text(impl_comp_str[0], all_needs)
                structure_text += retval[2] + retval[0] + retval[1] + retval[3]
                structure_text += gen_interface_element(iface, all_needs, True)
                linkage_text += f"{gen_link_text(impl_comp, '-u->',
                                all_needs[iface],
                                'implements')} \n"
            else:
                print(f"{iface}: No implementing component defined")
                structure_text += gen_interface_element(iface, all_needs, True)

        for comp in comps:
            linkage_text += f"{gen_link_text(all_needs[comp],
                                            '-d[#green]->',
                                            all_needs[iface], 'uses')} \n"
    return structure_text, linkage_text


#       ╭──────────────────────────────────────────────────────────────────────────────╮
#       │                    Classes with hashing to enable caching                    │
#       ╰──────────────────────────────────────────────────────────────────────────────╯


class draw_full_feature:
    def __repr__(self):
        return "draw_full_feature" + " in " + scripts_directory_hash()

    def __call__(
        self, need: dict[str, str], all_needs: dict[str, dict[str, str]]
    ) -> str:
        interfacelist = self._get_interface_list(need, all_needs)
        structure_text, impl_comp = self._generate_structure_and_components(
            interfacelist, all_needs
        )
        link_text = self._generate_links(interfacelist, impl_comp, all_needs, need)
        return gen_header() + structure_text + link_text

    def _get_interface_list(
        self, need: dict[str, str], all_needs: dict[str, dict[str, str]]
    ) -> list[str]:
        interfacelist: list[str] = []
        for need_inc in need.get("includes", []):
            iface = get_interface_from_int(need_inc, all_needs)
            if iface not in interfacelist:
                interfacelist.append(iface)
        return interfacelist

    def _generate_structure_and_components(
        self,
        interfacelist: list[str],
        all_needs: dict[str, dict[str, str]],
    ) -> tuple[str, dict[str, str]]:
        structure_text = (
            f'actor "Feature User" as {get_alias({"id": "Feature_User"})} \n'
        )
        impl_comp: dict[str, str] = {}

        for iface in interfacelist:
            if all_needs.get(iface):
                structure_text += gen_interface_element(iface, all_needs, True)
                real_iface = get_real_interface_logical(iface, all_needs)
                if real_iface:
                    comps = get_impl_comp_from_real_iface(real_iface[0], all_needs)
                    if comps:
                        impl_comp[iface] = comps[0]
                if im := impl_comp.get(iface):
                    structure_text += f"{gen_struct_element('component',
                                         all_needs[im])}\n"
            else:
                logger.info(f"Interface {iface} could not be found")
        return structure_text, impl_comp

    def _generate_links(
        self,
        interfacelist: list[str],
        impl_comp: dict[str, str],
        all_needs: dict[str, dict[str, str]],
        need: dict[str, str],
    ) -> str:
        link_text = ""
        for iface in interfacelist:
            if imcomp := impl_comp.get(iface):
                link_text += f"{gen_link_text({'id': 'Feature_User'}, '-d->',
                                    all_needs[iface],
                                    'use')} \n"
                link_text += f"{gen_link_text(all_needs[imcomp],
                                    '-u->',
                                    all_needs[iface],
                                    'implements')} \n"
            else:
                logger.info(f"{need}: Interface {iface} could not be found")
        return link_text


class draw_full_module:
    def __repr__(self):
        return "draw_full_module" + " in " + scripts_directory_hash()

    def __call__(
        self, need: dict[str, str], all_needs: dict[str, dict[str, str]]
    ) -> str:
        structure_text, linkage_text = draw_module(need, all_needs)

        return gen_header() + structure_text + linkage_text


class draw_full_component:
    def __repr__(self):
        return "draw_full_component" + " in " + scripts_directory_hash()

    def __call__(
        self, need: dict[str, str], all_needs: dict[str, dict[str, str]]
    ) -> str:
        structure_text, linkage_text, _, _ = draw_comp_incl_impl_int(
            need, all_needs, dict(), dict()
        )

        return gen_header() + structure_text + linkage_text


class draw_full_interface:
    def __repr__(self):
        return "draw_full_interface" + " in " + scripts_directory_hash()

    def __call__(
        self, need: dict[str, str], all_needs: dict[str, dict[str, str]]
    ) -> str:
        structure_text = gen_interface_element(need["id"], all_needs, True)

        return structure_text + "\n"


CallableType = Callable[[dict[str, Any], dict[str, dict[str, Any]]], str]

draw_uml_function_context: dict[str, CallableType] = {
    "draw_interface": draw_full_interface(),
    "draw_module": draw_full_module(),
    "draw_component": draw_full_component(),
    "draw_feature": draw_full_feature(),
}
