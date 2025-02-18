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
import pytest
import json
from types import SimpleNamespace
from pathlib import Path
from sphinx_needs.data import SphinxNeedsData
from sphinx.testing.util import SphinxTestApp
from docs._tooling.extensions.score_feature_flag_handling import read_filter_tags


#                    ╭──────────────────────────────────────────────────────────────────────────────╮
#                    │                                  Unit Tests                                  │
#                    ╰──────────────────────────────────────────────────────────────────────────────╯
def test_read_filter_tags(sphinx_base_dir, caplog):
    feature_flags_dir = sphinx_base_dir / "feature_flags"
    feature_flags_dir.mkdir(exist_ok=True)
    tag_str = "some-ip, feature1, feature2"
    (feature_flags_dir / "filter_tags.txt").write_text(tag_str)

    # filter_tags_file_path happy path
    fake_app_ok = SimpleNamespace()
    fake_app_ok.config = SimpleNamespace()
    fake_app_ok.config.filter_tags_file_path = str(
        feature_flags_dir / "filter_tags.txt"
    )

    # When filter_tags_file_path is not set
    fake_app_path_missing = SimpleNamespace()
    fake_app_path_missing.config = SimpleNamespace()

    # When filter_tags_file_path is empty
    fake_app_path_empty = SimpleNamespace()
    fake_app_path_empty.config = SimpleNamespace()
    fake_app_path_empty.config.filter_tags_file_path = ""

    assert ["some-ip", "feature1", "feature2"] == read_filter_tags(fake_app_ok)

    with pytest.raises(AssertionError):
        read_filter_tags(fake_app_path_missing)

    with pytest.raises(FileNotFoundError) as exc_info:
        read_filter_tags(fake_app_path_empty)
        assert "could not read file: " in caplog.text
        assert "Error: " in caplog.text


#                    ╭──────────────────────────────────────────────────────────────────────────────╮
#                    │                         Integration Tests via Sphinx                         │
#                    ╰──────────────────────────────────────────────────────────────────────────────╯


@pytest.fixture(scope="session")
def sphinx_base_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("sphinx")


@pytest.fixture(scope="session")
def sphinx_app_setup(sphinx_base_dir):
    def _create_app(conf_content, rst_content, filter_tags=None):
        src_dir = sphinx_base_dir / "src"
        src_dir.mkdir(exist_ok=True)

        (src_dir / "conf.py").write_text(conf_content)
        (src_dir / "index.rst").write_text(rst_content)
        (src_dir / "filter_tags.txt").write_text(filter_tags)

        app = SphinxTestApp(
            freshenv=True,
            srcdir=Path(src_dir),
            confdir=Path(src_dir),
            outdir=sphinx_base_dir / "out",
            buildername="html",
            warningiserror=True,
            confoverrides={"filter_tags_file_path": str(src_dir / "filter_tags.txt")},
        )

        return app

    return _create_app


@pytest.fixture(scope="session")
def positive_filter_tags():
    return "test-feat, some-ip"


@pytest.fixture(scope="session")
def negative_filter_tags():
    return "tag1, tag2"


@pytest.fixture(scope="session")
def empty_filter_tags():
    return ""


@pytest.fixture(scope="session")
def basic_conf():
    return """ 
extensions = [
    "sphinx_needs",
    "score_feature_flag_handling",
]
needs_types = [
    dict(directive="test_req", title="Testing Requirement", prefix="TREQ_", color="#BFD8D2", style="node"),
    dict(directive="tool_req", title="Tooling Requirement", prefix="TOOL_", color="#BFD8D2", style="node"),
]
needs_extra_links = [
    {
        "option": "satisfies",
        "incoming": "is satisfied by",
        "outgoing": "satisfies",
        "style_start": "-up",
        "style_end": "->",
    }
]
"""


@pytest.fixture(scope="session")
def basic_rst_file():
    return """
.. tool_req:: Test Tool Requirement
   :id: TOOL_REQ_1
   :tags: test-feat, feature1
   :satisfies: TEST_REQ_1, TEST_REQ_20

   Some content for the tool requirement

.. test_req:: Testing Requirement 1
   :id: TEST_REQ_1 
   :tags: test-feat

   Some content should be here

.. test_req:: Testing Requirement 20
   :id: TEST_REQ_20
   :tags: feature1

   More content, this one is different

.. needtable:: Testtable
  :tags: test-feat, feature1
"""


def test_modularity_hide_ok(
    sphinx_app_setup, basic_conf, basic_rst_file, positive_filter_tags, sphinx_base_dir
):
    app = sphinx_app_setup(basic_conf, basic_rst_file, positive_filter_tags)
    try:
        app.build()
        Needs_Data = SphinxNeedsData(app.env)
        needs_data = {x["id"]: x for x in Needs_Data.get_needs_view().values()}
        html = (app.outdir / "index.html").read_text()

        assert "TOOL_REQ_1" in needs_data
        assert "TEST_REQ_1" in needs_data
        assert "TEST_REQ_20" in needs_data
        assert needs_data["TOOL_REQ_1"]["hide"] == False
        assert needs_data["TOOL_REQ_1"]["satisfies"] == ["TEST_REQ_20"]
        assert needs_data["TEST_REQ_1"]["hide"] == True
        assert needs_data["TEST_REQ_20"]["hide"] == False

        assert "TOOL_REQ_1" in html
        assert "TEST_REQ_20" in html
        # making sure we do not see this in the final HTML
        # (neither as an element, nor as a link)
        assert "TEST_REQ_1" not in html
    finally:
        app.cleanup()


def test_modularity_hide_no_match(
    sphinx_app_setup, basic_conf, basic_rst_file, negative_filter_tags, sphinx_base_dir
):
    app = sphinx_app_setup(basic_conf, basic_rst_file, negative_filter_tags)
    try:
        app.build()
        Needs_Data = SphinxNeedsData(app.env)
        needs_data = {x["id"]: x for x in Needs_Data.get_needs_view().values()}
        html = (app.outdir / "index.html").read_text()

        assert "TOOL_REQ_1" in needs_data
        assert "TEST_REQ_1" in needs_data
        assert "TEST_REQ_20" in needs_data
        assert needs_data["TEST_REQ_1"]["hide"] == False
        assert needs_data["TEST_REQ_20"]["hide"] == False
        assert needs_data["TOOL_REQ_1"]["hide"] == False
        assert needs_data["TOOL_REQ_1"]["satisfies"] == ["TEST_REQ_1", "TEST_REQ_20"]

        assert "TOOL_REQ_1" in html
        assert "TEST_REQ_1" in html
        assert "TEST_REQ_20" in html
    finally:
        app.cleanup()


def test_modularity_hide_no_filters(
    sphinx_app_setup, basic_conf, basic_rst_file, empty_filter_tags, sphinx_base_dir
):
    app = sphinx_app_setup(basic_conf, basic_rst_file, empty_filter_tags)
    try:
        app.build()
        Needs_Data = SphinxNeedsData(app.env)
        needs_data = {x["id"]: x for x in Needs_Data.get_needs_view().values()}
        html = (app.outdir / "index.html").read_text()

        # The outcome should be the same as when we found no matches, just ensuring it doesn't error and nothing was changed
        assert "TOOL_REQ_1" in needs_data
        assert "TEST_REQ_1" in needs_data
        assert "TEST_REQ_20" in needs_data
        assert needs_data["TEST_REQ_1"]["hide"] == False
        assert needs_data["TEST_REQ_20"]["hide"] == False
        assert needs_data["TOOL_REQ_1"]["hide"] == False
        assert needs_data["TOOL_REQ_1"]["satisfies"] == ["TEST_REQ_1", "TEST_REQ_20"]

        assert "TOOL_REQ_1" in html
        assert "TEST_REQ_1" in html
        assert "TEST_REQ_20" in html
    finally:
        app.cleanup()
