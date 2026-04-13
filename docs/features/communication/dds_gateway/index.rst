..
   # *******************************************************************************
   # Copyright (c) 2024 Contributors to the Eclipse Foundation
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

DDS Gateway
===========

Overview
--------

The DDS Gateway introduces a communication bridge within the S-CORE communication stack.
It enables controlled and configurable data exchange between ``mw::com (LoLa)`` (intra-ECU communication via IPC binding) and DDS-based systems (inter-ECU
communication), allowing integration with distributed DDS environments without requiring changes to existing application implementations.

Scope
-----

The DDS Gateway provides:

- Bridging between ``mw::com (LoLa)`` and DDS via the gateway:

  - ``mw::com (LoLa)`` → DDS (publishing local data to DDS domains)
  - DDS → ``mw::com (LoLa)`` (delivering DDS data to local communication)
  - ``mw::com (LoLa)`` → DDS → ``mw::com (LoLa)`` (inter-ECU communication via DDS)

- Configurable routing:

  - Mapping between ``mw::com`` events(TBD for fields and methods) and DDS topics
  - Support for DDS domain-based routing

- Dynamic Type handling:

  - Runtime type definition via configuration
  - No dependency on DDS IDL generation
  - Enables data translation and consistent serialization across middleware boundaries

- End-to-End (E2E) protection:

  - Centralized handling of Counter, CRC, and DataID
  - Validation and protection configurable per route

- DDS stack abstraction:

  - Pluggable DDS implementations via defined interfaces

Motivation
----------

S-CORE currently focuses on local communication via ``mw::com (LoLa)`` but does
not provide a standardized mechanism to integrate DDS-based communication systems.

In mixed middleware environments:

- Integration with DDS requires custom adapters
- Applications may need to embed DDS logic, reducing abstraction
- Communication with native DDS applications is not standardized
- Multi-domain DDS setups are difficult to manage consistently
- E2E protection across middleware boundaries is duplicated

The DDS Gateway addresses these challenges by introducing a centralized,
configurable component responsible for bridging and routing communication
across middleware boundaries.

Key Value
---------

- Standardized integration with DDS systems
- Direct interoperability with native DDS applications via the gateway
- Clean separation between ``mw::com (LoLa)`` and DDS
- Reduced integration effort
- Support for distributed and multi-domain systems

- Interoperability across heterogeneous systems:

  - Enables communication between systems with different architectures
    (e.g., 32-bit / 64-bit, different endianness)
  - Ensures consistent data representation via Dynamic Type handling

- Centralized handling of safety (E2E) and type management

Reference
---------

The detailed Feature Request, including full design description, configuration
model, and implementation considerations, is available here:

- DDS Gateway Feature Request:https://github.com/eclipse-score/score/issues/2726
