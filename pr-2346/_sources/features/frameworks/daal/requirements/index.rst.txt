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

General
================================

.. feat_req:: Support for Time-based Architecture
   :id: feat_req__daal__time_based_arch
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_time
   :status: valid

   The daal framework shall provide Trigger to support a time-based architecture.

.. feat_req:: Lifecycle Interface
   :id: feat_req__daal__lifecycle
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__overall_goals__reuse_of_app_soft,stkh_req__execution_model__processes,stkh_req__execution_model__low_power
   :status: valid

   Lifecycle of executables should use one generic API

.. feat_req:: Execution Environments
   :id: feat_req__daal__env
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__functional_req__operating_system
   :status: valid

   It should be possible to use the framework with all specified os like qnx and linux



.. feat_req:: Communication
   :id: feat_req__daal__com
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__app_architectures__support_data
   :status: valid

   The communication layer should use the IPC Framework

.. feat_req:: Logging
   :id: feat_req__daal__log
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dev_experience__logging_support
   :status: valid

   Core Logging API should be used

.. feat_req:: Trigger
   :id: feat_req__daal__trigger
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Singe Shot and Cyclic execution should be possible

.. feat_req:: Health & Error Management
   :id: feat_req__daal__health_error
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Error and Health Management should be availability


Open Issues
-----------

[Any points that are still being decided/discussed.]

   .. note::
       While a CR is in draft, ideas can come up which warrant further discussion.
       Those ideas should be recorded so people know that they are being thought about but do not have a concrete resolution.
       This helps make sure all issues required for the CR to be ready for consideration are complete and reduces people duplicating prior discussion.



Footnotes
---------

[A collection of footnotes cited in the CR, and a place to list non-inline hyperlink targets.]
