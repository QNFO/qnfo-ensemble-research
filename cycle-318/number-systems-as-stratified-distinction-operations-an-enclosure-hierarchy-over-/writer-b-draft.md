# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark

## Abstract

The conventional tower of number systems—$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$—augmented by the $p$-adic fields $\mathbb{Q}_{p}$ and the adele ring $\mathbb{A}$ is usually presented as a sequence of completions without a unifying generative principle. This paper supplies a quantitative layer to the conjecture that each system arises from a single primitive *distinction* operation applied to a Laws-of-Form-style mark. We define a family of enclosure operators $E_{i}$, each of which closes the previous stratum under a specific act of distinction, and an information-loss functional $\Lambda_{i\to j}=\log_{2}N_{i}-\log_{2}N_{j}$, where $N_{i}$ counts distinguishable states in stratum $S_{i}$. For the tree-to-continuum (Monna) projection we compute $\Lambda_{6\to4}=7$ bits at depth $n=10$, base $p=2$ and real precision $\varepsilon=2^{-3}$; we prove the exact linear law $\Lambda_{6\to4}(n)=n-3$ at fixed $\varepsilon$ and identify the loss-free matching depth $n=3$. Finite simultaneous-valuation products over the primes $\{2,3,5\}$ yield $30$ states at depth 1 and $900$ at depth 2. For $p=3$ at the same precision no integer depth yields zero loss, since the required depth $3/\log_{2}3\approx1.893$ is not an integer. All numbers are derived by hand; no simulation or external measurement is used. The result converts a philosophical thesis into a family of falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: $\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$, with $\mathbb{Q}_{p}$ and $\mathbb{A}$ attached to $\mathbb{Q}$ as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model lacks a principled way to decide whether the continuum is forced or merely conventional; a logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order; a computer scientist working with finite-precision arithmetic has no theory of what information is destroyed when a tree-structured limit is flattened onto a line. If the progression $\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}$ could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The measurement-stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure—marking, ratio comparison, convergent sequences, lossy projection to the continuum, imaginary enclosure, $p$-adic enclosure [10]. The computable-real-boundary work builds number systems from two primitives of Spencer-Brown's *Laws of Form*: the mark, whose repeated indication collapses under the Calling rule, and the enclosure, the boundary a distinction creates [11]. Neither supplies a quantitative layer; this paper adds one.

We posit a primitive mark $M$ and a family of enclosure operators $E_{i}$, each a closure-type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable-state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree-to-continuum cross-stratum comparison—the projection analogous to the lossy-projection enclosure of [10]. Every number reported in Section 5 is derived by hand in Section 4; no simulation, measurement, or external data is used.

**Contributions.**
1. Explicit state-count derivations for the tally, real-enclosure, and $p$-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).
2. The corrected Monna cross-stratum loss budget: $\Lambda_{6\to4}=7$ bits at $(p=2,n=10,\varepsilon=2^{-3})$, the exact linearity $\Lambda_{6\to4}(n)=n-3$ at fixed precision, the vanishing of the loss at matched depth $n=3$, and the explicit reclassification of this quantity as a cross-stratum rather than adjacent-stratum loss (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous-valuation product counts of $30$ and $900$ over the primes $\{2,3,5\}$ at depths 1 and 2 (Section 4, Derivation 6).
4. The non-dyadic no-matching result: for $p=3$ and $\varepsilon=2^{-3}$, no integer depth yields zero loss, because the required depth $n=3/\log_{2}3\approx1.893$ is not an integer (Section 4, Derivation 8).
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of $\Lambda$, stated so that a single counterexample kills the corresponding claim (Section 3.4, analyzed in Sections 6 and 7).

## 2. Background and Related Work

We review the related work, citing each source for the specific result its text states.

The primitive vocabulary of the computable-real-boundary work derives $\mathbb{N}$ from iterated marking under the Calling rule $\texttt{\#}\texttt{\#}=\texttt{\#}$, positional notation from nested enclosures, and $\mathbb{Q}$ from enclosures of ratio groups; it identifies the fixed point of finite enclosure operations with the computable reals $\mathbb{R}_{\text{comp}}$ [11]. Our stratum 3 adopts this identification, and stratum 4 (the lossy continuum) is the structure that lies beyond the computable fixed point.

The measurement-stratigraphy work states the stratigraphy thesis—that the history of number systems is a history of expanding distinction operations, each yielding a richer system while embedding a new hidden assumption—and organizes cross-domain analogues of completion, lossy projection, and invariance across physics, computer science, and information theory [10]. Our operator list $E_{1},\dots,E_{7}$ is a formalization of that thesis, and our loss functional $\Lambda$ attaches a number to the "lossy projection" row of its cross-domain table.

The adelic-physics work states Ostrowski's theorem: every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard Archimedean absolute value (completion $\mathbb{R}$) or to a $p$-adic absolute value for some prime $p$ (completion $\mathbb{Q}_{p}$), and argues from it that $\mathbb{R}$ is a choice of completion rather than a necessity [9]. This theorem underwrites our falsifier F3 and justifies the operator list of Section 3.2; it also supplies the physical motivation for taking the $p$-adic and adele strata seriously rather than as curiosities.

The prior version of this work introduced the enclosure hierarchy, the loss functional, and the Monna cross-stratum computation, and recorded in its own discussion that state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth and that $\Lambda$ counts states but not structure [8]. The present paper is a revision of that work: it keeps the verified derivations, reclassifies the Monna loss explicitly as cross-stratum, corrects two misattributions of cited results (noted in Section 6), and sharpens the falsifiability conditions.

Two congruence papers exhibit deep, still-active structure in the $p$-adic stratum. The first poses conjectures, found by calculation, on sums of binomial coefficients and Apéry-like numbers modulo $p^{2}$, with the residues splitting according to the representation of $p$ by quadratic forms such as $p=x^{2}+4y^{2}$ [3]. The second extends this program to congruences modulo $p^{3}$, with residues involving the representation $4p=x^{2}+27y^{2}$ when $3\mid p-1$ [6]. These results show that the internal arithmetic of the divisibility enclosure $E_{6}$ is a live research frontier whose phenomena lie far beyond the simple field structure our operator list generates.

The super-powers paper proves, for sequences $s_{n}=\sum_{i=1}^{k}\prod_{j=0}^{\ell}x_{i,j}^{n^{j}}$, that the following are equivalent: the existence of a real $\theta>1$ and infinitely many $n$ for which the number $\omega(s_{n})$ of distinct prime factors of $s_{n}$ exceeds the super-logarithm $\mathrm{slog}_{\theta}(n)$, together with two companion conditions; the analysis is conducted through $p$-adic valuations $v_{p}$ [7]. This demonstrates how the valuation structure attached to $E_{6}$ can serve as an analytic instrument for counting prime factors, a counting problem our state-count formalism must accommodate.

The noncanonical-number-systems paper studies positional systems $\left(\mathbb{Z},b,\mathcal{D}\right)$ with digit sets that do not contain 0, and proves that such digit sets exist and gives infinitely many examples for every base with $|b|\ge4$; its examples include the valid digit set $\{1,2\}$ for base $-2$ [5]. This supplies the non-canonicality failure mode of Section 6: a single enclosure operator admits many inequivalent concrete realizations, so the operator, not the digit set, determines the stratum.

The stratified-$\beta$-numbers paper introduces a modified version of P. Jones's $\beta$-numbers for Carnot groups and proves that an analogue of Jones's traveling salesman theorem on 1-rectifiability holds in any Carnot group when the earlier $\beta$-numbers are replaced by stratified ones [2]. Its Section 3 shows that the non-stratified $\beta$'s cannot provide sharp two-sided inequalities for certain Carnot groups. This is our model for F4: a scalar measure (there, the classical $\beta$; here, $\Lambda$) can be inadequate for the structure it is meant to grade, and the fix is a stratified refinement.

The Tate-conjectures paper proves Tate's two conjectures for algebraic cycles on certain products of elliptic curves and abelian surfaces over number fields, working with $\ell$-adic cycle class maps and compatible systems of semisimple $\ell$-adic representations, and using potential automorphy as a hypothesis in its chain of implications [1]. It shows how much of modern arithmetic is phrased in $\ell$-adic, i.e. $p$-adic-type, language—evidence that the $E_{6}$ stratum and its Galois-theoretic extensions carry structure our seven-operator list does not yet generate.

The additive-number-theory survey of the Caccetta-Hággkvist conjecture records Kemperman's theorem, which gives an upper bound for the growth of product sets $A\cdot B$ in a group via the quantity $k(A,B)=|A|+|B|-|A+B|$ [4]. Product-set growth is the combinatorial shadow of our state counts: iterating an enclosure on a finite set is exactly an iterated product set, so Kemperman-type bounds are the natural tool for proving state-count formulas beyond the small strata verified here.

Collectively these works provide concrete instances of the operators, the state-count phenomena, and the deep arithmetic that the stratified-distinction framework must accommodate.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark $M$ satisfying the idempotent law

$$MM = M,$$

the *Calling* rule of the Laws of Form calculus [11]. A *distinction operation* $D$ partitions a structure into distinguishable classes. An *enclosure operator* $E$ is a closure-type operator on structures satisfying

$$S\subseteq E(S),\qquad E(E(S))=E(S),\qquad S\subseteq T\;\Rightarrow\;E(S)\subseteq E(T).$$

Each stratum is defined as

$$S_{i}=E_{i}(S_{i-1}),\qquad i=1,\dots,7,$$

with the operators indexed by their target stratum.

### 3.2 The strata

| Stratum | Operator $E_{i}$ | Minimal algebraic structure | Distinguishable-state count $N_{i}$ (parameterised) |
|---|---|---|---|
| 0 (the mark) | — | $\{M\}$ | $N_{0}=1$ |
| 1 (tally, $\mathbb{N}$) | tally enclosure | free monoid on one generator $\to\mathbb{N}$ with addition | $N_{1}(n)=n+1$ (depth $n$) |
| 2 (ratio, $\mathbb{Q}$) | ratio-compare | field of fractions of $\mathbb{Z}$ $\to\mathbb{Q}$ | $N_{2}$ infinite (no finite truncation) |
| 3 (convergent sequences, $\mathbb{R}_{\text{comp}}$) | Cauchy-sequence enclosure | computable reals $\mathbb{R}_{\text{comp}}$ | $N_{3}$ infinite |
| 4 (lossy tree projection, $\mathbb{R}$) | Monna-type projection $\pi_{M}$ | continuum $\mathbb{R}$ | $N_{4}(\varepsilon)=1/\varepsilon$ (real precision $\varepsilon$) |
| 5 (phase enclosure, $\mathbb{C}$) | phase enclosure | $\mathbb{C}\cong\mathbb{R}\times S^{1}$ | $N_{5}$ infinite |
| 6 (divisibility enclosure, $\mathbb{Q}_{p}$) | $p$-adic completion | $\mathbb{Q}_{p}$ | $N_{6}(n)=p^{n}$ (depth $n$) |
| 7 (simultaneous valuations, $\mathbb{A}$) | adele enclosure | $\mathbb{A}= \mathbb{R}\times\!\!\prod_{p}'\mathbb{Q}_{p}$ | $N_{7}$ infinite (restricted product) |

The recovery claims—that $E_{4}$ yields $\mathbb{R}$, $E_{5}$ yields $\mathbb{C}$, and $E_{7}$ yields $\mathbb{A}$—are conjectural, consistent with the stratigraphy framework's own status for these strata [10]. Only the state-count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below; the formula $N_{4}(\varepsilon)=1/\varepsilon$ is a definition of the target precision, not a verified recovery claim.

### 3.3 Morphisms and the loss functionals

Between adjacent strata $S_{i}\to S_{i+1}$ we take the canonical map induced by the operator. The *adjacent-stratum information-loss functional* is

$$\Lambda_{i\to i+1}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{i+1}(\text{params}),$$

the base-2 logarithm of the ratio of distinguishable-state counts.

**Cross-stratum loss functional.** For any ordered pair of strata $i,j$ with finite counts we define

$$\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),$$

which reduces to the adjacent-stratum functional when $j=i+1$. The Monna projection $\pi_{M}$ maps a depth-$n$, base-$p$ tree (state count $N_{6}(n)=p^{n}$) onto a line at precision $\varepsilon$ (state count $N_{4}(\varepsilon)=1/\varepsilon$); source and target are strata 6 and 4, which are not adjacent. Consequently the Monna loss is a cross-stratum quantity

$$\Lambda_{\text{Monna}}(n,p,\varepsilon)=\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr).$$

### 3.4 Falsifiability conditions

Following the discipline of [11], each recovery claim carries a stated falsifier.

* **F1 (stratification).** Exhibit a number system in the historical sequence that no closure operator over the mark can generate.
* **F2 (loss functional).** Exhibit a projection whose state-count loss decreases as the source is refined at fixed target precision.
* **F3 (operator list).** Exhibit a completion of $\mathbb{Q}$ outside the list $\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}$.
* **F4 ($\Lambda$ adequacy).** Exhibit two intuitively different projections with identical $\Lambda$ but markedly different information content.

## 4. Analysis

All inputs are either definitions of Section 3 or explicitly stated here; every arithmetic step is shown.

**Input 1.** Tally depth $n=9$. (Chosen parameter.)
**Input 2.** Prime $p=2$, tree depth $n=10$. (Chosen parameter.)
**Input 3.** Real precision $\varepsilon=2^{-3}$ (unit interval partitioned into cells of width $2^{-3}$). (Chosen parameter.)
**Input 4.** Primes $\{2,3,5\}$ for the finite adele-type product. (Chosen parameter.)

### Derivation 1 (tally states)

With $n=9$ marks the distinguishable counts are $\{0,1,\dots,9\}$, so

$$N_{1}(9)=9+1=10.$$

### Derivation 2 (real-enclosure states)

The unit interval $[0,1]$ partitioned into cells of width $\varepsilon=2^{-3}$ contains

$$N_{4}(\varepsilon)=\frac{1}{\varepsilon}= \frac{1}{2^{-3}} = 2^{3}=8$$

distinguishable cells.

### Derivation 3 ($p$-adic tree states)

The residue ring $\mathbb{Z}/p^{n}\mathbb{Z}$ with $p=2$, $n=10$ has exactly

$$N_{6}(10)=2^{10}=1024$$

elements. Equivalently, the rooted binary tree of depth 10 has $2^{10}=1024$ leaves, one per residue class modulo $2^{10}$.

### Derivation 4 (Monna cross-stratum loss)

The Monna projection $\pi_{M}$ maps the depth-10 binary tree onto the real line at precision $\varepsilon=2^{-3}$. As a cross-stratum comparison $\Lambda_{6\to4}$ we obtain

$$\Lambda_{6\to4}= \log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon) = \log_{2}(1024)-\log_{2}(8)=10-3=7.$$

Checking via the ratio form

$$\Lambda_{6\to4}= \log_{2}\!\left(\frac{1024}{8}\right)=\log_{2}(128)=7,$$

and $2^{7}=128$ confirms the ratio.

### Derivation 5 (linearity and vanishing)

Fix $\varepsilon=2^{-3}$ and vary depth $n$. Since $N_{6}(n)=2^{n}$ and $N_{4}(\varepsilon)=2^{3}$,

$$\Lambda_{6\to4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3,$$

which is strictly increasing in $n$. At $n=3$ the loss is

$$\Lambda_{6\to4}(3)=3-3=0,$$

so a depth-3 binary tree and a precision-$2^{-3}$ real enclosure have identical state counts ($2^{3}=8$) and the projection is loss-free.

### Derivation 6 (finite adele-type product)

With primes $\{2,3,5\}$ at depth $n_{p}=1$ each,

$$N_{\mathbb{A},\text{fin}}=\prod_{p\in\{2,3,5\}}p = 2\times3\times5 = 30.$$

At depth $n_{p}=2$ each,

$$N_{\mathbb{A},\text{fin}}=2^{2}\times3^{2}\times5^{2}=4\times9\times25=900.$$

### Derivation 7 (stratum count)

The operator list of Section 3.2 contains seven operators $E_{1},\dots,E_{7}$ acting on $S_{0}$, producing $S_{1},\dots,S_{7}$; total strata including the mark:

$$7+1=8.$$

### Derivation 8 (non-dyadic loss)

For $p=3$ and $\varepsilon=2^{-3}$,

$$\Lambda_{6\to4}(n)=\log_{2}(3^{n})-3 = n\log_{2}3-3.$$

Setting $\Lambda_{6\to4}=0$ gives $n=3/\log_{2}3$. Since $\log_{2}3\approx1.58496$,

$$n=\frac{3}{1.58496}\approx1.893,$$

which is not an integer. Hence no integer depth yields zero loss for $p=3$ at this precision; the loss-free matching of Result R2 is a dyadic accident. In general an integer loss-free depth exists iff $\log_{2}(1/\varepsilon)/\log_{2}p$ is an integer.

### Derivation 9 (adjacent-stratum loss at verified strata)

The only adjacent pair with two finite counts among the verified strata is $S_{0}\to S_{1}$:

$$\Lambda_{0\to1}(n)=\log_{2}N_{0}-\log_{2}N_{1}(n)=\log_{2}(1)-\log_{2}(n+1)=-\log_{2}(n+1).$$

At $n=9$ this equals $-\log_{2}(10)\approx-3.3219$ bits. The negative sign indicates that the tally enclosure creates distinguishable states rather than destroying them, as expected for an expanding operator.

### Derivation 10 (sensitivity of the Monna loss to base and precision)

Fix depth $n=8$ and evaluate $\Lambda_{\text{Monna}}(8,p,\varepsilon)=8\log_{2}p-\log_{2}(1/\varepsilon)$ for three cases.

*For $p=2$, $\varepsilon=2^{-4}$:*

$$\Lambda_{\text{Monna}}(8,2,2^{-4})=8\cdot1-4=4\ \text{bits}.$$

*For $p=5$, $\varepsilon=2^{-4}$:* using $\log_{2}5=\ln 5/\ln 2\approx1.60944/0.69315\approx2.32193$,

$$\Lambda_{\text{Monna}}(8,5,2^{-4})=8\cdot2.32193-4\approx18.57544-4=14.575425\ \text{bits}.$$

*For $p=3$, $\varepsilon=10^{-2}$:* using $\log_{2}3\approx1.58496$ and $\log_{2}100\approx6.64386$,

$$\Lambda_{\text{Monna}}(8,3,10^{-2})=8\cdot1.58496-6.64386\approx12.67968-6.64386=6.0358438\ \text{bits}.$$

For fixed depth, increasing the base $p$ raises the loss in proportion to $\log_{2}p$, while finer real precision (smaller $\varepsilon$) reduces the loss linearly in $\log_{2}(1/\varepsilon)$.

### Derivation 11 (limiting case $\varepsilon\to0$)

If the real precision tends to zero, $1/\varepsilon\to\infty$ and $\log_{2}(1/\varepsilon)\to\infty$. Hence

$$\lim_{\varepsilon\to0}\Lambda_{\text{Monna}}(n,p,\varepsilon)=-\infty,$$

i.e. the loss becomes unboundedly negative: an infinitely precise continuum can represent more distinguishable states than any finite $p$-adic tree, so loss-free matching is impossible when the target has infinite resolution.

## 5. Results

All quantities below are computed in Section 4; no simulation or external measurement is reported.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth $n=9$ | $N_{1}(9)=10$ | Derivation 1 |
| Real cells at $\varepsilon=2^{-3}$ | $N_{4}=8$ | Derivation 2 |
| Binary tree states at depth $n=10$ | $N_{6}(10)=1024$ | Derivation 3 |
| Monna cross-stratum loss at $(p=2,n=10,\varepsilon=2^{-3})$ | $\Lambda_{6\to4}=7$ bits | Derivation 4 |
| Monna cross-stratum loss at depth $n$, $\varepsilon=2^{-3}$ | $\Lambda_{6\to4}(n)=n-3$ | Derivation 5 |
| Loss-free matching depth | $n=3$ ($\Lambda_{6\to4}=0$) | Derivation 5 |
| Finite adele-type product, depth 1, $\{2,3,5\}$ | $30$ | Derivation 6 |
| Finite adele-type product, depth 2 | $900$ | Derivation 6 |
| Total strata (mark + 7 operators) | $8$ | Derivation 7 |
| Non-dyadic matching depth for $p=3$ | none (required $n\approx1.893$) | Derivation 8 |
| Adjacent loss $\Lambda_{0\to1}$ at $n=9$ | $\approx-3.3219$ bits | Derivation 9 |
| Loss at $(p=2,n=8,\varepsilon=2^{-4})$ | $4$ bits | Derivation 10 |
| Loss at $(p=5,n=8,\varepsilon=2^{-4})$ | $\approx14.575425$ bits | Derivation 10 |
| Loss at $(p=3,n=8,\varepsilon=10^{-2})$ | $\approx6.0358438$ bits | Derivation 10 |
| Projected loss for $p=3,n=5,\varepsilon=10^{-2}$ (assumption) | $\approx1.28$ bits | Projection (see text) |

**Result R1.** The Monna cross-stratum loss is exactly linear in tree depth at fixed real precision: $\Lambda_{6\to4}(n)=n-3$ bits for $\varepsilon=2^{-3}$, $p=2$. Deeper trees carry strictly more information than any fixed-precision continuum target.

**Result R2.** There exists a matched-parameter pair $(n=3,\varepsilon=2^{-3})$ at which the $p$-adic tree and the real enclosure have identical state counts ($2^{3}=8$), i.e. zero cross-stratum loss. This matching is dyadic; for $p=3$ no integer depth yields zero loss (Derivation 8).

**Result R3.** The stratum sequence has eight levels including the mark, and the finite simultaneous-valuation product over $\{2,3,5\}$ at depth 1 yields $30$ states, at depth 2 yields $900$ states.

**Projection (labeled, not a result).** Assuming the general law $\Lambda_{i\to j}(n,p,\varepsilon)=n\log_{2}p-\log_{2}(1/\varepsilon)$ holds beyond the verified cases, for $p=3$, $n=5$, $\varepsilon=10^{-2}$ the projected loss is

$$\Lambda\approx\log_{2}(3^{5})-\log_{2}(100)\approx7.925-6.644\approx1.28\text{ bits}.$$

The uncertainty is bounded by the unverified generality of the state-count formulas; this figure is a projection under stated assumptions, not a derived result.

## 6. Discussion

**Limitations.**
* The recovery claims for strata 4, 5, and 7 remain conjectural; state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth. The formula $N_{4}(\varepsilon)=1/\varepsilon$ is a definition of the target, not a verified count of the continuum.
* The loss functional $\Lambda$ counts *states* but not *structure*: two projections can destroy the same number of bits while destroying very different algebraic features (e.g., order versus branching).
* The Monna analysis assumes the tree is exactly a $p$-adic ball in state count; a more general tree-like limit with a different branching profile would alter $\Lambda$.
* The finite adele-type product of Derivation 6 is a toy: the true adele ring is a restricted product including the real factor, and the count of 30 says nothing about its topology.
* $\Lambda$ is defined only for finite state counts; at infinite depth both source and target counts diverge, requiring renormalisation or a rate formulation.
* Two citation corrections relative to the prior version [8] are recorded here. First, the prior version cited a harmonic-number congruence confirming a conjecture of Z-W Sun to a reference whose actual subject is polynomial systems involving Stirling numbers of the second kind; that congruence claim is not supported by any source available to this revision and has been removed, replaced by the binomial-coefficient and Apéry-like congruence programs of [3] and [6], which the available