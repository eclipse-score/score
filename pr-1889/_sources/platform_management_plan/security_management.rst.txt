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

.. document:: Platform Security Plan
   :id: doc__platform_security_plan
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: PROCESS_wp__platform_security_plan, PROCESS_wp__tailoring
   :tags: platform_management

Security management / Platform Security Plan
--------------------------------------------

Security Roles & Responsibilities
=================================

- Security Manager - will ensure that security activities are actively
  planned, developed, analyzed, verified and tested and managed
  throughout the life cycle of the project. As all the implementation of
  security functions takes place within module development, there is a
  security manager appointed in the module’s security plan, who defines
  the security process and creates a security management plan.
- Security Engineer - performs the security analysis using methodologies
  such as TARA
- Contributors - developers who follow secure coding guidelines

Continuous secure software development
=======================================

Secure coding guidelines
-------------------------

All developers shall be aware of and shall adhere to the following secure coding guidelines for c++ and rust as applicable:

1.  `SEI CERT C++ Coding
    Standard <https://wiki.sei.cmu.edu/confluence/display/cplusplus>`__
2.  `Guidelines for the use of the C++14 language in critical and
    safety-related
    systems <https://www.autosar.org/fileadmin/standards/R22-11/AP/AUTOSAR_RS_CPP14Guidelines.pdf>`__
3.  `MISRA C++:2023 Guidelines for the use C++:17 in critical
    systems <https://misra.org.uk/product/misra-cpp2023/>`__
4.  `Secure Rust
    guidelines <https://anssi-fr.github.io/rust-guide/01_introduction.html>`__
5.  `The Rustonomicon (Unsafe Code Guidelines &
    Pitfalls) <https://doc.rust-lang.org/nomicon/>`__
6.  `Rust Secure Code Working
    Group <https://github.com/rust-secure-code/wg>`__ 

Automated code scanning
-----------------------
    The following tools should be part of the CI/CD pipeline and should run automatically for every patch, minor and major release:

1.  Static code analysis tools such as coverity for c/c++ and clippy for rust
2.  SCA (software composition analysis) tools - scanning of open source
    libraries for CVEs - such as `RustSec
    Crates <https://github.com/rustsec/rustsec>`__ or Blackduck
3.  Fuzz testing (semi automated) - someone has to create special
    harnesses for the fuzz testing - can be done by tools such as
    `Google oss fuzz <https://github.com/google/oss-fuzz>`__
4. Regular checking of clean code by functional test coverage and
    checking for cyclic dependencies etc.

Security Analysis or TARA (threat analysis risk assessment)
===========================================================

- Security analysis shall be performed on the features and how
  modules/components interact with one another to implement a feature
- Analysis results shall be documented and shall serve as security
  requirements for the features.

Security code reviews 
=====================
  Contributors should perform regular security code reviews. Assign a few developers
  as security champions who should receive security trainings to perform
  such code reviews. 
  
Security Work Packages 
========================

+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Deliverable                               | Description                                                                                | Responsible Person                            |
+===========================================+============================================================================================+===============================================+
| Item definition                           | defining boundaries, assets etc                                                            | Security Manager/Engineer                     |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Data flow diagrams                        | document the interaction and data flow between the components in a system                  | Contributors                                  |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| TARA                                      | enumerate threats, analyze attack feasibility and impact, decide treatment                 | Security Engineer                             |
|                                           | (mitigate/transfer/accept/avoid).                                                          |                                               |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Cybersecurity goals                       | Security goals should be defined for the whole S-CORE middleware. These goals will serve   | Security Manager                              |
|                                           | as the input for the security analysis.                                                    |                                               |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Horizontal Security Requirements          | applicable to all modules/components                                                       | Security Manager                              |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Security concepts resulting from the      | Security concepts should document different options and a favorable option should be       | Contributors and Security Manager/engineer    |
| goals and TARA                            | implemented                                                                                |                                               |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Hardening guide for Integrators           | Some identified risks are mitigated by hardening the platform. Such mitigations shall be   | Contributors and Security Manager             |
|                                           | part of this guide                                                                         |                                               |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| Security sign off process before releases | A checklist should be created and signed to ensure that all documented risks are mitigated | Contributors and Security Manager             |
+-------------------------------------------+--------------------------------------------------------------------------------------------+-----------------------------------------------+


Vulnerability Management
========================

- SBOMs needs to be defined and used in CVE scanning (SBOM driven CVE
  scanning). This process should be automated to run in the CI/CD
  pipeline.
- When a vulnerability is reported or identified, the following tasks
  shall be performed by the following responsible persons:

+-----------------------+-----------------------+-----------------------+
| Task                  | Description           | Responsible Person    |
+=======================+=======================+=======================+
| Vulnerability         | Validating whether    | Contributors          |
| Validation and        | the reported issue is |                       |
| classification        | a security            |                       |
|                       | vulnerability and     |                       |
|                       | mapping it a known    |                       |
|                       | CWE (common weakness  |                       |
|                       | enumeration)          |                       |
+-----------------------+-----------------------+-----------------------+
| CVSS score            | Calculating CVSS      | Security              |
| calculation           | score to understand   | Engineer/Manager and  |
|                       | the criticality of    | contributors          |
|                       | the reported          |                       |
|                       | vulnerability         |                       |
+-----------------------+-----------------------+-----------------------+
| Prioritization        | Decision on when to   | Security Manager and  |
|                       | issue a patch         | contributors          |
+-----------------------+-----------------------+-----------------------+
| Responsible           | Decide whether this   | Security Manager      |
| disclosure            | should be disclosed   |                       |
|                       | or not. Request a CVE |                       |
|                       | Id if needed to be    |                       |
|                       | disclosed.            |                       |
+-----------------------+-----------------------+-----------------------+

Links to the tools
==================

TARA tools :

- https://github.com/devmatic-it/taralizer
- https://github.com/cjneely10/TARA-Analysis

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. needtable::
   :style: table
   :columns: title;id;status;realizes
   :colwidths: 25,25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["document"]):
      if need and "platform_management" in need["tags"]:
                results.append(need)
