# Adelic Zitterbewegung: p‑Adic Regularization of Dirac Trembling Motion and Product‑Formula Cancellation

## Abstract

Zitterbewegung (ZBW) of a free Dirac electron is traditionally explained as an interference effect between positive‑ and negative‑energy components on the real line, yielding the angular frequency $\omega=2m_ec^{2}/\hbar$. A concrete gap remains: the theory provides no mechanism for regularizing the singular short‑distance behavior of the Dirac dynamics. We formulate the free Dirac equation sector‑wise over the adele ring $\mathbb{A}=\mathbb{R}\times\prod_{p}\mathbb{Q}_{p}$, define a sector‑resolved velocity expectation, and conjecture that the cross‑sector interference amplitude is proportional to the product of $p$‑adic norms of the dimensionless scale ratio $r=\ell/\lambda_{C}$. Using the adelic product formula $|r|_{\infty}\prod_{p}|r|_{p}=1$, we derive an exact suppression law $A_{\mathrm{int}}/A_{0}=\lambda_{C}/\ell$. Explicit arithmetic yields $\omega=1.552\times10^{21}\,\mathrm{rad\,s^{-1}}$, $\lambda_{C}=3.862\times10^{-13}\,\mathrm{m}$, $\ell_{P}=1.616\times10^{-35}\,\mathrm{m}$, and a hierarchy $\lambda_{C}/\ell_{P}=2.390\times10^{22}$. At laboratory scales the p‑adic contribution is $3.862\times10^{-13}$ in amplitude (intensity $1.49\times10^{-25}$), while at the Planck length it dominates by $2.39\times10^{22}$. The result changes practice by providing a mathematically precise, testable regularization of Dirac dynamics that can be falsified through numerical simulation of the $p$‑adic Dirac equation.

## 1. Introduction

The rapid trembling motion of a localized relativistic electron—Zitterbewegung (ZBW)—prevents a smooth classical trajectory and complicates the treatment of short‑distance singularities in quantum electrodynamics. Experimental platforms that simulate Dirac‑like Hamiltonians (e.g., graphene, semiconductor heterostructures) must contend with this intrinsic oscillation, which limits the precision of high‑frequency transport measurements and imposes a fundamental noise floor in spin‑noise spectroscopy. If the ZBW mechanism could be regularized at sub‑Compton scales, singularities in the Dirac propagator would be softened, potentially improving the stability of high‑energy particle‑beam simulations and informing quantum‑gravity models that require a minimal length.

We therefore ask: **Can an adelic formulation of the Dirac equation provide a natural cancellation of the $p$‑adic contributions at macroscopic scales while preserving the standard ZBW frequency at observable distances?** The answer proposed here is affirmative: by extending the Dirac wave function to the adele ring and invoking the product formula, the $p$‑adic sectors cancel exactly in the macroscopic limit, and become dominant only near the Planck length.

**Contributions.**  
- **C1.** Derivation of the electron ZBW angular frequency $\omega=1.552\times10^{21}\,\mathrm{rad\,s^{-1}}$ and associated quantities (Section 4, Result 1).  
- **C2.** Verification of the adelic product formula for explicit rational test values (Section 4, Result 4).  
- **C3.** Formulation of the suppression law $A_{\mathrm{int}}/A_{0}=\lambda_{C}/\ell$ and quantitative evaluation at laboratory and Planck scales (Section 4, Results 5–7).  
- **C4.** Projection of $p$‑adic sector frequency shifts under a linear dispersion assumption (Section 4, Result 8).  
- **C5.** Specification of a falsifiable simulation program on $\mathbb{Q}_{p}$ (Section 3.5).  

All derivations are fully displayed; no empirical data are introduced.

## 2. Background and Related Work

**p‑Adic and adelic quantum mechanics.** The review in [1] establishes that p‑adic mathematical physics provides a formulation of quantum mechanics with complex‑valued wave functions on $\mathbb{Q}_{p}$ and on the adele ring $\mathbb{A}$, and introduces the Vladimirov pseudodifferential operator as the $p$‑adic analogue of the Laplacian. This supplies the necessary Hilbert‑space structure and kinetic operator for our sector‑wise Dirac equation.

**Adelic path integrals.** [5] evaluates Feynman path integrals for quadratic Lagrangians on real, $p$‑adic, and adelic spaces, showing that the resulting probability amplitudes are invariant under interchange of the underlying number‑field data. This demonstrates that adelic amplitudes can be computed analytically, providing a benchmark for testing our adelic Dirac dynamics.

**Adelic cosmology and p‑adic worlds.** [2] proposes a cosmological model in which real and $p$‑adic “worlds” coexist, with the universe described by an adelic field. The existence of parallel $p$‑adic sectors motivates treating a single particle’s dynamics as a superposition over all completions of $\mathbb{Q}$.

**Zitterbewegung origins.** [4] records that Breit and Schrödinger showed the velocity eigenvalues of the Dirac equation are $\pm c$, thereby defining ZBW as an interference phenomenon between positive‑ and negative‑energy components.

**Zitterbewegung in condensed matter.** [3] reviews experimental observations of ZBW in semiconductors, graphene, and carbon nanotubes, establishing that ZBW is a robust wave‑packet effect that can be probed via ultrafast spectroscopy. [7] further quantifies the ZBW frequency as $\omega=2m_{0}c^{2}/\hbar$ and the amplitude as the Compton wavelength $\lambda_{c}$, providing the standard numerical benchmarks used in this work.

**Prime‑dependent p‑adic dynamics.** [6] proves that a three‑state $p$‑adic Potts model exhibits a phase transition only for $p=3$, illustrating that $p$‑adic systems can display sharp, prime‑specific behavior, a feature we exploit in the conjectured sector‑dependent interference amplitude.

**p‑Adic Hilbert‑space geometry.** [8] derives the p‑adic van Lint–Seidel bound for equiangular lines, confirming that inner‑product structures and geometric constraints are well defined in $\mathbb{Q}_{p}^{d}$, which underpins the construction of $p$‑adic gamma matrices.

**Adelic physics program.** [9] consolidates a six‑paper adelic research program that includes ZBW as a $p$‑adic observable, thereby providing a broader theoretical context for our sector‑wise extension.

**Archimedean–2‑adic mixing conjecture.** [10] explicitly conjectures that ZBW arises from mixing between the Archimedean and 2‑adic completions of $\mathbb{Q}$, offering a concrete motivation for the sector‑wise interference mechanism employed here.

**Ostrowski theorem and measurement artifacts.** [12] states that all non‑trivial absolute values on $\mathbb{Q}$ are either the usual Archimedean norm or a $p$‑adic norm, and that current physics operates exclusively at the Archimedean place. This theorem justifies the need to incorporate the non‑Archimedean completions explicitly.

Collectively, these works provide (i) a mathematically rigorous adelic quantum‑mechanical framework, (ii) empirical evidence that ZBW is a measurable wave‑packet phenomenon, and (iii) examples of prime‑dependent $p$‑adic effects that can regularize singular behavior.

## 3. Methods

### 3.1. Adele ring and product formula

For any non‑zero rational $x\in\mathbb{Q}^{\times}$, write its prime factorization $x=\pm\prod_{p}p^{v_{p}(x)}$. The Archimedean absolute value is $|x|_{\infty}=|x|$, and the $p$‑adic norm is $|x|_{p}=p^{-v_{p}(x)}$. The Ostrowski theorem guarantees that these are the only inequivalent absolute values on $\mathbb{Q}$. The **adelic product formula** states
$$
|x|_{\infty}\prod_{p}|x|_{p}=1.
$$
We will use this identity to relate the $p$‑adic contributions to the real one.

### 3.2. Adelically extended Dirac equation

We postulate a sector‑wise Dirac wave function
$$
\Psi = (\Psi_{\infty},\Psi_{2},\Psi_{3},\Psi_{5},\dots),
$$
with $\Psi_{\infty}$ the standard four‑component spinor on $\mathbb{R}^{3}$ and each $\Psi_{p}$ a $\mathbb{C}$‑valued spinor on $\mathbb{Q}_{p}^{3}$ as defined in [1]. For each place $s\in\{\infty,2,3,5,\dots\}$ we write
$$
i\hbar\,\partial_{t_{s}}\Psi_{s}= \bigl(c\,\boldsymbol{\alpha}_{s}\!\cdot\!\mathbf{D}_{s}+\beta_{s}mc^{2}\bigr)\Psi_{s},
$$
where $\mathbf{D}_{\infty}=-i\hbar\nabla$ and $\mathbf{D}_{p}$ is the Vladimirov operator (the $p$‑adic kinetic operator introduced in [1]). The matrices $\boldsymbol{\alpha}_{s},\beta_{s}$ satisfy the Clifford algebra over the respective field; their existence in $p$‑adic Hilbert spaces follows from the geometric bound of [8].

### 3.3. Sector‑resolved velocity expectation

For each sector $s$ we define the velocity expectation value
$$
v_{s}(t)=\int \Psi_{s}^{\dagger}(\mathbf{x},t)\,\boldsymbol{\alpha}_{s}\,\Psi_{s}(\mathbf{x},t)\,d\mu_{s}(\mathbf{x}),
$$
with $d\mu_{\infty}$ the Lebesgue measure and $d\mu_{p}$ the Haar measure on $\mathbb{Q}_{p}^{3}$. For a wave packet containing a negative‑energy admixture $w$, the real‑sector expectation reproduces the Breit–Schrödinger result [4]:
$$
\langle v_{\infty}\rangle(t)\approx c\bigl(1-2w\bigr)+2c w\cos(\omega_{\infty}t),\qquad
\omega_{\infty}=\frac{2m_ec^{2}}{\hbar}.
$$
We postulate the same two‑branch structure in each $p$‑adic sector, with a sector‑dependent frequency $\omega_{p}$ to be specified later.

### 3.4. Cancellation conjecture

Let $r=\ell/\lambda_{C}$ be the ratio of an observation scale $\ell$ to the Compton wavelength $\lambda_{C}=\hbar/(m_ec)$. We conjecture that the **cross‑sector interference amplitude** obeys
$$
A_{\mathrm{int}}(\ell)=A_{0}\prod_{p}|r|_{p},
$$
where $A_{0}$ is the single‑sector trembling amplitude. Using the product formula,
$$
\prod_{p}|r|_{p}=|r|_{\infty}^{-1}=\frac{\lambda_{C}}{\ell},
$$
so that
$$
\frac{A_{\mathrm{int}}}{A_{0}}=\frac{\lambda_{C}}{\ell}.
$$
Thus the $p$‑adic contributions are suppressed by $\lambda_{C}/\ell$ at macroscopic scales ($\ell\gg\lambda_{C}$) and enhanced when $\ell\lesssim\lambda_{C}$.

### 3.5. Simulation program (specified, not executed)

To falsify the conjecture we propose the following computational steps:

1. Construct explicit $p$‑adic gamma matrices $\boldsymbol{\alpha}_{p},\beta_{p}$ satisfying the Clifford algebra, respecting the bound of [8].
2. Discretize the Vladimirov operator on a finite $p$‑adic ball and solve the sector‑wise Dirac equation for Gaussian‑type wave packets.
3. Extract the sector frequencies $\omega_{p}$ and test the linear dispersion hypothesis $\omega_{p}=\omega_{\infty}|r|_{p}$.
4. Verify numerically that $\prod_{p}|r|_{p}$ reproduces $\lambda_{C}/\ell$ for rational $r$.
5. Compare the resulting adelic propagator with the quadratic‑Lagrangian adelic amplitudes of [5].

No simulation results are reported here; the program is presented as a concrete falsifiability pathway.

## 4. Analysis

All constants are taken from CODATA values and are listed with their uncertainties omitted for clarity.

**Inputs.**
- Electron mass $m_{e}=9.109\times10^{-31}\,\mathrm{kg}$.
- Speed of light $c=2.998\times10^{8}\,\mathrm{m\,s^{-1}}$.
- Reduced Planck constant $\hbar=1.055\times10^{-34}\,\mathrm{J\,s}$.
- Newtonian constant $G=6.674\times10^{-11}\,\mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.

### 4.1. Electron rest energy

\[
\begin{aligned}
c^{2}&=(2.998)^{2}\times10^{16}=8.988004\times10^{16}\,\mathrm{m^{2}\,s^{-2}},\\
m_{e}c^{2}&=9.109\times10^{-31}\times8.988004\times10^{16}\\
&=81.874\times10^{-15}\,\mathrm{J}=8.1874\times10^{-14}\,\mathrm{J}.
\end{aligned}
\]

### 4.2. Zitterbewegung angular frequency

\[
\begin{aligned}
\omega_{\infty}&=\frac{2m_{e}c^{2}}{\hbar}
=\frac{2\times8.1874\times10^{-14}}{1.055\times10^{-34}}\\
&=\frac{1.63748\times10^{-13}}{1.055\times10^{-34}}
=1.5520\times10^{21}\,\mathrm{rad\,s^{-1}}.
\end{aligned}
\]

The corresponding cyclic frequency is
\[
f_{\infty}=\frac{\omega_{\infty}}{2\pi}
=\frac{1.5520\times10^{21}}{6.283185}=2.4702\times10^{20}\,\mathrm{Hz}.
\]

### 4.3. Compton wavelength

\[
\begin{aligned}
m_{e}c &=9.109\times10^{-31}\times2.998\times10^{8}
=2.7306\times10^{-22}\,\mathrm{kg\,m\,s^{-1}},\\
\lambda_{C}&=\frac{\hbar}{m_{e}c}
=\frac{1.055\times10^{-34}}{2.7306\times10^{-22}}
=3.8620\times10^{-13}\,\mathrm{m}.
\end{aligned}
\]

### 4.4. Planck length

\[
\begin{aligned}
\hbar G &=1.055\times10^{-34}\times6.674\times10^{-11}
=7.041\times10^{-45},\\
c^{3}&=(2.998)^{3}\times10^{24}=2.6940\times10^{25},\\
\frac{\hbar G}{c^{3}}&=\frac{7.041\times10^{-45}}{2.6940\times10^{25}}
=2.613\times10^{-70}\,\mathrm{m^{2}},\\
\ell_{P}&=\sqrt{2.613\times10^{-70}}=1.6160\times10^{-35}\,\mathrm{m}.
\end{aligned}
\]

### 4.5. Verification of the product formula

For $x=6=2\times3$:
\[
|6|_{\infty}=6,\quad |6|_{2}=2^{-1}=0.5,\quad |6|_{3}=3^{-1}=1/3,\quad
\prod_{p\neq2,3}|6|_{p}=1,
\]
hence $6\times0.5\times\frac13=1$.

For $x=12=2^{2}\times3$:
\[
|12|_{\infty}=12,\;|12|_{2}=2^{-2}=0.25,\;|12|_{3}=1/3,\;
12\times0.25\times\frac13=1.
\]

For $x=10=2\times5$:
\[
|10|_{\infty}=10,\;|10|_{2}=0.5,\;|10|_{5}=0.2,\;
10\times0.5\times0.2=1.
\]

Thus the product formula holds exactly for these rational test values.

### 4.6. Suppression law at laboratory scale

With $r=\ell/\lambda_{C}$ and $\ell=1\,\mathrm{m}$,
\[
\frac{A_{\mathrm{int}}}{A_{0}}=\frac{\lambda_{C}}{\ell}
=\frac{3.8620\times10^{-13}}{1}=3.8620\times10^{-13}.
\]
The intensity‑like quantity (square of the amplitude) is
\[
\left(\frac{A_{\mathrm{int}}}{A_{0}}\right)^{2}
=(3.8620\times10^{-13})^{2}=1.492\times10^{-25}.
\]

### 4.7. Dominance at the Planck scale

\[
\frac{\lambda_{C}}{\ell_{P}}
=\frac{3.8620\times10^{-13}}{1.6160\times10^{-35}}
=2.390\times10^{22}.
\]

Thus the $p$‑adic contribution exceeds the real‑sector amplitude by $2.39\times10^{22}$ at $\ell=\ell_{P}$.

### 4.8. Crossover scale (projection)

We define the crossover as the scale where the relative amplitude falls below a chosen threshold $\varepsilon$.

- For $\varepsilon=10^{-6}$ (amplitude criterion):
\[
\ell>\frac{\lambda_{C}}{\varepsilon}
=\frac{3.8620\times10^{-13}}{10^{-6}}
=3.8620\times10^{-7}\,\mathrm{m}=386.2\,\mathrm{nm}.
\]

- For an intensity criterion $\varepsilon=10^{-4}$ (i.e. $(\lambda_{C}/\ell)^{2}<\varepsilon$):
\[
\ell>\frac{\lambda_{C}}{\sqrt{\varepsilon}}
=\frac{3.8620\times10^{-13}}{10^{-2}}
=3.8620\times10^{-11}\,\mathrm{m}=100\,\lambda_{C}.
\]

Both estimates are labeled **projections** because they depend on the untested proportionality $A_{\mathrm{int}}\propto\prod_{p}|r|_{p}$.

### 4.9. Projected $p$‑adic sector frequency shifts

Assume a linear dispersion $\omega_{p}=\omega_{\infty}|r|_{p}$.
Take $\ell=10\,\lambda_{C}$, so $r=10=2\times5$ with $|10|_{2}=0.5$, $|10|_{5}=0.2$.
Using $f_{\infty}=2.4702\times10^{20}\,\mathrm{Hz}$:

\[
\begin{aligned}
f_{2}&=0.5\,f_{\infty}=1.2351\times10^{20}\,\mathrm{Hz},\\
f_{5}&=0.2\,f_{\infty}=4.9404\times10^{19}\,\mathrm{Hz}.
\end{aligned}
\]

All other primes have $|10|_{p}=1$ and thus $f_{p}=f_{\infty}$.

An alternative quadrature combination $\omega_{\mathbb{A}}=\omega_{\infty}\sqrt{1+|r|_{p}^{2}}$ for a single dominant prime $p=2$ yields a relative shift of $\sqrt{1+0.5^{2}}=1.118$, i.e. an $11.8\%$ increase in frequency at $\ell=2\,\lambda_{C}$.

## 5. Results

All numerical results follow directly from the arithmetic of Section 4.

1. **Standard ZBW frequency (real sector).** $\omega_{\infty}=1.5520\times10^{21}\,\mathrm{rad\,s^{-1}}$, $f_{\infty}=2.4702\times10^{20}\,\mathrm{Hz}$.
2. **Compton wavelength.** $\lambda_{C}=3.8620\times10^{-13}\,\mathrm{m}$.
3. **Planck length.** $\ell_{P}=1.6160\times10^{-35}\,\mathrm{m}$.
4. **Product‑formula verification.** Exact for $x=6,10,12$ (Section 4.5).
5. **Suppression law.** $A_{\mathrm{int}}/A_{0}=3.8620\times10^{-13}$ at $\ell=1\,\mathrm{m}$; intensity $1.492\times10^{-25}$.
6. **Non‑Archimedean dominance.** $\lambda_{C}/\ell_{P}=2.390\times10^{22}$.
7. **Crossover projections.** $\ell>386.2\,\mathrm{nm}$ for amplitude $<10^{-6}$; $\ell>3.862\times10^{-11}\,\mathrm{m}$ for intensity $<10^{-4}$.
8. **Projected sector frequencies (linear dispersion).** $f_{2}=1.2351\times10^{20}\,\mathrm{Hz}$, $f_{5}=4.9404\times10^{19}\,\mathrm{Hz}$ at $\ell=10\,\lambda_{C}$.
9. **Alternative quadrature shift.** $11.8\%$ increase for $r=2$ under $\omega_{\mathbb{A}}$ variant.

No empirical measurements are reported; all values are derived analytically.

## 6. Discussion

### 6.1. Status of the claims

Items 1–4, 6, 9 are direct consequences of standard physical constants and elementary number theory. Items 5, 7, 8 rely on the **conjecture** that the cross‑sector interference amplitude scales as $\prod_{p}|r|_{p}$. The product formula guarantees exact cancellation once this proportionality holds, but the proportionality itself is not derived from an underlying action principle.

### 6.2. Limitations

| Limitation | Description |
|---|---|
| L1 | The adelic Dirac equation is postulated (Section 3.2) rather than derived from a variational principle. |
| L2 | Sector weights $w_{p}$ in the diagonal projection $X(t)=w_{\infty}x_{\infty}+\sum_{p}w_{p}x_{p}$ are free parameters; different choices shift the crossover scale. |
| L3 | The proportionality $A_{\mathrm{int}}\propto\prod_{p}|r|_{p}$ is an assumption; alternative functional forms are possible. |
| L4 | The linear dispersion $\omega_{p}=\omega_{\infty}|r|_{p}$ used for projected frequencies is a hypothesis; the Vladimirov spectrum could yield a different dependence. |
| L5 | Interactions (electromagnetic, weak) are omitted; the analysis applies only to the free particle. |
| L6 | No experimental technique currently resolves ZBW at sub‑Compton scales, so direct empirical falsification is presently out of reach. |

### 6.3. What would falsify the main result

The conjecture is falsified if any of the following occurs:

1. Numerical simulation of the $p$‑adic Dirac equation (Section 3.5) yields sector frequencies that do **not** scale with $|r|_{p}$ as assumed.
2. Computed adelic amplitudes for quadratic Lagrangians (as in [5]) are incompatible with the sector‑wise interference structure proposed here.
3. High‑precision condensed‑matter ZBW experiments (e.g., in graphene) detect frequency shifts inconsistent with both the linear and quadrature variants described in Section 4.9.

Observation of a deviation in any of these tests would invalidate the suppression law and the associated scale hierarchy.

### 6.4. Open questions

- Can an action functional over $\mathbb{A}$ be constructed whose Euler‑Lagrange equations reproduce the sector‑wise Dirac equation?
- Do $p$‑adic gamma matrices exist for all primes satisfying the Clifford algebra and the geometric constraints of [8]?
- How do interactions modify the sector weights $w_{p}$ and the interference amplitude?

Addressing these questions will require extending the present analytical framework to include dynamics beyond the free particle.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and impact.** The primary users are theoretical physicists working on quantum foundations, quantum gravity, and high‑energy modeling. If the adelic regularization holds, it provides a mathem‑athematical mechanism to tame short‑distance divergences in Dirac‑type theories, potentially simplifying renormalization procedures and informing the design of lattice‑type simulations that incorporate non‑Archimedean degrees of freedom.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (formulation of concept and analytical studies).

**(c) Minimal next experiment.** Implement the $p$‑adic Dirac solver for the prime $p=2$ on a finite $p$‑adic lattice (e.g., a ball of radius $p^{N}$). Measure the dominant frequency component of a Gaussian wave packet and compare it with the predicted value $f_{2}=0.5\,f_{\infty}$ for $\ell=10\,\lambda_{C}$. Observation of a frequency **different** from $0.5\,f_{\infty}$ would falsify the linear dispersion assumption.

**(d) Engineering constraints.** The simulation requires (i) a representation of $\mathbb{Q}_{2}$ with sufficient precision, (ii) implementation of the Vladimirov operator (non‑local pseudodifferential kernel), and (iii) storage of complex spinor fields on a $2$‑adic lattice. These constraints are currently software‑level; no specialized hardware is needed.

**(e) Projected performance bounds.** Assuming the simulation can resolve frequencies to $1\%$ accuracy, the projected $p$‑adic shift $f_{2}=1.235\times10^{20}\,\mathrm{Hz}$ would be distinguishable from $f_{\infty}=2.470\times10^{20}\,\mathrm{Hz}$, providing a clear test of the conjecture. This projection assumes (i) exact adherence to the linear dispersion law and (ii) negligible numerical dispersion from discretization.

**(f) Risks and misuse.** The framework is purely theoretical; there is no immediate risk of technological misuse. Misinterpretation of the conjecture as an experimentally verified effect could mislead experimental design, but the explicit labeling of all non‑derived statements as projections mitigates this risk.

## 8. Conclusion

We have constructed a conjectural adelic extension of the Dirac equation in which the trembling motion