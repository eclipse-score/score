..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
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

Security & Cryptography
#######################

.. document:: Security & Crpyto Feature Requirements
   :id: doc__security_crypto_feat_reqs
   :status: valid
   :safety: QM
   :security: YES
   :realizes: wp__feat_request


.. toctree::
   :hidden:

   requirements/index.rst


Feature flag
============

To activate this feature, use the following feature flag:

``experimental_security_crypto``


Abstract
========

Embedded systems have general security goals like confidentiality, integrity, and availability
(CIA). A security component inside of S-CORE needs to provide several functionalities to
achieve these properties by using cryptographic algorithms.


Motivation
==========

S-CORE will be embedded in an automotive embedded System-on-a-Chip (SoC) and interconnected via
network interfaces with the overall vehicle network. It will process data fom various sources,
provide data internally and outside of its own hosting chipset. S-CORE as a SW platform will ensure
that itself, processed data and its hosted applications operate in a secure manner.


Rationale
=========

The features presented in this proposal are derived from the above mentioned security goals.
A single feature offering just 'cryptographic algorithms' is not enough to provide effective
measures to ensure confidentiality, integrity, and availability.
Therefore this proposal already considers this as a security & crypto component.


Specification
=============

In order to achieve the above mentioned security goals, a security component needs to provide the
following functionalities.

* 'Symmetric encryption' - with the same key known to both communication parties
* 'Asymmetric encryption' - to allow a trusted exchange of secrets with a pair of keys (public and
  private) for encryption and decryption.
* 'Signature functionality' - to ensure that data is authentic and not tampered (integrity) if
  verified to be valid. Functionality is to create and verify a signature.
* 'Certificate management' - to manage a set of signed and verified (trusted) certificates.
* 'Generation of entropy' - to ensure algorithm can rely on true/sufficiently random numbers
* 'Ensure data integrity' - achieved with a hash function.
* 'Ensure data confidentially' - achieved with an encryption and decryption function.

Additionally a cryptographic component will typically as well offer

* key management: secure generation, import, storage, update and deletion of key material
* the usage of the above mentioned functionality (decrypt, encrypt) while not revealing the
  key material to users of the API

The cryptographic component should be aware that certain attacks will try to observe the overall
system to analyze its inner workings to guess secrets (side channel/timing attacks) or to
influence it to limit its availability for system critical tasks.


Backwards Compatibility & Dependencies
======================================

* The cryptographic component typically needs to 'rely on hardware acceleration' to execute
  operations efficiently or to access a TRNG (True random number generator) for entropy.
  Additionally, it MAY be a good idea to as well have a software-only solution.
* Will use system level means (co-processor, hardware security module, Trusted Execution
  Environment, ...) to ensure it is protected (memory, CPU) from applications and the normal
  operating system while still offering its functionality to applications and middleware services.
* 'Time' in the sense of real world wall clock is crucial for the cryptographic component to ensure
  that for example a certificate or token is only used within its validity period.

Architecture::

           | --> Signature (create / verify)
           | --> Symmetric crypto (encrypt, decrypt)
           | --> Asymmetric crypto (encrypt, decrypt)
           | --> Key Management (generate, import, update, delete, check)
           | --> Certificate Management (add, update, verify)
           | --> Hash (create / verify)
           |
  |------------------|
  | Crypto-API       |---------> used by Applications / Other middleware
  |------------------|
            |
            |
            |
  |------------------------------|      |<------- Real-world trusted time
  | Security-component           |------|
  |                              |      | -------> HW-Accelerated execution in HSM or SW-Emulation
  | ---------------------        |
  | | Crypto-Algorithms |        |
  | ---------------------        |
  |------------------------------|
           |
           |
  |------------------|
  |    KeyStore      |
  |------------------|


Proposal for common crypto algorithms
-------------------------------------

The following algorithms should match the above goals and shall be offered by the security
component. The selection of algorithms is a proposal and subject to joint discussion.
Side note: The Eclipse Heimlig project directly supports these.
Link to project: `Eclipse Heimlig <https://github.com/eclipse-heimlig>`_


* Symmetric encryption and decryption (AES-CBC, AES-GCM, AES-CCM, Chacha20Poly1305)
* RSA for asymmetric encryption (EDDSA, MLDSA, SLDSA)
* Signing and verification (ECDSA)
* Key exchange (ECDH)
* Hashing (SHA-2, SHA-3, BLAKE3)
* Random number generation (ChaCha20Rng)


Security Impact
===============

As the security component is used for security purposes, it is security relevant.

As the security component of S-CORE will be open source, it must be ensured that
an attacker can analyze the security component without gaining benefits from it with regards to
compromising a system in which S-SCORE is deployed on the road.
(Obvious: avoid security by obscurity)


Safety Impact
=============

Depends on the usage of the security component. If it is used within safety relevant components,
it may also be safety relevant. E.g. if safety communication should also be authentic.


License Impact
==============

Certain strong cryptographic functionality needs to be considered with respect to export control
regulations.


How to Teach This
=================

TBD, e.g. Training material, Demo use cases.


Rejected Ideas
==============

TBD


Additional thinking
===================

Security concept
----------------

A detailed security concept should be developed for the SW platform, including the security
component. The SW platform and the security component itself should limit the surface for
attacks.

Further security concept should consider: 'security goals', 'plausible attacks',
'critical failures', and 'countermeasures'.

Due to the nature of our overall target system to be
deployed  for 10+ years in an embedded systems the security concept needs to cover as well
'software-update strategy', 'field observation', 'crypto algorithm updates', 'repair-ability',
and 'withstand reverse engineering of secrets'.

Finally the security component needs to consider the production scenario where potentially several
'initial production keys' are brought into the system.

Memory safe language
---------------------

Following the state-of-art technology and other industry voices to improve robustness of
critical systems by using memory safe languages S-CORE decided to have Rust as a 1st class
citizen. The security component MAY be developed entirely in Rust.


Open Issues
===========

* OS security mechanisms
* Trusted computing environment / HSM
* Roles and capability rights management
* Connection to IDS / anomaly detection
* Critical component states
* Attack scenario by exceeding computation capabilities (DoS) with malicious messages that create
  exceptional load


Post quantum readiness
----------------------

See `NIST <https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-
quantum-encryption-standards>`:

* https://csrc.nist.gov/pubs/fips/203/final
* https://csrc.nist.gov/pubs/fips/204/final
* https://csrc.nist.gov/pubs/fips/205/final.

