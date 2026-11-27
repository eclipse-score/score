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

DR-004-Arch: Integrate the ETAS KVS implementation
============================================================

.. warning::

   Working draft, 2026-11-20; not accepted or ready for Final Comment Period (FCP). TODO DR004-18: recheck provisional DR numbering before merge; no conflict was found on 2026-11-20.

.. dec_rec:: Integrate the ETAS KVS implementation through staged replacement
   :id: dec_rec__arch__etas_kvs_integration
   :status: proposed
   :version: 1
   :tracking: https://github.com/eclipse-score/score/issues/3513
   :context: ETAS offers an existing proprietary KVS implementation requiring an agreed integration, compatibility and verification strategy.
   :decision: Propose bottom-up integration alongside the existing KVS, followed by a gated switch to the ETAS C++ implementation and a Rust binding.

* Author: `@tizava <https://github.com/tizava>`_.
* Shepherd: `@umaucher <https://github.com/umaucher>`_.
* Classification: Enhancement / major Feature Modification proposed; see TODO DR004-07 in the impact analysis.
* Umbrella epic: `eclipse-score/persistency#735 <https://github.com/eclipse-score/persistency/issues/735>`_; focused delivery topics use sub-issues.

Context / Problem
-----------------

Persistency currently provides C++ and Rust implementations. ETAS proposes integrating its existing KVS implementation to improve internal data handling and configuration. The `ETAS component presentation`_ provides supporting details on the improvements, benefits and replacement rationale.

Decision proposed
-----------------

1. Retain the existing C++ implementation for S-CORE v1.0.
2. After FEP acceptance and applicable contribution clearance, integrate reviewable ETAS component batches bottom-up under ``score/kvs/<component>``.
3. Keep implementations side-by-side temporarily, using distinct build targets and explicit selection; do not silently change existing defaults.
4. Provide a Rust interface to the incoming C++ backend, replacing the independent Rust backend only after contract and FFI verification.
5. Target the default switch and old-backend retirement for v1.1.0, conditional on completed compatibility/migration evidence, FIT, documentation and assurance reviews. Each component batch already needs its own tests and review documentation.

The FEP establishes the integration approach and architectural boundaries, not a complete implementation design. Component models, dependencies, configuration flows, interfaces and build-selection details are refined incrementally and reviewed with the corresponding component integration PRs. Each batch includes the documentation and tests needed to assess it; merging a batch does not replace the existing implementation or change its default selection.

Rust-binding planning and design/verification follow-up are tracked in `eclipse-score/persistency#772 <https://github.com/eclipse-score/persistency/issues/772>`_. The independent Rust backend is replaced only after the binding's contract and verification are complete.

Backwards Compatibility
-----------------------

API compatibility is the goal; expected non-API changes and transition requirements are described in :doc:`DR-004-arch/impact-analysis` under TODO DR004-07.

Alternatives Considered
-----------------------

* Port selected improvements: less replacement risk, but may duplicate ETAS work; the delivered delta must justify replacement.
* Single large replacement: shorter coexistence, but a larger review and rollback surface.
* Retain independent C++/Rust backends permanently: avoids new FFI obligations, but retains duplicated maintenance and parity work.

Rationale
---------

Staging separates contribution review from default selection. Consolidation may reduce duplicated maintenance, but ETAS must demonstrate that benefits outweigh migration and FFI costs. Proprietary production use alone does not establish S-CORE compliance or ASIL-B suitability.

Consequences
------------

Complete :doc:`DR-004-arch/impact-analysis` and update its identified work products; neither draft replaces the required requirements, architecture or assurance evidence. Coordination, delivery sub-issues and lifecycle status belong in `eclipse-score/score#3513 <https://github.com/eclipse-score/score/issues/3513>`_.

Readiness gates
---------------

Before FCP, establish the integration scope, architectural boundaries, compatibility approach and impact assessment sufficiently for stakeholders to judge the proposal. Detailed component and Rust-binding design may mature through the reviewed implementation work described above; decisions needed to assess the proposal cannot be deferred as implementation details. Publication, review and Feature Team planning are tracked in GitHub.

TODO DR004-19: before default switch/removal, merge required components, Rust binding, documentation and FIT; demonstrate accepted contracts or approved migrations; obtain assurance/integration/release dispositions; verify data-safe rollback or explicitly agree downgrade restrictions. Material deviations from the accepted design require a follow-up FEP.

References
----------

* `Current FEP guide`_
* `DR-002-Proc`_
* `Change Management Plan`_
* `ETAS component presentation`_ (2026-11-02)

.. _Current FEP guide: https://eclipse-score.github.io/score/main/contribute/contribution_request/feature_request.html
.. _DR-002-Proc: https://eclipse-score.github.io/score/main/design_decisions/process/DR-002-proc.html
.. _Change Management Plan: https://eclipse-score.github.io/score/main/platform_management_plan/change_management.html
.. _ETAS component presentation: https://github.com/user-attachments/files/35339296/PersistencyImprovements_2026_11_02.pdf

.. toctree::
   :hidden:

   DR-004-arch/impact-analysis
