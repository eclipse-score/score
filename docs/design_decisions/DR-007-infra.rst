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

- **Date:** 2026-02-02

.. dec_rec:: Move examples to docs-as-code repository
   :id: dec_rec__infra__dependency_docs_as_code
   :status: accepted
   :context: Infrastructure
   :decision: Option 5

Context / Problem
-----------------

Currently, there are two repositories defining the docs-as-code principles with Sphinx and Sphinx-Needs:

- The ``eclipse_score/process_description`` repository defines the process and the requirements for the meta model of the Sphinx-Needs objects (sphinx objects for requirements, architecture, processes, etc.).
  It includes also example Sphinx-Needs objects that illustrate the usage of the defined meta model.
- The ``eclipse_score/docs_as_code`` repository provides the base docs as code infrastructure and uses the process requirements to define the sphinx needs meta model and includes Sphinx-Needs objects from the process repository for testing.

However, the process repository also uses the ``docs_as_code`` repository's as infrastructure for the process documentation and the meta model for Sphinx-Needs objects, creating a **cyclic dependency** between the two repositories.
Any change in the process requirements (in ``process_description``) for the meta model possibly leads to a change in the docs-as-code meta model, but any change in the docs-as-code meta model can cause build errors in the process_description repo and this happens during the docs-as-code build as Sphinx-Needs objects from the process repo are imported.
This tight coupling makes maintenance and evolution of both repositories difficult and error-prone.

.. image:: img/DR-007-issue.drawio.svg
   :alt: Cyclic dependency between process and docs-as-code repositories
   :align: center

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- **Effort**: Don't spend much one-time effort to implement the change proposed here.
- **Independence**: Enable independent evolution of process requirements for the meta model and the meta model verification implementation.
- **UX**: Enable a process change rollout which does not require multiple pull requests in a single repository due to dependency cycles.
- **Maintainability**: Keep long-term maintenance effort low.

Non-Goals
~~~~~~~~~

- Redesigning the entire docs-as-code or process description approach.
- Removing Sphinx or Sphinx-Needs as documentation tools.


Options Considered
------------------

Option 0: No change
^^^^^^^^^^^^^^^^^^^

Keep the current repository structure and workflows as they are.
Accept the cyclic dependency between ``process_description`` and ``docs_as_code`` and manage it through careful coordination and communication between maintainers.
Continue handling build errors manually when they occur.

Effort 💚: None.

Independence 😡: The repos ``process_description`` and ``docs_as_code`` are coupled.

UX 😡: Poor due to the coupling some back and forth changes are necessary.

Maintainability 😡: Poor (ongoing coordination burden).


Option 1: Merge both repositories into one
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Combine ``process_description`` and ``docs_as_code`` into a single repository.
This eliminates the cyclic dependency by having a single source of truth for both the meta model and the Sphinx-Needs objects/examples, but process is repo is potentially large and complex and is implementation specific.

.. image:: img/DR-007-issue_option_1.drawio.svg
   :alt: Merged repository eliminating cyclic dependency
   :align: center

Effort 😡: Disruptive effort to merge repos.
Such changes conflict with practically all parallel pull requests.
Dependencies across all S-CORE repos are necessary.

Independence 💚: Coupling is tolerable because both can be changed as an atomic commit.

UX 💚: Excellent as single source.

Maintainability 💚: Good because everything is in one place.

Option 2: Move meta model definition to process repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define and maintain the `metamodel.yaml <https://github.com/eclipse-score/docs-as-code/blob/v2.3.3/src/extensions/score_metamodel/metamodel.yaml>`_
solely in the process repository.
The docs-as-code repository would then only provide the infrastructure for the meta model, not define or modify it.
The process repository would be the authoritative source for the meta model.
Also tests (scripts) and examples would be maintained there.

.. image:: img/DR-007-issue_option_2.drawio.svg
   :alt: Meta model defined in process repository
   :align: center

Implication:
If the docs-as-code module would select the metamodel yaml version on its own,
we would not have resolved the cyclic dependency issue.
Thus, ``process_description`` would need to define which version of ``metamodel.yaml`` to use
and ``docs_as_code`` provides a configuration option to specify it.

Effort 💛: Medium effort.

Independence 💚: Good because ``docs_as_code`` just consumes.

UX 💚: Excellent since authority is clear.

Maintainability 💚: Good because of clear ownership.

Option 3: Move examples (Sphinx-Needs objects) to a third repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extract all example Sphinx-Needs objects (currently imported into docs-as-code) into a separate third repository.
The process repository will become independent and docs-as-code repositories would depend on this third repository for examples, breaking the cyclic dependency.
But this adds complexity with an additional repository to maintain and still contains cyclic dependencies between all three repositories.

.. image:: img/DR-007-issue_option_3.drawio.svg
   :alt: Examples moved to a third repository
   :align: center

Effort 😡: High effort (new repo setup).

Independence 💚: Good because process repo becomes independent.

UX 😡: The number of pull requests might be as high as now.
Instead of multiple changes to the same repo, more repos must be changed.

Maintainability 😡😡: More repos to maintain.

Option 4: Move meta model and examples into a separate repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create or use a dedicated meta model repository that contains only the Sphinx-Needs meta model definitions and the examples.
Both the process repository and docs-as-code repository would depend on this meta model repository (if necessary), making it the single source of truth.
This breaks the cycle by introducing a clear hierarchical dependency structure.

.. image:: img/DR-007-issue_option_4.drawio.svg
   :alt: Meta model and examples in a separate repository
   :align: center

Effort 😡: High effort (new repo setup and migration).

Independence 💚: Good because process repo becomes independent.

UX 😡: The number of pull requests might be as high as now.
Instead of multiple changes to the same repo, more repos must be changed.

Maintainability 😡😡: More repos to maintain.

Option 5: Move examples to docs-as-code repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Move all example Sphinx-Needs objects from the process repository to the docs-as-code repository.
The process repository would define requirements for the meta model, while docs-as-code would provide infrastructure, the meta model and host the examples that demonstrate the meta model.
This breaks the cycle by removing the import dependency from docs-as-code back to the process repository.

.. image:: img/DR-007-issue_option_5.drawio.svg
   :alt: Examples moved to docs-as-code repository
   :align: center

Effort 💚: Low effort.

Independence 💚: Good because ``process_description`` just consumes.

UX 💚: Excellent since authority is clear.

Maintainability 💚: Good because of clear ownership.

Option 6: Change error handling from warnings as errors to warnings only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Keep the current repository structure but change the Sphinx build configuration in the docs-as-code repository to treat warnings as warnings instead of errors.
This would allow the build to succeed even when imported Sphinx-Needs objects from the process repository have inconsistencies with the meta model, effectively breaking the tight coupling that causes build failures.
The cyclic dependency would remain, but its impact would be reduced and only real errors like type name changes would cause build failures.
Please notice that missing mandatory links or fields, as well as additional links only generate warnings in this setup.
Only unknown types would still cause errors.

Effort 💚: Low effort because only config and documentation needs to be changed.

Independence 💚: Good because no errors are blocking anymore.

UX 💚: Easy because problems can be ignored.

Maintainability 😡: Poor because warnings won't be fixed as quickly as errors.

Evaluation
----------

How well each option achieves the goals in order of goal importance:

.. csv-table::
   :header: Goals, Option 0, Option 1, Option 2, Option 5, Option 6
   :widths: 20, 15, 15, 15, 15, 15

   Effort,          💚, 😡, 💛, 💚, 💚
   Independence,    😡, 💚, 💚, 💚, 💚
   UX,              😡, 💚, 💚, 💚, 💚
   Maintainability, 😡, 💚, 💚, 💚, 😡

Option 0 scores poorly with respect to independence, UX, and maintainability.
Option 1 requires high effort.
Option 6 compromises maintainability.

**Decision:** Option 2 or Option 5 both provide the same benefits but Option 5 requires less effort, so we pick it.
