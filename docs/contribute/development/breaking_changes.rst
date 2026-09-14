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

.. document:: Breaking Changes
   :id: doc__breaking_changes
   :status: valid
   :version: 1
   :safety: ASIL_B
   :security: NO
   :realizes: wp__sw_development_plan[version==1]

.. _breaking_changes:

Breaking Changes
#################

Scope
*****

This document only concerns **source-level** breaking changes, i.e. changes that require a user of a
module (another S-CORE module, a downstream integrator or an external consumer) to adapt their own
source code, build files or configuration in order to keep building or behaving correctly.

**ABI-level** breakage (i.e. loss of binary compatibility between releases that does not require source
changes) is out of scope of this document.

Policy
******

Source-level breaking changes are **not acceptable**.

S-CORE has internal users, i.e. S-CORE modules depending on other S-CORE modules, as well as an unknown
and potentially large number of external users depending on S-CORE modules. A breaking change does not
affect a single consumer only: it forces every internal and external user of the affected interface to
adapt. This harms the usage and adoption of S-CORE, as it undermines the trust that a stable,
continuously consistent stack is meant to provide.

This is also reflected in the design decision documented in
:need:`dec_rec__strat__consistent_stack_vs_reference`, which establishes S-CORE as a continuously
consistent stack and requires that breaking changes be justified in terms of stack-level objectives
rather than module-local priorities alone.

Mitigation: Deprecate Instead of Break
***************************************

Breaking changes can, and should, be mitigated by introducing new functionality alongside the existing
one, while marking the functionality it is meant to replace as a candidate for future removal, i.e.
**deprecated**.

This means:

#. New behavior, APIs or interfaces are added without altering the observable behavior, signature or
   contract of what already exists.
#. The functionality that the new addition is meant to replace is marked as deprecated (e.g. via
   language-specific deprecation attributes/annotations, documentation notes, and/or compiler or linter
   warnings), so that users are made aware of the planned removal as early as possible.
#. Users are given a **grace period** during which both the deprecated and the new functionality are
   available and working, allowing them to migrate at their own pace.
#. Only after the grace period has elapsed may the deprecated functionality be removed.

This approach decouples the introduction of new functionality from the removal of old functionality,
splitting a single disruptive breaking change into two independent, non-breaking steps.

Example (C++)
=============

Assume ``ComputeChecksum`` needs an additional parameter to select the checksum algorithm. Changing its
signature in place would break every existing caller. Instead, add a new overload and deprecate the old
one using the standard ``[[deprecated]]`` attribute:

.. code-block:: cpp

   class ChecksumCalculator
   {
   public:
       // New functionality: added alongside the existing overload, does not alter its behavior.
       std::uint32_t ComputeChecksum(std::span<const std::byte> data, ChecksumAlgorithm algorithm) const;

       // Deprecated: candidate for removal after the grace period.
       // Use ComputeChecksum(data, algorithm) instead.
       [[deprecated("Use ComputeChecksum(data, algorithm) instead. Will be removed after v3.0.")]]
       std::uint32_t ComputeChecksum(std::span<const std::byte> data) const
       {
           return ComputeChecksum(data, ChecksumAlgorithm::kCrc32);
       }
   };

The ``[[deprecated]]`` attribute makes the compiler emit a warning at every call site of the old overload.
This gives users of the module clear, tool-supported notice, while their existing code keeps building and
behaving unchanged. Only once the announced grace period (e.g. tied to a number of releases or a
deadline stated in the deprecation message) has elapsed may the deprecated overload be removed.

Handling Unavoidable Breaking Changes
**************************************

There may be rare cases where a breaking change cannot be avoided, even if deprecation was considered.
In such cases:

* The commit introducing the breaking change **must** clearly state that it contains a breaking change,
  including what breaks and, if applicable, how affected users can adapt. See
  :need:`doc__git_coding_guidelines` for the general commit message format.
* The breaking change **must** be explicitly mentioned in the release notes of the release that contains
  it, so that it is impossible to miss by anyone consuming that release. See
  :need:`doc__platform_release_management_plan` for the release process.

The absence of such a statement must not be treated as evidence that a release contains no breaking
changes. Its presence, however, is mandatory whenever a breaking change is unavoidable.
