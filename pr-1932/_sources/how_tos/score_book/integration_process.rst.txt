Integration process
====================

Integration process in s-core project is not a trivial thing and as s-core project is quite young,
we still gather our experience and adapt it to meet our needs.

There are several discussions and concepts written to this topic, that you can find here:

(TODO: Links)

This chapter will not go to much into details and will try to give you the overall idea of the
integration process for s-core.

(TODO: here the image with the reference integration)

Idea of our integration process can be summarized with the following bullet points:

1. Compliance to s-core software development process
   
   -  we do encourage every software module inside of the s-core GitHub organization or also outside of it 
      to follow the s-core development process continiously and introduce it including approtiated checks into
      the CI/CD pipeline, so that compliance to the s-core project is checked with every PR. But the fact is, that
      we can not enforce this, even inside of the GitHub organization. This has various reasons. One reason could be,
      that the software module already exists and is used in multiple other projecs. The other reason could be, that
      the software module was open sources by another company that needs to follow another interanl software development
      process and switching to the s-core development process can not happen immedediately. Therefore, it is possible
      (but not very welcomed), that every software module follows its own software development process inside of its repo.

   - to announce a new version of your module and make it available inside of s-core, you need to add it to bazel registry.
     This is where our integration process comes in place. To be able to add your module to s-core bazel registry you need to
     fulfill two things:

     - you need to fulfill our so called "integration gate". This is a collection of checks and jobs that need to be fulfilled
       be every module in s-core. This automated jobs and checks ensure, that you are compliant with s-core software development
       process, e.g. code can be compiled with gcc/qcc compiler, unit tests are not failing, requirements and architecture are
       properly linked and so on.
     - after your software module fulfills integration gate (changes to software module code and further artifacts can be necessary
       for this), you can create a PR to s-core bazel registry repo. This is the point in time where your PR will be reviewed by
       safety, security and quality managers of the s-core project. After all findings are fixed, the PR will be merged to the s-core
       bazel registry and the software module will be officialy available to the s-core community.
  
2. Reference integration

The first step ensures, that the software module is compliant to the s-core development process. But it is not ensured
yet, that the new version of the software module works together with another modules. This is where the reference integration comes into place.

Reference integration repository contains reference image(s), that are used to execute feature integration tests, that ensure,
that every feature, that is built up of multiple modules, implements its requirements and can be used by the end-user.

Reference integration overwrites all dependencies set by the software module itself, meaning that if we configure reference integration
to depend on the software module A in version 1.0 then also all other software modules in scope of reference integration will be built using
automatically the version 1.0 of the module A independently of what is configured as their local dependency. This ensures, that we always have
a consistent unique state of software module versions. 

It can happen that introducing a newer version of the software module into reference integration repository lead to problems, as other modules
are not compatible with changes done in the newer module. In theory, such problems should be avoided using proper planning and concept
of deprecated interfaces. In praxis, such situations can not be always avoided and in case they happen, s-core integration team should
take over solving of such kind of problems.

Based on agreed timeline and in case all feature integration tests can be successfully executed and other s-core project metrics are fulfilled,
a release of reference integration repository hereby an official S-cre release can be done. It consists mainly of

- a release tag on the reference integration repository, that automatically also freezes specific version of every software module referenced
  by the reference integration repo and therefore indicates all software modules, that are officially part of this s-core release.
- release notes
- further documents.  



