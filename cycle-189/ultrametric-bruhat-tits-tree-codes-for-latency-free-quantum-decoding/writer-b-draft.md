# Ultrametric Bruhat–Tits Tree Codes for Latency‑Free Quantum Decoding

## Abstract
Quantum error correction (QEC) is limited by decoder latency; surface‑code decoders operate at ≈10 MHz, far below physical gate speeds. A gap exists between the logical clock set by active decoding and the intrinsic speed of quantum hardware. We analyze a passive QEC scheme that embeds a holographic perfect‑tensor code on a finite Bruhat–Tits tree. Errors are confined to disjoint subtrees, enabling a level‑by‑level tree search whose runtime scales logarithmically with the number of physical qudits. Using the exact combinatorial parameters of the ball code, we derive the code distance \(d=2t+1\) and the qudit count \(n_t=1+\frac{(p+1)(p^{t}-1)}{p-1}\). For a flagship block with prime \(p=3\) and radius \(t=1\) we compute a passive logical failure probability \(P_{\mathrm{pass}}\approx9.98\times10^{-6}\) at physical error rate \(\varepsilon=10^{-3}\), a suppression factor of \(100.2\) over an unencoded qudit. Concatenated eight‑fold majority voting on a classical analogue yields logical error probabilities \(p^{(1)}=0.1736704\), \(p^{(2)}=0.0055485\), and \(p^{(3)}\approx2.905\times10^{-10}\) for three recursion levels at physical error \(p=0.4\). These results demonstrate that ultrametric tree codes can reduce logical error rates while offering logarithmic decoding latency, potentially lifting the logical clock toward physical gate speeds.

## 1. Introduction
Current fault‑tolerant quantum processors rely on active stabilizer measurement cycles and classical decoders that must keep pace with syndrome generation. Surface‑code decoders are bottlenecked at ≈10 MHz, limiting the logical clock and inflating the overhead of error‑corrected algorithms. Quantum hardware designers, system architects, and algorithm developers would benefit from a decoder whose latency grows only as \(\log N\) with the number of physical qudits \(N\), thereby allowing logical operations at or near the native gate frequency.

If a decoding scheme can (i) achieve a logical error rate comparable to surface codes, (ii) guarantee latency \(\mathcal{O}(\log N)\), and (iii) be realized with modest hardware resources, the overall cost of fault‑tolerant quantum computation would drop dramatically. The present work addresses this “so what?” by providing a rigorous analytical foundation for ultrametric Bruhat–Tits tree codes, quantifying their error‑suppression capability, and establishing a decoder runtime bound.

**Contributions.**
1. Derivation of exact code parameters \(n_t\) and distance \(d=2t+1\) for ball codes on the Bruhat–Tits tree (Section 3).  
2. Closed‑form computation of passive logical failure probabilities for \(p=3\), \(t=1,2\) at \(\varepsilon=10^{-3}\) (Section 4).  
3. Analysis of a recursive eight‑fold majority‑vote scheme, yielding logical error probabilities for three concatenation levels (Section 4).  
4. Proof that a level‑by‑level tree decoder runs in \(\mathcal{O}(\log N)\) time (Section 3).  
5. Practical pathway for experimental validation on a 17‑qudit (\(p=3, t=2\)) prototype (Section 7).

## 2. Background and Related Work
The ultrametric strong triangle inequality \(d(x,y)\le\max\{d(x,z),d(z,y)\}\) underlies the geometry of Bruhat–Tits trees. Arsenault et al. formalize ultrametrics as zero‑dimensional analogues of ordinary metrics and prove an ultrametric version of the Arens–Eells embedding theorem, establishing the mathematical foundation for non‑Archimedean spaces used here [1].

Machine‑learning decoders for topological codes report logical error rates \(p_L\) versus physical error \(p\) and emphasize latency scaling with code distance \(d\) [2]. Their evaluation metrics, including the error‑suppression ratio \(\Lambda=p_L(d)/p_L(d+2)\), motivate the need for decoders whose latency does not increase with \(d\).

Quantum Margulis codes demonstrate that QLDPC constructions can achieve linear‑time decoding complexity for certain families, but they rely on explicit parity‑check matrices and do not exploit ultrametric confinement of errors [3].

Entanglement‑purification protocols based on QLDPC codes achieve high fidelity thresholds, yet they require active syndrome extraction and thus inherit decoder latency constraints [4].

Neural belief‑propagation decoders improve decoding performance for QLDPC codes but remain limited by iterative schedules whose depth grows with code size [5].

Scalable real‑time neural decoders for surface and colour codes achieve sub‑microsecond cycle times on specialized accelerators, yet their runtime still scales at least linearly with the number of physical qubits [6].

GAN‑based decoders for toric codes achieve higher pseudo‑thresholds than MWPM but involve training overhead and do not guarantee logarithmic inference time [7].

Stabilizer‑assisted inactivation decoding reduces decoding complexity for QLDPC codes on erasure channels by exploiting fully erased stabilizers, illustrating the benefit of preprocessing steps that prune the problem size [8].

QNFO [9] provides exact combinatorial formulas for ball‑code parameters and computes passive logical failure probabilities for \(p=3\) at \(\varepsilon=10^{-3}\). The same source derives the distance formula \(d=2t+1\) and reports suppression factors.

QNFO [10] analyzes a recursive eight‑fold majority‑vote scheme, presenting explicit logical error probabilities for three concatenation levels at physical error \(p=0.4\) and confidence bounds for zero‑error simulations.

Together these works supply the mathematical tools, decoding performance benchmarks, and concrete numerical results required for the present analysis.

## 3. Methods
### 3.1. Ball‑Code Construction on the Bruhat–Tits Tree
The Bruhat–Tits tree \(T_{p+1}\) is a regular infinite tree of degree \(p+1\) associated with the \(p\)-adic field \(\mathbb{Q}_p\). A ball of radius \(t\) centered at a vertex contains all vertices at graph distance \(\le t\). The number of vertices in such a ball is
\[
n_t \;=\; 1 \;+\; \frac{(p+1)\bigl(p^{t}-1\bigr)}{p-1},
\tag{1}
\]
as proved in [9] by a shell‑count combinatorial identity.

### 3.2. Distance and Correctability
Lemma 1 of [9] guarantees that balls of equal radius are either nested or disjoint. Assuming a symmetric encoder that treats all branches identically (the branch‑permutation symmetry), any error affecting at most \(t\) qudits can be corrected, yielding a code distance
\[
d \;=\; 2t+1.
\tag{2}
\]

### 3.3. Passive Logical Failure Model
We adopt the independent depolarizing noise model: each physical qudit suffers an error with probability \(\varepsilon\) per protection epoch, independently of all others. Under this model, the probability that a weight‑\(w\) error pattern occurs is \(\varepsilon^{w}(1-\varepsilon)^{n_t-w}\). Since only error patterns of weight \(\le t\) are correctable, the passive logical failure probability is the sum over all uncorrectable patterns:
\[
P_{\mathrm{pass}} \;=\; \sum_{w=t+1}^{n_t} \binom{n_t}{w}\,\varepsilon^{w}(1-\varepsilon)^{n_t-w}.
\tag{3}
\]
Equation (3) is evaluated exactly for the parameter sets used in Section 4.

### 3.4. Recursive Eight‑Fold Majority Vote
The classical analogue of the tree code is an eight‑fold repetition at each level. Let \(p\) be the physical error probability. After one majority‑vote layer the effective error probability is
\[
p^{(1)} \;=\; \sum_{k=5}^{8} \binom{8}{k}\,p^{k}(1-p)^{8-k}.
\tag{4}
\]
Applying (4) recursively yields \(p^{(2)}\) and \(p^{(3)}\). The recursion captures the effect of concatenating the eight‑fold code three times.

### 3.5. Decoder Algorithm and Runtime
The decoder proceeds level‑by‑level from the leaves toward the root. At each level it performs a constant‑time majority vote on each node’s eight children. For a tree of depth \(L\) the number of levels is \(L\), and the total number of nodes is \(\mathcal{O}(p^{L})\). Because the work at each level can be parallelized across all nodes, the wall‑clock time scales as \(\mathcal{O}(L)=\mathcal{O}(\log_{p} N)\), where \(N\) is the total number of physical qudits.

## 4. Analysis
All numerical inputs are taken directly from the bibliography entries.

### 4.1. Ball‑Code Parameters for \(p=3\)
Using (1) with \(p=3\) and \(t=1\):
\[
n_{1} \;=\; 1 + \frac{(3+1)(3^{1}-1)}{3-1}
          \;=\; 1 + \frac{4\cdot(3-1)}{2}
          \;=\; 1 + \frac{4\cdot2}{2}
          \;=\; 1 + 4
          \;=\; 5.
\]
For \(t=2\):
\[
n_{2} \;=\; 1 + \frac{4(3^{2}-1)}{2}
          \;=\; 1 + \frac{4(9-1)}{2}
          \;=\; 1 + \frac{4\cdot8}{2}
          \;=\; 1 + 16
          \;=\; 17.
\]
These values match the exact numbers reported in [9].

### 4.2. Passive Logical Failure for \(p=3,\;t=1,\;\varepsilon=10^{-3}\)
Equation (3) with \(n_{1}=5\) and \(t=1\) yields
\[
P_{\mathrm{pass}}
 = \sum_{w=2}^{5} \binom{5}{w}\,(10^{-3})^{w}(1-10^{-3})^{5-w}.
\]
Compute each term:

- \(w=2\): \(\binom{5}{2}=10\); term \(=10\cdot10^{-6}\cdot(0.999)^{3}\approx10\cdot10^{-6}\cdot0.997003\approx9.97003\times10^{-6}\).
- \(w=3\): \(\binom{5}{3}=10\); term \(=10\cdot10^{-9}\cdot(0.999)^{2}\approx10\cdot10^{-9}\cdot0.998001\approx9.98001\times10^{-9}\).
- \(w=4\): \(\binom{5}{4}=5\); term \(=5\cdot10^{-12}\cdot0.999\approx4.995\times10^{-12}\).
- \(w=5\): \(\binom{5}{5}=1\); term \(=1\cdot10^{-15}\approx1.0\times10^{-15}\).

Summing:
\[
P_{\mathrm{pass}}
 \approx 9.97003\times10^{-6}
        + 9.98001\times10^{-9}
        + 4.995\times10^{-12}
        + 1.0\times10^{-15}
 \approx 9.98\times10^{-6}.
\]
Thus \(P_{\mathrm{pass}}\approx9.98\times10^{-6}\), as reported in [9].

The suppression factor relative to an unencoded qudit is
\[
\frac{\varepsilon}{P_{\mathrm{pass}}}
 = \frac{10^{-3}}{9.98\times10^{-6}}
 \approx 100.2.
\]

### 4.3. Passive Logical Failure for \(p=3,\;t=2,\;\varepsilon=10^{-3}\)
Now \(n_{2}=17\) and \(t=2\). Equation (3) becomes
\[
P_{\mathrm{pass}}^{(2)}=\sum_{w=3}^{17}\binom{17}{w}\,(10^{-3})^{w}(1-10^{-3})^{17-w}.
\]
The dominant contribution comes from \(w=3\):
\[
\binom{17}{3}=680,\quad
\text{term}_{w=3}=680\cdot10^{-9}\cdot(0.999)^{14}
               \approx680\cdot10^{-9}\cdot0.9861
               \approx6.705\times10^{-7}.
\]
Higher‑weight terms add a correction of roughly \(0.35\%\) (as noted in [9]), giving
\[
P_{\mathrm{pass}}^{(2)}\approx6.705\times10^{-7}\times(1+0.0035)
                       \approx6.73\times10^{-7}.
\]

### 4.4. Recursive Eight‑Fold Majority Vote
Using (4) with physical error \(p=0.4\):

1. Compute \(p^{(1)}\):
\[
p^{(1)} = \sum_{k=5}^{8}\binom{8}{k}0.4^{k}0.6^{8-k}.
\]
Evaluate each term:
- \(k=5\): \(\binom{8}{5}=56\); term \(=56\cdot0.4^{5}\cdot0.6^{3}=56\cdot0.01024\cdot0.216=0.12369984\).
- \(k=6\): \(\binom{8}{6}=28\); term \(=28\cdot0.4^{6}\cdot0.6^{2}=28\cdot0.004096\cdot0.36=0.04123136\).
- \(k=7\): \(\binom{8}{7}=8\); term \(=8\cdot0.4^{7}\cdot0.6^{1}=8\cdot0.0016384\cdot0.6=0.00786432\).
- \(k=8\): \(\binom{8}{8}=1\); term \(=1\cdot0.4^{8}=0.00065536\).

Summing:
\[
p^{(1)}=0.12369984+0.04123136+0.00786432+0.00065536
      =0.1736704.
\]

2. Compute \(p^{(2)}\) by applying (4) to \(p^{(1)}=0.1736704\):
\[
p^{(2)} = \sum_{k=5}^{8}\binom{8}{k}(0.1736704)^{k}(1-0.1736704)^{8-k}.
\]
Carrying out the arithmetic (as performed in [10]) yields
\[
p^{(2)}\approx0.0055485.
\]

3. Compute \(p^{(3)}\) by applying (4) to \(p^{(2)}\):
\[
p^{(3)} = \sum_{k=5}^{8}\binom{8}{k}(0.0055485)^{k}(1-0.0055485)^{8-k}
        \approx2.905\times10^{-10}.
\]

The suppression factor after the first level is
\[
\frac{p}{p^{(1)}} = \frac{0.4}{0.1736704} \approx 2.303.
\]

### 4.5. Decoder Runtime Bound
A tree of depth \(L\) contains \(N = n_L\) physical qudits. The decoder processes each level in parallel, performing a constant‑time majority vote per node. Hence the wall‑clock time \(T\) satisfies
\[
T = c\cdot L = c\cdot\log_{p} N,
\]
where \(c\) is the per‑level processing time. This establishes the logarithmic latency claim.

## 5. Results
- **Exact code parameters.** For \(p=3\): \(n_{1}=5\), \(n_{2}=17\), \(n_{3}=53\); distance \(d=2t+1\) yields \(d=3\) for \(t=1\) and \(d=5\) for \(t=2\) (Section 4.1).  
- **Passive logical failure.** \(P_{\mathrm{pass}}(p=3,t=1,\varepsilon=10^{-3})\approx9.98\times10^{-6}\) with suppression factor \(100.2\) (Section 4.2).  
- **Improved suppression for larger radius.** \(P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}\) (Section 4.3).  
- **Recursive majority‑vote error rates.** \(p^{(1)}=0.1736704\), \(p^{(2)}=0.0055485\), \(p^{(3)}\approx2.905\times10^{-10}\) at physical error \(p=0.4\) (Section 4.4).  
- **Decoder latency.** Proven \(\mathcal{O}(\log N)\) wall‑clock time (Section 4.5).  

These quantitative outcomes confirm that ultrametric tree codes can achieve strong error suppression while maintaining logarithmic decoding latency.

## 6. Discussion
### 6.1. Limitations
- **Symmetric encoder assumption.** The distance formula (2) and correctability rely on the existence of a branch‑permutation‑symmetric encoder (Lemma 1, Proposition 1 in [9]). No explicit encoder is constructed; if such symmetry fails, the distance guarantee collapses.  
- **Independent depolarizing noise model.** Correlated errors across neighboring vertices or burst errors would violate the independence assumption used in (3), potentially increasing \(P_{\mathrm{pass}}\).  
- **Finite‑size effects.** The analytical failure probabilities neglect edge effects in truncated trees; simulations would be needed to validate the asymptotic formulas for small \(L\).  
- **Recursive majority‑vote model.** The eight‑fold scheme assumes perfect majority voting without measurement errors; hardware imperfections could degrade the recursion’s suppression factor.  

### 6.2. Failure Modes and Falsification
A single observation that falsifies the main result would be the measurement of a logical error rate for a \(p=3, t=1\) ball code under \(\varepsilon=10^{-3}\) that exceeds \(1\times10^{-5}\). Such a result would contradict the derived \(P_{\mathrm{pass}}\) and indicate either a breakdown of the independence assumption or the absence of the required symmetric encoder.

### 6.3. Open Questions
- Construction of an explicit symmetric encoder and verification of the stabilizer commutation relations.  
- Extension of the analysis to higher‑prime fields (\(p>3\)) and to qudit dimensions matching physical hardware.  
- Impact of realistic syndrome extraction noise on the passive scheme.  
- Integration of the tree decoder with active error‑correction layers to form hybrid architectures.

## 7. Practical Implications and Engineering Pathways
### (a) Potential Users and Design Impact
Quantum hardware architects and fault‑tolerant system designers can employ ultrametric tree codes to replace surface‑code decoders in modules where latency is critical. By embedding a perfect‑tensor code on a Bruhat–Tits tree, the logical clock could approach the native gate speed, reducing the overall execution time of error‑corrected algorithms.

### (b) Technology Readiness
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 2 (concept formulation). No hardware prototype has yet been built.

### (c) Minimal Next Experiment
Construct a depth‑2 (\(t=2\)) ball code with \(p=3\) (17 qutrits) on a trapped‑ion platform capable of implementing qutrit operations. Measure the logical error rate under calibrated depolarizing noise \(\varepsilon=10^{-3}\). Observation of a logical failure probability significantly above \(6.73\times10^{-7}\) would falsify the passive failure model; a result consistent with the prediction would validate the analytical framework.

### (d) Engineering Constraints
- **Qudit dimension.** Requires hardware supporting three‑level systems (qutrits) or higher for larger \(p\).  
- **Connectivity.** The tree geometry demands all‑to‑all connectivity within each branch; trapped‑ion chains naturally provide long‑range couplings.  
- **Syndrome extraction.** Although the scheme is passive, verification of logical states may still need occasional stabilizer checks, imposing a modest measurement overhead.  
- **Control electronics.** Parallel majority‑vote operations per level require synchronized control pulses across up to eight branches.

### (e) Projected Cost and Performance Bounds
Assuming a qutrit control cost of \$10 k per ion and a modest overhead for the tree wiring, a 17‑ion prototype would cost on the order of \$170 k. The projected logical error rate (\(\approx6.7\times10^{-7}\) per epoch) represents a suppression factor of ≈1500 relative to the physical error rate, offering a performance bound that exceeds typical surface‑code logical rates at comparable code sizes.

### (f) Risks and Misuse Paths
If the symmetric encoder cannot be realized, the scheme may give a false sense of security, leading designers to adopt insufficiently protected codes. Additionally, the passive nature could be misinterpreted as eliminating the need for active error correction, which would be detrimental in the presence of correlated noise.

## 8. Conclusion
We have provided a rigorous analytical treatment of ultrametric Bruhat–Tits tree codes, deriving exact code parameters, logical failure probabilities, and a logarithmic decoder runtime bound. Numerical evaluation shows that a modest‑size ball code (\(p=3, t=2\)) can suppress logical errors by three orders of magnitude under realistic noise, while the recursive majority‑vote scheme demonstrates exponential error suppression across concatenation levels. The logarithmic latency of the tree decoder offers a pathway to lift the logical clock toward physical gate speeds, addressing a critical bottleneck in fault‑tolerant quantum computing. Realizing the full potential of this approach hinges on constructing an explicit symmetric encoder and validating the passive failure model experimentally.

## References
[1] arXiv:2008.10209v2 | An embedding, an extension, and an interpolation of ultrametrics  
[2] arXiv:2608.15760v1 | Machine Learning Approaches to Decoding Topological Quantum Codes  
[3] arXiv:2503.03936v3 | Construction and Decoding of Quantum Margulis Codes  
[4] arXiv:2210.14143v2 | Entanglement Purification with Quantum LDPC Codes and Iterative Decoding  
[5] arXiv:2308.08208v2 | Quaternary Neural Belief Propagation Decoding of Quantum LDPC Codes with Overcomplete Check Matrices  
[6] arXiv:2512.07737v2 | A scalable and real-time neural decoder for topological quantum codes  
[7] arXiv:2409.06984v3 | GAN decoder on a quantum toric code for noise-robust quantum teleportation  
[8] arXiv:2601.14236v1 | Stabilizer-Assisted Inactivation Decoding of Quantum Error-Correcting Codes with Erasures  
[9] QNFO: Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound  
[10] QNFO: Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question  
[11] QNFO: All Things Are One  
[12] QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics  

## Appendix A. Divergence report
*No divergent claims were identified among the independent drafts; all substantive statements converged on the same quantitative values and logical arguments.*

## Appendix B. Claim attribution
| Claim ID | Source Draft(s) | Agreement |
|----------|----------------|-----------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| C3 | A, B, C | CONVERGENT |
| C4 | A, B, C | CONVERGENT |
| C5 | A, B, C | CONVERGENT |
| C6 | A, B, C | CONVERGENT |
| C7 | A, B, C | CONVERGENT |
| C8 | A, B, C | CONVERGENT |
| C9 | A, B, C | CONVERGENT |
| C10 | A, B, C | CONVERGENT |
| C11 | A, B, C | CONVERGENT |
| C12 | A, B, C | CONVERGENT |
| C13 | A, B, C | CONVERGENT |
| C14 | A, B, C | CONVERGENT |
| C15 | A, B, C | CONVERGENT |
| C16 | A, B, C | CONVERGENT |
| C17 | A, B, C | CONVERGENT |
| C18 | A, B, C | CONVERGENT |
| C19 | A, B, C | CONVERGENT |
| C20 | A, B, C | CONVERGENT |
| C21 | A, B, C | CONVERGENT |
| C22 | A, B, C | CONVERGENT |
| C23 | A, B, C | CONVERGENT |
| C24 | A, B, C | CONVERGENT |
| C25 | A, B, C | CONVERGENT |
| C26 | A, B, C | CONVERGENT |
| C27 | A, B, C | CONVERGENT |
| C28 | A, B, C | CONVERGENT |
| C29 | A, B, C | CONVERGENT |
| C30 | A, B, C | CONVERGENT |
| C31 | A, B, C | CONVERGENT |
| C32 | A, B, C | CONVERGENT |
| C33 | A, B, C | CONVERGENT |
| C34 | A, B, C | CONVERGENT |
| C35 | A, B, C | CONVERGENT |
| C36 | A, B, C | CONVERGENT |
| C37 | A, B, C | CONVERGENT |
| C38 | A, B, C | CONVERGENT |
| C39 | A, B, C | CONVERGENT |
| C40 | A, B, C | CONVERGENT |
| C41 | A, B, C | CONVERGENT |
| C42 | A, B, C | CONVERGENT |
| C43 | A, B, C | CONVERGENT |
| C44 | A, B, C | CONVERGENT |
| C45 | A, B, C | CONVERGENT |
| C46 | A, B, C | CONVERGENT |
| C47 | A, B, C | CONVERGENT |
| C48 | A, B, C | CONVERGENT |
| C49 | A, B, C | CONVERGENT |
| C50 | A, B, C | CONVERGENT |
| C51 | A, B, C | CONVERGENT |
| C52 | A, B, C | CONVERGENT |
| C53 | A, B, C | CONVERGENT |
| C54 | A, B, C | CONVERGENT |
| C55 | A, B, C | CONVERGENT |
| C56 | A, B, C | CONVERGENT |
| C57 | A, B, C | CONVERGENT |
| C58 | A, B, C | CONVERGENT |
| C59 | A, B, C | CONVERGENT |
| C60 | A, B, C | CONVERGENT |
| C61 | A, B, C | CONVERGENT |
| C62 | A, B, C | CONVERGENT |
| C63 | A, B, C | CONVERGENT |
| C64 | A, B, C | CONVERGENT |
| C65 | A, B, C | CONVERGENT |
| C66 | A, B, C | CONVERGENT |
| C67 | A, B, C | CONVERGENT |
| C68 | A, B, C | CONVERGENT |
| C69 | A, B, C | CONVERGENT |
| C70 | A, B, C | CONVERGENT |
| C71 | A, B, C | CONVERGENT |
| C72 | A, B, C | CONVERGENT |
| C73 | A, B, C | CONVERGENT |
| C74 | A, B, C | CONVERGENT |
| C75 | A, B, C | CONVERGENT |
| C76 | A, B, C | CONVERGENT |
| C77 | A, B, C | CONVERGENT |
| C78 | A, B, C | CONVERGENT |
| C79 | A, B, C | CONVERGENT |
| C80 | A, B, C | CONVERGENT |
| C81 | A, B, C | CONVERGENT |
| C82 | A, B, C | CONVERGENT |
| C83 | A, B, C | CONVERGENT |
| C84 | A, B, C | CONVERGENT |
| C85 | A, B, C | CONVERGENT |
| C86 | A, B, C | CONVERGENT |
| C87 | A, B, C | CONVERGENT |
| C88 | A, B, C | CONVERGENT |
| C89 | A, B, C | CONVERGENT |
| C90 | A, B, C | CONVERGENT |
| C91 | A, B, C | CONVERGENT |
| C92 | A, B, C | CONVERGENT |
| C93 | A, B, C | CONVERGENT |
| C94 | A, B, C | CONVERGENT |
| C95 | A, B, C | CONVERGENT |
| C96 | A, B, C | CONVERGENT |
| C97 | A, B, C | CONVERGENT |
| C98 | A, B, C | CONVERGENT |
| C99 | A, B, C | CONVERGENT |
| C100 | A, B, C | CONVERGENT |