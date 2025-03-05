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

Orchestration
=============

.. document:: Orchestration
   :id: DOC__Orchestration
   :status: draft
   :safety: ASIL_B
   :tags: feature_request

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_Orchestration``

Abstract
========
In the domain of multi-core and multi-threaded programming, traditional approaches often face challenges such as race conditions, deadlocks, and inefficient resource utilization. 
These issues arise due to the complexity of manually managing threads and their interactions with shared resources. Typical failures in multi-threaded programming:

- Dead-Locks: Two threads mutually wait for resources of the respective other thread. No progress is made, the termination criteria for the threads is violated.
- Live-Locks: Two threads mutually aquire and release resources of the respective other thread. The threads are in a busy mode, but no progress is made, the termination criteria for the threads is violated.
- Starvation: A thread is not or rarely able to acquire the resources it needs to make progress because other threads are always ahead in acquiring the resource. The thread starves and does not progress as required.

Task-based parallel programming, particularly when combined with an orchestrator, offers a more robust solution by abstracting low-level thread management and enabling better resource allocation. 
Unlike conventional multi-threaded programming, which relies on the programmer to handle synchronization, task dependencies, and scheduling, task-based systems allow the orchestrator to distribute work across available cores, 
balancing the load dynamically. This approach not only minimizes the risks of common concurrency issues, but also improves scalability, fault tolerance, and ease of development. 
As a result, task-based parallel programming with an orchestrator is a superior choice for efficiently leveraging the full potential of modern multi-core processors, offering a more 
scalable, maintainable, and high-performance solution compared to traditional multi-threading models. 
Furthermore, task orchestration inherently supports mixed-criticality tasks, by leveraging real-time scheduling policies, fault tolerance mechanisms, and priority-aware execution. 
This ensures that safety-critical tasks meet stringent timing and correctness requirements.


Glossary
========
- Task: A task is a light weight, self-contained unit that can be executed independently. Tasks are typically smaller and more numerous than threads, but rather than being managed by the OS scheduler, they are managed by the orchestrator.
- Concurrent: Concurrent execution refers to the execution of multiple tasks in an overlapping time period. These tasks may not necessarily be executing simultaneously; rather, they are being managed in such a way that they appear to progress together.
- Parallel: Parallel execution refers to the simultaneous execution of multiple tasks or operations, usually across multiple processors or cores. In parallel execution, tasks are literally running at the same time, not just interleaved.


Motivation
==========

a) Decoupling application design from deployment
------------------------------------------------
In task-based programming, decoupling application design from deployment is important because it allows the program to be more flexible, scalable, and maintainable. 
The main idea is that the application logic (the tasks and their interactions) should be designed independently from how and where those tasks are executed in the actual deployment environment. 
This decoupling offers several significant advantages such as:

   i) Flexibility in Resource Allocation:
      Decoupling allows the task execution logic to be independent of the specific resources (e.g., threads, processing units, or cores) available at runtime. The application defines the tasks and their dependencies, but the underlying system or orchestrator can decide how to allocate resources (e.g., distributing tasks across different threads, cores, or processing units). This flexibility ensures that the application can efficiently adapt to different hardware configurations or deployment environments without changing its core logic.
   ii) Improved Scalability:
      By decoupling the design of the application from its deployment, the application can scale more easily. For instance, if the load increases, the task orchestrator can scale the number of resources (e.g., threads, cores, or processing units) without needing to rewrite or redesign the application code.  This also leads to efficient utilization of resources by consolidating multiple applications/programs within one thread pool.

b) Getting concurrent code right is hard
----------------------------------------
The emergence of multicore hardware and the growing computational demands have rendered parallel programming essential in modern software development. Getting concurrent code right is difficult because it involves managing and coordinating multiple threads, each of which might execute at unpredictable times and interact with shared resources. The challenges include:

- Race conditions and non-determinism
- Deadlocks and livelocks
- Synchronization and thread management overhead
- Difficulties in testing, debugging, and ensuring correctness in a multi-threaded environment

Effective concurrent programming requires a deep understanding of thread synchronization, resource management, and system-level behavior.

c) Striving for optimal performance and efficiency
--------------------------------------------------
Local optimizations within individual applications may not always result in optimal performance and efficiency. The orchestration enables the integrator to configure the system to:

- Balance the load to utilize resources effectively
- Manage task dependencies to maximize parallelism while ensuring correct execution order
- Assign task to appropriate computational resources

d) Streamlining heterogeneous computing
---------------------------------------
The growing demands for artificial intelligence, large data processing, and energy efficiency are encouraging the industry to adopt heterogeneous computing architectures. However, developing applications that leverage such architectures can be complex and may result in non-portable code. The applications usually utilize these heterogeneous computes within their algorithms and therefore have a need for synchronization/coordination of CPU and non CPU tasks. This also leads to the requirement to be able to profile and configure the access to the these shared compute devices in order to resolve competing access to this shared resource (from the integrator point of view).

e) Facilitating a holistic system analysis/tracing
--------------------------------------------------
Obtaing data to gain insight into dynamic behavior of multi-threaded applications is crucial because it helps to:

- Optimize performance by identifying bottlenecks and inefficiencies
- Gain insights into thread scheduling and improve load balancing
- Validate deterministic execution

The orchestrator can facilitate the provision of this data as it coordinates the execution of tasks and threads.


Rationale
=========
TBD.
[Describe why particular design decisions were made.]

   .. note::
      The rationale should provide evidence of consensus within the community and discuss important objections or concerns raised during discussion.

Specification
=============

- The feature shall support a task-based parallel programming model.
   Rationale:  To abstract the complexities of thread management and enable developers to focus on defining the tasks that need to be executed, rather than managing how these tasks are distributed across threads and processing units.

- The feature shall support configuration of executor behavior, called as Program i.e. grouping of tasks and defining dependencies between tasks or execution order such as sequential/concurrent/conditional/loop.
   Rationale: Managing task dependencies is essential to avoid race conditions and ensure the correct execution order. We define essential flow control constructs:

   i) Sequential: For sequential execution of tasks
   ii) Concurrent: For concurrent execution of tasks 
   iii) Branches: For condition and state based execution of tasks
   iv) Loop: For repeated exectution of flow control
   v) Exceptions: Raise and capture deterministic exceptions to branch the control flow upon the occurence of error conditions.

- The feature shall support an Executor or Execution Engine with thread pool to dynamically schedule tasks of Program(s) on available processing units based on predefined strategy (e.g., system load, resource availability and computation characteristics).
   Rationale: Dynamic resource allocation maximizes system utilization and efficiency.

- The feature shall support synchronization of tasks intra-process, inter-process and inter-processing units.
   Rationale: Without proper synchronization, tasks may lead to race conditions or data corruption when accessing shared resources. Managing resource contention ensures safe and correct interactions between tasks, avoiding concurrency bugs such as deadlock, livelock, starvation and improving system stability.

- The feature shall support high resolution timers for time controlled task execution.
   Rationale: Time triggered one-shot/cyclic execution of tasks and timeout conditions.
 
- The feature shall support runtime error handling.
   Rationale: Handling of runtime errors such as error conditions raised by tasks, communication errors, task deployment errors etc.

- The feature shall support cancellation of task.
   Rationale: In real-world applications, tasks may need to be stopped before completion due to error or real-time constraints. Task cancellation ensures that resources are not wasted on unnecessary work, and system efficiency is maintained.

- The feature shall support heterogeneous architecture.
   Rationale: To leverage the computational power of heterogeneous architecture for artificial intelligence, large data processing, and energy efficiency.

- The feature shall support monitoring of tasks execution for deadline and error conditions.
   Rationale: Monitoring for deadline and error conditions is crucial for ensuring correctness and responsive system.

- The feature shall provide data for profiling control flow, etc.
   Rationale: Obtaing data to gain insight into dynamic behavior of multi-threaded applications is crucial because it helps to:

   i) Optimize performance by identifying bottlenecks and inefficiencies
   ii) Gain insights into thread scheduling and improve load balancing
   iii) Validate deterministic execution

- The feature shall support task prioritization and real-time scheduling policies.
   Rationale: Certain tasks may require higher priority due to urgency or dependencies, and an effective scheduling mechanism ensures that critical tasks are completed first, leading to better system responsiveness and efficiency.

- The feature shall support deployment configuration of runtime resources such as CPU, threads, etc.
   Rationale: The ability to configure resources allows applications to adapt to varying hardware environments, from multi-core to heterogeneous architecture, improving scalability and flexibility.

- The feature shall be compatible with any POSIX-compliant operating system.
   Rationale: Portability across various operating systems.

- The feature shall support C++ and Rust applications.
   Rationale: Re-use of existing applications and development of new applications in appropriate language.


Backwards Compatibility
=======================

Not applicable.


Security Impact
===============

No impact on security.


Safety Impact
=============

Integrator shall not mix tasks of different safety levels in one OS Process.


License Impact
==============

TBD


How to Teach This
=================

TBD


References
==========
a) Taskflow: A Lightweight Parallel and Heterogeneous Task Graph Computing System
https://tsung-wei-huang.github.io/papers/tpds21-taskflow.pdf

b) Determinism Is Not Enough: Making Parallel Programs Reliable with Stable Multithreading
https://www.cs.columbia.edu/~junfeng/papers/smt-cacm.pdf
