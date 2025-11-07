Introduction
=============


.. image:: _assets/score_image.png
   :alt: Eclipse Score
   :width: 400
   :align: center


Welcome to the Eclipse S-CORE project. As Eclipse S-CORE project is continuously developing, the decision was taken
to write a small tutorial, a **Eclipse S-CORE book**, that tries to explain how the Eclipse S-CORE project technically works.
As neither the Eclipse S-CORE project nor this book are currently in the final state, everyone is kindly invited to contribute
to the Eclipse S-CORE project and to extend this book.

Before we dive into the technical details, we think, that it is worthful to explain the background and the goals of
the Eclipse S-CORE project. Eclipse S-CORE project was founded mainly by the companies from the automotive world, that were inspired
by the open-source achievements in the last decades and that share the same vision, that a common open-source software platform
for the automotive electronical control units will empower the automotive industry to do the next step. The main reason for this,
is that software platforms need to provide more and more features with every new series of vehicles as the requirements are getting
more and more complicated. Developing and maintaining such platforms by every company separately is not efficient and also very
expensive. Therefore open source approach looks like a better alternative, where the automotive companies can share the effort and 
also have a platform for exchanging their problems and needs and that enables them to search for new solutions together.

Eclipse S-CORE project is not the first project that tries to solve these kinds of problems. In the past, such projects
as `Autosar <https://www.autosar.org/>`_, tried to
solve at least some of the problems through the standardization. Eclipse S-CORE project by no way contradicts to the ideas of Autosar. Furthermore
it tries to make the next step based on the experience of autosar and comparable standardization projects. The main two goals besides
the standardization, that we try to achieve with the Eclipse S-CORE project are the following:

- Eclipse S-CORE project aims to provide not only the specification of the modules, but also the implementation. As we all know,
  a lot of problems become clear only during the integration of the software stack and not during its specification. Beside this,
  some of the aspects of the implementation, e.g. performance, are hard to specify. Working on the same implementation in the open-source
  allows to fix the problems directly on the implementation level and to ensure, that they will not happen in the future by always
  reusing the same implementation.

- Another important aspect that normally comes up by the integration of the software stack, especially in ASIL relevant systems, is its quality
  and the software development process according to which it was developed, including following aspects: code quality, requirements and architecture,
  test coverage and so on. Therefore one of the most important goals of the Eclipse S-CORE project is not only to provide an efficient, state of the art implementation
  of the automotive software platform but also to define an ASIL conform software development process to ensure, that all implementations of
  Eclipse S-CORE modules follow this process, mainly by automated checks and in case not yet implemented, with help of manual reviews. The clear
  goal is to specify only those parts of software development process, that also can be validated with automated checks in the future.

It is important to understand, that Eclipse S-CORE project is not a final product, that can be "out-of-the-box" integrated into the automotive series projects.
This has multiple reasons. First of all, Eclipse S-CORE is an open-source project, meaning there is no any commercial company behind this project,
that can be liable for anything. The strength of the Eclipse S-CORE project is that both its software development process and the corresponding tooling
to ensure fulfillment of this process, e.g. automated checks and test execution in CI, are all open-source, so everyone can have a look and check, whether
it is doing exactly the same what it is supposed to do. Furthermore it is a well maintained basis with clear communicated things that we do and
that we do not (yet) do, that can be used by multiple automotive companies as basis for their commercial distribution. The maintainers of the Eclipse S-CORE project
strongly believe, that at least after some time further automotive companies will understand the benefits of having an open-source standard for an
automotive software platform and will start not only reusing but also actively contributing to the Eclipse S-CORE project.



