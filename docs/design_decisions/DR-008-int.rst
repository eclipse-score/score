..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-008-Int: S-CORE integration scope in reference_integration repository
========================================================================

- **Date:** 2026-03-31

.. dec_rec:: Integration scope in reference_integration repository
   :id: dec_rec__int__scope_reference_integration
   :status: accepted
   :context: Integration
   :decision: Option 2

Context / Problem
-----------------

Currently there is no clear definition of scope and responsibilities of the ``reference_integration`` repository.
The process of integration of S-CORE modules is time consuming and leaves open space for misalignment
between the process and the feature teams.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

- **Effort**: The integration process should be as efficient as possible with clear feedback loops.
- **Independence**: Modules should be independent with their implementation scope.
- **Integration**: Modules should have clear common requirements for S-CORE release integration.
- **Clear Ownership**: Each module should have a clear vision of responsibilities for integrating into reference_integration.
- **Maintainability**: Keep long-term maintenance effort low.

Non-Goals
~~~~~~~~~

- Controlling every release of each Module - Modules can release independently and some releases can be not integrated into S-CORE.

Options Considered
------------------

Option 1: Execute only Feature Integration Tests in reference_integration repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference_integration repository is a place where only Feature Integration Tests are executed.
Every Module is responsible for executing static tests, UTs, CITs in their respective repositories,
used configurations, compiling flags and workflows should be aligned with S-CORE guidelines.

Reference_integration will provide a means to conduct continuous integration, based on only Feature Integration Tests,
of latest Modules states to ensure early feedback and breaking changes notifications.

For S-CORE releases, Modules need to deliver artifacts from local tests as their release assets to be used for certification and documentation.

Pros:
* Modules have full control over their own scope
* Quick integration jobs in reference_integration repository as only Feature Integration tests are executed

Cons:
* No control over configuration, compiling flags, variants
* Documentation and artifacts are distributed across different repositories
* Full-stack S-CORE release might resolve to different version of dependencies that were tested in Module repositories
which makes the release not compliant with S-CORE release requirements.

Option 2: Re-execute all quality checks in the reference_integration repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference_integration repository is a place where all kinds of tests - static, UTs, CITs, FITs are re-executed
for full verification of the S-CORE full-stack. Every Module needs to ensure their tests are executable in reference_integration
repository. For the verification process, common configuration, compiling flags are used across all Modules to ensure the compliance with current S-CORE guidelines.

Reference_integration will provide a means to conduct continuous integration of latest Modules states to ensure early feedback and breaking changes notifications.

All necessary artifacts and single documentation build are generated in reference_integration repository to be used for certification and documentation
of S-CORE releases.

Pros:
* Single point of truth for configurations, compiling flags, documentation and certification artifacts
* Better control over resolved dependencies
* Better traceability of the tests and documentation for full-stack S-CORE releases

Cons:
* Additional effort for the Module teams to maintain their tests and dependencies to be fully executable in reference_integration repository
* Longer integration jobs in reference_integration repository as all tests are executed

Evaluation
----------

Option 1 makes S-CORE provide a set of SEooCs without being a full-stack project that has been selected
in :need:`dec_rec__strat__consistent_stack_vs_reference`.
Modules are responsible for their own compliance with the S-CORE release requirements, which makes it difficult
to validate the final S-CORE release for the process compliance.
The biggest risk is that Module A can deliver a release and artifacts with dependency on Module B in version x.y.z,
but in reference_integration thus overall S-CORE release, Module B will be resolved in version x.y.z+1,
which makes Module A artifacts not compliant.

Option 2 truly makes S-CORE a full-stack project and provides a single point of truth for the
configurations, compiling flags, variants, documentation and certification artifacts.
However, it requires additional effort for the module teams to maintain their tests and dependencies to be fully
executable in the reference_integration repository with both public APIs and tests.
It allows generating a single documentation build with full traceability across different repositories which will stay persistent
and will not require external linking.

**Decision:** Option 2 has been most favored by the community.
We accept additional effort for the integration process in exchange for a better traceability.
