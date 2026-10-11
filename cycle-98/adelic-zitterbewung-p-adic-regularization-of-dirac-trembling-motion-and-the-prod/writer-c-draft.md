# Adelic Zitterbewegung: p-Adic Regularization of Dirac Trembling Motion and the Product-Formula Cancellation at Macroscopic Scales

## Abstract

Zitterbewegung (ZBW) — the trembling motion of Dirac wave packets at the Compton scale — is conventionally treated as a purely Archimedean interference effect between positive- and negative-energy branches. We propose a conjectural extension in which the free Dirac equation is formulated over the adele ring $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$, so that the trembling motion acquires simultaneous oscillatory components in the real sector and in every $p$-adic sector. We define a sector-resolved velocity expectation value, propose a product-formula cancellation mechanism whereby the $p$-adic contributions to the macroscopic motion cancel by the adele norm identity $|x|_\infty \prod_p |x|_p = 1$, and show with explicit arithmetic that the cross-sector interference amplitude scales as $\lambda_C/\ell$, where $\lambda_C$ is the Compton wavelength and $\ell$ the observation scale: at $\ell = 1\,\mathrm{m}$ this is $3.86 \times 10^{-13}$, while at the Planck length the $p$-adic sector dominates by a factor $\approx 2.39 \times 10^{22}$. We further compute model-projected sector frequency shifts under a stated $p$-adic dispersion assumption. The framework motivates simulation of wave-packet dynamics under the Vladimirov operator and a regularized adelic path integral, connecting non-Archimedean geometry to observable relativistic quantum dynamics.

## 1. Introduction

The Dirac equation predicts that a localized relativistic electron does not move smoothly: interference between its positive- and negative-energy components produces a rapid trembling motion at the Compton scale, with characteristic angular frequency $\omega = 2mc^2/\hbar$. This phenomenon, named Zitterbewegung by Schrödinger, has been known since the work of Breit and Schrödinger around 1930, who showed that the velocity eigenvalues of Dirac wave packets are $\pm c$ [4]. Modern reviews document that the effect is not merely formal: trembling motion of charge carriers is predicted and analyzed in semiconductors, monolayer and bilayer graphene, and carbon nanotubes [3], and in narrow-gap materials where Gaussian wave packets exhibit the effect in a controlled way [7].

At the same time, a parallel line of physics proposes that spacetime at very short scales is better described by non-Archimedean fields. p-Adic mathematical physics arose precisely from efforts to find a non-Archimedean description of spacetime and string dynamics at the Planck scale, and has produced a working formulation of p-adic and adelic quantum mechanics with complex-valued wave functions of p-adic and adelic arguments respectively [1]. Path integrals for such systems have been evaluated analytically for quadratic Lagrangians in ordinary, p-adic, and adelic settings [5], and adelic ideas have been extended to cosmology, where real and p-adic "worlds" together compose the universe as a whole [2].

This paper combines the two lines. We ask: what happens to Zitterbewegung if the Dirac equation is formulated not on $\mathbb{R}$ alone but on the adele ring $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$? The conjecture is that the trembling motion decomposes into a real-sector oscillation at the standard frequency $\omega_\infty = 2mc^2/\hbar$ plus p-adic sector oscillations whose amplitudes are governed by p-adic norms; that by the adele product formula the p-adic contributions cancel identically at macroscopic scales, recovering the standard real oscillation; and that near the Compton or Planck length the non-Archimedean terms dominate, discretizing or fractalizing the motion and preventing singularities. The program builds on the adelic physics synthesis of [9], on the specific conjecture of ZBW as Archimedean–2-adic channel mixing [10], and on the observation that physics currently operates exclusively at the Archimedean place of $\mathbb{Q}$ [12].

Our contribution is threefold. First, we write down the sector-resolved form of the adelic Dirac dynamics and the velocity (α-matrix) expectation values. Second, we give an explicit, fully arithmetized cancellation mechanism based on the adele product formula, with numerical evaluation at laboratory and Planck scales. Third, we state a testable projection: scale-dependent frequency shifts in the p-adic sectors, and a regularized path-integral comparison enabled by the analytic adelic path-integral formulas of [5].

## 2. Background and Related Work

**p-Adic and adelic quantum mechanics.** The foundational review [1] (arXiv:hep-th/0312046v1) explains that p-adic mathematical physics emerged from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and that its main achievement is a successful formulation and development of p-adic and adelic quantum mechanics, with complex-valued wave functions of p-adic and adelic arguments respectively. This is the mathematical substrate on which our construction rests: an adelic wave function $\Psi(x,t)$ with $x \in \mathbb{A}$ is an object of exactly the type whose theory [1] establishes. The supplied summary of [1] is truncated and gives no further detail on spectral or dynamical aspects, so we rely on it only for the existence and scope of the adelic quantum-mechanical formalism.

**Adelic path integrals.** Reference [5] (arXiv:1011.6589v1) considers Feynman's path integrals in ordinary, p-adic and adelic quantum mechanics, evaluates the probability amplitudes $K(x'',t'';x',t')$ for two-dimensional systems with quadratic Lagrangians analytically, generalizes the expressions to any finite-dimensional spaces, and presents them in a form invariant under interchange of the relevant data. For our program this matters directly: any regularized adelic path integral we propose in Section 6 can be tested against the exactly solvable quadratic cases treated in [5], providing a consistency check between our ZBW regularization and known adelic amplitudes.

**Adelic cosmology and p-adic worlds.** Reference [2] (arXiv:hep-th/0602044v1) reviews p-adic and adelic cosmology, covering p-adic aspects of gravity, classical cosmology, quantum mechanics, quantum cosmology and the wave function of the universe, and introduces "p-adic worlds" made of p-adic matter distinct from the real world of ordinary matter, with real and p-adic worlds making up the universe as a whole. This ontological picture — coexisting real and p-adic sectors — is the cosmological analogue of the sector-resolved dynamics we propose for a single Dirac particle.

**Zitterbewegung: origins.** Reference [4] (arXiv:1411.1854v2) records that around 1930 both Gregory Breit and Erwin Schrödinger showed that the eigenvalues of the velocity of a particle described by wave-packet solutions to the Dirac equation are simply $\pm c$, and that this led Schrödinger to coin the term Zitterbewegung, German for "trembling motion," in which particles of matter zig-zag back and forth at the speed of light. The supplied summary is truncated beyond this historical statement; we use [4] for the founding observation and terminology, and note that its framing of ZBW as a statistical-mechanical problem suggests that trembling motion admits treatments beyond plain two-branch interference — a point our multi-sector extension exploits.

**Zitterbewegung in condensed matter.** Reference [3] (arXiv:1101.0623v1) reviews ZBW of electrons in semiconductors, presenting a brief history of the subject, considering trembling motion in semirelativistic and spin systems, emphasizing its main features, and elaborating ZBW of charge carriers in monolayer and bilayer graphene and carbon nanotubes. Reference [7] (arXiv:0805.0478v1) reviews the theory of ZB of charge carriers in narrow-gap materials — nearly free electrons in a periodic potential, InSb-type semiconductors, bilayer and monolayer graphene, carbon nanotubes — and shows that when charge carriers are prepared as Gaussian wave packets the ZB (the summary continues beyond the truncation point). Together [3] and [7] establish that ZBW is a robust, tunable wave-packet phenomenon, which is precisely the regime our adelic modification targets: wave-packet dynamics, not plane-wave kinematics.

**p-Adic statistical structure.** Reference [6] (arXiv:math-ph/0512018v2) studies the three-state p-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of p-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero interaction, also solving the uniqueness problem completely. We cite this as evidence that p-adic statistical systems exhibit sharp, prime-dependent structural thresholds — a phenomenon class our conjectured prime-dependent ZBW regularization would join, though we make no quantitative use of the Potts results themselves.

**p-Adic geometry of state spaces.** Reference [8] (arXiv:2408.00810v3) introduces p-adic equiangular lines and derives the first fundamental relation between common angle, dimension, and number of lines: if $\{\tau_j\}_{j=1}^n$ is a p-adic $\gamma$-equiangular family in $\mathbb{Q}_p^d$, then $|n|^2 \leq |d|\max\{|n|, \gamma^2\}$, termed the p-adic van Lint–Seidel relative bound. This shows that Hilbert-space-geometric notions (frames, angle bounds) survive in $\mathbb{Q}_p^d$, supporting the coherence of defining gamma-matrix structures and wave-packet inner products over p-adic fields.

**The adelic physics program.** Reference [9] consolidates a six-paper adelic physics chain into a unified research program spanning Zitterbewegung as a p-adic observable, Majorana correlators, Bruhat–Tits readout protocols, p-adic anyon braiding, and Ostrowski-based quantum error correction; our paper is a concrete dynamical instantiation of its ZBW strand. Reference [10] develops the specific conjecture that ZBW — the trembling motion of Dirac wave packets at the Compton scale, first identified by Breit and Schrödinger, and conventionally explained as interference between positive- and negative-energy branches on the real line — should be understood as Archimedean–2-adic channel mixing, with testable consequences; the supplied summary is truncated before those consequences are stated, so we treat [10] as the motivating conjecture and supply our own explicit arithmetic. Reference [12] records that the Ostrowski theorem partitions all non-trivial completions of $\mathbb{Q}$ into exactly one Archimedean and infinitely many non-Archimedean completions, that physics operates exclusively at the Archimedean place, and catalogues measure-theoretic artifacts across 5 categories with 16 documented completion failures; our work responds by constructing dynamics that genuinely uses all places. Reference [11] asks what changes in geometric phenomenology (perspective, the Monna map) if physical space were non-Archimedean and ultrametric; it supplies conceptual background for visualizing ultrametric motion but no dynamical results, and we use it only as such.

## 3. Methods

### 3.1 Adelic setup

By the Ostrowski theorem, every non-trivial absolute value on $\mathbb{Q}$ is equivalent to the usual Archimedean one $|\cdot|_\infty$ or to a p-adic norm $|\cdot|_p$ for some prime $p$ [12]. The adele ring is $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$ (restricted product). For a rational number $x \neq 0$ embedded diagonally, the product formula holds:

$$|x|_\infty \prod_p |x|_p = 1.$$

We posit an adelic Dirac wave function $\Psi = (\Psi_\infty, \Psi_2, \Psi_3, \Psi_5, \dots)$, where $\Psi_\infty$ is the standard complex Dirac spinor on $\mathbb{R}^3$ and $\Psi_p$ is a $\mathbb{C}$-valued spinor on $\mathbb{Q}_p^3$ of the type constructed in adelic quantum mechanics [1]. The free adelic Dirac equation is postulated sector-wise:

$$i\hbar \frac{\partial \Psi_p}{\partial t_p} = \left( c\, \boldsymbol{\alpha}_p \cdot \mathbf{D}_p + \beta_p m c^2 \right) \Psi_p, \qquad p \in \{\infty, 2, 3, 5, \dots\},$$

where $\mathbf{D}_\infty = -i\hbar \nabla$ is the usual momentum operator and $\mathbf{D}_p$ for $p$ finite is taken to be the Vladimirov-type pseudo-differential operator (the p-adic analogue of the Laplacian derivative, whose spectral theory underlies p-adic quantum mechanics [1]); $\boldsymbol{\alpha}_p, \beta_p$ are gamma-matrix structures over the respective field, whose existence as algebraic objects is consistent with p-adic linear-algebra geometry [8].

### 3.2 Sector-resolved velocity expectation

For each sector $s \in \{\infty, 2, 3, 5, \dots\}$ define the velocity expectation

$$v_s(t) = \int \Psi_s^\dagger(\mathbf{x},t)\, \alpha_s\, \Psi_s(\mathbf{x},t)\, d\mu_s(\mathbf{x}),$$

with $d\mu_\infty$ Lebesgue measure and $d\mu_p$ the Haar measure on $\mathbb{Q}_p^3$. For a wave packet that is a superposition of positive- and negative-energy branches with weights $a_+$ and $a_-$, the standard cross term produces an oscillatory contribution at the branch energy gap; in the real sector this is the Schrödinger–Breit trembling motion [4]. We postulate the same structure sector-wise, with the p-adic sector oscillation frequencies determined by the p-adic dispersion relation of the Vladimirov operator. The observable macroscopic position is the adele-diagonal projection

$$X(t) = w_\infty x_\infty(t) + \sum_{p \leq P} w_p x_p(t),$$

where $P$ is a finite cutoff (only finitely many p-adic norms of a rational differ from 1) and $w_s$ are sector weights.

### 3.3 Cancellation mechanism (conjecture)

Let $r = \ell/\lambda_C$ be the dimensionless ratio of the observation scale $\ell$ to the Compton wavelength $\lambda_C = \hbar/(mc)$, approximated by a rational number. We conjecture that the cross-sector interference amplitude in $X(t)$ is proportional to the product of p-adic norms of $r$:

$$A_{\mathrm{int}}(\ell) = A_0 \prod_{p} |r|_p = A_0 \frac{\lambda_C}{\ell},$$

where the last equality is the adele product formula, and $A_0$ is the single-sector trembling amplitude. Thus the p-adic contribution to the observed motion is suppressed by $\lambda_C/\ell$ at scales $\ell \gg \lambda_C$, and enhanced at $\ell \lesssim \lambda_C$. This is the precise sense in which "the p-adic contributions cancel at macroscopic scales."

### 3.4 Simulation plan

The conjecture is falsifiable by computation: (i) solve the p-adic Dirac equation with the Vladimirov operator on $\mathbb{Q}_p$ for Gaussian-type test packets, in the spirit of the Gaussian wave-packet analyses of ZBW in [7]; (ii) extract the sector frequency spectrum and check whether the p-adic sector frequencies scale with $|r|_p$ as conjectured; (iii) verify the product-formula cancellation numerically for truncated prime sets; (iv) compare the regularized adelic path integral against the exactly solvable quadratic-Lagrangian amplitudes of [5].

## 4. Analysis

All input constants are standard physical constants, stated here with their values; every subsequent number is derived from them by shown arithmetic.

**Inputs.**
- Electron mass $m_e = 9.109 \times 10^{-31}\,\mathrm{kg}$.
- Speed of light $c = 2.998 \times 10^{8}\,\mathrm{m\,s^{-1}}$.
- Reduced Planck constant $\hbar = 1.055 \times 10^{-34}\,\mathrm{J\,s}$.
- Newtonian constant $G = 6.674 \times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$.

**Step 1: Electron rest energy.**

$$m_e c^2 = 9.109 \times 10^{-31} \times (2.998 \times 10^{8})^2.$$

First, $c^2 = (2.998)^2 \times 10^{16} = 8.988 \times 10^{16}\,\mathrm{m^2\,s^{-2}}$. Then

$$m_e c^2 = 9.109 \times 8.988 \times 10^{-31+16} = 81.87 \times 10^{-15} = 8.187 \times 10^{-14}\,\mathrm{J}.$$

**Step 2: Zitterbewegung angular frequency.**

$$\omega_\infty = \frac{2 m_e c^2}{\hbar} = \frac{2 \times 8.187 \times 10^{-14}}{1.055 \times 10^{-34}} = \frac{1.6374 \times 10^{-13}}{1.055 \times 10^{-34}} = 1.552 \times 10^{21}\,\mathrm{rad\,s^{-1}}.$$

The corresponding cyclic frequency is

$$f_\infty = \frac{\omega_\infty}{2\pi} = \frac{1.552 \times 10^{21}}{6.2832} = 2.470 \times 10^{20}\,\mathrm{Hz}.$$

**Step 3: Compton wavelength.**

$$\lambda_C = \frac{\hbar}{m_e c} = \frac{1.055 \times 10^{-34}}{9.109 \times 10^{-31} \times 2.998 \times 10^{8}}.$$

Denominator: $9.109 \times 2.998 = 27.31$, so $m_e c = 2.731 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$. Then

$$\lambda_C = \frac{1.055 \times 10^{-34}}{2.731 \times 10^{-22}} = 3.862 \times 10^{-13}\,\mathrm{m}.$$

**Step 4: Planck length.**

$$\ell_P = \sqrt{\frac{\hbar G}{c^3}}.$$

Numerator: $\hbar G = 1.055 \times 10^{-34} \times 6.674 \times 10^{-11} = 7.041 \times 10^{-45}$. Denominator: $c^3 = (2.998 \times 10^8)^3 = 26.946 \times 10^{24} = 2.6946 \times 10^{25}$. Ratio:

$$\frac{\hbar G}{c^3} = \frac{7.041 \times 10^{-45}}{2.6946 \times 10^{25}} = 2.613 \times 10^{-70}\,\mathrm{m^2},$$

$$\ell_P = \sqrt{2.613 \times 10^{-70}} = 1.616 \times 10^{-35}\,\mathrm{m}.$$

**Step 5: Cross-sector interference amplitude at laboratory scale.** By the conjectured mechanism of Section 3.3, with $r = \ell/\lambda_C$:

$$\frac{A_{\mathrm{int}}(\ell)}{A_0} = \prod_p |r|_p = \frac{1}{|r|_\infty} = \frac{\lambda_C}{\ell}.$$

At $\ell = 1\,\mathrm{m}$:

$$\frac{A_{\mathrm{int}}}{A_0} = \frac{3.862 \times 10^{-13}}{1} = 3.862 \times 10^{-13}.$$

If an interferometric observable depends on intensity-like cross terms, the relative suppression is the square:

$$\left(\frac{A_{\mathrm{int}}}{A_0}\right)^2 = (3.862 \times 10^{-13})^2 = 1.492 \times 10^{-25}.$$

**Step 6: p-Adic dominance at the Planck scale.** At $\ell = \ell_P$:

$$\frac{\lambda_C}{\ell_P} = \frac{3.862 \times 10^{-13}}{1.616 \times 10^{-35}} = \frac{3.862}{1.616} \times 10^{22} = 2.390 \times 10^{22}.$$

That is, at the Planck length the product of p-adic norms exceeds the Archimedean norm ratio by a factor $\approx 2.39 \times 10^{22}$: the non-Archimedean sector dominates the interference amplitude by roughly 22 orders of magnitude, which is the quantitative content of the claim that "near the Compton/Planck length non-archimedean terms dominate."

**Step 7: Crossover scale.** The cancellation is "complete" to a given precision $\varepsilon$ when $\lambda_C/\ell < \varepsilon$, i.e. $\ell > \lambda_C/\varepsilon$. For single-precision-level suppression $\varepsilon = 10^{-6}$:

$$\ell > \frac{3.862 \times 10^{-13}}{10^{-6}} = 3.862 \times 10^{-7}\,\mathrm{m} = 386.2\,\mathrm{nm}.$$

So beyond optical wavelengths the p-adic interference is suppressed below $10^{-6}$ in amplitude.

**Step 8: Model-projected sector frequency shifts (labeled projection).** Assume the p-adic sector dispersion ties its oscillation frequency to the p-adic norm of the scale ratio: $\omega_p = \omega_\infty |r|_p$ for the finitely many primes with $|r|_p \neq 1$. Take $\ell = 10\,\lambda_C$, so $r = 10 = 2 \times 5$. Then $|10|_2 = 2^{-1} = 0.5$, $|10|_5 = 5^{-1} = 0.2$, and $|10|_p = 1$ for all other primes. Check of the product formula: $|10|_\infty \cdot |10|_2 \cdot |10|_5 = 10 \times 0.5 \times 0.2 = 1$. ✓. The projected sector frequencies are

$$f_2 = 0.5 \times 2.470 \times 10^{20} = 1.235 \times 10^{20}\,\mathrm{Hz}, \qquad f_5 = 0.2 \times 2.470 \times 10^{20} = 4.940 \times 10^{19}\,\mathrm{Hz}.$$

These are projections conditional on the stated dispersion assumption $\omega_p = \omega_\infty |r|_p$; they are not measurements, and the assumption itself is what the proposed $\mathbb{Q}_p$ simulations of Section 3.4 must test.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are empirical measurements.

1. **Standard ZBW frequency (real sector).** $\omega_\infty = 1.552 \times 10^{21}\,\mathrm{rad\,s^{-1}}$, i.e. $f_\infty = 2.470 \times 10^{20}\,\mathrm{Hz}$ for the electron, derived as $\omega_\infty = 2m_ec^2/\hbar$ (Steps 1–2).

2. **Compton wavelength.** $\lambda_C = 3.862 \times 10^{-13}\,\mathrm{m}$ (Step 3).

3. **Planck length.** $\ell_P = 1.616 \times 10^{-35}\,\mathrm{m}$ (Step 4).

4. **Product-formula cancellation (conjectured mechanism, exact arithmetic).** The cross-sector interference amplitude ratio is $A_{\mathrm{int}}/A_0 = \lambda_C/\ell$. At $\ell = 1\,\mathrm{m}$: $3.862 \times 10^{-13}$ in amplitude, $1.492 \times 10^{-25}$ in intensity-like terms (Step 5). The mechanism is exact for rational $r$ by the adele product formula; its physical content is the conjecture that the interference amplitude is proportional to $\prod_p |r|_p$.

5. **Non-Archimedean dominance at the Planck scale.** $\lambda_C/\ell_P = 2.390 \times 10^{22}$: the p-adic sector interference exceeds the real-sector scale ratio by about 22 orders of magnitude at $\ell = \ell_P$ (Step 6).

6. **Crossover scale.** p-Adic interference falls below relative amplitude $10^{-6}$ for $\ell > 3.862 \times 10^{-7}\,\mathrm{m} = 386.2\,\mathrm{nm}$ (Step 7).

7. **Projected sector frequency shifts (projection, stated assumption).** Under the assumption $\omega_p = \omega_\infty |r|_p$ with $r = 10$ ($\ell = 10\lambda_C$): $f_2 = 1.235 \times 10^{20}\,\mathrm{Hz}$, $f_5 = 4.940 \times 10^{19}\,\mathrm{Hz}$, all other sectors unshifted; the product formula check $10 \times 0.5 \times 0.2 = 1$ holds exactly (Step 8). Uncertainty in these projections is dominated by the untested dispersion assumption, not by the constants, which are exact to the digits given.

## 6. Discussion

**Status of the claims.** The numerical results (items 1–3, 6 of Section 5) are ordinary consequences of standard constants. The genuinely new content — items 4 and 5 — rests on one conjectural identification: that the cross-sector interference amplitude of the adelic Dirac dynamics is proportional to $\prod_p |r|_p$. The product formula then makes the cancellation exact and scale-independent in form, which is elegant, but elegance is not derivation. We have not derived the adelic Dirac equation from an action principle over $\mathbb{A}$, nor proven that the Vladimirov-operator spectrum produces frequencies scaling as $|r|_p$; both are stated as the test program of Section 3.4, not as results.

**Failure modes.** (i) The p-adic sector dynamics may not support oscillatory solutions at all: the Vladimirov operator has a spectral theory, but whether its Dirac-type coupling yields a two-branch structure with a gap analogous to $2mc^2$ is unverified. If the p-adic spectrum is continuous and gapless, there is no trembling analog and the entire cancellation mechanism is moot. (ii) The sector weights $w_p$ in the observable projection $X(t)$ are undetermined; if physical observables couple only to the Archimedean sector by construction, the p-adic sectors are dynamically inert decoration, and the "cancellation" is trivial. (iii)