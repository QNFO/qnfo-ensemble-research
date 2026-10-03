# Grounding block - source: 4754bfb6-49de-4f09-b1ba-8c782c19f9a6

## Research idea

From Random Quantum Codes to Explicit qLDPC Codes via Local Properties — arXiv 2609.40252v1. Auto-candidate from daily research scan; triage for QNFO research fit.

## Existing paper under revision (remediation only)

(none - new paper)

## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2609.40252&amp;start=0&amp;max_results=1

ABSTRACT: Constructing explicit codes matching the parameters of random codes has been a central and largely elusive question in coding theory. The quantum setting is even more challenging since it is highly desirable that the quantum code be an LDPC code. Local coordinate-wise linear (LCL) [Levi, Mosheiff, and Shagrithaya, FOCS 2025] witnesses provide a unifying language for many coding-theoretic properties, from distance to list decoding and list recovery. In particular, it provides a framework to study properties of random linear codes, which achieve optimal parameters for many properties of linear codes. For CSS quantum codes, however, a local witness has two distinct ranks: its physical rank before quotienting by stabilizers and its logical rank after quotienting. We develop a quantum version of the LCL framework for nested spaces $S \subseteq C$, in which local constraints are imposed on physical representatives while independence is measured in the logical quotient $C/S$. The resulting theory gives a threshold theorem for random CSS codes, and as a consequence shows that the per-sector rate threshold is equal to the classical rate threshold. We also define a quantum analogue of subspace design [Guruswami and Xing, STOC 2013] and show that they can be described in a natural manner within the quantum-LCL framework. Finally, we give explicit constructions for arbitrary folded quantum-LCL properties, in a manner similar to the LCL derandomization of [Jeronimo and Shagrithaya, STOC 2026]. As a consequence, we obtain the first explicit constructions of quantum list-decodable codes and list-recoverable codes that have optimal list sizes, in addition to explicit quantum subspace design codes. We note that all our explicit constructions are qLDPC codes, an important property for quantum error-correcting codes.

## Related literature (arXiv, real identifiers)

arXiv:2609.40252v1 | From Random Quantum Codes to Explicit qLDPC Codes via Local Properties
  Constructing explicit codes matching the parameters of random codes has been a central and largely elusive question in coding theory. The quantum setting is even more challenging since it is highly desirable that the quantum code be an LDPC code. Local coordinate-wise linear (LCL) [Levi, Mosheiff, and Shagrithaya, FOCS 2025] witnesses provide a unifying language for many coding-theoretic propertie
arXiv:2111.07029v2 | Finite Rate QLDPC-GKP Coding Scheme that Surpasses the CSS Hamming Bound
  Quantum error correction has recently been shown to benefit greatly from specific physical encodings of the code qubits. In particular, several researchers have considered the individual code qubits being encoded with the continuous variable GottesmanKitaev-Preskill (GKP) code, and then imposed an outer discrete-variable code such as the surface code on these GKP qubits. Under such a concatenation
arXiv:2210.14143v2 | Entanglement Purification with Quantum LDPC Codes and Iterative Decoding
  Recent constructions of quantum low-density parity-check (QLDPC) codes provide optimal scaling of the number of logical qubits and the minimum distance in terms of the code length, thereby opening the door to fault-tolerant quantum systems with minimal resource overhead. However, the hardware path from nearest-neighbor-connection-based topological codes to long-range-interaction-demanding QLDPC co
arXiv:2605.03180v2 | Mitigating Classical Resource Costs in Quantum Error Correction via Generalized qLDPC Predecoding
  Large-scale fault-tolerant quantum computing (FTQC) will require quantum-classical interfaces (QCIs) that orchestrate real-time decoding over thousands to millions of logical qubits simultaneously. To scale FTQC systems, complex decoding resources must be shared between logical qubits, creating resource contention bottlenecks in the QCI. Mitigating this contention via optimal resource allocation r
arXiv:2305.00137v6 | Spatially-Coupled QLDPC Codes
  Spatially-coupled (SC) codes is a class of convolutional LDPC codes that has been well investigated in classical coding theory thanks to their high performance and compatibility with low-latency decoders. We describe toric codes as quantum counterparts of classical two-dimensional spatially-coupled (2D-SC) codes, and introduce spatially-coupled quantum LDPC (SC-QLDPC) codes as a generalization. We
arXiv:2510.19442v3 | Accelerating Fault-Tolerant Quantum Computation with Good qLDPC Codes
  We propose a fault-tolerant quantum computation scheme that is broadly applicable to quantum low-density parity-check (qLDPC) codes. The scheme achieves constant qubit overhead and a time overhead of $O(d^{a+o(1)})$ for any $[[n,k,d]]$ qLDPC code with constant encoding rate and distance $d = Ω(n^{1/a})$. For good qLDPC codes, the time overhead is minimized and reaches $O(d^{1+o(1)})$. In contrast,
arXiv:2509.17223v2 | Fusion-based implementation of qLDPC codes with quantum emitters
  Quantum low-density parity check (qLDPC) codes offer higher encoding rate than topological codes, e.g. surface codes, making them favourable for practical, fault-tolerant quantum computing with low overhead. These codes are particularly well-suited for fusion-based photonic implementations as this platform readily supports non-local connections. We propose an architecture specifically tailored to 
arXiv:2404.17676v2 | Toward a 2D Local Implementation of Quantum LDPC Codes
  Geometric locality is an important theoretical and practical factor for quantum low-density parity-check (qLDPC) codes which affects code performance and ease of physical realization. For device architectures restricted to 2D local gates, naively implementing the high-rate codes suitable for low-overhead fault-tolerant quantum computing incurs prohibitive overhead. In this work, we present an erro

## QNFO corpus context (Vectorize)

QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending
  X3.3 — Resource-commensurable comparison of bosonic codes vs surface codes using photons/logical-qubit metric at p_L=10^-6. Bosonic codes require 5-40x fewer photons and ~100x fewer modes. Novel claim: HO as QM IR attractor implies bosonic codes are the native encoding.
QNFO: Extending v_p^max Code Classification: Testing the Mahler Spectral Conjecture on Additional Stabilizer Code Families | DOI 10.5281/zenodo.21754148
  ACRP-06: Tests UF paper C7.3 on 8 additional codes. Golay CSS confirmed v_p^max=28; all other stabilizer codes cluster at random baseline (1-6). C7.3 bound to Golay-type self-dual codes.
QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle
  
QNFO: Qudit Quantum Error Correction | DOI 10.5281/zenodo.22749408
  Extends the Ultrametric Foundation thesis into quantum computing. Formalizes geometric error confinement on tree-topology quantum processors.

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.40252&amp;start=0&amp;max_results=1

ABSTRACT: Constructing explicit codes matching the parameters of random codes has been a central and largely elusive question in coding theory. The quantum setting is even more challenging since it is highly desirable that the quantum code be an LDPC code. Local coordinate-wise linear (LCL) [Levi, Mosheiff, and Shagrithaya, FOCS 2025] witnesses provide a unifying language for many coding-theoretic properties, from distance to list decoding and list recovery. In particular, it provides a framework to study properties of random linear codes, which achieve optimal parameters for many properties of linear codes. For CSS quantum codes, however, a local witness has two distinct ranks: its physical rank before quotienting by stabilizers and its logical rank after quotienting. We develop a quantum version of the LCL framework for nested spaces $S \subseteq C$, in which local constraints are imposed on physical representatives while independence is measured in the logical quotient $C/S$. The resulting theory gives a threshold theorem for random CSS codes, and as a consequence shows that the per-sector ra
[2] arXiv:2609.40252v1 | From Random Quantum Codes to Explicit qLDPC Codes via Local Properties
  Constructing explicit codes matching the parameters of random codes has been a central and largely elusive question in coding theory. The quantum setting is even more challenging since it is highly desirable that the quantum code be an LDPC code. Local coordinate-wise linear (LCL) [Levi, Mosheiff, and Shagrithaya, FOCS 2025] witnesses provide a unifying language for many coding-theoretic propertie
[3] arXiv:2111.07029v2 | Finite Rate QLDPC-GKP Coding Scheme that Surpasses the CSS Hamming Bound
  Quantum error correction has recently been shown to benefit greatly from specific physical encodings of the code qubits. In particular, several researchers have considered the individual code qubits being encoded with the continuous variable GottesmanKitaev-Preskill (GKP) code, and then imposed an outer discrete-variable code such as the surface code on these GKP qubits. Under such a concatenation
[4] arXiv:2210.14143v2 | Entanglement Purification with Quantum LDPC Codes and Iterative Decoding
  Recent constructions of quantum low-density parity-check (QLDPC) codes provide optimal scaling of the number of logical qubits and the minimum distance in terms of the code length, thereby opening the door to fault-tolerant quantum systems with minimal resource overhead. However, the hardware path from nearest-neighbor-connection-based topological codes to long-range-interaction-demanding QLDPC co
[5] arXiv:2605.03180v2 | Mitigating Classical Resource Costs in Quantum Error Correction via Generalized qLDPC Predecoding
  Large-scale fault-tolerant quantum computing (FTQC) will require quantum-classical interfaces (QCIs) that orchestrate real-time decoding over thousands to millions of logical qubits simultaneously. To scale FTQC systems, complex decoding resources must be shared between logical qubits, creating resource contention bottlenecks in the QCI. Mitigating this contention via optimal resource allocation r
[6] arXiv:2305.00137v6 | Spatially-Coupled QLDPC Codes
  Spatially-coupled (SC) codes is a class of convolutional LDPC codes that has been well investigated in classical coding theory thanks to their high performance and compatibility with low-latency decoders. We describe toric codes as quantum counterparts of classical two-dimensional spatially-coupled (2D-SC) codes, and introduce spatially-coupled quantum LDPC (SC-QLDPC) codes as a generalization. We
[7] arXiv:2510.19442v3 | Accelerating Fault-Tolerant Quantum Computation with Good qLDPC Codes
  We propose a fault-tolerant quantum computation scheme that is broadly applicable to quantum low-density parity-check (qLDPC) codes. The scheme achieves constant qubit overhead and a time overhead of $O(d^{a+o(1)})$ for any $[[n,k,d]]$ qLDPC code with constant encoding rate and distance $d = Ω(n^{1/a})$. For good qLDPC codes, the time overhead is minimized and reaches $O(d^{1+o(1)})$. In contrast,
[8] arXiv:2509.17223v2 | Fusion-based implementation of qLDPC codes with quantum emitters
  Quantum low-density parity check (qLDPC) codes offer higher encoding rate than topological codes, e.g. surface codes, making them favourable for practical, fault-tolerant quantum computing with low overhead. These codes are particularly well-suited for fusion-based photonic implementations as this platform readily supports non-local connections. We propose an architecture specifically tailored to 
[9] arXiv:2404.17676v2 | Toward a 2D Local Implementation of Quantum LDPC Codes
  Geometric locality is an important theoretical and practical factor for quantum low-density parity-check (qLDPC) codes which affects code performance and ease of physical realization. For device architectures restricted to 2D local gates, naively implementing the high-rate codes suitable for low-overhead fault-tolerant quantum computing incurs prohibitive overhead. In this work, we present an erro
[10] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending
  X3.3 — Resource-commensurable comparison of bosonic codes vs surface codes using photons/logical-qubit metric at p_L=10^-6. Bosonic codes require 5-40x fewer photons and ~100x fewer modes. Novel claim: HO as QM IR attractor implies bosonic codes are the native encoding.
[11] QNFO: Extending v_p^max Code Classification: Testing the Mahler Spectral Conjecture on Additional Stabilizer Code Families | DOI 10.5281/zenodo.21754148
  ACRP-06: Tests UF paper C7.3 on 8 additional codes. Golay CSS confirmed v_p^max=28; all other stabilizer codes cluster at random baseline (1-6). C7.3 bound to Golay-type self-dual codes.
[12] QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle
  
[13] QNFO: Qudit Quantum Error Correction | DOI 10.5281/zenodo.22749408
  Extends the Ultrametric Foundation thesis into quantum computing. Formalizes geometric error confinement on tree-topology quantum processors.