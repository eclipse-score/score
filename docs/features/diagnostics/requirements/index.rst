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

.. _diagnostics_requirements:

Requirements
############

Diagnostic and Fault Management
===============================

.. feat_req:: SOVD Standard
   :id: feat_req__diagnostics__sovd_std
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd
   :status: valid
   :valid_from: v1.0.0

   The SOVD implementation shall conform to the SOVD standard as defined in ISO/DIS 17978 (or the latest available draft or final publication).

.. feat_req:: SOVD Server
   :id: feat_req__diagnostics__sovd_server
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd, stkh_req__diagnostics__secure_access
   :status: valid
   :valid_from: v1.0.0

   The diagnostic system shall include a central SOVD server that exposes diagnostic functionality via a standard REST interface.

.. feat_req:: SOVD Configuration
   :id: feat_req__diagnostics__sovd_config
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd
   :status: valid
   :valid_from: v1.5.0

   The system shall provide configuration management for SOVD components, including protocol parameters and security settings.

.. feat_req:: SOVD Server Configuration Integration
   :id: feat_req__diagnostics__sovd_config_mgr
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd
   :status: valid
   :valid_from: v1.5.0

   The SOVD server shall integrate with the S-CORE Configuration Manager to support runtime access and modification of configuration data.

.. feat_req:: SOVD Server Authentication Integration
   :id: feat_req__diagnostics__sovd_auth_mgr
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__secure_access
   :status: valid
   :valid_from: v1.5.0

   The SOVD server shall enforce access control and validate client credentials.

.. feat_req:: SOVD Gateway
   :id: feat_req__diagnostics__sovd_gateway
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__distributed_support
   :status: valid
   :valid_from: v1.0.0

   The system shall include a SOVD gateway to route diagnostic requests between different network domains and protocols.

.. feat_req:: SOVD Client
   :id: feat_req__diagnostics__sovd_client
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd, stkh_req__diagnostics__secure_access
   :status: valid
   :valid_from: v1.0.0

   The system shall provide a SOVD client to allow external applications to communicate with the SOVD server.

.. feat_req:: SOVD Client Deployment Core
   :id: feat_req__diagnostics__sovd_client_core
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd
   :status: valid
   :valid_from: v1.0.0

   The SOVD client shall be designed as a reusable core component that can be deployed in off-board, on-board, or cloud environments.

.. feat_req:: Diagnostic Service Application
   :id: feat_req__diagnostics__service_app
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__custom_services
   :status: valid
   :valid_from: v1.0.0

   The diagnostic system shall include a base service application (AKA routine) that is triggered by the SOVD Server and used to derive custom service applications.

.. feat_req:: OEM Diagnostic Plug In
   :id: feat_req__diagnostics__oem_plugin
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__custom_services
   :status: valid
   :valid_from: v1.5.0

   The diagnostic system shall provide a plug-in mechanism to include OEM-specific features.

.. feat_req:: Diagnostic Fault Library
   :id: feat_req__diagnostics__fault_lib
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting
   :status: valid
   :valid_from: v1.0.0

   The system shall include a fault reporting library that provides an interface for applications and platform components to report diagnostic faults including metadata.

.. feat_req:: Fault Library Catalog
   :id: feat_req__diagnostics__fault_lib_catalog
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting
   :status: valid
   :valid_from: v1.0.0

   The fault library shall provide the ability to define faults via a component fault catalog for the scope of the respective parent component.

.. feat_req:: Fault Library Debouncing
   :id: feat_req__diagnostics__fault_lib_debounce
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting
   :status: valid
   :valid_from: v1.5.0

   The fault library shall support configurable error debouncing.

.. feat_req:: Diagnostic Fault Manager
   :id: feat_req__diagnostics__fault_manager
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting, stkh_req__diagnostics__dtc_read_sovd
   :status: valid
   :valid_from: v1.0.0

   The system shall include a central diagnostic fault manager that aggregates data from fault libraries, provides DTC status to the SOVD server, and interfaces with a persistent diagnostic database.

.. feat_req:: Fault Catalog Aggregation
   :id: feat_req__diagnostics__fault_catalog_agg
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting
   :status: valid
   :valid_from: v1.0.0

   The Diagnostic Fault Manager shall be configureable via the aggregated fault catalog derived from all fault libraries in the system.

.. feat_req:: Diagnostic Database
   :id: feat_req__diagnostics__db
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting, stkh_req__diagnostics__dtc_read_sovd
   :status: valid
   :valid_from: v1.0.0

   The system shall include a diagnostic database to store DTCs, occurrence counts, and associated metadata for fault events.

.. feat_req:: Diagnostic Database Persistence
   :id: feat_req__diagnostics__db_persistence
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__fault_reporting
   :status: valid
   :valid_from: v1.0.0

   The diagnostic database shall store all diagnostic data persistently.

.. feat_req:: Classic Diagnostic Adapter
   :id: feat_req__diagnostics__classic_adapter
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__uds_ecus
   :status: valid
   :valid_from: v1.0.0

   The system shall include a classic diagnostic adapter to translate SOVD requests into UDS commands.

.. feat_req:: Classic Diagnostic Adapter ODX Configuration
   :id: feat_req__diagnostics__classic_adapter_odx
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__uds_ecus
   :status: valid
   :valid_from: v1.0.0

   The classic diagnostic adapter shall support configuration via ODX files that describe the UDS command mappings and behavior per ECU.

.. feat_req:: UDS to SOVD Proxy
   :id: feat_req__diagnostics__uds2sovd_proxy
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__uds_tester_compat
   :status: valid
   :valid_from: v1.5.0

   The system shall include a proxy to translate UDS diagnostic requests to SOVD protocol requests.

.. feat_req:: UDS2SOVD Proxy ODX Configuration
   :id: feat_req__diagnostics__uds2sovd_odx
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__uds_tester_compat
   :status: valid
   :valid_from: v1.5.0

   The UDS2SOVD proxy shall support configuration via standardized ODX files to define which SOVD services are exposed via the UDS interface.

.. feat_req:: Diagnostic system internal communication
   :id: feat_req__diagnostics__internal_com
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__diagnostics__via_sovd, stkh_req__diagnostics__dtc_read_sovd
   :status: valid
   :valid_from: v1.0.0

   All internal communication between diagnostic components that do not use UDS or SOVD protocols shall be implemented using the S-CORE::COM middleware.
