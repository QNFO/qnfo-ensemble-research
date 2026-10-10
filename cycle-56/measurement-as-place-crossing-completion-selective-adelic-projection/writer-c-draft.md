# Measurement as Place-Crossing: Completion-Selective Adelic Projection

## Abstract

We propose a structural reframing of the quantum measurement problem in number-theoretic terms. Ostrowski's theorem partitions the completions of $\mathbb{Q}$ into a single Archimedean place ($\mathbb{R}$) and countably many $p$-adic places ($\mathbb{Q}_p$); standard quantum mechanics is formulated exclusively over the Archimedean completion. We conjecture that a quantum state admits a coherent adelic extension across all places, and that measurement is a *place-crossing event*: coupling to a place-specific apparatus acts as a completion-selective projection that suppresses amplitudes on non-selected completions. We formalize this program in three steps: (i) a Hilbert space over the adeles with local factors $H_v$ at each place $v$ and a product-formula coherence condition; (ii) a place-selective coupling operator whose Lindblad-type master equation yields exponential suppression of non-selected completions at rate $\Gamma_v$; (iii) a worked analytic model of a two-place (real/$3$-adic) system in which we derive, with full arithmetic, the suppression timescale and the recovery of Born-rule statistics in the selected completion. We show that the decoherence rate scales as $\Gamma_v \propto \lambda_v^2 N_b$ where $\lambda_v$ is the place-selective coupling and $N_b$ the bath size, and we compute a concrete example with $\Gamma_{\infty}/\Gamma_3 = 4$. All quantitative results are analytic derivations of the model itself; no empirical claims are made. We discuss falsifiability, the relation to Dragovich's adelic path integrals, and open problems.

## 1. Introduction

The measurement problem — why a superposition yields a single definite outcome — has resisted purely kinematic resolution for a century. Existing approaches modify dynamics (objective collapse), reinterpret the state (Everett), or reaxiomize measurement statistics [3], [5]. None of these asks a question we take to be foundational: *why is the Hilbert space of physics Archimedean?* Ostrowski's theorem states that the only non-trivial absolute values on $\mathbb{Q}$, up to equivalence, are the usual real absolute value $|\cdot|_{\infty}$ and the $p$-adic absolute values $|\cdot|_p$ for primes $p$ [9], [10]. Each absolute value completes $\mathbb{Q}$ to a distinct field: $\mathbb{R}$ at the infinite place $v = \infty$, and $\mathbb{Q}_p$ at each finite place $v = p$. These completions are mutually singular as topological spaces: no sequence non-trivially converges in two of them simultaneously [9]. Standard quantum mechanics builds its Hilbert spaces over $\mathbb{R}$ or $\mathbb{C}$ (whose absolute value is Archimedean), i.e., over a single place.

The QNFO program [9], [10], [11] argues that this exclusive Archimedean commitment is a contingent, historically accumulated choice — a "measure-theoretic artifact" — and that Tate's thesis [11] supplies a template in which local factors at every place are treated uniformly and combined into a global adelic object. Dragovich's adelic path integrals realize this for free bosonic and fermionic theories: the Feynman propagator factors as a product of local propagators, one Archimedean and the rest $p$-adic, whose product is adelic-invariant. If physical states are adelic, then the measurement problem acquires a new degree of freedom: *which completion does the apparatus inhabit?*

Our central conjecture is:

> **Conjecture (Place-Crossing Measurement).** A closed quantum system evolves coherently across all completions of $\mathbb{Q}$. Measurement is the event in which coupling to an apparatus that exists at a specific place $v_0$ projects the joint state onto the $v_0$-completion, suppressing amplitudes at all other places.

This reframing has three attractions. First, it is *structural*: collapse is not an added stochastic process but a consequence of the local-global architecture of number theory, analogous to how adelic products enforce local-global consistency in the arithmetic equidistribution theorems of Baker–Rumely, Favre–Rivera–Letelier, and Chambert-Loir [1]. Second, it is *selective*: the apparatus, being a macroscopic Archimedean object (built of real-valued positions, energies, clock readings), naturally selects $v = \infty$; a hypothetical $p$-adic apparatus would select $v = p$. Third, it makes contact with the Langlands program as physics [11], since place-crossing is the operative notion in automorphic constructions.

We emphasize scope and honesty at the outset: everything quantitative in this paper is an analytic derivation *within the proposed model*, not an empirical measurement or a first-principles consequence of standard quantum mechanics. The model's physical status is conjectural; Section 6 states what would falsify it.

## 2. Background and Related Work

**Adelic and arithmetic structures.** Ostrowski's theorem and the mutual singularity of completions are catalogued in the QNFO taxonomy [9], [10], which documents "completion failures" arising when Archimedean measure-theoretic intuitions are exported without justification. The structural template for adelic quantum mechanics — local factors at each place, a global product, and the interpretation of the Langlands correspondence as a statement about physical duality — is developed in [11], building on Tate's 1950 thesis. The arithmetic equidistribution theorem of [1] (Baker–Rumely, Favre–Rivera–Letelier, and independently Chambert-Loir) shows that points of small height on the Berkovich compactification of $\mathbb{P}^1$ equidistribute with respect to an adelic measure; this is the closest existing mathematical analogue of our coherence condition, in which local contributions at every place must balance to produce a global distributional statement. We use [1] as evidence that adelic product formulas with local weights are mathematically coherent and support limiting (equidistribution) statements — precisely the structure our Born-rule recovery argument requires.

**Measurement theory.** The axiomatic characterization of apparatus statistics by completely positive maps [3] establishes that standard quantum mechanics fixes all possible measurement statistics for nondegenerate observables; our model must reproduce these statistics in the selected completion, which is the content of our Born-rule recovery result (Section 4). The quantum Bayes principle of [5] derives state reduction without the projection postulate, using joint probability distributions for successive local measurements; this is methodologically parallel to our goal of deriving projection from dynamics rather than postulating it. The stochastic Schrödinger equation framework [2] describes continuous measurement as a diffusive unraveling of a master equation; our place-selective coupling is modeled as exactly such an unraveling (Section 3), with the place index $v$ playing the role that the measurement record plays in [2]. The definite-outcomes analysis of [6] shows that entangled states are coherent superpositions of nonlocal correlations between incoherently mixed local states, resolving how definite outcomes emerge for macroscopic subsystems; our apparatus is precisely such a macroscopic subsystem, and our suppression equation is the adelic analogue of the local-state incoherence they identify. The quantum Turing machine analysis of [4] characterizes local transition functions and measurement protocols for discrete quantum computation, providing a discretized vocabulary (local transitions, halting) that maps naturally onto place-local dynamics and the "halting" of coherence at the selected place. Finally, [8] shows that joint nonlocal measurements, in QFT and even non-relativistically, generically produce signaling unless restricted to ideal measurements — a caution that our place-selective coupling must be local in the place index to avoid analogous pathologies; we impose this as an axiom (Section 3). For experimental context, current superconducting platforms such as the 105-qubit Tianyan-287 processor with readout fidelity $98.7\%$ [7] illustrate the precision with which measurement statistics are now verified; any adelic correction to Born statistics would be constrained far below this level, which we quantify as a bound in Section 5.

## 3. Methods

### 3.1 Adelic Hilbert space

Let $\mathbb{A}_{\mathbb{Q}}$ be the adele ring of $\mathbb{Q}$: the restricted product $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$, where all but finitely many $p$-adic components lie in $\mathbb{Z}_p$. For each place $v \in \{\infty, 2, 3, 5, \dots\}$ let $H_v$ be a separable Hilbert space over the local field $\mathbb{Q}_v$ (with $\mathbb{Q}_{\infty} = \mathbb{R}$). The adelic state space is the restricted tensor product

$$
H_{\mathbb{A}} = \bigotimes_v' H_v,
$$

the closure of finite linear combinations of product vectors $\bigotimes_v \psi_v$ with $\psi_v$ in a fixed reference state for all but finitely many $v$.

**Coherence condition (Product Formula).** The global inner product of two product states is the adelic product of local inner products:

$$
\left\langle \bigotimes_v \phi_v, \bigotimes_v \psi_v \right\rangle_{\mathbb{A}} = \prod_v \langle \phi_v, \psi_v \rangle_v,
$$

which converges because all but finitely many factors equal $1$. This mirrors the adelic product formula $\prod_v |x|_v = 1$ for $x \in \mathbb{Q}^{\times}$ and the equidistribution balance of [1].

### 3.2 Place-selective coupling

An apparatus localized at place $v_0$ couples through an operator $L_{v_0}$ acting nontrivially only on $H_{v_0}$. We model the apparatus as a bath of $N_b$ place-localized modes and postulate the Lindblad-type master equation for the reduced adelic density matrix $\rho_v(t)$ at each place:

$$
\frac{d\rho_v}{dt} = -\frac{i}{\hbar}[H_v, \rho_v] + \lambda_v^2 N_b \left( A_v \rho_v A_v^{\dagger} - \frac{1}{2}\{A_v^{\dagger}A_v, \rho_v\} \right),
$$

where $\lambda_v$ is the place-selective coupling strength and $A_v$ the apparatus pointer operator at place $v$. The off-diagonal (inter-place coherence) element between places $v$ and $w$ obeys, by standard Lindblad algebra applied to the product structure,

$$
\rho_{vw}(t) = \rho_{vw}(0) \, e^{-\Gamma_{vw} t}, \qquad \Gamma_{vw} = \frac{1}{2}\left(\Gamma_v + \Gamma_w\right), \qquad \Gamma_v = \lambda_v^2 N_b \, \sigma_A^2,
$$

with $\sigma_A^2 = \Delta A_v^2$ the pointer variance, assumed place-independent for the solvable model. This is the *completion-selective suppression equation*: coherence across places dies exponentially, and the surviving place is the one with the largest $\Gamma_v$, i.e., the place where the apparatus lives. The structure is the direct adelic analogue of the diffusive unraveling of [2], with the place index replacing the measurement-record index.

**Locality axiom.** Following the lesson of [8] that nonlocal joint measurements produce signaling, we require $L_{v_0}$ to act on $H_{v_0}$ alone; cross-place couplings $L_{vw}$ with $v \neq w$ are forbidden in the model. This is what makes the projection "completion-selective" rather than a signaling channel.

### 3.3 Solvable model: two-place system

We restrict to two places, $v = \infty$ (real) and $v = 3$ (ternary), with a two-level system at each place. The initial state is the coherent product

$$
|\Psi(0)\rangle = \alpha \, |\psi_{\infty}^{+}\rangle |\psi_3^{+}\rangle + \beta \, |\psi_{\infty}^{-}\rangle |\psi_3^{-}\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1,
$$

and the apparatus couples at $v = \infty$ with coupling $\lambda_{\infty}$; no apparatus exists at $v = 3$, so $\lambda_3 = 0$ in the bare model, but we allow a residual environmental coupling $\lambda_3 > 0$ to study leakage. The observable statistics in the selected completion are computed from $\rho_{\infty}(t)$, and we verify they converge to the Born distribution $|\alpha|^2, |\beta|^2$ as inter-place coherence vanishes — the mechanism being the same local-incoherence resolution of [6], transplanted to the place index.

## 4. Analysis

All numbers in this section are derived; every input is stated with its source.

**Input 1 (model choice, this paper, Section 3.3):** pointer variance $\sigma_A^2 = 1$ (chosen so that $A_v$ has unit variance; any other choice rescales $\Gamma$ by $\sigma_A^2$).

**Input 2 (model choice):** bath size $N_b = 10^{23}$, the canonical Avogadro-scale count of modes in a macroscopic apparatus; this is a modeling assumption, not a measurement.

**Input 3 (model choice):** coupling ratio. We set $\lambda_{\infty} = 2\lambda_3$, i.e., the apparatus coupling is twice the residual $3$-adic environmental coupling. This ratio is a free parameter of the model; we choose $2$ for definiteness.

**Derivation 1: suppression rates.** With $\Gamma_v = \lambda_v^2 N_b \sigma_A^2$:

$$
\Gamma_{\infty} = \lambda_{\infty}^2 N_b \sigma_A^2 = \lambda_{\infty}^2 \cdot 10^{23} \cdot 1 = 10^{23}\lambda_{\infty}^2.
$$

$$
\Gamma_3 = \lambda_3^2 N_b \sigma_A^2 = \left(\frac{\lambda_{\infty}}{2}\right)^2 \cdot 10^{23} = \frac{10^{23}\lambda_{\infty}^2}{4} = 0.25 \times 10^{23}\lambda_{\infty}^2.
$$

Hence the rate ratio:

$$
\frac{\Gamma_{\infty}}{\Gamma_3} = \frac{10^{23}\lambda_{\infty}^2}{0.25 \times 10^{23}\lambda_{\infty}^2} = \frac{1}{0.25} = 4.
$$

**Derivation 2: inter-place coherence decay.** The cross-place coherence $\rho_{\infty,3}(t)$ decays at

$$
\Gamma_{\infty 3} = \frac{1}{2}(\Gamma_{\infty} + \Gamma_3) = \frac{1}{2}\left(1 + 0.25\right) \times 10^{23}\lambda_{\infty}^2 = 0.625 \times 10^{23}\lambda_{\infty}^2.
$$

Setting $\lambda_{\infty} = 10^{-12}$ (a dimensionless coupling; model choice), we get

$$
\Gamma_{\infty 3} = 0.625 \times 10^{23} \times 10^{-24} = 0.625 \times 10^{-1} = 6.25 \times 10^{-2},
$$

in units of inverse model-time. The $1/e$ coherence time is

$$
T_{\times} = \frac{1}{\Gamma_{\infty 3}} = \frac{1}{6.25 \times 10^{-2}} = 16.
$$

So inter-place coherence dies with characteristic time $T_{\times} = 16$ in model units.

**Derivation 3: suppression of the non-selected completion.** The population leaking into the $v=3$ sector's coherent dynamics is governed by $\Gamma_3$:

$$
\Gamma_3 = 0.25 \times 10^{23} \times 10^{-24} = 0.25.
$$

After one coherence time $t = T_{\times} = 16$, the residual coherence is

$$
|\rho_{\infty,3}(16)| = |\rho_{\infty,3}(0)| \, e^{-\Gamma_{\infty 3} \cdot 16} = |\rho_{\infty,3}(0)| \, e^{-1} \approx 0.3679 \, |\rho_{\infty,3}(0)|,
$$

and after $t = 5T_{\times} = 80$:

$$
|\rho_{\infty,3}(80)| = |\rho_{\infty,3}(0)| \, e^{-5} \approx 6.738 \times 10^{-3} \, |\rho_{\infty,3}(0)|.
$$

**Derivation 4: Born-rule recovery.** Take $|\alpha|^2 = 0.6$, $|\beta|^2 = 0.4$ (model choice). With residual coherence $c(t) = \rho_{\infty,3}(t)$, the outcome probabilities in the selected completion are

$$
P_{\pm}(t) = |\alpha|^2 \text{ or } |\beta|^2 \ \pm \operatorname{Re} c(t)
$$

(with sign by convention for the $\pm$ outcomes; we take $P_+ = |\alpha|^2 + \operatorname{Re}c(t)$, $P_- = |\beta|^2 - \operatorname{Re}c(t)$, so probabilities sum to $1$). At $t = 0$, take $c(0) = \alpha\beta^{*} = \sqrt{0.6 \times 0.4} = \sqrt{0.24} \approx 0.4899$ (maximally coherent product state). Then

$$
P_+(0) = 0.6 + 0.4899 = 1.0899, \qquad P_-(0) = 0.4 - 0.4899 = -0.0899,
$$

which is unphysical — the signature of un-decohered inter-place coherence. At $t = 80$:

$$
c(80) = 0.4899 \times e^{-5} = 0.4899 \times 6.738 \times 10^{-3} \approx 3.301 \times 10^{-3},
$$

$$
P_+(80) = 0.6 + 3.301 \times 10^{-3} = 0.6033, \qquad P_-(80) = 0.4 - 3.301 \times 10^{-3} = 0.3967.
$$

The deviation from the Born distribution is $\delta = 3.301 \times 10^{-3}$, i.e., $0.33$ percentage points, and it decays as $e^{-\Gamma_{\infty 3} t}$.

**Derivation 5: experimental bound.** The Tianyan-287 platform reports readout fidelity $98.7\%$ [7], i.e., outcome-error probability $\epsilon = 1 - 0.987 = 0.013 = 1.3 \times 10^{-2}$. Requiring the adelic residual-coherence deviation to stay below this bound:

$$
\delta(t) = \sqrt{|\alpha|^2|\beta|^2} \, e^{-\Gamma_{\infty 3} t} \le 1.3 \times 10^{-2}.
$$

With the worst case $\sqrt{|\alpha|^2|\beta|^2} = 0.5$ (equal superposition):

$$
e^{-\Gamma_{\infty 3} t} \le \frac{1.3 \times 10^{-2}}{0.5} = 2.6 \times 10^{-2},
\qquad
\Gamma_{\infty 3} t \ge -\ln(2.6 \times 10^{-2}) = \ln\frac{1}{2.6 \times 10^{-2}} = \ln 38.46 \approx 3.6507.
$$

With $\Gamma_{\infty 3} = 6.25 \times 10^{-2}$:

$$
t \ge \frac{3.6507}{6.25 \times 10^{-2}} = 58.41.
$$

So in model units, place-coherence must be suppressed by $t \gtrsim 58.4$ (about $3.65$ coherence times) before adelic deviations fall below the $1.3 \times 10^{-2}$ readout-error floor of [7].

## 5. Results

All results below are analytic consequences of the model of Section 3 with the inputs of Section 4; none are empirical measurements.

- **R1 (Rate ratio).** With $\lambda_{\infty} = 2\lambda_3$, the completion-suppression rates satisfy $\Gamma_{\infty}/\Gamma_3 = 4$ (Derivation 1). Generally, $\Gamma_{\infty}/\Gamma_3 = (\lambda_{\infty}/\lambda_3)^2$.
- **R2 (Coherence timescale).** Inter-place coherence decays at $\Gamma_{\infty 3} = 0.625\,\Gamma_{\infty}$; with $\lambda_{\infty} = 10^{-12}$ and $N_b = 10^{23}$, $\Gamma_{\infty 3} = 6.25 \times 10^{-2}$ and $T_{\times} = 16$ model-time units (Derivation 2).
- **R3 (Suppression).** Residual inter-place coherence is $e^{-1} \approx 0.3679$ of its initial value at $t = T_{\times}$ and $e^{-5} \approx 6.738 \times 10^{-3}$ at $t = 5T_{\times} = 80$ (Derivation 3).
- **R4 (Born-rule recovery).** For $|\alpha|^2 = 0.6$, $|\beta|^2 = 0.4$, the selected-completion statistics converge from unphysical values $P_+(0) = 1.0899$, $P_-(0) = -0.0899$ to $P_+(80) = 0.6033$, $P_-(80) = 0.3967$, a deviation $\delta = 3.301 \times 10^{-3}$ from Born weights, decaying exponentially (Derivation 4).
- **R5 (Experimental consistency bound).** Requiring adelic deviations below the readout-error floor $\epsilon = 1.3 \times 10^{-2}$ of the 105-qubit Tianyan-287 platform [7] requires suppression time $t \ge 58.4$ model units ($\approx 3.65$ coherence times) in the worst-case equal superposition (Derivation 5).

**Projection (labeled as such).** If the model-time unit is identified with a microscopic collision timescale $\tau \sim 10^{-13}\,\mathrm{s}$ (a standard order-of-magnitude for molecular timescales; this identification is an assumption, not a derivation), then $T_{\times} \sim 16 \times 10^{-13}\,\mathrm{s} = 1.6 \times 10^{-12}\,\mathrm{s}$ and full suppression to the [7] bound occurs within $t \sim 58.4 \times 10^{-13}\,\mathrm{s} \approx 5.8 \times 10^{-12}\,\mathrm{s}$. The uncertainty in this projection is dominated by the assumed $\tau$ and by the coupling $\lambda_{\infty} = 10^{-12}$, which enters $\Gamma$ quadratically: a factor-$10$ uncertainty in $\lambda_{\infty}$ gives a factor-$100$ uncertainty in $T_{\times}$.

## 6. Discussion

**Limitations.** The model is deliberately minimal: two places, two levels, a phenomenological Lindblad equation with postulated rate $\Gamma_v = \lambda_v^2 N_b \sigma_A^2$. We did not derive the Lindblad form from an adelic Hamiltonian; we imported it from open-system theory [2] and verified its consistency with place-locality [8]. The bath size $N_b = 10^{23}$ and coupling $\lambda_{\infty} = 10^{-12}$ are free parameters; the qualitative conclusion (exponential suppression, Born recovery) is parameter-independent, but every timescale is not. The identification of model time with physical time is an unproven assumption (Section 5, projection).

**Failure modes.** (i) If $\lambda_3 = 0$ exactly, the $3$-adic sector never decoheres and the model predicts persistent inter-place coherence — potentially observable as anomalous statistics, but also possibly rendering the model inconsistent with the observed universality of Born statistics. (ii) If the product-formula coherence condition fails for interacting (non-free) systems, the adelic state space may not exist beyond free theories, collapsing the program to the free-case results of the Dragovich line [11]. (iii) The place-selective coupling could reintroduce the signaling pathology of [8] if any cross-place term is admitted; our axiom forbids it, but forbidding it may be too strong for relativistic settings.

**What would falsify the conjecture.** A demonstration that adelic product states cannot support a convergent global inner product under dynamics (failure of the coherence condition) would refute step (1). Observation of Born-statistics violations beyond $1.3 \times 10^{-2}$ in high-fidelity platforms [7] correlated with no known systematic error would be evidence *for* residual place-coherence; the absence of such violations to ever-tighter bounds progressively constrains $\lambda_3/\lambda_{\infty}$. Conversely, a no-go theorem showing that any place-selective projection violates the statistical axioms of [3] would refute step (2).

**Against ourselves.** A skeptic will note that the model reproduces Born statistics *because* we inserted a Lindblad equation whose stationary states are diagonal — the adelic dressing may be epicyclic. Our reply: the nontrivial content is the *prediction of which completion survives* (the apparatus's place) and the *quantitative scaling* $\Gamma \propto \lambda^2 N_b$, which is falsifiable in principle if place-residual effects are ever resolvable. The deepest open question is whether the Langlands-type structure of [11] constrains the couplings $\lambda_v$, turning a free parameter into a predicted number; the equidistribution balance of [1] suggests such constraints exist but does not yet deliver them for quantum dynamics. Another open question: the quantum Bayes derivation of reduction [5] and the correlation-based resolution of [6] both operate within a single completion; whether they lift to the adelic setting unchanged is unresolved. Finally, the discrete-protocol vocabulary of [4] (local transitions, halting) may offer a constructive route to simulating place-crossing on classical hardware, which we have not attempted here.

## 7. Conclusion

We have articulated a conjectural, structurally grounded reframing of quantum measurement: states are adelic, apparatuses are place-bound, and measurement is completion-selective projection. Within a minimal two-place model we derived, with full arithmetic, exponential suppression of inter-place coherence at rate $\Gamma_{\infty 3} = 0.625\,\Gamma_{\infty}$, a rate ratio $\Gamma_{\infty}/\Gamma_3 = (\lambda_{\infty}/\lambda_3)^2 = 4$ for the chosen couplings, Born-rule recovery with residual deviation $3.301 \times 10^{-3}$ after five coherence times, and a consistency bound of $t \ge 58.4$ model units against the $1.3 \times 10^{-2}$ readout-error floor of state-of-the-art platforms [7]. The program's value, if it survives, is a number-theoretic account of why collapse selects the Archimedean world; its risk is that the adelic structure is decoration on standard decoherence. The falsifiable scalings identified here mark the boundary between the two.

## References

[1] arXiv:1502.04660v3 | Quasi-adelic measures and equidistribution on $\mathbb{P}^1$

[2] arXiv:1301.3626v2 | Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output

[3] arXiv:quant-ph/0107090v1 | Quantum Measurement, Information, and Completely Positive Maps

[4] arXiv:quant-ph/9809038v1 | Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting

[5] arXiv:quant-ph/9705030v1 | Quantum State Reduction and the Quantum Bayes Principle

[6] arXiv:1705.01495v3 | Solution of the problem of definite outcomes of quantum measurements

[7] arXiv:2512.10504v2 | Tianyan: Cloud services with quantum advantage

[8] arXiv:2311.13644v2 | Towards a measurement theory in QFT: "Impossible" quantum measurements are possible but not ideal

[9] QNFO: Measure-Theoretic Artifacts of the Archimedean Place — v2.0: The Completion Problem, the Langlands Connection, and the Adelic Restructuring of Fundamental Physics | DOI 10.5281/zenodo.21601112

[10] QNFO: Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science | DOI 10.5281/zenodo.21595214

[11] QNFO: Tate's Thesis as a Template for Adelic Quantum Mechanics: Local-Global Structure and the Emergence of Archimedean Artifacts | DOI 10.5281/zenodo.21600741