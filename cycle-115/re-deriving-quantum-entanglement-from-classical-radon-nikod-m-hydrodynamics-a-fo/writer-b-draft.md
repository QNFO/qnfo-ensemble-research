# Re-Deriving Multi-Particle Entanglement from Classical Radon–Nikodým Hydrodynamics: A Formal Falsification Framework for the Hydrodynamic Stability Hypothesis

## Abstract

The Hydrodynamic Stability Hypothesis (HSH) conjectures that standard quantum mechanics, including multi-particle entangled states, can be axiomatically re-grounded in classical measure theory: wavefunctions are interpreted as relaxing into basins of attraction of classical Radon–Nikodým measures under a local hydrodynamic transport. If correct, this would restore local realism without superdeterminism, contradicting mainstream non-local interpretations. We subject this conjecture to a formal analysis. We first state the HSH axioms precisely in measure-theoretic language and attempt an explicit derivation of the three-qubit GHZ state and its Bell-type (Mermin) correlations purely from classical measure-theoretic axioms. We show that reproducing the GHZ correlation function $E_{\mathrm{GHZ}}(\phi_a,\phi_b,\phi_c)=\cos(\phi_a+\phi_b+\phi_c)$ at the quantum value $M_{\mathrm{Q}}=4$ of the Mermin expression, against the local hidden-variable bound $M_{\mathrm{LHV}}=2$, forces either non-local hidden variables or a contradiction with the locality axiom — a falsification of the strong form of the hypothesis. We then define the weaker, weaker-than-quantum simulation target: sub-femtosecond particle tracking of the proposed hydrodynamic transport, and derive a projection of the required computational resources, with stated assumptions and uncertainty bounds. We argue that the falsification framework, not the derivation, is the hypothesis's most testable contribution.

## 1. Introduction

The relationship between quantum and classical mechanics remains an open problem more than three-quarters of a century after the term "entanglement" was coined for a peculiar feature inherent to quantum systems [3]. Semiclassical analyses of closed systems as Planck's constant becomes vanishingly small show that the fate of entanglement in that limit is subtle rather than trivially classical [3]. At the same time, a body of work constructs explicit bridges between classical and quantum descriptions: unified formulations that provide a continuous passage between strictly classical and strictly quantized states via path-integral-like structures [8], and entanglement-free regimes in which classical particle paradigms (material point, test-particle, droplet model) arise as limit cases of quantum states of interacting pairs [5].

The Hydrodynamic Stability Hypothesis (HSH), documented in the QNFO research record [9], takes the strongest possible position in this landscape: that quantum mechanics — including multi-particle entangled states such as the GHZ state — can be *axiomatically re-derived* from classical measure theory, via a local hydrodynamic picture in which wavefunctions relax into basins of attraction of classical Radon–Nikodým measures. The Radon–Nikodým theorem allows a measure absolutely continuous with respect to a base measure to be represented by a density; the HSH proposes that the quantum wavefunction $|\psi\rangle$ is, at the foundational level, such a density over a classical phase space, and that "measurement" or "state preparation" is a stability phenomenon: trajectories fall into attracting basins of these measures.

This position matters because, if correct, it would restore local realism without superdeterminism — a combination widely believed to be excluded by Bell-type analyses. It also matters practically: multipartite entanglement is the resource that empowers quantum networks beyond bipartite link-by-link distribution [2], enables hierarchical network protocols using hybrid entanglement between different degrees of freedom [6], and underlies tripartite coherence dynamics studied even when qubits couple to classical environments [4]. If entanglement were re-derivable classically, the resource picture underlying these network proposals would change fundamentally.

Rather than advocate, we *test*. Following the falsification logic stated in the source idea, we attempt an explicit derivation of the GHZ state and its Bell-inequality-violating correlations purely from classical measure-theoretic axioms (Section 3–4). If the derivation forces non-local variables or yields a contradiction, the strong hypothesis is falsified. Complementarily, we specify the numerical experiment — sub-femtosecond particle tracking of the hydrodynamic transport — that would check whether apparent instantaneous state changes across spatial barriers are always accompanied by continuous local wave propagation, and we derive the computational cost of that experiment as an explicitly labeled projection (Section 4.4).

Our conclusions are deliberately two-sided: the strong derivation fails in a precise, reproducible way (Section 4.2–4.3), which falsifies one form of the hypothesis; but the failure is itself informative, and the weaker "stability-simulation" program remains a well-posed numerical question.

## 2. Background and Related Work

We organize the literature into four strands, citing each work only for what its supplied abstract states.

**Entanglement as a dynamical and statistical resource.** Reference [1] articulates the philosophy that, as in statistical mechanics and random-matrix theory, individual instances of complex quantum circuits are essentially intractable to simulate while the statistical properties of random ensembles obey simple universal laws; the abstract applies this philosophy to the dynamics of quantum information in ideal and noisy quantum circuits. This is directly relevant to HSH: any hydrodynamic "stability" account must reproduce not individual trajectories but the ensemble statistics that [1]'s framework describes, and ensemble-level universality is precisely where classical and quantum descriptions are hardest to distinguish. Reference [2] presents an algorithm for generating multipartite entanglement between distant nodes of a quantum network, arguing that multipartite entanglement may empower the quantum internet for additional or better applications in communications, sensing, and computation beyond bipartite distribution. Reference [6] introduces hybrid entangled states — entanglement between different degrees of freedom — and aims to exploit them for communication over quantum networks with fewer resources, noting that entanglement shared over networks faces limitations (the supplied abstract is truncated before specifying them). These works define the operational stakes: HSH, if true, would re-derive the very resource these protocols consume.

**The classical–quantum interface.** Reference [3] discusses the fate of entanglement in a closed system as Planck's constant becomes vanishingly small, drawing on recent results in semiclassical systems, and frames the quantum–classical connection as an open problem 75 years after the coining of "entanglement". This is the closest mainstream framing to HSH's motivation: the classical limit of entanglement is genuinely unsettled. Reference [5] identifies three classical, pre-quantum paradigms for particles — the material point, the test-particle, and the diluted particle (droplet model) — as limit cases of a quantum regime in which pairs of particles interact without becoming entangled, and notes this entanglement-free regime provides a simplified model relevant to decoherence-related descriptions (the abstract is truncated at this point). This is significant for HSH because it demonstrates that classical-looking particle descriptions *can* emerge from quantum states without entanglement — the reverse direction of HSH's proposed reduction. Reference [8] proposes a unified combination of classical and quantum systems, aiming to overcome the two separate languages and create a smooth, continuous passage between strictly classical and strictly quantized states, with path integration among the tools mentioned (the abstract truncates there). HSH is a stronger claim than [8]'s unification: HSH asserts classical *priority* (quantum emerges from classical measures), whereas [8] constructs a common framework without privileging either side.

**Tripartite entanglement and classical environments.** Reference [4] studies the dynamics of entanglement and coherence for three non-interacting qubits initially prepared in a maximally entangled GHZ-like state coupled to independent classical environments, considering two different Gaussian environment models (the abstract truncates before giving results). This work is a natural empirical anchor for HSH: it already treats GHZ coherence in the presence of *classical* noise, which is the regime a hydrodynamic measure-relaxation model must match.

**Classical–quantum algorithms.** Reference [7] shows that the scaling of the $\alpha$-QPE family of phase-estimation algorithms — which interpolates continuously between quantum speedup and circuit depth, following Wang, Higgott and Brierley [2019, Phys. Rev. Lett. 122 140504] — can be derived succinctly within a classical–quantum framework using quantum singular value transformations (the abstract truncates before details). We cite this as evidence that partial classical–quantum interpolations are mathematically productive, while noting it addresses algorithms, not foundations.

**The hypothesis itself and its audit trail.** Reference [9] is the QNFO record of the Hydrodynamic Stability Hypothesis itself; its supplied entry contains no summary text, so we can only state that it is the internal source of the conjecture analyzed here and rely on the research-idea statement in the grounding block for its content. Reference [10] is an archive of the Post-Quantum Synthesis (PQS) investigation, described as a neutral investigation of PQS's four sub-pillars mapped against external literature, plus an earlier-iteration analysis of AI gate-check convergence between Claude and Gemini evaluating PQS; we use it only to note that the present hypothesis belongs to a documented research program with prior gate-check analysis. References [11] (a category-theoretic foundation for finite measurement, "Valuation Without R") and [12] (POST QUANTUM SYNTHESIS) have empty supplied summaries; we note that [11]'s title suggests a finite, real-number-free measurement formalism that would be the natural axiomatic substrate for a measure-theoretic re-derivation, but the supplied entry gives no further detail, and we make no claim about its content beyond the title.

## 3. Methods

### 3.1 Axioms of the Hydrodynamic Stability Hypothesis

We formalize the conjecture as follows. Let $(\Omega, \mathcal{F}, \mu_0)$ be a classical probability space, with $\Omega$ a phase space of hidden classical states $\omega \in \Omega$.

- **A1 (Measure grounding).** Every quantum state $|\psi\rangle$ corresponds to a Radon–Nikodým density $\rho_\psi = \frac{d\mu_\psi}{d\mu_0}$, with $\mu_\psi \ll \mu_0$, such that all quantum predictions are recoverable as functionals of $\rho_\psi$.
- **A2 (Local hydrodynamic transport).** The time evolution of $\rho_\psi$ is generated by a local flow $\Phi_t$ on $\Omega$: $\rho_{\psi,t} = \rho_\psi \circ \Phi_{-t}$, where $\Phi_t$ acts only on neighborhoods in $\Omega$ (locality).
- **A3 (Stability).** Preparation and measurement correspond to relaxation of $\rho_\psi$ into basins of attraction $\mathcal{B}_k \subset \Omega$ of stable fixed measures; the observed outcome indexes the basin.
- **A4 (No superdeterminism).** The initial measure $\mu_0$ is not correlated with future measurement settings; settings are free variables independent of $\mu_\psi$.

The strong claim of HSH is that A1–A4 suffice to derive the quantum formalism, including entangled states.

### 3.2 Derivation target: the GHZ state and Mermin correlations

The three-qubit GHZ state is

$$|\mathrm{GHZ}\rangle = \frac{1}{\sqrt{2}}\bigl(|000\rangle + |111\rangle\bigr),$$

with the defining property that its $X$-basis correlations violate a Mermin-type Bell inequality. For measurement settings $\phi_a, \phi_b, \phi_c$ (phase angles in the equatorial plane of each qubit), quantum mechanics predicts the three-party correlation

$$E_{\mathrm{Q}}(\phi_a,\phi_b,\phi_c) = \cos(\phi_a + \phi_b + \phi_c).$$

The Mermin expression is

$$M = E(\phi_a,\phi_b,0) + E(\phi_a,0,\phi_c) + E(0,\phi_b,\phi_c) - E(\phi_a,\phi_b,\phi_c),$$

with the standard choice $\phi_a = \phi_b = \phi_c = 0$ for the first three terms and $\phi_a=\phi_b=\phi_c = \pi/2$-type offsets for the fourth; we use the conventional assignment giving $M_{\mathrm{Q}} = 4$ (computed explicitly in Section 4.2). Any local hidden-variable model satisfies $M_{\mathrm{LHV}} \le 2$.

### 3.3 Falsification protocol

We attempt to construct, under A1–A4, a hidden-variable assignment $\lambda \in \Omega$ and local response functions $A(\lambda, \phi_a)$, $B(\lambda, \phi_b)$, $C(\lambda, \phi_c) \in \{\pm 1\}$ such that

$$E_{\mathrm{LHV}}(\phi_a,\phi_b,\phi_c) = \int_\Omega \rho_\psi(\lambda)\, A(\lambda,\phi_a)\, B(\lambda,\phi_b)\, C(\lambda,\phi_c)\, d\mu_0(\lambda)$$

reproduces $E_{\mathrm{Q}}$ on the Mermin test set. If no such construction exists (or if constructing one forces a violation of A2 or A4), the strong hypothesis is falsified. This is a derivation-and-contradiction analysis, not a numerical simulation; the complementary simulation target is specified in Section 4.4.

## 4. Analysis

### 4.1 Input numbers and their sources

We use exactly three quantitative inputs, all standard and stated here explicitly:

- $I_1 = 2$: the local hidden-variable (Mermin) bound, a theorem of Bell-type analysis for deterministic local assignments $A, B, C \in \{\pm 1\}$ (source: standard Bell-theorem result, restated and re-derived below in Section 4.3, not taken from any cited work).
- $I_2 = \cos 0 = 1$ and $I_3 = \cos(\pi/2) = 0$: trigonometric values used in the correlation evaluation (source: elementary trigonometry).
- $N_{\mathrm{terms}} = 4$: the number of correlation terms in the Mermin expression (structural, from its definition in Section 3.2).

### 4.2 Quantum value of the Mermin expression

Using $E_{\mathrm{Q}}(\phi_a,\phi_b,\phi_c) = \cos(\phi_a+\phi_b+\phi_c)$ with the conventional Mermin settings $(\phi_a,\phi_b,\phi_c) \in \{(0,0,0), (0,0,0), (0,0,0), (0,\tfrac{\pi}{2},\tfrac{\pi}{2})\text{-type}\}$ — concretely, the standard assignment where the first three terms have phase sums $0$ and the fourth has phase sum $\pi$:

$$E_1 = \cos(0) = 1, \qquad E_2 = \cos(0) = 1, \qquad E_3 = \cos(0) = 1,$$
$$E_4 = \cos(\pi) = -1.$$

Then

$$M_{\mathrm{Q}} = E_1 + E_2 + E_3 - E_4 = 1 + 1 + 1 - (-1) = 4.$$

Step by step: $1 + 1 = 2$; $2 + 1 = 3$; $3 - (-1) = 3 + 1 = 4$. So $M_{\mathrm{Q}} = 4$.

### 4.3 Local hidden-variable bound under A1–A4

Under A1–A4, each particle's response is a deterministic local function of $\lambda$ and its own setting. For any fixed $\lambda$, define the sign product

$$s(\lambda) = A(\lambda,\phi_a)\,B(\lambda,\phi_b)\,C(\lambda,\phi_c)\,A(\lambda,\phi_a)\,B(\lambda,\phi_b)\,C(\lambda,\phi_c') \cdots$$

More directly: for the four Mermin terms with settings $(a,b,c)$, $(a,b',c')$, $(a',b,c')$, $(a',b',c)$ (primes denoting alternative settings), the product of the four deterministic products is

$$\bigl[A_a B_b C_c\bigr]\bigl[A_a B_{b'} C_{c'}\bigr]\bigl[A_{a'} B_b C_{c'}\bigr]\bigl[A_{a'} B_{b'} C_{c}\bigr].$$

Each letter $A_a, A_{a'}, B_b, B_{b'}, C_c, C_{c'} \in \{\pm 1\}$ appears exactly twice in this product, so the total product is

$$\prod_{x \in \{A_a, A_{a'}, B_b, B_{b'}, C_c, C_{c'}\}} x^2 = (+1)^6 = 1.$$

Hence at least one of the four terms equals $-1$ for every $\lambda$ (if all four were $+1$, their product would be $+1$ — consistent — but the bound argument is: the arithmetic mean of four numbers in $[-1, +1]$ whose product constraint forces at least one to be $-1$ whenever the other three are $+1$ satisfies)

$$|M_{\mathrm{LHV}}| = |E_1 + E_2 + E_3 - E_4| \le 2,$$

since the maximum of $E_1 + E_2 + E_3 - E_4$ subject to $E_i \in [-1,1]$ and the product constraint above is attained at $(1,1,1,-1)$, giving $1+1+1-(-1) = 4$ for quantum but for *local* assignments the product constraint $s(\lambda) = 1$ with an odd number of minus signs means the pattern $(1,1,1,-1)$ requires $E_4 = -1$ while $E_1 = E_2 = E_3 = +1$ at the *same* $\lambda$; the deterministic product at that $\lambda$ would then be $(+1)(+1)(+1)(-1) = -1 \ne +1$, contradicting the constraint. Therefore for every $\lambda$ at least one term contributes negatively, and averaging over $\lambda$:

$$M_{\mathrm{LHV}} = \left|\int \rho_\psi(\lambda)\bigl[E_1 + E_2 + E_3 - E_4\bigr](\lambda)\, d\mu_0\right| \le 2.$$

The gap is

$$\Delta M = M_{\mathrm{Q}} - M_{\mathrm{LHV}} = 4 - 2 = 2,$$

i.e., the quantum prediction exceeds the local bound by a factor

$$\frac{M_{\mathrm{Q}}}{M_{\mathrm{LHV}}} = \frac{4}{2} = 2.$$

**Falsification.** Reproducing $E_{\mathrm{Q}} = \cos(\phi_a+\phi_b+\phi_c)$ on the Mermin test set under A1–A4 requires violating the product constraint derived above, which follows from A2 (locality of the flow: $A$ depends only on $\lambda$ and $\phi_a$, not on $\phi_b, \phi_c$) and A4 (no superdeterministic correlation between $\rho_\psi$ and settings). The derivation therefore forces one of: (i) abandonment of A2 — non-local hidden variables; (ii) abandonment of A4 — superdeterminism; or (iii) a contradiction. Since HSH asserts all four axioms, the strong form of the hypothesis — that GHZ correlations are derivable from classical measure theory under A1–A4 — is **falsified** by this derivation.

### 4.4 Simulation target: sub-femtosecond tracking (explicit projection)

The complementary program requires tracking the hydrodynamic transport $\Phi_t$ at sub-femtosecond resolution to check whether apparent instantaneous state changes across spatial barriers are accompanied by continuous local wave propagation. This is a *projection*, not a result; we state all assumptions.

**Assumptions.** (a) A one-dimensional model particle with wavepacket scale $L = 1\,\mathrm{nm} = 10^{-9}\,\mathrm{m}$ (typical mesoscopic coherence scale, assumed). (b) Sub-femtosecond resolution requirement $\Delta t = 10^{-16}\,\mathrm{s}$ (one attosecond, assumed as "sub-femtosecond"). (c) A phase-space discretization with $N_{\mathrm{grid}}$ cells per spatial dimension and $d = 1$ spatial dimension plus conjugate momentum, giving $N_{\mathrm{cells}} = N_{\mathrm{grid}}^2$ cells for the $(x,p)$ phase plane; we assume $N_{\mathrm{grid}} = 10^3$ per axis (assumed resolution). (d) One flow-map update per cell per timestep, cost $c_0 = 1$ floating-point operation per cell per step (assumed).

**Derivation.** Number of cells:

$$N_{\mathrm{cells}} = N_{\mathrm{grid}}^{2} = (10^{3})^{2} = 10^{6}.$$

Number of timesteps to cover one wavepacket transit time $T = L / v$, with $v$ taken as $10^{5}\,\mathrm{m\,s^{-1}}$ (assumed slow mesoscopic velocity):

$$T = \frac{L}{v} = \frac{10^{-9}\,\mathrm{m}}{10^{5}\,\mathrm{m\,s^{-1}}} = 10^{-14}\,\mathrm{s},$$

$$N_{\mathrm{steps}} = \frac{T}{\Delta t} = \frac{10^{-14}}{10^{-16}} = 10^{2}.$$

Total operation count:

$$N_{\mathrm{ops}} = N_{\mathrm{cells}} \times N_{\mathrm{steps}} \times c_0 = 10^{6} \times 10^{2} \times 1 = 10^{8}.$$

At a sustained rate of $R = 10^{12}\,\mathrm{op\,s^{-1}}$ (assumed single-workstation throughput), wall-clock time:

$$t_{\mathrm{wall}} = \frac{N_{\mathrm{ops}}}{R} = \frac{10^{8}}{10^{12}}\,\mathrm{s} = 10^{-4}\,\mathrm{s}.$$

**Uncertainty bounds.** Each assumed input carries at least an order of magnitude of uncertainty. If $N_{\mathrm{grid}} = 10^{4}$ (ten times finer per axis), $N_{\mathrm{cells}} = 10^{8}$ and $N_{\mathrm{ops}} = 10^{10}$, giving $t_{\mathrm{wall}} = 10^{-2}\,\mathrm{s}$. If instead a three-dimensional, three-particle GHZ-type simulation is required, with $d_{\mathrm{eff}} = 6$ phase-space dimensions per particle $\times 3$ particles $= 18$ dimensions and $N_{\mathrm{grid}} = 10$ per axis (coarse but illustrative):

$$N_{\mathrm{cells}}^{(3q)} = 10^{18}, \qquad N_{\mathrm{ops}}^{(3q)} = 10^{18} \times 10^{2} = 10^{20}, \qquad t_{\mathrm{wall}}^{(3q)} = \frac{10^{20}}{10^{12}}\,\mathrm{s} = 10^{8}\,\mathrm{s} \approx 3.17\,\mathrm{years},$$

where $10^{8}\,\mathrm{s} / (3.156 \times 10^{7}\,\mathrm{s\,yr^{-1}}) \approx 3.17$ (arithmetic: $10^{8} / 3.156 \times 10^{7} = 3.169\ldots$, rounded to $3.17$). The projection therefore spans from trivial ($10^{-4}\,\mathrm{s}$) to infeasible-on-a-workstation ($\approx 3.17$ years) depending entirely on dimensionality and resolution — the uncertainty is dominated by the unstated dimensional requirement of the hydrodynamic model, which is itself an open specification of HSH [9].

## 5. Results

We report only quantities computed in Section 4.

- **R1 (computed).** The quantum value of the Mermin expression for the GHZ state is $M_{\mathrm{Q}} = 4$ (Section 4.2: $1 + 1 + 1 - (-1) = 4$).
- **R2 (computed).** The local hidden-variable bound under axioms A1–A4 is $M_{\mathrm{LHV}} \le 2$, from the sign-product constraint $(+1)^6 = 1$ forcing at least one negative term per $\lambda$ (Section 4.3).
- **R3 (computed).** The violation gap is $\Delta M = 4 - 2 = 2$, a factor of $M_{\mathrm{Q}}/M_{\mathrm{LHV}} = 2$.
- **R4 (falsification result).** The strong form of HSH — derivation of GHZ correlations from classical measure-theoretic axioms A1–A4 — is falsified: reproducing $E_{\mathrm{Q}}$ forces either non-local variables (dropping A2) or superdeterminism (dropping A4).
- **R5 (projection, assumptions in Section 4.4).** Sub-femtosecond hydrodynamic tracking of a one-particle, one-dimensional model requires $N_{\mathrm{ops}} = 10^{8}$ operations and $t_{\mathrm{wall}} = 10^{-4}\,\mathrm{s}$ at $R = 10^{12}\,\mathrm{op\,s^{-1}}$; a three-qubit, 18-dimensional variant requires $N_{\mathrm{ops}}^{(3q)} = 10^{20}$ and $t_{\mathrm{wall}}^{(3q)} \approx 3.17$ years. These are projections with stated assumptions, not measurements.

## 6. Discussion

**What the falsification does and does not show.** The derivation in Section 4.3 falsifies the *strong* claim: that GHZ-type Bell-violating correlations follow from classical measure theory plus local hydrodynamic transport plus freedom of settings. It does not falsify weaker versions. In particular, a version of HSH that drops A2 — allowing the Radon–Nikodým measure to be non-local on $\Omega$ — or that reinterprets "locality" at the level of the flow rather than the response functions, escapes the argument. We flag this as the hypothesis's most likely retreat position, and it is exactly the position that mainstream non-local interpretations occupy; the value of the derivation is that it shows HSH cannot simultaneously keep locality, measurement freedom, and the GHZ correlations.

**Against ourselves: possible escapes we cannot exclude.** First, our formalization A1–A4 is our own; the source record [9] supplies no summary text (its entry is empty), so the hypothesis's author might formalize "stability" or "locality" differently in ways that evade our axioms. The falsification is conditional on our formalization being faithful. Second, we assumed deterministic response functions $A, B, C \in \{\pm 1\}$; stochastic local response functions change the bound derivation's bookkeeping but not the underlying product constraint, though a fully rigorous treatment of the stochastic case is not given here. Third, the connection between "basins of attraction" (A3) and Born-rule statistics is nowhere derived in this paper; even if the correlation structure were classically reproducible, the *probabilities* would need a separate derivation, and reference [11]'s category-theoretic finite-measurement program (whose supplied entry gives no detail beyond the title) might be the intended substrate — we cannot verify this from the supplied material.

**What would falsify our falsification.** A single explicit construction of local response functions $A(\lambda,\phi_a), B(\lambda,\phi_b), C(\lambda,\phi_c)$ and a measure $\rho_\psi$ satisfying A1–A4 that reproduces $E_{\mathrm{Q}}(\phi_a,\phi_b,\phi_c) = \cos(\phi_a+\phi_b+\phi_c)$ on the Mermin test set would overturn R4. This is a sharply specified, machine-checkable target.

**Simulation program: failure modes.** The projection in Section 4.4 shows the simulation's feasibility is entirely assumption-dependent: the one-dimensional case is trivial ($10^{-4}\,\mathrm{s}$), the three-qubit case is workstation-infeasible ($\approx 3.17$ years) at the assumed resolution. Failure modes include: (i) the hydrodynamic flow $\Phi_t$ may not admit a stable discretization at $\Delta t = 10^{-16}\,\mathrm{s}$; (ii) "continuous local wave propagation across barriers" may be indistinguishable from numerical dispersion artifacts at any feasible resolution; (iii) the model's dimensional requirement is unspecified, so no definitive resource estimate is possible. A negative simulation result would not rescue the strong hypothesis (already falsified analytically), but a positive one — continuous local propagation underpinning apparent state updates — would support only the weak, dynamical form of HSH.

**Relation to the literature.** Our result is consistent with the open-problem framing of [3]: the classical limit of entanglement is genuinely unresolved, and semiclassical analyses do not trivially eliminate entanglement. It is also consistent with the existence of entanglement-free classical-limit regimes [5] and unified classical–quantum frameworks [8]: these show partial classical–quantum passages are possible without full classical *reduction*. The resource-oriented literature [2], [6], [4] and the ensemble-statistics philosophy of [1] describe phenomena any residual (weak) HSH must reproduce; the algorithmic interpolation of [7] is orthogonal to our foundational question. The prior audit record [10] situates this work in a documented research program; we note that our analytic result is independent of that program's gate-check methodology.

**Open questions.** (1) Does a stochastic-response version of the Mermin bound under A1–A4 change the falsification? (2) Can A3 (basin relaxation) be shown to reproduce the Born rule at all, even for single systems? (3) What is the minimal dimensional specification of the hydrodynamic transport needed to make the simulation projection of Section 4.4 definite?

## 7. Conclusion

We formalized the Hydrodynamic Stability Hypothesis as four axioms (A1–A4) on classical Radon–Nikodým measures with local hydrodynamic transport and stability basins, and attempted an explicit classical derivation of the three-qubit GHZ state's Mermin correlations. The derivation yields a precise falsification: the quantum value $M_{\mathrm{Q}} = 4$ exceeds the local bound $M_{\mathrm{LHV}} \le 2$ by a factor of $2$, and reproducing the quantum correlations under A1–A4 forces either non-local hidden variables or superdeterminism. The strong form of the hypothesis — local realism without superdeterminism via classical measure theory — is therefore falsified, conditional on our formalization. The weak, dynamical form remains open and is testable by the sub-femtosecond tracking simulation we costed as an explicit projection ($10^{-4}\,\mathrm{s}$ for a one-dimensional toy; $\approx 3.17$ years for a three-qubit, 18-dimensional variant at assumed resolution). The principal contribution is the falsification protocol itself: a sharply specified, machine-checkable target — an explicit local construction reproducing $E_{\mathrm{Q}} = \cos(\phi_a+\phi_b+\phi_c)$ — whose production would overturn our conclusion.

## References

[1] arXiv:2111.08018v2 | Entanglement dynamics in hybrid quantum circuits
[2] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks
[3] arXiv:1110.0157v1 | Entanglement, the quantum formalism and the classical world
[4] arXiv:2107.11259v1 | Probing tripartite entanglement and coherence dynamics in pure and mixed independent classical environments
[5] arXiv:1206.5715v2 | Coherent states and the classical-quantum limit considered from the point of view of entanglement
[6] arXiv:2004.13176v3 | Hierarchical Quantum Network using Hybrid Entanglement
[7] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations
[8] arXiv:2010.03984v2 | A Unified Combination of Classical and Quantum Systems
[9] QNFO: Hydrodynamic Stability Hypothesis
[10] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis
[11] QNFO: Valuation Without R: A Category-Theoretic Foundation for Finite Measurement
[12] QNFO: POST QUANTUM SYNTHESIS