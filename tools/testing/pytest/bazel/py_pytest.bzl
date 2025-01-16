"""Bazel interface for running pytest"""

load("@pytest_pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_test")

def py_pytest(name, srcs, args = [], data = [], deps = [], plugins = [], pytest_ini = None, **kwargs):
    pytest_bootstrap = Label("@score_pytest//:main.py")

    if not pytest_ini:
        pytest_ini = Label("@score_pytest//:pytest.ini")

    plugins = ["-p %s" % plugin for plugin in plugins]

    py_test(
        name = name,
        srcs = [
            pytest_bootstrap,
        ] + srcs,
        main = pytest_bootstrap,
        args = args +
               ["-c $(location %s)" % pytest_ini] +
               [
                   "-p no:cacheprovider",
                   "--show-capture=no",
               ] +
               plugins +
               ["$(location %s)" % x for x in srcs],
        deps = [
            requirement("pytest"),
        ] + deps,
        data = [
            pytest_ini,
        ] + data,
        env = {
            "PYTHONDONOTWRITEBYTECODE": "1",
        },
        **kwargs
    )
