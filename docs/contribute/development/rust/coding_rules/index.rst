..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

.. _rust_coding_rules_overview:

Rust Coding Rules (MISRA-derived draft)
#######################################

.. document:: Rust Coding Rules
   :id: doc__rust_coding_rules
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan[version==1]

.. note::

   Proposed rulebook revision: **0.2.0-draft**, aligned on 2026-09-18 with the SCRC MISRA C++
   cross-reference at commit ``9e81abd4``.
   The rules are available for technical and safety review. Publishing this section
   does not approve the rulebook, establish MISRA compliance, or enable any CI check.

.. toctree::
   :maxdepth: 1

   rules
   applicability
   verification_and_deviations

Attribution
===========

The applicability assessments in this catalogue come from the *Rust Cross Reference with
MISRA C++ 2023* prepared by the Coding Guidelines Subcommittee of the
`Safety-Critical Rust Consortium <https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines>`_
and submitted as
`pull request #1226 <https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/pull/1226>`_,
still under review at the time of writing and used here as a working reference, not
as an approved standard. The rule grouping started from the paper
`MISRust: Mapping MISRA-C++ Coding Guidelines to the Rust Programming Language
<https://arxiv.org/abs/2605.23490v2>`_ by Marius Molz, Niels Schneider, Sven Lechner,
Stefan Kowalewski and Alexandru Kampmann (RWTH Aachen University) and its
`research dataset <https://github.com/embedded-software-laboratory/MISRust>`_, which
remain a secondary reference. Both sources are licensed under
`Creative Commons Attribution 4.0 International <https://creativecommons.org/licenses/by/4.0/>`_
and their classifications are reproduced unchanged in the applicability register.

The grouping into Rust rules, the rule wording, the proposed levels, the enforcement
candidates, the dispositions and the review queue are S-CORE modifications and
additions. They should not be attributed to the SCRC or the MISRust authors, and
neither has reviewed or endorsed this draft.

The register refers to MISRA guidelines by number, kind and category only. MISRA
guideline text remains the property of The MISRA Consortium Limited and is not
reproduced here. Readers need their own licensed copy of MISRA C++:2023 to consult
the original guidelines. Full source details are in
:ref:`rust_coding_rules_applicability`.

Relation to the S-CORE Rust coding guidelines
=============================================

:need:`doc__rust_coding_guidelines` states the S-CORE position on Rust coding
guidelines: practical, evidence-based checks enforced through the ``rustc`` and Clippy
configuration in the ``score_rust_policies`` repository are preferred over rigid
language subsetting, and research such as MISRust is used as supporting rationale
rather than as normative compliance criteria.

This section does not change that position. It takes the SCRC's own draft MISRA
C++:2023 cross-reference as the working reference for which guidelines apply to Rust,
and proposes S-CORE rule text for the applicable guidelines. At the pinned revision
three of them already have a draft SCRC coding guideline, for shift-count bounds,
numeric uses of ``as`` and recursion; the corresponding S-CORE rules link to those
drafts and are to be reconciled with them rather than compete. For the remaining
applicable guidelines no SCRC rule text exists yet. This
lets reviewers check the existing lint profile for gaps and decide, rule by rule, which
obligations S-CORE wants to adopt, map to a validated check, or reject with a recorded
reason. A rule listed here binds a component only after it has been adopted through the
component's Software Development Plan. Rule text that proves useful is a candidate
contribution to the SCRC guidelines rather than a competing standard.

Purpose and scope
=================

The catalogue contains 43 proposed Rust rules: 38 interpretations of MISRA C++:2023
guidelines and five S-CORE supplements or adaptations without a retained MISRA C++
source, for buffer extents at foreign interfaces, absent-pointer representation,
dependency and generated-code soundness, foreign-language boundaries and verification
governance. The foreign-boundary supplement also links MISRA C++ sources that the SCRC
draft assesses as applicable. Together the rules link 83 of the 92 MISRA C++ guidelines
the SCRC draft assesses as applicable to safe or unsafe Rust, plus one guideline
retained by S-CORE although the SCRC draft assesses it as not applicable, with a stated
reason. Linking a source records an interpretation; whether a rule
makes every obligation of its sources explicit is part of the review. Nine
applicable guidelines have no S-CORE rule yet and are listed in the review queue of
the :ref:`applicability register <rust_coding_rules_applicability>`. Grouping is
many-to-one: the number of Rust rules is not the number of mapped source guidelines.

The scope is first-party production Rust and the dependency, generated-code and
foreign-interface evidence needed for its safety claims. Both QM and safety-related
components select and document their applicability; this draft assumes no automatic
exemption or complete applicability based solely on the component's classification.

Project adoption
================

A component choosing this rulebook records the rulebook revision, applicable rule
IDs, component scope and justified exclusions in its
:need:`Software Development Plan <wp__sw_development_plan>`. The selected scope
includes compiler revision, Rust edition, target, features, dependency resolution,
panic strategy and overflow-check settings.

Production, test and tooling profiles are identified separately. A test profile may
permit test panics or test-only APIs without weakening the production library's
obligations. Mixed production/test files are assessed by item and configuration.
Safe-only status describes first-party source separately from dependency soundness.

The proposed levels mean:

* **Required:** after adoption, demonstrate conformance or an approved scoped
  deviation. A deviation cannot make Rust undefined behavior acceptable.
* **Advisory:** assess and document nonconformance and its disposition.

These are proposed S-CORE levels, not inherited MISRA categories. S-CORE assigns
**Required** where a violation can lead to undefined behavior, silent data corruption,
a masked error or an unchecked invalid state, or where a validated automatic check
makes conformance cheap to demonstrate. It assigns **Advisory** where the residual
concern in Rust is readability or structure, or where enforcement would rest on manual
judgement because the C++ hazard behind the source does not exist in Rust. Where the
resulting level differs from the category of every MISRA C++ source, the rule entry
states a level rationale; seven rules currently do. The source categories and
classification decisions remain in the
:ref:`applicability register <rust_coding_rules_applicability>`. The ``draft``
status of this section describes its review state, independently of a rule's
proposed enforcement level.

Each rule has a stable ``SCR-RUST-NNN`` identifier, which is used in the data files,
in the applicability register and as the anchor of its catalogue entry. Verification
evidence and deviation records refer to rules by this identifier together with the
rulebook revision.

Responsibilities and maintenance
================================

.. list-table:: Ownership of the rulebook and its implementation
   :header-rows: 1
   :widths: 25 75

   * - Location
     - Responsibility
   * - This section of the ``score`` documentation
     - Rule text, rationale, source traceability, applicability and evidence policy.
   * - ``score_rust_policies`` and shared analysis tooling
     - Versioned compiler/Clippy configuration, custom checker implementations and checker tests.
   * - Component repositories
     - Adopted rulebook revision, component-specific constraints, deviations and verification results.

Adoption follows :need:`wf__sw_development_plan`; implementation and review follow
:need:`wf__sw_detailed_design` and :need:`wf__sw_verify_implementation`. This draft
does not create a separate approval authority. The applicable project plan identifies
the accountable reviewers for safety-relevant interpretations and deviations.

The rule text and metadata are maintained in ``_assets/rules.json`` beside this page.
The rendered catalogue and the compact source table are generated from the data files.
Maintainers edit the data files, never the generated ones. After a change, from the
repository root:

.. code-block:: bash

   # regenerate rules.rst, applicability_summary.csv and review_queue.csv from the data
   python3 tools/render_rust_coding_rules.py
   # read-only: fail if the generated files are stale or the data is inconsistent (CI use)
   python3 tools/render_rust_coding_rules.py --check
   # optional: compare every register row with a local copy of the pinned SCRC file
   python3 tools/render_rust_coding_rules.py --check --upstream path/to/misra-cpp-2023-mapping.rst
   # the repository's normal documentation check, and the HTML build for viewing
   bazel run //:docs_check
   bazel run //:docs

Without ``--upstream`` the check verifies internal consistency and that the SCRC totals
equal the pinned revision; it cannot detect two rows whose assessments were swapped.

Review rule changes together with their applicability and checker-impact changes.
When the SCRC cross-reference changes, re-pin its revision in the source manifest and
re-align the register before publishing a new rulebook revision. Upstream changes do
not silently alter an adopted component revision.
