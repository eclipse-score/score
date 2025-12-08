..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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
.. _integration_process:

Integration process
====================

.. toctree::
   :maxdepth: 1
   :glob:

The integration process is a core activity within Eclipse S-CORE and is still evolving as the project gathers experience.
Several discussions and concepts have shaped the current approach.
A detailed description is available in the following `decision record <https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html>`_.
This chapter provide a high-level overview of how integration works in Eclipse S-CORE.

.. image:: ../_assets/release_integration_concept.drawio.svg
   :alt: release_integration_concept
   :align: center


Compliance with the Eclipse S-CORE software development process
----------------------------------------------------------------
All software modules - whether inside or outside the Eclipse S-CORE GitHub organization –
are encouraged to follow the Eclipse S-CORE development process strictly and to enforce it through CI/CD checks.
This ensures that compliance is validated with every pull request. 

However, strict compliance cannot always be guaranteed. Reasons include: 

- Many modules are reused in other projects beyond S-CORE. 
- Some modules originate from companies with their own established software development process.
  An immediate migration to the Eclipse S-CORE development process is not feasible.

Therefore, it is acceptable (but not recommended) for software modules to follow their own
software development process inside its repository. 
To make a module available for Eclipse S-CORE, a new version must first be added to the bazel registry first.

This is where the S-CORE integration process applies. 
Before adding a module to the Eclipse S-CORE bazel registry, two conditions must be met:

-  **Fulfillment of the “Integration Gate”**
   
   The integration gate is a mandatory set of checks that validates compliance with the Eclipse S-CORE software development process.
   Examples include:

   -	code compiles with gcc/qcc 
   -	unit tests pass
   -	requirements and architecture are properly linked according to the metamodel
   
   Module owners may need to update code or artefacts to meet these criteria. 
- **Review and Approval**
  
  After meeting integration gate requirements, a pull request to Eclipse S-CORE bazel registry repo can be created. 
  This pull request is reviewed by safety, security and quality managers. Once all findings were resolved,
  the pull request is merged to the Eclipse S-CORE bazel registry, and the software module becomes officially
  available to the Eclipse S-CORE community.


Reference Integration
---------------------

The first step, passing the integration gate, ensures Process compliance, but not compatibility with other modules. 
This is the purpose of the reference integration. 

The reference integration repository assembles all modules into reference images 
and executes feature integration tests. These tests ensure: 

- correct implementation of feature requirements
- compatibility between dependent modules
- testability of features from an end-user perspective

Unified Dependency Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Within Reference integration, all module dependencies are overwriten by the versions defined in the reference integration configuration. 

For example: 
If the reference integration specifies software module “A” in version 1.0,
all software modules in that integration are built against “A” version 1.0 – regardless of their local dependency settings.
This ensures a consistent and unique state of all software module versions which are included
in the same reference integration repository.

Handling of Incompatibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Introducing  a new version into the reference integration repository can cause incompatibilities
if other modules have not yet adapted to changes.
Although proper planning and deprecation strategies help to avoid such issues, they cannot always be avoided.
The **Eclipse S-CORE integration team** is in charge for solving such problems when they occurr

Release of Reference Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once: –

- all feature integration tests have passed, and 
- other Eclipse S-CORE project metrics for the release cycle are fulfilled

a new release of the reference integration repository is created. An official S-CORE release typically consists of:

- A **release tag** in the reference integration repository (freezing versions of all included software modules)
- **Release Notes**
- **Additional documents as required**

This markst he complete and validated version of the Eclipse S-CORE platform for that release milestone. 
