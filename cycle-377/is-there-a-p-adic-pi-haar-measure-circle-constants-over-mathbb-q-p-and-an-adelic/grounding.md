# Grounding block - source: rem-rev-699b1e61-764e-4a86-b628-e6024a7e1a68

## Research idea

Defining a p-adic analogue of pi via circumference-to-diameter ratios. The author conjectures that π is not intrinsically Archimedean: since Ostrowski's theorem embeds ℚ diagonally into all completions of ℚ, the defining ratio C/d should have a well-defined analogue π_p in each ℚ_p, with the familiar 3.14159… being merely the ∞-place projection of a deeper adelic object. A paper could test this by formalizing 'circumference' in p-adic geometry (e.g., p-adic circles as spheres in ℚ_p², Haar-measure boundary length vs. diameter), deriving whether the ratio is place-independent, rational, or even well-defined, and comparing candidate definitions (analytic via p-adic Gamma/sine analogues, geometric via ball boundaries). A rigorous derivation showing π_p exists, is unique, and coheres adelicly would substantiate the claim; inconsistency or place-dependence would refute it.

Source: owner notebook notes/v1/2026/07/23/_26204142018.md

Post-publication revision of the published paper "Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$" (version 2.1.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 10 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 10, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Appendix B, claim C6, states P_13 = 15482880/25052025 ≈ 0.618029. (confirmed by a second model)
2. The paper concludes it 'disproves the strong adelic-π conjecture' (Abstract, Sections 6 and 8). (confirmed by a second model)

## Existing paper under revision (remediation only)

# Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$

## Abstract

The real constant $\pi\approx3.14159$ is defined as the ratio of a Euclidean circle’s circumference to its diameter and appears in every quantitative model of continuous space. An active adelic‑physics program postulates a place‑wise analogue $\pi_p=(p-1)/p$ for each prime $p$, but no geometric computation has verified whether $p$‑adic circle geometry supports such a value, and the archimedean $\pi$ enters every quantitative model that such a program would seek to re‑derive place by place. We therefore compute, in the Haar‑measure framework on $\mathbb{Q}_p^{2}$, the measure of the $p$‑adic “circle’’ $S_{r}=\{x\in\mathbb{Q}_p^{2}:\|x\|=r\}$ and the associated scale‑invariant ratios. The analysis yields the exact formulas  
\[
\mu(B_r)=r^{2},\qquad C_{p}(r)=\mu(S_r)=r^{2}\!\left(1-p^{-2}\right),\qquad 
\kappa_{p}=1-p^{-2},\qquad \kappa'_{p}=\tfrac12\!\left(1-p^{-2}\right),
\]  
independent of the radius $r$. For the first five primes $p=2,3,5,7,11$ the decimal values of $\kappa_{p}$ are listed explicitly. The finite product $\prod_{p\le13}\kappa_{p}=15482880/25050025\approx0.618078$ approximates the Euler product $\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$, with a gap of about $0.010151$, and the all‑place combination $\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$. Comparing $\kappa_{p}$ with the corpus conjecture gives the exact difference $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$, which is non‑zero for every prime and vanishes only asymptotically. Consequently, the Haar‑measure formulation disproves the strong adelic‑$\pi$ conjecture while preserving the weak global product identity. The result provides a concrete consistency check for any adelic model that assumes a place‑wise $\pi_{p}$.

## 1. Introduction

Designers of precision metrology, quantum‑field theorists, and number‑theoretic physicists all rely on the constant $\pi$ as the ratio $C/D$ of a Euclidean circle’s circumference $C$ to its diameter $D$. Because $\pi$ is defined by archimedean geometry, any theory formulated over all Ostrowski completions of $\mathbb{Q}$ must decide whether each non‑archimedean place carries its own circle constant. An active adelic‑physics program asserts that a $p$‑adic analogue $\pi_{p}$ exists at every Ostrowski completion of $\mathbb{Q}$ and that $\pi_{p}=(p-1)/p$ for each prime $p$. If true, any theory formulated over the adeles $\mathbb{A}_{\mathbb{Q}}$ could replace the archimedean $\pi$ by the family $\{\pi_{p}\}$, potentially simplifying adelic regularizations and offering new consistency checks across places. However, no direct geometric computation has tested whether $p$‑adic circle geometry supports any place‑wise constant, let alone the specific value $(p-1)/p$.

We therefore ask: does the ratio $C/D$ admit a well‑defined $p$‑adic counterpart intrinsic to each $\mathbb{Q}_p$, and if so, how does it compare with the corpus conjecture? Our answer is obtained in the Haar‑measure framework, which is the natural analogue of Lebesgue area on $\mathbb{Q}_p^{2}$. The paper proceeds as follows. Section 2 surveys eight works that provide the arithmetic, geometric, and physical context for $p$‑adic constants. Section 3 describes the sup‑norm, Haar‑measure normalization, and the definition of a $p$‑adic circle. Section 4 carries out the full arithmetic derivation of ball and sphere measures, ultrametric diameters, and the resulting ratios $\kappa_{p}$ and $\kappa'_{p}$, together with a term‑by‑term comparison with $\pi_{p}=(p-1)/p$. Section 5 collects the numerical outcomes. Section 7 discusses the implications for the adelic‑$\pi$ conjecture, lists limitations, and states a falsifiability condition. Section 8 translates the findings into practical guidance for adelic modelers, assesses technology readiness, proposes the smallest prototype experiment, and enumerates engineering constraints, cost projections, and misuse risks. The relevant section concludes.

**Contributions.**  
1. An explicit Haar‑measure computation showing $\mu(B_r)=r^{2}$ and $C_{p}(r)=r^{2}(1-p^{-2})$ (Section 4).  
2. The identification of the scale‑invariant ratios $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=(1-p^{-2})/2$, with exact decimal values for $p=2,3,5,7,11$ (Section 4).  
3. The exact evaluation $\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$, the finite‑prime approximation $P_{13}=15482880/25050025\approx0.618078$, and the all‑place product $6/\pi\approx1.909859\neq1$ (Section 4).  
4. A term‑by‑term comparison with the corpus conjecture $\pi_{p}=(p-1)/p$, yielding the exact difference $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$ (Section 4).  
5. A critical assessment of the adelic‑$\pi$ conjecture, including a falsifiability statement and a practical pathway for adelic‑physics participants (Sections 7–7).

## 2. Background and Related Work

The arithmetic of special values provides a natural setting for $p$‑adic analogues of classical constants. Entry [1] formulates a $p$‑adic Beilinson conjecture for number fields, showing that $p$‑adic $L$‑functions and syntomic regulators can parallel the archimedean special‑value formulas; this demonstrates that translating archimedean statements into $p$‑adic language is an active program.  Entry [7] develops the fundamentals of $p$‑adic multiple $L$‑functions and carries out the evaluation of their special values, providing worked instances of how classical special‑value computations transfer to the $p$‑adic setting; both works support the premise that place‑wise analogues of classical constants are a live and computable subject.

In mathematical physics, entry [2] studies phase transitions for a $p$‑adic Potts model on a Cayley tree, showing that $p$‑adic statistical‑mechanical systems exhibit place‑dependent critical phenomena; this motivates the investigation of place‑dependent geometric ratios. Entry [5] proposes a $p$‑adic description of the Higgs mechanism and, in doing so, constructs two concrete $p$‑adic geometric objects: a $p$‑adic square root and a $p$‑adic light cone, showing that physical geometry can be rebuilt place by place from $p$‑adic primitives. Entry [6] develops a $p$‑adic physics program in which the basic geometric and physical objects are rebuilt on $p$‑adic fields, constructing the place‑wise structures that such a program requires; together with [5] it supplies the kind of place‑wise geometric machinery into which a $p$‑adic circle constant such as $\kappa_{p}$ would have to fit.

In combinatorial geometry, entry [4] establishes a $p$‑adic analogue of the van Lint–Seidel relative bound for equiangular lines, deriving an explicit bound on the number of equiangular lines in $\mathbb{Q}_p^{n}$ in terms of $p$‑adic angles; the resulting extremal constants are inherently place‑specific, which is precisely the behavior our computed $\kappa_{p}=1-p^{-2}$ exhibits. The motivating corpus document [9] advocates a harmonic, adelic re‑evaluation of physical constants under Ostrowski’s theorem and explicitly posits $\pi_{p}=(p-1)/p$ at each prime; the Haar‑measure computation tests whether $p$‑adic circle geometry supports this hypothesis.

## 3. Methods

**Arena and norm.**  Fix a prime $p$.  On $\mathbb{Q}_p^{2}$ we use the sup‑norm  
\[
\|x\|=\max\bigl(|x_{1}|_{p},\;|x_{2}|_{p}\bigr),\qquad x=(x_{1},x_{2})\in\mathbb{Q}_p^{2},
\]  
which is the standard ultrametric norm on $\mathbb{Q}_p^{2}$.  The values taken by $\|\cdot\|$ on $\mathbb{Q}_p^{2}\setminus\{0\}$ are exactly $r\in p^{\mathbb Z}$.

**Measure.**  Let $\mu$ be the Haar measure on the additive group $\mathbb{Q}_p^{2}$, normalized by  
\[
\mu(B_{1})=1,\qquad B_{1}=\{x\in\mathbb{Q}_p^{2}:\|x\|\le1\}.
\]  
Haar measure is the unique translation‑invariant Borel measure on $\mathbb{Q}_p^{2}$; under dilation $x\mapsto a x$ it transforms by the factor $|a|_{p}^{2}$.

**Circle.**  For $r\in p^{\mathbb Z}$, $r>0$, define the closed ball and sphere  
\[
B_{r}=\{x:\|x\|\le r\},\qquad S_{r}=\{x:\|x\|=r\}=B_{r}\setminus B_{r/p}.
\]  
$S_{r}$ is the $p$‑adic analogue of a Euclidean circle: it consists of all points at exact distance $r$ from the origin.

**Circumference and diameters.**  
\[
C_{p}(r)=\mu(S_{r}),\qquad D_{p}(r)=\operatorname{diam}(S_{r})=\sup\{\|x-y\|:x,y\in S_{r}\},
\]  
and the archimedean‑style diameter $D'_{p}(r)=2r$.  The candidate constants are the scale‑invariant ratios  
\[
\kappa_{p}=\frac{C_{p}(r)}{D_{p}(r)},\qquad \kappa'_{p}=\frac{C_{p}(r)}{D'_{p}(r)}.
\]

**Corpus comparison.**  We assume the conjecture $\pi_{p}=(p-1)/p$ at each prime for the purpose of comparison.  We treat this as a hypothesis about the same quantity our geometry produces and compute, for each prime, the difference $\kappa_{p}-(p-1)/p$ and the ratio $\kappa_{p}/((p-1)/p)$, as well as the behavior of the product $\prod_{p}(p-1)/p$.

**Adelic product.**  We compute the finite product $P_{N}=\prod_{p\le N}\kappa_{p}$ and combine it with the archimedean ratio $\kappa_{\infty}=\pi$ using the Euler product identity $\prod_{p}(1-p^{-2})=1/\zeta(2)=6/\pi^{2}$.

## 4. Analysis

All inputs are definitions from Section 3, classical number‑theoretic identities, or the assumed conjecture $\pi_{p}=(p-1)/p$ stated in Section 3; no empirical data are used.

**Step 1: Measure of a ball.**  Write $r=p^{m}$ with $m\in\mathbb Z$.  The dilation $x\mapsto p^{-m}x$ sends $B_{1}$ to $B_{r}$, and Haar measure transforms by $|p^{-m}|_{p}^{2}=p^{2m}=r^{2}$.  Hence  
\[
\mu(B_{r})=r^{2}.
\]

**Step 2: Circumference.**  Since $S_{r}=B_{r}\setminus B_{r/p}$,  
\[
C_{p}(r)=\mu(S_{r})=\mu(B_{r})-\mu(B_{r/p})=r^{2}-\left(\frac{r}{p}\right)^{2}
=r^{2}\!\left(1-\frac{1}{p^{2}}\right).
\]

**Step 3: Ultrametric diameter.**  For any $x,y\in S_{r}$, the ultrametric inequality gives $\|x-y\|\le r$.  Choosing $x=(p^{-m}u,0)$ and $y=(0,p^{-m}u)$ with a $p$‑adic unit $u$ yields $\|x-y\|=r$, so  
\[
D_{p}(r)=r.
\]

**Step 4: Ratios.**  
\[
\kappa_{p}=\frac{C_{p}(r)}{D_{p}(r)}=\frac{r^{2}(1-p^{-2})}{r}=1-\frac{1}{p^{2}},
\]  
\[
\kappa'_{p}=\frac{C_{p}(r)}{2r}=\frac{r^{2}(1-p^{-2})}{2r}
=\frac12\!\left(1-\frac{1}{p^{2}}\right).
\]  
Both are independent of $r$.

Explicit values:  

- $p=2$: $\kappa_{2}=3/4=0.75$, $\kappa'_{2}=3/8=0.375$.  
- $p=3$: $\kappa_{3}=8/9\approx0.888889$, $\kappa'_{3}=4/9\approx0.444444$.  
- $p=5$: $\kappa_{5}=24/25=0.96$, $\kappa'_{5}=12/25=0.48$.  
- $p=7$: $\kappa_{7}=48/49\approx0.979592$, $\kappa'_{7}=24/49\approx0.489796$.  
- $p=11$: $\kappa_{11}=120/121\approx0.991736$, $\kappa'_{11}=60/121\approx0.495868$.

**Step 5: Finite adelic product.**  
\[
P_{13}=\frac34\cdot\frac89\cdot\frac{24}{25}\cdot\frac{48}{49}\cdot\frac{120}{121}\cdot\frac{168}{169}
=\frac{15482880}{25050025}\approx0.618078.
\]

**Step 6: Infinite product.**  The Euler product for $\zeta(2)$ gives  
\[
\prod_{p}\kappa_{p}=\prod_{p}\!\left(1-\frac1{p^{2}}\right)=\frac1{\zeta(2)}=\frac6{\pi^{2}}
\approx0.607927.
\]

**Step 7: All‑place combination.**  
\[
\kappa_{\infty}\cdot\prod_{p}\kappa_{p}=\pi\cdot\frac6{\pi^{2}}=\frac6\pi\approx1.909859\neq1.
\]

**Step 8: Comparison with the corpus conjecture $\pi_{p}=(p-1)/p$.**  Using $\kappa_{p}=\frac{(p-1)(p+1)}{p^{2}}$,  
\[
\kappa_{p}-\frac{p-1}{p}
=\frac{(p-1)(p+1)}{p^{2}}-\frac{p(p-1)}{p^{2}}
=\frac{p-1}{p^{2}}.
\]  
The ratio is  
\[
\frac{\kappa_{p}}{(p-1)/p}
=\frac{(p-1)(p+1)/p^{2}}{(p-1)/p}
=\frac{p+1}{p}=1+\frac1p.
\]  
Thus the difference is strictly positive for every prime and tends to $0$ only as $p\to\infty$.

## 5. Results

1. **Ball and sphere measures.**  For $r=p^{m}$, $\mu(B_{r})=r^{2}$ and $C_{p}(r)=r^{2}(1-p^{-2})$ (Steps 1–2).  
2. **Circle constants.**  $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=(1-p^{-2})/2$, independent of $r$ (Step 4).  Exact and decimal values are listed above.  
3. **Finite product.**  $P_{13}=15482880/25050025\approx0.618078$ (Step 5).  
4. **Infinite product.**  $\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$ (Step 6).  
5. **All‑place combination.**  $\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$ (Step 7).  
6. **Corpus comparison.**  $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$ and $\kappa_{p}/((p-1)/p)=1+1/p$ for every prime (Step 8).  

Qualitatively, a place‑wise family of scale‑invariant circle constants exists; each member is rational, bounded by $1$, and tends to $1$ rather than to $\pi$.  The Euler product over all finite places reproduces $6/\pi^{2}$, and the all‑place product with the archimedean factor yields $6/\pi$, confirming that $\pi$ survives only as a global invariant of the finite places, not as any single $\pi_{p}$.

## 6. Extended Derivations and Worked Examples

In this section we deepen the arithmetic analysis of the Haar‑measure constants $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=\tfrac12(1-p^{-2})$, explore limiting regimes, and relate the results to existing $p$‑adic number‑theoretic frameworks.

### 1. Sensitivity of $\kappa_{p}$ to the prime index  

Treating the prime $p$ as a continuous variable $x>1$, the derivative of $\kappa_{x}=1-x^{-2}$ is  
\[
\frac{d\kappa_{x}}{dx}=2x^{-3}.
\]  
For any prime $p$ the absolute change produced by increasing $p$ to the next prime $p'$ satisfies  
\[
|\kappa_{p'}-\kappa_{p}|\le \max_{x\in[p,p']}\bigl|2x^{-3}\bigr|\,(p'-p)
\le 2p^{-3}(p'-p).
\]  
Since $p'-p\le p$ for all $p\ge2$, the bound simplifies to $|\kappa_{p'}-\kappa_{p}|\le2p^{-2}$.  Thus the sequence $\{\kappa_{p}\}$ converges to $1$ at a rate $O(p^{-2})$, confirming the asymptotic statement in the main text.

### 2. Worked example: finite product up to $p=13$  

Using the explicit formula $\kappa_{p}=1-p^{-2}$ we compute the product $P_{13}=\prod_{p\le13}\kappa_{p}$.  The factors are  

\[
\begin{aligned}
\kappa_{2}&=1-2^{-2}= \tfrac34,\\
\kappa_{3}&=1-3^{-2}= \tfrac89,\\
\kappa_{5}&=1-5^{-2}= \tfrac{24}{25},\\
\kappa_{7}&=1-7^{-2}= \tfrac{48}{49},\\
\kappa_{11}&=1-11^{-2}= \tfrac{120}{121},\\
\kappa_{13}&=1-13^{-2}= \tfrac{168}{169}.
\end{aligned}
\]  

Multiplying step‑by‑step (all arithmetic shown explicitly):  

\[
\begin{aligned}
\frac34\cdot\frac89 &= \frac{3\cdot8}{4\cdot9}= \frac{24}{36}= \frac{2}{3},\\[4pt]
\frac{2}{3}\cdot\frac{24}{25} &= \frac{2\cdot24}{3\cdot25}= \frac{48}{75}= \frac{16}{25},\\[4pt]
\frac{16}{25}\cdot\frac{48}{49} &= \frac{16\cdot48}{25\cdot49}= \frac{768}{1225},\\[4pt]
\frac{768}{1225}\cdot\frac{120}{121} &= \frac{768\cdot120}{1225\cdot121}= \frac{92160}{148225},\\[4pt]
\frac{92160}{148225}\cdot\frac{168}{169} &= \frac{92160\cdot168}{148225\cdot169}= \frac{15482880}{25050025}.
\end{aligned}
\]  

Hence  
\[
P_{13}= \frac{15482880}{25050025}\approx0.618078,
\]  
exactly as reported in the main text.  The same fraction appears in the original computation of the Haar‑measure circle constants (see the definition of $P_{13}$ in Section 4).

### 3. Connection with $p$‑adic $L$‑functions  

Entry [3] develops a $p$‑adic Stark regulator attached to an Artin motive and proves an interpolation formula for the associated $p$‑adic $L$‑function $L_{p}(s,\rho)$.  In the special case $s=2$ and a trivial motive, the interpolation factor reduces to the Euler factor $(1-p^{-2})$ (see the discussion of the Euler product in § 3 of [3]).  Consequently the product $\prod_{p\le N}(1-p^{-2})$ that appears in our finite adelic product $P_{N}$ is precisely the product of the $p$‑adic Euler factors of the $L$‑function at $s=2$.  This observation explains why the infinite product $\prod_{p}(1-p^{-2})$ equals $1/\zeta(2)=6/\pi^{2}$, a classical identity recovered in Step 6 of Section 4.

### 4. Comparison with the adelic product formula  

The adelic product formula $\displaystyle\prod_{v}|q|_{v}=1$ for any non‑zero rational $q$ is stated in entry [10] (see the product formula displayed in § 1.3).  Setting $q=p$ and using $|p|_{\infty}=p$ and $|p|_{p}=p^{-1}$, the product over all places reduces to $p\cdot p^{-1}=1$, confirming the consistency of our normalization $\mu(B_{1})=1$ across the finite places.  Moreover, the Euler product $\prod_{p}(1-p^{-2})$ that yields $6/\pi^{2}$ can be interpreted as the product of the non‑archimedean contributions to the special value $\zeta(2)$, while the archimedean factor $\pi^{2}/6$ supplies the complementary infinite‑place contribution.  This decomposition mirrors the adelic factorization discussed in [10].

### 5. Adelic constraints and the strong $\pi_{p}$ conjecture  

Entry [11] frames the broader research program of testing whether adelic completions constrain physical constants.  The explicit computation of $\kappa_{p}=1-p^{-2}$ provides a concrete counterexample to the strong conjecture $\pi_{p}=(p-1)/p$ because the difference  
\[
\kappa_{p}-\frac{p-1}{p}=\frac{p-1}{p^{2}}>0
\]  
holds for every prime (Step 8, Section 4).  The systematic approach advocated in [11]—formulating a falsifiable adelic prediction and then checking it against a mathematically rigorous computation—is precisely what is carried out here.

### 6. Limiting case: $p\to\infty$  

Taking the limit $p\to\infty$ in $\kappa_{p}=1-p^{-2}$ yields  
\[
\lim_{p\to\infty}\kappa_{p}=1.
\]  
In contrast, the conjectured $\pi_{p}=(p-1)/p$ also tends to $1$ as $p\to\infty$, so the two families become indistinguishable in the asymptotic regime.  However, for any finite prime the exact rational values differ, as quantified by the difference $\frac{p-1}{p^{2}}$.  This asymptotic agreement explains why the weak global product identity $\pi\prod_{p}\kappa_{p}=6/\pi$ survives (Section 4, Step 7) even though the strong place‑wise identification fails.

### 7. Worked example: alternative norm  

If one replaces the sup‑norm $\|x\|_{\infty}=\max(|x_{1}|_{p},|x_{2}|_{p})$ by the $p$‑adic Euclidean‑style norm $\|x\|_{E}=\sqrt{|x_{1}|_{p}^{2}+|x_{2}|_{p}^{2}}$, the ball $B_{r}^{E}=\{x:\|x\|_{E}\le r\}$ still satisfies $\mu(B_{r}^{E})=r^{2}$ because Haar measure scales with $|a|_{p}^{2}$ under dilation $x\mapsto a x$.  However, the sphere $S_{r}^{E}=B_{r}^{E}\setminus B_{r/p}^{E}$ now has measure  
\[
\mu(S_{r}^{E})=r^{2}\!\left(1-p^{-1}\right),
\]  
since the annulus thickness in the Euclidean‑style norm is $r-p^{-1}r=r(1-p^{-1})$.  The corresponding ratio becomes $\kappa_{p}^{E}=1-p^{-1}$, which decays more slowly than $1-p^{-2}$.  This alternative illustrates how the choice of norm (a constraint listed in Section 7(d)) directly influences the resulting circle constant, and it provides a concrete “what‑if” scenario for future investigations.  

These extended derivations and examples reinforce the main conclusions, situate the Haar‑measure constants within the broader $p$‑adic analytic landscape, and highlight the precise ways in which the strong adelic‑$\pi$ conjecture is falsified while the weak adelic product structure remains intact.

## 7. Discussion

**Implications for the adelic‑$\pi$ conjecture.**  In the Haar‑measure formulation the strong conjecture—existence of a place‑wise family $\{\pi_{p}\}$ interpolating toward $\pi$—fails: the computed constants $\kappa_{p}$ are rational, depend on $p$, and satisfy $\lim_{p\to\infty}\kappa_{p}=1\neq\pi$.  The weak form survives because $\pi$ reappears as the global invariant $\prod_{p}\kappa_{p}=6/\pi^{2}$.

**Limitations.**  
1. *Definition of circumference.*  We defined $C_{p}(r)$ as Haar measure of $S_{r}$.  Since $\mathbb{Q}_p$ is totally disconnected, $S_{r}$ is not a topological boundary; alternative definitions (e.g. $p$‑adic line integrals) could yield different constants.  
2. *Diameter convention.*  Both the ultrametric diameter $D_{p}(r)=r$ and the archimedean‑style diameter $D'_{p}(r)=2r$ were reported.  Different conventions would alter $\kappa'_{p}$ but not $\kappa_{p}$.  
3. *Normalization.*  The choice $\mu(B_{1})=1$ fixes the overall scale; any other normalization rescales $C_{p}(r)$ and $D_{p}(r)$ proportionally, leaving the ratios unchanged.  
4. *Euler product interpretation.*  The identity $\prod_{p}(1-p^{-2})=6/\pi^{2}$ is a number‑theoretic theorem; its appearance does not imply a geometric adelic circle structure beyond the product formula.

**What would falsify the main claim.**  If a construction produced a $p$‑adic circle constant $\pi_{p}$ satisfying $\pi_{p}\to\pi$ as $p\to\infty$, or if an adelic product of geometrically defined constants equaled $1$ under a principled normalization, then our conclusion that the Haar‑measure formulation fails would be falsified.

**Open questions.**  
- Do other norms on $\mathbb{Q}_p^{2}$ (e.g. a Euclidean‑style $p$‑adic norm) produce irrational or $\pi$‑approaching constants?  
- Can a $p$‑adic analogue of arc length be defined via a parametrization that yields a non‑rational constant?  
- How does the harmonic‑paradigm program adapt if one replaces the simple Haar‑measure circle by a more sophisticated $p$‑adic geometric object?

## 8. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  Number‑theoretic physicists and mathematicians developing adelic formulations of quantum field theory would use the derived constants $\kappa_{p}$ to benchmark any proposed $p$‑adic geometric construction.  If a new $p$‑adic model claims to reproduce $\pi$ at each place, the explicit values $\kappa_{p}=1-p^{-2}$ provide a minimal consistency check: the model must either reproduce these rational numbers or justify a different definition of circumference.

**(b) Technology readiness.**  The work is purely analytical, has not undergone peer review, and therefore resides at NASA Technology Readiness Level 1–2.  As an analytical study it cannot exceed TRL 3.

**(c) Smallest next experiment/prototype/calculation.**  The most direct de‑risking step is an independent recomputation of the $p$‑adic ball and sphere measures using an alternative definition of circumference, for example defining $C_p(r)$ as the Haar measure of the boundary of $B_r$ in the sense of a $p$‑adic line integral.  If that calculation yields a constant different from $\kappa_p=1-p^{-2}$, the present result would be falsified.

**(d) Binding engineering constraints.**  The derivation relies on (i) the sup‑norm on $\mathbb{Q}_p^{2}$, (ii) the normalization $\mu(B_1)=1$, and (iii) the use of Haar measure; any change to these conventions would alter the numerical constants.  These are therefore the primary constraints; all other potential constraints (material, energy, cost) are open questions for future implementation.

**(e) Order‑of‑magnitude projections.**  Under the existing normalization, the sphere measure scales as $C_p(r)=r^{2}(1-p^{-2})$, so for a unit radius $r=1$ the measure is bounded by $0< C_p(1)<1$.  No further cost or performance projection is applicable beyond this analytic bound.

**(f) Direct risks or misuse paths.**  Misapplication could occur if a modeler assumes $\kappa_p$ to be a physical length‑to‑circumference ratio in a setting where a genuine $p$‑adic notion of arc length is required; this would lead to incorrect predictions of scale‑dependent phenomena.

## Conclusion

We have computed, with fully displayed arithmetic, the Haar‑measure geometry of $p$‑adic circles in $\mathbb{Q}_p^2$: the sphere of radius $r$ has measure $r^2(1-p^{-2})$, the ultrametric diameter equals $r$, and the resulting scale‑invariant circle constants are $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$. These constants are rational, place‑dependent, bounded by $1$, and tend to $1$ rather than to $\pi$. The Euler product over all finite places equals $6/\pi^2\approx0.607927$, and the all‑place product including the archimedean factor is $6/\pi\approx1.909859\neq1$. Hence the adelic‑$\pi$ conjecture, in its strong Haar‑measure formulation, fails place‑wise while surviving globally: $\pi$ appears only as a product invariant of the finite places, not as any single $\pi_p$.

Thus, the Haar‑measure analysis provides a definitive answer to the question of a $p$‑adic circle constant within the chosen geometric framework, and delineates the precise way in which adelic consistency is achieved without invoking a place‑wise $\pi_p$ equal to $(p-1)/p$.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence Report; Appendix B. Claim Attribution. references 12 -> 8. length 3282 -> 2819 words.
- Version 2.1.0 (2026-10-23, from 2.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. sections folded or removed: Appendix A. Divergence Report; Appendix B. Claim Attribution. references 8 -> 10. length 2863 -> 3243 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.0-no-registrar). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On the p-adic Beilinson conjecture for number fields. arXiv:0707.3682v2. https://arxiv.org/abs/0707.3682v2
[2] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[3] On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives. arXiv:2103.06864v4. https://arxiv.org/abs/2103.06864v4
[4] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound. arXiv:2408.00810v3. https://arxiv.org/abs/2408.00810v3
[5] p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone. arXiv:hep-th/9410058v3. https://arxiv.org/abs/hep-th/9410058v3
[6] p-Adic TGD: Mathematical Ideas. arXiv:hep-th/9506097v2. https://arxiv.org/abs/hep-th/9506097v2
[7] Fundamentals of p-adic multiple L-functions and evaluation of their special values. arXiv:1508.07185v2. https://arxiv.org/abs/1508.07185v2
[9] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation. QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis.
[10] https://papers.qnfo.org/papers/measure-theoretic-artifacts-archimedean-place. QNFO: Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science.
[11] https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-1. QNFO: Adelic Constraints on Quantum Field Theory: Phase 1.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:0707.3682v2 | On the p-adic Beilinson conjecture for number fields
arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree
arXiv:2103.06864v4 | On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives
arXiv:2408.00810v3 | p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound
arXiv:hep-th/9410058v3 | p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone
arXiv:hep-th/9506097v2 | p-Adic TGD: Mathematical Ideas
arXiv:1508.07185v2 | Fundamentals of p-adic multiple L-functions and evaluation of their special values

## QNFO corpus context (Vectorize)

QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis | https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation
QNFO: Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$ | https://papers.qnfo.org/papers/is-there-a-p-adic-pi-haar-measure-circle-constants-over-mathbb-q-p-and-an-adelic
QNFO: Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science | https://papers.qnfo.org/papers/measure-theoretic-artifacts-archimedean-place
QNFO: Adelic Constraints on Quantum Field Theory: Phase 1 | https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-1

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:0707.3682v2 | On the p-adic Beilinson conjecture for number fields
  We formulate a conjectural p-adic analogue of Borel's theorem relating regulators for higher K-groups of number fields to special values of the corresponding zeta-functions, using syntomic regulators and p-adic L-functions. We also formulate a corresponding conjecture for Artin motives, and state a conjecture about the precise relation between the p-adic and classical situations. Parts of he conje
  Full text (https://arxiv.org/html/0707.3682v2), excerpts of its own sections:
  § 1. Introduction: The Beilinson conjectures about special values of $L$ -functions   [ 2 ] are a far reaching generalization of the class number formula for the Dedekind zeta function. For every algebraic variety $X$ over the rationals it predicts the leading term of the Taylor expansions of $L(H^{i}(X),s)$ at certain points, up to a rational multiple, in terms of arithmetic information associated with $X$ , namely, its algebraic K-groups $K_{j}(X)$   [ 43 ] . More generally, these conjectures can also be formulated for motives. There have been several important steps taken towards verification of these conjectures in various cases, although, strictly speaking they have only been verified completely in the case where $X$ is the spectrum of a number field, where they follow from famous theorems of Borel  [ 10 , 11 ] . To motivate what follows, let us briefly recall the conjecture that interests us the most (for an introduction see  [ 23 , 46 ] ). One associates with $X$ two cohomology groups. [...]
  § 2. The $p$ -adic Beilinson conjecture for totally real fields: Let $k$ be a number field with $r_{1}$ real embeddings, $2r_{2}$ complex embeddings, ring of algebraic integers ${\mathcal{O}}_{k}$ , and discriminant $D_{k}$ . As is well-known, ${\mathcal{O}}_{k}^{*}$ is a finitely generated Abelian group of rank $r=r_{1}+r_{2}-1$ , and its regulator $R$ satisfies $w\sqrt{|D_{k}|}\,\text{Res}_{s=1}\zeta_{k}(s)=2^{r_{1}}(2\pi)^{r_{2}}\,|\text{Cl}({\mathcal{O}}_{k})|\,R$ , with $\text{Cl}({\mathcal{O}}_{k})$ the class group of ${\mathcal{O}}_{k}$ , and $w$ the number of roots of unity in $k$ . Because $K_{0}({\mathcal{O}}_{k})\cong\text{Cl}({\mathcal{O}}_{k})\oplus\mathbb{Z}$ and $K_{1}({\mathcal{O}}_{k})\cong{\mathcal{O}}_{k}^{*}$ , so $|\text{Cl}({\mathcal{O}}_{k})|=|K_{0}({\mathcal{O}}_{k})_{\text{tor}}|$ and $w=|K_{1}({\mathcal{O}}_{k})_{\text{tor}}|$ , this can be interpreted as a statement about the $K$ -theory of ${\mathcal{O}}_{k}$ , and it is from this point of view that it can be generalized to $\zeta_{k}(n)$ for $n\geq 2$ . [...]
  § 3. A motivic version of the conjecture: If $E$ is any extension of $\mathbb{Q}$ , and $k/\mathbb{Q}$ is finite and Galois with Galois group $G$ , then we let $M^{E}=E\otimes_{\mathbb{Q}}k$ and $K_{2n-1}(k)_{E}=E\otimes_{\mathbb{Q}}K_{2n-1}(k)_{\mathbb{Q}}$ , which are $E[G]$ -modules. The goal of this section is to refine Conjecture  2.17 to a conjecture for Artin motives with coefficients in $E$ , or equivalently, idempotents in the group ring $E[G]$ , when $E$ is a number field. Definition 3.1 . For an idempotent $\pi$ in $E[G]$ we let $M_{\pi}^{E}=\pi M^{E}$ and $K_{2n-1}(M_{\pi}^{E})=\pi K_{2n-1}(k)_{E}$ . Now fix an embedding $\phi_{\infty}:k\to\mathbb{C}$ . The pairing $G\times k\to\mathbb{C}$ mapping $(\sigma,a)$ to $\phi_{\infty}(\sigma(a))$ leads to an $E$ -bilinear pairing (3.2) $\displaystyle E[G]\times M^{E}$ $\displaystyle\to E\otimes_{\mathbb{Q}}\mathbb{C}$ $\displaystyle(e\sigma,e^{\prime}\otimes a)$ $\displaystyle\mapsto ee^{\prime}\otimes\phi_{\infty}(\sigma(a))\,.$ and we consider its restriction $(\,\cdot\,,\,\cdot\,)_{\infty}:E[G]\pi\times M_{\pi}^{E}\to E\otimes_{\mathbb{Q}}\mathbb{C}\,. [...]
  § 4. More explicit $K$ -groups and regulators: In this section we first describe an inductive procedure that conjecturally gives $K_{2n-1}(k)_{\mathbb{Q}}$ ( $n\geq 2$ ) for any number field $k$ . It is originally due to Zagier [ 54 ] , but we essentially give a reformulation by Deligne [ 21 ] . We also describe results concerning Conjecture  3.18 when the action of $G$ on $E[G]\pi$ is Abelian. [...]
[2] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree
  In the paper we considere three state $p$-adic Potts model with competing interactions on a Cayley tree of order two. We reduce a problem of describing of the $p$-adic Gibbs measures to the solution of certain recursive equation, and using it we will prove that a phase transition occurs if and only if $p=3$ for any value (non zero) of interactions. As well, we completely solve the uniqueness probl
  Full text (https://arxiv.org/html/math-ph/0512018v2), excerpts of its own sections:
  § 1. Introduction: A non-Kolmogorovian probability models [ 7 ] , [ 8 ] in that probabilities belong to the filed of $p$ -adic numbers ${\mathbb{Q}}_{p}$ were developed in connection with $p$ -adic quantum models (see for example, [ 1 ] , [ 6 ] , [ 14 ] , [ 22 ] ). In [ 7 ] , [ 9 ] a measure-theoretical axiomatics of the $p$ -adic probability theory were proceeded. In [ 10 ] , [ 12 ] certain, various limit theorems for $p$ -adic valued probabilities have been proved. In [ 11 ] the theory of stochastic processes with values in $p$ -adic and more general non-Archimedean fields having probability distributions with non-Archimedean values has been developed. There a non-Archimedean analogue of the Kolmogorov theorem was proved, that gives the opportunity to construct wide classes of stochastic processes by using finite dimensional probability distributions. This allowed us to begin the study and the development of certain problems of statistical mechanics in a context of the $p$ -adic probability theory. [...]
  § 2.1. $p$ -adic numbers and measures: Let ${\mathbb{Q}}$ be the field of rational numbers. Throughout the paper $p$ will be a fixed prime number. Every rational number $x\neq 0$ can be represented in the form $x=p^{r}\frac{n}{m}$ , where $r,n\in{\mathbb{Z}}$ , $m$ is a positive integer and $p,n,m$ are relatively prime. The $p$ -adic norm of $x$ is given by $|x|_{p}=p^{-r}$ and $|0|_{p}=0$ . This norm satisfies so called the strong triangle inequality $|x+y|_{p}\leq\max\{|x|_{p},|y|_{p}\}.$ This is a ultrametricity of the norm. The completion of ${\mathbb{Q}}$ with respect to $p$ -adic norm defines the $p$ -adic field which is denoted by ${\mathbb{Q}}_{p}$ . Let $B(a,r)=\{x\in{\mathbb{Q}}_{p}|\ |x-a|_{p} 0$ . By $\log_{p}$ and $\exp_{p}$ we mean $p$ -adic logarithm and exponential which are defined as series with the usual way (see, for more details [ 13 ] ). The domain of converge for them are $B(1,1)$ and $B(0,p^{-1/(p-1)})$ respectively. [...]
  § 2.2. The Cayley tree: The Cayley tree $\Gamma^{k}$ of order $k\geq 1$ is an infinite tree, i.e., a graph without cycles, such that each vertex of which lies on $k+1$ edges . Let $\Gamma^{k}=(V,\Lambda),$ where $V$ is the set of vertices of $\Gamma^{k}$ , $\Lambda$ is the set of edges of $\Gamma^{k}$ . The vertices $x$ and $y$ are called nearest neighbor , which is denoted by $l= $ if there exists an edge connecting them. A collection of the pairs $ ,..., $ is called a path from $x$ to $y$ . [...]
  § 5. Conclusions: In the paper we have considered three state $p$ -adic Potts model with competing interactions on a Cayley tree order two. We reduced a problem of describing of the $p$ -adic Gibbs measures to the solution of certain recursive equation, and using it we proved that a phase transition occurs if and only if $p=3$ for any value (non zero) of interactions. If $p\neq 3$ we showed that there is only a unique Gibbs measure for the inhomogeneous Potts model with zero external filed, as well as we established that result for homogeneous model but with non-zero external filed. From these results we conclude that a phase transition depends only on a value of $p$ . These results totaly different from the real case, since in this setting there is a phase transition on some constraints for the interaction parameters (see [ 3 ] , [ 18 ] ). When a $p$ -adic Gibbs measure is unique, then by means of a method of paper [ 16 ] one can be shown that the measure is bounded as well. The results concerning the uniqueness of the Gibbs measures extend results obtained in [ 16 , 17 ] . [...]
[3] arXiv:2103.06864v4 | On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives
  Given an odd prime number $p$ and a $p$-stabilized Artin representation $ρ$ over $\mathbb{Q}$, we introduce a family of $p$-adic Stark regulators and we formulate an Iwasawa-Greenberg main conjecture and a $p$-adic Stark conjecture which can be seen as an explicit strengthening of conjectures by Perrin-Riou and Benois in the context of Artin motives. We show that these conjectures imply the $p$-pa
  Full text (https://arxiv.org/html/2103.06864v4), excerpts of its own sections:
  § 1. Introduction: Iwasawa theory traditionally focuses on the construction of $p$ -adic $L$ -functions and on their relation with arithmetic invariants of number fields. Concurrently with the first major achievements of the theory [ MW84 , Wil90 , Rub91 ] , several attempts were made in order to define the conjectural $p$ -adic $L$ -function of a motive [ CPR89 , Coa91 , Gre94 ] and its corresponding Selmer group [ Gre89 , Gre91 ] . [...]
  § 1.2. The main results: We fix once and for all an odd prime $p$ at which $\rho$ is unramified. Our first result (Theorem 3.7.4 ) generalizes [ Mak21 , Théorème A] and yields an interpolation formula for a generator of $\textrm{char}_{\Lambda}X_{\infty}(\rho,\rho^{+})$ which is similar to EX ${}_{\rho,\rho^{+}}$ . As a piece of notation, we let $U_{\infty}=\varprojlim_{n}U_{n}$ be the $\Lambda$ -module of all norm-coherent sequences of elements in the pro- $p$ completion $U_{n}$ of the group of units of $H\cdot\mathbb{Q}_{n}$ . It is a finitely generated $\Lambda$ -module endowed with a linear action of $\Gal(H\cdot\mathbb{Q}_{\infty}/\mathbb{Q}_{\infty})$ . Theorem A . (1) Fix a $G_{\mathbb{Q}}$ -stable $\mathcal{O}_{p}$ -lattice $T_{p}$ of $W_{p}$ , a $p$ -stabilization $\rho^{+}$ of $\rho$ and a $T_{p}$ -optimal basis $\omega_{p}^{+}=t_{1}\wedge\ldots\wedge t_{d^{+}}$ of $\det W_{p}^{+}$ . [...]
  § 2.1. Classical results on Coleman maps: Fix an odd prime number $p$ . Let $K$ be an unramified finite extension of ${\mathbb{Q}_{p}}$ and let $\varphi\in\Gal(K/{\mathbb{Q}_{p}})$ be the Frobenius automorphism. The Galois group $\Gal(K(\mu_{p^{\infty}})/{\mathbb{Q}_{p}})$ splits into a product $\Gal(K/{\mathbb{Q}_{p}})\times\Gamma_{{\cyc}}\simeq\Gal(K/{\mathbb{Q}_{p}})\times\Gamma\times\Gal(K(\mu_{p})/K)$ , where we have put $\Gamma_{{\cyc}}=\Gal(K(\mu_{p^{\infty}})/K)$ and where $\Gamma$ is the Galois group of ${\mathbb{Z}_{p}}$ -cyclotomic extension of $K$ . The cyclotomic character induces an isomorphism $\chi_{\cyc}:\Gamma_{{\cyc}}\simeq\mathbb{Z}^{\times}_{p}$ and $\Gamma$ can be identified with $1+p{\mathbb{Z}_{p}}\subset\mathbb{Z}^{\times}_{p}$ . Let us fix once and for all a system of compatible roots of unity $\tilde{\zeta}:=(\zeta_{n})_{n\geq 0}$ of $p$ -power order ( i.e. , $\zeta_{n+1}^{p}=\zeta_{n}$ , $\zeta_{0}=1$ and $\zeta_{1}\neq 1$ ). [...]
  § 5.3. Iwasawa main conjectures: In the two last sections we explore the relation between Conjecture A and the various conjectures on Rubin-Stark elements of § 4.1 . We henceforth assume that $\chi$ is of prime-to- $p$ order. In what follows, the basis of a given $p$ -stabilization $W_{p}^{+}$ of $W_{p}$ is always assumed to be a $T_{p}$ -optimal eigenbasis for $\sigma_{p}$ as in Lemma 3.7.3 . Theorem 5.3.1 . Assume Conjectures 4.1.3 and 4.1.4 and pick any $p$ -stabilization $W_{p}^{+}$ of $W_{p}$ . (1) The statement EX ${}_{\rho,\rho^{+}}$ in Conjecture A is true, and the element $\theta_{\rho,\rho^{+}}^{\prime}$ of Proposition 3.3.3 coincides with $\mathscr{C}^{\mathrm{str}}_{\omega_{p}^{+}}(\psi_{\varepsilon_{\infty}^{\chi}})$ , where $\mathscr{C}_{\omega_{p}^{+}}^{\mathrm{str}}$ is the operator introduced in § 3.7 . (2) Conjecture 4.2.2 implies that $\theta_{\rho,\rho^{+}}$ has an order of vanishing at $\mathds{1}$ greater than or equal to $e$ . The converse implication also holds if we moreover assume that $W_{p}^{+}$ is admissible and that $\mathcal{L}(\rho,\rho^{+})$ does not vanish. Proof. [...]
[4] arXiv:2408.00810v3 | p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound
  We introduce the notion of p-adic equiangular lines and derive the first fundamental relation between common angle, dimension of the space and the number of lines. More precisely, we show that if $\{τ_j\}_{j=1}^n$ is p-adic $γ$-equiangular lines in $\mathbb{Q}^d_p$, then \begin{align*} (1) \quad\quad \quad \quad |n|^2\leq |d|\max\{|n|, γ^2 \}. \end{align*} We call Inequality (1) as the p-adic van 
  Full text (https://arxiv.org/html/2408.00810v3), excerpts of its own sections:
  § 1. Introduction: Let $d\in\mathbb{N}$ and $\gamma\in[0,1]$ . Recall that a collection $\{\tau_{j}\}_{j=1}^{n}$ of unit vectors in $\mathbb{R}^{d}$ is said to be $\gamma$ -equiangular lines [ 4 , 8 ] if $\displaystyle|\langle\tau_{j},\tau_{k}\rangle|=\gamma,\quad\forall 1\leq j,k\leq n,j\neq k.$ A fundamental problem associated with equiangular lines is the following. Problem 1.1 . Given $d\in\mathbb{N}$ and $\gamma\in[0,1]$ , what is the upper bound on $n$ such that there exists a collection $\{\tau_{j}\}_{j=1}^{n}$ of $\gamma$ -equiangular lines in $\mathbb{R}^{d}$ ? An answer to Problem 1.1 , which is fundamental driving force in the study of equiangular lines, is the following result of van Lint and Seidel [ 9 , 8 ] . Theorem 1.2 . [ 9 , 8 ] ( van Lint-Seidel Relative Bound ) Let $\{\tau_{j}\}_{j=1}^{n}$ be $\gamma$ -equiangular lines in $\mathbb{R}^{d}$ . Then $\displaystyle n(1-d\gamma^{2})\leq d(1-\gamma^{2}).$ In particular, if $\displaystyle\gamma then $\displaystyle n\leq\frac{d(1-\gamma^{2})}{1-d\gamma^{2}}. [...]
  § 2. $p$ -adic Equiangular Lines: We begin by recalling the notion of $p$ -adic Hilbert space. We refer [ 5 , 2 , 3 , 6 , 1 ] for more information on $p$ -adic Hilbert spaces. Definition 2.1 . [ 2 , 3 ] Let $\mathbb{K}$ be a non-Archimedean valued field with valuation $|\cdot|$ and $\mathcal{X}$ be a non-Archimedean Banach space with norm $\|\cdot\|$ over $\mathbb{K}$ . We say that $\mathcal{X}$ is a $p$ -adic Hilbert space if there is a map (called as $p$ -adic inner product) $\langle\cdot,\cdot\rangle:\mathcal{X}\times\mathcal{X}\to\mathbb{K}$ satisfying following. (i) If $x\in\mathcal{X}$ is such that $\langle x,y\rangle=0$ for all $y\in\mathcal{X}$ , then $x=0$ . (ii) $\langle x,y\rangle=\langle y,x\rangle$ for all $x,y\in\mathcal{X}$ . (iii) $\langle\alpha x,y+z\rangle=\alpha(\langle x,y\rangle+\langle x,z\rangle)$ for all $\alpha\in\mathbb{K}$ , for all $x,y,z\in\mathcal{X}$ . (iv) $|\langle x,y\rangle|\leq\|x\|\|y\|$ for all $x,y\in\mathcal{X}$ . The following is the standard example of a $p$ -adic Hilbert space which we consider in the paper. Example 2.2 . [ 5 ] Let $p$ be a prime. [...]
[5] arXiv:hep-th/9410058v3 | p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone
  This paper is the first one in the series devoted to the calculation of particle mass spectrum in Topological GeometroDynamics. TGD Universe is critical at quantum level and an attractive idea to realize criticality is via conformal invariance. Ordinary real numbers do not allow this but if one assumes that in long length scales p-adic topology replaces real topology as effective topology situatio
  Full text (https://arxiv.org/html/hep-th/9410058v3), excerpts of its own sections:
  § 1 Introduction: Quantum TGD has developed during past sixteen years from an attractive idea for realizing Poincare invariant gravitation to a quantitative theory of basic interactions. The basic features of TGD [ Pitkänena , Pitkänenb ] relevant for this work are following. a) TGD spacetime is surface of space $H=M^{4}_{+}\times CP_{2}$ . The topology of 2-space is generalized to the concept of topological condensate: particle like 3-surfaces are glued by topological sum operation to larger 3-surface, which in turned are glued to larger surface and a many sheeted fractal like structure results. 3-surfaces can have boundaries. Even the boundaries of macroscopic objects correspond to boundaries of 3-surface. 3-space need not be even connected: topological evaporation or the formation of Baby Universe is in key role in TGD even at elementary particle length scales. b) Quantum TGD describes Universe, which is critical at quantum level. The breakthrough through the realization that p-adic numbers [ Brekke and Freund ] might provide technical tool for realizing criticality in four dimensions. [...]
  § 2 p-Adic square root function and p-adic light cone: The corner stone of the p-adic TGD is the following observation related to the existence of square root of real p-adic number: the algebraic extensions of p-adic numbers allowing square root near p-adic real axis have dimension $D=4$ in $p>2$ -adic case and dimension $D=8$ in 2-adic case. The proof of the result was based on the Taylor expansion of square root and number theoretic facts. Unfortunately the question about the radius of the convergence was not considered at all. The worst situation would be that convergence radius is zero! This is not the case and the region of spacetime allowing square root function can be regarded as the p-adic counterpart of the future light cone. The result demonstrates nice consistency of p-adic TGD with the general assumptions of TGD and that big bang cosmology might be related to the existence of p-adic square root!
  § 2.1 p-Adic square root function for $p>2$: The study of the properties of the series representation of square root function shows that the definition of square root function is possible in certain region around real p-adic axis. What is nice that this region can be regarded as the p-adic counterpart of the future light cone defined by the condition $\displaystyle N_{p}(Im(Z))$ $\displaystyle $\displaystyle N_{p}(t=Re(Z))=p^{k}$ (1) where the real p-adic coordinate $t=Re(Z)$ is identified as time coordinate and the imaginary part of the p-adic coordinate is identified as spatial coordinate. p-Adic norm for four-dimensional extension is analogous to ordinary Euclidian distance. p-Adic light cone consists of ’cylinders’ parallel to time axis having radius $N_{p}(t)=p^{k}$ and length $p^{k-1}(p-1)$ : at points $t=p^{k}$ . As a real space (recall the canonical correspondence) the cross section of the cylinder corresponds to parallelpiped rather than ball. The result can be understood heuristically as follows. [...]
  § 2.2 Convergence radius for square root function: In the following it will be shown that the convergence radius of $\sqrt{t+Z}$ is indeed nonvanishing for $p>2$ . The expression for the Taylor series of $\sqrt{t+Z}$ reads as $\displaystyle\sqrt{t+Z}$ $\displaystyle=$ $\displaystyle=\sqrt{x}\sum_{n}a_{n}$ $\displaystyle a_{n}$ $\displaystyle=$ $\displaystyle(-1)^{n}\frac{(2n-3)!!}{2^{n}n!}x^{n}$ $\displaystyle x$ $\displaystyle=$ $\displaystyle\frac{Z}{t}$ (9) The necessary criterion for the convergence is that the terms of the power [...]
[6] arXiv:hep-th/9506097v2 | p-Adic TGD: Mathematical Ideas
  The mathematical basis of p-adic Higgs mechanism discussed in papers hep-th@xxx.lanl.gov 9410058-62 is considered in this paper. The basic properties of p-adic numbers, of their algebraic extensions and the so called canonical identification between positive real numbers and p-adic numbers are described. Canonical identification induces p-adic topology and differentiable structure on real axis and
  Full text (https://arxiv.org/html/hep-th/9506097v2), excerpts of its own sections:
  § 1 Introduction: There are a lot of speculations about the role of p-adic numbers in Physics [ Volovich , Freund and Olson , Gervais ] . In [ Brekke and Freund ] one can find a review of the work done. In general the work is related to quantum theory and based on assumption that quantum mechanical state space is ordinary complex Hilbert space. This is not absolutely necessary since p-adic unitarity and probability concepts make sense [ Khrennikov ] . What is however essential is some kind of correspondence between p-adic and real numbers since the predictions of, say, p-adic quantum mechanics should be expressed in terms of real numbers. The formulation of physical theory using p-adic state space and p-adic dynamical variables requires also the construction of p-adic differential and integral calculus. Also the p-adic counterpart of Riemann geometry as well as group theory are needed. In this chapter the aim is to carry out these generalizations. [...]
  § 2 p-Adic numbers: p-Adic numbers ( $p$ is prime: 2,3,5,… ) can be regarded as a completion of rational numbers using norm which, is different from the ordinary norm of real numbers [ Borevich and Shafarevich ] . p-Adic numbers are representable as power expansion of the prime number $p$ of form: $\displaystyle x$ $\displaystyle=$ $\displaystyle\sum_{k\geq k_{0}}x(k)p^{k},\ x(k)=0,....,p-1$ (1) The norm of a p-adic number given by $\displaystyle|x|$ $\displaystyle=$ $\displaystyle p^{-k_{0}(x)}$ (2) Here $k_{0}(x)$ is the lowest power in the expansion of p-adic number. The norm differs drastically from the norm of ordinary real numbers since it depends on the lowest pinary digit of the p-adic number only. Arbitrarily high powers in the expansion are possible since the norm of p-adic number is finite also for numbers, which are infinite with respect to the ordinary norm. A convenient representation for p-adic numbers is in the form $\displaystyle x$ $\displaystyle=$ $\displaystyle p^{k_{0}}\varepsilon(x)$ (3) where $\varepsilon(x)=k+.... [...]
  § 3 Canonical correspondence between p-adic and real numbers: There exists a natural continuous map $Id:R_{p}\rightarrow R_{+}$ from p-adic numbers to non-negative real numbers given by the ”pinary” expansion of the real number for $x\in R$ and $y\in R_{p}$ this correspondence reads $\displaystyle y$ $\displaystyle=$ $\displaystyle\sum_{k>N}y_{k}p^{k}\rightarrow x=\sum_{k $\displaystyle y_{k}$ $\displaystyle\in$ $\displaystyle\{0,1,..,p-1\}$ (6) This map is continuous as one easily finds out. There is however a little difficulty associated with the definition of the inverse map since the pinary expansion like also desimal expansion is not unique ( $1=0.999... [...]
  § 4 Algebraic extensions of p-adic numbers: Real numbers allow only complex numbers as an algebraic extension. For p-adic numbers algebraic extensions of arbitrary dimension are possible [ Borevich and Shafarevich ] . The simplest manner to construct (n+1)-dimensional extensions is to consider irreducible polynomials $P_{n}(t)$ in $R_{p}$ assumed to have rational coefficients: irreduciblity means that polynomial does not possess roots in $R_{p}$ so that one cannot decompose it into a product of lower order $R_{p}$ valued polynomials. [...]
  § 5 Algebraic extension allowing square root on p-adic real axis: The existence of square root of «real« p-adic number is a common theme in various applications of p-adic numbers. a) The p-adic generalization of the representation theory of ordinary groups and Super Kac Moody and Super Virasoro algebras exists provided an extension of p-adic numbers [...]
[7] arXiv:1508.07185v2 | Fundamentals of p-adic multiple L-functions and evaluation of their special values
  We construct $p$-adic multiple $L$-functions in several variables, which are generalizations of the classical Kubota-Leopoldt $p$-adic $L$-functions, by using a specific $p$-adic measure. Our construction is from the $p$-adic analytic side of view, and we establish various fundamental properties of these functions.
  Full text (https://arxiv.org/html/1508.07185v2), excerpts of its own sections:
  § 0. Introduction: Let $\mathbb{N}$ , $\mathbb{N}_{0}$ , $\mathbb{Z}$ , $\mathbb{Q}$ , $\mathbb{R}$ and $\mathbb{C}$ be the set of natural numbers, non-negative integers, rational integers, rational numbers, real numbers and complex numbers, respectively. For $s\in\mathbb{C}$ , denote by $\Re s$ and $\Im s$ the real and the imaginary parts of $s$ , respectively. The aim of the present paper is to introduce $p$ -adic multiple $L$ -functions, multiple analogues of Kubota-Leopoldt $p$ -adic $L$ -functions, and show basic properties, particularly their special values at both positive and non-positive integer points. The construction of these functions is motivated by the technique of desingularization of complex multiple zeta functions and a certain evaluation method of their special values at non-positive integer points, which were introduced and developed in our previous paper [ 12 ] . In Definition 1.16 , we construct the multivariable $p$ -adic multiple $L$ -function , $L_{p,r}(s_{1},\ldots,s_{r};\omega^{k_{1}},\ldots,\omega^{k_{r}};\gamma_{1},\ldots,\gamma_{r};c). [...]
  § 1. $p$ -adic multiple $L$ -functions: In this section, we will construct certain $p$ -adic multiple $L$ -functions (Definition 1.16 ) which can be regarded as multiple analogues of Kubota-Leopoldt $p$ -adic $L$ -functions, as well as $p$ -adic analogues of complex multiple $L$ - (zeta-)functions. We then investigate some of their $p$ -adic properties; in particular, we shall prove $p$ -adic analyticity with respect to certain variables, in Theorem 1.21 , and $p$ -adic continuity with respect to other variables, in Theorem 1.24 .
  § 1.1. Kubota-Leopoldt $p$ -adic $L$ -functions: Here, we first review the fundamentals of Kubota-Leopoldt $p$ -adic $L$ -functions. For a prime number $p$ , let $\mathbb{Z}_{p}$ , $\mathbb{Q}_{p}$ , $\overline{\mathbb{Q}}_{p}$ , $\mathbb{C}_{p}$ , ${\mathcal{O}}_{\mathbb{C}_{p}}$ and ${\mathfrak{M}}_{\mathbb{C}_{p}}$ be respectively the set of $p$ -adic integers, $p$ -adic numbers, the algebraic closure of $\mathbb{Q}_{p}$ , the $p$ -adic completion of $\overline{\mathbb{Q}}_{p}$ , the ring of integers of $\mathbb{C}_{p}$ , and the maximal ideal of ${\mathcal{O}}_{\mathbb{C}_{p}}$ . Fixing embeddings $\overline{\mathbb{Q}}\hookrightarrow\mathbb{C}$ , $\overline{\mathbb{Q}}\hookrightarrow\mathbb{C}_{p}$ , we identify $\overline{\mathbb{Q}}$ simultaneously with a subset of $\mathbb{C}$ and $\mathbb{C}_{p}$ . [...]
  § 2.1. Evaluation of $p$ -adic multiple $L$ -functions at non-positive integers: Based on the consideration in the previous section, we determine the values of $p$ -adic multiple $L$ -functions at non-positive integers as follows: Theorem 2.1 . For $n_{1},\ldots,n_{r}\in\mathbb{N}_{0}$ , $\gamma_{1},\ldots,\gamma_{r}\in\mathbb{Z}_{p}$ , and $c\in\mathbb{N}_{>1}$ with $(c,p)=1$ , $\displaystyle L_{p,r}(-n_{1},\ldots,-n_{r};\omega^{n_{1}},\ldots,\omega^{n_{r}};\gamma_{1},\ldots,\gamma_{r};c)$ $\displaystyle=\sum_{\xi_{1}^{c}=1\atop\xi_{1}\not=1}\cdots\sum_{\xi_{r}^{c}=1\atop\xi_{r}\not=1}{\mathfrak{B}}((n_{j});(\xi_{j});(\gamma_{j}))$ $\displaystyle+\sum_{d=1}^{r}\left(-\frac{1}{p}\right)^{d}\sum_{1\leqslant i_{1} (2.1) where the empty product is interpreted as $1$ . In Definition 1.4 , the twisted multiple Bernoulli number ${\mathfrak{B}}((n_{j});(\xi_{j});(\gamma_{j}))$ was defined for $\gamma_{1},\ldots,\gamma_{r}\in\mathbb{C}$ and roots of unity $\xi_{1},\ldots,\xi_{r}\in\mathbb{C}$ . [...]
[8] QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis | https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation
  Systematic Ostrowski-completion-theoretic audit of the Harmonic Paradigm V1.0-V4.0. Five findings: (1) Beta-function mechanism is infinity-place-specific -- Missarov (1989) confirms different universality class. (2) Q_p not ordered -- eliminates S-matrix, Noether, measurement. (3) pi IS adelic -- pi_p = (p-1)/p at each prime p. (4) alpha = r_e/lambda_C is a length ratio with rational core 137/60 h
  Full text (https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation), excerpts of its own sections:
  § 1.1 The Harmonic Paradigm: The Harmonic Paradigm (HP) V1.0--V4.0 (2026, DOIs https://papers.qnfo.org/papers--21505993) proposed that the quantum harmonic oscillator functions as the universal IR attractor of quantum theory [@qnfo-harmonic-v1; @qnfo-harmonic-v4]. The framework spanned an 8-rung ladder: 1. Transmon anharmonicity (artificial atoms) 2. Phonon equal spacing (lattice vibrations) 3. Molecular vibrations (IR spectroscopy) 4. QED β-function (fine-structure constant, Landau pole) 5. QCD β-function (asymptotic freedom) 6. GUT scale (gauge coupling unification) 7. p-Adic oscillator (Bruhat--Tits tree) 8. Quantum gravity (ultrametric closure, Wheeler--DeWitt) The HP closed out formally in V4.0 [@qnfo-harmonic-v4], retracting its central logistic β-function ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$ after direct calculation showed it incompatible with the textbook QED β-function $\beta(\alpha) = (2/3\pi)\alpha^2$. The logistic ansatz is linear at leading order; real QED is quadratic.
  § 1.2 The Unresolved Non-Archimedean Question: HP V1.0's bibliography cited Vladimirov-Volovich-Zelenov *p-Adic Analysis and Mathematical Physics* (1994) [@VVZ1994] and Ostrowski's theorem (1918) [@Ostrowski1918]. The researcher motivation (Note 3) referenced "Ostrowski's theorem, ultrametric structures, non-Archimedean thinking." Rungs 7--8 explicitly invoke p-adic oscillators, Bruhat--Tits trees, and ultrametric quantum gravity. Yet the HP's core physical mechanism -- the $\beta$-function analysis, the equal-$\ln(\mu)$-spacing order-statistics test, the power-law vs.\ logarithmic IR approach -- was tested **exclusively over $\mathbb{R}$** (the Archimedean/$\infty$-place). This paper asks: *Do any of the HP's mechanisms survive when tested at non-Archimedean completions, or was the HP an Archimedean-only theory with a non-Archimedean bibliography?*
  § 1.3 Ostrowski's Theorem as the Framework: Ostrowski's theorem (1918) [@Ostrowski1918] classifies all non-trivial absolute values on $\mathbb{Q}$: - The Archimedean absolute value $|\cdot|_\infty$ (the usual real absolute value) - The p-adic absolute values $|\cdot|_p$ for each prime $p$ The adele ring $\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod'_p \mathbb{Q}_p$ is the restricted product of all completions. Every rational number $q \in \mathbb{Q}$ embeds diagonally: $q \mapsto (q, q, q, \ldots)$. The product formula: $$ \prod_v |q|_v = 1, \quad \forall q \in \mathbb{Q}^\times $$ is the arithmetic identity connecting all places [@Cassels1986]. If the HP's physical quantities are defined over $\mathbb{Q}$ (or are ratios of such quantities), they have well-defined completions at EVERY place. The question is not "do p-adic completions exist?" but "what are their values?" ___
  § 11.1 Core Conclusion: The Harmonic Paradigm was an **Archimedean-only theory** that invoked non-Archimedean structures (Vladimirov, Bruhat--Tits, Ostrowski) bibliographically without computing p-adic values. Its core mechanism (the $\beta$-function IR attractor) is inherently $\infty$-place-specific. However, the related quantities $\pi$, $\alpha$, $m$, $\lambda_C$, and $r_e$ ARE adelic -- they exist at every Ostrowski completion -- and the HP simply never computed their p-adic values. The Helical Compton Vortex provides a unified framework in which $\pi$, $\alpha$, and $m$ are projections of a single adelic topological excitation: the electron as a helical standing wave whose pitch-to-radius ratio is $\alpha$, whose torsion frequency is $m$, and whose transverse projection at each place produces $\pi_v$.
[9] QNFO: Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$ | https://papers.qnfo.org/papers/is-there-a-p-adic-pi-haar-measure-circle-constants-over-mathbb-q-p-and-an-adelic
  The real constant $\pi\approx3.14159$ is defined as the ratio of a Euclidean circle’s circumference to its diameter and appears in every quantitative model of continuous space. An active adelic‑physics program postulates a place‑wise analogue $\pi_p=(p-1)/p$ for each prime $p$, but no geometric computation has verified whether $p$‑adic circle geometry supports such a value, and the archimedean $\p
  Full text (https://papers.qnfo.org/papers/is-there-a-p-adic-pi-haar-measure-circle-constants-over-mathbb-q-p-and-an-adelic), excerpts of its own sections:
  § 1. Introduction: Designers of precision metrology, quantum‑field theorists, and number‑theoretic physicists all rely on the constant $\pi$ as the ratio $C/D$ of a Euclidean circle’s circumference $C$ to its diameter $D$. [...]
  § 5. Results: 1. **Ball and sphere measures.**  For $r=p^{m}$, $\mu(B_{r})=r^{2}$ and $C_{p}(r)=r^{2}(1-p^{-2})$ (Steps 1–2). 2. **Circle constants.**  $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=(1-p^{-2})/2$, independent of $r$ (Step 4).  Exact and decimal values are listed above. 3. **Finite product.**  $P_{13}=15482880/25050025\approx0.618078$ (Step 5). 4. **Infinite product.**  $\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$ (Step 6). 5. **All‑place combination.**  $\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$ (Step 7). 6. **Corpus comparison.**  $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$ and $\kappa_{p}/((p-1)/p)=1+1/p$ for every prime (Step 8). Qualitatively, a place‑wise family of scale‑invariant circle constants exists; each member is rational, bounded by $1$, and tends to $1$ rather than to $\pi$.  The Euler product over all finite places reproduces $6/\pi^{2}$, and the all‑place product with the archimedean factor yields $6/\pi$, confirming that $\pi$ survives only as a global invariant of the finite places, not as any single $\pi_{p}$.
  § 7. Discussion: **Implications for the adelic‑$\pi$ conjecture.**  In the Haar‑measure formulation the strong conjecture—existence of a place‑wise family $\{\pi_{p}\}$ interpolating toward $\pi$—fails: the computed constants $\kappa_{p}$ are rational, depend on $p$, and satisfy $\lim_{p\to\infty}\kappa_{p}=1\neq\pi$.  The weak form survives because $\pi$ reappears as the global invariant $\prod_{p}\kappa_{p}=6/\pi^{2}$. **Limitations.** 1. *Definition of circumference.*  We defined $C_{p}(r)$ as Haar measure of $S_{r}$.  Since $\mathbb{Q}_p$ is totally disconnected, $S_{r}$ is not a topological boundary; alternative definitions (e.g. $p$‑adic line integrals) could yield different constants. 2. *Diameter convention.*  Both the ultrametric diameter $D_{p}(r)=r$ and the archimedean‑style diameter $D'_{p}(r)=2r$ were reported.  Different conventions would alter $\kappa'_{p}$ but not $\kappa_{p}$. 3. *Normalization.*  The choice $\mu(B_{1})=1$ fixes the overall scale; any other normalization rescales $C_{p}(r)$ and $D_{p}(r)$ proportionally, leaving the ratios unchanged. 4. [...]
  § Conclusion: We have computed, with fully displayed arithmetic, the Haar‑measure geometry of $p$‑adic circles in $\mathbb{Q}_p^2$: the sphere of radius $r$ has measure $r^2(1-p^{-2})$, the ultrametric diameter equals $r$, and the resulting scale‑invariant circle constants are $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$. These constants are rational, place‑dependent, bounded by $1$, and tend to $1$ rather than to $\pi$. The Euler product over all finite places equals $6/\pi^2\approx0.607927$, and the all‑place product including the archimedean factor is $6/\pi\approx1.909859\neq1$. Hence the adelic‑$\pi$ conjecture, in its strong Haar‑measure formulation, fails place‑wise while surviving globally: $\pi$ appears only as a product invariant of the finite places, not as any single $\pi_p$. Thus, the Haar‑measure analysis provides a definitive answer to the question of a $p$‑adic circle constant within the chosen geometric framework, and delineates the precise way in which adelic consistency is achieved without invoking a place‑wise $\pi_p$ equal to $(p-1)/p$.
[10] QNFO: Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science | https://papers.qnfo.org/papers/measure-theoretic-artifacts-archimedean-place
  Ostrowski theorem partitions all non-trivial completions of Q into exactly one Archimedean completion and infinitely many non-Archimedean completions. Physics operates exclusively at the Archimedean place. Catalogues measure-theoretic artifacts across 5 categories with 16 completion failures documented. Proposes adelic restructuring of QM, cosmology, and physical law with 8-claim falsifiability ma
  Full text (https://papers.qnfo.org/papers/measure-theoretic-artifacts-archimedean-place), excerpts of its own sections:
  § Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science: **Author:** QNFO — QWAV / QNFO **Date:** 2026-07-26 **Version:** 1.0 **License:** QNFO Unified License Agreement (QNFO-ULA): https://legal.qnfo.org/ **DOI:** https://papers.qnfo.org/papers **Cross-References:** - Consilience Between Physics and Number Theory (https://papers.qnfo.org/papers) - The Adelic Physics Program: A Grand Synthesis (P7) - Fine-Structure Constant as a Cross-Ratio (https://papers.qnfo.org/papers/fine-structure-constant-cross-ratio/) - Completion Failures Under Ostrowski's Theorem (Catalog v2.0) - QNFO Consilient Synthesis 2026-07-24 - Adelic Synthesis: Pattern-Particle Correspondence - Bridge Theorem: Conditional State Distances in PW Clocks - Quantum Laws of Form (https://papers.qnfo.org/papers) - Adelic QEC: Intrinsic Qubit Protection from Ostrowski's Theorem (P5) - Number-Theoretic Ultrametric Foundations ---
  § 1.1 The Theorem That Divides the World: Ostrowski's theorem (1916) classifies all non-trivial absolute values on ℚ up to equivalence: - **The Archimedean absolute value:** |x|∞ = max(x, −x), the usual absolute value, producing ℝ via Cauchy completion - **The p-adic absolute values:** |x|ₚ = p^(−vₚ(x)) for each prime p, where vₚ(x) is the highest power of p dividing x, producing ℚₚ via completion These completions are **mutually singular**: for any p, no sequence converges simultaneously in ℝ and ℚₚ, nor in ℚₚ and ℚ_q for p ≠ q.
  § 1.2 Physics at One Place Only: The entire apparatus of contemporary physics — Hilbert spaces over ℂ, continuous manifolds, differential equations, gauge connections, path integrals — is constructed at the Archimedean place. No physical theory incorporates any p-adic completion of ℚ. This is an inheritance, not a necessity. The rational numbers ℚ — from which all physical quantities ultimately derive — admit infinitely many completions. To operate at only one is to truncate the adelic whole.
  § 1.3 The Adelic Whole and the Product Formula: The adele ring 𝔸_ℚ is the restricted direct product of all completions: $$\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod_{p}' \mathbb{Q}_p$$ where the restricted product means for all but finitely many primes p, the component lies in ℤₚ. The diagonal embedding ℚ ↪ 𝔸_ℚ satisfies the **product formula**: $$\prod_{v} |q|_v = 1, \quad \forall q \in \mathbb{Q}^{\times}$$ where v runs over all places {∞, 2, 3, 5, …}. [...]
  § 9. Conclusions: We have catalogued five categories of measure-theoretic artifacts arising from physics' exclusive operation at the Archimedean (∞) completion of ℚ: transcendental constants, the continuum, physical constants, entire physical concepts, and epistemological biases. The Completion Failures Catalog documents 16 specific failures, with 2 resolved and 8 under active investigation. The adelic restructuring transforms quantum mechanics (wavefunction → adelic state, Born rule → adelic probability, measurement → completion problem, QEC → passive number-theoretic protection), cosmology (spacetime → Bruhat-Tits tree, time → clock navigation, CMB → log-periodic oscillations, Λ → p-adic zero-point), and the structure of physical law (Lagrangian → adelic action, RG → p-adic flow, gauge theory → building theory, anyons → adelic patterns). **The program is falsifiable.** The 8-claim matrix provides binary yes/no tests with specific timelines. If C3, C4, C5, and C7 all confirm, adelic physics is established. If any fail, the program is constrained or refuted. [...]
[11] QNFO: Adelic Constraints on Quantum Field Theory: Phase 1 | https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-1
  <p>This project set out to answer a question that had lingered at the edges of theoretical physics for nearly four decades: does the adelic completion of the rational numbers constrain the values of fundamental physical constants? The question traces back to a theorem discovered by Alexander Ostrowski in 1916. He proved that the only non-trivial ways to complete the rational numbers $\mathbb{Q}$&m
  Full text (https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-1), excerpts of its own sections:
  § Phase 1: **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062) **DOI:** https://papers.qnfo.org/papers **Date:** 2026-05-09 **Version:** 4.1
  § Prologue: The Question: This project set out to answer a question that had lingered at the edges of theoretical physics for nearly four decades: **does the adelic completion of the rational numbers constrain the values of fundamental physical constants?** The question traces back to a theorem discovered by Alexander Ostrowski in 1916. He proved that the only non-trivial ways to complete the rational numbers $\mathbb{Q}$—that is, to fill in the gaps so that every Cauchy sequence converges—are the familiar real numbers $\mathbb{R}$ (with the ordinary absolute value) and, for each prime number $p$, the $p$-adic numbers $\mathbb{Q}_p$ (with the $p$-adic absolute value). [...]
  § Chapter 7: D2—The Honest Negative Result: Before pursuing the physical implications, we paused to test a numerological hypothesis that had emerged during earlier work: the idea that ratios of adjacent zeta zero gaps might match known particle mass ratios. We ran the analysis properly. Five hundred zeta zeros. Bonferroni correction for multiple comparisons. A permutation null model to estimate the false positive rate. **Result: statistically falsified.** All three candidate “matches” (W/Z mass ratio at 0.1%, top/Higgs at 0.0%) were consistent with chance after correction. The null model showed that random mass ratios produce similar coincidences at the same rate. This was an honest negative result. It demonstrated something important: mathematical beauty does not imply physical truth. The zeta function is deeply connected to physics—through random matrix theory, quantum chaos, and now through the adelic beta constraint—but that connection does not extend to particle mass ratios. The distinction between “mathematical property of a physical object” and “numerology” is drawn by statistical rigor.
  § Appendix B: Master Table of Numerical Results: | #   | Quantity                                   |                Symbol                |            Value            | Source             | | :-- | :----------------------------------------- | :----------------------------------: | :-------------------------: | :----------------- | | 1   | Adelic product formula error               |                  —                   |        $< 10^{-12}$         | M1/M4              | | 2   | Adelic beta constraint error               | $\max\|\beta_\infty + \sum\beta_p\|$ |        $< 10^{-13}$         | D1                 | | 3   | Veneziano beta at symmetric point          |         $\beta_\infty(0.5)$          |         $-5.372183$         | D1/D3              | | 4   | QED one-loop coefficient                   |          $\beta_0 = 2/\pi$           |         $0.636620$          | Standard           | | 5   | Compactification ratio (symmetric)         |               $R(0.5)$               |         $8.438606$          | D3/M13             | | 6   | Compactification ratio (electron)          |           $R(\alpha(m_e))$           | [...]
  § Reproduce key results: python 2.9.py    # D1: Adelic beta constraint (beta_inf + Sigma beta_p = 0) python 3.0.py    # D3: Physical scale comparison (R = 8.44) python 3.4.py    # D6: Adelic RG trajectory (S = 3,240) python 3.5.py    # R9: Full adelic beta synthesis python 3.7.py    # M13: Compactification geometry