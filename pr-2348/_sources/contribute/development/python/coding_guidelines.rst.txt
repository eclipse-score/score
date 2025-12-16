..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

Writing Python Code
###################

.. document:: Coding Guidelines Python
  :id: doc__python_coding_guidelines
  :status: valid
  :safety: QM
  :security: NO
  :realizes: wp__sw_development_plan

Coding Guidelines
=================
.. warning:: Python is not meant to be used directly in safety critical systems. The following guidelines are only meant for tooling.
   Every tool written will need to be evaluated for safety criticallity (TCL).


**Consistency within score matters more than personal preference**.

The art lies in balancing completeness of this document vs keeping it short, since frankly, no one
will read a long document. Let's focus on issues that actively come up in real life and are worth
discussing and agreeing upon, not on things that *might* be important.

We don't want to write a book here. And we don't have to, since Python is not used for safety
critical systems. However, to provide sufficient argumentation for code quality when it comes to
tool qualification it is necessary to have and actively use guidelines.

This guide is a **living document**—keep it concise, relevant, and practical.

We assume basic programming and software-engineering know-how and will not repeat basics here! Go
ask Google or ChatGPT. Or one of these established Python best practice websites:

- `PEP 8 <https://pep8.org/>`_
- `The Hitchhiker's Guide to Python <https://docs.python-guide.org/>`_
- `Real Python <https://realpython.com/>`_

Comments
--------
- The first rule of comments is to write them **only when something is worth explaining**.
- Comments should explain *why* the code does something, not *what* it does.
- Avoid redundant comments: if the code is clear enough, a comment is not needed.
- Take the user's perspective when writing docstrings

Testing
-------
- **Readability:** For some reason, people tend to forget all they have ever learned about
  readability when writing tests. **Tests do not have tests.** They must be even more readable than
  production code!
- **Mocking is an anti-pattern.** Well... it's complex. We don't want to write a book on mocking
  here. Just really, really consider whether mocking is the best approach. - Favor dependency
  injection and lightweight fixtures over excessive mocking. Mocks should not replace proper
  design.
- **Do not test every single function or class!** Instead: - Focus on testing *behavior*, not
  implementation details. Overly fine-grained tests lead to brittle code and high maintenance.
- **Boundary conditions:** - Edge cases often break things. Think about invalid input, large data
  sets, empty cases, and concurrency issues.

Documentation
--------------------
- If your documentation doesn't fit into a comment, create a `README.md` in the directory of the
  tool.
- `README.md` should explain the overall architecture and key design decisions.
- If the design impacts multiple components, consider an architecture diagram.
- User-facing documentation is stored under `docs/guidance`.

Type Annotations
----------------
Type annotations in Python improve code readability and enable static type checking.
We use `pyright <https://github.com/eclipse-score/score/blob/main/pyproject.toml>`_
for type checks (currently only in IDEs).

- Annotate **all function parameters**.
- Ensure **pyright can always infer the type**, using annotations, ``cast()``, or other means.
- Prefer **modern type hints (PEP 585+)**:
  - Use ``list[int]`` instead of ``List[int]``
  - Use ``int | None`` instead of ``Optional[int]``
- Use **generic types**, especially for APIs, not concrete containers:
  - Prefer ``Sequence[str]`` or ``Iterable[str]`` over ``list[str]``
  - Prefer ``Mapping[str, Any]`` over ``dict[str, Any]``

This guideline is intentionally short. For details, refer to the `pyright config
<https://github.com/eclipse-score/score/blob/main/pyproject.toml>`_.


Tools & Versions
================

We're using Python, Ruff (linting & formatting), Pyright (linting) and pytest for our tooling. The
versions are managed by the infrastructure community and will be updated as frequently as possible.
The configuration is managed by infrastructure and process communities.

*Compliance to all tools is mandatory, and will be enforced by pull request checks.*
