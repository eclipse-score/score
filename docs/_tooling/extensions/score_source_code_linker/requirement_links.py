import subprocess
import os
import argparse
import collections
import json
from typing import Optional
from pathlib import Path


TAGS = [
    "# req-traceability:",
    "# req-Id:",
]

GITHUB_BASE_URL = "https://github.com/eclipse-score/score/blob/"


def extract_requirements(
    source_file: str, git_hash_func: Optional[callable] = None
) -> dict[str, list]:
    """
    This extracts the file-path, lineNr as well as the git hash of the file where a tag was found.

    Args:
        source_file (str): path to source file that should be parsed.
        git_hash_func (Optional[callable]): Optional parameter only supplied during testing. If left empty func 'get_git_hash' is used.

    Returns:
        Returns dictionary per file like this:
        {
            "TOOL_REQ__toolchain_sphinx_needs_build__requirement_linkage_types": [
                    https://github.com/dependix/platform/blob/3b3397ebc2777f47b1ae5258afc4d738095adb83/tools/sphinx_extensions/sphinx_extensions/utils.py,
                    ... # further found places of the same ID if there are any
                ]
            "TOOL_REQ__toolchain_sphinx_needs_build__...": [
                    https://github.com/dependix/platform/blob/3b3397ebc2777f47b1ae5258afc4d7wadhjalk83/tools/sphinx_extensions/build/build.py,
                    ... # places where this ID as found
            ]
        }
    """
    requirement_mapping = collections.defaultdict(list)
    get_hash = git_hash_func if git_hash_func is not None else get_git_hash
    with open(source_file, "r") as f:
        for line_number, line in enumerate(f):
            line_number = line_number + 1
            line = line.strip()
            if any(x in line for x in TAGS):
                hash = get_hash(source_file)
                req_id = line.split()[-1].strip()
                link = f"{GITHUB_BASE_URL}{hash}/{source_file}#L{line_number}"
                requirement_mapping[req_id].append(link)
    return requirement_mapping


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
        # HACK: could not think of a better way to get the root directory.
        platform_path = abs_path.__str__().split("platform")[0] + "platform"
        if not os.path.isfile(abs_path):
            print(f"File not found: {abs_path}", flush=True)
            return "file_not_found"
        result = subprocess.run(
            ["git", "log", "-n", "1", "--pretty=format:%H", "--", abs_path],
            cwd=platform_path,
            capture_output=True,
        )
        decoded_result = result.stdout.strip().decode()

        # sanity check
        assert all(c in "0123456789abcdef" for c in decoded_result)
        return decoded_result
    except Exception as e:
        print(f"Unexpected error: {abs_path}: {e}", flush=True)
        return "error"


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
