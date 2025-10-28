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

.. _decision_record_dd_001_logging:

DR-001-logging: Rust Frontend Logging Interface Design
========================================================

.. dec_rec:: Rust Frontend Logging Interface Design
   :id: dec_rec__logging__001_rust_frontend
   :status: accepted
   :context: S-Core currently provides a C++ logging API. S-Core requires equivalent Rust APIs, but existing Rust logging solutions do not meet S-Core requirements. This decision record determines the approach for Rust logging implementation.
   :decision: Implement a staged approach - Stage 1: Fork log crate (temporary solution). Stage 2: Implement a Custom Rust logging frontend that exposes macros identical to `log`/`tracing`, supports typed message fields, allows optional contextual information, maintains log levels consistent with the `log` crate plus `fatal`, and provides a single, consistent interface for all Rust components on the platform.

   The platform requires a structured, type-safe logging frontend in Rust that is:

   - Compatible with existing `log` and `tracing` macros (`info!`, `warn!`, `error!`, etc.).
   - Capable of retaining typed values for logged messages (int, float, string, bool, etc.).
   - Able to carry optional contextual information (key-value pairs, span-like data).
   - Supporting all standard log levels plus an explicit `fatal` level.

   Several options exist for Rust logging libraries:

   1. **log crate with kv module** — standard facade, typed key-value logging via log::kv.
   2. **Custom logging crate** — implements log/tracing macros, type retention, and context.
   3. **tracing crate** — structured events and spans, async-aware, different macro API.
   4. **slog** — structured, hierarchical logging with typed fields; different macro/API style.
   5. **defmt** — typed, minimal, embedded-focused; different macros and limited context.

   .. list-table:: Comparison of Rust Logging Libraries
      :header-rows: 1
      :widths: 15 15 18 12 15 25

      * - Library
        - Typed Fields
        - Spans / Context
        - Macro/API
        - Performance
        - Suitability for this platform
      * - log + kv
        - via kv
        - flat events only
        - compatible
        - low overhead
        - Good for flat typed events; lacks hierarchy
      * - custom logger
        - full control
        - full control
        - identical macros
        - low overhead
        - Ideal for platform needs; API compatible
      * - tracing
        - native
        - built-in spans
        - compatible
        - moderate
        - Powerful for async/hierarchical logging
      * - slog
        - structured only
        - hierarchical
        - different
        - moderate
        - Structured logging only; macro signature rules are fixed
      * - defmt
        - built-in
        - minimal
        - different
        - very low
        - Embedded/no_std oriented; not ideal for platform-wide

   **Stage 1 (Temporary Solution):** Fork log crate and use as interim measure.

   **Stage 2 (Final Solution):** Implement a Custom Rust logging frontend that:

   - Exposes macros identical to log/tracing (info!, warn!, error!, fatal!).
   - Supports typed message fields for all standard types.
   - Allows optional contextual information (for task or logical grouping).
   - Maintains log levels consistent with the log crate plus fatal.
   - Provides a single, consistent interface for all Rust components on the platform.

   **Architecture drivers for future Stage 2 decision:**

   - **Performance**
   - **Safety**
   - **Usability**
   - **Maintenance cost**
   - **Complexity**

   **Justification:**

   - Keeps developer-facing API familiar and compatible with existing crates.
   - Offers full control over type retention and context without external dependency constraints.
   - Provides a foundation for optional adapters to tracing or slog in the future.
   - Supports context propagation and hierarchical grouping.

   **Consequences:**

   - Requires maintaining custom macros and backend handling.
   - Does not leverage the ecosystem directly (log, tracing, or slog) for runtime behavior.
   - Spans / async context need explicit management if desired; no automatic propagation like tracing.
