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

- **Date:** 2026-02-04

.. dec_rec:: Move examples to module_template repository
   :id: dec_rec__infra__dependency_docs_as_code
   :status: accepted
   :context: Infrastructure
   :decision: Option 3

Context / Problem
-----------------

Currently, there are two repositories defining the docs-as-code principles with Sphinx and Sphinx-Needs:

- The ``eclipse_score/process_description`` repository defines the process and the requirements for the meta model of the Sphinx-Needs objects (sphinx objects for requirements, architecture, processes, etc.).
  It includes also example Sphinx-Needs objects that illustrate the usage of the defined meta model.
- The ``eclipse_score/docs_as_code`` repository provides the base docs as code infrastructure and uses the process requirements to define the sphinx needs meta model and includes Sphinx-Needs objects from the process repository for testing.

However, the process repository also uses the ``docs_as_code`` repository's as infrastructure for the process documentation and the meta model for Sphinx-Needs objects, creating a **cyclic dependency** between the two repositories.
Any change in the process requirements (in ``process_description``) for the meta model possibly leads to a change in the docs-as-code meta model, but any change in the docs-as-code meta model can cause build errors in the process_description repo and this happens during the docs-as-code build as Sphinx-Needs objects from the process repo are imported.
This tight coupling makes maintenance and evolution of both repositories difficult and error-prone.

.. uml::
   :align: center
   :caption: Cyclic dependency between process and docs-as-code repositories

   left to right direction
   database process_description {
      artifact examples
      artifact templates
   }
   database docs_as_code {
      artifact metamodel.yaml as yaml
   }

   process_description --> docs_as_code : defines metamodel
   docs_as_code --> process_description : checks metamodel

The artifacts within those repos are:

* "examples" are exemplary instances of the metamodel like :need:`feat__example_feature`.
* "templates" (more precisely `folder templates <https://eclipse-score.github.io/process_description/main/folder_templates/index.html>`_)
  are instances which can be copied when creating new modules
  like :need:`doc__feature_name_architecture`.
* "metamodel.yaml" is `this file <https://github.com/eclipse-score/docs-as-code/blob/v2.3.3/src/extensions/score_metamodel/metamodel.yaml>`__.

This means to roll out a change to the process looks like this:

1. Change ``process_description`` but *not* the examples and folder templates.
2. Change ``docs_as_code`` accordingly (potentially with constraints because ``@process_description//:needs_json`` includes old examples and folder templates)
3. Change ``process_description`` a *second* time adapting the examples and folder templates.
4. Change ``docs_as_code`` a *second* time removing constraints from step 2.

Currently the `module_template repo <https://github.com/eclipse-score/module_template>`_
is not used and not up to date.
However, the Process community intends to use it for the folder templates in the future.
Thus, step 3 above will become a pull request to a third repository eventually.
Still, there is no plan to move the examples to that repository.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- **Effort**: Don't spend much one-time effort to implement the change proposed here.
- **Independence**: Enable independent evolution of process requirements for the meta model and the meta model verification implementation.
- **UX**: Enable a process change rollout which does not require multiple pull requests in a single repository due to dependency cycles.
- **Clear Ownership**: Each repository should have a clear responsibility and ownership of its contents.
- **Maintainability**: Keep long-term maintenance effort low.

Non-Goals
~~~~~~~~~

- Redesigning the entire docs-as-code or process description approach.
- Removing Sphinx or Sphinx-Needs as documentation tools.
- Avoid inconsistencies between process and tool implementation.

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

Clear Ownership 💚: Process community and docs-as-code are clearly separated.


Option 1: Merge both repositories into one
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Combine ``process_description`` and ``docs_as_code`` into a single repository.
This eliminates the cyclic dependency by having a single source of truth for both the meta model and the Sphinx-Needs objects/examples, but process is repo is potentially large and complex and is implementation specific.

.. uml::
   :align: center
   :caption: Merge both repositories into one

   left to right direction
   database "process_description\n+ docs_as_code" {
      artifact metamodel.yaml as yaml
      artifact examples
      artifact templates
   }

Effort 😡😡: Disruptive effort to merge repos.
Such changes conflict with practically all parallel pull requests.
Dependencies across all S-CORE repos are necessary.

Independence 💚: Coupling is tolerable because both can be changed as an atomic commit.

UX 💚: Excellent as single source.

Maintainability 💚: Good because everything is in one place.

Option 2: Move meta model definition to process repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define and maintain the ``metamodel.yaml``
solely in the process repository.
The docs-as-code repository would then only provide the infrastructure for the meta model, not define or modify it.
The process repository would be the authoritative source for the meta model.
Also tests (scripts) and examples would be maintained there.

.. uml::
   :align: center
   :caption: Move meta model definition to process repository

   left to right direction
   database process_description {
      artifact examples
      artifact templates
      artifact metamodel.yaml as yaml
   }
   database docs_as_code {
   }

   process_description --> docs_as_code : defines metamodel
   yaml --> docs_as_code : as input
   docs_as_code --> process_description : checks metamodel

Implication:
If the docs-as-code module would select the metamodel yaml version on its own,
we would not have resolved the cyclic dependency issue.
Thus, ``process_description`` would need to define which version of ``metamodel.yaml`` to use
and ``docs_as_code`` provides a configuration option to specify it.

Moving only the ``metamodel.yaml`` file means that a few Python-implemented checks still remain in ``docs_as_code``.
While the problem is not solved completely, it should fix most of the cases.

Effort 😡: Medium effort.

Independence 😡: Rather good because ``docs_as_code`` mostly consumes except a few remaining checks.

UX 💚: Excellent since authority is clear.

Maintainability 💚: Good because of clear ownership.

Clear Ownership 💚: Cleanly separated.

Option 3: Move examples to docs_as_code and templates to module_template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Move all examples from ``process_description`` into ``docs_as_code`` repo
and all templates from ``process_description`` into ``module_template`` repo.
No relevant cyclic dependency remains.

.. uml::
   :align: center
   :caption: Move examples to docs_as_code and templates to module_template

   left to right direction
   database process_description {
   }
   database docs_as_code {
      artifact metamodel.yaml as yaml
      artifact examples
   }
   database module_template {
      artifact templates
   }

   process_description --> docs_as_code : defines metamodel
   docs_as_code --> module_template : checks metamodel

Effort 💚: Low.

Independence 💚: Good because process repo becomes independent.

UX 💚: Excellent since authority is clear.

Maintainability 😡: More repos to maintain.

Clear Ownership 💚: Process community is responsible for ``process_description`` and ``module_template``.

Option 4: Move meta model and examples into a separate repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create or use a dedicated meta model repository that contains only the Sphinx-Needs meta model definitions and the examples.
Both the process repository and docs-as-code repository would depend on this meta model repository (if necessary), making it the single source of truth.
This breaks the cycle by introducing a clear hierarchical dependency structure.

.. uml::
   :align: center
   :caption: Move meta model and examples into a separate repository

   left to right direction
   database process_description {
   }
   database docs_as_code {
   }
   database module_template {
      artifact metamodel.yaml as yaml
      artifact examples
      artifact templates
   }

   process_description --> docs_as_code : defines metamodel
   docs_as_code --> module_template : checks metamodel
   yaml --> docs_as_code : as input

Effort 😡: High effort for the configurable ``metamodel.yaml``.

Independence 💚: Good because process repo becomes independent.

UX 😡: It is strange that same checks are implemented in ``docs_as_code`` and some in ``module_template``.

Maintainability 😡: More repos to maintain.

Clear Ownership 💚: Clearly, the Process community takes authority over ``metamodel.yaml``.

Option 5: Move examples and templates to docs-as-code repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Move all example Sphinx-Needs objects from the ``process_description`` repository to the ``docs_as_code`` repository.
The process repository would define requirements for the meta model, while docs-as-code would provide infrastructure, the meta model and host the examples that demonstrate the meta model.
This breaks the cycle by removing the import dependency from docs-as-code back to the process repository.

.. uml::
   :align: center
   :caption: Move examples to docs-as-code repository

   left to right direction
   database process_description {
   }
   database docs_as_code {
      artifact examples
      artifact templates
      artifact metamodel.yaml as yaml
   }

   process_description --> docs_as_code : defines metamodel

Effort 💚: Low effort.

Independence 💚: Good because ``process_description`` just consumes.

UX 💚: Fine.

Maintainability 💚: Good because of clear ownership.

Clear Ownership 😡: Process community wants control of the templates but they are in the ``docs_as_code`` repo.

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

Maintainability 😡😡: Poor because warnings won't be fixed as quickly as errors.

Evaluation
----------

The effort for Option 1 is prohibitively high, so we ignore it for the evaluation.
Likewise we ignore Option 6 due to grave maintainability concerns.

Here is the summary, how well each option achieves the goals in order of goal importance:

.. csv-table::
   :header: Goals, Option 0, Option 2, Option 3, Option 4, Option 5
   :widths: 15, 10, 10, 10, 10, 10

   Effort,          💚, 😡, 💚, 😡, 💚
   Independence,    😡, 😡, 💚, 💚, 💚
   UX,              😡, 💚, 💚, 😡, 💚
   Clear Ownership, 💚, 💚, 💚, 💚, 😡
   Maintainability, 😡, 💚, 😡, 😡, 💚

Due to our most important goal, effort, Options 2 and 4 are disqualified.
Then Option 0 is disqualified due to independence concerns (among others).
Option 5 is disqualified due to the ownership issue.

**Decision:** Option 3 is the remaining best choice.
We accept the maintainability tradeoff.
