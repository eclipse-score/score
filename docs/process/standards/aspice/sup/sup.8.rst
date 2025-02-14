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

.. req:: SUP.8.BP1: Identify configuration items
   :id: R_ASPICE-40_SUP-8-BP1
   :status: valid
   :links: R_ASPICE-40_IIC-18-53, R_ASPICE-40_IIC-01-52

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

.. req:: SUP.8.BP2: Define configuration item properties
   :id: R_ASPICE-40_SUP-8-BP2
   :status: valid
   :links: R_ASPICE-40_IIC-01-52

   Define the necessary properties needed for the modification and control of configuration items.

   .. note::

      The configuration item properties may be defined for single configuration items or a group of items.

   .. note::

      Configuration item properties may include a status model (e.g., Under Work, Tested, Released, etc.), storage location, access rights, etc.

   .. note::

      The application of properties may be implemented by attributes of configuration items.

.. req:: SUP.8.BP3: Establish configuration management
   :id: R_ASPICE-40_SUP-8-BP3
   :status: valid
   :links: R_ASPICE-40_IIC-16-03, R_ASPICE-40_IIC-14-01

   Establish configuration management mechanisms for control of identified configuration items including the configuration item properties,
   including mechanisms for controlling parallel modifications of configuration items.

   .. note::

      This may include specific mechanisms for different configuration item types, such as branch and merge management, or checkout control.

.. req:: SUP.8.BP4: Control modifications
   :id: R_ASPICE-40_SUP-8-BP4
   :status: valid
   :links: R_ASPICE-40_IIC-16-03, R_ASPICE-40_IIC-14-01

   Control modifications using the configuration management mechanisms.

   .. note::

      This may include the application of a defined status model for configuration items.

.. req:: SUP.8.BP5: Establish baselines
   :id: R_ASPICE-40_SUP-8-BP5
   :status: valid
   :links: R_ASPICE-40_IIC-16-03, R_ASPICE-40_IIC-13-08

   Define and establish baselines for internal purposes, and for external product delivery, for all relevant configuration items.

.. req:: SUP.8.BP6: Summarize and communicate configuration status
   :id: R_ASPICE-40_SUP-8-BP6
   :status: valid
   :links: R_ASPICE-40_IIC-14-01, R_ASPICE-40_IIC-15-56

   Record, summarize, and communicate the status of configuration items and established baselines
   to affected parties in order to support the monitoring of progress and status.

   .. note::

      Regular communication of the configuration status, e.g., based on a defined status model supports
      project management, quality activities, and dedicated project phases such as software integration.

.. req:: SUP.8.BP7: Ensure completeness and consistency
   :id: R_ASPICE-40_SUP-8-BP7
   :status: valid
   :links: R_ASPICE-40_IIC-01-52, R_ASPICE-40_IIC-13-08, R_ASPICE-40_IIC-13-51

   Ensure that the information about configuration items is correct and complete including configuration item properties.
   Ensure the completeness and consistency of baselines.

   .. note::

      Completeness and consistency of a baseline means that all required configuration items are included and consistent,
      and have the required status. This can be used to support e.g., project gate approval.

.. req:: SUP.8.BP8: Verify backup and recovery mechanisms availability.
   :id: R_ASPICE-40_SUP-8-BP8
   :status: valid
   :links: R_ASPICE-40_IIC-06-52

   Verify the availability of appropriate backup and recovery mechanisms for the configuration management including
   the controlled configuration items. Initiate measures in case of insufficient backup and recovery mechanisms.

   .. note::

      Backup and recovery mechanisms may be defined and implemented by organizational units outside the project team.
      This may include references to corresponding procedures or regulations.


