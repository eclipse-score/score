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

General
=======

Naming Conventions of Files
---------------------------

The overall naming convention is to use snake case for all files and folders (all files are named lowercase and spaces are replaced by underscores).

.. _Platform_Folder_Structure:

Folder Structure of Platform Repository
---------------------------------------

The following shows the folder structure of the platform repository (ordered alphabetically). The ordering of the documentation in the rendered documentation
can be in a different order.

.. code-block:: text

    docs/                                           -> Global documentation of the platform.
        concepts/                                   -> Description of overall concepts.
        glossary/                                   -> Glossary of abbreviations used in the platform context.
        manual/                                     -> user and integration manual(s)
        overview/                                   -> Introduction and high-level description of the platform features.
        platform_management_plan/                   -> Overall Platform Management Plan  [WP_PLATFORM_MGMT], consisting of ...
            project_management.rst                  -> ... Project Management.
            stakeholder_management.rst              -> ... Stakeholder Management.
            safety_management.rst                   -> ... Safety Management incl. platform safety plan [WP_PLATFORM_SAFETY_PLAN]
            risk_management.rst                     -> ... Risk Management.
            quality_management.rst                  -> ... Quality Management [WP_QMS].
            config_management.rst                   -> ... Configuration Management.
            tool_management.rst                     -> ... Tool Management.
            release_management.rst                  -> ... Release Management.
            problem_resolution.rst                  -> ... Problem Management.
            change_management.rst                   -> ... Change Management.
            requirements_management.rst             -> ... Requirements Management.
            software_development.rst                -> ... Development [WP_SW_DEV_PLAN].
            software_verification.rst               -> ... Verification [WP_VERIFICATION_PLAN].
            documentation_management.rst            -> ... Documentation Management.
            security_management.rst                 -> ... Security Management.
        release/                                    -> [WP_PLATFORM_SW_RELEASE_NOTE]
        safety/                                     -> safety documentation on platform level (SEooC): [WP_FEATURE_DFA], [WP_PLATFORM_SW_SAFETY_MANUAL], [WP_PLATFORM_SAFETY_CASE], [WP_CMR_REPORTS], [WP_ASSESSMENT_REPORT]
        security/                                   -> security documentation on platform level
        requirements/                               -> requirements on platform level ...
            stakeholder/                            -> ... Stakeholder requirements [WP_STAKEHOLDER_REQ].
            tool/                                   -> ... Tool requirements [WP_TOOL_REQ]
        tutorials/                                  -> General tutorials.

    examples/                                       -> examples how a C++, Rust, Python module can be set up

    features/                                       -> All features of the platform.
        <feature_name>/                             -> Folder containing all sub-folders corresponding to one feature and the contribution request [WP_CONT_REQUEST]
            docs/                                   -> Documentation of the feature consisting of ...
                architecture/                       -> ... Feature architecture [WP_FEATURE_ARCHITECTURE].
                requirements/                       -> ... Feature requirements [WP_FEATURE_REQ].
                safety_analysis/                    -> ... Safety analysis on feature level [WP_FEATURE_SAFETY_ANALYSES]
                safety_planning/                    -> ... the feature specific safety workproducts planning
                verification/                       -> ... Feature verification report (reporting all feature verifications) [WP_PLATFORM_SW_VERIFICATION_REPORT]
            tests/                                  -> Feature tests, consisting of ...
                integration-tests/                  -> ... integration tests [WP_FEATURE_INTEGRATION_TEST].
        toolchain/                                  -> Definition of toolchain

    modules/                                        -> Modules of the SW platform.
        <module_name>/                              -> Folder containing all artifacts corresponding to one module.
            docs/                                   -> Documentation of the module consisting of ...
                manual/                             -> ... Module manual, e.g. integration manual, assumptions of use and safety manual [WP_SW_COMPONENT_AOU], [WP_MODULE_SW_SAFETY_MANUAL].
                release/                            -> ... Module release note [WP_MODULE_SW_RELEASE_NOTE] plus safety assessment [WP_ASSESSMENT_REPORT]
                safety_plan/                        -> ... Module safety plan [WP_MODULE_SAFETY_PLAN], module safety case [WP_MODULE_SAFETY_CASE] and their conformance reviews [WP_CMR_REPORTS]
                safety_analysis/                    -> ... Safety analysis on module level [WP_SW_COMPONENT_DFA]
                verification/                       -> ... Module verification report (reporting all module's components verifications) [WP_MODULE_SW_VERIFICATION_REPORT] plus safety analysis conformance reviews [WP_CMR_REPORTS]

            components/                             -> Components of the module.
                <component_name>/                   -> Folder containing all artifacts corresponding to one component.
                    docs/                           -> Documentation of the component consisting of ...
                        architecture/               -> ... Component architecture (only if sub-components exist) [WP_SW_COMPONENT_ARCHITECTURE].
                        requirements/               -> ... Component requirements [WP_SW_COMPONENT_REQ] and HSI (if relevant) [WP_HSI].
                        safety_analysis/            -> ... Safety analysis on component level [WP_SW_COMPONENT_SAFETY_ANALYSES]
                        verification/               -> ... Architecture review [WP_SW_ARCH_VERIFICATION], code inspection [WP_SW_CODE_INSPECT]
                    src/                            -> Source files of the component (incl. detailed design) [WP_SW_IMPLEMENTATION].
                    include/                        -> Include files of the component
                    tests/                          -> Component tests, consisting of ...
                        unit/                       -> ... unit tests [WP_SW_UNIT_TEST] (for lowest level of components).
                        integration/                -> ... integration tests [WP_SW_COMPONENT_INTEGRATION_TEST].
                        verification/               -> ... verification tests [WP_SW_COMPONENT_TEST].
                    <sub_component_name>/           -> Sub-Component of the Component.
                         copy the relevant folders below <component-name> if applicable (example: no code inspection needed for sub-components from the Open Source)

    platform_integration_tests/                     -> Integration tests on reference hardware.

    process/                                        -> process definition including workflows, workproducts, roles, guidance [WP_PROCESS_DEFINITION]

    registry/                                       -> infrastructure configuration

    README.md                                       -> Entrypoint of the repository.

.. toctree::
   :maxdepth: 1
   :glob:
