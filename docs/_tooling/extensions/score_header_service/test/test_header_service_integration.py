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
from collections.abc import Callable
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
import score_header_service.header_service as hs
from pytest import TempPathFactory
from sphinx.testing.util import SphinxTestApp


@pytest.fixture(scope="session", autouse=True)
def add_metadata(record_testsuite_property: Callable[[str, str | list[str]], None]):
    record_testsuite_property("Verifies", ["GD__automatic_document_header_generation"])
    record_testsuite_property(
        "Description", "It should check the generation of the header information."
    )
    record_testsuite_property("ASIL", "ASIL_D")
    record_testsuite_property("Priority", "1")
    record_testsuite_property("TestType", "Requirements-based test")
    record_testsuite_property("DerivationTechnique", "Analysis of requirements")


@pytest.fixture(scope="session")
def sphinx_base_dir(tmp_path_factory: TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("sphinx")


@pytest.fixture(scope="session")
def sphinx_app_setup(
    sphinx_base_dir: Path,
) -> Callable[[str, str, str, dict[str, Any] | None], SphinxTestApp]:
    def _create_app(
        conf_content: str,
        rst_content: str,
        template_content: str,
        conf_overrides: dict[str, Any] | None = None,
    ) -> SphinxTestApp:
        conf_overrides = conf_overrides or {}
        src_dir = sphinx_base_dir / "src"
        src_dir.mkdir(exist_ok=True)
        template_folder = sphinx_base_dir / "_templates"
        template_folder.mkdir(exist_ok=True)
        (template_folder / "header.need").write_text(template_content)
        (src_dir / "conf.py").write_text(conf_content)
        (src_dir / "index.rst").write_text(rst_content)
        conf_overrides.update(
            {
                "needs_template_folder": str(template_folder),
                "templates_path": str(template_folder),
            }
        )

        return SphinxTestApp(
            freshenv=True,
            srcdir=Path(src_dir),
            confdir=Path(src_dir),
            outdir=sphinx_base_dir / "out",
            buildername="html",
            warningiserror=False,
            confoverrides=conf_overrides,
        )

    return _create_app


@pytest.fixture(scope="session")
def basic_conf():
    def wrapper(use_github_data: bool = True):
        return f"""
extensions = [
    "sphinx_needs",
    "score_header_service",
]
needs_types = [
    dict(title = "Review Header", directive = "review_header", color="#BFD8D2", style="node",
        prefix = "review_header__"),
]
needs_id_regex = ".*"
needs_extra_options = [
    "security",
    "safety",
    "rationale",
    "reqtype",
    "codelink",
    "testlink",
    "reqcovered",
    "testcovered",
    "hash",
    "author",
    "reviewers",
    "approvers",
]
header_service_use_github_data = {use_github_data}
"""

    return wrapper


@pytest.fixture(scope="session")
def basic_needs():
    return """
TESTING HEADER SERVICE
======================

.. needservice:: header-service

"""


@pytest.fixture(scope="session")
def template_needs():
    return """
.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - **DOCUMENT IDENTIFICATION**
     -
   * - Document Type
     - Checklist
   * - Document ID
     - DPX-CONTR-REVIEW-CHECKLIST
   * - Project Name
     - Dependix
   * - ASIL
     - B
   * - Security Classification
     - CONFIDENTIAL
   * - Author
     - {{ author }}
   * - Reviewer
     -
{%- for r in reviewers.split(", ") %}
       | {{ r -}}
{% endfor %}
   * - Approver
     -
{%- for a in approvers.split(", ") %}
       | {{ a -}}
{% endfor %}
   * - Version
     - {{ hash }}
   * - Status
     - RELEASED
"""


@patch("score_header_service.header_service.generate_hash")
@patch("score_header_service.header_service._extract_github_data")
def test_header_service_integration_github_data(
    mock_extract_github_data: MagicMock,
    mock_generate_hash: MagicMock,
    sphinx_app_setup: Callable[[str, str, str, dict[str, Any] | None], SphinxTestApp],
    basic_conf: Callable[[], str],
    basic_needs: str,
    template_needs: str,
):
    github_data = {
        "author": "John Doe",
        "approvers": "approver_1",
        "reviewers": "reviewer_1",
        "hash": "abcdef",
    }
    mock_generate_hash.return_value = "abcdef"
    mock_extract_github_data.return_value = github_data
    mock_basic_conf = basic_conf()
    app: SphinxTestApp = sphinx_app_setup(
        mock_basic_conf, basic_needs, template_needs, None
    )
    try:
        app.build()
        html_content: str = (app.outdir / "index.html").read_text()
        mock_extract_github_data.assert_called_once()
        assert "John Doe" in html_content
        assert "approver_1" in html_content
        assert "reviewer_1" in html_content
        assert "abcdef" in html_content
    except Exception as err:
        raise AssertionError(f"Build failed: {err}") from err


@patch("score_header_service.header_service.generate_hash")
@patch("score_header_service.header_service._extract_merge_commit_data")
def test_header_service_integration_commit_data(
    mock_extract_merge_commit_data: MagicMock,
    mock_generate_hash: MagicMock,
    sphinx_app_setup: Callable[[str, str, str, dict[str, Any] | None], SphinxTestApp],
    basic_needs: str,
    template_needs: str,
    basic_conf: Callable[..., Any],
):
    github_data = {
        "author": "John Doe",
        "approvers": "approver_1",
        "reviewers": "reviewer_1",
        "hash": "abcdef",
    }
    mock_generate_hash.return_value = "abcdef"
    mock_extract_merge_commit_data.return_value = github_data
    mock_basic_conf = basic_conf(use_github_data=False)
    app: SphinxTestApp = sphinx_app_setup(
        mock_basic_conf, basic_needs, template_needs, None
    )
    try:
        app.build()
        html_content: str = (app.outdir / "index.html").read_text()
        mock_extract_merge_commit_data.assert_called_once()
        assert "John Doe" in html_content
        assert "approver_1" in html_content
        assert "reviewer_1" in html_content
        assert "abcdef" in html_content
    except Exception as err:
        raise AssertionError(f"Build failed: {err}") from err
