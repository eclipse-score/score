..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

Assumptions of Use
##################

.. document:: Operating System Assumptions of Use
   :id: doc__os_aou
   :status: draft
   :safety: ASIL_B
   :security: NO
   :realizes: wp__requirements_comp

.. aou_req:: No Root Privileges
   :id: aou_req__os__nonroot
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   No process running on the SW-platform shall request root privileges.

   Note: The root privilege is dangerous for security and safety as it destroys process isolation.

.. aou_req:: Safe OS Function Use
   :id: aou_req__os__safe_fctn_use
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   If an application or SW-platform component is safety relevant and uses OS functions, it shall only use the safe functions.

   Note: For checking the "to be expected" safe functions the developer can consider the safe function list
   published by the OS supplier. For QNX this can be found for example in `appendices here <https://fs-products.tuvasi.com/certificates?keywords=Blackberry&productcategory_id=1#prodid_9842>`_ (for one version).

.. aou_req:: OS Public API Use
   :id: aou_req__os__public_api
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   All components shall only use the public API of the OS components.

.. aou_req:: C++ Library Preference
   :id: aou_req__os__cxx_preference
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   All components should prefer the use of C++ standard lib over the C lib to call a functionality.
   If C lib must be used, it shall not be mixed with C++ lib for the same functionality.

.. aou_req:: Minimal Process Privileges
   :id: aou_req__os__minimal_privileges
   :reqtype: Functional
   :security: YES
   :safety: ASIL_B
   :status: valid

   All components shall only use the privileges that are indispensable for their function.

   Note1: OS safety manuals provide lists of allowed and not allowed privileges.

   Note2: One example is the "channel connect" - only IPC connections are allowed which are specified in the architecture.

   Note3: Another example is mmap_peer which would allow accessing other processes memory if wrongly used.

.. needextend:: "__os_" in id
   :+tags: operating_system
