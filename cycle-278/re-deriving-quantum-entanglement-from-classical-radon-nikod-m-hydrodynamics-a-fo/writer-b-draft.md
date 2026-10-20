# Re-Deriving Quantum Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Analysis of the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) conjectures that standard quantum mechanics, including multi-particle entangled states such as the Greenberger–Horne–Zeilinger (GHZ) state, can be axiomatically re-grounded in classical measure theory: wavefunctions are interpreted as Radon–Nikodým densities that relax into basins of attraction of classical probability measures under a local hydrodynamic transport, restoring local realism without superdeterminism. The open gap is that no explicit derivation of GHZ-type Bell-violating correlations from classical measure-theoretic axioms has been produced, and no analysis has tested whether the hypothesis's own published formal machinery survives such a derivation. We state the hypothesis as four explicit axioms (classical probability space, local state variables, local continuous transport, free measurement settings) and attempt the derivation. We show with full arithmetic that the axioms force the pointwise product constraint $P_1 P_2 P_3 P_4 = +1$ on the four GHZ triple correlations, while the quantum stabilizer values require $-1$; the Mermin expression reaches $M_{\mathrm{Q}} = 4$ against the classical bound $M_{\mathrm{LHV}} = 2$, a violation factor of $2$, and a CHSH cross-check gives $2\sqrt{2} \approx 2.828427$ against the bound $2$. We further show that the correlation-history theorem of the related Post-Quantum Synthesis framework is a convex mixture of local models and is therefore confined to $|S| \le 2$ by the same algebra. The strong form of the hypothesis is falsified. As labeled projections we compute the propagation timescales ($t_{\min} = 3.333333 \times 10^{-12}\ \mathrm{s}$ at millimeter separation) that the hypothesis's proposed particle-tracking tests must resolve.

## 1. Introduction

Engineers designing quantum networks today must treat multipartite entanglement as a scarce physical resource: distributing it between distant nodes is the explicit goal of quantum-internet architectures, and algorithms for optimizing its distribution over noisy links are an active engineering problem [2]. If entanglement were instead derivable from classical probability theory — if the GHZ state were nothing but a particular Radon–Nikodým density relaxing into an attracting basin of a classical measure — the resource accounting underlying these network designs, the entanglement-distribution algorithms, and the entanglement-concentration protocols built around maximally entangled states [6] would need to be rethought from the ground up. That is the practical stake of the Hydrodynamic Stability Hypothesis (HSH).

HSH is documented as a concrete research program [10]. It identifies a "chronological fallacy" in quantum foundations — the axiomatization of quantum mechanics by von Neumann in 1932 predated the rigorous formulation of classical probability by Kolmogorov in 1933 — and proposes a hybrid continuous-attractor model in which "the system *is* a continuous fluid (Kolmogorovian/Madelung), but it *appears* discrete (von Neumann) because we only observe it after it has settled into stable resonant modes (attractors) driven by the act of observation" [10]. The hypothesis is local: apparent instantaneous state changes across spatial barriers are supposed to be accompanied by continuous local wave propagation, and the program explicitly calls for sub-femtosecond particle-tracking simulations and a weak-energy-tomography experiment on a hydrogen superposition as decisive tests [10].

If HSH is correct, locality is restored without superdeterminism, contradicting the mainstream reading of Bell-type analyses. If it is wrong, the failure should be demonstrable without any new experiment — purely from the hypothesis's own classical measure-theoretic language. That is the test this paper performs. The decision that changes with the result is a researcher's decision about where to invest effort: whether to attempt a classical re-derivation of entangled statistics, or to accept that any such derivation must abandon locality of the response functions and therefore collapse into a position indistinguishable from existing non-local interpretations.

Our method is deliberately adversarial to the hypothesis. We (i) write down the minimal axiom set that any classical Radon–Nikodým hydrodynamic re-grounding must satisfy, (ii) attempt an explicit derivation of the GHZ state and its measurement correlations from those axioms alone, and (iii) show that the derivation reaches a fork: either the model introduces variables that correlate spacelike-separated outcomes directly, abandoning locality, or it contradicts the quantum predictions it was supposed to re-derive. We execute the fork quantitatively with the Mermin GHZ argument and a CHSH cross-check, all arithmetic shown, and we extend the argument to the published correlation theorem of the Post-Quantum Synthesis (PQS) framework [11], which is a concrete instance of the model class HSH requires. Finally, we give a projection analysis — clearly labeled, with stated assumptions — of the sub-femtosecond particle-tracking simulation program that the hypothesis proposes as a complementary test [10].

The contributions are:

- An explicit axiomatization (A1–A4) of the strong form of HSH, checked against the hypothesis's own published description of its hybrid continuous-attractor model (Section 3.1).
- A derivation, with fully shown arithmetic, that A1–A4 force the pointwise product $P_1 P_2 P_3 P_4 = +1$ on the four GHZ triple correlations, contradicting the quantum stabilizer values whose product is $-1$ (Section 4.2).
- The Mermin bound $M_{\mathrm{LHV}} = 2$ versus the quantum value $M_{\mathrm{Q}} = 4$, a violation factor of $2$, with a CHSH cross-check giving $2\sqrt{2} \approx 2.828427$ versus the classical bound $2$ (Sections 4.3 and 4.4).
- A new result: the PQS correlation-history theorem [11] is a convex mixture of factorized local models, and the CHSH functional of any such mixture is bounded by $2$ by an explicit convexity argument (Section 4.5).
- Labeled projections of the propagation timescales ($t_{\min} = 3.333333 \times 10^{-12}\ \mathrm{s}$ for a $1.0 \times 10^{-3}\ \mathrm{m}$ barrier; $3.333333 \times 10^{-9}\ \mathrm{s}$ for $1.0\ \mathrm{m}$) that the hypothesis's particle-tracking program must resolve (Section 4.6).

## 2. Background and Related Work

We review the literature in five strands. Every statement about a work below is restricted to what the work's own text states.

**Entanglement as an ensemble-statistical phenomenon.** The central philosophy of the hybrid-circuit literature is drawn from statistical mechanics and random-matrix theory: while individual instances of complex quantum circuits are essentially intractable to simulate, the statistical properties of random ensembles obey simple universal laws, and this philosophy is applied to the dynamics of quantum information in ideal and noisy quantum circuits [1]. The same work maps measurement-resolved circuit dynamics onto a classical statistical-mechanics model: imposing different boundary conditions yields partition functions $Z_A$ and $Z_0$ from which the averaged Rényi entropy is obtained in the replica limit, and the mapping establishes the existence of an entanglement transition through convergence of strong- and weak-coupling expansions [1]. This is the strongest known sense in which a classical statistical-mechanical substrate reproduces quantum-information phenomenology — and it is crucially an ensemble-level, not a single-trajectory, description. A Radon–Nikodým measure is likewise an ensemble object, so any classical hydrodynamic re-grounding of quantum mechanics must live at exactly this level of description; our axiom set in Section 3 is phrased accordingly.

**Multipartite entanglement as an engineered resource.** A quantum internet aims at distributing bipartite entanglement between distant nodes, but multipartite entanglement between nodes may empower it for additional or better applications in communications, sensing, and computation; an algorithm has been presented for generating multipartite entanglement between distributed nodes over a noisy network modeled as a graph with noisy quantum links and quantum memories, with the fidelity of the final state and the rate of distribution computed as the necessary metrics [2]. The same work shows the algorithm remains optimal under a star-scheme when links may be used more than once [2]. Separately, hybrid entangled states — entanglement between different degrees of freedom — enable quantum computational and communication tasks with fewer resources, and maximally entangled states are required for unit-success deterministic teleportation; because a maximally entangled state degrades through interaction with the surroundings, entanglement concentration protocols are needed to extract it before use, and one has been proposed for the Omega-type hybrid state using single- and two-mode superpositions of coherent states [6]. Together [2] and [6] establish that GHZ-type multipartite entanglement is an operational, technologically targeted resource with quantified fidelity and rate metrics; any re-grounding of quantum mechanics must reproduce it exactly, which is the target of our Section 4.

**The classical–quantum boundary from the quantum side.** Seventy-five years after Schrödinger coined "entanglement" — his phrase, quoted in [3], was that it is "the characteristic trait of quantum mechanics, the one that enforces its entire departure from classical lines of thought" — the connection between quantum and classical mechanics remains an open problem, and in semiclassical systems there is no classical quantity corresponding to entanglement, so a well-defined classical version of the entanglement rate cannot be computed except perhaps in a weak-coupling regime where exact semiclassical expansions are analytic [3]. From the decoherence side, three classical pre-quantum paradigms for particles — the material point, the test-particle, and the diluted particle (droplet model) — are identified as limit cases of a quantum regime in which pairs of particles interact without getting entangled, an entanglement-free regime connected to the Quantum Darwinist environment-induced superselection principle, under which coherent states emerge as classical pointer states maximizing Shannon–von Neumann information [5]. These two works study how classicality emerges from quantum mechanics; HSH claims the reverse reduction. Notably, [5] shows that the classical limit is reached only through an entanglement-*free* interaction regime — the boundary cases where entanglement disappears are exactly where classical descriptions succeed — which is consistent with our finding that the entangled sector resists classical re-derivation.

**GHZ dynamics under classical environments.** The dynamics of entanglement and coherence have been analyzed for three non-interacting qubits initially prepared as a maximally entangled GHZ-like state coupled with independent classical environments, using an entanglement witness $E(t) = -\mathrm{Tr}[\mathbb{W}_o \rho_{abc}(t)]$ with $\mathbb{W}_o = \tfrac{1}{2}I - \rho_o$, across four noisy external-field models (pure power-law, pure fractional Gaussian, power-law maximized, and fractional Gaussian maximized), with final density matrices computed by ensemble averages over the stochastic process [4]. The reported result is that dephasing effects on tripartite non-local correlation and coherence are fundamentally different in pure and mixed noisy configurations, with power-law noise more damaging in the mixed condition than in the pure case [4]. This is the closest antecedent to HSH's program, because it couples a GHZ state to explicitly classical noise; but the classical environments enter as stochastic external fields degrading a quantum state, not as a substrate replacing the quantum formalism. The entanglement is still detected and quantified with quantum witnesses. HSH claims something far stronger: that the GHZ state itself is a classical measure-theoretic object.

**Classical–quantum interpolation programs.** A unified formulation has been constructed that treats a classical system and its quantum version as limits of a single action functional, with the goal of a continuous passage between the strictly classical and the strictly quantized state; its central technical difficulty is that promoting arbitrary classical variables $(p,q)$ to operators $(P,Q)$ generally changes the Hamiltonian, $\overline{H}(\overline{P},\overline{Q}) \neq H(P,Q)$, so a procedure is needed to select the favored variables whose promotion yields the correct quantum operators [8]. In the algorithmic domain, the scaling of the $\alpha$-QPE family of phase-estimation algorithms — for which a continuous trade-off exists between quantum speedup and circuit depth — has been derived within a classical–quantum framework using quantum singular value transformations, with the interpolating parameter $\alpha$ related to the approximation parameters by $\eta + \tfrac{1}{2}\delta^{\alpha} = 1$ [7]. Both [7] and [8] interpolate between fixed classical and fixed quantum formalisms; HSH is more radical, claiming the quantum formalism is derivable from the classical one. Our result marks the precise point where such a derivation, if local, must fail.

**The hypothesis under test and its neighboring programs.** The HSH paper itself [10] argues from a "chronological fallacy" (von Neumann's 1932 axiomatization predating Kolmogorov's 1933 classical probability), summarizes its hybrid model as unifying the continuous ontology of the Schrödinger equation with the discrete phenomenology of the spectral theorem via dynamical stability, and cites three converging lines of evidence: a Kolmogorovian reconstruction proving a classical probability space can host quantum phenomena without contradiction, experimental observation of continuous trajectories between eigenstates in superconducting circuits, and Bohmian-trajectory reproduction of high-harmonic generation spectra [10]. It issues a call for weak energy tomography on a hydrogen superposition, predicting a continuous energy distribution whose observation "must" force abandonment of the spectral theorem [10]. The related PQS framework [11] proves a set of theorems directly relevant here: a no-physical-collapse theorem (measurement is continuous Hamiltonian evolution; only the observer's density operator changes), a no-spooky-action theorem (a local unitary on one system leaves the spacelike-separated marginal unchanged), a correlation-history theorem giving joint statistics as $P(o_1, o_2) = \sum_i |c_i|^2 P_1(o_1|\phi_1^i) P_2(o_2|\phi_2^i)$ with correlations arising from coefficients "established during the initial interaction," and a redundancy-threshold theorem with $P_{\mathrm{error}} \le e^{-N\gamma}$ and $N_0 = \frac{1}{\gamma}\log\frac{1}{\epsilon}$ [11]. The PQS audit record [12] additionally derives the Born rule from rational-consistency conditions via Gleason's theorem, with non-contextuality of probabilities as a required condition, and explains which-path measurements as physical disturbance plus Bayesian update of an epistemic state [12]. A prior falsification analysis of HSH [9] formalized the hypothesis as four axioms and derived the Mermin contradiction; this paper re-derives that result with full arithmetic, extends it to the PQS correlation theorem, and adds the timescale projections for the simulation program the hypothesis itself proposes.

## 3. Methods

### 3.1 Axiomatization of the hypothesis

We formalize the strong form of HSH as four axioms, chosen to be generous: each is the weakest assumption the hypothesis's own description requires. Let $(\Lambda, \mathcal{F}, \mu)$ be a classical probability space, with $\Lambda$ a configuration space of hidden classical states $\lambda \in \Lambda$.

- **(A1) Classical measure grounding.** Every quantum state corresponds to a measure $\mu_\psi \ll \mu$ with Radon–Nikodým derivative $\rho_\psi = \frac{d\mu_\psi}{d\mu}$, such that all quantum predictions are recoverable as functionals of $\rho_\psi$.
- **(A2) Local state variables.** For $N$ spatially separated parties, the configuration decomposes as $\lambda = (\lambda_1, \ldots, \lambda_N)$ with $\lambda_i \in \Lambda_i$, and each party's outcome is a local function $A_i = f_i(\lambda_i, s_i)$ of its own variable and its own setting $s_i$.
- **(A3) Local continuous transport.** The time evolution $\mu_t = (\Phi_t)_* \mu_0$ is generated by a local flow $\Phi_t$ on $\Lambda$ propagating information at finite speed $v_{\max}$, so that no influence connects spacelike-separated events; preparation and measurement correspond to relaxation into basins of attraction $\mathcal{B}_k \subset \Lambda$ of stable measures, the observed outcome indexing the basin.
- **(A4) Free settings.** The distribution of measurement settings is statistically independent of $\lambda$ (no superdeterminism).

This axiomatization is faithful to the hypothesis's own published description in the following sense. The hybrid model of [10] states that the system is a continuous Kolmogorovian fluid whose discrete appearance arises from settling into stable resonant modes (attractors) under observation — this is A1 (classical probability grounding) plus the basin-relaxation clause of A3. The hypothesis's locality commitment — that apparent instantaneous changes are accompanied by continuous local wave propagation [10] — is A3's finite-speed clause, and the related PQS no-spooky-action theorem [11] is the corresponding statement at the level of response functions, which is A2. The hypothesis explicitly disavows superdeterminism, which is A4. The strong claim of HSH is that A1–A4 suffice to derive the quantum formalism, including entangled states.

### 3.2 Falsification protocol

Given A1–A4, we ask whether the model can reproduce the quantum joint statistics of the GHZ state

$$|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|000\rangle + |111\rangle\bigr)$$

under local Pauli measurements $X$ and $Y$ on each of the three qubits. The protocol is: (i) derive the classical constraint that A1–A4 impose on the four relevant triple correlations, (ii) compute the quantum values of those same correlations from the GHZ state, and (iii) compare. Any mismatch falsifies the strong form, because the hypothesis claims to re-derive the quantum statistics from the classical axioms. This is a derivation-and-contradiction analysis, not a numerical simulation; the complementary simulation target is specified as a projection in Section 4.6.

### 3.3 Extension protocol for the PQS correlation theorem

The PQS framework publishes an explicit formula for entangled-system statistics [11], Theorem 8.2. We test whether that formula, taken as the response-function structure of a concrete model in the HSH class, can violate a Bell inequality. The method is: (i) recognize the structure of the formula as a convex mixture of factorized local models, (ii) prove the CHSH functional of any such mixture is bounded by $2$ by convexity, and (iii) compare with the quantum maximum. This targets the published mathematics of the neighboring program rather than an invented model.

### 3.4 Simulation projection protocol

The complementary test proposed by the hypothesis is sub-femtosecond particle tracking of the hydrodynamic transport $\Phi_t$, to check whether apparent instantaneous state changes across spatial barriers are accompanied by continuous local wave propagation [10]. We compute, as labeled projections with stated assumptions, the propagation timescales such a simulation must resolve for the hypothesis's locality claim to be checked.

## 4. Analysis

### 4.1 Quantum correlations of the GHZ state (inputs and derivation)

**Input 1 (explicit assumption, not sourced).** We take the GHZ state to be $|\mathrm{GHZ}\rangle = (|000\rangle + |111\rangle)/\sqrt{2}$. The work [4] analyzes a maximally entangled GHZ-like state of three qubits but does not state the explicit superposition in its text; the formula above is therefore adopted here as a working assumption of the analysis, not as a claim derived from the cited literature.

**Input 2 (explicit assumption, not sourced).** We assume the Pauli operators $X$ and $Y$ each have eigenvalues $\pm 1$. No cited work states this; it is taken as a standard assumption of the quantum formalism under test.

**Step 1: action of Pauli strings on GHZ.** Using $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$, $Y|0\rangle = i|1\rangle$, $Y|1\rangle = -i|0\rangle$:

$$XXX\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|111\rangle + |000\rangle\bigr) = +|\mathrm{GHZ}\rangle,$$

$$XYY\,|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl((i)(i)|011\rangle + (-i)(-i)|100\rangle\bigr) = \frac{1}{\sqrt{2}}\bigl(i^2|011\rangle + (-i)^2|100\rangle\bigr) = \frac{1}{\sqrt{2}}\bigl(-|011\rangle - |100\rangle\bigr) = -|\mathrm{GHZ}\rangle,$$

and identically for $YXY$ and $YYX$ by symmetry of the GHZ state under qubit exchange.

**Step 2: quantum triple products.** Since $XXX\,|\mathrm{GHZ}\rangle = |\mathrm{GHZ}\rangle$, the product of the three outcomes for settings $(X,X,X)$ is deterministically

$$\langle XXX \rangle_Q = +1.$$

Since $XYY$, $YXY$, $YYX$ each act as $-1$ on $|\mathrm{GHZ}\rangle$,

$$\langle XYY \rangle_Q = \langle YXY \rangle_Q = \langle YYX \rangle_Q = -1.$$

These four stabilizer eigenvalues are the quantum predictions any successful re-derivation must reproduce. (We deliberately do not use the $(Y,Y,Y)$ setting: its expectation in $|\mathrm{GHZ}\rangle$ requires phase bookkeeping that adds nothing to the argument, since the four settings above already suffice for the contradiction.)

### 4.2 The classical constraint from axioms A1–A4

Under A1–A4, each party $i \in \{1,2,3\}$ carries a local variable $\lambda_i$ and predetermined outcomes $A_i(\lambda_i, s_i) \in \{-1, +1\}$ for settings $s_i \in \{X, Y\}$. Define the four triple products:

$$P_1 = A_1^X A_2^X A_3^X, \quad P_2 = A_1^X A_2^Y A_3^Y, \quad P_3 = A_1^Y A_2^X A_3^Y, \quad P_4 = A_1^Y A_2^Y A_3^X.$$

Each $P_k \in \{-1, +1\}$ pointwise. Their product, computed pointwise for every fixed $\lambda$:

$$P_1 P_2 P_3 P_4 = (A_1^X)^2 (A_1^Y)^2 (A_2^X)^2 (A_2^Y)^2 (A_3^X)^2 (A_3^Y)^2 = (+1)^6 = +1,$$

since each local outcome appears exactly twice and squares to $1$. Taking expectations and using that the pointwise identity holds almost everywhere with respect to $\mu$ (A1):

$$\langle P_1 P_2 P_3 P_4 \rangle_\mu = +1.$$

But the quantum values require $\langle P_1\rangle_Q = +1$ and $\langle P_2\rangle_Q = \langle P_3\rangle_Q = \langle P_4\rangle_Q = -1$, so the quantum product of the four correlations is

$$(+1) \times (-1) \times (-1) \times (-1) = -1 \ne +1.$$

**The contradiction is already complete here:** the classical axioms force the pointwise product $+1$; the quantum statistics require $-1$.

### 4.3 Mermin bound and violation factor

Equivalently, in Mermin-inequality form: for any model satisfying A1–A4,

$$\bigl|\langle P_1\rangle - \langle P_2\rangle - \langle P_3\rangle - \langle P_4\rangle\bigr| \le 2,$$

because the pointwise expression $|P_1 - P_2 - P_3 - P_4| = 2$ whenever $P_1 P_2 P_3 P_4 = +1$. Check of the cases: if all four $P_k = +1$, then $|1 - 1 - 1 - 1| = 2$; if exactly two are $-1$ (e.g. $P_2 = P_3 = -1$), then $|1 + 1 + 1 - 1| = 2$; the all-four-negative case also has product $+1$ (four negatives is an even count) and gives $|-1 - (-1) - (-1) - (-1)| = |-1 + 1 + 1 + 1| = 2$. Hence every assignment with $P_1 P_2 P_3 P_4 = +1$ — zero, two, or four negative terms — yields exactly $|P_1 - P_2 - P_3 - P_4| = 2$, and the classical bound is $M_{\mathrm{LHV}} = 2$.

The quantum values give

$$\bigl|\langle P_1\rangle_Q - \langle P_2\rangle_Q - \langle P_3\rangle_Q - \langle P_4\rangle_Q\bigr| = |(+1) - (-1) - (-1) - (-1)| = |1 + 1 + 1 + 1| = 4 = M_{\mathrm{Q}}.$$

Step by step: $1 + 1 = 2$; $2 + 1 = 3$; $3 + 1 = 4$. The violation gap and factor are

$$\Delta M = M_{\mathrm{Q}} - M_{\mathrm{LHV}} = 4 - 2 = 2, \qquad \frac{M_{\mathrm{Q}}}{M_{\mathrm{LHV}}} = \frac{4}{2} = 2.$$

### 4.4 CHSH cross-check

For two parties, the CHSH combination is

$$S = E(a,b) + E(a,b') + E(a',b) - E(a',b'),$$

with each $E \in [-1, 1]$ classically, giving the classical bound $|S| \le 2$: pointwise, $|ab + ab' + a'b - a'b'| \le 2$ since $b, b' \in \{\pm 1\}$ and one of the two pairs cancels for every assignment. As a clearly labeled projection with stated assumptions — namely, the assumption that standard quantum mechanics predicts the Tsirelson-type maximum $S_{\max} = 2\sqrt{2}$ for singlet-type correlations, a value not stated in any cited work — we take

$$S_{\max} = 2\sqrt{2}.$$

Arithmetic: $\sqrt{2} \approx 1.414214$ (check: $1.414214^2 = 2.0000006 \approx 2$), so $2\sqrt{2} \approx 2 \times 1.414214 = 2.828427$. The violation factor over the classical bound is

$$\frac{2\sqrt{2}}{2} = \sqrt{2} \approx 1.414214.$$

Thus any local classical Radon–Nikodým model reproducing two-party entangled statistics is confined to $|S| \le 2$, while quantum mechanics reaches $2\sqrt{2} \approx 2.828427$; the gap is a factor of $\sqrt{2} \approx 1.414214$, confirming the three-party result at the two-party level.

### 4.5 The PQS correlation-history theorem is classically bounded

The PQS framework publishes an explicit formula for the joint measurement statistics of two entangled systems [11]:

$$P(o_1, o_2) = \sum_i |c_i|^2 P_1(o_1|\phi_1^i)\, P_2(o_2|\phi_2^i),$$

with the correlations arising from coefficients $c_i$ "established during the initial interaction" — a shared-history construction. This formula is a convex mixture (weights $|c_i|^2 \ge 0$, summing to $1$ by normalization of the initial state) of factorized product distributions $P_1(o_1|\phi_1^i) P_2(o_2|\phi_2^i)$. Each factorized component is a local hidden-variable model in the sense of A2: party 1's outcome depends only on $\phi_1^i$ and its setting, party 2's only on $\phi_2^i$ and its setting.

**Convexity argument.** For each mixture component $i$, define the component CHSH value

$$S_i = E_i(a,b) + E_i(a,b') + E_i(a',b) - E_i(a',b'),$$

where $E_i$ is computed from the factorized distribution $P_1(\cdot|\phi_1^i) P_2(\cdot|\phi_2^i)$. By the pointwise argument of Section 4.4 applied to each component, $|S_i| \le 2$ for every $i$. The mixture correlation functions are

$$E(x,y) = \sum_i |c_i|^2 E_i(x,y),$$

so the mixture CHSH value is

$$S = \sum_i |c_i|^2 S_i,$$

and by the triangle inequality, using $\sum_i |c_i|^2 = 1$:

$$|S| = \Bigl|\sum_i |c_i|^2 S_i\Bigr| \le \sum_i |c_i|^2 |S_i| \le \sum_i |c_i|^2 \cdot 2 = 2