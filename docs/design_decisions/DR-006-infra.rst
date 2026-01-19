..
   Copyright (c) 2025 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-006-Infra: Hosting Strategy for Module Documentation
=======================================================

.. dec_rec:: Hosting strategy for module webspaces
   :id: dec_rec__infra__webspace
   :status: accepted
   :context: Infrastructure
   :decision: Combine Website from multiple Repos

Problem Description
-------------------

We currently host module documentation using GitHub Pages (per-repo webspaces).
**GitHub Pages only allows 1GiB of webspace**.
While this works so far, the storage and site limits are becoming noticeable.
The score platform repository currently has 1GiB in gh-pages (460MiB ``.git`` repo size).
More diagrams, pull-requests, and versions will exacerbate the problem.

.. plantuml::

   collections "Module Repos" as ModuleRepo
   collections ".gh_pages branches" as gh_pages
   cloud "GitHub Pages" as GitHubPages

   ModuleRepo -> gh_pages : "build"
   gh_pages -> GitHubPages : "publish"

Context
^^^^^^^

In addition to GitHub Pages, the project also has the website
https://eclipse.dev/score/ hosted via the Eclipse Foundation.
The website is relatively small and there are plans to move most content elsewhere
(where it can be managed via Wordpress).

The foundation updates the content every 5 minutes from
the `eclipse-score-website-published <https://github.com/eclipse-score/eclipse-score-website-published>`_ repo.
The sources are in the `eclipse-score-website <https://github.com/eclipse-score/eclipse-score-website>`_ repo
and get deployed automatically using the GitHub Action
`Build and Archive <https://github.com/eclipse-score/eclipse-score-website/actions/workflows/build_and_publish.yml>`_.

.. plantuml::

   node "eclipse-score-website-published" as PublishedRepo
   node "eclipse-score-website" as WebsiteSrc
   cloud "eclipse.dev/score" as EclipseSite

   WebsiteSrc -> PublishedRepo : "Build & Archive"
   PublishedRepo <. EclipseSite : "pull every 5min"

No limits for this hosting are known.

Goals and Requirements
^^^^^^^^^^^^^^^^^^^^^^

1. Provide sufficient storage and bandwidth for documentation (releases and PR-previews).
2. Keep a consistent site/URL structure and navigation across modules.
3. Keep hosting and maintenance costs predictable and low.
4. Dedicated space for releases?

⚠️ What about additional documentation artifacts from DoxyGen, RustDoc, ...?

Options Considered
------------------

Option G: Continue with per-repo GitHub Pages (status quo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Keep publishing module webspaces to GitHub Pages.
Invest efforts to keep space needs low as we only have 1GiB per repository.
e.g. by optimizing page size, or providing PR previews only on demand.

😡 Effort: Increasing.

The effort is serious enough that we don't consider the other criteria at all.

Option P: Publish Action into "published" Repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we alread have the "eclipse-score-website-published" repository,
we can push more content in there.
Up to the 10GiB repo limit.

.. plantuml::

   collections "Module Repos" as ModuleRepo
   node "eclipse-score-website-published" as PublishedRepo
   node "eclipse-score-website" as WebsiteSrc
   cloud "eclipse.dev/score" as EclipseSite

   ModuleRepo -> PublishedRepo : "build"
   WebsiteSrc -> PublishedRepo : "Build & Archive"
   PublishedRepo <. EclipseSite : "pull every 5min"
   ModuleRepo -[hidden]-> WebsiteSrc

The limit is not 1GiB per repo anymore but 10GiB for all repos.
That sounds worse at first, because with 20 repos, it would be 10GiB / 20.
However, here the *average* size per repository matters.
With option G above a single repo limit is already a problem.
Still, this might not ease the problem sufficiently.

💚 Effort: We must adapt our GitHub action's deploy steps.

😡 Speed: Updating a huge "published" repo will take time.

😡 Size: 10GiB total limit.

💚 Independence: No HelpDesk needed to potentially adapt configuration.

Option C: Combine Website from multiple Repos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We let the eclipse.dev website pull content from multiple repositories.
`The configuration is done by the Eclipse Foundation <https://gitlab.eclipse.org/eclipsefdn/software-dev/frameworks-and-tools/hugo-eclipsefdn-website-boilerplate#update-pmi>`_:

  Finally, to publish your website on eclipse.dev,
  you'll need support from us to update your project's website metadata in the projects.eclipse.org (PMI).
  This informs us on where to find the necessary static HTML to serve.
  You can request an update to your website deployment metadata by opening a ticket.

The configuration is visible as ``website_repo`` from
`the Eclipse API of S-CORE <https://projects.eclipse.org/api/projects/automotive.score>`_.

.. plantuml::

   collections "Module Repos" as ModuleRepo
   node "eclipse-score-website-published" as PublishedRepo
   node "eclipse-score-website" as WebsiteSrc
   cloud "eclipse.dev/score" as EclipseSite
   collections ".gh_pages branches" as gh_pages

   ModuleRepo -> gh_pages : "build"
   WebsiteSrc -> PublishedRepo : "Build & Archive"
   PublishedRepo <. EclipseSite : "pull every 5min"
   gh_pages <. EclipseSite : "pull every 5min"
   ModuleRepo -[hidden]-> WebsiteSrc

💚 Effort: Request config change via Eclipse HelpDesk.

💚 Speed: Faster than option P because many *small* repos.

💚 Size: 10GiB per repo should suffice for a long time.

😡 Independence: HelpDesk needed to adapt configuration. (Add repo, rename folder)

Option D: Direct Webspace Push
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instead of using the foundation's pulling mechanism,
we could push directly to some webspace from each module's GitHub Action.

The eclipse.dev/score website is separate and not relevant for this option.

.. plantuml::

   collections "Module Repos" as ModuleRepo
   cloud webspace

   ModuleRepo -> webspace : "build & publish"

😡 Effort: Requires custom setup for the publication?

💚 Speed: Fast

💚 Size: Independent of any GitHub limits.

💚 Independence: Full control because custom.

Evaluation
----------

All options have the same costs in terms of hosting fees.

Criteria in order of importance (most important first):

.. csv-table::
   :header: Criteria, Option G, Option P, Option C, Option D
   :widths: 20, 10, 10, 10, 10

   Effort,      😡, 💚, 💚, ❓
   Size,        😡, 😡, 💚, 💚
   Speed,        ❔, 😡, 💚, 💚
   Independence, ❔, 💚, 😡, 💚

Option G is not sustainable due to increasing effort.
Option P still has risky size limits.
Thus we pick option E because deployment speed is more important than independence.

⚠️ evaluate option D properly
