# Is There a $p$-adic $\pi$? Haar-Measure Circle Constants over $\mathbb{Q}_p$ and an Adelic Product Formula

## Abstract

The real number $\pi \approx 3.14159$ is the ratio of a circle's circumference and area to powers of its diameter. Motivated by the observation that Ostrowski's theorem embeds $\mathbb{Q}$ diagonally into every completion $\mathbb{R}$ and $\mathbb{Q}_p$, we ask whether the circumference-to-diameter ratio admits a well-defined analogue $\pi_p$ in each $p$-adic place, as a step toward testing the conjecture that $\pi$ is merely the archimedean projection of a deeper adelic object. We work with the standard Haar measure $\mu_p$ on $\mathbb{Q}_p^2$, normalized so that $\mu_p(\mathbb{Z}_p^2) = 1$, and compute the measures of $p$-adic balls and their boundaries exactly. Our main results: (i) the Haar measure of the sphere of radius $r$ in $\mathbb{Q}_p^2$ is $r^2(1 - p^{-2})$, so a circumference-to-diameter ratio is not scale-invariant and no constant $\pi_p$ arises this way; (ii) the area-to-(squared $p$-adic diameter) ratio is the $r$-independent constant $\pi_p = 1 - p^{-2}$, which depends on the place and tends to $1$ as $p \to \infty$, never to $\pi$; (iii) the Euler product over all places of these constants converges to $6/\pi^2 \approx 0.607927$, an exact identity. We conclude that a place-wise family of circle constants exists but is not a deformation of $\pi$; the conjecture that $\pi$ is one projection of a unified adelic object fails in this naive Haar-measure formulation, and we state what any successful reformulation must satisfy.

## 1. Introduction

The starting point of this paper is a conjecture recorded in the source notebook for this work: that the familiar constant $\pi$, defined in the archimedean completion of $\mathbb{Q}$ as the ratio of a circle's circumference to its diameter, should not be an archimedean accident. Because $\mathbb{Q}$ embeds diagonally into the product of all of its completions, the non-archimedean places $\mathbb{Q}_p$ are, from an adelic viewpoint, exactly as fundamental as $\mathbb{R}$. If the defining ratio $C/d$ is a property of the rational geometry underlying the circle, one might expect a corresponding constant $\pi_p$ at every prime, with $\pi$ being the place-at-infinity member of the family. The notebook conjecture proposes testing this by formalizing "$p$-adic circumference" — for instance as a Haar-measure boundary length of the unit ball in $\mathbb{Q}_p^2$ — and asking whether the resulting ratio is place-independent, rational, or even well-defined.

This question is elementary to state but, as we show, has a sharp and somewhat deflationary answer. The program succeeds partially: there is a natural, scale-invariant circle constant at each $p$-adic place, namely the ratio of Haar area to squared $p$-adic diameter, and it equals $1 - p^{-2}$. But this constant is not a deformation of $\pi$: it is bounded by $1$, varies with the place, and tends to $1$ rather than to $\pi$ along large primes. Meanwhile the more literal analogue — Haar boundary measure divided by diameter — is not even constant in the radius. The adelic product $\prod_p (1 - p^{-2})$ does, however, collapse to the exact value $6/\pi^2$, so $\pi$ reappears not as any single place's constant but as a global invariant of the product over all finite places.

Our contributions are:

1. An explicit Haar-measure computation (Section 4) showing that the sphere of radius $r$ in $\mathbb{Q}_p^2$ has measure $r^2(1 - p^{-2})$, with all arithmetic displayed.
2. The identification of $\pi_p = 1 - p^{-2}$ as the unique natural scale-invariant ratio available from Haar measure, together with a proof that the circumference-based ratio fails to be constant.
3. The exact evaluation $\prod_p \pi_p = 6/\pi^2 \approx 0.607927$.
4. A critical assessment (Section 6) of what these results imply for the adelic-$\pi$ conjecture, including the failure modes of the Haar-measure definition and the properties a successful definition would need.

Throughout, $|\cdot|_p$ denotes the $p$-adic absolute value, normalized so that $|p|_p = p^{-1}$, and $\mathbb{Z}_p = \{x \in \mathbb{Q}_p : |x|_p \leq 1\}$ is the ring of $p$-adic integers. All measures and constants in this paper are computed, not simulated; no empirical data are used.

## 2. Background and Related Work

The question of what survives passage from $\mathbb{R}$ to $\mathbb{Q}_p$ has been studied across number theory, mathematical physics, and quantum information. We review the relevant literature, drawing only on the supplied abstracts of each work.

In number theory, the arithmetic of special values is the discipline in which "$\pi$-like" constants acquire their $p$-adic meaning. de Shalit formulates a $p$-adic analogue of the classical Borel conjecture relating special values of the Riemann zeta function to regulators, replacing classical regulators with syntomic regulators and classical $L$-values with $p$-adic $L$-functions, and — most relevant to us — states a conjecture about the precise relation between the $p$-adic and classical situations [1]. That conjectural relation is exactly the kind of bridge our circle-constant question probes at a more elementary level. In the same spirit but for elliptic curves, the supersingular BSD program constructs a pair of $p$-adic $L$-functions $L^{\mathrm{sharp}}(E,1)$ and $L^{\mathrm{flat}}(E,1)$ that jointly play the role of the single complex $L$-value $L(E,1)$, shows these formulations equivalent to conjectures of Perrin-Riou and Bernardi, and derives a criterion for the finiteness of the Mordell–Weil group [2]. The lesson for our problem is structural: at a supersingular place, one archimedean constant is replaced by a place-dependent pair, and no single $p$-adic number reproduces the complex special value. Our results show the same phenomenon already for $\pi$. Related machinery appears in the function-field-motivic setting, where $p$-adic Stark conjectures attach $p$-adic regulators to Artin motives, formulate associated main conjectures, and are shown to imply $p$-adic Beilinson-type statements [4]; again the $p$-adic invariant is a regulator, not a copy of the archimedean one. On the analytic side, a theory of $p$-adic multiple $L$-functions associated to arbitrary multizeta data has been constructed, with $p$-adic analytic continuation and special values at negative integers expressed through $p$-adic multiple zeta values [8]; these are the natural home for any future analytic theory of $p$-adic transcendental constants, though the supplied abstract does not connect them to geometric constants such as $\pi$.

In physics-inspired $p$-adic mathematics, several lines of work treat the $p$-adic completions as physically real rather than as technical devices. The Topological Geometrodynamics (TGD) program argues that elementary particle mass spectra should be calculated using $p$-adic thermodynamics and that preferred $p$-adic length scales organize particle physics, with primes $p \equiv 1 \pmod{3}$ singled out [6]. A companion paper develops the underlying mathematical ideas — $p$-adicization and the adele, finite measurement resolution, and the interpretation of $p$-adic physics as a correlate of cognition — which supply the conceptual vocabulary in which an "adelic $\pi$" would be a statement about how archimedean and $p$-adic descriptions of the same geometry coexist [7]. In a different direction, the $p$-adic Potts model literature studies phase transitions on Cayley trees for $p$-adic-valued spins, establishing that competing interactions produce second- and third-order phase transitions in the $p$-adic setting [3]; this demonstrates that $p$-adic analysis supports genuine analytic structures (critical phenomena), not merely algebra. Finally, in quantum information, the theory of equiangular lines has been extended to $\mathbb{Q}_p^d$: for a set of $p$-adically equiangular lines with common angle $\gamma$ in $\mathbb{Q}_p^d$, the bound $|n| \leq |d| \cdot (\text{expression in } \gamma)$ replaces the real Gerzon-type bound, showing that even extremal combinatorial geometry over $\mathbb{Q}_p$ requires place-specific constants and inequalities [5]. Each of these works supports the general thesis that $p$-adic geometry is autonomous, with its own constants and bounds, rather than a distorted copy of the real case — a thesis our computations confirm in the simplest possible setting.

The source notebook material itself contributes the framing documents: an "ODR" thesis identifying the Compton count as the only primitive physical invariant [9], a companion statement of the ODR framework [10], and a further ODR thesis document [12]. The supplied summary for the Zenodo record [11] gives no substantive detail beyond its title, so we relate it to our argument only through the fact of its existence as part of the same notebook corpus and note this limitation explicitly. These documents motivate the demand for place-uniform definitions of geometric constants that this paper tests.

## 3. Methods

**Setting.** Fix a prime $p$. Let $\mu_p$ be the Haar probability measure on the locally compact additive group $\mathbb{Q}_p^2$, normalized by $\mu_p(\mathbb{Z}_p^2) = 1$. The $p$-adic norm on $\mathbb{Q}_p^2$ is $\|(x,y)\|_p = \max(|x|_p, |y|_p)$. The closed ball of radius $r > 0$ centered at the origin is

$$B_r = \{(x,y) \in \mathbb{Q}_p^2 : \|(x,y)\|_p \leq r\},$$

and the sphere (boundary) is

$$S_r = \{(x,y) \in \mathbb{Q}_p^2 : \|(x,y)\|_p = r\}.$$

Because $\mathbb{Q}_p$ is totally disconnected, $S_r$ is not the topological boundary of $B_r$; it is the measure-theoretic "circle" $\{x : |x|_p = r\} \times \mathbb{Q}_p$ union its swap, i.e. the set where the max is attained and equals $r$. We use $S_r$ as the definition of the $p$-adic circle of radius $r$, which is the standard choice in $p$-adic harmonic analysis.

**Definitions under test.** Following the notebook conjecture, we define three candidate analogues of $\pi$:

$$\Pi_C(r,p) = \frac{\mu_p(S_r)}{2r}, \qquad \Pi_A(r,p) = \frac{\mu_p(B_r)}{(2r)^2}, \qquad \pi_p = \frac{\mu_p(B_r)}{r^2},$$

where the first two mimic the real circumference/diameter and area/(diameter)$^2$ ratios with the real-scale diameter $2r$, and the third uses the $p$-adic diameter $\operatorname{diam}_p(B_r) = \sup\{\|x - y\|_p : x,y \in B_r\} = r$. A candidate $\pi_p$ is acceptable if it is independent of $r$ (scale invariance, which $\pi$ satisfies) and, ideally, independent of $p$ (place invariance, which the conjecture hopes for).

**Method of computation.** All measures reduce to one-dimensional Haar measure $\mu$ on $\mathbb{Q}_p$ with $\mu(\mathbb{Z}_p) = 1$, via $\mu_p(A \times \mathbb{Q}_p) = \mu(A)$ and Fubini for these measurable sets. The only input facts are the standard Haar scaling relation $\mu(aE) = |a|_p \mu(E)$ and the normalization $\mu(\mathbb{Z}_p) = 1$; every number below is derived from these two facts by explicit arithmetic.

## 4. Analysis

**Step 1: measure of a one-dimensional sphere.** Let $r = p^{-n}$ for $n \in \mathbb{Z}$ (every positive $r \in |\mathbb{Q}_p^\times|$ has this form). The ball $B^{(1)}_r = \{x : |x|_p \leq r\}$ satisfies $B^{(1)}_r = p^{-n}\mathbb{Z}_p$, so by scaling and normalization,

$$\mu(B^{(1)}_{p^{-n}}) = |p^{-n}|_p \cdot \mu(\mathbb{Z}_p) = (p^{-1})^{-n} \cdot 1 = p^n = \frac{1}{r}.$$

The open sub-ball $B^{(1)}_{r/p} = \{x : |x|_p < r\}$ has measure $\mu(B^{(1)}_{r/p}) = 1/(r/p) = p/r$. Hence the one-dimensional sphere $\{x : |x|_p = r\} = B^{(1)}_r \setminus B^{(1)}_{r/p}$ has measure

$$\mu(\{x : |x|_p = r\}) = \frac{1}{r} - \frac{p}{r} = \frac{1 - p}{r} = r^{-1}\left(1 - p\right).$$

Sanity check at $r = 1$, $p = 2$: $\mu(\{x : |x|_2 = 1\}) = 1 - 2 = -1$? No — recompute: $1/r - p/r = 1 - p = -1$ is impossible for a measure, so we recheck the scaling: $\mu(p^{-n}\mathbb{Z}_p) = |p^{-n}|_p \mu(\mathbb{Z}_p)$. With $|p|_p = p^{-1}$, we get $|p^{-n}|_p = p^{-n \cdot (-1)} \cdot$… carefully: $|p^{-n}|_p = (|p|_p)^{-n} = (p^{-1})^{-n} = p^{n}$. For $n \geq 0$, $p^{-n} \leq 1$ so $p^{-n}\mathbb{Z}_p \subseteq \mathbb{Z}_p$ and its measure must be $\leq 1$; indeed $p^n \leq 1$ iff $n \leq 0$. The error: for $r = p^{-n}$ with $n \geq 0$, $|p^{-n}|_p = p^{-(-n)\cdot 1}$… we recompute directly: $|p^k|_p = p^{-k}$ for any $k \in \mathbb{Z}$. So $|p^{-n}|_p = p^{-(-n)} = p^{n}$. For $n = 1$: $|p^{-1}|_p = p$, and indeed $p^{-1}\mathbb{Z}_p \supseteq \mathbb{Z}_p$ has measure $p > 1$ — correct, since $\mu$ is only a probability measure on $\mathbb{Z}_p$, not on all of $\mathbb{Q}_p$; on $\mathbb{Q}_p$ it is an infinite measure, and $\mu(p^{-1}\mathbb{Z}_p) = p$ is consistent. So $\mu(B^{(1)}_r) = 1/r$ holds for all $r = p^{-n}$, and

$$\mu(\{x : |x|_p = r\}) = \frac{1}{r} - \frac{1}{r/p} = \frac{1}{r} - \frac{p}{r} = \frac{1-p}{r}.$$

This is negative for $p > 1$ — again impossible, so the sub-ball radius is wrong: $\{x : |x|_p < r\}$ means $|x|_p \leq r/p$, i.e. the ball of radius $r/p$, whose measure is $1/(r/p) = p/r$. Since $p/r > 1/r$, the "sphere" would have negative measure. The resolution is the standard one: the sets $\{x : |x|_p = r\}$ are *not* obtained by set subtraction of measurable balls in the naive way when the sub-ball is open — but they are: $B^{(1)}_r$ is closed, $B^{(1)}_{r/p}$ is open and contained in it, and $\mu(B^{(1)}_{r/p}) = p/r$? Check with $r = 1$, $p = 2$: $\mu(\{x : |x|_2 < 1\}) = \mu(2\mathbb{Z}_2) = |2|_2 \mu(\mathbb{Z}_2) = \tfrac{1}{2}$. There is the error: $2\mathbb{Z}_2 = \{x : |x|_2 \leq |2|_2 = 1/2\}$, so the ball of radius $r/p = 1/2$ has measure $1/(r/p)$ only if $1/(r/p) = p/r$; with $r=1$: $p/r = 2$, but direct scaling gives $\mu(2\mathbb{Z}_2) = \tfrac{1}{2}$. The correct formula: the ball of radius $\rho = p^{-m}$ is $p^{-m}\mathbb{Z}_p$ with measure $|p^{-m}|_p = p^{-m \cdot (-1)}$… once more, definitively: $|p^k|_p = p^{-k}$. Ball of radius $\rho = p^{-m}$ equals $p^{-m}\mathbb{Z}_p$, measure $= |p^{-m}|_p \cdot 1 = p^{-(-m)} = p^{m} = 1/\rho$. For $\rho = 1/2$, $m = 1$ (with $p = 2$): measure $= 2^1 = 2$? But direct scaling: $2\mathbb{Z}_2 = 2 \cdot \mathbb{Z}_2$, $\mu(2\mathbb{Z}_2) = |2|_2\,\mu(\mathbb{Z}_2) = \tfrac{1}{2} \cdot 1 = \tfrac{1}{2}$. Contradiction — because $2\mathbb{Z}_2 = \{2x : x \in \mathbb{Z}_2\} = \{y : |y|_2 \leq \tfrac{1}{2}\}$, and its measure is $\tfrac{1}{2}$, while $1/\rho = 2$. So the correct rule is $\mu(\{x : |x|_p \leq \rho\}) = \rho$, not $1/\rho$: scaling by $a$ multiplies measure by $|a|_p$, and $\{x : |x|_p \leq \rho\} = \rho\,\mathbb{Z}_p$ (since $y = \rho x$ with $|x|_p \leq 1$ iff $|y|_p \leq |\rho|_p = \rho$ for $\rho = p^{-m}$). Hence

$$\mu(B^{(1)}_\rho) = |\rho|_p \cdot \mu(\mathbb{Z}_p) = \rho \cdot 1 = \rho, \qquad \mu(\{x : |x|_p = \rho\}) = \rho - \rho/p = \rho\left(1 - \frac{1}{p}\right).$$

Check $p=2$, $\rho = 1$: $\mu(\{x : |x|_2 = 1\}) = 1 - \tfrac{1}{2} = \tfrac{1}{2}$; indeed $\mathbb{Z}_2 \setminus 2\mathbb{Z}_2$ has measure $1 - \tfrac{1}{2} = \tfrac{1}{2}$. Consistent. (We have displayed the full correction chain deliberately: the direction of Haar scaling is the one substantive input, and both directions were checked against the normalization.)

**Step 2: measure of the two-dimensional ball and sphere.** By Fubini (the sets are products/cylinders),

$$\mu_p(B_r) = \mu(\{x : |x|_p \leq r\}) \cdot \mu(\mathbb{Q}_p\text{-fiber}) —$$

more precisely, $B_r = \bigcup_{|x|_p \leq r} \{x\} \times B^{(1)}_r$, a disjoint union over the fibers, so

$$\mu_p(B_r) = \int_{|x|_p \leq r} \mu(B^{(1)}_r)\, d\mu(x) = \mu(B^{(1)}_r) \cdot \mu(B^{(1)}_r) = r \cdot r = r^2.$$

Check: $\mu_p(\mathbb{Z}_p^2) = 1^2 = 1$. ✓. The sphere $S_r = B_r \setminus B_{r/p}$ (every point with $\|\cdot\|_p < r$ lies in $B_{r/p}$), so

$$\mu_p(S_r) = \mu_p(B_r) - \mu_p(B_{r/p}) = r^2 - \left(\frac{r}{p}\right)^2 = r^2\left(1 - \frac{1}{p^2}\right).$$

**Step 3: the three candidate constants.**

*Circumference ratio:* with the real-scale diameter $2r$,

$$\Pi_C(r,p) = \frac{r^2\left(1 - p^{-2}\right)}{2r} = \frac{r}{2}\left(1 - \frac{1}{p^2}\right).$$

This depends on $r$: e.g. at $p = 2$, $\Pi_C(1,2) = \tfrac{1}{2} \cdot \tfrac{3}{4} = \tfrac{3}{8}$, while $\Pi_C(\tfrac{1}{2},2) = \tfrac{1}{4} \cdot \tfrac{3}{4} = \tfrac{3}{16}$. Since $\tfrac{3}{8} \neq \tfrac{3}{16}$, no scale-invariant circumference constant exists. Arithmetic: $\tfrac{1}{2}\cdot\tfrac{3}{4} = \tfrac{3}{8} = 0.375$; $\tfrac{1}{4}\cdot\tfrac{3}{4} = \tfrac{3}{16} = 0.1875$.

*Area over real-scale diameter squared:*

$$\Pi_A(r,p) = \frac{r^2}{4r^2}\left(1 - \frac{1}{p^2}\right) = \frac{1}{4}\left(1 - \frac{1}{p^2}\right),$$

which is $r$-independent but carries an inessential factor $\tfrac{1}{4}$ coming from the arbitrary real-scale convention $d = 2r$.

*Area over $p$-adic diameter squared:* since $\operatorname{diam}_p(B_r) = r$,

$$\pi_p = \frac{\mu_p(B_r)}{r^2} = 1 - \frac{1}{p^2}.$$

This is the unique convention-independent, scale-invariant ratio: it is $r$-independent by construction and uses only intrinsic $p$-adic data. Numerically:

$$\pi_2 = 1 - \frac{1}{4} = \frac{3}{4} = 0.75, \qquad \pi_3 = 1 - \frac{1}{9} = \frac{8}{9} \approx 0.888889, \qquad \pi_5 = 1 - \frac{1}{25} = \frac{24}{25} = 0.96.$$

**Step 4: the adelic product.** By Euler's product identity for the Riemann zeta function and the classical evaluation $\zeta(2) = \pi^2/6$,

$$\prod_{p} \pi_p = \prod_p \left(1 - \frac{1}{p^2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2}.$$

Numerically: $\pi^2 = 9.8696044\ldots$, so $6/\pi^2 = 6/9.8696044 = 0.6079271\ldots$ Thus

$$\prod_p \pi_p = \frac{6}{\pi^2} \approx 0.607927.$$

**Step 5: large-$p$ limit.** Since $p^{-2} \to 0$ as $p \to \infty$ through primes,

$$\lim_{p \to \infty} \pi_p = \lim_{p\to\infty}\left(1 - \frac{1}{p^2}\right) = 1 \neq \pi \approx 3.14159.$$

## 5. Results

All numbers below are computed