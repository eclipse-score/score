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

.. document:: FEO Module Safety Manual
   :id: doc__feo_safety_manual
   :status: draft
   :security: NO
   :safety: ASIL_B
   :realizes: wp__module_safety_manual
   :tags: module_feo


FEO Module Safety Manual
========================

Introduction/Scope
------------------
This is a first *partial draft* version of the FEO (Fixed Order Execution Environment) module safety manual.
For now it only contains Assumptions of Use related to the use of Rust libraries.

Assumed Platform Safety Requirements
------------------------------------
For <S-CORE platform / FEO> the following safety related stakeholder requirements are assumed to define the top level functionality (purpose)>. I.e. from these all the feature and component requirements implemented are derived.
<List here all the stakeholder requirements, with safety not equal to QM, the module's components requirements are derived from.>

Assumptions of Use
------------------

Assumptions on the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| Generally the assumption of the S-CORE platform SEooC is that it is integrated in a safe system, i.e. the POSIX OS it runs on is qualified and also the HW related failures are taken into account by the system integrator, if not otherwise stated in the module's safety concept.


.. aou_req:: on_target_crates
   :id: aou_req__feo__on_target_crates
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: invalid

   Only the following crates of the FEO module shall be used to build code that runs on
   targets in release builds.

   - feo
   - feo-cpp-build
   - feo-cpp-macros
   - feo-time


.. aou_req:: rust_core_lib
   :id: aou_req__feo__rust_core_lib
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   The Rust core lib used to build FEO shall be qualified according to the same ASIL level as the FEO framework.


.. aou_req:: rust_std_lib_modules
   :id: aou_req__feo__rust_std_lib_modules
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: invalid

   The following items from the Rust std library shall be safety qualified:

   - std::collections::HashMap
   - std::collections::HashSet
   - std::fs::File
   - std::fs::OpenOptions
   - std::io::BufWriter
   - std::io::Cursor
   - std::io::Error
   - std::io::Read
   - std::io::Result
   - std::io::Write
   - std::net::TcpStream
   - std::path::Path
   - std::path::PathBuf
   - std::sync::mpsc::bounded
   - std::sync::mpsc::Receiver
   - std::sync::mpsc::RecvTimeoutError
   - std::sync::mpsc::SyncSender
   - std::sync::OnceLock
   - std::thread::JoinHandle
   - std::thread::spawn
   - std::time::Instant
   - std::time::SystemTime
   - std::time::UNIX_EPOCH
   - std::vec::Vec

   **Note:** The above list is not yet complete. It needs to be refined based on a final implementation.
   At the moment, it covers approximately 95% of std library usages.
   An accurate list could be determined by switching feo to #![no_std] and looking at the compilation errors,
   but it gets quickly out of date with a changing codebase.



List of AoUs expected from the environment the platform / module runs on:


.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" in need["tags"]:
                results.append(need)

Assumptions on the User
^^^^^^^^^^^^^^^^^^^^^^^
| As there is no assumption on which specific OS and HW is used, the integration testing of the stakeholder and feature requirements is expected to be performed by the user of the platform SEooC. Tests covering all stakeholder and feature requirements performed on a reference platform (tbd link to reference platform specification), reviewed and passed are included in the platform SEooC safety case.
| Additionally the components of the platform may have additional specific assumptions how they are used. These are part of every module documentation: <link to add>. Assumptions from components to their users can be fulfilled in two ways:
| 1. There are assumption which need to be fulfilled by all SW components, e.g. "every user of an IPC mechanism needs to make sure that he provides correct data (including appropriate ASIL level)" - in this case the AoU is marked as "platform".
| 2. There are assumption which can be fulfilled by a safety mechanism realized by some other S-CORE platform component and are therefore not relevant for an user who uses the whole platform. But those are relevant if you chose to use the module SEooC stand-alone - in this case the AoU is marked as "module". An example would be the "JSON read" which requires "The user shall provide a string as input which is not corrupted due to HW or QM SW errors." - which is covered when using together with safe S-CORE platform persistency feature.

List of AoUs on the user of the platform features or the module of this safety manual:

.. needtable::
   :style: table
   :columns: title;id;status
   :colwidths: 25,25,25
   :sort: title

   results = []

   for need in needs.filter_types(["aou_req"]):
      if need and "environment" not in need["tags"]:
                results.append(need)

Safety concept of the SEooC
---------------------------
| <Describe here the safety concept incl. which faults are taken care of, reactions of the implemented functions under anomalous operating conditions ... if this is not already documented sufficiently in the feature documentation "safety impact" section of all the features the module is used in.>

Safety Anomalies
----------------
| Anomalies (bugs in ASIL SW, detected by testing or by users, which could not be fixed) known before release are documented in the platform/module release notes <add link to release note>.

References
----------
| <link to the user manual>
| <other links>
