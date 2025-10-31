Integration process
====================

.. _integration_process:

Integration process in S-Core project is not a trivial thing and as S-Core project is quite young,
we still gather our experience and adapt it to meet our needs.

There are several discussions and concepts written to this topic, the most exhaustive description can be
found in the following `decision record <https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html>`_.

This chapter will not go to much into details and will try to give you the overall idea of the
integration process for s-core.

.. image:: _assets/release_integration_concept.drawio.svg
   :alt: release_integration_concept
   :align: center

Compliance to s-core software development process
--------------------------------------------------
   
We do encourage every software module inside of the S-Core GitHub organization or also outside of it 
to follow the S-Core development process continiously and introduce it by including approtiated checks into
the CI/CD pipeline, so that compliance to the S-Core project is checked with every PR. But the fact is, that
we can not enforce this, even inside of the GitHub organization. This has various reasons. One reason could be,
that the software module already exists and is used in multiple other projecs. The other reason could be, that
the software module was open sourced by another company that needs to follow another internal software development
process and switching to the S-Core development process can not happen immediately. Therefore, it is possible
(but not encouraged), that every software module follows its own software development process inside of its repo.

To announce a new version of your module and make it available inside of S-Core, you will need to add it to bazel registry.
This is where our integration process comes in place. To be able to add your module to S-Core bazel registry you need to
fulfill two things:

- you need to fulfill our so called "integration gate". This is a collection of checks and jobs that need to be fulfilled
  be every module in s-core. This automated jobs and checks ensure, that you are compliant with S-Core software development
  process, e.g. code can be compiled with gcc/qcc compiler, unit tests are not failing, requirements and architecture are
  properly linked and so on.
- after your software module fulfills integration gate (changes to software module code and further artifacts can be necessary
  for this), you can create a PR to S-Core bazel registry repo. This is the point in time where your PR will be reviewed by
  safety, security and quality managers of the S-Core project. After all findings are fixed, the PR will be merged to the S-Core
  bazel registry and the software module will be officialy available to the S-Core community.
  
Reference integration
---------------------

The first step ensures, that the software module is compliant to the s-core development process. But it is not ensured
yet, that the new version of the software module works together with other modules.
This is where the reference integration comes into place.

Reference integration repository contains reference image(s), that are used to execute feature integration tests, that ensure,
that every feature, that is built up of multiple modules, implements its feature requirements and can be used by the end-user.

Reference integration overwrites all dependencies set by the software module itself, meaning that if we configure reference integration
to depend on the software module A in version 1.0 then also all other software modules in scope of reference integration will be built using
automatically the version 1.0 of the module A, independently of what is configured as their local dependency. This ensures, that we always have
a consistent unique state of software module versions in the reference integration repository. 

It can happen that introducing a newer version of the software module into reference integration repository lead to problems, as other modules
are not compatible with changes done in the newer version of the software module. In theory, such problems should be avoided using proper planning and concept
of deprecated interfaces. In praxis, such situations can not be always avoided and in case they happen, S-Core integration team should
take over solving of such kind of problems.

Based on agreed timeline and in case all feature integration tests can be successfully executed and other S-Core project metrics are fulfilled,
a release of reference integration repository, hereby an official S-Core release, can be done. It consists mainly of

- a release tag on the reference integration repository, that automatically also freezes specific version of every software module referenced
  by the reference integration repo and therefore indicates all software modules, that are officially part of the particular S-Core release.
- release notes
- further documents.  



