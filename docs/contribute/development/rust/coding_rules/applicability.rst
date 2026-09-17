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

.. _rust_coding_rules_applicability:

Sources and Applicability
#########################

.. document:: Rust Coding Rules Applicability Register
   :id: doc__rust_coding_rules_applicability
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_development_plan[version==1]

Primary analysis
================

The primary input is the paper
`MISRust: Mapping MISRA-C++ Coding Guidelines to the Rust Programming Language
<https://arxiv.org/abs/2605.23490v2>`_ by Marius Molz, Niels Schneider, Sven Lechner,
Stefan Kowalewski and Alexandru Kampmann (RWTH Aachen University, Embedded Software
Laboratory), arXiv:2605.23490v2, 27 August 2026. The study covers Rust 1.92.0 /
edition 2024; its full cross-language FFI analysis is explicitly out of scope.

The paper explains the methodology and selected adaptations; the
`pinned MISRust research dataset <https://github.com/embedded-software-laboratory/MISRust/blob/9aafed8ea5d222625d4be7982b4f9e8ca2e29bec/misra_cpp_rust_comparison_rules.csv>`_
supplies all 179 guideline classifications. The MISRA C++:2023 document was used
to check source identifiers, original categories and rule intents.

The supporting MISRA C:2025 Addendum 6 assesses applicability **to Rust**, including
foreign interfaces. It supports the boundary review in
:ref:`SCR-RUST-042 <scr-rust-042>`. The full MISRA C:2025 standard was not
part of the analysis, so a complete C-rule interpretation is not claimed.

The
`Safety-Critical Rust Consortium guidelines <https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines>`_
are a further source for review. This draft does not yet include a full mapping
to that guideline set.

Attribution and records
=======================

Classification facts are reproduced unchanged from the MISRust authors' research
artifacts, licensed under
`CC-BY-4.0 <https://creativecommons.org/licenses/by/4.0/>`_. Rule grouping, Rust
requirements, dispositions, assessment notes, enforcement assessments and corrections
are S-CORE modifications and additions. The register cites MISRA guidelines by
number, kind, category and page only; no MISRA guideline text is reproduced, and the
MISRA documents are not redistributed here. The source manifest records the
documents used by role and content hash.

* :download:`Source manifest with document hashes <_assets/sources.json>`
* :download:`Full 179-row applicability register <_assets/applicability.csv>`
* :download:`Machine-readable Rust rules <_assets/rules.json>`

The source manifest pins the paper version, research artifact commit and dataset
checksum. The complete register includes original rule/directive category, physical
MISRA C++ PDF page (counted from 1), artifact row and draft review disposition.

Classification and adoption
===========================

.. list-table:: MISRust classifications
   :header-rows: 1
   :widths: 15 10 35 40

   * - Class
     - Count
     - Study classification
     - Draft treatment
   * - C1
     - 15
     - C++ library-specific
     - Candidate native-Rust exclusion; reassess foreign boundaries.
   * - C2
     - 42
     - C++ feature-specific
     - Candidate exclusion; review semantic analogues.
   * - C3
     - 53
     - Claimed language coverage
     - Verify compiler/diagnostic assumptions; restore selected obligations.
   * - C4 excluding C6
     - 36
     - Retained outside the safe subset
     - Explicit Rust obligations, with corrected scope where necessary.
   * - C6
     - 22
     - Retained even in safe Rust
     - Explicit Rust obligations.
   * - C5
     - 11
     - Adaptation needed
     - Explicit Rust interpretations.

In the paper C6 is a subset of C4: C4 totals 58. The artifact encodes C4 (36)
and C6 (22) separately. Therefore the retained total is 36 + 22 + 11 = **69**.
The paper's page 8 reference to C3/C4 for that set appears to be a label typo;
its diagram and counts identify C4/C5.

The 22 C6 entries are not a complete safe-Rust policy. Adapted rules, dependencies,
configuration, runtime failures and safe raw-pointer operations need assessment too.
Each adopting component must check the analysis against its actual Rust edition,
toolchain and delivered configurations.

Corrections requiring explicit review
=====================================

The register preserves the authors' classifications and records draft interpretation
separately. In particular:

* Raw pointers may be created, cast and compared outside unsafe blocks. Pointer
  restrictions must scan all code, not just unsafe syntax.
* A warning is not a hard language guarantee. Unused/unreachable-code coverage
  depends on diagnostics, visibility, configuration and suppression policy.
* Dynamic shifts (7.0.4), escaping raw pointers (6.8.2), immediately discarded
  guards (9.2.1), destructor panics (18.4.1) and allocator customization (21.6.4)
  need reconsideration even where the study sets a guideline aside.
* Safe code can leak or forget resources; destruction is not guaranteed.
  ``Pin`` is a type, not a trait.
* ``ptr::copy`` permits overlap; ``copy_nonoverlapping`` does not. Pointer API
  contracts, provenance and valid ownership determine correctness.
* Memory safety, panic freedom, bounded resource use, race-free application logic
  and functional correctness are separate claims.

Technical references for these interpretations include the
`Rust operator reference <https://doc.rust-lang.org/reference/expressions/operator-expr.html>`_,
`pointer documentation <https://doc.rust-lang.org/std/ptr/index.html>`_,
`undefined-behavior reference <https://doc.rust-lang.org/reference/behavior-considered-undefined.html>`_,
`forget contract <https://doc.rust-lang.org/std/mem/fn.forget.html>`_,
`copy contract <https://doc.rust-lang.org/std/ptr/fn.copy.html>`_,
`Drop documentation <https://doc.rust-lang.org/std/ops/trait.Drop.html>`_,
`allocator interfaces <https://doc.rust-lang.org/std/alloc/index.html>`_ and
`pinning documentation <https://doc.rust-lang.org/std/pin/index.html>`_.
Recheck these against the selected toolchain's supported language documentation.

Complete source mapping
=======================

Every entry is a draft requiring review, including candidate exclusions and compiler
coverage. A link to a Rust rule records an interpretation, not proven enforcement.
The original source level is distinct from a Rust rule's proposed S-CORE level.

.. csv-table:: MISRA C++ to proposed Rust rules
   :file: _assets/applicability_summary.csv
   :header-rows: 1
   :widths: 9 6 10 25 50
