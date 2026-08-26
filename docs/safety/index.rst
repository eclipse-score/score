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

.. _platform_safety:

Platform Safety Documents
=========================

.. document:: Platform Safety Documents
   :id: doc__safety_documents_platform
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__safety_tailoring[version==1]
   :tags:

.. needtable:: Platform Safety Documents
   :style: table
   :columns: title;id;safety;security;status
   :colwidths: 25,45,10,10,10
   :sort: docname

   results = []

   for need in needs.filter_types(["document"]):
       if need["docname"] is not None and "safety/" in need["docname"] and need["docname"] != "safety/index":
          results.append(need)

.. toctree::
   :maxdepth: 1
   :hidden:

   fdr_reports_safety_analyses_DFA
   fdr_reports_safety_package
   fdr_reports_safety_platform_safety_plan
   platform_dfa
   platform_safety_manual
