load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")
load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "modularity",
    srcs = glob(["modularity/*.py"]),
    imports = ["modularity"],
    visibility = [
        "//visibility:public",
    ],
    deps = [
        requirement("sphinx"),
        requirement("sphinx-needs"),
    ],
)
