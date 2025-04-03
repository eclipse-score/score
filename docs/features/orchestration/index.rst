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


.. document:: Orchestration
   :id: doc__orchestration
   :status: valid
   :safety: ASIL_B
   :tags: contribution_request, feature_request

Orchestration
=============

Motivation
----------

The rapid evolution of high-performance computing (HPC) architectures and the increased availability of multi-core processors in centralized E/E systems have driven the need for a platform capable of hosting advanced ADAS/AD applications while upintegrating existing ECU functionalities. This approach facilitates the deployment of loosely coupled applications that support flexible maintenance and updates, with the goal of hosting between 100 and 150 individual applications.

Increasing Performance in a Highly Concurrent System
******************************************************

In existing platforms for microprocessors (µP), each application is expected to interact with approximately 15 system services or daemons - such as ``ara::diag`` for diagnostics and ``ara::com`` for SOME/IP communication. Under a straightforward implementation, this interaction model results in the creation of around 15 threads per application. When scaled to 100-150 applications, this amounts to roughly 1500 to 2250 threads solely managing inter-process communication, excluding those performing the core application tasks.

Given that the HPC's µP typically provides between 2 and 16 cores, only a limited number of threads can be processed in parallel. In POSIX-like operating systems, threads become the currency for concurrency, meaning that when the thread count far exceeds available cores, the system must rely on context switching. With context switching times estimated between 2µs and 4.5µs [#f1]_ [#f2]_ [#f3]_, even a 100ms time slice could spend between 3% and 10% of its duration on context switching alone - assuming each thread is scheduled once. This overhead increases dramatically if threads are forced to switch more frequently due to competition for processing time.

Enabling a User-Friendly and Deterministic Interface for Concurrent Programs
*****************************************************************************

Concurrent programming in our target environment spans multiple scopes. At one level, concurrency exists within the algorithms of individual applications or system services, while at another level, multiple applications must execute concurrently across the platform. The challenge is to offer an interface that is not only simple and expressive but also deterministic and reliable - a critical requirement in safety-critical systems.

Traditional thread-based concurrency in POSIX-like environments introduces complexities such as deadlocks, livelocks, and starvation. These issues, coupled with the inherent difficulties in debugging and validating thread-based systems, can compromise both performance and reliability [#f4]_ [#f5]_ [#f6]_. Moreover, current designs often separate the management of timing requirements, monitoring, and error handling from the control flow. Integrating these aspects closer to the application logic would promote higher cohesion and lower coupling, enabling more effective debugging and validation, particularly when addressing application-specific scenarios.

Managing Reliable Integrations in Mixed-Criticality Environments
*****************************************************************

The broader objective of the HPC platform is to support the concurrent integration and maintenance of multiple applications, potentially sourced from different vendors. Unlike traditional microcontroller (µC) platforms that are statically configured, this platform must allow dynamic updates, upgrades, and new deployments throughout the vehicle's lifecycle. This introduces significant complexity in managing concurrency, particularly in mixed-criticality environments where applications of varying criticality levels must coexist without interference.

Currently, application developers are expected to manage runtime scheduling directly via the operating system, controlling thread lifecycles, priorities, and affinities. Such an approach ties the configuration too closely to a specific deployment scenario and often leads to discrepancies between behaviors observed during development and those on the target system. This misalignment complicates integration efforts, as integrators must repeatedly iterate with the application developer to meet the system's reliability requirements. An orchestrator that abstracts these complexities could alleviate these challenges by offering a uniform, deterministic interface for managing runtime scheduling, thus ensuring that lower-criticality applications do not adversely affect the performance or reliability of higher-criticality ones.

Specification
-------------

Now that we know the motivation behind the feature request, let's dive deeper into the proposed solution for the problem statements described above.

How to increase performance in a highly concurrent system?
***********************************************************

An approach to avoid unnecessary thread context switching - and therefore more effectively utilize existing system resources - is to employ user-level scheduling, commonly known as cooperative multi-tasking. The key benefit is that task switching in this model is significantly cheaper than traditional thread context switching, costing roughly ~30ns instead of ~2-4µs. This efficiency is achieved because control does not need to be handed off to the operating system, there is less data to swap (no registers or caches are switched), and the memory overhead is lower since tasks can share the same stack [#s1]_ [#s2]_ [#s3]_ [#s4]_.

How to enable a user-friendly & deterministic interface for concurrent programs?
*********************************************************************************

To harness the benefits of user-space multi-tasking while still providing a user-friendly and deterministic interface for concurrent programs, this proposal advocates for a nested task-based programming framework. The choice for a nested structure over a graph-based one is driven by the need to design reliable programs and enable straightforward control flow analysis - a requirement that becomes critical during safety inspections. Although graph-based structures may have a gentler learning curve and offer rapid initial results, they often become limiting when more complex scheduling descriptions are needed, such as conditional branching, time monitoring, and error handling paths.

The envisioned programming framework will be:
   - Free from explicit thread management.
   - Free from complex synchronization mechanisms.
   - Capable of expressing both concurrent and sequential dependencies.
   - Capable of expressing timing constraints and error handling paths directly within the program.
   - Expressive, transparent, and deterministic to facilitate straightforward control-flow analysis.

How to manage reliable integrations in mixed-criticality environments?
************************************************************************

To address the challenge of integrating applications developed by distributed teams - each with only a partial view of the final target system - the solution must decouple algorithm design from deployment details. Application developers should be able to define algorithms that can exploit parallel execution when processing resources are available without binding their implementations to a specific deployment scenario.

This can be achieved by leveraging the proposed programming framework to express application structures without direct dependence on kernel threads. Integrators would then define a shared thread pool that executes the routines of these programs via cooperative multi-tasking. This design allows integrators to manage the number, affinity, and priorities of threads in the pool, providing full control over system resources. Consequently, integrators can assign computing resources during deployment without the need for iterative fine-tuning with each application developer.

Additionally, the system will use priority-based preemption between thread pools to ensure that lower-priority programs cannot interfere with higher-priority ones. Error handling is managed independently of the application's normal execution paths, with misbehaving code preemptively handled to maintain overall system stability. This mechanism empowers developers to build robust safety mechanisms on top of the orchestration feature.

In summary, to manage reliable integrations in mixed-criticality environments, the orchestration feature must:
   - Provide a resource-independent definition of algorithm design.
   - Allow the assignment of computing resources during integration and deployment.
   - Utilize preemptive prioritization between criticalities along with robust error handling.
   - Offer tracing and profiling of program execution to verify the behavior and control flow of the final integrated system.


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
