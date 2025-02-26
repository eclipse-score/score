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
import subprocess
import os
import argparse
import collections
import functools
import json
from typing import Optional
from pathlib import Path


TAGS = [
    "# req-traceability:",
    "# req-Id:",
]

GITHUB_BASE_URL = "https://github.com/eclipse-score/score/blob/"


def get_git_hash(file_path: str) -> str:
    """
    Grabs the latest git hash found for perticular file

    Args:
        file_path (str): Filepath of for which the githash should be retrieved.

    Returns:
        (str): Full 40char length githash of the latest commit this file was changed.

        Example:
                3b3397ebc2777f47b1ae5258afc4d738095adb83
    """
    try:
        abs_path = Path(file_path).resolve()
        if not os.path.isfile(abs_path):
            print(f"File not found: {abs_path}", flush=True)
            return "file_not_found"
        result = subprocess.run(
            ["git", "log", "-n", "1", "--pretty=format:%H", "--", abs_path],
            cwd=Path(abs_path).parent,
            capture_output=True,
        )
        decoded_result = result.stdout.strip().decode()

        # sanity check
        assert all(c in "0123456789abcdef" for c in decoded_result)
        return decoded_result
    except Exception as e:
        print(f"Unexpected error: {abs_path}: {e}", flush=True)
        return "error"


def extract_requirements(
    source_file: str, git_hash_func: Optional[callable] = get_git_hash
) -> dict[str, list]:
    """
    This extracts the file-path, lineNr as well as the git hash of the file where a tag was found.

    Args:
        source_file (str): path to source file that should be parsed.
        git_hash_func (Optional[callable]): Optional parameter only supplied during testing. If left empty func 'get_git_hash' is used.

    Returns:
        # TODO: change these links
        Returns dictionary per file like this:
        {
            "TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_types": [
                    https://github.com/eclipse-score/score/blob/3b3397ebc2777f47b1ae5258afc4d738095adb83/_tooling/extensions/score_metamodel/utils.py,
                    ... # further found places of the same ID if there are any
                ]
            "TOOL_REQ__toolchain_sphinx_needs_build__...": [
                    https://github.com/eclipse-score/score/blob/3b3397ebc2777f47b1ae5258afc4d738095adb83/_tooling/extensions/score_metamodel/checks/id.py,
                    ... # places where this ID as found
            ]
        }
    """
    requirement_mapping = collections.defaultdict(list)
    with open(source_file, "r") as f:
        for line_number, line in enumerate(f):
            line_number = line_number + 1
            line = line.strip()
            if any(x in line for x in TAGS):
                hash = git_hash_func(source_file)
                cleaned_line = (
                    line.replace("'", "").replace('"', "").replace(",", "").strip()
                )
                check_tag = cleaned_line.split(":")[1].strip()
                if check_tag:
                    req_id = cleaned_line.split(":")[-1].strip()
                    link = f"{GITHUB_BASE_URL}{hash}/{source_file}#L{line_number}"
                    requirement_mapping[req_id].append(link)
    return requirement_mapping


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    parser.add_argument("inputs", nargs="*")

    args, _ = parser.parse_known_args()
    requirement_mappings = collections.defaultdict(list)
    for input in args.inputs:
        with open(input, "r") as f:
            for source_file in f:
                rm = extract_requirements(source_file.strip())
                for k, v in rm.items():
                    requirement_mappings[k].extend(v)
    with open(args.output, "w") as f:
        f.write(json.dumps(requirement_mappings, indent=2))
