# Torsion as a Candidate Geometric Generator of Quantum Phase and Statistics: A Formalization and Falsifiability Analysis

## Abstract

Quantum mechanics is built on postulates — the complex phase of the wavefunction, the quadratic dimension of the state space, and the boson/fermion restriction on exchange symmetry — that are empirically successful but deductively unexplained. A conjecture in current circulation holds that spacetime torsion in Einstein-Cartan gravity generates all three: the axial torsion vector supplies the wavefunction's phase gradient, the geometry of the Lorentz factor fixes a $\pi/2$ angular normalization, and the topology of torsional exchange paths permits only $\pm 1$ exchange phases. This paper formalizes the claimed deductive chain link by link. We show that the exchange-phase restriction follows from the double-swap identity alone, that the normalized state space of an $N$-level system carries $K = N^2 - 1$ real parameters (3, 8, and 15 for $N = 2, 3, 4$), and that the integral of the Lorentz factor over physical velocities evaluates to $\pi/2 \approx 1.5707963$, reproducing the claimed angular normalization. We write the Madelung form of a torsion-coupled probability current and show that the identification of the axial torsion vector with the phase gradient is dimensionally consistent but unproven. The dark-matter "torsion lump" conjecture remains outside our derivations and is treated as an open hypothesis. The chain is partially derivable: statistics and state-space dimension reduce to topology and counting, while the torsion-phase identification is the load-bearing unproven link. We specify the calculation that would confirm or break it.

## 1. Introduction

Physicists who design quantum experiments and interpret quantum data currently accept three structural facts as postulates rather than derivations. First, the state of a quantum system lives in a complex Hilbert space, so an $N$-level system's normalized state carries $K = N^2 - 1$ real parameters; no one derives this count from deeper structure. Second, exchanging two identical particles multiplies the wavefunction by $e^{i\varphi}$ with $\varphi \in \{0, \pi\}$ only — bosons or fermions — a restriction imposed as the symmetrization postulate. Third, the wavefunction's complex phase has no accepted geometric origin; it is inserted by hand. These gaps have practical costs. Anyon-like "transtatistics" generalizations are proposed and searched for without a principled reason they should or should not exist in $3+1$ dimensions [2]; quantum state estimation theory must assume the Hilbert-space geometry whose origin it cannot explain [1]; and any proposed modification of quantum statistics lacks a criterion for which modifications geometry forbids.

If the torsion conjecture holds, these postulates become theorems of Einstein-Cartan geometry, and the design criterion for exotic-statistics searches changes from "look everywhere" to "look only where torsional topology allows it." If it fails, the failure localizes exactly which link breaks — the phase generation, the dimension count, or the exchange restriction — and tells reconstruction programs what any geometric foundation of quantum mechanics must supply instead. Either outcome is decision-relevant for the quantum foundations and quantum-statistics communities.

This paper does not claim to prove the conjecture. It does three things that a proof attempt requires first. It separates the conjecture's four claimed links and derives the ones that are derivable from standard mathematics and the cited literature. It writes the torsion-coupled Madelung equations explicitly, so that the phase-generation link has a definite mathematical form that can be checked or refuted. It states, with shown arithmetic, the quantitative content of each derived link.

The contributions are:

- A derivation, from the double-swap identity stated in [2], that exchange phases in three spatial dimensions are restricted to $e^{i\varphi} = \pm 1$, with the arithmetic shown (Section 4.1).
- A derivation of the real parameter count $K = N^2 - 1$ of the normalized quantum state space from the Hermiticity and trace constraints written in [1], evaluated for $N = 2, 3, 4$ (Section 4.2).
- A derivation that the integral of the Lorentz factor $\gamma(\beta) = (1-\beta^2)^{-1/2}$ over $\beta \in [0,1]$ equals $\pi/2 \approx 1.5707963$, reproducing the conjecture's claimed angular normalization (Section 4.3).
- The explicit Madelung form of a torsion-coupled probability current, with the axial-torsion/phase-gradient identification stated as a dimensionally consistent ansatz and its unproven status made precise (Section 4.4).
- A falsifiability analysis: the specific calculation whose outcome would confirm or break the torsion-phase link, and the observations that would falsify each derived link (Sections 5 and 6).

## 2. Background and Related Work

The torsion conjecture sits at the intersection of quantum statistical mechanics, quantum reconstruction, geometric phase theory, and geometric approaches to phase transitions. We review the works that supply the specific results our analysis uses.

Gill and Levit [1] develop quantum statistics on finite-dimensional Hilbert spaces and state the geometric substrate on which the whole field rests: a $d$-dimensional system's state is a $d \times d$ density matrix $\rho$, Hermitian, non-negative, with trace 1, and for $d = 2$ every state is $\rho = \frac{1}{2}(\mathbf{1} + \theta_1\sigma_1 + \theta_2\sigma_2 + \theta_3\sigma_3)$ with $\theta_1^2 + \theta_2^2 + \theta_3^2 \leq 1$ — a three-real-parameter ball. Their derivation of asymptotic Bayes-risk lower bounds via the Holevo quantum Cramér-Rao bound, including the collective-measurement advantage over separate measurements, presupposes this geometry rather than explaining it. Our Section 4.2 takes their explicit parameterization as the input and counts the parameters for general $N$; the conjecture's claim that this count is geometrically forced is tested against their stated structure.

Diaz-Marino and collaborators on statistics reconstruction [2] give the sharpest available statement of the exchange-phase problem. Their Introduction derives the two-statistics restriction in one line: if $\psi(x_2,x_1) = e^{i\varphi}\psi(x_1,x_2)$, then applying the swap twice gives $e^{i\varphi} = \pm 1$ — bosons and fermions. They note that the physical motivation for the symmetrization postulate "remains poorly understood," that exotic statistics have never been observed in nature, and that their operational reconstruction, following Hardy's instrumentalist approach with single-particle unitary channels and number-only detectors, makes the Fock-space structure emerge rather than assume it. Their partition theorem shows that not every $U(1)$-character induces a valid $U(d)$-character: the example $\chi_1(x) = 1 + x^2$ produces a negative expansion coefficient $c_{(1,1)}$ for two modes, so candidate generalized statistics are already constrained by positivity. Our Section 4.1 reproduces their double-swap arithmetic as the topological core of the exchange link, and Section 6 asks whether torsional topology adds anything beyond it.

Le Hur [3] treats quantum phase transitions in spin-boson systems, where a two-level system couples to a bath of harmonic oscillators and dissipation drives or modifies phase transitions; in the ohmic case the order parameter $\langle\sigma_z\rangle$ jumps by a non-universal amount $\sqrt{1/\alpha_c}$ along the quantum critical line with $\alpha_c = 1 + \mathcal{O}(\Delta/\omega_c)$. This supplies a worked example of a quantum statistical structure — the bosonic bath — whose existence the torsion conjecture would derive; we cite it as the phenomenological end point that any derivation of bosonic statistics must ultimately reproduce.

The Tianyan platform paper [4] reports a 105-qubit superconducting processor with single-qubit gate, two-qubit gate, and readout fidelities of 99.90%, 99.56%, and 98.7% respectively, cloud-accessible, and demonstrates random circuit sampling with 74 qubits and 24 cycles. We cite it in Section 7 as the class of currently available testbed on which statistics-sensitive interference experiments could be specified, without claiming any torsion-specific capability for it.

Sarandy and collaborators [5] extend geometric phases to open quantum systems: for cyclic adiabatic evolution under a Lindblad master equation, they derive Abelian and non-Abelian geometric phase expressions that generalize the Berry and Wilczek-Zee phases, prove their gauge invariance, and find robustness against dephasing and spontaneous emission for a spin-1/2 in a magnetic field — robustness that fails for the bit-flip channel because it does not commute with the Hamiltonian superoperator. This matters for our program because if torsion generates the quantum phase, the phase is geometric in precisely the Berry sense, and [5] supplies the machinery for asking whether a torsion-generated phase survives decoherence.

Simpson and collaborators [6] argue for fusing statistics with network science in complex functional brain network analysis, a case study in combining statistical inference with geometric/graph-theoretic structure. We cite it only for the specific methodological point its abstract makes — that network science (an interdisciplinary offshoot of graph theory) enabled examining the brain as an integrated system — as an analogy for how statistical and geometric descriptions of the same system must be fused rather than juxtaposed; our Madelung analysis in Section 4.4 performs the analogous fusion for probability currents.

Kastner and collaborators [7] propose, against the topological hypothesis, that a substantial change in the geometry — not the topology — of the accessible configuration space is the necessary condition for a phase transition, with Conj. 1 proposing that a discontinuity in the mixing time on configuration space is necessary for a first-order transition in the thermodynamic limit; their hard-disk and hard-sphere quotient-space results found that discontinuity locations in the diffusion diameter were robust under changes of the quotienting symmetry group. This is directly relevant: the torsion conjecture is a claim that geometry generates quantum structure, and [7] provides a worked precedent for geometry-versus-topology adjudication in a neighboring problem, including the caution that geometric and topological features can change dramatically with symmetry choices while the physically relevant discontinuities do not.

The QNFO corpus supplies four works in the same geometric-reduction program. The Riemannian superdeterministic Bell-violations paper [8] proposes that Bell-inequality violations emerge from intrinsic curvature of a discretized state-space manifold, violating measurement independence through a global geometric constraint, and identifies entanglement saturation, fractal jitter, and gravitational variance in Bell-test correlations as falsification channels. We cite it for its specific argument that flat-space Hilbert geometry is an approximation whose breakdown has observable signatures — the same methodological bet as the torsion conjecture, applied to correlations rather than phase and statistics. The From Force to Fractal paper [9] argues for replacing force-based descriptions with geometric ontic structures, citing the reduction of gravity to Riemannian curvature as the precedent, and models the ontic bedrock as a hyperdimensional fractal manifold with "gappy" Planck-scale structure; we cite its Riemannian-precedent argument because the torsion conjecture extends exactly that precedent from gravity to quantum mechanics. The Hopf fibration paper [10] documents the Hopf map $S^3 \to S^2$ — decomposing the 3-sphere into circles parameterized by a 2-sphere — as a governing structure behind phenomena from rigid-body kinematics to magnetic-charge quantization; this is the standard topology of the two-level state space whose $K = 3$ parameter count we derive in Section 4.2, and it makes precise why the qubit's geometry is non-trivial. The thermodynamic-viability paper [11] quantifies a "Protection Deficit" of approximately $10^{12}$ between the metabolic efficiency of biological systems and the energy cost of state-of-the-art engineered quantum processors, and argues that "forced" discrete control hits a thermodynamic wall while "geodesic" evolution does not; we cite it in Section 7 for its specific claim that control philosophy, not quantum mechanics, sets the scalability constraint — relevant to how a torsion-based reformulation would or would not change engineering practice.

## 3. Methods

Our method is analytic decomposition of the conjecture into four links, each of which is either derived, formalized, or declared open. We state the links and the tools used on each.

**Link L1 (exchange statistics).** Claim: torsional topology permits only $\pm 1$ exchange symmetries in $3+1$ dimensions. Tool: the double-swap identity for the exchange operator, as written in [2], plus the topology of the exchange path space in three spatial dimensions. We derive the phase restriction from the identity alone and then ask what, if anything, torsion adds.

**Link L2 (state-space dimension).** Claim: Hardy-type continuity axioms force the quadratic state space with $K = N^2$ parameters. Tool: direct counting of the real degrees of freedom of a $d \times d$ Hermitian trace-one matrix, using the density-matrix definition stated in [1]. We resolve the count precisely and reconcile it with the conjecture's $K = N^2$ phrasing.

**Link L3 (angular normalization).** Claim: the $\pi/2$ normalization arises from integrating the Lorentz factor as a Möbius map on the Riemann sphere. Tool: direct evaluation of the integral of the Lorentz factor over its physical domain. We evaluate the integral exactly and note what part of the Möbius/Riemann-sphere claim remains interpretive.

**Link L4 (phase generation).** Claim: the axial component of the Einstein-Cartan torsion tensor reproduces the wavefunction's phase gradient. Tool: the Madelung transformation of the Schrödinger equation, written for a probability current with a torsion coupling, followed by a dimensional consistency check of the identification of the axial torsion vector with the phase gradient. This link we can formalize but not derive; we state the ansatz and its status explicitly.

**Link L5 (torsion lumps as dark matter).** Claim: stable torsion lumps in Einstein-Cartan solutions have the mass spectrum and collisionless dynamics of cold dark matter. Tool: none available within our derivations. We treat this link as an open hypothesis and specify in Section 7 what calculation would begin to test it.

Throughout, every number we report is either computed in Section 4 with shown arithmetic, quoted from a cited work with its stated value, or labeled a projection with stated assumptions. We use natural units $\hbar = c = 1$ except where $\hbar$ is displayed to track dimensions.

## 4. Analysis

### 4.1 Link L1: exchange phases from the double-swap identity

The input is the exchange relation stated in [2]: for a two-particle state $\psi(x_1, x_2)$, exchange acts as

$$\psi(x_2, x_1) = e^{i\varphi}\,\psi(x_1, x_2).$$

Applying the swap a second time returns the original configuration, so

$$\psi(x_1, x_2) = e^{i\varphi}\,\psi(x_2, x_1) = e^{i\varphi}\, e^{i\varphi}\,\psi(x_1, x_2) = e^{2i\varphi}\,\psi(x_1, x_2).$$

For a nonzero state this requires $e^{2i\varphi} = 1$, i.e. $2\varphi = 2\pi k$ for $k \in \mathbb{Z}$, hence

$$\varphi = \pi k, \qquad e^{i\varphi} = (-1)^k \in \{+1, -1\}.$$

The two cases $k$ even and $k$ odd are bosons and fermions. This is the arithmetic [2] presents, and it is the entire content of the exchange restriction at the level of the wavefunction: the square of the exchange operator is the identity, and one-dimensional unitary representations of $\mathbb{Z}_2$ are exactly $\pm 1$.

What this derivation does not fix is why only one-dimensional representations occur in $3+1$ dimensions — in two spatial dimensions, the exchange group is the braid group rather than $\mathbb{Z}_2$, and arbitrary phases $e^{i\theta}$ are allowed (anyons). The torsion conjecture's specific claim is that torsional topology of the exchange path space enforces the $\mathbb{Z}_2$ restriction. Our derivation shows the restriction is already a consequence of the permutation group's structure as stated in [2]; the torsion mechanism would be an explanation of why physical exchange realizes the permutation group rather than the braid group, not an independent derivation of $\pm 1$. We return to this distinction in Section 6.

### 4.2 Link L2: the real parameter count of the quantum state space

The input is the density-matrix definition in [1]: the state of a $d$-dimensional system is a $d \times d$ matrix $\rho$ that is self-adjoint ($\rho^{*} = \rho$), non-negative ($\rho \geq \mathbf{0}$), and normalized ($\mathrm{trace}(\rho) = 1$). Non-negativity is an inequality constraint that does not reduce the dimension of the ambient space, so we count the Hermitian trace-one matrices.

A $d \times d$ Hermitian matrix has real diagonal entries: $d$ real parameters. Its off-diagonal entries satisfy $\rho_{ij} = \rho_{ji}^{*}$ for $i \neq j$, so each conjugate pair $(i,j)$ and $(j,i)$ carries one complex number, i.e. 2 real parameters. The number of pairs with $i < j$ is

$$\binom{d}{2} = \frac{d(d-1)}{2},$$

so the off-diagonal contribution is

$$2 \cdot \frac{d(d-1)}{2} = d(d-1)$$

real parameters. The total for the Hermitian matrix is

$$d + d(d-1) = d^2.$$

The trace constraint $\mathrm{trace}(\rho) = 1$ is one linear equation, removing one parameter:

$$K = d^2 - 1.$$

Check against the $d = 2$ case stated in [1]: $K = 2^2 - 1 = 3$, matching the Bloch vector $(\theta_1, \theta_2, \theta_3)$ with $\theta_1^2 + \theta_2^2 + \theta_3^2 \leq 1$. Further values:

$$K(2) = 3, \qquad K(3) = 9 - 1 = 8, \qquad K(4) = 16 - 1 = 15.$$

The conjecture as stated says "Hardy's continuity axiom forces the $K = N^2$ quadratic state space." Our count gives $K = N^2 - 1$ for normalized states; the $N^2$ figure is recovered if one counts the unnormalized positive matrices (trace unconstrained), or equivalently the cone before normalization. We adopt the convention $K = N^2 - 1$ for physical states and record this as a definitional reconciliation, not a disagreement about substance: both counts describe the same cone, differing by whether the normalization is imposed before or after counting.

The substantive question the conjecture raises is not the count itself — the count is bookkeeping — but whether a continuity axiom can be shown to force the quadratic scaling $K \sim N^2$ rather than, say, a linear simplex $K = N - 1$ (classical probability) or another scaling. That forcing argument is Hardy-type reconstruction machinery of the kind [2] employs operationally; we do not reproduce it here and mark it as the unproven part of L2.

### 4.3 Link L3: the Lorentz-factor integral and the $\pi/2$ normalization

The conjecture claims a $\pi/2$ angular normalization from integrating the Lorentz factor. The Lorentz factor for velocity fraction $\beta = v/c$ is

$$\gamma(\beta) = \frac{1}{\sqrt{1 - \beta^2}}.$$

We evaluate its integral over the full physical subluminal range $\beta \in [0, 1]$:

$$\int_0^1 \frac{d\beta}{\sqrt{1 - \beta^2}} = \left[\arcsin \beta\right]_0^1 = \arcsin(1) - \arcsin(0) = \frac{\pi}{2} - 0 = \frac{\pi}{2}.$$

Numerically,

$$\frac{\pi}{2} \approx 1.5707963.$$

This is the claimed angular normalization: the Lorentz factor, integrated over its physical domain, yields exactly a quarter turn. The conjecture's further claim — that this arises from treating the Lorentz factor as a Möbius map on the Riemann sphere — is consistent with the fact that the substitution $\beta = \sin\theta$ converts the integral to $\int_0^{\pi/2} d\theta$, a quarter of the full circle, but we have not derived the Möbius-map interpretation from independent structure; the exact value $\pi/2$ is the derived content, and the geometric interpretation of why the domain ends at $\beta = 1$ (the light cone) supplying a quarter-turn is the interpretive remainder.

### 4.4 Link L4: the Madelung form and the torsion-phase ansatz

Write the wavefunction in polar form, $\psi = \sqrt{\rho}\, e^{iS/\hbar}$, where $\rho$ is the probability density and $S$ the phase action. The Schrödinger equation $i\hbar\,\partial_t \psi = -\frac{\hbar^2}{2m}\nabla^2 \psi + V\psi$ separates, on substituting the polar form and splitting real and imaginary parts, into

$$\partial_t \rho + \nabla \cdot \left(\rho \frac{\nabla S}{m}\right) = 0,$$

$$\partial_t S + \frac{|\nabla S|^2}{2m} + V + Q = 0, \qquad Q = -\frac{\hbar^2}{2m}\,\frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}}.$$

The first is a continuity equation for the probability current $j = \rho\,\nabla S/m$; the second is a Hamilton-Jacobi equation with the quantum potential $Q$. The phase gradient $\nabla S$ is the velocity field of the probability flow.

The conjecture's L4 claim is that the axial torsion vector of Einstein-Cartan geometry reproduces this phase gradient. In Einstein-Cartan theory the torsion tensor $T^{\lambda}{}_{\mu\nu}$ (the antisymmetric part of the affine connection) has an irreducible axial (trace) part, conventionally

$$A_{\mu} = \epsilon_{\mu\nu\rho\sigma}\, T^{\nu\rho\sigma},$$

a pseudovector with dimension of inverse length. The phase gradient divided by $\hbar$, $\nabla S / \hbar$, also has dimension of inverse length: $S$ has dimension of action (energy $\times$ time), so $\nabla S$ has dimension of momentum, and momentum$/\hbar$ is inverse length. We therefore state the ansatz

$$\frac{\nabla_{\mu} S}{\hbar} \;\overset{?}{=}\; \kappa\, A_{\mu},$$

with $\kappa$ a dimensionless coupling to be fixed by dynamics. Dimensionally the ansatz is consistent: both sides are covectors of dimension inverse length. Substituting into the Madelung current gives a torsion-coupled flow

$$j_{\mu} = \frac{\rho\, \hbar\, \kappa\, A_{\mu}}{m},$$

and the continuity equation becomes a statement that probability flows along the axial torsion field.

This is where the derivation stops. Three things are unproven. First, the proportionality $\nabla_{\mu}S = \hbar\kappa A_{\mu}$ is an ansatz, not a consequence of the Einstein-Cartan field equations; deriving it would require showing that the torsion-coupled action for a spinning fluid reproduces the Schrödinger Lagrangian with the identification forced. Second, the coupling $\kappa$ is undetermined; the conjecture predicts $\kappa$ is fixed (perhaps $\kappa = \pm 1$ or a known constant), but no derivation exists here. Third, in standard Einstein-Cartan matter coupling, torsion is algebraically determined by the spin density of matter and is negligible at laboratory scales; whether a torsion field of the magnitude the ansatz requires can exist without contradicting known torsion bounds is an open question we flag in Section 6 rather than resolve.

### 4.5 Link L5 status

The torsion-lump dark-matter conjecture requires: (i) existence of stable localized Einstein-Cartan solutions, (ii) a mass spectrum, (iii) collisionless dynamics at galactic scales. None of these is derivable from the tools of this paper, and we make no quantitative claim about any of them. We carry the link forward only as a specification of what a future calculation must demonstrate (Section 7).

## 5. Results

We report only numbers derived in Section 4 or quoted from cited works.

**R1 (exchange phases).** From the double-swap identity of [2], the exchange phase satisfies $\varphi = \pi k$, so $e^{i\varphi} = \pm 1$: exactly two statistics in the permutation-group setting (Section 4.1). The torsion conjecture's exchange link is consistent with, but not additionally required by, this arithmetic; the open part is why the exchange group is $\mathbb{Z}_2$ rather than the braid group in $3+1$ dimensions.

**R2 (state-space dimension).** The normalized state space of an $N$-level system carries

$$K = N^2 - 1$$

real parameters, derived from the Hermitian trace-one count in Section 4.2, with values $K = 3, 8, 15$ for $N = 2, 3, 4$, and the $N = 2$ value matching the Bloch-ball parameterization stated in [1]. The conjecture's $K = N^2$ is recovered for the unnormalized cone; the two conventions describe the same structure.

**R3 (angular normalization).** The Lorentz-factor integral over the physical domain evaluates to

$$\int_0^1 \frac{d\beta}{\sqrt{1-\beta^2}} = \frac{\pi}{2} \approx 1.5707963,$$

reproducing the conjecture's claimed $\pi/2$ normalization exactly (Section 4.3).

**R4 (torsion-phase ansatz).** The identification $\nabla_{\mu}S = \hbar\kappa A_{\mu}$ is dimensionally consistent (both sides inverse length) and yields a torsion-coupled probability current $j_{\mu} = \rho\hbar\kappa A_{\mu}/m$, but is not derived from the Einstein-Cartan field equations; the coupling $\kappa$ is undetermined (Section 4.4).

**R5 (hardware context, quoted).** Cloud-accessible superconducting processors of the class reported in [4] — 105 qubits, gate fidelities 99.90% (single-qubit), 99.56% (two-qubit), 98.7% (readout) — exist as an experimental substrate on which statistics-sensitive multi-particle interference experiments could be specified. No torsion-specific prediction for such hardware is derived in this paper.

**R6 (link status table).**

| Link | Claim | Status | Quantitative content |
|---|---|---|---|
| L1 | $\pm 1$ exchange symmetry | Derived from [2]'s identity; torsion's role open | $\varphi = \pi k$ |
| L2 | Quadratic state space | Count derived; forcing argument open | $K = N^2 - 1$; $3, 8, 15$ |
| L3 | $\pi/2$ normalization | Integral derived; Möbius interpretation open | $\pi/2 \approx 1.5707963$ |
| L4 | Torsion generates phase | Ansatz formalized; unproven | Dimensional consistency only |
| L5 | Torsion lumps as dark matter | Open hypothesis | None |

The principal result is the pattern across R1–R4: two of the conjecture's quantitative claims (the exchange restriction and the $\pi/2$ value) are derivable from standard structure without torsion, one (the parameter count) is bookkeeping whose forcing argument remains open, and the central physical claim (torsion generates the phase) is formalizable but unproven. The chain is therefore partially derivable, with L4 as the load-bearing unproven link.

## 6. Discussion

**What the derivations do and do not establish.** R1 and R3 are genuine derivations, but a skeptic should note what they derive from. The exchange restriction follows from the permutation group's structure, which is assumed, not derived; the $\pi/2$ integral follows from the Lorentz factor's functional form, which is special relativity, not torsion. If the conjecture's value is that torsion explains why these structures hold, our derivations do not deliver that value — they deliver the targets that a torsion-based explanation must reach. The strongest honest statement is: the conjecture's numerical claims are correct and reachable, but the derivations we exhibit do not route through torsion.

**The load-bearing link.** L4 carries the conjecture's physical novelty. If $\nabla_{\mu}S = \hbar\kappa A_{\mu}$ cannot be derived from the Einstein-Cartan field equations with a fixed $\kappa$, the conjecture reduces to a restatement of known results (R1–R3) plus an undetermined ansatz. Conversely, a derivation of the ansatz with $\kappa$ fixed would be the first genuinely new content. Our formalization makes this testable by giving the ansatz explicit form.

**Falsification of the main result.** The main result of this paper is the link-status pattern of R6, and specifically the claim that L4 is unproven but formalizable. The observation that would falsify the conjecture's central claim is: a direct computation of the torsion-coupled spinning-fluid action showing that its Euler-Lagrange equations do not close on the Madelung pair (continuity plus Hamilton-Jacobi) for any constant $\kappa$ — i.e., that no dimensionless $\kappa$ makes the ansatz dynamically consistent. The observation that would fals