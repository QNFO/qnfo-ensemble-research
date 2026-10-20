# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis (Version 3.0)

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) proposes that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction of classical probability measures under a local hydrodynamic transport. The specific gap is the absence of an explicit derivation of GHZ‑type Bell‑violating correlations from the hypothesis's own axioms. We formalize the strong form of HSH as four axioms (classical probability space, local state variables, local continuous transport, free measurement settings) and derive, with full arithmetic, that the axioms force the pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ on the four GHZ triple correlations, whereas quantum mechanics predicts a product of $-1$. The resulting Mermin violation factor is $2$ and the CHSH violation factor is $\sqrt{2}\approx1.414214$. We also compute, as a labeled projection conditional on stated assumptions, that a particle‑tracking simulation of the hydrodynamic transport at a millimetre barrier scale would need timesteps of about $333\ \mathrm{fs}$ to resolve the fastest local signals the hypothesis permits. The strong form of HSH is therefore falsified: any classical re‑derivation of GHZ statistics must relax at least one axiom, and the fork of available relaxations is wider than locality alone.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics, and if so which axiom of such a derivation they should expect to give up first. A falsification that identifies the specific axiom under strain converts an open philosophical program into a bounded engineering decision.

This paper is a post‑publication revision of the falsification analysis first issued as version 2.0.0 [9]. Two corrections are carried through. First, the earlier version presented the consequence of the product constraint as exactly two mutually exclusive options (abandon the locality axiom or accept contradiction); the derivation in Section 4.5 shows that the constraint blocks the conjunction of all four axioms, so the complete fork has more branches, and the corrected text enumerates them. Second, the earlier abstract stated that sub‑picosecond timesteps are required for any particle‑tracking simulation that tests the locality claim of HSH; the timescale figures are projections conditional on assumed barrier widths and a speed bound, and the corrected text states them as such.

Our contributions are:
1. Formalization of the strong form of HSH as four minimal axioms (Section 3.1).
2. Derivation of the quantum GHZ stabilizer values and the classical pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ from the axioms, with full arithmetic (Sections 4.1–4.2).
3. Quantitative Mermin and CHSH violation analysis, with violation factors $2$ and $\sqrt{2}\approx1.414214$ (Sections 4.3–4.4).
4. A corrected falsification verdict that enumerates the full fork of axiom relaxations rather than a binary choice (Section 4.5).
5. A labeled projection of the temporal resolution a particle‑tracking test of the locality claim would need, conditional on stated assumptions (Section 4.6).

## 2. Background and Related Work

**Ensemble‑statistical view of quantum dynamics.** Reference [1] develops the philosophy that while individual instances of complex quantum circuits are intractable to simulate, the statistical properties of random ensembles obey simple universal laws, and it maps measurement‑induced phase transitions in random circuits onto classical statistical‑mechanics spin models, deriving averaged Rényi entropies as domain‑wall free energies in a replica limit. This establishes that classical statistical descriptions of quantum information operate at the ensemble level, which is why the axioms of Section 3.1 are phrased for ensembles of hidden configurations rather than single trajectories.

**Multipartite entanglement as a network resource.** Reference [2] presents an algorithm for generating multipartite entanglement between nodes of a noisy quantum network, computing the fidelity of the final state from memory noise and decoherence and the distribution rate from communication time and process stochasticity, and proving optimality under a star‑scheme when links may be reused. Any classical foundation that claims to re‑derive quantum statistics must reproduce exactly these fidelity and rate metrics for quantum‑network applications to function as designed; the GHZ correlations tested in Section 4 are the smallest multipartite instance of that requirement.

**The classical limit of entanglement from the quantum side.** Reference [3] studies entanglement generation in coupled semiclassical systems and states the obstacle for the reverse program directly: since there is no classical quantity corresponding to entanglement, it is not possible to compute a well‑defined classical version of the entanglement growth rate, although chaos generically tends to increase the entanglement rate. HSH attempts to reverse the direction of derivation—quantum statistics from a classical substrate—and the GHZ analysis of Section 4 quantifies precisely where that reversal fails under locality.

**Tripartite entanglement under classical environments.** Reference [4] examines three non‑interacting qubits prepared in a maximally entangled GHZ‑like state coupled to independent classical environments, using an entanglement witness $E(t)=-\mathrm{Tr}[\mathbb{W}_{o}\rho_{abc}(t)]$ and reporting that dephasing of tripartite non‑local correlation differs fundamentally between pure and mixed noisy configurations, with power‑law noise more damaging in the mixed case. This is the closest antecedent to HSH's program in the literature, but it treats the classical environments as external probes that degrade quantum coherence, not as a substrate from which the quantum statistics are derived; the falsification in Section 4 concerns the latter, stronger claim.

**Entanglement‑free classical regimes.** Reference [5] identifies three classical paradigms (material point, test particle, diluted droplet) as limit cases of a quantum regime in which interacting particles do not entangle, connecting them to Quantum Darwinism's environment‑induced superselection principle and showing that coherent states are classical pointer states under a maximal‑information rule. This work demonstrates that large portions of classical behaviour can be recovered from quantum descriptions without entanglement; HSH claims the converse derivation, and the GHZ stabilizer algebra shows the converse cannot hold locally.

**Hybrid entanglement in networks.** Reference [6] constructs an Omega‑type hybrid maximally entangled state over four parties, notes that deterministic teleportation requires maximally entangled states to achieve unit success probability, and proposes an entanglement concentration protocol to extract the maximally entangled state from degraded copies. The resource‑criticality of maximally entangled states motivates the practical weight of the falsification: a foundation that cannot reproduce GHZ‑class statistics cannot underwrite these concentration and distribution protocols.

**Classical–quantum interpolation inside the quantum formalism.** Reference [7] derives the scaling of the $\alpha$‑QPE family of phase‑estimation algorithms within the Quantum Singular Value Transformation framework, trading circuit depth against statistical sampling with the approximation parameters related by $\eta+\frac{1}{2}\delta^{\alpha}=1$. This program interpolates between classical and quantum resources while remaining inside the quantum formalism; HSH's claim is more radical because it reverses the direction of derivation, and Section 4 shows the reversal fails at the level of multipartite correlations.

**Unified classical–quantum formulations.** Reference [8] builds a continuous passage between classical and quantized descriptions through a common action functional, and flags the central obstruction: promoting classical variables to operators is not canonical, since $\overline{H}(\overline{P},\overline{Q})\neq H(P,Q)$ under variable change, so a procedure for choosing the correct promotion is required. HSH's Radon–Nikodým grounding faces an analogous promotion problem from measures to quantum states, and the GHZ analysis shows that no local promotion reproduces the stabilizer values.

**The hypothesis under test.** The HSH paper [10] identifies a "chronological fallacy" in that von Neumann's 1932 axiomatization predated Kolmogorov's 1933 formulation of classical probability, proposes the hydrodynamic stability hypothesis to resolve the schism between continuous hydrodynamic ontology and discrete spectral phenomenology, summarizes a hybrid continuous‑attractor model in which the system is a continuous fluid that appears discrete because it is observed only after settling into stable resonant modes, and calls for weak energy tomography on a hydrogen superposition as the decisive experiment. The axioms of Section 3.1 formalize the locality and attractor claims of [10]; the falsification targets those claims, not the tomography proposal.

**The neighboring PQS program.** The Post‑Quantum Synthesis framework [11] proves a No Spooky Action theorem (local operations on one system leave the spatially separated marginal unchanged), a Correlation History theorem expressing joint statistics as $P(o_{1},o_{2})=\sum_{i}|c_{i}|^{2}P_{1}(o_{1}|\phi_{1}^{i})P_{2}(o_{2}|\phi_{2}^{i})$, and a redundancy threshold $N_{0}=\frac{1}{\gamma}\log\frac{1}{\epsilon}$ for objective outcomes. The Correlation History theorem is a convex mixture of factorized local response models, and Section 4.4's CHSH bound applies to any such mixture. An independent audit of PQS [12] documents its derivation of the Born rule from Gleason's theorem under non‑negativity, normalization and non‑contextuality conditions, and its account of which‑path detection as a physical interaction plus a Bayesian update; the audit's gate‑check record is the source of the observation that PQS's local factorized structure is subject to the same Bell constraints analyzed here.

**The prior version of this analysis.** Reference [9] is the published version 2.0.0 of this falsification analysis, whose Results section reports the same GHZ stabilizer values, product constraint, Mermin and CHSH factors, and simulation projections that Sections 4 and 5 re‑derive and, where the reported errors require it, correct.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms:

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure $\mu_{\psi}\ll\mu$ with Radon–Nikodým derivative $\rho_{\psi}=\frac{d\mu_{\psi}}{d\mu}$, such that all quantum predictions are recoverable as functionals of $\rho_{\psi}$.
- **(A2) Local state variables.** For $N$ spatially separated parties, the hidden configuration decomposes as $\lambda=(\lambda_{1},\ldots,\lambda_{N})$ with $\lambda_{i}\in\Lambda_{i}$; each party's outcome is a local function $A_{i}=f_{i}(\lambda_{i},s_{i})$ of its own variable and its own setting $s_{i}$.
- **(A3) Local continuous transport.** The time evolution $\mu_{t}=(\Phi_{t})_{*}\mu_{0}$ is generated by a local flow $\Phi_{t}$ on $\Lambda$ propagating information at finite speed $v_{\max}$, so that no influence connects spacelike‑separated events. Preparation and measurement correspond to relaxation into basins of attraction $\mathcal{B}_{k}\subset\Lambda$ of stable measures, the observed outcome indexing the basin.
- **(A4) Free settings.** The distribution of measurement settings is statistically independent of $\lambda$ (no superdeterminism).

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality expressed by the No Spooky Action and Correlation History theorems of [11] (A2), and the rejection of superdeterminism implicit in [10]'s framing (A4). The formalization is our own; [10] does not publish a numbered axiom list, so alternative formalizations are discussed in Section 6.

### 3.2 Falsification protocol

Given A1–A4, we test whether the model can reproduce the quantum joint statistics of the GHZ state
$$
|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|000\rangle+|111\rangle\bigr)
$$
under local Pauli measurements $X$ and $Y$ on each qubit. The protocol is: (i) derive the classical constraint imposed by A1–A4 on the four relevant triple correlations, (ii) compute the quantum values of those correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re‑derive the quantum statistics from the classical axioms. The comparison uses the Mermin inequality as the primary instrument and the CHSH inequality as an independent two‑party cross‑check.

### 3.3 Simulation projection protocol

The hypothesis calls for particle‑tracking of the hydrodynamic transport $\Phi_{t}$ [10]. We compute, as a labeled projection with stated assumptions, the propagation timescales such a simulation must resolve for the locality claim of A3 to be testable rather than vacuous: if the simulation's timestep is coarser than the propagation time across the relevant barrier, a local continuous signal and an instantaneous change are observationally indistinguishable in the simulation, and the test loses its discriminating power.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (assumption).** The GHZ state is $|\mathrm{GHZ}\rangle=(|000\rangle+|111\rangle)/\sqrt{2}$.

**Input 2 (assumption).** Pauli operators $X$ and $Y$ have eigenvalues $\pm1$, with actions $X|0\rangle=|1\rangle$, $X|1\rangle=|0\rangle$, $Y|0\rangle=i|1\rangle$, $Y|1\rangle=-i|0\rangle$.

Applying the stabilizer operators:
$$
\begin{aligned}
XXX\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(X|0\rangle X|0\rangle X|0\rangle + X|1\rangle X|1\rangle X|1\rangle\bigr)
= \frac{1}{\sqrt{2}}\bigl(|111\rangle+|000\rangle\bigr)=+|\mathrm{GHZ}\rangle,\\
XYY\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(|1\rangle\, i|1\rangle\, i|1\rangle + |0\rangle\,(-i|0\rangle)(-i|0\rangle)\bigr)
= \frac{1}{\sqrt{2}}\bigl(i^{2}|111\rangle+(-i)^{2}|000\rangle\bigr)=-|\mathrm{GHZ}\rangle,\\
YXY\,|\mathrm{GHZ}\rangle &=-|\mathrm{GHZ}\rangle \quad\text{(by the same phase arithmetic, } i\cdot i=i^{2}=-1\text{)},\\
YYX\,|\mathrm{GHZ}\rangle &=-|\mathrm{GHZ}\rangle \quad\text{(likewise)}.
\end{aligned}
$$

Hence the quantum triple‑product expectations are
$$
\langle XXX\rangle_{Q}=+1,\qquad \langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1.
$$

The product of the four quantum correlations is
$$
(+1)\times(-1)\times(-1)\times(-1)=-1.
$$

### 4.2 The classical constraint from axioms A1–A4

For each party $i\in\{1,2,3\}$ define local predetermined outcomes $A_{i}^{X},A_{i}^{Y}\in\{-1,+1\}$, which exist by A2. The four triple products are
$$
\begin{aligned}
P_{1}&=A_{1}^{X}A_{2}^{X}A_{3}^{X},\qquad
P_{2}=A_{1}^{X}A_{2}^{Y}A_{3}^{Y},\\
P_{3}&=A_{1}^{Y}A_{2}^{X}A_{3}^{Y},\qquad
P_{4}=A_{1}^{Y}A_{2}^{Y}A_{3}^{X}.
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
since each local outcome appears exactly twice and squares to $+1$. Taking expectations with respect to the measure $\mu$ (A1) gives
$$
\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1.
$$

This identity holds pointwise for any deterministic or stochastic assignment of the six local outcomes, because it depends only on the counting structure of A2 and not on the distribution of $\lambda$; A4 (freedom of settings) guarantees that the expectation is taken over the same $\lambda$‑distribution for all four combinations, so no context‑dependence of the outcomes can evade it. Thus the classical axioms force a product of $+1$, whereas quantum mechanics requires $-1$.

### 4.3 Mermin bound and violation factor

For any model satisfying A1–A4, the Mermin combination obeys
$$
\bigl|\langle P_{1}\rangle-\langle P_{2}\rangle-\langle P_{3}\rangle-\langle P_{4}\rangle\bigr|\le 2,
$$
because pointwise $|P_{1}-P_{2}-P_{3}-P_{4}|$ takes only the values $0$ or $2$ when $P_{1}P_{2}P_{3}P_{4}=+1$: expanding, the expression equals $P_{1}(1-P_{2}P_{3}P_{4})-P_{2}P_{3}-P_{4}+2P_{2}P_{3}+2P_{4}$ in absolute form, and since $P_{2}P_{3}P_{4}=P_{1}$ under the product constraint, the pointwise value is $\bigl|P_{1}-P_{2}-P_{3}-P_{4}\bigr|=\bigl|P_{1}(1-P_{2}P_{3}P_{4})\bigr|+\bigl|{-P_{2}-P_{3}-P_{4}+P_{1}P_{2}P_{3}+P_{1}P_{4}}\bigr|$'s simpler equivalent $2\bigl|P_{1}\bigr|\in\{0,2\}$; in every case the pointwise magnitude is at most $2$, and the expectation of a quantity bounded pointwise by $2$ is bounded by $2$. The quantum values give
$$
\bigl|(+1)-(-1)-(-1)-(-1)\bigr|=|1+1+1+1|=4.
$$
Hence the classical bound is $M_{\mathrm{LHV}}=2$, the quantum value is $M_{Q}=4$, the gap is $\Delta M=4-2=2$, and the violation factor is
$$
\frac{M_{Q}}{M_{\mathrm{LHV}}}=\frac{4}{2}=2.
$$

### 4.4 CHSH cross‑check

For two parties the CHSH combination is
$$
S=E(a,b)+E(a,b')+E(a',b)-E(a',b').
$$
Classically, with local outcomes $A,A',B,B'\in\{\pm1\}$, the pointwise identity $S=A(B+B')+A'(B-B')$ gives $|S|\le2$ since $|B+B'|+|B-B'|=2$. Quantum mechanics attains the Tsirelson bound $S_{\max}=2\sqrt{2}$. Using $\sqrt{2}\approx1.414214$:
$$
2\sqrt{2}\approx 2\times1.414214=2.828427.
$$
The violation factor over the classical bound is
$$
\frac{2\sqrt{2}}{2}=\sqrt{2}\approx1.414214.
$$
This cross‑check matters for the neighboring PQS program: the Correlation History theorem of [11] writes joint statistics as a convex sum $\sum_{i}|c_{i}|^{2}P_{1}(o_{1}|\phi_{1}^{i})P_{2}(o_{2}|\phi_{2}^{i})$ of factorized local models, and a convex combination of models each obeying $|S|\le2$ obeys $|S|\le2$ as well, so the same gap of $2.828427-2=0.828427$ applies to that framework's two‑party predictions.

### 4.5 The fork and the falsification verdict

The derivation establishes that the conjunction A1 $\wedge$ A2 $\wedge$ A3 $\wedge$ A4 is incompatible with the GHZ stabilizer statistics: the product constraint of Section 4.2 follows from A2 (local response functions) together with A4 (a single setting‑independent $\lambda$‑distribution), and the contradiction with Section 4.1 follows once A1 commits all predictions to functionals of the classical measure. The earlier version of this analysis [9] presented the consequence as exactly two mutually exclusive options; that presentation was incomplete, because the constraint blocks the conjunction of four axioms and any one of them may be relaxed. The complete fork is:

1. **Relax A2 (locality of response functions).** Allow the outcome functions $A_{i}$ to depend on distant settings, thereby abandoning local realism in its response‑function form.
2. **Relax A4 (setting freedom).** Permit correlations between $\lambda$ and the settings (superdeterminism), which HSH explicitly excludes but which restores a single joint distribution in which the product constraint need not bind the observed statistics in the same way.
3. **Relax A1 (classical probability grounding).** Replace the Kolmogorov measure space with a non‑classical probability structure, abandoning the Radon–Nikodým grounding that defines HSH.
4. **Retain all four axioms and accept contradiction.** Concede that the model cannot reproduce the GHZ stabilizer values, i.e., that it is empirically refuted on these correlations.

Every branch falsifies the strong claim that HSH simultaneously satisfies A1–A4 and reproduces GHZ statistics. The corrected verdict is therefore weaker in scope but more precise than the binary fork: the falsification identifies an incompatibility of the conjunction, not a unique culprit axiom, and the choice among branches is a research decision rather than a derivation.

### 4.6 Simulation timescale projection (explicitly labeled projection)

**Assumptions.**
(P1) The transport speed is bounded by $v_{\max}=c=3.0\times10^{8}\ \mathrm{m\,s^{-1}}$.
(P2) The spatial barrier width is $L=1.0\times10^{-3}\ \mathrm{m}$ (laboratory scale).
(P3) The simulation timestep must be at most one‑tenth of the propagation time to resolve the signal.

**Derivation.** Minimum propagation time:
$$
t_{\min}=\frac{L}{v_{\max}}=\frac{1.0\times10^{-3}}{3.0\times10^{8}}=3.333333\times10^{-12}\ \mathrm{s}\approx3.33\ \mathrm{ps}.
$$
Required timestep:
$$
\Delta t\le\frac{t_{\min}}{10}=3.333333\times10^{-13}\ \mathrm{s}\approx333\ \mathrm{fs}.
$$
Number of timesteps for one crossing:
$$
N_{\mathrm{steps}}=\frac{t_{\min}}{\Delta t}=10.
$$

For a macroscopic barrier $L=1.0\ \mathrm{m}$:
$$
t_{\min}=\frac{1.0}{3.0\times10^{8}}=3.333333\times10^{-9}\ \mathrm{s}\approx3.33\ \mathrm{ns},
\qquad
N_{\mathrm{steps}}=\frac{3.333333\times10^{-9}}{3.333333\times10^{-13}}=1.0\times10^{4}.
$$

These projections are conditional on P1–P3. They establish the temporal resolution a particle‑tracking simulation would need in order to discriminate a continuous local signal from an instantaneous state change across a barrier of the assumed width; they are not requirements independent of those assumptions, and other choices of $L$ scale $t_{\min}$ and $N_{\mathrm{steps}}$ linearly while leaving $\Delta t$ unchanged at fixed P3.

## 5. Results

All quantitative statements below follow directly from the arithmetic in Section 4.

1. **Quantum GHZ correlations** (Section 4.1): $\langle XXX\rangle_{Q}=+1$; $\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1$.
2. **Classical pointwise constraint** (Section 4.2): $P_{1}P_{2}P_{3}P_{4}=+1$ pointwise, implying $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1$, which conflicts with the quantum product $-1$.
3. **Mermin bound** (Section 4.3): classical $M_{\mathrm{LHV}}=2$; quantum $M_{Q}=4$; gap $\Delta M=2$; violation factor $2$.
4. **CHSH bound** (Section 4.4): classical bound $2$; quantum maximum $2\sqrt{2}\approx2.828427$; violation factor $\sqrt{2}\approx1.414214$; the same bound applies to the convex factorized mixtures of the Correlation History theorem of [11].
5. **Falsification verdict** (Section 4.5): the conjunction of A1–A4 is incompatible with the GHZ stabilizer statistics; the fork of consistent relaxations has four branches (relax A2, relax A4, relax A1, or retain all and accept empirical refutation), not two.
6. **Simulation timescale projections** (Section 4.6, conditional on P1–P3): for $L=1.0\times10^{-3}\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-12}\ \mathrm{s}$, $\Delta t\le3.333333\times10^{-13}\ \mathrm{s}$, $N_{\mathrm{steps}}=10$; for $L=1.0\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-9}\ \mathrm{s}$, $N_{\mathrm{steps}}=1.0\times10^{4}$.

## 6. Discussion

**Scope of the falsification.** The derivation shows that the strong claim of HSH—local classical measure theory reproducing GHZ‑type Bell‑violating correlations—is untenable as a conjunction. It does not identify which axiom must be abandoned, and it does not address weaker versions that relax A2, reinterpret locality at the level of the flow $\Phi_{t}$, or restrict the claim to states and measurements outside the GHZ stabilizer set.

**Potential escapes.**
1. The formalization A1–A4 is our own interpretation; [10] does not publish a numbered axiomatization, so an alternative formalization might locate the failure elsewhere. Any such formalization must still reproduce the four stabilizer values, and the counting argument of Section 4.2 applies to any model with local binary response functions and a setting‑independent hidden‑variable distribution.
2. Stochastic response functions do not escape: the identity $P_{1}P_{2}P_{3}P_{4}=+1$ holds pointwise for every assignment of the six local outcomes, so averaging over any distribution preserves it.
3. The connection between basins of attraction (A3) and the Born rule is not derived here; a separate probabilistic mechanism might alter the mapping from $\rho_{\psi}$ to observed frequencies, but it cannot change the algebraic constraint, which precedes any frequency mapping.
4. Relaxing A4 (superdeterminism) is a logically open branch of the fork; HSH's own framing rejects it, but the falsification alone does not close it.

**Limitations.**
- The timescale projections depend on the assumed barrier width $L$ and the generous speed bound $v_{\max}=c$; other parameter choices scale the numbers linearly, and P3's one‑tenth rule is a resolution convention, not a physical law.
- The analysis treats only the four GHZ stabilizer measurements; other settings (e.g., $YYY$) are omitted because they do not affect the contradiction.
- The derivation assumes binary outcomes $\pm1$; extensions to higher‑dimensional outcomes are not considered.
- The CHSH cross‑check is stated for the two‑party restriction of the framework; the numerical Tsirelson value is quoted as standard quantum mechanics, not derived from the HSH axioms, which is consistent with the falsification logic (the axioms fail to reach it).

**What would falsify the falsification.** A single explicit construction of response functions $A_{i}(\lambda_{i},s_{i})$ on a classical probability space, with a setting‑independent $\lambda$‑distribution, whose induced statistics match all four GHZ stabilizer values, would invalidate the product‑constraint argument and overturn the main result. Equivalently, a demonstration that the pointwise product $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}$ can equal $-1$ under A2 and A4 would falsify Section 4.2. The falsification also fails if the GHZ stabilizer values themselves are not properties of the state under the measurement model HSH adopts—but they follow from the standard Pauli algebra used in every quantum‑network fidelity calculation of the kind in [2], so abandoning them would cost HSH its contact with the resource statistics the field actually uses.

**Open questions.** Whether a non‑local but still measure‑theoretic re‑grounding (relaxed A2 with retained A1) can reproduce all quantum statistics, not merely GHZ; whether the basin‑of‑attraction picture can be given a Born‑rule derivation at all; and whether the hydrodynamic transport $\Phi_{t}$ admits a well‑defined speed bound $v_{\max}$ below $c$, which would tighten the simulation projections of Section 4.6.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers in quantum foundations, designers of quantum‑network protocols of the kind optimized in [2], and theorists exploring classical–quantum unification programs of the kind in [8] would use this result to assess whether a purely local classical underpinning can support multipartite entanglement resources. If the result holds, any research program that assumes a local‑realist foundation for GHZ‑type correlations should expect to relax A2 (or another axiom) explicitly, and protocol designers can treat local‑realist re‑derivations of multipartite statistics as bounded rather than open‑ended: the specific axiom under strain is named, so effort can be directed at the relaxation rather than at repeated attempts to satisfy all four axioms at once.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; under the NASA Technology Readiness Level definitions it resides at TRL 1–2 (basic principles observed and reported). Analytical work of this nature never exceeds TRL 3, and no manufacturing or deployment readiness is claimed.

**(c) Smallest next experiment or prototype.** The minimal de‑risking test is a constructive proof‑of‑principle: devise explicit local deterministic or stochastic response functions $A_{i}(\lambda_{i},s_{i})$ on a classical probability space with a setting‑independent $\lambda$‑distribution that reproduce the four GHZ stabilizer values. A successful construction would falsify this paper's central result; a demonstrated impossibility would convert the falsification from an analysis of one formalization into a theorem about the axiom class. A complementary computational test, proposed conditionally: a particle‑tracking simulation of $\Phi_{t}$ across a barrier of width $L=1.0\times10^{-3}\