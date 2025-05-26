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

Concept Description
###################

.. doc_concept:: Safety Analysis Concept
   :id: doc_concept__safety__analysis
   :status: valid
   :tags: safety_analysis

In this section a concept for the safety analyses will be discussed. Inputs for this concept are the requirements of ISO26262 Part 6 Chapter 7 and Part 9 Chapter 7 and 8.

Inputs
******

#. Stakeholders for the safety analysis?
#. Who needs which information?
#. How to analyze existing safety mitigation?
#. How to add new safety mitigations?

Stakeholders for the Safety Analysis
====================================

#. :need:`Contributor <rl__contributor>`

   * Contributes features and components to grow the **S-CORE** content

#. :need:`Committer <rl__committer>`

   * Analyse the feature architecture by performing the safety analyses and DFA
   * Analyse the component architecture by performing the safety analyses and DFA
   * Monitor/veryfiy the Safety Analysis and DFA

#. :need:`Technical Lead <rl__technical_lead>`

   * Support the feature safety analyses and DFA
   * Support the monitoring and veryfing of the feature safety analyses and DFA

#. :need:`Module Lead <rl__module_lead>`

   * Support the component safety analyses and DFA
   * Support the monitoring and veryfing of the component safety analyses and DFA

#. :need:`Safety Manager <rl__safety_manager>`

   * Approve the safety analysis and DFA
   * Approve the verification of the safety analysis and DFA

#. :need:`Security Manager <rl__security_manager>`

   * Support the safety analyses and DFA
   * Support the monitoring and veryfing of the safety analyses and DFA


Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO26262
* ISO SAE 21434

How to analyze?
===============

DFA
^^^

A DFA :need:`gd_guidl__safety_analysis` shall be used to proof the absence of dependent failures. For the analysis a list
of DFA failure initiators :need:`gd_guidl__dfa_failure_initiators` is available.

Safety Analysis
^^^^^^^^^^^^^^^

For the safety analyses the templates :ref:`safety_analysis_templates` shall be used. For the safety analysis we selected
the method FMEA on feature and component level. The safety analysis is done on architectural diagrams (state and sequence diagrams).
For the safety analysis fault models shall be used :need:`gd_guidl__fault_models`.

How to add new safety mitigations?
=========================================

Identified faults without a mitigation stay open and are monitored in the issue tracking sytem :need:`wp__issue_track_system` until they are resolved.
