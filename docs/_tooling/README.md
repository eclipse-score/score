# Score Project Tooling Guide

This document will offer an overview and help to get started with setting up and navigating the development environment for the tooling of the Score project.

## Table of Contents
- [Development Environment Overview](#development-environment-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up Your Environment](#setting-up-your-environment)
- [Build System](#build-system)
  - [Bazel Commands](#bazel-commands)
  - [Documentation Generation](#documentation-generation)
- [Development Tools](#development-tools)
  - [Python Development](#python-development)
  - [Testing Framework](#testing-framework)
- [Project Structure](#project-structure)
- [Additional Resources](#additional-resources)

## Development Environment Overview


- **Bazel (7.4.0)**: Primary build system
  - Managed through Bazelisk for version control
  - Handles documentation building
  - Manages dependencies and versioning
  - Enables multi-repository setup
  - Coordinates test execution

- **Python (3.12)**: Used for documentation and testing
  - Integrated with Bazel
  - Powers Sphinx documentation
  - Supports pytest-based testing

- **Esbonio (0.16.5)**: Sphinx/RST documentation support
  - Provides real-time documentation warnings
  - Enables IDE integration

## Getting Started


>**Score currently supports Linux environments**

### Setting Up Your Environment

1. Install Bazelisk following the [official instructions](https://github.com/bazelbuild/bazelisk)
2. Clone the Score repository
3. Set up IDE support (detailed below)

## Build System

### Bazel Commands

Here are the most commonly used Bazel commands:

```bash
# Build documentation in sandbox mode
bazel build //docs:docs

# Run incremental documentation build
bazel run //docs:incremental

# Generate the python virtual environment
bazel run //docs:ide_support

# Run all tests
bazel test //...

# Check formatting
bazel test //:format.check

# Fix formatting issues
bazel test //:format.fix

# Check copyright headers
bazel run //:copyright.check

# Fix copyright headers
bazel run //:copyright.fix
```

### Documentation Generation

Score offers three approaches to documentation generation:

1. **Sandboxed Builds** (Clean, isolated environment)
   ```bash
   bazel build //docs:docs
   ```
   Output location: `bazel-bin/docs/docs/_build/html`

2. **Incremental Builds** (Fast development iterations)
   ```bash
   bazel run //docs:incremental
   ```
   Output location: `_build` directory

3. **IDE Integration** (Live preview and warnings)
   - Requires Esbonio setup => [IDE Setup/Integration]()
   - Provides real-time feedback


## Development Tools

### Python Development

To set up a Python development environment that matches the Bazel sandbox:

1. Generate the virtual environment:
   ```bash
   bazel run //docs:ide_support
   ```

2. Select `.venv_docs/bin/python` as your IDE's Python interpreter

This setup provides:
- Consistent import paths with Bazel
- IDE features (code navigation, completion)
- Standard Python development experience

### Testing Framework

Score uses pytest for Python testing, integrated with Bazel. You can:

- Run all tests:
  ```bash
  bazel test //...
  ```

- Run language-specific tests:
  ```bash
  bazel query 'kind(py.*, tests(//...))' | xargs bazel test
  ```

- Run tests by tag:
  ```bash
  bazel test --test_tag_filters=docs-build
  ```

## Project Structure

The project's tooling is organized in two main directories:

### 1. docs/_tooling/
```
docs/_tooling/
├── assets/           # CSS files for documentation
├── conf_extras/      # Extra sphinx configurations
├── decision_records/ # Architecture decisions
├── extensions/       # Custom sphinx extensions
│   └── score_metamodel/
│       ├── checks/  # Custom sphinx-needs checks
│       └── tests/   # Test suite
└── templates/        # Documentation templates
```

### 2. tools/
Contains general development tools (formatters, testing frameworks, etc.). 
```
tools
├── cr_checker # copyright checker integration
│   ├── resources # configurations used by cr_checker
│   └── tool # cr_checker implementation
├── format # implementation of formatters
└── testing
    └── pytest # pytest integration
```
See the [tools README](tools/README.md) for details.

## Additional Resources

- [Score Metamodel Documentation](/docs/_tooling/extensions/score_metamodel/README.md)
- [Tools Documentation](/tools/README.md)
- [IDE Setup Guide]() (Coming soon)
- [Pytest Integration Guide](/tools/testing/pytest/README.md)

---

For specific tool documentation, refer to the README files in their respective directories as outlined in the project structure above.
