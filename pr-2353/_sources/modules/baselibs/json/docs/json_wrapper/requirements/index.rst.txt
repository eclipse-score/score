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
============

.. document:: JSON Wrapper Requirements
   :id: doc__json_wrapper_requirements
   :status: valid
   :safety: ASIL_B
   :realizes: wp__requirements_comp

Due to low complexity, the requirements of the JSON component were not split into the "sub" components
"JSON Wrapper" and "nlohman_json". Reasoning is the low number of requirements (only about ten).
The component split was done nevertheless, because "JSON Wrapper" is implemented as part of the S-CORE project and
"nlohman_json" is reused from open source.

So the requirements for "JSON Wrapper" are documented in :need:`doc__json_requirements`
(all requirements which are "fulfilled_by" :need:`comp_arc_sta__baselibs__json_wrapper`)
