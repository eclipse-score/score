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

Module Security Plan Template
=============================

.. gd_temp:: Module Security Plan Template
   :id: gd_temp__module_security_plan
   :status: valid
   :complies:

This document implements <add "need" link>


   | **1. Security Management Context**
   | This Security Plan adds to the :ref:`process_security_management` all the module development relevant work products needed for ISO SAE 21434 conformity.
   |
   | **2. Security Management Scope**
   | This Security Plan's scope is a SW module of the SW platform <link to module documentation in platform/modules/<modulename>/index.rst>.
   | The module consists of one or more SW components and will be qualified as a EooC.
   |
   | **3. Security Management Roles**

   +---------------------------+--------------------------------------------------------+
   | Security Manager          | <link to Module's Security Manager assignment or name> |
   +---------------------------+--------------------------------------------------------+
   | Project Manager           | <link to Module's Project Manager assignment or name>  |
   +---------------------------+--------------------------------------------------------+

   | **4. Tailoring**
   | Additional to the tailoring in the SW platform project as defined in the :ref:`process_security_management` we define here the additional tailoring on module level.
   |
   | - Excluded for this module are additionally the following work products (and their related requirements):
   |   - <ISO SAE 21434 reference>: <work product/requirement> - <Argumentation why it is not needed or replaced by another work product or activity.>
   |
   | **5. Security Module Work Products**
   | One set of workproducts for the module and one set for each component of the module:

.. list-table:: Module Work Products
        :header-rows: 1

        * - Work Product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__module_security_plan`
          - :ref:`guideline_security_management`
          - <automated>
          - <Link to issue>
          - this document
          - see above

        * - :need:`wp__module_security_package`
          - :ref:`guideline_security_management`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__fdr_reports` (module Security Plan)
          - :need:`gd_chklst__security_plan`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__fdr_reports` (module Security Package)
          - :need:`gd_chklst__security_package`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__fdr_reports` (module's Security Analyses)
          - Security Analysis FDR tbd
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__audit_report`
          - performed by external experts
          - n/a
          - <Link to issue>
          - <Link to WP>
          - <WP status (manual)>

        * - :need:`wp__module_sw_build_config`
          - :ref:`sw_development`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_security_manual`
          - :need:`gd_temp__security_manual`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification__module_ver_report`
          - :ref:`process_verification`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__module_sw_release_note`
          - :ref:`release_management`
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_module_sbom`
          - :ref:`tool_management`
          - not started
          - <Link to issue>
          - <Link to WP>
          - <automated>


.. list-table:: Component <name> Work Products
        :header-rows: 1

        * - Work Product Id
          - Link to process
          - Process status
          - Link to issue
          - Link to WP
          - WP status

        * - :need:`wp__requirements__comp`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__requirements__comp_aou`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__hsi`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__requirements__inspect`
          - <Link to process>
          - <automated>
          - n/a
          - Checklist used in Pull Request Review
          - n/a

        * - :need:`wp__component_arch`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_component_security_analysis`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_arch_verification`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification__sw_unit_test`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__sw_implementation_inspection`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification__comp_int_test`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>

        * - :need:`wp__verification__component_test`
          - <Link to process>
          - <automated>
          - <Link to issue>
          - <Link to WP>
          - <automated>
