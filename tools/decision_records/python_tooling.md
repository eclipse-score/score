# Decision Record: Python Tooling Selection

## Status
Agreed

## Context
Selection of Python development tools needs to be made to aid in consistent code quality and maintainability across our codebase.   
This decision covers core development tool selection in these categories:

- Code formatting and linting
- Type checking and static analysis
- Testing and coverage

Note: Tool configurations will be determined in a separate decision record.

## Decision
We will use the following tools:

| Category | Selected Tool | Purpose |
|----------|---------------|----------|
| Formatting & Linting | Ruff | Fast code style enforcement and formatting |
| Type Checking | pyright | Static type analysis |
| Testing | pytest | Test framework |
| Coverage | pytest-cov | Test coverage reporting |
| Static Analysis | pylint | Code quality analysis |

### Tool Selection Criteria
Our tools were chosen based on:
- Established open-source adoption and stability
- Team familiarity and consensus
- Proven reliability through their own test coverage:
  - pyright: 99% (local verification)
  - pytest: 97% (codecov.io verification)
  - pylint: 96% (codecov.io verification)

### Tools Compatibility
All selected tools support Python version 3.12 used inside the project.

### Alternatives Considered

#### Formatting & Linting
- Flake8: While well-established, Ruff provides equivalent functionality with significantly better performance
- Black: Now integrated into Ruff, making a separate Black installation unnecessary
- Using only Pylint: While we're keeping Pylint for static analysis, Ruff's speed makes it superior for day-to-day linting

#### Type Checking
- mypy: While mypy is the original Python type checker, pyright was chosen for:
  - Better performance on large codebases
  - More detailed error messages
  - VS Code integration through Pylance

#### Testing
- unittest: Rejected due to:
  - Limited fixture support
  - More verbose test writing
  - Fewer plugins compared to pytest
- hypothesis: Features it provides are currently not needed; this, in combination with team unfamiliarity, makes pytest the better option

#### Coverage
- coverage.py: Chose pytest-cov for direct pytest integration and simpler workflow
- radon: More focused on complexity metrics than coverage reporting, which doesn't match our immediate needs
