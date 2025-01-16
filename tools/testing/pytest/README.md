# Score pytest wrapper

This module implements support for running [pytest](https://docs.pytest.org/en/latest/contents.html) based tests.

## Usage
MODULE.bazel
```
bazel_dep(name = "score_pytest", version = "0.1")
```

BUILD
```
load("@score_pytest//:defs.bzl", "py_pytest")

py_pytest(
    name = "test_my_first_check",
    srcs = [
        "test_my_first_check.py"
    ],
    plugins = [
        # Specify optional plugins, that will register their fixtures
    ],
    args = [
        # Specify optional arguments, ex:
        "--basetemp /tmp/pytest",
    ],
    # Optionally provide pytest.ini file, that will override the default one
    pytest_ini = "//my_pytest:my_pytest_ini",

    # Optionally provide tags the test should have, in order to allow for execution grouping
    tags = ["integration", #...]
)
```

## Development

### Regenerating pip dependencies
```
$ bazel run //:requirements.update
```

### Running test
```
$ bazel test //test/...
```
