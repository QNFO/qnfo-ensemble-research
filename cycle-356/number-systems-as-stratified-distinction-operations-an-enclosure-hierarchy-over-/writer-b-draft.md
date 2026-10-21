# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark (Revised Version 3.0)

## Abstract

The conventional tower of number systems—$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$—augmented by the $p$-adic fields $\mathbb{Q}_{p}$ and the adele ring $\mathbb{A}$ is usually presented as a sequence of completions without a unifying generative principle. What is missing is a quantitative layer: a countable, falsifiable account of what each successive act of distinction adds and what it destroys. This paper supplies that layer for the conjecture that each number system arises from a primitive *distinction* operation applied to a Laws-of-Form-style mark. We define a family of enclosure operators $E_{i}$ closing each stratum into the next, and an information-loss functional $\Lambda_{i\to j}=\log_{2}N_{i}-\log_{2}N_{j}$ over distinguishable-state counts $N_{i}$. The tree-to-continuum (Monna) projection is reclassified as a *cross-stratum* quantity $\Lambda_{6\to4}$, not an instance of the adjacent-stratum functional; at depth $n=10$, base $p=2$ and precision $\varepsilon=2^{-3}$ it equals $7$ bits, with the exact law $\Lambda_{6\to4}(n)=n-3$ and loss-free matching at $n=3$. For $p=3$ at the same precision no integer depth yields zero loss, since the required depth $3/\log_{2}3\approx1.893$ is not an integer. Finite simultaneous-valuation products over $\{2,3,5\}$ give $30$ states at depth $1$ and $900$ at depth $2$. All numbers are derived by hand; the result converts a philosophical thesis into falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: $\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$, with $\mathbb{Q}_{p}$ and $\mathbb{A}$ attached to $\mathbb{Q}$ as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model has no principled way to decide whether the continuum is forced or merely conventional; the adelic-physics program argues that the choice of $\mathbb{R}$ as the base field of physics is an unjustified assumption, since every measurement produces a rational number to finite precision and every simulation operates on finite-precision rationals [11]. A logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order. A computer scientist working with finite-precision arithmetic has no theory of what information is destroyed when a tree-structured limit is flattened onto a line. If the progression $\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}$ could be derived from increasingly refined acts of distinction, each of these decisions would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The measurement-stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure—marking, ratio comparison, convergent sequences, lossy projection to the continuum, imaginary enclosure, $p$-adic enclosure [12]. The computable-real-boundary work builds number systems from the two primitives of Spencer-Brown's *Laws of Form*: the mark, whose repeated indication collapses under the Calling rule, and the enclosure, the boundary a distinction creates; it identifies the fixed point of finite enclosure operations with the computable reals $\mathbb{R}_{\text{comp}}$ [13]. Neither work supplies a quantitative layer; this paper adds one, and repairs the errors of its own published predecessor [10].

We posit a primitive mark $M$ and a family of enclosure operators $E_{i}$, each a closure-type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable-state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree-to-continuum cross-stratum comparison. Three corrections to the published version [10] are incorporated and documented in the body: the Monna quantity is reclassified as cross-stratum rather than an instance of the adjacent-stratum loss functional; the falsifier F3 is restated so that it no longer misreads Ostrowski's theorem, which *supports* rather than blocks the operator list; and two misattributed citations are repaired, so that the harmonic-number congruence confirming a conjecture of Z.-W. Sun is now cited to the paper that proves it [3] and the super-powers bound on $\omega(s_{n})$ to the paper that proves it [9]. Every number reported is derived by hand in Section 4; no simulation, measurement, or external data is used.

**Contributions.**
1. Explicit state-count derivations for the tally, real-enclosure, and $p$-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).
2. The corrected Monna cross-stratum loss budget: $\Lambda_{6\to4}=7$ bits at $(p=2,n=10,\varepsilon=2^{-3})$, the exact linearity $\Lambda_{6\to4}(n)=n-3$ at fixed precision, the vanishing of the loss at matched depth $n=3$, and the explicit reclassification of this quantity as cross-stratum rather than adjacent-stratum loss, correcting the presentation error of the published version (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous-valuation product counts of $30$ and $900$ over the primes $\{2,3,5\}$ at depths 1 and 2 (Section 4, Derivation 6).
4. The non-dyadic no-matching result: for $p=3$ and $\varepsilon=2^{-3}$, no integer depth yields zero loss, because the required depth $n=3/\log_{2}3\approx1.893$ is not an integer (Section 4, Derivation 7), together with a labeled projection of $\approx1.28$ bits for $(p=3,n=5,\varepsilon=10^{-2})$ (Section 4, Derivation 8).
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of $\Lambda$, with F3 restated consistently with Ostrowski's theorem as stated in the adelic-physics work [11] (Section 3.4, analyzed in Sections 5–6).

## 2. Background and Related Work

We review the related work, citing each source for the specific result its text states.

* The computable-real-boundary work constructs numbers from the two primitives of distinction: it derives $\mathbb{N}$ from iterated marking under the Calling rule $\texttt{\#}\texttt{\#}=\texttt{\#}$, positional notation from nested enclosures grouped by a base, and $\mathbb{Q}$ from enclosures of ratio groups; its conclusion identifies the fixed point of finite enclosure operations with the computable reals $\mathbb{R}_{\text{comp}}$, and places everything beyond that closure in the category of forms that cannot be reduced to void by any finite sequence of the two primitive laws [13]. Our stratum 3 adopts this identification, and stratum 4 (the lossy continuum) is the structure that lies beyond the computable fixed point.

* The measurement-stratigraphy work states the stratigraphy thesis that the history of number systems is a history of expanding distinction operations, each yielding a richer number system while embedding a new hidden assumption, and maps eras to marking ($\mathbb{N}$), ratio comparison ($\mathbb{Q}$), convergent sequences ($\mathbb{R}_{\text{comp}}$), lossy projection ($\mathbb{R}$), imaginary enclosure ($\mathbb{C}$), and $p$-adic enclosure ($\mathbb{Q}_{p}$) [12]. The present paper adopts the same mapping for the operators $E_{1},\dots,E_{6}$, and attaches quantitative analyses—a loss functional and state-count sensitivity—to each step of that hierarchy. Its cross-domain consilience audit, which maps lossy projection to coarse-graining in physics, lossy compression in computer science, and noisy channels in information theory, is the pattern our $\Lambda$ functional instantiates for number systems specifically.

* The adelic-physics work states Ostrowski's theorem in the form: every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard Archimedean absolute value $|\cdot|_{\infty}$ (whose completion is $\mathbb{R}$) or to a $p$-adic absolute value $|\cdot|_{p}$ for some prime $p$ (whose completion is $\mathbb{Q}_{p}$), and draws the consequence that if $\mathbb{Q}$ is the physical base field, the Archimedean completion and every $p$-adic completion are equally legitimate completions of the physical number system [11]. This theorem underwrites our falsifier F3 and justifies the operator list of Section 3.2: the list of completions $\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}$ is complete *by the theorem*, so the adele stratum, which combines all of them, sits consistently at the top of the hierarchy rather than in conflict with it.

* The prior version of this work introduced the enclosure hierarchy, the loss functional, and the Monna cross-stratum computation, and recorded in its own discussion that state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth and that $\Lambda$ counts states but not structure [10]. The present paper is a revision of that work: it keeps the verified derivations, reclassifies the Monna loss explicitly as cross-stratum, corrects two misattributions of cited results, and sharpens the falsifiability conditions.

* The paper on certain polynomial systems involving Stirling numbers of the second kind solves linear systems with coefficients in multivariate polynomial rings that arise in computing parametric Bernstein–Sato polynomials associated with hypergeometric ideals in the Weyl algebra; its Section 1 shows that the Stirling numbers of the first kind $s(d,k)$, defined by $x(x-1)\cdots(x-d+1)=\sum_{k=0}^{d}s(d,k)x^{k}$, can be characterized as the solution of a triangular linear system in the Stirling numbers of the second kind $S(i,j)$, and its Section 3 defines explicit polynomial systems $C(k_{1},k_{2},\ell)\in\mathbb{Z}[x,y,z]$ built from binomial coefficients and Stirling numbers [1]. This is directly relevant to our program's computational layer: the algebraic structures our enclosure operators generate are finite polynomial objects, and the machinery of [1] is an existing instrument for solving exactly the kind of triangular polynomial system that a closure operator's iterated application produces.

* The harmonic-congruence paper proves, for any prime $p\geq7$, the congruence $\sum_{k=1}^{p-1}H_{k}^{2}/k^{2}\equiv\frac{4}{5}pB_{p-5}\pmod{p^{2}}$ for harmonic numbers $H_{n}=\sum_{k=1}^{n}1/k$, confirming a conjecture of Z.-W. Sun, and proves two similar congruences modulo $p^{2}$ [3]. This is the correct citation for the congruence that the published version of the present paper had attributed elsewhere; it also exhibits the kind of $p$-adic residue structure—Bernoulli numbers appearing modulo $p^{2}$—that lives inside the divisibility enclosure $E_{6}$ and that our simple field-level operator list does not generate.

* Two further congruence papers exhibit deep, still-active structure in the $p$-adic stratum. The first poses conjectures, found by calculation with Maple, on sums of binomial coefficients and Apéry-like numbers modulo $p^{2}$, with the residues splitting according to the representation of $p$ by quadratic forms such as $p=x^{2}+4y^{2}$ and $4p=x^{2}+27y^{2}$ [5]. The second extends this program to congruences modulo $p^{3}$, with residues involving the representation $4p=x^{2}+27y^{2}$ when $3\mid p-1$ [8]. Together these show that the internal arithmetic of the divisibility enclosure $E_{6}$ is a live research frontier whose phenomena lie far beyond the simple field structure our operator list generates.

* The super-powers paper studies sequences $s_{n}=\sum_{i=1}^{k}\prod_{j=0}^{\ell}x_{i,j}^{n^{j}}$ and proves that the following are equivalent: there exist a real $\theta>1$ and infinitely many indices $n$ for which the number $\omega(s_{n})$ of distinct prime factors of $s_{n}$ exceeds a super-logarithmic bound; its proof works with the $p$-adic valuation $\upsilon_{p}(x)$, the exponent of the largest power of $p$ dividing $x$ [9]. This is the correct citation for the valuation-based bound that the published version had attributed elsewhere; it demonstrates how the valuation structure attached to $E_{6}$ serves as an analytic instrument for counting prime factors, a counting problem our state-count formalism must accommodate.

* The noncanonical-number-systems paper studies positional systems $(\mathbb{Z},b,\mathcal{D})$ with digit sets that do not contain $0$, proves that such digit sets exist and gives infinitely many examples for every base with $|b|\geq4$, and shows in its examples section that $\{1,2\}$ is a valid digit set for the base $-2$, with the $n$-fold digit set $\mathcal{D}^{n}$ valid for base $(-2)^{n}$ precisely for odd $n$ [7]. This supplies the non-canonicity failure mode of Section 6: a single enclosure operator can admit many inequivalent concrete realizations, so the operator, not the digit set, determines the stratum.

* The stratified-$\beta$-numbers paper introduces a modified version of P. Jones's $\beta$-numbers $\beta_{E}(x,r)=\inf_{L}\sup_{z\in E\cap B(x,r)}d(z,L)/r$ for Carnot groups and proves that an analogue of Jones's traveling-salesman theorem on 1-rectifiability holds in any Carnot group when the earlier $\beta$'s are replaced by stratified ones; its Section 3 demonstrates that the non-stratified $\beta$'s cannot provide sharp two-sided traveling-salesman inequalities for the Carnot group $\mathbb{R}^{2}\times\mathbb{H}$ [4]. This is our model for falsifier F4: a scalar measure (there, the classical $\beta$; here, $\Lambda$) can be inadequate for the structure it is meant to grade, and the fix is a stratified refinement.

* The expository paper on the Caccetta-Hággkvist conjecture records Kemperman's theorem, which gives an upper bound for the growth of product sets $A\cdot B=\{ab:a\in A,\,b\in B\}$ in a group via the quantity $k(A,B)=|A|+|B|-|A+B|$, and uses it to prove the conjecture for Cayley graphs and vertex-transitive graphs [6]. Product-set growth is the combinatorial shadow of our state counts: iterating an enclosure on a finite set is exactly an iterated product set $B^{k}$, so Kemperman-type bounds are the natural tool for proving state-count formulas beyond the small strata verified here.

* The Tate-conjectures paper proves Tate's two conjectures for algebraic cycles of arbitrary codimension on certain products of elliptic curves and abelian surfaces over number fields, working with $\ell$-adic cycle class maps $\mathrm{Ch}^{r}(X)\otimes\mathbb{Q}_{\ell}\to H^{2r}(X_{\bar{F}},\mathbb{Q}_{\ell}(r))^{\Gamma_{F}}$ and compatible systems of semisimple $\ell$-adic representations, and using potential automorphy as a hypothesis in its chain of implications [2]. It shows how much of modern arithmetic is phrased in $\ell$-adic, i.e. $p$-adic-type, language—evidence that the $E_{6}$ stratum and its Galois-theoretic extensions carry structure our operator list does not yet generate.

Together these works provide concrete instances of the operators, the state-count phenomena, and the deep arithmetic that the stratified-distinction framework must accommodate.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark $M$ satisfying the idempotent law

$$MM = M,$$

the *Calling* rule of the Laws of Form calculus (assumed, following the construction of [13]). A *distinction operation* $D$ partitions a structure into distinguishable classes. An *enclosure operator* $E$ is a closure-type operator on structures satisfying

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

The recovery claims—that $E_{4}$ yields $\mathbb{R}$, $E_{5}$ yields $\mathbb{C}$, and $E_{7}$ yields $\mathbb{A}$—are conjectural, consistent with the stratigraphy framework's own status for these strata [12]. Only the state-count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below, as recorded in the published version's own limitation [10]; the formula $N_{4}(\varepsilon)=1/\varepsilon$ is a definition of the target precision, not a verified recovery claim.

### 3.3 Morphisms and the loss functionals

Between adjacent strata $S_{i}\to S_{i+1}$ we take the canonical map induced by the operator. The *adjacent-stratum information-loss functional* is

$$\Lambda_{i\to i+1}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{i+1}(\text{params}),$$

the base-2 logarithm of the ratio of distinguishable-state counts.

**Cross-stratum loss functional.** For any ordered pair of strata $i,j$ with finite counts we define

$$\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),$$

which reduces to the adjacent-stratum functional when $j=i+1$. The Monna projection $\pi_{M}$ maps a depth-$n$, base-$p$ tree (state count $N_{6}(n)=p^{n}$) onto a line at precision $\varepsilon$ (state count $N_{4}(\varepsilon)=1/\varepsilon$); source and target are strata 6 and 4, which are not adjacent. Consequently the Monna loss is a *cross-stratum* quantity,

$$\Lambda_{\text{Monna}}(n,p,\varepsilon)=\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr).$$

This reclassification corrects the presentation error of the published version [10], which had presented $\Lambda_{\text{Monna}}$ as an instance of the adjacent-stratum functional; it is an instance only of the more general cross-stratum functional, and the two coincide only when source and target strata are adjacent, which $6\to4$ is not.

### 3.4 Falsifiability conditions

Following the discipline of the present framework, each recovery claim carries a stated falsifier.

* **F1 (stratification).** Exhibit a number system in the historical sequence that no closure operator over the mark can generate.
* **F2 (loss functional).** Exhibit a projection whose state-count loss decreases as the source is refined at fixed target precision.
* **F3 (operator list).** Exhibit a completion of $\mathbb{Q}$ outside the list $\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}$. By Ostrowski's theorem as stated in [11], every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the Archimedean one or to a $p$-adic one, so the theorem itself asserts that no such completion exists; F3 is therefore a *consistency check* on the operator list rather than an open possibility, and the adele stratum, which combines all completions the theorem licenses, is the natural top stratum rather than a conjecture in conflict with the classification.
* **F4 ($\Lambda$ adequacy).** Exhibit two intuitively different projections with identical $\Lambda$ but markedly different information content.

## 4. Analysis

All inputs are either definitions of Section 3 or explicitly stated here; every arithmetic step is shown.

**Input 1.** Tally depth $n=9$. (Chosen parameter.)
**Input 2.** Prime $p=2$, tree depth $n=10$. (Chosen parameter.)
**Input 3.** Real precision $\varepsilon=2^{-3}$ (unit interval partitioned into cells of width $2^{-3}$). (Chosen parameter.)
**Input 4.** Primes $\{2,3,5\}$ for the finite adele-type product. (Chosen parameter.)
**Input 5.** Prime $p=3$ for the non-dyadic analysis. (Chosen parameter.)
**Input 6.** For the labeled projection of Derivation 8: $p=3$, $n=5$, $\varepsilon=10^{-2}$. (Chosen parameters, labeled as a projection.)

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

$$\Lambda_{6\to4}= \log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon)
= \log_{2}(1024)-\log_{2}(8)=10-3=7.$$

Checking via the ratio form,

$$\Lambda_{6\to4}= \log_{2}\!\left(\frac{1024}{8}\right)=\log_{2}(128)=7,$$

and $2^{7}=128$ confirms the ratio.

### Derivation 5 (linearity and vanishing)

Fix $\varepsilon=2^{-3}$ and vary depth $n$. Since $N_{6}(n)=2^{n}$ and $N_{4}(\varepsilon)=2^{3}$,

$$\Lambda_{6\to4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3,$$

which is strictly increasing in $n$. At $n=3$ the loss is

$$\Lambda_{6\to4}(3)=3-3=0,$$

so the depth-3 binary tree and the precision-$2^{-3}$ continuum have identical state counts $2^{3}=8$ and the projection is loss-free there.

### Derivation 6 (finite simultaneous-valuation products)

Take the primes $\{2,3,5\}$ (Input 4). At depth $n=1$ the simultaneous-valuation state space is the product of residue rings $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}\times\mathbb{Z}/5\mathbb{Z}$, with count

$$N_{7}^{(1)}=2\cdot3\cdot5=30.$$

At depth $n=2$ it is $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/9\mathbb{Z}\times\mathbb{Z}/25\mathbb{Z}$, with count

$$N_{7}^{(2)}=4\cdot9\cdot25=900.$$

Both products are finite because each factor is finite; the count multiplies because the Chinese remainder theorem makes the simultaneous residue classes independent.

### Derivation 7 (non-dyadic no-matching)

Fix $\varepsilon=2^{-3}$ (Input 3) and take $p=3$ (Input 5). Zero loss requires

$$n\log_{2}3=\log_{2}(1/\varepsilon)=3,$$

so the required depth is

$$n=\frac{3}{\log_{2}3}.$$

We compute $\log_{2}3=\ln 3/\ln 2=1.098612\ldots/0.693147\ldots=1.584963\ldots$, hence

$$n=\frac{3}{1.584963\ldots}=1.892789\ldots\approx1.893.$$

Since $1.892789\ldots$ is not an integer, and $\Lambda_{6\to4}(n)=n\log_{2}3-3$ is strictly increasing in $n$, no integer depth yields zero loss: at $n=1$ the loss is $1.584963\ldots-3=-1.415037\ldots$ bits (the tree is *coarser* than the target), and at $n=2$ it is $3.169925\ldots-3=0.169925\ldots$ bits (the tree is already finer). The loss jumps across zero without vanishing.

### Derivation 8 (labeled projection for a non-dyadic case)

We assume the parameters $p=3$, $n=5$, $\varepsilon=10^{-2}$ (Input 6); this is a projection, not a derived recovery claim. Then

$$\log_{2}(1/\varepsilon)=\log_{2}100=\frac{\ln 100}{\ln 2}=\frac{4.605170\ldots}{0.693147\ldots}=6.643856\ldots,$$

and

$$\Lambda_{6\to4}=5\log_{2}3-\log_{2}100=5\times1.584963\ldots-6.643856\ldots=7.924813\ldots-6.643856\ldots=1.280957\ldots\approx1.28\text{ bits}.$$

This value is reported in Section 5 as a projection under the stated assumptions.

## 5. Results

All quantities below are obtained from the explicit derivations of Section 4; no simulation, measurement, or external data are used.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth $n=9$ | $N_{1}(9)=10$ | Derivation 1 |
| Real-enclosure cells at $\varepsilon=2^{-3}$ | $N_{4}=8$ | Derivation 2 |
| Binary-tree states at depth $n=10$ | $N_{6}(10)=1024$ | Derivation 3 |
| Monna cross-stratum loss for $(p=2,n=10,\vare