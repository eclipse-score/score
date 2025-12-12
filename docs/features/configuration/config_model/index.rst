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

.. _feature_template:

Configuration Model
###################

.. note:: Document header

.. document:: Configuration Model
   :id: doc__configuration_model
   :status: draft
   :safety: NO
   :security: NO
   :realizes: wp__feat_request
   :tags: template


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_configuration_model``


Abstract
========

This proposal introduces a unified approach to static module configuration in S-CORE by combining a Configuration Guideline and a Configuration Model. While the guideline defines how configurations should be structured—covering naming conventions, identifier usage, storage formats, and parameter organization—the model specifies what needs to be configured, focusing on common elements that must remain consistent across all modules. The dual approach ensures clarity, predictability, and maintainability, reducing integration complexity and improving user experience. By standardizing both the structure and the content of configurations, the solution enables faster onboarding of new modules, supports future extensions (e.g., JSON or FlatBuffers), and lays the foundation for automated compliance checks.

Motivation
==========

The current configuration landscape in S-CORE suffers from fragmentation: contributors define static configurations independently, leading to inconsistencies in identifiers, variable naming, and file storage. Beyond structural differences, there is no common understanding of what must be configured for each module (e.g. support for "multiple instances"). This results in missing or redundant parameters, unclear dependencies, and unpredictable integration behavior. Without a shared model, cross-module consistency can hardly be guaranteed, making maintenance and scaling difficult. Introducing both a guideline and a model addresses these gaps by ensuring uniformity in configuration structure and content, reducing errors, and improving overall system reliability.


Rationale
=========

Will be added during implementation.

Specification
=============

Guideline and model definition is part of the pitch. They should cover at least the following aspects:

Requirements
------------

* **Common Format**: Define a formal description language for the configuration model (e.g., JSON schema or FlatBuffers) to ensure machine-readable and validated configurations.
* **Self-Contained Module Configuration**: Each module must be able to carry its own configuration for portability. This introduces a potential conflict with centralized consistency. Compromise: Implement consistency checks across modules rather than enforcing a single shared configuration file.
* **Extensibility**: The model should be designed to accommodate future features and extensions without breaking existing configurations.
* **Supported Features**:
  * Configuration scope of current module configurations need to be considered
  * Multiple instantiations of the same module with distinct configurations.
  * Versioning of configuration schema for backward compatibility.
  * further features to be defined.

Architecture
------------

* **Configuration Schema Layer**: Defines the model in JSON schema or FlatBuffers.
* **Validation Engine**: Performs consistency checks across modules and validates schema compliance.
* **Integration Layer**: Ensures that module configurations can be loaded independently while maintaining global consistency rules.

Changes Introduced
------------------

* **Requirements**: Add mandatory adherence to the guideline and model for all new modules.
* **Architecture**: Introduce schema-based configuration and validation components.
* **Implementation**: Provide reference templates and examples for contributors.
* **Process**: Update module development workflow to include configuration compliance checks.
* **Documentation**: Publish guideline and model specifications with examples.
* **Infrastructure**: Add tooling for automated validation and integration testing.



Backwards Compatibility
=======================

**Impact Assessment**: Low to Medium

The configuration model is designed with extensibility and versioning to maintain backward compatibility. However, some existing modules may require minor configuration adjustments to align with the new standardized model.


Security Impact
===============

none

Safety Impact
=============

none

License Impact
==============

none


How to Teach This
=================

**Implementation Roadmap**:

1. **Documentation Package**:
   * Configuration guideline with naming conventions and structure rules
   * Model specification with required and optional elements
   * Migration guide for existing modules
   * Best practices and common patterns

2. **Developer Resources**:
   * Updated module templates with configuration sections
   * Validation tools and IDE integration
   * Example configurations for common use cases
   * Training workshops for development teams

3. **Integration Support**:
   * Automated compliance checking in CI/CD pipelines
   * Configuration validation utilities
   * Migration assistance for legacy modules


Rejected Ideas
==============

**Centralized Configuration File**: Would compromise module portability and independence

**Purely Structural Approach**: Fails to address content fragmentation issues

**Hard-coded Standards**: Too inflexible for future extensions and diverse module needs

**Runtime Configuration Only**: Misses static configuration requirements for build-time optimization

Open Issues
===========

1. **Schema Implementation Language**: Final decision between JSON Schema and FlatBuffers pending performance analysis

2. **Migration Timeline**: Coordination with existing module development cycles

3. **Validation Granularity**: Define scope of cross-module consistency checks vs. module autonomy

4. **Tooling Integration**: Specify IDE and build system integration requirements



References
==========

* **JSON Schema**: https://json-schema.org/ - Specification for configuration validation
* **FlatBuffers**: https://google.github.io/flatbuffers/ - Alternative serialization format
* **Module Development Guide**: Internal project documentation
* **Configuration Examples**: Available in project repository under `/examples/config/`


.. toctree::
   :hidden:

   architecture/index.rst
   architecture/chklst_arc_inspection.rst
   requirements/index.rst
   requirements/chklst_req_inspection.rst
   safety_analysis/fmea.rst
   safety_analysis/dfa.rst
   safety_planning/index.rst
