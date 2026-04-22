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


.. document:: Static Reflection Architecture Inspection Checklist
   :id: doc__static_reflection_arc_inspection
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__sw_arch_verification

Architecture Inspection Checklist
=================================

Component is missing in feature architecture :need:`doc__baselibs_architecture` and this has to be corrected.

The following static views in "valid" state and with "inspected" tag set are in the scope of this inspection:

.. needtable::
   :filter: "static_reflection" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_sta
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title

and the following dynamic views:

.. needtable::
   :filter: "static_reflection" in docname and "architecture" in docname and docname is not None and status == "valid"
   :style: table
   :types: comp_arc_dyn
   :columns: id;status;tags
   :colwidths: 25,25,25
   :sort: title
