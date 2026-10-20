# Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$ and an Adelic Product Formula

## Abstract

The real constant $\pi\approx3.14159$ is defined as the ratio of a Euclidean circle’s circumference to its diameter. Ostrowski’s theorem embeds $\mathbb{Q}$ diagonally into every completion $\mathbb{R}$ and $\mathbb{Q}_p$, prompting the question whether an analogue $\pi_p$ exists at each $p$‑adic place. We formalize a $p$‑adic “circle’’ as the sphere $S_r=\{x\in\mathbb{Q}_p^2:\|x\|=r\}$ with respect to the sup‑norm and define its circumference as the Haar measure $\mu(S_r)$. Using the normalization $\mu(B_1)=1$, we derive exactly that $\mu(B_r)=r^2$ for $r\in p^{\mathbb Z}$ and $\mu(S_r)=r^2(1-p^{-2})$. The ultrametric diameter equals $r$, while the archimedean‑style diameter equals $2r$, yielding the scale‑invariant ratios $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$. Both are rational, depend on $p$, and satisfy $\lim_{p\to\infty}\kappa_p=1\neq\pi$. The finite product $\prod_{p\le13}\kappa_p\approx0.618029$ approximates the Euler product $\prod_p\kappa_p=6/\pi^2\approx0.607927$, and the all‑place product $\pi\prod_p\kappa_p=6/\pi\approx1.909859\neq1$. Consequently, a place‑wise family of circle constants exists but does not deform to $\pi$; the adelic‑$\pi$ conjecture fails in this Haar‑measure formulation while $\pi$ reappears only as a global invariant of the product over all finite places.

## 1. Introduction

Designers of precision metrology, quantum‑field theorists, and number‑theoretic physicists all rely on the constant $\pi$ as the ratio $C/D$ of a Euclidean circle’s circumference $C$ to its diameter $D$. In modern high‑energy experiments the numerical value of $\pi$ enters cross‑section calculations, while in lattice simulations the discretization error scales with $\pi$‑dependent trigonometric factors. If a $p$‑adic analogue $\pi_p$ existed, then any theory formulated over the adeles $\mathbb{A}_\mathbb{Q}$ could replace the archimedean $\pi$ by a family $\{\pi_p\}$, potentially simplifying adelic regularizations and offering new consistency checks across places. The present work asks: does the ratio $C/D$ admit a well‑defined $p$‑adic counterpart intrinsic to each $\mathbb{Q}_p$, and if so, do the values $\{\pi,\pi_2,\pi_3,\dots\}$ assemble into a coherent adelic object?

We answer this question in the Haar‑measure framework. Our contributions are:

1. An explicit Haar‑measure computation (Section 4) showing that the sphere of radius $r$ in $\mathbb{Q}_p^2$ has measure $r^2(1-p^{-2})$, with all arithmetic displayed.  
2. The identification of the two scale‑invariant ratios $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$, together with exact decimal values for $p=2,3,5,7,11$ (Section 4).  
3. The exact evaluation $\prod_p\kappa_p=6/\pi^2\approx0.607927$ and a finite‑prime approximation $P_{13}\approx0.618029$ (Section 4).  
4. A critical assessment (Section 6) of what these results imply for the adelic‑$\pi$ conjecture, including a falsifiability statement.  

## 2. Background and Related Work

The arithmetic of special values provides a natural setting for $p$‑adic analogues of classical constants. Entry [1] formulates a $p$‑adic Beilinson conjecture for number fields, showing that $p$‑adic $L$‑functions and syntomic regulators can parallel the archimedean special‑value formulas; this demonstrates that translating archimedean statements into $p$‑adic language is an active program. Entry [2] presents a formulation of $p$‑adic Birch–Swinnerton‑Dyer conjectures in the supersingular case, establishing that deep conjectures in arithmetic geometry admit $p$‑adic versions even in delicate settings. Entry [4] discusses generalized Iwasawa main conjectures and $p$‑adic Stark conjectures for Artin motives, extending $p$‑adic special‑value conjectures beyond elliptic curves. Entry [8] constructs $p$‑adic multiple $L$‑functions via a specific $p$‑adic measure and evaluates their special values, illustrating that $p$‑adic analytic objects can encode arithmetic data analogous to real $L$‑functions.

In mathematical physics, entry [3] studies phase transitions for a $p$‑adic Potts model on a Cayley tree, showing that $p$‑adic statistical‑mechanical systems exhibit place‑dependent critical phenomena; this motivates the investigation of place‑dependent geometric ratios. Entry [6] proposes a $p$‑adic description of the Higgs mechanism based on $p$‑adic square roots and light cones, providing evidence that $p$‑adic geometry can be employed in fundamental physics. Entry [7] collects the mathematical ideas behind a $p$‑adic physics program, emphasizing that archimedean and non‑archimedean descriptions may coexist within an adelic framework.

In combinatorial geometry, entry [5] establishes a $p$‑adic analogue of the van Lint–Seidel bound for equiangular lines, showing that extremal geometric constants over $\mathbb{Q}_p$ are inherently place‑specific. Finally, the corpus documents that motivate the question itself are [9] and [10]; their titles propose a harmonic paradigm under Ostrowski’s theorem and an adelic constraint program, respectively, and they serve as the source of the adelic‑$\pi$ conjecture tested here. Entries [11] and [12] are cited only for completeness; their titles do not provide quantitative claims relevant to our analysis.

## 3. Methods

**Arena and norm.** Fix a prime $p$. On $\mathbb{Q}_p^2$ we use the sup‑norm  
\[
\|x\|=\max\bigl(|x_1|_p,\;|x_2|_p\bigr),\qquad x=(x_1,x_2)\in\mathbb{Q}_p^2,
\]  
which is the standard ultrametric norm on $\mathbb{Q}_p^2$. The values taken by $\|\cdot\|$ on $\mathbb{Q}_p^2\setminus\{0\}$ are exactly $r\in p^{\mathbb Z}$.

**Measure.** Let $\mu$ be the Haar measure on the additive group $\mathbb{Q}_p^2$, normalized by  
\[
\mu(B_1)=1,\qquad B_1=\{x\in\mathbb{Q}_p^2:\|x\|\le1\}.
\]  
Haar measure is the unique translation‑invariant Borel measure on $\mathbb{Q}_p^2$; under dilation $x\mapsto a x$ it transforms by the factor $|a|_p^2$.

**Circle.** For $r\in p^{\mathbb Z}$, $r>0$, define the closed ball and sphere  
\[
B_r=\{x:\|x\|\le r\},\qquad S_r=\{x:\|x\|=r\}=B_r\setminus B_{r/p}.
\]  
$S_r$ is the $p$‑adic analogue of a Euclidean circle: it consists of all points at exact distance $r$ from the origin.

**Circumference and diameters.**  
\[
C_p(r)=\mu(S_r),\qquad D_p(r)=\operatorname{diam}(S_r)=\sup\{\|x-y\|:x,y\in S_r\},
\]  
and the archimedean‑style diameter $D'_p(r)=2r$. The candidate constants are the scale‑invariant ratios  
\[
\kappa_p=\frac{C_p(r)}{D_p(r)},\qquad \kappa'_p=\frac{C_p(r)}{D'_p(r)}.
\]

**Adelic product.** We compute the finite product $P_N=\prod_{p\le N}\kappa_p$ and combine it with the archimedean ratio $\kappa_\infty=\pi$ using the Euler product identity $\prod_p(1-p^{-2})=1/\zeta(2)=6/\pi^2$.

## 4. Analysis

All inputs are definitions from Section 3 or classical identities; no empirical data are used.

**Step 1: Measure of a ball.** Write $r=p^m$ with $m\in\mathbb Z$. The dilation $x\mapsto p^{-m}x$ sends $B_1$ to $B_r$, and Haar measure transforms by $|p^{-m}|_p^2=p^{2m}=r^2$. Hence  
\[
\mu(B_r)=r^2.
\]

**Step 2: Circumference.** Since $S_r=B_r\setminus B_{r/p}$,  
\[
C_p(r)=\mu(S_r)=\mu(B_r)-\mu(B_{r/p})=r^2-\left(\frac{r}{p}\right)^2
=r^2\!\left(1-\frac1{p^2}\right).
\]

**Step 3: Ultrametric diameter.** For any $x,y\in S_r$, the ultrametric inequality gives $\|x-y\|\le r$. Choosing $x=(p^{-m}u,0)$ and $y=(0,p^{-m}u)$ with a $p$‑adic unit $u$ yields $\|x-y\|=r$, so  
\[
D_p(r)=r.
\]

**Step 4: Ratios.**  
\[
\kappa_p=\frac{C_p(r)}{D_p(r)}=\frac{r^2(1-p^{-2})}{r}=1-\frac1{p^2},
\]  
\[
\kappa'_p=\frac{C_p(r)}{2r}=\frac{r^2(1-p^{-2})}{2r}
=\frac12\!\left(1-\frac1{p^2}\right).
\]  
Both are independent of $r$.

Explicit values:  

- $p=2$: $\kappa_2=3/4=0.75$, $\kappa'_2=3/8=0.375$.  
- $p=3$: $\kappa_3=8/9\approx0.888889$, $\kappa'_3=4/9\approx0.444444$.  
- $p=5$: $\kappa_5=24/25=0.96$, $\kappa'_5=12/25=0.48$.  
- $p=7$: $\kappa_7=48/49\approx0.979592$, $\kappa'_7=24/49\approx0.489796$.  
- $p=11$: $\kappa_{11}=120/121\approx0.991736$, $\kappa'_{11}=60/121\approx0.495868$.

**Step 5: Finite adelic product.**  
\[
P_{13}=\frac34\cdot\frac89\cdot\frac{24}{25}\cdot\frac{48}{49}\cdot\frac{120}{121}\cdot\frac{168}{169}
=\frac{15482880}{25052025}\approx0.618029.
\]

**Step 6: Infinite product.** The Euler product for $\zeta(2)$ gives  
\[
\prod_p\kappa_p=\prod_p\!\left(1-\frac1{p^2}\right)=\frac1{\zeta(2)}=\frac6{\pi^2}
\approx0.607927.
\]

**Step 7: All‑place combination.**  
\[
\kappa_\infty\cdot\prod_p\kappa_p=\pi\cdot\frac6{\pi^2}=\frac6\pi\approx1.909859\neq1.
\]

All arithmetic steps are displayed; no hidden arguments are used.

## 5. Results

1. **Ball and sphere measures.** For $r=p^m$, $\mu(B_r)=r^2$ and $C_p(r)=\mu(S_r)=r^2(1-p^{-2})$ (Steps 1–2).  
2. **Circle constants.** $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$, independent of $r$ (Step 4). Exact and decimal values are listed above.  
3. **Finite product.** $P_{13}=15482880/25052025\approx0.618029$ (Step 5).  
4. **Infinite product.** $\prod_p\kappa_p=6/\pi^2\approx0.607927$ (Step 6).  
5. **All‑place combination.** $\pi\prod_p\kappa_p=6/\pi\approx1.909859\neq1$ (Step 7).  

Qualitatively, a place‑wise family of scale‑invariant circle constants exists; each member is rational, bounded by $1$, and tends to $1$ as $p\to\infty$. The archimedean constant $\pi$ reappears only through the global Euler product, not as any single $\pi_p$.

## 6. Discussion

**Implications for the adelic‑$\pi$ conjecture.** In the Haar‑measure formulation the conjecture fails in its strong form: there is no place‑wise deformation $\{\pi_p\}$ interpolating toward $\pi$. The constants $\kappa_p$ are rational, depend on $p$, and satisfy $\lim_{p\to\infty}\kappa_p=1\neq\pi$. The weak form survives because $\pi$ is recovered as the global invariant $\prod_p\kappa_p=6/\pi^2$.

**Limitations.**  
1. *Definition of circumference.* We defined $C_p(r)$ as Haar measure of $S_r$. Since $\mathbb{Q}_p$ is totally disconnected, $S_r$ is not a topological boundary; alternative definitions (e.g., $p$‑adic line integrals or other norms) could yield different constants.  
2. *Diameter convention.* We reported both the ultrametric diameter $D_p(r)=r$ and the archimedean‑style diameter $D'_p(r)=2r$. Different conventions would change $\kappa'_p$ but not $\kappa_p$.  
3. *Normalization.* The choice $\mu(B_1)=1$ fixes the overall scale; any other normalization rescales $C_p(r)$ and $D_p(r)$ proportionally, leaving the ratios unchanged.  
4. *Euler product interpretation.* The identity $\prod_p(1-p^{-2})=6/\pi^2$ is a number‑theoretic theorem; its appearance here does not imply a geometric adelic circle structure beyond the product formula.

**What would falsify the main claim.** If a construction produced a $p$‑adic circle constant $\pi_p$ satisfying $\pi_p\to\pi$ as $p\to\infty$ or if an adelic product of geometrically defined constants equaled $1$ under a principled normalization, then our conclusion that the Haar‑measure formulation fails would be falsified.

**Open questions.**  
- Do other norms on $\mathbb{Q}_p^2$ (e.g., $\|x\|_2=\sqrt{|x_1|_p^2+|x_2|_p^2}$) produce irrational or $\pi$‑approaching constants?  
- Can a $p$‑adic analogue of arc length be defined via a parametrization that yields a non‑rational constant?  
- How does the harmonic‑paradigm program [9] adapt if one replaces the simple Haar‑measure circle by a more sophisticated $p$‑adic geometric object?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  
Number‑theoretic physicists and mathematicians working on adelic formulations of quantum field theory would use the derived constants $\kappa_p$ to benchmark any proposed $p$‑adic geometric construction. If a new $p$‑adic model claims to reproduce $\pi$ at each place, the explicit values $\kappa_p=1-p^{-2}$ provide a minimal consistency check: the model must either reproduce these rational numbers or justify a different definition of circumference.

**(b) Technology readiness.**  
The work is purely analytical, has not undergone peer review, and therefore resides at NASA Technology Readiness Level 1–2. As an analytical study it cannot exceed TRL 3.

**(c) Smallest next experiment.**  
A minimal prototype would compute the Haar measure of $S_r$ for a small prime (e.g., $p=3$) by enumerating points in $\mathbb{Z}_3^2$ modulo $3^k$ for increasing $k$ and observing convergence to $r^2(1-p^{-2})$. The experiment would measure the proportion of lattice points lying in $S_r$ versus $B_r$. If the observed proportion deviates from $1-p^{-2}$ beyond statistical fluctuations, the Haar‑measure definition would be falsified.

**(d) Engineering constraints.**  
- *Normalization*: The Haar measure must be normalized by $\mu(B_1)=1$; any implementation must respect this scaling.  
- *Norm choice*: The sup‑norm is required for the derivations; switching to another norm changes the sphere definition and must be documented.  
- *Computational resources*: Enumerating points modulo $p^k$ grows as $p^{2k}$; feasible prototypes are limited to $k\le4$ for $p\ge3$ on standard hardware.

**(e) Cost and performance projections.**  
Given the analytical nature of the result, no material cost is incurred. The computational cost of the prototype in (c) scales roughly as $O(p^{2k})$ operations; for $p=3$, $k=4$ this is $3^{8}=6561$ elementary operations, well within the capability of a standard laptop.

**(f) Risks and misuse.**  
A potential misuse is the insertion of the rational constants $\kappa_p$ into numerological arguments that claim to predict physical quantities across places. Since $\kappa_p$ are bounded by $1$, any extrapolation to large physical constants would be mathematically unfounded. Users should avoid treating $\kappa_p$ as a substitute for $\pi$ in engineering formulas without proper justification.

## 8. Conclusion

We have computed, with fully displayed arithmetic, the Haar‑measure geometry of $p$‑adic circles in $\mathbb{Q}_p^2$: the sphere of radius $r$ has measure $r^2(1-p^{-2})$, the ultrametric diameter equals $r$, and the resulting scale‑invariant circle constants are $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$. These constants are rational, place‑dependent, bounded by $1$, and tend to $1$ rather than to $\pi$. The Euler product over all finite places equals $6/\pi^2\approx0.607927$, and the all‑place product including the archimedean factor is $6/\pi\approx1.909859\neq1$. Hence the adelic‑$\pi$ conjecture, in its Haar‑measure formulation, fails place‑wise while surviving globally: $\pi$ appears only as a product invariant of the finite places, not as a deformation target of place‑wise constants.

## References

[1] arXiv:0707.3682v2 | On the p‑adic Beilinson conjecture for number fields  
[2] arXiv:1512.09362v1 | A formulation for p‑adic versions of the Birch and Swinnerton‑Dyer conjectures in the supersingular case  
[3] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$‑Adic Potts Model with Competing Interactions on a Cayley Tree  
[4] arXiv:2103.06864v4 | On generalized Iwasawa main conjectures and $p$‑adic Stark conjectures for Artin motives  
[5] arXiv:2408.00810v3 | p‑adic Equiangular Lines and p‑adic van Lint‑Seidel Relative Bound  
[6] arXiv:hep-th/9410058v3 | p‑Adic description of Higgs mechanism I: p‑Adic square root and p‑adic light cone  
[7] arXiv:hep-th/9506097v2 | p‑Adic TGD: Mathematical Ideas  
[8] arXiv:1508.07185v2 | Fundamentals of p‑adic multiple L‑functions and evaluation of their special values  
[9] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation/ | QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p‑Adic/Adélic Re‑Evaluation with Helical Compton Vortex Synthesis  
[10] https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-1/ | QNFO: Adelic Constraints on Quantum Field Theory: Phase 1  
[11] https://papers.qnfo.org/papers/odr-thesis-five-question-synthesis/ | QNFO: ODR Thesis: The Compton Count as the Only Primitive — A Five‑Question Synthesis  
[12] https://papers.qnfo.org/papers/odr-thesis/ | QNFO: ODR Thesis: The Compton Count as the Only Primitive  

## Appendix A. Divergence Report

No divergent claims were identified among the three independent drafts; all substantive statements converged on the same quantitative results and interpretations.

## Appendix B. Claim Attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | $\mu(B_r)=r^2$ for $r=p^m$ | A, B, C | Convergent |
| C2 | $C_p(r)=r^2(1-p^{-2})$ | A, B, C | Convergent |
| C3 | $D_p(r)=r$ | A, B, C | Convergent |
| C4 | $\kappa_p=1-p^{-2}$, $\kappa'_p=(1-p^{-2})/2$ | A, B, C | Convergent |
| C5 | Explicit decimal values for $p=2,3,5,7,11$ | A, B, C | Convergent |
| C6 | $P_{13}=15482880/25052025\approx0.618029$ | A, B, C | Convergent |
| C7 | $\prod_p\kappa_p=6/\pi^2\approx0.607927$ | A, B, C | Convergent |
| C8 | $\pi\prod_p\kappa_p=6/\pi\approx1.909859\neq1$ | A, B, C | Convergent |
| C9 | Limitations list (definition, diameter, normalization, Euler product) | A, B, C | Convergent |
| C10 | Falsifiability statement (existence of $\pi_p\to\pi$) | A, B, C | Convergent |
| C11 | Practical implications for adelic modelers | A, B, C | Convergent |
| C12 | TRL assessment (TRL 1‑2) | A, B, C | Convergent |
| C13 | Prototype proposal (enumerate points modulo $p^k$) | A, B, C | Convergent |
| C14 | Engineering constraints (normalization, norm, computational scaling) | A, B, C | Convergent |
| C15 | Cost/performance projection (computational cost $O(p^{2k})$) | A, B, C | Convergent |
| C16 | Risk of numerological misuse | A, B, C | Convergent |