Configuration Model
###################

.. document:: Configuration Model
   :id: doc__configuration_model
   :status: draft
   :safety: QM
   :security: NO
   :tags: feature_request

Feature flag
============

To activate this feature, use the following feature flag:

``experimental_configuration_model``


Abstract
========

This proposal introduces a unified approach to static component configuration in S-CORE by combining a Configuration Guideline and a Configuration Model. It covers both platform and application components. While the guideline defines how configurations should be structured—covering naming conventions, identifier usage, storage formats, and parameter organization—the model specifies what needs to be configured, focusing on common elements that must remain consistent across all components. The dual approach ensures clarity, predictability, and maintainability, reducing integration complexity and improving user experience. By standardizing both the structure and the content of configurations, the solution enables faster onboarding of new components, supports future extensions (e.g., JSON or FlatBuffers), and lays the foundation for automated compliance checks.

Motivation
==========

The current configuration landscape in S-CORE suffers from fragmentation: contributors define static configurations independently, leading to inconsistencies in identifiers, variable naming, and file storage. Beyond structural differences, there is no common understanding of what must be configured for each component (e.g., support for "multiple instances"). This results in missing or redundant parameters, unclear dependencies, and unpredictable integration behavior. Without a shared model, cross-component consistency can hardly be guaranteed, making maintenance and scaling difficult. Introducing both a guideline and a model addresses these gaps by ensuring uniformity in configuration structure and content, reducing errors, and improving overall system reliability.

Focus of this proposal is on static post compile time configurations of application and middleware components. Pre-compile time configurations like 'feature_selection' are out of scope.

Rationale
=========

Will be added during implementation.

Specification
=============

Guideline and model definition is part of the pitch. They should cover at least the following aspects:

Requirements
------------

* **Common Format**: Define a formal description language for the configuration model (e.g., JSON schema) to ensure machine-readable and validated configurations.
* **Self-Contained Component Configuration**: To provide a self-contained component, each component must be able to carry its own configuration. This introduces a potential conflict with centralized consistency. Potential compromise: Implement consistency checks across components rather than enforcing a single shared configuration file.
* **Extensibility**: The model should be designed to accommodate future features and extensions without breaking existing configurations.
* **Simplicity**: The guideline and model should be easy to understand and each configuration parameter should have a clear purpose.
* **Supported Features**:

  * Configuration scope of current component configurations need to be considered
  * Configuration of required and provided capabilities of components.
  * Multiple instantiations of the same component with distinct configurations.
  * Versioning of configuration schema for backward compatibility.
  * further features to be defined.

Architecture
------------

* **Configuration Schema Layer**: Defines the model, e.g. in JSON schema.
* **Validation Engine**: Performs consistency checks across components and validates schema compliance.
* **Integration Layer**: Ensures that component configurations can be loaded independently while maintaining global consistency rules.

Changes Introduced
------------------

* **Requirements**: Add mandatory adherence to the guideline and model for all new components.
* **Architecture**: Introduce schema-based configuration and validation components.
* **Implementation**: Provide reference templates and examples for contributors.
* **Process**: Update component development workflow to include configuration compliance checks.
* **Documentation**: Publish guideline and model specifications with examples.
* **Infrastructure**: Add tooling for automated validation and integration testing.



Backwards Compatibility
=======================

**Impact Assessment**: Low to Medium

The configuration model is designed with extensibility and versioning to maintain backward compatibility. However, some existing components may require minor configuration adjustments to align with the new standardized model.


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
   * Migration guide for existing components
   * Best practices and common patterns

2. **Developer Resources**:
   * Updated component templates with configuration sections
   * Validation tools and IDE integration
   * Example configurations for common use cases
   * Training workshops for development teams

3. **Integration Support**:
   * Automated compliance checking in CI/CD pipelines
   * Configuration validation utilities
   * Migration assistance for legacy components


Rejected Ideas
==============

**Centralized Configuration File**: Would compromise component portability and independence

**Purely Structural Approach**: Fails to address content fragmentation issues

**Hard-coded Standards**: Too inflexible for future extensions and diverse component needs

**Runtime Configuration Only**: Will not meet runtime requirements like fast startup time

Open Issues
===========

1. **Schema Implementation Language**: Final decision between JSON Schema and FlatBuffers pending performance analysis

2. **Migration Timeline**: Coordination with existing component development cycles
3. **Validation Granularity**: Define scope of consistency checks between local (component specific) and global (cross component) configuration aspects, considering self-containment of component configuration vs. cross component consistency.
4. **Tooling Integration**: Specify IDE and build system integration requirements



References
==========

* **JSON Schema**: https://json-schema.org/ - Specification for configuration validation
* **FlatBuffers**: https://google.github.io/flatbuffers/ - Alternative serialization format
* **Module Development Guide**: Internal project documentation
* **Configuration Examples**: Available in project repository under `/examples/config/`


.. toctree::
   :hidden:
