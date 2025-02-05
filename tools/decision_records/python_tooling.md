# Decision Record: Python Tooling

## Context
Selection of Python development tools for consistent code quality and maintainability, regarding the following categories:

- Code formatting and linting
- Type checking and static analysis
- Testing and coverage

## Decision
| Category | Selected Tool | Purpose |
|----------|---------------|----------|
| Formatting & Linting | [Ruff](https://github.com/astral-sh/ruff) | Code style enforcement |
| Type Checking | [pyright](https://github.com/microsoft/pyright) | Static type analysis |
| Testing | [pytest](https://github.com/pytest-dev/pytest/) | Test framework |
| Coverage | [pytest-cov](https://github.com/pytest-dev/pytest-cov) | Test coverage reporting |
| Static Analysis | [pylint](https://github.com/pylint-dev/pylint) | Code quality analysis |


### Tool Selection Criteria
- Established open-source adoption
- Team familiarity and consensus
- High test coverage (verified)
  - pyright: 99% (local verification)
  - pytest: 97% ([source](https://app.codecov.io/gh/pytest-dev/pytest))
  - pylint: 96% ([source](https://app.codecov.io/gh/pylint-dev/pylint))

### Alternatives Considered

#### Formatting & Linting
- Flake8: Replaced by Ruff's equivalent functionality
- Black: Integrated into Ruff
- Pylint: Retained for static analysis, but using Ruff for linting due to speed

#### Type Checking
- mypy: 

#### Testing
- unittest: Limited feature set
- hypothesis: Team unfamiliarity

#### Coverage
- coverage.py: 
- radon: Team unfamiliarity
