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
from dataclasses import dataclass, field
import os
from sphinx.testing.util import SphinxTestApp
from sphinx_needs.data import SphinxNeedsData
import pytest
from pathlib import Path
import shutil

RST_DIR = Path(__file__).absolute().parent / "rst"
DOCS_DIR = Path(__file__).absolute().parent.parent.parent.parent.parent
TOOLING_DIR_NAME = "_tooling"

RST_FILES = [str(f.relative_to(RST_DIR)) for f in Path(RST_DIR).rglob("*.rst")]


@pytest.fixture
def sphinx_base_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    base_dir: Path = tmp_path_factory.mktemp("docs")
    shutil.copy(DOCS_DIR / "conf.py", base_dir)
    shutil.copytree(
        DOCS_DIR / TOOLING_DIR_NAME,
        base_dir / TOOLING_DIR_NAME,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("*.rst"),
    )
    return base_dir


@pytest.fixture
def index_file() -> Callable[[Path], str]:
    def _create_rst_file(rst_file: Path) -> str:
        index_rst: str = f"""
.. toctree::
   {rst_file.stem}
"""
        return index_rst

    return _create_rst_file


@pytest.fixture
def sphinx_app_setup(
    sphinx_base_dir: Path, index_file: Callable[[Path], str]
) -> Callable[[Path], SphinxTestApp]:
    def _create_app(rst_file: Path) -> SphinxTestApp:
        shutil.copy(rst_file, sphinx_base_dir)
        index_context: str = index_file(rst_file)
        (sphinx_base_dir / "index.rst").write_text(index_context)
        app: SphinxTestApp = SphinxTestApp(
            freshenv=True,
            srcdir=sphinx_base_dir,
            outdir=sphinx_base_dir / "out",
            buildername="html",
        )
        return app

    return _create_app


@dataclass
class InfoElement:
    lineno: int = 0
    expected: list[str] = field(default_factory=list)
    not_expected: list[str] = field(default_factory=list)


def extract_warning(line: str) -> str:
    return line.split(": ", 1)[1].strip()


def extract_test_data(rst_file: Path) -> list[InfoElement] | None:
    with open(rst_file, "r") as f:
        statements: list[InfoElement] = []
        test_info: InfoElement | None = None
        for no, line in enumerate(f, start=1):
            if line.startswith(".. "):  # Beginning of new need
                if test_info:
                    test_info.lineno = no
                    statements.append(test_info)
                test_info = None
            elif line.startswith("#EXPECT:") or line.startswith("#EXPECT-NOT:"):
                if test_info is None:
                    test_info = InfoElement()
                target_list = (
                    test_info.expected
                    if line.startswith("#EXPECT:")
                    else test_info.not_expected
                )
                target_list.append(extract_warning(line))
        # Check last InfoElement
        if test_info:
            print("ERROR: Teststatement without according need found")
        return statements
    return None


@pytest.mark.parametrize("rst_file", RST_FILES)
def test_check_rules(
    rst_file: str, sphinx_app_setup: Callable[[Path], SphinxTestApp]
) -> None:
    assert (
        test_data := extract_test_data(RST_DIR / rst_file)
    ), "Unable to extract test data"
    app: SphinxTestApp = sphinx_app_setup(RST_DIR / rst_file)
    try:
        os.chdir(app.srcdir)  # Change working directory to the source directory
        app.build()
        warn_text: str = app.warning.getvalue()
        for test in test_data:
            for expected in test.expected:
                assert (
                    f"{Path(rst_file).name}:{test.lineno}: WARNING: {expected}"
                    in warn_text
                ), f"Expected warning: {[expected]} not found"
            for not_expected in test.not_expected:
                assert (
                    f"{Path(rst_file).name}:{test.lineno}: WARNING: {not_expected}"
                    not in warn_text
                ), f"Unexpected warning: {[not_expected]} found"
    except Exception as e:
        assert False, f"Build failed: {e}"
    finally:
        app.cleanup()
