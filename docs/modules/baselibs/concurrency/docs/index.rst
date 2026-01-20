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

concurrency
###########

.. document:: Concurrency Library
   :id: doc__concurrency
   :status: draft
   :safety: ASIL_B
   :tags: baselibs_concurrency
   :realizes: wp__cmpt_request
   :security: YES

.. toctree::
   :hidden:

   architecture/index.rst

Abstract
========

This component request proposes a concurrency library that provides abstractions for managing concurrent tasks, threads, and synchronization mechanisms.

Motivation and Rationale
========================

The concurrency library shall provide safe and efficient way to handle concurrent operations. It aims to simplify the development of multi-threaded applications by offering high-level abstractions for task management, synchronization, and inter-thread communication.
The library is designed to improve code readability, maintainability, and portability across different platforms.
