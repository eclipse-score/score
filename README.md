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
1.  **Documentation builds** for building the documentation.
2. **IDE independent live preview** for live previews of documentation without IDE integration.
3. **IDE integration** for live previews, live warnings and even faster iterations.


```sh
bazel run //:docs 
```
The output will be located in `_build`


#### IDE independent live preview

For a documentation live preview independent of an IDE (CLI + browser only), `sphinx-autobuild` can be used.  
This will automatically rebuild the preview after save and have it available at `http://127.0.0.1:8000`  
```sh
bazel run //:live_preview 
```

#### IDE integration

For live previews, warnings, and linting during development, integrate Esbonio with your IDE (e.g., VS Code):

```sh
bazel run //:ide_support
```

VS Code: Install the Esbonio extension in VS Code. After installation, restart your IDE.
You should now have live preview available when you open a `.rst` file.  

> Note: if the extension was already installed when you ran the `ide_support` command,
you will need to restart your IDE.  

For features like type detection in conf.py or extensions,
point your IDE to the .venv_docs virtual environment.  
Re-run //docs:ide_support if you update Sphinx extensions or other dependencies.


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

> *Note: In order for a test to be picked up by this it has to be marked with the tag. Read more [here](/tools/testing/pytest/README.md)


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
* Bazel builds output in the `_build` directory (cmd: `bazel run //:docs`)
* Incremental builds output to _build, regardless of chosen way.

#### Troubleshooting
* Restart your IDE if live previews or warnings are not working after running ide_support.
* Ensure your virtual environment is up-to-date by re-running //docs:ide_support when dependencies
  change.
* Ensure you ran //:ide_support before executing //:format.check or //:format.fix
