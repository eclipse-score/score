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

.. doc_concept:: Concept Description
   :id: doc_concept__tool__process
   :status: valid
   :tags: tool_management

In this section a concept for the Tool Management will be discussed. Inputs for this concepts
are the requirements of ISO2 6262 Part-8, Clause 11, ASPICE PAM 4.0, SUP.8 and
ISO SAE 21434 Clause 5, 5.4.5 additionally including the requirements of the different stakeholders
for the Tool Management process.

Key concept
***********
S-CORE objective is to use OSS Tools only. The selection criteria for OSS Tool therefore must
include the determination of the Tool Confidence Level `(TCL) <https://www.validas.de/publications/automotive2012.pdf>`_
for the tool under consideration.
Based on the resulting TCL additional Tool Qualification activities may required.


Inputs
******

#. Stakeholders for the Tool Management?
#. Which documentations are required?
#. Which activities are required?

Stakeholders for the Tool Management
************************************

#. :need:`Infrastructure, Tooling Community <rl__infrastructure_tooling_community>`

   * Contributes tooling, infrastructure elements to grow and mature the **S-CORE** development environment

#. :need:`Safety Manager<rl__safety_manager>`, :need:`Security Manager <rl__security_manager>`

   * Verifies and approves the the tool verification report

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO 26262
* ASPICE
* ISO SAE 21434

Required documentation
**********************

For each tool the :need:`gd_temp__tool_management__verif_rpt_template` shall be used to document
the relevant information.

Activities for Tool Management
******************************

.. _tlm_creation:

Creation of the Tool Verification Report
========================================

Use the :need:`Tool Verification Report Review Checklist Template <gd_chklst__tool__cr_review>` to
check the completeness of the Tool Verification Report.
