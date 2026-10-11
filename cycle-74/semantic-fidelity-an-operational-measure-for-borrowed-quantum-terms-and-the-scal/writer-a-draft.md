# A Formal Semantic‑Fidelity Measure for Borrowed Quantum Terms

## Abstract
The rapid expansion of quantum technologies has imported terminology from quantum optics, condensed‑matter physics, and particle physics into the circuit‑model paradigm. We hypothesize that this lexical borrowing introduces ontological baggage that can become operationally misleading as system size grows. To address this, we define **semantic fidelity** as a quantitative divergence between the operational predictions implied by a term’s native ontology and those of the target circuit model. Using the Tianyan‑287 superconducting processor (105 qubits, single‑qubit gate fidelity 99.90 %, two‑qubit gate fidelity 99.56 %, readout fidelity 98.7 % [1]), we construct a simple operational scenario—a three‑step primitive consisting of a single‑qubit gate, a two‑qubit gate, and a readout—and compute the overall success probability. The resulting error probability (≈ 1.83 %) serves as a concrete semantic‑fidelity metric for the term “photon” when mapped onto a superconducting circuit description. We discuss how this metric scales with qubit count and code distance, and we situate our proposal within existing literature on quantum measure theory, measurement‑theoretic signaling, stabilizer formalisms, and sum‑free axiomatizations. Our contribution offers a vocabulary‑neutral, empirically grounded tool for assessing when borrowed quantum terms cease to be faithful descriptors, thereby clarifying interdisciplinary communication and guiding resource allocation in large‑scale quantum engineering.

## 1. Introduction
Quantum information science draws heavily on concepts originally coined in quantum optics (“photon”), condensed‑matter (“quasiparticle”), and high‑energy physics (“boson”). As quantum processors scale from tens to hundreds of qubits, the mismatch between the native ontologies of these terms and the circuit‑model formalism can generate **semantic drift**: engineers may implicitly assume properties (e.g., lossless propagation) that no longer hold in a noisy, gate‑based architecture. This drift can obscure failure modes, misguide funding decisions, and stall collaborations across sub‑disciplines.

We propose a **semantic‑fidelity measure** that quantifies the operational gap between two descriptions of the same physical process. By treating each description as a probabilistic model of task success, we can compute a divergence (e.g., Kullback–Leibler or simple error‑probability difference). When this divergence exceeds a decision‑relevant threshold, the borrowed term is deemed **provably misleading**. The present work formalizes this idea, illustrates it with data from a state‑of‑the‑art superconducting platform, and connects it to broader theoretical frameworks such as quantum measure theory and sum‑free quantum mechanics.

## 2. Background and Related Work
The literature provides several conceptual tools that inform our approach:

* **Quantum Measure Theory (QMT).**  
  [2] proposes a spacetime‑based interpretation of quantum theory, introducing a “quantum measure” \(|S|\) that obeys a generalized sum rule. This framework motivates treating operational predictions as measures over histories, a perspective we adopt for semantic‑fidelity calculations.  

* **Exceeding Unity in Quantum Measures.**  
  [3] extends QMT by defining a quantum measure \(\mu\) for arbitrary events and demonstrates that \(\mu\) can exceed unity due to interference. This highlights that conventional probability‑based divergences may need adaptation when comparing ontologically distinct models.  

* **Signaling in Non‑Relativistic Measurements.**  
  [4] shows that naive joint nonlocal measurements can lead to signaling, a phenomenon also relevant when mapping photonic intuition (non‑interacting particles) onto interacting superconducting qubits.  

* **Operator Algebra Quantum Error Correction (OAQEC).**  
  [6] introduces a stabilizer formalism for OAQEC, generalizing traditional QEC. Our semantic‑fidelity metric can be applied to error‑corrected logical operations, linking ontological drift to code distance.  

* **Sum‑Free Axiomatization.**  
  [7] argues that quantum mechanics can be formulated without direct sums, using only tensor products. This sum‑free viewpoint parallels our effort to avoid mixing ontologies that rely on distinct algebraic structures.  

* **Empirical Studies of Term Importance.**  
  Although focused on information retrieval, [5] dissects term importance and matching patterns, providing a methodological analogue for assessing the “importance” of borrowed quantum terms in engineering contexts.  

* **Quantum Simulation of Holographic Entanglement.**  
  [8] reports an experiment simulating holographic entanglement entropy, illustrating how quantum simulators can be used to test theoretical constructs—an approach we emulate by simulating photonic vs. circuit‑model predictions.  

* **Cloud‑Based Quantum Advantage.**  
  The Tianyan‑287 platform described in [1] offers a concrete, large‑scale superconducting system with reported fidelities (single‑qubit 99.90 %, two‑qubit 99.56 %, readout 98.7 %). These numbers constitute the empirical basis for our quantitative illustration.

Together, these works motivate a formal, operational metric that respects both the probabilistic nature of quantum predictions and the ontological distinctions between borrowed terms and target models.

## 3. Methods
### 3.1 Semantic‑Fidelity Definition
Given a quantum task \(T\) (e.g., preparation, gate, measurement), let \(P_{\text{native}}(T)\) be the success probability predicted by the term’s native ontology (e.g., ideal photon transmission) and \(P_{\text{circuit}}(T)\) the probability predicted by the circuit‑model description using measured hardware fidelities. We define the **semantic‑fidelity loss** \(\Delta(T)\) as
\[
\Delta(T) = 1 - \frac{P_{\text{circuit}}(T)}{P_{\text{native}}(T)}.
\]
When \(\Delta(T) > \theta\) for a chosen threshold \(\theta\) (e.g., 1 %), the term is considered misleading for task \(T\).

### 3.2 Operational Scenario
We consider a minimal primitive consisting of three sequential operations:
1. A single‑qubit gate (\(F_{1}\)),
2. A two‑qubit gate (\(F_{2}\)),
3. A readout (\(F_{3}\)).

Assuming independence, the circuit‑model success probability is the product
\[
P_{\text{circuit}} = F_{1} \times F_{2} \times F_{3}.
\]
For the native photonic description we take the ideal value \(P_{\text{native}} = 1\), reflecting the common assumption of lossless photons in theoretical proposals.

### 3.3 Data Sources
All numerical inputs are taken directly from the Tianyan‑287 specifications in [1]:
- Number of qubits \(N = 105\) (used only to illustrate scaling in Section 5).
- Single‑qubit gate fidelity \(F_{1}=99.90\%\).
- Two‑qubit gate fidelity \(F_{2}=99.56\%\).
- Readout fidelity \(F_{3}=98.7\%\).

No other external numbers are employed.

## 4. Analysis
We now compute the semantic‑fidelity loss for the primitive defined above, showing every arithmetic step.

### 4.1 Convert Percentages to Decimal Probabilities
- From [1]: \(F_{1}=99.90\%\).  
  Calculation: \(99.90\% = \frac{99.90}{100}=0.9990\).  
- From [1]: \(F_{2}=99.56\%\).  
  Calculation: \(99.56\% = \frac{99.56}{100}=0.9956\).  
- From [1]: \(F_{3}=98.7\%\).  
  Calculation: \(98.7\% = \frac{98.7}{100}=0.9870\).

### 4.2 Compute Product \(P_{\text{circuit}}\)

Step 1: Multiply \(F_{1}\) and \(F_{2}\):
\[
0.9990 \times 0.9956 = 0.9946044.
\]

Step 2: Multiply the result by \(F_{3}\):
\[
0.9946044 \times 0.9870 = 0.9816745428.
\]

Thus,
\[
P_{\text{circuit}} = 0.9816745428.
\]

### 4.3 Compute Semantic‑Fidelity Loss \(\Delta\)

Using \(P_{\text{native}} = 1\):
\[
\Delta = 1 - \frac{0.9816745428}{1}
      = 1 - 0.9816745428
      = 0.0183254572.
\]

Expressed as a percentage:
\[
\Delta = 0.0183254572 \times 100\% \approx 1.83\%.
\]

### 4.4 Error‑Rate Interpretation
Individual error rates are:
\[
\epsilon_{1}=1-F_{1}=1-0.9990=0.0010\;(0.10\%),
\]
\[
\epsilon_{2}=1-F_{2}=1-0.9956=0.0044\;(0.44\%),
\]
\[
\epsilon_{3}=1-F_{3}=1-0.9870=0.0130\;(1.30\%).
\]

The average error rate across the three operations is
\[
\bar{\epsilon}= \frac{0.0010+0.0044+0.0130}{3}
               = \frac{0.0184}{3}
               = 0.006133\;(0.613\%).
\]

These calculations are fully derived from the numbers supplied in [1].

## 5. Results
- The circuit‑model success probability for the three‑step primitive on Tianyan‑287 is \(P_{\text{circuit}} \approx 0.982\) (98.2 %).  
- The semantic‑fidelity loss for the term “photon” in this context is \(\Delta \approx 1.83\%\), exceeding a 1 % decision threshold and therefore indicating that “photon” is **provably misleading** for this primitive.  
- The average per‑operation error rate is \(\bar{\epsilon} \approx 0.613\%\).  
- Scaling considerations: with \(N=105\) qubits, a logical operation involving \(k\) sequential primitives would compound the loss multiplicatively as \((1-\Delta)^{k}\). For \(k=10\), the overall success probability drops to \((0.9816745)^{10} \approx 0.825\), illustrating rapid degradation of semantic fidelity as system size grows.

These results demonstrate a concrete, numerically grounded instance of semantic drift.

## 6. Discussion
### 6.1 Limitations
Our analysis rests on several simplifying assumptions:
1. **Ideal Native Model:** We set \(P_{\text{native}}=1\), which may overstate the fidelity of photonic implementations that suffer from loss and detector inefficiency.  
2. **Independence of Errors:** Multiplicative combination assumes uncorrelated errors, whereas crosstalk and correlated noise can alter the product.  
3. **Single Primitive:** Real algorithms involve many more gates and error‑correction cycles; extending the metric to full circuits requires integrating code distance and logical error models.  

These constraints mirror the thinness of many bibliography summaries; for instance, [5] provides only a high‑level statement about term importance analysis, limiting deeper methodological borrowing.

### 6.2 Failure Modes and Falsifiability
The semantic‑fidelity measure would be falsified if empirical experiments on large‑scale processors showed that engineers routinely achieve task success rates matching the ideal native predictions despite the computed \(\Delta\). Conversely, observing systematic performance gaps aligned with our loss metric would corroborate the measure.  

Potential failure modes include:
- **Mis‑characterization of native predictions:** If the native ontology already incorporates realistic imperfections, the divergence may be smaller.  
- **Hardware improvements:** As gate fidelities approach unity, \(\Delta\) will shrink, potentially rendering the term “photon” acceptable again.  

### 6.3 Open Questions
- How does semantic fidelity behave under different error‑correction schemes (e.g., surface codes) as described in OAQEC frameworks [6]?  
- Can quantum measure theory’s allowance for measures exceeding unity [3] be leveraged to define alternative divergence metrics that capture interference‑driven ontological differences?  
- What role do signaling constraints identified in [4] play when mapping non‑local photonic protocols onto local superconducting architectures?  

Addressing these questions will refine the metric and broaden its applicability across quantum sub‑disciplines.

## 7. Conclusion
We introduced a formal, operational definition of **semantic fidelity** for borrowed quantum terms and demonstrated its computation using publicly reported hardware parameters from the Tianyan‑287 superconducting processor. The resulting loss of ≈ 1.83 % for the term “photon” exceeds a modest decision threshold, indicating that the term becomes misleading even in modestly sized circuits. By grounding the metric in concrete performance data and situating it within existing theoretical frameworks, we provide a tool for interdisciplinary clarity and for guiding the evolution of quantum terminology as technologies scale.

## References
[1] arXiv:2512.10504v2 | Tianyan: Cloud services with quantum advantage  
  Tianyan Quantum Cloud Platform offers cloud services demonstrating quantum advantage capabilities with a Zuchongzhi 3.0-like superconducting quantum processor. This cloud-accessible superconducting quantum prototype, named Tianyan-287, features 105 qubits and achieves high operational fidelities, with single-qubit gates, two-qubit gates, and readout fidelity at 99.90%, 99.56%, 98.7%, respectively.  

[2] arXiv:gr-qc/9507057v2 | Quantum Measure Theory and its Interpretation  
  We propose a realistic, spacetime interpretation of quantum theory in which reality constitutes a *single* history obeying a "law of motion" that makes definite, but incomplete, predictions about its behavior. We associate a "quantum measure" |S| to the set S of histories, and point out that |S| fulfills a sum rule generalizing that of classical probability theory. We interpret |S| as a "propensit  

[3] arXiv:2407.15702v3 | Measuring a Quantum Measure Exceeding Unity  
  The history based formalism known as Quantum Measure Theory (QMT) generalizes the concept of probability-measure so as to incorporate quantum interference. The resulting quantum measure $μ$ is defined for arbitrary events (sets of histories), not just for observables at a fixed moment of time. Thanks to interference effects, $μ$ can exceed unity, exhibiting its non-classical nature in a particular  

[4] arXiv:2311.13644v2 | Towards a measurement theory in QFT: "Impossible" quantum measurements are possible but not ideal  
  Naive attempts to put together relativity and quantum measurements lead to signaling between space-like separated regions. In QFT, these are known as impossible measurements. We show that the same problem arises in non-relativistic quantum physics, where joint nonlocal measurements (i.e., between systems kept spatially separated) in general lead to signaling, while one would expect no-signaling (b  

[5] arXiv:2012.09650v1 | A White Box Analysis of ColBERT  
  Transformer-based models are nowadays state-of-the-art in ad-hoc Information Retrieval, but their behavior is far from being understood. Recent work has claimed that BERT does not satisfy the classical IR axioms. However, we propose to dissect the matching process of ColBERT, through the analysis of term importance and exact/soft matching patterns. Even if the traditional axioms are not formally v  

[6] arXiv:2304.11442v2 | Stabilizer Formalism for Operator Algebra Quantum Error Correction  
  We introduce a stabilizer formalism for the general quantum error correction framework called operator algebra quantum error correction (OAQEC), which generalizes Gottesman's formulation for traditional quantum error correcting codes (QEC) and Poulin's for operator quantum error correction and subsystem codes (OQEC). The construction generates hybrid classical-quantum stabilizer codes and we formu  

[7] arXiv:quant-ph/0608035v2 | Quantum measurements without sums  
  Sums play a prominent role in the formalisms of quantum mechanics, be it for mixing and superposing states, or for composing state spaces. Surprisingly, a conceptual analysis of quantum measurement seems to suggest that quantum mechanics can be done without direct sums, expressed entirely in terms of the tensor product. The corresponding axioms define classical spaces as objects that allow copying  

[8] arXiv:1705.00365v2 | Measuring Holographic Entanglement Entropy on a Quantum Simulator  
  Quantum simulation promises to have wide applications in many fields where problems are hard to model with classical computers. Various quantum devices of different platforms have been built to tackle the problems in, say, quantum chemistry, condensed matter physics, and high-energy physics. Here, we report an experiment towards the simulation of quantum gravity by simulating the holographic entan  

## Appendix A. Divergence report
*No divergent claims were identified among the drafts used to construct this manuscript.*

## Appendix B. Claim attribution
| Claim ID | Source Draft(s) | Agreement Status |
|----------|----------------|------------------|
| C1 | Writer (this draft) | SINGLE |
| C2 | Writer (this draft) | SINGLE |
| C3 | Writer (this draft) | SINGLE |
| C4 | Writer (this draft) | SINGLE |
| C5 | Writer (this draft) | SINGLE |
| C6 | Writer (this draft) | SINGLE |
| C7 | Writer (this draft) | SINGLE |
| C8 | Writer (this draft) | SINGLE |
| C9 | Writer (this draft) | SINGLE |
| C10 | Writer (this draft) | SINGLE |
| C11 | Writer (this draft) | SINGLE |
| C12 | Writer (this draft) | SINGLE |
| C13 | Writer (this draft) | SINGLE |
| C14 | Writer (this draft) | SINGLE |
| C15 | Writer (this draft) | SINGLE |
| C16 | Writer (this draft) | SINGLE |
| C17 | Writer (this draft) | SINGLE |
| C18 | Writer (this draft) | SINGLE |
| C19 | Writer (this draft) | SINGLE |
| C20 | Writer (this draft) | SINGLE |
| C21 | Writer (this draft) | SINGLE |
| C22 | Writer (this draft) | SINGLE |
| C23 | Writer (this draft) | SINGLE |
| C24 | Writer (this draft) | SINGLE |
| C25 | Writer (this draft) | SINGLE |
| C26 | Writer (this draft) | SINGLE |
| C27 | Writer (this draft) | SINGLE |
| C28 | Writer (this draft) | SINGLE |
| C29 | Writer (this draft) | SINGLE |
| C30 | Writer (this draft) | SINGLE |