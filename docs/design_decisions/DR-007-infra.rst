..
   Copyright (c) 2025 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-007-Infra: Solution for cyclic dependencies between docs-as-code and process description
===========================================================================================

- **Date:** 2026-01-26

.. dec_rec:: Design decision for cyclic dependencies between docs-as-code and process description
   :id: dec_rec__infra__dependency_docs_as_code
   :status: proposed
   :context: Infrastructure
   :decision: open

Context / Problem
-----------------

Currently, there are two repositories defining the docs-as-code principles with Sphinx and Sphinx-Needs:

- The **process description repository** defines the requirements and the meta model for the Sphinx-Needs objects (requirements, architecture, processes, etc.). It includes also example Sphinx-Needs objects that illustrate the defined meta model.
- The **docs-as-code repository** provides the base docs as code infrastructure and uses the process requirements to define the sphinx needs meta model and includes Sphinx-Needs objects from the process repository for testing.

However, the process repository also uses the docs-as-code repository's as infrastructure for the rocess documentation and the meta model for Sphinx-Needs objects, creating a **cyclic dependency** between the two repositories. Any change in the process requirements (in the process repo) leads to a change in the docs-as-code meta model, but any change in the docs-as-code meta model can cause build errors in the process_description repo and this happens during the docs-as-code build as Sphinx-Needs objects from the process repo are imported. This tight coupling makes maintenance and evolution of both repositories difficult and error-prone.

.. image:: img/DR-007-issue.drawio.svg
   :alt: Cyclic dependency between process and docs-as-code repositories
   :align: center

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- Avoid cyclic dependencies between repositories.
- Enable independent evolution of process requirements and meta model definitions.
- Ensure that example Sphinx-Needs objects and meta model definitions remain consistent and buildable.
- Minimize build errors and maintenance overhead.

Non-Goals
~~~~~~~~~

- Redesigning the entire docs-as-code or process description approach.
- Removing Sphinx or Sphinx-Needs as documentation tools.


Options Considered
------------------

Option 0: No change
^^^^^^^^^^^^^^^^^^^
Keep the current repository structure and workflows as they are. Accept the cyclic dependency between the process description and docs-as-code repositories and manage it through careful coordination and communication between maintainers. Continue handling build errors manually when they occur.


Option 1: Merge both repositories into one
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Combine the process description and docs-as-code repositories into a single repository. This eliminates the cyclic dependency by having a single source of truth for both the meta model and the Sphinx-Needs objects/examples.

.. image:: img/DR-007-issue_option_1.drawio.svg
   :alt: Merged repository eliminating cyclic dependency
   :align: center


Option 2: Move meta model definition to process repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Define and maintain the Sphinx-Needs meta model solely in the process repository. The docs-as-code repository would then only provide the infrastructure for the meta model, not define or modify it. The process repository would be the authoritative source for the meta model. Also tests and examples would be maintained there.

.. image:: img/DR-007-issue_option_2.drawio.svg
   :alt: Meta model defined in process repository
   :align: center

Option 3: Move examples (Sphinx-Needs objects) to a third repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Extract all example Sphinx-Needs objects (currently imported into docs-as-code) into a separate third repository. The process repository will become independent and docs-as-code repositories would depend on this third repository for examples, breaking the cyclic dependency. But this adds complexity with an additional repository to maintain and still contains cyclic dependencies between all three repositories.

.. image:: img/DR-007-issue_option_3.drawio.svg
   :alt: Examples moved to a third repository
   :align: center

Option 4: Move meta model and examples into a separate repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create or use a dedicated meta model repository that contains only the Sphinx-Needs meta model definitions and the examples. Both the process repository and docs-as-code repository would depend on this meta model repository (if necessary), making it the single source of truth. This breaks the cycle by introducing a clear hierarchical dependency structure.

.. image:: img/DR-007-issue_option_4.drawio.svg
   :alt: Meta model and examples in a separate repository
   :align: center

Option 5: Move examples to docs-as-code repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Move all example Sphinx-Needs objects from the process repository to the docs-as-code repository. The process repository would define requirements for the meta model, while docs-as-code would provide infrastructure, the meta model and host the examples that demonstrate the meta model. This breaks the cycle by removing the import dependency from docs-as-code back to the process repository.

.. image:: img/DR-007-issue_option_5.drawio.svg
   :alt: Examples moved to docs-as-code repository
   :align: center

Option 6: Change error handling from warnings as errors to warnings only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Keep the current repository structure but change the Sphinx build configuration in the docs-as-code repository to treat warnings as warnings instead of errors. This would allow the build to succeed even when imported Sphinx-Needs objects from the process repository have inconsistencies with the meta model, effectively breaking the tight coupling that causes build failures. The cyclic dependency would remain, but its impact would be reduced and only real errors like type name changes would cause build failures. Please notice that missing mandatory links or fields, as well as additional links only generate warnings in this setup. Only unknown types would still cause errors.

Evaluation
----------

**Evaluation Criteria:**

- **Effort**: Implementation work required (time, resources, migration complexity).
- **UX**: User experience and ease of use for developers and maintainers.
- **Bureaucracy**: Administrative overhead and coordination requirements between repositories.
- **Speed**: How quickly the solution can be implemented and deployed.
- **Flexibility**: Ability to adapt and evolve the solution over time.
- **Independence**: Degree of decoupling between repositories and autonomous evolution.
- **Maintainability**: Long-term ease of maintaining and updating the solution.
- **Scalability**: Ability to handle growth in content, contributors, and complexity.

.. csv-table::
   :header: Criteria, Option 0, Option 1, Option 2, Option 3, Option 4, Option 5, Option 6
   :widths: 20, 10, 10, 10, 10, 10, 10, 10

   Effort, 💚, 😡, 😐, 😡, 😡, 💚, 💚
   UX, 😡, 💚, 💚, 😐, 😐, 💚, 😡
   Bureaucracy, 💚, 😐, 💚, 😡, 😡, 💚, 💚
   Speed, 💚, 😡, 💚, 😡, 😡, 💚, 💚
   Flexibility, 😡, 💚, 💚, 😐, 💚, 💚, 😐
   Independence, 😡, 😐, 💚, 💚, 💚, 💚, 😡
   Maintainability, 😡, 💚, 💚, 😐, 💚, 💚, 😡
   Scalability, 😡, 😐, 😐, 😡, 💚, 😐, 😡

**Rationale:**

- **Option 0 (No change)**: No effort required, poor UX (frequent build failures), low bureaucracy (current process), immediate (no implementation needed), poor flexibility (locked into current structure), poor independence (cyclic dependency remains), poor maintainability (ongoing coordination burden), poor scalability (problem worsens as repos grow).
- **Option 1 (Merge)**: High effort to merge repos, but excellent UX (single source), good maintainability (everything in one place), moderate scalability (single repo can become large).
- **Option 2 (Meta model to process repo)**: Low effort, excellent UX (clear authority), low bureaucracy, fast implementation, good flexibility (centralized control), good independence (docs-as-code just consumes), good maintainability (clear ownership), moderate scalability (single authority may become bottleneck).
- **Option 3 (Third repo for examples)**: High effort (new repo setup), moderate UX (more repos to navigate), high bureaucracy (three repos to coordinate), slow implementation, moderate flexibility (still dependencies), good independence (process repo becomes independent), moderate maintainability (three repos to maintain), poor scalability (complexity increases with more repos).
- **Option 4 (Separate meta model repo)**: High effort (new repo setup and migration), moderate UX (clear separation but another repo), high bureaucracy (third repo to coordinate), slow implementation, good flexibility (dedicated meta model evolution), excellent independence (clear hierarchy), good maintainability (focused responsibility), excellent scalability (clean separation of concerns).
- **Option 5 (Examples to docs-as-code)**: Low effort (moving examples only), excellent UX (examples with infrastructure), low bureaucracy (two repos), fast implementation, good flexibility (examples can evolve with infrastructure), good independence (process repo independent), good maintainability (examples maintained where used), moderate scalability (docs-as-code repo grows with examples), but no examples in the process description.
- **Option 6 (Warnings only)**: Very low effort (config change only), poor UX (silent failures, inconsistencies not caught), low bureaucracy (no structural change), very fast implementation, moderate flexibility (doesn't address root cause), poor independence (cyclic dependency remains), poor maintainability (masks problems instead of solving them), poor scalability (technical debt accumulates).

**Recommendation:** Option 2 (moving the meta model to the process repository) provides the best balance of low effort, fast implementation, and clear ownership. It directly breaks the cyclic dependency by making the process repo authoritative for both requirements and meta model, with the docs-as-code repo serving purely as infrastructure.
