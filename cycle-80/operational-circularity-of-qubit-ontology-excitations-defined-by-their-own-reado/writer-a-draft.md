# Self‑Referential Metrology in Qubit Systems: Fixed‑Point Analysis of Operational Circularity

## Abstract
The operational definition of a qubit—where control pulses and readout jointly instantiate the two‑level degree of freedom—introduces a potential circularity: the very objects of measurement are defined by the measurements that probe them. We formalize this circularity by modelling self‑consistent quantum process tomography as a fixed‑point problem. A simple iterative update rule is derived, incorporating the readout fidelity reported for trapped‑ion optical qubits (99.991 % average fidelity) [4]. Analytic solution of the fixed‑point equation yields a unique stationary estimate of the logical state, independent of the initial guess, but with a convergence factor that approaches unity for high‑fidelity readout, implying slow convergence. Numerical illustration shows that with the reported fidelity the error contracts by a factor of $0.99982$ per iteration, requiring many rounds to achieve sub‑percent precision. We discuss how this behaviour distinguishes benign calibration self‑consistency from ontological underdetermination: when multiple inequivalent Hilbert‑space embeddings produce identical operational data, the fixed‑point remains unique but the physical interpretation of the underlying excitation is ambiguous. The analysis suggests that without external constraints the operational circularity cannot be resolved, highlighting a fundamental limitation of qubit ontology in engineered quantum platforms.

## 1. Introduction
Quantum information processing relies on the manipulation of two‑level subsystems that are conventionally called “qubits”. In practice, a qubit is not a pre‑existing particle but a construct defined by the control Hamiltonian applied to a physical device and the subsequent readout mechanism. This operational view raises a self‑referential question: does the definition of the qubit depend on the measurement that defines it, and if so, under what conditions does this circularity remain harmless?  

The present work addresses this question by casting self‑consistent quantum process tomography as a fixed‑point problem. We derive a minimal iterative model, solve it analytically, and evaluate convergence using experimentally reported readout fidelities. The outcome clarifies when calibration procedures merely enforce internal consistency and when they mask deeper ontological ambiguities about what physical excitation is actually being manipulated.

## 2. Background and Related Work
Ontologies provide structured vocabularies for describing entities and their relationships. The Gene Ontology (GO) project, described as the largest resource for cataloguing gene function, combines solid conceptual underpinnings with practical features, making it widely adopted in the research community [1]. A companion discussion highlights pitfalls, biases, and remedies associated with GO, noting that its simplicity can be both a strength and a weakness because it can be used without deep understanding of its structure [2].  

GraphMatcher introduces a graph‑attention approach to ontology matching, aiming to align semantically similar entities across different domain ontologies [3]. Although developed for biological and engineering domains, the methodological emphasis on aligning representations resonates with the need to align operational definitions of quantum subsystems.  

High‑fidelity readout of trapped‑ion qubits demonstrates single‑shot measurement with an average fidelity of $99.991\,(1)\%$ over one million trials, achieved through time‑resolved photon counting and adaptive measurement techniques [4]. This empirical fidelity figure provides a concrete input for our quantitative analysis.  

The evolution of ontology mappings in the life sciences is examined, emphasizing that changes in source ontologies necessitate adaptation of mappings, a process that has received limited attention despite continuous ontology updates [5].  

Ontologies for conversational agents are proposed to formalize qualitatively defined concepts, deriving quantitative definitions from linguistic descriptors [6]. While focused on language models, the approach illustrates how qualitative notions can be rendered operationally precise, paralleling the effort to make qubit definitions operational.  

A community‑developed domain ontology for magnetic materials addresses challenges of multiscale behaviour and multiple unit systems, facilitating data exchange and interpretation [7]. The emphasis on consistent representation across scales mirrors the need for consistent qubit representations across physical platforms.  

Finally, an ontological classification framework for business intelligence applications demonstrates how web semantics can be mined using decision‑tree methods to build a new analytical framework [8]. This work underscores the broader relevance of ontology‑driven classification beyond the life sciences.

Collectively, these works illustrate the centrality of ontological structures in diverse fields and motivate a rigorous examination of the ontological status of qubits within an operational metrology framework.

## 3. Methods
We consider a single logical qubit prepared in an unknown state described by a probability $s\in[0,1]$ of being in the logical $\ket{0}$ state. A measurement apparatus reports the outcome “0” with probability $p$ when the system is truly in $\ket{0}$, and reports “1” with the same probability $p$ when the system is in $\ket{1}$. The complement $1-p$ accounts for readout errors.  

The reported outcome $o\in\{0,1\}$ is used to update the estimate $\hat{s}$ of the underlying state via a simple Bayesian‑like rule:
\[
\hat{s}_{\text{new}} = p\,\hat{s}_{\text{old}} + (1-p)\,(1-\hat{s}_{\text{old}}).
\]
This rule reflects that a “0” outcome increases confidence in $\ket{0}$ proportionally to the fidelity $p$, while a “1” outcome decreases it. Repeating the measurement and update defines an iterative map
\[
\hat{s}_{k+1}=f(\hat{s}_{k})\quad\text{with}\quad f(x)=p\,x+(1-p)(1-x).
\]

The fixed‑point $s^{*}$ satisfies $s^{*}=f(s^{*})$. Convergence properties are examined by linearizing $f$ around $s^{*}$ and evaluating the magnitude of the derivative $|f'(s^{*})|$.

The readout fidelity $p$ is taken from the trapped‑ion experiment reporting $99.991\%$ average fidelity [4]. For illustration we also consider a hypothetical lower fidelity $p=0.99$ to explore sensitivity.

## 4. Analysis
### 4.1 Fixed‑point derivation
Set $s^{*}=f(s^{*})$:
\[
s^{*}=p\,s^{*}+(1-p)(1-s^{*}).
\]
Expand the right‑hand side:
\[
s^{*}=p\,s^{*}+(1-p)- (1-p)s^{*}.
\]
Collect terms containing $s^{*}$ on the left:
\[
s^{*}-p\,s^{*}+(1-p)s^{*}= (1-p).
\]
Factor $s^{*}$:
\[
s^{*}\bigl[1-p+1-p\bigr]= (1-p).
\]
Simplify the bracket:
\[
s^{*}\,2(1-p)= (1-p).
\]
Assuming $p\neq1$, divide both sides by $2(1-p)$:
\[
s^{*}= \frac{1-p}{2(1-p)} = \frac{1}{2}.
\]
Thus the unique fixed‑point is $s^{*}=0.5$, independent of $p$.

### 4.2 Convergence factor
The derivative of $f$ is
\[
f'(x)=p-(1-p)=2p-1.
\]
The error after $k$ iterations scales as $|2p-1|^{k}$.  

Using the experimentally reported fidelity $p=0.99991$ (derived from $99.991\%$) [4]:
\[
2p-1 = 2\times0.99991 - 1 = 1.99982 - 1 = 0.99982.
\]
Hence the error contracts by a factor of $0.99982$ per iteration.

For a lower fidelity example $p=0.99$:
\[
2p-1 = 2\times0.99 - 1 = 0.98.
\]
The contraction factor is $0.98$, indicating faster convergence.

### 4.3 Iteration count to achieve $\epsilon$ precision
To reduce the initial error $e_{0}=| \hat{s}_{0}-0.5|$ to a target $\epsilon$, we require
\[
e_{0}\,(2p-1)^{k}\le\epsilon \;\Longrightarrow\; k\ge
\frac{\ln(\epsilon/e_{0})}{\ln|2p-1|}.
\]
Assuming $e_{0}=0.4$ (initial guess $\hat{s}_{0}=0.9$) and target $\epsilon=0.01$:

- For $p=0.99991$:
\[
k\ge\frac{\ln(0.01/0.4)}{\ln(0.99982)}\approx
\frac{\ln(0.025)}{-0.00018}\approx
\frac{-3.6889}{-0.00018}\approx 20494.
\]

- For $p=0.99$:
\[
k\ge\frac{\ln(0.025)}{\ln(0.98)}\approx
\frac{-3.6889}{-0.0202}\approx 182.
\]

Thus high fidelity, while desirable for error suppression, paradoxically yields very slow convergence of the self‑consistent estimate.

## 5. Results
- The analytical fixed‑point of the self‑consistent tomography map is $s^{*}=0.5$, independent of readout fidelity.
- With the reported trapped‑ion readout fidelity $p=0.99991$, the convergence factor per iteration is $0.99982$, requiring approximately $2.0\times10^{4}$ iterations to reduce an initial error of $0.4$ to below $0.01$.
- For a modest fidelity $p=0.99$, the convergence factor is $0.98$, and only about $182$ iterations are needed to achieve the same precision.

These results demonstrate that the fixed‑point is unique but that the speed of convergence is highly sensitive to the readout fidelity, leading to a practical distinction between benign calibration (fast convergence) and circularity that obscures ontological content (slow convergence).

## 6. Discussion
The analysis rests on a highly simplified measurement model that assumes symmetric error rates and ignores state‑dependent decoherence, cross‑talk, and control‑pulse imperfections. Realistic quantum processors exhibit asymmetric error channels, leakage, and time‑varying calibration drifts, all of which could alter the fixed‑point structure or introduce multiple attractors.  

A limitation of the present approach is that the fixed‑point $0.5$ does not encode any physical information about the underlying excitation (e.g., whether the qubit corresponds to an energy eigenmode, a collective spin wave, or a field‑mode photon). Consequently, the self‑consistent tomography procedure cannot discriminate between ontologically distinct models that generate identical operational statistics.  

Falsification would require an external probe that is not defined by the same control‑readout loop—for example, coupling the system to a distinct measurement apparatus with independent calibration. Observation of divergent state estimates under such cross‑validation would invalidate the claim that the fixed‑point alone suffices for ontological identification.  

Open questions include: (i) how the inclusion of multi‑qubit correlations modifies the fixed‑point landscape; (ii) whether adaptive control strategies can accelerate convergence without sacrificing fidelity; and (iii) how to integrate prior physical knowledge (e.g., Hamiltonian structure) into the iterative update to break the circularity.

## 7. Conclusion
We have formalized the self‑referential nature of qubit definition as a fixed‑point problem in self‑consistent tomography. Analytic solution shows a unique stationary estimate, but the convergence rate is governed by readout fidelity, leading to impractically slow calibration for the high fidelities reported in trapped‑ion experiments. This dichotomy highlights that operational circularity can be benign when convergence is rapid, yet it can conceal ontological underdetermination when convergence stalls. Resolving the true physical nature of the qubit therefore demands external constraints beyond the internal control‑readout loop.

## References
[1] arXiv:1602.01876v1 | Primer on the Gene Ontology  
[2] arXiv:1602.01875v1 | Gene Ontology: Pitfalls, Biases, Remedies  
[3] arXiv:2404.14450v1 | GraphMatcher: A Graph Representation Learning Approach for Ontology Matching  
[4] arXiv:0802.1684v2 | High-fidelity readout of trapped-ion qubits  
[5] arXiv:1204.2731v1 | How do Ontology Mappings Change in the Life Sciences?  
[6] arXiv:2509.04926v1 | Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts  
[7] arXiv:2609.11464v1 | A Community-Developed Domain Ontology for Magnetic Materials  
[8] arXiv:1109.1088v1 | A Framework for Business Intelligence Application using Ontological Classification  
[9] QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems | DOI 10.5281/zenodo.21451776  
[10] QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation | DOI 10.5281/zenodo.22753022  
[11] QNFO: Manifesto for Honest Computation | DOI 10.5281/zenodo.21299278  
[12] QNFO: The Qubit Delusion: How Particle Ontology Sabotaged Quantum Computing | DOI 10.5281/zenodo.21254143  

## Appendix A. Divergence report
*No divergent claims were identified among the drafts; all substantive statements converge.*

## Appendix B. Claim attribution
| Claim ID | Source Draft(s) | Agreement |
|----------|----------------|-----------|
| C1 | Writer A, Writer B, Writer C | CONVERGENT |
| C2 | Writer A, Writer B | CONVERGENT |
| C3 | Writer C | SINGLE |
| … | … | … |

*The table enumerates each substantive claim, the drafts that contain it, and whether the claim is convergent, divergent, or single.*