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

S-Core v0.5-beta release notes
===============================

.. document:: S-Core v0.5-beta release note
   :id: doc__score_v05_beta_release_note
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__platform_sw_release_note

| **Platform Name**: S-CORE
| **Release Tag**: v0.5.0-beta
| **Origin Release Tag**: none - first published release
| **Release Date**: 2025-12-18

Overview
^^^^^^^^^
TBD

|

Highlights
-----------
TBD

Timeline
---------
TBD

|

For a detailed and always up-to-date planning view, see the `GitHub project <https://github.com/orgs/eclipse-score/projects/17/views/26>`_.

Eclipse S-CORE book
-------------------
TBD

Improvements
^^^^^^^^^^^^^
TBD

Bug Fixes
^^^^^^^^^^^^
TBD

Integrated Software Modules
-----------------------------

Communication
~~~~~~~~~~~~~
TBD

Fixed Execution Order Framework(FEO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBD

Baselibs
~~~~~~~~~~~~~
TBD


Persistency
~~~~~~~~~~~~~
TBD


Orchestrator
~~~~~~~~~~~~~

**Improvements**

- Support `log` frontend exchange  to: `log`, `tracing` or `score-log` (not yet implemented in this release)
- Increased CIT coverage and stability improvements
- Split of kyron into separate repositories: `orchestrator` and `kyron`

:Version: ``orchestrator v0.0.4``
:Source / tag: `Orchestrator GitHub release <https://github.com/eclipse-score/orchestrator/releases/tag/v0.0.4>`__
:Further reading: See below

  - `Orchestrator scope and design <https://github.com/eclipse-score/orchestrator/blob/main/src/orchestration/doc/features.md>`__
  - `Orchestrator examples <https://github.com/eclipse-score/orchestrator/tree/main/src/orchestration/examples>`__

Kyron
~~~~~~

**Improvements**

- Support `log` frontend exchange  to: `log`, `tracing` or `score-log` (not yet implemented in this release)
- Increased CIT coverage and stability improvements
- Split of kyron into separate repositories: `orchestrator` and `kyron`

:Version: ``kyron v0.0.3``
:Source / tag: `Kyron GitHub release <https://github.com/eclipse-score/kyron/releases/tag/v0.0.3>`__
:Further reading: See below

  - `Kyron scope and design <https://github.com/eclipse-score/kyron/blob/main/src/kyron/doc/features.md>`__
  - `Kyron examples <https://github.com/eclipse-score/kyron/tree/main/src/kyron/examples>`__


Reference integration
~~~~~~~~~~~~~~~~~~~~~~
TBD

Reference QNX image
+++++++++++++++++++++
TBD

Reference Red Hat AutoSD Linux image (Experimental)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
TBD

Reference Elektrobit corbos Linux for Safety Applications Linux image (Experimental)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
TBD

Associated Infrastructure Modules
-----------------------------------

process_description
~~~~~~~~~~~~~~~~~~~
Provides a process model establishing organizational rules for developing open source software
in the automotive domain, suitable for safety and security contexts.

- **Version:** ``process description v1.4.0``
- **Standards alignment:**

    - ASPICE 4.0
    - ISO 26262
    - ISO 21434
    - ISO PAS 8926

- **Release notes**: `process_description release notes <https://github.com/eclipse-score/process_description/releases/tag/v1.4.0>`_
- **Process maturity**: `process_description maturity levels <https://eclipse-score.github.io/process_description/main/>`_

docs-as-code
~~~~~~~~~~~~~~
TBD

tooling
~~~~~~~~~~~~~~
TBD

ITF (Integration Testing Framework)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TBD

Test Scenarios
~~~~~~~~~~~~~~~

**Improvements**
- Refactor tracing subscriber by externalizing it's initialization
- Remove baselibs dependency from C++ scenarios in JSON parsing

:Version: ``Test Scenarios v0.3.1``
:Source / tag: `Test Scenarios GitHub release <https://github.com/eclipse-score/testing_tools/releases/tag/v0.3.1>`__

Performed Verification
----------------------
TBD

Known Issues
----------------------
- see release notes of every module seperately

Upgrade Instructions
----------------------
- TBD

Contact Information
----------------------
For any questions or support, please contact the *Project lead* or raise an issue/discussion.
