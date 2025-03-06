"""Defines Bazel targets for running docs related actions."""

load("@aspect_rules_py//py:defs.bzl", "py_binary")
load("@pip_sphinx//:requirements.bzl", "all_requirements")
load("//docs:BUILD", "plantuml_for_python") # TODO temp @unused

sphinx_requirements = all_requirements + [
    "@rules_python//python/runfiles", ":plantuml_for_python"
]

def incremental(name = "incremental", extra_dependencies = list()):
    """
    A target for building docs incrementally at runtime.

    Args:
        name: Optional custom name for the target. Defaults to "incremental".
        extra_dependencies: Additional dependencies besides the centrally maintained "sphinx_requirements".
    """
    dependencies = sphinx_requirements + extra_dependencies

    py_binary(
        name = name,
        srcs = ["incremental.py"],
        # data = [":collected_files_for_score_source_code_linker"],
        deps = dependencies,
    )

def plantuml():
    # ⚠️ TODO: function not "tested" yet, pseudo code!

    java_binary(
        name = "plantuml",
        jvm_flags = ["-Djava.awt.headless=true"],
        main_class = "net.sourceforge.plantuml.Run",
        runtime_deps = [
            "@plantuml//jar",
        ],
    )

    # Note: this is the old comment. copy pasted here.

    # This makes it possible for py_venv to depend on plantuml.
    # Note: py_venv can only depend on py_library.
    # TODO: Investigate if this can be simplified with a custom bzl rule
    #       which replaces / wraps py_venv.
    #       see https://github.com/aspect-build/rules_py/blob/main/py/private/py_venv.bzl
    #       see https://github.com/bazelbuild/rules_python/blob/main/sphinxdocs/private/sphinx.bzl
    py_library(
        name = "plantuml_for_python",
        srcs = ["dummy.py"],
        data = [
            ":plantuml",
        ],
    )
