# Score Project Tooling Development Guide

*This document is meant for *developers* of the `_tooling` aspect of the score repository.*  
It should be treated as a 'get-started' guide, giving you all needed information to get up and running.

## Quick Start

1. Install Bazelisk (version manager for Bazel)
2. Clone the repository  
3. Setup the environment
- *No Devcontainer*
    1. Create the Python virtual environment:
   ```bash
   bazel run //docs:ide_support
   ```
    2. Select `.venv_docs/bin/python` as the python interpreter inside your IDE  
    *Note: This virtual environment does **not** have pip, therefore `pip install` is not available.*  
<br>

- *With Devcontainer (VSCode)*
    1. Click the `reopen current folder in dev container` prompt
        -  If no prompt appears: `ctrl+shift+p` => `Dev Containers: Reopen in Containers`


## Development Environment Requirements

- **Operating System**: Linux (required)
- **Core Tools**:
  - Bazel 7.4.0 (via Bazelisk)
  - Python 3.12
  - Git


### Key external tools used inside `_tooling`

1. **Bazel Build System**
   - Version: 7.4.0
   - Primary build orchestrator
   - Handles dependency management
   - Coordinates testing and documentation
   - Manages multi-repository setup

2. **Documentation Tools**
   - Sphinx with custom extensions
   - Esbonio 0.16.5 for IDE integration
   - Real-time documentation validation

3. **Development Tools**
   - Gitlint for commit message standards
   - Pytest for testing infrastructure
   - Custom formatters and linters



## Tooling Directory Architecture

```
docs/_tooling/
├── assets/           # Documentation styling (CSS)
├── conf_extras/      # Sphinx configuration extensions
├── decision_records/ # Architecture Decision Records (ADRs)
├── extensions/       # Custom Sphinx extensions
│   └── score_metamodel/
│       ├── checks/  # Sphinx-needs validation
│       └── tests/   # Extension test suite
└── templates/        # Documentation templates
```

## Development Workflow


#### Documentation Development
```bash
# Incremental documentation build (recommended during development)
bazel run //docs:incremental

# Full documentation build
bazel build //docs:docs
```

#### Testing
```bash
# Run all tests
bazel test //...

# Run specific test suite
bazel test //docs:<test_suite_name>
```

#### Code Quality
```bash
# Format checking
bazel test //:format.check

# Auto-format code
bazel run //:format.fix

# Copyright headers check
bazel run //:copyright.check
bazel run //:copyright.fix
```

### Adding New Test Suites

To add a new test suite to the build system:

1. Create a new entry in `docs/BUILD`:
```python
py_library(
    name = "your_tool",
    srcs = glob(["_tooling/your_tool/**/*.py"]),
    imports = ["required_imports"],
    visibility = ["//visibility:public"],
)

score_py_pytest(
    name = "your_tool_test",
    size = "small",  # small/medium/large
    srcs = glob(["_tooling/your_tool/tests/**/*.py"]),
    deps = [":your_tool"],
)
```

2. Run your tests:
```bash
bazel test //docs:your_tool_test
```

## Developing new tools

1. Place code in appropriate directory or create new ones. E.g. sphinx-extensions inside `extensions`
2. Create a dedicated test directory
3. Include an appropriate README in markdown

> If you want to develop your own sphinx extension, check out the [extensions guide](/docs/_tooling/docs/extension_guide.md)

## Best Practices

1. **Documentation**
   - Keep READMEs up-to-date
   - Document architectural decisions in `decision_records/`
   - Include examples in extension documentation

2. **Testing**
   - Write tests for all new functionality
   - Use appropriate test sizes (small/medium/large)
   - Include both positive and negative test cases

3. **Code Organization**
   - Follow existing directory structure
   - Keep extensions modular and focused
   - Use consistent naming conventions

## Troubleshooting

Common issues and solutions:

1. **Bazel Build Failures**
   - Check Bazel version compatibility
   - Verify Python environment
   - Review recent changes to BUILD files

2. **Documentation Build Issues**
   - Validate Sphinx configuration
   - Check for RST syntax errors
   - Verify extension dependencies

## Additional Resources
- [Sphinx extension guide](/docs/_tooling/docs/extension_guide.md)
- [Score Metamodel Documentation](/docs/_tooling/extensions/score_metamodel/README.md)
- [Pytest Integration Guide](/tools/testing/pytest/README.md)
