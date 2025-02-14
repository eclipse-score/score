# Score Platform

## Building

### Supported environment
The build currently supports Linux environments.

### Use bazelisk for bazel version management
Follow [instructions](https://github.com/bazelbuild/bazelisk) and setup bazelisk to manage your bazel version based on the .bazelversion file.

### Check and fix formatting
```
$ bazel test //:format.check
$ bazel run //:format.fix
```

## Documentation

Score supports multiple methods for generating documentation, tailored to different workflows:
1. **Bazel-based builds** for clean, sandboxed outputs.
2. **Incremental builds** for quick iterations during development.
3. **IDE integration** for live previews, live warnings and even faster iterations.
4. **IDE independent live preview** for live previews of documentation without IDE integration.

### Bazel-based Build

This method ensures clean and isolated documentation builds in a controlled Bazel environment.
It is best suited for CI pipelines or production-ready outputs, although it takes longer compared to
incremental builds.

```sh
bazel build //docs:docs
```
The output will be located in bazel-bin/docs/docs/_build/html.


### Incremental build

For local changes and faster feedback, use the incremental build.
This method generates the documentation directly in the _build directory.

```sh
bazel run //docs:incremental
```
Unlike IDE integration, which renders only the current file, this approach is ideal for quickly
verifying edits across the entire documentation during development.


### IDE integration

For live previews, warnings, and linting during development,
integrate Esbonio with your IDE (e.g., VS Code):

```sh
bazel run //docs:ide_support
```

VS Code: Install the Esbonio extension in VS Code. After installation, restart your IDE.
You should now have live preview available when you open a `.rst` file.
Note: if the extension was already installed when you ran the `ide_support` command,
you will need to restart your IDE.

For features like type detection in conf.py or extensions,
point your IDE to the .venv_docs virtual environment.

Re-run //docs:ide_support if you update Sphinx extensions or other dependencies.

### IDE independent live preview

For a documentation live preview independent of an IDE (CLI + browser only), `sphinx-autobuild` can be used.
This will automatically rebuild the preview after save and have it available at http://127.0.0.1:8000

```sh
bazel run //docs:live_preview
```


### Testing

Use the following command to run all available tests:

```
$ bazel test //...
```

However it's also  possible to run specific tests or set of tests.

To run all tests of a certain language use the command below, here an example for python.
```
$ bazel query 'kind(py.*, tests(//...))' | xargs bazel tests
```

Grouping of tests via tags is also supported:
```
$ bazel test --test_tag_filters=docs-build
```
You can add as many tags as you like, as long as a test has at least one of the tags it will be executed.
*Note: In order for a test to be picked up by this it has to be marked with the tag. Read more [here](/tools/testing/pytest/README.md)


### Notes
#### Output Locations
* Bazel builds output to bazel-bin/docs/docs/_build/html.
* Incremental builds output to _build.

#### Troubleshooting
* Restart your IDE if live previews or warnings are not working after running ide_support.
* Ensure your virtual environment is up-to-date by re-running //docs:ide_support when dependencies
  change.
