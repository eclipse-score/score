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
                                          [:need:`wp__sw_development_plan`],
                                          [:need:`wp__training_path`]
        design_decision/               -> Design decisions on platform level
        features/                      -> All features of the platform. [:need:`wp__platform_arch`]
            <feature_name>/            -> Features including feature id, logical interfaces and feature
                                       -> (change) request [:need:`wp__feat_request`] and belonging sub-folders
               architecture/           -> Feature architecture [:need:`wp__feature_arch`]
                                             only feature id and logical interface definition
                                             (static and dynamic architecture only if the feature is not yet
                                             implemented by one module, otherwise the static and dynamic
                                             architecture is defined in the module repository)
               requirements/           -> Feature requirements [:need:`wp__requirements_feat`]
        glossary/                      -> Glossary of abbreviations used in the platform context
        handbook/                      -> Background, scope, high-level architecture of the platform features
                                             and handbook for the platform [:need:`wp__platform_handbook`],
                                             (e.g., onboarding, development guidelines, etc.)
        manuals/                       -> User and integration manual(s)
        modules/                       -> Modules of the SW platform. [:need:`wp__platform_arch`]
        platform_management_plan/      -> Overall Platform Management Plan [:need:`wp__platform_mgmt`]
                                             containing: [:need:`wp__project_mgt`], [:need:`wp__platform_safety_plan`],
                                             [:need:`wp__platform_security_plan`], [:need:`wp__qms_plan`],
                                             [:need:`wp__config_mgt_plan`], [:need:`wp__tlm_plan`],
                                             [:need:`wp__platform_sw_release_plan`], [:need:`wp__prm_plan`],
                                             [:need:`wp__chm_plan`],
                                             [:need:`wp__verification_plan`], [:need:`wp__document_mgt_plan`],
                                             [:need:`wp__issue_track_system`] (mentioned),
                                             [:need:`wp__policies`], [:need:`wp__tailoring_work_products`]
                                             [:need:`wp__safety_tailoring`]
                                             also mention [:need:`wp__process_description`] and [:need:`wp__process_strategy`] (own repository)
        quality/                       -> Quality documentation on platform level: [:need:`wp__qms_report`],
                                             [:need:`wp__process_impr_report`]
        requirements/                  -> Requirements on platform level
            stakeholder/               -> Stakeholder requirements [:need:`wp__requirements_stkh`]
            tool/                      -> Tool requirements (not covered in tool repositories)
                                             [:need:`wp__requirements_proc_tool`]
            platform_assumptions/      -> Assumptions of use on platform level [:need:`wp__requirements_sw_platform_aou`]
        safety/                        -> Safety documentation on platform level (SEooC):
                                             [:need:`wp__platform_dfa`], [:need:`wp__platform_safety_manual`],
                                             [:need:`wp__platform_safety_package`], [:need:`wp__fdr_reports`],
                                             [:need:`wp__audit_report`]
        score_releases/                -> [:need:`wp__platform_sw_release_note`]
        score_tools/                   -> Tool list and [:need:`wp__tool_verification_report`]
        security/                      -> Security documentation on platform level:
                                             [:need:`wp__platform_security_manual`], [:need:`wp__platform_security_package`],
                                             [:need:`wp__sw_platform_sbom`], [:need:`wp__platform_security_analysis`],
                                             [:need:`wp__audit_report_security`]
        verification_report/           -> Platform verification report (reporting all platform feature's verifications)
                                             [:need:`wp__verification_platform_ver_report`]
    tools/                             -> Platform tools (not covered in tool repositories)
        decision_records/              -> Design decision records for tools on platform level
    README.md                          -> Entrypoint of the repository

.. _reference_integration_folder_structure:

Reference Integration Repository Folder Structure
-------------------------------------------------

The reference integration repository (see `reference_integration <https://github.com/eclipse-score/reference_integration>`_)
integrates multiple Eclipse S-CORE modules into a single Bazel build environment to validate
cross-repository builds and detect integration issues early in the development cycle.

.. parsed-literal::

    bazel_common/                      -> Common Bazel functionalities shared across images:
                                             toolchain setups, common tooling deps,
                                             common S-CORE module deps, common .bzl extensions
    ci/                                -> CI configuration and scripts
    docs/                              -> Documentation of the reference integration
    feature_integration_tests/         -> Feature integration tests verifying stakeholder requirements.
                                             [:need:`wp__verification_platform_int_test`]
    images/                            -> Concrete images for each target platform as Bazel modules.
                                             Each platform has its own folder named ``{platform}_{arch}``,
                                             e.g. ``qnx_aarch64``, ``autosd_x86_64``, ``ebclfsa_aarch64``,
                                             ``linux_x86_64``. Each image deploys all showcases and
                                             contains platform-specific code.
    patches/                           -> Patches applied during the build
    runners/                           -> Thin logic to reuse runners (e.g. docker runner) between images
    rust_coverage/                     -> Rust coverage configuration
    scripts/                           -> Internal tooling scripts (known_good management,
                                             workspace metadata generation, etc.)
        tooling/                       -> Single point of interaction with all tooling artifacts
    showcases/                         -> S-CORE wide showcases deployed into images
        cli/                           -> CLI tool running on the target to guide users through examples
    MODULE.bazel                       -> Bazel module definition
    known_good.json                    -> Pinned versions of all integrated S-CORE modules
    score_starter                      -> Launcher script to select and run an integration scenario
    README.md                          -> Entrypoint of the repository

.. _module_folder_structure:

Module Folder Structure
-----------------------

The modules and components shall follow the folder structure which was presented. However if there are good reasons the structure can be adapted.

See also `module template repository <https://github.com/eclipse-score/module_template>`_ for more details on the folder structure of a module.

.. parsed-literal::

   <module_name>/                      -> Folder containing all artifacts corresponding to one module.
                                             As folder optional if the repository only contains a single module.
      docs/                            -> Documentation of the module
        features/                      -> All features of the module.
            <feature_name>/            -> Features including sub-folders and feature/component (change) request
                                             [:need:`wp__feat_request`], [:need:`wp__cmpt_request`]
               architecture/           -> Feature architecture [:need:`wp__feature_arch`], [:need:`wp__sw_arch_verification`]
               safety_analysis/        -> Safety analysis on feature level [:need:`wp__feature_fmea`], [:need:`wp__feature_dfa`]
               safety_planning/        -> Feature specific safety workproducts planning  [:need:`wp__platform_safety_plan`]
               security_analysis/      -> Security analysis on feature level [:need:`wp__feature_security_analysis`]
               security_planning/      -> Feature specific security workproducts planning  [:need:`wp__platform_security_plan`]
         manuals/                      -> Module manual, e.g. integration manual, assumptions of use,
                                             safety manual [:need:`wp__requirements_comp_aou`],
                                             [:need:`wp__requirements_feat_aou`],
                                             [:need:`wp__module_safety_manual`],
                                             security_manual [:need:`wp__module_security_manual`].
         release/                      -> Module release note [:need:`wp__module_sw_release_note`],
                                             module release plan [:need:`wp__module_sw_release_plan`],
         safety_mgt/                   -> Module safety plan [:need:`wp__module_safety_plan`],
                                             module safety package [:need:`wp__module_safety_package`],
                                             formal documents reviews [:need:`wp__fdr_reports`],
                                             safety analysis formal reviews [:need:`wp__fdr_reports`],
                                             safety tailoring [:need:`wp__safety_tailoring`]
                                             safety component classification [:need:`wp__sw_component_class`]
         security_mgt/                 -> Module security plan [:need:`wp__module_security_plan`],
                                             module security package [:need:`wp__module_security_package`],
                                             formal documents reviews [:need:`wp__fdr_reports_security`],
                                             module SW bill of material [:need:`wp__sw_module_sbom`]
         verification_report/          -> Module verification report
                                             module verifications [:need:`wp__verification_module_ver_report`],
      score/                           -> Folder containing all artifacts corresponding to all components of the module.
         <component_name>/             -> Components of the module.
                                             Folder containing all artifacts corresponding to one component.
            docs/                      -> Documentation of the component
                architecture/          -> Component architecture (only if lower level components exist)
                                             [:need:`wp__component_arch`].
                detailed_design/       -> Detailed Design [:need:`wp__sw_implementation`] and
                                             Detail design + code inspection [:need:`wp__sw_implementation_inspection`],
                manuals/               -> User documentation (of a single component, e.g., user manual of a library component, optional)
                requirements/          -> Component requirements [:need:`wp__requirements_comp`],
                                             requirements inspection [:need:`wp__requirements_inspect`]
                safety_analysis/       -> Safety analysis on component level (only if component architecture exists)
                                             [:need:`wp__sw_component_fmea`], [:need:`wp__sw_component_dfa`]
                security_analysis/     -> Security analysis on component level (only if component architecture exists)
            src/                       -> Source files of the component consisting of
                                             Include files
                                             Source Files [:need:`wp__sw_implementation`]
                                             Test doubles
                                             Unit tests [:need:`wp__verification_sw_unit_test`]
                <lower_level_comp>/    -> lower level component following <component_name> folder structure
                tests/                 -> Component-level tests (e.g., unit tests) [:need:`wp__verification_sw_unit_test`]
            tests/                     -> Module-level tests (e.g., feature integration tests, system tests) [:need:`wp__verification_comp_int_test`]
                                       -> Feature Integration tests [:need:`wp__verification_feat_int_test`]
