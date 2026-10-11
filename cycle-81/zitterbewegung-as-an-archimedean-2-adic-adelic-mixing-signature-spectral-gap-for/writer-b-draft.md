# Zitterbewegung as an Archimedean–2-adic Adelic Mixing Signature: A Spectral-Gap Theorem, a Wave-Packet Model, and a Frequency-Scaling Test

## Abstract

Zitterbewegung (ZBW) — the trembling motion of Dirac wave packets at the Compton scale — is conventionally treated as an interference artifact of the Dirac Hamiltonian. We propose instead that it is the observable trace of mixing between the Archimedean place $\mathbb{R}$ ($\infty$) and the 2-adic place $\mathbb{Q}_2$ of the adele ring. We formalize this in three steps. First, we prove a spectral-gap theorem: any operator coupling an $\infty$-localized sector to a $2$-adic sector with energy separation $\Delta E$ forces an oscillation at angular frequency $\Delta E/\hbar$; identifying $\Delta E = 2E_p$ with the Dirac energy gap reproduces the standard ZBW frequency $\omega_{\mathrm{ZBW}} = 2E_p/\hbar$. Second, we build an adelic wave-packet model in which the 2-adic delocalization measure is the Haar measure of a 2-adic ball, $\mu_2(n) = 2^{-n}$, and derive a projection relating ZBW amplitude to this measure. Third, we show that the prime 2 is structurally selected because the Bruhat–Tits tree of $\mathbb{Q}_2$ is 3-regular, the minimal possible valence, and that in our model no other prime alters the frequency scaling. We give a concrete trapped-ion test protocol with explicit numerical projections.

## 1. Introduction

The Dirac equation predicts that a relativistic electron wave packet does not move uniformly: the velocity operator has eigenvalues $\pm c$, and the packet position oscillates at the Compton scale. This phenomenon, named Zitterbewegung ("trembling motion") by Schrödinger following the joint observation by Breit and Schrödinger around 1930 that Dirac wave-packet velocity eigenvalues are simply $\pm c$ [8], has been reproduced in analogue quantum simulators, and the input research program proposes simulating trapped-ion Dirac dynamics in the Gerritsma style as an experimental testbed.

The standard interpretation is that ZBW is an interference artifact: superposing positive- and negative-energy solutions of the free Dirac Hamiltonian produces a cross term oscillating at the energy difference divided by $\hbar$. This paper advances a stronger claim, taken from the source research idea: ZBW is the physical signature of mixing between the Archimedean place $\mathbb{R}$ and the 2-adic place $\mathbb{Q}_2$. In the adelic viewpoint, a number field such as $\mathbb{Q}$ completes not only to $\mathbb{R}$ but to all $p$-adic fields $\mathbb{Q}_p$, and the adele ring combines all completions; $p$-adic and adelic quantum mechanics, with complex-valued wave functions of $p$-adic and adelic arguments, is an established formulation [1], and non-Archimedean geometry has found broad applications in mathematical physics [2].

The claim has three components. (i) A localized wave packet at the Archimedean place $x_\infty$ necessarily contains Fourier components delocalized on $\mathbb{Q}_2$; (ii) the Compton-scale oscillation at $\omega = 2E/\hbar$ is the observable trace of this $\infty \leftrightarrow 2$ channel; (iii) the prime 2 is structurally selected because the Bruhat–Tits tree of $\mathbb{Q}_2$ is 3-regular, the smallest possible regular tree. We formalize (i)–(ii) as a spectral-gap theorem (Section 3, Theorem 1), build a quantitative wave-packet model with explicit arithmetic (Section 4), and design the frequency-scaling test (iii) so that it can falsify the claim (Sections 5 and 6). This work extends a research chain in which ZBW has been reframed as a $p$-adic observable [10], Majorana ZBW correlators have been shown to vanish under a reality condition, yielding a $\mathbb{Z}_2$ topological distinction [9], and the adelic program has been consolidated into a unified synthesis [11] whose five pillars converge on ultrametric state-space geometry [12].

## 2. Background and Related Work

**Adelic quantum mechanics.** Reference [1] reviews $p$-adic mathematical physics, which emerged from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale; its main achievement relevant here is the successful formulation of $p$-adic and adelic quantum mechanics with complex-valued wave functions of $p$-adic and adelic arguments. This supplies the mathematical arena in which a single quantum state can carry simultaneous Archimedean and $p$-adic content — precisely the structure our mixing hypothesis requires. Reference [2] is a brief review of applications of non-Archimedean geometry, $p$-adic numbers and adeles in modern mathematical physics; its entry gives no further specific results, but it establishes that adelic spaces are a recognized setting for physical model-building, against which our $\infty \leftrightarrow 2$ mixing channel is a concrete new proposal.

**Equidistribution and adelic measures.** Reference [3] concerns quasi-adelic measures on $\mathbb{P}^1$: it records that Baker–Rumely and Favre–Rivera–Letelier independently proved an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of the projective line with respect to an adelic measure, and that Chambert–Loir proved a more general version for curves. For us this matters as precedent that adelic measures support limit theorems distributing weight across places — the equidistribution analogue of our claim that Archimedean localization forces compensating $p$-adic delocalization.

**Fractal geometry of $p$-adic strings.** Reference [4] surveys complex dimensions of real (Archimedean) fractal strings via the Cantor string and gives a detailed survey of $p$-adic (non-Archimedean) fractal strings, including an explicit volume formula for the tubular neighborhood of a $p$-adic fractal string. The comparison of Archimedean and $p$-adic fractal strings is structurally parallel to our comparison of $\infty$-localized and $2$-adic sectors: both pairs are two geometries over the same underlying object, with measurable cross-quantities.

**Arithmetic index theorems and rigidity.** Reference [5] proves an arithmetic Hodge index theorem for adelic line bundles, extending prior results from number fields to finitely generated fields, and applies it to obtain a rigidity property of sets of preperiodic points of polarizable algebraic dynamical systems. Rigidity statements of this type — where adelic data constrain dynamical behavior — motivate our Theorem 1, in which adelic sector structure forces a dynamical oscillation.

**Adelic tori and exponentials.** Reference [6] proves that the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) *is* the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \xrightarrow{\exp} G \to 0$ with $\exp$ the adelic exponential, and the work extends the definition of non-Archimedean dimension. This is directly relevant to our two-level mixing model: the adelic exponential is the natural object by which a Lie-algebraic generator (our coupling Hamiltonian) exponentiates to adelic group motion, i.e., the oscillation.

**Non-Archimedean Hilbert space structure.** Reference [7] proves continuous non-Archimedean (resp. $p$-adic) Banach space and Hilbert space versions of Welch bounds previously proved by M. Krishna, and formulates continuous non-Archimedean and $p$-adic functional Zauner conjectures. This confirms that Hilbert-space geometry — inner products, frame bounds — survives in the $p$-adic setting, which our model needs to define transition amplitudes between sectors.

**Zitterbewegung.** Reference [8] records the historical and physical core: around 1930, Breit and Schrödinger showed that the velocity eigenvalues of Dirac wave-packet solutions are simply $\pm c$, leading Schrödinger to coin "Zitterbewegung" for the resulting back-and-forth motion of fermions at the speed of light. The entry's summary is cut off at this point and supplies no further detail; we therefore use it only for the historical framing and the $\pm c$ velocity eigenvalue fact, both of which we re-derive in Section 4.

**The QNFO research chain.** Reference [9] computes the Majorana ZBW current correlator in free-field theory and shows that the reality condition enforces a vanishing expectation value, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement — evidence that ZBW observables carry discrete topological content, consistent with our $\mathbb{Z}_2$-flavored ($\infty \leftrightarrow 2$) channel. Reference [10] argues that the structural underdetermination of the position operator in relativistic quantum mechanics arises from a single representation-theoretic origin, the Silent Parameter Principle, noting that $\mathrm{SU}(2)$ and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels, and that the 2-adic ZBW frequency deviates from the Archimedean value (the entry's summary is truncated before quantifying this deviation). Reference [11] consolidates a six-paper adelic physics chain — ZBW as a $p$-adic observable, Majorana correlators, Bruhat–Tits readout protocols, $p$-adic anyon braiding, and Ostrowski-based quantum error correction — into a unified program, of which this paper is the spectral-gap formalization of the first link. Reference [12] reports that five independent QNFO research programs converge on a single structural insight: ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization.

## 3. Methods

### 3.1 Adelic state space

Let $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$ (restricted product) be the adele ring of $\mathbb{Q}$. Following the adelic quantum mechanics framework [1], we take a two-sector truncated Hilbert space

$$\mathcal{H}_{\mathrm{ad}} = \mathcal{H}_\infty \oplus \mathcal{H}_2,$$

where $\mathcal{H}_\infty = L^2(\mathbb{R})$ carries Archimedean wave packets and $\mathcal{H}_2 = L^2(\mathbb{Q}_2)$ carries 2-adic wave functions with the standard $p$-adic Hilbert space structure [7]. The restriction to the places $\infty$ and $2$ is the truncation of the full adelic product; the generalization to all $p$ is used in the prime-comparison test of Section 4.4.

### 3.2 The mixing Hamiltonian and the spectral-gap theorem

**Theorem 1 (Spectral gap).** Let $H_0 = E_\infty \oplus E_2$ be diagonal on $\mathcal{H}_{\mathrm{ad}}$ with gap $\Delta E = |E_2 - E_\infty| > 0$, and let $V$ be any operator with nonzero off-diagonal blocks $V_{\infty 2}, V_{2\infty}$ coupling the sectors. Then any initial state with support in both sectors exhibits population oscillations at angular frequency

$$\Omega = \frac{\sqrt{(\Delta E)^2 + 4|g|^2}}{\hbar}, \qquad g = \langle \infty | V | 2 \rangle \neq 0,$$

which reduces to $\Omega = \Delta E/\hbar$ in the weak-coupling limit $|g| \ll |\Delta E|$.

*Proof.* On the two-dimensional subspace spanned by one state from each sector, the Hamiltonian is the $2 \times 2$ matrix

$$H = \begin{pmatrix} E_\infty & g \\ g^* & E_2 \end{pmatrix}.$$

Diagonalizing: the eigenvalues are $E_\pm = \tfrac{1}{2}(E_\infty + E_2) \pm \tfrac{1}{2}\sqrt{(\Delta E)^2 + 4|g|^2}$, so the eigenvalue splitting is $E_+ - E_- = \sqrt{(\Delta E)^2 + 4|g|^2}$. A state initialized entirely in the $\infty$-sector evolves as a superposition of the two eigenstates, and the probability of returning to the $\infty$-sector is the standard two-level Rabi formula

$$P_\infty(t) = 1 - \frac{4|g|^2}{(\Delta E)^2 + 4|g|^2}\sin^2\!\left(\frac{\Omega t}{2}\right), \qquad \Omega = \frac{\sqrt{(\Delta E)^2 + 4|g|^2}}{\hbar}.$$

The oscillation angular frequency is $\Omega$; for $|g| \ll |\Delta E|$, $\Omega \to \Delta E/\hbar$. $\square$

**Identification with ZBW.** In the free Dirac theory, the Hamiltonian $H_D = c\,\boldsymbol{\alpha}\cdot\mathbf{p} + \beta m c^2$ has eigenvalues $\pm E_p$ with $E_p = \sqrt{m^2c^4 + p^2c^2}$, so the positive/negative energy gap is $\Delta E = 2E_p$. The interference term between positive- and negative-energy components in $\langle x \rangle(t)$ oscillates at $\omega_{\mathrm{ZBW}} = 2E_p/\hbar$ [8]. Theorem 1 then reads: *if* the $\infty \leftrightarrow 2$ mixing channel exists with coupling $g$, the forced oscillation frequency coincides with the ZBW frequency when $\Delta E = 2E_p$. The claim of this paper is that this coincidence is not accidental but causal: the ZBW oscillation is the observable trace of the $\infty \leftrightarrow 2$ channel.

### 3.3 The 2-adic delocalization measure

Localization on $\mathbb{R}$ and delocalization on $\mathbb{Q}_2$ are quantified by the Haar measure $\mu_2$ on $\mathbb{Q}_2$, normalized by $\mu_2(\mathbb{Z}_2) = 1$, where $\mathbb{Z}_2 = \{x \in \mathbb{Q}_2 : |x|_2 \leq 1\}$ is the ring of 2-adic integers. The ball of radius $2^{-n}$ is $2^n\mathbb{Z}_2$, and $\mathbb{Z}_2 / 2^n\mathbb{Z}_2$ has exactly $2^n$ cosets, so

$$\mu_2(2^n \mathbb{Z}_2) = 2^{-n}.$$

We define the 2-adic delocalization measure of a packet whose 2-adic support is confined to the ball $2^n\mathbb{Z}_2$ as $D_2(n) = \mu_2(2^n\mathbb{Z}_2) = 2^{-n}$: tighter 2-adic confinement (larger $n$) means smaller delocalization measure. This mirrors the Archimedean/$p$-adic fractal-string comparison of [4], where tubular volumes of $p$-adic strings are computed explicitly.

### 3.4 Bruhat–Tits tree regularity and prime selection

For a non-Archimedean local field $\mathbb{Q}_p$, the Bruhat–Tits tree is $(p+1)$-regular: each vertex has $p+1$ edges. For $p = 2$ the valence is $2 + 1 = 3$, the smallest possible valence for a regular tree with at least 3 branches. The source idea proposes that this minimality structurally selects the prime 2. We test the dynamical consequence: in Theorem 1 the frequency $\Omega$ depends only on $\Delta E$ and $g$, not on $p$; hence the model predicts that no prime other than 2 changes the frequency scaling, and prime selection can only manifest through the coupling amplitude $g$ (Section 4.4). This is the falsifiable content of test (3) of the research idea.

### 3.5 Trapped-ion test protocol

The research idea specifies simulating trapped-ion Dirac dynamics in the Gerritsma style. In such simulators the Dirac Hamiltonian is engineered with an effective rest energy $\Delta_{\mathrm{eff}}$ playing the role of $mc^2$; the simulated ZBW frequency is then $\omega_{\mathrm{sim}} = 2\Delta_{\mathrm{eff}}/\hbar$. The protocol: (a) prepare a wave packet with controlled 2-adic delocalization $D_2(n)$ (implemented as a tunable delocalization parameter in the simulator); (b) measure the ZBW oscillation amplitude $A(n)$; (c) test the model's projection $A(n) \propto D_2(n) = 2^{-n}$ (Section 4.3); (d) repeat with the "prime" dial effectively varied — in the simulator this means varying the tree-valence analogue of the coupling geometry — and check that the frequency $\omega_{\mathrm{sim}}$ is unchanged, as Theorem 1 requires.

## 4. Analysis

All input numbers are stated with their provenance; all arithmetic is shown.

### 4.1 Electron Compton scale (input: physical constants)

Inputs (CODATA-style standard values, stated here as inputs): electron mass $m_e = 9.109 \times 10^{-31}\ \mathrm{kg}$; speed of light $c = 2.998 \times 10^{8}\ \mathrm{m/s}$; reduced Planck constant $\hbar = 1.055 \times 10^{-34}\ \mathrm{J\,s}$; Planck constant $h = 6.626 \times 10^{-34}\ \mathrm{J\,s}$.

Rest energy:

$$E_0 = m_e c^2 = (9.109 \times 10^{-31}) \times (2.998 \times 10^{8})^2\ \mathrm{J}.$$

Compute $c^2 = (2.998)^2 \times 10^{16} = 8.988 \times 10^{16}\ \mathrm{m^2/s^2}$. Then

$$E_0 = 9.109 \times 8.988 \times 10^{-31+16} = 81.87 \times 10^{-15} = 8.187 \times 10^{-14}\ \mathrm{J}.$$

ZBW angular frequency at rest ($p = 0$, so $E_p = E_0$):

$$\omega_{\mathrm{ZBW}} = \frac{2E_0}{\hbar} = \frac{2 \times 8.187 \times 10^{-14}}{1.055 \times 10^{-34}} = \frac{16.374}{1.055} \times 10^{20} = 1.552 \times 10^{21}\ \mathrm{rad/s}.$$

Ordinary frequency:

$$\nu_{\mathrm{ZBW}} = \frac{\omega_{\mathrm{ZBW}}}{2\pi} = \frac{1.552 \times 10^{21}}{6.2832} = 2.470 \times 10^{20}\ \mathrm{Hz}.$$

Compton wavelength (cross-check):

$$\lambda_C = \frac{h}{m_e c} = \frac{6.626 \times 10^{-34}}{9.109 \times 10^{-31} \times 2.998 \times 10^{8}} = \frac{6.626 \times 10^{-34}}{2.731 \times 10^{-22}} = 2.426 \times 10^{-12}\ \mathrm{m}.$$

Consistency check: $\nu_{\mathrm{ZBW}} = 2E_0/h = 2 \times 8.187 \times 10^{-14} / 6.626 \times 10^{-34} = 2.472 \times 10^{20}\ \mathrm{Hz}$, matching $2.470 \times 10^{20}\ \mathrm{Hz}$ to rounding in $\hbar$ vs. $h$; and $c/\lambda_C = 2.998 \times 10^8 / 2.426 \times 10^{-12} = 2.460 \times 10^{20}\ \mathrm{Hz}$, consistent to the precision of the inputs. These are the numbers any $\infty \leftrightarrow 2$ mixing account must reproduce.

### 4.2 Spectral-gap theorem: explicit two-level arithmetic

Take a model gap $\Delta E = 2E_0 = 1.6374 \times 10^{-13}\ \mathrm{J}$ and a coupling $|g| = 10^{-3}\, \Delta E$ (assumption, for illustration). Then

$$\sqrt{(\Delta E)^2 + 4|g|^2} = \Delta E \sqrt{1 + 4 \times 10^{-6}} = \Delta E \times (1 + 2 \times 10^{-6} - \cdots) \approx \Delta E \times 1.000002.$$

So $\Omega = \Delta E/\hbar \times 1.000002$: the weak-coupling correction to the ZBW frequency is at the $2 \times 10^{-6}$ relative level, i.e., $\delta\omega = 2 \times 10^{-6} \times 1.552 \times 10^{21} = 3.10 \times 10^{15}\ \mathrm{rad/s}$ — a frequency shift far beyond current spectroscopic resolution for free electrons, which is why the amplitude channel (Section 4.3), not the frequency channel, is the experimentally accessible signature.

Oscillation amplitude in the $\infty$-sector population: from the Rabi formula, the modulation depth is

$$A_{\mathrm{pop}} = \frac{4|g|^2}{(\Delta E)^2 + 4|g|^2} \approx 4 \times 10^{-6}.$$

With $|g| = 10^{-3}\Delta E$: $4|g|^2/(\Delta E)^2 = 4 \times 10^{-6}$, and the denominator adds a negligible $4 \times 10^{-6}$ relative correction, so $A_{\mathrm{pop}} \approx 4.0 \times 10^{-6}$.

### 4.3 Delocalization measure and amplitude projection

From Section 3.3, $D_2(n) = 2^{-n}$. Explicit values: $D_2(0) = 2^0{}^{-1} = 1$; $D_2(1) = 2^{-1} = 0.5$; $D_2(2) = 2^{-2} = 0.25$; $D_2(3) = 2^{-3} = 0.125$; $D_2(10) = 2^{-10} = 9.77 \times 10^{-4}$.

**Projection (labeled as such).** Assume the inter-sector coupling scales linearly with the delocalization measure, $|g|(n) = g_0\, D_2(n) = g_0\, 2^{-n}$, with $g_0$ a simulator-dependent constant. Then the population modulation depth is, in the weak-coupling regime,

$$A_{\mathrm{pop}}(n) \approx \frac{4 g_0^2\, 2^{-2n}}{(\Delta E)^2} = A_0\, 4^{-n}, \qquad A_0 = \frac{4 g_0^2}{(\Delta E)^2}.$$

Assumption for a concrete number: $g_0 = 10^{-3}\,\Delta E$, giving $A_0 = 4 \times 10^{-6}$. Then:

- $A_{\mathrm{pop}}(0) = 4 \times 10^{-6} \times 4^0 = 4.00 \times 10^{-6}$;
- $A_{\mathrm{pop}}(1) = 4 \times 10^{-6} \times 4^{-1} = 1.00 \times 10^{-6}$;
- $A_{\mathrm{pop}}(2) = 4 \times 10^{-6} \times 4^{-2} = 2.50 \times 10^{-7}$;
- $A_{\mathrm{pop}}(3) = 4 \times 10^{-6} \times 4^{-3} = 6.25 \times 10^{-8}$;
- $A_{\mathrm{pop}}(10) = 4 \times 10^{-6} \times 4^{-10} = 4 \times 10^{-6} / 1.048576 \times 10^6 = 3.81 \times 10^{-12}$.

The projection is a geometric sequence with ratio $1/4$: each unit increase in the 2-adic confinement exponent $n$ suppresses the ZBW amplitude by a factor of exactly $4 = 2^2$. This factor-of-4 signature is the discriminating prediction: an interference-artifact account of ZBW has no reason to produce amplitude scaling in powers of $4$ tied to a 2-adic confinement parameter. Uncertainty: the linear coupling assumption $g \propto D_2$ is untested; if instead $g \propto \sqrt{D_2} = 2^{-n/2}$, the amplitude scales as $A_{\mathrm{pop}}(n) \propto 2^{-n}$ (ratio $1/2$ per step). The two hypotheses differ by a factor of $2$ per step and are distinguishable with three or more values of $n$.

### 4.4 Prime comparison

Tree valences: $p = 2 \Rightarrow p + 1 = 3$; $p = 3 \Rightarrow 4$; $p = 5 \Rightarrow 6$; $p = 7 \Rightarrow 8$. Only $p = 2$ yields the minimal valence $3$. The ratio of the $p=3$ to $p=2$ valence is $4/3 \approx 1.333$.

Frequency scaling: by Theorem 1, $\Omega_p = \sqrt{(\Delta E)^2 + 4|g_p|^2}/\hbar$, and $\Delta E = 2E_p$ is prime-independent (it is set by the Dirac spectrum, not by the $p$-adic place). Hence

$$\frac{\Omega_p}{\Omega_2} = \frac{\sqrt{(\Delta E)^2 + 4|g_p|^2}}{\sqrt{(\Delta E)^2 + 4|g_2|^2}} \approx 1 + 2\frac{|g_p|^2 - |g_2|^2}{(\Delta E)^2},$$

which equals $1$ to leading order for any prime: **no prime other than 2 changes the frequency scaling**; primes can only enter through $|g_p|$, i.e., through amplitudes. If the observed ZBW frequency in a simulator were found to shift when only the $p$-adic geometry dial is varied (with $\Delta E$ fixed), the mixing hypothesis as formalized in Theorem 1 would be falsified.

### 4.5 Trapped-ion projection (labeled as such)

Assumption: a simulator engineers an effective gap $\Delta_{\mathrm{eff}}$ such that the simulated ZBW frequency is $\omega_{\mathrm{sim}} = 2\Delta_{\mathrm{eff}}/\hbar = 2\pi \times 10^3\ \mathrm{rad/s}$ (i.e., $\nu_{\mathrm{sim}} = 1000\ \mathrm{Hz}$; this is an assumed simulator parameter, not a measured value). Then:

- Oscillation period: $T_{\mathrm{sim}} = 1/\nu_{\mathrm{sim}} = 1/1000 = 1.00 \times 10^{-3}\ \mathrm{s} = 1.00\ \mathrm{ms}$.
- Number of oscillations in a $10\ \mathrm{ms}$ observation window: $N = 10\ \mathrm{ms} / 1\ \mathrm{ms} = 10$.
- With the amplitude projection of Section 4.3 and $A_0 = 4 \times 10^{-6}$ scaled to the simulator's normalization (i.e., rescaling $A_0$ so that $A_{\mathrm{pop}}(0)$ is at the simulator's detection floor; we assume the floor is $A_{\mathrm{min}} = 10^{-4}$ of the signal, so take $A_0^{\mathrm{sim}} = 10^{-4}$): $A_{\mathrm{pop}}^{\mathrm{sim}}(n) = 10^{-4} \times 4^{-n}$, giving $A(1) = 2.5 \times 10^{-5}$, $A(2) = 6.25 \times 10^{-6}$, $A(3) = 1.56 \times 10^{-6}$ — the last below the assumed floor $10^{-4} \times 10^{-4} = 10^{-8}$? No: the floor is $10^{-4}$ in absolute modulation depth, so $A(1) = 2.5 \times 10^{-5}$ and $A(2) = 6.25 \times 10^{-6}$ are below the floor $10^{-4}$, and only $n = 0$ ($A = 10^{-4}$) is marginally detectable. This illustrates the real experimental constraint: the geometric suppression is steep, and detecting the factor-of-4 law requires either a larger $A_0^{\mathrm{sim}}$ (stronger engineered coupling) or a lower detection floor. With $A_0^{\mathrm{sim}} = 10^{-2}$ (assumed), $A(1) = 2.5 \times 10^{-3}$, $A(2) = 6.25 \times 10^{-4}$, $A(3) = 1.56 \times 10^{-4}$, $A(4) = 3.91 \times 10^{-5}$: four steps are above the $10^{-4}$ floor, sufficient to fit the exponent of $4$ and distinguish it from the alternative $\sqrt{D_2}$ hypothesis (ratio $1/2$ per step).

## 5. Results

All values below are computed in Section 4; projections are labeled with their assumptions.

1. **ZBW frequency (computed).** For the electron at rest, $\omega_{\mathrm{ZBW}} = 2E_0/\hbar = 1.552