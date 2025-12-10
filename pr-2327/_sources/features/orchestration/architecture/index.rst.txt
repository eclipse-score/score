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

Feature Architecture
====================

.. document:: Orchestration Architecture
   :id: doc__orchestration_architecture
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feature_arch
   :tags: orchestration


Overview
--------
The orchestration feature provides frameworks for deterministic, scalable, and maintainable execution of mixed-criticality software applications. It introduces two main abstractions: the **Executor**, which offers cooperative user-space multitasking with configurable thread pools, and the **Orchestrator**, which enables declarative modeling of cause-effect chains, timing constraints, and fault handling logic. These frameworks are designed to improve integration, timing predictability, and validation of cross-component timing chains, supporting robust system integration in automotive and safety-critical environments.

Description
-----------

The orchestration framework is structured in layers, separating application logic from deployment and resource management. The **Executor** manages cooperative and preemptive tasks, dedicated threads for blocking operations, and provides observability hooks for system monitoring. The **Orchestrator** allows developers to define Programs as runtime-static execution graphs, specifying control flow, timing contracts, event-based synchronization, and fault handling. The API is code-first, enabling direct integration with application logic and improved debuggability. Observability is a key aspect, with tracing and metrics exposed at the Orchestrator, Executor, and kernel levels. The design enforces that inter-process communication and synchronization are exclusively handled via secure IPC mechanisms, ensuring safety and security in multi-process environments.


Rationale Behind Architecture Decomposition
*******************************************

The decomposition of the orchestration architecture is driven by the need for modularity, scalability, and maintainability in complex, safety-critical systems. By separating concerns into distinct layers and abstractions, the architecture enables:

- **Clear Separation of Responsibilities:** The division between the Executor and Orchestrator allows for independent evolution of scheduling mechanisms and high-level control logic. This separation ensures that timing, resource management, and application logic can be developed and validated independently.

- **Determinism and Predictability:** Layered decomposition supports deterministic execution by isolating timing-sensitive components and providing explicit control over execution flows and resource allocation.

- **Scalability and Reusability:** Modular components can be reused across different applications and deployment scenarios. This reduces duplication and enables the orchestration framework to scale from simple to highly complex systems.

- **Testability and Observability:** Isolated modules with well-defined interfaces facilitate targeted testing and verification. The architecture’s observability hooks at multiple layers enable comprehensive tracing and diagnostics, which are essential for safety and reliability.

- **Safety and Security:** By enforcing strict boundaries between application logic, resource management, and inter-process communication, the architecture minimizes the risk of unintended interactions and supports compliance with safety and security standards.

- **Ease of Integration:** The decomposition allows for declarative modeling of execution graphs and timing contracts, simplifying the integration of new features and components while maintaining system integrity.

This architectural approach is informed by best practices in automotive and safety-critical software engineering, ensuring that the system remains robust, adaptable, and maintainable as requirements evolve.

Static Architecture
-------------------

.. feat_arc_sta:: Static View
   :id: feat_arc_sta__orchestration__static_view
   :security: YES
   :safety: ASIL_B
   :status: invalid
   :fulfils: feat_req__orchestration__orch_static_graphs, feat_req__orchestration__exec_async_rt
   :includes: logic_arc_int__orchestration__user, logic_arc_int__orchestration__design, logic_arc_int__orchestration__deployment

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_feature(need(), needs) }}

API Components
--------------

The API is split into three key components:

1. **Design**

   - Provides a way to register all application callables (functions, async functions, objects, etc.)

   - Allows the creation of an application task flow in the `config-by-code` case

2. **Deployment**

   - Provides a way to bind specific application actions to concrete implementations in the current system:

      #. Binding events to Local/Remote/Timers
      #. Configuring certain threads for callables

3. **Orchestration**

   - Acts as the central API for managing designs and transitioning them into a deployment-ready state

   - Handles the creation of programs and their orchestration

Purpose of Orchestration, Design, and Deployment Split
------------------------------------------------------

The split between **Orchestration**, **Design**, and **Deployment** is intentional and reflects
a separation of concerns in the orchestration process:

- **Design**: Focuses on the **definition** of the system's components, encapsulating configuration
  and metadata for specific parts of the system.

- **Deployment**: Focuses on the **execution** of the designs, handling specific details of the
  given system.

- **Orchestration**: Acts as the **entry point** for managing designs and transitioning them into
  deployment, bridging the gap between the design phase and the deployment phase.

This separation ensures that each phase of the orchestration process is modular, testable, and maintainable.


Interface Description
---------------------

The public API for the frontend is defined as:

.. logic_arc_int:: Orchestration Interface
   :id: logic_arc_int__orchestration__user
   :security: YES
   :safety: ASIL_B
   :status: valid
   :fulfils: feat_req__com__interfaces

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int:: Design Interface
   :id: logic_arc_int__orchestration__design
   :security: YES
   :safety: ASIL_B
   :status: valid

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int:: Deployment Interface
   :id: logic_arc_int__orchestration__deployment
   :security: YES
   :safety: ASIL_B
   :status: valid


   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}
