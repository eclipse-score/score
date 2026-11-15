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

.. document:: PF Configuration Management Plan
   :id: doc__platform_config_mgt_plan
   :status: draft
   :version: 2
   :safety: ASIL_B
   :security: YES
   :tags: platform_management
   :realizes: wp__config_mgt_plan[version==1]

PF Configuration Management Plan
================================

Purpose
-------

The Configuration Management Plan defines how the integrity, consistency, and
traceability of project-relevant work products and other configuration items
are established and maintained throughout the project lifecycle.

Objectives and scope
--------------------

The objective of this plan is to define:

* how configuration items are identified;
* where configuration items are stored;
* how configuration items are made available to relevant stakeholders;
* how configuration items can be located;
* how specific versions of configuration items can be retrieved;
* how configuration items can be modified and how such modifications are controlled;
* how versions of configuration items are created and stored;
* how baselines are established and managed;
* how backup, recovery, and long-term storage are handled; and
* how configuration status is monitored and reported.

For the definition of :term:`Configuration Item`, see
:need:`doc_concept__configuration_process`.

Approach
--------

Configuration management in S-CORE covers the identification, storage,
retrieval, modification, versioning, branching, and baselining of configuration
items, as well as backup, recovery, and configuration status reporting.


Lifecycle
~~~~~~~~~

Configuration management applies throughout the complete S-CORE development
lifecycle, including the Concept, Development, and Maintenance phases.

Identification and Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each work product is identified by its Sphinx-Needs ID. This also applies to
documents, which are identified through their document header as defined in
:need:`gd_temp__documentation`.

The complete list of project documents is maintained in
:need:`doc__documentation_mgt_plan`.

Sphinx-Needs IDs are checked for uniqueness according to
:need:`gd_req__configuration_uid`. Sphinx-Needs is also used to maintain the
properties and attributes of work products as defined by the respective
process area descriptions.

Work products are stored in text or source-code files within GitHub
repositories. Files are identified by their repository path and filename.

GitHub repositories realize the Delivery Containers described in
:need:`doc_concept__general_building_blocks`. S-CORE consists of the
`platform repository <https://GitHub.com/eclipse-score/score/>`_ and additional
repositories containing sets of Dependable Elements for which a
:need:`Delivery Team <rl__delivery_team>` is responsible.

Each S-CORE repository shall contain a single ``MODULE.bazel`` file defining
its version and dependencies. Additional ``MODULE.bazel`` files are permitted
only where required for testing purposes.

Other configuration items are identified as follows:

* **Files:** identified by their repository path and filename and version-controlled
  in GitHub.
* **Precompiled tools and binaries:** identified by the Bazel build configuration,
  including their integrity information, such as a hash where applicable.
* **External tools and binaries built by the S-CORE CI:** identified by the version
  defined in the Bazel build configuration.


Retrieval
~~~~~~~~~

Work products and files are stored in GitHub repositories and can be retrieved
in accordance with the Eclipse Foundation's access and contribution rules.

The applicable work products are defined by the corresponding process and
process-area work-product descriptions. Their location within the project
structure can be determined using :ref:`platform_folder_structure`.

Git provides access to every version-controlled state of a file. In GitHub,
the ``History`` view can be used to inspect the commits affecting a file, while
the ``Blame`` view provides line-level information about the corresponding
changes.

Baselines can be retrieved through Git tags. A tag identifies the set of
repository content belonging to a specific baseline and is used as the basis
for producing release artifacts such as documentation, software, and
verification reports.

Release versioning follows the rules defined in the corresponding section of
the release guideline.

External artifacts that need to be maintained within S-CORE are integrated
into the appropriate S-CORE repository and subsequently managed according to
the same configuration management principles.

Control and Modification
~~~~~~~~~~~~~~~~~~~~~~~~

New work products and modifications to existing configuration items are
prepared by a :need:`Contributor <rl__contributor>` on a development branch.

Changes are submitted through GitHub pull requests for review and integration
into the main branch. After successful review and fulfillment of the applicable
merge criteria, the change is merged by a :need:`Committer <rl__committer>`.

The pull request records the proposed modifications and provides the primary
basis for review and approval of the change.

For further information on change management, see
:need:`doc__platform_change_management_plan`.

Changes to tools and binary dependencies, including version updates, are
controlled through the Bazel build configuration. These configuration files
are themselves version-controlled and subject to the same GitHub-based change
and review process.

Branches and Baselines
~~~~~~~~~~~~~~~~~~~~~~

Branches support parallel and controlled development. S-CORE uses the following
branch types:

* **Development branches:** created from a remote branch and used by contributors
  to prepare changes. No project-wide naming convention is imposed unless
  otherwise specified.
* **Main branch:** the remote ``main`` branch containing the latest integrated
  changes that have passed the applicable CI checks and review process.
* **:term:`Release Branch`:** a remote branch derived from ``main`` and used to
  prepare a release. Functional development is not permitted on a release
  branch; changes are restricted to bug fixes and improvements resulting from
  verification activities. Merges into a release branch require approval by
  a :need:`rl__project_lead`. Release branch naming follows
  :need:`doc_concept__rel_process`.

A remote branch resides in the GitHub repository and is distinguished from a
developer's local branches.

Because S-CORE configuration items are maintained in GitHub repositories, a
repository-level baseline is sufficient to identify the consistent state of
the configuration items contained in that repository.

Baselines are established using Git tags. The tag name shall follow the release
versioning scheme and identify the applicable release, patch version, and,
where applicable, pre-release version.

For further information, see :need:`doc__platform_release_management_plan`.

As described in `Identification and Properties`_, S-CORE consists of multiple
repositories. Baselines are therefore established individually for each
repository. Repositories may use different versioning schemes where appropriate.

Where repositories depend on one another, the providing repository shall be
baselined before the consuming repository. The consuming repository records
the version or baseline of its dependencies. Consequently, a platform baseline
also identifies the versions of the Delivery Containers from which the
platform is composed. These versions are also reported in the platform release
notes.

Changes made on a release branch shall also be incorporated into the main
branch. The responsible Delivery Team defines the appropriate mechanism, for
example by implementing the change on ``main`` and cherry-picking it to the
release branch.

Backup and Recovery
~~~~~~~~~~~~~~~~~~~

Backup and recovery of the GitHub-hosted project repositories are covered by
the infrastructure provided by the Eclipse Foundation.

Additional measures for long-term retention of configuration items are defined
in :need:`gd_req__config_workproducts_storage`.

Status and Reporting
~~~~~~~~~~~~~~~~~~~~

Work products defined by the S-CORE processes have status attributes that are
used to communicate their maturity and configuration status to stakeholders.

The primary overview is the project document list, which contains the planned
documents and their current status. The document list is maintained in the
Documentation Management Plan :need:`doc__documentation_mgt_plan`, which is
part of the Platform Management Plan as defined in
:need:`gd_guidl__documentation`.

At least for every release, the completeness of the configuration baseline is
checked against the list of planned documents maintained in the Documentation
Management Plan.

Work products that consist of multiple Sphinx-Needs elements are collected
into a corresponding document. For example, a feature requirements document
(``doc__*``) contains the associated feature requirements (``feat_req__*``).
The same principle applies to requirements, architecture, detailed design, and
safety analysis work products.

Source-code and test-code files are not represented as documents in this
sense. Their validity is controlled through the applicable code review,
verification, and CI checks required before integration.

The configuration status and versions of tools are reported through a tool
list. The tool list may be maintained within the Documentation Management Plan
or referenced from it and shall also be subject to completeness checks.


Configuration Management Tooling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S-CORE implements configuration management primarily through the standard
version-control infrastructure provided by the Eclipse Foundation together
with the project's Docs-as-Code and build infrastructure.

The principal configuration management tools are:

* **Version control and collaboration:** GitHub
* **Docs-as-Code and work-product identification:** Sphinx-Needs
* **Build and dependency management:** Bazel

GitHub provides storage, versioning, retrieval, modification control,
branching, change history, and baselining of configuration items.

Sphinx-Needs provides identification, attributes, relationships, and
traceability for work products represented within the project documentation.

Bazel provides reproducible build and dependency configuration and identifies
the versions of tools, binaries, and repository dependencies used to produce
S-CORE artifacts.
