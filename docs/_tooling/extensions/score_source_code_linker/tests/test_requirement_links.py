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
from collections import defaultdict
from score_source_code_linker.parse_source_files import (
    get_git_hash,
    extract_requirements,
    GITHUB_BASE_URL,
)


@pytest.fixture(scope="session")
def create_tmp_files(tmp_path_factory):
    root_dir = tmp_path_factory.mktemp("test_root")
    test_file_contents = """ 


def implementation_1():
    pass

# req-Id: TEST_REQ__LINKED_ID
def implementation_tagged():
    pass

# req-traceability: TEST_REQ__LINKED_TRACE
def implementation_tagged_2():
    pass 
"""
    with open(root_dir / "testfile.txt", "w") as f:
        f.write(test_file_contents)

    test_file_contents2 = """ 

# req-Id: TEST_REQ__LINKED_DIFFERENT_FILE
def implementation_separate():
    pass
"""
    with open(root_dir / "testfile2.txt", "w") as f:
        f.write(test_file_contents2)
    test_file_contents3 = """ 

def implementation_14():
    pass

def implementation_4():
    pass

# comments
def implementation_4():
    pass
        """
    with open(root_dir / "testfile3.txt", "w") as f:
        f.write(test_file_contents3)
    return root_dir


def dummy_git_hash_func(input):
    return lambda _: input


def test_extract_requirements(create_tmp_files):
    root_dir = create_tmp_files

    results_dict1 = extract_requirements(
        root_dir / "testfile.txt", dummy_git_hash_func("no-hash")
    )
    expected_dict1 = defaultdict(list)
    expected_dict1["TEST_REQ__LINKED_ID"].append(
        f"{GITHUB_BASE_URL}no-hash/{root_dir}/testfile.txt#L7"
    )
    expected_dict1["TEST_REQ__LINKED_TRACE"].append(
        f"{GITHUB_BASE_URL}no-hash/{root_dir}/testfile.txt#L11"
    )

    # Assumed random hash here to test if passed correctly
    results_dict2 = extract_requirements(
        root_dir / "testfile2.txt",
        dummy_git_hash_func("aacce4887ceea1f884135242a8c182db1447050"),
    )
    expected_dict2 = defaultdict(list)
    expected_dict2["TEST_REQ__LINKED_DIFFERENT_FILE"].append(
        f"{GITHUB_BASE_URL}aacce4887ceea1f884135242a8c182db1447050/{root_dir}/testfile2.txt#L3"
    )

    results_dict3 = extract_requirements(root_dir / "testfile3.txt")
    expected_dict3 = defaultdict(list)

    # if there is no git-hash returned from command. This happens if the file is new and not commited yet.
    results_dict4 = extract_requirements(
        root_dir / "testfile2.txt", dummy_git_hash_func("")
    )
    expected_dict4 = defaultdict(list)
    expected_dict4["TEST_REQ__LINKED_DIFFERENT_FILE"].append(
        f"{GITHUB_BASE_URL}/{root_dir}/testfile2.txt#L3"
    )

    assert results_dict1 == expected_dict1
    assert results_dict2 == expected_dict2
    assert results_dict3 == expected_dict3
    assert results_dict4 == expected_dict4


def test_get_git_hash():
    assert get_git_hash("testfile.x") == "file_not_found"
    assert get_git_hash("") == "file_not_found"
