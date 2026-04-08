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
import re
import xml.etree.ElementTree as ET
from collections.abc import Sequence

from docutils import nodes
from sphinx.util.nodes import make_refnode
from sphinx.util.docutils import SphinxDirective
from sphinx_needs.api import add_external_need
from sphinx_needs.data import SphinxNeedsData

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
# safety_relevant and root_cause are now in the metamodel.
_NEED_EXTRA_KWARGS = {"fault_id", "failure_effect", "sufficient", "safety_relevant", "root_cause"}
_NEED_LINK_KWARGS = {"violates", "mitigated_by"}

# fault_id values (e.g. "MF_01_01") map to needs in the process_description build
# using the prefix "fmea_fault_model__" + lower-case value as the anchor.
_FAULT_ID_NEED_PREFIX = "fmea_fault_model__"


class FmeaNeedRef(nodes.Inline, nodes.Element):
    """Placeholder node for need references rendered by fmea_xml_table."""


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
                safety_relevant=row["safety_relevant"],
                root_cause=row["root_cause"],
                violates=violates_str,
                mitigated_by=mitigated_str,
            )

        result_nodes.append(_build_table(entries, self))
        return result_nodes


def _append_fault_id_link(paragraph: nodes.paragraph, value: str, base_url: str) -> None:
    """Render a fault_id value as a link to the fault models guideline page."""
    full_need_id = f"{_FAULT_ID_NEED_PREFIX}{value.lower()}"
    ref = nodes.reference(value, value, refuri=f"{base_url}#{full_need_id}")
    paragraph += ref


def _append_need_links(paragraph: nodes.paragraph, value: str, directive: SphinxDirective) -> None:
    """Render a need-link field value as clickable references."""
    need_ids = [token.strip() for token in re.split(r"[,|]", value) if token.strip()]
    if not need_ids:
        paragraph += nodes.Text(value)
        return

    for index, need_id in enumerate(need_ids):
        if index:
            paragraph += nodes.Text(", ")

        need_ref = FmeaNeedRef("", reftarget=need_id)
        need_ref += nodes.Text(need_id)
        paragraph += need_ref


def _resolve_fmea_need_refs(app, doctree: nodes.document, fromdocname: str) -> None:
    """Replace placeholder FMEA need refs with final links once all needs are known."""
    needs_view = SphinxNeedsData(app.env).get_needs_view()

    for node in doctree.findall(FmeaNeedRef):
        need_id = str(node.get("reftarget", ""))
        target_need = needs_view.get(need_id)

        if target_need and target_need.get("docname") and not target_need.get("is_external"):
            node.replace_self(
                make_refnode(
                    app.builder,
                    fromdocname,
                    target_need["docname"],
                    need_id,
                    nodes.Text(need_id),
                    need_id,
                )
            )
            continue

        external_url = target_need.get("external_url") if target_need else None
        if external_url:
            ref = nodes.reference(need_id, need_id, refuri=external_url)
            external_css = target_need.get("external_css") if target_need else None
            if external_css:
                ref["classes"].append(external_css)
            node.replace_self(ref)
            continue

        node.replace_self(nodes.Text(need_id))


def _build_table(entries: list[dict[str, str]], directive: SphinxDirective) -> nodes.table:
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
            paragraph = nodes.paragraph()
            value = row.get(col, "")
            if col in _NEED_LINK_KWARGS and value:
                _append_need_links(paragraph, value, directive)
            elif col == "fault_id" and value:
                base_url = directive.env.app.config.fmea_fault_model_base_url
                if base_url:
                    _append_fault_id_link(paragraph, value, base_url)
                else:
                    paragraph += nodes.Text(value)
            else:
                paragraph += nodes.Text(value)
            cell += paragraph
            trow += cell

    return table


def setup(app):
    app.add_config_value("fmea_fault_model_base_url", "", "env")
    app.add_directive("fmea_xml_table", FmeaXmlTable)
    app.connect("doctree-resolved", _resolve_fmea_need_refs)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
