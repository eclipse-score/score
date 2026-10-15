..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

.. dec_rec:: S-CORE V1.0 Release Target
   :id: dec_rec__strat__SCORE_1_0_Taregt
   :status: proposed
   :context: Contents, Quality, Maintaining of SCORE 1.0
   :decision:
   :tracking:
   :version:
   :affects: <link to work products>
   :consequences: <impact of this change>

   Context
   -------

   S-CORE 1.0 is expected to provide a **reproducible** and **usable** software baseline for its
   defined **functional scope**. The release does not require a dedicated long-term-support branch.
   Its quality evidence should support an **appropriate quality-management level**, covering
   - static analysis and compiler cleanliness,
   - structural test coverage,
   - requirements traceability and
   - sufficient documentation.

   Backward compatibility is expected only in later releases.

   Functional Scope
   ^^^^^^^^^^^^^^^^
   The expectations apply to the functionality declared as part of the S-CORE 1.0 release.
   Interfaces and dependencies needed to build, integrate, configure and use this functionality
   are part of the usable baseline and integrated in the related reference integration.

   •	BAS - Baselibs
   •	COM - Communication
   •	CFG - Configuration
   •	LCM - Lifecycle Management
   •	LOG - Logging
   •	PER - Persistency
   •	SEC-CRYPTO - Security and Cryptography
   •	SOME/IP-GW - SOME/IP Gateway
   •	TIME - Time services

   Problem Resolution and Maintenance of S-CORE 1.0
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   •	There is no dedicated long-term-support commitment for S-CORE 1.0.
   •	Bug-fixes are only provided in the forward development path.
   •	There is no special release branch maintenance or patch-delivery strategy supported.
   •	Each user has to consider to fix his used version

   Quality
   ^^^^^^^

   Although the initaial idea was to provide already with S-CORE 1.0 a certifieable version,
   the quality scope has to be reduced for feasibility reasons, but quality artifacts
   supporting an appropriate quality-management level are provided.

   **Static quality**

   •	Static code analysis results are available for the released source baseline.
   •	Compiler warnings are controlled and documented.

   **Test coverage**

   •	C0 statement coverage evidence is available. Target is 85%
   •	C1 branch coverage evidence is available. Target is 85%

   **Requirements traceability**

   •	Relevant requirements for the released scope are identified.
   •	Traceability exists from requirements to implementation and verification evidence.

   **Documentation**

   •	Documentation supports understanding, integration, configuration, build and use of the released functionality.
   •	Known limitations and applicable constraints are documented.

   **Usability**

   •	The release is usable as an integrated baseline

   **Deviations & Risk Assessment**

   Quality deviations are documented / mitigated on Feature level with the help of a verification report.

   **Reproducibility and Infrastructure**

   No special infrastructure or tooling requirements are defined.
   Reproducibility is nevertheless mandatory.

   •	The released source baseline and its dependencies can be identified unambiguously.
   •	Build and generation steps for the declared release scope are documented.
   •	The same declared inputs can reproduce the relevant release outputs.
   •	Used Tools will not be classified aor qualfied

   **Image**
   A downloadable image shall be available.

   Consequences
   ------------
   <your text, diagrams, etc>


   Note:
   Throughout the discussion of a CR, various ideas will be proposed which are not accepted.
   Those rejected ideas should be recorded along with the reasoning as to why they were rejected.
   This both helps record the thought process behind the final version of the CR as well as preventing people from bringing up the same rejected idea again in subsequent discussions.
   In a way this section can be thought of as a breakout section of the Rationale section that is focused specifically on why certain ideas were not ultimately pursued.

   Justification for the Decision
   ------------------------------
   <your text>


   Impact Analysis (Optional)
   --------------------------
   The impact analysis template can be used to detail out the impact on the platform
   and if applicable for other aspects, especially for safety/security.
   Either reference here to the filled-out template or copy the content from
   the template in this chapter and fill it out here.
   The impact analysis template is available in [1].





DR-004-Strat: S-CORE 1.0 Release Target
=======================================
