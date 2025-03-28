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

Configuration as code
#######################

Documentation
***************

Description
===========

S-CORE project uses GitHub for hosting source code as well as GitHub
Actions for all CI/CD task. The configuration of the organization and
repositories is managed by otterdog, a config-as-code solution. GitHub
provides several approaches to set up repositories. In order to provide
unified experience among all the S-CORE repositories, the following rules
should be followed.

For in depth description of the properties and the relations, please
refer to the otterdog documentation.

Current setup can be viewed in the dashboard:
https://otterdog.eclipse.org/projects/automotive.score

Automatically generated documentation for eclipse-score otterdog
configuration is here: https://eclipse-score.github.io/.eclipsefdn/

All changes to the configuration should be handled by pull requests in
https://github.com/eclipse-score/.eclipsefdn/

Organization settings
---------------------

-  ``default_branch_name`` - the default branch name for newly created
   repositories is set to ``main``.
-  ``has_discussions`` - organisation level discussions are enabled.
-  ``discussion_source_repository`` - organization level discussiones
   are attached to ``eclipse-score/score`` repository.

Repository settings
-------------------

-  ``homepage`` - the link that is displayed when opening the repository
   in github.
-  ``environments`` - ``github-pages`` environment needs to be defined
   for building documentation.
-  ``gh_pages_build_type`` - set to ``workflow`` to build the
   documentation rather than serve static content.

References
==========

-  GitHub documentation: https://docs.github.com/en
-  GitHub repositories: https://docs.github.com/en/repositories
-  GitHub actions: https://docs.github.com/en/actions
-  otterdog: https://otterdog.readthedocs.io/en/latest/
