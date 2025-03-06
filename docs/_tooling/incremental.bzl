"""Defines Bazel rules for running incremental docs build."""

load("@aspect_rules_py//py:defs.bzl", "py_binary")
load("@pip_sphinx//:requirements.bzl", "all_requirements")
load("//docs:BUILD", "plantuml_for_python") # TODO temp @unused

# Maintain either a central "sphinx_requirements".
sphinx_requirements = all_requirements + [
    "@rules_python//python/runfiles", ":plantuml_for_python"
]

def incremental_binary(name = "incremental", extra_dependencies = list()):
    """
    Creates a py_binary target for the incremental tool.

    Args:
        name: Optional custom name for the target. Defaults to "incremental".
        extra_dependencies: Additional dependencies besides the centrally maintained "sphinx_requirements".
    """
    # global sphinx_requirements
    dependencies = sphinx_requirements + extra_dependencies

    py_binary(
        name = name,
        srcs = ["incremental.py"],
        # data = [":collected_files_for_score_source_code_linker"],
        deps = dependencies,
    )
