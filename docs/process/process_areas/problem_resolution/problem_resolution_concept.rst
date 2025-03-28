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

Concept Description
###################

.. doc_concept:: Concept Description
   :id: doc_concept__problem__process
   :status: valid
   :tags: problem_resolution

In this section a concept for the Problem Resolution will be discussed. Inputs for this concepts
are both the requirements of ISO26262 Part-2 and ASPICE Requirements from SUP.9 additionally
including the requirements of the different stakeholders for the Problem Resolution process.

Key concept
***********
A Problem Report is the **ONLY** way to report (compare :need:`gd_guidl__contr_request_guideline`)
deviations of an expected result of existing features in the **S-CORE** project.
Deviations include problems found by user, bugs found during verification activites by tester,
quality issues found by quality checks, safety anomalies, vulnerabilites or any other malfunction.

Inputs
******

#. Stakeholders for the Problem report?
#. Which categories are required?
#. Which attributes are required?
#. Which activities are required?

Stakeholders for the Problem Report
***********************************

#. :need:`Contributor <rl__contributor>`

   * Contributes features and components to grow the **S-CORE** content

#. :need:`Committer <rl__committer>`

   * Verifies that the contribution fulfills the **S-CORE** policies
   * Approves the contribution

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO SAE 21434

Problem Categories
******************

User: Problems relating to requirements, design, ore code found by user of the platform.

Bug: Problems found by contributor based on component, feature or platform integration tests.

Quality: Problems or gaps found by Quality Management activities as defined in the Quality

Compare Problem template: :ref:`prm_templates`.

.. _prm_attributes:

Attributes of Problem reports
*****************************

The required attributes for the Change Requests are defined here:

Compare Process Problem attributes: :ref:`prm_process_problem_attributes`.


Activities for Problem Resolution
*********************************

.. _prm_creation:

Creation of the Problem Report
==============================

Use therefore the :ref:`Problem Template <prm_templates>`.

In case safety or security is affected, in addition the impact analysis template
: :ref:`Impact Analysis Template <chm_impact_analysis_templates>`  can be used in addition.

.. _prm_analysis:

Anaylsis of the Problem Report
==============================

Based on the analysis results decision about the acceptance or rejection must be taken
by authorized persons.

Authorized person includes

#. :need:`Technical Lead <rl__technical_lead>`
#. :need:`Module Lead <rl__module_lead>`
#. :need:`Safety Manager <rl__safety_manager>`
#. :need:`Security Manager <rl__security_manager>`
#. :need:`Quality Manager <rl__quality_manager>`

Further prioritization must be done, e.g. based on release planning.

.. _prm_implementation_monitoring:

Implementation and Monitoring of the Problem resolution
=======================================================
If the Problem report is accepted, the implementation of the resolution must be initiated and
monitored.

The Problem Resolution im must be tracked until it is closed.

The status of the Problem report must be communicated by the
:need:`Technical Lead <rl__technical_lead>` or :need:`Module Lead <rl__module_lead>` until
the implementation is completed and confirmed.

.. _prm_closing:

Closing of the Problem Resolution
=================================

Use the :ref:`Problem Report Checklist <prm_checklist>` to control the completeness of the closed
Problem report.

Especially the effectiveness of the solution measures must be shown, based on concincing
arguments, e.g. verification measures must be use to confirm the implementation.
