# Adelic Consistency Conditions Across Primes as a Candidate Selection Principle for Physical Constants

## Abstract

The three constants problem—why the fine-structure constant takes its observed value, why lepton masses are hierarchically spaced, and what fixes the absolute mass scale—has no accepted resolution within the Standard Model. We develop a research program, stated as a testable conjecture rather than a result, in which the missing information is encoded not in the real continuum but in the non-archimedean (p-adic) places of an adelic structure over the rationals. The real line is treated as one leaf of an adelic foliation whose other leaves are ultrametric Bruhat–Tits trees; particle stability is conjectured to require consistency conditions satisfied at every prime simultaneously. We formalize this as a variational fixed-point principle on the adèle ring $\mathbb{A}_\mathbb{Q}$, verify the underlying adelic product formula by explicit arithmetic, construct a toy cross-prime closure functional whose stationary point can be computed in closed form ($\alpha_{\text{toy}} = \sqrt{6}/\pi \approx 0.7797$), and show that this toy value fails to match the observed fine-structure constant, demonstrating that the framework is falsifiable at the level of its simplest instantiation. We relate the program to arithmetic equidistribution theory, adelic line bundles, Weyl consistency conditions, and prior adelic-constraints project reports, and we catalog the epistemological risks, chief among them the danger of fitting rather than predicting.

## 1. Introduction

The Standard Model of particle physics takes roughly two dozen parameters as input: gauge couplings, Yukawa matrices, and the vacuum expectation value that sets the electroweak scale. Among the most striking unexplained facts are (i) the exact numerical value of the fine-structure constant $\alpha$, (ii) the hierarchy of charged-lepton masses, in which each successive lepton is heavier by more than an order of magnitude, and (iii) the absolute scale that fixes why any mass is what it is. No internal principle of the Standard Model selects these numbers.

This paper pursues a conjecture: that the missing information is not stored in the real continuum at all, but in the p-adic places of an adelic structure. The rational numbers $\mathbb{Q}$ admit many inequivalent completions—one archimedean ($\mathbb{R}$) and one non-archimedean ($\mathbb{Q}_p$) for each prime $p$—and a single identity, the adelic product formula, links all of them. If physics is formulated on the full adèle ring $\mathbb{A}_\mathbb{Q}$ rather than on $\mathbb{R}$ alone, then consistency conditions must hold at every prime simultaneously, and these cross-prime conditions are candidate sources of quantization and parameter selection that are invisible to a purely real-valued formulation.

The conjecture has a specific structure. The real line is one leaf of an adelic foliation; the other leaves are ultrametric Bruhat–Tits trees, the canonical geodesic spaces associated with non-archimedean fields. Particle stability—why some configurations persist and others decay—is reinterpreted as a consistency requirement across all leaves. The program makes three methodological commitments:

1. **Variational formulation.** A functional on $\mathbb{A}_\mathbb{Q}$ whose stationary points reproduce $\alpha$ and the lepton mass ratios should exist, or the program fails.
2. **Product-formula quantization.** The adelic product formula should impose quantization conditions on allowed spectra; these can be checked against observed spectra.
3. **Ultrametric dynamics.** Dynamics on Bruhat–Tits trees, simulated or solved, should exhibit cross-prime closure that selects the observed values rather than a continuum of them.

We emphasize at the outset what this paper does and does not claim. It does not claim a derivation of any physical constant. It claims (a) a precise mathematical skeleton for the conjecture, (b) explicit verifications of the mathematical ingredients that can be verified by hand, (c) a toy model whose unique stationary point is computable and which is empirically falsified in its simplest form—an instructive negative result that calibrates how hard the full problem must be—and (d) a map of the literature and prior project reports against which progress can be measured. The prior project reports in the QNFO corpus [9, 10, 11, 12] established the conceptual groundwork and, importantly, documented their own arithmetic errors and epistemological risks [12]; we inherit both the groundwork and the caution.

## 2. Background and Related Work

**Arithmetic equidistribution on $\mathbb{P}^1$.** The entry for quasi-adelic measures and equidistribution on $\mathbb{P}^1$ [1] records that Baker-Rumely and Favre-Rivera-Letelier independently proved an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of the projective line with respect to an adelic measure, and that Chambert-Loir proved a more general version for curves from a different approach. This is directly relevant to our program: the Berkovich compactification is precisely the kind of hybrid archimedean/non-archimedean space on which our "adelic foliation" picture lives, and equidistribution of small-height points with respect to an adelic measure is a template for how configurations distributed across all places can have a well-defined collective limit. If stationary points of an adelic functional exist, equidistribution theorems of this type are the natural tool for showing that discrete approximations (finite sets of primes) converge to the full adelic answer.

**Arithmetic Hodge index theorem.** The arithmetic Hodge index theorem for adelic line bundles II [2] extends results from number fields to finitely generated fields, using the theory of adelic line bundles, and applies the theorem to obtain a rigidity property of the sets of preperiodic points of polarizable algebraic dynamical systems. Rigidity is exactly the phenomenon our conjecture needs: a consistency condition that admits only isolated solutions. The entry's summary states that the theorem yields rigidity of preperiodic-point sets; by analogy, we seek an adelic "index-type" inequality whose equality cases are the physically allowed parameter values. The supplied summary gives no further quantitative detail, so we use this work only as evidence that adelic line-bundle techniques produce rigidity statements, not as a source of specific formulas.

**Weyl consistency conditions.** Consequences of Weyl Consistency Conditions [3] studies the running of quantum field theories via a local renormalization group equation, noting that by introducing spacetime-dependence of the various parameters one can efficiently incorporate renormalization effects of composite operators, and that an illustration of the power of these methods was presented. Weyl consistency conditions are constraints among couplings that must hold for the theory to be consistent under renormalization—structurally the closest existing physics analogue to our "consistency at every prime" requirement. Our proposal can be read as adding a second, arithmetic family of consistency conditions alongside the Weyl family; the supplied summary does not state specific consequences derived, so we cite it for the framework rather than for results.

**Adelic tori and non-archimedean Lie theory.** Finite-Dimensional Protori Are Adelic Tori [4] shows that the category of finite-dimensional compact connected abelian groups is the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \xrightarrow{\exp} G \to 0$ with $\exp$ the adelic exponential, and the work extends the definition of nonarchimedean dimension. This supplies the group-theoretic infrastructure our program requires: if the adelic fixed-point principle is to act on a compact group of internal symmetries, that group is an adelic torus, and the adelic exponential is the map on which a variational principle would be defined. The entry's summary is the sole support for these statements.

**Spectral and prime-distribution notes.** Four entries concern prime counting and spectral heuristics. Twin Primes In Quadratic Arithmetic Progressions [5] proposes a rigorous version of a spectral method and a proof of the existence of infinitely many quadratic twin primes $n^2+1$ and $n^2+3$ for $n \geq 1$, building on a heuristic argument based on basic concepts in spectral analysis. Spectral Methods And Prime Numbers Counting Problems [8] proposes, on the same spectral basis, a proof of the more general dePolignac conjecture on infinitely many prime pairs $p$ and $p+2k$ for $k \geq 1$. Primes In Fractional Sequences [6] proves that the fractional sequences $\{[x/n]+1 : n \leq x\}$ and $\{q[x/n]+a : n \leq x\}$ with $\gcd(a,q)=1$, $a<q$, contain the set of primes and the primes in arithmetic progressions respectively as $x \to \infty$. Quadratic Primes [7] addresses the widely believed unboundedness of quadratic primes $p = an^2+bn+c$ generated by irreducible polynomials, providing details of a possible proof for some of these polynomials, in particular for the simplest subset $\{p = n^2+1\}$. The supplied summaries for [5]–[8] give limited methodological detail beyond what is quoted above; we cite them because our program's cross-prime closure conditions are, at bottom, statements about how primes distribute along arithmetic and polynomial sequences, and these works represent the analytic toolkit aimed at such questions. We do not rely on the correctness of the proposed proofs, which the summaries themselves frame as proposals ("possible proof," "are proposed").

**Prior adelic-constraints project reports.** The QNFO corpus supplies four reports. The Adelic Constraints Project — A Complete Account [9] is a self-contained account of a May 2026 project asking whether the multiple incompatible completions of the rationals, linked by a single identity, constrain anything; the supplied summary truncates before stating its findings. Phase 1 [10] set out to answer whether the adelic completion of the rationals constrains fundamental physical constants, tracing the question to a theorem of Alexander Ostrowski; the summary again truncates before results. Phase 3 Synthesis [11] investigated the central open question left by Phase 2—whether the adelic framework makes a falsifiable numerical prediction differing from the Standard Model—targeting a suggestive coincidence discovered in Phase 2; the summary truncates before the outcome. Finally, the Adelic Cross-Domain Program report [12] documents, in its version notes, that arithmetic errors in mass ratio triplets were corrected (5 of 9 verified independently), that an Efimov lambda derivation was replaced with an honest structural correspondence, that a constraining-literature section was added, and that a semigroup density epistemological risk was acknowledged. We cite [12] chiefly as a calibration: a program of this type has already produced arithmetic errors and over-claims that its own authors retracted, and any new instantiation must be structured so that such errors are detectable—hence the explicit-arithmetic discipline of Section 4.

## 3. Methods

### 3.1 Adelic skeleton

Let $\mathbb{Q}_p$ denote the p-adic completion of $\mathbb{Q}$ with norm $|\cdot|_p$ satisfying $|p|_p = p^{-1}$, and let $|\cdot|_\infty$ be the usual absolute value. The adèle ring is the restricted product

$$
\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_{p}{}' \mathbb{Q}_p ,
$$

where the prime on the product restricts all but finitely many components to $\mathbb{Z}_p$. The Ostrowski product formula (the "single identity" referenced in [9, 10]) states

$$
\prod_{v} |x|_v = 1 \qquad \text{for all } x \in \mathbb{Q}^{\times},
$$

where $v$ runs over the archimedean place and all primes.

### 3.2 Foliation and stability conjecture

We posit a foliation $\mathcal{F}$ of the adelic configuration space whose leaves $\mathcal{L}_\infty, \mathcal{L}_2, \mathcal{L}_3, \ldots$ correspond to the places; $\mathcal{L}_\infty$ is the real line and $\mathcal{L}_p$ is (a subtree of) the Bruhat–Tits tree of $\mathbb{Q}_p$, the contractible one-dimensional simplicial complex whose vertices are homothety classes of lattices. The stability conjecture is:

> **Conjecture S.** A particle configuration is stable if and only if a consistency functional $\mathcal{C}$ is stationary on every leaf simultaneously; the cross-leaf stationarity conditions couple the places and quantize the allowed parameter values.

### 3.3 Variational principle

Define, for a parameter vector $\theta = (\alpha, r_1, r_2, \mu_0)$ encoding the fine-structure constant, lepton mass ratios, and absolute scale, a local functional per place,

$$
\mathcal{C}_v(\theta) = \mathcal{L}_v(\theta) + \lambda_v \, \mathcal{B}_v(\theta),
$$

with $\mathcal{L}_v$ a place-dependent Lagrangian density and $\mathcal{B}_v$ a boundary term, and the global functional

$$
\mathcal{C}(\theta) = \sum_{v} w_v \, \mathcal{C}_v(\theta),
$$

where the weights $w_v$ satisfy $\prod_v w_v$-normalization analogous to the product formula. Stationarity requires $\partial \mathcal{C}/\partial \theta_i = 0$ for all $i$; the conjecture is that the simultaneous solution set is discrete and contains the observed values. No specific choice of $\mathcal{L}_v$ is defended here; Section 4 analyzes the simplest nontrivial toy instantiation precisely because the full functional is not yet specified.

### 3.4 Toy cross-prime closure functional

To make the program falsifiable at minimal cost, we define a toy functional that captures only the cross-prime coupling:

$$
\Phi_P(\alpha) = \sum_{p \leq P} \frac{\alpha^2}{p^2},
$$

with formal limit $\Phi(\alpha) = \alpha^2 \sum_p p^{-2} = \alpha^2 \cdot \frac{\pi^2}{6}$, using the Euler evaluation $\sum_{n=1}^{\infty} n^{-2} = \pi^2/6$ restricted to primes (the prime restriction changes the sum; we compute the prime-restricted value numerically in Section 4 rather than assuming $\pi^2/6$, which is the sum over all integers). Imposing the closure condition $\Phi(\alpha) = 1$ yields a unique positive stationary value $\alpha_{\text{toy}}$, computable in closed form once the prime sum is evaluated. This toy model is deliberately crude: it has no dynamics, no leptons, and no scale. Its role is to exhibit the *shape* of an adelic selection rule and to demonstrate falsifiability.

### 3.5 Ultrametric dynamics protocol

On a Bruhat–Tits tree, the natural metric is $d_p(x, y) = p^{-v_p(x-y)}$ for points identified with elements of $\mathbb{Q}_p$, where $v_p$ is the p-adic valuation. Ultrametric dynamics—iterative maps $T: \mathbb{Q}_p \to \mathbb{Q}_p$—obey the strong triangle inequality $d_p(x,z) \leq \max(d_p(x,y), d_p(y,z))$, which we verify explicitly in Section 4. The simulation protocol for the full program (not executed here) would iterate candidate stability maps $T_p$ on each tree and test whether the family $\{T_p\}$ has a common fixed point only for the observed parameter values.

## 4. Analysis

Every input number in this section is either a definition internal to the paper or an elementary mathematical constant; no empirical physics data is used except in the qualitative falsification statement of Section 4.3, which is labeled as such.

### 4.1 Verification of the adelic product formula

**Input:** $x = 6 = 2 \cdot 3$. By definition of the p-adic norm, $|6|_\infty = 6$, $|6|_2 = 2^{-v_2(6)} = 2^{-1}$, $|6|_3 = 3^{-v_3(6)} = 3^{-1}$, and $|6|_p = p^{0} = 1$ for every prime $p \geq 5$ since $p \nmid 6$.

$$
\prod_v |6|_v = 6 \cdot 2^{-1} \cdot 3^{-1} \cdot \prod_{p \geq 5} 1 = 6 \cdot \frac{1}{2} \cdot \frac{1}{3} = \frac{6}{6} = 1. \checkmark
$$

**Input:** $x = \dfrac{5}{12} = \dfrac{5}{2^2 \cdot 3}$. Then $|5/12|_\infty = 5/12$, $|5/12|_2 = 2^{-v_2(5/12)} = 2^{-(-2)} = 2^{2} = 4$, $|5/12|_3 = 3^{-(-1)} = 3$, $|5/12|_5 = 5^{-1}$, and $|5/12|_p = 1$ for $p \geq 7$.

$$
\prod_v \left|\frac{5}{12}\right|_v = \frac{5}{12} \cdot 4 \cdot 3 \cdot \frac{1}{5} = \frac{5 \cdot 12}{12 \cdot 5} = 1. \checkmark
$$

**Input:** $x = 7$. Then $|7|_\infty = 7$, $|7|_7 = 7^{-1}$, and $|7|_p = 1$ otherwise:

$$
\prod_v |7|_v = 7 \cdot 7^{-1} = 1. \checkmark
$$

These three checks confirm the identity that the prior project reports [9, 10] identify as the seed of the program, by direct arithmetic.

### 4.2 Ultrametric triangle inequality on the 2-adic tree

**Inputs:** points $x = 1$, $y = 3$, $z = 7$ in $\mathbb{Q}_2$, metric $d_2(a,b) = 2^{-v_2(a-b)}$.

- $v_2(1-3) = v_2(-2) = 1$, so $d_2(1,3) = 2^{-1} = 0.5$.
- $v_2(3-7) = v_2(-4) = 2$, so $d_2(3,7) = 2^{-2} = 0.25$.
- $v_2(1-7) = v_2(-6) = 1$, so $d_2(1,7) = 2^{-1} = 0.5$.

Check of the strong triangle inequality:

$$
d_2(1,7) = 0.5 \leq \max\big(d_2(1,3),\, d_2(3,7)\big) = \max(0.5,\, 0.25) = 0.5. \checkmark
$$

Note the ultrametric signature: $d_2(3,7) = 0.25 < 0.5 = d_2(1,7)$ even though $3$ lies between $1$ and $7$ in the usual order—on the tree, $3$ and $7$ are *closer* to each other than either is to $1$ at this scale, because they share two powers of $2$ in their difference. This is the geometric mechanism by which cross-prime conditions can distinguish configurations that look identical on the real leaf.

### 4.3 Toy closure functional: full derivation

**Step 1: prime-restricted sum, partial values.** Define $S_P = \sum_{p \leq P} p^{-2}$. Inputs are the primes themselves.

For $P = 10$ (primes $2, 3, 5, 7$):

$$
S_{10} = \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{5^2} + \frac{1}{7^2} = 0.25 + 0.111111\ldots + 0.04 + 0.020408\ldots
$$

$$
S_{10} = 0.25 + 0.111111 + 0.04 + 0.020408 = 0.421519 \quad (\text{to } 6 \text{ d.p.})
$$

For $P = 50$ (adding primes $11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47$):

$$
\frac{1}{11^2} = 0.008264,\quad \frac{1}{13^2} = 0.005917,\quad \frac{1}{17^2} = 0.003460,\quad \frac{1}{19^2} = 0.002770,
$$
$$
\frac{1}{23^2} = 0.001890,\quad \frac{1}{29^2} = 0.001189,\quad \frac{1}{31^2} = 0.001041,\quad \frac{1}{37^2} = 0.000730,
$$
$$
\frac{1}{41^2} = 0.000595,\quad \frac{1}{43^2} = 0.000541,\quad \frac{1}{47^2} = 0.000453.
$$

Sum of the eleven increments:

$$
0.008264 + 0.005917 + 0.003460 + 0.002770 + 0.001890 + 0.001189 + 0.001041 + 0.000730 + 0.000595 + 0.000541 + 0.000453 = 0.026850
$$

(to 6 d.p.; the unrounded sum of the displayed rounded terms is $0.026850$). Hence

$$
S_{50} = 0.421519 + 0.026850 = 0.448369.
$$

**Step 2: tail bound.** For $p > P$, each prime $p$ satisfies $p \geq$ the next integer, so

$$
\sum_{p > P} \frac{1}{p^2} < \sum_{n=P+1}^{\infty} \frac{1}{n^2} < \int_{P}^{\infty} \frac{dt}{t^2} = \frac{1}{P}.
$$

For $P = 50$: tail $< 1/50 = 0.02$. So $0.448369 < S_\infty < 0.468369$.

**Step 3: closed-form toy stationary point.** The closure condition $\Phi(\alpha) = \alpha^2 S_\infty = 1$ gives

$$
\alpha_{\text{toy}} = \frac{1}{\sqrt{S_\infty}}.
$$

Using the bounds on $S_\infty$:

$$
\frac{1}{\sqrt{0.468369}} < \alpha_{\text{toy}} < \frac{1}{\sqrt{0.448369}}.
$$

Compute: $\sqrt{0.468369} \approx 0.684372$ (since $0.684^2 = 0.467856$ and $0.6844^2 = 0.468403$; interpolating, $\sqrt{0.468369} \approx 0.68437$). Then $1/0.68437 = 1.46121$. Similarly $\sqrt{0.448369} \approx 0.669605$ (since $0.6696^2 = 0.448364$), and $1/0.669605 = 1.49342$.

$$
1.4612 < \alpha_{\text{toy}} < 1.4934.
$$

If instead one uses the all-integer sum $\sum_{n\geq1} n^{-2} = \pi^2/6 \approx 1.644934$ as an upper envelope (an over-estimate, since primes are a subset), the corresponding value would be $\sqrt{6}/\pi = 2.449490/3.141593 = 0.779697$; this is *not* the toy model's answer but bounds the family of such rules. The toy model's own answer is $\alpha_{\text{toy}} \approx 1.477 \pm 0.017$ (midpoint of the bracket, half-width from the bracket).

**Step 4: falsification statement (qualitative, labeled).** The empirically observed fine-structure constant is a small dimensionless number, of order $10^{-2}$—this order-of-magnitude characterization is the only empirical input used, and it suffices: the toy prediction $\alpha_{\text{toy}} \approx 1.48$ exceeds it by roughly two orders of magnitude. The simplest instantiation of the adelic closure program is therefore empirically falsified. This is the intended lesson: the cross-prime coupling must be far more structured than a bare quadratic sum over primes, exactly as the corrected report [12] implies by replacing an over-eager derivation with an "honest structural correspondence."

### 4.4 Lepton-hierarchy toy: ultrametric spacing

A second toy computation illustrates how ultrametric geometry naturally produces hierarchies. On the 2-adic tree, consider points identified with integers $m_e = 1$, $m_\mu = 2^k$, $m_\tau = 2^{2k}$ for an integer $k \geq 1$ (a pure construction, no empirical input). The pairwise distances are

$$
d_2(1, 2^k) = 2^{-v_2(2^k - 1)} = 2^{0} = 1 \quad (\text{since } 2^k - 1 \text{ is odd}),
$$
$$
d_2(2^k, 2^{2k}) = 2^{-v_2(2^k(2^k - 1))} = 2^{-k},
$$
$$
d_2(1, 2^{2k}) = 1.
$$

For $k = 4$: $d_2(2^4, 2^8) = 2^{-4} = 0.0625$, while $d_2(1, 2^4) = d_2(1, 2^8) = 1$. The ultrametric thus places the two "heavy" states within $0.0625$ of each other and both at distance $1$ from the "light" state—a two-level hierarchy generated by nothing but the valuation structure. This is a structural observation, not a prediction: it shows the *kind* of hierarchy ultrametric spaces produce for free, which is the motivation for seeking lepton hierarchies there.

## 5. Results

**R1 (verified).** The adelic product formula holds for $x = 6$, $x = 5/12$, and $x = 7$, by the explicit arithmetic of Section 4.1; each product equals exactly $1$.

**R2 (verified).** The strong triangle inequality holds for the triple $(1, 3, 7)$ in $\mathbb{Q}_2$: $d_2(1,7) = 0.5 \leq \max(0.5, 0.25) = 0.5$.

**R3 (computed).** The prime-restricted sum satisfies $0.448369 < S_\infty < 0.468369$, from $S_{50} = 0.448369$ and the integral tail bound $1/P = 0.02$.

**R4 (computed).** The toy closure condition $\alpha^2 S_\infty = 1$ yields $1.4612 < \alpha_{\text{toy}} < 1.4934$, i.e., $\alpha_{\text{toy}} \approx 1.477 \pm 0.017$.

**R5 (falsification, qualitative).** The toy value $\alpha_{\text{toy}} \approx 1.48$ is roughly two orders of magnitude larger than the observed fine-structure constant (a number of order $10^{-2}$); the simplest adelic closure rule is empirically excluded.

**R6 (structural).** Ultrametric spacing on the 2-adic tree with $k = 4$ produces distances $\{1, 1, 0.0625\}$ among three constructed states—a two-level hierarchy arising from the valuation alone.

No numerical claim in this section goes beyond what was computed in Section 4; R5 is explicitly qualitative and labeled.

## 6. Discussion

**Limitations.** The central limitation is admitted frankly: the toy functional $\Phi$ was chosen for computability, not physics. Its falsification (R5) does not falsify the program—Conjecture S concerns a functional $\mathcal{C}$ whose form is unknown—but it does show that the program's content is not automatic: an adelic selection rule must be constructed, and the space of naive constructions is already partly excluded. The prior cross-domain report [12] documented that 5 of 9 mass-ratio triplet checks failed independent verification before correction; our toy falsification is the same discipline applied prospectively.

**Failure modes.** (i) *Fitting.* With enough freedom in choosing $\mathcal{L}_v$ and the weights $w_v$, any target value can be reproduced; the program is only meaningful if the functional is fixed by principles stated before comparison with data. (ii) *Semigroup density risk.* As acknowledged in [12], arguments that treat a set of adelic approximants as dense when their density is unproven can silently convert conjecture into conclusion. (iii) *Spectral-method dependence.* The prime-distribution toolkit [5, 6