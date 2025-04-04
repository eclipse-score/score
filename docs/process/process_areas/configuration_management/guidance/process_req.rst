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

Configuration Management Process Requirements
=============================================

.. gd_req:: Permanent Storage
   :id: gd_req__workproducts_storage
   :status: valid
   :complies: std_req__iso26262__support_745

   At least every platform release shall be stored permanently as a collection of text documents
   (docs and code) including the used OSS tooling outside of github servers.

   Note: This is to ensure to have the development artefacts available during the complete lifetime of the
   products (cars) the SW platform is used in.



.. gd_req:: Baseline Differences
   :id: gd_req__baseline_diff
   :status: valid
   :complies: std_req__iso26262__support_741

   It shall be possible to show the differences between two baselines.

   Note: This could be done by showing all the commits which happened between these baselines in one release branch.
