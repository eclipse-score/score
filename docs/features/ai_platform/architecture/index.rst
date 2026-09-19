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

.. document:: AI-Platform Architecture
   :id: doc__ai_platform_architecture
   :status: draft
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__feature_arch[version==1]

.. feat:: AI-Platform
   :id: feat__ai_platform
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1


Interfaces
----------

**Inference**

The inference interface is the application-facing entry point of the AI Platform.
It is intentionally narrow: it exposes the common denominator of the supported backends and omits vendor-specific
options, accelerator selection and memory placement, which remain platform-internal.

.. logic_arc_int:: Inference Interface
   :id: logic_arc_int__ai_platform__inference_if
   :included_by: feat__ai_platform
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :fulfils: feat_req__ai_platform__workloads_execution[version==1], feat_req__ai_platform__static_backend[version==1], feat_req__ai_platform__safety_backends[version==1]

   .. needarch::
      :scale: 50
      :align: center

      {{ draw_interface(need(), needs) }}

.. logic_arc_int_op:: load
   :id: logic_arc_int_op__ai_platform__load
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__ai_platform__inference_if

   Resolves a model by identity and version constraint and returns a model handle.
   Input and output descriptors are fixed once the model is loaded.

.. logic_arc_int_op:: describe
   :id: logic_arc_int_op__ai_platform__describe
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__ai_platform__inference_if

   Returns the input and output descriptors of a loaded model, consisting of name, data type, shape and layout.

.. logic_arc_int_op:: invoke
   :id: logic_arc_int_op__ai_platform__invoke
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__ai_platform__inference_if

   Executes a loaded model synchronously within a given deadline.
   Exceeding the deadline is reported as an error instead of blocking the caller indefinitely.

.. logic_arc_int_op:: invoke_async
   :id: logic_arc_int_op__ai_platform__invoke_async
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__ai_platform__inference_if

   Starts an execution and returns a handle that allows waiting for completion.

.. logic_arc_int_op:: cancel
   :id: logic_arc_int_op__ai_platform__cancel
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__ai_platform__inference_if

   Requests termination of a pending asynchronous execution and releases its resources.

.. logic_arc_int_op:: unload
   :id: logic_arc_int_op__ai_platform__unload
   :security: NO
   :safety: ASIL_B
   :status: valid
   :version: 1
   :included_by: logic_arc_int__ai_platform__inference_if

   Releases a model handle and the resources associated with it.


Interface Sketch
----------------

The following sketch illustrates the interface from an application perspective.
It is illustrative and does not fix the final signatures.

.. code-block:: cpp

   namespace score::ai {

   // Describes one input or output of a model. Shapes are fixed after Load.
   struct TensorDesc {
     std::string_view name;
     DataType type;             // e.g. Float32, Float16, Int8, UInt8
     std::span<const int64_t> shape;
     Layout layout;             // e.g. NCHW, NHWC, Linear
   };

   // Opaque handle to a platform-managed buffer. Allows zero-copy for data that
   // already resides in accelerator memory (e.g. camera output).
   class Buffer;

   class Model {
    public:
     std::span<const TensorDesc> Inputs() const;
     std::span<const TensorDesc> Outputs() const;

     Result<void> Invoke(std::span<const Buffer> inputs,
                         std::span<Buffer> outputs,
                         Deadline deadline);

     Result<Execution> InvokeAsync(std::span<const Buffer> inputs,
                                   std::span<Buffer> outputs,
                                   Deadline deadline);
   };

   // Resolves a model by identity and version constraint; the platform selects the
   // backend and the accelerator.
   Result<Model> Load(ModelId id, VersionConstraint constraint);

   }  // namespace score::ai

Properties implied by this interface:

- **Identity instead of paths**: applications reference a model by identity and version constraint, so model artifacts
  can be updated, signed and rolled back without changing the application.
- **Fixed shapes after load**: descriptors are known after loading, which allows buffer allocation and timing analysis
  before the first execution.
- **Explicit deadlines**: every execution carries a deadline, so a missed deadline is a defined, reportable error.
- **Buffer handles instead of pointers**: data may stay in accelerator memory, which keeps zero-copy paths possible
  without exposing the memory model to the application.
- **No backend in the signature**: the selected runtime (e.g. ONNX Runtime, TensorRT, QNN) is a deployment decision and
  does not appear in application code.
