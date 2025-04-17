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

.. _orchestration_feature:

Orchestration
#############

.. document:: Orchestration
   :id: doc__orchestration
   :status: valid
   :safety: ASIL_B
   :tags: change_management


.. toctree::
   :hidden:

   requirements.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_orchestration``


Abstract
========

In response to the increasing complexity of modern centralized E/E architectures and the need to support hundreds of applications, this feature request proposes a comprehensive orchestration framework for managing concurrency in high-performance computing (HPC) systems. The motivation for this proposal is rooted in the significant performance penalties incurred by conventional thread-based approaches, where an excessive number of threads leads to costly context switching in operating systems.

The proposed solution introduces user-level scheduling through cooperative multi-tasking, allowing task switches to occur in the nanosecond range instead of microseconds. By treating tasks as the fundamental unit of concurrency and enabling multiple tasks to share the same OS thread, the framework significantly reduces overhead and simplifies resource allocation.

Overall, this orchestration feature is designed to provide a safe and secure, deterministic, user-friendly interface that streamlines concurrent execution, optimizes resource utilization, and facilitates the reliable integration of mixed-criticality applications in complex automotive and embedded systems.


Motivation
==========

The rapid evolution of high-performance computing (HPC) architectures and the increased availability of multi-core processors in centralized E/E systems have driven the need for a platform capable of hosting advanced ADAS/AD applications while upintegrating existing ECU functionalities. This approach facilitates the deployment of loosely coupled applications that support flexible maintenance and updates, with the goal of hosting between 100 and 150 individual applications.


Motivation: Increasing Performance in a Highly Concurrent System
-----------------------------------------------------------------

In existing platforms for microprocessors (µP), each application is expected to interact with approximately 15 system services or daemons - such as ``ara::diag`` for diagnostics and ``ara::com`` for SOME/IP communication. Under a straightforward implementation, this interaction model results in the creation of around 15 threads per application. When scaled to 100-150 applications, this amounts to roughly 1500 to 2250 threads solely managing inter-process communication, excluding those performing the core application tasks.

Given that the HPC's µP typically provides between 2 and 16 cores, only a limited number of threads can be processed in parallel. In POSIX-like operating systems, threads become the currency for concurrency, meaning that when the thread count far exceeds available cores, the system must rely on context switching. With context switching times estimated between 2µs and 4.5µs [#f1]_ [#f2]_ [#f3]_, even a 100ms time slice could spend between 3% and 10% of its duration on context switching alone - assuming each thread is scheduled once. This overhead increases dramatically if threads are forced to switch more frequently due to competition for processing time.

Furthermore, reducing context switching overhead not only improves raw performance but also enhances overall safety and reliability. By minimizing the number of context switches, the CPU can devote more time to executing critical application logic and monitoring system health, thereby reducing the risk of timing violations in safety-critical functions. This reduction in overhead also minimizes the likelihood of cascading delays and resource starvation, which bolsters system resilience and ensures predictable, real-time execution for safety-critical tasks.


Motivation: Enabling a User-Friendly and Deterministic Interface for Concurrent Programs
-----------------------------------------------------------------------------------------

Concurrent programming in our target environment spans multiple scopes. At one level, concurrency exists within the algorithms of individual applications or system services, while at another level, multiple applications must execute concurrently across the platform. The challenge is to offer an interface that is not only simple and expressive but also deterministic and reliable - an important requirement in safety-critical systems.

Traditional thread-based concurrency in POSIX-like environments introduces complexities such as deadlocks, livelocks, and starvation. These issues, coupled with the inherent difficulties in debugging and validating thread-based systems, can compromise both performance and reliability. [#f4]_ [#f5]_ [#f6]_ Moreover, current designs often separate the management of timing requirements, monitoring, and error handling from the control flow. Integrating these aspects closer to the application logic would promote higher cohesion and lower coupling, enabling more effective debugging and validation, particularly when addressing application-specific scenarios.


Motivation: Managing Reliable Integrations in Mixed-Criticality Environments
-----------------------------------------------------------------------------

The broader objective of the HPC platform is to support the concurrent integration and maintenance of multiple applications, potentially sourced from different vendors. Unlike traditional microcontroller (µC) platforms that are statically configured, this platform must allow dynamic updates, upgrades, and new deployments throughout the vehicle's lifecycle. This introduces significant complexity in managing concurrency, particularly in mixed-criticality environments where applications of varying criticality levels must coexist without interference.

Currently, application developers are expected to manage runtime scheduling directly via the operating system, controlling thread lifecycles, priorities, and affinities. Such an approach ties the configuration too closely to a specific deployment scenario and often leads to discrepancies between behaviors observed during development and those on the target system. This misalignment complicates integration efforts, as integrators must repeatedly iterate with the application developer to meet the system's reliability requirements. An orchestrator that abstracts these complexities could alleviate these challenges by offering a uniform, deterministic interface for managing runtime scheduling, thus ensuring that lower-criticality applications do not adversely affect the performance or reliability of higher-criticality ones.


.. Rationale
.. ==========


Specification
=============

Now that we know the motivation behind the feature request, let's dive deeper into the proposed solution for the problem statements described above.


Specification: How to increase performance in a highly concurrent system?
--------------------------------------------------------------------------

To address the performance challenges described in the motivation - where an excessive number of threads leads to significant context-switch overhead - the proposed solution is to adopt user-level scheduling through cooperative multi-tasking. This approach minimizes overhead by reusing existing threads within a process instead of creating one thread per session or task within a service or application component. By handling task switching at the user level, the system avoids the costly transition between user space and kernel space, reducing the typical context switch cost from the microsecond to the nanosecond range. [#s1]_ [#s2]_ [#s3]_ [#s4]_

The proposed solution provides a framework where tasks, rather than threads, serve as the fundamental unit of concurrency. In this model, concurrent tasks can share the same OS thread, thereby significantly reducing the number of threads and the associated context-switch overhead. To enable parallelism for concurrent tasks, the solution will implement a configurable thread pool. In the target application of the framework, additional thread pools will only be introduced when necessary - for instance, in cases where application tasks differ in criticality or are separated by process boundaries. This reuse of threads not only minimizes the performance penalty associated with managing a vast number of threads but also simplifies resource allocation and scheduling in the final target scenario.

The solution includes the following key functionalities:
   - User-level scheduling to efficiently handle task switches in the nanosecond range.
   - Cooperative multi-tasking, allowing multiple concurrent tasks to use the same OS thread.
   - Provision of a configurable thread pool to enable parallelism for concurrent tasks.
   - Introduction of additional thread pools only when necessary, such as when tasks differ in criticality or require separation by process boundaries.

.. admonition:: Related Requirements

   - :need:`feat_req__orchestration__user_level`
   - :need:`feat_req__orchestration__cooperative_multi`
   - :need:`feat_req__orchestration__configurable_thread`


.. _how_to_enable_a_user_friendly_deterministic_interface_for_concurrent_programs:

Specification: How to enable a user-friendly & deterministic interface for concurrent programs?
------------------------------------------------------------------------------------------------

To harness the benefits of user-space multi-tasking while still providing a user-friendly and deterministic interface for concurrent programs, this proposal advocates for a nested task-based programming framework. The choice for a nested structure over a graph-based one is driven by the need to design reliable programs and enable straightforward control flow analysis - a requirement that becomes critical during safety inspections. Although graph-based structures may have a gentler learning curve and offer rapid initial results, they often become limiting when more complex scheduling descriptions are needed, such as conditional branching, time monitoring, and error handling paths.

The envisioned programming framework will be:
   - Free from explicit thread management.
   - Free from complex synchronization mechanisms.
   - Capable of expressing both concurrent and sequential dependencies.
   - Capable of expressing conditional branching within the program.
   - Capable of expressing timing constraints and error handling paths directly within the program.
   - Expressive, transparent, and deterministic to facilitate straightforward control-flow analysis.

.. admonition:: Related Requirements

   - :need:`feat_req__orchestration__deterministic_and`
   - :need:`feat_req__orchestration__configurable_error`


.. _how_to_manage_reliable_integrations_in_mixed_criticality_environments:

Specification: How to manage reliable integrations in mixed-criticality environments?
--------------------------------------------------------------------------------------

To address the challenge of integrating applications developed by distributed teams - each with only a partial view of the final target system - the solution must decouple algorithm design from deployment details. Application developers should be able to define algorithms that can exploit parallel execution when processing resources are available without binding their implementations to a specific deployment scenario.

This can be achieved by leveraging the proposed programming framework to express application structures without direct dependence on kernel threads. Integrators would then define a shared thread pool that executes the routines of these programs via cooperative multi-tasking. This design allows integrators to manage the number, affinity, and priorities of threads in the pool, providing full control over system resources. Consequently, integrators can assign computing resources during deployment without the need for iterative fine-tuning with each application developer.

Additionally, the system will use priority-based preemption between thread pools to ensure that lower-priority programs cannot interfere with higher-priority ones. Error handling is managed independently of the application's normal execution paths, with misbehaving code preemptively handled to maintain overall system stability. This mechanism empowers developers to build robust safety mechanisms on top of the orchestration feature.

In summary, to manage reliable integrations in mixed-criticality environments, the orchestration feature must:
   - Provide a resource-independent definition of algorithm design.
   - Allow the assignment of computing resources during integration and deployment.
   - Utilize preemptive prioritization between criticalities along with robust error handling.
   - Offer tracing and profiling of program execution to verify the behavior and control flow of the final integrated system.

.. admonition:: Related Requirements

   - :need:`feat_req__orchestration__resource`
   - :need:`feat_req__orchestration__tracing_and`
   - :need:`feat_req__orchestration__priority_based`


.. Backwards Compatibility
.. =======================


Security Impact
===============

.. note::

   This section does not replace a formal security impact analysis. This only guides the design thoughts behind security related topics and is to be understood as a starting point for later workflows.

The design of this orchestration feature is based on the assumption that all code executing within a process is trusted. Consequently, the attack surface within a single process is inherently minimized, as the task isolation provided by threads is secure due to the fact that threads cannot be accessed from outside the process.

A potential attack surface arises from the synchronization between tasks or threads that belong to different processes. To mitigate this risk, the feature request mandates the exclusive use of the :ref:`ipc_feature` for any inter-process synchronization. This communication feature has been previously evaluated with regard to its security impact on synchronization primitives and is considered secure. No alternative forms of exchange or synchronization between processes are permitted for this feature.

By adhering to this design, the orchestration feature maintains a robust security posture, ensuring that inter-process communication is managed in a controlled and secure manner.

.. admonition:: Related Requirements

   - :need:`feat_req__orchestration__trusted_intra`
   - :need:`feat_req__orchestration__exclusive_use_of_ipc`


Safety Impact
=============

.. note::

   This section does not replace a formal safety impact analysis. This only guides the design thoughts behind safety related topics and is to be understood as a starting point for later workflows.

The orchestration feature is designed under the assumption that all tasks within a single process share the same ASIL level. As a result, the internal task management must not mix different safety levels. In the section :ref:`how_to_enable_a_user_friendly_deterministic_interface_for_concurrent_programs`, the capability to define robust error handling mechanisms is described. These mechanisms are intended to serve as integral safety elements within an application's safety concept. Consequently, the feature must ensure that if error handling mechanisms are present, they are isolated from the effects of misbehaving tasks (for example, in the worst-case scenario where all threads in the pool become occupied by tasks in an infinite loop). This functionality shall be implemented in a configurable manner, recognizing that not all applications require safety mechanisms to be defined through the orchestration feature, and that ensuring guaranteed reactivity typically incurs a cost.

In addition, the orchestration feature must expose hooks for external supervision of its safety mechanisms. These hooks enable integration with an external watchdog, while the feature itself will not directly connect to a watchdog, thereby preserving platform maintainability.

Finally, for mixed-criticality deployments - as discussed in :ref:`how_to_manage_reliable_integrations_in_mixed_criticality_environments` - the feature shall enforce that all tasks within a thread pool (or process) have the same criticality level. Lower-criticality tasks must not influence the timing behavior of higher-criticality tasks. This is achieved by leveraging the OS's preemptive scheduling between thread pools, and by managing inter-process synchronization exclusively via the :ref:`ipc_feature`, which is already validated for this purpose.

The solution includes the following key safety functionalities:
   - All tasks within a process must share the same ASIL level.
   - Integrated, configurable error handling mechanisms that are insulated from misbehaving tasks.
   - Exposure of hooks for external supervision (e.g., integration with a watchdog), without direct coupling to the watchdog.
   - Enforcement of homogeneous criticality within thread pools to prevent lower-criticality tasks from affecting higher-criticality tasks.
   - Exclusive use of the :ref:`ipc_feature` for inter-process synchronization to uphold criticality boundaries.

.. admonition:: Related Requirements

   - :need:`feat_req__orchestration__homogeneous_asil`
   - :need:`feat_req__orchestration__configurable_error`
   - :need:`feat_req__orchestration__external_supervision`
   - :need:`feat_req__orchestration__enforcement_of`
   - :need:`feat_req__orchestration__priority_based`
   - :need:`feat_req__orchestration__exclusive_use_of_ipc`


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
      A unit of work or a logical operation scheduled for execution by the orchestration framework. Tasks represent the individual functions or routines within an application that can be managed independently of the underlying thread.

   thread
      The smallest sequence of programmed instructions that can be managed independently by an operating system. Threads share a process's resources, such as memory, and are scheduled by the operating system or by user-level schedulers.

   concurrent
      The ability of a system to manage multiple tasks over overlapping time periods. Concurrency does not necessarily mean that tasks are executed simultaneously, but rather that progress can be made on more than one task during the same time interval.

   parallel
      The simultaneous execution of multiple tasks on different processing units, such as CPU cores. Parallelism is a subset of concurrency and is used to speed up processing by dividing tasks among available hardware resources.

   cooperative
      A scheduling model in which tasks voluntarily yield control to enable other tasks to execute. In cooperative multitasking, task switching occurs at well-defined points, reducing the overhead of context switching and simplifying the management of shared resources.


.. _footnotes:

Footnotes
=========

.. [#f1] Paul Turner, "User-level threads....... with threads", YouTube, https://www.youtube.com/watch?v=KXuZi9aeGTw.
.. [#f2] "Measuring context switching and memory overheads for Linux threads", Eli the Green Place, https://eli.thegreenplace.net/2018/measuring-context-switching-and-memory-overheads-for-linux-threads.
.. [#f3] "QNX® Neutrino® Realtime OS: Kernel Benchmark Results", QNX Support, https://support7.qnx.com/download/download/19099/qnx_freescale_i-mx31-ads_final.pdf.
.. [#f4] "Determinism Is Not Enough: Making Parallel Programs Reliable with Stable Multithreading", Columbia University, https://www.cs.columbia.edu/~junfeng/papers/smt-cacm.pdf.
.. [#f5] "Design of an Empirical Study for Comparing the Usability of Concurrent Programming Languages", CiteSeerX, https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=011212ec94ae9497f96e2a27f4f823722cb84a2f.
.. [#f6] "Taskflow: A Lightweight Parallel and Heterogeneous Task Graph Computing System", Taskflow Paper, https://tsung-wei-huang.github.io/papers/tpds21-taskflow.pdf.

.. [#s1] "Asynchronous Programming in Rust", The Rust Async Book, https://rust-lang.github.io/async-book/part-guide/concurrency.html.
.. [#s2] "Skyloft: A General High-Efficient Scheduling Framework in User Space", ACM Digital Library, https://dl.acm.org/doi/pdf/10.1145/3694715.3695973.
.. [#s3] "Cooperative Scheduling of Parallel Tasks with General Synchronization Patterns", Semantic Scholar, https://pdfs.semanticscholar.org/ef9f/7fa173808fd0a4a21f318fc2c9890ccd9e5a.pdf.
.. [#s4] "Scheduler Activations: Effective Kernel Support for the User-Level Management of Parallelism", ACM Digital Library, https://dl.acm.org/doi/pdf/10.1145/146941.146944.
