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
   :input: wp__module_safety_case, wp__module_sw_release_plan, wp__module_sw_verification_report
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__req__process, doc_concept__req__process

   The module release note provides clarity what is included in the current version of the software
   module release. It shall indicate also the distinct changes to previous versions and provide
   information regarding the time of the release.

.. workflow:: Create/Maintain Platform Release Note
   :id: wf__rel__platform_rel_note
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__platform_safety_case, wp__platform_sw_release_plan, wp__platform_sw_verification_report
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__req__process, doc_concept__req__process

   The platform release note provides clarity what is included in the current version of the platform
   release. The platform release note mentions all individual software modules used in the platform
   release and their used released versions. It shall indicate also the distinct changes to previous
   platform versions and provide information regarding the time of the release.

.. workflow:: Plan Module Release
   :id: wf__rel__mod_rel_plan
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__module_safety_case, wp__issue_track_system, wp__platform_mgmt
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__rel__process

   The module release plan is a strategic document that outlines the features planned for upcoming
   module releases along with their estimated release dates. It provides a roadmap for the
   development and release of new features, ensuring that all stakeholders are aligned on the
   module's future direction.

.. workflow:: Plan Platform Release
   :id: wf__rel__platform_rel_plan
   :status: draft
   :tags: release_management
   :responsible: rl__technical_lead
   :approved_by: rl__project_lead
   :input: wp__module_safety_case, wp__platform_safety_case, wp__issue_track_system, wp__platform_mgmt
   :output: wp__module_sw_release_note
   :contains: gd_temp__rel__mod_rel_note
   :has: doc_concept__rel__process

   The platform release plan is a high-level document that outlines which software modules
   will be included in the overall platform and what features can be expected within the platform.
   It provides a strategic overview of the platform's development, ensuring that all
   stakeholders are aligned on the platform's future direction and the integration of
   various software modules.
