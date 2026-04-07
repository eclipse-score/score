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
"""
Sphinx extension that provides the ``fmea_xml_table`` directive.

The directive reads a FMEA XML file and:
  1. Registers each entry as a hidden ``feat_saf_fmea`` need in sphinx-needs.
  2. Renders all entries as a table with the columns defined in FMEA_COLUMNS.

Usage in RST::

    .. fmea_xml_table:: path/to/fmea.xml

The path is resolved relative to the document that contains the directive.
"""

import os
import xml.etree.ElementTree as ET
from collections.abc import Sequence

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx_needs.api import add_external_need

FMEA_COLUMNS = [
    "id",
    "violates",
    "fault_id",
    "failure_effect",
    "mitigated_by",
    "sufficient",
    "status",
    "safety_relevant",
    "root_cause",
    "content",
]

# Fields passed to add_need (must match metamodel's feat_saf_fmea definition).
# safety_relevant and root_cause are not in the metamodel, so they are
# displayed in the table only.
_NEED_EXTRA_KWARGS = {"fault_id", "failure_effect", "sufficient"}
_NEED_LINK_KWARGS = {"violates", "mitigated_by"}


class FmeaXmlTable(SphinxDirective):
    """Import FMEA data from an XML file and render it as a table."""

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self) -> Sequence[nodes.Node]:
        xml_rel_path = self.arguments[0]
        xml_abs_path = self.env.relfn2path(xml_rel_path, self.env.docname)[1]

        if not os.path.exists(xml_abs_path):
            msg = f"fmea_xml_table: file not found: {xml_abs_path}"
            return [nodes.system_message(msg, level=3, type="ERROR", line=self.lineno)]

        tree = ET.parse(xml_abs_path)
        root = tree.getroot()

        entries: list[dict[str, str]] = []
        result_nodes: list[nodes.Node] = []

        for entry_elem in root.findall("entry"):
            row = {
                field: (entry_elem.findtext(field) or "").strip()
                for field in FMEA_COLUMNS
            }
            entries.append(row)

            violates_str = row["violates"]
            mitigated_str = row["mitigated_by"]

            add_external_need(
                app=self.env.app,
                need_type="feat_saf_fmea",
                title=row["id"],
                id=row["id"],
                external_url="",
                content=row["content"],
                status=row["status"],
                fault_id=row["fault_id"],
                failure_effect=row["failure_effect"],
                sufficient=row["sufficient"],
                violates=violates_str,
                mitigated_by=mitigated_str,
            )

        result_nodes.append(_build_table(entries))
        return result_nodes


def _build_table(entries: list[dict[str, str]]) -> nodes.table:
    table = nodes.table()
    tgroup = nodes.tgroup(cols=len(FMEA_COLUMNS))
    table += tgroup

    for _ in FMEA_COLUMNS:
        tgroup += nodes.colspec(colwidth=1)

    # Header
    thead = nodes.thead()
    tgroup += thead
    hrow = nodes.row()
    thead += hrow
    for col in FMEA_COLUMNS:
        cell = nodes.entry()
        cell += nodes.paragraph(text=col)
        hrow += cell

    # Body
    tbody = nodes.tbody()
    tgroup += tbody
    for row in entries:
        trow = nodes.row()
        tbody += trow
        for col in FMEA_COLUMNS:
            cell = nodes.entry()
            cell += nodes.paragraph(text=row.get(col, ""))
            trow += cell

    return table


def setup(app):
    app.add_directive("fmea_xml_table", FmeaXmlTable)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
