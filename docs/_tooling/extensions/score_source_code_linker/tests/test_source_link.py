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
import json
from pathlib import Path

import pytest
from score_source_code_linker.parse_source_files import GITHUB_BASE_URL
from sphinx.testing.util import SphinxTestApp
from sphinx_needs.data import SphinxNeedsData


@pytest.fixture(scope="session")
def sphinx_base_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("sphinx")


@pytest.fixture(scope="session")
def sphinx_app_setup(sphinx_base_dir):
    def _create_app(conf_content, rst_content, requierments_text=None):
        src_dir = sphinx_base_dir / "src"
        src_dir.mkdir(exist_ok=True)

        (src_dir / "conf.py").write_text(conf_content)
        (src_dir / "index.rst").write_text(rst_content)
        (src_dir / "requierments.txt").write_text(json.dumps(requierments_text))

        return SphinxTestApp(
            freshenv=True,
            srcdir=Path(src_dir),
            confdir=Path(src_dir),
            outdir=sphinx_base_dir / "out",
            buildername="html",
            warningiserror=True,
            confoverrides={
                "source_code_linker_file": str(src_dir / "requierments.txt")
            },
        )

    return _create_app


@pytest.fixture(scope="session")
def basic_conf():
    return """
extensions = [
    "sphinx_needs",
    "score_source_code_linker",
]
needs_types = [
    dict(
        directive="test_req",
        title="Testing Requirement",
        prefix="TREQ_",
        color="#BFD8D2",
        style="node",
    ),
]
needs_extra_options = ["source_code_link"]
needs_string_links = {
    "source_code_linker": {
        "regex": r"(?P<value>[^,]+)",
        "link_url": "{{value}}",
        "link_name": "Source Code Link",
        "options": ["source_code_link"],
    },
}
"""


@pytest.fixture(scope="session")
def basic_needs():
    return """
TESTING SOURCE LINK
===================

.. test_req:: TestReq1
   :id: TREQ_ID_1
   :status: valid

.. test_req:: TestReq2
   :id: TREQ_ID_2
   :status: open
"""


@pytest.fixture(scope="session")
def example_source_link_text_all_ok():
    return {
        "TREQ_ID_1": [
            f"{GITHUB_BASE_URL}aacce4887ceea1f884135242a8c182db1447050/tools/sources/implementation1.py#L2",
            f"{GITHUB_BASE_URL}/tools/sources/implementation_2_new_file.py#L20",
        ],
        "TREQ_ID_2": [
            f"{GITHUB_BASE_URL}f53f50a0ab1186329292e6b28b8e6c93b37ea41/tools/sources/implementation1.py#L18"
        ],
    }


@pytest.fixture(scope="session")
def example_source_link_text_non_existent():
    return {
        "TREQ_ID_200": [
            f"{GITHUB_BASE_URL}f53f50a0ab1186329292e6b28b8e6c93b37ea41/tools/sources/bad_implementation.py#L17"
        ],
    }


def test_source_link_integration_ok(
    sphinx_app_setup,
    basic_conf,
    basic_needs,
    example_source_link_text_all_ok,
    sphinx_base_dir,
):
    app = sphinx_app_setup(basic_conf, basic_needs, example_source_link_text_all_ok)
    try:
        app.build()
        Needs_Data = SphinxNeedsData(app.env)
        needs_data = {x["id"]: x for x in Needs_Data.get_needs_view().values()}
        assert "TREQ_ID_1" in needs_data
        assert "TREQ_ID_2" in needs_data
        # extra_options are only available at runtime
        assert (
            ",".join(example_source_link_text_all_ok["TREQ_ID_1"])
            == needs_data["TREQ_ID_1"]["source_code_link"]  # type: ignore
        )
        assert (
            ",".join(example_source_link_text_all_ok["TREQ_ID_2"])
            == needs_data["TREQ_ID_2"]["source_code_link"]  # type: ignore
        )
    finally:
        app.cleanup()


def test_source_link_integration_non_existent_id(
    sphinx_app_setup,
    basic_conf,
    basic_needs,
    example_source_link_text_non_existent,
    sphinx_base_dir,
):
    app = sphinx_app_setup(
        basic_conf, basic_needs, example_source_link_text_non_existent
    )
    try:
        app.build()
        warnings = app._warning.getvalue()
        assert (
            "WARNING: Could not find TREQ_ID_200 in the needs id's. Found in "
            "file(s): ['tools/sources/bad_implementation.py#L17']" in warnings
        )
    finally:
        app.cleanup()
