# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) proposes that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction of classical probability measures under a locally bounded hydrodynamic transport. The specific gap is the absence of an explicit derivation of GHZ‑type Bell‑violating correlations from the hypothesis’s own axioms. Four minimal axioms (classical measure grounding, local hidden variables, locally bounded continuous transport, and free measurement settings) are formalized, and the algebraic pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) is derived. Quantum mechanics predicts a product of \(-1\) for the same four GHZ triple correlations, yielding a Mermin violation factor of \(2\) and a CHSH violation factor of \(\sqrt{2}\approx1.414214\). A projection of the temporal resolution required for particle‑tracking simulations yields a minimum propagation time of \(3.33\ \mathrm{ps}\) across a millimetre barrier and a sub‑picosecond timestep of \(\approx333\ \mathrm{fs}\). The strong, local‑realist form of HSH is therefore falsified, and the engineering demands for any simulation that tests the locality claim are quantified.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics or accept that any such derivation must abandon locality of the response functions.

The contributions are:
1. Formalization of HSH as four minimal axioms (Section 3.1).  
2. Derivation of the classical pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) from the axioms (Section 4.2).  
3. Computation of the quantum GHZ stabilizer values and the resulting contradiction (Section 4.1).  
4. Quantitative Mermin and CHSH violation analysis (Sections 4.3–4.4).  
5. Projection of the temporal resolution required for particle‑tracking simulations at picosecond‑scale propagation times and sub‑picosecond timesteps (Section 4.6).

## 2. Background and Related Work

Reference [1] shows that statistical properties of random quantum circuits map onto classical statistical‑mechanics models, establishing that any classical re‑grounding must operate at the ensemble level. Reference [2] quantifies fidelity and distribution‑rate metrics for multipartite entanglement over noisy networks, establishing target statistics for quantum‑network applications. Reference [3] argues that entanglement has no classical analogue and discusses semiclassical limits, highlighting challenges for classical reinterpretations. Reference [4] studies GHZ‑like states coupled to independent classical environments, providing a concrete model of tripartite entanglement under classical noise. Reference [5] describes entanglement‑free regimes as classical limits via quantum Darwinism, offering a perspective on classical emergence. Reference [6] presents hybrid entangled states as resources for quantum networks, illustrating the relevance of multipartite entanglement. Reference [7] develops hybrid classical‑quantum algorithms, demonstrating continuous trade‑offs between classical and quantum resources. Reference [8] proposes a unified formalism bridging classical action functionals and quantum operators, illustrating a pathway for classical‑quantum interpolation. Reference [10] introduces the Hydrodynamic Stability Hypothesis, specifying a continuous‑attractor model with local transport and free settings. Reference [11] formulates the Post‑Quantum Synthesis theorem that local operations do not affect spatially separated systems, providing a local‑realist benchmark.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

The strong form of HSH is formalized as four axioms:

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure \(\mu_{\psi}\ll\mu\) with Radon–Nikodým derivative \(\rho_{\psi}= \frac{d\mu_{\psi}}{d\mu}\), such that all quantum predictions are recoverable as functionals of \(\rho_{\psi}\).
- **(A2) Local hidden variables.** For \(N\) spatially separated parties, the hidden configuration decomposes as \(\lambda=(\lambda_{1},\ldots,\lambda_{N})\) with \(\lambda_{i}\in\Lambda_{i}\); each party’s outcome is a local function \(A_{i}=f_{i}(\lambda_{i},s_{i})\) of its own variable and its own setting \(s_{i}\).
- **(A3) Locally bounded continuous transport.** The time evolution \(\mu_{t}= (\Phi_{t})_{*}\mu_{0}\) is generated by a local flow \(\Phi_{t}\) on \(\Lambda\) propagating information at finite speed \(v_{\max}\), so that no influence connects spacelike‑separated events. Preparation and measurement correspond to relaxation into basins of attraction \(\mathcal{B}_{k}\subset\Lambda\) of stable measures, the observed outcome indexing the basin.
- **(A4) Free settings.** The distribution of measurement settings is statistically independent of \(\lambda\) (no superdeterminism).

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality of the PQS no‑spooky‑action theorem [11] (A2), and the explicit rejection of superdeterminism in [10] (A4).

### 3.2 Falsification protocol

Given A1–A4, the protocol is: (i) derive the classical constraint imposed by A1–A4 on the four relevant triple correlations, (ii) compute the quantum values of those correlations from the GHZ state
\[
|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|000\rangle + |111\rangle\bigr),
\]
under local Pauli measurements \(X\) and \(Y\) on each qubit, and (iii) compare. Any mismatch falsifies the strong claim because the hypothesis asserts reproduction of the quantum statistics from the classical axioms.

### 3.3 Simulation projection protocol

The hypothesis proposes particle‑tracking of the hydrodynamic transport \(\Phi_{t}\) at the temporal resolution derived in Section 4.6: picosecond‑scale propagation times and sub‑picosecond (hundreds of femtoseconds) timesteps. The projection is labeled and conditional on the assumptions listed in Section 4.6.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (assumption).** The GHZ state is taken as \(|\mathrm{GHZ}\rangle = (|000\rangle + |111\rangle)/\sqrt{2}\).

**Input 2 (assumption).** Pauli operators \(X\) and \(Y\) have eigenvalues \(\pm1\).

Using \(X|0\rangle=|1\rangle\), \(X|1\rangle=|0\rangle\), \(Y|0\rangle=i|1\rangle\), \(Y|1\rangle=-i|0\rangle\):
\[
\begin{aligned}
XXX\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(|111\rangle + |000\rangle\bigr)=+|\mathrm{GHZ}\rangle,\\
XYY\,|\mathrm{GHZ}\rangle &= -|\mathrm{GHZ}\rangle,\\
YXY\,|\mathrm{GHZ}\rangle &= -|\mathrm{GHZ}\rangle,\\
YYX\,|\mathrm{GHZ}\rangle &= -|\mathrm{GHZ}\rangle.
\end{aligned}
\]

Hence the quantum triple‑product expectations are
\[
\langle XXX\rangle_{Q}=+1,\qquad
\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1.
\]

The product of the four quantum correlations is
\[
(+1)\times(-1)\times(-1)\times(-1) = -1.
\]

### 4.2 The classical constraint from axioms A1–A4

For each party \(i\in\{1,2,3\}\) define local predetermined outcomes \(A_{i}^{X},A_{i}^{Y}\in\{-1,+1\}\). The four triple products are
\[
\begin{aligned}
P_{1}&=A_{1}^{X}A_{2}^{X}A_{3}^{X},\\
P_{2}&=A_{1}^{X}A_{2}^{Y}A_{3}^{Y},\\
P_{3}&=A_{1}^{Y}A_{2}^{X}A_{3}^{Y},\\
P_{4}&=A_{1}^{Y}A_{2}^{Y}A_{3}^{X}.
\end{aligned}
\]

Pointwise multiplication yields
\[
\begin{aligned}
P_{1}P_{2}P_{3}P_{4}
&=(A_{1}^{X})^{2}(A_{1}^{Y})^{2}(A_{2}^{X})^{2}(A_{2}^{Y})^{2}(A_{3}^{X})^{2}(A_{3}^{Y})^{2}\\
&=(+1)^{6}=+1,
\end{aligned}
\]
since each local outcome appears exactly twice and squares to \(+1\). Taking expectations with respect to the measure \(\mu\) (A1) gives
\[
\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1.
\]

Thus the classical axioms force a product of \(+1\), whereas quantum mechanics requires \(-1\).

### 4.3 Mermin bound and violation factor

For any model satisfying A1–A4,
\[
\bigl|\langle P_{1}\rangle - \langle P_{2}\rangle - \langle P_{3}\rangle - \langle P_{4}\rangle\bigr|\le 2,
\]
because the pointwise expression \(|P_{1}-P_{2}-P_{3}-P_{4}|=2\) whenever \(P_{1}P_{2}P_{3}P_{4}=+1\). The quantum values give
\[
\bigl|(+1)-(-1)-(-1)-(-1)\bigr| = |1+1+1+1| = 4.
\]
Hence the classical bound is \(M_{\mathrm{LHV}}=2\), the quantum value is \(M_{\mathrm{Q}}=4\), the gap \(\Delta M = 2\), and the violation factor is \(M_{\mathrm{Q}}/M_{\mathrm{LHV}} = 2\).

### 4.4 CHSH cross‑check

For two parties the CHSH combination is
\[
S = E(a,b) + E(a,b') + E(a',b) - E(a',b').
\]
Classically \(|S|\le 2\). Quantum mechanics attains the Tsirelson bound \(S_{\max}=2\sqrt{2}\). Using \(\sqrt{2}\approx1.414214\):
\[
2\sqrt{2}\approx 2\times1.414214 = 2.828427.
\]
The violation factor over the classical bound is \(\sqrt{2}\approx1.414214\).

### 4.5 The fork and the falsification verdict

The derivation forces exactly two mutually exclusive options:

1. **Abandon A2.** Allow the outcome functions \(A_{i}\) to depend on distant settings, thereby violating locality.
2. **Retain A2 and accept contradiction.** Keep the locality and free‑setting axioms, but concede that the model cannot reproduce the GHZ stabilizer values.

Either option falsifies the strong claim that HSH simultaneously satisfies A1–A4 and reproduces GHZ statistics.

### 4.6 Simulation timescale projection (explicitly labeled projection)

**Assumptions.**  
(P1) The transport speed is bounded by \(v_{\max}=c=3.0\times10^{8}\ \mathrm{m\,s^{-1}}\).  
(P2) The spatial barrier width is \(L=1.0\times10^{-3}\ \mathrm{m}\) (typical laboratory scale).  
(P3) The simulation timestep must be at most one‑tenth of the propagation time.

**Derivation.** Minimum propagation time:
\[
t_{\min}= \frac{L}{v_{\max}} = \frac{1.0\times10^{-3}}{3.0\times10^{8}} = 3.333333\times10^{-12}\ \mathrm{s}\approx3.33\ \mathrm{ps}.
\]
Required timestep:
\[
\Delta t \le \frac{t_{\min}}{10}=3.333333\times10^{-13}\ \mathrm{s}\approx333\ \mathrm{fs}.
\]
Number of timesteps for one crossing:
\[
N_{\mathrm{steps}} = \frac{t_{\min}}{\Delta t}=10.
\]

For a macroscopic barrier \(L=1.0\ \mathrm{m}\):
\[
t_{\min}= \frac{1.0}{3.0\times10^{8}} = 3.333333\times10^{-9}\ \mathrm{s}\approx3.33\ \mathrm{ns},
\qquad
N_{\mathrm{steps}} = \frac{3.33\times10^{-9}}{3.33\times10^{-13}} = 1.0\times10^{4}.
\]

These projections are conditional on P1–P3 and establish the temporal resolution any particle‑tracking simulation must achieve.

## 5. Results

All quantitative statements below follow directly from the arithmetic in Section 4.

1. **Quantum GHZ correlations** (Section 4.1): \(\langle XXX\rangle_{Q}=+1\); \(\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1\).
2. **Classical pointwise constraint** (Section 4.2): \(P_{1}P_{2}P_{3}P_{4}=+1\) pointwise, implying \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1\), which conflicts with the quantum product \(-1\).
3. **Mermin bound** (Section 4.3): classical \(M_{\mathrm{LHV}}=2\); quantum \(M_{\mathrm{Q}}=4\); violation factor \(2\).
4. **CHSH bound** (Section 4.4): classical bound \(2\); quantum maximum \(2\sqrt{2}\approx2.828427\); violation factor \(\sqrt{2}\approx1.414214\).
5. **Falsification verdict** (Section 4.5): the strong form of HSH is falsified; any model reproducing GHZ statistics must abandon locality (A2) or contradict quantum predictions.
6. **Simulation timescale projections** (Section 4.6): for \(L=1.0\times10^{-3}\ \mathrm{m}\), \(t_{\min}=3.333333\times10^{-12}\ \mathrm{s}\), \(\Delta t\le3.333333\times10^{-13}\ \mathrm{s}\), \(N_{\mathrm{steps}}=10\); for \(L=1.0\ \mathrm{m}\), \(t_{\min}=3.333333\times10^{-9}\ \mathrm{s}\), \(N_{\mathrm{steps}}=1.0\times10^{4}\).

## 6. Discussion

**Scope of the falsification.** The derivation shows that the *strong* claim of HSH—local classical measure theory reproducing GHZ‑type Bell‑violating correlations—is untenable. Weaker versions that relax A2 or reinterpret locality at the level of the flow \(\Phi_{t}\) are not addressed.

**Potential escapes.**  
1. The formalization A1–A4 is an interpretation; the original record [10] does not provide a detailed axiomatization, so alternative formalizations might evade the product constraint.  
2. Stochastic response functions could be considered; however, the algebraic identity \(P_{1}P_{2}P_{3}P_{4}=+1\) holds pointwise for any deterministic or stochastic assignment because each local outcome appears twice.  
3. The connection between basins of attraction (A3) and the Born rule is not derived here; a separate probabilistic mechanism might alter the mapping from \(\rho_{\psi}\) to observed frequencies, but it would not change the deterministic algebraic constraint.

**Limitations.**  
- The timescale projections depend on the assumed barrier width \(L\) and the generous speed bound \(v_{\max}=c\); other parameter choices would scale the numbers linearly.  
- The analysis treats only the four GHZ stabilizer measurements; other settings (e.g., \(YYY\)) are omitted because they do not affect the contradiction.  
- Binary outcomes \(\pm1\) are assumed; extensions to higher‑dimensional outcomes are not considered.

**Failure modes.** If a construction of local response functions satisfying A1–A4 and reproducing all four stabilizer values were exhibited, the pointwise product argument would be invalidated, falsifying the present falsification. Likewise, an empirical demonstration that the GHZ stabilizer statistics admit a local stochastic model with \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=-1\) would overturn the argument.

**Sensitivity analysis.** Varying the barrier width \(L\) by an order of magnitude changes the minimum propagation time \(t_{\min}\) proportionally, while the required timestep \(\Delta t\) remains one‑tenth of \(t_{\min}\). Consequently, the number of timesteps for a crossing remains fixed at ten, independent of \(L\). This linear scaling emphasizes that the primary engineering challenge is achieving sub‑picosecond temporal resolution rather than handling large numbers of steps.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols, and theorists exploring classical‑quantum unification will use this result to assess whether a purely local classical underpinning can support multipartite entanglement resources. If the result holds, any design that assumes a local‑realist foundation for GHZ‑type correlations must be revised to incorporate non‑local or hybrid mechanisms.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions, it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic (or stochastic) response functions \(A_{i}(\lambda_{i},s_{i})\) that satisfy A1–A4 and reproduce the four GHZ stabilizer values. Demonstrating the impossibility of such a construction would falsify the present falsification; success would falsify the present result.

**(d) Engineering constraints.** The projection in Section 4.6 identifies the primary constraints for any simulation that attempts to verify the locality claim: (i) a maximum signal speed \(v_{\max}\) (taken as \(c\) for a generous bound), (ii) spatial barrier dimensions that set the propagation time, and (iii) a timestep resolution at least one‑tenth of the propagation time to resolve the signal. No further material, computational, or cost constraints are derived from the analysis.

**(e) Projected performance bounds.** Assuming the barrier width \(L=1.0\times10^{-3}\ \mathrm{m}\) and \(v_{\max}=c\), the required timestep is \(\Delta t\le3.33\times10^{-13}\ \mathrm{s}\) ($\approx$ 333 fs). For a macroscopic barrier \(L=1.0\ \mathrm{m}\), the required timestep remains the same but the total number of steps increases to \(10^{4}\). These are projections conditional on the stated assumptions.

**(f) Direct risks or misuse paths.** No immediate misuse is identified; the result merely constrains theoretical program design. Misinterpretation of the falsification as a proof that all classical approaches are impossible would be a misuse; the paper explicitly limits the claim to the strong, local form of HSH.

## 8. Conclusion

By formalizing the Hydrodynamic Stability Hypothesis as four minimal axioms and deriving the algebraic pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\), it has been shown that the hypothesis cannot simultaneously satisfy locality, measurement‑setting freedom, and reproduce the GHZ stabilizer statistics of quantum mechanics. The resulting Mermin and CHSH violations quantify the gap between the classical bound and quantum predictions. Projection of the required simulation timescales clarifies the engineering demands of any particle‑tracking test of the hypothesis. The strong, local‑realist version of HSH is therefore falsified; any viable classical re‑grounding must relax at least one of the axioms.

## References

[1] arXiv:2111.08018v2 | Entanglement dynamics in hybrid quantum circuits  
[2] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks  
[3] arXiv:1110.0157v1 | Entanglement, the quantum formalism and the classical world  
[4] arXiv:2107.11259v1 | Probing tripartite entanglement and coherence dynamics in pure and mixed independent classical environments  
[5] arXiv:1206.5715v2 | Coherent states and the classical-quantum limit considered from the point of view of entanglement  
[6] arXiv:2004.13176v3 | Hierarchical Quantum Network using Hybrid Entanglement  
[7] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations  
[8] arXiv:2010.03984v2 | A Unified Combination of Classical and Quantum Systems  
[9] QNFO: Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/re-deriving-quantum-entanglement-from-classical-radon-nikod-m-hydrodynamics-a-fo  
[10] QNFO: Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis  
[11] QNFO: POST QUANTUM SYNTHESIS | https://papers.qnfo.org/papers/post-quantum-synthesis  
[12] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis | https://papers.qnfo.org/papers/pqs-ai-evaluation-audit