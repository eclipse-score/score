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

SWE.1 Software Requirements Analysis
------------------------------------

The purpose is to establish a structured and analyzed set of software
requirements consistent with the system requirements, and the system
architecture.

Process outcomes
~~~~~~~~~~~~~~~~

1. Software requirements are specified.
2. Software requirements are structured and prioritized.
3. Software requirements are analyzed for correctness and technical
   feasibility.
4. The impact of software requirements on the operating environment is
   analyzed.
5. Consistency and bidirectional traceability are established between
   software requirements and system requirements.
6. Consistency and bidirectional traceability are established between
   software requirements and system architecture.
7. The software requirements are agreed and communicated to all affected
   parties.

Base practices
~~~~~~~~~~~~~~

.. std_req:: SWE.1.BP1: Specify software requirements
   :id:std_bp__aspice-40__SWE-1-BP1
   :status: valid
   :links:std_bp__aspice-40__iic-17-00

   Use the system requirements and the system
   architecture to identify and document the functional and non-functional requirements for the
   software according to defined characteristics for requirements.

   .. note::

      Characteristics of requirements are defined in standards such as ISO IEEE 29148, ISO
      26262-8:2018, or the INCOSE Guide for Writing Requirements.

   .. note::

      Examples for defined characteristics of requirements shared by technical standards are
      verifiability (i.e., verification criteria being inherent in the requirements text),
      unambiguity/comprehensibility, freedom from design and implementation, and not contradicting any
      other requirement.

   .. note::

      In case of software-only development, the system requirements and the system architecture
      refer to a given operating environment. In that case, stakeholder requirements can be used as the
      basis for identifying the required functions and capabilities of the software.

   .. note::

      The hardware-software-interface (HSI) definition puts in context hardware and therefore it is
      an interface decision at the system design level. If such a HSI exists, then it may provide input to
      software requirements.


.. std_req:: SWE.1.BP2: Structure software requirements
   :id:std_bp__aspice-40__SWE-1-BP2
   :status: valid
   :links:std_bp__aspice-40__iic-17-00;std_bp__aspice-40__iic-17-54

   Structure and prioritize the software requirements.

   .. note::

      Examples for structuring criteria can be grouping (e.g., by functionality) or expressing
      product variants.

   .. note::

      Prioritization can be done according to project or stakeholder needs via e.g., definition of
      release scopes. Refer to SPL.2.BP1.


.. std_req:: SWE.1.BP3: Analyze software requirements
   :id:std_bp__aspice-40__SWE-1-BP3
   :status: valid
   :links:std_bp__aspice-40__iic-15-51

   Analyze the specified software requirements
   including their interdependencies to ensure correctness, technical feasibility, and to support
   project management regarding project estimates.

   .. note::

      See MAN.3.BP3 for project feasibility and MAN.3.BP5 for project estimates.

   .. note::

      Technical feasibility can be evaluated based on e.g., platform or product line, or by
      prototyping.


.. std_req:: SWE.1.BP4: Analyze the impact on the operating environment
   :id:std_bp__aspice-40__SWE-1-BP4
   :status: valid
   :links:std_bp__aspice-40__iic-15-51

   Analyze the impact that the
   software requirements will have on elements in the operating environment.

.. std_req:: SWE.1.BP5: Ensure consistency and establish bidirectional traceability
   :id:std_bp__aspice-40__SWE-1-BP5
   :status: valid
   :links:std_bp__aspice-40__iic-13-51

   Ensure
   consistency and establish bidirectional traceability between software requirements and system
   architecture. Ensure consistency and establish bidirectional traceability between software
   requirements and system requirements.

   .. note::

      Redundant traceability is not intended.

   .. note::

      There may be non-functional system requirements that the software requirements do not
      trace to. Examples are process requirements or requirements related to later software product
      lifecycle phases such as incident handling. Such requirements are still subject to verification.

   .. note::

      Bidirectional traceability supports consistency, and facilitates impact analysis of change
      requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links,
      does not necessarily mean that the information is consistent with each other.

   .. note::

      In case of software development only, the system requirements and system architecture
      refer to a given operating environment. In that case, consistency and bidirectional traceability can be
      ensured between stakeholder requirements and software requirements.


.. std_req:: SWE.1.BP6: Communicate agreed software requirements and impact on the operating environment
   :id:std_bp__aspice-40__SWE-1-BP6
   :status: valid
   :links:std_bp__aspice-40__iic-13-52

   Communicate the agreed software requirements, and the results of the analysis
   of impact on the operating environment, to all affected parties.

.. needextend:: "process/process_model/standards/aspice" in docname
   :+tags: aspice
