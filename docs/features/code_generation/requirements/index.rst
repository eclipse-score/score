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

.. _codegen_requirements:

Requirements
============

.. feat_req:: The system uses a human-readable definition language.
   :id: feat_req__code_generation__definitionlanguage
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__dev_experience__idl_support
   :status: valid

   The system shall be modeled in YAML-syntax files. This means the system should
   use YAML due to the availability of parsers in Rust and C++. The
   system should prefer YAML over JSON due to its simpler syntax.

.. feat_req:: Software Compute Units signal initialization failures by returning an Error indicating failure.
   :id: feat_req__code_generation__initialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Software Compute Unit Instances shall be considered to have failed
   permanently if they fail to initialize.

.. feat_req:: Software Compute Units correctly deallocate any dynamically allocated memory in the onShutdown function.
   :id: feat_req__code_generation__deinitialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Software Compute Unit instances shall have onInit and onShutdown
   called only once during their lifecycle.

.. feat_req:: Software Compute Units do not spawn a variable number of threads.
   :id: feat_req__code_generation__nomultithreading
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Software Compute Units shall have a predetermined number of threads
   if they spawn any threads at all. Software Compute Units shall not
   dynamically spawn and join or detach worker threads.

.. feat_req:: Software Compute Units do not throw exceptions or "panic".
   :id: feat_req__code_generation__error_handling1
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Software Compute Units shall handle any exceptions in dependency
   libraries completely inside the standard interface functions. Software Compute Units shall signal an error by returning an Error that contains an ErrorCode other than Success. Software Compute Units shall terminate execution if unhandled exceptions occur.

.. feat_req:: Software Compute Units do not attempt to trigger program termination.
   :id: feat_req__code_generation__error_handling2
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__execution_model__processes
   :status: valid

   Software Compute Units shall return an Error with a suitable
   Errorcode and follow the defined error propagation mechanism to
   handle errors. Software Compute Units shall not manage their own
   lifecycle.

.. feat_req:: Software Compute Units do not call their own standard interface methods.
   :id: feat_req__code_generation__error_handling3
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__runtime_determinism
   :status: valid

   Software Compute Units shall not interfere with their external
   lifecycle management by calling their own interface methods
   (onInit, onUpdate, onReset, onShutdown). Software Compute Units may
   call onReset() from onShutdown() if required for avoiding code
   duplication.

.. feat_req:: Software Compute Units implement transient error recovery mechanisms in onReset.
   :id: feat_req__code_generation__error_handling4
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__runtime_determinism
   :status: valid

   Software Compute Units shall signal transient errors as a failure of
   onUpdate. The responsible Software Compute Unit shall trigger
   onReset to recover from transient errors based on logic modeled for
   the Archetype.

.. feat_req:: Software Compute Units signal reset and recovery failures via the Error return value of onReset.
   :id: feat_req__code_generation__error_handling5
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__runtime_determinism
   :status: valid

   Software Compute Units shall be considered to have failed permanently if they return a failure on onReset.
