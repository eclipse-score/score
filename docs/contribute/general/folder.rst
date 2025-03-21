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

.. code-block:: text

    docs/                              -> Global documentation of the platform
        contribute/                    -> Description on how to contribute
        features/                      -> All features of the platform
            <feature_name>/            -> Features including sub-folders and contribution request
                                             [wp__cont_request]
               docs/                   -> Documentation of the feature
                   architecture/       -> Feature architecture [wp__feature_architecture]
                   requirements/       -> Feature requirements [wp__requirements__feat]
                   safety_analysis/    -> Safety analysis on feature level [wp__feature_safety_analysis]
                   safety_planning/    -> Feature specific safety workproducts planning
                   verification/       -> Feature verification report (reporting all feature verifications)
                                             [wp__platform_sw_verification_report]
               tests/                  -> Feature tests, consisting of
                  integration-tests/   -> Integration tests [wp__feature_integration_test]

            toolchain/                 -> Definition of toolchain
        glossary/                      -> Glossary of abbreviations used in the platform context
        manuals/                       -> user and integration manual(s)
        overview/                      -> Introduction and high-level description
                                          of the platform features.
        platform_management_plan/      -> Overall Platform Management Plan [wp__platform_mgmt]
        score_releases/                -> [wp__platform_sw_release_note]
        safety/                        -> safety documentation on platform level (SEooC):
                                             [wp__feature_dfa], [wp__platform_sw_safety_manual],
                                             [wp__platform_safety_case], [wp__cmr_reports],
                                             [wp__assessment_report]
        security/                      -> security documentation on platform level
        requirements/                  -> requirements on platform level
            stakeholder/               -> Stakeholder requirements [wp__stakeholder_req]

    modules/                           -> Modules of the SW platform.
    platform_integration_tests/        -> Integration tests on reference hardware

    process/                           -> process definition including workflows, workproducts,
                                             roles, guidance [wp__process_definition]

    registry/                          -> infrastructure configuration

    README.md                          -> Entrypoint of the repository

.. _module_folder_structure:

Module Folder Structure
-----------------------

The modules and components shall follow the folder structure which was presented. However if there are good reasons the structure can be adapted.

.. code-block:: text

   <module_name>/                      -> Folder containing all artifacts corresponding to one module.
      docs/                            -> Documentation of the module
         manual/                       -> Module manual, e.g. integration manual, assumptions of use,
                                             safety manual [wp__sw_component_aou], [wp__module_sw_safety_manual].
         release/                      -> Module release note [wp__module_sw_release_note],
                                             safety assessment [wp__assessment_report]
         safety_plan/                  -> Module safety plan [wp__module_safety_plan],
                                             module safety case [wp__module_safety_case],
                                             conformance reviews [wp__cmr_reports]
         safety_analysis/              -> Safety analysis on module level [wp__sw_component_dfa]
         verification/                 -> Module verification report
                                             components verifications [wp__module_sw_verification_report],
                                             safety analysis conformance reviews [wp__cmr_reports]

      <component_name>/                -> Components of the module.
                                             Folder containing all artifacts corresponding to one component.

         src/                          -> Source files of the component consisting of
                                             Include files of the component
                                             Detailed Design
                                             Component- [wp__sw_unit_test],
                                             Unit tests [wp__sw_implementation]
            <lower_level_comp>/        -> lower level component following <component> folder structure

         docs/                         -> Documentation of the component
            architecture/              -> Component architecture (only if lower level components exist)
                                             [wp__cr_mt_comparch].
            requirements/              -> Component requirements [wp__sw_component_req],
                                             HSI (if relevant) [wp__hsi]
            safety_analysis/           -> Safety analysis on component level
                                             [wp__sw_component_safety_analyses]
            verification/              -> Architecture review [wp__sw_arch_verification],
                                             code inspection [wp__sw_code_inspect]
            <lower_level_comp>/        -> Lower level component following <component> folder structure

         tests/                        -> Feature level tests, consisting of
                                             integration tests [wp__sw_component_integration_test]
                                             verification tests [wp__sw_component_test]

If the module consist only of one component the folder <component_name> can also be skipped.
