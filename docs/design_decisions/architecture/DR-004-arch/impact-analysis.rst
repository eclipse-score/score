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

   Draft template for :doc:`../DR-004-arch`, not an approved assessment. Follows the recommended `Impact Analysis Template <https://eclipse-score.github.io/process_description/main/process_areas/change_management/guidance/change_management_impact_analysis_template.html>`_. Responsible GitHub usernames are resolved under TODO DR004-10; completion status belongs in the FEP tracker.

Type and dependencies
---------------------

Change type: see the FEP. TODO DR004-08: identify dependent change requests or explicitly record none.

Affected elements and work products
------------------------------------------------------------

TODO DR004-08: pin revisions and reference the FEP's component/dependency model and connected consumers. Use traceability links to list affected requirements, architecture/interfaces, implementation/build/dependencies, verification/integration, assurance, manuals and release material. For each, record whether modification is needed, the responsible GitHub username and evidence link.

Compatibility and platform impact
---------------------------------

TODO DR004-07: assess intended compatibility and record the before/after contract, affected consumers, severity, owner and evidence for each surface:

* C++/Rust APIs, errors, lifecycle and build/link interfaces; representative unchanged consumers.
* Stored data/snapshots, checksums, versions, defaults and recovery; old-data readability and reverse readability wherever downgrade is promised.
* Configuration schemas/defaults, paths, permissions, tooling and invalid-input behavior.
* Flush/durability, reset, concurrency, corruption handling and resource limits.
* Known consumers and reference integration on the agreed Linux/QNX architecture matrix.

TODO DR004-07: if breaking, complete the impact inventory of integrators/configurations/deliverables, migration steps and effort, deprecation timeline or rationale for none, rollback constraints and affected-team lead acknowledgments. Otherwise provide evidence supporting the non-breaking classification. Record the disposition before FCP; execute the agreed verification before cutover.

Verification and realization
----------------------------

TODO DR004-09: link verification methods for each changed work product, baseline/differential tests, validation of the FEP's FFI contract, measurable resource/performance budgets, target matrix and acceptance evidence.

TODO DR004-10: estimate effort, resources and risks; nominate ETAS/S-CORE owners and reviewers by GitHub username, including cross-organization responsibilities and ongoing maintenance. Confirm implementation/verification milestones and dependencies against the FEP's release assumptions.

Security impact
---------------

TODO DR004-11, security owner: identify changed security requirements, threat scenarios/attack paths, trust boundaries, permissions, input/configuration validation, dependency exposure and safety interaction. Link updated analyses and required mitigations; this template is not a completed security review.

Safety impact
-------------

The Persistency module declares ASIL_B; incoming implementation suitability is unproven. TODO DR004-12, safety owner: identify affected safety requirements, integrity/recovery and resource failure modes, common-cause/cascading failures, Rust/C++ boundary effects, mitigations and required updates to DFA/FMEA, assumptions and assurance evidence.

License impact
--------------

TODO DR004-13, ETAS/project committers: confirm contribution authorization before source publication, applicable Eclipse review route, origins/third-party inventory, license compatibility, copyright/notices and SBOM changes. FEP acceptance does not grant contribution clearance.
