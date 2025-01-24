import pytest
import json
from pathlib import Path
from sphinx_needs.data import SphinxNeedsData
from sphinx.testing.util import SphinxTestApp


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
    "modularity",
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

        # The outcome should be the same as when we found no matches, just making sure it doesn't error and nothing happens
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
