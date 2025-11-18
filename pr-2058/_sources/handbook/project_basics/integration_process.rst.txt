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

The integration process cannot be taken easily, and since Eclipse S-CORE project just recently started,
we´re still gathering experience and adapting the process based on our needs.
Several discussions and concepts were written to this topic.
On of the most exhaustive description can be found in the following `decision record <https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html>`_.
In this chapter, we´ll not dive in into details yet will give you just the overall idea of the integration process of Eclipse S-CORE instead.


.. image:: ../_assets/release_integration_concept.drawio.svg
   :alt: release_integration_concept
   :align: center


Compliance to Eclipse S-CORE software development process
---------------------------------------------------------

We encourage every software module -inside and outside the Eclipse S-CORE GitHub organization-
to follow the Eclipse S-CORE development process strictly and to introduce it by including appropriate checks
into the CI/CD pipeline. By doing so, the compliance to the Eclipse S-CORE project is validated with every pull request.
But the truth is, due to various reasons we cannot even enforce this inside our GitHub organization.

One reason for this is, that most software modules are used by multiple other projects apart from S-CORE.
Another reason is, that a software module is being open sourced by a company which follows other/ own software development process.
In this case, an immediate switch to the Eclipse S-CORE development process is not possible.

Therefore, it is acceptable (but not recommended), that every software module follows its own software development process inside its repo.
To announce a new version of a module and make it available inside Eclipse S-CORE, it needs to be added to the bazel registry first.
This is where our integration process comes in place. Before adding a module to the Eclipse S-CORE bazel registry,
following two conditions have to be fulfill:

- **Requirements of the “integration gate”** need to be fulfilled.
  This is a mandatory collection of checks and jobs which need to be passed by every module in Eclipse S-CORE.
  Those ensure compliance with the Eclipse S-CORE software development process, e.g., “code can be compiled with gcc/qcc compiler”,
  “unit tests are not failing”, “requirements and architecture are properly linked” and so on.

- Once a software module meets integration gate´s requirements (code changes of the software modules or related artifacts might be needed),
  a pull request to Eclipse S-CORE bazel registry repo can be created. Next, the pull request is being reviewed by safety,
  security and quality managers. Once all findings were fixed, the pull request is being merged to the Eclipse S-CORE bazel registry.
  Now the software module is officially available to the Eclipse S-CORE community.
  
Reference Integration
---------------------

The first step ensures, that the software module is compliant to the Eclipse S-CORE development process.
But it is not ensured yet, that the new version of the software module works together with other modules.
This is where the reference integration comes into place.
Reference integration repository contains reference image(s), which are used to execute feature integration tests.
Integration tests ensure that every feature, which was built by multiple modules, implements its feature requirements and can be used by the end-user.

**Reference integration overwrites all dependencies**, which were set by the software module itself.
This means, if a reference integration depends on the software module “A” in version 1.0,
then this is valid for all other software modules which are included in the same reference integration.
In consequence, all modules will also be built by using the same version 1.0 of the module A, independently from their locally configured dependency.
This ensures a consistent and unique state of all software module versions which are included in the same reference integration repository.

Sometimes, the introduction of new versions of a software module into the reference integration repository can lead to problems.
This is the case, when other modules are not compatible with changes included in the newer version.
In theory, such problems can be avoided by using proper planning and concept of deprecated interfaces.
Since in praxis such situations cannot be always avoided, the **Eclipse S-CORE integration team**
is in charge for solving such problems once occurred.

Based on agreed timeline -all feature integration tests are successfully executed/ other Eclipse S-CORE
project metrics are fulfilled- a release of reference integration repository
(official Eclipse S-CORE release) can be done. It consists mainly of:

- A **release tag** on the reference integration repository, which automatically also freezes relevant version of every referenced software module.
  Therefore, all software modules are indicated, which are officially part of the particular S-CORE release.
- **Release Notes.**
- **Further documents.**  



