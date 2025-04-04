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


Workflow Release Management
#################################

.. workflow:: Create/Maintain Module Release Note
   :id: wf__rel__mod_rel_note
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__module_safety_package, wp__module_sw_release_plan, wp__verification__module_ver_report
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__req__process, doc_concept__req__process

   The module release note is created for each release by the module technical lead. It may be updated
   later in case of bugs found after the release is published.

.. workflow:: Create/Maintain Platform Release Note
   :id: wf__rel__platform_rel_note
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__platform_safety_package, wp__platform_sw_release_plan, wp__verification__platform_ver_report
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__req__process, doc_concept__req__process

   The platform release note is created for each release by the technical lead circle. It may be updated
   later in case of bugs found after the release is published.

.. workflow:: Plan Module Release
   :id: wf__rel__mod_rel_plan
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__module_safety_package, wp__issue_track_system, wp__platform_mgmt
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__issue
   :has: doc_concept__rel__process

   The module release plan is created as part of the modules planning and documented as part of the module's project planning.

.. workflow:: Plan Platform Release
   :id: wf__rel__issue
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__module_safety_package, wp__platform_safety_package, wp__issue_track_system, wp__platform_mgmt
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__rel__process

   The platform release plan is created as part of the project planning and documented in the platform management plan.
