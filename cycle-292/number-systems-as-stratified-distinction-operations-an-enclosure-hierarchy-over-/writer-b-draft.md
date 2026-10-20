# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark (Revised Version 2.1.0)

## Abstract

The conventional tower of number systems—$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$, augmented by the $p$-adic fields $\mathbb{Q}_{p}$ and the adele ring $\mathbb{A}$—is usually presented as a sequence of completions without a unifying generative principle. This paper supplies a quantitative layer to the conjecture that each system arises from a single primitive *distinction operation* applied to a Laws-of-Form-style mark. We define a family of enclosure operators $E_{i}$, each of which closes the previous stratum under a specific act of distinction, and an information-loss functional $\Lambda_{i\to j}=\log_{2}N_{i}-\log_{2}N_{j}$ on distinguishable-state counts $N_{i}$. A correction to the published version is central here: the Monna tree-to-continuum loss compares stratum 6 (the $p$-adic tree) directly to stratum 4 (the real enclosure) and is therefore a *cross-stratum* comparison $\Lambda_{6\to 4}$, not an instance of the adjacent-stratum functional $\Lambda_{i\to i+1}$. For this cross-stratum loss we compute $\Lambda_{6\to 4}=7$ bits at depth $n=10$, base $p=2$, real precision $\varepsilon=2^{-3}$; we prove the exact linear law $\Lambda_{6\to 4}(n)=n-3$ at fixed $\varepsilon$, identify the loss-free matching depth $n=3$, and show that no integer loss-free depth exists for $p=3$ at dyadic precision. Finite simultaneous-valuation products over the primes $\{2,3,5\}$ yield 30 states at depth 1 and 900 at depth 2. State-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth; the recovery claims for the continuum, complex, and adele strata remain conjectural. All numbers are derived by hand; no simulation or external measurement is used. The result converts a philosophical thesis into falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: $\mathbb{N} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$, with $\mathbb{Q}_{p}$ and $\mathbb{A}$ attached to $\mathbb{Q}$ as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model lacks a principled way to decide whether the continuum is forced or merely conventional; a logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order; a computer scientist working with finite-precision arithmetic has no theory of what information is destroyed when a tree-structured limit is flattened onto a line. If the progression $\mathbb{N} \to \mathbb{Q} \to \mathbb{R} \to \mathbb{C} \to \mathbb{Q}_{p} \to \mathbb{A}$ could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The thesis has existing advocates, and each supplies a piece of the vocabulary. The measurement-stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure—marking, ratio comparison, convergent sequences, lossy projection to the continuum, imaginary enclosure, $p$-adic enclosure—and frames every earlier framework as "not wrong, but incomplete" [11]. The Adelic Physics Program argues that the physically accessible base field is $\mathbb{Q}$ rather than $\mathbb{R}$, because every measurement produces a rational number to finite precision, and that Ostrowski's theorem then forces every $p$-adic completion of $\mathbb{Q}$ to be physically meaningful on par with the Archimedean one [10]. The computable-real-boundary work builds number systems from two primitives of Spencer-Brown's *Laws of Form*: the mark, whose repeated indication collapses under the Calling rule, and the enclosure, the boundary a distinction creates; it identifies the fixed point of finite enclosure operations with the computable reals $\mathbb{R}_{\text{comp}}$ [12]. None of these programs supplies a quantitative layer—state counts, loss budgets, falsifiers—with full arithmetic. This paper adds one, and repairs two defects found in its own published predecessor [9].

The two corrections that motivate this revision are stated plainly. First, the published version's Derivation 4 presented the quantity $\Lambda_{\text{Monna}}=\log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon)$ as an instance of the adjacent-stratum loss functional $\Lambda_{i\to i+1}$. That presentation was wrong: the source stratum 6 ($p$-adic tree) and the target stratum 4 (real enclosure at precision $\varepsilon$) are not adjacent in the hierarchy, since strata 5 (phase enclosure) and the intervening structure lie between them in the operator list, and the canonical map $S_{6}\to S_{7}$ is the adele enclosure, not the Monna projection. The correct reading, adopted throughout this revision, is that $\Lambda_{\text{Monna}}$ is a *cross-stratum* comparison $\Lambda_{6\to 4}$, defined by the same counting formula but not instantiating the adjacent-stratum morphism sequence. Second, the published limitation that "state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth" is confirmed and retained: no finite-depth verification exists for strata 2, 4, 5, or 7, and every recovery claim for those strata is labeled conjectural.

We posit a primitive mark $M$ and a family of enclosure operators $E_{i}$, each a closure-type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable-state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree-to-continuum cross-stratum comparison—the projection analogous to the lossy-projection enclosure of [11]. Every number reported in Section 5 is derived by hand in Section 4; no simulation, measurement, or external data is used.

**Contributions.**
1. Explicit state-count derivations for the tally, real-enclosure, and $p$-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).
2. The corrected Monna cross-stratum loss budget: $\Lambda_{6\to 4}=7$ bits at $(p=2,n=10,\varepsilon=2^{-3})$, the exact linearity $\Lambda_{6\to 4}(n)=n-3$ at fixed precision, the vanishing of the loss at matched depth $n=3$, and the explicit reclassification of this quantity as a cross-stratum rather than adjacent-stratum loss (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous-valuation product counts of 30 and 900 over the primes $\{2,3,5\}$ at depths 1 and 2 (Section 4, Derivation 6).
4. The non-dyadic no-matching result: for $p=3$ and $\varepsilon=2^{-3}$, no integer depth yields zero loss, because the required depth $n=3/\log_{2}3\approx 1.893$ is not an integer (Section 4, Derivation 8).
5. Falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of $\Lambda$, stated so that a single counterexample kills the corresponding claim (Section 3.4, analyzed in Section 6).

## 2. Background and Related Work

We review the related work, citing each source for the specific results its text states.

The measurement-stratigraphy framework proposes that the history of number systems is a history of expanding distinction operations, each yielding a richer number system while embedding a new hidden assumption, and it states the goals of identifying those hidden assumptions, forecasting future eras, and grounding the forecast in falsifiable calibration entries [11]. Its banner principle—"not wrong, but incomplete"—reframes skepticism about earlier frameworks into a search for the larger structure that heals incompleteness while preserving local validity [11]. The framework also supplies a cross-domain consilience table in which "lossy projection" is mapped to coarse-graining in physics, lossy compression in computer science, categorization in cognitive science, and the noisy channel in information theory [11]; our loss functional $\Lambda$ is the number-theoretic instance of that row. The framework leaves the recovery claims for the continuum, complex, and adele strata as conjectures, which is exactly the gap this paper's state-count arithmetic addresses.

The Adelic Physics Program argues that physics operates exclusively at the Archimedean place, that this choice is an unjustified assumption, and that the physically accessible numbers are rational: every measurement produces a rational number to finite precision, and every computer simulation operates on finite-precision rationals [10]. Its anchor is Ostrowski's theorem, which it states as the classification of every non-trivial absolute value on $\mathbb{Q}$ as equivalent either to the standard Archimedean one (completion $\mathbb{R}$) or to a $p$-adic one (completion $\mathbb{Q}_{p}$), and it draws the conclusion that the Archimedean completion and every $p$-adic completion are equally legitimate completions of the physical number system [10]. This theorem is the reason our falsifier F3 (a completion of $\mathbb{Q}$ outside the standard list) is expected to fail, making the adele stratum the safest conjecture in the hierarchy.

The primitive vocabulary is supplied by the computable-real-boundary work, which builds number systems from the mark and the enclosure of Spencer-Brown's *Laws of Form*, governed by the Calling rule (two identical indications collapse to one) and the Crossing rule (a distinction entered and exited cancels) [12]. Its "LoF Number Builder" table derives the number 1 from a single indication, $\mathbb{N}$ from iterated marking under Calling, positional notation from nested enclosures grouped by a base, and $\mathbb{Q}$ from enclosures of ratio groups [12]. Its central claim is that the fixed point of re-entry under finite enclosure operations is exactly $\mathbb{R}_{\text{comp}}$, and that everything beyond this closure—non-computable reals, non-measurable sets—belongs to "Cognitive Fiction," with the burden of proof on those who claim a non-computable number is physically necessary [12]. Our stratum 3 and its Cauchy-sequence enclosure adopt this identification, and our stratum 4 (the lossy continuum) is the structure that lies beyond the computable fixed point.

The published predecessor of this paper states the seven-operator hierarchy, the state-count table for the first strata, and the loss functional, and its own results table reports the Monna loss of 7 bits, the linear law $\Lambda(n)=n-3$, the matched depth $n=3$, and the finite adele-type products 30 and 900 [9]. Its discussion already flags that state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth and that $\Lambda$ counts states but not structure [9]. This revision keeps those verified numbers, corrects the misclassification of the Monna quantity as an adjacent-stratum loss, and strengthens the falsifiability apparatus.

Non-canonical number systems show that the tally operator $E_{1}$ admits many digit-set realizations: the paper investigates whether every integer has a finite expansion on a given integer base $b$ when the digit set does not contain 0, proves that such digit sets exist, and provides infinitely many examples for every base with $|b|\ge 4$ [6]. Its examples section proves that $\{1,2\}$ is a valid digit set for base $-2$, and analyzes validity through the dynamic mapping $T:\mathbb{Z}\to\mathbb{Z}$, $a\mapsto(a-d(a))/b$ and its attractor [6]. This supports the claim that the operator, not the particular digit set, is the invariant of the tally stratum—and simultaneously weakens any claim that the operator uniquely determines the canonical $\mathbb{N}$, a failure mode we carry into Section 6.

Stratified $\beta$-numbers modify P. Jones's $\beta$-numbers for Carnot groups, where $\beta_{E}(x,r)=\inf_{L}\sup_{z\in E\cap B(x,r)} d(z,L)/r$ measures how closely a set $E$ lies to an affine line, and prove that an analogue of Jones's traveling-salesman theorem on 1-rectifiability holds in any Carnot group when the $\beta$-numbers are replaced by stratified ones [3]. The paper also shows that the non-stratified $\beta$'s cannot provide sharp two-sided traveling-salesman inequalities for certain Carnot groups, which necessitates the stratified variant [3]. The methodological parallel is exact: a stratified quantity supplies a scale-sensitive measure of how well a discrete object fits a smooth one, and Section 6 proposes refining $\Lambda$ along these lines.

Three congruence papers exhibit deep, still-active structure in the $p$-adic stratum. The first proves, for every prime $p\ge 7$, the congruence $\sum_{k=1}^{p-1} H_{k}^{2}/k^{2} \equiv \frac{4}{5}pB_{p-5} \pmod{p^{2}}$, where $H_{k}$ are harmonic numbers and $B_{m}$ Bernoulli numbers, confirming a conjecture of Z.-W. Sun, and proves two similar congruences modulo $p^{2}$ [2]. The second poses many conjectures on congruences involving binomial coefficients and Apéry-like numbers modulo $p^{2}$, with case distinctions governed by quadratic representations such as $4p=x^{2}+27y^{2}$ [4]. The third extends the program to congruences modulo $p^{3}$ for sums involving binomial coefficients and Apéry-like numbers, again with case distinctions by quadratic representations of $p$ [7]. These results show that the internal arithmetic of the divisibility enclosure $E_{6}$ is a live research frontier whose phenomena (Bernoulli numbers, Apéry-like sums, quadratic representations) lie beyond the simple field structure our operator list generates—a pressure point on falsifier F3.

The Tate-conjecture note proves both Tate conjectures for algebraic cycles on products of elliptic curves and abelian surfaces over number fields: it shows that the Hodge conjecture for $X_{\mathbb{C}}$ and the Mumford–Tate conjecture for $X$ together imply Tate I, and reduces Tate II to showing $\dim V_{\ell}^{\Gamma_{F}}=-\operatorname{ord}_{s=1}L(V,s)$ [1]. The objects live over $\mathbb{Q}$ and its finite extensions, illustrating that deep arithmetic geometry is conducted over number fields whose completions are exactly the strata our hierarchy organizes.

The survey of the Caccetta–Häggkvist conjecture—which states that a finite directed graph with at least $n/k$ edges out of each vertex contains a directed cycle of length at most $k$—records that Hamidoune used additive number theory to prove the conjecture for Cayley graphs and vertex-transitive graphs, with the proof resting on Kemperman's theorem bounding the growth of iterated product sets $B^{k}$ in a group [5]. Repeated application of a generator expanding a reachable set is the combinatorial shadow of the tally operator $E_{1}$, and Section 6 asks whether Kemperman-type growth bounds can be repurposed as lower bounds on the state growth of $E_{1}$.

The super-powers paper studies sequences $s_{n}=\sum_{i=1}^{k}\prod_{j=0}^{\ell}x_{i,j}^{n^{j}}$ and proves an equivalence concerning the number $\omega(s_{n})$ of distinct prime factors: there exist a real $\theta>1$ and infinitely many $n$ with $\omega(s_{n})$ exceeding a super-logarithmic bound, with the analysis conducted through $p$-adic valuations $\upsilon_{p}(x)$, the exponent of the largest power of $p$ dividing $x$ [8]. That a theorem about prime-factor counts is proved through $p$-adic valuations is a concrete instance of the divisibility enclosure $E_{6}$ acting as an analytic instrument, not merely a completion.

These works collectively provide concrete instances of the operators, the state-count phenomena, and the deep arithmetic that the stratified-distinction framework must accommodate.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark $M$ satisfying the idempotent law

$$MM = M,$$

the *Calling* rule of the Laws of Form calculus [12]. A *distinction operation* $D$ partitions a structure into distinguishable classes. An *enclosure operator* $E$ is a closure-type operator on structures satisfying

$$S\subseteq E(S),\qquad E(E(S))=E(S),\qquad S\subseteq T\;\Rightarrow\;E(S)\subseteq E(T).$$

Each stratum is defined as

$$S_{i}=E_{i}(S_{i-1}),\qquad i=1,\dots,7,$$

with the operators indexed by their target stratum.

### 3.2 The strata

| Stratum | Operator $E_{i}$ | Minimal algebraic structure | Distinguishable-state count $N_{i}$ (parameterised) |
|---|---|---|---|
| 0 (the mark) | — | $\{M\}$ | $N_{0}=1$ |
| 1 (tally, $\mathbb{N}$) | tally enclosure | free monoid on one generator $\to$ $\mathbb{N}$ with addition | $N_{1}(n)=n+1$ (depth $n$) |
| 2 (ratio, $\mathbb{Q}$) | ratio-compare | field of fractions of $\mathbb{Z}$ $\to$ $\mathbb{Q}$ | $N_{2}$ infinite (no finite truncation needed) |
| 3 (convergent sequences, $\mathbb{R}_{\text{comp}}$) | Cauchy-sequence enclosure | computable reals $\mathbb{R}_{\text{comp}}$ | $N_{3}$ infinite |
| 4 (lossy tree projection, $\mathbb{R}$) | Monna-type projection $\pi_{M}$ | continuum $\mathbb{R}$ | $N_{4}(\varepsilon)=1/\varepsilon$ (real precision $\varepsilon$) |
| 5 (phase enclosure, $\mathbb{C}$) | phase enclosure | $\mathbb{C}\cong\mathbb{R}\times S^{1}$ | $N_{5}$ infinite |
| 6 (divisibility enclosure, $\mathbb{Q}_{p}$) | $p$-adic completion | $\mathbb{Q}_{p}$ | $N_{6}(n)=p^{n}$ (depth $n$) |
| 7 (simultaneous valuations, $\mathbb{A}$) | adele enclosure | $\mathbb{A}= \mathbb{R}\times\!\!\prod_{p}'\mathbb{Q}_{p}$ | $N_{7}$ infinite (restricted product) |

The recovery claims—that $E_{4}$ applied to a tree-like limit yields the continuum $\mathbb{R}$, that $E_{5}$ yields $\mathbb{C}$, and that $E_{7}$ yields the adele ring—are conjectures, consistent with the stratigraphy framework's own status for these strata [11]. Only the state-count formulas for strata 0, 1, 3 (as the infinite count inherited from the computable fixed point of [12]), and 6 are used in finite arithmetic below.

### 3.3 Morphisms and the loss functionals

Between adjacent strata $S_{i}\to S_{i+1}$ we take the canonical map induced by the operator. The *adjacent-stratum information-loss functional* is

$$\Lambda_{i\to i+1}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{i+1}(\text{params}),$$

the base-2 logarithm of the ratio of distinguishable-state counts, i.e. the number of bits destroyed by the projection.

**Correction to the published version [9].** The published Derivation 4 presented the Monna quantity as an instance of $\Lambda_{i\to i+1}$. It is not. The Monna projection $\pi_{M}$ maps a depth-$n$, base-$p$ tree (whose state count is $N_{6}(n)=p^{n}$) onto a line at precision $\varepsilon$ (whose state count is $N_{4}(\varepsilon)=1/\varepsilon$); source and target are strata 6 and 4, which are not adjacent, and the canonical adjacent map out of $S_{6}$ is the adele enclosure $E_{7}$, not $\pi_{M}$. We therefore define a *cross-stratum loss functional* for any ordered pair of strata $i,j$ with finite counts:

$$\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),$$

of which the adjacent-stratum functional is the special case $j=i+1$. The Monna quantity is

$$\Lambda_{\text{Monna}}(n,p,\varepsilon)=\Lambda_{6\to 4}(n,p,\varepsilon)=\log_{2}\!\bigl(p^{n}\bigr)-\log_{2}\!\bigl(1/\varepsilon\bigr)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr).$$

All Monna results in this paper are stated as properties of $\Lambda_{6\to 4}$. The physical motivation for comparing strata 6 and 4 specifically comes from the adelic thesis that $\mathbb{Q}$ (and its $p$-adic completions) is the physically accessible base and the continuum a derived, lossy representation [10]; the cross-stratum loss measures exactly the cost of that representation.

### 3.4 Falsifiability conditions

Following the discipline of [12], each recovery claim carries a stated falsifier.

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

The Monna projection $\pi_{M}$ maps the depth-10 binary tree onto the real line at precision $\varepsilon=2^{-3}$. As established in Section 3.3, this is a cross-stratum comparison $\Lambda_{6\to 4}$, not an adjacent-stratum loss:

$$\Lambda_{6\to 4} = \log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon)
= \log_{2}(1024)-\log_{2}(8)=10-3=7.$$

Checking via the ratio form:

$$\Lambda_{6\to 4} = \log_{2}\!\left(\frac{1024}{8}\right)=\log_{2}(128)=7,$$

and $2^{7}=128$ confirms the ratio. The numerical value 7 bits is unchanged from the published version [9]; what changes is its classification.

### Derivation 5 (linearity and vanishing)

Fix $\varepsilon=2^{-3}$ and vary depth $n$. Since $N_{6}(n)=2^{n}$ and $N_{4}(\varepsilon)=2^{3}$,

$$\Lambda_{6\to 4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3,$$

which is strictly increasing in $n$. At $n=3$ the loss is

$$\Lambda_{6\to 4}(3)=3-3=0,$$

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

$$\Lambda_{6\to 4}(n)=\log_{2}(3^{n})-3 = n\log_{2}3-3.$$

Setting $\Lambda_{6\to 4}=0$ gives $n=3/\log_{2}3$. Since $\log_{2}3=\ln 3/\ln 2\approx 1.05361/0.69315\approx 1.58496$,

$$n=\frac{3}{1.58496}\approx 1.893,$$

not an integer. Hence no integer depth yields zero loss for $p=3$ at this precision; the loss-free matching of Result R2 is a dyadic accident. In general, an integer loss-free depth exists if and only if $\log_{2}(1/\varepsilon)/\log_{2}p$ is an integer, i.e. the target precision is a power of the source base.

### Derivation 9 (adjacent-stratum losses at the verified strata)

For completeness we evaluate the adjacent-stratum functional where both endpoints have finite counts. The only adjacent pair with two finite counts among the verified strata is none: stratum 0 has $N_{0}=1$ and stratum 1 has $N_{1}(n)=n+1$, so

$$\Lambda_{0\to 1}(n)=\log_{2}(1)-\log_{2}(n+1)=-\log_{2}(n+1),$$

which is negative for $n\ge 1$: the tally enclosure *creates* distinguishable states rather than destroying them, as expected for an expanding operator. At $n=9$ this is $-\log_{2}(10)\approx -3.3219$ bits. This sign check is the simplest verification that the functional is being applied consistently: enclosure operators that refine distinctions must yield negative adjacent loss, and only projections (such as $\pi_{M}$) yield positive loss.

## 5. Results

All quantities below are computed in Section 4; no simulation or external measurement is reported.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth $n=9$ | $N_{1}(9)=10$ | Derivation 1 |
| Real cells at $\varepsilon=2^{-3}$ | $N_{4}=8$ | Derivation 2 |
| Binary tree states at depth $n=10$ | $N_{6}(10)=1024$ | Derivation 3 |
| Monna cross-stratum loss at $(p=2,n=10,\varepsilon=2^{-3})$ | $\Lambda_{6\to 4}=7$ bits | Derivation 4 |
| Monna cross-stratum loss at depth $n$, $\varepsilon=2^{-3}$ | $\Lambda_{6\to 4}(n)=n-3$ | Derivation 5 |
| Loss-free matching depth | $n=3$ ($\Lambda_{6\to 4}=0$) | Derivation 5 |
| Finite adele-type product, depth 1, $\{2,3,5\}$ | $30$ | Derivation 6 |
| Finite adele-type product, depth 2 | $900$ | Derivation 6 |
| Total strata (mark + 7 operators) | $8$ | Derivation 7 |
| Non-dyadic matching depth for $p=3$ | none (required $n\approx 1.893$) | Derivation 8 |
| Adjacent loss $\Lambda_{0\to 1}$ at $n=9$ | $\approx -3.3219$ bits (state creation) | Derivation 9 |
| Projected loss for $p=3,n=5,\varepsilon=10^{-2}$ (assumption) | $\approx 1.28$ bits | Projection (see text) |

**Result R1.** The Monna cross-stratum loss is exactly linear in tree depth at fixed real precision: $\Lambda_{6\to 4}(n)=n-3$ bits for $\varepsilon=2^{-3}$, $p=2$. Deeper trees carry strictly more information than any fixed-precision continuum target.

**Result R2.** There exists a matched-parameter pair $(n=3,\varepsilon=2^{-3})$ at which the $p$-adic tree and the real enclosure have identical state counts ($2^{3}=8$), i.e. zero cross-stratum loss. This is the precise sense in which the tree-like limit and the continuum carry "the same information, differently metricized" at matched resolution. The matching is dyadic: Derivation 8 shows no integer matching depth exists for $p=3$ at dyadic precision.

**Result R3.** The stratum sequence has eight levels including the mark