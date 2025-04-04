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
   :id: doc_concept__platform__process
   :status: valid
   :tags: platform_management

In this section a concept for the Platform Management will be discussed. Inputs for this concepts
are both the requirements of ISO26262 Part-2 and ASPICE Requirements from MAN.3 additionally
including the requirements of the different stakeholders for the Platform Management process.

Key concept
***********
The Platform Management Plan is the container for all plan documents. As container it shall include
the plans defined in the :ref:`Platform Management Plan Template <platform_templates>`.
The concept of the plan documents, beside Project Management is defined in the
corresponding process areas, which generate them.

The Project Management Plan should identify and control the activities, and establish resources
necessary to develop the project, in the context of the project’s requirements and constraints.

Inputs
******

#. Stakeholders for the Platform Management Plan?
#. Which plans are required?
#. Which activities are required?

Stakeholders for the Platform Management Plan
*********************************************

#. :need:`Technical Lead <rl__technical_lead>`

   * Plans, Develops, Controls and Adjust all platform project activities

#. :need:`Module Lead <rl__module_lead>`

   * Plans, Develops, Controls and Adjust all module project activities

#. :need:`Committer <rl__committer>`
#. :need:`Contributor <rl__contributor>`

   * Implements and verifies the defined project activities

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO SAE 21434

Plans for Platform Management
*****************************

Compare :ref:`Platform Management Plan Template <platform_templates>`.


Activities for the Platform Management Plan
*******************************************

Create/Maintain Platform Management Plan
========================================

The platform management is created and maintained by the :need:`Technical Lead <rl__technical_lead>`.
As it is a container, this activity is valid for all addressed plan documents.

Monitor/Improve Platform Management Plan
========================================

:need:`Technical Lead <rl__technical_lead>` is responsible for the monitoring of the
work products and activities against the platform management plan. If deviations are detected,
the plan must be adjusted.
