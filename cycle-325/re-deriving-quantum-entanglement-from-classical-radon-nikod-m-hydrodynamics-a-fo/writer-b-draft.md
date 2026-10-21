# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis (Version 3.0)

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) proposes that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction of classical probability measures under a locally bounded hydrodynamic transport. The specific gap is the absence of an explicit derivation of GHZ‑type Bell‑violating correlations from the hypothesis's own axioms. We formalize the strong form of HSH as four minimal axioms (classical measure grounding, local hidden variables, locally bounded continuous transport, and free measurement settings) and derive, with full arithmetic, that the axioms force the pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ on the four GHZ triple correlations, whereas quantum mechanics predicts a product of $-1$. The resulting Mermin violation factor is $2$ and the CHSH violation factor is $\sqrt{2}\approx1.414214$. As a labeled projection conditional on stated assumptions ($v_{\max}=c$, barrier width $L=1.0\times10^{-3}\ \mathrm{m}$, timestep at most one‑tenth of the crossing time), a particle‑tracking simulation of the hydrodynamic transport would need timesteps of about $333\ \mathrm{fs}$ to resolve the fastest local signals the hypothesis permits; the requirement scales linearly with $L$ and is not universal. The strong form of HSH is therefore falsified: any classical re‑derivation of GHZ statistics must relax at least one axiom, and the fork of consistent relaxations comprises four distinct branches.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics, and if so which axiom of such a derivation they should expect to give up first. A falsification that identifies the specific axiom(s) under strain converts an open philosophical program into a bounded engineering decision.

This paper is a post‑publication revision of the formal falsification analysis of HSH [9]. It corrects three errors identified in the published version: the fork of axiom relaxations in the earlier Section 4.5 was presented as a binary choice when four branches are logically available; the abstract overstated the timestep projection as a universal requirement of any particle‑tracking simulation, when it holds only under stated assumptions on signal speed, barrier width and resolution convention; and the earlier text attributed the product constraint of Section 4.2 to axioms A2 and A4 jointly, when the pointwise identity follows from A2 alone and A4 enters only when the pointwise identity is promoted to a statement about expectations under a single distribution. All three corrections are incorporated below, and the derivations are restated with full arithmetic.

Our contributions are:
1. Formalization of the strong form of HSH as four minimal axioms (Section 3.1).
2. Derivation of the quantum GHZ stabilizer values and the classical pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ from the axioms, with full arithmetic, including the corrected attribution of the constraint to A2 alone (Sections 4.1–4.2).
3. Quantitative Mermin and CHSH violation analysis, with violation factors $2$ and $\sqrt{2}\approx1.414214$ (Sections 4.3–4.4).
4. A corrected falsification verdict that enumerates the full four‑branch fork of axiom relaxations rather than a binary choice (Section 4.5).
5. A labeled projection of the temporal resolution a particle‑tracking test of the locality claim would need, conditional on stated assumptions and explicitly not universal (Section 4.6).

## 2. Background and Related Work

**Ensemble‑statistical view of quantum dynamics.** Reference [1] develops the philosophy that while individual instances of complex quantum circuits are essentially intractable to simulate, the statistical properties of random ensembles obey simple universal laws, and it maps measurement‑induced phase transitions in random circuits onto classical statistical‑mechanics spin models, deriving averaged Rényi entropies as domain‑wall free energies in a replica limit via $\overline{S^{(n)}_{A}}=\lim_{k\to 0}\frac{F_{A}-F_{0}}{k(n-1)}$. This establishes that classical statistical descriptions of quantum information operate at the ensemble level, which is why the axioms of Section 3.1 are phrased for ensembles of hidden configurations rather than single trajectories.

**Multipartite entanglement as a network resource.** Reference [2] presents an algorithm for generating multipartite entanglement between nodes of a noisy quantum network, computing the fidelity of the final state from memory noise and decoherence and the distribution rate from communication time and process stochasticity, and proving optimality under a star‑scheme when links may be used more than once. Any classical foundation that claims to re‑derive quantum statistics must reproduce exactly these fidelity and rate metrics for quantum‑network applications to function as designed; the GHZ correlations tested in Section 4 are the smallest multipartite instance of that requirement.

**Entanglement and the classical limit.** Reference [3] discusses the fate of entanglement as Planck's constant becomes vanishingly small, showing that in semiclassical systems the quantum wavefunction propagates along classical trajectories and that, since there is no classical quantity corresponding to entanglement, it is not possible to compute a well‑defined classical version of the entanglement rate except in weak‑coupling regimes where exact semiclassical expansions exist. This work frames the precise question HSH answers in the opposite direction: rather than asking how entanglement behaves as the classical limit is approached, HSH claims entanglement statistics can be derived from classical distributions outright, and Section 4 shows the claim fails for GHZ correlations.

**Tripartite entanglement under classical environments.** Reference [4] examines three non‑interacting qubits prepared in a maximally entangled GHZ‑like state coupled to independent classical environments, using an entanglement witness $E(t)=-\mathrm{Tr}[\mathbb{W}_{o}\rho_{abc}(t)]$ and reporting that dephasing of tripartite non‑local correlation differs fundamentally between pure and mixed noisy configurations, with power‑law noise more damaging in the mixed case. This is the closest antecedent to HSH's program in the literature, but it treats the classical environments as external probes that degrade quantum coherence, not as a substrate from which the quantum statistics are derived; the falsification in Section 4 concerns the latter, stronger claim.

**Entanglement‑free classical regimes.** Reference [5] identifies three classical paradigms (material point, test particle, diluted droplet) as limit cases of a quantum regime in which interacting particles do not entangle, connecting them to Quantum Darwinism's environment‑induced superselection principle and showing that, under very general conditions, coherent states are classical pointer states under a maximal‑information rule. This work demonstrates that large portions of classical behaviour can be recovered from quantum descriptions without entanglement; HSH claims the converse derivation, and the GHZ stabilizer algebra shows the converse cannot hold locally.

**Hybrid entanglement as a network resource.** Reference [6] exploits Omega‑type hybrid maximally entangled states, defined on optical logical qubits $|0_{L}\rangle=|+\rangle|\alpha\rangle$ and $|1_{L}\rangle=|-\rangle|-\alpha\rangle$, for communication over quantum networks, and proposes entanglement concentration protocols to extract a maximally entangled state from a degraded non‑maximally entangled one before application. Together with [2], this fixes the resource‑level requirements any re‑derivation program must meet; the stabilizer correlations analyzed here are the algebraic core of such resources.

**Classical–quantum interpolation inside the quantum formalism.** Reference [7] derives the scaling of the $\alpha$‑QPE family of phase‑estimation algorithms within the Quantum Singular Value Transformation framework, trading circuit depth against statistical sampling with the approximation parameters related by $\eta+\frac{1}{2}\delta^{\alpha}=1$. This program interpolates between classical and quantum resources while remaining inside the quantum formalism; HSH's claim is more radical because it reverses the direction of derivation, and Section 4 shows the reversal fails at the level of multipartite correlations.

**Unified classical–quantum formulations.** Reference [8] builds a continuous passage between classical and quantized descriptions through a common action functional, and flags the central obstruction: promoting classical variables to operators is not canonical, since generally $\overline{H}(\overline{P},\overline{Q})\neq H(P,Q)$ under variable change, so a procedure for choosing the correct promotion is absolutely necessary. HSH's Radon–Nikodým grounding faces an analogous promotion problem from measures to quantum states, and the GHZ analysis shows that no local promotion reproduces the stabilizer values.

**The hypothesis under test.** Reference [10] proposes the hydrodynamic stability hypothesis itself: it identifies a "chronological fallacy" in that von Neumann's 1932 axiomatization of quantum mechanics predated Kolmogorov's 1933 formulation of classical probability, introduces a continuous‑attractor hybrid model in which the system is a continuous fluid but appears discrete because it is observed only after settling into stable resonant modes, cites converging evidence including continuous trajectories between eigenstates in superconducting circuits and Bohmian reproduction of high‑harmonic generation spectra, and issues a call for weak energy tomography on a hydrogen superposition as the decisive experiment. The axioms of Section 3.1 formalize the locality and attractor claims of [10]; the falsification targets those claims, not the tomography proposal.

**The neighboring PQS program.** The Post‑Quantum Synthesis framework [11] proves a No‑Spooky‑Action theorem (local operations on one system leave the spatially separated marginal $\rho_2=\sum_i |c_i|^{2}|\phi_2^{i}\rangle\langle\phi_2^{i}|$ unchanged), a No‑Physical‑Collapse theorem (collapse affects only the observer's density operator, not the continuous physical state), a Correlation History theorem expressing joint statistics as $P(o_{1},o_{2})=\sum_{i}|c_{i}|^{2}P_{1}(o_{1}|\phi_{1}^{i})P_{2}(o_{2}|\phi_{2}^{i})$, and a redundancy threshold $N_{0}=\frac{1}{\gamma}\log\frac{1}{\epsilon}$ for objective outcomes. The Correlation History theorem is a convex mixture of factorized local response models, and Section 4.4's CHSH bound applies to any such mixture. An independent audit of PQS [12] documents its derivation of the Born rule from Gleason's theorem under non‑negativity, normalization and non‑contextuality conditions, and its account of which‑path detection as a necessary physical interaction with the field followed by a Bayesian update on the observer's knowledge state; the audit's gate‑check record is the source of the observation that PQS's local factorized structure is subject to the same Bell constraints analyzed here.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms:

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure $\mu_{\psi}\ll\mu$ with Radon–Nikodým derivative $\rho_{\psi}=\frac{d\mu_{\psi}}{d\mu}$, such that all quantum predictions are recoverable as functionals of $\rho_{\psi}$.
- **(A2) Local hidden variables.** For $N$ spatially separated parties, the hidden configuration decomposes as $\lambda=(\lambda_{1},\ldots,\lambda_{N})$ with $\lambda_{i}\in\Lambda_{i}$; each party's outcome is a local function $A_{i}=f_{i}(\lambda_{i},s_{i})$ of its own variable and its own setting $s_{i}$.
- **(A3) Locally bounded continuous transport.** The time evolution $\mu_{t}=(\Phi_{t})_{*}\mu_{0}$ is generated by a local flow $\Phi_{t}$ on $\Lambda$ propagating information at finite speed $v_{\max}$, so that no influence connects spacelike‑separated events. Preparation and measurement correspond to relaxation into basins of attraction $\mathcal{B}_{k}\subset\Lambda$ of stable measures, the observed outcome indexing the basin.
- **(A4) Free settings.** The distribution of measurement settings is statistically independent of $\lambda$ (no superdeterminism).

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality expressed by the No‑Spooky‑Action and Correlation History theorems of [11] (A2), and the rejection of superdeterminism implicit in [10] (A4). The formalization is our own; [10] does not publish a numbered axiom list, so alternative formalizations are discussed in Section 6.

### 3.2 Falsification protocol

Given A1–A4, we test whether the model can reproduce the quantum joint statistics of the GHZ state
$$|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|000\rangle+|111\rangle\bigr)$$
under local Pauli measurements $X$ and $Y$ on each qubit. The protocol is: (i) derive the classical constraint imposed by A1–A4 on the four relevant triple correlations, (ii) compute the quantum values of those correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re‑derive the quantum statistics from the classical axioms. The comparison uses the Mermin inequality as the primary instrument and the CHSH inequality as an independent two‑party cross‑check.

### 3.3 Simulation projection protocol

The hypothesis calls for particle‑tracking of the hydrodynamic transport $\Phi_{t}$ [10]. We compute, as a labeled projection with stated assumptions, the propagation timescales such a simulation must resolve for the locality claim of A3 to be testable rather than vacuous: if the simulation's timestep is coarser than the propagation time across the relevant barrier, a local continuous signal and an instantaneous change are observationally indistinguishable in the simulation, and the test loses its discriminating power. The projection is conditional on the assumed signal speed, barrier width and resolution convention; it is not a universal requirement of every particle‑tracking simulation, and Section 4.6 states the scaling explicitly.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (assumption).** The GHZ state is $|\mathrm{GHZ}\rangle=(|000\rangle+|111\rangle)/\sqrt{2}$.

**Input 2 (assumption).** Pauli operators $X$ and $Y$ have eigenvalues $\pm1$, with actions $X|0\rangle=|1\rangle$, $X|1\rangle=|0\rangle$, $Y|0\rangle=i|1\rangle$, $Y|1\rangle=-i|0\rangle$.

Applying the stabilizer operators:
$$
\begin{aligned}
XXX\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(|111\rangle+|000\rangle\bigr)=+|\mathrm{GHZ}\rangle,\\
XYY\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(X|0\rangle Y|0\rangle Y|0\rangle + X|1\rangle Y|1\rangle Y|1\rangle\bigr)\\
&= \frac{1}{\sqrt{2}}\bigl(|1\rangle\cdot i|1\rangle\cdot i|1\rangle + |0\rangle\cdot(-i|0\rangle)\cdot(-i|0\rangle)\bigr)\\
&= \frac{1}{\sqrt{2}}\bigl(i^{2}|111\rangle + (-i)^{2}|000\rangle\bigr)
= \frac{1}{\sqrt{2}}\bigl(-|111\rangle-|000\rangle\bigr)=-|\mathrm{GHZ}\rangle,
\end{aligned}
$$
and identically for $YXY$ and $YYX$ by symmetry of the state under party permutation. Hence the quantum triple‑product expectations are
$$\langle XXX\rangle_{Q}=+1,\qquad \langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1.$$

The product of the four quantum correlations is
$$(+1)\times(-1)\times(-1)\times(-1)=-1.$$

### 4.2 The classical constraint from the axioms

For each party $i\in\{1,2,3\}$ define local predetermined outcomes $A_{i}^{X},A_{i}^{Y}\in\{-1,+1\}$, which exist by A2. The four triple products are
$$
\begin{aligned}
P_{1}&=A_{1}^{X}A_{2}^{X}A_{3}^{X},\\
P_{2}&=A_{1}^{X}A_{2}^{Y}A_{3}^{Y},\\
P_{3}&=A_{1}^{Y}A_{2}^{X}A_{3}^{Y},\\
P_{4}&=A_{1}^{Y}A_{2}^{Y}A_{3}^{X}.
\end{aligned}
$$

Pointwise multiplication yields
$$
\begin{aligned}
P_{1}P_{2}P_{3}P_{4}
&=(A_{1}^{X})^{2}(A_{1}^{Y})^{2}(A_{2}^{X})^{2}(A_{2}^{Y})^{2}(A_{3}^{X})^{2}(A_{3}^{Y})^{2}\\
&=(+1)^{6}=+1,
\end{aligned}
$$
since each local outcome appears exactly twice and squares to $+1$.

**Corrected attribution.** This pointwise identity is a consequence of A2 alone: it holds for every assignment of the six local outcomes, independently of how those outcomes are distributed and independently of any relation between $\lambda$ and the settings. A4 enters only at the next step. Because A2 assigns each party a single pair $(A_{i}^{X},A_{i}^{Y})$ per hidden configuration regardless of which measurements are actually performed, the four products $P_{1},\ldots,P_{4}$ are simultaneously defined on one probability space, and their product can be taken pointwise before averaging. Taking expectations with respect to the measure $\mu$ (A1) then gives
$$\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1.$$
A4 (setting freedom) is what licenses reading the four experimentally accessible correlations $\langle P_{k}\rangle$ as expectations over one and the same distribution of $\lambda$; without it, the experiments that measure $P_{1}$ and the experiments that measure $P_{2}$ could sample different $\lambda$‑distributions, and the pointwise identity would not transfer to a constraint on the experimentally observed product. The constraint therefore rests on A2 for its pointwise form and on A2 with A4 for its experimental force; the earlier published statement that it "follows from A2 together with A4" as a joint hypothesis is corrected accordingly.

Thus the classical axioms force a product of $+1$, whereas quantum mechanics requires $-1$.

### 4.3 Mermin bound and violation factor

For any model satisfying A1–A4,
$$\bigl|\langle P_{1}\rangle-\langle P_{2}\rangle-\langle P_{3}\rangle-\langle P_{4}\rangle\bigr|\le 2,$$
because pointwise $|P_{1}-P_{2}-P_{3}-P_{4}|=2$ whenever $P_{1}P_{2}P_{3}P_{4}=+1$: with the product fixed at $+1$, either one or three of the four values equal $-1$, and in both cases the signed sum $P_{1}-P_{2}-P_{3}-P_{4}$ takes the value $+2$ or $-2$. The quantum values give
$$\bigl|(+1)-(-1)-(-1)-(-1)\bigr|=|1+1+1+1|=4.$$
Hence the classical bound is $M_{\mathrm{LHV}}=2$, the quantum value is $M_{\mathrm{Q}}=4$, the gap $\Delta M=2$, and the violation factor is
$$\frac{M_{\mathrm{Q}}}{M_{\mathrm{LHV}}}=\frac{4}{2}=2.$$

### 4.4 CHSH cross‑check

For two parties the CHSH combination is
$$S = E(a,b) + E(a,b') + E(a',b) - E(a',b').$$
Classically $|S|\le 2$. Quantum mechanics attains the Tsirelson bound $S_{\max}=2\sqrt{2}$. Using $\sqrt{2}\approx1.414214$:
$$2\sqrt{2}\approx 2\times1.414214 = 2.828427.$$
The violation factor over the classical bound is
$$\frac{2\sqrt{2}}{2}= \sqrt{2}\approx1.414214.$$

This cross‑check applies beyond HSH proper: the Correlation History theorem of [11] expresses joint statistics as a convex mixture $P(o_{1},o_{2})=\sum_{i}|c_{i}|^{2}P_{1}(o_{1}|\phi_{1}^{i})P_{2}(o_{2}|\phi_{2}^{i})$ of factorized local response models, and any such mixture satisfies the CHSH bound $|S|\le2$ by the same pointwise argument, so the two‑party constraint binds PQS's local factorized structure in the same way it binds HSH.

### 4.5 The fork and the falsification verdict

The derivation establishes that the conjunction
$$\text{A1}\;\wedge\;\text{A2}\;\wedge\;\text{A3}\;\wedge\;\text{A4}$$
is incompatible with the GHZ stabilizer statistics. The contradiction with Section 4.1 follows once A1 commits all predictions to functionals of the classical measure, A2 supplies the pointwise product identity, and A4 licenses its promotion to the experimentally observed correlations. The complete fork of consistent relaxations is:

1. **Relax A2 (locality of response functions).** Allow the outcome functions $A_{i}$ to depend on distant settings, thereby abandoning local realism in its response‑function form.
2. **Relax A4 (setting freedom).** Permit correlations between $\lambda$ and the measurement settings (superdeterminism), which HSH explicitly excludes but which would remove the single $\lambda$‑distribution assumption used to promote the pointwise identity to the observed correlations.
3. **Relax A1 (classical probability grounding).** Replace the Kolmogorov measure space with a non‑classical probability structure, abandoning the Radon–Nikodým grounding that defines HSH.
4. **Retain all four axioms and accept contradiction.** Concede that the model cannot reproduce the GHZ stabilizer values, i.e., that it is empirically refuted on these correlations.

Every branch falsifies the strong claim that HSH simultaneously satisfies A1–A4 and reproduces GHZ statistics. The corrected verdict therefore identifies an incompatibility of the conjunction, not a unique culprit axiom, and the choice among branches is a research decision rather than a derivation. The earlier published version presented this fork as "exactly two mutually exclusive options" (abandon A2 or accept contradiction); that presentation was incomplete, because relaxing A1 and relaxing A4 are each logically sufficient to dissolve the contradiction, and the four‑branch enumeration above is the complete fork.

### 4.6 Simulation timescale projection (explicitly labeled projection)

**Assumptions.**
(P1) The transport speed is bounded by $v_{\max}=c=3.0\times10^{8}\ \mathrm{m\,s^{-1}}$.
(P2) The spatial barrier width is $L=1.0\times10^{-3}\ \mathrm{m}$ (laboratory scale, taken as an assumption).
(P3) The simulation timestep must be at most one‑tenth of the propagation time (a resolution convention, not a physical law).

**Derivation.** Minimum propagation time:
$$t_{\min}= \frac{L}{v_{\max}} = \frac{1.0\times10^{-3}}{3.0\times10^{8}} = 3.333333\times10^{-12}\ \mathrm{s}\approx3.33\ \mathrm{ps}.$$
Required timestep:
$$\Delta t \le \frac{t_{\min}}{10}=3.333333\times10^{-13}\ \mathrm{s}\approx333\ \mathrm{fs}.$$
Number of timesteps for one crossing:
$$N_{\mathrm{steps}} = \frac{t_{\min}}{\Delta t}=10.$$

For a macroscopic barrier $L=1.0\ \mathrm{m}$:
$$t_{\min}= \frac{1.0}{3.0\times10^{8}} = 3.333333\times10^{-9}\ \mathrm{s}\approx3.33\ \mathrm{ns},\qquad N_{\mathrm{steps}} = \frac{3.33\times10^{-9}}{3.33\times10^{-13}} = 1.0\times10^{4}.$$

**Scope of the projection.** These numbers are conditional on P1–P3. They establish the temporal resolution a particle‑tracking simulation would need in order to discriminate a continuous local signal from an instantaneous state change across a barrier of the assumed width, under the assumed speed bound and the one‑tenth resolution convention. They are not a universal requirement of every particle‑tracking simulation of the hydrodynamic transport: a simulation targeting a different barrier width $L$ scales $t_{\min}$ linearly ($t_{\min}=L/c$), and a simulation that adopts a different resolution fraction $f$ (timestep $=f\,t_{\min}$) scales $\Delta t$ proportionally, with $N_{\mathrm{steps}}=1/f$ independent of $L$. The projection is therefore a parameterized design envelope, not a fixed threshold.

## 5. Results

All quantitative statements below follow directly from the arithmetic in Section 4.

1. **Quantum GHZ correlations** (Section 4.1): $\langle XXX\rangle_{Q}=+1$; $\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1$.
2. **Classical pointwise constraint** (Section 4.2): $P_{1}P_{2}P_{3}P_{4}=+1$ pointwise, a consequence of A2 alone, promoted to $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1$ with A4 licensing the single‑distribution reading; this conflicts with the quantum product $-1$.
3. **Mermin bound** (Section 4.3): classical $M_{\mathrm{LHV}}=2$; quantum $M_{\mathrm{Q}}=4$; violation factor $2$.
4. **CHSH bound** (Section 4.4): classical bound $2$; quantum maximum $2\sqrt{2}\approx2.828427$; violation factor $\sqrt{2}\approx1.414214$.
5. **Falsification verdict** (Section 4.5): the conjunction of A1–A4 is incompatible with the GHZ stabilizer statistics; the fork of consistent relaxations has four branches (relax A2, relax A4, relax A1, or retain all and accept empirical refutation).
6. **Simulation timescale projections** (Section 4.6, conditional on P1–P3): for $L=1.0\times10^{-3}\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-12}\ \mathrm{s}$, $\Delta t\le3.333333\times10^{-13}\ \mathrm{s}$, $N_{\mathrm{steps}}=10$; for $L=1.0\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-9}\ \mathrm{s}$, $N_{\mathrm{steps}}=1.0\times10^{4}$; in general $t_{\min}=L/v_{\max}$, $\Delta t\le t_{\min}/10$, $N_{\mathrm{steps}}=10$.

## 6. Discussion

**Scope of the falsification.** The derivation shows that the strong claim of HSH—local classical measure theory reproducing GHZ‑type Bell‑violating correlations—is untenable as a conjunction. It does not identify a unique axiom that must be abandoned, and it does not address weaker versions that relax A2, reinterpret locality at the level of the flow $\Phi_{t}$, or restrict the claim to states and measurements outside the GHZ stabilizer set.

**Potential escapes.**
1. The formalization A1–A4 is our own interpretation; [10] does not publish a numbered axiomatization, so an alternative formalization might locate the failure elsewhere. Any such formalization must still reproduce the four stabilizer values, and the counting argument of Section 4.2 applies to any model with local binary response functions and a setting‑independent hidden‑variable distribution.
2. Stochastic response functions do not escape: the identity $P_{1}P_{2}P_{3}P_{4}=+1$ holds pointwise for every assignment of the six local outcomes, so averaging over any distribution preserves it.
3. The connection between basins of attraction (A3) and the Born rule is not derived here; a separate probabilistic mechanism might alter the mapping from $\rho_{\psi}$ to observed frequencies, but it cannot change the algebraic constraint, which precedes any frequency mapping.
4. Relaxing A4 (superdeterminism) is a logically open branch of the fork; HSH's own framing rejects it, but the falsification alone does not close it.

**What would falsify the present result.** The central claim is the incompatibility of A1–A4 with the GHZ stabilizer statistics. A single concrete counterexample would overturn it: an explicit construction of local deterministic (or stochastic) response functions $A_{i}(\lambda_{i},s_{i})$ on a classical probability space, with a setting‑independent $\lambda$‑distribution, that reproduce all four stabilizer values $\langle XXX\rangle=+1$, $\langle XYY\rangle=\langle YXY\rangle=\langle YYX\rangle=-1$. Equivalently, any demonstration that the pointwise product $P_{1}P_{2}P_{3}P_{4}$ can equal $-1$ for some assignment of six binary local outcomes would invalidate the counting argument, since the argument rests on each outcome appearing exactly twice in the product. Absent such a construction, the algebra is closed: six factors, each squared, is an identity in $\{-1,+1\}^{6}$.

**Limitations.**
- The formalization A1–A4 is an interpretation of [10], which publishes no numbered axiom list; a different formalization could shift which axiom bears the contradiction, though not the existence of a contradiction for any local‑response, setting‑free model.
- The timescale projections depend on the assumed barrier width $L$ and the generous speed bound $v_{\max}=c$; other parameter choices scale the numbers linearly, and P3's one‑tenth rule is a resolution convention, not a physical law. The projections are not requirements of every particle‑tracking simulation.
- The analysis treats only the four GHZ stabilizer measurements; other settings (e.g., $YYY$) are omitted because they do not affect the contradiction.
- The derivation assumes binary outcomes $\pm1$; extensions to higher‑dimensional outcomes are not considered.
- The CHSH cross‑check is stated for the standard two‑party combination and applies to convex mixtures of factorized local models, of which the Correlation History theorem of [11] is one instance; it is not a new Bell theorem but a restatement applied to the programs under review.

**Failure modes.** If a construction of local deterministic (or stochastic) response functions satisfying A1–A4 and reproducing all four stabilizer values were exhibited, the pointwise product argument would be invalidated, falsifying the present falsification. Likewise, an empirical demonstration that the GHZ stabilizer statistics admit a local stochastic model with $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=-1$ would overturn the argument.

**Sensitivity analysis.** Varying the barrier width $L$ by an order of magnitude changes the minimum propagation time $t_{\min}$ proportionally, while the required timestep $\Delta t$ remains one‑tenth of $t_{\min}$. Consequently, the number of timesteps for a crossing remains fixed at ten, independent of $L$. This linear scaling emphasizes that the primary engineering challenge is achieving sub‑picosecond temporal resolution at laboratory barrier scales rather than handling large numbers of steps, and that at macroscopic scales the challenge shifts to step count ($10^{4}$ per crossing at $L=1.0\ \mathrm{m}$) at a relaxed nanosecond timestep.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols of the kind optimized in [2] and [6], and theorists exploring classical‑quantum unification programs of the kind in [8] would use this result to assess whether a purely local classical underpinning can support multipartite entanglement resources. If the result holds, any design that assumes a local‑realist foundation for GHZ‑type correlations must be revised to incorporate non‑local or hybrid mechanisms; effort can be redirected toward explicit relaxation of the identified axioms.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; under NASA Technology Readiness Level definitions it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3, and no manufacturing or deployment readiness is claimed.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic or stochastic response functions $A_{i}(\lambda_{i},s_{i})$ on a classical probability space with a setting‑independent $\lambda$‑distribution that reproduce the four GHZ stabilizer values. A successful construction would falsify the present result; a demonstrated impossibility would convert the fals