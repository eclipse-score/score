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

Tracing Requirements
####################

.. document:: Tracing Requirements
   :id: doc__tracing_requirements
   :status: valid
   :version: 1
   :safety: QM
   :security: YES
   :realizes: wp__requirements_feat[version==1]

.. feat_req:: Tracing Support
   :id: feat_req__tracing__support
   :reqtype: Functional
   :security: NO
   :safety: QM
   :derived_from: stkh_req__dev_experience__logging_support[version==1]
   :satisfied_by: feat__tracing[version==1]
   :status: valid
   :version: 1
   :valid_from: v1.0.0

   The tracing :term:`framework` shall be able to trace opaque data provided by registered trace clients.
