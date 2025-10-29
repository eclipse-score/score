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

.. feat_req:: Definition language should be a human-readible format
   :id: feat_req__code_generation__definitionlanguage
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   In our case, the system is modeled in YAML-syntax files that use a
   specific description language. A major advantage of YAML is that it
   is easy to find parser for YAML either in Rust or C++. Advantage of
   YAML over JSON is the easy syntax (no begin and end closure).
   
.. feat_req:: Software Compute Units should signal initialization failures by returning an Error indicating failure.
   :id: feat_req__code_generation__initialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Software Compute Unit Instances that fail to initialize are considered to have
   failed permanently.
   
.. feat_req:: Software Compute Unit are responsible for correct deallocation of any dynamically allocated memory in the onShutdown function.
   :id: feat_req__code_generation__deinitialization
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Developers can assume that onInit and onShutdown will only ever be called once during the lifecycle of a Software Compute Unit Instance.
   
.. feat_req:: Software Compute Units may not spawn a variable number of threads.
   :id: feat_req__code_generation__nomultithreading
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   If Software Compute Units are to spawn any threads at all, which is
   not recommended, Software Compute Units must have a predetermined
   number of threads that are spawned. Software Compute Units may not dynamically
   spawn and join or detach worker threads.
   
.. feat_req:: Software Compute Unit may not throw exceptions or "panic".
   :id: feat_req__code_generation__error_handling1
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Any exceptions in e.g. dependency libraries must be handled
   completely inside the standard interface functions of the
   Software Compute Unit. The only allowed way for a Software Compute Unit to signal an error is
   by returning an Error that contains an
   ErrorCode other than Success. Any unhandled exceptions
   will cause the Software Compute Unit to terminate
   execution.
   
.. feat_req:: Software Compute Units should not attempt to trigger program termination.
   :id: feat_req__code_generation__error_handling2
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Software Compute Unit are not responsible for managing their own
   lifecycle. The correct way to handle errors is to return an Error
   with a suitable Errorcode and to follow the defined error
   propagation mechanism.
   
.. feat_req:: Software Compute Units should not call their own standard interface methods.
   :id: feat_req__code_generation__error_handling3
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Software Compute Units must not interfere with their external
   lifecycle management by calling their own interface methods
   (onInit, onUpdate, onReset, onShutdown) with the exception that
   onShutdown() may call onReset() if this is required for avoiding
   code duplication.
   
.. feat_req:: Software Compute Units should implement transient error recovery mechanisms in onReset.
   :id: feat_req__code_generation__error_handling4
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Software Compute Units should signal transient errors as a failure of
   onUpdate. The triggering of onReset to recovery from transient
   errors should be done by the responsible Software Compute Unit based on logic modeled
   for the Archetype. 
   
.. feat_req:: Software Compute Units should signal reset and recovery failures via the Error return value of onReset.
   :id: feat_req__code_generation__error_handling5
   :reqtype: Functional
   :security: NO
   :safety: ASIL_B
   :satisfies: stkh_req__ai_platform__enablement
   :status: valid

   Software Compute Units that return a failure on onReset are considered to have failed permanently.

   
   
