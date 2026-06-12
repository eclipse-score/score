..
   Copyright (c) 2026 Contributors to the Eclipse Foundation

   See the NOTICE file(s) distributed with this work for additional
   information regarding copyright ownership.

   This program and the accompanying materials are made available under the
   terms of the Apache License Version 2.0 which is available at
   https://www.apache.org/licenses/LICENSE-2.0

   SPDX-License-Identifier: Apache-2.0

DR-002-Strat: Eclipse Project Structure for S-Core
===================================================

- **Date:** 2026-05-22

.. dec_rec:: Eclipse Project Structure for S-Core
   :id: dec_rec__strat__eclipse_project_structure
   :status: accepted
   :context: Strategy
   :decision: Option 1

Context / Problem
-----------------

S-Core needs to decide how its modules are structured within the Eclipse Foundation and GitHub.
Two organisational models are under consideration: keeping all modules within one Eclipse project
(the current approach), or splitting each module into a separate Eclipse project.

The choice has implications for community governance, Committer nomination processes, GitHub
organisation management, and the long-term risk to the S-Core v1.0 release.

Options Considered
------------------

Option 1: One Eclipse Project (currently used)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Supports the idea: "S-Core is a platform"* (e.g. same as Android)

All S-Core relevant modules reside together in one GitHub organisation under one Eclipse project.

.. uml::
   :align: center
   :caption: Option 1 – One Eclipse project containing all S-Core repositories

   skinparam componentStyle rectangle

   component "eclipse" as ef <<Eclipse Foundation>> {
      component "eclipse-score" as org <<GitHub Organisation>> {
         component "score" as score
         component "feo" as feo
         component "baselibs" as baselibs
         component "logging" as logging
         component "persistence" as persistence
         component "process_description" as proc
         component "docs-as-code" as dac
      }
   }

   score -[hidden]right- feo
   feo -[hidden]right- baselibs
   baselibs -[hidden]right- logging
   score -[hidden]down- persistence
   persistence -[hidden]right- proc
   proc -[hidden]right- dac

**Pros**

- All S-Core relevant modules are together in one GitHub organisation → it is immediately visible
  what belongs to the S-Core project.
- One infrastructure, one timeline, one community → things are kept together.
- One authority (PLs) for all modules that can ensure the same behaviour for all modules.

**Cons**

- Eclipse Foundation project handbook rules were not designed for such big projects. This leads
  among others to the following problems:

  - It is typically not possible to nominate initial Committers for newly contributed modules.
  - The Committer model does not completely scale for such big projects. Having a large number of
    modules in one Eclipse project leads to the necessity of having a big number of Committers
    with various areas of responsibility.

- Community management and building is more complicated due to the size of the project.

**Possible mitigation**

- Eclipse Foundation and PMC must acknowledge and agree that new modules in S-Core are treated
  as new Eclipse projects for the purpose of initial Committer nomination.
- Mapping/restricting of Committer responsibilities in the project to dedicated areas is done
  using the CODEOWNERS file in GitHub (already in place).

Option 2: Multiple Eclipse Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Supports the idea: "S-Core is a pure integration project"* (e.g. same as Yocto)

Every module becomes its own Eclipse project; a central S-Core project serves as the integration
project.

.. uml::
   :align: center
   :caption: Option 2 – Multiple Eclipse projects, S-Core as the central integration project

   top to bottom direction
   skinparam componentStyle rectangle

   component "eclipse (parent)" as ef_parent <<Eclipse Foundation>> {
      component "eclipse-score / score\n(integration project)" as score_central
   }

   component "eclipse A" as ef_a <<Eclipse Foundation>> {
      component "... / baselibs" as baselibs
   }

   component "eclipse B" as ef_b <<Eclipse Foundation>> {
      component "... / logging" as logging
   }

   component "eclipse ..." as ef_n <<Eclipse Foundation>> {
      component "..." as more
   }

   score_central <.. baselibs : sub-project
   score_central <.. logging  : sub-project
   score_central <.. more     : sub-project

**Pros**

- Every module is a "small" Eclipse project, which is exactly what the Eclipse Foundation project
  handbook is built for → Clear Committer/Contributor/PL management.

**Cons**

- Every project is a completely standalone project. The S-Core project PLs do not have tools to
  manage the separate Eclipse projects with implementation modules, which creates a significant
  risk that the S-Core community could fracture.
- Every module/project has its own GitHub Organisation → enforcing the same rules and processes
  is complicated; belonging to S-Core project is not obvious.

**Possible mitigation**

- S-Core becomes a "parent project" and all other S-Core relevant modules become sub-projects.
  This would make it clear that the modules are part of the S-Core project and it would still
  be easily possible to follow Eclipse project handbook rules for every sub-project, e.g. for
  initial Committer nomination.
- The Eclipse Foundation technically enables S-Core and all sub-projects/modules to be located
  within the same GitHub organisation.

Conclusion
----------

**We proceed with Option 1 and initiate a Proof of Concept for Option 2.**

Rationale
^^^^^^^^^

- There are currently no major blockers that would make the switch to Option 2 obligatory.
- Switching the structure of the project and module repositories poses a high risk for the
  S-Core v1.0 release, which is planned for the end of the year.

Follow-up Actions
^^^^^^^^^^^^^^^^^

- **X-Core approaches Eclipse Foundation**: Eclipse Foundation and PMC must acknowledge and agree
  that new modules in S-Core are treated as new Eclipse projects for the purpose of initial
  Committer nomination.
- **POC for Option 2**: The OpenSOVD project and its integration into S-Core will be used as a
  Proof of Concept (POC) for Option 2.
- The topic should be revisited after the S-Core v1.0 release is delivered.
