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

.. _naming_convention_files:

Naming Conventions of Files
---------------------------

The overall naming convention is to use snake case for all files and folders (all files are named lowercase and spaces are replaced by underscores).

.. _naming_convention_needs:

Naming Convention for UIDs
--------------------------

The naming convention for the UIDs of **all** elements shall be defined as follows:

* It should not exceed 30 characters
* It shall show a meaningful name
* It shall only consist of lowercase, digits and underscores

For the naming of the UIDs also following convention shall be applied:

* It shall consist of 3 parts separated by double underscore
   * | prefix
     | (defined in the Metamodel)
   * | structural element
     | (e.g. abbreviation for the feature / subfeature)
   * | keyword (s)
     | (keyword(s) referring the the description, separated by underscore)

As examples:

* feat_req__ipc__e2e_protection
* comp_req__kvs__storage

Only for **process UIDs** the structural element is optional:

* gd_temp__review
* gd_req__req__structure

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
        platform_management_plan/                   -> Overall Platform Management Plan  [wp__PLATFORM_MGMT], consisting of ...
            project_management.rst                  -> ... Project Management.
            stakeholder_management.rst              -> ... Stakeholder Management.
            safety_management.rst                   -> ... Safety Management incl. platform safety plan [wp__PLATFORM_SAFETY_PLAN]
            risk_management.rst                     -> ... Risk Management.
            quality_management.rst                  -> ... Quality Management [wp__QMS].
            config_management.rst                   -> ... Configuration Management.
            tool_management.rst                     -> ... Tool Management.
            release_management.rst                  -> ... Release Management.
            problem_resolution.rst                  -> ... Problem Management.
            change_management.rst                   -> ... Change Management.
            requirements_management.rst             -> ... Requirements Management.
            software_development.rst                -> ... Development [wp__SW_DEV_PLAN].
            software_verification.rst               -> ... Verification [wp__VERIFICATION_PLAN].
            documentation_management.rst            -> ... Documentation Management.
            security_management.rst                 -> ... Security Management.
        release/                                    -> [wp__PLATFORM_SW_RELEASE_NOTE]
        safety/                                     -> safety documentation on platform level (SEooC): [wp__FEATURE_DFA], [wp__PLATFORM_SW_SAFETY_MANUAL], [wp__PLATFORM_SAFETY_CASE], [wp__CMR_REPORTS], [wp__ASSESSMENT_REPORT]
        security/                                   -> security documentation on platform level
        requirements/                               -> requirements on platform level ...
            stakeholder/                            -> ... Stakeholder requirements [wp__STAKEHOLDER_REQ].
            tool/                                   -> ... Tool requirements [wp__TOOL_REQ]
        tutorials/                                  -> General tutorials.

    examples/                                       -> examples how a C++, Rust, Python module can be set up

    features/                                       -> All features of the platform.
        <feature_name>/                             -> Folder containing all sub-folders corresponding to one feature and the contribution request [wp__CONT_REQUEST]
            docs/                                   -> Documentation of the feature consisting of ...
                architecture/                       -> ... Feature architecture [WP_FEATURE_ARCHITECTURE].
                requirements/                       -> ... Feature requirements [wp__requirements__feat].
                safety_analysis/                    -> ... Safety analysis on feature level [WP_FEATURE_SAFETY_ANALYSES]
                safety_planning/                    -> ... the feature specific safety workproducts planning
                verification/                       -> ... Feature verification report (reporting all feature verifications) [wp__PLATFORM_SW_VERIFICATION_REPORT]
            tests/                                  -> Feature tests, consisting of ...
                integration-tests/                  -> ... integration tests [wp__FEATURE_INTEGRATION_TEST].
        toolchain/                                  -> Definition of toolchain

    modules/                                        -> Modules of the SW platform.
        <module_name>/                              -> Folder containing all artifacts corresponding to one module.
            docs/                                   -> Documentation of the module consisting of ...
                manual/                             -> ... Module manual, e.g. integration manual, assumptions of use and safety manual [wp__SW_COMPONENT_AOU], [wp__MODULE_SW_SAFETY_MANUAL].
                release/                            -> ... Module release note [wp__MODULE_SW_RELEASE_NOTE] plus safety assessment [wp__ASSESSMENT_REPORT]
                safety_plan/                        -> ... Module safety plan [wp__MODULE_SAFETY_PLAN], module safety case [wp__MODULE_SAFETY_CASE] and their conformance reviews [wp__CMR_REPORTS]
                safety_analysis/                    -> ... Safety analysis on module level [wp__SW_COMPONENT_DFA]
                verification/                       -> ... Module verification report (reporting all module's components verifications) [wp__MODULE_SW_VERIFICATION_REPORT] plus safety analysis conformance reviews [wp__CMR_REPORTS]

            components/                             -> Components of the module.
                <component_name>/                   -> Folder containing all artifacts corresponding to one component.
                    docs/                           -> Documentation of the component consisting of ...
                        architecture/               -> ... Component architecture (only if sub-components exist) [wp__SW_COMPONENT_ARCHITECTURE].
                        requirements/               -> ... Component requirements [wp__SW_COMPONENT_REQ] and HSI (if relevant) [wp__HSI].
                        safety_analysis/            -> ... Safety analysis on component level [wp__SW_COMPONENT_SAFETY_ANALYSES]
                        verification/               -> ... Architecture review [wp__SW_ARCH_VERIFICATION], code inspection [wp__SW_CODE_INSPECT]
                    src/                            -> Source files of the component (incl. detailed design) [wp__SW_IMPLEMENTATION].
                    include/                        -> Include files of the component
                    tests/                          -> Component tests, consisting of ...
                        unit/                       -> ... unit tests [wp__SW_UNIT_TEST] (for lowest level of components).
                        integration/                -> ... integration tests [wp__SW_COMPONENT_INTEGRATION_TEST].
                        verification/               -> ... verification tests [wp__SW_COMPONENT_TEST].
                    <sub_component_name>/           -> Sub-Component of the Component.
                         copy the relevant folders below <component-name> if applicable (example: no code inspection needed for sub-components from the Open Source)

    platform_integration_tests/                     -> Integration tests on reference hardware.

    process/                                        -> process definition including workflows, workproducts, roles, guidance [wp__PROCESS_DEFINITION]

    registry/                                       -> infrastructure configuration

    README.md                                       -> Entrypoint of the repository.

.. toctree::
   :maxdepth: 1
   :glob:
