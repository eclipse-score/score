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


Rust External Crate Qualification Manual
=========================================

This document describes the process for qualifying an external Rust crate for use in the
safety-critical S-CORE Rust codebase. The qualification process ensures that a crate meets
the required safety and quality standards before it is used in safety-critical applications
or libraries.

Process Overview
----------------

.. uml::

   @startuml
   skinparam defaultTextAlignment center
   skinparam ArrowColor #555555
   skinparam ActivityBorderColor #555555

   start

   :Step 1 — Crate Assessment & Classification
   Submit PR to score-crates;

   :Step 2 — Classification Review;

   if (Classification outcome?) then (Q or QR)
     :Step 3 — Address Findings
     <i>coverage · docs · requirements · design · traceability</i>;

     :Step 4 — Final Review & Certification;
     stop
   else (NQ)
     :Crate cannot be used\nin the safety-critical codebase;
     stop
   endif

   @enduml


Step 1: Crate Assessment & Classification
-----------------------------------------

Before starting the classification report, record the qualification target for the crate:

- crate name and version
- source repository and revision (tag or commit)
- enabled features and relevant configuration
- supported target platforms
- dependency baseline (crate version) used for the assessment

Evaluate the crate across the following dimensions:

- Size of the crate: lines of code (excluding comments), number of dependencies.
- Code quality: style, readability, and maintainability.
- External dependencies: are they already qualified? If not, they must also go through this process or be replaced with a qualified alternative.
- Documentation: quality and completeness of the crate-level documentation and API docs.
- Test coverage: coverage level and quality of the existing test suite, including unit, integration tests.
- CI setup: whether the CI pipeline effectively catches regressions and enforces standards, all the required checks are available or not (e.g., coverage, clippy, miri, etc).
- Maintenance: update frequency and responsiveness to issues and release management, because if the crate is unmaintained then it may not be up to date with latest Rust versions and may have unresolved security vulnerabilities.
- Security history: known vulnerabilities and how quickly they were resolved.
- Unsafe code: any usage of ``unsafe`` and its justification, Safety comments and documentation.
- Requirements & design: availability of functional and design documentation.

Based on this evaluation, create a **Component Classification Report** using the
`S-CORE Component Classification template <https://eclipse-score.github.io/module_template/main/score/component_example/docs/component_classification.html>`_.

The report contains three tables:

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Table
     - Evaluates
     - Possible Outcomes
   * - **Table 1 - Process (P)**
     - Requirements, specs, design, verification, CI
     - | ``HE`` - High Evidence
       | ``PE`` - Partial Evidence
       | ``NE`` - No Evidence
   * - **Table 2 - Complexity (C)**
     - LoC, unsafe code, test coverage, public interfaces
     - | ``NH`` - Not High
       | ``HM`` - High but Manageable
       | ``NM`` - Not Manageable
   * - **Table 3 - Classification (CLAS_OUT)**
     - Derived from (P) and (C)
     - | ``Q``  - Qualified
       | ``QR`` - Qualified with Restrictions
       | ``NQ`` - Not Qualified

Fill in the justification, references, and all relevant details for each indicator.
See the `pastey component classification report <https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/component_classification.rst>`_
as a concrete example.

.. note::

   - The classification outcome (Q / QR / NQ) in Table 3 is your initial proposal.
     It is not final and may change after review by the SCORE Safety team.
   - **Q** or **QR**: the crate is eligible for use in the safety-critical codebase and
     must proceed through the remaining qualification steps.
   - **NQ**: the crate cannot be used in the safety-critical codebase.

Because qualified crates typically reside in external repositories, submit the report as a pull request to
the `score-crates repository <https://github.com/eclipse-score/score-crates/>`_.


Step 2: Classification Review
------------------------------

The SCORE Safety team reviews the submitted report and provides feedback. They may request
additional information, clarification, or corrections before the classification is confirmed.

Only crates classified as **Q** or **QR** continue to Step 3.


Step 3: Address Findings
-------------------------

Based on the review feedback and your own assessment, resolve the identified findings.
The following categories of findings are common:

**Coverage**

- Achieve 100 % line and branch coverage for the crate.
- If the upstream CI does not have a coverage job, add one.
- Add tests for any uncovered code paths in the upstream repository whenever possible.

.. note::

   Branch coverage requires nightly Rust (LLVM-based tools). Configure the CI job
   to use nightly when generating branch coverage reports.

**Documentation**

- Verify that the README or crate-level documentation is sufficient for safety-critical use,
  covering design decisions, safety considerations, and usage guidelines.
- Extend the upstream documentation if it does not affect the rust `crate-docs <https://docs.rs/pastey/latest/pastey/>`_.

**Requirements**

Requirements must be written in TRLC format and follow the three-level hierarchy below.
Because upstream repositories are typically not suitable for hosting safety artifacts,
create the requirement files in the ``score-crates`` repository and link them in the report.
Follow the same crate-specific directory layout as the pastey example, for example
``docs/<crate>/docs/requirement/``.

.. uml::

   @startuml
   skinparam defaultTextAlignment center
   skinparam ArrowColor #555555
   skinparam ComponentBorderColor #555555
   skinparam ComponentBackgroundColor #f8f8f8

   component "Assumed System Requirement (ASR)\none shared file in score-crates" as ASR
   component "Feature Requirement (FEAT)\none entry per crate" as FEAT
   component "Component Requirement (REQ_COMP_*)\nnew file per crate" as COMP

   ASR -down-> FEAT
   FEAT -down-> COMP

   @enduml

- **Assumed System Requirement** - a single shared file already exists in ``score-crates``:
  `assumed_system_requirements.trlc <https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/requirement/assumed_system_requirements.trlc>`_

- **Feature Requirement** - add one feature requirement for the crate to the shared feature
  requirements file, linked to the assumed system requirement:
  `feature_requirements.trlc <https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/requirement/feature_requirements.trlc>`_

- **Component Requirements** - create a new file for the crate with detailed component
  requirements, each linked to the feature requirement:
  `component_requirements.trlc <https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/requirement/component_requirements.trlc>`_

In addition, provide the following safety artifacts required for traceability:

- **Assumptions of Use (AoU)** - preconditions that the integrator must satisfy.
- **Failure Modes** - identified failure modes with effect and cause.

See the `pastey safety analysis <https://github.com/eclipse-score/score-crates/tree/main/docs/pastey/docs/safety_analysis>`_ as an example.

**Design**

- Create architectural and static design documentation for the crate (UML diagrams where
  applicable) and host it in the ``score-crates`` repository.
- Link the design artifacts in the classification report and the traceability report.

See the `pastey design documentation <https://github.com/eclipse-score/score-crates/tree/main/docs/pastey/docs/design>`_ as an example.

**Traceability**

- Create the requirement-traced test cases and related LOBSTER inputs in the ``score-crates``
  repository and trace them to the component requirements.
- Use the **LOBSTER** tool from S-CORE tooling to generate the traceability report.

.. note::

   For test additions and coverage improvements, prefer merging changes into the upstream
   repository when possible. Requirements, design, safety analysis, requirement-traced test
   cases, and traceability artefacts are maintained in ``score-crates`` so the LOBSTER report
   can be generated there.

   See `score-crates PR #39 <https://github.com/eclipse-score/score-crates/pull/39>`_ as an example.


Step 4: Final Review & Certification
--------------------------------------

Submit the updated pull request with all findings resolved. The SCORE Safety team performs
a final review and, if all standards are met, certifies the crate for use in the
safety-critical S-CORE Rust codebase.
