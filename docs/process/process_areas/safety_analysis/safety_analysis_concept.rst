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

In this section a concept for the safety analyses will be discussed. Inputs for this concept are the requirements of ISO26262 Part-9.

Inputs
******

#. Stakeholders for the safety analysis?
#. Who needs which information?
#. How to analyze existing safety measure/mechanism?
#. How to add new safety measure/mechanisms?

Stakeholders for the Safety Analysis
====================================

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
* ASPICE
* ISO SAE 21434

How to analyze?
===============

DFA
^^^

A DFA :need:`gd_guidl__safety_analysis` shall be used to proof the absence of dependent failures. For the analysis a checklist
:need:`gd_chklst__dfa` is available.

Safety Analysis
^^^^^^^^^^^^^^^

For the safety analyses the safety analyses :need:`gd_temp__safety_analysis` shall be used. The safety analysis
is done on architectural diagrams (activity and/or sequence diagrams). Therefore fault models shall be used
:need:`gd_guidl__fault_models`.

How to add new safety measure/mechanisms?
=========================================

Identified faults without a mechanism/measure stay open and were monitored in
the issue tracking sytem :need:`wp__issue_track_system` until there are closed.
