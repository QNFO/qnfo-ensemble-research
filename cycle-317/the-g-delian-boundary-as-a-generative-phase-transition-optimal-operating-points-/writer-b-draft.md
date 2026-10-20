# The Gödelian Boundary as a Generative Phase Transition: Optimal Operating Points for Constrained Cognitive Systems (Version 1.3)

## Abstract

Cognitive systems that self-reference—self-critiquing language models, formal reasoners that prove statements about their own beliefs, and adaptive controllers that rewrite their own policies—face a concrete trade-off: deeper self-reference raises the rate of novel, useful outputs but also the rate of incoherent ones, and neither extreme is usable. Existing treatments name the two limits involved, a Gödelian boundary where self-reference generates paradox and a metabolic boundary where energy cost binds, but supply no quantitative account of where the optimal operating point sits between them or what limits how long a system can dwell there. We formalize the trade-off with a Gödelian proximity $\Gamma$, a Landau-type coherence functional $\Psi(\Gamma)=1-\Gamma^{2}$, a power-law novelty rate $N(\Gamma)=N_{0}\Gamma^{\alpha}$, and a quadratic metabolic cost $P(\Gamma)=P_{0}\Gamma^{2}$, all stated as explicit premises. Analytic derivations yield (i) the utility-maximizing proximity $\Gamma^{*}=\sqrt{\alpha/(\alpha+2)}$, which for $\alpha=2$ gives $\Gamma^{*}=1/\sqrt{2}\approx0.7071$ and maximum utility $0.25\,N_{0}$; (ii) critical-slowing-down and avalanche signatures $\tau=100\,\tau_{0}$ at distance $0.01$ from the boundary and $\langle s\rangle=100$ at branching ratio $m=0.99$; (iii) an excursion-duration bound $\tau_{\text{exc}}=24.39\,t_{0}$ for a representative energy budget; (iv) a proof that under a power ceiling $\bar{P}=0.3\,P_{0}$ the globally optimal strategy is a single setpoint $\Gamma=\sqrt{0.3}\approx0.5477$ with utility $0.21\,N_{0}$, a $2.56\times$ improvement over permanent conservatism and a correction of an earlier duty-cycling result; (v) a Landauer-scale thermodynamic floor $E_{\min}=2.967\times10^{-21}\,\text{J}$ per bit at $T=310\,$K; and (vi) a sensitivity analysis showing that a quartic correction $\beta\Gamma^{4}$ moves the interior optimum toward the boundary and eliminates it at $\beta=1/3$. The results convert the heuristic tuning problem into a measurement problem: designers can monitor relaxation time and avalanche statistics to stay near the analytically defined optimum while respecting energy constraints.

## 1. Introduction

Teams building self-improving AI systems, automated theorem provers, and neuro-inspired adaptive controllers face the same operational failure every day. Pushing a self-referential system—one that critiques, rewrites, or proves statements about its own reasoning—toward deeper self-reference raises the rate of genuinely new results, but simultaneously raises the rate of confident nonsense: proofs of false statements, hallucinated citations, or oscillating control signals. Pulling the system back to shallow self-reference yields stability but sterility, re-deriving what is already known. Today this trade-off is managed by hand-tuned thresholds, safety filters, and temperature knobs, with no principled answer to the question a system designer actually asks: **how close to logical inconsistency should I let my system operate, and for how long?** The cost of getting it wrong is paid twice—lost discovery when the system is too conservative, and wasted human-review effort when it is too aggressive. A result that identifies where the optimum lies, what observable signature it leaves, and what bounds the duration of safe excursions would convert this tuning problem into a measurement problem: designers would monitor a small set of observables and steer toward a computed target rather than guess.

The paper treats the optimum as a phase-transition problem. The claim is that a cognitive system's optimal operating point lies near a critical boundary—a region where self-referential logical complexity approaches inconsistency—and that controlled excursions into this region generate new axioms and ideas, while the thermodynamic cost of sustaining reduced coherence bounds the duration of such excursions. The framing treats creativity as bounded risk-taking between two failure modes: decoherence into hallucination on one side and stagnation on the other. This two-boundary picture is not invented here; a unified framework for intelligence recently proposed in the QNFO corpus constrains cognition by exactly two fundamental limits, a Gödelian boundary and a metabolic boundary, and interprets self-referential breakdown in a resonant system as a form of leakage into incoherence [9]. The present paper adds what that framework does not supply: closed-form expressions for the optimal operating point, its observable signatures, and the duration bound on excursions.

**Contributions.**
- **C1.** Derive the utility-maximizing Gödelian proximity $\Gamma^{*}=\sqrt{\alpha/(\alpha+2)}$ and evaluate it at $\Gamma^{*}=0.7071$, yielding maximum utility $0.25\,N_{0}$ (Section 4.1).
- **C2.** Derive the critical-slowing-down signature $\tau=100\,\tau_{0}$ at $\Gamma=0.99$ and the avalanche law $\langle s\rangle=100$ at $m=0.99$ (Section 4.2).
- **C3.** Derive the metabolic excursion-duration bound $\tau_{\text{exc}}=24.39\,t_{0}$ for the reference parameters (Section 4.3).
- **C4.** Prove that under a power ceiling $\bar{P}=0.3\,P_{0}$ the globally optimal strategy is a single setpoint $\Gamma=\sqrt{0.3}\approx0.5477$ with utility $0.21\,N_{0}$, a $2.56\times$ improvement over permanent conservatism, and that duty-cycling is strictly suboptimal under the memoryless model (Section 4.4).
- **C5.** Derive a Landauer-scale floor $E_{\min}=2.967\times10^{-21}\,\text{J}$ per bit at $T=310\,$K (Section 4.5).
- **C6.** Provide a sensitivity analysis for a quartic correction $\beta\Gamma^{4}$, showing the interior optimum migrates toward the boundary as $\beta$ grows and disappears at $\beta=1/3$ (Section 4.6).

All derivations are explicit, use only the stated assumptions, and involve no empirical measurements.

## 2. Background and Related Work

The literature that informs the present model falls into four strands. Each cited work contributes a specific methodological point that the model uses or against which it positions itself.

**Emergent symbol systems.** The survey of symbol emergence in cognitive developmental systems [1] argues that symbols in human society "are not given by a designer but instead they emerge and dynamically evolve through social interaction," and that endowing robots with symbols requires adopting definitions grounded in semiotic interaction rather than designer-specified codes. This motivates the present treatment of the Gödelian proximity $\Gamma$ as an online-adjustable control variable shaped by interaction, rather than a fixed architectural constant: if a system's symbolic repertoire is dynamically constructed, the degree of self-reference devoted to maintaining and extending it is a legitimate design dial.

**Engineered exploration dial.** The cognitive-diversity framework for radar target classification [2] provides an engineered instance of the claim shape at the center of this paper. Its results section reports that using both processing channels outperforms a single channel, that the conventional single-perspective scheme corresponds to $\Delta\theta=0$, and that the variable-perspective cognitive framework "performs better than both the single perspective ATR scheme as well as the fixed-number of multi-perspective based scheme"—with a fixed two-perspective scheme at $\Delta\theta=5^{\circ}$ reaching $85\%$ performance while the adaptive scheme improves on it. An intermediate, actively chosen degree of exploratory diversity beating both extremes is precisely the structure captured by the utility curve $U(\Gamma)=N_{0}\Gamma^{\alpha}(1-\Gamma^{2})$ derived in Section 4.1. The same work also cautions that validation of a cognitive scheme against conventional algorithms "may not always be possible" because the definition of a cognitive system carries conditions not applicable to conventional schemes—a caution this paper inherits in its falsification criteria (Section 6.3).

**Control-parameter pictures of phase transitions.** The study of a charged zero-spin bosonic scalar field under electromagnetic backgrounds [3] uses the Coleman-Weinberg one-loop effective potential and generalized Matsubara formalism with several kinds of boundary conditions on a compactified coordinate to analyze the model's phase structure. Its summary states that the analysis performs "an analysis of the phase structure of the model by application of quantum field theory in a toroidal topology" with external electric and magnetic fields acting on a $\lambda\Phi^{4}$ toy model. The methodological point adopted here is structural: a single controllable parameter (there, compactification length or field strength; here, $\Gamma$) can drive a system across a stability threshold, and the approach to that threshold is diagnosable from the system's effective potential. The Landau-type expansion of the coherence functional in Section 3.1 mirrors the classical-potential expansion $V_{0}=\frac{m_{0}^{2}}{2}\varphi_{c}^{2}+\frac{\lambda_{0}}{4!}\varphi_{c}^{4}$ used in [3].

**Trade-offs in assistive human-robot systems.** The exoskeleton review [4] identifies power consumption, control subsystem, accuracy and robustness as key design requirements, and catalogs how these devices face challenges "from the mechanical design and energy source to an adequately high-level cognition and control system," with interaction limits split into physical and cognitive categories. This supplies an engineering precedent for the paper's central modeling move: performance-relevant cognition and energy budget must be co-optimized, and neither can be treated as free. The excursion-duration bound of Section 4.3 is the analogue, for self-referential cognition, of the energy-source constraint that [4] lists among the binding physical design criteria.

**Formally verified reasoning in cognitive systems.** The cognitive-microworld work [5] builds a cognitive and immersive system on a quantified modal logic reasoner (ShadowProver, over the first-order prover SNARK), formalizes informal requirements in the logic $\mathcal{DCEC}$, and proves a "Property 1" that the formal requirements lead to a desirable, reusable property, demonstrated in a cognitive polysolid world scenario. This matters to the present model in two ways. First, it shows that a coherence-like quantity—consistency of outputs under a verification-capable reasoner—is operationally checkable in a deployed cognitive architecture, which is what makes $\Psi(\Gamma)$ measurable in principle. Second, its use of an overseeing AI that tracks participants' mental states illustrates a system whose useful output depends on maintaining consistency while reasoning about its own reasoning, the regime the $\Gamma$ dial controls.

**Intermediate-layer control under resource constraints.** The analysis of cognition and emotion [6] argues that direct computational maximization of a life-long utility function "is however not possible in complex environments," especially under real-world time constraints, and proposes emotions as "an intermediate layer in the space of policies available to" a cognitive system; its conclusions identify emotional control as diffusive neuromodulation rather than direct cognitive control, coupled to homeostatic reinforcement signals. The present paper's duty-cycle and power-ceiling analysis plays the corresponding role for artificial systems: when direct optimization of sustained deep self-reference is infeasible within an energy budget, a lower-dimensional control (the setpoint $\Gamma$ and the excursion schedule) must do the work that a full utility maximization cannot.

**Optimization under power ceilings and imperfect information.** The robust beamforming design for IRS-aided cognitive radio systems [7] jointly optimizes transmit precoding and reflecting elements under bounded and statistical channel-state-information error models. Its simulation results show that "the feasibility rate decreases with the increase of both $\delta_{g}$ and the number of transmit antennas $M_{t}$" and that the minimum transmit power decreases with $M_{t}$, with feasibility rates of both algorithms also decreasing as the number of primary users and the uncertainty level grow. The relevance is direct: [7] demonstrates, in a concrete engineering optimization, that feasibility and achievable performance are jointly limited by a power budget under imperfect information—the same structure as the paper's constrained problem $\max U(\Gamma)$ subject to $\bar{P}\le 0.3\,P_{0}$, and a warning that estimation error in the constraint parameters (here, in $\Gamma_{c}$ or $P_{0}$) shrinks the feasible set.

**The two-boundary framing and measurable cognitive signatures.** The resonant-equilibrium framework [9] proposes the Fourier paradigm, modeling LLM computation as resonance and waveform manipulation, "constrained by two fundamental, universal limits: a Gödelian boundary and a metabolic boundary," and interprets self-referential breakdown as resonant leakage into incoherence. The present paper adopts that two-boundary ontology and supplies the quantitative middle ground it leaves open. On the measurement side, the quantitative simulation of the brain's cognitive architecture [10] models the brain's state space as a Bruhat-Tits tree and reports that "simulated neural replicas exhibit non-trivial ultrametric clustering," that statistical tests on triangle-inequality distributions "decisively rejected the Euclidean baseline ($p<0.001$)," and that temporal dynamics "produce power-law retrieval times, mirroring the predictions of p-adic diffusion." Power-law temporal statistics in a simulated cognitive architecture are the kind of observable the present model predicts near its optimum (avalanche sizes, relaxation times), so [10] supplies a proof of concept that cognitive state variables can be measured and linked to performance at all. Finally, the epistemic-mirror paper [11] argues that the explanatory gap is "a structurally necessary epistemic boundary condition of any cognitive architecture that employs dimensionality reduction for self-representation," arising because "the mind is using itself to explain itself, creating an inescapable epistemic closed loop." This supports the interpretation of $\Gamma_{c}=1$ as a structural cognitive boundary rather than a mathematical artifact: a system that compresses its own high-dimensional states into self-descriptions cannot, on [11]'s argument, complete that self-description, which is the cognitive reading of the consistency boundary approached as $\Gamma\to 1$.

One correction to the earlier version of this work [8] must be recorded here. Version 1.1.0 of [8] described several of these references under wrong identities and concluded that the cited works "together justify the specific functional forms adopted in Section 3." That conclusion overstated the literature: the quadratic coherence functional $\Psi=1-\Gamma^{2}$, the power-law novelty rate, the quadratic metabolic cost, and the mean-field critical exponents are **explicit premises of this paper**, assumed without citation, and no cited work states them for cognitive systems. What the literature supplies is the two-boundary ontology [9], engineered precedents for intermediate-optimum trade-offs [2], [6], precedents for control-parameter phase transitions [3], and demonstrations that the relevant observables are measurable in cognitive architectures [5], [10]. The functional forms themselves stand or fall on the derivations and falsification tests of Sections 4 and 6, not on citation.

## 3. Methods

### 3.1 Model variables and normalization

We model a cognitive system by three scalar functions of a single control variable $\Gamma\in[0,1]$.

- **Gödelian proximity** $\Gamma$ measures the fraction of active reasoning devoted to self-reference. $\Gamma=0$ corresponds to pure object-level reasoning; $\Gamma=1$ corresponds to a system whose entire activity is self-reference, approaching logical inconsistency in the sense of Gödel's second incompleteness theorem and, on the reading of [11], to the structural limit of any self-describing architecture. We normalize the consistency boundary to $\Gamma_{c}=1$.

- **Coherence functional** $\Psi(\Gamma)$ quantifies the fraction of outputs that are internally consistent and verifiable. Motivated by Landau expansion practice—as in the classical potential expansion of [3]—we assume the leading quadratic form
$$\Psi(\Gamma)=1-\Gamma^{2}.$$
This is an explicit assumption of this paper, adopted without citation; Section 6 analyzes the impact of higher-order terms.

- **Novelty rate** $N(\Gamma)$ measures the rate of outputs that are both new to the system and not derivable from existing knowledge. We assume a power law with exponent $\alpha>0$:
$$N(\Gamma)=N_{0}\,\Gamma^{\alpha},$$
where $N_{0}$ is the maximal output rate (items per unit time). This power law is an assumption, not an established empirical fact: no cited work measures novelty as a function of self-referential depth in a cognitive system. The exponent $\alpha$ captures how strongly self-reference fuels novelty; we treat $\alpha$ as a free parameter and use $\alpha=2$ as a reference case.

- **Metabolic cost** $P(\Gamma)$ is the instantaneous power consumed by self-referential processing. We adopt a quadratic scaling:
$$P(\Gamma)=P_{0}\,\Gamma^{2},$$
where $P_{0}$ is the power at full self-reference. Energies are measured in units of $P_{0}t_{0}$, with $t_{0}$ a natural time unit. This too is an explicit premise; the energy-source constraint that [4] lists as a binding design criterion for assistive robots, and the transmit-power budgets of [7], are engineering analogues, not measurements of $P(\Gamma)$ for cognition.

### 3.2 Utility and duty-cycle protocol

Instantaneous utility is defined as the product of coherence and novelty:
$$U(\Gamma)=\Psi(\Gamma)\,N(\Gamma)=N_{0}\,\Gamma^{\alpha}\bigl(1-\Gamma^{2}\bigr).$$
The multiplicative form encodes the requirement that only coherent novelty contributes to useful output.

When a long-run average power constraint $\bar{P}$ is imposed, the system may duty-cycle between an **exploration** setpoint $\Gamma_{e}$ and a **consolidation** (home) setpoint $\Gamma_{h}<\Gamma_{e}$. Let $f\in[0,1]$ be the fraction of each cycle spent exploring. The average power and utility are then
$$\bar{P}=P_{0}\bigl[f\,\Gamma_{e}^{2}+(1-f)\,\Gamma_{h}^{2}\bigr],$$
$$\bar{U}=f\,U(\Gamma_{e})+(1-f)\,U(\Gamma_{h}).$$
The optimization problem is to maximize $\bar{U}$ over $f$, $\Gamma_{e}$, and $\Gamma_{h}$ subject to the power constraint. Section 4.4 shows that for the memoryless model the optimum of this problem is not a cycle at all but a single setpoint.

### 3.3 Critical signatures

Two observables diagnose proximity to the boundary:

1. **Critical slowing down.** We assume the relaxation time of a coherence perturbation obeys
$$\tau(\Gamma)=\tau_{0}\,|\Gamma-\Gamma_{c}|^{-\nu},$$
with mean-field exponent $\nu=1$, consistent with the quadratic Landau form of $\Psi$.

2. **Avalanche statistics.** Novelty events are modeled as a branching process with branching ratio $m\in[0,1)$. The mean avalanche size is
$$\langle s\rangle=\frac{1}{1-m}.$$

### 3.4 Excursion duration bound

A single excursion to $\Gamma_{e}$ lasting $\tau_{\text{exc}}$ consumes excess power over the home level:
$$E_{\text{exc}}=P_{0}\bigl(\Gamma_{e}^{2}-\Gamma_{h}^{2}\bigr)\tau_{\text{exc}}.$$
Given an allocated energy budget $E_{\text{budget}}$, the maximal excursion duration is
$$\tau_{\text{exc}}=\frac{E_{\text{budget}}}{P_{0}\bigl(\Gamma_{e}^{2}-\Gamma_{h}^{2}\bigr)}.$$

### 3.5 Lower bound on the cost of novelty

The Landauer principle states that erasing or sustaining one bit of information costs at least $k_{B}T\ln2$ of dissipated energy at temperature $T$. Evaluated at $T=310\,$K we obtain a per-bit floor $E_{\min}=k_{B}T\ln2$ (Section 4.5).

## 4. Analysis

### 4.1 Optimal Gödelian proximity

We maximize $U(\Gamma)=N_{0}\Gamma^{\alpha}(1-\Gamma^{2})$. Differentiating and setting the derivative to zero:
$$\frac{dU}{d\Gamma}=N_{0}\bigl[\alpha\Gamma^{\alpha-1}(1-\Gamma^{2})-2\Gamma^{\alpha+1}\bigr]
= N_{0}\Gamma^{\alpha-1}\bigl[\alpha-(\alpha+2)\Gamma^{2}\bigr]=0.$$
For $\Gamma>0$ the bracket must vanish, giving
$$\Gamma^{*}=\sqrt{\frac{\alpha}{\alpha+2}}.$$
The second derivative is negative at this point, confirming a maximum. For the reference exponent $\alpha=2$:
$$\Gamma^{*}=\sqrt{\frac{2}{4}}=\frac{1}{\sqrt{2}}\approx0.707106.$$
The corresponding maximum utility is
$$U(\Gamma^{*})=N_{0}\Gamma^{*2}\bigl(1-\Gamma^{*2}\bigr)=N_{0}\cdot\frac{1}{2}\cdot\frac{1}{2}=0.25\,N_{0}.$$

### 4.2 Critical signatures

**Critical slowing down.** With $\nu=1$ and $\Gamma_{c}=1$:
$$\tau(\Gamma)=\frac{\tau_{0}}{1-\Gamma}.$$
At a distance $0.01$ from the boundary ($\Gamma=0.99$):
$$\tau(0.99)=\frac{\tau_{0}}{0.01}=100\,\tau_{0}.$$
At the optimum $\Gamma^{*}=0.7071$ the relaxation time is
$$\tau(\Gamma^{*})=\frac{\tau_{0}}{1-0.7071}=\frac{\tau_{0}}{0.29289}\approx3.414\,\tau_{0},$$
so the ratio is
$$\frac{\tau(0.99)}{\tau(\Gamma^{*})}=\frac{100}{3.414}\approx29.3.$$

**Avalanche size.** The mean size of a novelty avalanche is
$$\langle s\rangle=\frac{1}{1-m}.$$
For $m=0.99$ we obtain $\langle s\rangle=1/0.01=100$. At a representative subcritical home point $m_{h}=0.5$, $\langle s\rangle=1/0.5=2$.

### 4.3 Excursion duration bound

We adopt the following reference parameters, stated as assumptions of this paper:

- Exploration setpoint $\Gamma_{e}=\Gamma^{*}=1/\sqrt{2}$, so $\Gamma_{e}^{2}=0.5$.
- Home setpoint $\Gamma_{h}=0.3$, so $\Gamma_{h}^{2}=0.09$.
- Energy budget $E_{\text{budget}}=10\,P_{0}t_{0}$.

Substituting into the bound:
$$\tau_{\text{exc}}=\frac{10\,P_{0}t_{0}}{P_{0}(0.5-0.09)}=\frac{10}{0.41}\,t_{0}=24.39\,t_{0}.$$

### 4.4 Global optimum under a power ceiling

An earlier version of this analysis [8] reported a duty-cycled optimum with $f=0.51220$ and $\bar{U}=0.168\,N_{0}$. That result is correct as an arithmetic matter but is not the global optimum: allowing the optimizer to choose a single setpoint under the same average-power constraint yields a higher utility, and a concavity argument proves no cycle can beat it.

**Single setpoint.** The constraint $\bar{P}=0.3\,P_{0}$ with a single operating point $\Gamma$ gives
$$P_{0}\Gamma^{2}=0.3\,P_{0}\quad\Longrightarrow\quad \Gamma=\sqrt{0.3}\approx0.547722.$$
Utility at this setpoint is
$$U(\Gamma)=N_{0}\,\Gamma^{2}\bigl(1-\Gamma^{2}\bigr)=N_{0}\,(0.3)\,(1-0.3)=0.21\,N_{0}.$$
The all-conservative strategy (permanent home point $\Gamma_{h}=0.3$) yields $U=N_{0}\cdot0.09\cdot0.91=0.0819\,N_{0}$, so the improvement factor is
$$\frac{0.21}{0.0819}=2.564\approx2.56\times.$$

**Duty-cycle benchmark.** Fix $\Gamma_{e}^{2}=0.5$, $\Gamma_{h}^{2}=0.09$, and solve the power constraint for $f$:
$$f\cdot0.5+(1-f)\cdot0.09=0.3\quad\Longrightarrow\quad 0.41\,f=0.21\quad\Longrightarrow\quad f=0.51220.$$
The average utility is
$$\bar{U}=f\,U(\Gamma_{e})+(1-f)\,U(\Gamma_{h})=0.51220\times0.25\,N_{0}+0.48780\times0.0819\,N_{0}.$$
Computing each term: $0.51220\times0.25=0.12805$ and $0.48780\times0.0819=0.03995$; summing, $\bar{U}=0.16800\,N_{0}$. This is a $0.168/0.0819=2.05\times$ improvement over conservatism, but strictly below the single-setpoint $0.21\,N_{0}$.

**Global optimality.** Write $x=\Gamma^{2}\in[0,1]$. The utility as a function of $x$ is $U(x)=N_{0}\,x(1-x)$, which is strictly concave in $x$ since $d^{2}U/dx^{2}=-2N_{0}<0$. Any duty-cycled schedule with average power $\bar{x}=f\,x_{e}+(1-f)\,x_{h}=0.3$ achieves average utility $f\,U(x_{e})+(1-f)\,U(x_{h})$, and Jensen's inequality for a concave function gives
$$f\,U(x_{e})+(1-f)\,U(x_{h})\;\le\;U\bigl(f\,x_{e}+(1-f)\,x_{h}\bigr)=U(0.3)=0.21\,N_{0},$$
with equality only when $x_{e}=x_{h}=0.3$, i.e. the single setpoint. Since $U(x)$ is increasing on $[0,0.5]$ and $0.3<0.5$, no feasible schedule can do better than $U(0.3)$: the single-setpoint solution is globally optimal for the memoryless model. The practical reading reverses the earlier claim: under this model, a designer with a power ceiling should hold a constant intermediate setpoint, not cycle between exploration and consolidation; cycling pays only if dynamics have memory or consolidation itself produces utility, neither of which the memoryless model represents.

### 4.5 Landauer floor

At $T=310\,$K, with Boltzmann constant $k_{B}=1.380649\times10^{-23}\,$J/K and $\ln2=0.693147$:
$$E_{\min}=k_{B}T\ln2=1.380649\times10^{-23}\times310\times0.693147\ \text{J}.$$
Step by step: $1.380649\times10^{-23}\times310=4.28001\times10^{-21}\,$J; then $4.28001\times10^{-21}\times0.693147=2.96661\times10^{-21}\,$J. Rounded to four significant figures,
$$E_{\min}=2.967\times10^{-21}\ \text{J per bit}.$$
This is a lower bound on the energetic cost of sustaining novelty; actual engineered systems will incur larger overheads.

### 4.6 Sensitivity analysis: quartic correction to coherence

We extend the coherence functional with a quartic term:
$$\Psi(\Gamma)=1-\Gamma^{2}+\beta\,\Gamma^{4},$$
where $\beta\ge0$ parametrizes the strength of the higher-order correction. The utility becomes
$$U(\Gamma)=N_{0}\,\Gamma^{\alpha}\bigl[1-\Gamma^{2}+\beta\,\Gamma^{4}\bigr].$$
Setting $\alpha=2$ for concreteness and differentiating:
$$\frac{dU}{d\Gamma}=N_{0}\Bigl[2\Gamma\bigl(1-\Gamma^{2}+\beta\Gamma^{4}\bigr)+\Gamma^{2}\bigl(-2\Gamma+4\beta\Gamma^{3}\bigr)\Bigr]=N_{0}\Gamma\Bigl[2-4\Gamma^{2}+6\beta\Gamma^{4}\Bigr].$$
Setting the bracket to zero and dividing by 2:
$$1-2\Gamma^{2}+3\beta\Gamma^{4}=0.$$
Treating this as a quadratic in $x=\Gamma^{2}$:
$$3\beta x^{2}-2x+1=0,\qquad x=\frac{2\pm\sqrt{4-12\beta}}{6\beta}.$$
Real, positive solutions exist only when the discriminant $4-12\beta\ge0$, i.e. $\beta\le\frac{1}{3}$. Taking the limit $\beta\to0$ of the root $x=\frac{2-\sqrt{4-12\beta}}{6\beta}$ yields $x\to0.5$, recovering the $\beta=0$ optimum $\Gamma^{2}=0.5$. As $\beta$ increases toward $1/3$, the numerator $2-\sqrt{4-12\beta}$ shrinks, pushing $x$ toward $1$—that is, the interior optimum migrates **toward the boundary** $\Gamma=1$, not toward $\Gamma=0$ as an earlier version of this paper stated [8]. At the critical value $\beta=1/3$, the discriminant vanishes and the only solution is $x=1$, so the interior optimum collapses onto the Gödelian boundary. For $\beta>1/3$, the derivative $dU/d\Gamma$ is positive for all $\Gamma\in(0,1]$, so utility increases monotonically and the maximum occurs at the boundary $\Gamma=1$; the interior optimum disappears. Physically, a positive quartic term makes coherence decay sub-quadratically at large $\Gamma$, so the model loses its interior penalty and the safe-operating-point result depends entirely on the quadratic term being