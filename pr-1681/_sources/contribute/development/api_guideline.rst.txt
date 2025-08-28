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

Designing API
#############

.. document:: API Guidelines
   :id: doc__api_guidelines
   :status: draft

User friendly API design
========================

* Each public API shall support the idioms of the programming language it is written in.
* Each public API shall use core infrastructure of its programming language and accompanying standard libraries, whenever possible and meaningful.

Error handling
==============

* (C++) exceptions shall not be used for error handling, as these will be directly leading to an abort and thus reducing availability of the S-CORE platform.
* The best way to deal with errors is to try to resolve those component internally. If not possible the caller of the function shall be notified of the error.
* For (error) returns there is a specific library to be used in S-CORE, it is the Score::Result library which is part of the :ref:`baselibs_feature` feature.
