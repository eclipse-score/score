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

.. _introduction:

Introduction
============

Background
----------

With the upcoming of central EE architectures in vehicles, computing power has been upgraded on few central components called 'High Performance Computers' or HPC. Together with these computing units comes an upgrade of operating systems towards multi-threaded schedulers with memory and resource separation in processes. There is a gap between these operating systems and the application layer that requires a common interface with functions and features for applications and application domains. The sum of these common and domain-agnostic functions is generally called "Middleware". The project uses the term "Core Software Stack" for this kind of functionality in differentiation to domain specific software stacks.

.. _introduction_scope:

Scope
-----

The scope of this project is the development of an open source core stack for Software Defined Vehicles (SDVs), specifically targeting embedded high-performance Electronic Control Units (ECUs).

Safe Open Vehicle Core is targeting to be the non-differentiating core of a software stack running on HPC ECUs of a software-defined vehicle. Consequently, this project's scope are the "inner layers" of such a stack between a hardware abstraction as its 'lower bound', 'southbound interface' and a platform API towards vehicle function applications as its 'upper bound', 'northbound interface'.

Out of scope are said applications running on this stack (those carry the differentiating aspects covered by adopters of the stack). As well out of scope are any aspects related to a concrete hardware target, which will be freely chosen by each adopter individually, as per the needs of and as they see fit with their vehicle architecture — except support for a potential reference hardware. Furthermore, any off-board functionality (e.g. cloud services) is considered out of scope. Looking beyond mere implementations in code, the project very well considers establishing concepts and implementations of processes, or a "way of doing things", or best practices to be in scope — but only as long as it pertains to making code fit for automotive grade.

Guiding Principles
------------------
The project aims to BUILD THE BEST AUTOMOTIVE RUNTIME SOLUTION ONLY ONCE. To achieve this, it is guided by several key principles.

Common Stack & Industry-Wide Collaboration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The Safe Open Vehicle Core project aims to create a common full stack solution of a software runtime that serves as the best possible solution for shared industry problems. By achieving efficiencies through a single, joint solution instead of multiple specific ones, the project addresses non-differentiating scopes and ensures that the scope is significant for multiple parties, rather than catering to singular interests.

Speed
^^^^^

   The project accelerates development by working in open source, focusing on code-centric and iterative methods rather than primarily on textual specifications.

Abstraction and Extensibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The project emphasizes the decoupling of hardware (HW) and software (SW), ensuring that applications do not depend on specific hardware characteristics. It establishes predetermined breaking points to enable the exchange of implementations of individual layers, aspects, and components, such as ECU communication protocols. Additionally, it focuses on enabling project-specific extensions of the stack, providing a flexible framework that can be customized and extended to meet the specific requirements of different projects.

Quality & Efficiency
^^^^^^^^^^^^^^^^^^^^

   The Safe Open Vehicle Core project aims for a lean, no-frills solution to lower complexity and increase efficiency. The project strives for support of modern implementation paradigms and languages like Rust or C++, uses human-readable specification languages that are domain and target-driven, and avoids complex exchange data formats. It seeks the optimal balance between modularity and resource consumption and follows state-of-the-art processes to develop safe and secure software in an open source environment.



By achieving these goals and adhering to these key principles, the Safe Open Vehicle Core Project aims to deliver a versatile, safe and secure core stack that supports the evolving needs of the automotive industry and accelerates the adoption of software-defined vehicle technologies.

Architecture
------------

The following figures show a draft version of the planned architecture of the core stack. The architecture will be refined further as part of the project.

High Level View on the Core Stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following high level architecture picture gives you an overview of the main platform building blocks
including hardware specific peripherals.

.. image:: _assets/score_architecture_high_level_overview.png
   :width: 900
   :alt: High level view on the core stack
   :align: center

Target Picture of Core Stack - PRELIMINARY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following image shows platform architecture in more details including surroundings as
Board support package (BSP) and HW specific.

.. image:: _assets/score_architecture_core_stack_target_picture.png
   :width: 900
   :alt: Target picture the core stack (preliminary)
   :align: center

.. _introduction_roadmap:

Roadmap
-------

Here you can find the preliminary roadmap of the project:

.. image:: _assets/score_roadmap.drawio.svg
   :alt: project roadmap
   :align: center

Please be aware, that the roadmap is transferred to and maintained in the `GitHub project <https://github.com/orgs/eclipse-score/projects/13/views/2>`_.
Please follow this link to get the latest state of the planning.

MVP Phase
^^^^^^^^^

The main goals of the *MVP Phase* are following:

* establish a working infrastructure, that enables every developer of the project to specify
  requirements and architecture, implement code and test it accordingly.
* set-up project structure, that covers all aspects of the open source software development including
  cooperation between developers and teams, planning, creation of the roadmap and coordination meetings.
* define a software development process compliant to ISO 26262:2018, that is a pre-requisite for any other software development in the project.

A lot of preparation was already done in the background, therefore we are quite optimistic to finish the *MVP Phase*
latest in the beginning of 2025.

Alignment Phase
^^^^^^^^^^^^^^^

In the *Alignment Phase* the main goal is to align on the feature architecture and requirements of the *S-CORE Platform v1.0*.
Additionally it is important to define the roadmap and the order, in which the features should be implemented.

Development Phase
^^^^^^^^^^^^^^^^^

The *Development Phase* is the phase, where the implementation of the main modules of the platform should happen.
The most important milestone here is the *Release v0.5*, that should contain the basic modules, e.g *IPC*.
The *Release v0.5* milestone will show, whether previously defined software development process will work and how big is the acceptance and
the interest of the automotive community to the project.

Series Stability & Evolution Phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this phase the project should be in an well established state and accepted by the community. Continuous development
of the features is taking place.

How we Work
-----------

Meetings
^^^^^^^^

Regular meetings (and corresponding meeting minutes) are held as part of the project:

- `Teams & Circles <https://github.com/orgs/eclipse-score/discussions>`_

Typically teams and circles meet weekly.

A public meeting calendar for the *S-CORE* project is in preparation.

Partners
^^^^^^^^

The people working in this project are listed `here <https://projects.eclipse.org/projects/automotive.score/who>`_.


How to contribute
^^^^^^^^^^^^^^^^^
For a guide on how to get involved and start contributing, please checkout :ref:`contribute`.
