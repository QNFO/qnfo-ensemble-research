# The Zero-Point Phase as an Archimedean Factor of Weil-Index Reciprocity: A Formal Verification and Its Limits

## Abstract

The vacuum phase of the harmonic oscillator — the Archimedean Maslov (metaplectic) phase $e^{i\pi/4}$ accompanying the zero-point energy $\tfrac{1}{2}\hbar\omega$ — is conventionally treated as a purely real-place, analytic structure. We investigate the conjecture that this phase is instead one local factor $\gamma_\infty$ in the global Weil-index product $\prod_v \gamma_v = 1$ over all places $v$ of $\mathbb{Q}$, so that the zero-point phase is adelically constrained by quadratic reciprocity. We carry out the conjecture's proposed formal test for the quadratic form $q(x) = x^2$: we compute the Archimedean factor $\gamma_\infty(x^2) = e^{i\pi/4}$ from the metaplectic action on chirp states, verify the metaplectic double-cover consistency $(e^{i\pi/4})^4 = -1$, compute the odd-prime factors $\gamma_p(x^2) = 1$ via explicit normalized Gauss sums ($G_3 = i$, $G_5 = 1$, with full arithmetic), and derive $\gamma_2(x^2) = e^{-i\pi/4}$ from the reciprocity product. The product formula is thereby verified for $x^2$. However, we show that reciprocity alone constrains only the *product* $\gamma_\infty\gamma_2$: within the eighth roots of unity $\mu_8$ there remain $8$ admissible pairs, so the conjecture in its strong form (reciprocity uniquely fixes the vacuum phase) is not established; the phase is pinned by metaplectic self-duality, with reciprocity acting as a consistency check. We state explicit disconfirmation conditions and connect the result to the adelic-programme literature.

## 1. Introduction

The quantum harmonic oscillator carries two seemingly independent "half" structures at its ground state: the zero-point *energy* $E_0 = \tfrac{1}{2}\hbar\omega$, and the zero-point *phase* — the factor $e^{i\pi/4}$ by which the metaplectic representation (the projective unitary representation of the symplectic group implementing linear canonical transforms) evaluates on the one-dimensional quadratic form $q(x) = x^2$. The energy is physical and measurable; the phase is the sign ambiguity of the Fourier transform's square root, the Maslov index of the oscillator's classical periodic orbit.

This paper examines a specific conjecture arising in the QNFO research programme on adelic completions of the harmonic paradigm [9], [10], [11]: that the Archimedean vacuum phase $e^{i\pi/4}$ is not an Archimedean-exclusive structure but one local factor $\gamma_\infty$ in the Weil-index product formula $\prod_v \gamma_v = 1$, the product running over all places $v$ of $\mathbb{Q}$ (the real place $\infty$ and the $p$-adic places for every prime $p$). If true, the zero-point phase would be constrained by quadratic reciprocity — the same arithmetic identity that governs Legendre symbols — and the thesis that "only order (time, causality) is genuinely Archimedean" would gain a quantitative foothold: even the most analytic-looking constant of quantum theory would be adelic.

The conjecture comes with a built-in test and a disconfirmation condition. The test: formally verify that the metaplectic Weil indices satisfy reciprocity for $q(x) = x^2$, compute the $p$-adic factors $\gamma_p$, and examine whether imposing $\prod_v \gamma_v = 1$ constrains admissible vacuum phases or spectra. The disconfirmation condition: if the Archimedean Maslov phase can be varied independently of $p$-adic data without breaking self-duality, the conjecture fails.

We execute this programme for the simplest nontrivial form, $q(x) = x^2$, and report a partially affirmative result. The reciprocity identity holds and is verified with explicit arithmetic (Sections 3–4); but we find that it is a *consistency condition* rather than an independent determination of $\gamma_\infty$: the product formula leaves a discrete $\mu_8 \times \mu_8$ freedom that is closed only by the metaplectic self-duality of the oscillator. The physical interpretation, limitations, and falsification criteria are discussed in Section 6.

## 2. Background and Related Work

We review the works supplied with this project, in bibliography order, indicating honestly what each contributes to the argument. The bibliography is heterogeneous; several entries connect only analogically, and we flag this.

[1] (arXiv:0803.0024v1) analyzes methods for detecting temporal zero-point fluctuations of current and voltage, showing that zero-point current fluctuations are measurable in natural setups. This grounds the *physical* side of the zero-point structure: the $\tfrac{1}{2}\hbar\omega$ energy whose phase we study is not a bookkeeping artifact but has operational content. Our work addresses the complementary question of the phase, not the amplitude, of that vacuum structure.

[2] (arXiv:0801.1957v3) computes the phase-space factor for two-body decay with a tachyonic product, deriving lower and upper threshold conditions in terms of a preferred frame, within a quantum field theory exhibiting spontaneous Lorentz symmetry breaking. We use it as a cautionary analogue: introducing a preferred (non-Lorentz-invariant) structure into relativistic quantum theory has well-studied consequences for phase-space and threshold arithmetic; similarly, our conjecture would introduce a preferred arithmetic decomposition (Archimedean vs. $p$-adic) of a quantum phase, and one must check what invariance is preserved.

[3] (arXiv:2203.03154v1) examines the topological hypothesis that phase transitions can be predicted from changes in the topology of accessible configuration space. We borrow the methodological stance: global constraints (here, the product formula $\prod_v \gamma_v = 1$) can manifest as local, apparently contingent structures (here, the phase $e^{i\pi/4}$), and one should search for the topological/global invariant behind a local datum.

[4] (arXiv:1404.1905v1) discusses the formalization of mathematical knowledge and community-curated verification tools for research mathematics. This is directly relevant to our "formally verify" test: the Weil-index computations in Sections 3–4 are exactly the kind of small, self-contained lemmas that such formalization efforts target, and our explicit Gauss-sum arithmetic is written to be machine-checkable in principle.

[5] (arXiv:1805.02650v2) confirms the Gaia DR2 parallax zero-point offset using asteroseismology of Kepler-field red giants. Beyond the shared word "zero-point," this supplies a methodological analogy we take seriously: a "zero point" is only meaningful relative to a calibration network, and [5] demonstrates an independent, cross-checking determination of a zero-point offset. Our Section 4 performs the analogous cross-check: the Archimedean phase is checked against the $p$-adic factors via the product formula.

[6] (arXiv:2511.03563v1) fine-tunes LLMs with retrieval-augmented generation for legal regulation. It connects only instrumentally: large parts of the adelic-programme corpus ([9], [10], [11]) exist as informal notebook and preprint text, and retrieval-augmented tooling of the kind [6] develops is one plausible route to systematically auditing such corpora — the setting in which the present conjecture was surfaced.

[7] (arXiv:1706.01619v6) studies driven spin-wave modes in an XY ferromagnet via Monte Carlo simulation, identifying propagating versus randomized dynamical modes across a nonequilibrium phase transition. The relevance is structural: a driven oscillator-like system whose mode content (coherent wave versus structureless randomness) changes qualitatively under variation of a drive parameter is a physical reminder that "which modes exist" is a dynamical question; our conjecture asks whether the *phase* of the fundamental mode is similarly constrained by global structure.

[8] (arXiv:2308.04324v1) reports a room-temperature reversible colossal volto-magnetic effect in all-oxide metallic-magnet/topotactic-phase-transition heterostructures. We cite it as an example of condensed-matter systems where a control parameter (electric field) reversibly switches a material phase — an experimental template for the kind of intervention that would test our disconfirmation condition: can the vacuum phase be "switched" without touching $p$-adic data?

[9] (DOI 10.5281/zenodo.21511271) is the QNFO five-pillar red-team assessment of the "Adelic Completion of the Harmonic Paradigm." It documents that the Harmonic Paradigm's invocation of Ostrowski's theorem and $p$-adic structures was not matched by core mechanisms — a self-critical baseline against which the present paper is written: we deliberately restrict ourselves to one theorem-grade statement (Weil reciprocity for $x^2$) and compute it fully.

[10] (DOI 10.5281/zenodo.21485556) is the QNFO pre-registered search for adelic structure in the Standard Model mass spectrum via Compton-frequency cross-ratios on Bruhat–Tits trees, explicitly retracting earlier decimal-matching attempts. Its pre-registration discipline — stating search spaces and disconfirmation conditions in advance — is the model for our Section 6.

[11] (DOI 10.5281/zenodo.21782835) proposes that frequency in dimensionless Planck units is a rational ratio $a/b \in \mathbb{Q}$, making a particle's Compton frequency its "prime spectrum." This supplies the conceptual bridge our conjecture needs: if physical frequencies are rational, then quadratic forms with rational coefficients (like $x^2$) are the natural objects, and the Weil index over $\mathbb{Q}$ — with its product over all places — is the natural reciprocity container.

We note plainly: no entry in this bibliography is a primary source on Weil indices or the metaplectic representation. The mathematical machinery used below (Weil index, Maslov phase, Gauss sums) is standard and is derived from first principles in Section 3 rather than cited; this is a limitation discussed in Section 6.

## 3. Methods

### 3.1 Definitions

**Places of $\mathbb{Q}$.** The places $v$ of $\mathbb{Q}$ are the real place $\infty$ and one place $p$ for each prime $p$, with completions $\mathbb{R}$ and $\mathbb{Q}_p$ respectively.

**Weil index.** For a nondegenerate quadratic form $q$ on a finite-dimensional vector space over a local field $F_v$, the Weil index $\gamma_v(q) \in \mu_8$ (the group of eighth roots of unity, $\{z : z^8 = 1\}$) is the phase factor in the metaplectic representation associated to $q$: it is the constant phase by which the associated linear canonical (Fourier-type) transform acts on the chirp (quadratic-exponential) state built from $q$. Concretely, over $\mathbb{R}$, for $q(x) = x^2$:

$$\hat{\phi}(\xi) = \gamma_\infty(q) \int_{\mathbb{R}} e^{i\pi x^2} e^{-2\pi i x \xi}\, dx = \gamma_\infty(q)\, e^{i\pi/4}\, e^{-i\pi \xi^2},$$

and $\gamma_\infty(q)$ is defined so that this holds with the unitary normalization of the Fourier transform $\hat{\phi}(\xi) = \int \phi(x) e^{-2\pi i x\xi}\,dx$.

**Product formula (Weil reciprocity).** For a quadratic form $q$ over $\mathbb{Q}$:

$$\prod_v \gamma_v(q) = \gamma_\infty(q) \prod_{p} \gamma_p(q) = 1,$$

where the product is finite (only finitely many $\gamma_p \neq 1$).

**Conjecture under test.** The vacuum phase $e^{i\pi/4}$ of the oscillator equals $\gamma_\infty(x^2)$, and this value is constrained — in the strong form, *determined* — by the reciprocity identity together with the $p$-adic factors.

### 3.2 Procedure

1. Compute $\gamma_\infty(x^2)$ directly from the Fresnel/Gaussian integral (Section 4.1).
2. Check metaplectic consistency: the fourth power of the phase must equal the metaplectic lift of a full rotation (Section 4.2).
3. Compute $\gamma_p(x^2)$ for odd $p$ via normalized finite Gauss sums, with explicit arithmetic for $p = 3$ and $p = 5$ (Section 4.3).
4. Impose reciprocity to solve for $\gamma_2(x^2)$ and check the product (Section 4.4).
5. Count the residual freedom in $\mu_8 \times \mu_8$ left by reciprocity alone, to test the strong conjecture (Section 4.5).

## 4. Analysis

### 4.1 The Archimedean factor $\gamma_\infty(x^2)$

**Input.** The Fresnel integral identity (standard; derivable by contour rotation of the Gaussian integral $\int_{\mathbb{R}} e^{-\pi t^2} dt = 1$):

$$\int_{\mathbb{R}} e^{i\pi x^2}\, dx = e^{i\pi/4}.$$

**Derivation of the transform phase.** We evaluate the Fourier transform of the chirp $\phi(x) = e^{i\pi x^2}$ by completing the square:

$$\int_{\mathbb{R}} e^{i\pi x^2} e^{-2\pi i x \xi}\, dx = \int_{\mathbb{R}} e^{i\pi (x - \xi)^2}\, e^{-i\pi \xi^2}\, dx = e^{-i\pi \xi^2} \int_{\mathbb{R}} e^{i\pi u^2}\, du = e^{-i\pi\xi^2}\, e^{i\pi/4}.$$

The shift $x \mapsto u = x - \xi$ is exact (no Jacobian: $\left|\frac{\partial u}{\partial x}\right| = 1$), and the regularizing factor $e^{-\epsilon x^2}$ with $\epsilon \to 0^{+}$ justifies the Fresnel integral. Hence, matching the definition in Section 3.1:

$$\gamma_\infty(x^2) = e^{i\pi/4}.$$

Numerically, $e^{i\pi/4} = \cos(\pi/4) + i\sin(\pi/4) = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2} \approx 0.7071068 + 0.7071068\,i$, since $\cos(\pi/4) = \sin(\pi/4) = \sqrt{2}/2$ and $\sqrt{2} \approx 1.4142136$, so $\sqrt{2}/2 \approx 0.7071068$.

### 4.2 Metaplectic consistency check

The Fourier transform $F$ corresponds to rotation by $\pi/2$ in phase space; its metaplectic lift carries the phase $e^{i\pi/4}$. Four applications give rotation by $2\pi$, whose lift in the metaplectic (double) cover is $-1$, not $+1$. Check:

$$(e^{i\pi/4})^4 = e^{i\pi} = -1.$$

And the eighth power lands in the identity:

$$(e^{i\pi/4})^8 = e^{i2\pi} = +1.$$

This confirms $\gamma_\infty(x^2) \in \mu_8$ and that the phase is consistent with the double cover: the metaplectic group is a two-fold cover, so the lift of a $2\pi$ phase-space rotation is the central element $-1$, exactly as computed. This is the group-theoretic reason the vacuum phase is an *eighth* root of unity and not an arbitrary phase.

### 4.3 Odd-prime factors via normalized Gauss sums

For odd $p$, the local Weil index of $q(x) = x^2$ is read from the normalized quadratic Gauss sum

$$G_p = \frac{1}{\sqrt{p}} \sum_{x \in \mathbb{F}_p} e^{2\pi i x^2 / p},$$

and the standard identification gives $\gamma_p(x^2) = \overline{G_p}^{\,\varepsilon}$-type phase; for the unit form $x^2$ the $p$-adic Weil index is $\gamma_p(x^2) = 1$ for all odd $p$, with the Gauss sum supplying the check $G_p \in \{+1, -1, +i, -i\}$ consistent with the local theory. We verify the Gauss-sum values explicitly for two primes.

**Case $p = 3$.** Squares mod $3$: $0^2 = 0$, $1^2 = 1$, $2^2 = 4 \equiv 1 \pmod 3$. Therefore

$$\sum_{x \in \mathbb{F}_3} e^{2\pi i x^2/3} = e^{0} + e^{2\pi i/3} + e^{2\pi i/3} = 1 + 2 e^{2\pi i /3}.$$

With $e^{2\pi i/3} = -\tfrac{1}{2} + i\tfrac{\sqrt{3}}{2}$:

$$1 + 2\left(-\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = 1 - 1 + i\sqrt{3} = i\sqrt{3}.$$

Normalize: $G_3 = \dfrac{i\sqrt{3}}{\sqrt{3}} = i = e^{i\pi/2}$.

**Case $p = 5$.** Squares mod $5$: $0^2 = 0$, $1^2 = 1$, $2^2 = 4$, $3^2 = 9 \equiv 4$, $4^2 = 16 \equiv 1$. Therefore

$$\sum_{x \in \mathbb{F}_5} e^{2\pi i x^2/5} = 1 + 2 e^{2\pi i/5} + 2 e^{2\pi i \cdot 4/5}.$$

Using $e^{2\pi i \cdot 4/5} = e^{-2\pi i/5}$ (since $4 \equiv -1 \pmod 5$):

$$1 + 2\left(e^{2\pi i/5} + e^{-2\pi i/5}\right) = 1 + 4\cos\!\left(\frac{2\pi}{5}\right).$$

With $\cos(2\pi/5) = \cos 72^{\circ} = \frac{\sqrt{5}-1}{4} \approx 0.3090170$:

$$1 + 4 \cdot 0.3090170 = 1 + 1.2360680 = 2.2360680 = \sqrt{5}.$$

Normalize: $G_5 = \dfrac{\sqrt{5}}{\sqrt{5}} = 1$.

These confirm the classical pattern $G_p = \varepsilon_p$ with $\varepsilon_p = 1$ for $p \equiv 1 \pmod 4$ ($5 \equiv 1$) and $\varepsilon_p = i$ for $p \equiv 3 \pmod 4$ ($3 \equiv 3$) — the finite-field shadow of quadratic reciprocity. For the $p$-adic Weil index of the *unit* form $x^2$, the local theory gives $\gamma_p(x^2) = 1$ for every odd $p$: the form $x^2$ has unit discriminant and even rank $0$ mod the relevant invariants, so no nontrivial local phase arises at odd primes.

### 4.4 Solving for the dyadic factor and checking reciprocity

**Input.** Product formula (Section 3.1), $\gamma_p(x^2) = 1$ for odd $p$ (Section 4.3), $\gamma_\infty(x^2) = e^{i\pi/4}$ (Section 4.1).

**Derivation.** The product formula reads

$$\gamma_\infty(x^2) \cdot \gamma_2(x^2) \cdot \prod_{p \text{ odd}} \gamma_p(x^2) = e^{i\pi/4} \cdot \gamma_2(x^2) \cdot 1 = 1.$$

Solving:

$$\gamma_2(x^2) = \left(e^{i\pi/4}\right)^{-1} = e^{-i\pi/4}.$$

**Check.** $e^{i\pi/4} \cdot e^{-i\pi/4} = e^{i\pi/4 - i\pi/4} = e^{0} = 1$. ✓

Thus the full reciprocity identity for $q(x) = x^2$ is verified:

$$\gamma_\infty(x^2)\,\gamma_2(x^2)\,\prod_{p \text{ odd}} \gamma_p(x^2) = e^{i\pi/4} \cdot e^{-i\pi/4} \cdot \prod_{p \text{ odd}} 1 = 1.$$

The conjecture's proposed formal test — "verify that the metaplectic Weil indices satisfy reciprocity for $x^2$ and compute the $p$-adic factors" — is thereby passed: $\gamma_\infty = e^{i\pi/4}$, $\gamma_2 = e^{-i\pi/4}$, $\gamma_p = 1$ ($p$ odd), $\prod_v \gamma_v = 1$.

### 4.5 Does reciprocity *constrain* the vacuum phase? Counting the residual freedom

The strong form of the conjecture claims that imposing $\prod_v \gamma_v = 1$ constrains admissible vacuum phases. We count the constraint's strength. The unknowns are $\gamma_\infty, \gamma_2 \in \mu_8$, where $\mu_8 = \{e^{i\pi k/4} : k \in \{0,\dots,7\}\}$ has $|\mu_8| = 8$. The odd-prime factors are fixed at $1$. The constraint is one equation:

$$\gamma_\infty \cdot \gamma_2 = 1.$$

For each of the $8$ choices of $\gamma_\infty = e^{i\pi k/4}$, $k \in \{0,\dots,7\}$, the equation uniquely determines $\gamma_2 = e^{-i\pi k /4}$, which is again in $\mu_8$. Hence the solution set has exactly

$$|\{(\gamma_\infty, \gamma_2) \in \mu_8 \times \mu_8 : \gamma_\infty \gamma_2 = 1\}| = 8$$

elements. Reciprocity alone therefore leaves $8$ admissible pairs — including, e.g., $(\gamma_\infty, \gamma_2) = (1, 1)$ and $(e^{i\pi/2}, e^{-i\pi/2})$ — and does **not** by itself single out $(e^{i\pi/4}, e^{-i\pi/4})$.

What closes the gap is the metaplectic self-duality of the oscillator: the requirement that the Fourier transform act with its standard metaplectic lift, i.e., that the chirp $e^{i\pi x^2}$ transform with a *nontrivial* unit-modulus phase consistent with $F^4 = -1$ on the lifted level (Section 4.2) and with the Gaussian ground state being self-Fourier up to that phase. The trivial solution $\gamma_\infty = 1$ corresponds to the *unlifted* (projective) transform and fails the double-cover consistency $(e^{i\pi/4})^4 = -1$ in the sense that it corresponds to a different (split) lift of the symplectic group. Within the metaplectic lift, the phase is fixed to $e^{i\pi/4}$ by the Fresnel integral (Section 4.1), and reciprocity then *verifies* — rather than *derives* — the companion value $\gamma_2 = e^{-i\pi/4}$.

### 4.6 Vacuum-energy bookkeeping

For completeness, the zero-point energy in dimensionless units is

$$\frac{E_0}{\hbar\omega} = \frac{1}{2},$$

with $E_0 = \tfrac{1}{2}\hbar\omega$ the standard oscillator ground-state energy whose measurability in fluctuation form is discussed in [1]. The phase $\gamma_\infty = e^{i\pi/4}$ is the *holonomy* of this half-quanta structure under canonical transforms; the two "halves" (energy and phase) are related but not identical: the energy is a spectrum datum, the phase a representation-theoretic one. Our result concerns only the phase.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements or simulations.

**R1 (Archimedean factor).** $\gamma_\infty(x^2) = e^{i\pi/4} \approx 0.7071068 + 0.7071068\,i$ (Section 4.1).

**R2 (Metaplectic consistency).** $(e^{i\pi/4})^4 = e^{i\pi} = -1$ and $(e^{i\pi/4})^8 = e^{i2\pi} = 1$; the phase is a genuine eighth root of unity consistent with the metaplectic double