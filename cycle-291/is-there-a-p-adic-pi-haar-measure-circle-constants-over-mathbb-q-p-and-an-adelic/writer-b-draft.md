# Is There a $p$-Adic $\pi$? Haar-Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p = (p-1)/p$

## Abstract

The real number $\pi \approx 3.14159$ is defined as the ratio of a circle's circumference to its diameter, and Ostrowski's theorem embeds $\mathbb{Q}$ diagonally into every completion $\mathbb{R}$ and $\mathbb{Q}_p$. A current adelic-physics program asserts that $\pi$ is adelic with the place-wise value $\pi_p = (p-1)/p$ at each prime, and builds falsifiability matrices and quantum-field-theory constraint programs on such claims; no geometric computation has tested whether circle geometry over $\mathbb{Q}_p$ supports any place-wise value. We work with the Haar measure $\mu$ on $\mathbb{Q}_p^2$ normalized by $\mu(B_1) = 1$ for the unit ball of the sup norm, and compute exactly: $\mu(B_r) = r^2$ and the sphere measure $C_p(r) = r^2(1 - p^{-2})$ for $r \in p^{\mathbb{Z}}$. Two scale-invariant ratios follow: $\kappa_p = 1 - p^{-2}$ (ultrametric diameter) and $\kappa'_p = (1 - p^{-2})/2$ (diameter $2r$). Both are rational, place-dependent, bounded by $1$, and tend to $1$ rather than to $\pi$. Against the corpus conjecture, $\kappa_p - (p-1)/p = (p-1)/p^2$, which vanishes only in the limit $p \to \infty$. The Euler product gives $\prod_p \kappa_p = 6/\pi^2 \approx 0.607927$, and the all-place product is $6/\pi \approx 1.909859 \neq 1$. The adelic-$\pi$ conjecture fails place-wise in this formulation; $\pi$ survives only as a global product invariant.

## 1. Introduction

A program of "adelic physics" currently in active development faces a concrete verification problem. Its central documents assert that fundamental constants, including $\pi$, exist at every Ostrowski completion of $\mathbb{Q}$ and carry specific $p$-adic values: one document states the finding that "$\pi$ IS adelic -- $\pi_p = (p-1)/p$ at each prime $p$" [9]; a companion catalogs sixteen "completion failures" of archimedean-only physics and proposes an eight-claim falsifiability matrix on which the whole program stands or falls [10]; a third runs numerical constraint programs on adelic beta functions and reports, as its own honest negative result, that numerological zeta-zero/mass-ratio matches were statistically falsified after correction for multiple comparisons [11]. If the place-wise value $\pi_p = (p-1)/p$ is wrong, every downstream claim that consumes it inherits the error, and the falsifiability matrix of [10] is testing a corrupted input. What is missing is a direct geometric computation: does circle geometry over $\mathbb{Q}_p$, done with the same measure-theoretic tools the program itself invokes, produce a place-wise constant at all, and does it equal $(p-1)/p$?

This paper performs that computation and reports a deflationary answer. Using the Haar measure on $\mathbb{Q}_p^2$ — the direct analogue of Lebesgue area, and the unique translation-invariant Borel measure up to scaling — we find that a natural, scale-invariant circle constant exists at every place, namely $\kappa_p = 1 - p^{-2}$ (or $\kappa'_p = (1-p^{-2})/2$ under the archimedean-style diameter convention). But neither equals the corpus value $(p-1)/p$: the difference $\kappa_p - (p-1)/p = (p-1)/p^2$ is nonzero at every prime and vanishes only asymptotically. Meanwhile the Euler product over all finite places collapses to the exact value $6/\pi^2$, so $\pi$ reappears not as any single place's constant but as a global invariant of the product. The strong form of the adelic-$\pi$ conjecture — a place-wise family interpolating toward $\pi$ — fails; the weak form — $\pi$ encoded globally — survives.

Our contributions are:

1. An explicit Haar-measure computation (Section 4) showing that the ball of radius $r = p^m$ in $\mathbb{Q}_p^2$ has measure $r^2$ and the sphere has measure $r^2(1 - p^{-2})$, with all arithmetic displayed.
2. The identification of the two scale-invariant ratios $\kappa_p = 1 - p^{-2}$ and $\kappa'_p = (1 - p^{-2})/2$, with exact values for $p = 2, 3, 5, 7, 11$ (Section 4).
3. The exact evaluation $\prod_p \kappa_p = 6/\pi^2 \approx 0.607927$, the finite product $P_{13} \approx 0.618029$ over $p \leq 13$, and the all-place combination $6/\pi \approx 1.909859 \neq 1$ (Section 4).
4. A term-by-term comparison with the corpus conjecture $\pi_p = (p-1)/p$ [9], giving the exact difference $\kappa_p - (p-1)/p = (p-1)/p^2$ and ratio $\kappa_p \cdot p/(p-1) = (p+1)/p$, and the divergence to $0$ of the corresponding product $\prod_p (p-1)/p$ (Section 4).
5. A critical assessment (Section 6) of what these results imply for the adelic-$\pi$ conjecture, including failure modes of the Haar-measure definition, and a practical pathway (Section 7) for the program's participants.

Throughout, $|\cdot|_p$ denotes the $p$-adic absolute value, normalized so that $|p|_p = p^{-1}$ and $|q|_p = 1$ for every prime $q \neq p$, and $\mathbb{Z}_p = \{x \in \mathbb{Q}_p : |x|_p \leq 1\}$ is the ring of $p$-adic integers. All measures and constants in this paper are computed, not simulated; no empirical data are used.

## 2. Background and Related Work

The question of a $p$-adic $\pi$ sits at the intersection of three bodies of work: the arithmetic of $p$-adic special values, $p$-adic geometry and physics, and the adelic-physics corpus that motivates the test.

**Special values in $p$-adic number theory.** The translation of archimedean special-value statements into $p$-adic language is an established program, and its flagship results display exactly how $\pi$ behaves when it appears in arithmetic formulas. Borel's theorem, as recalled in [1], relates regulators of number fields to special values of zeta functions through the class number formula $w\sqrt{|D_k|}\,\mathrm{Res}_{s=1}\zeta_k(s) = 2^{r_1}(2\pi)^{r_2}\,|\mathrm{Cl}(\mathcal{O}_k)|\,R$: the factor $(2\pi)^{r_2}$ is the archimedean regulator contribution. The same work formulates a conjectural $p$-adic analogue of Borel's theorem using syntomic regulators and $p$-adic $L$-functions, together with a corresponding conjecture for Artin motives and a conjecture about the precise relation between the $p$-adic and classical situations [1]. The structural lesson for us is that in every such formula $\pi$ enters through the archimedean place only, and the $p$-adic side carries its own regulators; nothing in that program suggests a place-wise $\pi_p$. The motivic extension is carried further in [3], which, for an odd prime $p$ and a $p$-stabilized Artin representation, introduces a family of $p$-adic Stark regulators, formulates an Iwasawa–Greenberg main conjecture, and proves an interpolation formula (Theorem A) for a generator of a characteristic ideal of the $\Lambda$-module $U_\infty$ of norm-coherent unit sequences; again the $p$-adic objects are $L$-functions and regulators, not geometric constants. On the analytic side, [7] constructs $p$-adic multiple $L$-functions in several variables as generalizations of the Kubota–Leopoldt $p$-adic $L$-functions via a specific $p$-adic measure, proves their $p$-adic analyticity and continuity (Theorems 1.21 and 1.24), and evaluates their special values at non-positive integers in terms of twisted multiple Bernoulli numbers (Theorem 2.1). These functions are the natural analytic home for any future theory of $p$-adic transcendental constants, and the fact that their special values are Bernoulli-theoretic rather than geometric reinforces the expectation that a geometric $\pi_p$, if it existed, would be a new kind of object.

**$p$-adic geometry with its own constants.** That $p$-adic geometry is autonomous rather than a distorted copy of the real case is documented in several places. In extremal combinatorial geometry, [4] introduces $p$-adic equiangular lines in $\mathbb{Q}_p^d$ and derives the $p$-adic van Lint–Seidel relative bound $|n|^2 \leq |d|\max\{|n|, \gamma^2\}$, the $p$-adic counterpart of the classical bound $n(1-d\gamma^2) \leq d(1-\gamma^2)$; the bound takes a different functional form from its real archetype, which is the same phenomenon we quantify for the circle ratio. In statistical mechanics, [2] reduces the description of $p$-adic Gibbs measures for the three-state Potts model with competing interactions on a Cayley tree of order two to a recursive equation and proves that a phase transition occurs if and only if $p = 3$, for any nonzero interaction value, with uniqueness of the Gibbs measure otherwise; the authors explicitly note that these results are totally different from the real case, where phase transitions depend on interaction constraints rather than on the place. Place-dependence of the kind $\kappa_p$ exhibits is therefore already visible in $p$-adic physics. In relativistic geometry, [5] shows that the algebraic extensions of $\mathbb{Q}_p$ allowing a square root near the $p$-adic real axis have dimension $D = 4$ for $p > 2$ and $D = 8$ for $p = 2$, that the convergence radius of the square-root Taylor series is nonvanishing, and that the resulting region is the $p$-adic counterpart of the future light cone, built from cylinders of radius $N_p(t) = p^k$ and length $p^{k-1}(p-1)$ whose cross-sections are parallelepipeds rather than balls. The last detail is directly relevant to us: even the $p$-adic "ball" of a relativistic light cone is not a ball, so the choice of geometric primitive in $\mathbb{Q}_p$ is genuinely conventional, as our diameter ambiguity in Section 3 will also show. The mathematical infrastructure is surveyed in [6], which describes the $p$-adic norm as depending only on the lowest pinary digit of the expansion, the canonical identification $\mathrm{Id}: R_p \to R_+$ mapping $p$-adic to non-negative real numbers, and the fact that algebraic extensions of $p$-adic numbers of arbitrary dimension exist — the toolkit within which any $p$-adic circle theory must be built.

**The motivating corpus.** The adelic-physics program itself supplies the conjecture under test. The Harmonic Paradigm audit [9] reports five findings, the third of which is the claim "$\pi$ IS adelic -- $\pi_p = (p-1)/p$ at each prime $p$"; the same document concludes that the Paradigm's core $\beta$-function mechanism was tested exclusively over $\mathbb{R}$ and was retracted after direct calculation showed the logistic ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$ incompatible with the textbook QED coefficient $\beta(\alpha) = (2/3\pi)\alpha^2$, and it invokes the adelic product formula $\prod_v |q|_v = 1$ as the arithmetic identity connecting all places. The value $(p-1)/p$ is thus a specific, checkable prediction, and Section 4 checks it. The taxonomy document [10] states the product formula $\prod_v |q|_v = 1$ over all places $\{\infty, 2, 3, 5, \dots\}$, catalogs sixteen completion failures across five categories with two resolved and eight under active investigation, and proposes an eight-claim falsifiability matrix with binary yes/no tests; our computation supplies exactly the kind of binary test that matrix calls for. The constraint program [11] reports an adelic beta constraint error $< 10^{-13}$ and an adelic product formula error $< 10^{-12}$ in its master table, and — importantly for methodological standards — documents an honest negative result in which candidate matches between zeta-zero gaps and particle mass ratios were statistically falsified after Bonferroni correction and a permutation null model; we adopt the same standard here by reporting our own negative result for the place-wise conjecture.

**The predecessor computation.** The earlier version of this analysis [8] established the Haar-measure framework and the constants $\kappa_p = 1 - p^{-2}$ and $\kappa'_p = (1-p^{-2})/2$, the products $6/\pi^2$ and $6/\pi$, and the conclusion that the adelic-$\pi$ conjecture fails place-wise while surviving globally. The present paper revises that work in three ways: it removes the framework's dependence on any untestable conjectural framing, it adds the term-by-term comparison with the corpus value $(p-1)/p$ that the predecessor did not perform, and it adds the practical pathway of Section 7.

None of the works above states a Haar-measure circle constant, and only [9] states a candidate value for a $p$-adic $\pi$; the gap this paper fills is the direct confrontation between the two.

## 3. Methods

**Arena and norm.** Fix a prime $p$. On $\mathbb{Q}_p^2$ we use the sup norm

$$\|x\| = \max\bigl(|x_1|_p,\ |x_2|_p\bigr), \qquad x = (x_1, x_2) \in \mathbb{Q}_p^2,$$

which is the standard ultrametric norm on $\mathbb{Q}_p^2$. The values attained by $\|\cdot\|$ on $\mathbb{Q}_p^2 \setminus \{0\}$ are exactly $r \in p^{\mathbb{Z}}$, since $|x_i|_p \in p^{\mathbb{Z}} \cup \{0\}$.

**Measure.** Let $\mu$ be the Haar measure on the additive group $\mathbb{Q}_p^2$, normalized by

$$\mu(B_1) = 1, \qquad B_1 = \{x \in \mathbb{Q}_p^2 : \|x\| \leq 1\}.$$

Haar measure is the unique (up to scaling) translation-invariant Borel measure on $\mathbb{Q}_p^2$; it is the direct analogue of Lebesgue measure on $\mathbb{R}^2$. Under the dilation $x \mapsto a x$, Haar measure transforms by the modulus of the dilation automorphism, which is $|a|_p^2$ on the two-dimensional group.

**Circle.** For $r \in p^{\mathbb{Z}}$, $r > 0$, define the closed ball and sphere

$$B_r = \{x : \|x\| \leq r\}, \qquad S_r = \{x : \|x\| = r\}.$$

Because the norm takes values in the discrete set $p^{\mathbb{Z}} \cup \{0\}$, every point of $B_r$ has norm either $\leq r/p$ or exactly $r$; hence

$$S_r = B_r \setminus B_{r/p}.$$

The set $S_r$ is the locus of points at distance exactly $r$ from the origin, the direct analogue of the Euclidean circle, and we adopt it as the definition of the $p$-adic circle. (Since $\mathbb{Q}_p$ is totally disconnected, $S_r$ is not the topological boundary of $B_r$; it is the measure-theoretic circle standard in $p$-adic harmonic analysis. The precedent for conventional geometric primitives is noted in Section 2: the $p$-adic light cone of [5] has parallelepiped, not ball, cross-sections.)

**Circumference and diameters.** We define the $p$-adic circumference of $S_r$ as its Haar measure, $C_p(r) = \mu(S_r)$, the analogue of arc length. For diameter we compute both available notions:

- $D_p(r) = \operatorname{diam}(S_r) = \sup\{\|x - y\| : x, y \in S_r\}$, the intrinsic ultrametric diameter;
- $D'_p(r) = 2r$, the archimedean-style diameter, meaningful because $2$ is a $p$-adic unit for every odd $p$ (the case $p = 2$ is included for completeness but the convention is then less natural).

The candidate constants are the scale-invariant ratios

$$\kappa_p = \frac{C_p(r)}{D_p(r)}, \qquad \kappa'_p = \frac{C_p(r)}{D'_p(r)}.$$

A candidate is acceptable if it is independent of $r$ (scale invariance, which $\pi$ satisfies) and, ideally, independent of $p$ (place invariance, which the conjecture hopes for).

**Corpus comparison.** The Harmonic Paradigm audit states the prediction $\pi_p = (p-1)/p$ at each prime [9]. We treat this as a pointwise hypothesis about the same quantity our geometry produces and compute, for each prime, the difference $\kappa_p - (p-1)/p$ and the ratio $\kappa_p / \bigl((p-1)/p\bigr)$, as well as the behavior of the product $\prod_p (p-1)/p$ over primes.

**Adelic product.** We compute the finite product $P_N = \prod_{p \leq N} \kappa_p$ and combine it with the archimedean ratio $\kappa_\infty = \pi$ using the classical Euler product identity $\prod_p (1 - p^{-2}) = 1/\zeta(2) = 6/\pi^2$, a theorem of elementary number theory, not an empirical claim.

## 4. Analysis

All inputs are definitions from Section 3, classical identities of number theory, or the stated prediction of [9]; no empirical data are used.

**Step 1: measure of a ball.** Let $r = p^m$ with $m \in \mathbb{Z}$. The ball $B_r$ is the dilation of the unit ball by $a = p^{-m}$: indeed $x \in B_r$ means $\|x\| \leq p^m$, i.e. $x = p^{-m} y$ with $\|y\| \leq 1$. Haar measure transforms under $x \mapsto p^{-m} x$ by the factor $|p^{-m}|_p^2 = (p^m)^2 = p^{2m} = r^2$. Hence

$$\mu(B_r) = |p^{-m}|_p^2 \cdot \mu(B_1) = p^{2m} \cdot 1 = r^2.$$

Check against normalization: $m = 0$ gives $\mu(B_1) = 1$, as required. Sanity check in one dimension: $\mu(\{x : |x|_p \leq r\}) = r$ for $r = p^m$, since $\{x : |x|_p \leq p^m\} = p^{-m}\mathbb{Z}_p$ and $|p^{-m}|_p \cdot \mu(\mathbb{Z}_p) = p^m = r$; then Fubini over the two coordinates gives $\mu(B_r) = r \cdot r = r^2$, agreeing with the dilation computation.

**Step 2: circumference.** Since $S_r = B_r \setminus B_{r/p}$ and $B_{r/p} \subset B_r$:

$$C_p(r) = \mu(S_r) = \mu(B_r) - \mu(B_{r/p}) = r^2 - \left(\frac{r}{p}\right)^2 = r^2\left(1 - \frac{1}{p^2}\right).$$

Explicitly, $r^2 - r^2 p^{-2} = r^2 \frac{p^2 - 1}{p^2}$, and $p^2 - 1 = (p-1)(p+1)$, so $C_p(r) = r^2 \frac{(p-1)(p+1)}{p^2}$.

**Step 3: ultrametric diameter.** For $x, y \in S_r$, the ultrametric inequality gives $\|x - y\| \leq \max(\|x\|, \|y\|) = r$. Conversely, take $x = (p^{-m} u, 0)$ and $y = (0, p^{-m} u)$ for any $p$-adic unit $u$ with $|u|_p = 1$; then $\|x\| = \|y\| = p^{-m} \cdot 1 = r$, so both lie in $S_r$, and

$$\|x - y\| = \max\bigl(|p^{-m} u|_p,\ |{-p^{-m} u}|_p\bigr) = p^m = r.$$

Hence

$$D_p(r) = r.$$

Note the ultrametric surprise: the diameter of the $p$-adic circle equals its radius, not $2r$.

**Step 4: the two ratios.**

$$\kappa_p = \frac{C_p(r)}{D_p(r)} = \frac{r^2(1 - p^{-2})}{r} = 1 - \frac{1}{p^2} = \frac{p^2 - 1}{p^2},$$

$$\kappa'_p = \frac{C_p(r)}{2r} = \frac{r^2(1 - p^{-2})}{2r} = \frac{1}{2}\left(1 - \frac{1}{p^2}\right) = \frac{p^2 - 1}{2p^2}.$$

Both are independent of $r$ (Haar measure and diameter scale identically under dilation) and both are rational. Explicit values, with arithmetic:

- $p = 2$: $\kappa_2 = 1 - \frac{1}{4} = \frac{3}{4} = 0.75$; $\kappa'_2 = \frac{3}{8} = 0.375$.
- $p = 3$: $\kappa_3 = 1 - \frac{1}{9} = \frac{8}{9} \approx 0.888889$; $\kappa'_3 = \frac{4}{9} \approx 0.444444$.
- $p = 5$: $\kappa_5 = 1 - \frac{1}{25} = \frac{24}{25} = 0.96$; $\kappa'_5 = \frac{12}{25} = 0.48$.
- $p = 7$: $\kappa_7 = 1 - \frac{1}{49} = \frac{48}{49} \approx 0.979592$; $\kappa'_7 = \frac{24}{49} \approx 0.489796$.
- $p = 11$: $\kappa_{11} = 1 - \frac{1}{121} = \frac{120}{121} \approx 0.991736$; $\kappa'_{11} = \frac{60}{121} \approx 0.495868$.

**Step 5: comparison with the corpus conjecture $\pi_p = (p-1)/p$.** The Harmonic Paradigm audit states $\pi_p = (p-1)/p$ at each prime [9]. Compare term by term with $\kappa_p = \frac{(p-1)(p+1)}{p^2}$:

$$\kappa_p - \frac{p-1}{p} = \frac{(p-1)(p+1)}{p^2} - \frac{p(p-1)}{p^2} = \frac{(p-1)\bigl((p+1) - p\bigr)}{p^2} = \frac{p-1}{p^2}.$$

This difference is strictly positive for every prime $p$ and tends to $0$ only as $p \to \infty$. The ratio is

$$\frac{\kappa_p}{(p-1)/p} = \frac{(p-1)(p+1)/p^2}{(p-1)/p} = \frac{p+1}{p} = 1 + \frac{1}{p}.$$

Explicit values, with arithmetic:

- $p = 2$: $(p-1)/p = \frac{1}{2} = 0.5$; $\kappa_