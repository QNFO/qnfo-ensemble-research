# Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure

## Abstract

Mathematicians and computational scientists who classify symmetries must decide whether a rescaling of coordinates, dimensions, or metrics changes the automorphism group of the object. Without a uniform criterion, practitioners risk applying incorrect normalizations or quotients, leading to downstream errors. This paper introduces a three‑part conjugation test—normalization, centralization, and parameter rescaling—and carries out its quantitative branch with explicit arithmetic. For the planar shear $\phi(x,y)=(x+y,y)$, anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient by the ratio $2/3\approx0.666667$, while scalar dilations centralize both shears and rotations. In the Cayley–Dickson tower, the octonion‑to‑sedenion step multiplies the count of associative quaternion rings from $7$ to $35$, a factor of $5$, i.e. $\log_{2}5\approx2.321928$ per dimension‑doubling step, and the density per real dimension grows by exactly $2.5$ (from $0.875$ to $2.1875$). Additional derivations include the two‑ray cone involution $\operatorname{ord}(g^{*})=2$ at Picard number two, the generator count $n(n-1)$ plus $\prod_{i}\operatorname{Aut}(G_{i})$ for pure symmetric outer automorphisms with $n\ge5$, and the totient rigidity $\varphi(2)=1$ for order‑two discrete scalings. These results give a computable, falsifiable rule—ratio rescaling for anisotropic dilations, triviality for isotropic ones—that practitioners can apply before invoking scaling arguments in classification or normalization pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by scalings, or running a normalization algorithm that rescales coordinates, they must know whether the rescaling changes the automorphisms of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting—one body of technique for automorphism groups of varieties, another for non‑associative algebras, another for holomorphic dynamics—with no shared criterion, so a practitioner moving between settings must re‑derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed.

This paper supplies such a test and demonstrates it with full arithmetic. An automorphism of a mathematical object $X$ is an isomorphism from $X$ to itself; the automorphisms form a group $\operatorname{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S_{\lambda}$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$ without changing the structure type. The literature provides isolated observations but no systematic framework. We fill this gap with a three‑part conjugation test and extend it with new explicit derivations across nine settings.

The conjugation test asks three questions of a pair $(S,\phi)$ with $S$ a scaling and $\phi\in\operatorname{Aut}(X)$:

1. **Normalization:** does $S\phi S^{-1}$ remain an automorphism, i.e. is $S\operatorname{Aut}(X)S^{-1}\subseteq\operatorname{Aut}(X)$?
2. **Centralization:** does $S$ commute with $\phi$, i.e. is $S\phi=\phi S$?
3. **Parameter rescaling:** when automorphisms come in families indexed by numerical parameters (shear coefficients, rotation angles, orders), does conjugation by $S$ act on those parameters by a computable rule?

Question 3 is where scaling becomes quantitative. We show that conjugation by the anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient of the planar unipotent map $\phi(x,y)=(x+y,y)$ by exactly $2/3$, that scalar dilations act trivially on both shears and rotations, and that in the Cayley–Dickson tower the count of associative quaternion rings grows from $7$ (octonions) to $35$ (sedenions) — a factor of $5$, or $\log_{2}5\approx2.321928$ per dimension‑doubling step — while ring density per real dimension grows by exactly $2.5$. We also derive the two‑ray cone structure and the involution $\operatorname{ord}(g^{*})=2$ at Picard number two, the generator structure $n(n-1)$ plus $\prod_{i}\operatorname{Aut}(G_{i})$ for pure symmetric outer automorphisms at $n\ge5$ free factors, and the totient obstruction $\varphi(2)=1$ for order‑two discrete scalings.

Our contributions are:

- A derivation of the conjugation test's central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_{1}/\lambda_{2}$ of dilation factors while scalar dilations centralize shears and rotations exactly (Sections 3 and 4.2–4.3).
- A growth analysis of associative structure in the Cayley–Dickson tower, with the factor $5$, the exponent $\log_{2}5\approx2.321928$, and the density ratio $2.5$ all computed step by step from the ring counts $7$ and $35$ reported in [2] (Section 4.4).
- Derivations connecting scaling to cone combinatorics at Picard number two, including the involution $\operatorname{ord}(g^{*})=2$ for maps permuting the two extremal rays of the pseudo‑effective cone, from the proof machinery of [1] (Section 4.5).
- A generator‑count derivation for pure symmetric outer automorphisms of free‑product splittings, $n(n-1)$ conjugation generators plus $\prod_{i}\operatorname{Aut}(G_{i})$, from the presentation of [5] (Section 4.6).
- A discrete‑scaling rigidity result via Euler’s totient, $\varphi(2)=1$, with its consequence for the Cayley–Dickson doubling step (Section 4.7).
- An explicit statement of limitations, falsification conditions, and the smallest next computations that would de‑risk or refute the framework (Sections 6 and 7).

## 2. Background and Related Work

We discuss the related works in their fixed numbering, citing each for a specific method, result, or number its full text states.

**[1] Birational automorphism groups of projective varieties of Picard number two.** This paper defines the pseudo‑automorphism group $\operatorname{Bir}_{2}(X)$, introduces the Picard number $\rho(X)=\dim_{\mathbb{R}}\operatorname{NS}_{\mathbb{R}}(X)$, and proves that at Picard number two the pseudo‑effective cone $\overline{\operatorname{Eff}}(X)$ is generated by two rays $\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]$. It shows that a map $g$ permuting the extremal rays satisfies $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$ with $ab=1$ and $\operatorname{ord}(g^{*})=2$. These statements provide the two‑ray cone input for Section 4.5.

**[2] Automorphisms of Sedenions.** The introduction states the Cayley–Dickson series $\mathrm{A}_{N}$ has $n=2^{N}$ basis elements and reports that octonions contain $7$ associative quaternion rings while sedenions contain $35$. These numbers are the sole inputs for the growth analysis in Section 4.4.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism.** The introduction defines a nonsymplectic automorphism of order $n>1$ as one acting on the holomorphic two‑form by $\sigma^{*}(\omega_{X})=\zeta_{n}\omega_{X}$ with $\zeta_{n}=e^{2\pi i/n}$, and records that admissible orders satisfy $\varphi(n)\le20$ with the single exception $n\neq60$. This totient bound is used in Section 4.7.

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries.** Proposition 3.1 establishes a bijection between centralizing actions $J$ on the graded piece $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_{J}$ of the center $Z(G_{0})$. This centralizer description underlies the geometric interpretation of the centralization branch in Section 4.8.

**[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product.** The main result states that for $n\ge5$ the group $\operatorname{Out}(G;G_{1},\dots,G_{n})$ is generated by $n(n-1)$ factor‑isomorphism groups together with $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$, and describes the action on the $0$‑skeleton as a permutation of $n$ labelled objects. These facts supply the generator‑count input for Section 4.6.

**[6] Induced Automorphisms on Irreducible Symplectic Manifolds.** The introduction distinguishes natural (induced) automorphisms from the few known non‑natural ones and provides a criterion for when an automorphism of a $K3^{[n]}$‑type manifold is induced by an automorphism of the underlying K3 surface. This descent perspective is invoked in Section 4.8 as a qualitative analogue of scaling across hierarchical levels.

**[7] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$.** The outline constructs automorphisms $F$ of $\mathbb{C}^{2}$ with a non‑recurrent Fatou component biholomorphic to $\mathbb{C}\times\mathbb{C}^{*}$, where $F$ acts as an irrational rotation on an invariant curve and as a translation in adapted coordinates. This example motivates the open question about extending the ratio rule to nonlinear automorphisms (Section 6).

**[8] QNFO: Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure.** This work states that practitioners lack a uniform test for when a rescaling acts nontrivially on automorphism parameters, motivating the present three‑part conjugation test introduced in Section 1.

**[9] QNFO: ULTRAMETRIC PHYSICS.** This source proposes a ratio‑centric paradigm in which scaling ratios $q\in\mathbb{R}^{+}$ serve as fundamental operators and links discrete scaling ratios to hierarchical structures; it supplies the conceptual background for the discussion of discrete‑scaling rigidity and the speculative projection in Section 7(e).

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ with automorphism group $\operatorname{Aut}(X)$, and let $\mathcal{S}(X)$ be a distinguished class of self‑bijections of $X$ called **scalings**: maps $S\!:\!X\to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate, a dimension grading) without changing the structure type. We use two concrete families:

- **Scalar dilations** $S_{\lambda}(x)=\lambda x$ on a vector space or algebra, with $\lambda\in\mathbb{R}_{>0}$ or $\mathbb{C}^{*}$.
- **Anisotropic dilations** $D=\operatorname{diag}(\lambda_{1},\dots,\lambda_{n})$ on $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$, with $\lambda_{i}>0$ and not all equal.

The conjugation test applied to a pair $(S,\phi)$, $S\in\mathcal{S}(X)$, $\phi\in\operatorname{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1}\in\operatorname{Aut}(X)\;? \qquad
\text{(C)}\quad S\phi=\phi S\;? \qquad
\text{(P)}\quad \text{does }S(\cdot)S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism; the interesting content arises when $S$ is not an automorphism of the particular object but the conjugate still preserves the structure type. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi)=\{S\in\mathcal{S}(X):S\phi=\phi S\}$. Question (P) is the quantitative core, carried out in Section 4.

### 3.2 Model automorphisms

Two planar linear maps serve as canonical test automorphisms of $\mathbb{R}^{2}$:

$$
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y), \qquad
\phi_{\mathrm{rot}}(x,y)=(\cos\theta\,x-\sin\theta\,y,\;\sin\theta\,x+\cos\theta\,y),
$$

a unipotent shear with coefficient $c=1$ and a rotation by angle $\theta$.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non‑associative setting of [2], the paper reports $N_{\mathrm{oct}}=7$ associative quaternion rings in the octonions and $N_{\mathrm{sed}}=35$ in the sedenions, and its introduction states the dimension law of the Cayley–Dickson series: $\mathrm{A}_{N}$ has $n=2^{N}$ basis elements, with octonions $\mathrm{A}_{3}$ and sedenions $\mathrm{A}_{4}$. We therefore treat the octonion‑to‑sedenion passage as one dimension‑doubling step with dimensions $2^{3}=8$ and $2^{4}=16$, both taken directly from [2]. We define:

- the per‑step growth exponent $g=\log_{2}\!\bigl(N_{\mathrm{sed}}/N_{\mathrm{oct}}\bigr)$;
- the ring density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$ carrying $N(A)$ associative quaternion rings, and the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic appears in Section 4.4.

### 3.4 Cone and group‑counting derivations

Two further derivation tracks use inputs stated in the full texts of [1] and [5]. From [1]: at Picard number two, the pseudo‑effective cone is $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]$, and a map $g$ permuting the extremal rays satisfies $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$ with $ab=1$ and $\operatorname{ord}(g^{*})=2$. We re‑derive these relations and compute the face structure of the two‑ray cone. From [5]: the generator statement for $\operatorname{Out}(G;G_{1},\dots,G_{n})$ at $n\ge5$ is the $n(n-1)$ groups $G_{i_{j}}\cong G_{i}$ (realizing isomorphisms between factors) together with $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$; we compute $n(n-1)$ for small $n$ and interpret it as ordered‑pair counting on the factor set, consistent with the labelling‑permutation action described in [5].

### 3.5 Discrete‑scaling rigidity

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling‑compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler’s totient $\varphi(k)$. We evaluate $\varphi$ for small $k$ and connect the case $k=2$ to the Cayley–Dickson doubling ratio. The same totient function bounds admissible orders of nonsymplectic K3 automorphisms through the condition $\varphi(n)\le20$ recorded in [3], giving the function two distinct roles in the framework.

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

| Item | Value / expression | Source |
|------|-------------------|--------|
| Generator families for $\operatorname{Out}(G;G_{1},\dots,G_{n})$ | $n(n-1)$ groups $G_{i_{j}}$ plus $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$, for $n\ge5$ | [5], Main Result |
| Action on the $0$‑skeleton | labelling $(H_{1},\dots,H_{n})\mapsto(\psi(H_{1}),\dots,\psi(H_{n}))$ | [5], Section 2.3 |
| Two‑ray cone at $\rho=2$ | $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]$ | [1], proof section |
| Ray‑permutation relations | $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$, $ab=1$, $\operatorname{ord}(g^{*})=2$ | [1], proof section |
| Totient bound on nonsymplectic orders | $\varphi(n)\le20$, $n\neq60$ | [3], Introduction |
| Parabolic centralization | bijection $J\in Z(\underline{\operatorname{Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))\leftrightarrow s_{J}\in Z(G_{0})$ | [4], Proposition 3.1 |
| Octonion and sedenion ring counts | $N_{\mathrm{oct}}=7$, $N_{\mathrm{sed}}=35$ | [2], Introduction |
| Dimension law $n=2^{N}$ | $n=2^{N}$ for $\mathrm{A}_{N}$ | [2], Introduction |

No other numerical inputs are used anywhere in this paper.

### 4.2 Conjugation of the shear by an anisotropic dilation

Take $D=\operatorname{diag}(\lambda_{1},\lambda_{2})=\operatorname{diag}(2,3)$ and $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$. We compute $D\,\phi_{\mathrm{uni}}\,D^{-1}$ in three lines:

$$
D^{-1}(x,y)=\left(\frac{x}{\lambda_{1}},\frac{y}{\lambda_{2}}\right)=\left(\frac{x}{2},\frac{y}{3}\right),
$$

$$
\phi_{\mathrm{uni}}\!\left(\frac{x}{2},\frac{y}{3}\right)=\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right),
$$

$$
D\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right)=\left(2\left(\frac{x}{2}+\frac{y}{3}\right),\;3\cdot\frac{y}{3}\right)=\left(x+\frac{2}{3}y,\;y\right).
$$

Hence

$$
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y)=\left(x+\frac{\lambda_{1}}{\lambda_{2}}\,y,\;y\right)=\left(x+\frac{2}{3}y,\;y\right),
$$

so conjugation rescales the shear coefficient by the ratio of diagonal entries:

$$
c\;\longmapsto\;c'=\frac{\lambda_{1}}{\lambda_{2}}\,c=\frac{2}{3}\cdot1=\frac{2}{3}\approx0.666667.
$$

For general $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ the same three lines give $c'=\frac{\lambda_{1}}{\lambda_{2}}c$; the computation above is the instance $\lambda_{1}=2$, $\lambda_{2}=3$. This is the paper’s headline quantitative result: anisotropic dilations act nontrivially on automorphism parameters, by multiplicative ratios of scaling factors, while the structure type (a unipotent shear of $\mathbb{R}^{2}$) is preserved.

### 4.3 Triviality of scalar‑dilation conjugation

Let $S_{\lambda}(x)=\lambda x$ with $\lambda>0$ scalar on $\mathbb{R}^{2}$.

**Shear.** $S_{\lambda}^{-1}(x,y)=(x/\lambda,y/\lambda)$; applying $\phi_{\mathrm{uni}}$ gives $((x+y)/\lambda,\,y/\lambda)$; applying $S_{\lambda}$ gives $(x+y,\,y)$. Thus

$$
S_{\lambda}\,\phi_{\mathrm{uni}}\,S_{\lambda}^{-1}=\phi_{\mathrm{uni}}\quad\text{for all }\lambda>0.
$$

**Rotation.** Since $S_{\lambda}=\lambda I_{2}$ is a scalar matrix, it commutes with every $2\times2$ matrix, in particular with the rotation matrix $R_{\theta}$; explicitly $S_{\lambda}R_{\theta}S_{\lambda}^{-1}=R_{\theta}$. The rotation angle is invariant: $\theta\mapsto\theta$.

Scalar dilations therefore lie in the centralizer of both model automorphisms. 

### 4.4 Growth of associative structure in the Cayley–Dickson tower

From [2]: $N_{\mathrm{oct}}=7$, $N_{\mathrm{sed}}=35$. The ratio is

$$
\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=\frac{35}{7}=5.
$$

The per‑dimension‑doubling growth exponent is

$$
g=\log_{2}5=\frac{\ln5}{\ln2}\approx\frac{1.609438}{0.693147}\approx2.321928.
$$

So the count of associative quaternion rings grows by a factor of $5$ — equivalently by about $2.32$ bits — across the single octonion‑to‑sedenion step.

**Dimensions.** The introduction of [2] states the dimension law $\dim\mathrm{A}_{N}=2^{N}$, hence

$$
D_{3}=2^{3}=8,\qquad D_{4}=2^{4}=16,\qquad \frac{D_{4}}{D_{3}}=\frac{16}{8}=2.
$$

**Densities.** With $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$:

$$
\delta(\mathbb{O})=\frac{7}{8}=0.875,\qquad
\delta(\mathbb{S})=\frac{35}{16}=2.1875,
$$

$$
\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})}= \frac{35/16}{7/8}=5\cdot\frac{8}{16}=5\cdot\frac12=2.5.
$$

Thus the density per real dimension grows by exactly $2.5$ while the ambient dimension doubles.

### 4.5 Scaling and cone combinatorics at Picard number two

The proof section of [1] gives, at Picard number $\rho=2$, the two‑ray presentation

$$
\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}],
$$

and for a map $g$ permuting the extremal rays the relations $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$ with $a,b>0$. Since $g^{*}$ is defined on the integral lattice $\operatorname{NS}(X)/\text{torsion}$, $\deg(g^{*})=\pm1$, hence $ab=1$, and therefore $\operatorname{ord}(g^{*})=2$. We re‑derive the last step explicitly: with $ab=1$ and $a,b>0$, the pullback swaps the two rays with reciprocal stretching factors, so its square fixes both rays and has determinant $1$; the induced map on ray pairs has order $2$, i.e. $\operatorname{ord}(g^{*})=2$.

**Face count.** A $2$‑dimensional simplicial cone has $\binom{2}{k}$ faces of dimension $k$, so its total face count is

$$
F=\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4,
$$

with $2$ extremal rays. This face count follows directly from the input $\rho=2$ from [1].

**Scaling reading.** An anisotropic rescaling $[f_{1}]\mapsto\mu_{1}[f_{1}]$, $[f_{2}]\mapsto\mu_{2}[f_{2}]$ preserves the cone and conjugates the ray‑swap $g^{*}$ to a map with stretching factors $\mu_{2}/\mu_{1}$ and $\mu_{1}/\mu_{2}$ on the two rays—the same ratio mechanism as Section 4.2, now on cone rays. The rigidity $ab=1$ forces the product of the stretching factors to be $1$, preventing a nontrivial ratio from arising from an automorphism.

### 4.6 Generator counts for pure symmetric outer automorphisms

The Main Result of [5] states that for a free splitting $G_{1}*\dots*G_{n}$ with each $G_{i}$ non‑trivial and $n\ge5$, the group $\operatorname{Out}(G;G_{1},\dots,G_{n})$ is generated by the $n(n-1)$ groups $G_{i_{j}}\cong G_{i}$ together with $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$, subject to relations including $[f_{i_{j}}(g),f_{i_{k}}(h)]=1$ within each factor. Direct evaluation:

$$
n=5:\;5\cdot4=20,\qquad
n=6:\;6\cdot5=30,\qquad
n=7:\;7\cdot6=42.
$$

The full symmetric group on $n$ factors has order $n!$:

$$
3!=6,\qquad 4!=24,\qquad 5!=120.
$$

These are combinatorial ceilings on the permutation scope of the symmetric condition; the presentation of [5] does not claim that the group attains these orders.

### 4.7 Discrete‑scaling rigidity via Euler’s totient

If a scaling transformation has a discrete parameter group of order $k$, the number of admissible rescalings of its parameter equals $\varphi(k)$. Direct evaluation:

$$
\varphi(2)=1,\quad
\varphi(3)=2,\quad
\varphi(4)=2,\quad
\varphi(5)=4,\quad
\varphi(6)=2.
$$

In particular $\varphi(2)=1$: a discrete scaling of order $2$ admits no nontrivial rescaling of its own parameter. This matters because the Cayley–Dickson doubling step of Section 4.4 has ratio exactly $2$: the dimension‑scaling itself is totally rigid as a discrete parameter, so all the growth observed in Section 4.4 must live in the substructure counts, not in the scaling parameter.

The same totient function bounds admissible orders of nonsymplectic K3 automorphisms: the introduction of [3] records that a nonsymplectic automorphism of order $n>1$ acts on the holomorphic two‑form by $\sigma^{*}(\omega_{X})=\zeta_{n}\omega_{X}$ with $\zeta_{n}=e^{2\pi i/n}$, and that the possible orders are the $n$ whose Euler function satisfies $\varphi(n)\le20$ (single exception $n\neq60$). Thus $\varphi$ appears both as a bound on discrete scaling and as a bound on automorphism orders.

### 4.8 Geometric interpretation of the centralization branch

Proposition 3.1 of [4] gives a bijection between actions $J$ in the centralizer $Z(\underline{\operatorname{Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))$ on the graded tangent piece $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_{J}$ of the center $Z(G_{0})$ of the structure‑group reduction. Parabolic geometries carry graded decompositions $\mathfrak{g}=\mathfrak{g}^{-k}\oplus\cdots\oplus\mathfrak{g}^{-1}\oplus\mathfrak{g}^{0}$, and the center of $G_{0}$ acts on each graded piece by a dilation; the centralizer condition of [4] is therefore a centralization statement (question C) at the level of graded pieces, with the dilations that centralize the automorphism action exactly the elements of $Z(G_{0})$.

The induced‑automorphism framework of [6] provides a qualitative counterpart: an automorphism at a higher hierarchical level can be induced by an automorphism at a lower level, mirroring how a scaling of a hierarchy relates its levels. This analogy supports the interpretation of the ratio rule as a “vertical”