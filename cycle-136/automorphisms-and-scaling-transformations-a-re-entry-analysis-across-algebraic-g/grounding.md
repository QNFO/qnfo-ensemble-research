# Grounding block - source: rem-d141a742-64fd-49f6-960c-dfc00103ee9e

## Research idea

Re-entry from 10.5281/zenodo.22758467: automorphisms relate to scaling transformations?

## Existing paper under revision (remediation only)

# Automorphisms and Scaling Transformations: A Re-Entry Analysis Across Algebraic, Geometric, and Dynamical Settings

## Abstract

We examine the relationship between automorphisms — structure-preserving self-maps of algebraic, geometric, or dynamical objects — and scaling transformations, i.e., dilations that rescale coordinates, dimensions, or metrics without changing the underlying structure type. Motivated by a re-entry prompt asking whether automorphisms "relate to scaling transformations," we organize twelve supplied sources — eight arXiv mathematics papers on automorphisms of varieties, calibrations, parabolic geometries, free-product splittings, curves, symplectic manifolds, and holomorphic dynamics, plus four corpus entries supplied with titles only — into a common framework in which every automorphism is tested against a distinguished class of dilations. We introduce a conjugation test (normalization, centralization, parameter rescaling) and give explicit derivations with all arithmetic shown: conjugation of a unipotent planar automorphism by the diagonal dilation $D=\mathrm{diag}(2,3)$ rescales its shear coefficient by $\lambda_1/\lambda_2 = 2/3$; scalar dilations act trivially on rotations and unipotents; and in the Cayley–Dickson tower the count of associative quaternion rings grows from $7$ (octonions) to $35$ (sedenions), a factor of $5$, corresponding to $\log_2 5 \approx 2.321928$ per dimension-doubling step, while ring density grows by exactly $2.5$. We conclude that scaling relates to automorphisms primarily through conjugation action on parameter spaces, and we state falsification conditions and open questions.

## 1. Introduction

An automorphism of a mathematical object $X$ is an isomorphism from $X$ to itself; the set of all automorphisms forms a group $\mathrm{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S_\lambda$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$. The question posed in the re-entry prompt — whether automorphisms "relate to scaling transformations" — is deliberately open: it does not specify the category (algebraic varieties, non-associative algebras, parabolic geometries, groups, dynamical systems), and the answer plausibly differs across categories.

This paper treats the question as a comparative-structural one. Rather than proving a single theorem, we construct a uniform lens — the **conjugation test** — and apply it to a fixed bibliography of recent work on automorphisms. The lens asks three questions of each setting:

1. **Normalization:** does a dilation $S$ send automorphisms to automorphisms, i.e., does $S\,\mathrm{Aut}(X)\,S^{-1} \subseteq \mathrm{Aut}(X)$?
2. **Centralization:** does $S$ commute with some or all automorphisms, i.e., is $S\phi = \phi S$?
3. **Parameter rescaling:** when automorphisms come in families indexed by numerical parameters (shear coefficients, rotation angles, orders), does conjugation by $S$ act on those parameters by a computable rule?

The third question is where scaling becomes visible and quantitative. We show by explicit computation that conjugation by an anisotropic dilation $D=\mathrm{diag}(2,3)$ rescales the shear coefficient of the planar unipotent map $\phi(x,y)=(x+y,\,y)$ by exactly $2/3$, while scalar dilations act trivially on both unipotents and rotations. We also quantify the growth of associative structure in the Cayley–Dickson tower, where the supplied literature reports $7$ quaternion rings for octonions and $35$ for sedenions: the raw ratio is $5$, the per-dimension density ratio is $2.5$, and the per-step exponent is $\log_2 5 \approx 2.321928$.

Our contributions are: (i) a uniform three-part framework for relating automorphisms to scalings; (ii) explicit arithmetic derivations of conjugation effects and growth ratios; (iii) a structured reading of the supplied bibliography, each work discussed strictly within what its supplied abstract states; and (iv) an honest account of the limits of this exercise, including the fact that four supplied corpus entries (the QNFO items) carry no abstract content and can be used only as pointers.

The paper is organized as follows. Section 2 reviews the supplied literature. Section 3 formalizes the conjugation test. Section 4 carries out the derivations with all arithmetic shown. Section 5 reports results. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

We discuss all twelve bibliography entries in their supplied numbering. Entries [1]–[8] are arXiv mathematics papers whose supplied summaries we paraphrase strictly; entries [9]–[12] are QNFO corpus documents supplied with empty summaries, and we say so explicitly, relating them to our argument only through their titles.

**[1] Birational automorphism groups of projective varieties of Picard number two (arXiv:1307.5490v2).** This work extends results of Oguiso on birational or automorphism groups, and of Lazić–Peternell on the Morrison–Kawamata cone conjecture, from Calabi–Yau manifolds of Picard number two to arbitrary singular varieties $X$ (resp. to klt Calabi–Yau pairs in the broad sense) of Picard number two. Its headline structural dichotomy is that when $X$ has only klt singularities and is not a complex torus, either $\mathrm{Aut}(X)$ is almost cyclic, or (the abstract truncates here). The *Picard number* $\rho(X)$, defined as the rank of the Néron–Severi group of divisor classes modulo numerical equivalence, equals $2$ in this setting, so the natural cone object attached to $X$ is two-dimensional and the automorphism group acts on it. The abstract supplies no further detail on the second branch of the dichotomy, and we do not speculate beyond it.

**[2] Automorphisms of Sedenions (arXiv:2512.07210v3).** This paper extends the octonion calibration in Clifford algebra to two related sedenion calibrations. Associative calibrations map quaternion rings in Clifford algebra to those in Cayley–Dickson algebras; the abstract states that octonions consist of seven such rings and sedenions of thirty-five. A new non-associative calibration is found, related to the sedenion associative calibration but invertible (the abstract truncates mid-sentence). This is the most directly quantitative entry in the bibliography for our purposes: the pair $(7, 35)$ supplies the inputs for our growth derivations in Section 4, and the Cayley–Dickson tower is the canonical setting in which dimension doubling and automorphism-relevant substructure interact.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism (arXiv:2110.13834v2).** The authors construct a modular compactification via stable slc pairs for moduli spaces of K3 surfaces equipped with a nonsymplectic group of automorphisms, under the assumption that some combination of the fixed loci of the automorphisms defines an effective big divisor, and prove the compactification is semitoroidal. A *nonsymplectic* automorphism is one that does not preserve the holomorphic symplectic form of the K3 surface. For our framework, the fixed-locus/divisor condition is a compatibility condition between automorphisms and a divisorial (cone-like) object, and semitoroidal compactifications are built from toroidal (cone-complex) data, the same cone geometry that appears in entry [1]. The abstract gives no numerical data.

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries (arXiv:1312.7318v3).** This work studies automorphisms of homogeneous parabolic geometries that possess a fixed point, with a prescribed "natural" action on the distinguished distributions that parabolic geometries carry. The authors describe the sets of such automorphisms in detail and classify whether there are non-flat homogeneous parabolic geometries (the abstract truncates here). Parabolic geometries are built from filtered structures with graded pieces; a dilation of the grading is the natural scaling in this setting, and the fixed-point hypothesis is exactly the situation where the tangent-level (linear, hence scale-sensitive) action of an automorphism can be read off. The abstract supplies no further classification detail.

**[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product (arXiv:2412.04250v2).** The authors give a concise presentation for the group of pure symmetric outer automorphisms of a splitting of a free product $G_1 \ast \dots \ast G_n$ — the (outer) automorphisms preserving the conjugacy classes of the free factors $G_i$ — by considering the action of these automorphisms on a particular subcomplex of Outer Space, which they show to be simply connected. The "symmetric" condition permits permutation of the factor conjugacy classes, giving a natural action on a set of $n$ objects; this is the combinatorial skeleton on which our counting derivation in Section 4 rests. The abstract makes no scale-invariance claim, and we attribute none to it.

**[6] Bounding the order of automorphisms of certain curves (arXiv:alg-geom/9411016v2).** This paper studies upper bounds on the order of automorphisms of non-singular curves $X$ satisfying at least one of two hypotheses: (1) $X$ is an $m$-sheeted covering of exactly one non-singular curve of genus $\gamma$, where $m$ is prime; or (2) the center of the group of automorphisms of $X$ is non-trivial. The scaling connection is qualitative: a finite-order automorphism acts on tangent spaces with eigenvalues that are roots of unity, all of modulus $1$, so an order bound bounds the finite set of "scales" the action can exhibit. The abstract states the hypotheses and the goal but no explicit bound, and we do not supply one from memory.

**[7] Induced Automorphisms on Irreducible Symplectic Manifolds (arXiv:1405.5706v2).** The authors introduce the notion of induced automorphisms to state a criterion determining whether a given automorphism on a manifold of $K3^{[n]}$ type is induced by an automorphism of a $K3$ surface, with the manifold realized as a moduli space of stable objects on the $K3$. The criterion is applied to the classification of non-symplectic prime order automorphisms on manifolds of $K3^{[2]}$ type (the abstract truncates). For our framework this is a *descent* statement: an automorphism at one level of a hierarchy is explained by an automorphism at a lower level, structurally analogous to a scaling relation between levels of a hierarchy. The abstract supports the criterion-and-classification reading but no metric statement.

**[8] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^2$ (arXiv:1909.00765v2).** The authors show the existence of automorphisms $F$ of $\mathbb{C}^2$ with a non-recurrent Fatou component $\Omega$ biholomorphic to $\mathbb{C}\times\mathbb{C}^*$ that is the basin of attraction to an invariant entire curve on which $F$ acts as an irrational rotation; moreover the biholomorphism $\Omega \to \mathbb{C}\times\mathbb{C}^*$ can be chosen to conjugate $F$ to a translation (the abstract truncates mid-formula). This is the most dynamically explicit entry: an automorphism whose asymptotic behavior is a rotation on an invariant curve and a translation in adapted coordinates. Rotations and translations are precisely the maps for which the scalar-dilation conjugation computation of Section 4 is trivial, making this entry a natural anchor for the centralization branch of our framework.

**[9]–[12] QNFO corpus entries (QNFO: ULTRAMETRIC PHYSICS; QNFO: Ultrametric Physics Research Plan; QNFO: Meta-Analysis of Categorical Equivalence and Scale Invariance; QNFO: Alpha Pi Project).** These four entries are supplied with titles only and no abstract text; the supplied material gives no further detail beyond the titles. We therefore cannot state what they contain, argue, or found. We note only that their titles indicate a research program in which ultrametric (hierarchical, non-Archimedean) structures, categorical equivalence, and scale invariance are central themes — themes consonant with the automorphism–scaling question of this paper — and we flag in Section 6 that any integration of this corpus into the present analysis would require source material beyond what is supplied here.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ and let $\mathrm{Aut}(X)$ be its automorphism group. Let $\mathcal{S}(X)$ denote a distinguished class of self-bijections of $X$ that we call **scalings**: maps $S: X \to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate, a dimension grading) without changing the structure type. Concretely we use:

- **Scalar dilations** $S_\lambda(x) = \lambda x$ on a vector space or algebra, with $\lambda \in \mathbb{R}_{>0}$ or $\mathbb{C}^*$.
- **Anisotropic dilations** $D = \mathrm{diag}(\lambda_1, \dots, \lambda_n)$ on $\mathbb{R}^n$ or $\mathbb{C}^n$, with $\lambda_i > 0$.

The **conjugation test** applied to a pair $(S, \phi)$ with $S \in \mathcal{S}(X)$, $\phi \in \mathrm{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1} \in \mathrm{Aut}(X)\,? \qquad
\text{(C)}\quad S\phi = \phi S\,? \qquad
\text{(P)}\quad \text{does } S(\cdot)S^{-1} \text{ act on parameters of } \phi \text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism; the interesting content arises when $S$ is not an automorphism of the particular object but the conjugate still preserves the structure type. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi) = \{S \in \mathcal{S}(X) : S\phi = \phi S\}$. Question (P) is the quantitative core and is carried out in Section 4.

### 3.2 Model automorphisms

We use two planar linear maps as canonical test automorphisms of $\mathbb{R}^2$ (both are automorphisms of the vector space structure):

$$
\phi_{\mathrm{uni}}(x,y) = (x + y,\; y), \qquad
\phi_{\mathrm{rot}}(x,y) = (\cos\theta\, x - \sin\theta\, y,\; \sin\theta\, x + \cos\theta\, y),
$$

a unipotent shear and a rotation by angle $\theta$. These model, respectively, the translation-type asymptotics and the irrational-rotation behavior reported in [8]: the supplied abstract states that $F$ acts as an irrational rotation on an invariant entire curve and is conjugate to a translation in adapted coordinates on $\Omega \cong \mathbb{C}\times\mathbb{C}^*$.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non-associative setting of [2], the supplied abstract gives two counts of associative quaternion rings: $N_{\mathrm{oct}} = 7$ for octonions and $N_{\mathrm{sed}} = 35$ for sedenions. We treat the passage octonion $\to$ sedenion as one **dimension-doubling step**. We explicitly label this as a standard-mathematical assumption of the present paper: the Cayley–Dickson construction is conventionally taken to send a real algebra of dimension $d$ to one of dimension $2d$, and we use this assumption to define the density invariant below. The supplied abstract of [2] does not itself state that the construction doubles dimension or that octonions and sedenions are successive in the tower; it supplies only the two ring counts. With that assumption in place, we define:

- the per-step growth exponent $g = \log_2\!\left(N_{\mathrm{sed}}/N_{\mathrm{oct}}\right)$;
- the *ring density* $\delta(A) = N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$ carrying $N(A)$ associative quaternion rings, and the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic is shown in Section 4.

### 3.4 Method of survey-and-count

Because the supplied source material consists of abstracts, our method is necessarily conservative: (i) extract from each abstract the structural claims it explicitly makes about an automorphism group or a scaling-like construction; (ii) where the abstract supplies integer counts (as in [2]), compute derived invariants with full arithmetic; (iii) where the abstract is truncated or silent, record the gap and use the entry only at the level of its explicit statements. No claim in this paper about a cited work goes beyond its supplied summary.

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
| Picard number | $\rho = 2$ | Supplied abstract of [1] |

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

**Rotation.** Since $S_\lambda = \lambda\, I_2$ is a scalar matrix, it commutes with every $2\times 2$ matrix, in particular with the rotation matrix $R_\theta$; explicitly $S_\lambda R_\theta S_\lambda^{-1} = \lambda I_2\, R_\theta\, \frac{1}{\lambda} I_2 = R_\theta$. The rotation angle is invariant: $\theta \mapsto \theta$.

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

**Dimensions.** Each Cayley–Dickson doubling step sends real dimension $d$ to $2d$, so after $k$ steps the dimension is $D_k = 2^k$. The octonions sit three steps above the reals and the sedenions four:

$$
D_3 = 2^3 = 8, \qquad D_4 = 2^4 = 16, \qquad \frac{D_4}{D_3} = \frac{16}{8} = 2.
$$

**Densities.** With Definition 3.3:

$$
\delta(\mathbb{O}) = \frac{N_{\mathrm{oct}}}{D_3} = \frac{7}{8} = 0.875, \qquad
\delta(\mathbb{S}) = \frac{N_{\mathrm{sed}}}{D_4} = \frac{35}{16} = 2.1875,
$$

$$
\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})} = \frac{N_{\mathrm{sed}}/D_4}{N_{\mathrm{oct}}/D_3} = \frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}} \cdot \frac{D_3}{D_4} = 5 \cdot \frac{8}{16} = 5 \cdot \frac{1}{2} = 2.5.
$$

**Interpretation.** Under one Cayley–Dickson doubling, ambient dimension scales by exactly $2$, but the count of associative quaternion subalgebras scales by $5$, and their density per real dimension by exactly $2.5$. This mismatch — structural growth outpacing dimensional growth — is a concrete, checkable instance of the paper's thesis that automorphism-relevant structure does not scale linearly with its ambient object.

Two purely arithmetic observations on these same two supplied numbers, offered as observations about the numbers and not as claims about the paper [2]:

$$
7 = \binom{7}{1}, \qquad 35 = \binom{7}{3} = \frac{7\cdot 6\cdot 5}{3\cdot 2\cdot 1} = 35.
$$

Whether these binomial identities reflect structure or coincidence is an open question we do not resolve; the supplied abstract of [2] does not address it.

### 4.5 Scaling and the automorphism-group constraints of [1] and [6]

The supplied abstract of [1] states a dichotomy: for klt singular varieties of Picard number two that are not complex tori, either $\mathrm{Aut}(X)$ is almost cyclic, or (truncated). In the almost-cyclic branch, $\mathrm{Aut}(X)$ is, up to finite index, generated by one element; a dilation $S$ with $S\,\mathrm{Aut}(X)\,S^{-1} = \mathrm{Aut}(X)$ then acts by conjugation on a virtually cyclic group, a rigid situation in which conjugation preserves the cyclic generator up to powers. The abstract supplies no further detail on the second branch, so we record the first-branch observation only.

As a piece of cone combinatorics enabled by $\rho = 2$ from [1]: a simplicial cone of dimension $2$ has $\binom{2}{k}$ faces of dimension $k$, so its total face count is

$$
F = \binom{2}{0} + \binom{2}{1} + \binom{2}{2} = 1 + 2 + 1 = 4,
$$

with $2$ extreme rays. This face count is a standalone computation of the present paper, carried out on the input $\rho = 2$ supplied by [1]; whether it constrains, or is consistent with, the almost-cyclic first branch of the dichotomy of [1] is a hypothesis of this paper that the supplied abstract neither states nor supports, and we flag it as such in Section 6.

The supplied abstract of [6] studies upper bounds on the order of automorphisms of curves under two hypotheses (prime covering degree $m$ over a curve of genus $\gamma$; non-trivial center of the automorphism group). The scaling connection is via eigenvalues: a finite-order automorphism acts on tangent spaces with eigenvalues that are roots of unity, all of modulus $1$; an order bound is therefore a bound on the finite set of "scales" (roots of unity) the action can exhibit. The abstract states no explicit bound, and we do not supply one.

### 4.6 Discrete-scaling rigidity and permutation combinatorics

**Discrete scaling.** If a scaling transformation has discrete parameter group and cyclic image of order $k$, a scaling-compatible automorphism (Definition 3.1, normalization form) induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. Direct evaluation:

$$
\varphi(2) = 1, \quad \varphi(3) = 2, \quad \varphi(4) = 2, \quad \varphi(5) = 5-1 = 4, \quad \varphi(6) = |\{1,5\}| = 2.
$$

In particular $\varphi(2) = 1$: a discrete scaling of order $2$ admits no nontrivial rescaling of its own parameter. This matters because the Cayley–Dickson doubling step of Section 4.4 has ratio exactly $2$.

**Permutation ceiling.** From [5], the symmetric condition permits permutation of the $n$ factor conjugacy classes of $G_1 \ast \dots \ast G_n$; the symmetric group on $n$ objects has order $n!$:

$$
3! = 6, \qquad 4! = 24, \qquad 5! = 120.
$$

These are combinatorial ceilings on the permutation scope of the symmetric condition, not claims that the group of [5] achieves these orders; the supplied summary gives no group order.

### 4.7 Synthesis

Across the eight settings, the conjugation test sorts as follows. Scalar dilations centralize rotation- and translation-type behavior ([8]) and unipotents (Section 4.3). Anisotropic dilations act nontrivially on automorphism parameters by ratio rules (Section 4.2). In moduli and induction settings ([3], [7]), scaling enters through degeneration and propagation of period/metric data, per the supplied abstracts' framing but without numbers. In group-theoretic settings ([5]), automorphisms act on a simply connected subcomplex of Outer Space, a space whose standard geometry is built from scaling-compatible metrics — though the supplied abstract itself makes no scale-invariance claim, and we do not attribute one. In the constrained-variety settings ([1], [6]), scaling interacts with rigidly bounded automorphism structure. In the non-associative setting ([2]), dimension-doubling scaling accompanies a factor-$5$ growth in associative sub-structure.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (Shear rescaling, exact).** Conjugation of $\phi_{\mathrm{uni}}(x,y) = (x+y,\,y)$ by $D = \mathrm{diag}(2,3)$ yields $D\phi_{\mathrm{uni}}D^{-1}(x,y) = (x + \tfrac{2}{3}y,\, y)$; the shear coefficient maps $c = 1 \mapsto c' = \tfrac{2}{3} \approx 0.666667$. General rule: $c' = \frac{\lambda_1}{\lambda_2} c$ (Section 4.2).

**R2 (Scalar-dilation triviality, exact).** For every scalar $\lambda > 0$: $S_\lambda \phi_{\mathrm{uni}} S_\lambda^{-1} = \phi_{\mathrm{uni}}$ and $S_\lambda R_\theta S_\lambda^{-1} = R_\theta$. Scalar dilations centralize both model automorphisms (Section 4.3).

**R3 (Ring-count growth, from [2]).** $\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}} = \frac{35}{7} = 5$; per-dimension-doubling exponent $g = \log_2 5 \approx 2.321928$ (Section 4.4).

**R4 (Dimension and density, from [2]).** $D_3 = 8$, $D_4 = 16$, dimension growth factor $2$; $\delta(\mathbb{O}) = 0.875$, $\delta(\mathbb{S}) = 2.1875$, density growth factor $2.5$ exactly (Section 4.4).

**R5 (Binomial identities, arithmetic observation).** $7 = \binom{7}{1}$ and $35 = \binom{7}{3}$, verified by direct evaluation in Section 4.4. Status: observation about the numbers, not a finding attributed to [2].

**R6 (Cone combinatorics, exact).** For Picard number $\rho = 2$ (source [1]), a simplicial $2$-cone has $2$ extreme rays and $1 + 2 + 1 = 4$ faces (Section 4.5).

**R7 (Discrete-scaling rigidity, exact).** A cyclic scaling subgroup of order $k$ admits $\varphi(k)$ parameter rescalings; in particular $\varphi(2) = 1$, so order-$2$ discrete scaling admits no nontrivial rescaling of its own parameter (Section 4.6).

**R8 (Permutation ceiling, exact).** For a free-product splitting with $n$ factors (source [5]), the symmetric-group ceiling on factor permutation is $n!$: $6$ for $n=3$, $24$ for $n=4$, $120$ for $n=5$. This is a combinatorial ceiling, not a group order (Section 4.6).

**Projection P1 (labeled as a projection, not a computation).** If the per-step ring-count factor of $5$ (R3) were to persist across a further hypothetical Cayley–Dickson step — an assumption with no support in the supplied abstract of [2], which reports only the octonion and sedenion counts — the next-step count would be $35 \times 5 = 175$ at dimension $2^5 = 32$, with density $175/32 = 5.46875$. Uncertainty is dominated entirely by the unverified linearity assumption; we assign no error bar and present the projection solely to make the framework's predictive content explicit and falsifiable.

**Qualitative results.** (Q1) The corpus exhibits scaling structure in three guises: literal dimension doubling ([2]), cone/grading geometry ([1], [3], [4]), and translation-type dynamics ([8]). (Q2) The automorphism side exhibits rigidity in three matching guises: the almost-cyclic dichotomy of [1] (for klt singular varieties of Picard number two that are not complex tori, the supplied abstract states that $\mathrm{Aut}(X)$ is almost cyclic in its first branch), the order bounds on automorphisms of curves studied in [6] under its two stated hypotheses, and the descent criterion of [7], which determines when an automorphism of a manifold of $K3^{[n]}$ type is induced by an automorphism of the underlying $K3$ surface. (Q3) The conjugation test of Section 3.1 is answered concretely in the linear setting: anisotropic dilations act nontrivially on automorphism parameters by ratio rules (R1), while scalar dilations act trivially (R2).

## 6. Discussion

**Limitations.** The central limitation of this study is the nature of its source base: the supplied material consists of abstracts, several of them truncated mid-sentence, and four corpus entries ([9]–[12]) supplied with titles only. Every structural claim we make about a cited work is therefore restricted to what its supplied summary explicitly states, and entries [9]–[12] contribute nothing beyond their titles. In particular: the second branch of the dichotomy of [1] is unavailable to us; the classification content of [4] and [7] is truncated; the abstract of [2] supplies two integer counts but no statement about dimension doubling, which we had to import as a labeled standard assumption (Section 3.3); and the abstract of [6] states its two hypotheses and its goal but no explicit bound, so we supply none.

**The density invariant depends on an imported assumption.** The density growth factor $2.5$ (R4) is computed from the two supplied counts divided by dimensions $8$ and $16$; the dimensions come from the standard Cayley–Dickson doubling assumption, not from the supplied abstract of [2]. If that assumption were dropped, the density ratio would be undefined within this paper's source base. We regard the assumption as safe — it is the textbook content of the construction — but it is an import, and we mark it as such.

**The binomial identities are unexplained.** The identities $7 = \binom{7}{1}$ and $35 = \binom{7}{3}$ (R5) are exact arithmetic observations about the two supplied counts. The supplied abstract of [2] does not address whether they reflect structure; a natural open question is whether the associative quaternion rings of a Cayley–Dickson algebra are indexed by subsets of a $7$-element set in a way that would explain $\binom{7}{3}$. We do not resolve this, and a demonstration that the match is coincidental would falsify any structural reading of R5.

**The cone-combinatorics connection is our own hypothesis.** Section 4.5 computes, from the input $\rho = 2$ supplied by [1], that a simplicial $2$-cone has $1 + 2 + 1 = 4$ faces and $2$ extreme rays. The claim that this rigidity is consistent with the almost-cyclic first branch of [1] is this paper's own unverified hypothesis: the supplied abstract of [1] says nothing about cones or face counts. It would be falsified by an example, within the hypotheses of [1], of a non-almost-cyclic automorphism group acting on a two-dimensional cone structure.

**The projection P1 rests on an unverified linearity assumption.** P1 extrapolates the per-step factor $5$ to a hypothetical further Cayley–Dickson step, yielding $35 \times 5 = 175$ rings at dimension $2^5 = 32$ and density $175/32 = 5.46875$. The supplied abstract of [2] reports only the octonion and sedenion counts and gives no support for persistence of the factor $5$; the projection is offered solely to make the framework falsifiable. A single further count from the tower that differs from $175$ would refute the linearity assumption.

**Failure modes of the framework.** The conjugation test is a lens, not a theorem: it sorts settings qualitatively and, in the linear models, quantitatively, but it does not classify automorphism groups in any of the eight cited settings. Its quantitative content (R1, R2) is confined to planar linear maps; whether the ratio rule $c' = \frac{\lambda_1}{\lambda_2}c$ has a counterpart for the nonlinear automorphisms of $\mathbb{C}^2$ in [8] is open, and the supplied abstract of [8], which reports an irrational rotation on an invariant curve and conjugacy to a translation, does not address dilations. The centralization branch (R2) is also model-dependent: scalar dilations commute with our two model maps, but an arbitrary automorphism group need not contain any map centralized by a non-scalar dilation.

**Open questions.** (O1) Does the factor-$5$ ring-count growth persist across further Cayley–Dickson steps, and is it explained by the binomial pattern of R5? (O2) Can the ratio rule of R1 be extended to conjugation of automorphisms of parabolic geometries ([4]) by grading-element scalings, within what the supplied abstract describes? (O3) What do the four QNFO corpus entries ([9]–[12]) contain; any integration of their themes — ultrametric structures, categorical equivalence, scale invariance — into the present framework would require source material beyond what is supplied here. (O4) Is the almost-cyclic branch of [1] stable under the kind of conjugation action studied in Section 4.2, in the setting of Picard number two?

## 7. Conclusion

We asked whether automorphisms relate to scaling transformations and answered with a uniform three-part conjugation test — normalization, centralization, parameter rescaling — applied to a fixed twelve-entry bibliography. The quantitative core is explicit: conjugation by the anisotropic dilation $D = \mathrm{diag}(2,3)$ rescales the shear coefficient of $\phi_{\mathrm{uni}}(x,y) = (x+y,\,y)$ by $\lambda_1/\lambda_2 = 2/3$, while scalar dilations centralize both model automorphisms, and the Cayley--Dickson step from octonions to sedenions multiplies the count of associative quaternion rings by $35/7 = 5$ and their density per real dimension by $2.5$. Scaling therefore relates to automorphisms chiefly through conjugation: trivially for isotropic scalings, and by computable ratio rules for anisotropic ones. The framework's quantitative content is confined to linear models and to the two supplied integer counts of [2]; its remaining connections are qualitative or explicitly labeled hypotheses and projections, each stated with its falsification condition in Section 6.

## References

[1] Birational automorphism groups of projective varieties of Picard number two. arXiv:1307.5490v2. https://arxiv.org/abs/1307.5490v2
[2] Automorphisms of Sedenions. arXiv:2512.07210v3. https://arxiv.org/abs/2512.07210v3
[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism. arXiv:2110.13834v2. https://arxiv.org/abs/2110.13834v2
[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries. arXiv:1312.7318v3. https://arxiv.org/abs/1312.7318v3
[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product. arXiv:2412.04250v2. https://arxiv.org/abs/2412.04250v2
[6] Bounding the order of automorphisms of certain curves. arXiv:alg-geom/9411016v2. https://arxiv.org/abs/alg-geom/9411016v2
[7] Induced Automorphisms on Irreducible Symplectic Manifolds. arXiv:1405.5706v2. https://arxiv.org/abs/1405.5706v2
[8] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$. arXiv:1909.00765v2. https://arxiv.org/abs/1909.00765v2
[9] QNFO: ULTRAMETRIC PHYSICS
[10] QNFO: Ultrametric Physics Research Plan
[11] QNFO: Meta-Analysis of Categorical Equivalence and Scale Invariance
[12] QNFO: Alpha Pi Project

## References

[1] Birational automorphism groups of projective varieties of Picard number two (arXiv:1307.5490v2).

[2] Automorphisms of Sedenions (arXiv:2512.07210v3).

[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism (arXiv:2110.13834v2).

[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries (arXiv:1312.7318v3).

[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product (arXiv:2412.04250v2).

[6] Bounding the order of automorphisms of certain curves (arXiv:alg-geom/9411016v2).

[7] Induced Automorphisms on Irreducible Symplectic Manifolds (arXiv:1405.5706v2).

[8] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^2$ (arXiv:1909.00765v2).

[9] QNFO: ULTRAMETRIC PHYSICS.

[10] QNFO: Ultrametric Physics Research Plan.

[11] QNFO: Meta-Analysis of Categorical Equivalence and Scale Invariance.

[12] QNFO: Alpha Pi Project.

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1307.5490v2 | Birational automorphism groups of projective varieties of Picard number two
arXiv:2512.07210v3 | Automorphisms of Sedenions
arXiv:2110.13834v2 | Compact moduli of K3 surfaces with a nonsymplectic automorphism
arXiv:1312.7318v3 | On automorphisms with natural tangent actions on homogeneous parabolic geometries
arXiv:2412.04250v2 | A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product
arXiv:1405.5706v2 | Induced Automorphisms on Irreducible Symplectic Manifolds
arXiv:1909.00765v2 | Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$

## QNFO corpus context (Vectorize)

QNFO: Automorphisms and Scaling Transformations: A Re-Entry Analysis Across Algebraic, Geometric, and Dynamical Settings
QNFO: ULTRAMETRIC PHYSICS

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1307.5490v2 | Birational automorphism groups of projective varieties of Picard number two
  We slightly extend a result of Oguiso on birational or automorphism groups (resp. of Lazić - Peternell on Morrison-Kawamata cone conjecture) from Calabi-Yau manifolds of Picard number two to arbitrary singular varieties X (resp. to klt Calabi-Yau pairs in broad sense) of Picard number two. When X has only klt singularities and is not a complex torus, we show that either Aut(X) is almost cyclic, or
  Full text (https://arxiv.org/html/1307.5490v2), excerpts of its own sections:
  § 1. Introduction: This note is inspired by Oguiso [ 8 ] and Lazić - Peternell [ 6 ] . Let $X$ be a normal projective variety defined over the field $\mathbb{C}$ of complex numbers. The following subgroup (of the birational group $\operatorname{Bir}(X)$ ) $\operatorname{Bir}_{2}(X):=\{g:X\dasharrow X\,|\,g\,\,\text{\rm is an isomorphism outside codimension two subsets}\}$ is also called the group of pseudo-automorphisms of $X$ . Let $\operatorname{NS}(X)=\{\text{\rm Cartier divisors}\}/(\text{\rm algebraic equivalence})$ be the Neron-Severi group, which is finitely generated. Let $\operatorname{NS}_{\mathbb{R}}(X):=\operatorname{NS}(X)\otimes\mathbb{R}$ with $\rho(X):=\dim_{\mathbb{R}}\operatorname{NS}_{\mathbb{R}}(X)$ the Picard number . Let $\operatorname{Eff}(X)\subset\operatorname{NS}_{\mathbb{R}}(X)$ be the cone of effective $\mathbb{R}$ -divisor ; its closure $\overline{\operatorname{Eff}}(X)$ is called the cone of pseudo-effective divisors . [...]
  § 2. Proof of Theorems: We use the notation and terminology in the book of Hartshorne and the book [ 5 ] . 2.1 . Proof of Theorem 1.2 Since $X$ has Picard number two, we can write the pseudo-effective closed cone as $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\geq 0}[f_{1}]+\mathbb{R}_{\geq 0}[f_{2}]$ (1) is proved in [ 8 ] and [ 6 ] . For reader’s convenience, we reproduce here. Let $g\in B_{2}^{-}$ or $A^{-}$ . Since $g$ permutes extremal rays of $\overline{\operatorname{Eff}}(X)$ , we can write $g^{*}f_{1}=af_{2}$ , $g^{*}f_{2}=bf_{1}$ with $a>0$ , $b>0$ . Since $g^{*}$ is defined on the integral lattice $\operatorname{NS}(X)/(\operatorname{torsion})$ , $\deg(g^{*})=\pm 1$ . Hence $ab=1$ . Thus $\operatorname{ord}(g^{*})=2$ and $g^{2}\in B_{2}^{0}$ . Now (1) follows from the observation that $B_{2}^{-}=gB_{2}^{+}$ or $A^{-}=gA^{+}$ . (2) The first equality is by the definition of $B_{2}^{0}$ . For the second equality, we just need to show that every $g\in B_{2}^{0}$ is in $\operatorname{Aut}(X)$ . Take an ample divisor $H$ on $X$ . [...]
[2] arXiv:2512.07210v3 | Automorphisms of Sedenions
  This paper extends the octonion calibration in Clifford algebra to two related sedenion calibrations. Associative calibrations map quaternion rings in Clifford algebra to those in Cayley-Dickson algebras, with octonions consisting of seven rings and sedenions having 35 rings. A new non-associative calibration is found that is related to the sedenion associative calibration but is invertible, provi
  Full text (https://arxiv.org/html/2512.07210v3), excerpts of its own sections:
  § 1 Introduction: The series of Cayley-Dickson algebras, ${\rm A_{N}}$ , provides $n=2^{N}$ basis elements generated by $N$ generators at each level, $N\geq 0$ . The series starts with the reals, ${\rm A_{0}}\cong{\mathbb{R}}$ , complex numbers, ${\rm A_{1}}\cong{\mathbb{C}}$ , quaternions, ${\rm A_{2}}\cong{\mathbb{H}}$ , octonions, ${\rm A_{3}}\cong{\mathbb{O}}$ , followed by the sedenions, ${\rm A_{4}}\cong{\mathbb{S}}$ . The series has increasingly complicated norms until sedenions and all ${\rm A_{N}}$ , for $N\geq 4$ , which have zero divisors, hence they are power-associative and can not be normed algebras. Because of this, until recently, they have been avoided by physicists as not being appropriate for reality. Mathematicians have struggled with the analysis of these algebras concentrating on the alternate rule, which is only valid for octonions [ 1 , 2 , 3 ] , and insufficient for embeddings of Lie algebras in the automorphisms of ${\rm A_{N}}$ , for $N\geq 4$ . [...]
  § 2 Sharp and Harp algebras: The ${\rm Sharp}({N})$ and ${\rm Harp}({N})$ algebras are subalgebras of Clifford algebras, ${\rm Cl}^{+}({n})$ and ${\rm Cl}({n})$ , respectively, where $n=2^{N}-1$ , $N>1$ . These are defined formally in the next section and introduced geometrically first. The 2-simplex is a triangle in 2-D that can be projected into a line segment in 1-D, called just a line. It has the perspective geometry that each edge has two vertices and each vertex has two edges. Clifford algebra adds $k$ -forms as labels to every geometric element and a parity as arrows to 2-forms and above. ${\rm Sharp}({2})$ is represented by a directed 2-simplex with consistent parity so that it can be projected to a 1-D directed line, as shown in Figure 2 . Taking any vertex label and multiplying by another vertex in ${\rm Cl}({3})$ gives the connecting edge, which is the dual of the third vertex. In other words the dual of one vertex multiplied by the dual of another gives the dual of the third and by the perspective geometry this applies to all edges so forms a ring. [...]
  § 3 Non-Associative Calibrations: Definition . Calibrations in ${\rm Cl}({n})$ are a sum of $k$ -forms representing simplices whereby each vertex intersects $k$ lots of $(k-1)$ -simplices and each of these simplices joins $k$ vertices. These are non-associative for $n>7$ . We now show that $\Phi=\Phi_{A}+\Phi_{O}+\Phi_{P}$ is an invertible calibration and also the associative calibration that maps to sedenions. [...]
  § 6 Summary: Calibrations in Clifford algebra provide a new way to analyse the structure of Cayley-Dickson algebras and this paper developed maps in order to understand this relationship. Such maps allowed the non-associative rings of sedenions to be inverse mapped to discover a new calibration in Clifford algebra. It is conjectured that such calibrations exist for all Cayley-Dickson algebras. The subset of Clifford algebras that map to Cayley-Dickson algebras were found to be related to ideals and the calibrations provide a classification of these ideals. The mechanism for deriving automorphisms of octonions from the calibration was extended to sedenions using the Sharp algebras and found to be more complicated than that for octonions and quaternions. The Sharp algebras may be considered as duals of Cayley-Dickson algebras since they have the same 3-cycle structure of quaternions but are commuting and have positive squares, for $N>2$ . [...]
[3] arXiv:2110.13834v2 | Compact moduli of K3 surfaces with a nonsymplectic automorphism
  We construct a modular compactification via stable slc pairs for the moduli spaces of K3 surfaces with a nonsymplectic group of automorphisms under the assumption that some combination of the fixed loci of automorphisms defines an effective big divisor, and prove that it is semitoroidal.
  Full text (https://arxiv.org/html/2110.13834v2), excerpts of its own sections:
  § 1. Introduction: Let $X$ be a smooth K3 surface over the complex numbers. An automorphism $\sigma$ of $X$ is called non-symplectic if it has finite order $n>1$ and $\sigma^{*}(\omega_{X})=\zeta_{n}\omega_{X}$ , where $\omega_{X}\in H^{2,0}(X)$ is a nonzero $2$ -form and $\zeta_{n}$ is a primitive $n$ th root of identity. By changing the generator of the cyclic group $\mu_{n}$ we can and will assume that $\zeta_{n}=\exp(2\pi i/n)$ . It is well known that a K3 surface admitting such an automorphism is projective. The possibilities for the order are the numbers $n$ whose Euler function satisfies $\varphi(n)\leq 20$ with the single exception $n\neq 60$ , see [ MO98 , Thm. 3] . In this paper we study compactification of moduli spaces of pairs $(X,\sigma)$ . But to begin with, the automorphism group $\Aut(X,\sigma)$ , i.e. those automorphisms of $X$ commuting with $\sigma$ , may be infinite. To fix this, we will usually additionally assume: ( $\exists g\geq 2$ ) $\text{The fixed locus }\operatorname{Fix}(\sigma)\text{ contains a curve $C_{1}$ of genus }g\geq 2. [...]
  § 2A. Notations: A lattice is a free abelian group with an integral-valued symmetric bilinear form. Let $L=H^{\oplus 3}\oplus E_{8}^{\oplus 2}$ be a fixed copy of the even unimodular lattice of signature $(3,19)$ , where $H=\textup{II}_{1,1}$ corresponds to the bilinear form $b(x,y)=xy$ and $E_{8}$ is the standard negative definite even lattice of rank $8$ . For any smooth K3 surface $X$ the cohomology lattice $H^{2}(X,{\mathbb{Z}})$ is isometric to $L$ . Denote by $S=S_{X}$ the Neron-Severi lattice $\Pic(X)=\operatorname{NS}(X)$ . By the Lefschetz $(1,1)$ -theorem, it equals $(H^{2,0}(X))^{\perp}\cap H^{2}(X,{\mathbb{Z}})\subset H^{2}(X,{\mathbb{C}})$ . We have $H^{2,0}(X)={\mathbb{C}}\omega_{X}$ for some nowhere vanishing holomorphic two-form $\omega_{X}$ . If $X$ is projective, then $S_{X}$ is nondegenerate of signature $(1,r_{X}-1)$ . In this case, its orthogonal complement $T_{X}=(S_{X})^{\perp}\subset H^{2}(X,{\mathbb{Z}})$ is the transcendental lattice , of signature $(2,20-r_{X})$ . [...]
  § 2B. Moduli of marked unpolarized K3s: The basic reference here is [ ast85 ] . Let $X$ be a K3 surface. A marking is an isometry $\phi\colon H^{2}(X,{\mathbb{Z}})\to L$ . Let ${\mathbb{D}}={\mathbb{P}}\{x\in L_{\mathbb{C}}\mid x\cdot x=0,\ x\cdot\bar{x}>0\},\quad\dim{\mathbb{D}}=20. [...]
  § 3G. The main theorem: Theorem 3.24 . Under the assumption  $(\exists g\geq 2)$ , $R=C_{1}$ is recognizable for $F_{\rho}$ . The stable pair compactification ${\overline{F}}_{\rho}^{\rm slc}$ is a semitoroidal compactification of ${\mathbb{D}}_{\rho}/\Gamma_{\rho}$ . Proof. By Theorem 3.23 , the second statement follows from the first. Let $(X,R)\to(C,0)$ be a Kulikov model with a flat family of divisors $R\subset X$ for which (1) there is an automorphism $\sigma$ on $X^{*}\to C^{*}$ making $(X_{t},\sigma_{t})\in F_{\rho}$ for $t\neq 0$ , (2) $R_{t}\subset{\rm Fix}(\sigma_{t})$ is the fixed component of genus at least $2$ for $t\neq 0$ , and (3) $R_{0}=\lim_{t\to 0}R_{t}$ . By [ AE21 , Prop. 6.12] , it suffices to show that if we make a one-parameter deformation the smoothing of $X_{0}$ into $F_{\rho}$ that keeps $X_{0}$ constant, the limiting curve $R_{0}$ does not deform, up to ${\rm Aut}^{0}(X_{0})$ . The automorphism $\sigma$ on the generic fiber of any smoothing defines a birational automorphism of $X$ . [...]
[4] arXiv:1312.7318v3 | On automorphisms with natural tangent actions on homogeneous parabolic geometries
  We consider automorphisms of homogeneous parabolic geometries with a fixed point. Parabolic geometries carry the distinguished distributions and we study those automorphisms which enjoy natural actions on the distributions at the fixed points. We describe the sets of such automorphisms on homogeneous parabolic geometries in detail and classify, whether there are non--flat homogeneous parabolic geo
  Full text (https://arxiv.org/html/1312.7318v3), excerpts of its own sections:
  § Introduction: In this article, we will investigate automorphisms of Cartan geometries $(\pi:\mathcal{G}\to M,\omega)$ of type $(G,P)$ over a connected smooth manifold that have fixed points and a natural tangent actions at that points. The crucial fact we will use is that the choice of a point $u\in\mathcal{G}$ in the fiber over the fixed point allows us to identify such automorphisms with elements of $P$ . In particular, we can view $u$ as a (higher order) frame of $T_{\pi(u)}M$ , and the elements of $P$ then prescribe the action of the automorphisms in this frame. The reduction to the first order frame of $T_{\pi(u)}M$ is then represented by the Lie group homomorphism $P\to Gl(\mathfrak{g}/\mathfrak{p})$ induced by the adjoint action. We would like to investigate automorphisms with natural tangent actions that do not depend on the choice of a preferred frame. In other words, we are interested in the elements that are mapped into the center of the image of the above Lie group homomorphism $P\to Gl(\mathfrak{g}/\mathfrak{p})$ . [...]
  § 1. Structure of parabolic geometries and their automorphisms: Basic facts on Cartan geometries. Before we start to study the parabolic geometries, let us recall several general facts on Cartan geometries of an arbitrary type from [ 1 , 12 ] we will use later. In particular, we discuss the automorphisms with a natural action on $TM$ . In the article, we will always consider a Cartan geometry $(\pi:\mathcal{G}\to M,\omega)$ of type $(G,P)$ over a connected smooth manifold $M$ with the curvature (function) $\kappa:\mathcal{G}\to\wedge^{2}(\mathfrak{g}/\mathfrak{p})^{*}\otimes\mathfrak{g}.$ We denote by ${\rm Aut}(\mathcal{G},\omega)$ the automorphism group of the Cartan geometry $(\pi:\mathcal{G}\to M,\omega)$ . Let us summarize here the crucial facts about ${\rm Aut}(\mathcal{G},\omega)$ we mentioned in the Introduction. Fact The choice of $u\in\mathcal{G}$ provides the inclusion ${\rm Aut}(\mathcal{G},\omega)\to\mathcal{G}$ given by the evaluation of each automorphisms at $u$ . [...]
  § 2. Homogeneous parabolic geometries and automorphisms of type $\Sigma$: Construction of homogeneous parabolic geometries. There is a general way how to construct all homogeneous parabolic geometries, see [ 1 ] or [ 7 ] . We recall the following definition. Definition 4 . Let $(K,H)$ and $(G,P)$ be types of Cartan geometries. Then the pair of maps $(i,\alpha)$ is called an extension of $(K,H)$ to $(G,P)$ if it satisfies the following conditions: (1) $i:H\to P$ is a Lie group homomorphism, (2) $\alpha:\mathfrak{k}\to\mathfrak{g}$ is a linear map extending $T_{e}i:\mathfrak{h}\to\mathfrak{p}$ , (3) $\alpha$ induces an isomorphism $\mathfrak{k}/\mathfrak{h}\rightarrow\mathfrak{g}/\mathfrak{p}$ of vector spaces, (4) ${\rm Ad}_{i(h)}\circ\alpha=\alpha\circ{\rm Ad}_{h}$ holds for all $h\in H$ . Each extension $(i,\alpha)$ determines the extension functor $\mathcal{F}_{\alpha}$ from the category of Cartan geometries of type $(K,H)$ to the category of Cartan geometries of type $(G,P)$ . [...]
  § 3. Homogeneous parabolic geometries and automorphisms of type $\Sigma_{J}$: Description of $\Sigma_{J}$ and structure of $Z(G_{0})$ . We focus here on types $\Sigma_{J}$ of automorphisms with a natural action on $T^{-1}M$ . In particular, we describe the set $\Sigma_{J}$ for $J\in Z(\underline{{\rm Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))$ in detail. Proposition 3.1 . For the pair $(G,P)$ , there is a bijection between actions $J\in Z(\underline{{\rm Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))$ and elements $s_{J}\in Z(G_{0})$ . [...]
[5] arXiv:2412.04250v2 | A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product
  We give a concise presentation for the group of pure symmetric outer automorphisms of a given splitting of a free product $G_{1}\ast\dots\ast G_{n}$. These are the (outer) automorphisms which preserve the conjugacy classes of the free factors $G_{i}$. This is achieved by considering the action of these automorphisms on a particular subcomplex of `Outer Space', which we show to be simply connected.
  Full text (https://arxiv.org/html/2412.04250v2), excerpts of its own sections:
  § Main Result: We follow the methods of Armstrong, Forrest, and Vogtmann [ 2 ] to give a concise presentation for the group of pure symmetric outer automorphisms of a given splitting $G_{1}\ast\dots\ast G_{n}$ of free product $G$ , denoted $\out(G;G_{1},\dots,G_{n})$ . In our case, we have a ‘strict fundamental domain’ for the action of $\out(G;G_{1},\dots,G_{n})$ , so can apply a more straightforward theorem of Brown [ 5 , Theorem 3] to extract our presentation, given below: {restatable*} thmpresentation Let $G_{1}\ast\dots\ast G_{n}$ be a free splitting of a group $G$ where each $G_{i}$ is non-trivial and $n\geq 5$ . For $i\in[n]:=\{1,\dots,n\}$ and $j\in[n]-\{i\}$ , let $f_{i_{j}}:G_{i}\to G_{i_{j}}$ be group isomorphisms, and for $g\in G_{i}$ let $\ad_{G_{i}}(g)$ be the inner automorphism $x\mapsto g^{-1}xg$ of $G_{i}$ . Then the group $\out(G;G_{1},\dots,G_{n})$ is generated by the $n(n-1)$ groups $G_{i_{j}}\cong G_{i}$ and $\Phi=\prod_{i=1}^{n}\aut(G_{i})$ , subject to relations: 1. $[f_{i_{j}}(g),f_{i_{k}}(h)]=1$ $\forall g,h\in G_{i}$ , for all $i\in[n]$ , $j,k\in[n]-\{i\}$ 2. [...]
  § 1.2 Key Theorems: We will later make repeated use of the Seifert–van Kampen Theorem. As our simplicial complexes are all closed, and we usually only care about closed subcomplexes of these, we will use a ‘closed version’ of the theorem. Such a theorem can be found in some undergraduate Algebraic Topology notes, such as [ 20 ] delivered by H. Wilton at the University of Cambridge. Theorem 1.2.1 (Seifert–Van Kampen (Closed Version)) . For closed sets $A$ and $B$ with $A$ , $B$ , and $A\cap B$ path-connected and such that there exist open sets $U\subset A$ and $V\subset B$ with $A\cap B$ a (strong) deformation retract of both $U$ and $V$ , we have that the diagram: is a pushout, where $i_{A}:A\cap B\hookrightarrow A$ , $i_{B}:A\cap B\hookrightarrow B$ , $j_{A}:A\hookrightarrow A\cup B$ , and $j_{B}:B\hookrightarrow A\cup B$ are inclusion maps. We will abuse notation and abbreviate this by writing: $\pi_{1}(A\cup B)\cong\pi_{1}(A)\ast_{\pi_{1}(A\cap B)}\pi_{1}(B)$ Remark . [...]
  § 2.3 The Action of $\outs(G)$ on $\mathcal{C}_{n}$ and its Fundamental Domain $\mathcal{D}_{n}$: By considering the action of $\outs(G)$ on our complex $\mathcal{C}_{n}$ , there is a natural idea of a quotient of $\mathcal{C}_{n}$ (two points are equivalent if they are in the same $\outs(G)$ -orbit). We can then pick a ‘fundamental domain’ $\mathcal{D}_{n}$ for the action by choosing a lift of this quotient in $\mathcal{C}_{n}$ . We begin by defining the action of $\outs(G)$ on the 0-skeleton $\mathcal{C}_{n}^{(0)}$ of $\mathcal{C}_{n}$ , and then extend this to an action on the full complex $\mathcal{C}_{n}$ . Definition 2.3.1 (Action of $\outs(G)$ on $\mathcal{C}_{n}^{(0)}$ ) . Let $[\psi]\in\outs(G)$ have representative $\psi\in\aut_{\mathfrak{S}}(G)$ and let $T$ be a point in $\mathcal{C}_{n}^{(0)}$ with $\mathfrak{S}$ -labelling $(H_{1},\dots,H_{n})$ . Then $T\cdot[\psi]$ is a graph of groups with the same underlying graph as $T$ and labelling $(\psi(H_{1}),\dots,\psi(H_{n}))$ (where $\psi(H_{i})$ is given by the usual action of $\aut(G)$ on $G$ , noting that $H_{i}\leq G$ ). Remark . [...]
  § 3 Properties of the Fundamental Domain $\mathcal{D}_{n}$: Before proving any structural statements about the fundamental domain $\mathcal{D}_{n}$ , we provide some illustrations to aid in understanding this subcomplex. We describe some of the substructures found within the 1-skeleton $\mathcal{D}_{n}^{(1)}$ of the fundamental domain of $\mathcal{C}_{n}$ . [...]
[6] arXiv:1405.5706v2 | Induced Automorphisms on Irreducible Symplectic Manifolds
  We introduce the notion of induced automorphisms in order to state a criterion to determine whether a given automorphism on a manifold of $K3^{[n]}$ type is, in fact, induced by an automorphism of a $K3$ surface and the manifold is a moduli space of stable objects on the $K3$. This criterion is applied to the classification of non-symplectic prime order automorphisms on manifolds of $K3^{[2]}$ typ
  Full text (https://arxiv.org/html/1405.5706v2), excerpts of its own sections:
  § Introduction: The present paper deals with several questions concerning irreducible holomorphic symplectic manifolds and their automorphisms. All known examples of irreducible symplectic manifolds arise from symplectic surfaces, often as moduli spaces of sheaves on these surfaces. The easiest such example is the Hilbert scheme of $n$ points on a $K3$ surface, constructed by Beauville in [ Beau83 ] . This kind of construction allows to produce several examples of automorphisms on irreducible symplectic manifolds, simply by taking a $K3$ surface with non-trivial automorphism group and considering the induced action on its Hilbert scheme. These kinds of automorphisms are called natural and were studied by Beauville [ Beau83b ] , Boissière [ Boi12 ] and many others. Very few examples of non-natural automorphisms are known, such as those constructed in [ OW13 ] , and a numerical criterion to distinguish between natural and non-natural automorphisms is available only in special cases, see [ BS12 ] and [ Mon13 ] . [...]
  § 1.1 Lattice theory: Let $L$ be an even lattice, the group $A_{L}=L^{\vee}/L$ is called the discriminant group and the quadratic form of $L$ induces a form $q_{A_{L}}$ with values in $\mathbb{Q}/2\mathbb{Z}$ . The length of $A_{L}$ is denoted by $l(A_{L})$ . If $X$ is an irreducible symplectic manifold, we denote by $A_{X}$ the discriminant group of the lattice $H^{2}(X,\mathbb{Z})$ . An overlattice of $L$ is any lattice $M\supset L$ such that $M/L$ is torsion. An embedding $L\hookrightarrow M$ is primitive if the quotient $M/L$ has no torsion. The divisor of $v\in L$ , denoted $div(v)$ , is the positive integer $n$ such that $(v,L)=n\mathbb{Z}$ . If $L$ is a lattice, we denote with $L(n)$ a lattice with the same structure as $\mathbb{Z}$ module but with quadratic form multiplied by $n$ . We denote with $A_{n}$ , $D_{n}$ and $E_{n}$ the positive definite lattices associated to the corresponding Dynkyn diagrams. [...]
  § 1.2 Useful notions on irreducible symplectic manifolds: Here we gather several known results on irreducible symplectic manifolds. Many of these results are taken from the survey of Huybrechts [ Huy01 ] . Definition 1.9 . A Kähler manifold $X$ is called an irreducible holomorphic symplectic manifold (short: an irreducible symplectic manifold) if the following hold: $\bullet$ $X$ is compact. $\bullet$ $X$ is simply connected. $\bullet$ $H^{2,0}(X)=\mathbb{C}\sigma_{X}$ , where $\sigma_{X}$ is an everywhere non-degenerate symplectic 2-form. There is the equivalent, but more differential geometric notion of hyperkähler manifold. In this article we keep with irreducible symplectic manifolds and refer the interested reader to the literature for a comparison of the two notions. There are not many known examples of irreducible symplectic manifolds and for a long time the only known ones were $K3$ surfaces (which are the only examples in dimension 2) and two families of examples given by Beauville [ Beau83 ] : Example 1.10 . Let $S$ be a $K3$ surface and let $S^{(n)}$ be its $n$ -th symmetric product. [...]
  § 1.3 Moduli of irreducible symplectic manifolds and the Torelli problem: Lemma 1.13 Let $X$ be an irreducible symplectic manifold with Kähler class $\omega$ and symplectic form $\sigma_{X}$ . Then there exists a family $\begin{array}[]{rcc}TW_{\omega}(X)&:=&X\times\mathbb{P}^{1}\\ &&\downarrow\\ \{(a,b,c)\,\in\,\mathbb{R}^{3},\,a^{2}+b^{2}+c^{2}=1\}=S^{2}&\cong&\mathbb{P}^{1}\end{array}$ called Twistor space such that $TW_{\omega}(X)_{(a,b,c)}\cong X$ with complex structure given by the Kähler class [...]
[7] arXiv:1909.00765v2 | Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$
  We show the existence of automorphisms $F$ of $\mathbb{C}^{2}$ with a non-recurrent Fatou component $Ω$ biholomorphic to $\mathbb{C}\times\mathbb{C}^{*}$ that is the basin of attraction to an invariant entire curve on which $F$ acts as an irrational rotation. We further show that the biholomorphism $Ω\to\mathbb{C}\times\mathbb{C}^{*}$ can be chosen such that it conjugates $F$ to a translation $(z,
  Full text (https://arxiv.org/html/1909.00765v2), excerpts of its own sections:
  § 1. Introduction: When studying the behaviour of iterates of a holomorphic endomorphism $F$ of $\mathbb{C}^{d}$ , $d\geq 1$ , one of the basic objects of interest is the Fatou set of all points in $\mathbb{C}^{d}$ that admit a neighbourhood on which $\{F^{n}\}_{n\in\mathbb{N}}$ is normal. The connected components of the Fatou set are called the Fatou components of $F$ . They can be thought of as maximal connected subsets of $\mathbb{C}^{2}$ on which the behaviour of $F$ is roughly the same. A Fatou component $V$ of $F$ is invariant , if $F(V)=V$ . It is recurrent if it contains an accumulation point of an orbit $\{F^{n}(p)\}_{n\in\mathbb{N}}$ for some $p\in V$ and non-recurrent or transient otherwise. $V$ is attracting to a point $p$ in the closure $\overline{V}$ of $V$ if all orbits starting in $V$ converge to $p$ . In one variable, an invariant Fatou component $V$ of an entire function is either attracting to a point in $\overline{V}$ , or all orbits in $V$ escape to $\infty$ ( $V$ is a Baker domain ), or $V$ is a rotation domain , i.e. [...]
  § Outline: In Section 2 , we construct our family of automorphisms. We first use results from [ Var01 ] and [ Var00 ] to show the existence of automorphisms $\check{F}$ of the form ( 1.2 ). We then blow up at the origin and observe that the lift $F$ of $\check{F}$ leaves invariant the proper transform of the $z$ -axis. Removing this subvariety from the blow-up leaves us with a copy of $\mathbb{C}^{2}$ on which $F$ acts as an automorphism. In Section 3 we use estimates on orbit behaviour in the Fatou component $\check{\Omega}$ to show that the proper transform $\Omega$ is still a Fatou component of $F$ . Then we establish coordinates on $\Omega$ conjugating $F$ to $(z,w)\mapsto(z+1,w)$ in Section 4 , which we use in Section 5 to identify the images of limit maps.
  § Conventions: We use the following notations for asymptotic behaviour (as $x\to x_{0}$ ): • $f(x)=O(g(x))$ , if $\limsup_{x\to x_{0}}\frac{|f(x)|}{|g(x)|}=C • $f(x)\approx g(x)$ , if $f(x)=O(g(x))$ and $g(x)=O(f(x))$ , • $f(x)\sim g(x)$ , if $\lim_{x\to x_{0}}\frac{|f(x)|}{|g(x)|}=1$ .
  § 2. The family of automorphisms: In this section we show that the automorphisms with non-recurrent Fatou components biholomorphic to $\mathbb{C}\times\mathbb{C}^{*}$ and attracted to the origin constructed in [ BRS ] can be chosen such that their lift to the blow-up at the origin can be restricted to an automorphism of a subset biholomorphic to $\mathbb{C}^{2}$ . We first recall the framework of [ BRS ] : Let $F_{{\rm N}}$ be a germ of biholomorphisms of $\mathbb{C}^{2}$ at the origin given by $F_{{\rm N}}(z,w):=\lparen\lambda z,\overline{\lambda}w\rparen\cdot\Big\lparen 1-\frac{zw}{2}\Big\rparen,$ where $\lambda\in S^{1}$ is Brjuno, i.e. (2.1) $-\sum_{\nu=1}^{\infty}2^{-\nu}\log\omega(2^{\nu}) where $\omega(m):=\min\{\lvert\lambda^{k}-\lambda\rvert\mid 2\leq k\leq m\}$ for $m\geq 2$ . Definition 2.1 . For $r>0$ , $\theta\in(0,\pi/2)$ , and $\beta\in(0,1/2)$ let $\displaystyle W(\beta)$ $\displaystyle:=\{(z,w)\in\mathbb{C}^{2}\mid|z| $\displaystyle S(r,\theta)$ $\displaystyle:=\{u\in\mathbb{C}\mid|\arg(u)| and $\check{B}(r,\theta,\beta):=\{(z,w)\in W(\beta)\mid zw\in S(r,\theta)\}. [...]
  § 3. The Fatou component: In the following we will examine the dynamics of $F$ near the invariant curve $\mathcal{C}$ and on the lifted local basin $B$ and show that the corresponding global basin $\Omega:=\Pi^{-1}(\check{\Omega})=\bigcup_{n\in\mathbb{N}}F^{-n}(B)$ is still a Fatou component. [...]
[8] QNFO: Automorphisms and Scaling Transformations: A Re-Entry Analysis Across Algebraic, Geometric, and Dynamical Settings
  We examine the relationship between automorphisms — structure-preserving self-maps of algebraic, geometric, or dynamical objects — and scaling transformations, i.e., dilations that rescale coordinates, dimensions, or metrics without changing the underlying structure type. Motivated by a re-entry prompt asking whether automorphisms "relate to scaling transformations," we organize twelve supplied so
  Full text (https://papers.qnfo.org/papers/automorphisms-and-scaling-transformations-a-re-entry-analysis-across-algebraic-g), excerpts of its own sections:
  § 1. Introduction: An automorphism of a mathematical object $X$ is an isomorphism from $X$ to itself; the set of all automorphisms forms a group $\mathrm{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S_\lambda$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$. [...]
  § 2. Background and Related Work: We discuss all twelve bibliography entries in their supplied numbering. Entries [1]–[8] are arXiv mathematics papers whose supplied summaries we paraphrase strictly; entries [9]–[12] are QNFO corpus documents [...]
  § 5. Results: We report only quantities computed in Section 4, plus clearly labeled projections. **R1 (Shear rescaling, exact).** Conjugation of $\phi_{\mathrm{uni}}(x,y) = (x+y,\,y)$ by $D = \mathrm{diag}(2,3)$ yields $D\phi_{\mathrm{uni}}D^{-1}(x,y) = (x + \tfrac{2}{3}y,\, y)$; the shear coefficient maps $c = 1 \mapsto c' = \tfrac{2}{3} \approx 0.666667$. General rule: $c' = \frac{\lambda_1}{\lambda_2} c$ (Section 4.2). **R2 (Scalar-dilation triviality, exact).** For every scalar $\lambda > 0$: $S_\lambda \phi_{\mathrm{uni}} S_\lambda^{-1} = \phi_{\mathrm{uni}}$ and $S_\lambda R_\theta S_\lambda^{-1} = R_\theta$. Scalar dilations centralize both model automorphisms (Section 4.3). **R3 (Ring-count growth, from [2]).** $\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}} = \frac{35}{7} = 5$; per-dimension-doubling exponent $g = \log_2 5 \approx 2.321928$ (Section 4.4). **R4 (Dimension and density, from [2]).** $D_3 = 8$, $D_4 = 16$, dimension growth factor $2$; $\delta(\mathbb{O}) = 0.875$, $\delta(\mathbb{S}) = 2.1875$, density growth factor $2.5$ exactly (Section 4.4). [...]
  § 6. Discussion: **Limitations.** The central limitation of this study is the nature of its source base: the supplied material consists of abstracts, several of them truncated mid-sentence, and four corpus entries ([9]–[12]) supplied with titles only. Every structural claim we make about a cited work is therefore restricted to what its supplied summary explicitly states, and entries [9]–[12] contribute nothing beyond their titles. In particular: the second branch of the dichotomy of [1] is unavailable to us; the classification content of [4] and [7] is truncated; the abstract of [2] supplies two integer counts but no statement about dimension doubling, which we had to import as a labeled standard assumption (Section 3.3); and the abstract of [6] states its two hypotheses and its goal but no explicit bound, so we supply none. [...]
  § 7. Conclusion: We asked whether automorphisms relate to scaling transformations and answered with a uniform three-part conjugation test — normalization, centralization, parameter rescaling — applied to a fixed twelve-entry bibliography. The quantitative core is explicit: conjugation by the anisotropic dilation $D = \mathrm{diag}(2,3)$ rescales the shear coefficient of $\phi_{\mathrm{uni}}(x,y) = (x+y,\,y)$ by $\lambda_1/\lambda_2 = 2/3$, while scalar dilations centralize both model automorphisms, and the Cayley--Dickson step from octonions to sedenions multiplies the count of associative quaternion rings by $35/7 = 5$ and their density per real dimension by $2.5$. Scaling therefore relates to automorphisms chiefly through conjugation: trivially for isotropic scalings, and by computable ratio rules for anisotropic ones. The framework's quantitative content is confined to linear models and to the two supplied integer counts of [2]; its remaining connections are qualitative or explicitly labeled hypotheses and projections, each stated with its falsification condition in Section 6.
[9] QNFO: ULTRAMETRIC PHYSICS
  This research plan presents a framework for ultrametric physics based on fundamental scaling ratios rather than anthropocentric number representations. The core insight: physical reality is described by dimensionless scaling ratios (π, φ, e, α, etc.) that operate on hierarchical discrete structures, independent of any base representation (decimal, binary, etc.) or continuum assumptions. Key Innova
  Full text (https://papers.qnfo.org/papers/ultrametric-physics-m1-ratio-based-valuation-theory), excerpts of its own sections:
  § RESEARCH PLAN: **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062) **DOI:** https://papers.qnfo.org/papers **Date:** 2026-04-06 **Version:** 2.0
  § EXECUTIVE: SUMMARY: THE RATIO-CENTRIC PARADIGM This research plan presents a framework for ultrametric physics based on **fundamental scaling ratios** rather than anthropocentric number representations. The core insight: physical reality is described by **dimensionless scaling ratios** (π, φ, e, α, etc.) that operate on hierarchical discrete structures, independent of any base representation (decimal, binary, etc.) or continuum assumptions. **Key Innovations:** 1. **Ratio-Based Valuations**: Scaling bases q ∈ ℝ⁺ as pure ratios, not decimal numbers 2. **Base-Invariant Formulations**: All mathematics independent of representation (decimal/binary/etc.) 3. **Hierarchical Discrete Reality**: Bruhat-Tits trees as fundamental substrate 4. **Unified Framework**: Addressing quantum computation, quantum gravity, and measurement theory simultaneously 5. **Constrained Methodology**: 0.5 FTE PI, LLM-assisted, open dissemination at papers.qnfo.org/ResearchGate
  § Resources:: **Personnel**: 0.5 FTE Principal Investigator (20 hrs/week) **Tools**: Large Language Models (DeepSeek, Google Gemini) **Computation**: Python execution within LLM chat threads **Output Format**: Markdown with MathJax → Obsidian → PDF **Dissemination**: the QNFO archive (DOI), ResearchGate, social media **Excluded**: Experimental facilities, arXiv, LaTeX, formal peer review
  § Research Protocol:: **Module Execution**: Each module as single LLM chat thread **Document Generation**: Markdown with MathJax, base-independent formulations **Code Implementation**: Python for simulations/toy models (executable in chat) **Archiving**: the QNFO archive deposit with DOI, ResearchGate upload **Dissemination**: Social media with the QNFO archive links
  § RESEARCH MODULES (12: MODULES) *Prioritized for consistency and quality control based on existing progress and monograph “Ultrametric Physics: From Discrete Hierarchical Geometry to Intrinsic Fault Tolerance and Quantum Gravity” (0.10.md)*
  § Module 1:: Ratio-Based Valuation Theory **Core Concept**: Scaling ratios q as fundamental, not integer primes **Research Questions:** 1. How to formalize valuations with arbitrary scaling ratios q ∈ ℝ⁺? 2. What algebraic structures emerge when q is a geometric ratio (π, φ, e)? 3. How do scaling ratios generate continuous appearances from discrete structures? [...]
  § CONCLUSION: THE: RATIO-CENTRIC PARADIGM This research plan presents a focused, executable program for developing ultrametric physics based on fundamental scaling ratios. By rejecting anthropocentric mathematical conventions (integer primes, real continuum, base-10 decimals) and focusing on ratio-based hierarchical structures, the framework offers a unified approach to quantum computation, quantum gravity, and consciousness. The constrained methodology (0.5 FTE PI, LLM-assisted, open dissemination) demonstrates that significant foundational progress is possible without traditional resources. The 12-module structure ensures consistency and quality control while covering the essential components of the framework. **Ultimate Goal**: A **paradigm shift** from number-based to ratio-based physics, developed with strict empirical discipline and rigorous mathematical foundations.