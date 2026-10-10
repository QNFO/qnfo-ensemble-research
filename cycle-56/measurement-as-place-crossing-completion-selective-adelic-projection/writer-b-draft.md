# Measurement as Place-Crossing: A Completion-Selective Adelic Projection Model of Quantum Measurement

## Abstract

We propose that the quantum measurement problem can be reframed as a *completion problem*. By Ostrowski's theorem, the field $\mathbb{Q}$ admits exactly one Archimedean completion $\mathbb{R}$ and countably many $p$-adic completions $\mathbb{Q}_p$; we conjecture that a quantum state is fundamentally an adelic object with coherent local factors at every place, and that measurement is a *place-crossing event*: coupling to a place-specific apparatus projects the state onto a single completion, suppressing all others. We formalize this with a Hilbert space over the adeles, a product-formula coherence condition, and a place-selective coupling operator whose Lindblad-type dynamics yields an explicit suppression equation for non-selected completions. We derive a concrete numerical result: for a two-place toy model with place-selective decoherence rates $\gamma_{\infty}$ and $\gamma_p$, the non-selected completion's weight decays as $e^{-\gamma t}$, and we compute the time at which coherence across places falls below $10^{-2}$ for representative rate ratios. We connect the framework to adelic path integrals, equidistribution of adelic measures, and continuous-measurement stochastic Schrödinger equations, and we outline a falsifiable simulation program for an adelic harmonic oscillator coupled to a place-specific bath. The framework is presented as a conjectural structural account, not a solved measurement problem; we state its limitations and failure modes explicitly.

## 1. Introduction

The measurement problem — why a superposition yields a single definite outcome — has resisted purely dynamical resolution in standard Hilbert-space quantum mechanics. Standard accounts (decoherence, collapse postulates, modal interpretations) all operate within a single Archimedean Hilbert space over $\mathbb{R}$ or $\mathbb{C}$. Yet number theory tells us that this Archimedean structure is not inevitable but *selected*: by Ostrowski's theorem, the completions of $\mathbb{Q}$ consist of exactly one Archimedean place and infinitely many non-Archimedean places $\mathbb{Q}_p$, and these topologies are mutually singular [9][10].

This paper develops a conjecture: the appearance of a single classical outcome is analogous to the appearance of a single completion. A quantum state is modeled as an adelic vector — a coherent product of local state vectors, one per place — and measurement is modeled as a *place-crossing*: the apparatus, being a macroscopic object embedded in one place's topology, couples selectively to that place's factor of the adelic state. Coherence across places is destroyed by this coupling, and the effective post-measurement state lives in the selected completion. The Born rule, in this picture, would be a theorem about the measure induced on the selected place by the adelic product structure, rather than a postulate.

Our contributions are: (i) a formal definition of an adelic Hilbert space with a product-formula coherence condition (Section 3); (ii) a place-selective coupling operator and a derived suppression equation with fully shown arithmetic for a two-place toy model (Sections 3–4); (iii) a concrete numerical derivation of the coherence-suppression timescale (Section 4); (iv) a simulation program for an adelic harmonic oscillator coupled to a place-specific bath, with explicit success criteria (Section 5); and (v) an honest accounting of what this framework does and does not solve (Section 6).

We emphasize at the outset that this is a *structural conjecture* in the lineage of Dragovich's adelic path integrals and the QNFO program on Archimedean artifacts [9][10][11]. No experiment described here has been performed; all quantitative claims are either derived here with shown arithmetic or explicitly labeled projections with stated assumptions.

## 2. Background and Related Work

**Adelic and arithmetic structures.** Ostrowski's theorem partitions the non-trivial absolute values of $\mathbb{Q}$ into the Archimedean one and the $p$-adic ones; the QNFO taxonomy work [9][10] argues that these completions are mutually singular as measure spaces and catalogues "measure-theoretic artifacts" — structures that exist only because physics has been formulated exclusively at the Archimedean place. Our proposal takes this diagnosis seriously and asks whether *measurement* is itself such an artifact: a place-selection event misdescribed as a collapse within one place. The Tate's-thesis template work [11] proposes that Tate's local-global factorization provides the structural skeleton for adelic quantum mechanics, noting that Dragovich's program has realized it for free theories and that Huang–Stoica–Zhong give a conformal-field-theory proof of concept. We adopt this template: our adelic Hilbert space (Section 3) is the state-space analogue of Tate's restricted product $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$.

Baker–Rumely, Favre–Rivera–Letelier, and Chambert-Loir proved arithmetic equidistribution of points of small height on the Berkovich projective line with respect to adelic measures [1]. This matters to us because equidistribution with respect to an *adelic* (not merely Archimedean) measure is the precise mechanism by which a measure concentrated at one place could emerge as a limit of globally defined objects; our Born-rule conjecture (Section 6) leans on exactly this style of result.

**Adelic quantum mechanics.** Dragovich's adelic harmonic oscillator [11, and the program it summarizes] constructs quantum-mechanical systems whose path integrals run over both Archimedean and $p$-adic domains, with the physical (Archimedean) sector recovered by an adelic product formula. Our Section 5 simulation target is directly this system, augmented with a place-specific bath.

**Measurement theory.** The axiomatic characterization of apparatus statistics via completely positive maps [3] shows that standard quantum mechanics already constrains what any measurement apparatus can do statistically; our model must reproduce these constraints at the selected place, which we take as a consistency requirement, not a competitor. The quantum Bayes principle approach [5] derives state reduction without the projection postulate, from the joint probability structure of successive local measurements — conceptually adjacent to our aim of deriving, rather than postulating, the effective projection. The definite-outcomes analysis of [6] demonstrates that entangled states are coherent superpositions of *nonlocal correlations* between incoherently mixed local states, so that even macroscopic subsystems need not carry definite local states; this supports our claim that definiteness is not a property of states but of *couplings* — in our language, of place-selection. Continuous-measurement theory via stochastic Schrödinger equations [2] provides the diffusive unravelling machinery we adapt in Section 3: our place-selective coupling generates a stochastic equation in which the "noise" is place-indexed, and the output-spectrum analysis of [2] is the natural tool for the simulation program's diagnostics. Quantum Turing machine foundations [4] characterize measurement, preparation, and halting as *local transition functions* on a discrete state space; the locality of these transitions is the computational analogue of our place-locality of apparatus coupling. Finally, the QFT measurement analysis [8] shows that joint nonlocal measurements generically produce signaling, i.e., that "measurement" is not a place-independent primitive even in standard physics; this is direct motivation for making the place-dependence of measurement explicit, as we do.

**Hardware context.** Superconducting quantum processors with high-fidelity readout [7] — e.g., 105-qubit devices with readout fidelity at the $10^{-2}$ error level — are the platforms where place-selective coupling would first be phenomenologically probed, since readout is precisely an apparatus-state coupling whose back-action is measurable.

## 3. Methods

### 3.1 Adelic Hilbert space

Let $\mathcal{P} = \{\infty, 2, 3, 5, \ldots\}$ be the set of places of $\mathbb{Q}$. For each $v \in \mathcal{P}$ let $\mathcal{H}_v$ be a separable Hilbert space over the local field $k_v$ ($k_{\infty} = \mathbb{R}$, $k_p = \mathbb{Q}_p$), carrying a representation $U_v$ of the local dynamics. Define the adelic state space as the restricted product

$$\mathcal{H}_{\mathbb{A}} = \mathcal{H}_{\infty} \times \prod_{p}' \mathcal{H}_p,$$

where the restricted product means that for almost all $p$ the local factor is in a fixed reference state $\lvert e_p \rangle$ (the analogue of Tate's integrality condition). A state is a vector $\lvert \Psi \rangle = \bigotimes_v \lvert \psi_v \rangle$ with the product-formula coherence condition:

$$\text{(PC)} \qquad \big\| \lvert \Psi \rangle \big\|_{\mathbb{A}}^2 = \prod_v \big\| \lvert \psi_v \rangle \big\|_v^2 = 1.$$

Condition (PC) is the adelic analogue of normalization and is the structural origin of our Born-rule conjecture: the global norm factorizes over places, so any place-selection induces a conditional probability equal to the local factor's norm, $\Pr(v_0) = \|\psi_{v_0}\|_{v_0}^2$ under uniform place weighting. We stress this is a conjecture about the correct place-prior, not a derivation.

### 3.2 Place-selective coupling

A measurement apparatus is modeled as a macroscopic degree of freedom $A_{v_0}$ localized at one place $v_0$. The coupling Hamiltonian is

$$H_{\text{int}} = \lambda \, \big( \Pi_{v_0} \otimes A_{v_0} \big),$$

where $\Pi_{v_0}$ projects onto the $v_0$-factor and $A_{v_0}$ is the apparatus observable. The induced master equation for the reduced adelic density matrix $\rho_{\mathbb{A}}(t)$, tracing out the apparatus, is postulated in Lindblad form with place-selective rates:

$$\frac{d\rho_{\mathbb{A}}}{dt} = -i[H_0, \rho_{\mathbb{A}}] + \sum_{v} \gamma_v \left( L_v \rho_{\mathbb{A}} L_v^{\dagger} - \frac{1}{2}\{L_v^{\dagger} L_v, \rho_{\mathbb{A}}\} \right),$$

where $L_v$ acts nontrivially only on the $v$-factor and $\gamma_v \geq 0$ is the coupling rate of the apparatus at place $v$. For an apparatus at $v_0$, we assume $\gamma_{v_0} = \gamma > 0$ and $\gamma_v = 0$ for $v \neq v_0$; the off-diagonal (cross-place coherence) element $\rho_{v_0, w}(t)$ between the selected place $v_0$ and any other place $w$ then obeys

$$\frac{d\rho_{v_0,w}}{dt} = -\frac{\gamma}{2}\, \rho_{v_0,w},$$

with solution $\rho_{v_0,w}(t) = \rho_{v_0,w}(0)\, e^{-\gamma t/2}$. This is the *completion-selective decoherence equation*: cross-place coherence dies exponentially, while the diagonal weight of the selected place is (to leading order) conserved, reproducing an effective projection onto the $v_0$-completion. The structure parallels the diffusive stochastic Schrödinger unravellings of continuous measurement [2], with the innovation that the unravelling index is a number-theoretic place rather than a measurement basis element.

### 3.3 Toy model

We take the minimal case: two places, $v_0 = \infty$ and $w = p$, each with a two-dimensional local factor, initial pure state

$$\lvert \Psi(0) \rangle = \alpha \lvert 1_{\infty} \rangle \lvert 1_p \rangle + \beta \lvert 0_{\infty} \rangle \lvert 0_p \rangle, \qquad |\alpha|^2 + |\beta|^2 = 1,$$

and an apparatus at the Archimedean place. All quantitative results below follow from this model and the rates $\gamma_{\infty} = \gamma$, $\gamma_p = 0$.

## 4. Analysis

We now derive the quantitative claims with every input and arithmetic step shown.

**Input 1 (structural).** From the master equation of Section 3.2 with $\gamma_{\infty} = \gamma$, $\gamma_p = 0$: the cross-place coherence element decays as

$$\rho_{\infty,p}(t) = \rho_{\infty,p}(0)\, e^{-\gamma t / 2}.$$

**Derivation 1 (coherence-suppression time).** We ask: at what time $t_{\varepsilon}$ has the cross-place coherence fallen to a fraction $\varepsilon$ of its initial magnitude? Setting

$$e^{-\gamma t_{\varepsilon}/2} = \varepsilon \quad \Longrightarrow \quad t_{\varepsilon} = \frac{2 \ln(1/\varepsilon)}{\gamma}.$$

For the representative threshold $\varepsilon = 10^{-2}$:

$$t_{10^{-2}} = \frac{2 \ln(10^{2})}{\gamma} = \frac{2 \times 4.60517}{\gamma} = \frac{9.21034}{\gamma}.$$

So the cross-place coherence falls below the $10^{-2}$ level at $t \approx 9.21/\gamma$. For example, if the apparatus coupling rate is $\gamma = 10^{6}\ \text{s}^{-1}$ (a typical laboratory-scale decoherence rate for a mesoscopic apparatus; this value is an *assumed input*, not a measurement), then

$$t_{10^{-2}} = \frac{9.21034}{10^{6}\ \text{s}^{-1}} = 9.21 \times 10^{-6}\ \text{s} \approx 9.2\ \mu\text{s}.$$

**Derivation 2 (suppression ratio at fixed time).** The ratio of surviving cross-place coherence to the selected place's diagonal weight at time $t$: with $\rho_{\infty,\infty}(0) = |\alpha|^2$ conserved to leading order and $\rho_{\infty,p}(0) = \alpha \beta^{*}$, the ratio is

$$R(t) = \frac{|\rho_{\infty,p}(t)|}{\rho_{\infty,\infty}(t)} = \frac{|\alpha \beta^{*}| e^{-\gamma t/2}}{|\alpha|^2} = \frac{|\beta|}{|\alpha|} e^{-\gamma t/2}.$$

For the balanced initial state $|\alpha| = |\beta| = 2^{-1/2}$ (so $|\beta|/|\alpha| = 1$) at $t = 9.21/\gamma$:

$$R\!\left(\frac{9.21}{\gamma}\right) = e^{-\gamma \cdot 9.21/(2\gamma)} = e^{-4.605} = 10^{-2}.$$

Arithmetic check: $e^{-4.605} = e^{-\ln(100)} = 1/100 = 10^{-2}$. ✓

**Derivation 3 (effective projection weight).** The selected place's diagonal weight evolves as $\rho_{\infty,\infty}(t) = |\alpha|^2$ (conserved under the dephasing-type Lindblad term, since $L_{\infty}$ is diagonal in the apparatus pointer basis). The unselected place's marginal weight is $\rho_{p,p}(t) = |\beta|^2$, unchanged by dephasing but *operationally inaccessible* from place $\infty$: any observable at place $\infty$ has expectation

$$\langle O_{\infty} \rangle = \mathrm{Tr}_{\infty}\big( \rho_{\infty,\infty}(t)\, O_{\infty} \big),$$

with no dependence on $\rho_{p,p}$. Thus the effective post-measurement state at place $\infty$ is the diagonal mixture with weights $\{|\alpha|^2, |\beta|^2\}$ — the Born-rule statistics *within* the selected place — while the cross-place quantum coherence has been exported to the apparatus/environment. This is the precise sense in which our model reproduces standard decoherence-based accounts [2][6] at the selected place while adding a structural claim about *which* place is selected.

**Derivation 4 (place-prior conjecture).** Under condition (PC) with the uniform place-prior conjecture, the probability of selecting place $v_0$ is $\Pr(v_0) = \|\psi_{v_0}\|_{v_0}^2$. For the toy model with $\|\psi_{\infty}\|_{\infty}^2 = |\alpha|^2 = 1/2$ and $\|\psi_p\|_p^2 = |\beta|^2 = 1/2$:

$$\Pr(\infty) + \Pr(p) = \frac{1}{2} + \frac{1}{2} = 1. \checkmark$$

The normalization of the place-prior is guaranteed by (PC); what is conjectural is the *uniformity* of the prior over places, which we flag as the framework's central open assumption (Section 6).

## 5. Results

We report only quantities derived in Section 4 or explicitly labeled projections.

**R1 (derived).** In the two-place toy model, cross-place coherence decays as $e^{-\gamma t/2}$ and falls below the $10^{-2}$ threshold at $t_{10^{-2}} = 9.21/\gamma$; for an assumed coupling rate $\gamma = 10^{6}\ \text{s}^{-1}$, this is $9.2\ \mu\text{s}$.

**R2 (derived).** The suppression ratio for a balanced initial state at $t = 9.21/\gamma$ is exactly $10^{-2}$.

**R3 (derived).** The selected place's outcome statistics are the diagonal weights $\{|\alpha|^2, |\beta|^2\}$, i.e., Born-rule-like within the selected completion, with cross-place coherence exported to the apparatus.

**R4 (projection, stated assumptions).** For the adelic harmonic oscillator of Dragovich's program coupled to a place-specific bath, we *project* — on the assumption that the bath coupling factorizes over places as in Section 3.2 and that the oscillator's adelic path-integral weights obey the product formula — that interference across places decays on the same timescale $t_{\varepsilon} = 2\ln(1/\varepsilon)/\gamma_{v_0}$. No simulation has been run; this is a design target with the success criterion that the simulated cross-place interference visibility fall below $10^{-2}$ within $10/\gamma_{v_0}$ and that the selected place's histogram match the local Born weights to within statistical uncertainty set by the number of sampled trajectories $N$ (standard error $\approx 1/\sqrt{N}$; e.g., $N = 10^{4}$ gives $\approx 10^{-2}$).

**R5 (projection, hardware context).** On superconducting platforms with readout error at the $10^{-2}$ level [7], the place-selection timescale would need to satisfy $t_{10^{-2}} \lesssim$ the readout duration to be phenomenologically consistent; with readout durations of order $10^{-7}$–$10^{-6}$ s typical of such devices, this requires $\gamma \gtrsim 9.21/(10^{-6}\ \text{s}) \approx 9.2 \times 10^{6}\ \text{s}^{-1}$. This is a consistency bound derived from the assumed $\gamma$, not a measurement.

## 6. Discussion

**What is solved and what is not.** The model derives an effective projection *within* the selected place by standard dephasing dynamics — this is not new relative to decoherence theory [2][6]. The new structural claim is the *selection of the place itself*, and here the framework is weakest: the uniform place-prior of Derivation 4 is a conjecture, and we have no dynamics that selects the Archimedean place over a $p$-adic one. If the prior is not uniform, the Born-rule analogy fails or requires a weighted prior whose origin is unexplained — arguably relocating rather than solving the measurement problem.

**Limitations and failure modes.** (i) The Lindblad postulate for place-selective coupling is an ansatz; a derivation from an underlying adelic unitary dynamics is absent. (ii) The restricted product requires almost all local factors to sit in a reference state; the dynamics of *leaving* the reference state (i.e., how a place becomes "active") is unspecified. (iii) The model is nonrelativistic; the QFT no-signaling constraints [8] suggest that place-selective measurements must respect locality, and an adelic version of microcausality is undeveloped. (iv) The equidistribution results for adelic measures [1] suggest a mechanism for place-emergence but have not been connected to dynamics here. (v) All rates are assumed inputs; no experimental signature distinguishes this model from ordinary decoherence at the selected place, since R3 is operationally identical to standard decoherence from within one place.

**What would falsify the claims.** The framework is falsified if (a) a consistent adelic unitary dynamics exists that does *not* factorize over places, breaking condition (PC); (b) the simulation program of R4 shows cross-place interference persisting at strong place-specific coupling; or (c) the place-prior conjecture leads to observable violations of Born statistics within the Archimedean place, which are not seen. Conversely, any observable deviation of readout statistics from standard predictions on platforms like [7] would be evidence *for* place-structure, but we predict none, making the framework currently empirically equivalent to decoherence — a serious weakness we acknowledge.

**Open questions.** What selects the Archimedean place in practice — is it the apparatus's own number-theoretic constitution, or a global boundary condition? Does the Langlands-type local-global machinery [11] constrain the allowed couplings $\gamma_v$? Can the equidistribution theorems [1] be repurposed to derive the place-prior dynamically?

## 7. Conclusion

We have reframed quantum measurement as a completion problem: an adelic state evolves coherently across all places of $\mathbb{Q}$, and measurement is a place-crossing event in which a place-specific apparatus suppresses cross-place coherence on the timescale $t_{\varepsilon} = 2\ln(1/\varepsilon)/\gamma$, yielding Born-rule-like statistics within the selected completion. The framework is structurally motivated by Ostrowski's theorem, the adelic quantum-mechanics program, and the equidistribution theory of adelic measures, and it is operationalizable as a simulation program on the adelic harmonic oscillator. Its central conjecture — the place-prior — remains open, and the framework is presently empirically equivalent to decoherence theory; its value is structural, offering a number-theoretic vocabulary for the selection event that standard accounts leave unformalized.

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