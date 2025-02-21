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

ASPICE 4.0
==========

This incorporates the detailed description of the `Automotive SPICE PAM
v4.0 <https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf>`__
to support the performance of process assessments, so that the process
assessment model can be used for its intended purpose.

`Automotive SPICE PAM
v4.0 <https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf>`__
provides following copyright release statement:

You may not alter, transform, or build upon this work without the prior consent of the VDA Quality Management Center. Such consent may be given provided ISO copyright is not infringed.

The detailed descriptions contained in this document may be incorporated as part of any tool or other material to support the performance of process assessments, so that this process assessment model can be used for its intended purpose, provided that any such material is not offered for sale.

All distribution of derivative works shall be made at no cost to the recipient.

Copyright notice
----------------
There is no alteration, transformation or building upon in the *SCORE* project. Detailed descriptions are included to facilitate process assessment in the *SCORE* project and are provided in an open source framework free of charge.


Tailoring
---------

| Standard's requirements in this document are already tailored to the SW platform project:
|
| - Generally, requirements (base (BP) and generic practices (GP)) and work product (information item characteristics (IIC)) links are only included if those are relevant (i.e., not tailored out).
|
| - Included are only the following process groups and the listed processes:
|   - SWE: Software Engineering Process Group (SWE.1-SWE.6)
|   - MAN: Management Process Group (MAN.3, MAN.5)
|   - SUP: Supporting Process Group (SUP.1, SUP.8-SUP.10)
|   - SPL: Supply Process Group (SPL.2)
|   - REU: Reuse Process Group (REU.2)
|   - PIM: Process Improvement Process Group (PIM.3)
|
| - Excluded are also the following process groups or processes from the mentioned process groups above:
|   - SYS: System Engineering Process Group (pure SW development project)
|   - HWE: Hardware Engineering Process Group (pure SW development project)
|   - MLE: Machine Learning Engineering Process Group (not applicable for now)
|   - SUP: SUP.11 - Machine Learning Data Management (not applicable for now)
|   - MAN: MAN.6 - Measurements (not applicable for now)
|   - VAL: Validation process group (pure SW with no (automobile) user interaction)
|   - ACQ: Acquisition process group (because there is no contracted supplier of the project)


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   man/index
   swe/index
   sup/index
   spl/index
   reu/index
   pim/index
   iic/index


PA 2.1 Process performance management process attribute
-------------------------------------------------------

The performance management process attribute is a measure of the extent
to which the performance of the process is managed.

Process attribute achievements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Strategy for the performance of the process is defined based on identified objectives.
2. Performance of the process is planned.
3. Performance of the process is monitored and adjusted to meet the planning.
4. Needs for human resources including responsibilities and authorities for performing the process are determined.
5. Needs for physical and material resources are determined.
6. Persons performing the process are prepared for executing their responsibilities.
7. Physical and material resources for performing the process are identified, made available, allocated and used.
8. Interfaces between the involved parties are managed to ensure both effective communication and the assignment of responsibilities.


Generic practices
~~~~~~~~~~~~~~~~~

.. std_req:: GP2.1.1: Identify the objectives and define a strategy for the performance of the process.
   :id:std_bp__aspice-40__gp-211
   :status: valid
   :links:std_bp__aspice-40__iic-19-01

   The scope of the process activities including the management of process performance and the management of work products are determined.
   Corresponding results to be achieved are determined.
   Process performance objectives and associated criteria are identified.

   .. note::

      Budget targets and delivery dates to the customer,
      targets for test coverage and process lead time are examples for process performance objectives.

   .. note::

      Performance objectives are the basis for planning and monitoring.

   Assumptions and constraints are considered when identifying the performance objectives.
   Approach and methodology for the process performance is determined.

   .. note::

      A process performance strategy may not necessarily be document-ed specifically for each process.
      Elements applicable for multiple processes may be documented jointly,
      e.g, as part of a common project handbook or in a joint test strategy.

.. std_req:: GP2.1.2: Plan the performance of the process.
   :id:std_bp__aspice-40__gp-212
   :status: valid
   :links:std_bp__aspice-40__iic-08-56,std_bp__aspice-40__iic-14-10

   The planning for the performance of the process is established according to the defined objectives, criteria, and strategy.
   Process activities and work packages are defined.
   Estimates for work packages are identified using appropriate methods.

   .. note::

      Schedule and milestones are defined.

.. std_req:: GP2.1.3: Determine resource needs.
   :id:std_bp__aspice-40__gp-213
   :status: valid
   :links:std_bp__aspice-40__iic-17-55

   The required amount of human resources, and experience, knowledge and skill needs for the for process performance are determined based on the planning.
   The needs for physical and material resources are determined based on the planning.

   .. note::

      Physical and material resources may include equipment, laboratories, materials, tools, licenses etc.

   Required responsibilities and authorities to perform the process, and to manage the corresponding work products are determined.

   .. note::

      The definition of responsibilities and authorities does not necessarily require formal role descriptions.

.. std_req:: GP2.1.4: Identify and make available resources.
   :id:std_bp__aspice-40__gp-214
   :status: valid
   :links:std_bp__aspice-40__iic-08-61

   The individuals performing and managing the process are identified and allocated according to the determined needs.
   The individuals performing and managing the process are being qualified to execute their responsibilities.

   .. note::

      Qualification of individuals may include training, mentoring, or coaching.

   The other resources, necessary for performing the process are identified, made available, allocated and used according to the determined needs.

.. std_req:: GP2.1.5: Monitor and adjust the performance of the process.
   :id:std_bp__aspice-40__gp-215
   :status: valid
   :links:std_bp__aspice-40__iic-08-56,std_bp__aspice-40__iic-13-14

   Process performance is monitored to identify deviations from the planning.
   Appropriate actions in case of deviations from the planning are taken.
   The planning is adjusted as necessary.

.. std_req:: GP2.1.6: Manage the interfaces between involved parties.
   :id:std_bp__aspice-40__gp-216
   :status: valid
   :links:std_bp__aspice-40__iic-08-62,std_bp__aspice-40__iic-13-52

   The individuals and groups including required external parties involved in the process performance are determined.
   Responsibilities are assigned to the relevant individuals or parties.
   Communication mechanisms between the involved parties are determined.
   Effective communication between the involved parties is established and maintained.


PA 2.2 Work product management process attribute
------------------------------------------------

The work product management process attribute is a measure of the extent
to which the work products produced by the process are appropriately managed.

Process attribute achievements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Requirements for the work products of the process are defined.
2. Requirements for storage and control of the work products are defined.
3. The work products are appropriately identified, stored, and controlled.
4. The work products are reviewed and adjusted as necessary to meet requirements.


Generic practices
~~~~~~~~~~~~~~~~~

.. std_req:: GP2.2.1: Define the requirements for the work products.
   :id:std_bp__aspice-40__gp-221
   :status: valid
   :links:std_bp__aspice-40__iic-17-05,std_bp__aspice-40__iic-18-07,std_bp__aspice-40__iic-18-59

   The requirements for the content and structure of the work products to be produced are defined.
   Quality criteria for the work products are identified.
   Appropriate review and approval criteria for the work products are defined.

   .. note::

      Possible sources of documentation requirements may be e.g.,
      best practices or lessons learned from other projects, standards,
      organization requirements, customer requirements, etc.

   .. note::

      There may be types of work products for which no review or approval
      is required, thus then there would be no need to define the corresponding criteria.

.. std_req:: GP2.2.2: Define the requirements for storage and control of the work products.
   :id:std_bp__aspice-40__gp-222
   :status: valid
   :links:std_bp__aspice-40__iic-17-05

   Requirements for the storage and control of the work products are defined, including their identification and distribution.

   .. note::

      Possible sources for the identification of requirements for storage and control may be e.g., legal requirements, data policies, best practices from other projects, tool related requirements, etc.

   .. note::

      Examples for work product storage are files in a file system, ticket in a tool, Wiki entry, paper documents etc.

   .. note::

      Where status of a work product is required in base practices, this should be managed via a defined status model.

.. std_req:: GP2.2.3: Identify, store and control the work products.
   :id:std_bp__aspice-40__gp-223
   :status: valid
   :links:std_bp__aspice-40__iic-13-08,std_bp__aspice-40__iic-16-00

   The work products to be controlled are identified.
   The work products are stored and controlled in accordance with the requirements.
   Change control is established for work products.
   Versioning and baselining of the work products is performed in accordance with the requirements for storage and control of the work products.
   The work products including the revision status are made available through appropriate mechanisms.

.. std_req:: GP2.2.4: Review and adjust work products.
   :id:std_bp__aspice-40__gp-224
   :status: valid
   :links:std_bp__aspice-40__iic-13-19

   The work products are reviewed against the defined requirements and criteria.
   Resolution of issues arising from work products reviews is ensured.


PA 3.1 Process definition process attribute
-------------------------------------------

The process definition process attribute is a measure of the extent to
which a standard process is maintained to support the deployment of the defined process.

Process attribute achievements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. A standard process is developed, established, and maintained that describes the fundamental elements that must be incorporated into a defined process.
2. The required inputs and the expected outputs for the standard process are defined.
3. Roles, responsibilities, authorities, and required competencies for performing the standard process are defined.
4. Tailoring guidelines for deriving the defined process from the standard process are defined.
5. Required physical and material resources and process infrastructure needs are determined as part of the standard process.
6. Suitable methods and required activities for monitoring the effectiveness, suitability and adequacy of the process are determined.


Generic practices
~~~~~~~~~~~~~~~~~

.. std_req:: GP3.1.1: Establish and maintain the standard process.
   :id: R_ASPICE-40_GP-311
   :status: valid
   :links:std_bp__aspice-40__iic-06-51,std_bp__aspice-40__iic-10-00,std_bp__aspice-40__iic-10-50,std_bp__aspice-40__iic-10-51

   A suitable standard process is developed including required activities and their interactions.
   Inputs and outputs of the standard process are defined including the corresponding entry and
   exit criteria to determine the interactions and sequence with other processes.
   Process performance roles are identified and assigned to the standard process activities including
   their type of involvement, responsibilities, and authorities.

   .. note::

      An example for describing the involvement of the process roles in the activities is a RASI/RASIC representation.
      Suitable guidance, procedures, and templates are provided to support the execution of the process as needed.

   .. note::

      Procedures may also include description of specific methods to be used.
      Appropriate tailoring guidelines including predefined unambiguous criteria as well as predefined and
      unambiguous proceedings are defined based on identified deployment needs and context of the standard process.
      The standard process is maintained according to corresponding feedback from the monitoring of the deployed processes.

   .. note::

      For guidance on how to perform process improvements see the Process Improvement process (PIM.3).

.. std_req:: GP3.1.2: Determine the required competencies.
   :id: R_ASPICE-40_GP-312
   :status: valid
   :links:std_bp__aspice-40__iic-10-50,std_bp__aspice-40__iic-10-51

   Required competencies, skills, and experience for performing the standard process are determined for the identified roles.
   Appropriate qualification methods to acquire the necessary competencies and skills are determined, maintained, and made available for the identified roles.

   .. note::

      Qualification methods are e.g., trainings, mentoring, self-study.

   .. note::

      Preparation includes e.g., identification or definition of trainings, mentoring concepts, self-learning material.

.. std_req:: GP3.1.3: Determine the required resources.
   :id: R_ASPICE-40_GP-313
   :status: valid
   :links:std_bp__aspice-40__iic-10-52

   Required physical and material resources and process infrastructure needs for performing the standard process are determined.

   .. note::

      This may include e.g., facilities, tools, licenses, networks, services, and samples supporting the establishment of the required work environment.

.. std_req:: GP3.1.4: Determine suitable methods to monitor the standard process.
   :id: R_ASPICE-40_GP-314
   :status: valid
   :links:std_bp__aspice-40__iic-08-63

   Methods and required activities for monitoring the effectiveness and adequacy of the standard process are determined.

   .. note::

      Methods and activities to gather feedback regarding the standard process may be lessons learned, process compliance checks,
      internal audits, management reviews, change requests, reflection of state-of-the-art such as applicable international standards, etc.
      Appropriate criteria and information needed to monitor the standard process are defined.

   .. note::

      Information about process performance may be of qualitative or quantitative nature.


PA 3.2 Process deployment process attribute
-------------------------------------------

The process deployment process attribute is a measure of the extent to which
the standard process is deployed as a defined process to achieve its process outcomes.

Process attribute achievements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. A defined process is deployed based upon an appropriately selected and/or tailored standard process.
2. Assignment of persons necessary for performing the defined process to roles is performed and communicated.
3. Required education, training and experience is ensured and monitored for the person(s) assigned to the roles.
4. Required resources for performing the defined process are made available, allocated, and maintained.
5. Appropriate information is collected and analyzed as a basis for understanding the behavior of the process.


Generic practices
~~~~~~~~~~~~~~~~~

.. std_req:: GP3.2.1: Deploy a defined process that satisfies the context specific requirements of the use of the standard process.
   :id: R_ASPICE-40_GP-321
   :status: valid
   :links:std_bp__aspice-40__iic-10-00,std_bp__aspice-40__iic-15-54

   The defined process is appropriately selected and/or tailored from the standard process.
   Conformance of defined process with standard process requirements and tailoring criteria is verified.
   The defined process is used as managed process to achieve the process outcomes.

   .. note::

      Changes in the standard process may require updates of the defined process.

.. std_req:: GP3.2.2: Ensure required competencies for the defined roles.
   :id: R_ASPICE-40_GP-322
   :status: valid
   :links:std_bp__aspice-40__iic-14-53

   Human resources are allocated to the defined roles according to the required competencies and skills.
   Assignment of persons to roles and corresponding responsibilities and authorities for performing the defined process are communicated.
   Gaps in competencies and skills are identified, and corresponding qualification measures are initiated and monitored.
   Availability and usage of the project staff are measured and monitored.

.. std_req:: GP3.2.3: Ensure required resources to support the performance of the defined process.
   :id: R_ASPICE-40_GP-323
   :status: valid
   :links:std_bp__aspice-40__iic-13-55

   Required information to perform the defined process is made available, allocated and used.
   Required physical and material resources, process infrastructure and work environment are made available, allocated and used.
   Availability and usage of resources are measured and monitored.

.. std_req:: GP3.2.4: Monitor the performance of the defined process.
   :id: R_ASPICE-40_GP-324
   :status: valid
   :links:std_bp__aspice-40__iic-03-06

   Information is collected and analyzed according to the determined process monitoring methods to understand the effectiveness and adequacy of the defined process.
   Results of the analysis are made available to all effected parties and used to identify where continual improvement of the standard and/or defined process can be made.

   .. note::

      For guidance on how to perform process improvements see the Process Improvement process (PIM.3).

.. needextend:: "process/process_model/standards/aspice" in docname
   :+tags: aspice

Appendix
--------

.. needtable:: General Practices
   :style: datatables
   :columns: id;title;status;content
   :filter: id.startswith("R_ASPICE-40_GP")
