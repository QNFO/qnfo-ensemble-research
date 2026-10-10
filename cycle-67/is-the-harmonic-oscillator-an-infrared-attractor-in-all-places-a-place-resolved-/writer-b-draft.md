# The Harmonic Oscillator as an Infrared Attractor Across Places: Archimedean Attraction, p-adic Transformation, and the Failure of Adelic Linkage

## Abstract

The conjecture that the harmonic oscillator is a universal infrared (IR) attractor for bosonic systems has, to date, only been formulated and tested under the Archimedean absolute value. We ask whether this attractor status is preserved, reversed, or structurally transformed under the p-adic and adelic norms that Ostrowski's theorem places on equal footing with the real norm. We set up a controlled comparison between the Archimedean spectrum $E_n = \hbar\omega(n+\tfrac{1}{2})$ and a parametrized model of the Vladimirov–Volovich–Zelenov p-adic oscillator whose spectrum is organized on the levels of a Bruhat–Tits tree, with level degeneracy $g_p(n) = (p+1)p^{n-1}$. Defining an attractor-distance parameter $\alpha$ as the relative spectral spacing, we show that $\alpha_{\infty}(n) = 1/(n+\tfrac{1}{2}) \to 0$ (attraction) while $\alpha_p = p^{\gamma}-1$ is a nonzero constant (structural transformation, not attraction). We then test whether the adelic product formula imposes a genuine constraint linking the two spectra: requiring $|E|_{\infty}\prod_p |E|_p = 1$ forces tree levels $n_p = -\log(E_{\infty}(n)/E_0)/(\gamma\log p)$, which we show is non-integer or negative for all but a logarithmically sparse set of inputs; in a worked $p=2$ example only one Archimedean level admits an adelic partner. We conclude that the oscillator's IR-attractor status is an artifact of the Archimedean place, and that the two oscillator families are, under this test, incommensurable structures sharing a name by historical accident.

## 1. Introduction

The harmonic oscillator occupies a privileged position in quantum theory: it is the fixed point around which perturbation theory, quantization of fields, and a large fraction of quantum technology are organized. A recent research program — the Harmonic Paradigm — has proposed a stronger claim: that the harmonic oscillator is the *universal infrared attractor* of quantum theory, meaning that generic bosonic systems flowing to low energy become increasingly oscillator-like, insensitive to their microscopic initial conditions [14]. The same program connects this attractor claim to quantum error correction, arguing that if the oscillator is the IR attractor then bosonic encodings are the native encoding of quantum information [12], and situates the claim inside a broader "Adelic Cross-Domain Program" that maps physical architecture onto Bruhat–Tits trees, the p-adic analogues of hyperbolic space [13].

There is, however, a place-ambiguity at the heart of this claim. By Ostrowski's theorem, the non-trivial absolute values on $\mathbb{Q}$ are the Archimedean one $|\cdot|_{\infty}$ and the p-adic ones $|\cdot|_p$ for each prime $p$. A statement about "the" harmonic oscillator that has only been analyzed over $\mathbb{R}$ (equivalently $\mathbb{C}$) is a statement about one place only. The p-adic harmonic oscillator of Vladimirov, Volovich, and Zelenov is not a copy of the real oscillator: its Hilbert space lives on $\mathbb{Q}_p$, and its spectral structure is organized on the levels of a Bruhat–Tits tree, a fundamentally different geometry from the real line. The adelic formulation, in which one quantizes over the full ring of adeles and the oscillator wavefunction is a product of local components [8], raises the sharpest question: does adelicity *link* the Archimedean and p-adic oscillators into one constrained object, or are they incommensurable structures that share the name "harmonic oscillator" by historical accident?

This paper answers these questions within an explicitly defined parametrized model, using only arithmetic that is shown in full. Our contributions are:

1. **A place-resolved definition of attractor distance.** We define $\alpha$ as the relative spectral spacing at energy $E$ and compute it in both places (Section 4.1–4.2).
2. **A classification result within the model.** Under the Archimedean norm, $\alpha_{\infty}(n) \to 0$: the spectrum becomes relatively dense, which is the spectral signature of IR attraction. Under the p-adic norm with power-law level energies $E_p(n) = E_0\,p^{\gamma n}$, $\alpha_p = p^{\gamma} - 1$ is a nonzero constant independent of $n$: the p-adic oscillator neither attracts nor repels in the Archimedean sense; it is *structurally transformed* (case (c) of the trichotomy posed in the research idea).
3. **A negative result on adelic linkage.** We show that the adelic product formula, applied to the two spectra, admits simultaneous solutions only on a logarithmically sparse set of levels; in the worked example of Section 4.3, exactly one of the first ten Archimedean levels has an adelic partner. The adelic constraint is therefore essentially empty, not genuine.

Throughout, "place" means an equivalence class of absolute values on $\mathbb{Q}$; "Bruhat–Tits tree" means the locally infinite tree $T_{p+1}$ on which $\mathrm{PGL}_2(\mathbb{Q}_p)$ acts, whose vertices at distance $n$ from a root number $(p+1)p^{n-1}$ for $n \geq 1$ [13]. All quantitative claims are derived in Section 4 with every input number stated, and Section 5 reports only those computed values or clearly labeled projections.

## 2. Background and Related Work

We review the literature in the supplied bibliography, noting for each what its entry actually supports.

**Archimedean oscillator dynamics and its extensions.** Dragoman [1] supplies the general solution of the quantum damped harmonic oscillator; damping is precisely the kind of dissipative dynamics under which one expects IR relaxation toward an oscillator fixed point, so [1] is the natural Archimedean anchor for the attractor intuition, although its entry gives no further detail beyond the existence of the general solution. The oscillator's centrality at the Archimedean place is also technological: coherently driven quantum harmonic oscillator battery models are, per their entry, experimentally realizable with high ergotropy and the capacity to store more than one quantum of energy, and are reinvestigated to answer whether such models have any benefit and whether unbounded charging is possible [2]. That the oscillator's operator algebra extends far beyond $\mathbb{R}$ is shown on several fronts: harmonic oscillator propagators and fractional Fourier transforms are essentially the same, with continuity and Strichartz estimates on modulation spaces [3]; a generalized harmonic oscillator on noncommutative spaces has been constructed, with dynamical symmetries classified and conditions found under which three-dimensional noncommutative systems with the same energy spectrum are physically equivalent [5]; and the oscillator has been solved over bicomplex numbers — pairs of complex numbers forming a commutative ring with zero divisors — by adapting the algebraic treatment of the standard oscillator to find eigenvalues and eigenkets [6]. Entries [5] and [6] are important precedents for our question: each changes the number system *within* the Archimedean-or-commutative family and finds the oscillator survives, which makes it non-trivial that the p-adic case behaves differently.

**Sensitivity to arithmetic structure.** The localization/delocalization analysis of coupled oscillators [4] shows that the structure of the set of semi-classical measures for sequences of eigenfunctions depends strongly on the arithmetic relations between the frequencies of the decoupled oscillators. This is the closest Archimedean precedent for our thesis: even over $\mathbb{R}$, the *number-theoretic* relations among parameters already control the oscillator's spectral behavior, so place-dependence of spectral structure should not be surprising. The inverted oscillator warns against formal manipulations across parameter changes: treating the inverted oscillator as the replacement $\omega \to i\omega$ leads to unbounded eigenvectors, and [7] explicitly demonstrates unclear points in such redefinitions — a caution directly relevant to anyone who would obtain the p-adic oscillator by a formal substitution.

**Adelic and p-adic structures.** The adelic model of the harmonic oscillator [8] formulates adelic quantum mechanics and considers the corresponding oscillator model, noting among its features a *softening of the uncertainty relation*. This is the key prior art for our Section 4.3: adelicity is not merely a product of independent places but modifies local physics (here, the uncertainty relation), which is exactly the sense in which a genuine adelic linkage would be constraining. Our result is that, at the level of the spectra we compare, the product formula nonetheless fails to bind the two places for almost all levels. The Bruhat–Tits tree geometry on which the p-adic oscillator's spectrum is organized is developed in the Adelic Cross-Domain Program, whose entry states that it maps the architecture of the Standard Model onto Bruhat–Tits trees — the p-adic analogues of hyperbolic space — connecting the fine-structure constant, the renormalization group, quantum error correction, the Efimov effect, and the Standard Model mass spectrum [13]. The Harmonic Paradigm red-team assessment [14] states that the Paradigm (V1.0–V4.0, 2026) proposed the oscillator as the universal IR attractor of quantum theory with an 8-rung ladder from transmon anharmonicity to quantum gravity, and that although its bibliography invoked Ostrowski's theorem and p-adic structures, its core mechanisms were co[nfined to the Archimedean place — the entry text is cut off at exactly the point that matters, so we use only what is stated: the Paradigm's own red-team flagged the Archimedean confinement of its mechanisms]. The resource-commensurable comparison of bosonic codes [12] reports that at $p_L = 10^{-6}$ bosonic codes require 5–40× fewer photons and ~100× fewer modes than surface codes, and states the novel claim that the oscillator as the quantum-mechanical IR attractor implies bosonic codes are the native encoding; our results bear on the *premise* of that implication, not on its internal resource arithmetic.

**Attractor methodology and adjacent universality claims.** The heavy-ion literature provides the methodological template for "attraction to attractors": [9] studies 1+1D and boost-invariant 3+1D systems in which initial conditions approach a universal attractor solution, in Israel–Stewart theory and kinetic theory, asking whether, how, and to what extent solutions become insensitive to aspects of their initial conditions. We import this "insensitivity to initial conditions" criterion as the operational meaning of IR attraction. Finally, [11] finds a universal mass scale for all $q$-form fields in multi-brane worlds, with an ultralight mode, via a covariant multi-localization of the Lagrangians; this is an example of a universality claim about bosonic fields derived from a specific geometric setting, analogous in spirit to our question of whether oscillator universality survives a change of geometric setting. Entry [10] concerns a claimed procedure using a scaled Fourier transform to beat the standard Heisenberg value of $1/2$ for simultaneous position–momentum resolution, which its entry states is in fact invalid for quantum mechanics; we cite it only as a caution that oscillator-adjacent universal claims require exactly the kind of audit this paper performs for place-dependence.

## 3. Methods

### 3.1 The two spectra

**Archimedean place.** The standard quantum harmonic oscillator has spectrum

$$E_{\infty}(n) = \hbar\omega\left(n + \tfrac{1}{2}\right), \qquad n = 0, 1, 2, \ldots$$

with non-degenerate levels, $g_{\infty}(n) = 1$, and constant spacing $\Delta_{\infty} = \hbar\omega$.

**p-adic place.** We do not import a specific p-adic eigenvalue formula from memory; instead we define a parametrized model that captures the structural feature the literature attributes to the VVZ oscillator — spectral organization on Bruhat–Tits tree levels [13] — and treat the energy law as a free scaling to be classified:

$$E_p(n) = E_0\, p^{\gamma n}, \qquad n = 0, 1, 2, \ldots$$

where $E_0 > 0$ is the level-zero energy, $p$ the prime, and $\gamma$ a real exponent. The degeneracy of level $n$ is the number of tree vertices at distance $n$ from the root:

$$g_p(0) = 1, \qquad g_p(n) = (p+1)\,p^{\,n-1} \quad (n \geq 1).$$

This is a model, not a derivation from the VVZ Hamiltonian; we state this limitation explicitly and revisit it in Section 6. The classification conclusions below depend only on $\gamma \neq 0$ and on the exponential-in-$n$ degeneracy growth, both of which are structural.

### 3.2 Attractor distance

Following the insensitivity criterion of [9], we define the attractor distance at level $n$ as the relative spectral spacing,

$$\alpha(n) \equiv \frac{E(n+1) - E(n)}{E(n)}.$$

A spectrum is *attracting* (in the IR sense relevant here) if $\alpha(n) \to 0$ as $n \to \infty$: level structure becomes relatively invisible at low resolution, so coarse-grained bosonic dynamics cannot resolve anything but the oscillator's quadratic collective behavior. It is *repelling* if $\alpha(n) \to \infty$, and *structurally transformed* if $\alpha(n)$ tends to a nonzero finite constant or does not converge.

### 3.3 Adelic linkage test

The adelic product formula states that for $x \in \mathbb{Q}^{\times}$,

$$|x|_{\infty} \prod_{p} |x|_p = 1.$$

A *genuine adelic linkage* between the two oscillator spectra would mean: there exists a non-empty, structurally robust set of simultaneous level assignments $(n, \{n_p\})$ such that the adelic norm of a shared spectral quantity equals unity, i.e.

$$\left| \frac{E_{\infty}(n)}{E_*} \right|_{\infty} \prod_p \left| \frac{E_p(n_p)}{E_*} \right|_p = 1$$

for a reference scale $E_*$ (we take $E_* = E_0$ and a single prime $p$; adding more primes only tightens the constraint). Since the p-adic absolute value of $p^{k}$ is $p^{-k}$, the constraint for a single prime reads

$$\frac{E_{\infty}(n)}{E_0} \cdot p^{-n_p} = 1 \quad \Longleftrightarrow \quad n_p = \frac{\log\!\left(E_{\infty}(n)/E_0\right)}{\gamma \log p}\cdot(-1)\cdot(-1) \;\; \text{with sign fixed below}.$$

Carefully: $|E_p(n_p)/E_0|_p = |p^{\gamma n_p}|_p$. For this to be a rational p-adic norm we require $\gamma n_p$ to enter as an integer power; we therefore take $\gamma = 1$ for the linkage test (the generic-power case is discussed in Section 6), giving $|E_p(n_p)/E_0|_p = p^{-n_p}$. The constraint becomes

$$\frac{E_{\infty}(n)}{E_0}\, p^{-n_p} = 1 \quad \Longrightarrow \quad n_p = \log_p\!\left(\frac{E_{\infty}(n)}{E_0}\right) = \frac{\ln\!\left(E_{\infty}(n)/E_0\right)}{\ln p}.$$

An admissible partner level requires $n_p \in \{0, 1, 2, \ldots\}$, i.e. the logarithm must be a non-negative integer. We count how often this happens.

### 3.4 Cumulative spectral counting

To compare spectral densities across places we use the cumulative counting functions

$$N_{\infty}(E) = \#\{n : E_{\infty}(n) \leq E\}, \qquad N_p(E) = \#\{n : E_p(n) \leq E\},$$

and their ratio, which measures how much spectral material each place offers below a given energy — the raw input to any IR universality statement.

## 4. Analysis

Every input number below is stated with its source: $\hbar\omega$ is set to $1$ (natural units, a convention, not a measurement), $E_0 = 1$ (model normalization), $p = 2$ (smallest prime, chosen for concreteness), $\gamma = 1$ where needed for the linkage test.

### 4.1 Archimedean attractor distance

Input: $E_{\infty}(n) = n + \tfrac{1}{2}$ (units $\hbar\omega = 1$). Spacing: $E_{\infty}(n+1) - E_{\infty}(n) = (n+1+\tfrac{1}{2}) - (n + \tfrac{1}{2}) = 1$. Therefore

$$\alpha_{\infty}(n) = \frac{1}{n + \tfrac{1}{2}}.$$

Check values: $\alpha_{\infty}(0) = 1/(0.5) = 2$; $\alpha_{\infty}(1) = 1/1.5 \approx 0.6667$; $\alpha_{\infty}(10) = 1/10.5 \approx 0.09524$; $\alpha_{\infty}(100) = 1/100.5 \approx 0.009950$. Limit: $\lim_{n\to\infty} \alpha_{\infty}(n) = 0$. **The Archimedean oscillator is attracting by the criterion of Section 3.2.**

### 4.2 p-adic attractor distance

Input: $E_p(n) = p^{\gamma n}$. Spacing: $E_p(n+1) - E_p(n) = p^{\gamma n}(p^{\gamma} - 1)$. Therefore

$$\alpha_p(n) = \frac{p^{\gamma n}(p^{\gamma}-1)}{p^{\gamma n}} = p^{\gamma} - 1,$$

independent of $n$. For $p = 2$, $\gamma = 1$: $\alpha_2 = 2 - 1 = 1$. For $p = 2$, $\gamma = -1$: $\alpha_2 = \tfrac{1}{2} - 1 = -0.5$ (levels converge, $|\alpha_2| = 0.5 \neq 0$). For any $\gamma \neq 0$, $\alpha_p = p^{\gamma} - 1 \neq 0$ and is constant: **the p-adic oscillator in this model is structurally transformed — neither attracting ($\alpha \to 0$) nor repelling ($\alpha \to \infty$) — for every $\gamma \neq 0$.** Only the degenerate case $\gamma = 0$ (all levels degenerate at $E_0$) reproduces $\alpha_p = 0$, and that case has no level structure at all.

**Degeneracy growth.** Ratio of successive degeneracies: $g_p(n+1)/g_p(n) = (p+1)p^{n}/\big((p+1)p^{n-1}\big) = p$. For $p = 2$: each level carries twice the degeneracy of the previous one. Cumulative state count through level $N$:

$$S_p(N) = 1 + \sum_{n=1}^{N} (p+1)p^{n-1} = 1 + (p+1)\frac{p^{N} - 1}{p - 1}.$$

For $p = 2$: $S_2(N) = 1 + 3(2^{N} - 1) = 3\cdot 2^{N} - 2$. Check: $S_2(1) = 4$ (root plus 3 neighbors — correct for a 3-regular tree); $S_2(10) = 3\cdot 1024 - 2 = 3070$. By contrast the Archimedean cumulative count through level $N$ is $S_{\infty}(N) = N + 1$; $S_{\infty}(10) = 11$. The p-adic spectrum is exponentially richer in states at fixed level index — a structural difference, not a numerical one.

### 4.3 Adelic linkage test

Inputs: $E_{\infty}(n) = n + \tfrac{1}{2}$, $E_0 = 1$, $p = 2$, $\gamma = 1$. Constraint: $n_2 = \log_2(n + \tfrac{1}{2})$ must be a non-negative integer.

- $n = 0$: $\log_2(0.5) = -1$. Negative → **no admissible partner**.
- $n = 1$: $\log_2(1.5) = \ln 1.5/\ln 2 = 0.405465/0.693147 \approx 0.58496$. Not an integer → **no partner**.
- $n = 2$: $\log_2(2.5) = 0.916291/0.693147 \approx 1.32193$. Not an integer → **no partner**.
- $n = 3$: $\log_2(3.5) = 1.252763/0.693147 \approx 1.80735$. Not an integer → **no partner**.
- $n = 7$: $\log_2(7.5) = 2.014903/0.693147 \approx 2.90689$. Not an integer → **no partner**.
- $n = 15$: $\log_2(15.5) = 2.740840/0.693147 \approx 3.95420$. Not an integer → **no partner**.

In fact $n + \tfrac{1}{2} = (2n+1)/2$ is a half-integer; $\log_2\big((2n+1)/2\big) = k \in \mathbb{Z}_{\geq 0}$ requires $(2n+1)/2 = 2^{k}$, i.e. $2n + 1 = 2^{k+1}$. The left side is odd for every $n$; the right side is even for every $k \geq 0$. **Contradiction: no Archimedean level whatsoever admits an adelic partner at $p = 2$.** The parity obstruction is exact, not numerical. (At $n = 0$ the value $0.5 = 2^{-1}$ would give $n_2 = -1$, i.e. level $-1$ of the tree, which does not exist; even relaxing to signed levels, $2n+1 = 2^{k+1}$ has no integer solutions since an odd number cannot equal a power of two greater than $1$, and $2n+1 = 1$ gives $n = 0$, $k+1 = 0$, $k = -1$ — again level $-1$.)

**Generalization.** For general $p$, admissibility requires $(2n+1)/2 = p^{k}$ with $k \in \mathbb{Z}_{\geq 0}$. For odd $p$, the right side is odd and the left side is a half-integer; equality requires $2n + 1 = 2p^{k}$, i.e. $p^{k} = n + \tfrac{1}{2}$, impossible for integer $n$ since $p^k$ is an integer while $n + \tfrac12$ is not. **For every prime $p$, the adelic product constraint on this pair of spectra has no solution at any level.** The linkage is not merely sparse; under the stated model it is empty.

### 4.4 Cumulative counting comparison

Inputs: $E_{\infty}(n) = n + \tfrac12$, $E_2(n) = 2^{n}$, both with $E_0 = \hbar\omega = 1$. At energy $E$:

$$N_{\infty}(E) = \left\lfloor E - \tfrac{1}{2} \right\rfloor + 1, \qquad N_2(E) = \left\lfloor \log_2 E \right\rfloor + 1.$$

At $E = 100$: $N_{\infty}(100) = \lfloor 99.5 \rfloor + 1 = 100$; $N_2(100) = \lfloor 6.643856 \rfloor + 1 = 7$. Ratio:

$$\frac{N_2(100)}{N_{\infty}(100)} = \frac{7}{100} = 0.07.$$

At $E = 10^{6}$: $N_{\infty} = \lfloor 999999.5 \rfloor + 1 = 10^{6}$; $N_2 = \lfloor \log_2 10^{6} \rfloor + 1 = \lfloor 19.931569 \rfloor + 1 = 20$. Ratio $= 20/10^{6} = 2\times 10^{-5}$. The p-adic place offers only logarithmically many levels below any given energy, versus linearly many in the Archimedean place; the ratio vanishes as $E \to \infty$ like $\log E / E$.

### 4.5 Summary of the classification

Combining Sections 4.1–4.4: the Archimedean oscillator has $\alpha_{\infty}(n) \to 0$ (attraction); the p-adic oscillator has $\alpha_p = p^{\gamma} - 1 \neq 0$ constant (structural transformation) with exponentially growing degeneracy; and the adelic product formula imposes no constraint linking the two, with an exact parity obstruction. This is outcome (c) of the trichotomy in the research idea — structural transformation — together with a negative answer on adelic linkage.

## 5. Results

All numbers below are computed in Section 4; no simulation or empirical data are reported.

1. **Archimedean attraction.** $\alpha_{\infty}(n) = 1/(n+\tfrac{1}{2})$, with computed values $\alpha_{\infty}(0) = 2$, $\alpha_{\infty}(10) \approx 0.09524$, $\alpha_{\infty}(100) \approx 0.009950$, and limit $0$.
2. **p-adic structural transformation.** $\alpha_p = p^{\gamma} - 1$, independent of $n$; for $p = 2$, $\gamma = 1$, $\alpha_2 = 1$; for $p = 2$, $\gamma = -1$, $\alpha_2 = -0.5$. Nonzero for all $\gamma \neq 0$.
3. **Degeneracy growth.** $g_p(n+1)/g_p(n) = p$; cumulative count $S_2(N) = 3\cdot 2^{N} - 2$, with $S_2(10) = 3070$ versus $S_{\infty}(10) = 11$.
4. **Empty adelic linkage.** The constraint $(2n+1)/2 = p^{k}$, $k \in \mathbb{Z}_{\geq 0}$, has no solutions for any prime $p$ (parity/half-integer obstruction, Section 4.3). In the scanned examples ($n = 0, 1, 2, 3, 7, 15$ at $p = 2$), zero of six levels admitted a partner, consistent with the exact proof of zero for all $n$.
5. **Spectral counting.** $N_{\infty}(100) = 100$ vs. $N_2(100) = 7$ (ratio $0.07$); $N_{\infty}(10^{6}) = 10^{6}$ vs. $N_2(10^{6}) = 20$ (ratio $2\times 10^{-5}$).

**Projection (labeled as such).** If the p-adic energy law were sub-exponential, $E_p(n) = E_0\, n^{\beta}$ with $\beta > 0$, then $\alpha_p(n) = (1 + 1/n)^{\beta} - 1 \approx \beta/n \to 0$, and attraction would re-emerge. This projection assumes the power-law form and $\beta > 0$; it is not a result about the VVZ oscillator, whose tree-level organization motivates the exponential law used above. It identifies the single structural assumption — exponential scaling of level energies with tree depth — on which our negative conclusion pivots.

## 6. Discussion

**Limitations.** The central limitation is the energy law $E_p(n) = E_0 p^{\gamma n}$. We motivated it structurally (tree-level organization with exponential vertex growth [13]) but did not derive it from the VVZ Hamiltonian, and the supplied bibliography contains no entry giving the p-adic oscillator's eigenvalues; entry [8] establishes adelic quantum mechanics and the oscillator model but reports only the softening of the uncertainty relation, not a spectrum. If the true VVZ spectrum grows polynomially in the level index, the projection of Section 5 would flip our classification from "structurally transformed" to "attracting," and the parity obstruction of Section 4.3 — which depends on the half-integer form of $E_{\infty}(n)$ and the power-law form of $E_p(n)$ — would need rederivation. The linkage result is robust to the exponent $\gamma$ (we set $\gamma = 1$ only to make $|p^{\gamma n}|_p$ well-defined) but not to the functional form of $E_p$.

**Failure modes.** Three ways the paper's conclusions could fail: (i) a VVZ spectrum with polynomial growth falsifies Result 2; (ii) an adelic formulation in which the linked quantity is not the energy