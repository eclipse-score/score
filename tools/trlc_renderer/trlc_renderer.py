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

import argparse
import debugpy
import re

import trlc.ast
from trlc.errors import Message_Handler
from trlc.trlc import Source_Manager

from bigtree import Node, preorder_iter

RST_HEADLINE_SEPERATOR = {
    0: "**********",
    1: "==========",
    2: "----------",
    3: "^^^^^^^^^^",
}


def parse_trlc_files_in(input_directory: str) -> trlc.ast.Symbol_Table:
    message_handler = Message_Handler()
    source_manager = Source_Manager(message_handler)

    source_manager.register_directory(input_directory)
    symbols = source_manager.process()
    if symbols is None:
        raise ValueError("Failed to parse TRLC Files")

    return symbols


def convert_symbols_to_objects(symbols: trlc.ast.Symbol_Table):
    requirements_root = Node("root")
    object_list = dict()
    obj: trlc.ast.Record_Object
    for obj in symbols.iter_record_objects():
        parent_root = Node("root")
        parent_tree = build_parent_tree(obj.section, parent_root)
        parent_tree.append(Node(obj.fully_qualified_name()))
        object_list.update({obj.fully_qualified_name(): obj})

        # Merge both trees
        to_tree = requirements_root
        for from_node in preorder_iter(parent_root):
            if from_node.is_root:
                continue

            found = False
            for to_node in to_tree.children:
                if to_node.name == from_node.name:
                    found = True
                    to_tree = to_node
                    break

            if found is True:
                continue

            to_tree.append(from_node)
            break
    return (requirements_root, object_list)

def split_at_capital(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

def generate_need_id_score(reqobj) -> str:
    return reqobj.n_typ.name.upper() + "__" + reqobj.n_package.name.lower() + "__" + reqobj.name


def render_restructured_text_file(requirements, objects, output_path):
    with open(output_path, "w", newline="") as file:
        file.write("Requirements\n")
        file.write("============\n")

        for node in preorder_iter(requirements):
            if node.is_root:
                continue

            if node.is_leaf is False:
                file.write(f"{node.name}\n")
                if node.depth in RST_HEADLINE_SEPERATOR:
                    file.write(f"{RST_HEADLINE_SEPERATOR[node.depth]}\n")
                else:
                    file.write("'''''''''\n")
            else:
                # Todo: This formatting can be extracted in future an specialized for each requirement type
                # Mapping for S-Core
                reqobj = objects[node.name]
                id = generate_need_id_score(reqobj)
                separateelements = split_at_capital(reqobj.n_typ.name)
                element = separateelements[0].lower() + '_' + separateelements[1].lower()

                # Create Needs header
                title = reqobj.field["title"].value
                file.write(f".. {element}:: {title}\n")
                file.write(f"   :id: {id}\n")

                # Write remaining attributes
                for key, value in reqobj.field.items():
                    if key in ["title", "description"]:
                        continue

                    if isinstance(value, trlc.ast.String_Literal):
                        attr_val = value.value
                    elif isinstance(value, trlc.ast.Integer_Literal):
                        attr_val = value.value
                    elif isinstance(value, trlc.ast.Record_Reference):
                        attr_val = generate_need_id_score(value.target)
                    else:
                        continue

                    file.write(f"   :{key}: {attr_val}\n")

                file.write("\n")
                file.write(f"   {reqobj.field['description'].value}\n")
                file.write("\n\n")


def build_parent_tree(section: trlc.ast.Section, root) -> Node:
    if section is None:
        return root
    else:
        parent = build_parent_tree(section.parent, root)
        return Node(section.name, parent=parent)


def trlc_renderer(input_directory, output_path):
    symbols = parse_trlc_files_in(input_directory)
    requirements, req_objects = convert_symbols_to_objects(symbols)
    render_restructured_text_file(requirements, req_objects, output_path)


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")

    return parser


def main() -> None:
    parser = argument_parser()
    args = parser.parse_args()
    debugpy.listen(("0.0.0.0", 5678))
    print("Waiting for client to connect")
    debugpy.wait_for_client()

    trlc_renderer(".", args.output)


if __name__ == "__main__":
    main()
