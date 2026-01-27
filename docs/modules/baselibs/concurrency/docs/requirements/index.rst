
..
   # *******************************************************************************
   # Copyright (c) 2026 Contributors to the Eclipse Foundation
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

Requirements
############

.. document:: Concurrency Requirements
   :id: doc__concurrency_requirements
   :status: draft
   :safety: ASIL_B
   :security: YES
   :realizes: wp__requirements_comp
   :tags: requirements, concurrency

Functional Requirements
=======================

.. comp_req:: Task Abstraction Interface
   :id: comp_req__concurrency__task_interface
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide interface that wraps callable objects for asynchronous execution, accepting a stop_token for cooperative cancellation and supporting move semantics.

.. comp_req:: Simple Task Implementation
   :id: comp_req__concurrency__simple_task
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__core_utilities, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide implementation for executing callable objects without returning results, supporting fire-and-forget asynchronous operations.

.. comp_req:: Task Result Management
   :id: comp_req__concurrency__task_result
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide implementation to access the result of an asynchronously running task or to request aborting the task when the result is no longer needed.

.. comp_req:: Periodic Task Execution
   :id: comp_req__concurrency__periodic_task
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide implementation for executing callable objects at regular intervals with configurable first execution time and period duration.

.. comp_req:: Delayed Task Execution
   :id: comp_req__concurrency__delayed_task
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide implementation for executing callable objects after a specified delay with support for early cancellation.

.. comp_req:: Executor Interface
   :id: comp_req__concurrency__executor_interface
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__consistent_apis
   :status: valid

   The concurrency module shall provide interface defining a common API for task submission operations, graceful shutdown, and maximum concurrency level reporting.

.. comp_req:: Thread Pool Implementation
   :id: comp_req__concurrency__thread_pool
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide implementation that manages submitted tasks in FIFO order with thread-safe queue operations using condition variables for efficient worker thread wake-up.

.. comp_req:: Interruptible Condition Variable
   :id: comp_req__concurrency__condition_variable
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide implementation that allocates a fixed number of threads at construction time and distributes tasks across worker threads with a dynamic task queue.

.. comp_req:: Interruptible Wait Utilities
   :id: comp_req__concurrency__interruptible_wait
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide  utilities offering simplified APIs for sleep operations.

.. comp_req:: Destruction Guard
   :id: comp_req__concurrency__destruction_guard
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide a mechanism to safely detect when an object has been destroyed to prevent accessing it from multiple threads.

.. comp_req:: Notification Mechanism
   :id: comp_req__concurrency__notification
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall allow one thread to notify another thread once, with a timeout option.

.. comp_req:: Synchronized Queue
   :id: comp_req__concurrency__synchronized_queue
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide a thread-safe queue where multiple threads can add items and one thread can remove them, with a maximum size limit and optional waiting.

.. comp_req:: Long-Running Threads Container
   :id: comp_req__concurrency__long_running_threads
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library, feat_req__baselibs__safety
   :status: valid

   The concurrency module shall provide a container for managing long-running threads, allowing addition and removal of threads.

Non-Functional Requirements
===========================

.. comp_req:: Memory Usage Control
   :id: comp_req__concurrency__memory_usage_control
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library
   :status: valid

   The concurrency module shall limit memory usage to prevent uncontrolled resource consumption.

.. comp_req:: Memory Reservation
   :id: comp_req__concurrency__memory_reservation
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library
   :status: valid

   The concurrency module shall allow reserving memory upfront for tasks to ensure predictable resource allocation.

.. comp_req:: Thread Count Reporting
   :id: comp_req__concurrency__thread_count_reporting
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library
   :status: valid

   The concurrency module shall report the maximum number of concurrent threads available for task execution.

.. comp_req:: Operation Timeout Protection
   :id: comp_req__concurrency__operation_timeout
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library
   :status: valid

   The concurrency module shall use timeouts to prevent operations from waiting forever.

.. comp_req:: Future Error Handling
   :id: comp_req__concurrency__error_handling
   :reqtype: Non-Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: feat_req__baselibs__concurrency_library
   :status: valid

   The concurrency module shall use error codes instead of throwing exceptions.

.. needextend:: "__concurrency" in id
   :+tags: concurrency
