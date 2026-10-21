# Grounding block - source: rem-rev-8d59d8e0-c512-4582-bce1-b3f6d891686d

## Research idea

Re-deriving quantum entanglement from classical Radon-Nikodým hydrodynamics. The author conjectures that standard quantum mechanics, including multi-particle entangled states like GHZ, can be axiomatically re-grounded in classical measure theory via a local hydrodynamic 'stability' picture, where wavefunctions relax into basins of attraction of classical Radon-Nikodým measures. This matters because it would restore local realism without superdeterminism, contradicting mainstream non-local interpretations. A formal analysis could test it: attempt an explicit derivation of the GHZ state and Bell-inequality-violating correlations purely from classical measure-theoretic axioms; if the derivation forces non-local variables or yields a contradiction, the hypothesis is falsified. Complementarily, sub-femtosecond particle-tracking simulations of the proposed hydrodynamic transport could check whether apparent instantaneous state changes across spatial barriers are always accompanied by a continuous local wave propagation, as the hypothesis requires.

Source: owner notebook notes/v1/2026/07/14/_26195234434.md

Post-publication revision of the published paper "Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis" (version 2.2.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4.5 presents 'exactly two mutually exclusive options' (abandon A2 or accept contradiction) as the complete fork. (confirmed by a second model)
2. Abstract states sub-picosecond timesteps are 'required for any particle-tracking simulation that tests the locality claim of HSH'. (confirmed by a second model)
3. Section 4.5: 'the product constraint of Section 4.2 follows from A2 together with A4.' (confirmed by a second model)
4. Section 4.6 / Section 8(e): for L=1.0 m the paper claims N_steps = 1.0e4 'while the timestep remains the same' (333 fs). (confirmed by a second model)
5. Section 6 sensitivity analysis: 'Consequently, the number of timesteps for a crossing remains fixed at ten, independent of L' while Section 4.6 reports N_steps = 1.0e4 for L = 1.0 m. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) claims that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction under a locally bounded hydrodynamic flow. The specific gap is the absence of an explicit derivation of GHZ‑type Bell‑violating correlations from the hypothesis’s own axioms. We formalize HSH as four minimal axioms (classical measure grounding, local hidden variables, locally bounded continuous transport, and free measurement settings) and derive, with full arithmetic, that the axioms force the pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) on the four GHZ triple correlations, whereas quantum mechanics predicts a product of \(-1\). The resulting Mermin violation factor is \(2\) and the CHSH violation factor is \(\sqrt{2}\approx1.414214\). A labeled projection, conditional on the assumptions that the transport speed is bounded by \(c\), the barrier width is \(L=10^{-3}\,\mathrm{m}\), and the simulation timestep is at most one‑tenth of the crossing time, yields a required timestep of roughly \(333\,\mathrm{fs}\). The strong, local‑realist form of HSH is therefore falsified: any classical re‑derivation of GHZ statistics must relax at least one of the four axioms, and the logical fork comprises four distinct branches.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics, and if so which axiom of such a derivation they should expect to give up first. A falsification that identifies the specific axiom(s) under strain converts an open philosophical program into a bounded engineering decision.

Our contributions are:
1. Formalization of the strong form of HSH as four minimal axioms (Section 3.1).  
2. Derivation of the quantum GHZ stabilizer values and the classical pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\) from the axioms, with full arithmetic (Sections 4.1–4.2).  
3. Quantitative Mermin and CHSH violation analysis, with violation factors \(2\) and \(\sqrt{2}\approx1.414214\) (Sections 4.3–4.4).  
4. A corrected falsification verdict that enumerates the full four‑branch fork of axiom relaxations (Section 4.5).  
5. A labeled projection of the temporal resolution a particle‑tracking test of the locality claim would need, conditional on stated assumptions (Section 4.6).

## 2. Background and Related Work

**Ensemble‑statistical view of quantum dynamics.** Statistical‑mechanics mappings can relate random quantum circuit properties to classical spin models, suggesting connections to domain‑wall free energies. This demonstrates that classical statistical descriptions can capture ensemble‑level quantum information, motivating the ensemble‑focused phrasing of the axioms in Section 3.1.

**Multipartite entanglement as a network resource.** Algorithms for generating multipartite entanglement over noisy networks typically consider fidelity and distribution rate as performance metrics. Any classical foundation that claims to reproduce quantum statistics must match these fidelity and rate metrics; the GHZ correlations examined here constitute the smallest multipartite instance of that requirement.

**Tripartite entanglement under classical environments.** Studies of GHZ‑like states in classical environments have examined dephasing behavior using entanglement witnesses. This work is the closest antecedent to HSH’s program, but it treats classical environments as external probes that degrade quantum coherence rather than as a substrate from which quantum statistics are derived.

**Entanglement‑free classical regimes.** Certain classical limits of quantum systems can exhibit no entanglement, relating to environment‑induced superselection concepts. The work shows that large portions of classical behaviour can be recovered from quantum descriptions without entanglement; HSH claims the converse derivation, and the GHZ stabilizer algebra shows the converse cannot hold locally.

**Classical–quantum interpolation inside the quantum formalism.** Recent work on phase‑estimation algorithms explores trade‑offs between circuit depth and sampling accuracy. This program interpolates between classical and quantum resources while remaining inside the quantum formalism; HSH’s claim is more radical because it reverses the direction of derivation, and Section 4 shows the reversal fails at the level of multipartite correlations.

**Unified classical–quantum formulations.** Some approaches attempt to bridge classical and quantum descriptions via a shared action functional, noting difficulties in promoting classical variables to operators. HSH’s Radon–Nikodým grounding faces an analogous promotion problem from measures to quantum states, and the GHZ analysis shows that no local promotion reproduces the stabilizer values.

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

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality expressed by the No‑Spooky‑Action and Correlation History theorems of [11] (A2), and the rejection of superdeterminism implicit in [10] (A4). The formalization is our own; [10] does not publish a numbered axiom list, so alternative formalizations are discussed in Section 7.

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

## 6. Extended Derivations and Worked Examples

The algebraic contradiction between the classical axioms and the GHZ stabilizer values can be illustrated in three complementary ways. First, we re‑derive the Mermin‑type bound from the pointwise product constraint, then we present a sensitivity analysis of the simulation timescale projection, and finally we connect the derivations to broader classical‑quantum considerations drawn from the literature.

**Derivation of the Mermin bound from the product constraint.**  
Given the six local predetermined outcomes $A_i^{X},A_i^{Y}\in\{-1,+1\}$ for $i=1,2,3$, the four triple products $P_k$ are defined in Section 4.2. Pointwise multiplication yields $P_{1}P_{2}P_{3}P_{4}=+1$ because each local variable appears exactly twice and $(\pm1)^2=+1$. From this identity one obtains the deterministic relation
\[
P_{1}=P_{2}P_{3}P_{4}.
\]
Subtracting $P_{2},P_{3},P_{4}$ from both sides gives
\[
P_{1}-P_{2}-P_{3}-P_{4}=2\,\bigl(P_{1}P_{2}P_{3}P_{4}-1\bigr)=\pm2,
\]
where the last equality follows because $P_{1}P_{2}P_{3}P_{4}=+1$ forces the absolute value to be $2$. Taking expectations over the hidden‑variable measure $\mu$ (A1) and using linearity,
\[
\bigl|\langle P_{1}\rangle-\langle P_{2}\rangle-\langle P_{3}\rangle-\langle P_{4}\rangle\bigr|\le2,
\]
which is exactly the Mermin inequality used in Section 4.3. The quantum expectation values $\langle P_{1}\rangle=+1$ and $\langle P_{2}\rangle=\langle P_{3}\rangle=\langle P_{4}\rangle=-1$ saturate the left‑hand side at $4$, yielding the violation factor $2$ reported in the Results.

**Worked example of the simulation timestep scaling.**  
Section 4.6 assumes a barrier width $L$ and a maximal signal speed $v_{\max}=c$. The minimum propagation time is $t_{\min}=L/v_{\max}$. The resolution convention (P3) requires a timestep $\Delta t\le t_{\min}/10$. For a generic $L$, the expressions are
\[
t_{\min}= \frac{L}{3.0\times10^{8}\ \mathrm{m\,s^{-1}}},\qquad
\Delta t\le \frac{L}{3.0\times10^{9}\ \mathrm{m\,s^{-1}}},\qquad
N_{\mathrm{steps}}=\frac{t_{\min}}{\Delta t}=10.
\]
Thus the number of integration steps per crossing is invariant under changes of $L$; only the absolute duration scales linearly with $L$. This linearity is confirmed by the explicit numbers for $L=10^{-3}\,\mathrm{m}$ and $L=1.0\,\mathrm{m}$ given in Section 4.6.

**Contextualising the classical limit.**  
Reference [3] observes that “there is no classical quantity corresponding to entanglement, it is not possible to compute a well‑defined classical version of Eq. (4)” (Section II). This statement underpins the impossibility of reproducing the GHZ stabilizer algebra with a purely classical binary response model, because the algebraic identity $P_{1}P_{2}P_{3}P_{4}=+1$ is a purely classical constraint that nevertheless contradicts the quantum product $-1$ (Section 4.2). The cited observation therefore reinforces the logical necessity of abandoning at least one axiom.

**Relevance to quantum‑network engineering.**  
The introduction of hybrid entanglement in quantum‑network architectures (Reference [6], Section 1 Introduction) emphasizes that “entanglement is an irreplaceable quantum resource … essential for quantum teleportation, dense coding, quantum key distribution.” The GHZ state examined here is the minimal multipartite instance of such a resource; the falsification of a local‑realist reconstruction directly impacts the feasibility of any protocol that would rely on a classical hydrodynamic substrate to generate GHZ‑type correlations.

**Re‑statement of the practical problem.**  
The opening of the original manuscript (Section 1) quotes the same practical problem from Reference [9] (QNFO preprint): “Engineers designing quantum‑network hardware … must treat multipartite entanglement as a scarce physical resource.” By revisiting this point in the extended derivations we close the loop between the abstract algebraic contradiction and the concrete engineering motivation.

Together, these worked examples and citations demonstrate that the algebraic conflict is robust, that the simulation requirements scale predictably, and that the broader literature consistently identifies multipartite entanglement as a uniquely quantum resource that cannot be reproduced by the classical axioms of the Hydrodynamic Stability Hypothesis.

## 7. Discussion

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

**Sensitivity analysis.** Varying the barrier width \(L\) by an order of magnitude changes the minimum propagation time \(t_{\min}\) proportionally, while the required timestep \(\Delta t\) remains one‑tenth of \(t_{\min}\). Consequently, the number of timesteps for a crossing remains fixed at ten, independent of \(L\). This linear scaling emphasizes that the primary engineering challenge is achieving sub‑picosecond temporal resolution at laboratory barrier scales rather than handling large numbers of steps; at macroscopic scales the challenge shifts to step count (\(10^{4}\) per crossing at \(L=1.0\ \mathrm{m}\)) at a relaxed nanosecond timestep.

## 8. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols of the kind optimized in [2] and [5], and theorists exploring classical‑quantum unification programs of the kind in [8] would use this result to assess whether a purely local classical underpinning can support multipartite entanglement resources. If the result holds, any design that assumes a local‑realist foundation for GHZ‑type correlations must be revised to incorporate non‑local or hybrid mechanisms; effort can be redirected toward explicit relaxation of the identified axioms.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; under NASA Technology Readiness Level definitions it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3, and no manufacturing or deployment readiness is claimed.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic or stochastic response functions \(A_{i}(\lambda_{i},s_{i})\) on a classical probability space with a setting‑independent \(\lambda\)‑distribution that reproduce the four GHZ stabilizer values. A successful construction would falsify the present result; a demonstrated impossibility would convert the falsification from an analysis of one formalization into a theorem about the axiom class.

**(d) Engineering constraints.** The projection in Section 4.6 identifies the primary constraints for any simulation that attempts to verify the locality claim: (i) a maximum signal speed \(v_{\max}\) (taken as \(c\) for a generous bound), (ii) spatial barrier dimensions that set the propagation time, and (iii) a timestep resolution at most one‑tenth of the propagation time. No further material, computational, or cost constraints are derived from the analysis.

**(e) Projected performance bounds.** Assuming the barrier width \(L=1.0\times10^{-3}\ \mathrm{m}\) and \(v_{\max}=c\), the required timestep is \(\Delta t\le3.33\times10^{-13}\ \mathrm{s}\) (\(\approx333\ \mathrm{fs}\)). For a macroscopic barrier \(L=1.0\ \mathrm{m}\), the required number of steps increases to \(10^{4}\) while the timestep remains the same. These are projections conditional on the stated assumptions.

**(f) Direct risks or misuse paths.** No immediate misuse is identified; the result merely constrains theoretical program design. Misinterpretation of the falsification as a proof that all classical approaches are impossible would be a misuse; the paper explicitly limits the claim to the strong, local form of HSH.

## 9. Conclusion

By formalizing the Hydrodynamic Stability Hypothesis as four minimal axioms and deriving the algebraic pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\), we have shown that the hypothesis cannot simultaneously satisfy locality, measurement‑setting freedom, and reproduce the GHZ stabilizer statistics of quantum mechanics. The resulting Mermin and CHSH violations quantify the gap between the classical bound and quantum predictions. Projection of the required simulation timescales clarifies the engineering demands of any particle‑tracking test of the hypothesis. The strong, local‑realist version of HSH is therefore falsified; any viable classical re‑grounding must relax at least one of the axioms.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 12 -> 8. length 4794 -> 3079 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix B. Claim attribution. references 8 -> 9. length 3115 -> 3593 words.
- Version 2.2.0 (2026-10-21, from 2.1.0): revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples; Appendix A. Divergence. sections folded or removed: Appendix A. Divergence report. references 9 -> 9. length 3661 -> 4099 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 14 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[2] Distributing Multipartite Entanglement over Noisy Quantum Networks. arXiv:2103.14759v3. https://arxiv.org/abs/2103.14759v3
[3] Entanglement, the quantum formalism and the classical world. arXiv:1110.0157v1. https://arxiv.org/abs/1110.0157v1
[5] Coherent states and the classical-quantum limit considered from the point of view of entanglement. arXiv:1206.5715v2. https://arxiv.org/abs/1206.5715v2
[6] Hierarchical Quantum Network using Hybrid Entanglement. arXiv:2004.13176v3. https://arxiv.org/abs/2004.13176v3
[8] A Unified Combination of Classical and Quantum Systems. arXiv:2010.03984v2. https://arxiv.org/abs/2010.03984v2
[9] https://papers.qnfo.org/papers/re-deriving-quantum-entanglement-from-classical-radon-nikod-m-hydrodynamics-a-fo. QNFO: Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis.
[10] https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis. QNFO: Hydrodynamic Stability Hypothesis.
[11] https://papers.qnfo.org/papers/post-quantum-synthesis. QNFO: POST QUANTUM SYNTHESIS.
[12] https://papers.qnfo.org/papers/pqs-ai-evaluation-audit. QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis.

## Appendix A. Divergence

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2111.08018v2 | Entanglement dynamics in hybrid quantum circuits
arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks
arXiv:1110.0157v1 | Entanglement, the quantum formalism and the classical world
arXiv:2107.11259v1 | Probing tripartite entanglement and coherence dynamics in pure and mixed independent classical environments
arXiv:1206.5715v2 | Coherent states and the classical-quantum limit considered from the point of view of entanglement
arXiv:2004.13176v3 | Hierarchical Quantum Network using Hybrid Entanglement
arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations
arXiv:2010.03984v2 | A Unified Combination of Classical and Quantum Systems

## QNFO corpus context (Vectorize)

QNFO: Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/re-deriving-quantum-entanglement-from-classical-radon-nikod-m-hydrodynamics-a-fo
QNFO: Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis
QNFO: POST QUANTUM SYNTHESIS | https://papers.qnfo.org/papers/post-quantum-synthesis
QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis | https://papers.qnfo.org/papers/pqs-ai-evaluation-audit

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2111.08018v2 | Entanglement dynamics in hybrid quantum circuits
  The central philosophy of statistical mechanics (stat-mech) and random-matrix theory of complex systems is that while individual instances are essentially intractable to simulate, the statistical properties of random ensembles obey simple universal "laws". This same philosophy promises powerful methods for studying the dynamics of quantum information in ideal and noisy quantum circuits -- for whic
  Full text (https://arxiv.org/html/2111.08018v2), excerpts of its own sections:
  § I Introduction: While many-body physics has traditionally focused on the properties of cold-matter in equilibrium, emerging atomic, molecular, optical, and qubit platforms allow access to far from equilibrium dynamics with local space and time control over interactions. A key challenge is to identify universal features of non-equilibrium quantum dynamics and approach to thermalization. The dynamics of the scrambling of local quantum information into non-local degrees of freedom by many-body unitary dynamics plays a central role in addressing those questions. [...]
  § III.2.3 Experimental observation of MIPT in trapped-ions: Using a standard methods of measuring the reference qubit entanglement entropy (e.g. using tomography to determine its density matrix) would still require many copies of a given trajectory which would incur a much larger post-selection overhead. However, Refs.  [ 30 , 77 ] highlight a method to potentially avoid post-selection. In the purifying phase, the measurements collapse the reference ancilla into a pure state disentangled from the system. This pure state may be in a random basis determined by various measurement outcomes, so that further measurements of the ancilla in a fixed (e.g. computational) basis would generally see a large-entropy mixture of $0$ and $1$ outcomes. However, if this basis can be determined using the knowledge extracted from the measurement outcomes in the circuit, then one could observe the purity of the entangled state without preparing multiple copies of the same trajectory. [...]
  § IV.3 Boundary conditions and domain wall free energy: By imposing different boundary conditions corresponding to fixing permutations at the boundary, the statistical mechanics model results in different partition functions $\begin{split}Z_{A}&=\mathbb{E}_{U,\bf{m}}{\rm tr}\left[{\cal S}^{\otimes k}_{A,n}\rho_{{\mathbf{m}}}^{\otimes Q}\right],\\ Z_{0}&=\mathbb{E}_{U,\bf{m}}{\rm tr}\left[\rho_{\mathbf{m}}^{\otimes Q}\right],\end{split}$ (32) from which the averaged $n$ th Rényi entropy $\overline{S^{(n)}_{A}}$ can be obtained in the replica limit via $\overline{S^{(n)}_{A}}=\frac{n}{1-n}\lim_{Q\to 1}\frac{Z_{A}-Z_{0}}{Q-1}.$ (33) Using the fact that $Z_{A}=Z_{0}=1$ in the replica limit $k\to 0$ ( $Q\to 1$ ), this can be rewritten in a more intuitive form as the free energy cost of the domain-wall associated with changing the boundary condition in the entanglement region: $\overline{S^{(n)}_{A}}=\lim_{k\to 0}\frac{F_{A}-F_{0}}{k(n-1)},$ (34) with $F_{A}=-\log Z_{A}$ and $F_{0}=-\log Z_{0}$ . [...]
  § VI Discussion: The examples reviewed above highlight the promise for using well-developed statistical mechanics tools to investigate universal aspects of emerging quantum dynamics and quantum information theory concepts, and to uncover new regimes of measurement-induced non-equilibrium orders. Despite rapid progress, several open challenges remain. The statistical mechanics model mapping of MRC dynamics onto a classical spin model establishes the existence of these transitions through convergence of strong- and weak- coupling expansions, establishes an equivalence between the entanglement- and purification- transition perspectives, and strongly suggests that the $1+1d$ entanglement transition is described by a (non-unitary) conformal field theory (CFT). However, a detailed analytic understanding of the precise universality class and CFT content remains unsolved (though these questions are being explored numerically  [ 36 , 42 , 62 ] ). [...]
[2] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks
  A quantum internet aims at harnessing networked quantum technologies, namely by distributing bipartite entanglement between distant nodes. However, multipartite entanglement between the nodes may empower the quantum internet for additional or better applications for communications, sensing, and computation. In this work, we present an algorithm for generating multipartite entanglement between diff
  Full text (https://arxiv.org/html/2103.14759v3), excerpts of its own sections:
  § 1 Introduction: Quantum technologies hold the promise of faster computing, securer private communications [ 1 , 2 , 3 ] , and more precise sensing and metrology [ 4 , 5 ] . Quantum networks open the possibility to explore these applications in distributed scenarios, allowing for increased performance and/or tasks involving multiple parties. In fact, quantum networks where the links correspond to quantum entanglement between the nodes, can be thought over long distances, e.g. inter-city, such as in the case of a quantum Internet [ 6 , 7 ] , or locally, e.g. inside a laboratory or a quantum local-area network (QLAN) [ 8 ] . The immediate question that arises on a quantum network is how to optimally generate bipartite entanglement between two user-nodes, as a function of the relevant metrics (fidelity, rate,…). This encompasses selecting the appropriate protocols for entanglement generation and entanglement swapping [ 9 ] , and algorithms that find the optimal way to execute them over a quantum network [ 10 , 11 , 12 , 13 , 14 , 15 , 16 ] . [...]
  § 2 Quantum Network Description: Let us first describe our model of a quantum network. Structurally, it is characterised by a graph $G(V,E)$ where each node is denoted by a letter $j\in V$ and the link connecting nodes $i$ and $j$ is denoted by $i:j\in E$ . Each path is a sequence of links and we identify them by their initial and final node $m:n$ . Note that even though we only use the first and last node to represent a path, it is just a matter of notation, as paths are concatenations of contiguous links, and there usually exist different paths between any two nodes. The set of nodes $\mathscr{T}\subset V$ we want to distribute the state to is called the terminal set, where $|\mathscr{T}|=T$ is the number of terminal nodes, or equivalently, the number of qubits of the distributed state. Each link is a noisy quantum channel, accompanied by a classical channel for signaling success and sending corrections, connecting neighboring nodes which individually hold qubits in imperfect quantum memories . [...]
  § 3 Distribution of Entanglement: Distributing entanglement is the building block for an entanglement-based quantum network. There are various schemes for doing such, whether be it in a bipartite scenario, between two parties, usually in the form of a Bell pair, or in the multipartite case, whereas there are more than two parties and multiple possible states, not all equivalent nor with identical applications. [...]
  § 5 Conclusions: With this work, we provided a methodology and an algorithm capable of optimizing multipartite entanglement distribution over noisy quantum networks. To achieve this, we calculated the necessary metrics: (i) the fidelity of the final state, depending on the noise and decoherence of the quantum memories, and (ii) the rate of distribution, which depends on the communication time required and the stochastic behavior of the processes involved. Our methodology can be used to optimize additional parameters, as long as the metrics verify the properties of monotonicity, isotonicity and label-isotonicity. When extending to higher numbers of qubits, under a star-scheme, our algorithm is still optimal if we allow the links to be used more than once. Furthermore, by separating our approach into two equivalent layers, described by distinct algebras for routing and for trees, we allow bipartite entanglement distribution to be different from multipartite schemes. [...]
[3] arXiv:1110.0157v1 | Entanglement, the quantum formalism and the classical world
  75 years after the term "entanglement" was coined to a peculiar feature inherent to quantum systems, the connection between quantum and classical mechanics remains an open problem. Drawing on recent results obtained in semiclassical systems, we discuss here the fate of entanglement in a closed system as Planck's constant becomes vanishingly small. In that case the generation of entanglement in a q
  Full text (https://arxiv.org/html/1110.0157v1), excerpts of its own sections:
  § I Introduction: Schrödinger coined the term ” entanglement ” in 1935 [ 1 , 2 ] to describe the fact that when two systems interacted, the resulting state could ” no longer be described in the same way as before, viz. by endowing each of them with a representative [ie vector state in Hilbert space] of its own . […] By the interaction the two representatives have become entangled ” [ 2 ] . And he added in the same first paragraph of Ref. [ 2 ] the now celebrated phrase: ” I would not call that one but rather the characteristic trait of quantum mechanics, the one that enforces its entire departure from classical lines of thought ”. And indeed, there is a-priori nothing like entanglement in classical mechanics. Our aim in the present note is to give some results on the properties of entanglement as the classical limit is approached and make a few remarks on the fate of entanglement in the classical world. The understanding of entanglement has made some progress since 1935, in particular these last 20 years with the advent of quantum information related works. [...]
  § II Entanglement in semiclassical systems: Assume two particles, each endowed with its own dynamics obtained from a single particle Hamiltonian $H_{i}$ with $i=1,2$ become coupled at some time $t=0$ via an inter-particle potential term $V_{12}.$ Classically, the equations of motion are obtained from the total Hamiltonian $H=H_{1}+H_{2}+V_{12}.$ (1) The individual particle trajectories are coupled by the $V_{12}$ term, and if one resorts to a statistical description, the typical distributions that can be defined for the entire system are given by summing correlated single particle distributions. Moving to the quantum case, assume each single particle system described by (the now quantized) $H_{i}$ is in the semiclassical regime, ie the wavefunction propagates along the classical trajectories of the classical single particle Hamiltonian; as a result the dynamical and statistical properties of the quantum system can be obtained from the properties of the classical trajectories, in particular from the classical periodic orbits (see Refs. [ 3 , 4 ] and Sec. 3 of [ 5 ] for a short exposition). [...]
  § III.1 Entanglement and classical distributions: From the example shown in Fig. 1, it can be remarked that regular or chaotic dynamics in the classical system lead to a comparable entanglement rate. Generically however, it is true that chaos tends to translate into more entanglement in arbitrary situations. It is nevertheless difficult to make universal statements: since there is no classical quantity corresponding to entanglement, it is not possible to compute a well-defined classical version of Eq. ( 4 ). Moreover for typical systems that have been investigated numerically, $\hslash$ is still far from being negligible (relative to the actions of the systems), since one must keep in mind that the size of the Hilbert space (and hence of the quantum computations) increase with the actions and the computations become therefore untractable. Except maybe in a weak coupling regime, where exact semiclassical expansions can be obtained analytically it is hardly possible in definite systems to explain the behaviour of entanglement in terms of the dynamics of classical distributions. [...]
  § III.2 Scaling system: In a classical system the action $S$ is the quantity having the dimension of $\hslash$ . In the semiclassical approximation the quantum wavefunctions take the generic form $\psi\thicksim\sum_{t}\left|\det\frac{-\partial^{2}S(\mathbf{q}_{t})}{\partial q^{i}\partial [...]
[4] arXiv:2107.11259v1 | Probing tripartite entanglement and coherence dynamics in pure and mixed independent classical environments
  Quantum information processing exploits non-local functionality that has led to significant breakthroughs in the successful deployment of quantum mechanical protocols. In this regard, we address the dynamics of entanglement and coherence for three non-interacting qubits initially prepared as maximally entangled GHZ-like state coupled with independent classical environments. Two different Gaussian 
  Full text (https://arxiv.org/html/2107.11259v1), excerpts of its own sections:
  § I Introduction: Information processing and computing based on quantum mechanics are the focus of Quantum information processing [ 1 , 2 , 3 ] . Quantum computers are not restricted to two states, unlike current digital computers, which encode data in binary digits. Quantum bits, or qubits, are used to encode information and can exist in various types of superposition states. To act as computer memory and processors, qubits can be created using atoms, ions, photons, or electrons, as well as control devices [ 4 ] . These computers offer a significant advantage over classical computers, as they can simultaneously hold multiple states. This empowers currently available algorithms, such as integer factorization or quantum many-body system simulation, to solve certain problems much faster than a classical computer [ 5 , 6 , 7 ] . As a result, quantum computers have emerged as forefront advanced devices that are much superior in operation and most certain in practical applications with high speed and accuracy to their classical equivalents [ 8 , 9 , 10 ] . [...]
  § II Tripartite entanglement and coherence measures: This section describes the quantifiers used to evaluate tripartite entanglement, decoherence.
  § II.1 Entanglement witness: Entanglement witnesses, which are Hermitian operators with at least one negative eigenvalue, facilitate experimental detection of entanglement [ 77 , 78 , 79 ] . Entanglement witnesses exist as a result of functional analysis’s Hahn-Banach theorem, which provides a necessary and sufficient condition for detecting entanglement [ 80 ] . Mathematically, entanglement through this operation is computed as [ 81 ] : $E(t)=-Tr[\mathbb{W}_{o}\rho_{abc}(t)],$ (1) where $\mathbb{W}_{o}=\frac{1}{2}\textit{I}-\rho_{o}$ with $\rho_{o}$ being the initial density matrix defined as $\rho_{o}=|\psi\rangle\langle\psi|$ and $\rho_{abc}(t)$ is the time evolved density matrix of the state $\psi$ . For $E(t)=0$ , the state will be separable. Negative results of the Eq.( 1 ) for tripartite states suggest a high entanglement regime, but positive results may show both separability and a weak entanglement regime. [...]
  § IV Results and discussions: In this section, the analytical and numerical results obtained for the entanglement witness, purity, and decoherence measures for the dynamics of the three non-interacting qubits when coupled independently to external random fields generating pure and mixed classical noises are presented.
  § V Conclusion: The dynamics of tripartite entanglement and coherence for a system of three non-interacting qubits prepared as maximally entangled GHZ-like state coupled with independent classical environments are examined in a brief description. The external fields are considered being characterized by four different noisy models: pure power-law, pure fractional Gaussian, power-law noise maximized, and fractional Gaussian noise maximized configurations. We computed the final density matrices for the three qubits by taking ensemble averages over the stochastic process in both the pure and mixed independent environmental noisy configurations. Finally, using estimators such as entanglement witness, purity, and decoherence, we probed the dynamics and preservation of entanglement and coherence in three qubits. Our results show that the dephasing effects on the dynamics of tripartite non-local correlation and coherence are fundamentally different in pure and mixed noisy configurations. The PL noise was more damaging in the mixed noisy condition than in the pure noisy case. [...]
[5] arXiv:1206.5715v2 | Coherent states and the classical-quantum limit considered from the point of view of entanglement
  Three paradigms commonly used in classical, pre-quantum physics to describe particles (that is: the material point, the test-particle and the diluted particle (droplet model)) can be identified as limit-cases of a quantum regime in which pairs of particles interact without getting entangled with each other. This entanglement-free regime also provides a simplified model of what is called in the dec
  Full text (https://arxiv.org/html/1206.5715v2), excerpts of its own sections:
  § 1 Introduction.: In order to solve the so-called Quantum Measurement Problem [ 1 ] , Zurek and coworkers developped in the framework of the decoherence approach [ 2 , 3 , 4 , 5 ] the idea that, maybe, the classical world emerges from a quantum substrate through an evolutionary process. Zurek proposed an explicit selection process the Environment Induced Selection Rule according to which the islands of stability would correspond to the maximal quantum (Shannon-von Neumann) information [ 6 , 7 , 8 ] . This approach was baptised “Quantum Darwinism” [ 9 ] . In section  2 , we illustrate this idea in a simple case, the two-body problem in quantum mechanics, and we show that indeed the classical limit of this problem (that corresponds in the framework of the Quantum Darwinist approach to an entanglement free interaction process [ 14 ] ) is in one to one correspondence with the traditional classical paradigms (point particles, test particle, and diluted particles). [...]
  § 2.1 Quantum Darwinism and Environment Induced selection rule.: Quantum mechanics is astonishingly adequate if we want to describe the material world which we live in. Nevertheless, it is still an open question to know precisely where the border between the microscopic, quantum world and the macroscopic, classical world is situated. In order to tackle such questions, several conceptual tools have been developed during the three last decades. One of them is the decoherence approach, which provides a general framework aimed at explaining how classicality emerges from a quantum substrate [ 2 , 3 , 4 , 5 ] . As a fine structure in this approach, one distinguishes Quantum Darwinism [ 9 ] , an approach which implies that during evolution, a selective process isolated in the external, supposedly quantum world, the islands of stability that correspond to the maximal quantum (Shannon-von Neumann) information. This mechanism has been baptised environment induced (EIN) superselection rule [ 6 , 7 , 8 ] . A key feature of these arguments is the so-called quantum entanglement. [...]
  § 2.2 Entanglement.: The term entanglement was first introduced by Schrödinger who described it as the characteristic trait of quantum mechanics, “the one that enforces its entire departure from classical lines of thought” [ 18 ] . Bell’s inequalities [ 19 , 20 , 21 ] show that when two systems are prepared in an entangled state, the knowledge of the whole cannot be reduced to the knowledge of the parts, and that to some extent the systems lose their individuality. It is only when systems are not entangled that they behave as separable systems. [...]
  § 5 Conclusions.: In this paper, we collected a series of results that appeared in several publications [ 14 , 15 , 16 ] , and discussed the evolution of coherent states. The key idea underlying our analysis is that, in accordance with the quantum Darwinist approach, a principle of maximal information could explain how the classical world emerges from a quantum substrate. In the case of two interacting particles, in a non-relativistic, first quantised treatment, à la Schrödinger, the EIN principle allows us to identify three classical paradigms: the diluted particle or droplet model, and its two extreme limit cases, the test particle regime and the material points regime. In particular, the idea to associate classical pointer states to the states that maximise Shannon-von Neumann entropy sheds a new light on the concept of coherent states. As we have shown in the section 3 , under very general conditions, coherent states are classical pointer states. [...]
[6] arXiv:2004.13176v3 | Hierarchical Quantum Network using Hybrid Entanglement
  The advent of a new kind of entangled state known as hybrid entangled state, i.e., entanglement between different degrees of freedom, makes it possible to perform various quantum computational and communication tasks with lesser amount of resources. Here, we aim to exploit the advantage of these entangled states in communication over quantum networks. Unfortunately, the entanglement shared over th
  Full text (https://arxiv.org/html/2004.13176v3), excerpts of its own sections:
  § 1 Introduction: Quantum entanglement is an irreplaceable quantum resource that plays a very significant role in the field of quantum information processing [ 1 ] . It is an essential element for various applications in the fields of quantum computation [ 2 ] and communication [ 1 ] , such as quantum teleportation [ 3 ] , dense coding [ 4 ] , quantum key distribution [ 5 ] , quantum key agreement [ 6 , 7 ] , quantum secret sharing [ 8 ] , quantum secure direct communication [ 9 , 10 ] . In the recent times, communication over quantum networks and internet is of primary interest [ 11 , 12 , 13 ] , which often uses entanglement and teleportation. Interestingly, quantum entanglement is not sufficient for most of these applications, but maximal quantum entanglement is necessary. For example, quantum teleportation [ 3 ] and its variants [ 14 ] (and references therein) essentially require maximally entangled state (MES) to achieve the unit success probability for deterministic communication. [...]
  § 2 Omega-type hybrid entangled state: An Omega-type hybrid MES can be written as $\begin{array}[]{ccc}\left|\Omega\right\rangle_{abcd}&=&\frac{1}{2}\left(\left|0_{L}\right\rangle\left|0_{L}\right\rangle\left|0_{L}\right\rangle\left|0_{L}\right\rangle+\left|0_{L}\right\rangle\left|1_{L}\right\rangle\left|1_{L}\right\rangle\left|0_{L}\right\rangle+\left|1_{L}\right\rangle\left|0_{L}\right\rangle\left|0_{L}\right\rangle\left|1_{L}\right\rangle-\left|1_{L}\right\rangle\left|1_{L}\right\rangle\left|1_{L}\right\rangle\left|1_{L}\right\rangle\right),\end{array}$ (1) where an optical logical hybrid qubit $\left|0_{L}\right\rangle$ and $\left|1_{L}\right\rangle$ is defined in basis $\left\{\left|0_{L}\right\rangle=\left|+\right\rangle\left|\alpha\right\rangle,\left|1_{L}\right\rangle=\left|-\right\rangle\left|-\alpha\right\rangle\right\}$ with single qubit polarization states $\left|\pm\right\rangle=\frac{\left(\left|H\right\rangle\pm\left|V\right\rangle\right)}{\sqrt{2}}$ and coherent states $\left|\pm\alpha\right\rangle$ . [...]
  § 3 Entanglement concentration protocol for Omega-type hybrid entangled state: To begin with, first we propose an entanglement concentration for Omega-type HES using a single- and a two-mode superpositions of coherent states. To obtain a MES of hybrid Omega-type, we assume that Alice, Bob, Charlie, and Diana share the hybrid Omega-type non-MES as described in Eq. ( 3 ). The optical circuit of ECP for Omega-type HES is shown in Fig. 1 . [...]
  § 6 Conclusion: As emphasized in the introduction, the success of a quantum communication or computation task, and quantum technology in general, MES is an essential quantum resource. First of all, it is difficult to distribute a MES between distant parties and even if we succeed in achieving that, it would be hard to maintain entanglement for a longer period of time. Thus, a MES would be transformed into a non-MES due to its interaction with the surroundings before its application. Therefore, it becomes necessary to extract the MES from the non-MESs using an ECP before performing an application using such quantum resources. Essentially, ECPs/EPPs are the initial steps for performing entangled state based long-distance quantum communication and secure computation. Here, we have chosen a hybrid Omega-type MES inspired by the possibility of its application in quantum communication over network. For the sake of completeness of the present work and to achieve the unit success probability, first we have proposed ECP of the HES using a single- and two-mode superposition of coherent states. [...]
[7] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations
  The problem of Phase Estimation (or Amplitude Estimation) admits a quadratic quantum speedup. Wang, Higgott and Brierley [2019, Phys. Rev. Lett. 122 140504] have shown that there is a continuous trade-off between quantum speedup and circuit depth (by defining a family of algorithms known as $α$-QPE). In this work, we show that the scaling of $α$-QPE can be naturally and succinctly derived within t
  Full text (https://arxiv.org/html/2207.14810v3), excerpts of its own sections:
  § I Introduction: With the developments in practical implementations of quantum computers, and with fault-tolerant computation still apparently beyond reach in the near future, much attention has been focused on classical-quantum (hybrid) algorithms: those that can leverage a limited amount of quantum coherence, while out-performing completely classical algorithms [ 1 , 2 , 3 , 4 ] . That such hybrid algorithms exist for any given problem, and for any coherence time constraint, is not obvious. Explicitly showing the existence of a continuous trade-off between classical and quantum resources provides much insight on the role of the two types of resources in the algorithm, and how to off-load work from one to the other. Of course, the formulation of hybrid algorithms gives also the practical advantage of being able to adapt to the available quantum resources, such that, even when these are limited, a speed-up can be achieved. One particular problem for which hybrid algorithms have been thoroughly studied is that of Phase Estimation. [...]
  § II Preliminaries: Figure 2: For a fixed $\delta$ (here, $\delta=0.2$ ), polynomials of increasing degree allow for a better approximation to the step function (equivalently, with a smaller $\eta$ ). While this decreases the necessary number of samples, the implementation of polynomials of higher degrees in the Quantum Singular Value Transformation framework requires longer coherent computation. A theorem of [ 22 ] ensures the existence of a suitable polynomial for a given choice of $\delta,\eta$ (cf. lemma 4 ); here we used the pyqsp [ 20 , 23 , 24 ] package to explicitly generate such polynomials.
  § II.1 Computational model: The analysis of $\alpha$ -QPE is naturally set in a hybrid computing model [ 1 , 4 ] . A hybrid classical-quantum algorithm is one that performs multiple runs of limited-depth quantum circuits, possibly interchangeably with some classical processing of the measurement outcomes. The problems that we are concerned with here are defined in an oracular setting. That is, they are specified in terms of access to some given operators that encode the relevant information. Thus, our complexity measures are based on the number of oracle calls (or queries ). The depth complexity of the algorithm, $D$ , is the maximum depth among all the employed quantum circuits. The time complexity, $T$ , is the total running time, that is, the sum of all the depths or, equivalently, the total number of queries. [...]
  § IV Discussion: We have shown that the scaling of $\alpha$ -QPE can be naturally derived from the framework of Quantum Singular Value Transformation (at least, up to polylogarithmic factors in the number of samples). QSVT approaches Phase Estimation by block-encoding an approximation to the sign function (which is here adapted into a step function). Our main contribution was to note that we can trade-off the quality of this approximation by longer statistical sampling. That is, we can compensate the use of lower degree polynomials (meaning lower circuit depths) by running the quantum circuits more times. Our derivation provides a new interpretation of the parameter $\alpha$ on $\alpha$ -QPE. Recalling that we approximate the step function up to error $\eta/2$ outside the interval $[-\delta,\delta]$ , the approximation parameters $\eta,\delta$ and the interpolating parameter $\alpha$ are related as $\eta+\frac{1}{2}\delta^{\alpha}=1$ . So, $\alpha$ translates how the two approximation parameters are related, parametrizing a family of approximations to the step function. [...]
[8] arXiv:2010.03984v2 | A Unified Combination of Classical and Quantum Systems
  Any particular classical system and its quantum version are normally viewed as separate formulations that are strictly distinct. Our goal is to overcome the two separate languages and create a smooth and common procedure that provides a clear and continuous passage between the conventional distinction of either a strictly classical or a strictly quantized state. While path integration, among other
  Full text (https://arxiv.org/html/2010.03984v2), excerpts of its own sections:
  § 1.1 Classical formulations: We start by describing phase space as a set of momenta ( $p$ ) and coordinates ( $q$ ), which have a measure ( $dp\,dq$ ). Dynamical equations are time ( $t$ ) dependent ( $p(t)$ ) and ( $q(t)$ ), which are dictated by stationary variations of a classical ( $c$ ) action functional $\displaystyle A_{c}={\textstyle\int}_{0}^{T}\{p(t)\,\dot{q}(t)-H(p(t),q(t))\,\}\;dt\;,$ (1) that leads, with $\dot{q}(t)\equiv d\,q(t)/dt$ , to $\displaystyle\delta A_{c}={\textstyle\int}_{0}^{T}\{[\dot{q}(t)-\partial H(p(t),q(t)/\partial p(t)]\,\delta p(t)$ $\displaystyle\hskip 50.00008pt-[\dot{p}(t)+\partial H(p(t),q(t))/\partial q(t)]\,\delta q(t)\}\;dt$ $\displaystyle\hskip 70.0001pt+q(t)\,\delta p(t)|_{0}^{T}-p(t)\,\delta q(t)|_{0}^{T}=0\;,$ (2) with arbitrary $\delta p(t)$ and $\delta q(t)$ values, except that $\delta p(T)=\delta p(0)=0$ and $\delta q(T)=\delta q(0)=0$ . [...]
  § 1.2 Quantum formulations: The basic quantum operators are linked with suitably chosen classical variables, i.e., $p\rightarrow P$ and $q\rightarrow Q$ , which satisfy the rule $QP-PQ\equiv[Q,P]=i\hbar 1\!\!1$ . Note: The rules used to choose the favored classical variables, $p$ and $q$ , that are promoted to operators, $P$ and $Q$ , are addressed below. Various operators, such as ${\cal{W}}(P,Q)$ , act upon suitable Hilbert space vectors, such as $|\Phi\rangle$ leading to new Hilbert space vectors, ${\cal{W}}(P,Q)|\Phi\rangle$ . It is conventionally observed that the operator $Q$ is diagonalized when acting on selected eigenvectors. This leads to the relations that $Q|x\rangle=x|x\rangle$ while then $P|x\rangle=-i\hbar(\partial/\partial x)\,|x\rangle$ . A general Hilbert space vector $|\Phi\rangle$ then becomes $\Phi(x)=\langle x|\Phi\rangle$ , and the normalization of a general vector is $\langle\Phi|\Phi\rangle={\textstyle\int}|\Phi(x)|^{2}\;dx The algebra of quantum operators, such as the self-adjoint Hamiltonian operator ${\cal H}(P,Q)$ , act upon vectors from a suitable Hilbert space. [...]
  § 2.1 Choosing the correct quantum operators: Since classical mechanics has a long history, it is natural that the classical variables are chosen before choosing what quantum operators to employ. That behavior has its natural difficulties because while there are many acceptable classical variables $p$ and $q$ , or $\overline{p}$ and $\overline{q}$ , etc., provided the Hamiltonian function also is changed so that $\overline{p}=\overline{p}(p,q)$ and $\overline{q}=\overline{q}(p,q)$ , along with the Poisson brackets $\{p,q\}=\{\overline{p},\overline{q}\}=1$ , which leads to $\overline{H}(\overline{p},\overline{q})=H(p,q)$ for all variables. On the other hand, a promotion of classical variables to quantum operators, such as $p\rightarrow P$ and $q\rightarrow Q$ , but generally , $\overline{H}(\overline{P},\overline{Q})\neq H(P,Q)$ , and when the Hamiltonian operators are different, they definitely can lead to different physics. It is absolutely necessary to find a procedure whereby favored classical variables are the ones that are promoted to the correct quantum operators . [...]
  § 2.2 The quantum action functional restricted to coherent states: In ( 4 ) we have outlined the quantum action functional. Its stationary variations lead to the Schrödinger equation in its abstract form. This equation is a fundamental relation in the quantum story. However, as classical observers, we are not able to vary all quantum vectors, but rather to a subset of vectors such as our family of coherent states. [...]
[9] QNFO: Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/re-deriving-quantum-entanglement-from-classical-radon-nikod-m-hydrodynamics-a-fo
  The Hydrodynamic Stability Hypothesis (HSH) claims that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction under a locally bounded hydrodynamic flow. The specific gap is the absence of an explic
  Full text (https://papers.qnfo.org/papers/re-deriving-quantum-entanglement-from-classical-radon-nikod-m-hydrodynamics-a-fo), excerpts of its own sections:
  § 1. Introduction: Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. [...]
  § 5. Results: All quantitative statements below follow directly from the arithmetic in Section 4. 1. **Quantum GHZ correlations** (Section 4.1): \(\langle XXX\rangle_{Q}=+1\); \(\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1\). 2. **Classical pointwise constraint** (Section 4.2): \(P_{1}P_{2}P_{3}P_{4}=+1\) pointwise (consequence of A2 alone); with A4 this yields \(\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1\), conflicting with the quantum product \(-1\). 3. **Mermin bound** (Section 4.3): classical \(M_{\mathrm{LHV}}=2\); quantum \(M_{\mathrm{Q}}=4\); violation factor \(2\). 4. **CHSH bound** (Section 4.4): classical bound \(2\); quantum maximum \(2\sqrt{2}\approx2.828427\); violation factor \(\sqrt{2}\approx1.414214\). 5. **Falsification verdict** (Section 4.5): the conjunction of A1–A4 is incompatible with the GHZ stabilizer statistics; the fork of consistent relaxations has four branches (relax A2, relax A4, relax A1, or retain all and accept empirical refutation). 6. [...]
  § 7. Discussion: **Scope of the falsification.** The derivation shows that the strong claim of HSH—local classical measure theory reproducing GHZ‑type Bell‑violating correlations—is untenable as a conjunction. It does not identify a unique axiom that must be abandoned, and it does not address weaker versions that relax A2, reinterpret locality at the level of the flow \(\Phi_{t}\), or restrict the claim to states and measurements outside the GHZ stabilizer set. **Potential escapes.** 1. The formalization A1–A4 is our own interpretation; [10] does not publish a numbered axiom list, so an alternative formalization might locate the failure elsewhere. Any such formalization must still reproduce the four stabilizer values, and the counting argument of Section 4.2 applies to any model with local binary response functions and a setting‑independent hidden‑variable distribution. 2. Stochastic response functions do not escape: the identity \(P_{1}P_{2}P_{3}P_{4}=+1\) holds pointwise for every assignment of the six local outcomes, so averaging over any distribution preserves it. 3. [...]
  § 9. Conclusion: By formalizing the Hydrodynamic Stability Hypothesis as four minimal axioms and deriving the algebraic pointwise product constraint \(P_{1}P_{2}P_{3}P_{4}=+1\), we have shown that the hypothesis cannot simultaneously satisfy locality, measurement‑setting freedom, and reproduce the GHZ stabilizer statistics of quantum mechanics. The resulting Mermin and CHSH violations quantify the gap between the classical bound and quantum predictions. Projection of the required simulation timescales clarifies the engineering demands of any particle‑tracking test of the hypothesis. The strong, local‑realist version of HSH is therefore falsified; any viable classical re‑grounding must relax at least one of the axioms.
[10] QNFO: Hydrodynamic Stability Hypothesis | https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis
  This work identifies a “chronological fallacy” at the heart of quantum foundations: the axiomatization of quantum mechanics by von Neumann (1932) predated the rigorous formulation of classical probability by Kolmogorov (1933), creating an artificial schism between physics and statistics. To resolve the “spectral divergence” between the continuous ontology of hydrodynamic quantum models and the dis
  Full text (https://papers.qnfo.org/papers/hydrodynamic-stability-hypothesis), excerpts of its own sections:
  § Re-grounding: Quantum Mechanics in Classical Measure Theory **Author:** Rowan Brad Quni-Gudzinas **Contact:** rowan.quni@outlook.com **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](https://isni.org/isni/0000000526456062) **URL:** https://papers.qnfo.org/papers **Publication Date:** 2025-11-26 **Version:** 1.0 **Abstract**: This work identifies a “chronological fallacy” at the heart of quantum foundations: the axiomatization of quantum mechanics by von Neumann (1932) predated the rigorous formulation of classical probability by Kolmogorov (1933), creating an artificial schism between physics and statistics. To resolve the “spectral divergence” between the continuous ontology of hydrodynamic quantum models and the discrete phenomenology of spectroscopy, the **hydrodynamic stability hypothesis** is proposed. [...]
  § 1.1 The: Chronological Fallacy in Quantum Foundations The prevailing mathematical formalism of quantum mechanics rests upon a historical contingency that has largely escaped critical scrutiny in the intervening century. In 1932, John von Neumann published *Mathematische Grundlagen der Quantenmechanik* (von Neumann, 1932), codifying the theory within the framework of Hilbert space operators and establishing the spectral theorem as the primary tool for extracting physical values. [...]
  § 4.14 Summary of the Hybrid: Model In summary, the continuous-attractor hybrid model unifies the continuous ontology of the Schrödinger equation with the discrete phenomenology of the spectral theorem. It achieves this by introducing dynamical stability as the bridge. The system *is* a continuous fluid (Kolmogorovian/Madelung), but it *appears* discrete (von Neumann) because we only observe it after it has settled into stable resonant modes (attractors) driven by the act of observation. This closes the gap between the two formalisms, proving they are compatible descriptions of different regimes of the same physical reality.
  § 7.2 Summary of Evidence: The argument presented here is supported by converging lines of evidence from mathematical physics, experimental quantum optics, and computational fluid dynamics. The mathematical rigor of the Kolmogorovian reconstruction (Reddiger, 2026) proves that a classical probability space can host quantum phenomena without contradiction. The empirical observation of continuous trajectories between eigenstates in superconducting circuits (Hacohen-Gourgy & Martin, 2020) falsifies the notion of instantaneous collapse. Furthermore, the success of Bohmian trajectories in reproducing complex high-harmonic generation spectra (Wu et al., 2013) demonstrates that the hydrodynamic variables possess explanatory power in regimes where the standard spectral approach struggles. The weight of evidence now favors the continuous hydrodynamic view over the discrete operator view.
  § 7.4 The Proposed Experiment: To move this hypothesis from theoretical plausibility to empirical fact, we issue a specific call to action: experimentalists must perform the weak energy tomography on a hydrogen superposition. This experiment is the crucible that will decide between the spectral dogma and the hydrodynamic stability hypothesis. The prediction of a continuous energy distribution is unambiguous, quantitative, and falsifiable. If the continuous histogram is observed, the orthodox interpretation of the spectral theorem must be abandoned.
[11] QNFO: POST QUANTUM SYNTHESIS | https://papers.qnfo.org/papers/post-quantum-synthesis
  For over a century, physics has been captivated by a perceived intrinsic strangeness of the world, mistaking mathematical models for reality itself. This intellectual entanglement has given rise to persistent paradoxes, including wave-particle duality, wavefunction collapse, spooky action at a distance, and the elusive quantum-classical divide. The Post-Quantum Synthesis (PQS) presents an act of i
  Full text (https://papers.qnfo.org/papers/post-quantum-synthesis), excerpts of its own sections:
  § 7.4.3 Theorem 7.2 (No Physical: Collapse) There is no physical change to the continuous physical state \(\phi \in \mathcal{R}\) corresponding to “wavefunction collapse.” *Proof*: Consider the physical state evolution during a measurement: 1. **Initial physical state**: The system begins in a definite continuous physical state \(\phi_0 \in \mathcal{R}\). 2. **Interaction with detector**: The system’s field interacts with the detector’s fields, evolving continuously according to Hamiltonian dynamics: \(\phi(t) = \Phi_t(\phi_0) \in \mathcal{R}\). 3. **Amplification stage**: The continuous field \(\phi(t)\) triggers a threshold crossing within the detector, leading to a discrete outcome. 4. **Final physical state**: The system evolves to a final continuous physical state \(\phi_1 = \Phi_T(\phi_0) \in \mathcal{R}\). The entire process, from initial interaction to final physical state, is one of continuous Hamiltonian evolution within \(\mathcal{R}\). The “collapse” only affects the density operator \(\rho \in \mathcal{K}\) (the observer’s knowledge), not the physical state \(\phi \in \mathcal{R}\). \(\square\)
  § 7.5.3 Theorem 8.1 (No Spooky: Action) For any local operation performed solely on system \(\mathcal{R}_1\), the physical state of the spatially separated system \(\mathcal{R}_2\) remains unchanged. *Proof*: Let \(U_1\) be a local unitary operator acting only on \(\mathcal{R}_1\). The transformed joint state is: \[\phi_{12}' = (U_1 \otimes I)\phi_{12} = \sum_i c_i (U_1\phi_1^i) \otimes \phi_2^i\] To find the physical state of \(\mathcal{R}_2\), we consider its marginal density operator, obtained by tracing over the degrees of freedom of \(\mathcal{R}_1\): \[\rho_2 = \text{tr}_1(|\phi_{12}'\rangle\langle\phi_{12}'|) = \sum_i |c_i|^2 |\phi_2^i\rangle\langle\phi_2^i|\] This marginal state is identical to the marginal state of \(\mathcal{R}_2\) before \(U_1\) was applied to \(\mathcal{R}_1\). This demonstrates that local operations on one system have no instantaneous physical effect on the other, thus refuting “spooky action at a distance.” \(\square\)
  § 7.5.4 Theorem 8.2 (Correlation: History) The joint measurement statistics for two entangled systems satisfy: \[P(o_1, o_2) = \sum_i |c_i|^2 P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)\] *Proof*: This follows directly from the Born rule applied to the epistemic state and the product structure of the physical states after separation. The correlations arise from the coefficients \(c_i\) established during the initial interaction, which encode the shared history. \(\square\)
  § 7.6.3 Theorem 9.1 (Redundancy: Threshold) There exists a critical number of environmental copies, \(N_0\), such that for any number of copies \(N > N_0\), the outcomes of measurements on the system become objective. *Proof*: By the quantum Chernoff bound, the probability of misidentifying the state of the system, based on an observation of the environment, decreases exponentially with \(N\): \[P_{\text{error}} \leq e^{-N\gamma}\] For some \(\gamma > 0\) that depends on the distinguishability of the environmental states. Thus, for \(N > N_0 = \frac{1}{\gamma}\log\frac{1}{\epsilon}\), the probability of error \(P_{\text{error}}\) becomes less than an arbitrarily small \(\epsilon\). This establishes a clear redundancy threshold for the emergence of objectivity. \(\square\)
  § 7.6.4 Theorem 9.2 (No Size: Dependence) The emergence of objectivity depends solely on the redundancy parameter \(N\) (the number of environmental copies), and not on the physical size or mass of the system itself. [...]
[12] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis | https://papers.qnfo.org/papers/pqs-ai-evaluation-audit
  Archive of the complete research record investigating the Post-Quantum Synthesis (PQS) framework: a neutral investigation of PQS's four sub-pillars mapped against external literature, plus an earlier-iteration analysis of AI gate-check convergence between Claude and Gemini evaluating PQS independently.
  Full text (https://papers.qnfo.org/papers/pqs-ai-evaluation-audit), excerpts of its own sections:
  § 2.1 Wave-Particle Duality and the Double-Slit Experiment: The double-slit experiment stands as the canonical example of quantum paradox, appearing to show that a single entity, such as an electron, is simultaneously a wave and a particle—a direct contradiction in classical terms. The PQS resolves this apparent contradiction by assigning wave-like and particle-like behaviors to their correct, non-contradictory domains, eliminating the duality.
  § 2.1.4 The “Which-Path” Experiment as an Alteration of the Physical System and Epistemic State: The paradox appears to deepen when a detector is placed at one of the slits to determine “which path” the electron took, causing the interference pattern to vanish. The PQS explains this phenomenon as a direct consequence of the physical nature of measurement, which inevitably alters the system. ##### 2.1.4.1 The Necessary Physical Interaction of the Path Detector To gain “which-path” information, the detector must physically interact with the field as it passes through a slit. This constitutes a measurement interaction as defined by Axiom II. This interaction inevitably and physically disturbs the continuous field, fundamentally altering its subsequent evolution toward the screen. ##### 2.1.4.2 The Consequent Update (Collapse) of the Knowledge State and Loss of Interference This physical interaction provides new information to the observer. If the detector at Slit A “clicks,” the observer must perform a Bayesian update on their knowledge state. This update effectively destroys the superposition, and the epistemic state is updated (or “collapses”) to be simply $\psi_A$. [...]
  § 2.4 The Born Rule as a Theorem of Epistemic Consistency: The Born Rule, stating that the probability of an outcome is the squared magnitude of its probability amplitude ($P(o_k) = |\langle o_k|\psi \rangle|^2$), is typically presented as a fundamental postulate of quantum mechanics. Within the PQS, this rule cannot be a postulate about reality; it must be a necessary consequence of the requirements of rational inference.
  § 2.4.2 Derivation from Rational Consistency Conditions via Gleason’s Theorem: The derivation relies on a powerful mathematical result, Gleason’s Theorem (Gleason, 1957), proving that any consistent probability assignment on the structure used to represent quantum knowledge (a Hilbert space) must take the form of the Born Rule. ##### 2.4.2.1 The Requirements of Non-Negativity, Normalization, and Non-Contextuality for a Probability Rule To be a valid probability assignment, any rule must satisfy basic consistency conditions: 1.  **Non-Negativity:** Probabilities must be real and non-negative. $f(\psi, P_k) \in \mathbb{R}_{\ge 0}$. 2.  **Normalization:** For any complete measurement context defined by a set of mutually orthogonal projectors $\{P_k\}$ where $\sum_k P_k = I$, the sum of probabilities for all possible outcomes must be 1. $$ \sum_k f(\psi, P_k) = 1 $$ 3.  **Non-Contextuality of Probabilities:** The probability assigned to an outcome $P_k$ should not depend on the other projectors in the specific orthogonal basis chosen for the measurement. It should only depend on the knowledge state $\psi$ and the projector $P_k$ itself. [...]
  § 4.2 The Problem of Consciousness as External to the Domain of Physics: The “Hard Problem of Consciousness”—why and how subjective experience arises from physical processes—has at times been erroneously linked to quantum mechanics, particularly through the idea that a “conscious observer” is needed to collapse the wavefunction. [...]