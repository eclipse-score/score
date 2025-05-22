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


Quality Work Product Review Guideline
=====================================

.. gd_guidl:: Quality work product review
   :id: gd_guidl__wp_review
   :status: valid

Purpose
-------
| Definition of a generic workflow to ensure the quality of work products.

Objectives
----------
| Check and assure the quality of the project/platform work products.

Process
-------

| Step  1: Create issue with label ``q_wp_review`` in status OPEN
| Step  2: Identify which work products will be checked during the review and document it in the created issue
| Step  3: Adjust :need:`gd_chklst__review_checklist_template` based on specified work products to review, which contains acceptance criteria for all work products
| Step  4: Create PR, Link the stored checklist in the PR to the issue
| Step  5: Perform review according to checklist
| Step  6: Report deviations from the acceptance criteria in the issue tracking system with label ``bug`` and link it to the review issue and the checklist
| Step  7: Review result:
|         negative, in case of any deviation, continue with STEP 8
|         positive, in case of no deviations, continue with STEP 10
| Step  8: Trigger authors of WPs with deviations to resolve them in the same PR and close the corresponding bug issue
| Step  9: If all bug issues are resolved, continue with 5, otherwise continue with 8
| Step 10: Merge the PR and communicate the result, initial issue is now in status CLOSED
