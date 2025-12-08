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

.. _security_crypto_requirements:

Requirements
============

Symmetric Encryption
--------------------

.. feat_req:: Symmetric Encryption and Decryption
   :id: feat_req__sec_crypt__sym_symmetric_encrypt
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide functionality for symmetric encryption and decryption.

.. feat_req:: AES-CBC Support
   :id: feat_req__sec_crypt__sym_symm_algo_aes_cbc
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the AES-CBC symmetric encryption algorithm.

.. feat_req:: AES-GCM Support
   :id: feat_req__sec_crypt__sym_sym_algo_aes_gcm
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the AES-GCM symmetric encryption algorithm.

.. feat_req:: AES-CCM Support
   :id: feat_req__sec_crypt__sym_sym_algo_aes_ccm
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the AES-CCM symmetric encryption algorithm.

.. feat_req:: ChaCha20-Poly1305 Support
   :id: feat_req__sec_crypt__sym_algo_chacha20
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the ChaCha20-Poly1305 symmetric encryption algorithm.

Asymmetric Encryption
---------------------

.. feat_req:: Asymmetric Encryption and Decryption
   :id: feat_req__sec_crypt__asym_encryption
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide functionality for asymmetric encryption and decryption.

.. feat_req:: ECDH Support
   :id: feat_req__sec_crypt__asym_algo_ecdh
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the ECDH algorithm for key exchange.


Digital Signatures
------------------

.. feat_req:: Signature Creation
   :id: feat_req__sec_crypt__sig_creation
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide functionality to create digital signatures.

.. feat_req:: Signature Verification
   :id: feat_req__sec_crypt__sig_verification
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide functionality to verify digital signatures.

.. feat_req:: ECDSA Support
   :id: feat_req__sec_crypt__sig_algo_ecdsa
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the ECDSA algorithm for digital signatures.

Message Authentication Code (MAC)
---------------------------------

.. feat_req:: Message Authentication Code
   :id: feat_req__sec_crypt__mac
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide functionality for Message Authentication Codes (MAC) to
   ensure message integrity and authenticity.

Hashing
-------

.. feat_req:: Hashing Functionality
   :id: feat_req__sec_crypt__hashing
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide hashing functionality.

.. feat_req:: SHA-2 Support
   :id: feat_req__sec_crypt__hashing_algo_sha2
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the SHA-2 hashing algorithm.

.. feat_req:: SHA-3 Support
   :id: feat_req__sec_crypt__hashing_algo_sha3
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the SHA-3 hashing algorithm.


Key Derivation Functions (KDF)
------------------------------

.. feat_req:: Key Derivation
   :id: feat_req__sec_crypt__kdf
   :reqtype: Functional
   :security: YES
   :safety: QM
   :status: valid
   :satisfies: stkh_req__dependability__security_features

   The security component shall provide Key Derivation Functions (KDFs) to derive one or more
   secret keys from a master key or password.

Random Number Generation
------------------------

.. feat_req:: Entropy Source
   :id: feat_req__sec_crypt__rng
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide a source of entropy for random number generation.

.. feat_req:: ChaCha20Rng Support
   :id: feat_req__sec_crypt__rng_algo_chacha20rng
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall use the ChaCha20Rng algorithm for random number generation.

Certificate Management
----------------------

.. feat_req:: Certificate Management
   :id: feat_req__sec_crypt__cert_management
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide functionality to manage a set of signed and verified
   (trusted) certificates.

Key Management
--------------

.. feat_req:: Secure Key Generation
   :id: feat_req__sec_crypt__key_generation
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the secure generation of key material.

.. feat_req:: Secure Key Import
   :id: feat_req__sec_crypt__key_import
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the secure import of key material.

.. feat_req:: Secure Key Storage
   :id: feat_req__sec_crypt__key_storage
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the secure storage of key material.

.. feat_req:: Secure Key Deletion
   :id: feat_req__sec_crypt__key_deletion
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the secure deletion of key material.

.. feat_req:: API to allow selection of different algorithms
   :id: feat_req__sec_crypt__flexible_api
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The API of the security component shall allow a selection of the available
   algorithms based on their unique name.

Non-Functional Requirements
---------------------------

 .. feat_req:: Performance benchmark tooling
   :id: feat_req__sec_crypt__performance_tooling
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall contain a set of extendable benchmark tests to derive KPIs from
   running all it's cryptographic operations on different systems.

.. feat_req:: Standardized Algorithm Naming
   :id: feat_req__sec_crypt__algo_naming
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall use a uniform and unambiguous naming scheme for cryptographic
   algorithms.

.. feat_req:: No Key Material Exposure
   :id: feat_req__sec_crypt__no_key_exposure
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The API of the security component shall not reveal key material to its users.

.. feat_req:: Side-Channel Attack Mitigation
   :id: feat_req__sec_crypt__side_channel_mitigation
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall be designed to mitigate side-channel and timing attacks.

.. feat_req:: API Lifecycle Management
   :id: feat_req__sec_crypt__api_lifecycle
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component API shall provide clear mechanisms for initialization, context management
    (request, reuse, release), and de-initialization of cryptographic resources.

.. feat_req:: Structured Error Handling
   :id: feat_req__sec_crypt__error_handling
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide a structured and consistent mechanism for error reporting
   and logging.

.. feat_req:: Security Concept
   :id: feat_req__sec_crypt__security_concept
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   A security concept shall be created for the security component, including security goals,
   plausible attacks, critical failures, and countermeasures.

.. feat_req:: Crypto Algorithm Update Strategy
   :id: feat_req__sec_crypt__algo_updates
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall allow the updating of its cryptographic algorithms.

.. feat_req:: Reverse Engineering Protection
   :id: feat_req__sec_crypt__reverse_eng_protection
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall withstand reverse engineering of its secrets.

.. feat_req:: Initial Production Key Handling
   :id: feat_req__sec_crypt__production_keys
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall consider the production scenario where initial production keys are
   brought into the system.

.. feat_req:: Post-Quantum Readiness
   :id: feat_req__sec_crypt__pqc_readiness
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall be designed to be ready for post-quantum cryptography.

.. feat_req:: Hardware Acceleration Support
   :id: feat_req__sec_crypt__hw_acceleration
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall be able to rely on hardware acceleration for cryptographic
   operations.

.. feat_req:: Software Fallback
   :id: feat_req__sec_crypt__sw_fallback
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   A software-only solution for cryptographic operations shall be available as a fallback.

.. feat_req:: Trusted Time Source
   :id: feat_req__sec_crypt__trusted_time
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall have access to a trusted real-world wall clock.

.. feat_req:: OS-Level Protection
   :id: feat_req__sec_crypt__os_protection
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall use system-level means (e.g., co-processor, HSM, TEE) to protect
   its memory and CPU from applications and the normal operating system.

.. feat_req:: Access Control
   :id: feat_req__sec_crypt__access_control
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support roles and capability rights management to enforce access
   control to cryptographic functions and key material.

.. feat_req:: Intrusion Detection System (IDS) Integration
   :id: feat_req__sec_crypt__ids_integration
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall provide a mechanism to report potential security anomalies or
   threats to an Intrusion Detection System (IDS).

.. feat_req:: Denial-of-Service (DoS) Mitigation
   :id: feat_req__sec_crypt__dos_mitigation
   :reqtype: Non-Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall incorporate measures to mitigate the risk of Denial-of-Service
   (DoS) attacks that could be caused by malicious messages creating exceptional computational
   load.

Secure Communication Protocols
------------------------------

.. feat_req:: TLS Support
   :id: feat_req__sec_crypt__tls_support
   :reqtype: Functional
   :security: YES
   :safety: QM
   :satisfies: stkh_req__dependability__security_features
   :status: valid

   The security component shall support the Transport Layer Security (TLS) 1.3 protocol for secure
   communication over Ethernet.
