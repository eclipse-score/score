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

.. _process_safety_analysis:

Process Safety Analysis
=======================

.. gd_req:: Safety Analysis Structure
   :id: gd_req__saf__structure
   :status: valid
   :tags: structure
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Safety Analysis shall be hierarchically grouped into different levels.

   Following levels are defined:

      * Feature architecture
      * Component architecture

.. _process_safety_analysis_attributes:

Process Safety Analysis Attributes
----------------------------------

.. gd_req:: Safety Analysis attribute: UID
   :id: gd_req__saf__attr_uid
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Each Safety Analysis shall have a unique ID. It shall be in a format which is also human readable and consists of

      * type of Safety Analysis
      * keyword descirbing the level of analysis
      * keyword describing the content of the Safety Analysis

   The naming convention is defined here: :ref:`naming_convention_needs`

.. gd_req:: Safety Analysis attribute: title
   :id: gd_req__saf_attr_title
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   The title of the Safety Analysis shall provide a short summary of the description

.. gd_req:: Safety Analysis attribute: description
   :id: gd_req__saf_attr_description
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Each Safety Analysis shall have a description. With this another person should be able to recognize the results of the Safety Analysis

.. gd_req:: DFA attribute: violation ID
   :id: gd_req__saf__attr_vid
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Each DFA shall have a violation ID. The violation ID is used to identify the related fault <:need:`gd_guidl__fault_models`>.

.. gd_req:: DFA attribute: violation cause
   :id: gd_req__saf__attr_vcause
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Every DFA shall have a short description of the violation cause.

.. gd_req:: FMEA attribute: failure node
   :id: gd_req__saf__attr_fnode
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Each FMEA shall have a failure node. The failure nod is used to identify the related fault <:need:`gd_guidl__fault_models`>.

.. gd_req:: FMEA attribute: failure effect
   :id: gd_req__saf__attr_veffect
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Every FMEA shall have a short description of the failure effect.

.. gd_req:: Safety Analysis attribute: measure
   :id: gd_req__saf_attr_measure
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_844, std_req__iso26262__analysis_746, std_req__iso26262__analysis_747

   Each violation shall have a measure for it.

.. gd_req:: Safety Analysis attribute: sufficient
   :id: gd_req__saf__attr_sufficient
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   Each measure shall have an statement if it's sufficient.

.. gd_req:: Requirement attribute: argument
   :id: gd_req__saf__attr_argument
   :status: valid
   :tags: attribute, mandatory
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   The argument shall describe why the measure is sufficient or not.

.. _process_safety_analysis_linkage:

Safety Analysis Requirement Linkage
'''''''''''''''''''''''''''''''''''

.. gd_req:: Safety Analysis Linkage
   :id: gd_req__saf__linkage
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   Safety Analysis shall be linked to its adjacent level via the attribute mitigates.

      * Feature Safety Analysis <-> feature architecture
      * Component Safety Analysis <-> component architecture

.. gd_req:: Safety Analysis attribute: measure coverage
   :id: gd_req__saf__attr_saf_cov
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   It shall be possible to specify the measure coverage.

      * 0 to 100 percent

.. gd_req:: Safety Analysis attribute: link to Aou
   :id: gd_req__saf__attr_aou
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_845

   It shall be possible to link Aou.

.. gd_req:: Safety Analysis attribute: versioning
   :id: gd_req__saf__attr_hash
   :status: valid
   :tags: attribute, automated
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies:

   It shall be possible to provide a versioning for Safety Analysis. It shall be possible to detect if any of the mandatory attributes differ from the versioning: :need:`gd_req__saf__attr_mandatory`


.. _process_safety_analysis_checks:

Process Requirements Checks
'''''''''''''''''''''''''''

.. gd_req:: Safety Analysis mandatory attributes provided
   :id: gd_req__saf__attr_mandatory
   :status: valid
   :tags: attribute, check
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   It shall be checked if all mandatory attributes for each Safety Analysis is provided by the user. For all Safety Analysis following attributes shall be mandatory:

   .. needtable:: Overview mandatory Safety Analysis attributes
      :filter: "mandatory" in tags and "attribute" in tags and "safety analysis" in tags and type == "gd_req"
      :style: table
      :columns: title
      :colwidths: 30

.. gd_req:: Safety Analysis linkage level
   :id: gd_req__saf__linkage_fulfill
   :status: valid
   :tags: attribute, check
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   Every feature- and component Safety Analysis shall be linked to at least one parent feature architecture.


.. gd_req:: Safety Analysis linkage safety
   :id: gd_req__saf__linkage_safety
   :status: valid
   :tags: attribute, check
   :satisfies: wf__analyse_featarch, wf__analyse_comparch
   :complies: std_req__iso26262__analysis_848, std_req__iso26262__analysis_749

   It shall be checked that Safety Analysis (Safety != QM) can only be linked against elements with the same ASIL.

.. needextend:: "process_areas/requirements_engineering" in docname
   :+tags: safety analysis
