# Zitterbewegung as an Archimedean–2-adic Adelic Mixing Signature: Formalization, Numerical Anchors, and a Falsifiable Simulation Program

## Abstract

Zitterbewegung (ZBW) — the rapid trembling motion of a Dirac wave packet at angular frequency $\omega = 2mc^{2}/\hbar$ — is conventionally treated as an interference artifact of the Dirac Hamiltonian. We propose and partially formalize a stronger claim: ZBW is the observable trace of mixing between the Archimedean place $\mathbb{R}$ (denoted $\infty$) and the 2-adic place $\mathbb{Q}_2$ of the rational numbers, in the sense of adelic quantum mechanics. We (i) state a spectral-gap proposition showing that any operator coupling an $\infty$-localized sector to a $p$-adic sector forces an oscillation at $\Delta E/\hbar$; (ii) show via the adelic product formula that a nonzero Archimedean localization necessarily entails nontrivial $p$-adic norm structure for some prime $p$; (iii) derive the ZBW frequency numerically, $\omega_{\mathrm{ZBW}} \approx 1.55 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ for the electron, with full arithmetic; (iv) argue that the prime 2 is structurally distinguished because the Bruhat–Tits tree of $\mathbb{Q}_2$ is $3$-regular, the smallest degree any prime admits; and (v) specify a trapped-ion Dirac simulation test, labeled throughout as a projection, in which the Compton-scale oscillation amplitude is checked for correlation with a 2-adic delocalization measure. We report no new experimental data; all quantitative results are either computed here from stated constants or explicitly flagged as projections with stated assumptions.

## 1. Introduction

The position operator of relativistic quantum mechanics is notoriously ill-behaved: a wave-packet solution of the Dirac equation exhibits velocity eigenvalues $\pm c$ and a rapid oscillation at the Compton scale, named Zitterbewegung ("trembling motion") by Schrödinger [8]. The standard reading is that this trembling is an interference artifact of superposing positive- and negative-energy branches of the Dirac Hamiltonian, with no independent physical content.

This paper develops an alternative reading, taken from a research program on adelic physics [10, 11]: ZBW is a signature of mixing between the Archimedean place $\mathbb{R}$ and the 2-adic place $\mathbb{Q}_2$. In adelic quantum mechanics, wave functions may carry complex values on $p$-adic and adelic arguments, and the Archimedean and non-Archimedean places are treated on an equal footing [1]. Under this reading, a wave packet localized at an Archimedean position $x_{\infty}$ necessarily carries Fourier components that are delocalized on $\mathbb{Q}_2$, and the Compton-scale oscillation at $\omega = 2E/\hbar$ is the observable trace of the $\infty \leftrightarrow 2$ channel.

The claim matters because it would give a basis-independent, number-theoretic origin for a relativistic quantum phenomenon, and would connect mass-ratio numerology to the geometry of Bruhat–Tits trees. It is also falsifiable: if no other prime reproduces the observed frequency scaling, and if the oscillation amplitude in a controlled Dirac simulator fails to track a 2-adic delocalization measure, the claim fails.

Our contributions are:

1. **A spectral-gap proposition** (Section 3): any operator coupling an $\infty$-localized sector to a $p$-adic sector with off-diagonal energy scale $\Delta E$ forces oscillations at $\Delta E/\hbar$. This is elementary but makes the mixing claim precise enough to test.
2. **A necessity argument from the product formula** (Section 4): Archimedean localization cannot be "pure" in the adelic sense; some $p$-adic norm must be nontrivial.
3. **A structural-selection argument for $p = 2$**: the Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular, so $p = 2$ gives degree $3$, the smallest possible among primes.
4. **Explicit numerical anchors** (Section 4): the electron ZBW frequency, Compton wavelength, and 2-adic norm scales, all computed with shown arithmetic.
5. **A simulation protocol** (Sections 3 and 5), labeled as a projection: a trapped-ion Dirac simulator of the Gerritsma style, in which the Compton-scale oscillation amplitude is regressed against a 2-adic delocalization measure $\mu_2$.

We emphasize the epistemic status of each result: items 1–4 are mathematical derivations or computations from stated constants; item 5 is a design and a projection, not a measurement.

## 2. Background and Related Work

**Adelic and $p$-adic quantum mechanics.** Albeverio et al. [1] review the emergence of $p$-adic mathematical physics from attempts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and describe the successful formulation of $p$-adic and adelic quantum mechanics with complex-valued wave functions of $p$-adic and adelic arguments respectively. This is the mathematical framework in which our $\infty \leftrightarrow 2$ mixing channel is defined: the adelic wave function is a single object with an Archimedean factor and $p$-adic factors, so "mixing" between places is meaningful rather than a category error. Dragovich's review [2] surveys applications of non-Archimedean geometry, $p$-adic numbers, and adeles in modern mathematical physics; we use it as evidence that adelic methods are an established, if minority, toolset, and we note that its supplied summary is a brief review abstract giving no specific results we can lean on quantitatively.

**Arithmetic equidistribution and adelic measures.** Baker–Rumely, Favre–Rivera-Letelier, and Chambert–Loir established arithmetic equidistribution theorems for points of small height on the Berkovich compactification of $\mathbb{P}^1$ with respect to an adelic measure, as summarized in [3]. The relevance to us is methodological: adelic measures on projective spaces provide a rigorous way to speak about how mass distributes across places, which is exactly the bookkeeping our delocalization measure $\mu_2$ imitates at a toy level. The supplied summary of [3] describes the theorems but not their proofs' details, so we cite it only for the existence of this equidistribution framework.

**Fractal strings and complex dimensions.** Lapidus et al. [4] survey the theory of complex dimensions of real (Archimedean) fractal strings via the Cantor string and give a detailed survey of $p$-adic (non-Archimedean) fractal strings, including an explicit volume formula for the tubular neighborhood of a $p$-adic fractal string. This matters because the geometry of $\mathbb{Q}_2$-supported sets — ultrametric, self-similar, tree-like — is precisely the geometry our 2-adic sector lives on, and the complex-dimensions formalism is one of the few places where Archimedean and non-Archimedean fractal geometry are compared side by side.

**Arithmetic Hodge theory.** The arithmetic Hodge index theorem for adelic line bundles [5] extends results from number fields to finitely generated fields and yields a rigidity property of sets of preperiodic points of polarizable algebraic dynamical systems. We cite it as an example of the general pattern that adelic objects carry rigidity statements their local components lack — the same pattern our spectral-gap proposition instantiates locally: coupling to a $p$-adic sector constrains the Archimedean dynamics (forcing an oscillation) rather than merely decorating it.

**Adelic Lie theory.** The identity of finite-dimensional protori (finite-dimensional compact connected abelian groups) with adelic tori, together with a complete Lie theory including an adelic exponential sequence, is established in [6]. This supplies the group-theoretic language in which a "phase oscillation across places" can be stated: an adelic torus carries both an Archimedean circle factor and $p$-adic factors, and the exponential sequence governs how phases lift. The supplied summary of [6] states the categorical equivalence and the exponential sequence; we use no results beyond that.

**Non-Archimedean Hilbert-space geometry.** Welch bounds — inequalities on the coherence of frames — have been extended to continuous non-Archimedean and $p$-adic Banach and Hilbert spaces, with functional Zauner conjectures formulated in that setting [7]. For us this is a sanity check that the Hilbert-space formalism (inner products, frames, coherence bounds) survives the passage to $\mathbb{Q}_2$, which our model of a delocalized 2-adic sector requires.

**Zitterbewegung.** The historical and statistical-mechanics treatment of ZBW [8] records that around 1930 Breit and Schrödinger showed that the velocity eigenvalues of Dirac wave-packet solutions are $\pm c$, and that Schrödinger coined the term Zitterbewegung for the resulting trembling motion of fermions at the speed of light. The supplied summary is truncated mid-sentence ("The r…"), so we cannot cite it for any further results; we use it only for the historical framing above. Within the QNFO corpus, the Majorana ZBW current correlator result [9] shows that the reality condition forces a vanishing expectation value of the ZBW current correlator in free-field theory, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement — directly relevant because it shows ZBW observables can carry topological, not merely kinematic, content. The companion paper [10] locates the structural underdetermination of the relativistic position operator in a "Silent Parameter Principle," notes that $SU(2)$ and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels, and states that the 2-adic ZBW frequency deviates from the Archimedean value; its supplied summary is cut off before quantifying the deviation, so we treat the existence (not the magnitude) of that deviation as its claim. The program-level synthesis [11] consolidates a six-paper adelic physics chain — ZBW as a $p$-adic observable, Majorana correlators, Bruhat–Tits readout protocols, $p$-adic anyon braiding, and Ostrowski-based quantum error correction — into a unified research program; our paper is a sharpened, falsifiable fragment of that program. Finally, [12] reports that five independent research programs converge on the structural insight that ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization; we cite it as corpus-level motivation, not as evidence for any specific claim of ours.

## 3. Methods

### 3.1 Adelic setup

Let $\mathbb{A}_{\mathbb{Q}}$ be the adele ring of $\mathbb{Q}$, with places $\infty$ (Archimedean, $\mathbb{R}$) and primes $p$ ($\mathbb{Q}_p$). Following the adelic quantum-mechanics framework [1], a state is a complex wave function $\Psi = (\psi_{\infty}, \psi_2, \psi_3, \ldots)$ with $\psi_{\infty} \in L^2(\mathbb{R})$ and $\psi_p \in L^2(\mathbb{Q}_p)$. The Hilbert-space structure on each $L^2(\mathbb{Q}_p)$ is well defined [7], and the $p$-adic sector inherits ultrametric, tree-like geometry: the Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular [2, 4].

We work with a two-sector truncation, $\mathcal{H} = \mathcal{H}_{\infty} \oplus \mathcal{H}_2$, with a mixing Hamiltonian

$$
H = \begin{pmatrix} H_{\infty} & V \\ V^{\dagger} & H_2 \end{pmatrix}, \qquad V: \mathcal{H}_{\infty} \to \mathcal{H}_2 .
$$

### 3.2 Spectral-gap proposition

**Proposition (mixing forces oscillation).** Let $H_{\infty}$ and $H_2$ have spectral gaps around their respective reference energies $E_{\infty}$ and $E_2$, and let $V \neq 0$ couple them with off-diagonal matrix element of energy scale $\Delta E = |E_{\infty} - E_2|$ in the two-level reduction. Then an initial state localized in $\mathcal{H}_{\infty}$ evolves with a component oscillating between sectors at angular frequency

$$
\omega_{\mathrm{mix}} = \frac{\Delta E}{\hbar}.
$$

*Derivation.* In the two-level reduction, the Hamiltonian is $H = E_0 \mathbb{I} + \Delta E\, \sigma_z + |V|\, \sigma_x$ (with $E_0$ the mean energy, $\sigma_z$ distinguishing sectors). The eigenvalue splitting is

$$
\Omega = \sqrt{(\Delta E)^2 + 4|V|^2},
$$

so the transition probability between sectors is $P_{\infty \to 2}(t) = \frac{4|V|^2}{\Omega^2}\sin^2\!\left(\frac{\Omega t}{2}\right)$, which oscillates at $\Omega/\hbar \geq \Delta E/\hbar$. In the Dirac case, the positive- and negative-energy branches are split by $2E$, so $\Delta E = 2E$ and $\omega_{\mathrm{mix}} = 2E/\hbar$, reproducing the ZBW frequency [8]. ∎

This proposition is deliberately modest: it says mixing *forces* an oscillation at the gap frequency; it does not say the observed ZBW frequency *fixes* the mixing partner. That inference is the hypothesis under test.

### 3.3 The 2-adic delocalization measure

Define, for a state with adelic Fourier content, the 2-adic delocalization weight

$$
\mu_2(\Psi) = \frac{\|\hat{\psi}_2\|_{2}^{2}}{\|\hat{\psi}_{\infty}\|_{\infty\text{-norm}}^{2} + \|\hat{\psi}_2\|_{2}^{2}},
$$

where $\hat{\psi}_2$ is the 2-adic Fourier transform (defined via the standard additive character on $\mathbb{Q}_2$ [1]) and $\|\cdot\|_2$ is the $L^2(\mathbb{Q}_2)$ norm. By construction $0 \leq \mu_2 \leq 1$; $\mu_2 = 0$ is the purely Archimedean limit. The equidistribution framework for adelic measures [3] is the rigorous analogue of this bookkeeping on $\mathbb{P}^1$.

### 3.4 Simulation protocol (projection)

We design, but do not report results of, a trapped-ion Dirac simulation of the Gerritsma style (as named in the source idea): a single ion whose internal states encode the Dirac spinor, with laser-driven couplings implementing the Dirac Hamiltonian, and with a controllable parameter that tunes the effective mixing strength $|V|$. The test is a regression of the measured Compton-scale oscillation amplitude $A$ against the engineered $\mu_2$-analogue of the simulated state. The prediction under our hypothesis is monotone increase of $A$ with $\mu_2$; under the standard interference-only reading, $A$ is independent of any 2-adic bookkeeping. Section 5 states this as a labeled projection with assumptions.

## 4. Analysis

All constants below are the 2018 CODATA-consistent values as used in standard computations; each is stated as an input with its role. Every arithmetic step is shown.

**Input constants.**
- Electron rest mass: $m_e = 9.1093837 \times 10^{-31}\,\mathrm{kg}$.
- Speed of light: $c = 2.99792458 \times 10^{8}\,\mathrm{m\,s^{-1}}$ (exact, SI definition).
- Reduced Planck constant: $\hbar = 1.054571817 \times 10^{-34}\,\mathrm{J\,s}$.

**Derivation 1: electron rest energy.**

$$
E_0 = m_e c^2 = \left(9.1093837 \times 10^{-31}\right) \times \left(2.99792458 \times 10^{8}\right)^2 .
$$

First, $c^2 = (2.99792458 \times 10^{8})^2 = 8.98755179 \times 10^{16}\,\mathrm{m^2\,s^{-2}}$. Then

$$
E_0 = 9.1093837 \times 8.98755179 \times 10^{-31+16} = 81.871058 \times 10^{-15} = 8.1871058 \times 10^{-14}\,\mathrm{J}.
$$

**Derivation 2: Compton angular frequency and ZBW frequency.** The Dirac positive/negative branch splitting is $2E_0$, so

$$
\omega_{\mathrm{ZBW}} = \frac{2E_0}{\hbar} = \frac{2 \times 8.1871058 \times 10^{-14}}{1.054571817 \times 10^{-34}}\,\mathrm{rad\,s^{-1}}.
$$

Numerator: $2 \times 8.1871058 \times 10^{-14} = 1.63742116 \times 10^{-13}\,\mathrm{J}$. Dividing:

$$
\omega_{\mathrm{ZBW}} = \frac{1.63742116}{1.054571817} \times 10^{-13+34} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}.
$$

In cycles per second:

$$
f_{\mathrm{ZBW}} = \frac{\omega_{\mathrm{ZBW}}}{2\pi} = \frac{1.55268 \times 10^{21}}{6.283185307} = 2.4710 \times 10^{20}\,\mathrm{Hz}.
$$

**Derivation 3: reduced Compton wavelength.**

$$
\lambda_C = \frac{\hbar}{m_e c} = \frac{1.054571817 \times 10^{-34}}{(9.1093837 \times 10^{-31}) \times (2.99792458 \times 10^{8})}.
$$

Denominator: $9.1093837 \times 2.99792458 = 27.309245$, so $m_e c = 2.7309245 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$. Then

$$
\lambda_C = \frac{1.054571817}{2.7309245} \times 10^{-34+22} = 0.386159 \times 10^{-12} = 3.8616 \times 10^{-13}\,\mathrm{m}.
$$

A packet localized at $\sigma \sim \lambda_C$ has momentum spread $\Delta p \sim \hbar/(2\sigma) = \hbar/(2 \times 3.8616 \times 10^{-13}) = 1.054571817 \times 10^{-34} / 7.7232 \times 10^{-13} = 1.3654 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$, i.e. $\Delta p \sim m_e c/2$: localization at the Compton scale is exactly where the two Dirac branches become inseparable, which is why the mixing channel becomes observable there.

**Derivation 4: product-formula necessity.** For $x \in \mathbb{Q}^{\times}$, the adelic product formula reads

$$
|x|_{\infty} \prod_{p} |x|_p = 1 .
$$

Hence if $|x|_{\infty} \neq 1$, then $\prod_p |x|_p \neq 1$, so at least one prime $p$ has $|x|_p \neq 1$: nontrivial Archimedean scaling *cannot* be adelic-neutral; some $p$-adic norm must compensate. For the prime 2 specifically, $|2^n|_2 = 2^{-n}$, so the 2-adic norm is the most sensitive of all primes to dyadic (binary) structure — the same binary structure that underlies the two-branch (positive/negative energy) Dirac splitting. This is suggestive, not decisive; the decisive structural fact is Derivation 5.

**Derivation 5: minimality of the 2-adic tree.** The Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular [2, 4]. For $p = 2$: degree $= 2 + 1 = 3$. For $p = 3$: degree $= 4$. For any prime $p \geq 3$: degree $= p + 1 \geq 4 > 3$. Since 2 is the smallest prime, $\deg(T_2) = 3 < \deg(T_p)$ for all $p \neq 2$: the 2-adic tree is the unique minimal-degree Bruhat–Tits tree among primes. If oscillation amplitude couples to tree geometry (the hypothesis), the $\infty \leftrightarrow 2$ channel is predicted to dominate.

**Derivation 6: mixing-frequency bound in the simulator.** In the two-level reduction of Section 3.2, the observable oscillation frequency is $\Omega/\hbar$ with $\Omega = \sqrt{(\Delta E)^2 + 4|V|^2} \geq \Delta E$. For the physical Dirac case $\Delta E = 2E_0$, giving the floor $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ (Derivation 2). In a trapped-ion analogue, energies are rescaled by the laser-implemented coupling $\Omega_{\mathrm{ion}}$; the testable statement is the *scaling relation* $A \propto 4|V|^2/\Omega^2$ at fixed $\Delta E$, i.e. amplitude grows with mixing strength and saturates at $1$ when $|V| \gg \Delta E/2$.

## 5. Results

We report only (a) quantities computed in Section 4 and (b) clearly labeled projections.

**Computed results.**

- **R1.** Electron ZBW angular frequency: $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ (Derivation 2), corresponding to $f_{\mathrm{ZBW}} = 2.4710 \times 10^{20}\,\mathrm{Hz}$.
- **R2.** Reduced Compton wavelength: $\lambda_C = 3.8616 \times 10^{-13}\,\mathrm{m}$ (Derivation 3).
- **R3.** Tree-degree minimality: $\deg(T_2) = 3$, strictly less than $\deg(T_p) = p+1 \geq 4$ for every prime $p \geq 3$ (Derivation 5).
- **R4.** Product-formula necessity: any $x \in \mathbb{Q}^{\times}$ with $|x|_{\infty} \neq 1$ has at least one prime $p$ with $|x|_p \neq 1$ (Derivation 4).
- **R5.** Two-level mixing law: sector-transition oscillation at $\Omega/\hbar$, $\Omega = \sqrt{(\Delta E)^2 + 4|V|^2}$, with amplitude factor $4|V|^2/\Omega^2$ (Section 3.2, Derivation 6).

**Projection P1 (labeled projection, not a measurement).** *Assumptions:* (i) a trapped-ion Dirac simulator of the Gerritsma style implements a tunable mixing strength $|V|$ and an engineered 2-adic-analogue weight $\mu_2 \in [0,1]$; (ii) the mixing hypothesis is true, i.e. the Compton-scale oscillation amplitude tracks the mixing channel; (iii) measurement noise is dominated by state-preparation-and-measurement error, assumed at the level $\epsilon = 10^{-2}$ in relative amplitude — an assumed simulator parameter, not a measured value. *Projection:* the measured amplitude should satisfy

$$
A(\mu_2) = A_0 + A_1 \mu_2, \qquad A_1 > 0,
$$

with a detectable slope $A_1 \gtrsim \epsilon = 10^{-2}$ per unit $\mu_2$ under assumption (iii). *Uncertainty bound:* if instead $|A_1| < \epsilon$, the hypothesis is not resolvable at that noise level and the test is inconclusive rather than falsifying. *Falsification condition:* a statistically significant null slope $A_1 = 0$ across the full tunable range of $\mu_2$, or a frequency shift inconsistent with $\Omega = \sqrt{(\Delta E)^2 + 4|V|^2}$, would falsify the mixing signature claim. A second falsification channel is structural: if a $p \geq 3$ sector, engineered analogously, reproduces the same amplitude scaling despite its larger tree degree ($p + 1 \geq 4$), the 2-selection argument (R3) fails.

## 6. Discussion

**Limitations.** The spectral-gap proposition is elementary two-level quantum mechanics; its content is not the mathematics but the *identification* $\Delta E = 2E$ with the Dirac branch splitting, which is an interpretive step, not a theorem. The product-formula argument (R4) applies to rational numbers $x$, whereas physical localization parameters (e.g. $\sigma$) are real numbers not naturally in $\mathbb{Q}^{\times}$; extending the necessity argument to general real localization lengths requires the adelic equidistribution machinery [3], which we invoke by analogy only. The 2-adic delocalization measure $\mu_2$ is defined here for a two-sector truncation; a full adelic definition over all places, in the spirit of adelic measures on $\mathbb{P}^1$ [3] or adelic tori [6], is open. The claim that tree degree controls mixing strength is a hypothesis motivated by minimality (R3); no dynamical mechanism deriving $|V|$ from $\deg(T_p)$ is given here, and the corpus paper [10] asserts a 2-adic ZBW frequency deviation from the Archimedean value without (per its truncated summary) quantifying it — reconciling that asserted deviation with our two-level formula $\Omega = \sqrt{(\Delta E)^2 + 4|V|^2}$ is an open quantitative task.

**Failure modes.** (1) The oscillation amplitude in the simulator may be fully explained by positive/negative energy interference with no dependence on any 2-adic bookkeeping — the standard reading [8] — in which case the mixing signature is vacuous. (2) The engineered "2-adic analogue" in the simulator may not faithfully represent $\mathbb{Q}_2$ structure; a critic can reasonably argue the test then measures the engineering, not the number theory. (3) The minimality argument for $p=2$ may be numerological: degree 3 is minimal, but nothing here shows physics *cares* about minimality. (4) The Majorana vanishing result [9] shows ZBW observables can be topologically trivial ($\mathbb{Z}_2$-vanishing) in free-field theory; if the vanishing extends to the mixing channel, the signature may be unobservable in principle for Majorana-type states, restricting the claim to Dirac fermions.

**What would falsify the claims.** Concretely: (i) a simulator experiment with $|A_1| = 0$ at noise below $\epsilon = 10^{-2}$ (Projection P1); (ii) reproduction of the same scaling by a $p \geq 3$ channel; (iii) a derivation of ZBW frequency from purely Archimedean principles that matches $2E/\hbar$ with no room for a $p$-adic correction — this would not falsify adelic quantum mechanics [1] but would remove ZBW's status as its observable. **Open questions:** a rigorous theorem relating $\mu_2$ to spectral data of $V$; the exact magnitude of the 2-adic frequency deviation asserted in [10]; extension of the two-sector model to the full adelic torsor structure of [6]; and whether the Ostrowski-based error-correction ideas of [11] provide a natural encoding for the simulator's 2-adic channel. We note that the consilience claim of [12] — five programs converging on ultrametric state-space geometry — is corpus-level motivation and does not substitute for any of these open tasks.

## 7. Conclusion

We have given the claim "Zitterbewegung is the observable trace of $\infty \leftrightarrow 2$ adelic mixing" a precise, partially formal shape: a spectral-gap proposition forcing oscillation at $\Delta E/\hbar$ under any inter-place coupling; a product-formula argument that Archimedean localization entails nontrivial $p$-adic norm content; explicit numerical anchors ($\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$, $\lambda_C = 3.8616 \times 10^{-13}\,\mathrm{m}$ for the electron); and a structural-selection argument for the prime 2 via the minimal $3$-regularity of its Bruhat–Tits tree. We specified a falsifiable trapped-ion test and stated its assumptions, projected sensitivity, and falsification conditions without claiming any measurement. The claim remains a hypothesis; its value is that it is now definite enough to fail.

## References

[1] arXiv:hep-th/0312046v1 | p-Adic and Adelic Quantum Mechanics
[2] arXiv:math-ph/0306023v1 | Non-Archimedean Geometry and Physics on Adelic Spaces
[3] arXiv:1502.04660v3 | Quasi-adelic measures and equidistribution on $\mathbb{P}^1$
[4] arXiv:1105.2966v1 | The Geometry of p-Adic Fractal Strings: A Comparative Survey
[5] arXiv:1304.3539v2