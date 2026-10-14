# Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure

## Abstract

Automorphism groups encode the symmetries of algebraic varieties, non-associative algebras, parabolic geometries, group splittings, and holomorphic dynamical systems, but the literature treats each setting with its own tools, and practitioners lack a uniform test for when a rescaling of coordinates, dimensions, or metrics acts nontrivially on automorphism parameters. This gap matters concretely: normalization and reduction routines in computer algebra, and classification arguments that quotient by scaling symmetries, silently assume that dilations either preserve or trivially commute with the automorphisms at hand. We adopt the conjugation test of a prior re-entry analysis [8] — normalization, centralization, and parameter rescaling — and extend it with new explicit derivations across nine settings. Conjugation of the planar shear $\phi(x,y)=(x+y,y)$ by the anisotropic dilation $D=\mathrm{diag}(2,3)$ rescales the shear coefficient by $\lambda_1/\lambda_2=2/3\approx 0.666667$, while scalar dilations centralize both the shear and rotations exactly. In the Cayley–Dickson tower, the step from octonions to sedenions multiplies the count of associative quaternion rings from $7$ to $35$, a factor of $5$, i.e., $\log_2 5\approx 2.321928$ per dimension-doubling step, while ring density per real dimension grows by exactly $2.5$ (from $0.875$ to $2.1875$). We further derive the two-ray structure of the pseudo-effective cone at Picard number two with $\mathrm{ord}(g^*)=2$ for cone-permuting maps, a generator count of $n(n-1)+1$ families for pure symmetric outer automorphisms at $n\geq 5$ free factors, and Euler-totient rigidity $\varphi(2)=1$ for order-two discrete scalings. The results give a computable, falsifiable rule — ratio rescaling for anisotropic dilations, triviality for isotropic ones — that practitioners can apply before invoking scaling arguments in classification or normalization pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by scalings, or running a normalization algorithm that rescales coordinates, they must know whether the rescaling changes the automorphisms of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting — one body of technique for automorphism groups of varieties, another for non-associative algebras, another for holomorphic dynamics — with no shared criterion, so a practitioner moving between settings must re-derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed.

This paper supplies such a test and demonstrates it with full arithmetic. An automorphism of a mathematical object $X$ is an isomorphism from $X$ to itself; the automorphisms form a group $\mathrm{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S_\lambda$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$ without changing the structure type. The question of how the two notions relate was posed in a prior re-entry analysis [8], which introduced a three-part conjugation test and computed its first instances. We take that framework as the starting point, tighten its derivations, and extend it to settings its predecessor treated only qualitatively, using the full-text content of the underlying papers rather than abstract-level statements alone.

The conjugation test asks three questions of a pair $(S,\phi)$ with $S$ a scaling and $\phi\in\mathrm{Aut}(X)$:

1. **Normalization:** does $S\phi S^{-1}$ remain an automorphism, i.e., is $S\,\mathrm{Aut}(X)\,S^{-1}\subseteq\mathrm{Aut}(X)$?
2. **Centralization:** does $S$ commute with $\phi$, i.e., is $S\phi=\phi S$?
3. **Parameter rescaling:** when automorphisms come in families indexed by numerical parameters (shear coefficients, rotation angles, orders), does conjugation by $S$ act on those parameters by a computable rule?

Question 3 is where scaling becomes quantitative. We show that conjugation by the anisotropic dilation $D=\mathrm{diag}(2,3)$ rescales the shear coefficient of the planar unipotent map $\phi(x,y)=(x+y,y)$ by exactly $2/3$, that scalar dilations act trivially on both shears and rotations, and that in the Cayley–Dickson tower the count of associative quaternion rings grows from $7$ (octonions) to $35$ (sedenions) — a factor of $5$, or $\log_2 5\approx 2.321928$ per dimension-doubling step — while ring density per real dimension grows by exactly $2.5$. We also derive, from the full text of the underlying papers, the two-ray cone structure and the involution property $\mathrm{ord}(g^*)=2$ at Picard number two, the generator structure $n(n-1)$ factor-permutation generators plus one product of automorphism groups for pure symmetric outer automorphisms, and the totient obstruction $\varphi(2)=1$ that makes order-two discrete scalings rigid.

Our contributions are:

- A tightened derivation of the conjugation test's central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_1/\lambda_2$ of dilation factors while scalar dilations centralize shears and rotations exactly (Sections 3 and 4.2–4.3).
- A growth analysis of associative structure in the Cayley–Dickson tower, with the factor $5$, the exponent $\log_2 5\approx 2.321928$, and the density ratio $2.5$ all computed step by step from the ring counts $7$ and $35$ reported in [2] (Section 4.4).
- New derivations connecting scaling to cone combinatorics at Picard number two, including the involution $\mathrm{ord}(g^*)=2$ for maps permuting the two extremal rays of the pseudo-effective cone, from the proof machinery of [1] (Section 4.5).
- A generator-count derivation for pure symmetric outer automorphisms of free-product splittings, $n(n-1)$ conjugation generators plus $\prod_i\mathrm{Aut}(G_i)$, from the presentation of [5] (Section 4.6).
- A discrete-scaling rigidity result via Euler's totient, $\varphi(2)=1$, with its consequence for the Cayley–Dickson doubling step (Section 4.7).
- An explicit statement of limitations, falsification conditions, and the smallest next computations that would de-risk or refute the framework (Sections 6 and 7).

## 2. Background and Related Work

We discuss the nine bibliography entries in their fixed numbering. Each is cited for specific content of its full text.

**[1] Birational automorphism groups of projective varieties of Picard number two (arXiv:1307.5490v2).** This paper extends results of Oguiso on birational or automorphism groups, and of Lazić–Peternell on the Morrison–Kawamata cone conjecture, from Calabi–Yau manifolds of Picard number two to arbitrary singular varieties and to klt Calabi–Yau pairs in the broad sense, also of Picard number two. Its introduction defines the group of pseudo-automorphisms $\mathrm{Bir}_2(X)$ as maps that are isomorphisms outside codimension-two subsets, and the Picard number $\rho(X)=\dim_{\mathbb{R}}\mathrm{NS}(X)\otimes\mathbb{R}$ from the Néron–Severi group. Its proof section shows that at Picard number two the pseudo-effective cone $\overline{\mathrm{Eff}}(X)$ is generated by two rays $\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2]$, and that a map $g$ permuting the extremal rays satisfies $g^*f_1=af_2$, $g^*f_2=bf_1$ with $a,b>0$; since $g^*$ preserves the integral lattice, $\deg(g^*)=\pm 1$, hence $ab=1$ and $\mathrm{ord}(g^*)=2$. The headline dichotomy is that for $X$ with only klt singularities and not a complex torus, either $\mathrm{Aut}(X)$ is almost cyclic, or a second alternative holds. The two-ray cone and the induced involution are exactly the structure on which our Section 4.5 computation operates: a two-dimensional cone is the minimal arena in which a scaling of one ray against the other becomes visible.

**[2] Automorphisms of Sedenions (arXiv:2512.07210v3).** This paper extends the octonion calibration in Clifford algebra to two related sedionion calibrations and reports that octonions consist of seven associative quaternion rings while sedenions have $35$. Its introduction lays out the Cayley–Dickson series $\mathrm{A}_N$ with $n=2^N$ basis elements generated by $N$ generators at each level, starting from $\mathrm{A}_0\cong\mathbb{R}$, $\mathrm{A}_1\cong\mathbb{C}$, $\mathrm{A}_2\cong\mathbb{H}$, $\mathrm{A}_3\cong\mathbb{O}$, $\mathrm{A}_4\cong\mathbb{S}$, and notes that all $\mathrm{A}_N$ for $N\geq 4$ have zero divisors, hence are power-associative but cannot be normed algebras. Its summary section reports that the mechanism for deriving automorphisms of octonions from the calibration extends to sedenions through the Sharp algebras and is more complicated than for octonions and quaternions, and it conjectures that such calibrations exist for all Cayley–Dickson algebras. Crucially for us, the dimension law $n=2^N$ is stated in the paper's own introduction, so the density computation of Section 4.4 does not rest on an imported assumption: the octonion-to-sedenion step is the passage $\mathrm{A}_3\to\mathrm{A}_4$, from dimension $2^3=8$ to $2^4=16$, with ring counts $7$ and $35$.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism (arXiv:2110.13834v2).** This paper constructs a modular compactification via stable slc pairs for moduli spaces of K3 surfaces with a nonsymplectic group of automorphisms, under the assumption that some combination of fixed loci defines an effective big divisor, and proves the compactification is semitoroidal. Its introduction defines a non-symplectic automorphism as one of finite order $n>1$ acting on the holomorphic two-form by $\sigma^*(\omega_X)=\zeta_n\omega_X$ with $\zeta_n=\exp(2\pi i/n)$ a primitive $n$-th root of unity, and records that the possible orders are the $n$ whose Euler function satisfies $\varphi(n)\leq 20$ with the single exception $n\neq 60$. This is a direct instance of scaling-visible arithmetic: the automorphism acts on a one-dimensional complex space of forms by multiplication by a root of unity, a discrete "phase scaling," and the admissible orders are bounded by a totient condition. Our Section 4.7 totient computations give the same function a second role, as the count of rescalings of a discrete scaling parameter. The paper's main theorem (Theorem 3.24) further shows the stable pair compactification $\overline{F}_\rho^{\mathrm{slc}}$ is semitoroidal over the period domain quotient $\mathbb{D}_\rho/\Gamma_\rho$, connecting automorphism data to cone-like (toroidal) geometry as in [1].

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries (arXiv:1312.7318v3).** This paper studies automorphisms of Cartan geometries $(\pi:\mathcal{G}\to M,\omega)$ of type $(G,P)$ that have fixed points and natural tangent actions there. Its introduction establishes the key mechanism: choosing a point $u$ in the fiber over the fixed point identifies such automorphisms with elements of the parabolic subgroup $P$, viewed as a higher-order frame of $T_{\pi(u)}M$, and the "natural" actions are those mapped into the center of the image of the Lie group homomorphism $P\to\mathrm{Gl}(\mathfrak{g}/\mathfrak{p})$ induced by the adjoint action. Its Section 3 gives a bijection (Proposition 3.1) between actions $J$ in the centralizer of the adjoint image on $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_J$ of the center $Z(G_0)$. This is the precise geometric locus where scaling meets automorphisms: parabolic geometries carry graded tangent decompositions $\mathfrak{g}=\mathfrak{g}^{-k}\oplus\cdots\oplus\mathfrak{g}^{-1}\oplus\mathfrak{g}^0$, and the center of $G_0$ acts on each graded piece by a dilation. The centralizer condition of [4] is therefore a centralization statement (question 2 of the conjugation test) at the level of graded pieces, and we use it in Section 4.8 to interpret our linear centralization results geometrically.

**[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product (arXiv:2412.04250v2).** This paper gives a concise presentation for the group $\mathrm{Out}(G;G_1,\dots,G_n)$ of pure symmetric outer automorphisms of a free-product splitting $G_1*\cdots *G_n$ — the outer automorphisms preserving the conjugacy classes of the free factors — by studying their action on a subcomplex of Outer Space shown to be simply connected. Its main result states that for $n\geq 5$ the group is generated by the $n(n-1)$ groups $G_{i_j}\cong G_i$ (realizing isomorphisms between factors) together with $\Phi=\prod_{i=1}^n\mathrm{Aut}(G_i)$, subject to explicit relations including commutativity $[f_{i_j}(g),f_{i_k}(h)]=1$ within each factor. Its Section 2.3 describes the action on the $0$-skeleton: a vertex with labelling $(H_1,\dots,H_n)$ is sent to the labelling $(\psi(H_1),\dots,\psi(H_n))$, i.e., the symmetric condition acts by permuting $n$ labelled objects. The count $n(n-1)$ is the arithmetic of ordered pairs of distinct factors — the number of ways to move one factor's content into another — and we compute it explicitly in Section 4.6 as the permutation-scope arithmetic of the symmetric condition.

**[6] Induced Automorphisms on Irreducible Symplectic Manifolds (arXiv:1405.5706v2).** This paper introduces induced automorphisms to state a criterion determining whether an automorphism of a manifold of $K3^{[n]}$ type is induced by an automorphism of the underlying K3 surface, when the manifold is a moduli space of stable objects on that surface; the criterion is applied to classify non-symplectic prime order automorphisms on manifolds of $K3^{[2]}$ type. Its introduction distinguishes natural automorphisms (induced by the action on the K3, studied by Beauville, Boissière and others) from the very few known non-natural ones, noting that a numerical criterion to separate the two classes is available only in special cases. Its Section 1.2 records the definition of irreducible symplectic manifolds (compact, simply connected, with $H^{2,0}=\mathbb{C}\sigma_X$) and the Beauville examples from symmetric products. For our framework this is a descent statement: an automorphism at one level of a hierarchy is explained by one at a lower level, structurally parallel to how a scaling of a hierarchy relates its levels. We use it in Section 4.8 as the qualitative counterpart of the quantitative ratio rule.

**[7] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^2$ (arXiv:1909.00765v2).** This paper shows the existence of automorphisms $F$ of $\mathbb{C}^2$ with a non-recurrent Fatou component $\Omega$ biholomorphic to $\mathbb{C}\times\mathbb{C}^*$ that is the basin of attraction to an invariant entire curve on which $F$ acts as an irrational rotation, and that the biholomorphism can be chosen to conjugate $F$ to the translation $(z,w)\mapsto(z+1,w)$. Its outline section describes the construction: automorphisms $\check{F}$ built from Brjuno rotation germs $F_{\mathrm{N}}(z,w)=(\lambda z,\overline{\lambda}w)\cdot(1-zw/2)$ with $\lambda\in S^1$ Brjuno, lifted to a blow-up at the origin, with the proper transform of the $z$-axis removed to leave a copy of $\mathbb{C}^2$ on which $F$ acts. Its Section 3 establishes that the lifted global basin $\Omega=\Pi^{-1}(\check{\Omega})=\bigcup_{n\in\mathbb{N}}F^{-n}(B)$ remains a Fatou component. This is the most dynamically explicit entry: the asymptotic behavior is a rotation on an invariant curve and a translation in adapted coordinates, precisely the two map types for which our scalar-dilation centralization computation of Section 4.3 is trivial, making [7] the natural anchor for the centralization branch of the framework.

**[8] Automorphisms and Scaling Transformations: A Re-Entry Analysis Across Algebraic, Geometric, and Dynamical Settings (papers.qnfo.org).** This prior analysis introduces the conjugation test used here — normalization, centralization, parameter rescaling — and reports its first quantitative instances: conjugation of the shear $\phi(x,y)=(x+y,y)$ by $D=\mathrm{diag}(2,3)$ rescales the shear coefficient to $2/3$, scalar dilations centralize both model automorphisms, and the octonion-to-sedenion ring-count ratio is $35/7=5$ with density ratio $2.5$. Its discussion section flags that its own quantitative content was confined to linear models and to the two integer ring counts, with the remaining connections qualitative. We adopt its framework wholesale, tighten its derivations (in particular, the density computation no longer needs an imported dimension assumption, because [2] states the dimension law $n=2^N$ directly), and extend the derivations to settings it treated only qualitatively.

**[9] QNFO: ULTRAMETRIC PHYSICS (papers.qnfo.org).** This research plan proposes a framework for ultrametric physics based on fundamental scaling ratios rather than anthropocentric number representations: physical reality described by dimensionless scaling ratios operating on hierarchical discrete structures, with ratio-based valuations using scaling bases $q\in\mathbb{R}^+$ as pure ratios, base-invariant formulations independent of decimal or binary representation, and Bruhat–Tits trees as the fundamental substrate. Its Module 1 poses the formalization of valuations with arbitrary scaling ratios $q\in\mathbb{R}^+$ and the question of which algebraic structures emerge when $q$ is a geometric ratio. For this paper it supplies the motivating external picture: a research program in which scaling ratios, not coordinates, are the primary objects — the same primacy of ratios that our conjugation rule $c'=(\lambda_1/\lambda_2)c$ exhibits internally. We use it only for this programmatic connection and note in Section 6 that integrating its hierarchical structures into the conjugation framework is open.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ with automorphism group $\mathrm{Aut}(X)$, and let $\mathcal{S}(X)$ be a distinguished class of self-bijections of $X$ called **scalings**: maps $S:X\to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate, a dimension grading) without changing the structure type. We use two concrete families:

- **Scalar dilations** $S_\lambda(x)=\lambda x$ on a vector space or algebra, with $\lambda\in\mathbb{R}_{>0}$ or $\mathbb{C}^*$.
- **Anisotropic dilations** $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$ on $\mathbb{R}^n$ or $\mathbb{C}^n$, with $\lambda_i>0$ and not all equal.

The conjugation test applied to a pair $(S,\phi)$, $S\in\mathcal{S}(X)$, $\phi\in\mathrm{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1}\in\mathrm{Aut}(X)\,? \qquad
\text{(C)}\quad S\phi=\phi S\,? \qquad
\text{(P)}\quad \text{does } S(\cdot)S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism; the interesting content arises when $S$ is not an automorphism of the particular object but the conjugate still preserves the structure type. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi)=\{S\in\mathcal{S}(X):S\phi=\phi S\}$. Question (P) is the quantitative core, carried out in Section 4.

### 3.2 Model automorphisms

Two planar linear maps serve as canonical test automorphisms of $\mathbb{R}^2$:

$$
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y), \qquad
\phi_{\mathrm{rot}}(x,y)=(\cos\theta\, x-\sin\theta\, y,\;\sin\theta\, x+\cos\theta\, y),
$$

a unipotent shear with coefficient $c=1$ and a rotation by angle $\theta$. These model the two asymptotic behaviors reported in [7]: the automorphism $F$ acts as an irrational rotation on an invariant entire curve and is conjugate to the translation $(z,w)\mapsto(z+1,w)$ in adapted coordinates on $\Omega\cong\mathbb{C}\times\mathbb{C}^*$.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non-associative setting of [2], the paper reports $N_{\mathrm{oct}}=7$ associative quaternion rings in the octonions and $N_{\mathrm{sed}}=35$ in the sedenions, and its introduction states the dimension law of the Cayley–Dickson series: $\mathrm{A}_N$ has $n=2^N$ basis elements, with octonions $\mathrm{A}_3$ and sedenions $\mathrm{A}_4$. We therefore treat the octonion-to-sedenion passage as one dimension-doubling step with dimensions $2^3=8$ and $2^4=16$, both taken directly from [2]. We define:

- the per-step growth exponent $g=\log_2\!\left(N_{\mathrm{sed}}/N_{\mathrm{oct}}\right)$;
- the ring density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$ carrying $N(A)$ associative quaternion rings, and the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic appears in Section 4.4.

### 3.4 Cone and group-counting derivations

Two further derivation tracks use inputs stated in the full texts of [1] and [5]. From [1]: at Picard number two, the pseudo-effective cone is $\overline{\mathrm{Eff}}(X)=\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2]$, and a map $g$ permuting the extremal rays satisfies $g^*f_1=af_2$, $g^*f_2=bf_1$ with $ab=1$ and $\mathrm{ord}(g^*)=2$. We re-derive these relations and compute the face structure of the two-ray cone. From [5]: the generator statement for $\mathrm{Out}(G;G_1,\dots,G_n)$ at $n\geq 5$ is the $n(n-1)$ factor-conjugation generators plus $\Phi=\prod_i\mathrm{Aut}(G_i)$; we compute $n(n-1)$ for small $n$ and interpret it as ordered-pair counting on the factor set, consistent with the labelling-permutation action on the $0$-skeleton described in [5].

### 3.5 Discrete-scaling rigidity

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling-compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. We evaluate $\varphi$ for small $k$ and connect the case $k=2$ to the Cayley–Dickson doubling ratio. The same totient function bounds admissible orders of non-symplectic K3 automorphisms through the condition $\varphi(n)\leq 20$ recorded in [3], giving the function two distinct roles in the framework.

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

| Quantity | Value | Source |
|---|---|---|
| Associative quaternion rings in octonions | $N_{\mathrm{oct}}=7$ | [2] |
| Associative quaternion rings in sedenions | $N_{\mathrm{sed}}=35$ | [2] |
| Cayley–Dickson dimension law | $\dim\mathrm{A}_N=2^N$; $\mathrm{A}_3=\mathbb{O}$, $\mathrm{A}_4=\mathbb{S}$ | [2], Introduction |
| Anisotropic dilation diagonal entries | $\lambda_1=2$, $\lambda_2=3$ | Chosen here (Section 3.1) |
| Shear coefficient of $\phi_{\mathrm{uni}}$ | $c=1$ | Definition in Section 3.2 |
| Rotation angle | $\theta$ irrational multiple of $\pi$ | Behavior of $F$ in [7] |
| Picard number | $\rho=2$ | [1] |
| Cone ray relations at $\rho=2$ | $g^*f_1=af_2$, $g^*f_2=bf_1$, $ab=1$, $\mathrm{ord}(g^*)=2$ | [1], proof section |
| Generator families for $\mathrm{Out}(G;G_1,\dots,G_n)$ | $n(n-1)$ groups $G_{i_j}$ plus $\Phi=\prod_i\mathrm{Aut}(G_i)$, $n\geq 5$ | [5], main result |
| Totient bound on K3 non-symplectic orders | $\varphi(n)\leq 20$, $n\neq 60$ | [3], Introduction |

No other numerical inputs are used anywhere in this paper.

### 4.2 Conjugation of the shear by an anisotropic dilation

Take $D=\mathrm{diag}(\lambda_1,\lambda_2)=\mathrm{diag}(2,3)$ and $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$. Compute $D\,\phi_{\mathrm{uni}}\,D^{-1}$ step by step:

$$
D^{-1}(x,y)=\left(\frac{x}{\lambda_1},\frac{y}{\lambda_2}\right)=\left(\frac{x}{2},\frac{y}{3}\right),
$$

$$
\phi_{\mathrm{uni}}\!\left(\frac{x}{2},\frac{y}{3}\right)=\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right),
$$

$$
D\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right)=\left(2\left(\frac{x}{2}+\frac{y}{3}\right),\;3\cdot\frac{y}{3}\right)=\left(x+\frac{2}{3}y,\;y\right).
$$

Hence

$$
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y)=\left(x+\frac{\lambda_1}{\lambda_2}\,y,\;y\right)=\left(x+\frac{2}{3}y,\;y\right),
$$

i.e., conjugation rescales the shear coefficient by the ratio of diagonal entries:

$$
c\;\longmapsto\;c'=\frac{\lambda_1}{\lambda_2}\,c=\frac{2}{3}\cdot 1=\frac{2}{3}\approx 0.666667.
$$

In general, for $D=\mathrm{diag}(\lambda_1,\lambda_2)$ the same three lines give $c'=\frac{\lambda_1}{\lambda_2}c$; the computation above is the instance $\lambda_1=2$, $\lambda_2=3$. This is the paper's headline quantitative result: **anisotropic scalings act