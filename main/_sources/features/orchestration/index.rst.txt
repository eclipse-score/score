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


.. _orch_feature:

Orchestration (v0.5 beta)
##########################

.. document:: Orchestration
   :id: doc__orchestration
   :status: valid
   :safety: ASIL_B
   :security: YES
   :realizes: wp__feat_request
   :tags: feature_request, change_management, orchestration


.. toctree::
   :hidden:

   requirements/index.rst
   architecture/index.rst
   safety_planning/index.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_orchestration``


Abstract
========

This feature proposes two frameworks, the Executor and the Orchestrator, to support deterministic, scalable, and maintainable execution of mixed-criticality software applications. The Executor provides cooperative user-space multitasking using a configurable thread pool, reducing overhead and improving control over scheduling behavior without relying on one-thread-per-task models. It supports safety-critical preemptive tasks, dedicated threads for blocking operations, and structured observability.

The Orchestrator complements this by offering a declarative model to define cause-effect chains, timing constraints, and fault handling logic. Programs are structured as runtime-static graphs mapped to Executors, enabling clear separation between application logic and deployment configuration. Integration workflows distinguish responsibilities between application developers and system integrators, supporting both unified and distributed development scenarios.

Together, these frameworks reduce integration effort, improve timing predictability, and allow validation of cross-component timing chains. Observability hooks enable correlation between application-level logic and OS-level scheduling. This design avoids runtime surprises due to implicit assumptions in thread usage and timing behavior, supporting more robust system integration in automotive and safety-critical environments.



Motivation
==========

Application Behavior in Mixed-Criticality Domains
-------------------------------------------------

In software systems for domains like ADAS and automated driving, applications frequently follow periodic cause-effect structures. A typical example includes a camera providing images at 30 frames per second, with each frame triggering object detection, which feeds into a fusion module to compute a new trajectory. This repeating, sensor-driven processing cycle defines how most software on the mixed-criticality processor domain is organized. The structure remains valid even when offloading is involved, such as using GPUs or NPUs for computation.

This execution model already shaped software development in microcontroller environments (e.g., Classic AUTOSAR), and continues to apply to more powerful systems. What changes is the complexity of algorithms and the compute and communication cost between them. But the underlying pattern, periodic execution triggered by external or internal stimuli, remains relevant and useful.

The goal is to support this type of application logic natively and systematically across different runtime environments without requiring developers to micromanage scheduling behavior or resource usage.

Integration Complexity Due to OS-Level Thread Management
--------------------------------------------------------

In today's systems, application development is often distributed across teams or organizations. These teams typically focus on their own application logic and do not have full visibility into the target deployment. However, current APIs often expect applications to manage thread lifecycles directly, including thread creation, priorities, and affinities, as is the case in Adaptive AUTOSAR. This results in applications being tightly coupled to assumptions about system resources and execution environments.

Once the application is deployed, these assumptions often break. A typical integration issue occurs when an application shows correct timing on the development system but exhibits unexpected behavior on the actual target. This leads to repeated coordination loops between developers and integrators, adjusting priorities and affinities manually. As a result, the deployment becomes brittle and tightly bound to the specific configuration of the system, making re-use and scalability difficult.

This issue is amplified in mixed-criticality environments, where scheduling decisions have direct safety implications. Lower-criticality software must not interfere with the timing of high-criticality components. This makes unmanaged threading even more problematic.

Timing Awareness and Predictability in Application Logic
--------------------------------------------------------

In current systems, timing supervision and error handling are often implemented in separate, system-level components like health monitors. This leads to low cohesion: timing constraints and critical behavior are managed far from the application logic that they affect. It also makes it difficult to validate cause-effect chains that span multiple applications or components.

A more robust design would allow timing monitors and error paths to be expressed alongside the application logic they supervise. This would improve local reasoning, simplify debugging, and support more deterministic system behavior, especially when coordinating multiple applications with timing dependencies.

Concurrency Overhead in Service Infrastructure
----------------------------------------------

The system must also support platform services such as diagnostics, configuration management, health supervision, and communication gateways. In existing stacks, these services often run one thread per client, leading to rapid thread growth. For instance, 15 services accessed by 150 applications would result in over 2,000 threads. This can create significant performance problems, including increased context-switching, memory pressure, and degraded throughput.

The platform must support a concurrency model that can scale to such numbers without relying on a one-thread-per-task model. Reducing thread count while preserving concurrency is essential, both for platform services and for user-level applications.

Observability and Validation in Real Deployments
------------------------------------------------

To support predictable behavior and real-time debugging, the system must offer visibility into task-level execution and its interaction with the OS scheduler. Developers and integrators need to answer questions such as: When was a specific task scheduled? On which thread? Was a delay caused by CPU starvation or by another blocking task?

This requires instrumentation that correlates user-space task execution with kernel-level scheduling behavior. Without such observability, it is difficult to validate integration or analyze failures in timing-critical systems.



.. Rationale
.. ==========



Specification
=============

To address these challenges, this proposal introduces two frameworks:

1. The **Executor**, which provides cooperative, user-space multitasking on top of a configurable thread pool.
2. The **Orchestrator**, which provides a declarative layer to define execution structures and timing requirements in a way that is independent of the deployment platform.

Together, these frameworks allow developers to write reusable application logic and enable integrators to manage deployment, scheduling, and timing without modifying the code.

Executor
--------

The Executor framework provides user-space multitasking through cooperative scheduling of tasks over a thread pool. It abstracts OS threads into lightweight tasks, enhancing concurrency without incurring excessive OS-level overhead. The framework addresses scalability, predictable scheduling, and controlled resource allocation in mixed-criticality software systems.

Task Model
~~~~~~~~~~

Tasks are the fundamental concurrency unit managed by the Executor. A task represents a schedulable computation defined through a future-based model. Specifically, a task is an independently executable sequence of computation that progresses cooperatively. Tasks explicitly yield execution at defined points (``await``), allowing controlled switching between tasks without preemption.

This cooperative scheduling model offers:

- Reduced overhead and context-switching.
- Improved system scalability due to lightweight task management.

Cooperative Multitasking
~~~~~~~~~~~~~~~~~~~~~~~~

By default, tasks execute cooperatively and must voluntarily yield execution. Tasks explicitly yield at await points or logical suspension points, aligning with models such as Rust's ``async/await`` semantics or C++ coroutines (``co_await``).

Tasks must avoid blocking or indefinite execution without yielding. Developers are responsible for ensuring tasks are appropriately structured to cooperate with the scheduler.

Handling Long-Running Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Long-running tasks, or tasks containing blocking calls, present challenges in cooperative scheduling environments. The Executor framework must provide mechanisms for handling these scenarios effectively:

- **Guidance on task chunking**: The Executor must provide guidelines for developers to divide long-running operations into smaller, cooperatively yielding segments. This approach aligns with best practices for embedded concurrency patterns, as detailed in the `Ferrous Systems article <https://ferrous-systems.com/blog/embedded-concurrency-patterns/#async--long-running-operations>`_.

- **Dedicated threading**: For tasks that cannot be chunked easily, such as tasks using third-party libraries with blocking operations, the Executor must support running these tasks on dedicated threads. These dedicated threads are isolated from cooperative tasks, ensuring predictable execution and avoiding interference with the cooperative task scheduling.

Preemptive Special Tasks
~~~~~~~~~~~~~~~~~~~~~~~~

Certain scenarios, particularly safety-critical fault detection or timing monitoring, require tasks that can preempt cooperative tasks. These special tasks are managed separately and guaranteed execution to avoid starvation or blocking. The Executor framework must provide mechanisms to support:

- Preemptive scheduling of these special tasks.
- Isolation and prioritization of safety-critical tasks distinct from standard cooperative tasks.

Thread Pool Management
~~~~~~~~~~~~~~~~~~~~~~

Tasks run on OS threads managed within statically configured thread pools. Each Executor instance has its own dedicated thread pool with:

- A fixed number of threads defined at configuration time.
- Identical OS-level thread priority across all threads within the same Executor.
- Optional configuration of thread affinity to specific CPU cores.

This ensures predictable timing and resource utilization. Thread pools are isolated per Executor instance; threads are not shared among Executors.

Task Scheduling and Prioritization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within an Executor, standard tasks have uniform priority and execute cooperatively without task-level priority distinctions. Task scheduling follows either FIFO or fairness-based ordering within the cooperative scheduling context.

Preemptive special tasks are managed distinctly and do not compete with cooperative tasks for scheduling.

Scaling
~~~~~~~

Scaling across multiple Executors is achieved through instantiating additional Executor instances rather than dynamically scaling existing thread pools. While each Executor is assigned to a single process, a single process may host multiple Executors to partition workloads or isolate scheduling domains. Each Executor instance is independently configured regarding:

- Thread pool size
- OS-level priority
- CPU affinity

This explicit configuration avoids interference across different criticality domains, maintaining determinism and composability in system integration.

Orchestrator
------------

The Orchestrator framework provides a structured, declarative way to define cause-effect chains and timing requirements within software applications. It enables developers to specify control flow, timing constraints, and error handling in a platform-independent manner. The Orchestrator integrates seamlessly with the Executor, clearly separating application logic from deployment and resource management.

Program Abstraction
~~~~~~~~~~~~~~~~~~~

The primary abstraction within the Orchestrator is the **Program**, which represents a runtime-static execution graph. Programs describe computation logic in terms of:

- Sequential, parallel, or conditional execution flows.
- Loops (bounded iteration or periodic execution).
- Timing contracts, including deadlines and timeouts.
- Trigger conditions via events and cross-program synchronization.
- Fault handling logic, such as fallback paths and retries.

Program structures are fixed either at compile-time or during startup. While parameters may be reconfigured dynamically, the structural form of a Program remains static.

Code-First API Design
~~~~~~~~~~~~~~~~~~~~~

The Orchestrator employs a code-first API approach rather than a textual DSL or IDL. This ensures:

- Direct integration with application logic.
- Improved debuggability and flexibility during development.
- Simplified tool support, enabling incremental addition of declarative frontends if needed.

Execution Model
~~~~~~~~~~~~~~~

Each Program is deployed to a single Executor instance. Executors may host multiple Programs to facilitate resource sharing or logical grouping. Programs communicate and synchronize through explicitly defined events. Events serve as triggers or synchronization points and form the interface between individual Programs (potentially shared across Executors and processes).

Design and Integration Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Orchestrator supports flexible development and integration scenarios:

- **Unified Development Scenario**: A single development team manages the complete cause-effect chain within one Program, explicitly defining all timing constraints and logic.

- **Distributed Scenario**: Different teams independently develop Programs for separate components. An Integrator combines these Programs into a coordinated *Program-of-Programs* by wiring events and managing global timing constraints and fault containment.

Timing Semantics
~~~~~~~~~~~~~~~~

Timing semantics in the Orchestrator are defined declaratively through three primitives:

1. **Events**: Trigger execution at defined intervals or upon external stimuli (e.g., sensor inputs).
2. **Logical Delays**: Insert cooperative, non-blocking delays within execution flows (``sleep(duration)``).
3. **Execution Monitors**: Observe and enforce timing constraints, triggering specified error handling paths upon violations.

This approach enables precise control over timing behaviors without relying on polling or dedicated monitoring threads.

Special Safety Tasks and Preemption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programs may define critical timing or safety measures within the error handling paths, which the Executor ensures to execute preemptively by utilizing the safety tasks introduced above. This guarantees that timing constraints and fault responses execute reliably, even during saturation or task overload conditions. Such preemptive execution is configurable per deployment scenario and activated only when explicitly defined by safety or timing constraints.

Integration Workflow
~~~~~~~~~~~~~~~~~~~~

**Application Developer Responsibilities**:

- Define Program logic using Orchestrator APIs.
- Declare events for synchronization and triggers.
- Establish timing and error-handling paths.

**Integrator Responsibilities**:

- Instantiate and configure Executors (thread count, priority, affinity, criticality).
- Map Programs explicitly to Executors.
- Wire events between Programs and external sources.
- Optionally integrate multiple Programs into coherent cause-effect chains (*Program-of-Programs*).

Anticipated Tooling (Out-of-Scope)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While initial development is code-first, the Orchestrator anticipates future integration of tools such as:

- Static analyzers to validate resource allocation.
- Timing validation tools (end-to-end latency calculators).
- Visualization tools mapping Program execution onto system resources and cores.

System Observability
--------------------

Effective observability in systems requires correlation across application logic, user-space task scheduling, and kernel-level scheduling behavior. To facilitate this, the Executor and Orchestrator frameworks expose structured tracing and metrics that enable developers and integrators to analyze, debug, and validate the system comprehensively.

Observability Correlation
~~~~~~~~~~~~~~~~~~~~~~~~~

Observability in this architecture spans three layers:

1. **Orchestrator-level Observability**:

   - Program transitions and execution flow (entry, exit, branching decisions).
   - Timing monitor status, including deadline tracking and violations.
   - Event timing and synchronization points.

2. **Executor-level Observability**:

   - Task lifecycle events: creation, scheduling, yielding, completion, or rejection.
   - Executor queue metrics, including load and scheduling delays.
   - Mapping and correlation of user-space tasks to OS-level threads.

3. **OS Scheduler Correlation**:

   - Visibility into OS thread scheduling decisions (context switches, core affinity adherence).
   - Identification of potential CPU starvation or blocking behaviors impacting task execution.

To achieve comprehensive observability, the system exposes standardized trace points.

Integration with Tracing Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The trace points are designed to integrate seamlessly with established tracing frameworks, such as e.g. Perfetto and LTTng. This ensures compatibility with existing system analysis tooling and minimizes additional overhead for trace processing and visualization. The tracing framework itself, however, is considered out of scope for the orchestrator feature request (see tracing feature).

External Supervision
--------------------

The Executor and Orchestrator frameworks expose observability hooks to integrate with external supervisory systems, such as systemd's watchdog or custom health monitors. These hooks provide mechanisms for external entities to verify and validate the health of Executors and Programs without requiring direct task-level instrumentation.

The Executor and Programs are considered healthy when:

- Either all timing constraints (execution monitors) within Programs are consistently satisfied, or the defined error-handling logic within Programs executes correctly and completely in response to any timing violations or other faults.
- And critical tasks are executed reliably, with no instances of starvation, deadlocks, or indefinite blocking observed within Executors.

The design ensures tasks themselves do not require explicit interfacing with external monitoring mechanisms. Instead, Executor and Program frameworks transparently integrate health checkpoints internally. The external health monitor is considered out of scope for the orchestrator feature request (see lifecycle and health feature).



.. Backwards Compatibility
.. =======================


Security Impact
===============

.. note::

   This section does not replace a formal security impact analysis. This only guides the design thoughts behind security related topics and is to be understood as a starting point for later workflows.

The design of this orchestration feature is based on the assumption that all code executing within a process is trusted. Consequently, the attack surface within a single process is inherently minimized, as the task isolation provided by threads is secure due to the fact that threads cannot be accessed from outside the process.

A potential attack surface arises from the synchronization between tasks or threads that belong to different processes. To mitigate this risk, the feature request mandates the exclusive use of the :ref:`communication_ipc` for any inter-process synchronization. This communication feature has been previously evaluated with regard to its security impact on synchronization primitives and is considered secure. No alternative forms of exchange or synchronization between processes are permitted for this feature.


Safety Impact
=============

.. note::

   This section does not replace a formal safety impact analysis. This only guides the design thoughts behind safety related topics and is to be understood as a starting point for later workflows.

The orchestration feature is designed under the assumption that all tasks within a single process share the same ASIL level. As a result, the internal task management must not mix different safety levels. In the specification section, the capability to define robust error handling mechanisms is described. These mechanisms are intended to serve as integral safety elements within an application's safety concept. Consequently, the feature must ensure that if error handling mechanisms are present, they are isolated from the effects of misbehaving tasks (for example, in the worst-case scenario where all threads in the pool become occupied by tasks in an infinite loop). This functionality shall be implemented in a configurable manner, recognizing that not all applications require safety mechanisms to be defined through the orchestration feature, and that ensuring guaranteed reactivity typically incurs a cost.

In addition, the orchestration feature must expose hooks for external supervision of its safety mechanisms. These hooks enable integration with an external watchdog, while the feature itself will not directly connect to a watchdog, thereby preserving platform maintainability.

Finally, for mixed-criticality deployments the feature shall enforce that all tasks within a thread pool (or process) have the same criticality level. Lower-criticality tasks must not influence the timing behavior of higher-criticality tasks. This is achieved by leveraging the OS's preemptive scheduling between thread pools, and by managing inter-process synchronization exclusively via the :ref:`communication_ipc`, which is already validated for this purpose.


.. License Impact
.. ==============


How to Teach This
==================
A good first read is The Rust Async Book [#s1]_. It helps to get a better understanding of how user-level context switching and cooperative multi-tasking works in theory. Additionally, the referenced material in the :ref:`footnotes` can be used to get more familiar with the problem statements and proposed solution of the feature request.

.. Rejected Ideas
.. ==============

.. Open Issues
.. ===========

Glossary
========

.. glossary::

   task
      A lightweight, independently schedulable unit of execution managed in user space. Typically represents a future, coroutine, or async function.

   thread
      The smallest sequence of programmed instructions that can be managed independently by an operating system. Threads share a process's resources, such as memory, and are scheduled by the operating system or by user-level schedulers.

   concurrent
      The ability of a system to manage multiple tasks over overlapping time periods. Concurrency does not necessarily mean that tasks are executed simultaneously, but rather that progress can be made on more than one task during the same time interval.

   parallel
      The simultaneous execution of multiple tasks on different processing units, such as CPU cores. Parallelism is a subset of concurrency and is used to speed up processing by dividing tasks among available hardware resources.

   cooperative
      A scheduling model in which tasks voluntarily yield control to enable other tasks to execute. In cooperative multitasking, task switching occurs at well-defined points, reducing the overhead of context switching and simplifying the management of shared resources.

   preemptive
      A scheduling model where task execution can be interrupted externally.

   fairness-based scheduling
      A scheduling strategy that aims to ensure all ready tasks or threads are given equitable opportunities to progress over time. In cooperative scheduling (e.g., async executors), this involves polling tasks in a way that prevents any single task from monopolizing the scheduler, assuming tasks yield control appropriately. In preemptive systems, it ensures that no runnable thread is starved of CPU time. Fairness may be implemented via round-robin, aging, or probabilistic approaches, but it does not guarantee strict time-sharing.

   program
      A static, declarative graph that defines the control flow and timing semantics of an application's task logic.

   application
      The smallest individually updateable software unit from a deployment or system architecture point of view. An application may contain one or more programs, which are the unit of execution logic.


.. _footnotes:

Footnotes
=========

.. [#s1] "Asynchronous Programming in Rust", https://rust-lang.github.io/async-book/
