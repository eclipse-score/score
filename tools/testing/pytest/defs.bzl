"""ITF public Bazel interface"""

load("@score_pytest//bazel:py_pytest.bzl", local_py_pytest = "py_pytest")

py_pytest = local_py_pytest
