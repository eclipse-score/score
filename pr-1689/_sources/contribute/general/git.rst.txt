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

.. document:: Git Guidelines
   :id: doc__git_coding_guidelines
   :status: valid
   :safety: ASIL_B
   :realizes: PROCESS_wp__sw_development_plan

.. _git_guidelines:

################
 Git Guidelines
################

***********
 Motivation
***********

The commit history and especially the commit messages are part of a
project's documentation. Therefore, the same rules that are valid for
documentation are also valid for commits and commit messages. A commit
message is written once, but read many times (especially when hunting
bugs). Git supports powerful tools to find out which commit introduced a
bug (e.g., git bisect, git blame). Their level of usefulness depends on
the quality of the commits and their respective commit messages.

******************
 Git Configuration
******************

Authors name and e-mail address are part of the commit (and thus be part of the commit history).
They must match the name and e-mail used for eclipse registration. They can be specified via the
.gitconfig file:

.. code-block::

   [user]
   email = <your-email-address> (e.g. max.mustermann@something.com)
   name = Max Mustermann

***************
 Merging PRs
***************

When merging a PR via the GitHub user interface:

Use ``Squash & Merge`` in case:

   #. there are multiple commits on top of the initial commit

      - Reasons for multiple commits are fixing of review findings or work in progress PRs.

      **AND**
   #. all commits by the same author.

Use ``Rebase & Merge`` or ``Merge Commit`` in case:

   #. the commits address different topics. Note however that it is preferred that a PR addresses a
      single/atomic topic.

      **OR**
   #. the commits have different authors

      - It is preferred to squash the commits, in case all authors agree to squash.
      - ``Co-authored-by: x y <x.y@z.com>`` can be a good option to show appreciation to co-authors.
      - Reasons to not squash a commit of multiple authors may be liability or IP concerns.

.. note::

   Keep in mind that upon merge the commit history of your branch will
   be preserved in the main branch of the repo as well.

**********************
 Commit Message Format
**********************

In S-CORE it is checked if git commit messages are written according
to guidelines. However, it cannot enforce the meaningfulness of the
message (and its parts).

The tool ``gitlint`` is used to check the compliance with the rules described below. Please check our
`gitlint configuration <https://github.com/eclipse-score/score/blob/main/.gitlint>`_
for an overview of the rules we use.

.. note::

   Remember that this information is shown in git log and other tools.

Wording
=======

Proper English language and full sentences are to be used in the commit
message. For both the subject and the body a singular imperative form is
required. E.g. **"Add unit test for class XY"** and not "I added unit
tests", "Adding unit tests" or "Various minor changes".

Additionally, the following specification for the content shall apply for
commit messages (according to [Eclipse Git Commit Records](https://www.eclipse.org/projects/handbook/#resources-commit)):

Summary
=======

.. code-block::

   <prefix_name>: Summary

The Subject shall describe what was changed in a single line max 72 characters long. It shall not
start or end with whitespace. It shall not end with a period.

Good and bad examples for a subject are:

-  **Show colorful output** not Add file
-  **Test Requirement SWS_CM_00001** not Add test
-  **Split responsibilities of job handling and execution** not Refactor code

Description
===========

The optional description can be used to provide a brief summary of the content of the
commit and why this is necessary.

Git commits are not required to mention issues. It is sufficient if the PR
links to any relevant issues.

The description may mention issues and link to them. Note that when squashing as described above, a
link to the PR is automatically added.

Footer
======

At the end of the commit message a footer may be specified
in the following format:

.. code-block::

   Also-by: Some Bodyelse <somebodyelse@nowhere.com>

Layout Summary
==============

In short the commit message shall consist of:

-  Summary
-  Empty line (required in case description is present)
-  Description (optional)
-  Empty line (required if footer is present)
-  Footer (optional)

Example
=======
.. code-block::

    Short one line summary of change

    More detailed explanatory text, optional. Wrap it to about 72
    characters or less. The blank line separating the summary from
    the body is critical (unless you omit the body entirely);

    -  Bullet points are okay, too
    -  Typically a hyphen or asterisk is used for the bullet, followed by a
       space, using a hanging indent

    Comment how the change was tested.

    Notes about dependencies to other tools or commits in other
    repositories.

    Also-by: Some Bodyelse <somebodyelse@nowhere.com>
