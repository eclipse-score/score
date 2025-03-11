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

Concept Description
###################

.. doc_concept:: Requirements Concept
   :id: doc_concept__req__process
   :status: valid
   :tags: requirements_engineering

In this section a concept for the requirements management will be discussed. Inputs for this concepts are both the requirements of ISO26262 Part-8 and ASPICE Requirements from SWE.1 additionally including the requirements of the different stakeholders for the requirement process.

Inputs
******

#. Stakeholders for the requirements?
#. Who needs which information?
#. Which Requirement Levels can we derive from that?
#. Which Attributes are required?
#. How do the different requirement levels correlate to each other?

Stakeholders for the requirements
=================================

#. :need:`Tech Lead Circle <rl__technical_lead>`

   * Define specification and content for the platform
   * Creation of a project timeline
   * Track project progress

#. :need:`SW Architect <rl__committer>`

   * Break down the platform specification into features (High Level)
   * Derive component architecture for each feature
   * Allocate requirements to architecture elements for specification of features/components
   * Define AoUs which arise from architecture

#. :need:`Tester <rl__committer>`

   * Verify that the specification is fulfilled by the elements under test
   * Consider AoUs for test case specification

#. :need:`Safety Architect <rl__safety_manager>`

   * *Dependent Failure Analysis*

     * Requires inputs towards independence and interference of the element under investigation

   * *Qualitative safety analysis* (e.g. FMEA)

     * Detailed element description to identify systematic errors within the element under investigation

#. :need:`Security Architect <rl__security_manager>`

   * Trust Boundary Analysis
   * Defense in Depth Analysis
   * Qualitative Security Analysis (TARA or at least Attack Potential Analysis with impact category Safety)

#. :need:`Platform/Tooling SW Developer <rl__committer>`

   * Implement the SW according to its specification
   * Create traceability by linking its specification to code
   * Consider AoUs of other components
   * Create AoUs for component under development

#. Feature User

   * Get detailed information concerning the specification of a feature
   * Be informed about its boundary conditions (AoUs)

#. :need:`Platform SW Developer of the Reference Integration <rl__committer>`

   * Requirements for Integration

Standard Requirements
=====================

Also requirements of standards need to be taken into consideration:

* ISO26262
* ASPICE
* ISO SAE 21434

Requirement Levels
******************

Based on the inputs of the previous chapter the types of requirements which need to be implemented in the project can be derived. The defined levels are shown in <TBD>

Stakeholder Requirements
========================

On the platform level the *Stakeholder (=customer) Requirements* are defined. These requirements describe which content the platform needs to contain, and serve as a project description of the top-level functionality. An example could be e.g.

.. code-block:: text

   The platform shall support configuration of applications via files (e.g. yaml, json)

Feature Requirements
====================

The *Feature Requirements* addresses mainly the integration level of SW modules and components. These shall describe the behavior of the feature on platform level shall be described including the correlations of the integrated components. They serves mainly as an input for (SW + Safety) Architects, Testers, Integrators and are derived from the *Stakeholder Requirements*. To provide an example

.. code-block:: text

   The feature shall accept JSON formatted string input according to RFC-8259

However the detailed interaction of the underlying components itself which is required to form a feature shall be defined in the feature architecture.

Component Requirements
======================

The lowest abstraction level is represented by the *component requirements*. They are derived from *feature requirements* and describe component specific implementation details. It is described which behavior a component itself needs to fulfil in the context of the feature, e.g.

.. code-block:: text

   The component shall provide API calls to read and interpret every field of a JSON body in C++

Assumption of Use Requirements
==============================

Last but not least a requirement type is needed which describes e.g. the boundary conditions which need to be fulfilled when using a software module. Those requirements are called *Assumption of Use* (AoUs)

.. code-block:: text

   The user shall provide a string as input which is not corrupted due to HW or QM SW errors.

Process Requirements
====================

Besides those four types of requirements which describe the contents of the platform also a type, describing the requirements towards the tooling from a process point of view, needs to be specified. These *process requirements* can be derived from a process description. Here it is defined which part of the process need to be performed manually and which parts of the process should be implemented by tooling

.. code-block:: text

   It shall be checked that safety requirements (Safety != QM) can only be linked against safety requirements.


.. _attributes of the requirements:

Attributes of the Requirements
******************************

The required attributes for the requirements are defined in this subchapter. On the top level we can distinguish between attributes which need to be filled manually and attributes which are generated during the *docs build*.

Following attributes need to be filled manually for each requirement:

.. list-table:: Manual Attributes
   :header-rows: 1
   :widths: 15,85

   * - Attribute
     - Description
   * - Status
     - The status for a requirement can either be valid or invalid. The reasoning for this is that the goal is to only have valid requirements in the main branch. So a status *draft* is not required. It is obvious that the requirement is in the status draft as long as the PR is not merged.
   * - Unique ID
     - The unique id consist of a prefix for the requirement type followed by a keyword for the feature/component and a short keyword describing its content. It is used as a unique identifier for a requirement which can be used e.g. for linking the requirements.
   * - Title
     - The title of the requirement shall be expressive and rely to the description of the requirement.
   * - Description
     - In this attribute the content for the requirement will be specified. Please be aware that a note in a requirement is not part of the requirement itself. This means that notes should only be used to give additional explanation or context to the requirement.
   * - Rationale / Linkage
     - In either of those attributes the reasoning for the requirement is included.
       For *Stakeholder Requirements* a rationale which provides some more background infos shall be provided.
       For any other requirement the reasoning can be deduced from the top level requirement.
   * - Safety
     - This attribute describes the impact of the requirement on functional safety. Currently only following values are defined [QM, ASIL_B, ASIL_D]. Other values are not required at the moment as *ASIL decomposition* is not used so far.
   * - Security
     - This attribute describes if the requirement has any impact on security of the platform.
   * - Requirements Type
     - The requirement type defines which category the requirement relates to. Following categories are defined: [Functional, Interface, Process, Legal, Non-Functional]

.. list-table:: Automated Attributes
   :header-rows: 1
   :widths: 15,70,15

   * - Attribute
     - Description
     - Tool
   * - Satisfied by
     - This attribute is automatically generated into the parent requirement based on the attribute satisfies of the current requirement
     - Sphinx Needs Build
   * - Hash
     - This attribute contains a hash value which is calculated over all mandatory requirement attributes. However this script needs to be executed manually, as this information is required to be present in the rst file.
     - Script / Bazel Target
   * - Satisfies Hash
     - It contains the hash of the parent requirement. If the parent requirement is changed the hash will also change and the linkage has to be revisited again. A more detailed description is provided here: :need:`gd_req__req__attr_hash`
     - Script / Bazel Target
   * - Implemented by
     - During Build the code files are parsed for a defined tag which includes the requirement id. If this is located a link to the code will be added in the requirement
     - Sphinx Needs Build
   * - Verified by
     - During build the junit test files are parsed for a defined marker which includes the requirement id. If the marker is located in the test a link to the test case will be added to the requirement
     - Sphinx Needs Build
   * - Requirement Covered
     - During build it will be checked if the requirements hashes which are mentioned in the coverage file match the hashes of the linked child requirements. If so then this attribute will be set to yes.
     - Sphinx Needs Build

More details about the generation of the automated attributes are explained in the following chapter where the general workflow for generating requirements including their status is shown.

.. _requirement_versioning:

Requirements Versioning
***********************

Individual Requirements
=======================

For the requirements the version management is basically provided by the git history. However it needs to be identified if the content of a requirement changed. So this concept aims only at identifying a change in the mandatory attributes of a requirement.

Calculate hash for current requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each requirement a hash shall be calculated and stored in its dedicated own attribute *Hash* in the RST file. It shall include all mandatory manual attributes:

.. _requirement_mandatory_attributes:

.. needtable:: Overview mandatory requirement attributes
   :filter: "mandatory" in tags and "attribute" in tags and type == "gd_req"
   :style: table
   :columns: title;id
   :colwidths: 60,40

There shall be a tooling available which can be executed by the user during the creation of the requirements. This tooling shall calculate the hashes based on the mandatory attributes, calculate the hash values and enter the calculated hash values into the rst file for each requirement in the attribute *hash*.

During Sphinx build it shall be checked if the attribute hash matches the actual has value of the requirement.

Linking child requirements including hashes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a requirement is linked to a top level requirement also the hash of the target requirement shall be part of the link. It shall automatically be written into the attribute *satisfies hash*. Upon Sphinx Build it shall be checked if the attribute *satisfies hash* matches the calculated hash of the requirement which is linked via *satisfies*.

As this check is included in the sphinx build as a warning it can be guaranteed that a change of a parent requirement can only be merged if the `linkhashes` in the requirements are also updated in a `Depends-On` PR.

.. figure:: _assets/requirements_versioning.drawio.svg
   :alt: Requirements Versioning
   :align: center
   :width: 50%

   Versioning of Requirements

.. _reviews of the requirements:

Sets of Requirements / Baselines
================================

GitHub standard functionality provides the means to version sets of requirements, as those are collected in files.
The files commit history can be displayed, to show change date, author and differences.
And via Git "Blame" also the changes on every requirement line.
Requirement baseline generation is part of the configuration mangement,
it is also done with GitHub means by tagging a complete set of artefacts/files in a repository.

Reviews of the Requirements
***************************

Some of the checks cannot be performed automatically. Therefore a manual inspection of the requirements is needed. The requirement review itself is triggered when a contributor wants to trigger a requirement review.

In the general for the reviews a guideline exists: <TBD>

.. _coverage_of_requirements:

Coverage of requirements
************************

According to the standards, requirements shall be derived from top to bottom. This means that at the point in time when the parent requirement is generated the coverage for itself can not be evaluated. In a second step all the parent requirements need to be broken down into child requirements which are linked to the parent requirement again. If during the creation of the child requirements any of the parent requirements would be touched again the hash value of the parent requirement would change and the linkage from the child to the parent requirement would be invalid again.

Therefore the information concerning requirement coverage is stored in a config file located in the same folder as the requirements file. It contains the parent requirements and it´s links to child requirements including hashes to the of the child requirements. If it is merged to the main branch it will specify exactly the coverage of child requirements which are required to fulfil the coverage of the parent requirement.

If this file will now be merged to the main branch a review will be triggered again. During this review it will only be checked if the parent requirement is covered by its child requirements.

Additionally during build it shall be checked if exactly the requirements and hashes which are specified in this file are linked to the requirement in the current documentation. If all items match then the requirement can be seen as covered. If now a child requirement is changed its hash will also be changed and the requirement coverage needs to be revisited again.

.. _traceability concept for requirements:

Traceability Concept for Requirements
*************************************

The standards require that a requirement can be traced throughout the complete hierarchy levels including its implementation and verification <TBD: Link>. In this project it is implemented the following way:

In general the traceability is visualized in main development work product traceability model (:numref:`wp_traceability_model`).
