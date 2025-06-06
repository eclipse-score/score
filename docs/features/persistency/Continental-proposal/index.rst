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


Persistence Features Proposition
################################

Collected information in context of Continental Automotive Technologies (GSA)

2.1 Partition and Images Management
===================================
- 2.1.0-1 Configuration: persistence flash mapping
- 2.1.0-2 Image management in system
- 2.1.0-3 Image creation offline toolchain
- 2.1.0-4 system boot: definition of the preload support for partition management
- 2.1.0-6 Security for Partition Management


2.2 File system
===============
- 2.2.0-1 Configuration file system
- 2.2.0-2 Generic POSIX compatible file system access
- 2.2.0-3 file system: ext4 - basically used in context of infotainment
- 2.2.0-4 file system: FAT32 - used for external devices like USB or SD-Card
- 2.2.0-5 file system: Read-Only File System access
- 2.2.0-7 file system: COW (Copy-on-write) File system, incl snapshot
- 2.2.0-8 Access Control: Mounting definition availability in system
- 2.2.0-9 Access Control: Application related read / write limitation
- 2.2.0-10 Access Control: Quota Limitation


2.3 Persistence data management
===============================
- 2.3.0-1 Configuration persistence data
- 2.3.0-2 Persistence Container: Hardware Info
- 2.3.0-3 Persistence Container: Early Data
- 2.3.0-4 Persistence Container: Secured Data
- 2.3.0-5 Persistence Container: Emergency Data
- 2.3.0-6 Persistence Container: System Data
- 2.3.0-7 Persistence Key-Value / Embedded Registry access
- 2.3.0-8 Persistence Custom Plugin Access for persistence client library
- 2.3.0-9 Persistence Adaptive AUTOSAR interface
- 2.3.0-10 Persistence Android API
- 2.3.0-11 Persistence client library
- 2.3.0-12 Persistence remote access server (service)
- 2.3.0-13 Persistence proxy service
- 2.3.0-14 Persistence Administration and Service
- 2.3.0-15 Persistence health monitoring

2.4 Flash Device
================
- 2.4.2 Support Embedded Flash
- 2.4.2.0-1 Configuration: embedded flash device
- 2.4.2.0-2 Support embedded flash block device access
- 2.4.2.0-3 Embedded Flash Component (EFC) provides flash maintenance functionality
- 2.4.2.0-5 Maintenance component provides refresh of UFS content

2.4.3 other Devices
===================
- 2.4.3.0-1 Support USB MSD
- 2.4.3.0-7 Flash Device: Support for preprogrammed devices


