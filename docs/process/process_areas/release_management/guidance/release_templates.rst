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

Templates
=========

.. gd_temp:: Platform Release Note Template
   :id: gd_temp__rel__plat_rel_note
   :status: valid
   :complies: std_req__iso26262__management_64134, std_req__iso26262__management_64135

   |  Platform Release Notes
   |  ======================
   |  Release Tag: vX.Y.Z
   |  Release Commit Hash: a1b2c3d4e5f6g7h8i9j0
   |  Release Date: YYYY-MM-DD
   |
   |  Overview
   |  --------
   |  This document provides an overview of the changes, improvements, and bug fixes included in the platform release version vX.Y.Z.
   |
   |  New Features
   |  ------------
   |  - **Feature 1**: Brief description of the new feature.
   |  - **Feature 2**: Brief description of the new feature.
   |  - **Feature 3**: Brief description of the new feature.
   |
   |  Improvements
   |  ------------
   |  - **Improvement 1**: Brief description of the improvement.
   |  - **Improvement 2**: Brief description of the improvement.
   |  - **Improvement 3**: Brief description of the improvement.
   |
   |  Bug Fixes
   |  ---------
   |  - **Bug 1**: Brief description of the bug fix.
   |  - **Bug 2**: Brief description of the bug fix.
   |  - **Bug 3**: Brief description of the bug fix.
   |
   |  Integrated Software Modules
   |  ---------------------------
   |  - **Module 1**: Version and brief description of the module. Link to Software module release note.
   |  - **Module 2**: Version and brief description of the module. Link to Software module release note.
   |  - **Module 3**: Version and brief description of the module. Link to Software module release note.
   |
   |  Known Issues
   |  ------------
   |  - **Issue 1**: Brief description of the known issue. Justification regarding safety impact.
   |  - **Issue 2**: Brief description of the known issue. Justification regarding safety impact.
   |  - **Issue 3**: Brief description of the known issue. Justification regarding safety impact.
   |
   |  Upgrade Instructions
   |  --------------------
   |
   |  1. **Step 1**: Description of the first step.
   |  2. **Step 2**: Description of the second step.
   |  3. **Step 3**: Description of the third step.
   |
   |  Contact Information
   |  -------------------
   |
   |  For any questions or support, please contact the *Project Lead* or raise an issue/discussion.

.. gd_temp:: Module Release Note Template
   :id: gd_temp__rel__mod_rel_note
   :status: valid
   :complies: std_req__iso26262__management_64134, std_req__iso26262__management_64135

   | Software Module Release Notes
   | =============================
   |
   | Module Name: [Module Name]
   | Release Tag: vX.Y.Z
   | Release Commit Hash: a1b2c3d4e5f6g7h8i9j0
   | Release Date: YYYY-MM-DD
   |
   | Overview
   | --------
   |
   | This document provides an overview of the changes, improvements, and bug fixes included in the software module release version vX.Y.Z.
   |
   | New Features
   | ------------
   |
   | - **Feature 1**: Brief description of the new feature.
   | - **Feature 2**: Brief description of the new feature.
   | - **Feature 3**: Brief description of the new feature.
   |
   | Improvements
   | ------------
   |
   | - **Improvement 1**: Brief description of the improvement.
   | - **Improvement 2**: Brief description of the improvement.
   | - **Improvement 3**: Brief description of the improvement.
   |
   | Bug Fixes
   | ---------
   |
   | - **Bug 1**: Brief description of the bug fix.
   | - **Bug 2**: Brief description of the bug fix.
   | - **Bug 3**: Brief description of the bug fix.
   |
   | Compatibility
   | -------------
   |
   | - **Dependencies**: List any dependencies and their versions.
   |
   | Known Issues
   | ------------
   |
   | - **Issue 1**: Brief description of the known issue. Justification regarding safety impact.
   | - **Issue 2**: Brief description of the known issue. Justification regarding safety impact.
   | - **Issue 3**: Brief description of the known issue. Justification regarding safety impact.
   |
   | Upgrade Instructions
   | --------------------
   |
   | 1. **Step 1**: Description of the first step.
   | 2. **Step 2**: Description of the second step.
   | 3. **Step 3**: Description of the third step.
   |
   | Contact Information
   | -------------------
   |
   | For any questions or support, please contact the *Project lead* or raise an issue/discussion.

.. gd_temp:: Release Issue Template
   :id: gd_temp__rel__issue
   :status: valid
   :complies: std_req__iso26262__management_64131, std_req__iso26262__management_64132, std_req__iso26262__management_64133

Copy the below steps into the release ticket:

Release <add version number> for <platform/module_name>
-------------------------------------------------------

1. Link this issue to the correct milestone and assign to the technical lead
2. Check respective Verification report on the release candidate's github tag
3. Check bugfixes or justify failed tests
4. Check the safety package completeness (supported by the safety manager)
5. Create/update the release note (pull request to close this issue)
6. Document safety manager's "recommendation to release" by asking his GitHub review approval of the release note
7. Create the "release" in GitHub according to :need:`gd_guidl__rel_management`
8. Merge PR and close this issue to complete the release
