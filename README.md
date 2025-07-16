# Score Platform

## Building

### Development environment
The build currently supports Linux environments.
Follow [instructions](https://eclipse-score.github.io/score/main/contribute/development/index.html) to set up your development environment.

Some important commands to get you started:

```sh
# Display useful bazel commands
bazel run //:help

# Check formatting
bazel test //:format.check

# Fix formatting
bazel run //:format.fix

# Check for license headers
bazel run //:copyright.check

# Fix license headers
bazel run //:copyright.fix
```

### Building Documentation

Score supports multiple methods for generating documentation, tailored to different workflows:
1. **Bazel-based builds** for clean, sandboxed outputs.
2. **Incremental builds** for quick iterations during development.
3. **IDE integration** for live previews, live warnings and even faster iterations.
4. **IDE independent live preview** for live previews of documentation without IDE integration.

#### Bazel-based Build

This method ensures clean and isolated documentation builds in a controlled Bazel environment.
It is best suited for CI pipelines or production-ready outputs, although it takes longer compared to
incremental builds.
Here it is possible to build it either with the current 'main' branch of [process](https://github.com/eclipse-score/process_description) or with the imported release version of it.


> Note: 'latest' might not work if it's executed behind a proxy or vpn. If this is the case please use 'release'


```sh
bazel build //docs:docs_latest # use current main branch of imported docs repositories (e.g. process_description)
bazel build //docs:docs_release # use release version imported in MODULE.bazel
```
The output will be located here,depending on which way was chosen: 
- bazel-bin/docs/docs_latest/_build/html. 
- bazel-bin/docs/docs_release/_build/html. 



#### Incremental build

For local changes and faster feedback, use the incremental build.
This method generates the documentation directly in the _build directory.

```sh
bazel run //docs:incremental_latest # use current main branch of imported docs repositories (e.g. process_description)
bazel run //docs:incremental_release # use release version imported in MODULE.bazel
```
Unlike IDE integration, which renders only the current file, this approach is ideal for quickly
verifying edits across the entire documentation during development.


#### IDE integration

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

#### IDE independent live preview

For a documentation live preview independent of an IDE (CLI + browser only), `sphinx-autobuild` can be used.
This will automatically rebuild the preview after save and have it available at http://127.0.0.1:8000
Release and latest are both available here as well.
```sh
bazel run //docs:live_preview_latest # use current main branch of imported docs repositories (e.g. process_description)
bazel run //docs:live_preview_release # use release version imported in MODULE.bazel
```


### Testing

Use the following command to run all available tests:

```sh
$ bazel test //...
```

However it's also  possible to run specific tests or set of tests.

To run all tests of a certain language use the command below, here an example for python.
```sh
$ bazel query 'kind(py.*, tests(//...))' | xargs bazel tests
```

Grouping of tests via tags is also supported:
```sh
$ bazel test --test_tag_filters=docs-build
```
You can add as many tags as you like, as long as a test has at least one of the tags it will be executed.
*Note: In order for a test to be picked up by this it has to be marked with the tag. Read more [here](/tools/testing/pytest/README.md)


### Test coverage for Python

To generate coverage data for Python test targets, run the following command:
```sh
bazel coverage --combined_report=lcov //docs:score_metamodel_test
```
This generates a coverage file `_coverage_report.dat` in the folder `bazel-out/_coverage` for the Python test target `//docs:score_metamodel_test`.
Replace the target to execute coverage for a different test target.

You can use the tool `genhtml` to generate an HTML report as follows:
```sh
genhtml --ignore-errors mismatch --branch-coverage --output genhtml "$(bazel info output_path)/_coverage/_coverage_report.dat"
```
This generates an HTML report in the folder `genhtml` which shows both line and branch coverage. Open file `genhtml/index.html` in a browser to show the report.

The tool `genhtml` is part of the `lcov` toolchain (https://github.com/linux-test-project/lcov).
You can install it on Debian/Ubuntu system as follows:
```sh
sudo apt update
sudo apt install lcov
```


### Notes
#### Output Locations
* Bazel builds output, depending on which build was chosen:
    - bazel-bin/docs/docs_latest/_build/html. 
    - bazel-bin/docs/docs_release/_build/html. 
* Incremental builds output to _build, regardless of chosen way.

#### Troubleshooting
* Restart your IDE if live previews or warnings are not working after running ide_support.
* Ensure your virtual environment is up-to-date by re-running //docs:ide_support when dependencies
  change.
* Ensure you ran //docs:ide_support before executing //:format.check or //:format.fix
