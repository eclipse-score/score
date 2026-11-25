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

ETAS KVS change impact analysis
============================================================

.. warning::

   Draft template for :doc:`../DR-004-arch`, not an approved assessment. Follows the recommended `Impact Analysis Template <https://eclipse-score.github.io/process_description/main/process_areas/change_management/guidance/change_management_impact_analysis_template.html>`_. Completion status belongs in the FEP tracker.

Type and dependencies
---------------------

Change type: see the FEP. TODO DR004-08: identify dependent change requests or explicitly record none.

Affected elements and work products
------------------------------------------------------------

TODO DR004-08: identify affected work products and required updates, referencing baseline revisions and component integration PRs.

Known consumers: `config_management <https://github.com/eclipse-score/config_management>`_ and `reference_integration <https://github.com/eclipse-score/reference_integration>`_; assess impact during module/integration builds.

Compatibility and platform impact
---------------------------------

The goal is to preserve C++/Rust APIs; any later breaking change follows S-CORE's applicable process. Stored data/snapshots, configuration and runtime behavior will change, with documentation and tests reviewed during integration. Transition may use conversion where feasible and needed, or recreation/reset where acceptable to affected consumers, explicitly accounting for data loss.

TODO DR004-07: clarify affected consumers and transition requirements, and assess whether the non-API changes are breaking. DR004-16 is currently not applicable but must be reconsidered if a break is identified.

Verification and realization
----------------------------

Each component integration PR includes unit tests using (GoogleTest) and CIT using ITF. Reuse/adapt existing FIT and, where feasible, run CIT/FIT against both implementations for comparison/regression testing; the `KVS tool <https://github.com/eclipse-score/persistency/issues/441>`_ may support this. Rust-binding verification is planned in `eclipse-score/persistency#772 <https://github.com/eclipse-score/persistency/issues/772>`_.

Component integration issues define test targets and acceptance criteria; their PRs provide verification evidence.

The DR records the rough release schedule. The Persistency Feature Team owns detailed implementation and verification planning under `eclipse-score/persistency#735 <https://github.com/eclipse-score/persistency/issues/735>`_; component integration issues capture effort, resources, risks, responsible GitHub usernames, cross-organization responsibilities, ongoing maintenance, milestones and dependencies.

Security impact
---------------

TODO DR004-11, security owner: identify changed security requirements, threat scenarios/attack paths, trust boundaries, permissions, input/configuration validation, dependency exposure and safety interaction. Link updated analyses and required mitigations; this template is not a completed security review.

Safety impact
-------------

The Persistency module declares ASIL_B; incoming implementation suitability is unproven. TODO DR004-12, safety owner: identify affected safety requirements, integrity/recovery and resource failure modes, common-cause/cascading failures, Rust/C++ boundary effects, mitigations and required updates to DFA/FMEA, assumptions and assurance evidence.

License impact
--------------

ETAS will contribute the implementation under Apache-2.0. Integration PRs undergo the standard S-CORE contribution and license checks.

TODO DR004-13: ETAS/project committers confirm contribution authorization and whether third-party content requires additional review.
