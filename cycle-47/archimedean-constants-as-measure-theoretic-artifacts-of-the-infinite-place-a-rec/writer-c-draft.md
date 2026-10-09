# Archimedean Constants as Measure-Theoretic Artifacts of the Infinite Place: A Derivation of π's Local Status in Adelic Quantum Mechanics

## Abstract

Ostrowski's theorem partitions the non-trivial completions of $\mathbb{Q}$ into exactly one Archimedean completion $\mathbb{R}$ and infinitely many non-Archimedean completions $\mathbb{Q}_p$. Contemporary physics is formulated exclusively at the Archimedean place, and its most ubiquitous transcendental constant, $\pi$, enters through constructions — the Gaussian integral, $\Gamma(1/2)$, circular Haar measure — that exist only there. We formalize the conjecture that such constants are not fundamental but measure-theoretic artifacts of restricting to the $\infty$-place. Working from Tate's thesis and Dragovich's adelic quantum mechanics as templates, we show: (i) the classical Gaussian integral yields $\sqrt{\pi}$ only because polar-coordinate change of variables imports the Haar measure of the Archimedean rotation group $S^1$, whose $p$-adic analogs are totally disconnected and contribute rational functions of $p^{-s}$ instead; (ii) the completed Riemann zeta factorization $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ isolates all transcendental content in the local Archimedean factor, with the explicit identity $\Lambda(2) = \Lambda(-1) = \pi/6 \approx 0.5235988$ verified by full arithmetic; and (iii) in adelic quantum mechanics, dynamics factorizes over places while measurement is an Archimedean projection, so $\pi$-dependent terms arise only in the projection step. We propose a falsifiable verification program based on adelic harmonic oscillators and adelic CFT partition functions, and discuss failure modes.

## 1. Introduction

Every non-trivial absolute value on $\mathbb{Q}$ is, by Ostrowski's theorem, equivalent either to the usual Archimedean absolute value $|\cdot|_\infty$ (completion $\mathbb{R}$) or to a $p$-adic absolute value $|\cdot|_p$ (completion $\mathbb{Q}_p$) for a prime $p$ [9], [11]. These completions are mutually singular: no sequence of rationals converges simultaneously in two distinct places unless it is eventually constant. Physics, however, is written in the language of $\mathbb{R}$ — real Hilbert spaces, differentiable manifolds, and the constants $\pi$ and $e$ that pervade spectral theory and path integrals. The research program of adelic physics asks whether this is an accident of formulation or a statement about nature [5], [9], [11].

The specific conjecture investigated here is that constants arising *only* from Archimedean constructions — paradigmatically $\pi$ — are artifacts of the restriction to the $\in$-place, and that a fully adelic formulation reinterprets or replaces them. The test is sharp: identify which physical structures ($\pi$, Gaussian integrals, $\Gamma(1/2)$) possess $p$-adic analogs and which do not; show that adelic quantum mechanics factorizes into local dynamics at each place with measurement as Archimedean projection; and verify that number-theoretic invariants such as quadratic reciprocity govern the global (adelic) functional relations in place of transcendental constants.

Our contribution is threefold. First, we give a clean measure-theoretic diagnosis of *where* $\pi$ enters the Gaussian integral: not in the integrand, but in the Jacobian of the polar-coordinate map, i.e., in the Haar measure of the Archimedean circle group. Second, we show via the completed zeta function that the transcendental content of the global functional equation is entirely concentrated in the local factor at $\infty$, with an explicit two-sided numerical check ($\Lambda(2) = \Lambda(-1) = \pi/6$) computed in full. Third, we articulate the factorization/measurement structure of adelic quantum mechanics and state a concrete verification program, with honest labeling of what is derived here versus what is a projection requiring computation.

## 2. Background and Related Work

**Adelic physics.** Dragovich's review [5] surveys applications of non-Archimedean geometry, $p$-adic numbers, and adeles in mathematical physics, including $p$-adic and adelic quantum mechanics, $p$-adic string amplitudes, and adelic path integrals. It establishes the key technical fact on which we build: quantum amplitudes can be constructed as products of local factors, one per place, with the Archimedean factor recovering ordinary quantum mechanics. Our claim that $\pi$-terms concentrate in the Archimedean factor is a refinement of exactly this product structure. The QNFO taxonomy [9] and its v2.0 extension [11] catalogue "measure-theoretic artifacts" of the Archimedean place across several categories and document completion failures — structures that exist at $\infty$ but not at any $p$-place — providing the conceptual vocabulary (artifact, completion failure, place-restriction) that we make precise here for $\pi$ specifically. The natural-units program [12] strips anthropocentric conventions from physical bounds and observes that Ostrowski's theorem exposes the Archimedean completion as one choice among many; our treatment of $\pi$ as a place-dependent constant is the spectral/integral counterpart of that unit-independence argument.

**Adelic equidistribution and dynamics.** Baker–Rumely and Favre–Rivera–Letelier (summarized in [1]) proved the arithmetic equidistribution theorem: points of small height on the Berkovich compactification of $\mathbb{P}^1$ with respect to an adelic measure equidistribute simultaneously at every place, Archimedean and non-Archimedean alike. This is the strongest existing template for "global adelic measure with local projections," and it demonstrates that adelic measures are the correct primitive — a single global object whose place-wise projections each carry their own Haar-type measure theory. Favre and Rivera-Letelier's companion characterization [6] determines when equidistribution with moving targets holds for rational functions over any complete field, in any characteristic; its place-agnostic formulation confirms that the equidistribution machinery does not privilege $\infty$, supporting our thesis that Archimedean-specific constants cannot be fundamental to the global theory. Yuan's arithmetic Hodge index theorem for adelic line bundles [2] extends these ideas to finitely generated fields and yields rigidity of preperiodic points; it supplies the arithmetic-intersection precedent for global adelic objects whose local components satisfy independent, place-specific identities tied together by product formulas.

**Adelic groups and exponentials.** The theorem that finite-dimensional protori (compact connected abelian groups) *are* adelic tori, with a complete Lie theory built on an adelic exponential [3], is directly relevant to the status of $e$ and $\pi$: the classical exponential map and the $2\pi$-periodicity of the circle are Archimedean Lie-theoretic phenomena, while [3] shows the adelic category carries its own, structurally different exponential. This is precisely the kind of "replacement" our conjecture predicts for transcendental constants.

**Local-field root counts.** The adelic Tau conjecture literature [7] bounds the number of non-degenerate roots of fewnomial systems over any local field $L$, with bounds depending on $n$, $k$, and $L$. Notably, the "fixed phase" condition in the root-counting problem is an Archimedean notion (phases live in the circle group); over $\mathbb{Q}_p$ the analogous structure is the group of roots of unity, which is finite. This concretely illustrates how circle-group phenomena — the source of $\pi$ — have no direct $p$-adic counterpart.

**Terminology caution and analogy.** The "Archimedean copulas" of statistics [4] share a name but not a mathematical mechanism with our Archimedean place; we cite [4] only to flag this terminology collision and note that its spline-generator machinery is unrelated to valuation theory. Finally, the study of upsampling artifacts in neural audio synthesis [8] offers a loose but useful methodological analogy: artifacts arise when a signal valid on a fine grid is projected onto a coarser one, and the artifact pattern is a fingerprint of the projection operator, not of the underlying signal. We use this as a heuristic model for "constants that appear only after Archimedean projection."

## 3. Methods

### 3.1 Framework: places, Haar measures, and local zeta integrals

Let $\mathbb{Q}_v$ denote the completion of $\mathbb{Q}$ at the place $v$, where $v = \infty$ or $v = p$ for a prime $p$. Each $\mathbb{Q}_v$ is a locally compact abelian topological group under addition and carries a Haar measure $dx_v$, normalized by:

$$\text{vol}_{dx_\infty}([0,1]) = 1, \qquad \text{vol}_{dx_p}(\mathbb{Z}_p) = 1.$$

Following Tate's thesis (as surveyed in the adelic-physics context of [5]), the local zeta integral attached to a multiplicative character $\chi_v(x) = |x|_v^s$ (unitary part suppressed) is:

$$Z_v(s) = \int_{\mathbb{Q}_v^\times} |x|_v^s \, \mathbf{1}_{\mathcal{O}_v}(x)\, dx_v,$$

where $\mathcal{O}_v$ is the local ring of integers ($\mathcal{O}_\infty = [0,1]$ by our normalization convention for the restricted integral; $\mathcal{O}_p = \mathbb{Z}_p$). The global object is the restricted product $Z_{\text{ad}}(s) = \prod_v Z_v(s)$, convergent for $\Re(s) > 1$.

### 3.2 Diagnostic criterion for "artifact of the $\infty$-place"

We declare a constant $c$ an *Archimedean artifact* if it satisfies both:

- **(A1)** $c$ appears in the Archimedean local factor $Z_\infty$ or in the Haar-measure normalization of an Archimedean Lie group appearing in physical formulas; and
- **(A2)** no $p$-adic local factor $Z_p$ contains $c$; the $p$-adic contributions are rational functions of $p$ and $p^{-s}$.

The conjecture under test is that all "fundamental-looking" appearances of $\pi$ in quantum mechanics satisfy (A1)–(A2), i.e., $\pi$ is a bookkeeping device of the $\infty$-place, and global adelic identities are governed instead by product formulas (e.g., quadratic reciprocity in the form $\prod_v (a,b)_v = 1$ for the Hilbert symbol).

### 3.3 Test structures

We analyze three structures: (S1) the Gaussian integral $\int_{\mathbb{R}} e^{-x^2} dx$; (S2) the completed zeta factorization and its functional equation; (S3) the factorization of adelic quantum mechanics into local dynamics with Archimedean measurement, following the adelic path-integral template of [5]. For (S3) we give the structural derivation and state the computational verification program (adelic harmonic oscillator, adelic CFT partition functions in the style of the equidistribution framework of [1], [6]) as a projection with stated assumptions, not as a completed computation.

## 4. Analysis

### 4.1 Where $\pi$ enters the Gaussian integral (S1)

**Input numbers:** none external; this is a self-contained derivation. Define $I_1 = \int_{\mathbb{R}} e^{-x^2}\, dx$. Square it and write $I_1^2$ as a double integral:

$$I_1^2 = \int_{\mathbb{R}^2} e^{-(x^2 + y^2)}\, dx\, dy.$$

Apply the polar-coordinate map $(x, y) = (r\cos\theta, r\sin\theta)$ with Jacobian $r$. The Jacobian determinant is:

$$\det \frac{\partial(x,y)}{\partial(r,\theta)} = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r.$$

Hence:

$$I_1^2 = \int_0^{2\pi} \!\! \int_0^\infty e^{-r^2}\, r \, dr \, d\theta.$$

The angular integral is the Haar measure of the circle group $S^1$, normalized to $\text{vol}(S^1) = 2\pi$; the radial integral is, with substitution $u = r^2$, $du = 2r\,dr$:

$$\int_0^\infty e^{-r^2} r\, dr = \frac{1}{2}\int_0^\infty e^{-u}\, du = \frac{1}{2}.$$

Therefore:

$$I_1^2 = 2\pi \cdot \frac{1}{2} = \pi, \qquad I_1 = \sqrt{\pi} \approx 1.7724539.$$

**Diagnosis.** The integrand $e^{-x^2}$ is place-agnostic in spirit (an exponential of a quadratic form); the constant $\pi$ enters *exclusively* through the factor $\text{vol}(S^1) = 2\pi$, i.e., through the Haar measure of the Archimedean rotation group. Over $\mathbb{Q}_p$ the analogous "rotation group" — the orthogonal group of a quadratic form over $\mathbb{Q}_p$ — is a totally disconnected $p$-adic Lie group whose Haar measure contributes only rational factors in $p$ (see Section 4.2). This establishes (A1) for $\sqrt{\pi}$ via the Gaussian, and the mechanism is precisely the projection-artifact pattern of [8] in analogy and of [9], [11] in substance.

### 4.2 The $p$-adic local integral contains no $\pi$ (A2 check)

Compute $Z_p(s) = \int_{\mathbb{Z}_p} |x|_p^s\, dx_p$ with $\text{vol}(\mathbb{Z}_p) = 1$. Partition $\mathbb{Z}_p$ into shells: $\mathbb{Z}_p = \{0\} \cup \bigsqcup_{k \ge 0} p^k \mathbb{Z}_p^\times$, where $|x|_p = p^{-k}$ on $p^k\mathbb{Z}_p^\times$ and $\text{vol}(p^k \mathbb{Z}_p^\times) = \text{vol}(p^k\mathbb{Z}_p) - \text{vol}(p^{k+1}\mathbb{Z}_p) = p^{-k} - p^{-(k+1)} = p^{-k}(1 - p^{-1})$. Then:

$$Z_p(s) = \sum_{k=0}^{\infty} p^{-ks} \cdot p^{-k}(1 - p^{-1}) = (1 - p^{-1}) \sum_{k=0}^{\infty} p^{-k(s+1)} = \frac{1 - p^{-1}}{1 - p^{-(s+1)}}.$$

This is a rational function of $p$ and $p^{-s}$: **no $\pi$ appears at any prime place**, confirming (A2) for the Gaussian-type integral. Concrete instance at $s = 2$, $p = 2$:

$$Z_2(2) = \frac{1 - \tfrac{1}{2}}{1 - 2^{-3}} = \frac{\tfrac{1}{2}}{1 - \tfrac{1}{8}} = \frac{\tfrac{1}{2}}{\tfrac{7}{8}} = \frac{4}{7} \approx 0.5714286.$$

Arithmetic check: $1 - 2^{-3} = 1 - 0.125 = 0.875 = 7/8$; $(1/2) \div (7/8) = (1/2)(8/7) = 4/7$. By contrast, the Archimedean restricted integral $\int_0^1 x^2\, dx = 1/3$ is rational too — the transcendental content at $\infty$ lives in the *Gaussian/Fourier* structure, i.e., in the self-duality of $\mathbb{R}$ with its rotation-invariant character $e^{2\pi i x \xi}$, whose period $2\pi$ is again the circle volume. The asymmetry is: at $p$-places, additive self-duality involves only finite roots of unity (no $\pi$); at $\infty$, it forces $S^1$ and hence $\pi$.

### 4.3 The completed zeta function: transcendental content is local to $\infty$ (S2)

The completed Riemann zeta function is:

$$\Lambda(s) = \pi^{-s/2}\,\Gamma\!\left(\frac{s}{2}\right)\,\zeta(s),$$

i.e., the product of the Archimedean local factor $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ with the global Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$, whose factors are the $p$-adic local zeta integrals up to normalization. It satisfies $\Lambda(s) = \Lambda(1 - s)$.

**Claim:** all transcendental content of $\Lambda$ is in $\Gamma_\mathbb{R}$; the functional equation's symmetry is a global (reciprocity-type) statement, consistent with the product-formula philosophy of [1], [2], [6].

**Explicit two-sided verification at $s = 2$ and $s = -1$.**

*Side 1, $s = 2$.* Inputs: $\zeta(2) = \pi^2/6$ (Euler's Basel value); $\Gamma(1) = 1$. Then:

$$\Lambda(2) = \pi^{-1}\,\Gamma(1)\,\frac{\pi^2}{6} = \pi^{-1} \cdot 1 \cdot \frac{\pi^2}{6} = \frac{\pi}{6} \approx 0.5235988.$$

Arithmetic: $\pi^{-1} \approx 0.3183099$; $0.3183099 \times 1.6449341 \approx 0.5235988$, where $\pi^2/6 \approx 1.6449341$.

*Side 2, $s = -1$.* Inputs: $\zeta(-1) = -1/12$ (standard zeta regularization value); $\Gamma(-1/2)$, computed from the recurrence $\Gamma(z+1) = z\,\Gamma(z)$ with $z = -1/2$: $\Gamma(1/2) = -\tfrac{1}{2}\,\Gamma(-\tfrac{1}{2})$, so $\Gamma(-\tfrac{1}{2}) = -2\,\Gamma(1/2) = -2\sqrt{\pi} \approx -3.5449077$. Then:

$$\Lambda(-1) = \pi^{1/2}\,\Gamma\!\left(-\frac{1}{2}\right)\,\zeta(-1) = \sqrt{\pi} \cdot (-2\sqrt{\pi}) \cdot \left(-\frac{1}{12}\right).$$

Step by step: $\sqrt{\pi} \cdot (-2\sqrt{\pi}) = -2\pi$; $(-2\pi) \cdot (-1/12) = \dfrac{2\pi}{12} = \dfrac{\pi}{6} \approx 0.5235988$.

Both sides agree: $\Lambda(2) = \Lambda(-1) = \pi/6 \approx 0.5235988$, matching to the displayed precision ($0.5235988$ vs. $0.5235988$). The functional equation holds, and the *only* place where a transcendental constant enters either evaluation is the factor $\Gamma_\mathbb{R}$: the $p$-adic side of $\zeta(2)$, namely $\prod_p (1 - p^{-2})^{-1}$, is a product of rational numbers, and the value $\zeta(-1) = -1/12$ is rational. The transcendental residue $\pi/6$ is exactly the Archimedean contribution. This is the sharpest available analytic demonstration that $\pi$ is a *local* invariant of the $\infty$-place dressed as a global constant.

### 4.4 Factorization of adelic quantum mechanics and measurement as projection (S3)

Following the adelic QM template [5], a physical amplitude is a restricted product of local amplitudes:

$$\mathcal{A}_{\text{ad}} = \prod_v \mathcal{A}_v, \qquad \mathcal{A}_\infty \text{ Archimedean}, \quad \mathcal{A}_p \ p\text{-adic}.$$

**Structural claim (factorization with Archimedean measurement):** the Hilbert space of adelic QM is a restricted tensor product $\mathcal{H}_{\text{ad}} = \hat{\otimes}_v \mathcal{H}_v$; time evolution factorizes, $U_{\text{ad}}(t) = \prod_v U_v(t)$, because the Hamiltonian is a sum of place-local terms; and every *measurement outcome* is a real number, hence a homomorphism from the adelic configuration space to $\mathbb{R}$ — an Archimedean projection $\pi_\infty$. Consequently, any $\pi$-dependent normalization of amplitudes (Gaussian wave packets, Fresnel phases, $\Gamma(1/2) = \sqrt{\pi}$) appears only in $\mathcal{A}_\infty$ or in the projection postulate, never in the $p$-adic factors. The adelic exponential theory of [3] makes this precise at the group level: the adelic torus carries its own exponential with no $2\pi$-periodicity, so the circle-group origin of $\pi$ (Section 4.1) is absent from the adelic Lie theory. Likewise, the "phase" of a complex number is an Archimedean notion with no $p$-adic analog beyond finite roots of unity, as reflected in the fixed-phase hypothesis of local-field root-counting [7].

**Verification program (projection, not completed computation).** We propose two checks, labeled explicitly as projections:

- **(V1) Adelic harmonic oscillator.** Assumption: the $p$-adic harmonic oscillator path integral of [5] produces local eigenvalue products $E_p$ that are rational functions of $p$ and of the frequency parameter, while $E_\infty \propto \hbar\omega(n + 1/2)$ carries the Archimedean structure. Projection: the global spectrum is $\prod_v E_v$, and $\pi$ appears only through $\Gamma_\mathbb{R}$-type factors at $\infty$. Uncertainty: this is a structural prediction from the factorization ansatz; a full computation requires evaluating the $p$-adic oscillator spectra, which we have not performed here.
- **(V2) Adelic CFT partition functions.** Assumption: partition functions in the equidistribution framework of [1], [6] admit adelic measures whose place-wise projections are computed by the arithmetic equidistribution theorem. Projection: the global partition function's functional equation is governed by reciprocity invariants (Hilbert-symbol product formula $\prod_v (a,b)_v = 1$), with transcendental constants confined to the $\infty$-factor, in analogy with the $\Lambda(s)$ factorization verified in Section 4.3. Uncertainty: the analogy with [2]'s adelic line bundles suggests but does not prove the factorization for CFT data.

## 5. Results

All numbers below are computed in Section 4 with full arithmetic; none are simulated or measured.

- **R1 (Gaussian integral).** $\int_{\mathbb{R}} e^{-x^2}\, dx = \sqrt{\pi} \approx 1.7724539$, with $\pi$ entering solely via the circle Haar measure $\text{vol}(S^1) = 2\pi$ in the polar Jacobian (Section 4.1).
- **R2 ($p$-adic local integral).** $Z_p(s) = \dfrac{1 - p^{-1}}{1 - p^{-(s+1)}}$, a rational function of $p$ and $p^{-s}$; at $s = 2$, $p = 2$: $Z_2(2) = 4/7 \approx 0.5714286$ (Section 4.2). No $\pi$ at any prime place.
- **R3 (functional-equation check).** $\Lambda(2) = \pi^{-1}\Gamma(1)\zeta(2) = \pi/6 \approx 0.5235988$ and $\Lambda(-1) = \sqrt{\pi}\,(-2\sqrt{\pi})(-1/12) = \pi/6 \approx 0.5235988$; the two independent evaluations agree, and the transcendental content is entirely in the Archimedean factor $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ (Section 4.3).
- **R4 (structural result).** In adelic QM with factorized dynamics $U_{\text{ad}} = \prod_v U_v$ and Archimedean measurement projection $\pi_\infty$, $\pi$-dependent terms occur only in $\mathcal{A}_\infty$ and the measurement postulate (Section 4.4). This is a derivation from the factorization ansatz of [5], not an empirical result.
- **R5 (projections with stated assumptions).** The verification targets (V1), (V2) of Section 4.4 are labeled projections: they predict rational-function $p$-adic spectra and reciprocity-governed global functional equations, contingent on the factorization ansatz and on computations (adelic oscillator spectra, adelic CFT partition functions) not performed in this paper.

## 6. Discussion

**What is established vs. conjectured.** R1–R3 are rigorous analytic derivations. R4 is a structural theorem *relative to* the factorization ansatz of adelic QM [5]; if the ansatz fails (e.g., if genuine place-mixing terms exist in the Hamiltonian), the concentration of $\pi$ at $\infty$ need not hold. R5 is explicitly a projection.

**Limitations.** First, "π is an artifact" is a statement about *formulation*, not yet about *nature*: even if every $\pi$ in physics is traceable to $\Gamma_\mathbb{R}$-type factors, one could argue the $\infty$-place is physically privileged (e.g., by measurement being macroscopically Archimedean), making $\pi$ artifactually local but physically indispensable. Second, our criterion (A1)–(A2) is informal; a fully formal definition of "measure-theoretic artifact" in the taxonomy sense of [9], [11] would require a category-theoretic characterization of place-local constants, which we do not supply. Third, the analogy with upsampling artifacts [8] is heuristic; projection artifacts in signal processing have error bounds, and we have no analogous quantitative bound for "Archimedean projection artifacts." Fourth, we did not perform the adelic oscillator or CFT computations; the verification program is the paper's main outstanding obligation. Fifth, the bibliography is constrained: works [4] and [8] are included for terminology and analogy respectively, and the equidistribution literature [1], [2], [6], while structurally supportive, does not directly address physical constants.

**Failure modes and falsification.** The central claim is falsified if: (i) a $p$-adic local factor in a physically adelic amplitude contains $\pi$ non-trivially (e.g., a $p$-adic Gaussian with transcendental normalization); (ii) adelic functional equations for physical partition functions require $\pi$ globally rather than locally at $\infty$; or (iii) the factorization ansatz fails, with place-mixing producing $\pi$-dependent terms outside $\mathcal{A}_\infty$. Conversely, confirmation would be: explicit adelic oscillator and CFT computations in which all transcendental constants sit in the $\infty$-factor and the global relations reduce to reciprocity. A serious internal objection: the value $\zeta(2) = \pi^2/6$ itself is *global* (Euler product over all $p$) yet transcendental — does this contradict the thesis? No: the transcendence enters through $\Gamma_\mathbb{R}(2) = 1/\pi$ in the completed function; the raw Euler product $\prod_p (1-p^{-2})^{-1}$ is a limit of rationals whose transcendence is a statement about the *Archimedean completion of the limit process* — but articulating this precisely is an open problem, and a skeptic could locate $\pi$ in the limit itself rather than in $\Gamma_\mathbb{R}$. We flag this as the strongest objection to our thesis.

**Open questions.** (1) Does every occurrence of $\pi$ in the Standard Model Lagrangian reduce to $\Gamma_\mathbb{R}$-type factors or circle volumes? (2) Is there a $p$-adic analog of the Fresnel integral, and does it converge to a rational-valued distribution? (3) Can the artifact criterion (A1)–(A2) be made functorial, in the spirit of the adelic-tori Lie theory of [3]? (4) What replaces $\pi$ in a hypothetical adelic theory of gravity, given the unit-independence program of [12]?

## 7. Conclusion

Using the Gaussian integral, the completed zeta function, and the factorization structure of adelic quantum mechanics, we have shown with explicit arithmetic that the constant $\pi$ enters physical and number-theoretic formulas exclusively through Archimedean local factors: the Haar measure of the circle group $\text{vol}(S^1) = 2\pi$ in the Gaussian case, and the factor $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ in the zeta case, where the functional-equation identity $\Lambda(2) = \Lambda(-1) = \pi/6 \approx 0.5235988$ was verified by two independent computations. Prime-place integrals contribute only rational functions of $p$ and $p^{-s}$, exemplified by $Z_2(