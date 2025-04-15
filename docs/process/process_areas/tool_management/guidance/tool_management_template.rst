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

.. _tlm_templates:

Tool Verification Report Template
=================================

.. gd_temp:: Tool Verification Report Template
   :id: gd_temp__tool_management__verif_rpt_template
   :status: valid
   :complies: std_req__iso26262__support_1141, std_req__iso26262__support_1142, std_req__iso26262__support_1143, std_req__iso26262__support_11441, std_req__iso26262__support_11442, std_req__iso26262__support_11451, std_req__iso26262__support_11452, std_req__iso26262__support_11453, std_req__iso26262__support_11454, std_req__iso26262__support_11461, std_req__iso26262__support_11462, std_req__isosae21434__org_management_5451, std_req__aspice_40__SUP-8-BP1, std_req__aspice_40__SUP-8-BP2


[Your Tool Name]
----------------

.. note:: Document header

.. document:: [Your Tool Name]
   :id: doc__tool__tool_name
   :status: draft
   :safety: ASIL_B
   :tags: tool_management

.. attention::
    The above directive must be updated according to your tool.

Identification
--------------
[Identify the tool]

E.g. by unique name or UID?

Add the tool version

Add tool verification status (draft, evaluated, qualified) defined?


Introduction
------------
[Describe the scope and purpose of the tool]

May also add some general information about the tool

May add some comments to get started

May add links to the public available information, if applicable.


Use cases
---------
[Describe the use case for the tool in the project]

Add the purposes of the tool (e.g. use cases, scenarios, etc.)

What are the inputs for the tool?

What are the output for the tool?

Add tool usage constraints/limitations


Installation
------------
[Describe here how to install the tool]

How is the tool is configured in order to be used in safe/secure way?

Describe environment and its constraints/limitations

(Constraints/Limitation must cover functional, safety, security)

E.g. version >= x.yz, access/usage protection required?, execution authority required?

May add links to the public available information, if applicable.


Integration
-----------
[Describe here how to integrate the tool in existing toolchain]

How works the tool together ?

Where is the tool located?

How are bugs of the tool tracked?

May add links to the public available information, if applicable.

Add malfunctions which the tool could introduce.

Add threats which the tool could introduce, e.g. unintended, non-authorized use.


Documentation
-------------
[Describe here detailed information about the tool documentation]

Where are the tool documents like User Manual, Guidelines, Erratas, etc. located?

May add links to the public available information, if applicable.


Evaluation
----------
[Describe here detailed information about the tool evaluation]

Determine the tool impact based on the malfunctions/threats

Define safety measures/security controls against the tool malfunctions/threats

Determine the  tool error detection based on confidence on the defined safety measures/security controls

Determine the tool confidence level based on tool impact and tool error detection defined?

Determine if  tool qualification is required


**Optional Section for Tool Qualification**
-------------------------------------------
based on method: validation of the software tool


Requirements and testing aspects
--------------------------------
[Describe here requirements and their tests from user point of view]

Where are tool requirements defined?

Where are the test cases for the requirements defined?

Where are the requirements coverage documented?


Usage and analysis perspective
------------------------------
[Describe here usage and analysis perspective]

Where is the architectural design of the tool defined?

Where is the tool input and output described?

Where are the use cases of the tool defined?

Where are workflows for the tool defined?

Where is the safety analysis for the tool defined?

Where is the security analysis for the tool defined?
