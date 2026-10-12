# Automorphisms and Scaling Transformations: A Re-Entry Analysis Across Algebraic, Geometric, and Dynamical Settings

## Abstract

We examine the relationship between automorphisms — structure-preserving self-maps of algebraic, geometric, or dynamical objects — and scaling transformations, i.e., dilations that rescale coordinates or metrics without changing the underlying structure type. Motivated by a re-entry prompt asking whether automorphisms "relate to scaling transformations," we organize eight recent arXiv works on automorphisms of varieties, calibrations, parabolic geometries, free-product splittings, curves, symplectic manifolds, and holomorphic dynamics into a common framework in which every automorphism is tested against a distinguished class of dilations. We introduce a conjugation test: a scaling transformation $S$ relates to an automorphism $\phi$ if $S$ normalizes, centralizes, or rescales parameters of $\phi$. We give explicit derivations: conjugation of a unipotent planar automorphism by the diagonal dilation $D=\mathrm{diag}(2,3)$ rescales its shear coefficient by the ratio $\lambda_1/\lambda_2 = 2/3$; scalar dilations act trivially on rotations and unipotents alike; and in the Cayley-Dickson tower the count of associative quaternion rings grows from $7$ (octonions) to $35$ (sedenions), a factor of $5$, corresponding to $\log_2 5 \approx 2.32$ bits per dimension-doubling step. We conclude that scaling relates to automorphisms through conjugation action on parameter spaces, not through new automorphisms per se.

## 1. Introduction

An automorphism of a mathematical object $X$ is an isomorphism from $X$ to itself; the set of all automorphisms forms a group $\mathrm{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S_\lambda$ that rescales a chosen coordinate, metric, or norm by a factor $\lambda$. The question posed in the re-entry prompt — whether automorphisms "relate to scaling transformations" — is deliberately open: it does not specify the category (algebraic varieties, non-associative algebras, parabolic geometries, groups, dynamical systems), and the answer plausibly differs across categories.

This paper treats the question as a comparative-structural one. Rather than proving a single theorem, we construct a uniform lens — the **conjugation test** — and apply it to a body of recent literature on automorphisms, all of it supplied to us as a fixed bibliography. The lens asks three questions of each setting:

1. **Normalization:** does a dilation $S$ send automorphisms to automorphisms, i.e., does $S\,\mathrm{Aut}(X)\,S^{-1} \subseteq \mathrm{Aut}(X)$?
2. **Centralization:** does $S$ commute with some or all automorphisms, i.e., is $S\phi = \phi S$?
3. **Parameter rescaling:** when automorphisms come in families indexed by numerical parameters (shear coefficients, rotation angles, orders), does conjugation by $S$ act on those parameters by a computable rule?

The third question is where scaling becomes visible and quantitative. We show by explicit computation that conjugation by an anisotropic dilation $D=\mathrm{diag}(2,3)$ rescales the shear coefficient of the planar unipotent map $\phi(x,y)=(x+y,\,y)$ by exactly $2/3$, while scalar dilations act trivially on both unipotents and rotations. We also quantify the growth of associative structure in the Cayley-Dickson tower, where the supplied literature reports $7$ quaternion rings for octonions and $35$ for sedenions.

Our contributions are: (i) a uniform three-part framework for relating automorphisms to scalings; (ii) explicit arithmetic derivations of conjugation effects and growth ratios; (iii) a structured reading of eight arXiv works, each discussed strictly within what its supplied abstract states; and (iv) an honest account of the limits of this exercise, including the fact that four supplied corpus entries (the QNFO items) carry no abstract content and can be used only as pointers.

The paper is organized as follows. Section 2 reviews the supplied literature. Section 3 formalizes the conjugation test. Section 4 carries out the derivations with all arithmetic shown. Section 5 reports results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

We discuss the eight arXiv works in the supplied bibliography, in its numbering, followed by the four QNFO corpus entries. Throughout, we restrict ourselves to what each supplied abstract states; where an abstract is truncated or absent, we say so.

**[1] Birational automorphism groups of projective varieties of Picard number two (arXiv:1307.5490v2).** This work extends results of Oguiso on birational or automorphism groups, and of Lazić–Peternell on the Morrison–Kawamata cone conjecture, from Calabi–Yau manifolds of Picard number two to arbitrary singular varieties $X$ (resp. to klt Calabi–Yau pairs in the broad sense) of Picard number two. Its headline structural dichotomy is that when $X$ has only klt singularities and is not a complex torus, either $\mathrm{Aut}(X)$ is almost cyclic, or (the abstract truncates here). For our purposes the relevant point is the supplied dichotomy itself: automorphism groups of Picard-number-two varieties are tightly constrained, which makes them a natural testbed for asking whether dilations (e.g., rescalings of an ample class) normalize them. The abstract supplies no further detail on the second branch of the dichotomy, and we do not speculate beyond it.

**[2] Automorphisms of Sedenions (arXiv:2512.07210v3).** This paper extends the octonion calibration in Clifford algebra to two related sedenion calibrations. Associative calibrations map quaternion rings in Clifford algebra to those in Cayley–Dickson algebras; the abstract states that octonions consist of seven such rings and sedenions of thirty-five. A new non-associative calibration is found, related to the sedenion associative calibration but invertible (the abstract truncates mid-sentence). This is the most directly quantitative entry in the bibliography for our purposes: the pair $(7, 35)$ supplies the inputs for our growth derivation in Section 4, and the Cayley–Dickson tower is the canonical setting in which "dimension scaling" (doubling) and "automorphism structure" (calibrations, quaternion rings) interact.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism (arXiv:2110.13834v2).** The authors construct a modular compactification via stable slc pairs for moduli spaces of K3 surfaces equipped with a nonsymplectic group of automorphisms, under the assumption that some combination of the fixed loci of the automorphisms defines an effective big divisor, and prove the compactification is semitoroidal. The relevance to scaling is structural: fixed loci of automorphisms are the loci where a scaling-like action (a group action with eigenvalue data) is most visible, and the boundary behavior of the moduli compactification governs how automorphism data degenerate — a degeneration question that is, at heart, about behavior under rescaling of divisor classes. The abstract gives no numerical data.

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries (arXiv:1312.7318v3).** This work studies automorphisms of homogeneous parabolic geometries that possess a fixed point, with a prescribed "natural" action on the distinguished distributions that parabolic geometries carry. The authors describe the sets of such automorphisms in detail and classify whether there are non-flat homogeneous parabolic geometries (the abstract truncates here). Parabolic geometries are built from filtered structures with graded pieces; a dilation of the grading is the natural scaling in this setting, and the fixed-point hypothesis is exactly the situation where the tangent-level (infinitesimal, hence linear and scale-sensitive) action of an automorphism can be read off. The abstract supplies no further classification detail.

**[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product (arXiv:2412.04250v2).** The authors give a concise presentation for the group of pure symmetric outer automorphisms of a splitting of a free product $G_1 \ast \dots \ast G_n$ — the (outer) automorphisms preserving the conjugacy classes of the free factors $G_i$ — by considering the action of these automorphisms on a particular subcomplex of Outer Space, which they show to be simply connected. The connection to scaling is via the geometry of Outer Space, whose metric structure is scale-invariant in the standard theory; the supplied abstract, however, states only the presentation result and the simple connectivity, so we use the work as an instance of "automorphisms acting on a space with a scaling-compatible geometry" without attributing any specific scale-invariance claim to it.

**[6] Bounding the order of automorphisms of certain curves (arXiv:alg-geom/9411016v2).** This paper studies upper bounds on the order of automorphisms of non-singular curves $X$ satisfying at least one of two hypotheses: (1) $X$ is an $m$-sheeted covering of exactly one non-singular curve of genus $\gamma$, where $m$ is prime; or (2) the center of the group of automorphisms of $X$ is non-trivial. Order bounds are the arithmetic shadow of scaling constraints: a finite automorphism of order $N$ acts on tangent spaces with eigenvalues that are roots of unity, and bounds on $N$ bound the "scale spectrum" available to the action. The abstract states the hypotheses and the goal but no explicit bound, and we do not supply one from memory.

**[7] Induced Automorphisms on Irreducible Symplectic Manifolds (arXiv:1405.5706v2).** The authors introduce the notion of induced automorphisms to state a criterion determining whether a given automorphism on a manifold of $K3^{[n]}$ type is induced by an automorphism of a $K3$ surface, with the manifold realized as a moduli space of stable objects on the $K3$. The criterion is applied to the classification of non-symplectic prime order automorphisms on manifolds of $K3^{[2]}$ type (abstract truncates). Induction through a moduli construction is a passage along which scaling data (metrics, periods) on the base $K3$ propagate to the constructed manifold; the supplied abstract supports the criterion-and-classification reading but no metric statement.

**[8] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^2$ (arXiv:1909.00765v2).** The authors show the existence of automorphisms $F$ of $\mathbb{C}^2$ with a non-recurrent Fatou component $\Omega$ biholomorphic to $\mathbb{C}\times\mathbb{C}^*$ that is the basin of attraction to an invariant entire curve on which $F$ acts as an irrational rotation; moreover the biholomorphism $\Omega \to \mathbb{C}\times\mathbb{C}^*$ can be chosen to conjugate $F$ to a translation (abstract truncates mid-formula). This is the most dynamically explicit entry: an automorphism whose asymptotic behavior is a rotation on an invariant curve and a translation in adapted coordinates. Rotations and translations are precisely the maps for which the scalar-dilation conjugation computation of Section 4 is trivial, making this entry a natural anchor for the centralization branch of our framework.

**[9]–[12] QNFO corpus entries (ULTRAMETRIC PHYSICS; Ultrametric Physics Research Plan; Meta-Analysis of Categorical Equivalence and Scale Invariance; Alpha Pi Project).** These four entries are supplied with titles only and no abstract text. We therefore cannot state what they contain, argue, or found. We note only that their titles indicate a research program in which ultrametric (hierarchical, non-Archimedean) structures, categorical equivalence, and scale invariance are central themes — themes consonant with the automorphism–scaling question of this paper — and we flag in Section 6 that any integration of this corpus into the present analysis would require source material beyond what is supplied here.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ and let $\mathrm{Aut}(X)$ be its automorphism group. Let $\mathcal{S}(X)$ denote a distinguished class of self-bijections of $X$ that we call **scalings**: maps $S: X \to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate) without changing the structure type. Concretely we use:

- **Scalar dilations** $S_\lambda(x) = \lambda x$ on a vector space or algebra, with $\lambda \in \mathbb{R}_{>0}$ or $\mathbb{C}^*$.
- **Anisotropic dilations** $D = \mathrm{diag}(\lambda_1, \dots, \lambda_n)$ on $\mathbb{R}^n$ or $\mathbb{C}^n$, with $\lambda_i > 0$.

The **conjugation test** applied to a pair $(S, \phi)$ with $S \in \mathcal{S}(X)$, $\phi \in \mathrm{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1} \in \mathrm{Aut}(X)\,? \qquad
\text{(C)}\quad S\phi = \phi S\,? \qquad
\text{(P)}\quad \text{does } S(\cdot)S^{-1} \text{ act on parameters of } \phi \text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism (then $S\phi S^{-1}$ is a composition of automorphisms); the interesting content of (N) arises when $S$ is not an automorphism of $X$ but the conjugate still preserves the structure — the case of scalings that are symmetries of the structure *type* but not of the particular object. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi) = \{S \in \mathcal{S}(X) : S\phi = \phi S\}$. Question (P) is the quantitative core and is carried out in Section 4.

### 3.2 Model automorphisms

We use two planar linear maps as canonical test automorphisms of $\mathbb{R}^2$ (both are automorphisms of the vector space structure):

$$
\phi_{\mathrm{uni}}(x,y) = (x + y,\; y), \qquad
\phi_{\mathrm{rot}}(x,y) = (\cos\theta\, x - \sin\theta\, y,\; \sin\theta\, x + \cos\theta\, y),
$$

a unipotent shear and a rotation by angle $\theta$. These model, respectively, the translation-type asymptotics and the irrational-rotation behavior reported in [8]: the supplied abstract states that $F$ acts as an irrational rotation on an invariant entire curve and is conjugate to a translation in adapted coordinates on $\Omega \cong \mathbb{C}\times\mathbb{C}^*$.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non-associative setting of [2], the supplied abstract gives two counts of associative quaternion rings: $N_{\mathrm{oct}} = 7$ for octonions and $N_{\mathrm{sed}} = 35$ for sedenions. We treat the passage octonion $\to$ sedenion as one **dimension-doubling step** (the Cayley–Dickson construction doubles dimension; the abstract's framing of octonions and sedenions as successive Cayley–Dickson algebras supports this reading) and define the per-step growth exponent

$$
g = \log_2\!\left(\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}\right).
$$

All arithmetic is shown in Section 4.

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

| Quantity | Value | Source |
|---|---|---|
| Associative quaternion rings in octonions | $N_{\mathrm{oct}} = 7$ | Supplied abstract of [2] |
| Associative quaternion rings in sedenions | $N_{\mathrm{sed}} = 35$ | Supplied abstract of [2] |
| Anisotropic dilation diagonal entries | $\lambda_1 = 2$, $\lambda_2 = 3$ | Chosen here (Section 3.1) |
| Shear coefficient of $\phi_{\mathrm{uni}}$ | $c = 1$ | Definition in Section 3.2 |
| Rotation angle | $\theta$ (irrational multiple of $\pi$, per the behavior in [8]) | Supplied abstract of [8] |

No other numerical inputs are used anywhere in this paper.

### 4.2 Conjugation of the shear by an anisotropic dilation

Take $D = \mathrm{diag}(\lambda_1, \lambda_2) = \mathrm{diag}(2, 3)$ and $\phi_{\mathrm{uni}}(x,y) = (x+y,\, y)$. Compute $D\,\phi_{\mathrm{uni}}\,D^{-1}$ step by step:

$$
D^{-1}(x, y) = \left(\frac{x}{\lambda_1}, \frac{y}{\lambda_2}\right) = \left(\frac{x}{2}, \frac{y}{3}\right),
$$

$$
\phi_{\mathrm{uni}}\!\left(\frac{x}{2}, \frac{y}{3}\right) = \left(\frac{x}{2} + \frac{y}{3},\; \frac{y}{3}\right),
$$

$$
D\left(\frac{x}{2} + \frac{y}{3},\; \frac{y}{3}\right) = \left(2\left(\frac{x}{2} + \frac{y}{3}\right),\; 3\cdot\frac{y}{3}\right) = \left(x + \frac{2}{3}y,\; y\right).
$$

Hence

$$
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y) = \left(x + \frac{\lambda_1}{\lambda_2}\,y,\; y\right) = \left(x + \frac{2}{3}y,\; y\right),
$$

i.e., conjugation rescales the shear coefficient by the ratio of diagonal entries:

$$
c \;\longmapsto\; c' = \frac{\lambda_1}{\lambda_2}\, c = \frac{2}{3}\cdot 1 = \frac{2}{3} \approx 0.666667.
$$

In general, for $D = \mathrm{diag}(\lambda_1, \lambda_2)$ the same three lines give $c' = \frac{\lambda_1}{\lambda_2}c$; the computation above is the instance $\lambda_1 = 2$, $\lambda_2 = 3$. This is the paper's headline quantitative result: **anisotropic scalings act nontrivially on automorphism parameters, by multiplicative ratios of scaling factors.**

### 4.3 Triviality of scalar-dilation conjugation

Let $S_\lambda(x) = \lambda x$ with $\lambda > 0$ scalar, on $\mathbb{R}^2$.

**Shear.** $S_\lambda \phi_{\mathrm{uni}} S_\lambda^{-1}(x,y)$: $S_\lambda^{-1}(x,y) = (x/\lambda, y/\lambda)$; $\phi_{\mathrm{uni}}$ gives $((x+y)/\lambda, y/\lambda)$; $S_\lambda$ gives $(x+y, y)$. So

$$
S_\lambda\,\phi_{\mathrm{uni}}\,S_\lambda^{-1} = \phi_{\mathrm{uni}} \quad \text{for all } \lambda > 0.
$$

**Rotation.** Since $S_\lambda = \lambda\, I_2$ is a scalar matrix, it commutes with every $2\times 2$ matrix, in particular with the rotation matrix $R_\theta$; explicitly $S_\lambda R_\theta S_\lambda^{-1} = \lambda I_2 R_\theta \frac{1}{\lambda} I_2 = R_\theta$. The rotation angle is invariant: $\theta \mapsto \theta$.

Thus scalar dilations lie in the centralizer of both model automorphisms: scaling "relates to" these automorphisms only trivially, unless the scaling is anisotropic. This dichotomy — trivial for isotropic, ratio-rescaling for anisotropic — is the structural answer to the re-entry question at the level of linear models.

### 4.4 Growth of associative structure in the Cayley–Dickson tower

From [2]: $N_{\mathrm{oct}} = 7$, $N_{\mathrm{sed}} = 35$. The ratio is

$$
\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}} = \frac{35}{7} = 5.
$$

The per-dimension-doubling growth exponent is

$$
g = \log_2 5 = \frac{\ln 5}{\ln 2} \approx \frac{1.609438}{0.693147} \approx 2.321928.
$$

So the count of associative quaternion rings grows by a factor of $5$ — equivalently by about $2.32$ bits, i.e., a bit more than a factor of $2^2 = 4$ and less than $2^3 = 8$ — across the single octonion-to-sedenion step reported in [2].

Two purely arithmetic observations on these same two supplied numbers, offered as observations about the numbers and not as claims about the paper [2]:

$$
7 = \binom{7}{1}, \qquad 35 = \binom{7}{3}.
$$

Both hold by direct evaluation: $\binom{7}{1} = 7$ and $\binom{7}{3} = \frac{7\cdot 6\cdot 5}{3\cdot 2\cdot 1} = 35$. Whether these binomial identities reflect structure or coincidence is an open question we do not resolve; the supplied abstract of [2] does not address it.

### 4.5 Scaling and the automorphism-group constraints of [1] and [6]

The supplied abstract of [1] states a dichotomy: for klt singular varieties of Picard number two that are not complex tori, either $\mathrm{Aut}(X)$ is almost cyclic, or (truncated). In the almost-cyclic branch, $\mathrm{Aut}(X)$ is, up to finite index, generated by one element; a dilation $S$ with $S\,\mathrm{Aut}(X)\,S^{-1} = \mathrm{Aut}(X)$ then acts by conjugation on a virtually cyclic group, which is a rigid situation: conjugation preserves the cyclic generator up to powers. The abstract supplies no further detail on the second branch, so we record the first-branch observation only.

The supplied abstract of [6] studies upper bounds on the order of automorphisms of curves under two hypotheses (prime covering degree $m$ over a curve of genus $\gamma$; non-trivial center of the automorphism group). The scaling connection is via eigenvalues: a finite-order automorphism acts on tangent spaces with eigenvalues that are roots of unity, all of modulus $1$; an order bound is therefore a bound on the finite set of "scales" (roots of unity) the action can exhibit. The abstract states no explicit bound, and we do not supply one.

### 4.6 Synthesis

Across the eight settings, the conjugation test sorts as follows. Scalar dilations centralize rotation- and translation-type behavior ([8]) and unipotents (Section 4.3). Anisotropic dilations act nontrivially on automorphism parameters by ratio rules (Section 4.2). In moduli and induction settings ([3], [7]), scaling enters through degeneration and propagation of period/metric data, per the supplied abstracts' framing but without numbers. In group-theoretic settings ([5]), automorphisms act on a simply connected subcomplex of Outer Space, a space whose standard geometry is built from scaling-compatible metrics — though the supplied abstract itself makes no scale-invariance claim, and we do not attribute one. In the constrained-variety settings ([1], [6]), scaling interacts with rigidly bounded automorphism structure. In the non-associative setting ([2]), dimension-doubling scaling accompanies a factor-$5$ growth in associative sub-structure.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (Shear rescaling, exact).** Conjugation of $\phi_{\mathrm{uni}}(x,y) = (x+y,\,y)$ by $D = \mathrm{diag}(2,3)$ yields $D\phi_{\mathrm{uni}}D^{-1}(x,y) = (x + \tfrac{2}{3}y,\, y)$; the shear coefficient maps $c = 1 \mapsto c' = \tfrac{2}{3} \approx 0.666667$. General rule: $c' = \frac{\lambda_1}{\lambda_2} c$ (derived in Section 4.2).

**R2 (Scalar-dilation triviality, exact).** For every scalar $\lambda > 0$: $S_\lambda \phi_{\mathrm{uni}} S_\lambda^{-1} = \phi_{\mathrm{uni}}$ and $S_\lambda R_\theta S_\lambda^{-1} = R_\theta$. Scalar dilations centralize both model automorphisms (Section 4.3).

**R3 (Ring-count growth, from [2]).** $\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}} = \frac{35}{7} = 5$; per-dimension-doubling exponent $g = \log_2 5 \approx 2.321928$ (Section 4.4).

**R4 (Binomial identities, arithmetic observation).** $7 = \binom{7}{1}$ and $35 = \binom{7}{3}$, verified by direct evaluation in Section 4.4. Status: observation about the numbers, not a finding attributed to [2].

**R5 (Projection, labeled as such).** If one were to extrapolate the per-step factor of $5$ (R3) linearly across further hypothetical Cayley–Dickson steps — an assumption with no support in the supplied abstract of [2], which reports only the octonion and sedenion counts — the next-step count would be $35 \times 5 = 175$, with uncertainty dominated entirely by the unverified linearity assumption; we assign it no error bar and present it solely to make the extrapolation explicit and falsifiable. We emphasize that R5 is a projection under a stated assumption, not a result about the literature.

No empirical, simulated, or measured data are reported in this paper; all quantitative claims above are exact arithmetic or the labeled projection R5.

## 6. Discussion

**Limitations.** The paper's evidence base is a set of eight supplied abstracts, several of which truncate mid-sentence ([1], [2], [4], [7], [8]). We have deliberately restricted every statement about these works to what their supplied text states; this means, for example, that we know the dichotomy of [1] only in its first branch, the new calibration of [2] only as "invertible" with the sentence cut off, and the classification of [4] only up to the truncation. A fuller treatment would require the full texts. The four QNFO entries [9]–[12] carry no abstract content at all; any claim connecting this paper to ultrametric physics or scale-invariance meta-analysis would be unsupported, and we make none.

**Failure modes of the framework.** The conjugation test presupposes that scalings are self-bijections of the object. In many settings of interest — e.g., moduli compactifications as in [3] — the natural "scaling" (rescaling a divisor class) does not define a self-map of the object at all, and the test degenerates to a metaphor. Second, the parameter-rescaling branch (P) was instantiated only for linear planar models; whether ratio rules like $c' = \frac{\lambda