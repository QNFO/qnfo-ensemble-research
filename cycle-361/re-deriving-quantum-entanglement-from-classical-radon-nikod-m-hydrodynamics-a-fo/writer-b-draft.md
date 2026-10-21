# Re‑Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis (Revision 3.0)

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) claims that quantum mechanics, including multipartite entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be reconstructed from classical measure theory by interpreting wavefunctions as Radon–Nikodým densities that relax into basins of attraction under a locally bounded hydrodynamic flow. The specific gap is the absence of an explicit derivation of GHZ‑type Bell‑violating correlations from the hypothesis's own axioms. We formalize the strong form of HSH as four minimal axioms (classical measure grounding, local hidden variables, locally bounded continuous transport, and free measurement settings) and derive, with full arithmetic, that the axioms force the pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ on the four GHZ triple correlations, whereas quantum mechanics predicts a product of $-1$. The resulting Mermin violation factor is $2$ and the CHSH violation factor is $\sqrt{2}\approx1.414214$. As a labeled projection, conditional on the assumptions that the transport speed is bounded by $c$, the barrier width is $L=10^{-3}\,\mathrm{m}$, and the simulation timestep is at most one‑tenth of the crossing time, the required timestep is roughly $333\,\mathrm{fs}$; this figure is a conditional resolution requirement for locality‑testing simulations of the assumed geometry, not a universal requirement of every particle‑tracking simulation. The strong, local‑realist form of HSH is therefore falsified: any classical re‑derivation of GHZ statistics must relax at least one of the four axioms, and the logical fork comprises four distinct branches.

## 1. Introduction

Engineers designing quantum‑network hardware and protocol designers optimizing entanglement distribution must treat multipartite entanglement as a scarce physical resource that enables secret sharing, distributed sensing, and fault‑tolerant computation. The practical problem is that Bell‑violating correlations impose stringent constraints on any underlying local‑realist description: a protocol whose correctness proof assumes GHZ‑type statistics cannot be re‑implemented on a substrate whose correlations obey classical bounds. If the Hydrodynamic Stability Hypothesis (HSH) were correct, it would provide a local‑realist, classical‑measure‑theoretic foundation for these resources, eliminating the need for non‑local explanations and potentially simplifying network‑level design. The decision that changes with the result is whether researchers invest effort in a classical re‑derivation of entangled statistics, and if so which axiom of such a derivation they should expect to give up first. A falsification that identifies the specific axiom or axioms under strain converts an open philosophical program into a bounded engineering decision.

The hypothesis at issue is stated in [10], which proposes HSH as a reconstruction of quantum mechanics inside classical Kolmogorov probability, motivated by what it calls a "chronological fallacy": the axiomatization of quantum mechanics by von Neumann (1932) predated the rigorous formulation of classical probability by Kolmogorov (1933). The hypothesis explicitly claims to reproduce quantum statistics without non‑locality, and it calls for particle‑tracking simulation of its hydrodynamic transport as an empirical test. This paper supplies the formal test that the hypothesis's own multipartite claims must pass, and shows that they fail.

Our contributions are:
1. Formalization of the strong form of HSH as four minimal axioms (Section 3.1).
2. Derivation of the quantum GHZ stabilizer values and the classical pointwise product constraint $P_{1}P_{2}P_{3}P_{4}=+1$ from the axioms, with full arithmetic, establishing that the constraint follows from the locality axiom A2 alone and that the setting‑freedom axiom A4 is needed only to promote the pointwise identity to observed correlations (Sections 4.1–4.2).
3. Quantitative Mermin and CHSH violation analysis, with violation factors $2$ and $\sqrt{2}\approx1.414214$ (Sections 4.3–4.4).
4. A falsification verdict that enumerates the complete four‑branch fork of axiom relaxations, replacing any two‑option framing (Section 4.5).
5. A labeled projection of the temporal resolution a particle‑tracking test of the locality claim would need, conditional on stated assumptions, with the timestep‑scaling convention stated consistently for all barrier widths (Section 4.6).

## 2. Background and Related Work

**Ensemble‑statistical mappings of quantum dynamics.** Reference [1] develops the program of mapping random quantum circuit dynamics onto classical statistical mechanics: its Section IV.3 derives boundary‑condition partition functions $Z_{A}$ and $Z_{0}$ whose difference yields the averaged Rényi entropy $\overline{S^{(n)}_{A}}$ as a domain‑wall free energy, and its Discussion states that this mapping "establishes an equivalence between the entanglement‑ and purification‑transition perspectives." This demonstrates that classical statistical descriptions can capture ensemble‑level quantum information, which motivates the ensemble‑focused phrasing of the axioms in Section 3.1; the GHZ analysis below shows that the same classical capture fails at the level of individual multipartite correlations.

**Multipartite entanglement as a network resource.** Reference [2] presents an algorithm for generating multipartite entanglement over noisy quantum networks, computing as performance metrics "the fidelity of the final state, depending on the noise and decoherence of the quantum memories, and the rate of distribution" (its Section 5). Any classical foundation that claims to reproduce quantum statistics must match these fidelity and rate metrics; the GHZ correlations examined here constitute the smallest multipartite instance of that requirement.

**Tripartite entanglement under classical environments.** Reference [4] studies three non‑interacting qubits prepared in a maximally entangled GHZ‑like state coupled to independent classical environments, using entanglement witnesses of the form $E(t)=-\mathrm{Tr}[\mathbb{W}_{o}\rho_{abc}(t)]$ and concluding that dephasing effects on tripartite non‑local correlation "are fundamentally different in pure and mixed noisy configurations." This work is the closest antecedent to HSH's program, but it treats classical environments as external probes that degrade quantum coherence rather than as a substrate from which quantum statistics are derived.

**Entanglement‑free classical regimes.** Reference [5] identifies classical limits of the two‑body problem — the material point, test‑particle and droplet paradigms — as regimes in which interacting particles do not entangle, connecting them to Zurek's environment‑induced superselection within the quantum formalism. Its Section 2.2 records Bell's theorem as showing that for entangled states "the knowledge of the whole cannot be reduced to the knowledge of the parts." HSH claims the converse derivation, from classical descriptions to quantum statistics; the GHZ stabilizer algebra shows the converse cannot hold locally.

**Classical–quantum interpolation inside the quantum formalism.** Reference [7] derives the scaling of the $\alpha$‑QPE family of phase‑estimation algorithms within the Quantum Singular Value Transformation framework, trading circuit depth against sampling through the relation $\eta+\frac{1}{2}\delta^{\alpha}=1$ between approximation parameters. This program interpolates between classical and quantum resources while remaining inside the quantum formalism; HSH's claim is more radical because it reverses the direction of derivation, and Section 4 shows the reversal fails at the level of multipartite correlations.

**Unified classical–quantum formulations.** Reference [8] constructs a common action functional for classical and quantum systems and devotes its Section 2.1 to the promotion problem: a change of classical variables $(p,q)\to(\bar{p},\bar{q})$ preserves the classical Hamiltonian, $\bar{H}(\bar{p},\bar{q})=H(p,q)$, but the promoted operators generally satisfy $\bar{H}(\bar{P},\bar{Q})\neq H(P,Q)$, so "it is absolutely necessary to find a procedure whereby favored classical variables are the ones that are promoted to the correct quantum operators." HSH's Radon–Nikodým grounding faces an analogous promotion problem from measures to quantum states, and the GHZ analysis shows that no local promotion reproduces the stabilizer values.

**The absence of a classical counterpart to entanglement.** Reference [3] studies entanglement as Planck's constant becomes small and states in its Section III.1 that "since there is no classical quantity corresponding to entanglement, it is not possible to compute a well‑defined classical version" of the entanglement‑generation equation. This observation underpins the impossibility results developed here: the algebraic identity derived in Section 4.2 is a purely classical constraint that nevertheless contradicts the quantum stabilizer product.

**Entanglement in quantum networks.** Reference [6] states in its introduction that "quantum entanglement is an irreplaceable quantum resource" essential for teleportation, dense coding, and quantum key distribution, and that maximally entangled states are required for unit‑success‑probability deterministic communication. The GHZ state analyzed below is the minimal multipartite instance of such a resource, so the falsification of a local‑realist reconstruction bears directly on any protocol that would rely on a classical hydrodynamic substrate to generate GHZ‑type correlations.

**Hydrodynamic Stability Hypothesis.** Reference [10] proposes HSH as a local‑realist, measure‑theoretic reconstruction of quantum mechanics. Its hybrid model section states that "the system *is* a continuous fluid (Kolmogorovian/Madelung), but it *appears* discrete (von Neumann) because we only observe it after it has settled into stable resonant modes (attractors) driven by the act of observation," and its proposed experiment calls for weak energy tomography on a hydrogen superposition. The hypothesis provides the target of the present falsification; its own call for particle‑tracking simulation motivates the projection in Section 4.6.

**Post‑Quantum Synthesis (PQS).** Reference [11] proves a No‑Spooky‑Action theorem — for a local unitary $U_1$ on system $\mathcal{R}_1$ alone, the marginal $\rho_2=\mathrm{tr}_1(|\phi'_{12}\rangle\langle\phi'_{12}|)=\sum_i |c_i|^{2}|\phi_2^{i}\rangle\langle\phi_2^{i}|$ is unchanged — and a Correlation History theorem expressing joint statistics as $P(o_1,o_2)=\sum_i |c_i|^{2}P_1(o_1|\phi_1^{i})P_2(o_2|\phi_2^{i})$. These theorems formalize the factorized local response structure that underlies Bell‑type constraints, directly relevant to the product‑constraint derivation in Section 4.2.

**PQS AI‑Evaluation Audit.** Reference [12] documents an independent audit of PQS, including a derivation of the Born rule from rational‑consistency conditions via Gleason's theorem, requiring non‑negativity, normalization, and non‑contextuality of probability assignments. The non‑contextuality requirement is the same structural condition that the GHZ product constraint enforces across measurement settings, and the audit's confirmation of the No‑Spooky‑Action and Correlation History theorems supports the reading of A2 used in Section 4.2.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms:

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure $\mu_{\psi}\ll\mu$ with Radon–Nikodým derivative $\rho_{\psi}= \frac{d\mu_{\psi}}{d\mu}$, such that all quantum predictions are recoverable as functionals of $\rho_{\psi}$.

- **(A2) Local hidden variables.** For $N$ spatially separated parties, the hidden configuration decomposes as $\lambda=(\lambda_{1},\ldots,\lambda_{N})$ with $\lambda_{i}\in\Lambda_{i}$; each party's outcome is a local function $A_{i}=f_{i}(\lambda_{i},s_{i})$ of its own variable and its own setting $s_{i}$.

- **(A3) Locally bounded continuous transport.** The time evolution $\mu_{t}= (\Phi_{t})_{*}\mu_{0}$ is generated by a local flow $\Phi_{t}$ on $\Lambda$ propagating information at finite speed $v_{\max}$, so that no influence connects spacelike‑separated events. Preparation and measurement correspond to relaxation into basins of attraction $\mathcal{B}_{k}\subset\Lambda$ of stable measures, the observed outcome indexing the basin.

- **(A4) Free settings.** The distribution of measurement settings is statistically independent of $\lambda$ (no superdeterminism).

These axioms capture the hybrid continuous‑attractor model of [10] (A1 and the basin clause of A3), the locality claim of [10] (A3), the response‑function locality expressed by the No‑Spooky‑Action and Correlation History theorems of [11] (A2), and the rejection of superdeterminism implicit in [10] (A4). The formalization is our own; [10] does not publish a numbered axiom list, so alternative formalizations are discussed in Section 6.

### 3.2 Falsification protocol

Given A1–A4, we test whether the model can reproduce the quantum joint statistics of the GHZ state
$$
|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|000\rangle+|111\rangle\bigr)
$$
under local Pauli measurements $X$ and $Y$ on each qubit. The protocol is: (i) derive the classical constraint imposed by A1–A4 on the four relevant triple correlations, (ii) compute the quantum values of those correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re‑derive the quantum statistics from the classical axioms. The comparison uses the Mermin inequality as the primary instrument and the CHSH inequality as an independent two‑party cross‑check.

### 3.3 Simulation projection protocol

The hypothesis calls for particle‑tracking of the hydrodynamic transport $\Phi_{t}$ [10]. We compute, as a labeled projection with stated assumptions, the propagation timescales such a simulation must resolve for the locality claim of A3 to be testable rather than vacuous: if the simulation's timestep is coarser than the propagation time across the relevant barrier, a local continuous signal and an instantaneous change are observationally indistinguishable in the simulation, and the test loses its discriminating power. The projection is conditional on the assumed signal speed, barrier width and resolution convention; it is not a universal requirement of every particle‑tracking simulation, and the timestep‑scaling convention is applied uniformly to all barrier widths in Section 4.6.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (assumption).** The GHZ state is $|\mathrm{GHZ}\rangle=(|000\rangle+|111\rangle)/\sqrt{2}$.

**Input 2 (assumption).** Pauli operators $X$ and $Y$ have eigenvalues $\pm1$, with actions $X|0\rangle=|1\rangle$, $X|1\rangle=|0\rangle$, $Y|0\rangle=i|1\rangle$, $Y|1\rangle=-i|0\rangle$.

Applying the stabilizer operators:
$$
\begin{aligned}
XXX\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(|111\rangle+|000\rangle\bigr)=+|\mathrm{GHZ}\rangle,\\
XYY\,|\mathrm{GHZ}\rangle &= \frac{1}{\sqrt{2}}\bigl(X|0\rangle Y|0\rangle Y|0\rangle + X|1\rangle Y|1\rangle Y|1\rangle\bigr)
= \frac{1}{\sqrt{2}}\bigl((i)(i)|111\rangle+(-i)(-i)|000\rangle\bigr)=-|\mathrm{GHZ}\rangle,
\end{aligned}
$$
and by the same computation with the single $X$ permuted among the three parties,
$$
YXY\,|\mathrm{GHZ}\rangle=-|\mathrm{GHZ}\rangle,\qquad YYX\,|\mathrm{GHZ}\rangle=-|\mathrm{GHZ}\rangle.
$$
In each of the last three cases the two amplitudes acquire factors $i\cdot i=-1$ and $(-i)\cdot(-i)=-1$ respectively, so both terms flip sign.

Hence the quantum triple‑product expectations are
$$
\langle XXX\rangle_{Q}=+1,\qquad
\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1.
$$

The product of the four quantum correlations is
$$
(+1)\times(-1)\times(-1)\times(-1)=-1.
$$

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
since each local outcome appears exactly twice and squares to $+1$. This identity follows from A2 alone: it holds for every assignment of the six local outcomes, independent of any distribution over $\lambda$. A4 plays no role in the pointwise identity; it is required only at the next step, where the identity is promoted to a statement about experimentally accessible correlations.

With A4 in place, the four products $P_{k}$ are expectations over a single distribution of $\lambda$. Taking expectations with respect to the measure $\mu$ (A1) and using that the pointwise identity holds for every $\lambda$,
$$
\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=\int P_{1}(\lambda)P_{2}(\lambda)P_{3}(\lambda)P_{4}(\lambda)\,d\mu(\lambda)=\int (+1)\,d\mu(\lambda)=+1.
$$

Thus the classical axioms force a product of $+1$, whereas quantum mechanics requires $-1$. The contradiction is between the conjunction A1$\wedge$A2$\wedge$A4 and the quantum statistics; A3 enters only through the physical interpretation of the transport, not through the algebra.

### 4.3 Mermin bound and violation factor

For any model satisfying A1–A4,
$$
\bigl|\langle P_{1}\rangle-\langle P_{2}\rangle-\langle P_{3}\rangle-\langle P_{4}\rangle\bigr|\le 2,
$$
because pointwise $|P_{1}-P_{2}-P_{3}-P_{4}|=2$ whenever $P_{1}P_{2}P_{3}P_{4}=+1$: with $P_{1}=P_{2}P_{3}P_{4}$, the quantity $P_{1}-P_{2}-P_{3}-P_{4}$ takes only the values $\pm2$ on the eight assignments consistent with the product constraint (a direct check of the two classes: if $P_{2}=P_{3}=P_{4}=+1$ then $P_{1}=+1$ and the expression is $1-1-1-1=-2$; if exactly one or exactly three of $P_{2},P_{3},P_{4}$ equal $-1$, then $P_{1}=-1$ and the expression is $-1+1+1+1=+2$ or $-1-1-1+1=-2$; the remaining assignments are excluded by the product constraint). The quantum values give
$$
\bigl|(+1)-(-1)-(-1)-(-1)\bigr|=|1+1+1+1|=4.
$$
Hence the classical bound is $M_{\mathrm{LHV}}=2$, the quantum value is $M_{\mathrm{Q}}=4$, and the violation factor is
$$
\frac{M_{\mathrm{Q}}}{M_{\mathrm{LHV}}}= \frac{4}{2}=2.
$$

### 4.4 CHSH cross‑check

For two parties the CHSH combination is
$$
S = E(a,b) + E(a,b') + E(a',b) - E(a',b').
$$
Classically $|S|\le 2$: pointwise, each of the four products of local outcomes appears twice in $S$ up to sign, so $|S|\le 2$ for every assignment of the four local outcomes, and averaging preserves the bound. Quantum mechanics attains the Tsirelson bound $S_{\max}=2\sqrt{2}$. Using $\sqrt{2}\approx1.414214$:
$$
2\sqrt{2}\approx 2\times1.414214 = 2.828427.
$$
The violation factor over the classical bound is
$$
\frac{2\sqrt{2}}{2}= \sqrt{2}\approx1.414214.
$$
This cross‑check is a restatement of the Bell constraint for convex mixtures of factorized local models, as embodied in the Correlation History theorem of [11]; it is not a new theorem.

### 4.5 The fork and the falsification verdict

The derivation establishes that the conjunction
$$
\text{A1}\;\wedge\;\text{A2}\;\wedge\;\text{A3}\;\wedge\;\text{A4}
$$
is incompatible with the GHZ stabilizer statistics. The complete fork of consistent responses is:

1. **Relax A2 (locality of response functions).** Allow the outcome functions $A_{i}$ to depend on distant settings, thereby abandoning local realism in its response‑function form.
2. **Relax A4 (setting freedom).** Permit correlations between $\lambda$ and the measurement settings (superdeterminism), which would remove the single‑distribution assumption used to promote the pointwise identity to the observed correlations.
3. **Relax A1 (classical probability grounding).** Replace the Kolmogorov measure space with a non‑classical probability structure, abandoning the Radon–Nikodým grounding that defines HSH.
4. **Retain all four axioms and accept contradiction.** Concede that the model cannot reproduce the GHZ stabilizer values, i.e., that it is empirically refuted on these correlations.

Every branch falsifies the strong claim that HSH simultaneously satisfies A1–A4 and reproduces GHZ statistics. The verdict therefore identifies an incompatibility of the conjunction, not a unique culprit axiom, and the choice among branches is a research decision rather than a derivation. The fork is not exhaustive over all conceivable modifications of the hypothesis — for example, a revision that changes the mapping from outcomes to basins while keeping A1–A4 would still fall under branch 4 — but it is exhaustive over relaxations of the four axioms as stated.

### 4.6 Simulation timescale projection (explicitly labeled projection)

**Assumptions.**
(P1) The transport speed is bounded by $v_{\max}=c=3.0\times10^{8}\ \mathrm{m\,s^{-1}}$.
(P2) The spatial barrier width is $L=1.0\times10^{-3}\ \mathrm{m}$ (laboratory scale).
(P3) The simulation timestep must be at most one‑tenth of the propagation time (a resolution convention), applied at every barrier width.

**Derivation.** Minimum propagation time:
$$
t_{\min}= \frac{L}{v_{\max}} = \frac{1.0\times10^{-3}\ \mathrm{m}}{3.0\times10^{8}\ \mathrm{m\,s^{-1}}} = 3.333333\times10^{-12}\ \mathrm{s}\approx3.33\ \mathrm{ps}.
$$
Required timestep under P3:
$$
\Delta t \le \frac{t_{\min}}{10}=3.333333\times10^{-13}\ \mathrm{s}\approx333\ \mathrm{fs}.
$$
Number of timesteps for one crossing:
$$
N_{\mathrm{steps}} = \frac{t_{\min}}{\Delta t}=10.
$$

For a macroscopic barrier $L=1.0\ \mathrm{m}$, applying the same convention P3 uniformly:
$$
t_{\min}= \frac{1.0\ \mathrm{m}}{3.0\times10^{8}\ \mathrm{m\,s^{-1}}} = 3.333333\times10^{-9}\ \mathrm{s}\approx3.33\ \mathrm{ns},
$$
$$
\Delta t \le \frac{t_{\min}}{10}=3.333333\times10^{-10}\ \mathrm{s}\approx333\ \mathrm{ps},
\qquad
N_{\mathrm{steps}} = \frac{t_{\min}}{\Delta t}=10.
$$

An alternative convention fixes the timestep at the laboratory‑scale value $\Delta t=333\ \mathrm{fs}$ regardless of $L$; under that convention, for $L=1.0\ \mathrm{m}$,
$$
N_{\mathrm{steps}} = \frac{3.333333\times10^{-9}\ \mathrm{s}}{3.333333\times10^{-13}\ \mathrm{s}} = 1.0\times10^{4}.
$$
The two conventions differ in which quantity is held fixed: P3 holds the step count fixed and scales the timestep with $L$; the fixed‑timestep convention holds the timestep fixed and scales the step count. This paper adopts P3 as its primary convention because it is the resolution requirement stated in Section 3.3, and reports the fixed‑timestep figure as the alternative. Under either convention, the timestep required at laboratory barrier scale is sub‑picosecond, which is the operative engineering constraint.

These projections are conditional on P1–P3 and establish the temporal resolution a particle‑tracking simulation must achieve in order to discriminate a continuous local signal from an instantaneous state change across a barrier of the assumed width. They are requirements for simulations that test the locality claim of A3 at the assumed geometry, not requirements for every particle‑tracking simulation of the hydrodynamic transport.

## 5. Results

All quantitative statements below follow directly from the arithmetic in Section 4.

1. **Quantum GHZ correlations** (Section 4.1): $\langle XXX\rangle_{Q}=+1$; $\langle XYY\rangle_{Q}=\langle YXY\rangle_{Q}=\langle YYX\rangle_{Q}=-1$.
2. **Classical pointwise constraint** (Section 4.2): $P_{1}P_{2}P_{3}P_{4}=+1$ pointwise (consequence of A2 alone); with A4 this yields $\langle P_{1}P_{2}P_{3}P_{4}\rangle_{\mu}=+1$, conflicting with the quantum product $-1$.
3. **Mermin bound** (Section 4.3): classical $M_{\mathrm{LHV}}=2$; quantum $M_{\mathrm{Q}}=4$; violation factor $2$.
4. **CHSH bound** (Section 4.4): classical bound $2$; quantum maximum $2\sqrt{2}\approx2.828427$; violation factor $\sqrt{2}\approx1.414214$.
5. **Falsification verdict** (Section 4.5): the conjunction of A1–A4 is incompatible with the GHZ stabilizer statistics; the fork of consistent responses has four branches (relax A2, relax A4, relax A1, or retain all and accept empirical refutation).
6. **Simulation timescale projections** (Section 4.6, conditional on P1–P3): for $L=1.0\times10^{-3}\ \mathrm{m}$, $t_{\min}=3.333333\times10^{-12}\ \mathrm{s}$, $\Delta t\le3.333333\times10^{-13}\ \mathrm{s}$, $N_{\mathrm{steps}}=10$; for $L=1.0\ \mathrm{m}$ under the same convention P3, $t_{\min}=3.333333\times10^{-9}\ \mathrm{s}$, $\Delta t\le3.333333\times10^{-10}\ \mathrm{s}$, $N_{\mathrm{steps}}=10$; under the alternative fixed‑timestep convention ($\Delta t=333\ \mathrm{fs}$ at all $L$), $N_{\mathrm{steps}}=1.0\times10^{4}$ for $L=1.0\ \mathrm{m}$. In general under P3, $t_{\min}=L/v_{\max}$, $\Delta t\le t_{\min}/10$, $N_{\mathrm{steps}}=10$ for every $L$.

## 6. Discussion

**Scope of the falsification.** The derivation shows that the strong claim of HSH — local classical measure theory reproducing GHZ‑type Bell‑violating correlations — is untenable as a conjunction. It does not identify a unique axiom that must be abandoned, and it does not address weaker versions that relax A2, reinterpret locality at the level of the flow $\Phi_{t}$, or restrict the claim to states and measurements outside the GHZ stabilizer set.

**Potential escapes.**
1. The formalization A1–A4 is our own interpretation; [10] does not publish a numbered axiom list, so an alternative formalization might locate the failure elsewhere. Any such formalization must still reproduce the four stabilizer values, and the counting argument of Section 4.2 applies to any model with local binary response functions and a setting‑independent hidden‑variable distribution.
2. Stochastic response functions do not escape: the identity $P_{1}P_{2}P_{3}P_{4}=+1$ holds pointwise for every assignment of the six local outcomes, so averaging over any distribution preserves it.
3. The connection between basins of attraction (A3) and the Born rule is not derived here; a separate probabilistic mechanism might alter the mapping from $\rho_{\psi}$ to observed