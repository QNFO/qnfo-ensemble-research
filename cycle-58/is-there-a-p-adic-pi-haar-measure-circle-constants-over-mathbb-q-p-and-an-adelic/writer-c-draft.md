# Is There a p-adic π? Haar-Measure Circumference of p-adic Balls and the Place-Dependence of the Circle Ratio

## Abstract

The research question examined here is whether the Archimedean constant $\pi$, defined as the ratio of a circle's circumference to its diameter, admits a well-defined analogue $\pi_p$ in each $p$-adic completion $\mathbb{Q}_p$ of the rationals, as suggested by the diagonal embedding of $\mathbb{Q}$ into its adelic ring. We set up the simplest geometric test: in $\mathbb{Q}_p^2$ with the sup norm and Haar measure normalized so that the unit ball has measure $1$, we compute the measure of the boundary ("circumference") of a ball of radius $r$ and divide by candidate notions of diameter. We prove the ratio is the rational number $1 - p^{-2}$ (ultrametric diameter) or $(1-p^{-2})/2$ (Archimedean-style diameter), independent of radius. For $p = 2, 3, 5, 7$ this gives $3/4, 8/9, 24/25, 48/49$, tending to $1$ as $p$ grows — not to $\pi \approx 3.14159$. We further compute the finite product over small primes and observe, using Euler's product $1/\zeta(2) = 6/\pi^2$, that the product of all $p$-adic correction factors with the Archimedean ratio $\pi$ equals $6/\pi \approx 1.90986$. The conclusion is that the naive geometric $\pi_p$ exists, is unique, is rational, and is place-dependent, but does not cohere with the Archimedean $\pi$; $\pi$ is not adelic in this sense.

## 1. Introduction

The motivating conjecture, taken from the grounding research idea, is the following: since Ostrowski's theorem tells us that $\mathbb{Q}$ embeds diagonally into all of its completions $\mathbb{Q}_p$ together with $\mathbb{R}$, and since the defining ratio $C/D$ of circumference to diameter is a purely geometric construction, one might hope that "the" circle ratio is a single adelic object of which the familiar $\pi \approx 3.14159265$ is merely the Archimedean projection, and which has a companion $\pi_p$ at every finite prime $p$. If such $\pi_p$ existed, were unique, and were place-independent (or cohered with $\pi$ under some product formula), the conjecture that $\pi$ is an intrinsically adelic constant would be substantiated. If instead every reasonable candidate turns out to be place-dependent and incompatible with $\pi$, the conjecture is refuted in its simplest form — itself a useful, publishable finding.

This paper carries out that test in the most canonical setting available. There is no shortage of $p$-adic special functions that could serve as analytic sources for a $\pi_p$: the literature on $p$-adic $L$-functions, $p$-adic Gamma functions, and $p$-adic period mappings is extensive, and several works in our bibliography construct or conjecture exact relations between $p$-adic and classical constants [1], [2], [4], [8]. But before invoking heavy analytic machinery, one should check the primitive geometric definition, because that is the definition that pins down $\pi$ on the real line: $\pi$ is the number $C/D$ for a circle. If the geometric route already produces a clean, computable, place-dependent answer, that answer is the benchmark any analytic candidate must meet or explicitly renounce.

Our contributions are:

1. A complete, elementary computation of the Haar measure of the boundary of a ball in $\mathbb{Q}_p^2$ (Section 4), yielding the "circumference" $\mu(S_r) = r^2(1 - p^{-2})$.
2. Two candidate circle ratios, $\kappa_p = 1 - p^{-2}$ and $\kappa'_p = (1-p^{-2})/2$, both rational and both computed explicitly for $p = 2, 3, 5, 7, 11$ (Section 4, tabulated in Section 5).
3. A finite adelic product computation, $\prod_{p \le 13} (1-p^{-2}) \approx 0.6180$, and, using the classical Euler product identity $1/\zeta(2) = 6/\pi^2$, the observation that $\pi \cdot \prod_{p}(1-p^{-2}) = 6/\pi \approx 1.90986$ (Section 4, Step 5).
4. A critical discussion of what these results do and do not refute, including failure modes of the construction itself (Section 6).

Throughout, $p$ denotes a prime number, $|\cdot|_p$ the $p$-adic absolute value normalized by $|p|_p = p^{-1}$, and $\mu$ the Haar measure on $\mathbb{Q}_p^2$ normalized in Section 3. All numerical values in Section 5 are computed in Section 4 with arithmetic shown, or are explicitly labeled projections.

## 2. Background and Related Work

We review the twelve supplied bibliography entries, in their exact numbering, and locate our question among them.

[1] (arXiv:0707.3682) formulates a $p$-adic analogue of the conjectures of Bloch–Kato type for number fields: a conjecture relating special values of $p$-adic zeta functions, constructed via syntomic cohomology, to values of classical $L$-functions, with a companion statement for Artin motives and a conjecture on the precise relation between the $p$-adic and classical situations. This is directly relevant to us: the entry explicitly anticipates that $p$-adic and Archimedean special values are related by a precise formula, i.e., that certain constants *do* cohere across places. Our geometric result shows that the most primitive circle ratio does not cohere in this way, so any such coherence must be mediated by non-geometric, arithmetic structure.

[2] (arXiv:1512.09152) treats the supersingular case of the Birch–Swinnerton-Dyer conjecture: for an elliptic curve with good supersingular reduction at $p$, the author formulates $p$-adic analogues of the BSD formula using a pair of $p$-adic $L$-functions $L^{(\alpha)}$ and $L^{(\beta)}$, shows equivalence with earlier formulations, and generalizes a rank criterion in terms of values of these functions. The relevance is methodological: in the supersingular setting the naive "one $p$-adic object per place" picture breaks and must be replaced by a pair of objects. Our result exhibits the same moral at the level of elementary geometry: even the circle ratio refuses to be a single $p$-adic number matching the real one, and we too must track two candidate normalizations $\kappa_p$ and $\kappa'_p$.

[3] (arXiv:0708.0962) studies phase transitions of the $q$-state Potts model on $p$-adic trees (Bethe lattices), proving that the number of Gibbs measures and the structure of the set of translation-invariant and periodic Gibbs measures depend on $q$, on $p$, and on the temperature parameter, with the phase-transition picture changing discontinuously as parameters vary. This is a worked example of how $p$-adic geometry produces qualitatively different, parameter-dependent behavior from its Archimedean counterpart — the same phenomenon we quantify for the circle ratio, where the "constant" depends on the prime $p$.

[4] (arXiv:2103.06864) introduces, for an Artin motive and a prime $p$ of the relevant reduction type, a family of $p$-adic Stark-type regulators and formulates a main conjecture of Iwasawa-theoretic type relating them to a $p$-adic $L$-function, proving that the conjecture implies the $p$-adic Beilinson-type conjecture in that context. Like [1], this entry supports the general expectation that $p$-adic and classical special values are bridged by conjectural exact formulas; our paper tests the simplest possible bridge and finds it absent at the purely geometric level.

[5] (arXiv:2401.04829) develops $p$-adic analogues of the uncertainty principle: for finite-index subgroups of the Heisenberg group over $\mathbb{Q}_p$, the author proves a $p$-adic version of the uncertainty principle in terms of the sizes of a function and its Fourier transform, and derives analogues of the Donoho–Stark uncertainty estimates. The entry demonstrates that genuinely Archimedean-flavored inequalities, involving constants tied to the geometry of the ambient group, admit $p$-adic analogues whose forms are structurally similar but numerically independent of the real constants. This is exactly the pattern our computation confirms for the circle ratio.

[6] (arXiv:2402.06254) studies the $p$-adic quantum walk on the ring of $p$-adic integers $\mathbb{Z}_p$, defining the walk via a unitary operator on $\ell^2(\mathbb{Z}_p)$ built from coherent states, and analyzes its dispersion and localization behavior, finding behavior qualitatively different from the real-line quantum walk. The entry supplies another instance of a real-line construction whose $p$-adic counterpart is well-defined but behaves differently; it motivates our choice of $\mathbb{Q}_p^2$ with its natural measure as the arena for a $p$-adic circle.

[7] (arXiv:2403.04947) proves a $p$-adic analogue of the Agmon–Nirenberg type uniqueness theorem for solutions of parabolic evolution equations over $\mathbb{Q}_p$, establishing conditions under which a nontrivial solution must be strictly positive, with the analysis carried out relative to the $p$-adic norm and Vladimirov-type operators. The entry shows that the analytic calculus on $\mathbb{Q}_p$ — norms, derivatives, evolution — is robust enough to support theorems with the same logical shape as their real counterparts, which is the background assurance one needs before defining geometric quantities such as circumference in $\mathbb{Q}_p^2$.

[8] (arXiv:2404.09214) constructs $p$-adic analogues of the classical Weierstrass elliptic functions $\wp$ and $\zeta$ over $\mathbb{Q}_p$, studies their addition formulas, division formulas, and associated elliptic function fields, and establishes the analogues of classical addition theorems. This is the closest analytic relative of our question in the bibliography: elliptic functions are the natural habitat of periods, and $\pi$ is a period. The entry establishes that the $p$-adic elliptic calculus exists and mirrors the classical one formally; our result supplies the cautionary datum that the simplest period-like ratio does not numerically carry over.

[9] (arXiv:2405.08352) investigates the $p$-adic Schrödinger operator with a point interaction potential on $\mathbb{Q}_p$, deriving the resolvent formula, analyzing the spectrum, and studying scattering-type phenomena relative to the $p$-adic norm. As with [5]–[7], the entry confirms the health of $p$-adic analysis as a discipline; it does not itself treat circle ratios, and we use it only as evidence that our arena $\mathbb{Q}_p^2$ supports the standard measure-theoretic and analytic apparatus our computation requires.

[10] (arXiv:2406.01234) proves a $p$-adic analogue of the Hardy–Littlewood–Sobolev inequality for the Vladimirov fractional derivative operator on $\mathbb{Q}_p$, identifying the sharp constant in the inequality and computing it explicitly in terms of Gamma-function values at $p$-adic arguments. This entry is notable for us because it contains an actual computed $p$-adic constant playing the role that dimensional constants play in the real HLS inequality: it is a precedent for "the $p$-adic analogue of a famous real constant is a definite, computable, different number," which is precisely the thesis our paper verifies for $\pi$ at the geometric level.

[11] (arXiv:2407.01539) studies the $p$-adic heat semigroup generated by the Vladimirov operator, establishing smoothing estimates, heat-kernel asymptotics, and the $p$-adic analogue of the Gaussian, with explicit kernel formulas in terms of the $p$-adic norm. The explicit heat kernel is the $p$-adic counterpart of the real Gaussian whose normalization involves $\sqrt{\pi}$; the entry thus touches, from the analytic side, the same network of constants we approach geometrically, though the supplied summary does not state a value of any $p$-adic $\pi$, and we draw no numerical claim from it.

[12] (arXiv:2408.02177) formulates a $p$-adic adelic product formula framework: the author considers products of local densities or local contributions over all places of $\mathbb{Q}$, including the Archimedean one, and proves that under suitable normalization the product is a rational number, illustrating the mechanism with explicit local computations at several primes. This is the closest structural precedent for our Step 5: an adelic product in which the Archimedean factor involves $\pi$ and the finite factors are rational. The entry's existence shows that "Archimedean factor times product of rational $p$-adic factors equals a rational number" is a live pattern; our computation realizes it for the circle ratio with the value $6/\pi$.

Two further entries in the supplied bibliography are notebook-level items rather than papers: the grounding research idea itself, and two Zenodo-recorded thesis items [11b], [12b] whose supplied summaries state only that they propose a "Compton count" as the only primitive physical invariant and an "ODR framework" built on it. The supplied summaries give no further detail, and no mathematical content connectable to $p$-adic constants; we therefore relate them to our argument only through what the summaries state, namely that they advocate reducing physical constants to a single primitive count — a program our result complicates, since it shows a flagship constant ($\pi$) does not reduce to a single place-independent primitive but fragments across places as the rational numbers $1 - p^{-2}$.

## 3. Methods

**Arena and norm.** Fix a prime $p$. Let $\mathbb{Q}_p$ be the $p$-adic completion of $\mathbb{Q}$, with absolute value $|\cdot|_p$ normalized by $|p|_p = p^{-1}$ and $|q|_p = 1$ for every prime $q \neq p$. On $\mathbb{Q}_p^2$ we use the sup norm

$$\|x\| = \max\bigl(|x_1|_p,\ |x_2|_p\bigr), \qquad x = (x_1, x_2) \in \mathbb{Q}_p^2,$$

which is the standard ultrametric norm on $\mathbb{Q}_p^2$ and the one relative to which the analytic literature of Section 2 ([5]–[10]) operates on $\mathbb{Q}_p$ and its quadratic extensions.

**Measure.** Let $\mu$ be the Haar measure on the additive group $\mathbb{Q}_p^2$, normalized by

$$\mu\bigl(B_1\bigr) = 1, \qquad B_1 = \{x \in \mathbb{Q}_p^2 : \|x\| \le 1\}.$$

Haar measure is the unique (up to scaling) translation-invariant Borel measure on $\mathbb{Q}_p^2$; it is the direct analogue of Lebesgue measure on $\mathbb{R}^2$ and is the measure used throughout the $p$-adic analysis literature cited above.

**Circle.** For $r \in p^{\mathbb{Z}}$ (the values the sup norm attains on $\mathbb{Q}_p^2$), define the closed ball and its boundary:

$$B_r = \{x : \|x\| \le r\}, \qquad S_r = \{x : \|x\| = r\}.$$

In the ultrametric, $S_r$ is exactly $B_r \setminus B_{r/p}$: every point with $\|x\| \le r$ either has $\|x\| \le r/p$ or $\|x\| = r$, because the norm takes values in the discrete set $p^{\mathbb{Z}} \cup \{0\}$. The set $S_r$ is the $p$-adic circle of radius $r$: it is the locus of points at distance exactly $r$ from the origin, just as the Euclidean circle is the locus of points at distance exactly $r$ from the origin in $\mathbb{R}^2$.

**Circumference and diameter.** We define the $p$-adic circumference of $S_r$ as its Haar measure, $C_p(r) = \mu(S_r)$ — the direct analogue of arc length in $\mathbb{R}^2$, where the circle's one-dimensional measure is its circumference. For diameter we compute both available notions:

- $D_p(r) = \operatorname{diam}(S_r) = \sup\{\|x - y\| : x, y \in S_r\}$, the intrinsic (ultrametric) diameter;
- $D'_p(r) = 2r$, the Archimedean-style diameter, meaningful because $2$ is a $p$-adic unit for every odd $p$ (and we treat $p = 2$ separately).

The candidate constants are the scale-invariant ratios

$$\kappa_p = \frac{C_p(r)}{D_p(r)}, \qquad \kappa'_p = \frac{C_p(r)}{D'_p(r)}.$$

**Adelic product.** We additionally compute the finite product $P_N = \prod_{p \le N} \kappa_p$ over the first primes, and combine it with the Archimedean ratio $\kappa_\infty = \pi$ using the classical Euler product identity $1/\zeta(2) = \prod_p (1 - p^{-2}) = 6/\pi^2$, which is a theorem of elementary number theory, not an empirical claim.

## 4. Analysis

All inputs are definitions from Section 3 or classical identities of number theory; no empirical data are used.

**Step 1: Scaling of ball measure.** Haar measure on $\mathbb{Q}_p^2$ transforms under dilation $x \mapsto a x$ by the factor $|a|_p^2$ (the modulus of the dilation automorphism on the two-dimensional group). Hence for $r = p^{-n}$, $n \in \mathbb{Z}$:

$$\mu(B_{p^{-n}}) = |p^{-n}|_p^2 \cdot \mu(B_1) = \left(p^{n}\right)^2 \cdot 1 = p^{2n}.$$

Check against normalization: $n = 0$ gives $\mu(B_1) = 1$, as required. Writing $r = p^{-n}$, this reads

$$\mu(B_r) = r^2 \qquad \text{for } r \in p^{\mathbb{Z}}.$$

**Step 2: Circumference.** Since $S_r = B_r \setminus B_{r/p}$ (Section 3) and $B_{r/p} \subset B_r$:

$$C_p(r) = \mu(S_r) = \mu(B_r) - \mu(B_{r/p}) = r^2 - \left(\frac{r}{p}\right)^2 = r^2\left(1 - p^{-2}\right).$$

**Step 3: Ultrametric diameter.** For $x, y \in S_r$, the ultrametric inequality gives $\|x - y\| \le \max(\|x\|, \|y\|) = r$. Conversely, take $x = (r, 0)$ and $y = (0, r)$: both lie in $S_r$ (their norms are $|r|_p \cdot |1|_p = r$ and $r$), and $\|x - y\| = \max(|r|_p, |{-r}|_p) = r$. Hence

$$D_p(r) = r.$$

Note the ultrametric surprise: the diameter of the $p$-adic circle equals its radius, not $2r$.

**Step 4: The two ratios.**

$$\kappa_p = \frac{C_p(r)}{D_p(r)} = \frac{r^2(1 - p^{-2})}{r} = 1 - p^{-2} = \frac{p^2 - 1}{p^2},$$

$$\kappa'_p = \frac{C_p(r)}{2r} = \frac{1 - p^{-2}}{2} = \frac{p^2 - 1}{2p^2}.$$

Both are independent of $r$ (scale-invariant, as Haar measure and diameter scale identically) and both are rational numbers. Explicit values:

- $p = 2$: $\kappa_2 = 1 - 2^{-2} = 1 - \tfrac{1}{4} = \tfrac{3}{4} = 0.75$; $\kappa'_2 = \tfrac{3}{8} = 0.375$.
- $p = 3$: $\kappa_3 = 1 - \tfrac{1}{9} = \tfrac{8}{9} \approx 0.888889$; $\kappa'_3 = \tfrac{4}{9} \approx 0.444444$.
- $p = 5$: $\kappa_5 = 1 - \tfrac{1}{25} = \tfrac{24}{25} = 0.96$; $\kappa'_5 = \tfrac{12}{25} = 0.48$.
- $p = 7$: $\kappa_7 = 1 - \tfrac{1}{49} = \tfrac{48}{49} \approx 0.979592$; $\kappa'_7 = \tfrac{24}{49} \approx 0.489796$.
- $p = 11$: $\kappa_{11} = 1 - \tfrac{1}{121} = \tfrac{120}{121} \approx 0.991736$; $\kappa'_{11} = \tfrac{60}{121} \approx 0.495868$.

**Step 5: Finite adelic product.** With $\kappa_\infty = \pi$ (the true Archimedean ratio $C/D = 2\pi r / 2r = \pi$) and $\kappa_p = (p^2-1)/p^2$:

$$P_{13} = \prod_{p \le 13} \kappa_p = \frac{3}{4} \cdot \frac{8}{9} \cdot \frac{24}{25} \cdot \frac{48}{49} \cdot \frac{120}{121} \cdot \frac{168}{169}.$$

Arithmetic, keeping exact fractions:

$$\frac{3}{4} \cdot \frac{8}{9} = \frac{24}{36} = \frac{2}{3}; \qquad \frac{2}{3} \cdot \frac{24}{25} = \frac{48}{75} = \frac{16}{25};$$

$$\frac{16}{25} \cdot \frac{48}{49} = \frac{768}{1225}; \qquad \frac{768}{1225} \cdot \frac{120}{121} = \frac{92160}{148225};$$

$$\frac{92160}{148225} \cdot \frac{168}{169} = \frac{15482880}{25052025} \approx 0.618029.$$

So $P_{13} \approx 0.618029$. By the Euler product for the Riemann zeta function at $s = 2$,

$$\prod_{p} \kappa_p = \prod_p \left(1 - p^{-2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2} \approx \frac{6}{9.869604} \approx 0.607927,$$

using $\pi^2 \approx 9.869604$ (from $\pi \approx 3.141593$, squared: $3.141593^2 = 9.869604$). The finite product $P_{13} \approx 0.618029$ lies above the infinite product $\approx 0.607927$, as it must, since every factor $1 - p^{-2} < 1$ and the omitted primes ($17, 19, \dots$) contribute further factors below $1$.

**Step 6: The combined adelic observation.** Multiply the Archimedean ratio by the full $p$-adic product:

$$\kappa_\infty \cdot \prod_p \kappa_p = \pi \cdot \frac{6}{\pi^2} = \frac{6}{\pi} \approx \frac{6}{3.141593} \approx 1.909859.$$

This is a genuine computation: given the theorem $\prod_p (1-p^{-2}) = 6/\pi^2$ and the definition $\kappa_\infty = \pi$, the product over all places of our circle ratios is exactly $6/\pi \approx 1.909859$ — a place-combined constant that is *not* rational and *not* $1$, i.e., the naive ratios do not satisfy a product formula equal to $1$.

**Step 7: Comparison with $\pi$.** The Archimedean value is $\pi \approx 3.141593$ (or $\pi/2 \approx 1.570796$ if one compares against $\kappa'$). Every $\kappa_p$ computed above lies in $(0, 1)$, and $\kappa_p \to 1$ as $p \to \infty$ since $p^{-2} \to 0$. Therefore

$$|\kappa_p - \pi| \ge \pi - 1 \approx 2.141593 \quad \text{for all } p,$$

and similarly $|\kappa'_p - \pi/2| \ge \pi/2 - 1/2 \approx 1.070796$. The geometric $p$-adic circle ratio never approaches the Archimedean one.

## 5. Results

All numbers below are computed in Section 4 with arithmetic shown; none are empirical, and none are projections.

**R1 (main theorem).** In $\mathbb{Q}_p^2$ with the sup norm and $\mu(B_1) = 1$, the Haar measure of the $p$-adic circle of radius $r \in p^{\mathbb{Z}}$ is

$$C_p(r) = r^2\left(1 - p^{-2}\right),$$

and the circle ratios are the rational, radius-independent, place-dependent constants

$$\kappa_p = 1 - p^{-2} = \frac{p^2-1}{p^2}, \qquad \kappa'_p = \frac{p^2-1}{2p^2}.$$

**R2 (table of values).**

| $p$ | $\kappa_p$ (decimal) | $\kappa'_p$ (decimal) |
|---|---|---|
| 2 | $3/4 = 0.75$ | $3/8 = 0.375$ |
| 3 | $8/9 \approx 0.888889$ | $4/9 \approx 0.444444$ |
| 5 | $24/25 = 0.96$ | $12/25 = 0.48$ |
| 7 | $48/49 \approx 0.979592$ | $24/49 \approx 0.489796$ |
| 11 | $120/121 \approx 