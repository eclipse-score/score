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

Requirements
############

Terms and definitions
=====================

.. feat_req:: Term definition of Parameter
   :id: feat_req__config_mgmt__term_parameter
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   An individual vehicle configuration property used for vehicle specific adaptations is called ``Parameter``.

.. feat_req:: Term definition of Parameter Set
   :id: feat_req__config_mgmt__term_parameter_set
   :reqtype: Non-Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Group of Parameters which belong to the same functionality and share an integrity protection is called ``Parameter Set``.

Data Housekeeping
=================

.. feat_req:: Central housekeeping for Parameters
   :id: feat_req__config_mgmt__central_housekeeping
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Configuration Management shall provide a central housekeeping for Parameters.

.. feat_req:: Parameter relation to a Set
   :id: feat_req__config_mgmt__parameter_set_relation
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Every Parameter shall be contained in exactly one Parameter Set.

.. feat_req:: Parameter name uniqueness
   :id: feat_req__config_mgmt__prm_name_unique
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Parameters names shall be unique for an ECU project.

.. feat_req:: Parameter name uniqueness
   :id: feat_req__config_mgmt__prm_set_name_unique
   :reqtype: Functional
   :security: NO
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Parameters Set names shall be unique for an ECU project.

.. feat_req:: Parameter Set configuration contents
   :id: feat_req__config_mgmt__prm_set_cfg_content
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Parameter Set configuration shall contain a mapping of Parameters to Parameter Sets, Parameter names and default values.

.. feat_req:: Parameter Set configuration source
   :id: feat_req__config_mgmt__prm_set_cfg_source
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Parameter Set configuration shall be determined solely by a read-only input source, deployed on the target.

.. feat_req:: Parameter modification
   :id: feat_req__config_mgmt__parameter_modification
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Parameter values shall be modifiable during runtime regarding modification procedure specific for a parameter kind.

Parameter Provision
===================

.. feat_req:: Config provider interface
   :id: feat_req__config_mgmt__provider_interface
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   Configuration Management shall provide a generic interface, independent of any Parameter definitions, for applications to access Parameters in read-only mode.

.. feat_req:: Parameter Set access
   :id: feat_req__config_mgmt__parameter_set_access
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__functional_req__file_based
   :status: valid

   A Parameter Set shall be accessible via interface using a key-value principle, where user application passes a Parameter Set name to the interface and its value is returned as result.

Parameter Qualification
=======================

.. feat_req:: Parameter Set qualifier
   :id: feat_req__config_mgmt__prm_set_qualifier
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__safe_config
   :status: valid

   A Parameter Set shall contain a qualifier to indicate its integrity.

.. feat_req:: Parameter initial qualifier
   :id: feat_req__config_mgmt__prm_initial_qualifier
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__safe_config
   :status: valid

   There shall exist an overall qualifier for all Parameter Sets to indicate the state of integrity checks at the point of time of initial provision of parameters.
