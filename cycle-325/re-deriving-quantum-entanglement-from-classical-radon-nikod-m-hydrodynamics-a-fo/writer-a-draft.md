# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) proposes that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction of classical probability measures under a locally bounded hydrodynamic transport. The specific gap is the absence of an explicit derivation of GHZ‑type Bell‑violating correlations from the hypothesis’s own axioms. We formalize the strong form of HSH as four minimal axioms (classical measure grounding, local hidden variables, locally bounded continuous transport, and free measurement settings) and derive, with full arithmetic, that the axioms force the pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) on the four GHZ triple correlations, whereas quantum mechanics predicts a product of \(-1\). The resulting Mermin violation factor is \(2\) and the CHSH violation factor is \(\sqrt{2}\approx1.414214\). We also compute, as a labeled projection conditional on stated assumptions, that a particle‑tracking simulation of the hydrodynamic transport at a millimetre‑scale barrier would need timesteps of about \(333\ \mathrm{fs}\) to resolve the fastest local signals the hypothesis permits. The strong form of HSH is therefore falsified: any classical re‑derivation of GHZ statistics must relax at least one axiom, and the fork of consistent relaxations comprises four distinct branches.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics, and if so which axiom of such a derivation they should expect to give up first. A falsification that identifies the specific axiom(s) under strain converts an open philosophical program into a bounded engineering decision.

Our contributions are:
1. Formalization of the strong form of HSH as four minimal axioms (Section 3.1).  
2. Derivation of the quantum GHZ stabilizer values and the classical pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) from the axioms, with full arithmetic (Sections 4.1–4.2).  
3. Quantitative Mermin and CHSH violation analysis, with violation factors \(2\) and \(\sqrt{2}\approx1.414214\) (Sections 4.3–4.4).  
4. A corrected falsification verdict that enumerates the full fork of axiom relaxations rather than a binary choice (Section 4.5).  
5. A labeled projection of the temporal resolution a particle‑tracking test of the locality claim would need, conditional on stated assumptions (Section 4.6).

## 2. Background and Related Work

**Ensemble‑statistical view of quantum dynamics.** Reference [1] develops the philosophy that while individual instances of complex quantum circuits are intractable to simulate, the statistical properties of random ensembles obey simple universal laws, and it maps measurement‑induced phase transitions in random circuits onto classical statistical‑mechanics spin models, deriving averaged Rényi entropies as domain‑wall free energies in a replica limit. This establishes that classical statistical descriptions of quantum information operate at the ensemble level, which is why the axioms of Section 3.1 are phrased for ensembles of hidden configurations rather than single trajectories.

**Multipartite entanglement as a network resource.** Reference [2] presents an algorithm for generating multipartite entanglement between nodes of a noisy quantum network, computing the fidelity of the final state from memory noise and decoherence and the distribution rate from communication time and process stochasticity, and proving optimality under a star‑scheme when links may be reused. Any classical foundation that claims to re‑derive quantum statistics must reproduce exactly these fidelity and rate metrics for quantum‑network applications to function as designed; the GHZ correlations tested in Section 4 are the smallest multipartite instance of that requirement.

**Tripartite entanglement under classical environments.** Reference [4] examines three non‑interacting qubits prepared in a maximally entangled GHZ‑like state coupled to independent classical environments, using an entanglement witness \(E(t)=-\mathrm{Tr}[\mathbb{W}_{o}\rho_{abc}(t)]\) and reporting that dephasing of tripartite non‑local correlation differs fundamentally between pure and mixed noisy configurations, with power‑law noise more damaging in the mixed case. This is the closest antecedent to HSH's program in the literature, but it treats the classical environments as external probes that degrade quantum coherence, not as a substrate from which the quantum statistics are derived; the falsification in Section 4 concerns the latter, stronger claim.

**Entanglement‑free classical regimes.** Reference [5] identifies three classical paradigms (material point, test particle, diluted droplet) as limit cases of a quantum regime in which interacting particles do not entangle, connecting them to Quantum Darwinism's environment‑induced superselection principle and showing that coherent states are classical pointer states under a maximal‑information rule. This work demonstrates that large portions of classical behaviour can be recovered from quantum descriptions without entanglement; HSH claims the converse derivation, and the GHZ stabilizer algebra shows the converse cannot hold locally.

**Classical–quantum interpolation inside the quantum formalism.** Reference [7] derives the scaling of the \(\alpha\)-QPE family of phase‑estimation algorithms within the Quantum Singular Value Transformation framework, trading circuit depth against statistical sampling with the approximation parameters related by \(\eta+\frac{1}{2}\delta^{\alpha}=1\). This program interpolates between classical and quantum resources while remaining inside the quantum formalism; HSH's claim is more radical because it reverses the direction of derivation, and Section 4 shows the reversal fails at the level of multipartite correlations.

**Unified classical–quantum formulations.** Reference [8] builds a continuous passage between classical and quantized descriptions through a common action functional, and flags the central obstruction: promoting classical variables to operators is not canonical, since \(\overline{H}(\overline{P},\overline{Q})\neq H(P,Q)\) under variable change, so a procedure for choosing the correct promotion is required. HSH's Radon–Nikodým grounding faces an analogous promotion problem from measures to quantum states, and the GHZ analysis shows that no local promotion reproduces the stabilizer values.

**Hydrodynamic Stability Hypothesis.** Reference [10] proposes HSH as a local‑realist, measure‑theoretic reconstruction of quantum mechanics, introducing basins of attraction of classical probability measures and a locally bounded hydrodynamic flow as the mechanism for wavefunction relaxation. The hypothesis explicitly claims to reproduce quantum statistics without non‑locality, providing the target for the present falsification.

**Post‑Quantum Synthesis (PQS).** Reference [11] proves a No‑Spooky‑Action theorem (local operations on one system leave the spatially separated marginal unchanged) and a Correlation History theorem expressing joint statistics as \(P(o_{1},o_{2})=\sum_{i}|c_{i}|^{2}P_{1}(o_{1}|\phi_{1}^{i})P_{2}(o_{2}|\phi_{2}^{i})\). These theorems formalize the factorized local response structure that underlies Bell‑type constraints, directly relevant to the product‑constraint derivation in Section 4.2.

**PQS AI‑Evaluation Audit.** Reference [12] documents an independent audit of PQS, confirming the derivations of the No‑Spooky‑Action and Correlation History theorems and highlighting that any model with local binary response functions and setting‑independent hidden variables must satisfy the same Bell constraints analyzed here.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms:

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure \(\mu_{\psi}\ll\mu\) with Radon–Nikodým derivative \(\rho_{\psi}= \frac{d\mu_{\psi}}{d\mu}\), such that all quantum predictions are recoverable as functionals of \(\rho_{\psi}\).

- **(A2) Local hidden variables.** For \(N\) spatially separated parties, the hidden configuration decomposes as \(\lambda=(\lambda_{1},\ldots,\lambda_{N})\) with \(\lambda_{i}\in\Lambda_{i}\); each party’s outcome is a local function \(A_{i}=f_{i}(\lambda_{i},s_{i})\) of its own variable and its own setting \(s_{i}\).

- **(A3) Locally bounded continuous transport.** The time evolution \(\mu_{t}= (\Phi_{t})_{*}\mu_{0}\) is generated by a local flow \(\Phi_{t}\) on \(\Lambda\) propagating information at finite speed \(v_{\max}\), so that no influence connects spacelike‑separated events. Preparation and measurement correspond to relaxation into basins of attraction \(\mathcal{B}_{k}\subset\Lambda\) of stable measures, the observed outcome indexing the basin.

- **(A4) Free settings.** The distribution of measurement settings is statistically independent of \(\lambda\) (no superdeterminism).

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality expressed by the No‑Spooky‑Action and Correlation History theorems of [11] (A2), and the rejection of superdeterminism implicit in [10] (A4). The formalization is our own; [10] does not publish a numbered axiom list, so alternative formalizations are discussed in Section 6.

### 3.2 Falsification protocol

Given A1–A4, we test whether the model can reproduce the quantum joint statistics of the GHZ state
\[
|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|000\rangle+|111\rangle\bigr)
\]
under local Pauli measurements \(X\) and \(Y\) on each qubit. The protocol is: (i) derive the classical constraint imposed by A1–A4 on the four relevant triple correlations, (ii) compute the quantum values of those correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re‑derive the quantum statistics from the classical axioms. The comparison uses the Mermin inequality as the primary instrument and the CHSH inequality as an independent two‑party cross‑check.

### 3.3 Simulation projection protocol

The hypothesis calls for particle‑tracking of the hydrodynamic transport \(\Phi_{t}\) [10]. We compute, as a labeled projection with stated assumptions, the propagation timescales such a simulation must resolve for the locality claim of A3 to be testable rather than vacuous: if the simulation’s timestep is coarser than the propagation time across the relevant barrier, a local continuous signal and an instantaneous change are observationally indistinguishable in the simulation, and the test loses its discriminating power.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (assumption).** The GHZ state is \(|\mathrm{GHZ}\rangle=(|000\rangle+|111\rangle)/\sqrt{2}\).

**Input 2 (assumption).** Pauli operators \(X\) and \(Y\) have eigenvalues \(\pm1\), with actions \(X|0\rangle=|1\rangle\), \(X|1\rangle=|0\rangle\), \(Y|0\rangle=i|1\rangle\), \(Y|1\rangle=-i|0\rangle\).

Applying the stabilizer operators:
\[
\begin{aligned}
XXX\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(|111\rangle+|000\rangle\bigr)=+|\mathrm{GHZ}\rangle,\\
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
(+1)\times(-1)\times(-1)\times(-1)=-1.
\]

### 4.2 The classical constraint from axioms A1–A4

For each party \(i\in\{1,2,3\}\) define local predetermined outcomes \(A_{i}^{X},A_{i}^{Y}\in\{-1,+1\}\), which exist by A2. The four triple products are
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
\bigl|\langle P_{1}\rangle-\langle P_{2}\rangle-\langle P_{3}\rangle-\langle P_{4}\rangle\bigr|\le 2,
\]
because pointwise \(|P_{1}-P_{2}-P_{3}-P_{4}|=2\) whenever \(P_{1}P_{2}P_{3}P_{4}=+1\). The quantum values give
\[
\bigl|(+1)-(-1)-(-1)-(-1)\bigr|=|1+1+1+1|=4.
\]
Hence the classical bound is \(M_{\mathrm{LHV}}=2\), the quantum value is \(M_{\mathrm{Q}}=4\), the gap \(\Delta M = 2\), and the violation factor is
\[
\frac{M_{\mathrm{Q}}}{M_{\mathrm{LHV}}}= \frac{4}{2}=2.
\]

### 4.4 CHSH cross‑check

For two parties the CHSH combination is
\[
S = E(a,b) + E(a,b') + E(a',b) - E(a',b').
\]
Classically \(|S|\le 2\). Quantum mechanics attains the Tsirelson bound \(S_{\max}=2\sqrt{2}\). Using \(\sqrt{2}\approx1.414214\):
\[
2\sqrt{2}\approx 2\times1.414214 = 2.828427.
\]
The violation factor over the classical bound is
\[
\frac{2\sqrt{2}}{2}= \sqrt{2}\approx1.414214.
\]

### 4.5 The fork and the falsification verdict

The derivation establishes that the conjunction
\[
\text{A1}\;\wedge\;\text{A2}\;\wedge\;\text{A3}\;\wedge\;\text{A4}
\]
is incompatible with the GHZ stabilizer statistics: the product constraint of Section 4.2 follows from A2 together with A4, and the contradiction with Section 4.1 follows once A1 commits all predictions to functionals of the classical measure. The complete fork of consistent relaxations is:

1. **Relax A2 (locality of response functions).** Allow the outcome functions \(A_{i}\) to depend on distant settings, thereby abandoning local realism in its response‑function form.  
2. **Relax A4 (setting freedom).** Permit correlations between \(\lambda\) and the measurement settings (superdeterminism), which HSH explicitly excludes but which would remove the single \(\lambda\)‑distribution assumption used in the product constraint.  
3. **Relax A1 (classical probability grounding).** Replace the Kolmogorov measure space with a non‑classical probability structure, abandoning the Radon–Nikodým grounding that defines HSH.  
4. **Retain all four axioms and accept contradiction.** Concede that the model cannot reproduce the GHZ stabilizer values, i.e., that it is empirically refuted on these correlations.

Every branch falsifies the strong claim that HSH simultaneously satisfies A1–A4 and reproduces GHZ statistics. The corrected verdict therefore identifies an incompatibility of the conjunction, not a unique culprit axiom, and the choice among branches is a research decision rather than a derivation.

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

These projections are conditional on P1–P3 and establish the temporal resolution any particle‑tracking simulation must achieve in order to discriminate a continuous local signal from an instantaneous state change across a barrier of the assumed width.

## 5. Results

All quantitative statements below follow directly from the arithmetic in Section 4.

1. **Quantum GHZ correlations** (Section 4.1): \(\langle XXX\rangle_{Q}=+1\); \(\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1\).  
2. **Classical pointwise constraint** (Section 4.2): \(P_{1}P_{2}P_{3}P_{4}=+1\) pointwise, implying \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1\), which conflicts with the quantum product \(-1\).  
3. **Mermin bound** (Section 4.3): classical \(M_{\mathrm{LHV}}=2\); quantum \(M_{\mathrm{Q}}=4\); violation factor \(2\).  
4. **CHSH bound** (Section 4.4): classical bound \(2\); quantum maximum \(2\sqrt{2}\approx2.828427\); violation factor \(\sqrt{2}\approx1.414214\).  
5. **Falsification verdict** (Section 4.5): the conjunction of A1–A4 is incompatible with the GHZ stabilizer statistics; the fork of consistent relaxations has four branches (relax A2, relax A4, relax A1, or retain all and accept empirical refutation).  
6. **Simulation timescale projections** (Section 4.6, conditional on P1–P3): for \(L=1.0\times10^{-3}\ \mathrm{m}\), \(t_{\min}=3.333333\times10^{-12}\ \mathrm{s}\), \(\Delta t\le3.333333\times10^{-13}\ \mathrm{s}\), \(N_{\mathrm{steps}}=10\); for \(L=1.0\ \mathrm{m}\), \(t_{\min}=3.333333\times10^{-9}\ \mathrm{s}\), \(N_{\mathrm{steps}}=1.0\times10^{4}\).

## 6. Discussion

**Scope of the falsification.** The derivation shows that the strong claim of HSH—local classical measure theory reproducing GHZ‑type Bell‑violating correlations—is untenable as a conjunction. It does not identify a unique axiom that must be abandoned, and it does not address weaker versions that relax A2, reinterpret locality at the level of the flow \(\Phi_{t}\), or restrict the claim to states and measurements outside the GHZ stabilizer set.

**Potential escapes.**  
1. The formalization A1–A4 is our own interpretation; [10] does not publish a numbered axiomatization, so an alternative formalization might locate the failure elsewhere. Any such formalization must still reproduce the four stabilizer values, and the counting argument of Section 4.2 applies to any model with local binary response functions and a setting‑independent hidden‑variable distribution.  
2. Stochastic response functions do not escape: the identity \(P_{1}P_{2}P_{3}P_{4}=+1\) holds pointwise for every assignment of the six local outcomes, so averaging over any distribution preserves it.  
3. The connection between basins of attraction (A3) and the Born rule is not derived here; a separate probabilistic mechanism might alter the mapping from \(\rho_{\psi}\) to observed frequencies, but it cannot change the algebraic constraint, which precedes any frequency mapping.  
4. Relaxing A4 (superdeterminism) is a logically open branch of the fork; HSH’s own framing rejects it, but the falsification alone does not close it.

**Limitations.**  
- The timescale projections depend on the assumed barrier width \(L\) and the generous speed bound \(v_{\max}=c\); other parameter choices scale the numbers linearly, and P3’s one‑tenth rule is a resolution convention, not a physical law.  
- The analysis treats only the four GHZ stabilizer measurements; other settings (e.g., \(YYY\)) are omitted because they do not affect the contradiction.  
- The derivation assumes binary outcomes \(\pm1\); extensions to higher‑dimensional outcomes are not considered.  

**Failure modes.** If a construction of local deterministic (or stochastic) response functions satisfying A1–A4 and reproducing all four stabilizer values were exhibited, the pointwise product argument would be invalidated, falsifying the present falsification. Likewise, an empirical demonstration that the GHZ stabilizer statistics admit a local stochastic model with \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=-1\) would overturn the argument.

**Sensitivity analysis.** Varying the barrier width \(L\) by an order of magnitude changes the minimum propagation time \(t_{\min}\) proportionally, while the required timestep \(\Delta t\) remains one‑tenth of \(t_{\min}\). Consequently, the number of timesteps for a crossing remains fixed at ten, independent of \(L\). This linear scaling emphasizes that the primary engineering challenge is achieving sub‑picosecond temporal resolution rather than handling large numbers of steps.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols of the kind optimized in [2], and theorists exploring classical‑quantum unification programs of the kind in [8] would use this result to assess whether a purely local classical underpinning can support multipartite entanglement resources. If the result holds, any design that assumes a local‑realist foundation for GHZ‑type correlations must be revised to incorporate non‑local or hybrid mechanisms; effort can be redirected toward explicit relaxation of the identified axioms.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; under NASA Technology Readiness Level definitions it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3, and no manufacturing or deployment readiness is claimed.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic or stochastic response functions \(A_{i}(\lambda_{i},s_{i})\) on a classical probability space with a setting‑independent \(\lambda\)‑distribution that reproduce the four GHZ stabilizer values. A successful construction would falsify the present result; a demonstrated impossibility would convert the falsification from an analysis of one formalization into a theorem about the axiom class.

**(d) Engineering constraints.** The projection in Section 4.6 identifies the primary constraints for any simulation that attempts to verify the locality claim: (i) a maximum signal speed \(v_{\max}\) (taken as \(c\) for a generous bound), (ii) spatial barrier dimensions that set the propagation time, and (iii) a timestep resolution at least one‑tenth of the propagation time to resolve the signal. No further material, computational, or cost constraints are derived from the analysis.

**(e) Projected performance bounds.** Assuming the barrier width \(L=1.0\times10^{-3}\ \mathrm{m}\) and \(v_{\max}=c\), the required timestep is \(\Delta t\le3.33\times10^{-13}\ \mathrm{s}\) (\(\approx333\ \mathrm{fs}\)). For a macroscopic barrier \(L=1.0\ \mathrm{m}\), the required number of steps increases to \(10^{4}\) while the timestep remains the same. These are projections conditional on the stated assumptions.

**(f) Direct risks or misuse paths.** No immediate misuse is identified; the result merely constrains theoretical program design. Misinterpretation of the falsification as a proof that all classical approaches are impossible would be a misuse; the paper explicitly limits the claim to the strong, local form of HSH.

## 8. Conclusion

By formalizing the Hydrodynamic Stability Hypothesis as four minimal axioms and deriving the algebraic pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\), it has been shown that the hypothesis cannot simultaneously satisfy locality, measurement‑setting freedom, and reproduce the GHZ stabilizer statistics of quantum mechanics. The resulting Mermin and CHSH violations quantify the gap between the classical bound and quantum predictions. Projection of the required simulation timescales clarifies the engineering demands of any particle‑tracking test of the hypothesis. The strong, local‑realist version of HSH is therefore falsified; any viable classical re‑grounding must relax at least one of the axioms.

## References

[1] arXiv:2111.08018v2 | Entanglement dynamics in hybrid quantum circuits  
[2] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks  
[4] arXiv:2107.11259v1 | Probing tripartite entanglement and coherence dynamics in pure and mixed independent classical environments  
[5] arXiv:1206.5715v2 | Coherent states and the classical-quantum limit considered from the point of view of entanglement  
[7] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations  
[8] arXiv:2010.03984v2 | A Unified Combination of Classical and Quantum Systems  
[10] QNFO: Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis  
[11] QNFO: POST QUANTUM SYNTHESIS | https://papers.qnfo.org/papers/post-quantum-synthesis  
[12] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis | https://papers.qnfo.org/papers/pqs-ai-evaluation-audit  

## Appendix A. Divergence report

**Divergence 1 – Fork of axiom relaxations (Section 4.5).**  
- *Writer A* presented a binary fork: (i) abandon A2 (locality) or (ii) accept contradiction.  
- *Writer B* enumerated four distinct branches: relax A2, relax A4 (setting freedom), relax A1 (classical grounding), or retain all axioms and accept empirical refutation.  

*Chosen convention:* The four‑branch enumeration from Writer B is retained, as it more completely reflects the logical possibilities arising from the product‑constraint derivation and aligns with the broader literature on Bell‑type constraints.