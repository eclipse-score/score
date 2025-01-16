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
        "itf.plugins.docker",
    ],
    args = [
        # Specify optional arguments, ex:
        "--docker-image=alpine:latest",
    ],
    # Optionally provide pytest.ini file, that will override the default one
    pytest_ini = "//my_pytest:my_pytest_ini",

    # Optionally provide tags the test should have, in order to allow for execution grouping
    tags = ["python", #...]
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

If you want to run only tests with a specific tag or tags you can do so via this command.

```
$ bazel test --test_tag_filters=python //..
```

This example will run all pytest configured tests that have the tag 'python'. 
If you want more tags, you can seperate them with a comma.  

```
$ bazel test --test_tag_filters=python,integration //..
```

The tests only have to have *one* of the tags mentioned to be able to be added to the run.
