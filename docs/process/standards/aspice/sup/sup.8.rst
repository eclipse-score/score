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

SUP.8 Configuration Management
------------------------------

The purpose of the Configuration Management Process is to establish and maintain
the integrity of relevant configuration items and baselines, and
make them available to affected parties.

Process outcomes
~~~~~~~~~~~~~~~~

1. Selection criteria for configuration items are defined and applied.
2. Configuration item properties are defined.
3. Configuration management is established.
4. Modifications are controlled.
5. Baselining is applied.
6. The status of the configuration items is recorded and reported.
7. The completeness and consistency of the baselines is ensured.
8. The availability of backup and recovery mechanisms is verified.

Base practices
~~~~~~~~~~~~~~

.. std_req:: SUP.8.BP1: Identify configuration items
   :id:std_bp__aspice-40__SUP-8-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-18-53,std_bp__aspice-40__iic-01-52

   Define selection criteria for identifying relevant work products to be subject to configuration management.
   Identify and document configuration items according to the defined selection criteria.

   .. note::

      Configuration items are representing work products or group of work products
      which are subject to configuration management as a single entity.

   .. note::

      Configuration items may vary in complexity, size, and type, ranging from an entire system including
      all system, hardware, and software documentation down to a single element or document.

   .. note::

      The selection criteria may be applied to single work products or a group of work products.

.. std_req:: SUP.8.BP2: Define configuration item properties
   :id:std_bp__aspice-40__SUP-8-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-01-52

   Define the necessary properties needed for the modification and control of configuration items.

   .. note::

      The configuration item properties may be defined for single configuration items or a group of items.

   .. note::

      Configuration item properties may include a status model (e.g., Under Work, Tested, Released, etc.), storage location, access rights, etc.

   .. note::

      The application of properties may be implemented by attributes of configuration items.

.. std_req:: SUP.8.BP3: Establish configuration management
   :id:std_bp__aspice-40__SUP-8-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-16-03,std_bp__aspice-40__iic-14-01

   Establish configuration management mechanisms for control of identified configuration items including the configuration item properties,
   including mechanisms for controlling parallel modifications of configuration items.

   .. note::

      This may include specific mechanisms for different configuration item types, such as branch and merge management, or checkout control.

.. std_req:: SUP.8.BP4: Control modifications
   :id:std_bp__aspice-40__SUP-8-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-16-03,std_bp__aspice-40__iic-14-01

   Control modifications using the configuration management mechanisms.

   .. note::

      This may include the application of a defined status model for configuration items.

.. std_req:: SUP.8.BP5: Establish baselines
   :id:std_bp__aspice-40__SUP-8-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-16-03,std_bp__aspice-40__iic-13-08

   Define and establish baselines for internal purposes, and for external product delivery, for all relevant configuration items.

.. std_req:: SUP.8.BP6: Summarize and communicate configuration status
   :id:std_bp__aspice-40__SUP-8-BP6
   :status: valid
   :links:std_bp__aspice-40__iic-14-01,std_bp__aspice-40__iic-15-56

   Record, summarize, and communicate the status of configuration items and established baselines
   to affected parties in order to support the monitoring of progress and status.

   .. note::

      Regular communication of the configuration status, e.g., based on a defined status model supports
      project management, quality activities, and dedicated project phases such as software integration.

.. std_req:: SUP.8.BP7: Ensure completeness and consistency
   :id:std_bp__aspice-40__SUP-8-BP7
   :status: valid
   :links:std_bp__aspice-40__iic-01-52,std_bp__aspice-40__iic-13-08,std_bp__aspice-40__iic-13-51

   Ensure that the information about configuration items is correct and complete including configuration item properties.
   Ensure the completeness and consistency of baselines.

   .. note::

      Completeness and consistency of a baseline means that all required configuration items are included and consistent,
      and have the required status. This can be used to support e.g., project gate approval.

.. std_req:: SUP.8.BP8: Verify backup and recovery mechanisms availability.
   :id:std_bp__aspice-40__SUP-8-BP8
   :status: valid
   :links:std_bp__aspice-40__iic-06-52

   Verify the availability of appropriate backup and recovery mechanisms for the configuration management including
   the controlled configuration items. Initiate measures in case of insufficient backup and recovery mechanisms.

   .. note::

      Backup and recovery mechanisms may be defined and implemented by organizational units outside the project team.
      This may include references to corresponding procedures or regulations.


