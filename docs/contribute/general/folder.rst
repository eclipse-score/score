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
    ├── architecture/                  -> Platform architecture description [:need:`wp__platform_arch`]
    ├── contribute/                    -> Description on how to contribute
    │                                     [:need:`wp__sw_development_plan`],
    │                                     [:need:`wp__training_path`]
    ├── design_decision/               -> Design decisions on platform level
    ├── features/                      -> All features of the platform. [:need:`wp__platform_arch`]
    │   └── <feature_name>/            -> Features including feature id, logical interfaces and feature
    │       │                             (change) request [:need:`wp__feat_request`] and belonging sub-folders
    │       ├── architecture/          -> Feature architecture [:need:`wp__feature_arch`]
    │       │                             only feature id and logical interface definition
    │       │                             (static and dynamic architecture only if the feature is not yet
    │       │                             implemented by one module, otherwise the static and dynamic
    │       │                             architecture is defined in the module repository)
    │       └── requirements/          -> Feature requirements [:need:`wp__requirements_feat`]
    ├── glossary/                      -> Glossary of abbreviations used in the platform context
    ├── handbook/                      -> Background, scope, high-level architecture of the platform features
    │                                     and handbook for the platform [:need:`wp__platform_handbook`],
    │                                     (e.g., onboarding, development guidelines, etc.)
    ├── manuals/                       -> User and integration manual(s) of the platform,
    │                                     may refer in the reference integration repository to the manuals for the modules.
    ├── platform_management_plan/      -> Overall Platform Management Plan [:need:`wp__platform_mgmt`]
    │                                     containing: [:need:`wp__project_mgt`], [:need:`wp__platform_safety_plan`],
    │                                     [:need:`wp__platform_security_plan`], [:need:`wp__qms_plan`],
    │                                     [:need:`wp__config_mgt_plan`], [:need:`wp__tlm_plan`],
    │                                     [:need:`wp__platform_sw_release_plan`], [:need:`wp__prm_plan`],
    │                                     [:need:`wp__chm_plan`],
    │                                     [:need:`wp__verification_plan`], [:need:`wp__document_mgt_plan`],
    │                                     [:need:`wp__issue_track_system`] (mentioned),
    │                                     [:need:`wp__policies`], [:need:`wp__tailoring_work_products`]
    │                                     [:need:`wp__safety_tailoring`]
    │                                     also mention [:need:`wp__process_description`] and [:need:`wp__process_strategy`]
    ├── quality/                       -> Quality documentation on platform level: [:need:`wp__qms_report`],
    │                                     [:need:`wp__process_impr_report`]
    ├── requirements/                  -> Requirements on platform level
    │   ├── stakeholder/               -> Stakeholder requirements [:need:`wp__requirements_stkh`]
    │   ├── tool/                      -> Tool requirements (not covered in tool repositories)
    │   │                                 [:need:`wp__requirements_proc_tool`]
    │   └── platform_assumptions/      -> Assumptions of use on platform level [:need:`wp__requirements_sw_platform_aou`]
    ├── safety/                        -> Safety documentation on platform level (SEooC):
    │                                     [:need:`wp__platform_dfa`], [:need:`wp__platform_safety_manual`],
    │                                     [:need:`wp__platform_safety_package`], [:need:`wp__fdr_reports`],
    │                                     [:need:`wp__audit_report`]
    ├── score_tools/                   -> Tool list and [:need:`wp__tool_verification_report`]
    ├── security/                      -> Security documentation on platform level:
    │                                     [:need:`wp__platform_security_manual`], [:need:`wp__platform_security_package`],
    │                                     [:need:`wp__sw_platform_sbom`], [:need:`wp__platform_security_analysis`],
    │                                     [:need:`wp__audit_report_security`]
    └── tools/                         -> Platform tools (not covered in tool repositories)
        └── decision_records/          -> Design decision records for tools on platform level
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
    cli/                               -> CLI tool running on the target to guide users through examples
    docs/                              -> Documentation of the reference integration
    ├── score_releases/                -> [:need:`wp__platform_sw_release_note`]
    └── verification_report/           -> Platform verification report (reporting all platform feature's verifications)
                                          [:need:`wp__verification_platform_ver_report`]
    feature_integration_tests/         -> Feature integration tests executed in the reference integration.
    │                                     [:need:`wp__verification_feat_int_test`]
    ├── configs/                       -> Configuration files for test execution
    ├── itf/                           -> Target-based tests using the Integration Test Framework
    ├── test_cases/                    -> Test orchestration, assertions, and shared fixtures
    │   └── tests/
    │       └── <feature_name>/        -> Test cases grouped by the feature under verification
    └── test_scenarios/                -> Executable scenarios invoked by the test cases
        ├── cpp/
        │   └── <feature_name>/        -> C++ scenarios for the feature
        └── rust/
            └── <feature_name>/        -> Rust scenarios for the feature
    images/                            -> Concrete images for each target platform as Bazel modules.
                                          Each platform has its own folder named ``platform_arch``,
                                          e.g. ``qnx_aarch64``, ``autosd_x86_64``, ``ebclfsa_aarch64``,
                                          ``linux_x86_64``. Each image deploys all showcases and
                                          contains platform-specific code.
    known_good.json                    -> Pinned versions of all integrated S-CORE modules
    patches/                           -> Patches applied during the build
    platform_integration_tests/        -> Integration tests on reference hardware verifying stakeholder requirements.
                                          [:need:`wp__verification_platform_int_test`]
                                          A further subfolder structuring (for example by feature or stakeholder area) is possible.
    runners/                           -> Thin logic to reuse runners (e.g. docker runner) between images
    rust_coverage/                     -> Rust coverage configuration
    scripts/                           -> Internal tooling scripts (known_good management,
        │                                 workspace metadata generation, etc.)
        └── tooling/                   -> Single point of interaction with all tooling artifacts
    showcases/                         -> S-CORE wide showcases deployed into images
    score_starter                      -> Launcher script to select and run an integration scenario
    MODULE.bazel                       -> Bazel module definition
    README.md                          -> Entrypoint of the repository

Language and feature subfolders under ``feature_integration_tests/`` are only needed when used.
Use the documented feature name consistently for test cases and scenarios, and keep shared fixtures
at the nearest common parent. Feature integration tests verify feature requirements, whereas
``platform_integration_tests/`` verify stakeholder requirements; execution on hardware or QEMU
alone does not determine the test level.

.. _module_folder_structure:

Module Folder Structure
-----------------------

The modules and components shall follow a defined folder structure, which is maintained in the `module template repository <https://eclipse-score.github.io/module_template/main/template>`_ .

Th folder structure is confirmed by :need:`dec_rec__platform__module_folder_structure`.
