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

.. _feature_request_template:

Feature Request Template
########################

.. gd_temp:: Feature Request Template
   :id: GD_TEMP__Feat_Request_Template
   :status: valid
   :tags: contribution_request

.. attention::
    Remove everything above when copying and filling the template.

[Your Feature Name]
===================

.. code-block:: rst

   .. document:: [Your Feature Name]
      :id: DOC__Your_Feature_Name
      :status: Your_Status
      :safety: Your_ASIL
      :tags: contribution_request, feature_request

.. attention::
    The above directive must be updated according to your Feature.

    - Modify ``name`` to be your Feature Name
    - Modify ``id`` to be your Feature Name in upper snake case preceded by ``DOC_``
    - Adjust ``status`` to be ``valid``
    - Adjust ``asil`` according to your needs
    - Extend ``tags`` according to your needs, but please keep two default tags there


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_[your_feature_name]``

    .. note::
     The feature flag must reflect the feature name in snake_case. Further, it is prepended with ``experimental_``, as
     long as the feature is not yet stable. See :doc:`/process/guidance/feature_flags/index` for more information.


Abstract
========

[A short (~200 word) description of the contribution being addressed.]


Motivation
==========

[Clearly explain why the existing platform/project solution is inadequate to address the topic that the Feature Request solves.]

    .. note::
     The motivation is critical for Feature Requests that want to change the existing features or infrastructure.
     It should clearly explain why the existing solution is inadequate to address the topic that the Feature Request solves.
     Feature Request submissions without sufficient motivation may be rejected.


Rationale
=========

[Describe why particular design decisions were made.]


   .. note::
      The rationale should provide evidence of consensus within the community and discuss important objections or concerns raised during discussion.


Specification
=============

[Describe the requirements, architecture of any new feature.] or
[Describe the change to requirements, architecture, implementation, process, documentation, infrastructure of any change request.]

   .. note::
      A Feature Request shall specify the stakeholder requirements as part of our platform/project.
      Thereby the :need:`RL_technical_lead` will approve these requirements as part of accepting the Feature Request (e.g. merging the PR with the Feature Request).


Backwards Compatibility
=======================

[Describe potential impact (especially including safety and security impacts) and severity on pre-existing platform/project elements.]


Security Impact
===============

[How could a malicious user take advantage of this new feature?]

   .. note::
      If there are security concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.



Safety Impact
=============

[How could the safety be impacted by the new feature?]

   .. note::
      If there are safety concerns in relation to the Feature Request, those concerns should be explicitly written out to make sure reviewers of the Feature Request are aware of them.
      ToDo - Link to the Safety Impact Method

[What is the expected ASIL level?]
[What is the expected classification of the contribution?]

   .. note::
      Use the component classification method here to classfiy your component, if it shall to be used in a safety context: (TODO: add link to component classification).


License Impact
==============

[How could the copyright impacted by the license of the new contribution?]


How to Teach This
=================
