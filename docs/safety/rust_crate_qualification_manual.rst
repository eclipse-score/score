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

.. code-block:: text

    ┌─────────────────────────┐
    │  1. Crate Assessment &  │
    │     Classification      │
    └────────────┬────────────┘
                 │  PR to score-crates
                 ▼
    ┌─────────────────────────┐
    │  2. Classification      │
    │     Review              │
    └────────────┬────────────┘
                 │  Q / QR → proceed   NQ → stop
                 ▼
    ┌─────────────────────────┐
    │  3. Address Findings    │
    │  (coverage, docs, reqs, │
    │   design, traceability) │
    └────────────┬────────────┘
                 │  updated PR
                 ▼
    ┌─────────────────────────┐
    │  4. Final Review &      │
    │     Certification       │
    └─────────────────────────┘


Step 1: Crate Assessment & Classification
-----------------------------------------

Evaluate the crate across the following dimensions:

- Size of the crate: lines of code (excluding comments), number of dependencies.
- External dependencies: are they already qualified? If not, they must also go through this process or change to a qualified alternative.
- Documentation: quality and completeness of README and crate-level docs.
- Test coverage: coverage level and quality of the existing test suite.
- CI setup: whether the CI pipeline effectively catches regressions and enforces standards.
- Maintenance: update frequency and responsiveness to issues.
- Security history: known vulnerabilities and how quickly they were resolved.
- Unsafe code: any usage of ``unsafe`` and its justification.
- Requirements & design: availability of functional and design documentation.
- Code quality: style, readability, and maintainability.

Based on this evaluation, create a **Component Classification Report** using the S-CORE template:

  https://eclipse-score.github.io/process_description/main/folder_templates/modules/module_name/component_name/docs/component_classification.html

The report contains three tables:

.. code-block:: text

    ┌────────────────────────────────────────────────────────────────┐
    │  Table 1 – Process (P)                                         │
    │  Evaluate: requirements, specs, design, verification, CI       │
    │  Outcome per indicator: HE | PE | NE                           │
    ├────────────────────────────────────────────────────────────────┤
    │  Table 2 – Complexity (C)                                      │
    │  Evaluate: LoC, unsafe code, test coverage, public interfaces  │
    │  Outcome per indicator: NH | HM | NM                           │
    ├────────────────────────────────────────────────────────────────┤
    │  Table 3 – Classification Outcome (CLAS_OUT)                   │
    │  Derived from (P) and (C):  Q | QR | NQ                        │
    └────────────────────────────────────────────────────────────────┘

Fill in the justification, references, and all relevant details for each indicator.
See the pastey crate as a concrete example:

  https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/component_classification.rst

.. note::

   The classification outcome (Q / QR / NQ) in Table 3 is your initial proposal.
   It is not final and may change following review by the SCORE Safety team.

   - **Q** or **QR**: the crate is eligible for use in the safety-critical codebase and
     must proceed through the remaining qualification steps.
   - **NQ**: the crate cannot be used in the safety-critical codebase.

Since all crates reside in external repositories, submit the report as a pull request to
the ``score-crates`` repository:

  https://github.com/eclipse-score/score-crates/


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
- Add tests for any uncovered code paths.

.. note::

   Branch coverage requires nightly Rust (LLVM-based tools). Configure the CI job
   to use nightly when generating branch coverage reports.

**Documentation**

- Verify that the README or crate-level documentation is sufficient for safety-critical use,
  covering design decisions, safety considerations, and usage guidelines.
- Extend the upstream documentation if necessary.

**Requirements**

Requirements must be written in TRLC format and follow the three-level hierarchy below.
Because upstream repositories are typically not suitable for hosting safety artifacts,
create the requirement files in the ``score-crates`` repository and link them in the report.

.. code-block:: text

    Assumed System Requirement (ASR)          ← one shared file in score-crates
              │
              ▼
    Feature Requirement (FEAT)                ← add one entry per crate
              │
              ▼
    Component Requirement (REQ_COMP_*)        ← new file per crate

- **Assumed System Requirement** – a single shared file already exists in ``score-crates``:

    https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/requirement/assumed_system_requirements.trlc

- **Feature Requirement** – add one feature requirement for the crate to the shared feature
  requirements file, linked to the assumed system requirement:

    https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/requirement/feature_requirements.trlc

- **Component Requirements** – create a new file for the crate with detailed component
  requirements, each linked to the feature requirement:

    https://github.com/eclipse-score/score-crates/blob/main/docs/pastey/docs/requirement/component_requirements.trlc

In addition, provide the following safety artifacts required for traceability:

- **Assumptions of Use (AoU)** – preconditions that the integrator must satisfy.
- **Failure Modes** – identified failure modes with effect, cause, and guideword.

See the pastey safety analysis as an example:

  https://github.com/eclipse-score/score-crates/tree/main/docs/pastey/docs/safety_analysis

**Design**

- Create architectural and static design documentation for the crate (UML diagrams where
  applicable) and host it in the ``score-crates`` repository.
- Link the design artifacts in the classification report and the traceability report.

See the pastey design documentation as an example:

  https://github.com/eclipse-score/score-crates/tree/main/docs/pastey/docs/design

**Traceability**

- Create test cases in the ``score-crates`` repository and trace them to the component
  requirements.
- Use the **LOBSTER** tool from S-CORE tooling to generate the traceability report.

.. note::

   For test additions and coverage improvements, prefer merging changes into the upstream
   repository when possible. Requirements, design, safety analysis, and traceability
   artefacts are maintained in ``score-crates``.

   See an example PR: https://github.com/eclipse-score/score-crates/pull/39


Step 4: Final Review & Certification
--------------------------------------

Submit the updated pull request with all findings resolved. The SCORE Safety team performs
a final review and, if all standards are met, certifies the crate for use in the
safety-critical S-CORE Rust codebase.
