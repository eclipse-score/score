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

Concept
#######

.. doc_concept:: Quality Management Concept
   :id: doc_concept__quality__process
   :status: valid
   :tags: quality_management

In this section a concept for the Quality Management will be discussed. Inputs for this concepts is ASPICE
as quality standard. And also in aspect to the development the adressed requirements from ISO 26262, ISO 21434
and ISO PAS 8926.

Inputs
******

#. Stakeholders for the Quality Management
#. Who needs which information?
#. How is Quality ensured?

Stakeholders for the Quality Management
=======================================

#. :need:`Quality Manager <rl__quality_manager>`
    * Responsible for the quality compliance in the platform and the project
    * Monitoring and improving of quality acitivities
    * Execution of Audit's, Quality Checks and Work Product Reviews
    * Aproval of work products

#. :need:`Technical Lead <rl__technical_lead>`
    * Support the work products
    * Approval of Process Audits


#. :need:`Committer <rl__committer>`
    * Responsible for the work products

#. :need:`Safety Manager <rl__safety_manager>`
    * Supports the quality activities

#. :need:`Security Manager <rl__security_manager>`
    * Supports the quality activities

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ASPICE
* ISO 26262:2018
* ISO 21434:2021
* ISO PAS 8926:2024

General Quality Concept
=======================

The Quality Concept is based on the requirements of the standards and were derived into the Quality Performance
Opbjectives that are listed in the Quality Plan :need:`doc__project_quality_plan`. The Quality shall be continous
checked and improved during the development. All tasks are planed within the Quality Plan.

For every release a platform process audit shall be performed. Also a compliance check for every feature release.
Only 100% compliante work products / releases will be delivered to the community.

Every person who contributes shall be trained according Quality aspects. The commitors will ensure the Quality
by following the workflows. The Quality Manager / Technical Lead for Platform Process Audit approve it.
Thus the independency between the Project and the Quality is ensured.
