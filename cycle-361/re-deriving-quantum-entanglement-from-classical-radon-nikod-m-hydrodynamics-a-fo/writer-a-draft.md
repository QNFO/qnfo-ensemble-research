# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The Hydrodynamic Stability Hypothesis (HSH) claims that quantum mechanics, including GHZ‑type Bell‑violating correlations, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction under a locally bounded hydrodynamic flow. The specific gap is the absence of an explicit derivation of GHZ‑type correlations from the hypothesis’s own axioms. We formalize HSH as four minimal axioms, derive the classical pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) on the four GHZ triple correlations, and show that quantum mechanics predicts a product of \(-1\). The resulting Mermin violation factor is \(2\) and the CHSH violation factor is \(\sqrt{2}\approx1.414214\). A labeled projection, conditional on the assumptions that the transport speed is bounded by \(c\), the barrier width is \(L=10^{-3}\,\mathrm{m}\), and the simulation timestep is at most one‑tenth of the crossing time, yields a required timestep of roughly \(333\,\mathrm{fs}\). The strong, local‑realist form of HSH is therefore falsified: any classical re‑derivation of GHZ statistics must relax at least one of the four axioms, and the logical fork comprises four distinct branches.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics, and if so which axiom of such a derivation they should expect to give up first. A falsification that identifies the specific axiom(s) under strain converts an open philosophical program into a bounded engineering decision.

Our contributions are:
1. Formalization of the strong form of HSH as four minimal axioms (Section 3.1).  
2. Derivation of the quantum GHZ stabilizer values and the classical pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) from the axioms, with full arithmetic (Sections 4.1–4.2).  
3. Quantitative Mermin and CHSH violation analysis, with violation factors \(2\) and \(\sqrt{2}\approx1.414214\) (Sections 4.3–4.4).  
4. A corrected falsification verdict that enumerates the full four‑branch fork of axiom relaxations (Section 4.5).  
5. A labeled projection of the temporal resolution a particle‑tracking test of the locality claim would need, conditional on stated assumptions (Section 4.6).

## 2. Background and Related Work

**Statistical‑mechanics mapping of quantum dynamics.** Entanglement dynamics in hybrid quantum circuits reveal that random‑circuit ensembles obey universal statistical laws, providing a bridge between many‑body quantum dynamics and classical spin models [1]. This motivates the ensemble‑focused phrasing of the axioms in Section 3.1.

**Multipartite entanglement as a network resource.** Distributing multipartite entanglement over noisy quantum networks is essential for quantum‑internet applications, with GHZ states representing the minimal multipartite resource [2]. Any classical foundation must reproduce the fidelity and rate metrics associated with such distribution.

**Absence of a classical analogue of entanglement.** The review of entanglement in the classical limit states that “there is no classical quantity corresponding to entanglement, it is not possible to compute a well‑defined classical version of Eq. (4)” [3]. This underscores the difficulty of reproducing GHZ stabilizer algebra with a purely classical binary response model.

**Tripartite entanglement in classical environments.** Studies of GHZ‑like states coupled to independent classical noise sources show dephasing behavior but treat the classical environment as an external probe rather than a substrate for deriving entanglement [4].

**Entanglement‑free classical regimes.** Analyses of coherent‑state limits identify entanglement‑free regimes where quantum Darwinism predicts classical pointer states, illustrating that certain quantum phenomena can emerge without entanglement [5].

**Hybrid entanglement in quantum networks.** Hierarchical quantum networks exploit hybrid entangled states as irreplaceable resources for teleportation, secret sharing, and secure communication [6].

**Hybrid classical‑quantum algorithms.** The existence of continuous trade‑offs between classical and quantum resources in hybrid algorithms demonstrates that partial quantum speed‑ups can be achieved without full quantum coherence [7]. HSH’s claim of a fully classical reconstruction is therefore more radical than these interpolations.

**Classical‑quantum unification via variable promotion.** Unified formulations discuss the difficulties of promoting classical phase‑space variables to quantum operators, an issue directly analogous to HSH’s attempt to promote Radon–Nikodým measures to quantum states [8].

**Hydrodynamic Stability Hypothesis.** The original HSH proposal introduces basins of attraction of classical probability measures and a locally bounded hydrodynamic flow as the mechanism for wavefunction relaxation, explicitly claiming to reproduce quantum statistics without non‑locality [10].

**Post‑Quantum Synthesis theorems.** The No‑Spooky‑Action and Correlation History theorems formalize the factorized local response structure that underlies Bell‑type constraints, providing the theoretical backbone for the product‑constraint derivation [11, 12].

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms:

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure \(\mu_{\psi}\ll\mu\) with Radon–Nikodým derivative \(\rho_{\psi}= \frac{d\mu_{\psi}}{d\mu}\), such that all quantum predictions are recoverable as functionals of \(\rho_{\psi}\).

- **(A2) Local hidden variables.** For \(N\) spatially separated parties, the hidden configuration decomposes as \(\lambda=(\lambda_{1},\ldots,\lambda_{N})\) with \(\lambda_{i}\in\Lambda_{i}\); each party’s outcome is a local function \(A_{i}=f_{i}(\lambda_{i},s_{i})\) of its own variable and its own setting \(s_{i}\).

- **(A3) Locally bounded continuous transport.** The time evolution \(\mu_{t}= (\Phi_{t})_{*}\mu_{0}\) is generated by a local flow \(\Phi_{t}\) on \(\Lambda\) propagating information at finite speed \(v_{\max}\), so that no influence connects spacelike‑separated events. Preparation and measurement correspond to relaxation into basins of attraction \(\mathcal{B}_{k}\subset\Lambda\) of stable measures, the observed outcome indexing the basin.

- **(A4) Free settings.** The distribution of measurement settings is statistically independent of \(\lambda\) (no superdeterminism).

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality expressed by the No‑Spooky‑Action and Correlation History theorems of [11, 12] (A2), and the rejection of superdeterminism implicit in [10] (A4). The formalization is our own; [10] does not publish a numbered axiom list, so alternative formalizations are discussed in Section 7.

### 3.2 Falsification protocol

Given A1–A4, we test whether the model can reproduce the quantum joint statistics of the GHZ state
\[
|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|000\rangle+|111\rangle\bigr)
\]
under local Pauli measurements \(X\) and \(Y\) on each qubit. The protocol is: (i) derive the classical constraint imposed by A1–A4 on the four relevant triple correlations, (ii) compute the quantum values of those correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re‑derive the quantum statistics from the classical axioms. The comparison uses the Mermin inequality as the primary instrument and the CHSH inequality as an independent two‑party cross‑check.

### 3.3 Simulation projection protocol

The hypothesis calls for particle‑tracking of the hydrodynamic transport \(\Phi_{t}\) [10]. We compute, as a labeled projection with stated assumptions, the propagation timescales such a simulation must resolve for the locality claim of A3 to be testable rather than vacuous: if the simulation’s timestep is coarser than the propagation time across the relevant barrier, a local continuous signal and an instantaneous change are observationally indistinguishable in the simulation, and the test loses its discriminating power. The projection is conditional on the assumed signal speed, barrier width and resolution convention; it is not a universal requirement of every particle‑tracking simulation.

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

### 4.2 The classical constraint from the axioms

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
since each local outcome appears exactly twice and squares to \(+1\). This identity follows from A2 alone: it holds for every assignment of the six local outcomes, independent of any distribution over \(\lambda\).

A4 (setting freedom) is required only to read the experimentally accessible correlations \(\langle P_{k}\rangle\) as expectations over a single distribution of \(\lambda\). With A4 in place, taking expectations with respect to the measure \(\mu\) (A1) gives
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
Hence the classical bound is \(M_{\mathrm{LHV}}=2\), the quantum value is \(M_{\mathrm{Q}}=4\), and the violation factor is
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
is incompatible with the GHZ stabilizer statistics. The complete fork of consistent relaxations is:

1. **Relax A2 (locality of response functions).** Allow the outcome functions \(A_{i}\) to depend on distant settings, thereby abandoning local realism in its response‑function form.  
2. **Relax A4 (setting freedom).** Permit correlations between \(\lambda\) and the measurement settings (superdeterminism), which would remove the single‑distribution assumption used to promote the pointwise identity to the observed correlations.  
3. **Relax A1 (classical probability grounding).** Replace the Kolmogorov measure space with a non‑classical probability structure, abandoning the Radon–Nikodým grounding that defines HSH.  
4. **Retain all four axioms and accept contradiction.** Concede that the model cannot reproduce the GHZ stabilizer values, i.e., that it is empirically refuted on these correlations.

Every branch falsifies the strong claim that HSH simultaneously satisfies A1–A4 and reproduces GHZ statistics. The verdict therefore identifies an incompatibility of the conjunction, not a unique culprit axiom, and the choice among branches is a research decision rather than a derivation.

### 4.6 Simulation timescale projection (explicitly labeled projection)

**Assumptions.**  
(P1) The transport speed is bounded by \(v_{\max}=c=3.0\times10^{8}\ \mathrm{m\,s^{-1}}\).  
(P2) The spatial barrier width is \(L=1.0\times10^{-3}\ \mathrm{m}\) (laboratory scale).  
(P3) The simulation timestep must be at most one‑tenth of the propagation time (a resolution convention).

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
2. **Classical pointwise constraint** (Section 4.2): \(P_{1}P_{2}P_{3}P_{4}=+1\) pointwise (consequence of A2 alone); with A4 this yields \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1\), conflicting with the quantum product \(-1\).  
3. **Mermin bound** (Section 4.3): classical \(M_{\mathrm{LHV}}=2\); quantum \(M_{\mathrm{Q}}=4\); violation factor \(2\).  
4. **CHSH bound** (Section 4.4): classical bound \(2\); quantum maximum \(2\sqrt{2}\approx2.828427\); violation factor \(\sqrt{2}\approx1.414214\).  
5. **Falsification verdict** (Section 4.5): the conjunction of A1–A4 is incompatible with the GHZ stabilizer statistics; the fork of consistent relaxations has four branches (relax A2, relax A4, relax A1, or retain all and accept empirical refutation).  
6. **Simulation timescale projections** (Section 4.6, conditional on P1–P3): for \(L=1.0\times10^{-3}\ \mathrm{m}\), \(t_{\min}=3.333333\times10^{-12}\ \mathrm{s}\), \(\Delta t\le3.333333\times10^{-13}\ \mathrm{s}\), \(N_{\mathrm{steps}}=10\); for \(L=1.0\ \mathrm{m}\), \(t_{\min}=3.333333\times10^{-9}\ \mathrm{s}\), \(N_{\mathrm{steps}}=1.0\times10^{4}\); in general \(t_{\min}=L/v_{\max}\), \(\Delta t\le t_{\min}/10\), \(N_{\mathrm{steps}}=10\).

## 6. Discussion

**Scope of the falsification.** The derivation shows that the strong claim of HSH—local classical measure theory reproducing GHZ‑type Bell‑violating correlations—is untenable as a conjunction. It does not identify a unique axiom that must be abandoned, and it does not address weaker versions that relax A2, reinterpret locality at the level of the flow \(\Phi_{t}\), or restrict the claim to states and measurements outside the GHZ stabilizer set.

**Potential escapes.**  
1. The formalization A1–A4 is our own interpretation; [10] does not publish a numbered axiom list, so an alternative formalization might locate the failure elsewhere. Any such formalization must still reproduce the four stabilizer values, and the counting argument of Section 4.2 applies to any model with local binary response functions and a setting‑independent hidden‑variable distribution.  
2. Stochastic response functions do not escape: the identity \(P_{1}P_{2}P_{3}P_{4}=+1\) holds pointwise for every assignment of the six local outcomes, so averaging over any distribution preserves it.  
3. The connection between basins of attraction (A3) and the Born rule is not derived here; a separate probabilistic mechanism might alter the mapping from \(\rho_{\psi}\) to observed frequencies, but it cannot change the algebraic constraint, which precedes any frequency mapping.  
4. Relaxing A4 (superdeterminism) is a logically open branch of the fork; HSH’s own framing rejects it, but the falsification alone does not close it.

**What would falsify the present result.** The central claim is the incompatibility of A1–A4 with the GHZ stabilizer statistics. A single concrete counterexample would overturn it: an explicit construction of local deterministic (or stochastic) response functions \(A_{i}(\lambda_{i},s_{i})\) on a classical probability space, with a setting‑independent \(\lambda\)‑distribution, that reproduce all four stabilizer values \(\langle XXX\rangle=+1\), \(\langle XYY\rangle=\langle YXY\rangle=\langle YYX\rangle=-1\). Equivalently, any demonstration that the pointwise product \(P_{1}P_{2}P_{3}P_{4}\) can equal \(-1\) for some assignment of six binary local outcomes would invalidate the counting argument, since the argument rests on each outcome appearing exactly twice in the product. Absent such a construction, the algebra is closed: six factors, each squared, is an identity in \(\{-1,+1\}^{6}\).

**Limitations.**  
- The formalization A1–A4 is an interpretation of [10]; a different formalization could shift which axiom bears the contradiction, though not the existence of a contradiction for any local‑response, setting‑free model.  
- The timescale projections depend on the assumed barrier width \(L\) and the generous speed bound \(v_{\max}=c\); other parameter choices scale the numbers linearly, and P3’s one‑tenth rule is a resolution convention, not a physical law. The projections are not requirements of every particle‑tracking simulation.  
- The analysis treats only the four GHZ stabilizer measurements; other settings (e.g., \(YYY\)) are omitted because they do not affect the contradiction.  
- The derivation assumes binary outcomes \(\pm1\); extensions to higher‑dimensional outcomes are not considered.  
- The CHSH cross‑check is a restatement of the Bell constraint for convex mixtures of factorized local models, as embodied in the Correlation History theorem of [11]; it does not constitute a new theorem.

**Failure modes.** If a construction of local deterministic (or stochastic) response functions satisfying A1–A4 and reproducing all four stabilizer values were exhibited, the pointwise product argument would be invalidated, falsifying the present falsification. Likewise, an empirical demonstration that the GHZ stabilizer statistics admit a local stochastic model with \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=-1\) would overturn the argument.

**Sensitivity analysis.** Varying the barrier width \(L\) by an order of magnitude changes the minimum propagation time \(t_{\min}=L/v_{\max}\) proportionally. The resolution convention (P3) fixes the timestep to one‑tenth of \(t_{\min}\), so the **number of timesteps required for a single crossing** remains exactly ten, independent of \(L\). For a macroscopic barrier (\(L=1.0\ \mathrm{m}\)) the crossing time is larger, yielding a total of \(10^{4}\) timesteps for the entire event, while the per‑crossing step count stays at ten. This linear scaling emphasizes that the primary engineering challenge at laboratory scales is achieving sub‑picosecond temporal resolution; at macroscopic scales the challenge shifts to handling larger absolute step counts.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols that rely on multipartite entanglement (e.g., secret sharing, distributed sensing) [2, 6], and theorists exploring classical‑quantum unification programs [8] would use this result to assess whether a purely local classical underpinning can support GHZ‑type correlations. If the result holds, any design that assumes a local‑realist foundation for GHZ‑type correlations must be revised to incorporate non‑local or hybrid mechanisms; effort can be redirected toward explicit relaxation of the identified axioms.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; under NASA Technology Readiness Level definitions it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3, and no manufacturing or deployment readiness is claimed.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic or stochastic response functions \(A_{i}(\lambda_{i},s_{i})\) on a classical probability space with a setting‑independent \(\lambda\)‑distribution that reproduce the four GHZ stabilizer values. A successful construction would falsify the present result; a demonstrated impossibility would convert the falsification from an analysis of one formalization into a theorem about the axiom class.

**(d) Engineering constraints.** The projection in Section 4.6 identifies the primary constraints for any simulation that attempts to verify the locality claim: (i) a maximum signal speed \(v_{\max}\) (taken as \(c\) for a generous bound), (ii) spatial barrier dimensions that set the propagation time, and (iii) a timestep resolution at most one‑tenth of the propagation time. No further material, computational, or cost constraints are derived from the analysis.

**(e) Projected performance bounds.** Assuming the barrier width \(L=1.0\times10^{-3}\ \mathrm{m}\) and \(v_{\max}=c\), the required timestep is \(\Delta t\le3.33\times10^{-13}\ \mathrm{s}\) (\(\approx333\ \mathrm{fs}\)). For a macroscopic barrier \(L=1.0\ \mathrm{m}\), the required number of steps increases to \(10^{4}\) while the timestep remains the same. These are projections conditional on the stated assumptions.

**(f) Direct risks or misuse paths.** No immediate misuse is identified; the result merely constrains theoretical program design. Misinterpretation of the falsification as a proof that all classical approaches are impossible would be a misuse; the paper explicitly limits the claim to the strong, local form of HSH.

## 8. Conclusion

By formalizing the Hydrodynamic Stability Hypothesis as four minimal axioms and deriving the algebraic pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\), we have shown that the hypothesis cannot simultaneously satisfy locality, measurement‑setting freedom, and reproduce the GHZ stabilizer statistics of quantum mechanics. The resulting Mermin and CHSH violations quantify the gap between the classical bound and quantum predictions. Projection of the required simulation timescales clarifies the engineering demands of any particle‑tracking test of the hypothesis. The strong, local‑realist version of HSH is therefore falsified; any viable classical re‑grounding must relax at least one of the axioms.

## References

[1] arXiv:2111.08018v2 | Entanglement dynamics in hybrid quantum circuits  
[2] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks  
[3] arXiv:1110.0157v1 | Entanglement, the quantum formalism and the classical world  
[4] arXiv:2107.11259v1 | Probing tripartite entanglement and coherence dynamics in pure and mixed independent classical environments  
[5] arXiv:1206.5715v2 | Coherent states and the classical-quantum limit considered from the point of view of entanglement  
[6] arXiv:2004.13176v3 | Hierarchical Quantum Network using Hybrid Entanglement  
[7] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations  
[8] arXiv:2010.03984v2 | A Unified Combination of Classical and Quantum Systems  
[9] QNFO: Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis. https://papers.qnfo.org/papers/re-deriving-quantum-entanglement-from-classical-radon-nikod-m-hydrodynamics-a-fo  
[10] QNFO: Hydrodynamic Stability Hypothesis. https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis  
[11] QNFO: POST QUANTUM SYNTHESIS. https://papers.qnfo.org/papers/post-quantum-synthesis  
[12] QNFO: PQS AI‑Evaluation Audit: Post‑Quantum Synthesis Investigation and AI Gate‑Check Analysis. https://papers.qnfo.org/papers/pqs-ai-evaluation-audit