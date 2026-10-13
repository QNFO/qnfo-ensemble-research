# Grounding block - source: db192bdc-5aec-489e-9798-71dc89c09800

## Research idea

Security Analysis of Unknown-Radix Encoding as a Cryptographic Primitive. The author conjectures a cipher whose secret key is the numerical radix B (plus a symbol-to-digit map) used to encode plaintext as an integer, and asks whether such 'secret base cryptography' could compete with modern or post-quantum schemes. A paper could formalize this: define the key space (admissible radices and digit mappings), compute its entropy, and prove an upper bound on security showing the scheme reduces to a monoalphabetic substitution with positional weighting, breakable by frequency analysis and brute force over plausible B. A computational study could empirically confirm ciphertext attack success rates as a function of radix size and message length, and compare against AES and lattice-based KEMs under Kerckhoffs's principle. This would rigorously establish whether radix obscurity offers any quantum-relevant advantage (it presumably does not), turning an informal comparison into a provable impossibility or separation result.

Source: owner notebook notes/v1/2026/07/26/_26207190933.md

## Existing paper under revision (remediation only)

(none - new paper)

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers)

arXiv:2607.21325v3 | Cryptographically verifiable authorization for autonomous AI agents: a falsifiable hypothesis and proof of concept
  Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight. Existing authentication and authorization mechanisms establish identity and delegate authority but do not inherently provide cryptographic evidence that a concrete request issued by a specific agent satisfies the applicable policy in a specific execution context. This s
arXiv:1003.1458v1 | Secured Cryptographic Key Generation From Multimodal Biometrics: Feature Level Fusion of Fingerprint and Iris
  Human users have a tough time remembering long cryptographic keys. Hence, researchers, for so long, have been examining ways to utilize biometric features of the user instead of a memorable password or passphrase, in an effort to generate strong and repeatable cryptographic keys. Our objective is to incorporate the volatility of the user's biometric features into the generated key, so as to make t
arXiv:1002.2527v1 | Secured Cryptographic Key Generation From Multimodal Biometrics Feature Level Fusion Of Fingerprint And Iris
  Human users have a tough time remembering long cryptographic keys. Hence, researchers, for so long, have been examining ways to utilize biometric features of the user instead of a memorable password or passphrase, in an effort to generate strong and repeatable cryptographic keys. Our objective is to incorporate the volatility of the users biometric features into the generated key, so as to make th
arXiv:2103.08436v1 | Formal Modelling and Security Analysis of Bitcoin's Payment Protocol
  The Payment Protocol standard BIP70, specifying how payments in Bitcoin are performed by merchants and customers, is supported by the largest payment processors and most widely-used wallets. The protocol has been shown to be vulnerable to refund attacks due to lack of authentication of the refund addresses. In this paper, we give the first formal model of the protocol and formalise the refund addr
arXiv:2603.22442v2 | Architecture-Derived CBOMs for Cryptographic Migration: A Security-Aware Architecture Tradeoff Method
  Cryptographic migration driven by algorithm deprecation, regulatory change, and post-quantum readiness requires more than an inventory of cryptographic assets. Existing Cryptographic Bills of Materials (CBOMs) are typically tool- or inventory-derived. They lack architectural intent, rationale, and security context, limiting their usefulness for migration planning. This paper introduces Security-Aw
arXiv:2206.02156v2 | Perspectives of Non-Expert Users on Cyber Security and Privacy: An Analysis of Online Discussions on Twitter
  Current research on users` perspectives of cyber security and privacy related to traditional and smart devices at home is very active, but the focus is often more on specific modern devices such as mobile and smart IoT devices in a home context. In addition, most were based on smaller-scale empirical studies such as online surveys and interviews. We endeavour to fill these research gaps by conduct
arXiv:2208.05586v3 | Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, &amp; Practical Key Management
  We present the first general construction of a Multi-Factor Key Derivation Function (MFKDF). Our function expands upon password-based key derivation functions (PBKDFs) with support for using other popular authentication factors like TOTP, HOTP, and hardware tokens in the key derivation process. In doing so, it provides an exponential security improvement over PBKDFs with less than 12 ms of additio
arXiv:2402.03114v1 | Augmenting Security and Privacy in the Virtual Realm: An Analysis of Extended Reality Devices
  In this work, we present a device-centric analysis of security and privacy attacks and defenses on Extended Reality (XR) devices, highlighting the need for robust and privacy-aware security mechanisms. Based on our analysis, we present future research directions and propose design considerations to help ensure the security and privacy of XR devices.

## QNFO corpus context (Vectorize)

QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle
  
QNFO: Silent-Radix Cryptography: Exploiting the Base Ambiguity of Positional Notation as a Cryptographic Primitive
  The silent radix — a positional numeral cannot internally specify its own base — is a cryptographic primitive. Silent Radix Encryption (SRE) uses a secret base b as a trapdoor for key encapsulation. Security reduces to an unknown-weight integer knapsack problem.
QNFO: HM-LWE v3.0
  Hidden-modulus LWE: novel hardness assumption

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2607.21325v3 | Cryptographically verifiable authorization for autonomous AI agents: a falsifiable hypothesis and proof of concept
  Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight. Existing authentication and authorization mechanisms establish identity and delegate authority but do not inherently provide cryptographic evidence that a concrete request issued by a specific agent satisfies the applicable policy in a specific execution context. This s
[2] arXiv:1003.1458v1 | Secured Cryptographic Key Generation From Multimodal Biometrics: Feature Level Fusion of Fingerprint and Iris
  Human users have a tough time remembering long cryptographic keys. Hence, researchers, for so long, have been examining ways to utilize biometric features of the user instead of a memorable password or passphrase, in an effort to generate strong and repeatable cryptographic keys. Our objective is to incorporate the volatility of the user's biometric features into the generated key, so as to make t
[3] arXiv:1002.2527v1 | Secured Cryptographic Key Generation From Multimodal Biometrics Feature Level Fusion Of Fingerprint And Iris
  Human users have a tough time remembering long cryptographic keys. Hence, researchers, for so long, have been examining ways to utilize biometric features of the user instead of a memorable password or passphrase, in an effort to generate strong and repeatable cryptographic keys. Our objective is to incorporate the volatility of the users biometric features into the generated key, so as to make th
[4] arXiv:2103.08436v1 | Formal Modelling and Security Analysis of Bitcoin's Payment Protocol
  The Payment Protocol standard BIP70, specifying how payments in Bitcoin are performed by merchants and customers, is supported by the largest payment processors and most widely-used wallets. The protocol has been shown to be vulnerable to refund attacks due to lack of authentication of the refund addresses. In this paper, we give the first formal model of the protocol and formalise the refund addr
[5] arXiv:2603.22442v2 | Architecture-Derived CBOMs for Cryptographic Migration: A Security-Aware Architecture Tradeoff Method
  Cryptographic migration driven by algorithm deprecation, regulatory change, and post-quantum readiness requires more than an inventory of cryptographic assets. Existing Cryptographic Bills of Materials (CBOMs) are typically tool- or inventory-derived. They lack architectural intent, rationale, and security context, limiting their usefulness for migration planning. This paper introduces Security-Aw
[6] arXiv:2206.02156v2 | Perspectives of Non-Expert Users on Cyber Security and Privacy: An Analysis of Online Discussions on Twitter
  Current research on users` perspectives of cyber security and privacy related to traditional and smart devices at home is very active, but the focus is often more on specific modern devices such as mobile and smart IoT devices in a home context. In addition, most were based on smaller-scale empirical studies such as online surveys and interviews. We endeavour to fill these research gaps by conduct
[7] arXiv:2208.05586v3 | Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, &amp; Practical Key Management
  We present the first general construction of a Multi-Factor Key Derivation Function (MFKDF). Our function expands upon password-based key derivation functions (PBKDFs) with support for using other popular authentication factors like TOTP, HOTP, and hardware tokens in the key derivation process. In doing so, it provides an exponential security improvement over PBKDFs with less than 12 ms of additio
[8] arXiv:2402.03114v1 | Augmenting Security and Privacy in the Virtual Realm: An Analysis of Extended Reality Devices
  In this work, we present a device-centric analysis of security and privacy attacks and defenses on Extended Reality (XR) devices, highlighting the need for robust and privacy-aware security mechanisms. Based on our analysis, we present future research directions and propose design considerations to help ensure the security and privacy of XR devices.
[9] QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle
  
[10] QNFO: Silent-Radix Cryptography: Exploiting the Base Ambiguity of Positional Notation as a Cryptographic Primitive
  The silent radix — a positional numeral cannot internally specify its own base — is a cryptographic primitive. Silent Radix Encryption (SRE) uses a secret base b as a trapdoor for key encapsulation. Security reduces to an unknown-weight integer knapsack problem.
[11] QNFO: HM-LWE v3.0
  Hidden-modulus LWE: novel hardness assumption