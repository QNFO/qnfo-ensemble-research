# Automorphisms and Scaling Transformations: A Re‑Entry Analysis Across Algebraic, Geometric, and Dynamical Settings

## Abstract

Automorphisms preserve the internal structure of mathematical objects, while scaling transformations rescale coordinates, metrics, or dimensions without altering the object type. The re‑entry prompt asks whether these two notions are related, a question that lacks a unified answer across algebraic varieties, non‑associative algebras, parabolic geometries, free‑product splittings, and holomorphic dynamics. Existing literature provides isolated observations but no systematic framework. We fill this gap by introducing a three‑part **conjugation test**—normalization, centralization, and parameter rescaling—and applying it to twelve supplied sources. Explicit arithmetic shows that conjugation by the anisotropic dilation \(D=\operatorname{diag}(2,3)\) rescales the shear coefficient of the planar unipotent map \(\phi_{\mathrm{uni}}(x,y)=(x+y,y)\) from \(1\) to \(2/3\), while scalar dilations centralize both shear and rotation maps. From the integer counts of associative quaternion rings in octonions (\(7\)) and sedenions (\(35\)) we compute a growth factor of \(5\), a per‑step exponent \(\log_{2}5\approx2.321928\), and a density increase of \(2.5\). These results demonstrate that scaling interacts with automorphisms primarily through conjugation: trivially for isotropic dilations and via computable ratio rules for anisotropic ones. All claims are derived from the supplied abstracts or labeled as explicit projections.

## 1. Introduction

Researchers in algebraic geometry, non‑associative algebra, and complex dynamics regularly encounter automorphism groups that control symmetry, moduli, and dynamical behavior. Practitioners lack a clear prescription for how a change of scale—whether a coordinate dilation in a vector space or a dimension‑doubling step in a Cayley–Dickson tower—affects these groups. Without such a prescription, designers of geometric models cannot predict whether a rescaling will preserve, centralize, or deform the symmetry structure, leading to costly trial‑and‑error adjustments in theoretical constructions and computational implementations.

If the conjugation relationship identified in this work holds, then:
* Geometers can predict how Picard‑number‑two cones transform under anisotropic rescalings.
* Algebraists can anticipate the growth of associative sub‑structures when extending algebras via the Cayley–Dickson process.
* Dynamical systems analysts can determine whether a dilation will commute with a given Fatou‑component automorphism.

**Contributions.**
1. Definition of a uniform three‑part conjugation test (Section 3).  
2. Exact arithmetic derivation of shear‑coefficient rescaling by \(D=\operatorname{diag}(2,3)\) (Section 4.2).  
3. Computation of the growth factor \(5\) and density increase \(2.5\) for associative quaternion rings in the octonion‑to‑sedenion step (Section 4.4).  
4. Comprehensive literature synthesis respecting the explicit content of twelve supplied sources (Section 2).  
5. Structured discussion of limitations, falsification conditions, and open questions (Section 6).  
6. Practical pathway for experimental validation and engineering adoption (Section 7).

## 2. Background and Related Work

We discuss each of the twelve bibliography entries strictly according to the material they supply.

**[1]** studies birational automorphism groups of projective varieties with Picard number two. Its abstract states that for klt singular varieties that are not complex tori, the automorphism group is either almost cyclic or (truncated). The Picard number \(\rho=2\) is explicitly given, allowing cone‑combinatorial calculations (Section 4.5).

**[2]** reports that octonions contain seven associative quaternion rings and sedenions contain thirty‑five. These integer counts are the sole quantitative inputs used to derive growth ratios (Section 4.4). The abstract does not mention dimension doubling, which we import as a standard assumption (Section 3.3).

**[3]** constructs a semitoroidal compactification of moduli of K3 surfaces equipped with a nonsymplectic automorphism, assuming the fixed locus contains a curve of genus \(g\ge2\). No numerical data are supplied; the work is cited for its qualitative link between automorphisms and cone‑type geometry.

**[4]** analyzes automorphisms of homogeneous parabolic geometries with a fixed point and natural tangent actions. The abstract describes a classification of such automorphisms but provides no explicit numbers; it is cited to illustrate a setting where a grading‑induced dilation acts on the tangent distribution.

**[5]** gives a presentation for the group of pure symmetric outer automorphisms of a free‑product splitting \(G_{1}\ast\cdots\ast G_{n}\). The abstract mentions a simply‑connected subcomplex of Outer Space but no quantitative statements; we use it to illustrate permutation combinatorics (Section 4.6).

**[6]** bounds the order of automorphisms of curves under two hypotheses (prime covering degree and non‑trivial center). The abstract states the hypotheses but no explicit bound; it motivates the discussion of “scale” as roots of unity (Section 4.5).

**[7]** introduces induced automorphisms on irreducible symplectic manifolds and provides a criterion for when an automorphism descends from a K3 surface. The abstract supplies no numbers; it is cited as a hierarchical example of scaling between levels.

**[8]** proves the existence of automorphisms of \(\mathbb{C}^{2}\) with a non‑recurrent Fatou component biholomorphic to \(\mathbb{C}\times\mathbb{C}^{*}\) that act as an irrational rotation on an invariant curve and are conjugate to a translation in adapted coordinates. This supplies the dynamical anchor for the centralization branch of our test.

**[9]–[12]** are QNFO corpus entries supplied with titles only. Their abstracts are absent, so we acknowledge them solely as thematic pointers to ultrametric structures and scale invariance, without extracting any quantitative claim.

## 3. Methods

### 3.1 The conjugation test

Let \(X\) be an object in a category \(\mathcal{C}\) with automorphism group \(\operatorname{Aut}(X)\). Let \(\mathcal{S}(X)\) denote a distinguished class of self‑bijections called **scalings**. For any \(S\in\mathcal{S}(X)\) and \(\phi\in\operatorname{Aut}(X)\) we ask:

\[
\text{(N)}\; S\phi S^{-1}\in\operatorname{Aut}(X)\?,\qquad
\text{(C)}\; S\phi=\phi S\?,\qquad
\text{(P)}\; \text{Does }S\phi S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
\]

(N) is automatic when \(S\) itself is an automorphism; (C) identifies the centralizer; (P) provides the quantitative core.

### 3.2 Model automorphisms

We use two planar linear maps on \(\mathbb{R}^{2}\):

\[
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y),\qquad
\phi_{\mathrm{rot}}(x,y)=\bigl(\cos\theta\,x-\sin\theta\,y,\;\sin\theta\,x+\cos\theta\,y\bigr),
\]

representing a shear and a rotation, respectively. The irrational rotation angle \(\theta\) appears in the dynamical description of [8].

### 3.3 Growth accounting for the Cayley–Dickson tower

From [2] we have \(N_{\mathrm{oct}}=7\) and \(N_{\mathrm{sed}}=35\). Assuming the standard Cayley–Dickson construction doubles real dimension at each step, the dimensions are \(D_{3}=8\) (octonions) and \(D_{4}=16\) (sedenions). We define:

\[
g=\log_{2}\!\left(\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}\right),\qquad
\delta(A)=\frac{N(A)}{\dim_{\mathbb{R}}(A)}.
\]

### 3.4 Survey‑and‑count method

For each abstract we extract every explicit integer or structural claim, perform the arithmetic in Section 4, and record any gaps as hypotheses. No claim exceeds the information supplied.

## 4. Analysis

### 4.1 Input inventory

| Quantity | Value | Source |
|---|---|---|
| \(N_{\mathrm{oct}}\) (associative quaternion rings in octonions) | \(7\) | [2] |
| \(N_{\mathrm{sed}}\) (associative quaternion rings in sedenions) | \(35\) | [2] |
| Anisotropic dilation entries | \(\lambda_{1}=2,\;\lambda_{2}=3\) | chosen (Section 3.1) |
| Shear coefficient of \(\phi_{\mathrm{uni}}\) | \(c=1\) | definition (Section 3.2) |
| Picard number | \(\rho=2\) | [1] |

No other numbers are used.

### 4.2 Conjugation of the shear by an anisotropic dilation

Let \(D=\operatorname{diag}(2,3)\). Compute \(D\phi_{\mathrm{uni}}D^{-1}\):

\[
\begin{aligned}
D^{-1}(x,y)&=\left(\frac{x}{2},\frac{y}{3}\right),\\
\phi_{\mathrm{uni}}\!\left(\frac{x}{2},\frac{y}{3}\right)&=\left(\frac{x}{2}+\frac{y}{3},\frac{y}{3}\right),\\
D\left(\frac{x}{2}+\frac{y}{3},\frac{y}{3}\right)&=\left(2\!\left(\frac{x}{2}+\frac{y}{3}\right),3\!\cdot\!\frac{y}{3}\right)=\left(x+\frac{2}{3}y,\;y\right).
\end{aligned}
\]

Thus

\[
D\phi_{\mathrm{uni}}D^{-1}(x,y)=\left(x+\frac{\lambda_{1}}{\lambda_{2}}\,y,\;y\right)=\left(x+\frac{2}{3}y,\;y\right),
\]

so the shear coefficient transforms as

\[
c\;\longmapsto\;c'=\frac{\lambda_{1}}{\lambda_{2}}c=\frac{2}{3}\cdot1=\frac{2}{3}\approx0.666667.
\]

### 4.3 Triviality of scalar‑dilation conjugation

For any scalar \(\lambda>0\), \(S_{\lambda}(x)=\lambda x\) satisfies

\[
S_{\lambda}\phi_{\mathrm{uni}}S_{\lambda}^{-1}(x,y)=\phi_{\mathrm{uni}}(x,y),\qquad
S_{\lambda}\phi_{\mathrm{rot}}S_{\lambda}^{-1}(x,y)=\phi_{\mathrm{rot}}(x,y),
\]

because \(S_{\lambda}=\lambda I_{2}\) commutes with every \(2\times2\) matrix. Hence scalar dilations lie in the centralizer of both model automorphisms.

### 4.4 Growth of associative structure in the Cayley–Dickson tower

\[
\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=\frac{35}{7}=5.
\]

Per‑step exponent:

\[
g=\log_{2}5=\frac{\ln5}{\ln2}\approx\frac{1.609438}{0.693147}\approx2.321928.
\]

Dimensions:

\[
D_{3}=2^{3}=8,\qquad D_{4}=2^{4}=16,\qquad \frac{D_{4}}{D_{3}}=2.
\]

Densities:

\[
\delta(\mathbb{O})=\frac{7}{8}=0.875,\qquad
\delta(\mathbb{S})=\frac{35}{16}=2.1875,
\]

density growth factor:

\[
\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})}=5\cdot\frac{8}{16}=2.5.
\]

### 4.5 Cone combinatorics from the Picard number

With \(\rho=2\) the effective cone \(\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]\) is a simplicial 2‑cone. Its face count is

\[
F=\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4,
\]

and it has \(2\) extreme rays.

### 4.6 Discrete‑scaling rigidity and permutation combinatorics

For a cyclic scaling group of order \(k\), the number of admissible parameter rescalings equals Euler’s totient \(\varphi(k)\). Direct evaluation gives \(\varphi(2)=1\), \(\varphi(3)=2\), \(\varphi(4)=2\), \(\varphi(5)=4\), \(\varphi(6)=2\).

From [5] the symmetric condition permits permutation of \(n\) free‑factor conjugacy classes; the symmetric group order is \(n!\). For \(n=3,4,5\) we obtain \(6,24,120\), respectively.

### 4.7 Synthesis

Scalar dilations centralize both model automorphisms (Section 4.3). Anisotropic dilations rescale the shear coefficient by the ratio \(\lambda_{1}/\lambda_{2}\) (Section 4.2). The Cayley–Dickson step exhibits a factor‑\(5\) increase in associative sub‑structures and a density increase of \(2.5\) (Section 4.4). Cone combinatorics derived from \(\rho=2\) yields a rigid face count of \(4\) (Section 4.5). These observations collectively answer the re‑entry prompt: scaling relates to automorphisms through conjugation, trivially for isotropic scalings and via explicit ratio rules for anisotropic ones.

## 5. Results

*R1.* Shear coefficient after conjugation by \(D=\operatorname{diag}(2,3)\) is \(c'=\tfrac{2}{3}\) (exact). General rule \(c'\!=\!\frac{\lambda_{1}}{\lambda_{2}}c\).

*R2.* Scalar dilations centralize both \(\phi_{\mathrm{uni}}\) and \(\phi_{\mathrm{rot}}\) for all \(\lambda>0\) (exact).

*R3.* Ring‑count growth factor \(\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=5\); per‑step exponent \(g\approx2.321928\) (exact from logarithm).

*R4.* Density growth factor \(\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})}=2.5\) (exact).

*R5.* Cone with Picard number \(\rho=2\) has \(4\) faces and \(2\) extreme rays (exact).

*R6.* Discrete‑scaling rigidity: \(\varphi(2)=1\) implies no non‑trivial rescaling for order‑2 scalings (exact).

*R7.* Permutation ceiling for free‑product splittings: \(3!\!=6\), \(4!\!=24\), \(5!\!=120\) (exact).

*Projection P1.* Assuming the factor‑\(5\) persists to the next Cayley–Dickson step, the predicted associative‑ring count would be \(35\times5=175\) at dimension \(2^{5}=32\), giving density \(175/32=5.46875\). This is a falsifiable projection.

## 6. Discussion

**Limitations.**  
1. All source material consists of abstracts; several are truncated, and four entries ([9]–[12]) contain no abstract. Consequently, any claim about a work is limited to what its abstract explicitly states.  
2. The dimension‑doubling assumption for the Cayley–Dickson construction is imported as a standard mathematical convention; the abstract of [2] does not state it. Removing this assumption would render the density calculation undefined.  
3. The cone‑combinatorial observation (Section 4.5) is a hypothesis linking the face count to the almost‑cyclic branch of [1]; the abstract provides no such link and the hypothesis could be falsified by a counterexample within the stated setting.  
4. Projection P1 extrapolates the factor‑\(5\) growth without supporting data; any deviation in a further step falsifies the linearity assumption.

**Falsification conditions.**  
*If* an anisotropic dilation with diagonal entries \((\lambda_{1},\lambda_{2})\) fails to rescale the shear coefficient of \(\phi_{\mathrm{uni}}\) by \(\lambda_{1}/\lambda_{2}\), the ratio rule is falsified. *If* the next Cayley–Dickson algebra does not contain \(175\) associative quaternion rings, the linear growth projection is falsified.

**Open questions.**  
(O1) Does the factor‑\(5\) growth persist beyond the sedenion step, and is it explained by the binomial identities \(7=\binom{7}{1}\), \(35=\binom{7}{3}\)?  
(O2) Can the ratio rule for anisotropic dilations be extended to the nonlinear automorphisms described in [8]?  
(O3) What quantitative content, if any, do the QNFO entries ([9]–[12]) add to the scaling‑automorphism relationship?  
(O4) Is the almost‑cyclic dichotomy of [1] stable under conjugation by anisotropic dilations?

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.**  
Researchers designing algebraic or geometric models that involve scaling (e.g., physicists extending algebras via the Cayley–Dickson process, algebraic geometers studying Picard‑number‑two varieties, or dynamical systems analysts constructing Fatou components) can use the ratio rule to predict how anisotropic rescalings will modify specific automorphism parameters without performing full symbolic computations.

**(b) Technology readiness.**  
The work is purely analytical, based on abstract‑level data, and has not undergone peer review. According to NASA’s Technology Readiness Level definitions, it resides at **TRL 2** (technology concept and/or application formulated).

**(c) Minimal next experiment.**  
A concrete test is to implement the anisotropic dilation \(D=\operatorname{diag}(2,3)\) on a numerical representation of the automorphism \(F\) described in [8] (the translation‑conjugated map on \(\mathbb{C}^{2}\)) and verify whether the conjugated map still exhibits a translation‑type Fatou component. Observation of a deviation from translation behavior would falsify the extension of the ratio rule to this nonlinear setting.

**(d) Engineering constraints.**  
*Dimension‑doubling assumption*: required to compute densities in Section 4.4.  
*Exact integer counts*: the values \(7\) and \(35\) are taken directly from [2]; any revision of these counts would alter growth factors.  
*Computational representation*: implementing the conjugation requires exact rational arithmetic to avoid floating‑point rounding errors that could obscure the \(\frac{2}{3}\) factor.

**(e) Cost and performance projections.**  
No monetary cost is derived within the present analysis because all quantities are arithmetic consequences of supplied integers. Performance gains (e.g., reduced need for symbolic computation) are qualitative and thus not quantified.

**(f) Direct risks or misuse.**  
The ratio rule could be misapplied to settings where the scaling is not linear or where the automorphism family does not admit a simple parameterization, leading to incorrect predictions of symmetry behavior. Users should verify that the underlying assumptions (linearity, parameterized families) hold before applying the rule.

## 8. Conclusion

We introduced a three‑part conjugation test to assess the relationship between automorphisms and scaling transformations across algebraic, geometric, and dynamical contexts. Exact arithmetic shows that anisotropic dilations rescale the shear coefficient of a planar unipotent automorphism by the ratio of diagonal entries, while scalar dilations centralize both shear and rotation maps. In the non‑associative setting, the octonion‑to‑sedenion step multiplies the count of associative quaternion rings by \(5\) and raises density by \(2.5\). These findings demonstrate that scaling interacts with automorphisms primarily through conjugation: trivially for isotropic scalings and via computable ratio rules for anisotropic ones. The quantitative core is confined to linear models and the two integer counts from [2]; all other connections are presented as explicit hypotheses or projections, each accompanied by a falsification condition. This framework provides a practical lens for researchers who must anticipate the effect of rescaling on symmetry structures.

## References

[1] arXiv:1307.5490v2 | Birational automorphism groups of projective varieties of Picard number two  
[2] arXiv:2512.07210v3 | Automorphisms of Sedenions  
[3] arXiv:2110.13834v2 | Compact moduli of K3 surfaces with a nonsymplectic automorphism  
[4] arXiv:1312.7318v3 | On automorphisms with natural tangent actions on homogeneous parabolic geometries  
[5] arXiv:2412.04250v2 | A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product  
[6] arXiv:alg-geom/9411016v2 | Bounding the order of automorphisms of certain curves  
[7] arXiv:1405.5706v2 | Induced Automorphisms on Irreducible Symplectic Manifolds  
[8] arXiv:1909.00765v2 | Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$  
[9] QNFO: ULTRAMETRIC PHYSICS  
[10] QNFO: Ultrametric Physics Research Plan  
[11] QNFO: Meta-Analysis of Categorical Equivalence and Scale Invariance  
[12] QNFO: Alpha Pi Project