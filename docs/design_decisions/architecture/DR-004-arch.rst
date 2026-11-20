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
   :tracking: https://github.com/eclipse-score/persistency/issues/739
   :context: ETAS offers an existing proprietary KVS implementation requiring an agreed integration, compatibility and verification strategy.
   :decision: Propose bottom-up integration alongside the existing KVS, followed by a gated switch to the ETAS C++ implementation and a Rust binding.

* TODO DR004-01: ETAS to nominate the separate author; support from `@tizava <https://github.com/tizava>`_.
* Shepherd: ``@umaucher``; separate from the author.
* Classification: Enhancement / major Feature Modification proposed; see TODO DR004-07 in the impact analysis.
* Umbrella epic: `eclipse-score/persistency#735 <https://github.com/eclipse-score/persistency/issues/735>`_; focused delivery topics use sub-issues.

Context / Problem
-----------------

Persistency currently provides C++ and Rust implementations. ETAS offers an existing implementation with reported improvements in internal data handling and configuration. TODO DR004-03: substantiate benefits and replacement rationale against the alternatives below. The umbrella epic records prior Architecture discussion and the FEP route; replacement and Rust backend consolidation require agreement with integrators.

Decision proposed
-----------------

1. Retain the existing C++ implementation for S-CORE v1.0.0; TODO DR004-04: confirm this baseline and the v1.1.0 switch target with release owners.
2. After FEP acceptance and applicable contribution clearance, integrate reviewable ETAS component batches bottom-up under ``score/kvs/<component>``.
3. Keep implementations side-by-side temporarily, using distinct build targets and explicit selection; do not silently change existing defaults.
4. Provide a Rust interface to the incoming C++ backend, replacing the independent Rust backend only after contract and FFI verification.
5. Target the default switch and old-backend retirement for v1.1.0, conditional on completed compatibility/migration evidence, FIT, documentation and assurance reviews. Each component batch already needs its own tests and review documentation.

TODO DR004-05: ETAS supplies the before/after component model, dependency graph, configuration flow, changed interface definitions and explicit coexistence/build selection before FCP. TODO DR004-06: specify the Rust binding's ownership/lifetimes, errors, panic/exception containment, concurrency and supported build/link targets.

Under TODO DR004-03, distinguish replacement parity from separately planned enhancements listed in the umbrella epic; they are not automatically committed scope.

Backwards Compatibility
-----------------------

Compatibility is intended, not proven; explicit changes may be agreed. TODO DR004-07 in :doc:`DR-004-arch/impact-analysis` owns compatibility and conditional migration requirements. Breaking-change governance is tracked under TODO DR004-16 in the tracking issue.

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

Complete :doc:`DR-004-arch/impact-analysis` and update its identified work products; neither draft replaces the required requirements, architecture or assurance evidence. Coordination, delivery sub-issues and lifecycle status belong in `eclipse-score/persistency#739 <https://github.com/eclipse-score/persistency/issues/739>`_.

Readiness gates
---------------

Before FCP, resolve proposal-shaping TODOs and agree the impact assessment and realization plan with affected owners. Publication and review actions are tracked in the issue, not duplicated here.

TODO DR004-19: before default switch/removal, merge required components, Rust binding, documentation and FIT; demonstrate accepted contracts or approved migrations; obtain assurance/integration/release dispositions; verify data-safe rollback or explicitly agree downgrade restrictions. Material deviations from the accepted design require a follow-up FEP.

References
----------

* `Current FEP guide <https://eclipse-score.github.io/score/main/contribute/contribution_request/feature_request.html>`_
* `DR-002-Proc <https://eclipse-score.github.io/score/main/design_decisions/process/DR-002-proc.html>`_
* `Change Management Plan <https://eclipse-score.github.io/score/main/platform_management_plan/change_management.html>`_

.. toctree::
   :hidden:

   DR-004-arch/impact-analysis
