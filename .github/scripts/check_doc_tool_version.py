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

#!/usr/bin/env python3
"""Docs-as-Code version consistency checker."""

import argparse
import re
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Check Doc-as-Code version consistency")
    parser.add_argument(
        "--doc",
        type=Path,
        help="Path to the documentation file (default: docs/score_tools/doc_as_code.rst)"
    )
    parser.add_argument(
        "--dac-module-name",
        default="score_docs_as_code",
        help="Module name to search for in MODULE.bazel (default: score_docs_as_code)"
    )
    args = parser.parse_args()

    ROOT = Path(__file__).resolve().parents[2]
    MODULE = ROOT / "MODULE.bazel"
    DOC = args.doc if args.doc else ROOT / "docs/score_tools/doc_as_code.rst"

    if not DOC.exists() or not MODULE.exists():
        raise SystemExit(f"Missing {DOC} or {MODULE}. Nothing to compare.")

    # Parse MODULE.bazel
    module_bazel = MODULE.read_text(encoding="utf-8")
    module_bazel_match = re.search(
        rf'bazel_dep\(\s*name\s*=\s*"{re.escape(args.dac_module_name)}",\s*version\s*=\s*"([^"\s]+)"',
        module_bazel,
    )
    module_bazel_version = module_bazel_match.group(1) if module_bazel_match else ""

    # Parse doc_as_code.rst
    doc_as_code_rst = DOC.read_text(encoding="utf-8")
    doc_match = re.search(r':version:\s*(\S+)', doc_as_code_rst)
    doc_version_raw = doc_match.group(1) if doc_match else ""
    doc_version = doc_version_raw.lstrip("vV") if doc_version_raw else ""

    # Compare versions
    mismatch = not module_bazel_version or not doc_version or module_bazel_version != doc_version

    comment = ""
    if mismatch:
        comment = "\n".join(
            [
                "Warning: Doc-as-Code version mismatch detected.",
                "",
                f"- MODULE.bazel version: {module_bazel_version or '(not found)'}",
                f"- doc_as_code.rst :version:: {doc_version_raw or '(not found)'}",
                "",
                "Please align the documentation with the Bazel dependency.",
            ]
        )

    if comment:
        print(comment)

    sys.exit(1 if mismatch else 0)

if __name__ == "__main__":
    main()
