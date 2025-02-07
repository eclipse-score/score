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

Since name and e-mail address are part of the commit (and thus be part
of the commit history) they shall be specified via the .gitconfig file.
So this file must at least include the following lines:

.. code-block::

   [user]
   email = <your-email-address> (e.g. max.mustermann@something.com)
   name = Max Mustermann

***************
 Commit History
***************

Before merging a PR all commits shall be squashed into few (desired only
one) logical commits.

.. note::

   Keep in mind that upon merge the commit history of your branch will
   be preserved in the main branch of the repo as well.

**********************
 Commit Message Format
**********************

In Score it is checked if git commit messages are written according
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

The Subject shall describe what was changed in a single line max 72
characters long. It shall include a prefix for the module, component or
feature which was changed e.g. "doc:" or "bazel:" It shall start with a
capital letter and should not be ended by a trailing period in the
subject line.

Good and bad examples for a subject are:

-  **mw: Show colorful output** not Add file
-  **bazel: Test Requirement SWS_CM_00001** not Add test
-  **osal: Split responsibilities of job handling and execution** not Refactor code

Description
===========

The description must contain a brief summary of the content of the
commit and why this is necessary. Furthermore it must be consistent and
logically complete.

If feasible, the commit message body should be extended with quoted
material such as compiler warnings, debugger stack traces or measurement
data for performance optimizations.

The description may mention issues and link to them. A detailed description
of linking commits to issues is available on `GitHub
<https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue>`__.
Be aware that keywords like (close | fix | resolve) will also close the
referenced issue if the pull request is merged.

Git commits are not required to mention issues. It is sufficient if the PR
links to any relevant issues.

Footer
======

At the end of the commit message a footer may be specified
in the following format:

.. code-block::

   Also-by: Some Bodyelse <somebodyelse@nowhere.com>

An additional check is implemented to suppress false positives: if a
commit message has revert/merge in the first line, the linting rules
will not be applied to it. Thereby headaches when performing reverts or
merges are reduced.

Layout Summary
==============

In short the commit message shall consist of:

-  Summary
-  Empty line
-  Description
-  Empty line
-  Footer

Example
=======
.. code-block::

    component: Short one line summary of change

    More detailed explanatory text, mandatory. Wrap it to about 72
    characters or less. The first line is treated as the subject and the
    rest of the text as the body. The blank line separating the summary from
    the body is critical (unless you omit the body entirely);

    -  Bullet points are okay, too
    -  Typically a hyphen or asterisk is used for the bullet, followed by a
       space, using a hanging indent

    Comment how the change was tested.

    Notes about dependencies to other tools or commits in other
    repositories.

    Also-by: Some Bodyelse <somebodyelse@nowhere.com>
