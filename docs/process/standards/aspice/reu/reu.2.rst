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

REU.2 Management of Products for Reuse
--------------------------------------

The purpose is to ensure that reused work products are analyzed, verified,
and approved for their target context.

Process outcomes
~~~~~~~~~~~~~~~~

1. Products for reuse are selected using defined criteria.
2. Products for reuse are analyzed for portability and interoperability.
3. Limitations for reuse are defined and communicated.
4. Products for reuse are verified.
5. Products for reuse are provided to affected parties.
6. Communication mechanism is established with the reuse product provider..

Base practices
~~~~~~~~~~~~~~

.. std_req:: REU.2.BP1: Select products for reuse
   :id:std_bp__aspice-40__REU-2-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-12-03

   Select the products to be reused using defined criteria.

   .. note::

      Products for reuse may be systems, hardware or software components, third party components or legacy components.

.. std_req:: REU.2.BP2: Analyze the reuse capability of the product
   :id:std_bp__aspice-40__REU-2-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-04-02,std_bp__aspice-40__iic-15-07

   Analyze the designated target architecture and the product to be reused to determine its
   applicability in the target architecture according to relevant criteria.

   .. note::

      Examples for criteria can be requirements compliance, verifiability of the product to be reused in the target architecture, or portability/interoperability.

.. std_req:: REU.2.BP3: Define limitations for reuse
   :id:std_bp__aspice-40__REU-2-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-04-02,std_bp__aspice-40__iic-15-07

   Define and communicate limitations for the products to be reused.

   .. note::

      Limitations may address parameters of operational environment.

.. std_req:: REU.2.BP4: Ensure qualification of products for reuse
   :id:std_bp__aspice-40__REU-2-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-13-53

   Provide evidence that the product for reuse is qualified for the intended use of the deliverable.

   .. note::

      Qualification may be demonstrated by verification evidence.

   .. note::

      Verification may include the appropriateness of documentation.

.. std_req:: REU.2.BP5: Provide products for reuse
   :id:std_bp__aspice-40__REU-2-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-12-03

   Make available the product to be reused to affected parties.

   .. note::

      Refer to HWE.3, SWE.5 or SYS.4 for more information on integration of hardware, software, or system components.

.. std_req:: REU.2.BP6: Communicate information about effectiveness of reuse activities
   :id:std_bp__aspice-40__REU-2-BP6
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Establish communication and notification mechanism about experiences and technical outcomes to the provider of reused products.

   .. note::

      The communication with the provider of a reused product may depend on whether the product is under development or not.




