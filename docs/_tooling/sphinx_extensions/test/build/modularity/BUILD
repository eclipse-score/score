load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("//tools/testing/pytest:defs.bzl", "score_py_pytest")

score_py_pytest(
    name = "test_modularity",
    size = "small",
    srcs = [
        "test_modularity.py",
    ],
    args = [
        "--basetemp /tmp/pytest",
        "-s",
    ],
    imports = ["."],
    plugins = [
        "sphinx.testing.fixtures",
    ],
    visibility = [
        "//visibility:public",
    ],
    deps = [
        "//docs/_tooling/sphinx_extensions/sphinx_extensions/build:modularity",
    ],
)
