# Adelic Zitterbewegung: p-Adic Regularization of Dirac Trembling Motion at Short Scales

## Abstract

Zitterbewegung (ZBW) — the trembling motion of Dirac wave packets at the Compton scale — is conventionally understood as interference between positive- and negative-energy branches of the free Dirac equation on the real line. We propose a conjectural extension in which the free Dirac equation is formulated over the adele ring $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$, so that the trembling motion occurs simultaneously in the Archimedean sector and in every $p$-adic sector. Using the adelic product formula, we show in a controlled toy model that the $p$-adic contributions to the velocity expectation value are suppressed at macroscopic scales by a computable relative weight, recovering the standard Schrödinger oscillation at angular frequency $\omega = 2m_e c^2/\hbar$, while near the Compton and Planck lengths the non-Archimedean terms are no longer negligible and can discretize or fractalize the motion. We derive the sector-wise structure of the adelic velocity operator, compute the relevant scale hierarchies ($\lambda_C/\ell_P \approx 2.39 \times 10^{22}$ for the electron), demonstrate the product-formula cancellation explicitly for rational test positions, and outline a simulation program for wave-packet dynamics on $\mathbb{Q}_p$ using the Vladimirov operator and $p$-adic gamma matrices. The framework suggests a concrete mechanism whereby adelic geometry regularizes relativistic quantum dynamics and modifies the short-distance path integral.

## 1. Introduction

The free Dirac equation predicts that the velocity operator of a relativistic particle has eigenvalues $\pm c$, and that a localized wave packet exhibits a rapid trembling motion — Zitterbewegung (ZBW) — at the Compton scale. As recounted in the historical review of the statistical mechanics of ZBW, around 1930 both Gregory Breit and Erwin Schrödinger showed that the eigenvalues of the velocity of a particle described by wave-packet solutions to the Dirac equation are simply $\pm c$, the speed of light, and this led Schrödinger to coin the term Zitterbewegung, German for "trembling motion" [4]. The modern semiconductor literature has revived interest in ZBW because it is in principle observable in solid-state analogues: reviews cover trembling motion of charge carriers in monolayer and bilayer graphene, carbon nanotubes, and narrow-gap materials such as InSb-type semiconductors, with Gaussian wave packets exhibiting damped oscillatory ZB [3], [7].

In parallel, $p$-adic and adelic quantum mechanics has matured into a framework in which quantum theory is formulated over the adele ring $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$, with complex-valued wave functions of $p$-adic and adelic arguments [1]. This program originated in efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and path integrals for quadratic Lagrangians have been evaluated analytically on ordinary, $p$-adic, and adelic spaces, with formulas invariant under interchange of the Archimedean and non-Archimedean places [5]. Cosmological extensions introduce $p$-adic worlds made of $p$-adic matter alongside the real world, with the two together making up the universe as a whole [2].

The present paper joins these two threads with a specific conjecture: **the trembling motion of a free Dirac particle is an adelic phenomenon**. In the standard real formulation, ZBW arises from interference between positive- and negative-energy branches on the real line. We conjecture instead that the interference structure exists sector by sector over the whole adele ring: the velocity expectation value decomposes as a product (or, in the toy model below, a weighted sum) of an Archimedean contribution and one contribution per prime $p$. By the adelic product formula, the $p$-adic contributions cancel against the Archimedean one at macroscopic scales, so that ordinary ZBW at $\omega = 2mc^2/\hbar$ is recovered; near the Compton length $\lambda_C$ and Planck length $\ell_P$, the non-Archimedean terms dominate, discretizing or fractalizing the motion and preventing the formation of singularities.

This work is deliberately positioned as a conjectural framework with fully explicit derivations. Every number in Section 4 is computed from stated inputs with shown arithmetic; no simulation results are reported. The simulation program (wave-packet dynamics on $\mathbb{Q}_p$ with the Vladimirov operator and $p$-adic gamma matrices) is specified in Section 3 as future work, and its expected signatures are labeled as projections with stated assumptions.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 sets up the adelic Dirac equation, the sector-wise velocity operator, and the toy cancellation model. Section 4 performs all derivations and arithmetic. Section 5 states the results. Section 6 discusses limitations, failure modes, and falsification criteria. Section 7 concludes.

## 2. Background and Related Work

**Adelic quantum mechanics.** The foundational review of $p$-adic mathematical physics describes its emergence from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale; its main achievement is a successful formulation and development of $p$-adic and adelic quantum mechanics with complex-valued wave functions of $p$-adic and adelic arguments respectively [1]. This is the mathematical substrate on which our conjecture is built: if adelic wave functions are already well defined, the question is whether a first-order-in-time equation of Dirac type can be given a sector-wise meaning, and whether observables such as the velocity expectation value factorize over the places.

**Adelic path integrals.** Path integrals for quadratic Lagrangians have been considered in ordinary, $p$-adic, and adelic quantum mechanics, with probability amplitudes for two-dimensional systems with quadratic Lagrangians evaluated analytically and generalized to any finite-dimensional spaces, in a form invariant under interchange of the places [5]. This invariance is directly relevant to our proposal: a regularized adelic path integral for the Dirac particle should reduce, in each sector, to a quadratic (or linearized) amplitude of the type treated there, and the sector-wise structure we assume for the velocity operator is the same structure that makes those formulas interchange-invariant.

**Adelic cosmology and $p$-adic matter.** A review of $p$-adic and adelic cosmology considers $p$-adic and adelic aspects of gravity, classical cosmology, quantum mechanics, quantum cosmology, and the wave function of the universe, and introduces $p$-adic worlds made of $p$-adic matter, distinct from the real world of ordinary matter, with real and $p$-adic worlds together making the universe as a whole [2]. This provides a physical precedent for our central assumption — that all places of the adele ring carry parallel dynamical content, with the real sector being only one member of a family — although the summary supplied for [2] gives no further detail on the dynamics, so we use it only as evidence for the general adelic-worlds picture.

**Zitterbewegung: history and statistics.** The historical study of the problem of motion records that around 1930 Breit and Schrödinger showed that the eigenvalues of the velocity of a wave-packet solution to the Dirac equation are $\pm c$, that Schrödinger coined the term Zitterbewegung for the resulting back-and-forth zig-zag of matter particles at the speed of light, and develops a statistical-mechanics treatment of the trembling motion [4]. Our conjecture reinterprets this interference picture: the positive/negative-energy interference on the real line is postulated to be the Archimedean shadow of a richer adelic interference involving all places.

**Zitterbewegung in condensed matter.** The semiconductor ZBW review covers trembling motion in semirelativistic and spin systems, elaborates ZB of charge carriers in monolayer and bilayer graphene and carbon nanotubes, and describes effective approaches [3]. The narrow-gap review treats nearly free electrons in a periodic potential, InSb-type semiconductors, bilayer and monolayer graphene, and carbon nanotubes, and shows that Gaussian wave packets exhibit ZB with characteristic damping and oscillation structure [7]. These works matter to us for two reasons: they establish that ZBW is a robust, model-independent interference phenomenon (appearing whenever two bands with a gap interfere), and they supply the experimental context against which any adelic correction to the ZBW frequency would have to be tested — in condensed matter, the effective parameters replace $m_e$ and $c$, so the adelic scale hierarchy of Section 4 would be rescaled.

**$p$-adic statistical mechanics.** The $p$-adic Potts model study reduces the description of $p$-adic Gibbs measures to a recursive equation on a Cayley tree and proves that a phase transition occurs if and only if $p = 3$ for any nonzero interaction value, also solving the associated uniqueness problem [6]. Although distant from ZBW, this work illustrates a general lesson we rely on: $p$-adic dynamical systems exhibit sharp, prime-dependent thresholds. In our setting, the analogous prime-dependence appears in the $p$-adic norms $|x|_p = p^{-v_p(x)}$ that control which sectors contribute at a given length scale (Section 4).

**$p$-adic geometry of state spaces.** The theory of $p$-adic equiangular lines introduces equiangular line sets in $\mathbb{Q}_p^d$ and derives the first fundamental relation between common angle, dimension, and number of lines — the $p$-adic van Lint–Seidel relative bound $|n|^2 \leq |d|\max\{|n|, \gamma^2\}$ [8]. This is relevant to the Hilbert-space geometry of our $p$-adic sectors: if $p$-adic gamma matrices and their eigenvectors are to support a wave-packet calculus, the combinatorics of admissible state configurations in $\mathbb{Q}_p^d$ is governed by bounds of this type. The summary supplied for [8] states the bound but gives no further applications, so we cite it only as a structural constraint on $p$-adic state spaces.

**The adelic physics program.** Three further works frame the broader program. The grand-synthesis paper consolidates a six-paper adelic physics chain into a unified research program running from Zitterbewegung as a $p$-adic observable through Majorana correlators, Bruhat–Tits readout protocols, $p$-adic anyon braiding, and Ostrowski-based quantum error correction [9]. The conjectural-framework paper develops ZBW as Archimedean–2-adic channel mixing, starting from the conventional interference explanation and proposing testable consequences within the adelic program [10]. The measure-theoretic taxonomy paper starts from the Ostrowski theorem — which partitions all non-trivial completions of $\mathbb{Q}$ into exactly one Archimedean completion and infinitely many non-Archimedean completions — observes that physics operates exclusively at the Archimedean place, and catalogues measure-theoretic artifacts across five categories with sixteen documented completion failures [12]. Finally, the Monna-map paper asks what changes to visual and geometric phenomenology if physical space were non-Archimedean and ultrametric rather than Archimedean [11]; we cite it as motivation for taking ultrametric geometry seriously as physical geometry at short scales, noting that its supplied summary concerns perception and rendering rather than dynamics.

## 3. Methods

### 3.1 The adele ring and the product formula

The adele ring is $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$ (restricted product). For a nonzero rational $x \in \mathbb{Q}^\times$, the Archimedean absolute value $|x|_\infty$ and the $p$-adic norms $|x|_p = p^{-v_p(x)}$, where $v_p(x)$ is the exponent of $p$ in the prime factorization of $x$, satisfy the product formula

$$\prod_{v \in \{\infty\} \cup \{p\}} |x|_v = 1.$$

This identity is the algebraic engine of our cancellation claim and is verified by explicit computation in Section 4.2.

### 3.2 The adelic Dirac equation, sector by sector

We postulate that the free Dirac equation holds independently in each place $v$:

$$i\hbar \frac{\partial \psi_v}{\partial t_v} = \left( c_v \, \boldsymbol{\alpha}_v \cdot \hat{\mathbf{p}}_v + \beta_v m_v c_v^2 \right) \psi_v, \qquad v \in \{\infty\} \cup \{p\},$$

where $\psi_v$ is a complex-valued spinor wave function on the sector $v$ (consistent with the complex-valued wave functions of $p$-adic and adelic arguments of adelic quantum mechanics [1]), $\boldsymbol{\alpha}_v$ and $\beta_v$ are the sector gamma-matrix structures, and $c_v$, $m_v$ are sector parameters. In the Archimedean sector, $c_\infty = c$ and $m_\infty = m_e$ are the observed constants. The values of $c_p$ and $m_p$ in the $p$-adic sectors are **not fixed by this paper**; the toy model of Section 3.4 treats them as free parameters and derives the cancellation as a function of their scaling. This is a deliberate limitation, discussed in Section 6.

### 3.3 Velocity expectation values

In each sector, the velocity operator is $\hat{v}_v = c_v \alpha_v$ (the component along the direction of motion), and the sector velocity expectation is

$$\langle v_v \rangle(t_v) = \int \psi_v^\dagger \, c_v \alpha_v \, \psi_v \, d\mu_v,$$

with $d\mu_v$ the Haar measure on the sector. The adelic velocity expectation is defined as the product over places:

$$\langle v \rangle_{\mathbb{A}}(t) = \prod_v \langle v_v \rangle(t_v).$$

The product form is chosen to mirror the product formula; a sum form is the main alternative and is treated as a model variant in Section 4.3. In the real sector, the standard result is that a positive-energy wave packet with negative-energy admixture $w$ gives

$$\langle v_\infty \rangle(t) \approx c\left(1 - 2w\right) + 2cw\cos(\omega t), \qquad \omega = \frac{2m_e c^2}{\hbar},$$

which is the Schrödinger trembling motion [4], [3].

### 3.4 Toy cancellation model

Let the adelic position of a packet be a rational multiple of the Compton wavelength, $x = N \lambda_C$ with $N \in \mathbb{Z}^+$, and let the $p$-adic contribution of sector $p$ to the velocity amplitude carry weight $|x|_p = p^{-v_p(x)}$ while the Archimedean contribution carries weight $|x|_\infty = N$. The product formula then forces exact cancellation of the total adelic weight:

$$|x|_\infty \prod_p |x|_p = N \cdot \prod_{p \mid N} p^{-v_p(N)} = 1.$$

The relative size of the non-Archimedean contribution against the Archimedean one is then

$$\epsilon(N) = \frac{\prod_{p \mid N} |x|_p}{|x|_\infty^2} = \frac{1}{N^2},$$

which vanishes rapidly at macroscopic $N$ and approaches $1$ as $N \to 1$, i.e., at the Compton scale itself. This is the quantitative core of the conjecture, computed explicitly in Section 4.3.

### 3.5 Simulation program (specified, not executed)

The following simulation is specified as the primary test of the framework but is **not** reported as performed in this paper:

1. Construct $p$-adic gamma matrices $\alpha_p, \beta_p$ acting on spinors over $\mathbb{Q}_p^d$, subject to the geometric constraints on $p$-adic state spaces such as the equiangular-line bound of [8].
2. Discretize the Vladimirov operator $D^{\alpha}_p$ (the $p$-adic analogue of $-\Delta$) on a finite ball of $\mathbb{Q}_p$.
3. Evolve Gaussian-type wave packets under the $p$-adic Dirac evolution and measure the trembling frequency and trajectory fractal dimension sector by sector.
4. Compare the sector-wise frequencies with the Archimedean $\omega = 2m_ec^2/\hbar$ and quantify the scale-dependent shift predicted by the toy model.

## 4. Analysis

All physical constants used below are stated here as inputs of the paper: $\hbar = 1.0546 \times 10^{-34}\ \mathrm{J\,s}$, $c = 2.998 \times 10^{8}\ \mathrm{m/s}$, $m_e = 9.109 \times 10^{-31}\ \mathrm{kg}$, $G = 6.674 \times 10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

### 4.1 Compton scales and the ZBW frequency

**Step 1: electron rest energy.**

$$E_0 = m_e c^2 = 9.109 \times 10^{-31}\ \mathrm{kg} \times (2.998 \times 10^{8}\ \mathrm{m/s})^2.$$

First, $c^2 = (2.998 \times 10^8)^2 = 8.988 \times 10^{16}\ \mathrm{m^2/s^2}$. Then

$$E_0 = 9.109 \times 10^{-31} \times 8.988 \times 10^{16} = 8.187 \times 10^{-14}\ \mathrm{J}.$$

**Step 2: Compton time.**

$$t_C = \frac{\hbar}{m_e c^2} = \frac{1.0546 \times 10^{-34}}{8.187 \times 10^{-14}} = 1.288 \times 10^{-21}\ \mathrm{s}.$$

**Step 3: ZBW angular frequency.** The standard interference frequency is $\omega = 2m_ec^2/\hbar = 2/t_C$:

$$\omega = \frac{2}{1.288 \times 10^{-21}\ \mathrm{s}} = 1.552 \times 10^{21}\ \mathrm{rad/s}.$$

The ordinary frequency is $f = \omega / 2\pi = 1.552 \times 10^{21} / 6.2832 = 2.470 \times 10^{20}\ \mathrm{Hz}$.

**Step 4: Compton wavelength.**

$$\lambda_C = c\, t_C = 2.998 \times 10^{8} \times 1.288 \times 10^{-21} = 3.862 \times 10^{-13}\ \mathrm{m}.$$

**Step 5: Planck length.**

$$\ell_P = \sqrt{\frac{\hbar G}{c^3}}.$$

Numerator: $\hbar G = 1.0546 \times 10^{-34} \times 6.674 \times 10^{-11} = 7.039 \times 10^{-45}\ \mathrm{kg\,m^3/s^2 \cdot s^{-1}}$ (units: $\mathrm{J\,s \cdot m^3 kg^{-1} s^{-2}} = \mathrm{m^4/s^3}$... carrying through: $7.039 \times 10^{-45}\ \mathrm{m^4/s^3}$ after unit reduction). Denominator: $c^3 = (2.998 \times 10^8)^3 = 2.694 \times 10^{25}\ \mathrm{m^3/s^3}$. Ratio:

$$\frac{\hbar G}{c^3} = \frac{7.039 \times 10^{-45}}{2.694 \times 10^{25}} = 2.612 \times 10^{-70}\ \mathrm{m^2},$$

$$\ell_P = \sqrt{2.612 \times 10^{-70}}\ \mathrm{m} = 1.616 \times 10^{-35}\ \mathrm{m}.$$

**Step 6: scale hierarchy.**

$$\frac{\lambda_C}{\ell_P} = \frac{3.862 \times 10^{-13}}{1.616 \times 10^{-35}} = 2.390 \times 10^{22}.$$

So the Compton length sits about twenty-two orders of magnitude above the Planck length; the non-Archimedean regime conjectured here spans this entire range.

### 4.2 Product formula: explicit verification

**Case $x = 2$.** $v_2(2) = 1$, $v_p(2) = 0$ for $p \neq 2$. Then $|2|_\infty = 2$, $|2|_2 = 2^{-1} = 0.5$, $|2|_p = 1$ otherwise:

$$|2|_\infty \cdot |2|_2 \cdot \prod_{p \neq 2} |2|_p = 2 \times 0.5 \times 1 = 1. \checkmark$$

**Case $x = 6$.** $v_2(6) = 1$, $v_3(6) = 1$. Then $|6|_\infty = 6$, $|6|_2 = 1/2$, $|6|_3 = 1/3$:

$$6 \times \frac{1}{2} \times \frac{1}{3} = 1. \checkmark$$

**Case $x = 12 = 2^2 \cdot 3$.** $|12|_\infty = 12$, $|12|_2 = 2^{-2} = 1/4$, $|12|_3 = 1/3$:

$$12 \times \frac{1}{4} \times \frac{1}{3} = 1. \checkmark$$

The product formula holds exactly for every rational test position, confirming that the cancellation mechanism is algebraic, not approximate.

### 4.3 Toy cancellation: relative non-Archimedean weight

With $x = N\lambda_C$ and the weights of Section 3.4, the relative weight of the non-Archimedean contribution is $\epsilon(N) = 1/N^2$.

**Case $N = 1$** (packet localized at one Compton wavelength): $\epsilon(1) = 1/1^2 = 1$. The $p$-adic sectors contribute at full relative strength; the motion is expected to be maximally adelic — this is the regime where discretization or fractalization is conjectured.

**Case $N = 10^6$**: $\epsilon(10^6) = 1/(10^6)^2 = 1/10^{12} = 10^{-12}$. The non-Archimedean contribution is twelve orders of magnitude below the Archimedean one; standard ZBW is recovered to relative accuracy $10^{-12}$.

**Case $N = 10^{22}$** (macroscopic scale, comparable to $\lambda_C/\ell_P \approx 2.39 \times 10^{22}$): taking $N = 2.39 \times 10^{22}$,

$$\epsilon(N) = \frac{1}{(2.39 \times 10^{22})^2} = \frac{1}{5.712 \times 10^{44}} = 1.751 \times 10^{-45}.$$

At macroscopic scales the $p$-adic trembling is suppressed to relative weight of order $10^{-45}$ — far below any conceivably measurable level, which is precisely why ordinary ZBW has been observed only in its Archimedean form [3], [4], [7].

**Crossover scale.** Setting $\epsilon(N) = \delta$ for a detectability threshold $\delta$ gives $N_\delta = \delta^{-1/2}$. For $\delta = 10^{-4}$ (a generous experimental threshold for a fractional frequency shift):

$$N_\delta = (10^{-4})^{-1/2} = 10^{2} = 100,$$

i.e., the crossover occurs at $x_\delta = 100\,\lambda_C = 100 \times 3.862 \times 10^{-13}\ \mathrm{m} = 3.862 \times 10^{-11}\ \mathrm{m}$, about four hundredths of a nanometer — atomic dimensions. This is a **projection** of the toy model, not a measurement: it assumes (i) the product-form weight assignment of Section 3.4, (ii) that sector parameters $c_p, m_p$ are of order unity relative to $c, m_e$, and (iii) that the detectability threshold is $10^{-4}$.

### 4.4 Frequency-shift projection under the sum variant

If the adelic frequency is instead a sum of sector contributions, $\omega_{\mathbb{A}}^2 = \omega_\infty^2 + \sum_p \omega_p^2$, with each $\omega_p = \omega_\infty \cdot |x|_p$ by the same weight assignment, then for $x = N\lambda_C$ with $N = 2^k$ (a single prime dominating):

$$\omega_{\mathbb{A}} = \omega_\infty \sqrt{1 + 2^{-2k}}.$$

For $k = 1$ ($N = 2$, $x = 2\lambda_C$): $\omega_{\mathbb{A}} = \omega_\infty\sqrt{1.25} = 1.1180\,\omega_\infty$, an $11.8\%$ shift. For $k = 7$ ($N = 128$, $x = 128\lambda_C$): $\omega_{\mathbb{A}} = \omega_\infty\sqrt{1 + 2^{-14}} = \omega_\infty\sqrt{1.0000610} = 1.0000305\,\omega_\infty$, a $3.05 \times 10^{-5}$ relative shift. These are projections under the stated sum-variant assumption; the product variant instead predicts exact cancellation and no shift, so the two variants are empirically distinguishable in principle at $x \lesssim 100\,\lambda_C$.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic, except where explicitly labeled projections.

**R1 (Compton scales).** For the electron: $t_C = 1.288 \times 10^{-21}\ \mathrm{s}$, $\lambda_C = 3.862 \times 10^{-13}\ \mathrm{m}$, and the ZBW frequency $\omega = 1.552 \times 10^{21}\ \mathrm{rad/s}$ ($f = 2.470 \times 10^{20}\ \mathrm{Hz}$).

**R2 (Planck scale and hierarchy).** $\ell_P = 1.616 \times 10^{-35}\ \mathrm{m}$ and $\lambda_C/\ell_P = 2.390 \times 10^{22}$.

**R3 (Product formula).** The adelic product formula $|x|_\infty \prod_p |x|_p = 1$ is verified exactly for $x = 2, 6, 12$; the cancellation it encodes is algebraic and exact for all rational positions.

**R4 (Suppression law).** In the toy model, the relative non-Archimedean weight is $\epsilon(N) = 1/N^2$ for a packet at $x = N\lambda_C$: $\epsilon(1) = 1$, $\epsilon(10^6) = 10^{-12}$, $\epsilon(2.39 \times 10^{22}) = 1.751 \times 10^{-45}$.

**R5 (Crossover projection).** Under the toy-model assumptions (product-form weights, sector parameters of order unity, threshold $\delta = 10^{-4}$), the adelic corrections become detectable only below $x_\delta = 100\,\lambda_C = 3.862 \times 10^{-11}\ \mathrm{m}$. Uncertainty: this projection is sensitive to the unknown sector parameters $c_p, m_p$; if these are smaller than unity by a factor $\kappa$, the crossover moves to $x_\delta \sim 100\,\lambda_C / \kappa$.

**R6 (Variant discrimination projection).** Under the sum variant with a single dominant prime, the frequency shift at $x = 2\lambda_C$ is $11.8\%$ and at $x = 128\lambda_C$ is $3.05 \times 10^{-5}$; the product variant predicts zero shift at all scales. No simulation or measurement of either variant has been performed in this paper.

## 6. Discussion

**Limitations.** The central weakness of this paper is that the adelic Dirac equation of Section 3.2 is postulated, not derived. The sector parameters $c_p$ and $m_p$ are undetermined; the entire quantitative content of the toy model (R4–R6) is conditional on their being of order unity. The product-form ansatz for the adelic velocity expectation is one choice among several; the sum variant gives qualitatively different predictions (R6), and the true observable structure could be neither. The weight assignment $|x|_p$ to sector amplitudes is motivated by the product formula but is not derived from a dynamics; a full derivation would require the $p$-adic gamma-matrix calculus and the Vladimirov-operator evolution specified but not executed in Section 3.5.

**Failure modes.** (i) If the $p$-adic sectors support no unitary time evolution compatible with a Dirac-type first-order equation, the conjecture fails at the outset. (ii) If the sector parameters $c_p, m_p$ are strongly scale-dependent, the clean $1/N^2$ suppression law is destroyed and the crossover projection R5 is void. (iii) If the adelic velocity expectation is not multiplicatively or additively separable across sectors, neither variant applies.

**What would falsify the claims.** A precision measurement or simulation of ZBW at scales $\lesssim 100\,\lambda_C$ (in high-energy settings, or in analogue systems where the effective Compton scale is engineered as in graphene and narrow-gap semiconductors [3], [7]) that shows **no** frequency shift and **no** trajectory discretization down to arbitrarily small scales would falsify the sum variant but not the product variant; conversely, a demonstrated exact product-form cancellation with no residual sector dynamics would falsify the conjecture's core claim that non-Archimedean terms dominate near $\lambda_C$. The sharpest falsifier of the framework as a whole is the construction of a no-go theorem showing that no nontrivial $p$-adic Dirac dynamics exists with the required interference structure.

**Against ourselves.** One may argue the conjecture is unfalsifiable as stated, because the undetermined sector parameters can always be tuned to evade bounds. We partially concede this: the paper's value is therefore in the *structure* it fixes — the exact product formula (R3) and the resulting suppression law's $N$-dependence, which is parameter-free once the ansatz is granted. A second objection: the adelic program's own literature treats $p$-adic worlds as physically parallel to the real world [2], [12],