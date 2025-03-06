"""Defines Bazel targets for running docs related actions."""

load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_venv")
load("@pip_sphinx//:requirements.bzl", "all_requirements")
load("@rules_java//java:defs.bzl", "java_binary")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
# load("//docs:BUILD", "plantuml_for_python") # TODO temp @unused

sphinx_requirements = all_requirements + ["@rules_python//python/runfiles", ":plantuml_for_python"]

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
        srcs = ["_tooling/bzl/incremental.py"],
        data = [":collected_files_for_score_source_code_linker"],
        deps = dependencies,
    )

def plantuml_bzl():
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
        srcs = ["_tooling/dummy.py"],
        data = [
            ":plantuml",
        ],
    )

def live_preview():
    py_binary(
        name = "live_preview",
        srcs = ["_tooling/live_preview.py"],
        deps = sphinx_requirements,
    )


def ide_support():
    py_venv(
        name = "ide_support",
        venv_name = ".venv_docs",
        deps = sphinx_requirements,
    )


def docs():
    sphinx_docs(
        name = "docs",
        srcs = native.glob([
            "**/*.png",
            "**/*.svg",
            "**/*.rst",
            "**/*.html",
            "**/*.css",
            "**/*.puml",
            # Include the docs tooling itself
            # Note: we don't use py_library here to make it as close as possible to docs:incremental.
            "**/*.py",
            "**/*.yaml",
            "**/*.json",
        ]),
        config = "conf.py",
        extra_opts = [
            "-W",
            "--keep-going",
            # This is 'overwriting' the configuration parameter inside sphinx. As we only get this information during runtime
            "--define=source_code_linker_file=$(location :collected_files_for_score_source_code_linker)",
        ],
        formats = [
            "html",
        ],
        sphinx = ":sphinx_build",
        tags = [
            "manual",
        ],
        tools = [
            ":collected_files_for_score_source_code_linker",
            ":plantuml",
        ],
    )

    sphinx_build_binary(
        name = "sphinx_build",
        deps = sphinx_requirements 
    )
