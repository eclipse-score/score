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

.. document:: Contribution Guidelines
   :id: doc__contribution_guidelines
   :status: valid
   :version: 1
   :safety: QM
   :security: NO
   :realizes: wp__sw_development_plan[version==1]

.. _contribution_guidelines:

########################
 Contribution Guidelines
########################

.. _pr_scope_and_size:

**********************************
 Scope and Size of a Pull Request
**********************************

A pull request does one thing and can be reviewed in one sitting. Content changes stay small;
purely formal changes applied to many elements may be large. Every change carries a reason.

#. **One concern per pull request.** A pull request does one thing: one fix, one step of a
   feature, one refactoring, or one formal change. Unrelated changes go into separate pull
   requests, even if they touch the same file.
#. **Reviewable in one sitting.** Keep content changes small enough that a reviewer can
   understand all of them at once. As orientation, aim for about 400 changed lines of
   hand-written content or less. Larger content needs a reason in the description. New topics
   start with an issue (:need:`doc__issue_guideline`) or, for new features and enhancements, a
   Feature & Enhancement Proposal (:need:`doc__feature_request_guideline`).
#. **Formal changes may be large.** A change that applies one rule to many elements (renaming an
   attribute across all needs, updating headers, migrating links, tool-generated formatting) may
   touch many files, if:

   - it is purely mechanical and contains no content change;
   - the description states the rule, and the command or script, so reviewers check the rule,
     not every line;
   - it is a pull request of its own, never mixed with content changes.

#. **Substance, not volume.** Every change needs a reason that the description states.
   Rewording, reformatting or extending text without a content reason is not a contribution.
   Reviewers may close such pull requests without a detailed review.
#. **Split, do not stack up.** Large work is delivered as a sequence of small pull requests:
   preparatory refactoring first, then the change itself. A draft pull request or an issue can
   show the whole picture.
#. **AI-assisted contributions** follow :need:`wp__policies`, which makes the
   `Eclipse Generative AI Usage Guidelines <https://www.eclipse.org/projects/guidelines/genai/>`_
   applicable: the contributor has reviewed and understands every line and can defend it in
   review, and AI use should be disclosed (``Assisted-by:`` trailer). The same size and substance
   rules apply.
#. **Reviewers may ask to split.** A committer may request that a pull request is split before
   reviewing it, and should say along which line.

.. note::

   Nothing here changes the Eclipse rule that contributions over 1,000 LoC need an IP Team
   review; rule 3 does not exempt a formal change from it.
