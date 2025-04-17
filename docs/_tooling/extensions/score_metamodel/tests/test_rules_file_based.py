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

import os
import shutil
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp

from docs._tooling.extensions.score_metamodel import (
    graph_check_function,
    local_check_function,
)

RST_DIR = Path(__file__).absolute().parent / "rst"
DOCS_DIR = Path(__file__).absolute().parent.parent.parent.parent.parent
TOOLING_DIR_NAME = "_tooling"

### List of relative paths of all rst files in RST_DIR
RST_FILES = [str(f.relative_to(RST_DIR)) for f in Path(RST_DIR).rglob("*.rst")]


@pytest.fixture
def sphinx_base_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    ### Create a temporary directory for Sphinx and copy all necessary files.
    base_dir: Path = tmp_path_factory.mktemp("docs")
    shutil.copy(RST_DIR / "conf.py", base_dir)
    shutil.copytree(
        DOCS_DIR / TOOLING_DIR_NAME,
        base_dir / TOOLING_DIR_NAME,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("*.rst"),
    )
    return base_dir


@pytest.fixture
def index_file() -> Callable[[Path], str]:
    ### Returns a function that creates an index.rst file.
    def _create_rst_file(rst_file: Path) -> str:
        ### returns an index.rst file with a toctree
        # that refers to the given rst file.
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
    ### Returns a function that creates a SphinxTestApp instance.
    def _create_app(rst_file: Path) -> SphinxTestApp:
        ### Create a SphinxTestApp instance.
        # The source directory is set to the temporary directory.
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
class WarningInfo:
    #### Class to hold information about warnings
    # Contains the line number and the expected and not expected warnings.
    lineno: int = 0
    expected: list[str] = field(default_factory=list)
    not_expected: list[str] = field(default_factory=list)


@dataclass
class RstData:
    #### Holds filename, all infos about warnings and
    # which checks to enable if not all
    filename: str
    checks: list[str] = field(default_factory=list)
    warning_infos: list[WarningInfo] = field(default_factory=list)


def extract_warning(line: str) -> str:
    #### Extract the warning message from the line
    # The line format is "#EXPECT: <warning message>"
    # or "#EXPECT-NOT: <warning message>"
    return line.split(": ", 1)[1].strip()


def extract_test_data(rst_file: Path) -> RstData | None:
    ### Extract test data from the given rst file
    # The function returns a list of WarningInfo objects
    # containing the line number and the expected and not expected warnings.
    # If no test data is found, it returns None.
    rst_data = RstData(filename=rst_file.name)
    with open(rst_file) as f:
        test_info: WarningInfo | None = None
        for no, line in enumerate(f, start=1):
            if line.startswith(".. "):  # Beginning of new need
                if test_info:
                    test_info.lineno = no
                    rst_data.warning_infos.append(test_info)
                    test_info = None
            elif line.startswith("#EXPECT:") or line.startswith("#EXPECT-NOT:"):
                if test_info is None:
                    test_info = WarningInfo()
                target_list = (
                    test_info.expected
                    if line.startswith("#EXPECT:")
                    else test_info.not_expected
                )
                target_list.append(extract_warning(line))
            elif line.startswith("#CHECK:"):
                assert not rst_data.checks, "only one CHECK per file allowed"
                rst_data.checks = extract_warning(line).split(",")
        # Check last InfoElement
        if test_info:
            print("ERROR: CHECK or EXPECT statement without according need found")
        return rst_data


def warning_matches(
    rst_data: RstData,
    warning_info: WarningInfo,
    expected_message: str,
    warnings: list[str],
) -> bool:
    ### Checks if any element of the warning list is includes the given warning info.
    # It returns True if found otherwise False.
    for warning in warnings:
        if (
            f"{rst_data.filename}:{str(warning_info.lineno)}" in warning
            and expected_message in warning
        ):
            return True
    return False


def apply_enabled_check_filter(
    checks: dict[str, list[local_check_function | graph_check_function]],
    enabled_checks: list[str],
):
    if enabled_checks:
        checks["local_checks"] = [
            check
            for check in checks["local_checks"]
            if check.__name__ in enabled_checks
        ]
        checks["graph_checks"] = [
            check
            for check in checks["graph_checks"]
            if check.__name__ in enabled_checks
        ]


@pytest.mark.parametrize("rst_file", RST_FILES)
def test_check_rules(
    rst_file: str, sphinx_app_setup: Callable[[Path], SphinxTestApp]
) -> None:
    ### Test function to check rules in the given rst file
    # The function uses the SphinxTestApp to build the documentation
    # and checks for the expected/unexpected warnings.
    assert (rst_data := extract_test_data(RST_DIR / rst_file)), (
        "Unable to extract test data"
    )
    app: SphinxTestApp = sphinx_app_setup(RST_DIR / rst_file)
    os.chdir(app.srcdir)  # Change working directory to the source directory

    apply_enabled_check_filter(app.config.score_metamodel_checks, rst_data.checks)

    app.build()
    warnings = app.warning.getvalue().splitlines()
    for warning_info in rst_data.warning_infos:
        for expected in warning_info.expected:
            assert warning_matches(rst_data, warning_info, expected, warnings), (
                f"Expected warning: {expected} not found"
            )
        for not_expected in warning_info.not_expected:
            assert not warning_matches(
                rst_data, warning_info, not_expected, warnings
            ), f"Unexpected warning: {not_expected} found"
