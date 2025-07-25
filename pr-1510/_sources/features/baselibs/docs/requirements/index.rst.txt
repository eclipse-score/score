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

Requirements
############

.. feat_req:: Core Software Utilities
   :id: feat_req__baselibs__core_utilities
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__base_libraries
   :status: valid

   The base libraries shall include core software utilities and common infrastructure components needed by multiple platform modules.

.. feat_req:: Safety Relevance
   :id: feat_req__baselibs__safety
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__base_libraries, stkh_req__dependability__automotive_safety
   :status: valid

   The base libraries shall implement functionality necessary to support safety-relevant platform components up to ASIL-B for selected functionalities.

.. feat_req:: Multi-Language APIs
   :id: feat_req__baselibs__multi_language_apis
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__base_libraries, stkh_req__dev_experience__prog_languages, stkh_req__dependability__automotive_safety
   :status: valid

   The base libraries shall provide APIs for C++, Rust, or both, depending on the requirements of consuming platform components.

.. feat_req:: Consistent APIs
   :id: feat_req__baselibs__consistent_apis
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__base_libraries, stkh_req__dev_experience__prog_languages, stkh_req__overall_goals__reuse_of_app_soft
   :status: valid

   The base libraries shall provide consistent APIs while respecting language-specific idioms.

.. feat_req:: Maintainable Design
   :id: feat_req__baselibs__maintainable_design
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__base_libraries, stkh_req__overall_goals__reuse_of_app_soft
   :status: valid

   The base libraries shall be designed for maintainability and code reuse.

.. feat_req:: Security Robustness
   :id: feat_req__baselibs__security
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__base_libraries
   :status: valid

   The base libraries shall adhere to secure coding standards to prevent vulnerabilities across platform components.
