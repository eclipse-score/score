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

Folder Structure
================

.. _platform_folder_structure:

Platform Folder Structure
-------------------------

The following shows the folder structure of the platform repository (ordered alphabetically). The ordering of the documentation in the rendered documentation can be in a different order.

.. parsed-literal::

    docs/                              -> Global documentation of the platform
        contribute/                    -> Description on how to contribute
        features/                      -> All features of the platform
            <feature_name>/            -> Features including sub-folders and feature (change) request [:need:`wp__feat_request`]
               architecture/           -> Feature architecture [:need:`wp__feature_arch`]
               requirements/           -> Feature requirements [:need:`wp__requirements_feat`]
               safety_analysis/        -> Safety analysis on feature level [:need:`wp__feature_fmea`], [:need:`wp__feature_dfa`]
               safety_planning/        -> Feature specific safety workproducts planning
               security_analysis/      -> Security analysis on feature level [:need:`wp__feature_security_analysis`]
               verification/           -> Feature verification, consisting of Architecture review [:need:`wp__sw_arch_verification`],
                  integration_tests/   -> Feature Integration tests [:need:`wp__verification_feat_int_test`]

        glossary/                      -> Glossary of abbreviations used in the platform context
        introduction/                  -> Background, scope and high-level architecture of the platform features
        manuals/                       -> User and integration manual(s)
        modules/                       -> Modules of the SW platform.
        platform_management_plan/      -> Overall Platform Management Plan [:need:`wp__platform_mgmt`]
        quality/                       -> Quality documentation on platform level:
                                             [:need:`wp__qms_report`]
        requirements/                  -> Requirements on platform level
            stakeholder/               -> Stakeholder requirements [:need:`wp__requirements_stkh`]
            tool/                      -> Tool requirements (not covered in tool repositories)
        safety/                        -> Safety documentation on platform level (SEooC):
                                             [:need:`wp__platform_dfa`], [:need:`wp__platform_safety_manual`],
                                             [:need:`wp__platform_safety_package`], [:need:`wp__fdr_reports`],
                                             [:need:`wp__audit_report`]
        score_releases/                -> [:need:`wp__platform_sw_release_note`]
        score_tools/                   -> Tool list and [:need:`wp__tool_verification_report`]
        security/                      -> Security documentation on platform level:
                                             [:need:`wp__platform_security_manual`], [:need:`wp__platform_security_package`], [:need:`wp__sw_platform_sbom`]
        verification_report/           -> Platform verification report (reporting all platform feature's verifications)
                                             [:need:`wp__verification_platform_ver_report`]

    platform_integration_tests/        -> Integration tests on reference hardware verifying stakeholder requirements. [:need:`wp__verification_platform_int_test`]
    tools/                             -> Platform tools (not covered in tool repositories)

    README.md                          -> Entrypoint of the repository

.. _module_folder_structure:

Module Folder Structure
-----------------------

The modules and components shall follow the folder structure which was presented. However if there are good reasons the structure can be adapted.

.. parsed-literal::

   <module_name>/                      -> Folder containing all artifacts corresponding to one module.
      docs/                            -> Documentation of the module
         manual/                       -> Module manual, e.g. integration manual, assumptions of use,
                                             safety manual [:need:`wp__requirements_comp_aou`],
                                             [:need:`wp__module_safety_manual`],
                                             security_manual [:need:`wp__module_security_manual`].
         release/                      -> Module release note [:need:`wp__module_sw_release_note`],
         safety_mgt/                   -> Module safety plan [:need:`wp__module_safety_plan`],
                                             module safety package [:need:`wp__module_safety_package`],
                                             formal documents reviews [:need:`wp__fdr_reports`]
         security_mgt/                 -> Module security plan [:need:`wp__module_security_plan`],
                                             module securty package [:need:`wp__module_security_package`],
                                             formal documents reviews [:need:`wp__fdr_reports_security`],
                                             module SW bill of material [:need:`wp__sw_module_sbom`]
         verification_report/          -> Module verification report
                                             components verifications [:need:`wp__verification_module_ver_report`],
                                             safety analysis formal reviews [:need:`wp__fdr_reports`]

      <component_name>/                -> Components of the module.
                                             Folder containing all artifacts corresponding to one component.

         src/                          -> Source files of the component consisting of
                                             Include files
                                             Source Files
                                             Unit tests [:need:`wp__verification_sw_unit_test`]
                                             Test doubles
            <lower_level_comp>/        -> lower level component following <component_name> folder structure
            details/                   -> Private implementation details of the component following <component_name> folder structure

         docs/                         -> Documentation of the component
            architecture/              -> Component architecture (only if lower level components exist)
                                             [:need:`wp__component_arch`].
            detailed_design/           -> Detailed Design [:need:`wp__sw_implementation`]
            requirements/              -> Component requirements [:need:`wp__requirements_comp`]
            safety_analysis/           -> Safety analysis on component level (only if component architecture exists)
                                             [:need:`wp__sw_component_fmea`], [:need:`wp__sw_component_dfa`]
            security_analysis/         -> Security analysis on component level (only if component architecture exists)
                                             [:need:`wp__sw_component_security_analysis`]
            verification/              -> Component verification, consisting of Architecture review [:need:`wp__sw_arch_verification`],
                                          code inspection [:need:`wp__sw_implementation_inspection`],
               integration_tests/      -> Component integration tests [:need:`wp__verification_comp_int_test`]
            <lower_level_comp>/        -> Lower level component following <component_name> folder structure
