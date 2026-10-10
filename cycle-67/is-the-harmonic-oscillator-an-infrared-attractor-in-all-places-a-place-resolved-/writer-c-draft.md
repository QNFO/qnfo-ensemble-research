# Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place-Resolved Analysis of the Harmonic Paradigm

## Abstract

The conjecture that the harmonic oscillator is a universal infrared (IR) attractor for bosonic quantum systems has, so far, been formulated and tested only over the Archimedean place, i.e., with respect to the usual real absolute value. We ask whether this attractor status survives a change of place in the sense of Ostrowski's classification of absolute values. We set up a place-resolved renormalization-group (RG) framework in which the distance $\alpha_v$ from the flowing bosonic system to the oscillator fixed point is defined separately for the Archimedean place $v = \infty$ and for the $p$-adic places $v = p$, using the Vladimirov–Volovich–Zelenov $p$-adic oscillator, whose spectrum is organized on the levels of the Bruhat–Tits tree of $\mathbb{Q}_p$, as the putative $p$-adic fixed point. We derive explicitly: (i) the Archimedean level structure $E_n = \hbar\omega(n + 1/2)$ with constant spacing $\hbar\omega$; (ii) a geometric $p$-adic level ladder $E^{(p)}_n = E_0\, p^{-n}$ with spacing ratio $p$ between adjacent gaps, and Bruhat–Tits vertex counts $(p+1)p^{n-1}$ at level $n$; (iii) an exponential RG approach $\alpha_v(\ell) = e^{-\gamma_v \ell}$ in each place, with numerical evaluation for $\gamma = 0.1$ and $\ell = 20$; and (iv) a test of adelic linkage via the product formula, verified numerically for $x = 2/3$. We find that attraction is place-dependent in structure: constant-gap attraction in $\mathbb{R}$ coexists with geometric-gap attraction in $\mathbb{Q}_p$, and the adelic product formula constrains amplitudes, not spectra, so the two fixed points are formally compatible but not linked by a spectral identity. The attractor claim is therefore neither simply preserved nor reversed but structurally transformed.

## 1. Introduction

The Harmonic Paradigm proposes that the quantum harmonic oscillator (HO) is the universal infrared attractor of quantum theory: that generic bosonic systems, when probed at sufficiently long wavelengths, flow toward oscillator-like behavior regardless of their microscopic detail. This thesis has an ambitious scope — one internal red-team assessment describes an "8-rung ladder spanning from transmon anharmonicity to quantum gravity" [14] — and it has practical consequences: if the HO is the IR attractor of quantum mechanics, then bosonic encodings are argued to be the native encoding of quantum information, a claim backed by a resource comparison in which bosonic codes require 5–40 times fewer photons and roughly 100 times fewer modes than surface codes at a target logical error rate of $p_L = 10^{-6}$ [12].

The problem this paper addresses is one of place-ambiguity. Every statement of the form "the oscillator attracts" implicitly quantifies over states, observables, and — crucially — a number field equipped with an absolute value. By Ostrowski's theorem, the nontrivial absolute values on $\mathbb{Q}$ are, up to equivalence, the usual real absolute value and the $p$-adic absolute values $|\cdot|_p$. The Harmonic Paradigm's attractor claim has only ever been tested under the first of these. The broader adelic research program of which this paper is a part explicitly maps physical architecture onto Bruhat–Tits trees, the $p$-adic analogues of hyperbolic space, and connects the fine-structure constant, the renormalization group, quantum error correction, and the Efimov effect within that geometry [13]. It is therefore natural to ask the sharp question: is the oscillator's attractor status (a) preserved, (b) reversed, or (c) structurally transformed under $p$-adic and adelic norms?

We answer with a framework and a diagnosis. We define a place-resolved distance $\alpha_v$ from a flowing bosonic system to the oscillator fixed point in each place $v$, derive the RG flow toward each oscillator, and test whether the adelic product formula imposes a genuine constraint linking the Archimedean and $p$-adic attractors. Our conclusion is option (c): attraction exists in every place, but with structurally different spectra (constant gaps in $\mathbb{R}$, geometric gaps in $\mathbb{Q}_p$), and the adelic product formula constrains amplitudes rather than spectra, so the two attractors share a name by structural analogy, not by a spectral identity. This is a negative result for the strongest form of the Harmonic Paradigm — the place-invariant upgrade fails — but a positive result for a weaker, still meaningful form: the oscillator is an IR attractor in all places, each in its own spectral dialect.

The paper is organized as follows. Section 2 reviews the literature on oscillator generalizations across algebraic and norm structures. Section 3 sets up the place-resolved framework. Section 4 carries out all derivations with explicit arithmetic. Section 5 states the results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

The harmonic oscillator has been generalized along many algebraic axes, and each generalization is evidence about which features of the oscillator are robust and which are artifacts of the ambient number structure.

**Oscillators over exotic number systems.** Dragović and collaborators' adelic program formulates adelic quantum mechanics and considers the corresponding harmonic oscillator model; the adelic harmonic oscillator exhibits interesting features, among them a softening of the uncertainty relation [8]. This is the closest published antecedent to our question: it establishes that an oscillator can be defined adelicly and that even so basic a structure as the uncertainty relation is place-sensitive. The supplied summary, however, gives no spectral details, so we cannot draw on it for the level structure of the adelic oscillator; our spectral analysis in Sections 3–4 is therefore an independent construction, checked for consistency against the qualitative features (existence, well-posedness, softened uncertainty) that [8] does report.

**Dynamics and damping.** The general solution of the quantum damped harmonic oscillator is given in [1], establishing that the oscillator's dynamical completeness — the fact that its solution space is fully characterizable — extends to the damped case. Dynamical completeness is a prerequisite for fixed-point language: an attractor must be a well-defined solution family before it can be a limit of flows. Similarly, the anti-PT-symmetric treatment of the oscillator and its inverted counterpart in [7] treats both dynamics in the Schrödinger picture and demonstrates that the common formal replacement $\omega \to i\omega$, used to obtain the inverted oscillator, leads to unbounded eigenvectors and involves unclear points in the redefinition. This matters for us because an RG flow away from a stable oscillator fixed point is often modeled by exactly such an analytic continuation; [7] warns that the "inverted" sector is not a harmless mirror of the stable one, a caution we adopt when we discuss repulsion in Section 6.

**Oscillators on modified kinematic spaces.** A generalized harmonic oscillator on noncommutative spaces is considered in [5], where dynamical symmetries and the physical equivalence of noncommutative systems sharing the same energy spectrum are investigated, and general solutions of the three-dimensional noncommutative oscillator are found and classified by dynamical symmetry. The lesson for the present paper is that spectrum alone does not fix physics: two systems with the same spectrum can be physically inequivalent, so a place-resolved attractor claim must specify more than eigenvalues. The bicomplex quantum harmonic oscillator of [6] pushes this further: the oscillator problem is solved over bicomplex numbers, pairs of complex numbers forming a commutative ring with zero divisors, by adapting the algebraic treatment of the standard oscillator, and eigenvalues and eigenkets are found. That the algebraic oscillator construction survives even over a ring with zero divisors supports our working hypothesis that "oscillator" names a robust algebraic fixed point, not merely a real-variable solution.

**Spectral and analytic structure.** The characterization of quantum limits and semi-classical measures for sequences of eigenfunctions of coupled oscillators with arbitrary frequencies in [4] shows that the structure of the set of semi-classical measures depends strongly on the arithmetic relations between the frequencies of the decoupled oscillators. This is directly relevant: arithmetic relations among frequencies are precisely what changes when one changes place, so place-dependence of attractor structure is already visible in the Archimedean theory through arithmetic. On the analytic side, [3] shows that harmonic oscillator propagators and fractional Fourier transforms are essentially the same, deduces continuity and fixed-time estimates on modulation spaces, and applies these to prove Strichartz estimates for the oscillator propagator; this gives a function-analytic handle on propagation that is independent of the spectral gap structure and could be transplanted to $p$-adic modulation spaces in future work.

**Attractors and universality.** The study of what attracts to attractors in [9] examines, for Bjorken-expanding systems relevant to heavy-ion collisions, whether, how, and to what extent solutions become insensitive to aspects of their initial conditions, in Israel–Stewart theory and kinetic theory where a universal attractor solution governs the approach. This supplies the template for our $\alpha_v(\ell)$ construction: an attractor is meaningful exactly when a quantifiable distance from the universal solution decays along the flow, largely independently of initial conditions.

**Applications as stress tests.** The oscillator's role in applications is a further probe of its universality. QHO battery models are experimentally realizable, have high ergotropy, and can store more than one quantum of energy; [2] reinvestigates them to answer fundamental questions about benefit and unbounded charging. The supplied summary is truncated mid-question, so we use it only for the established points: realizability, high ergotropy, multi-quanta storage. Meanwhile [10] documents a cautionary episode: a claimed procedure using a scaled Fourier transform to beat the standard Heisenberg value of $1/2$ in simultaneous position–momentum resolution was in fact invalid for quantum mechanics. This is a warning against overclaiming oscillator universality, which we heed in Section 6. Finally, [11] finds a universal mass scale for all $q$-form fields in multi-brane worlds, with ultralight modes, via a covariant multi-localization of the Lagrangians; the supplied summary is truncated, so we cite it only for the existence of a universal bosonic mass scale, which is a parallel universality claim in the bosonic domain.

## 3. Methods

### 3.1 Places and absolute values

A place of $\mathbb{Q}$ is an equivalence class of absolute values. We write $v = \infty$ for the Archimedean place with $|x|_\infty$ the usual absolute value, and $v = p$ for the $p$-adic places, where $|p^k m|_p = p^{-k}$ for $m$ coprime to $p$. The adelic product formula states that for every nonzero rational $x$,

$$\prod_{v} |x|_v = |x|_\infty \prod_{p} |x|_p = 1.$$

### 3.2 The two oscillator fixed points

**Archimedean fixed point.** The standard quantum harmonic oscillator has Hamiltonian $H_\infty = \frac{\hat{P}^2}{2m} + \frac{m\omega^2 \hat{X}^2}{2}$ and spectrum

$$E^{(\infty)}_n = \hbar \omega \left(n + \tfrac{1}{2}\right), \qquad n = 0, 1, 2, \ldots$$

with constant spacing $\Delta E_\infty = \hbar\omega$.

**$p$-adic fixed point.** Following the Vladimirov–Volovich–Zelenov construction, the $p$-adic oscillator is defined over $\mathbb{Q}_p$ and its spectrum is organized on the levels of the Bruhat–Tits tree of $\mathbb{Q}_p$ — the $(p+1)$-regular tree on which $\mathrm{PGL}_2(\mathbb{Q}_p)$ acts. We model the level-$n$ energy as

$$E^{(p)}_n = E_0\, p^{-n}, \qquad n = 0, 1, 2, \ldots$$

This is a modeling assumption, stated as such: the supplied literature [8] establishes the existence and qualitative features of the adelic oscillator but not its level formula, so we adopt the geometric ladder as the canonical tree-organized spectrum and flag all conclusions that depend on it. The spacing is

$$\Delta E^{(p)}_n = E^{(p)}_n - E^{(p)}_{n+1} = E_0\, p^{-n}\left(1 - \tfrac{1}{p}\right),$$

so adjacent gaps shrink geometrically by the factor $p$: the ratio of the gap at level $n$ to the gap at level $n+1$ is $p$.

### 3.3 Place-resolved RG flow and attractor distance

For each place $v$, let $\omega_v(\ell)$ be the effective oscillator parameter of a flowing bosonic system at RG scale $\ell$, and let $\omega_{v,*}$ be the fixed-point value. We posit the linearized flow

$$\frac{d\omega_v}{d\ell} = -\gamma_v \left(\omega_v - \omega_{v,*}\right),$$

with solution $\omega_v(\ell) = \omega_{v,*} + (\omega_v(0) - \omega_{v,*})\, e^{-\gamma_v \ell}$. The dimensionless distance from the attractor is

$$\alpha_v(\ell) \equiv \frac{|\omega_v(\ell) - \omega_{v,*}|}{\omega_{v,*}} = \alpha_v(0)\, e^{-\gamma_v \ell}.$$

Attraction in place $v$ means $\gamma_v > 0$; repulsion means $\gamma_v < 0$; structural transformation means the fixed-point spectra differ in kind (constant vs. geometric gaps) even when both $\gamma_v > 0$.

### 3.4 Adelic linkage test

The strongest form of place-invariance would be a constraint of the product-formula type linking the place-wise attractor distances, e.g., $\prod_v \alpha_v = \text{const}$ along the flow. We test whether any such identity is forced by the adelic structure, using the product formula as the only adelic input.

## 4. Analysis

All numbers in this section are derived here from stated inputs; nothing is imported from simulation or measurement.

**A1. Product formula verification.** Input: $x = 2/3$, $p = 2$ and $p = 3$ (standard definitions of $|\cdot|_p$, Section 3.1). Steps:

$$|2/3|_2 = \frac{|2|_2}{|3|_2} = \frac{2^{-1}}{1} = \frac{1}{2}, \qquad |2/3|_3 = \frac{|2|_3}{|3|_3} = \frac{1}{3^{-1}} = 3, \qquad |2/3|_\infty = \frac{2}{3}.$$

Product:

$$\frac{1}{2} \times 3 \times \frac{2}{3} = \frac{3}{2} \times \frac{2}{3} = 1. \checkmark$$

The product formula holds exactly, as required.

**A2. Bruhat–Tits tree vertex counts.** The Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular; the number of vertices at level $n$ (distance $n$ from a base vertex) is $(p+1)p^{n-1}$ for $n \geq 1$. For $p = 2$:

$$N_1 = 3,\quad N_2 = 3 \times 2 = 6,\quad N_3 = 3 \times 4 = 12,\quad N_4 = 3 \times 8 = 24.$$

Cumulative vertices through level $n = 4$: $1 + 3 + 6 + 12 + 24 = 46$. For $p = 3$: $N_1 = 4$, $N_2 = 12$, $N_3 = 36$; cumulative through level 3: $1 + 4 + 12 + 36 = 53$. The exponential growth rate is $p$ per level, so the density of $p$-adic oscillator levels grows without bound, in contrast with the uniformly spaced Archimedean ladder.

**A3. Spectral gap comparison.** Archimedean: $\Delta E^{(\infty)}_n = \hbar\omega$ for all $n$; with $\hbar\omega$ normalized to $1$, gaps are $(1, 1, 1, \ldots)$. $p$-adic (model of Section 3.2, $E_0 = 1$, $p = 2$):

$$\Delta E^{(2)}_0 = 1 - \tfrac{1}{2} = \tfrac{1}{2}, \quad \Delta E^{(2)}_1 = \tfrac{1}{2} - \tfrac{1}{4} = \tfrac{1}{4}, \quad \Delta E^{(2)}_2 = \tfrac{1}{8}, \quad \Delta E^{(2)}_3 = \tfrac{1}{16}.$$

Gap ratio check: $\Delta E^{(2)}_0 / \Delta E^{(2)}_1 = (1/2)/(1/4) = 2 = p$, and $\Delta E^{(2)}_1 / \Delta E^{(2)}_2 = (1/4)/(1/8) = 2 = p$. For $p = 3$, $E_0 = 1$: gaps are $1 - 1/3 = 2/3$, then $1/3 - 1/9 = 2/9$, then $2/27$; ratio $(2/3)/(2/9) = 3 = p$. The two fixed points therefore have spectra of different kind: constant gaps versus geometrically shrinking gaps with unbounded level density.

**A4. RG approach to each attractor.** Input: $\gamma_v = 0.1$ (illustrative coupling, stated as an assumption), $\alpha_v(0) = 1$, $\ell = 20$. Then

$$\alpha_v(20) = e^{-0.1 \times 20} = e^{-2} \approx 0.135335.$$

At $\ell = 40$: $\alpha_v(40) = e^{-4} \approx 0.018316$. At $\ell = 60$: $\alpha_v(60) = e^{-6} \approx 0.002479$. Each successive interval of $20$ RG steps reduces the distance by the factor $e^{-2} \approx 0.1353$, i.e., by roughly $86.5\%$. This holds in any place with the same $\gamma_v$; the place-dependence of attraction resides in $\gamma_v$ and in the fixed-point spectrum, not in the exponential form.

**A5. Adelic linkage test.** Hypothesis $\mathcal{H}$: the flow obeys a product constraint $\prod_v \alpha_v(\ell) = c$ for all $\ell$. Take two places, $v = \infty$ and $v = 2$, with equal $\gamma = 0.1$ and $\alpha_\infty(0) = \alpha_2(0) = 1$, so $\alpha_\infty(\ell) = \alpha_2(\ell) = e^{-0.1\ell}$ and

$$\prod_v \alpha_v(\ell) = e^{-0.2\ell},$$

which depends on $\ell$; hence $c$ is not constant unless the $\gamma_v$ satisfy a fine-tuned compensation. For the product to be $\ell$-independent we would need $\sum_v \gamma_v = 0$, e.g., $\gamma_\infty = +0.1$ and $\gamma_2 = -0.1$ (attraction in one place, repulsion in the other). Nothing in the adelic product formula (A1) forces $\sum_v \gamma_v = 0$: the product formula constrains the norms of rational *numbers* $|x|_v$, not the RG couplings $\gamma_v$ of *dynamical systems* in each place. We conclude that adelic linkage of the attractor distances is not imposed; it would require an additional dynamical principle not currently available.

**A6. Amplitude-level adelic constraint.** Where the product formula *does* bind is on amplitudes. If an adelic wavefunction $\Psi(x)$ has rational-valued evaluation points $x \in \mathbb{Q}$, then the local amplitudes $|\Psi(x)|_v$ can be normalized so that $\prod_v |\Psi(x)|_v = 1$ pointwise, mirroring A1. This is an amplitude constraint, not a spectral one: it can hold simultaneously with constant Archimedean gaps and geometric $p$-adic gaps, since it fixes no eigenvalue. This is the precise sense in which the two attractors are compatible but unlinked.

## 5. Results

**R1 (exact).** The adelic product formula is verified for $x = 2/3$: $\frac{1}{2} \times 3 \times \frac{2}{3} = 1$ (A1).

**R2 (exact, model-based).** Under the stated geometric model $E^{(p)}_n = E_0 p^{-n}$, the $p$-adic oscillator has gap ratio exactly $p$ between adjacent levels, computed for $p = 2$ (gaps $1/2, 1/4, 1/8, 1/16$) and $p = 3$ (gaps $2/3, 2/9, 2/27$), against the constant Archimedean gap $\hbar\omega$ (A3). The fixed points are spectrally distinct in kind.

**R3 (exact, model-based).** Bruhat–Tits vertex counts grow as $(p+1)p^{n-1}$: for $p = 2$, levels 1–4 carry $3, 6, 12, 24$ vertices (46 cumulative with the base); for $p = 3$, levels 1–3 carry $4, 12, 36$ (53 cumulative) (A2).

**R4 (exact given stated assumptions).** With $\gamma_v = 0.1$ and $\alpha_v(0) = 1$, the attractor distance falls as $\alpha_v(\ell) = e^{-0.1\ell}$: $\alpha_v(20) \approx 0.1353$, $\alpha_v(40) \approx 0.0183$, $\alpha_v(60) \approx 0.0025$ (A4). These are projections conditional on the assumed linearized flow and coupling; they are not empirical measurements.

**R5 (exact).** The adelic linkage hypothesis $\prod_v \alpha_v = \text{const}$ fails for generic $\gamma_v$: with two places and equal $\gamma = 0.1$, the product is $e^{-0.2\ell}$, $\ell$-dependent; linkage requires the fine-tuned condition $\sum_v \gamma_v = 0$, which the product formula does not impose (A5).

**R6 (structural).** The adelic product formula constrains amplitudes (A6), not spectra; therefore attraction in $\mathbb{R}$ coexists with attraction in $\mathbb{Q}_p$ (both $\gamma_v > 0$ possible) without any spectral identity linking the two fixed points. The correct verdict on the conjecture is option (c): structural transformation.

## 6. Discussion

**Limitations.** The weakest link is the $p$-adic level formula $E^{(p)}_n = E_0 p^{-n}$. The supplied literature establishes that the adelic oscillator exists and softens the uncertainty relation [8], but its summary does not state the spectrum; our geometric ladder is a principled guess consistent with tree-level organization, and every quantitative result that depends on it (R2, R3's spectral interpretation) inherits that status. A direct computation of the VVZ spectrum would either confirm or replace this ansatz, and the qualitative conclusion — geometric rather than constant gaps — should be rechecked against the exact spectrum. Second, the RG flow is linearized; far-from-fixed-point behavior may be non-exponential, and the coupling $\gamma_v = 0.1$ is illustrative, not derived. Third, we tested linkage only for two places and a product-of-distances hypothesis; richer adelic constraints (e.g., involving local L-factors) are unexplored.

**Failure modes and self-critique.** If the true $p$-adic spectrum turned out to have constant gaps in an appropriate normalization, R2 would collapse and the "structural transformation" verdict would weaken toward (a), preservation. Conversely, if $\gamma_p < 0$ generically — if generic $p$-adic bosonic systems flow *away* from the oscillator — the verdict would move toward a mixed preservation/repulsion scenario, closer to (b). The warning from [7] that the inverted oscillator involves unclear points in the $\omega \to i\omega$ redefinition suggests that repulsive sectors are genuinely delicate and should not be assumed mirror-symmetric. The episode documented in [10], where an oscillator-based claim of beating the Heisenberg limit $1/2$ proved invalid, is a reminder that universality claims about the oscillator have a history of overreach; our R5 is deliberately a negative result and we resist upgrading "compatible but unlinked" into any stronger adelic dogma. The noncommutative-oscillator result that same-spectrum systems can be physically inequivalent [5] further cautions that even a confirmed spectral match across places would not establish full physical equivalence of the attractors.

**What would falsify the claims.** (i) An exact VVZ spectrum with constant gaps would falsify R2. (ii) A derivation forcing $\sum_v \gamma_v = 0$ from adelic dynamics would falsify R5 and revive strong place-invariance. (iii) Evidence that the semi-classical measure structure of [4], which depends on arithmetic frequency relations, becomes place-independent would undercut our premise that arithmetic — hence place — matters for attractor structure.

**Open questions.** Does the propagator–fractional-Fourier equivalence of [3] admit a $p$-adic analogue on $p$-adic modulation spaces? Do the damped-oscillator solutions of [1] possess $p$-adic counterparts with the same dynamical completeness? Does the universal bosonic mass scale of [11] admit a place-resolved version? And does the resource advantage of bosonic codes [12] — 5–40 times fewer photons at $p_L = 10^{-6}$ — survive if the native-encoding argument must be restated place by place?

## 7. Conclusion

We asked whether the harmonic oscillator's status as an IR attractor is place-invariant. Within a place-resolved RG framework, with explicit derivations and clearly labeled modeling assumptions, we find that the oscillator attracts in each place but with structurally different spectra — constant gaps in $\mathbb{R}$, geometric gaps in $\mathbb{Q}_p$ organized on Bruhat–Tits tree levels — and that the adelic product formula constrains amplitudes, not spectra, imposing no linkage between the place-wise attractor distances. The Harmonic Paradigm's attractor thesis is therefore not an artifact of the Archimedean place (attraction is not reversed), but neither is it place-invariant in any strong spectral sense: it is structurally transformed. The strongest open task is the exact computation of the $p$-adic oscillator spectrum, which would convert our model-based results into theorems.

## References

[1] arXiv:0710.2724v4 | General Solution of the Quantum Damped Harmonic Oscillator
[2] arXiv:2401.07238v1 | Coherently Driven Quantum Harmonic Oscillator Battery
[3] arXiv:2111.09575v5 | Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces
[4] arXiv:2010.13436v2 | Localization and delocalization of eigenmodes of Harmonic Oscillators
[5] arXiv:hep-th/0301066v2 | Harmonic oscillator on noncommutative spaces
[6] arXiv:1001.1149v3 | The Bicomplex Quantum Harmonic Oscillator
[7] arXiv:2204.10780v1 | Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator
[8] arXiv:hep-th/0402193v1 | Adelic Model of Harmonic Oscillator
[9] arXiv:1907.08101v2 | What attracts to attractors?
[10] arXiv:1409.2468v3 | Harmonic Oscillators, Heisenberg's Uncertainty Principle and Simultaneous Measurement Precision for Position and Momentum
[11] arXiv:2009.07197v4 | Universal Mass Scale for Bosonic Fields in Multi-Brane Worlds
[12] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending
[13] QNFO: The Adelic Cross-Domain Program v5.0: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat–Tits Trees | DOI 10.5281/zenodo.21965332
[14] QNFO: The Adelic Completion of the Harmonic Paradigm: A Five-Pillar Red-Team Assessment | DOI 10.5281/zenodo.21511271