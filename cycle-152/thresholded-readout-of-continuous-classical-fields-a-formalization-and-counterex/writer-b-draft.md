# Thresholded Readout of Continuous Classical Fields: A Formalization and Counterexample to the Uniqueness Claim for Quantum Mechanics

## Abstract

A family of contemporary foundational programs asserts that reality is a continuum of local deterministic fields and that quantum mechanics is the unique calculus bridging this continuum to discrete measurement outcomes. If that uniqueness claim were correct, research seeking additional physical principles behind quantum statistics could stop; if it is wrong, the specific failure localizes where extra structure must be added. This paper formalizes the proposed bridge as a thresholded amplification map $M:\mathbb{R}\to\mathcal{O}$ and tests uniqueness by construction. Within the axiom class of continuous local deterministic fields plus irreversible discrete readout, we exhibit two distinct calculi — a linear threshold and a quadratic (intensity-like) threshold — that yield detection probabilities $0.1587$ and $0.3174$ respectively for a unit-variance Gaussian field at threshold $\Theta=1$, a structural factor of exactly $2$ that persists at other thresholds. A slope-matched noisy threshold detector with $\sigma_n=\sqrt{2/\pi}\approx0.7978846$ reproduces the two-outcome Born rule only approximately, with maximum deviation $0.1050$ and root-mean-square deviation $0.0602$ over a five-point angular grid. We prove the CHSH bound $|S|\le2$ for every deterministic local thresholded readout, against the quantum prediction $|S|=2\sqrt{2}\approx2.8284$. Uniqueness therefore fails at the level of the readout calculus. A projection shows $\approx130$ trials per setting suffice to distinguish the two calculi experimentally.

## 1. Introduction

Researchers working on classical reconstructions of quantum mechanics — and the reviewers, funders, and technical audiences who must evaluate such programs — currently face an unresolved decision. Several active programs assert that the universe is a continuum of local deterministic fields and that all measurement is an irreversible discrete mapping from a continuous state space to a finite outcome space, implemented by nonlinear amplification and thresholding [8], [10]. Some of these programs go further and claim that quantum mechanics is the logically necessary and unique calculus connecting the two domains. Today there is no shared, explicit procedure for testing that uniqueness claim: the assertions circulate as foundational theses, and acceptance or rejection rests on taste rather than on a computed counterexample or a computed agreement check. The stakes are concrete. If uniqueness holds, any research program hunting for additional physical principles behind quantum statistics (extra variables, selection rules, dynamical postulates) is redundant and should be disbanded. If uniqueness fails, the failure localizes exactly which additional structure a classical ontology must supply — and programs that omit it are making a falsifiable error, not a philosophical choice.

This paper supplies the missing procedure for one precisely stated version of the claim. We take two of the asserted properties as axioms — (i) the underlying state relevant to a detector is a continuous field value evolved by local deterministic dynamics, and (ii) measurement is an irreversible discrete map $\mathbb{R}\to\mathcal{O}$ realized by nonlinear amplification and thresholding — and we treat uniqueness as a falsifiable hypothesis about the class of calculi these axioms define. A *calculus* here means a rule assigning outcome probabilities to each outcome in $\mathcal{O}$ given the continuous field state. The test is direct: exhibit two members of the class that both satisfy the axioms and compute whether they agree. If they disagree, uniqueness fails, and the form of quantum statistics must come from structure beyond the axioms.

The strategy is falsificationist in both directions. If a thresholded classical map reproduced quantum statistics exactly and were the only calculus consistent with the axioms, uniqueness would be supported. If instead a second consistent calculus exists, or if the thresholded map fails to reproduce quantum statistics, uniqueness is refuted. We find the latter, and we localize the failure precisely: the thresholded map matches the Born rule only in a central regime and cannot match it at the certainty points, and no deterministic local thresholded model can violate the CHSH inequality.

The result bears on real programs, not straw men. The Post-Quantum Synthesis program states a no-collapse theorem in which a threshold crossing within the detector produces the discrete outcome during continuous Hamiltonian evolution [10], and it derives joint measurement statistics for entangled systems as $P(o_1,o_2)=\sum_i |c_i|^2 P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)$ [10]. The Continuum-is-Real program states that the universe is not quantized but our interaction with it is, through a binning mechanism [8]. Both programs therefore commit to exactly the axiom class formalized here, and both inherit whatever statistics that class actually produces. Our computations show the class produces statistics that are internally consistent but empirically distinguishable from quantum mechanics — so the programs must either add a selection principle or accept divergent predictions.

Our contributions are:

1. An explicit two-calculus counterexample: linear and quadratic thresholded amplifiers, both satisfying the axioms exactly, yield detection probabilities $P_1^{(L)}=0.1587$ and $P_1^{(Q)}=0.3174$ for a unit-variance Gaussian field at $\Theta=1$, a structural factor of exactly $2$ that persists at $\Theta=4$ (Sections 4.1–4.3, 4.8).
2. A quantitative bound on Born-rule reproduction: the best locally slope-matched noisy threshold detector, with $\sigma_n=\sqrt{2/\pi}\approx0.7978846$, deviates from the Born rule by up to $0.1050$ (at $\alpha=0$, where certainty is demanded) with root-mean-square deviation $0.0602$ over a five-point angular grid, and the deviation at certainty points is structural for any finite noise (Section 4.4).
3. A proof that every deterministic local thresholded readout obeys $|S|\le2$ for the CHSH combination, against the quantum prediction $|S|=2\sqrt{2}\approx2.8284$ at standard angles, with a demonstration that readout noise cannot close the gap (Sections 4.5–4.6).
4. A statistical power projection, labeled as such, that approximately $130$ trials per calculus suffice for a $3\sigma$ experimental discrimination between the two calculi under stated assumptions (Section 4.7).

## 2. Background and Related Work

The proposed ontology sits at the intersection of classical continuum modeling, axiomatic measurement theory, continuous-time quantum measurement, and contemporary classical-reconstruction programs. We review each connection using specific results from the works themselves.

**Continuous-time quantum measurement as the standard bridge.** The stochastic Schrödinger equation, of classical or quantum type, describes open quantum systems under measurement in continuous time, and the review [1] establishes that two formulations of quantum continuous measurement — one based on the Hudson-Parthasarathy equation and quantum stochastic calculus, the other on the SSE, the stochastic master equation, and conditional states — are equivalent, so that output spectra can be deduced from either the classical SSE or the quantum one, with Heisenberg-type bounds on the spectra of incompatible quadratures holding independently of the formulation. The review concludes from this equivalence that the "classical" SSE is not a semiclassical approximation to some quantum theory but is itself fully quantum [1]. This is the standard against which any proposed classical bridge must be measured: in the accepted calculus, the continuous description and the discrete record are connected through Hilbert-space structure, not through a threshold on a classical field amplitude. Our model inverts the direction of explanation — we ask whether a classical continuous process plus thresholding can generate quantum statistics — and Section 4 shows it cannot do so exactly.

**Axiomatic measurement theory.** The axiomatic approach of [3] characterizes all the possible statistical properties of apparatuses measuring an observable with nondegenerate spectrum allowed in standard quantum mechanics, treating an apparatus as inputting a state $\rho$ and outputting a classical outcome ${\bf x}$ together with the conditional state $\rho_{\{{\bf x}=x\}}$, with the statistical property consisting of the output distribution and the state reduction. The same work notes that the conventional description via the Born statistical formula and the projection postulate is much more restrictive than what quantum mechanics allows [3]. This supplies the quantum-side target set: any candidate calculus claiming to be *the* bridge must land inside the characterized set of apparatus statistics, and our counterexample calculus of Section 4.3 lands outside the quantum member of that set while remaining inside the proposed axiom class.

**Instruments, POVMs, and classical SDEs.** The theory of quantum continual measurements has been formulated using instruments and positive operator valued measures, using quantum stochastic differential equations, and using classical stochastic differential equations for vectors in Hilbert spaces or for trace-class operators [4]. Within this framework, a continual measurement is called quasi-complete when the a posteriori states are pure for every pure initial state, and a theorem quoted there establishes that the continual measurement is quasi-complete if and only if $\mathcal{L}_1=0$ and $J_k[\rho]/\mathop{\mathrm{Tr}}\{J_k[\rho]\}$ is a pure state for every $k$ and every pure state $\rho$ [4]. The relevance is structural: even when classical SDEs appear in the quantum formulation, they are SDEs for Hilbert-space objects, and the information-gain analysis runs through a posteriori states. Our thresholded map has no a posteriori state and no information-gain monotonicity; the contrast marks exactly what the proposed axioms omit.

**Realist unification programs.** The realist psychobiological interpretation of [2] proposes a quantum mechanical/biological dualism in which the methods of the quantum physicist and of the biological sciences are two alternative modes of description that supplement each other, with a proposed correspondence including collapse of the state vector mapped to a decision process and the measuring instrument mapped to structures which determine and regulate signals or forms [2]. This is a precedent for treating the link between an underlying reality and the quantum description as a mapping whose form requires independent justification — the interpretive move our formalization makes precise. Our result sharpens the precedent: the mapping's form is not merely underdetermined philosophically; within the proposed axiom class it is empirically underdetermined, with distinct members giving distinct statistics.

**Protective measurement and the continuous substrate.** The analysis of protective measurement in [6] derives the final system–apparatus state to first order in $1/T$ beyond the zeroth-order limit usually considered, and shows that the finite system–apparatus entanglement arising in a protective measurement entails that protective measurements can never transcend the irreducibly probabilistic element inherent in any measurement of an unknown quantum state; the readout itself cannot tell us whether information about the initial state has actually been obtained [6]. The same work raises the scaling problem of how the number of protective measurements required to reconstruct a wave function grows with system size, noting the exponential number required for multi-qubit states [6]. This removes one route by which the continuous wavefunction itself could be taken as directly measured, reinforcing the need for an explicit readout map between whatever continuous substrate is posited and the discrete record — the object we formalize in Section 3.

**Locality of discrete transition structure.** The foundations of quantum Turing machines in [7] characterize the local transition functions for fully general quantum Turing machines, requiring that only a finite system be in motion during any one step, that the motion depend only on the state of a finite subsystem, and that the rule specifying the motion be finitely given; the transition matrix elements take the local product form over the tape cells with nearest-neighbor head moves, and a halting protocol is proposed that works without augmenting the halting qubit and without spoiling the computation [7]. This demonstrates that locality constraints on discrete transition rules sitting on a quantum substrate are formally tractable. Our CHSH derivation in Section 4.5 imposes the analogous locality on classical readout functions $A(a,\lambda)$, $B(b,\lambda)$, and the tractability precedent supports the well-posedness of that constraint.

**Continuous-to-discrete mapping outside physics.** In virtual reality, self-avatars enhance presence and embodiment, and whether one uses a complex motion capture solution or a few trackers with inverse kinematics, the pipeline maps continuous tracked signals onto a discrete skeleton structure through a fixed adjustment procedure [5]. This is an engineering instance of the abstract operation the proposed axioms posit — irreversible discretization of a continuous signal — and it illustrates that the discretization step alone carries no quantum statistics; the statistics come from the ensemble distribution and the amplifier shape, which is exactly the degree of freedom our counterexample exploits.

**The programs under test.** The Continuum-is-Real program argues that the ontological crisis in physics stems from mistaking observational artifacts for fundamental properties, that the universe is not fundamentally quantized but our interaction with it is, and it resolves discreteness through a universal binning mechanism, reinterpreting quantum jumps and entanglement as informational phenomena related to the observation of a continuous field [8]. The Post-Quantum Synthesis program formalizes this with theorems: a no-physical-collapse theorem in which the continuous field triggers a threshold crossing within the detector leading to a discrete outcome while the physical state evolves continuously throughout [10]; a no-spooky-action theorem showing that a local unitary on one system leaves the marginal physical state of the spatially separated system unchanged [10]; a correlation-history theorem giving joint measurement statistics $P(o_1,o_2)=\sum_i |c_i|^2 P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)$ from coefficients $c_i$ established during the initial interaction [10]; and a redundancy-threshold theorem with $P_{\text{error}}\le e^{-N\gamma}$ and $N_0=\frac{1}{\gamma}\log\frac{1}{\epsilon}$ [10]. The audit record of this program additionally derives the Born rule as a theorem of epistemic consistency via Gleason's theorem, under non-negativity, normalization, and non-contextuality of the probability assignment, and explains which-path detection as a physical interaction that inevitably disturbs the continuous field followed by a Bayesian update of the observer's knowledge state [9]. Two points connect directly to our analysis. First, the threshold crossing in the amplification stage of [10] is precisely the readout map we formalize; second, the correlation formula of [10] is a mixture over shared-history coefficients, which is a local hidden-variable form, and Section 4.5 shows every such local form obeys $|S|\le2$ — so the program's own correlation theorem cannot reproduce the quantum value $2\sqrt{2}$ at the standard angles.

**Epistemic framing.** The map-territory distinction — that representational models differ from their source and that confusing the representation with the referenced entity leads to categorical errors — and the observation that self-reference is a structural condition of inquiry rather than a procedural obstacle [11] frame what a "bridging calculus" is: a map from continuous reality to discrete records, not the reality itself. Our formalization treats the calculus as exactly such a map and asks whether the axioms fix it uniquely; they do not.

No work in this literature derives the Born rule from a classical thresholding map on a classical field, and none exhibits a second calculus within the proposed axiom class. That is the gap this paper fills.

## 3. Methods

### 3.1 Axioms

We formalize the proposed ontology as three axioms on a measurement event.

- **A1 (Continuous substrate).** The state of the world relevant to a detector at any time is a field value $x\in\mathbb{R}$ (one-dimensional; the extension to fields on $\mathbb{R}^n$ is not needed for the results).
- **A2 (Local determinism).** The evolution $x(t)$ is generated by a local deterministic law; a detector's outcome depends only on its local setting and the local field value, never on distant settings or distant outcomes.
- **A3 (Irreversible discrete readout).** A measurement is a map $M:\mathbb{R}\to\mathcal{O}$ with $\mathcal{O}$ finite, implemented by nonlinear amplification followed by thresholding, and irreversible: the pre-threshold value is not recoverable from the outcome.

These axioms are a faithful formalization of the programs under test: the amplification-and-threshold-crossing stage of the no-collapse theorem in [10] is A3, and the locality of physical influence in its no-spooky-action theorem [10] is A2.

### 3.2 The readout map

A measurement device is a triple $(\mathcal{A},g,\Theta)$ where $\mathcal{A}$ is an amplifier acting on the continuous field variable $x\in\mathbb{R}$, $g>0$ is a gain, and $\Theta$ is a threshold. The amplifier produces an intermediate variable

$$y=\mathcal{A}_g(x),$$

and the readout map $M_\Theta:\mathbb{R}\to\mathcal{O}=\{0,1\}$ for a two-outcome detector is the step function

$$M_\Theta(y)=\begin{cases}1 & \text{if } y\ge\Theta,\\ 0 & \text{if } y<\Theta.\end{cases}$$

Irreversibility enters because $M_\Theta$ is many-to-one: the preimage of outcome $1$ is the set $\{x:\mathcal{A}_g(x)\ge\Theta\}$, and all continuous information within that set is discarded.

### 3.3 Candidate calculi

Within A1–A3 we define two calculi, each a complete rule assigning outcome probabilities to field ensembles:

- **Linear calculus ($\mathcal{C}_L$):** $\mathcal{A}_g(x)=g\,x$, so outcome $1$ occurs iff $x\ge\Theta/g$.
- **Quadratic calculus ($\mathcal{C}_Q$):** $\mathcal{A}_g(x)=g\,x^2$, so outcome $1$ occurs iff $|x|\ge\sqrt{\Theta/g}$; the amplifier is insensitive to sign, as intensity-like detectors are.

Both calculi satisfy the axioms exactly: the substrate is continuous, local, and deterministic; the readout is discrete, irreversible, and produced by amplification and thresholding. The quadratic amplifier is nonlinear in the stronger sense of the programs' wording; the linear amplifier is the degenerate affine member of the family, included as the minimal baseline. Section 6 discusses the reading on which the affine member is excluded.

### 3.4 Field ensemble

Over an ensemble of nominally identical preparation runs, the field value at the detector is distributed as a unit-variance Gaussian,

$$p(x)=\frac{1}{\sqrt{2\pi}}\,e^{-x^2/2},$$

in dimensionless units. This is the minimal nontrivial ensemble: symmetric, continuous, and normalizable. No quantum postulate is used at this stage; $p(x)$ is the ensemble distribution of the classical field amplitude. We write $\Phi(z)=\int_{-\infty}^{z}p(u)\,du$ for the standard normal cumulative distribution function.

For the Born-rule comparison we use the noisy threshold map with additive readout noise $\eta\sim\mathcal{N}(0,\sigma_n^2)$:

$$M_\theta(x)=\mathbf{1}\{x+\eta>\theta\},\qquad P(1\mid x)=\Phi\!\left(\frac{x-\theta}{\sigma_n}\right).$$

### 3.5 Target statistics and locality test

The quantum predictions to be tested are:

- **Born rule (two-outcome, single parameter).** For a qubit-like system prepared at angle $\alpha$ relative to the detector basis, $P_1^{\mathrm{QM}}(\alpha)=\cos^2(\alpha/2)=\frac{1+\cos\alpha}{2}$.
- **CHSH correlation.** For two parties with settings $a,a'$ and $b,b'$, the quantum correlation for a singlet-type state is $E_{\mathrm{QM}}(a,b)=-\cos(a-b)$, and the CHSH combination is $S=E(a,b)+E(a,b')+E(a',b)-E(a',b')$.

For the CHSH test, two spatially separated detectors each implement a factorized readout: detector $A$ outputs $A(a,\lambda)\in\{\pm1\}$ as a deterministic function of its local setting $a$ and the local field configuration $\lambda$, and detector $B$ outputs $B(b,\lambda)\in\{\pm1\}$ similarly, with no dependence of $A$ on $b$ or of $B$ on $a$. The correlation is

$$E(a,b)=\int\rho(\lambda)\,A(a,\lambda)\,B(b,\lambda)\,d\lambda,$$

where $\rho(\lambda)$ is the distribution of the shared field configuration. This factorized form is the direct classical analogue of the correlation-history structure $P(o_1,o_2)=\sum_i|c_i|^2P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)$ of [10]: both are mixtures over shared past variables with locally conditioned outcomes.

## 4. Analysis

All numbers in this section are computed explicitly from the inputs stated above; no simulation or external data are used. The only external numerical inputs are tabulated values of the standard normal integral, $\Phi(1)=0.8413$ and $\Phi(2)=0.9772$, and the mathematical constants $\sqrt{2}\approx1.4142136$ and $\sqrt{\pi}\approx1.7724539$.

### 4.1 Outcome probability under the quadratic calculus

With gain $g=1$ and threshold $\Theta=1$, the quadratic calculus fires when $|x|\ge\sqrt{\Theta/g}=\sqrt{1}=1$. The detection probability is

$$P_1^{(Q)}=\int_{-\infty}^{-1}p(x)\,dx+\int_{1}^{\infty}p(x)\,dx=2\int_{1}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\,dx=2\bigl(1-\Phi(1)\bigr).$$

Using $\Phi(1)=0.8413$:

$$P_1^{(Q)}=2(1-0.8413)=2\times0.1587=0.3174.$$

### 4.2 Outcome probability under the linear calculus

With the same $g=1$, $\Theta=1$, the linear calculus fires when $x\ge\Theta/g=1$:

$$P_1^{(L)}=\int_{1}^{\infty}p(x)\,dx=1-\Phi(1)=1-0.8413=0.1587.$$

### 4.3 Divergence between the calculi

The two calculi, both satisfying A1–A3 exactly, give

$$\Delta P=P_1^{(Q)}-P_1^{(L)}=0.3174-0.1587=0.1587,$$

with ratio

$$\frac{P_1^{(Q)}}{P_1^{(L)}}=\frac{0.3174}{0.1587}\approx2.000.$$

The factor of $2$ is structural, not coincidental. For any symmetric density, the quadratic threshold counts both tails while the linear threshold counts one, so analytically $P_1^{(Q)}=2\bigl(1-\Phi(\Theta/g)\bigr)$ while $P_1^{(L)}=1-\Phi(\Theta/g)$, and the ratio is exactly $2$; the rounded tabulated inputs give $0.3174/0.1587\approx1.9994$, which rounds to $2.000$. Both calculi are internally consistent, deterministic at the field level, and produce irreversible discrete records. Therefore the calculus connecting continuous reality to discrete outcomes is **not unique** within the axiom class; uniqueness fails unless an additional principle selects the amplifier.

### 4.4 Born-rule approximation by a slope-matched threshold detector

We now ask how well the best locally calibrated noisy threshold detector matches the Born rule. We posit the most favorable linear encoding of the preparation angle into the field amplitude, $x(\alpha)=\cos\alpha$, a threshold $\theta=0$, and readout noise scale $\sigma_n$. The model's outcome probability is