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
            <feature_name>/            -> Features including sub-folders and feature (change) request
               docs/                   -> Documentation of the feature
                   architecture/       -> Feature architecture [:need:`PROCESS_wp__feature_arch`]
                   requirements/       -> Feature requirements [:need:`PROCESS_wp__requirements__feat`]
                   safety_analysis/    -> Safety analysis on feature level [:need:`PROCESS_wp__feature_safety_analysis`]
                   safety_planning/    -> Feature specific safety workproducts planning
                   verification/       -> Feature verification report (reporting all feature verifications)
                                             [:need:`PROCESS_wp__verification__platform_ver_report`]
               tests/                  -> Feature tests, consisting of
                  integration-tests/   -> Integration tests [:need:`PROCESS_wp__verification__feat_int_test`]

            toolchain/                 -> Definition of toolchain
        glossary/                      -> Glossary of abbreviations used in the platform context
        manuals/                       -> user and integration manual(s)
        overview/                      -> Introduction and high-level description
                                          of the platform features.
        platform_management_plan/      -> Overall Platform Management Plan [:need:`PROCESS_wp__platform_mgmt`]
        score_releases/                -> [:need:`PROCESS_wp__platform_sw_release_note`]
        safety/                        -> safety documentation on platform level (SEooC):
                                             [:need:`PROCESS_wp__feature_dfa`], [:need:`PROCESS_wp__platform_safety_manual`],
                                             [:need:`PROCESS_wp__platform_safety_package`], [:need:`PROCESS_wp__fdr_reports`],
                                             [:need:`PROCESS_wp__audit_report`]
        security/                      -> security documentation on platform level
        requirements/                  -> requirements on platform level
            stakeholder/               -> Stakeholder requirements [:need:`PROCESS_wp__requirements__stkh`]

    modules/                           -> Modules of the SW platform.
    platform_integration_tests/        -> Integration tests on reference hardware verifying stakeholder requirements.

    process/                           -> process definition including workflows, workproducts,
                                             roles, guidance [:need:`PROCESS_wp__process_definition`]

    registry/                          -> infrastructure configuration

    README.md                          -> Entrypoint of the repository

.. _module_folder_structure:

Module Folder Structure
-----------------------

The modules and components shall follow the folder structure which was presented. However if there are good reasons the structure can be adapted.

.. parsed-literal::

   <module_name>/                      -> Folder containing all artifacts corresponding to one module.
      docs/                            -> Documentation of the module
         manual/                       -> Module manual, e.g. integration manual, assumptions of use,
                                             safety manual [:need:`PROCESS_wp__requirements__comp_aou`],
                                             [:need:`PROCESS_wp__module_safety_manual`].
         release/                      -> Module release note [:need:`PROCESS_wp__module_sw_release_note`],
                                             safety assessment [:need:`PROCESS_wp__audit_report`]
         safety_plan/                  -> Module safety plan [:need:`PROCESS_wp__module_safety_plan`],
                                             module safety case [:need:`PROCESS_wp__module_safety_package`],
                                             conformance reviews [:need:`PROCESS_wp__fdr_reports`]
         safety_analysis/              -> Safety analysis on module level [:need:`PROCESS_wp__sw_component_dfa`]
         verification/                 -> Module verification report
                                             components verifications [:need:`PROCESS_wp__verification__module_ver_report`],
                                             safety analysis conformance reviews [:need:`PROCESS_wp__fdr_reports`]

      <component_name>/                -> Components of the module.
                                             Folder containing all artifacts corresponding to one component.

         src/                          -> Source files of the component consisting of
                                             Include files
                                             Source Files
                                             Detailed Design [:need:`PROCESS_wp__sw_implementation`]
                                             Unit tests [:need:`PROCESS_wp__verification__sw_unit_test`]
            <lower_level_comp>/        -> lower level component following <component_name> folder structure

         docs/                         -> Documentation of the component
            architecture/              -> Component architecture (only if lower level components exist)
                                             [:need:`PROCESS_wp__component_arch`].
            requirements/              -> Component requirements [:need:`PROCESS_wp__requirements__comp`]
            safety_analysis/           -> Safety analysis on component level
                                             [:need:`PROCESS_wp__sw_component_safety_analysis`]
            verification/              -> Architecture review [:need:`PROCESS_wp__sw_arch_verification`],
                                             code inspection [:need:`PROCESS_wp__sw_implementation_inspection`]
            <lower_level_comp>/        -> Lower level component following <component_name> folder structure

         tests/                        -> Feature level tests, consisting of
                                             integration tests [:need:`PROCESS_wp__verification__comp_int_test`]
