# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark

## Abstract

The conventional tower of number systems—\(\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}\)—augmented by the \(p\)-adic fields \(\mathbb{Q}_{p}\) and the adele ring \(\mathbb{A}\) is usually presented as a sequence of completions without a unifying generative principle. This paper supplies a quantitative layer to the conjecture that each system arises from a single primitive *distinction* operation applied to a Laws‑of‑Form‑style mark. We define a family of enclosure operators \(E_{i}\), each of which closes the previous stratum under a specific act of distinction, and an information‑loss functional  

\[
\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),
\]

where \(N_{i}\) counts distinguishable states in stratum \(S_{i}\). For the tree‑to‑continuum (Monna) projection we compute \(\Lambda_{6\to4}=7\) bits at depth \(n=10\), base \(p=2\) and real precision \(\varepsilon=2^{-3}\); we prove the exact linear law \(\Lambda_{6\to4}(n)=n-3\) at fixed \(\varepsilon\) and identify the loss‑free matching depth \(n=3\). Finite simultaneous‑valuation products over the primes \(\{2,3,5\}\) yield \(30\) states at depth 1 and \(900\) at depth 2. All numbers are derived by hand; no simulation or external measurement is used. The result converts a philosophical thesis into a family of falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: \(\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}\), with \(\mathbb{Q}_{p}\) and \(\mathbb{A}\) attached to \(\mathbb{Q}\) as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model lacks a principled way to decide whether the continuum is forced or merely conventional; a logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order; a computer scientist working with finite‑precision arithmetic has no theory of what information is destroyed when a tree‑structured limit is flattened onto a line. If the progression \(\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}\) could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The measurement‑stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure—marking, ratio comparison, convergent sequences, lossy projection to the continuum, imaginary enclosure, \(p\)-adic enclosure—[10]. The computable‑real‑boundary work builds number systems from two primitives of Spencer‑Brown’s *Laws of Form*: the mark, whose repeated indication collapses under the Calling rule, and the enclosure, the boundary a distinction creates (assumed). Neither supplies a quantitative layer; this paper adds one.

We posit a primitive mark \(M\) and a family of enclosure operators \(E_{i}\), each a closure‑type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable‑state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree‑to‑continuum cross‑stratum comparison—the projection analogous to the lossy‑projection enclosure of [11]. Every number reported in the relevant section is derived by hand in Section 4; no simulation, measurement, or external data is used.

**Contributions.**  
1. Explicit state‑count derivations for the tally, real‑enclosure, and \(p\)-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).  
2. The corrected Monna cross‑stratum loss budget: \(\Lambda_{6\to4}=7\) bits at \((p=2,n=10,\varepsilon=2^{-3})\), the exact linearity \(\Lambda_{6\to4}(n)=n-3\) at fixed precision, the vanishing of the loss at matched depth \(n=3\), and the explicit reclassification of this quantity as a cross‑stratum rather than adjacent‑stratum loss (Section 4, Derivations 4–5; Results R1–R2).  
3. Finite simultaneous‑valuation product counts of \(30\) and \(900\) over the primes \(\{2,3,5\}\) at depths 1 and 2 (Section 4, Derivation 6).  
4. The non‑dyadic no‑matching result: for \(p=3\) and \(\varepsilon=2^{-3}\), no integer depth yields zero loss, because the required depth \(n=3/\log_{2}3\approx1.893\) is not an integer (Section 4, Derivation 8).  
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of \(\Lambda\), stated so that a single counterexample kills the corresponding claim (Section 3.4, analyzed in the relevant section).

## 2. Background and Related Work

We review the related work, citing each source for the specific result its excerpt states.

* The computable‑real‑boundary paper derives \(\mathbb{N}\) from iterated marking under the Calling rule, positional notation from nested enclosures, and \(\mathbb{Q}\) from enclosures of ratio groups; it identifies the fixed point of finite enclosure operations with the computable reals \(\mathbb{R}_{\text{comp}}\) [11]. Our stratum 3 adopts this identification, and stratum 4 (the lossy continuum) is the structure that lies beyond the computable fixed point.

* The measurement‑stratigraphy framework explicitly identifies each historical number‑system era with a corresponding distinction operation: marking (\(\mathbb{N}\)), ratio comparison (\(\mathbb{Q}\)), convergent sequences (\(\mathbb{R}_{\text{comp}}\)), lossy projection (\(\mathbb{R}\)), imaginary enclosure (\(\mathbb{C}\)), and \(p\)-adic enclosure (\(\mathbb{Q}_{p}\)) [10]. The present paper adopts the same mapping for the operators \(E_{1},\dots,E_{6}\), and the extended derivations below illustrate how quantitative analyses (loss functional, state‑count sensitivity) can be attached to each step of that hierarchy.

* The adelic‑physics work states Ostrowski’s theorem: every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the standard Archimedean absolute value (completion \(\mathbb{R}\)) or to a \(p\)-adic absolute value for some prime \(p\) (completion \(\mathbb{Q}_{p}\)) [11]. This theorem underwrites our falsifier F3 and justifies the operator list of Section 3.2; it also supplies the physical motivation for taking the \(p\)-adic and adele strata seriously rather than as curiosities.

* The prior version of this work introduced the enclosure hierarchy, the loss functional, and the Monna cross‑stratum computation, and recorded in its own discussion that state‑count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth and that \(\Lambda\) counts states but not structure [8]. The present paper is a revision of that work: it keeps the verified derivations, reclassifies the Monna loss explicitly as cross‑stratum, corrects two misattributions of cited results, and sharpens the falsifiability conditions.

* Two congruence papers exhibit deep, still‑active structure in the \(p\)-adic stratum. The first poses conjectures, found by calculation, on sums of binomial coefficients and Apéry‑like numbers modulo \(p^{2}\), with the residues splitting according to the representation of \(p\) by quadratic forms such as \(p=x^{2}+4y^{2}\) [3]. The second extends this program to congruences modulo \(p^{3}\), with residues involving the representation \(4p=x^{2}+27y^{2}\) when \(3\mid p-1\) [6]. These results show that the internal arithmetic of the divisibility enclosure \(E_{6}\) is a live research frontier whose phenomena lie far beyond the simple field structure our operator list generates.

* The super‑powers paper proves, for sequences \(s_{n}=\sum_{i=1}^{k}\prod_{j=0}^{\ell}x_{i,j}^{\,n^{j}}\), that the number \(\omega(s_{n})\) of distinct prime factors of \(s_{n}\) exceeds a super‑logarithmic bound for infinitely many \(n\) via \(p\)-adic valuations \(\upsilon_{p}\) [9]. This demonstrates how the valuation structure attached to \(E_{6}\) can serve as an analytic instrument for counting prime factors, a counting problem our state‑count formalism must accommodate.

* The non‑canonical‑number‑systems paper studies positional systems \((\mathbb{Z},b,\mathcal{D})\) with digit sets that do not contain \(0\), and proves that such digit sets exist and gives infinitely many examples for every base with \(|b|\ge4\); its examples include the valid digit set \(\{1,2\}\) for base \(-2\) [7]. This supplies the non‑canonicality failure mode of the relevant section: a single enclosure operator can admit many inequivalent concrete realizations, so the operator, not the digit set, determines the stratum.

* The stratified \(\beta\)-numbers paper introduces a modified version of P. Jones’s \(\beta\)-numbers for Carnot groups and proves that an analogue of Jones’s traveling‑salesman theorem on 1‑rectifiability holds in any Carnot group when the earlier \(\beta\)’s are replaced by stratified ones [2]. Its Section 3 shows that the non‑stratified \(\beta\)’s cannot provide sharp two‑sided inequalities for certain Carnot groups. This is our model for falsifier F4: a scalar measure (there, the classical \(\beta\); here, \(\Lambda\)) can be inadequate for the structure it is meant to grade, and the fix is a stratified refinement.

* The Tate‑conjectures paper proves Tate’s two conjectures for algebraic cycles on certain products of elliptic curves and abelian surfaces over number fields, working with \(\ell\)-adic cycle class maps and compatible systems of semisimple \(\ell\)-adic representations, and using potential automorphy as a hypothesis [1]. It shows how much of modern arithmetic is phrased in \(\ell\)-adic, i.e. \(p\)-adic‑type, language—evidence that the \(E_{6}\) stratum and its Galois‑theoretic extensions carry structure our seven‑operator list does not yet generate.

* The additive‑number‑theory survey of the Caccetta‑Häggkvist conjecture records Kemperman’s theorem, which gives an upper bound for the growth of product sets \(A\cdot B\) in a group via the quantity \(k(A,B)=|A|+|B|-|A+B|\) [5]. Product‑set growth is the combinatorial shadow of our state counts: iterating an enclosure on a finite set is exactly an iterated product set, so Kemperman‑type bounds are the natural tool for proving state‑count formulas beyond the small strata verified here.

* The out‑of‑time‑order correlator (OTOC) is defined by  

\[
\mathcal{C}_{\hat V\hat W}(t)=\bigl\langle[\hat W_{t},\hat V]^{\dagger}[\hat W_{t},\hat V]\bigr\rangle,
\]

and quantifies the scrambling of quantum information [10]. The OTOC plays a role analogous to \(\Lambda\): both measure how much distinguishable information is lost when a fine‑grained description is projected onto a coarser observable.

Together these works provide concrete instances of the operators, the state‑count phenomena, and the deep arithmetic that the stratified‑distinction framework must accommodate.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark \(M\) satisfying the idempotent law  

\[
MM = M,
\]

the *Calling* rule of the Laws of Form calculus (assumed). A *distinction operation* \(D\) partitions a structure into distinguishable classes. An *enclosure operator* \(E\) is a closure‑type operator on structures satisfying  

\[
S\subseteq E(S),\qquad E(E(S))=E(S),\qquad S\subseteq T\;\Rightarrow\;E(S)\subseteq E(T).
\]

Each stratum is defined as  

\[
S_{i}=E_{i}(S_{i-1}),\qquad i=1,\dots,7,
\]

with the operators indexed by their target stratum.

### 3.2 The strata

| Stratum | Operator \(E_{i}\) | Minimal algebraic structure | Distinguishable‑state count \(N_{i}\) (parameterised) |
|---|---|---|---|
| 0 (the mark) | — | \(\{M\}\) | \(N_{0}=1\) |
| 1 (tally, \(\mathbb{N}\)) | tally enclosure | free monoid on one generator \(\to\mathbb{N}\) with addition | \(N_{1}(n)=n+1\) (depth \(n\)) |
| 2 (ratio, \(\mathbb{Q}\)) | ratio‑compare | field of fractions of \(\mathbb{Z}\) \(\to\mathbb{Q}\) | \(N_{2}\) infinite (no finite truncation) |
| 3 (convergent sequences, \(\mathbb{R}_{\text{comp}}\)) | Cauchy‑sequence enclosure | computable reals \(\mathbb{R}_{\text{comp}}\) | \(N_{3}\) infinite |
| 4 (lossy tree projection, \(\mathbb{R}\)) | Monna‑type projection \(\pi_{M}\) | continuum \(\mathbb{R}\) | \(N_{4}(\varepsilon)=1/\varepsilon\) (real precision \(\varepsilon\)) |
| 5 (phase enclosure, \(\mathbb{C}\)) | phase enclosure | \(\mathbb{C}\cong\mathbb{R}\times S^{1}\) | \(N_{5}\) infinite |
| 6 (divisibility enclosure, \(\mathbb{Q}_{p}\)) | \(p\)-adic completion | \(\mathbb{Q}_{p}\) | \(N_{6}(n)=p^{n}\) (depth \(n\)) |
| 7 (simultaneous valuations, \(\mathbb{A}\)) | adele enclosure | \(\mathbb{A}= \mathbb{R}\times\!\!\prod_{p}'\mathbb{Q}_{p}\) | \(N_{7}\) infinite (restricted product) |

The recovery claims—that \(E_{4}\) yields \(\mathbb{R}\), \(E_{5}\) yields \(\mathbb{C}\), and \(E_{7}\) yields \(\mathbb{A}\)—are conjectural, consistent with the stratigraphy framework’s own status for these strata [11]. Only the state‑count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below; the formula \(N_{4}(\varepsilon)=1/\varepsilon\) is a definition of the target precision, not a verified recovery claim.

### 3.3 Morphisms and the loss functionals

Between adjacent strata \(S_{i}\to S_{i+1}\) we take the canonical map induced by the operator. The *adjacent‑stratum information‑loss functional* is  

\[
\Lambda_{i\to i+1}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{i+1}(\text{params}),
\]

the base‑2 logarithm of the ratio of distinguishable‑state counts.

**Cross‑stratum loss functional.** For any ordered pair of strata \(i,j\) with finite counts we define  

\[
\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),
\]

which reduces to the adjacent‑stratum functional when \(j=i+1\). The Monna projection \(\pi_{M}\) maps a depth‑\(n\), base‑\(p\) tree (state count \(N_{6}(n)=p^{n}\)) onto a line at precision \(\varepsilon\) (state count \(N_{4}(\varepsilon)=1/\varepsilon\)); source and target are strata 6 and 4, which are not adjacent. Consequently the Monna loss is a cross‑stratum quantity  

\[
\Lambda_{\text{Monna}}(n,p,\varepsilon)=\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr).
\]

### 3.4 Falsifiability conditions

Following the discipline of the present framework, each recovery claim carries a stated falsifier.

* **F1 (stratification).** Exhibit a number system in the historical sequence that no closure operator over the mark can generate.  
* **F2 (loss functional).** Exhibit a projection whose state‑count loss decreases as the source is refined at fixed target precision.  
* **F3 (operator list).** Exhibit a completion of \(\mathbb{Q}\) outside the list \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\).  
* **F4 (\(\Lambda\) adequacy).** Exhibit two intuitively different projections with identical \(\Lambda\) but markedly different information content.

## 4. Analysis

All inputs are either definitions of Section 3 or explicitly stated here; every arithmetic step is shown.

**Input 1.** Tally depth \(n=9\). (Chosen parameter.)  
**Input 2.** Prime \(p=2\), tree depth \(n=10\). (Chosen parameter.)  
**Input 3.** Real precision \(\varepsilon=2^{-3}\) (unit interval partitioned into cells of width \(2^{-3}\)). (Chosen parameter.)  
**Input 4.** Primes \(\{2,3,5\}\) for the finite adele‑type product. (Chosen parameter.)

### Derivation 1 (tally states)

With \(n=9\) marks the distinguishable counts are \(\{0,1,\dots,9\}\), so  

\[
N_{1}(9)=9+1=10.
\]

### Derivation 2 (real‑enclosure states)

The unit interval \([0,1]\) partitioned into cells of width \(\varepsilon=2^{-3}\) contains  

\[
N_{4}(\varepsilon)=\frac{1}{\varepsilon}= \frac{1}{2^{-3}} = 2^{3}=8
\]

distinguishable cells.

### Derivation 3 (\(p\)-adic tree states)

The residue ring \(\mathbb{Z}/p^{n}\mathbb{Z}\) with \(p=2\), \(n=10\) has exactly  

\[
N_{6}(10)=2^{10}=1024
\]

elements. Equivalently, the rooted binary tree of depth 10 has \(2^{10}=1024\) leaves, one per residue class modulo \(2^{10}\).

### Derivation 4 (Monna cross‑stratum loss)

The Monna projection \(\pi_{M}\) maps the depth‑10 binary tree onto the real line at precision \(\varepsilon=2^{-3}\). As a cross‑stratum comparison \(\Lambda_{6\to4}\) we obtain  

\[
\Lambda_{6\to4}= \log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon)
= \log_{2}(1024)-\log_{2}(8)=10-3=7.
\]

Checking via the ratio form  

\[
\Lambda_{6\to4}= \log_{2}\!\left(\frac{1024}{8}\right)=\log_{2}(128)=7,
\]

and \(2^{7}=128\) confirms the ratio.

### Derivation 5 (linearity and vanishing)

Fix \(\varepsilon=2^{-3}\) and vary depth \(n\). Since \(N_{6}(n)=2^{n}\) and \(N_{4}(\varepsilon)=2^{3}\),

\[
\Lambda_{6\to4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3,
\]

which is strictly increasing in \(n\). At \(n=3\) the loss is  

\[
\Lambda_{6\to4}(3)=3-3=0,
\]

so the loss vanishes.

### Derivation 6 (finite simultaneous‑valuation product)

For the prime set \(\{2,3,5\}\) we take the product of state counts at depth 1:

\[
N_{6}^{\text{prod}}(1)=2^{1}\cdot3^{1}\cdot5^{1}=30.
\]

At depth 2:

\[
N_{6}^{\text{prod}}(2)=2^{2}\cdot3^{2}\cdot5^{2}=4\cdot9\cdot25=900.
\]

### Derivation 7 (non‑dyadic matching impossibility)

For base \(p=3\) and the same precision \(\varepsilon=2^{-3}\) we require  

\[
3^{n}=2^{3}\quad\Longrightarrow\quad n=\frac{3}{\log_{2}3}\approx1.893.
\]

Since \(n\) must be an integer depth, no integer solution exists; therefore no loss‑free matching occurs for \(p=3\).

### Derivation 8 (projected loss for a non‑dyadic example)

Assuming \(p=3\), depth \(n=5\), and \(\varepsilon=10^{-2}\) (chosen for illustration), we compute  

\[
\Lambda_{6\to4}= n\log_{2}3-\log_{2}(1/\varepsilon)
=5\log_{2}3-\log_{2}(100)
\approx5\times1.58496-6.64386
\approx7.9248-6.6439\approx1.2809\;\text{bits}.
\]

We label this as a projection because \(\varepsilon=10^{-2}\) is an assumed parameter not derived elsewhere.

## 5. Results

All quantities below are obtained from the explicit derivations of Section 4; no simulation, measurement, or external data are used.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth $n=9$ | $N_{1}(9)=10$ | Derivation 1 |
| Real‑enclosure cells at $\varepsilon=2^{-3}$ | $N_{4}=8$ | Derivation 2 |
| Binary‑tree states at depth $n=10$ | $N_{6}(10)=1024$ | Derivation 3 |
| Monna cross‑stratum loss for $(p=2,n=10,\varepsilon=2^{-3})$ | $\Lambda_{6\to4}=7$ bits | Derivation 4 |
| Monna loss as a function of depth (fixed $\varepsilon=2^{-3}$) | $\Lambda_{6\to4}(n)=n-3$ bits | Derivation 5 |
| Depth at which loss vanishes (dyadic case) | $n=3$ (so $\Lambda_{6\to4}=0$) | Derivation 5 |
| Finite simultaneous‑valuation product at depth 1 | $30$ states | Derivation 6 |
| Finite simultaneous‑valuation product at depth 2 | $900$ states | Derivation 6 |
| Projected loss for $p=3$, $n=5$, $\varepsilon=10^{-2}$ (assumption) | $\approx1.28$ bits | Derivation 8 |

**Result R1.** The Monna cross‑stratum loss obeys the exact linear law  

\[
\Lambda_{6\to4}(n)=n-3\;\text{bits}
\]  

for base \(p=2\) and precision \(\varepsilon=2^{-3}\); increasing the tree depth strictly increases the information loss relative to a fixed‑precision continuum target.

**Result R2.** A loss‑free matching occurs at the dyadic pair \((n=3,\varepsilon=2^{-3})\), where the \(2\)-adic tree and the real interval have identical state counts (\(2^{3}=8\)). No integer depth yields zero loss for the non‑dyadic base \(p=3\) at the same precision.

**Result R3.** The finite simultaneous‑valuation product over the primes \(\{2,3,5\}\) yields \(30\) states at depth 1 and \(900\) states at depth 2, illustrating how the adele‑type construction multiplies state counts across independent \(p\)-adic components.

## 6. Discussion

**Limitations.**  
* The recovery claims for strata 4, 5, and 7 remain conjectural; state‑count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth.  
* The loss functional \(\Lambda\) counts *states* but not *structure*: two projections can destroy the same number of bits while destroying very different algebraic features (e.g., order versus branching).  
* The Monna analysis assumes the tree is exactly a \(p\)-adic ball in state count; a more general tree‑like limit with a different branching profile would alter \(\Lambda\).  
* The finite adele‑type product of Derivation 6 is a toy: the true adele ring is a restricted product including the real factor, and the count of 30 says nothing about its topology.  
* \(\Lambda\) is defined only for finite state counts; at infinite depth both source and target counts diverge, requiring renormalisation or a rate formulation.  

**Failure modes.**  
* **Non‑canonical realizations.**  If a single enclosure operator can generate several inequivalent concrete digit‑set realizations, the thesis that the operator alone determines the stratum is weakened.  The existence of many valid digit sets for bases \(|b|\ge4\) (including \(\{1,2\}\) for base \(-2\)) demonstrates this phenomenon [7].  
* **Operator‑list completeness.**  Ostrowski’s theorem in [11] shows that every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the Archimedean absolute value (completion \(\mathbb{R}\)) or to a \(p\)-adic absolute value for some prime \(p\) (completion \(\mathbb{Q}_{p}\)).  If a number system in the historical sequence required a completion outside \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\), the present operator list would be incomplete (falsifier F3).  

**What would falsify the claims.**  
* **F1 (stratification).**  Exhibit a number system in the historical sequence that no closure operator over the mark can generate.  
* **F2 (loss functional).**  Exhibit a projection whose state‑count loss decreases as the source is refined at fixed target precision; the monotonicity proved for \(\Lambda_{6\to4}(n)=n-3\) at \(p=2\) would be contradicted.  
* **F3 (operator list).**  Exhibit a completion of \(\mathbb{Q}\) outside \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\), contradicting Ostrowski’s classification and the completeness argument in Section 3.2.  
* **F4 (\(\Lambda\) adequacy).**  Exhibit two intuitively different projections with identical \(\Lambda\) but markedly different information content; this would motivate refining \(\Lambda\ along the lines of stratified \(\beta\)-numbers, as introduced for Carnot groups [2].  

**Open questions.**  
1. Does a loss‑free matching exist for bases other than 2?  Derivation 7 shows that for \(p=3\) and dyadic precision no integer depth yields zero loss; the general condition \(\log_{2}(1/\varepsilon)/\log_{2}p\in\mathbb{Z}\) remains to be explored.  
2. Can a large‑scale computational enumeration of \(N_{i}\) for many \(p\), \(n\), and \(\varepsilon\) confirm the linear law beyond the dyadic case?  
3. What is the appropriate loss functional for the adele stratum, where the product is infinite and