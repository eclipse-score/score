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

.. _Platform_Folder_Structure:

Folder Structure of Platform Repository
=======================================

The following shows the folder structure of the platform repository (ordered alphabetically). The ordering of the documentation in the rendered documentation
can be in a different order.

.. code-block:: text

    docs/                                           -> Global documentation of the platform.
        concepts/                                   -> Description of overall concepts.
        glossary/                                   -> Glossary of abbreviations used in the platform context.
        manual/                                     -> user and integration manual(s)
        overview/                                   -> Introduction and high-level description of the platform features.
        platform_management_plan/                   -> Overall Platform Management Plan  [wp__platform_mgmt], consisting of ...
            project_management.rst                  -> ... Project Management.
            stakeholder_management.rst              -> ... Stakeholder Management.
            safety_management.rst                   -> ... Safety Management incl. platform safety plan [wp__platform_safety_plan]
            risk_management.rst                     -> ... Risk Management.
            quality_management.rst                  -> ... Quality Management [wp__qms].
            config_management.rst                   -> ... Configuration Management.
            tool_management.rst                     -> ... Tool Management.
            release_management.rst                  -> ... Release Management.
            problem_resolution.rst                  -> ... Problem Management.
            change_management.rst                   -> ... Change Management.
            requirements_management.rst             -> ... Requirements Management.
            software_development.rst                -> ... Development [wp__sw_dev_plan].
            software_verification.rst               -> ... Verification [wp__verification_plan].
            documentation_management.rst            -> ... Documentation Management.
            security_management.rst                 -> ... Security Management.
        release/                                    -> [wp__platform_sw_release_note]
        safety/                                     -> safety documentation on platform level (SEooC): [wp__feature_dfa], [wp__platform_sw_safety_manual], [wp__platform_safety_case], [wp__cmr_reports], [wp__assessment_report]
        security/                                   -> security documentation on platform level
        requirements/                               -> requirements on platform level ...
            stakeholder/                            -> ... Stakeholder requirements [wp__stakeholder_req].
            tool/                                   -> ... Tool requirements [wp__tool_req]
        tutorials/                                  -> General tutorials.

    examples/                                       -> examples how a C++, Rust, Python module can be set up

    features/                                       -> All features of the platform.
        <feature_name>/                             -> Folder containing all sub-folders corresponding to one feature and the contribution request [wp__cont_request]
            docs/                                   -> Documentation of the feature consisting of ...
                architecture/                       -> ... Feature architecture [WP_FEATURE_ARCHITECTURE].
                requirements/                       -> ... Feature requirements [wp__requirements__feat].
                safety_analysis/                    -> ... Safety analysis on feature level [WP_FEATURE_SAFETY_ANALYSES]
                safety_planning/                    -> ... the feature specific safety workproducts planning
                verification/                       -> ... Feature verification report (reporting all feature verifications) [wp__platform_sw_verification_report]
            tests/                                  -> Feature tests, consisting of ...
                integration-tests/                  -> ... integration tests [wp__feature_integration_test].
        toolchain/                                  -> Definition of toolchain

    modules/                                        -> Modules of the SW platform.
        <module_name>/                              -> Folder containing all artifacts corresponding to one module.
            docs/                                   -> Documentation of the module consisting of ...
                manual/                             -> ... Module manual, e.g. integration manual, assumptions of use and safety manual [wp__sw_component_aou], [wp__module_sw_safety_manual].
                release/                            -> ... Module release note [wp__module_sw_release_note] plus safety assessment [wp__assessment_report]
                safety_plan/                        -> ... Module safety plan [wp__module_safety_plan], module safety case [wp__module_safety_case] and their conformance reviews [wp__cmr_reports]
                safety_analysis/                    -> ... Safety analysis on module level [wp__sw_component_dfa]
                verification/                       -> ... Module verification report (reporting all module's components verifications) [wp__module_sw_verification_report] plus safety analysis conformance reviews [wp__cmr_reports]

            components/                             -> Components of the module.
                <component_name>/                   -> Folder containing all artifacts corresponding to one component.
                    docs/                           -> Documentation of the component consisting of ...
                        architecture/               -> ... Component architecture (only if sub-components exist) [wp__sw_component_architecture].
                        requirements/               -> ... Component requirements [wp__sw_component_req] and HSI (if relevant) [wp__hsi].
                        safety_analysis/            -> ... Safety analysis on component level [wp__sw_component_safety_analyses]
                        verification/               -> ... Architecture review [wp__sw_arch_verification], code inspection [wp__sw_code_inspect]
                    src/                            -> Source files of the component (incl. detailed design) [wp__sw_implementation].
                    include/                        -> Include files of the component
                    tests/                          -> Component tests, consisting of ...
                        unit/                       -> ... unit tests [wp__sw_unit_test] (for lowest level of components).
                        integration/                -> ... integration tests [wp__sw_component_integration_test].
                        verification/               -> ... verification tests [wp__sw_component_test].
                    <sub_component_name>/           -> Sub-Component of the Component.
                         copy the relevant folders below <component-name> if applicable (example: no code inspection needed for sub-components from the Open Source)

    platform_integration_tests/                     -> Integration tests on reference hardware.

    process/                                        -> process definition including workflows, workproducts, roles, guidance [wp__process_definition]

    registry/                                       -> infrastructure configuration

    README.md                                       -> Entrypoint of the repository.
