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

Primary reference: SCRC MISRA C++ cross-reference
==================================================

The primary applicability reference is the *Rust Cross Reference with MISRA C++ 2023*
prepared by the Coding Guidelines Subcommittee of the Safety-Critical Rust Consortium
(SCRC). It is submitted as
`pull request #1226 <https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines/pull/1226>`_
to the `safety-critical-rust-coding-guidelines <https://github.com/Safety-Critical-Rust-Consortium/safety-critical-rust-coding-guidelines>`_
repository. The register uses the revision at commit ``9e81abd4`` of 9 September 2026.
The mapping is still under weekly review by the subcommittee and is not merged. The
pinned revision is recorded in the source manifest and must be re-checked, and the
register re-aligned, whenever the mapping changes.

The SCRC cross-reference assesses all 179 MISRA C++:2023 guidelines in three groups.
For each guideline it also names the related MISRA C:2025 guideline where one exists,
and the SCRC coding guideline that implements it where one exists.

.. list-table:: SCRC verdicts at the pinned revision
   :header-rows: 1
   :widths: 30 10 60

   * - SCRC group
     - Count
     - Register treatment
   * - Applicable to Rust in general (safe Rust)
     - 54
     - Mapped to S-CORE rules, or queued for rule assignment.
   * - Additionally applicable in the presence of unsafe code
     - 38
     - Mapped to S-CORE rules, or queued for rule assignment.
   * - Not currently applicable to Rust
     - 87
     - Excluded, except five guidelines retained with a stated reason.

At the pinned revision three guidelines have an SCRC coding guideline: 7.0.4, 8.2.2
and 8.2.10. The remaining applicable guidelines have a verdict and a rationale but no
SCRC rule text yet, which is the gap the S-CORE catalogue proposes to fill.

How the register follows the SCRC verdict
=========================================

Each register row records the SCRC verdict, the related MISRA C:2025 guideline, the
SCRC guideline link and category, and the S-CORE disposition:

* **proposed rust obligation** (83): SCRC marks the guideline applicable and one or
  more S-CORE rules interpret it.
* **rule assignment pending** (9): SCRC marks the guideline applicable but no S-CORE
  rule covers it yet. These need a new rule or an explicit exclusion decision.
* **not applicable** (82): SCRC marks the guideline not applicable and S-CORE agrees.
* **retained beyond SCRC** (5): SCRC marks the guideline not applicable but S-CORE
  keeps it as a supporting source for an existing rule, with the reason in the note.

The safe/unsafe distinction is recorded per source guideline and shown in the rule
catalogue. It does not by itself set the scope of an S-CORE rule; a rule's scope and
the component's production, test and tooling profiles decide where it applies.

Both open groups are listed in the :ref:`review queue <rust_coding_rules_review_queue>`
below. Resolving them, in either direction, is a review decision and is recorded in
the register with a note.

Secondary reference: MISRust
============================

The paper
`MISRust: Mapping MISRA-C++ Coding Guidelines to the Rust Programming Language
<https://arxiv.org/abs/2605.23490v2>`_ by Marius Molz, Niels Schneider, Sven Lechner,
Stefan Kowalewski and Alexandru Kampmann (RWTH Aachen University), arXiv:2605.23490v2,
27 August 2026, and its
`research dataset <https://github.com/embedded-software-laboratory/MISRust/blob/9aafed8ea5d222625d4be7982b4f9e8ca2e29bec/misra_cpp_rust_comparison_rules.csv>`_
were the starting point of this draft and remain a secondary reference. The
``misrust_class`` column keeps the study's C1 to C6 classification for every guideline
so that the origin of the rule grouping stays traceable.

Where MISRust and the SCRC cross-reference disagree, the SCRC verdict is followed. The
subcommittee's own
`analysis of the differences <https://github.com/inkreasing/safety-critical-rust-coding-guidelines/blob/misrust/src/appendices/standards-matrices/differences-to-misrust.rst>`_
identifies the main weaknesses of the study: compiler warnings treated as language
guarantees, raw-pointer operations in safe code overlooked, and foreign interfaces not
considered when dismissing C++ library guidelines. The corrections this draft had
applied to the study point in the same direction and are now superseded by the SCRC
verdicts.

Supporting references
=====================

MISRA C:2025 Addendum 6 assesses the applicability of MISRA C:2025 **to Rust**,
including foreign interfaces. The SCRC cross-reference names the related MISRA C
guideline per row, and the register carries that column. Addendum 6 supports the
boundary review in :ref:`SCR-RUST-042 <scr-rust-042>`. The full MISRA C:2025 rule
text was not part of the analysis, so a complete C-rule interpretation is not claimed.

The `SCRC coding guidelines <https://coding-guidelines.arewesafetycriticalyet.org/>`_
themselves are the intended long-term home of Rust-specific rule text. Where an SCRC
guideline exists for a mapped source, the register links it; S-CORE rule text for the
same source is a candidate contribution, not a competing standard.

Attribution and records
=======================

The SCRC cross-reference is documentation in the consortium repository and is
licensed under
`CC-BY-4.0 <https://creativecommons.org/licenses/by/4.0/>`_ per that repository's
COPYRIGHT file. Its verdicts, MISRA C references and guideline links are reproduced
unchanged; its rationale text is not copied, and readers should consult the pull
request for it. The MISRust classifications are reproduced unchanged from the CC-BY-4.0
research artifacts. Rule grouping, Rust rule text, dispositions, assessment notes and
the review queue are S-CORE modifications and additions. Neither the SCRC nor the
MISRust authors have reviewed or endorsed this draft.

The register cites MISRA guidelines by number, kind, category and page only; no MISRA
guideline text is reproduced, and the MISRA documents are not redistributed here. The
source manifest records the documents used by role and content hash.

* :download:`Source manifest with pinned revisions and document hashes <_assets/sources.json>`
* :download:`Full 179-row applicability register <_assets/applicability.csv>`
* :download:`Machine-readable Rust rules <_assets/rules.json>`

.. _rust_coding_rules_review_queue:

Review queue
============

Guidelines whose S-CORE disposition still diverges from a simple reading of the SCRC
verdict. Nine need a rule or an exclusion decision; five are retained beyond the SCRC
verdict and need confirmation or removal.

.. csv-table:: Open applicability decisions
   :file: _assets/review_queue.csv
   :header-rows: 1
   :widths: 8 9 8 8 20 47

Complete source mapping
=======================

Every entry is a draft requiring review. A link to a Rust rule records an
interpretation, not proven enforcement. The original MISRA level is distinct from a
Rust rule's proposed S-CORE level.

.. csv-table:: MISRA C++:2023 to proposed Rust rules
   :file: _assets/applicability_summary.csv
   :header-rows: 1
   :widths: 8 9 8 8 20 47
