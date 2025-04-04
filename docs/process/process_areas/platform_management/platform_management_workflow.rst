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

.. _workflow_platform_management:

Workflow Platform Management
############################

.. workflow:: Create/Maintain Platform Management Plan
   :id: wf__platform__cr_mt_platform_mgmt_plan
   :status: valid
   :tags: platform_management
   :responsible: rl__technical_lead
   :approved_by: rl__process_community
   :supported_by: rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__policies, wp__issue_track_system
   :output: wp__platform_mgmt, wp__project_mgt, wp__document_mgt_plan
   :contains: gd_temp__platform__mgmt_plan, gd_guidl__platform__mgmt_plan, gd_guidl__documentation, gd_chklst__documentation__review
   :has: doc_concept__platform__process, doc_getstrt__platform__process

   The Platform Management Plan shall include the plans as defined by the
   :ref:`Platform Management Plan Template <platform_templates>`.

   The project management plan should contain the scope of work, project life cycle, work packages,
   planning and monitoring approaches, project schedule, escalation and communication path.

.. workflow:: Monitor/Improve Platform Management Plan
   :id: wf__platform__mr_im_platform_mgmt_plan
   :status: valid
   :tags: platform_management
   :responsible: rl__technical_lead
   :approved_by: rl__process_community
   :supported_by: rl__safety_manager, rl__security_manager, rl__quality_manager
   :input: wp__platform_mgmt, wp__project_mgt, wp__document_mgt_plan
   :output: wp__issue_track_system
   :contains: gd_temp__platform__mgmt_plan, gd_guidl__platform__mgmt_plan, gd_guidl__documentation, gd_chklst__documentation__review
   :has: doc_concept__platform__process, doc_getstrt__platform__process

   The :need:`Technical Lead <rl__technical_lead>` is responsible for the monitoring and reporting
   of the work products and activities against the platform management plan.

   The :need:`Technical Lead <rl__technical_lead>` is responsible to adjust the plan,
   if deviations are detected.
