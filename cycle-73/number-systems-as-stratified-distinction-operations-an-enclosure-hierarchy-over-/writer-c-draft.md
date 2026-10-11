# Number Systems as Stratified Distinction Operations: A Formal Sketch of the Enclosure Hierarchy $\mathbb{N} \to \mathbb{Q} \to \mathbb{R} \to \mathbb{C} \to \mathbb{Q}_p \to \mathbb{A}$

## Abstract

We propose and partially formalize a conjecture: that the major number systems arise not as independent mathematical inventions but as successive primitive "distinction" operations applied to an undifferentiated mark, in the spirit of Laws-of-Form-style calculus of indications. Each operation—tallying, enclosure/comparison of ratios, convergence of sequences, phase enclosure, divisibility enclosure, and simultaneous valuation—generates a minimal algebraic structure that recovers, respectively, $\mathbb{N}$, $\mathbb{Q}$, the computable reals, $\mathbb{C}$, $\mathbb{Q}_p$, and the adele ring $\mathbb{A}$. We define a stratified hierarchy of closure operators $E_0 \le E_1 \le \cdots \le E_5$ over a mark, prove elementary recovery theorems for the first three strata, and characterize the information loss between adjacent strata, with particular attention to the projection from a tree-like limit structure to the smooth continuum. We derive quantitative distinguishability profiles for each operator: tallying on a budget of $b$ binary distinctions yields $b+1$ states, while positional enclosure yields $2^{b}$ states, an exponential separation that we compute explicitly. We connect the hierarchy to the adelic thesis that the physically accessible base field is $\mathbb{Q}$ rather than $\mathbb{R}$, under which all $p$-adic completions are demanded by Ostrowski's theorem. The framework is offered as a research program with explicit falsifiability conditions rather than a completed theory.

## 1. Introduction

Why does mathematics exhibit exactly the number systems it does? The standard answer is internalist: each system exists because some prior system lacked completeness, roots, or topology. This paper explores an externalist, operational answer: each number system is the *residue* of a specific primitive act of distinction performed on whatever the previous act left indistinguishable.

The conjecture, in its strongest form, is that the historical and structural progression
$$\mathbb{N} \;\longrightarrow\; \mathbb{Q} \;\longrightarrow\; \mathbb{R} \;\longrightarrow\; \mathbb{C} \;\longrightarrow\; \mathbb{Q}_p \;\longrightarrow\; \mathbb{A}$$
is not accidental but derivable from increasingly refined acts of distinction. Tallying—repeating a mark—generates $\mathbb{N}$. Enclosing and comparing marks—forming ratios—generates $\mathbb{Q}$. Demanding that every convergent sequence of marks have a limit generates the computable reals $\mathbb{R}_{\mathrm{comp}}$. Enclosing a tree-like limit structure by lossy projection generates the continuum. Phase enclosure—distinguishing orientation or rotation—generates $\mathbb{C}$. Divisibility enclosure—distinguishing with respect to a fixed prime—generates $\mathbb{Q}_p$. Performing all such enclosures simultaneously generates the adeles $\mathbb{A}$.

This program is a development of the "Stratigraphy of Measurement" framework, which reinterprets the history of number systems as a sequence of expanding distinction operations, each era adding a new enclosure: marking ($\mathbb{N}$), comparing ratios ($\mathbb{Q}$), convergent sequences ($\mathbb{R}_{\mathrm{comp}}$) [10]. It also builds on the idempotence-first critique of arithmetic, according to which the premise $1+1=2$ already presupposes two distinguishable marks, idempotence ($AA=A$) is the primitive law, and quantity is *created* distinction rather than repetition [12]. The present paper takes these programmatic statements and asks what a minimal formal skeleton would look like, what can be proved at low cost, and what quantitative signatures the hypothesis predicts.

Our contributions are:

1. A stratified hierarchy of enclosure operators $E_0, \ldots, E_5$ over a mark, with definitions precise enough to support recovery theorems (Section 3).
2. Elementary recovery theorems for the strata $\mathbb{N}$, $\mathbb{Q}$, and $\mathbb{R}_{\mathrm{comp}}$, with full proofs (Section 3, Section 4).
3. Explicit computation of the distinguishable-state counts and information-loss ratios between adjacent strata under fixed resource budgets (Section 4).
4. A statement of the adelic completion stratum as the unique maximal enclosure compatible with Ostrowski's theorem, following the adelic physics thesis [9].
5. Falsifiability conditions and a discussion of failure modes (Section 6).

We emphasize scope honestly: the recovery theorems here are elementary and known in essence; the novel content is the uniform operational reading, the quantitative loss profiles, and the proposed morphism structure between strata. The paper is a program sketch, not a classification theorem.

## 2. Background and Related Work

We review the supplied bibliography, noting that it is a heterogeneous corpus: several entries are number-theoretic works only loosely connected to our theme, and we cite them for what their supplied summaries actually state.

**[1] A note on Tate's conjectures for abelian varieties (arXiv:2112.15164v2).** This mostly expository note explains a proof of Tate's two conjectures for algebraic cycles of arbitrary codimension on certain products of elliptic curves and abelian surfaces over number fields. Its relevance to us is structural: Tate's conjectures concern how arithmetic information over a number field is detected by cohomological comparison maps, i.e., by distinctions visible only after passage to suitable completions or reductions. The supplied summary gives no further detail, so we use the work only as evidence that passage between a global field and its comparison structures is a live, nontrivial operation—the same passage our stratum $E_5$ (simultaneous valuation) formalizes.

**[2] Proof of a congruence for harmonic numbers conjectured by Z.-W. Sun (arXiv:1108.1171v2).** For a positive integer $n$ with harmonic number $H_n=\sum_{k=1}^{n}1/k$, this note proves that for any prime $p \ge 7$,
$$\sum_{k=1}^{p-1}\frac{H_k^2}{k^2} \equiv \frac{4}{5}\,p\,B_{p-5} \pmod{p^2},$$
confirming a conjecture of Sun, along with two similar congruences modulo $p^2$. For our purposes this is a concrete instance of the stratum $E_4$ at work: a statement about rational sums ($\mathbb{Q}$-stratum objects) becomes meaningful and provable only when enclosed by the divisibility distinction modulo $p^2$, i.e., by the $p$-adic valuation. Congruence arithmetic is precisely the lossy projection of $\mathbb{Q}$ onto $\mathbb{Z}/p^2\mathbb{Z}$ that our operator $E_4$ abstracts.

**[3] Stratified $\beta$-numbers and traveling salesman in Carnot groups (arXiv:1902.03268v2).** The authors introduce a modified version of P. Jones's $\beta$-numbers for Carnot groups, called *stratified $\beta$-numbers*, and show that an analogue of Jones's traveling salesman theorem on 1-rectifiability of sets holds for any Carnot group when previous notions of $\beta$-numbers are replaced by these. The word "stratified" here refers to the stratification of Carnot (nilpotent) groups, not to our hierarchy, but the structural analogy is direct: rectifiability of a set is detected by a scale-by-scale enclosure statistic ($\beta$-numbers measure how well a set at scale $d$ fits a line), and the theorem says that a set is a curve exactly when these enclosure defects are summable. This is a rigorous model of what our $E_3$ operator is meant to do—recover a smooth object from lossy, scale-indexed projections of a rougher one.

**[4] Conjectures on congruences involving binomial coefficients and Apéry-like numbers (arXiv:2007.12042v4).** This paper poses many challenging conjectures on congruences involving binomial coefficients and Apéry-like numbers. Its summary states no theorems, only the posing of conjectures; we cite it as evidence that the congruence (i.e., $p$-adic enclosure) stratum generates a large and active problem space, consistent with our claim that $E_4$ is a genuinely generative operation rather than a technical afterthought.

**[5] The Caccetta–Häggkvist conjecture and additive number theory (arXiv:math/0603469v1).** The Caccetta–Häggkvist conjecture states that if $G$ is a finite directed graph with at least $n/k$ edges going out of each vertex, then $G$ contains a directed cycle of length at most $k$; Hamidoune used methods and results from additive number theory to prove the conjecture for Cayley graphs and for vertex-transitive graphs, and this expository paper surveys those results. We cite it for the methodological parallel: additive number theory studies what structures survive when only coarse distinctions (sumsets, cardinalities) are available—an instance of our general theme that coarse distinction operators still force rigid structure.

**[6] Noncanonical number systems in the integers (arXiv:0804.2190v1).** This work investigates whether every integer could have a finite expansion on a given integer base $b$ when the digit set does not contain $0$; the authors prove that such digit sets exist and provide infinitely many examples for every base $b$ with $|b| \ge 4$. This is directly relevant to our stratum $E_1$: positional representation is our "enclosure/comparison" operator made concrete, and this result shows that the enclosure operator admits noncanonical variants—many distinct digit enclosures generate the same integers. In our language, the map from digit-system choice to generated monoid is many-to-one, which is exactly the kind of morphism/information-loss datum our framework is designed to record.

**[7] New conjectures involving binomial coefficients and Apéry-like numbers (arXiv:2111.04538v2).** This paper poses many challenging conjectures on congruences for sums involving binomial coefficients and Apéry-like numbers modulo $p^3$, where $p$ is an odd prime. As with [4], the summary states only conjectures; we cite it to note that the congruence stratum supports arbitrarily deep enclosures (modulo $p^3$, and in principle modulo $p^k$ for any $k \ge 1$), which our formalization treats as an increasing filtration inside $E_4$.

**[8] On the number of distinct prime factors of a sum of super-powers (arXiv:1511.08784v3).** Given fixed integers $x_{i,j}$ for $1 \le i \le k$ and $0 \le j \le \ell$, define for every $n \in \mathbb{N}^+$ the sum $s_n := \sum_{i=1}^k \prod_{j=0}^\ell x_{i,j}^{n^j}$. The authors prove an equivalence between: (a) there being a real $\theta > 1$ and infinitely many indices $n$ for which the number of distinct prime factors of $s_n$ exceeds a super-low bound (the summary is truncated at this point), and a second condition (b) not fully stated in the supplied text. We cite it because it studies exactly the interface our strata $E_1$ and $E_4$ straddle: the growth of the number of prime divisors of an integer sequence is a question about how the tally/sequence stratum ($\mathbb{N}$-objects $s_n$) is resolved by the divisibility enclosure (distinct prime factors). The supplied summary is truncated, so we draw no further specific conclusion from it.

**[9] QNFO: The Adelic Physics Program (DOI 10.5281/zenodo.21686727).** This program proposes that the physically accessible base field of physics is $\mathbb{Q}$, not $\mathbb{R}$, and that Ostrowski's theorem demands all $p$-adic completions of $\mathbb{Q}$ be physically meaningful; the paper provides the epistemological and pedagogical infrastructure for this position. Our stratum $E_5$ is the formal shadow of this thesis: once the base of distinctions is $\mathbb{Q}$, the maximal simultaneous enclosure is the adele ring, and any physical theory built on $\mathbb{R}$ alone has, on this view, silently discarded the $p$-adic distinction channels.

**[10] QNFO: The History and Future of Measurement Stratigraphy (DOI 10.5281/zenodo.21705220).** This is the direct ancestor of the present paper: it proposes a unified framework—the Stratigraphy of Measurement—that reinterprets the history of number systems as a sequence of expanding distinction operations, each era adding a new enclosure: marking ($\mathbb{N}$), comparing ratios ($\mathbb{Q}$), convergent sequences ($\mathbb{R}_{\mathrm{comp}}$), and further strata (the supplied summary is truncated after these). We adopt its stratum list and its historical reading, and supply the formal operator definitions and quantitative loss profiles it calls for.

**[11] QNFO: Embodied Mathematics After Lakoff & Núñez (DOI 10.5281/zenodo.21440894).** This review examines *Where Mathematics Comes From* (Lakoff & Núñez, 2000) from the QNFO perspective, identifying convergence on anti-Platonism, the symbol–concept distinction, and critique of formalism, with extensions including an ultrametric formalization of the four grounding metaphors and a cognitive calculus (summary truncated). It supplies the cognitive grounding our operational reading presupposes: distinction operations are embodied acts (subitizing, containment, path-following), and the ultrametric formalization mentioned in the summary anticipates our $E_4$ stratum, since ultrametrics are exactly the geometry of $p$-adic enclosure.

**[12] QNFO: The Idempotent Core (DOI 10.5281/zenodo.21916939).** A critique-first paper arguing that arithmetic's hidden premise is that $1+1=2$ presupposes two distinguishable marks; that idempotence ($AA=A$) is the primitive law; and that quantity is created distinction, not repetition. It proposes a reconstruction program ($\mathbb{Z}$ from a "!" modality) labeled as conjecture with falsifiability conditions. Our stratum $E_0$ is a formalization of exactly this move: before any tally exists, there is only the mark with $AA = A$, and each act of distinguishing creates one unit of quantity.

## 3. Methods

### 3.1 The mark and the primitive operators

Following [12], we begin with a single primitive object, the *mark* $M$, satisfying the idempotence law
$$M\,M = M.$$
No quantity exists yet; there is only the possibility of distinguishing. A *distinction operation* is an operator $E$ that, applied to a structure $S$, produces the closure of $S$ under a new primitive act. We define six operators:

- $E_0$ (marking): adjoins the act of drawing a mark. The free monoid on one generator under the relation that distinct marks are countable gives $\mathbb{N}$.
- $E_1$ (enclosure/comparison): adjoins the act of enclosing a marked region and comparing two enclosures by ratio. Applied to $\mathbb{N}$, this forces inverses of nonzero elements, giving $\mathbb{Q}$.
- $E_2$ (convergence): adjoins the act of asserting that a Cauchy sequence of enclosures converges. Applied to $\mathbb{Q}$ with an effective (computable) presentation, this gives the computable reals $\mathbb{R}_{\mathrm{comp}}$.
- $E_3$ (lossy projection of a tree): adjoins a projection from a tree-like limit structure (a nested system of enclosures indexed by refinement depth) onto a smooth continuum, deliberately discarding branch information.
- $E_4$ (divisibility enclosure): adjoins, for a fixed prime $p$, the act of distinguishing elements by their $p$-adic depth, giving $\mathbb{Q}_p$.
- $E_5$ (simultaneous valuation): performs $E_4$ for all primes at once, compatibly, giving the adele ring $\mathbb{A}$.

We write $S_{i} = E_i(S_{i-1})$ with $S_{-1} = \{M\}$, so $S_0 = \mathbb{N}$, $S_1 = \mathbb{Q}$, $S_2 = \mathbb{R}_{\mathrm{comp}}$, and so on.

### 3.2 Recovery theorems

**Theorem 1 ($E_0$ recovers $\mathbb{N}$).** The free structure generated by repeatedly applying the act "draw a mark distinct from all previous marks" to the initial mark, with the counting map $n \mapsto$ (number of marks drawn), is isomorphic to $(\mathbb{N}, 0, +1)$.

*Proof.* By construction each application of the act produces a state not previously produced (that is what "distinct from all previous marks" means), so the states are in bijection with application counts $n \in \mathbb{N}$. The successor operation is the act itself. $\square$

**Theorem 2 ($E_1$ recovers $\mathbb{Q}$).** The field of fractions of $\mathbb{N}$-generated additive structure (i.e., of $\mathbb{Z}$) is $\mathbb{Q}$.

*Proof.* Enclosure/comparison is formalized as: given two marked totals $a$ and $b$ with $b \ne 0$, the comparison act produces the pair $(a,b)$, subject to the identification $(a,b) \sim (a',b')$ iff $a b' = a' b$. This is precisely the field-of-fractions construction on $\mathbb{Z}$, whose result is $\mathbb{Q}$. $\square$

**Theorem 3 ($E_2$ recovers $\mathbb{R}_{\mathrm{comp}}$).** The completion of $\mathbb{Q}$ by Cauchy sequences restricted to computable sequences with computable moduli is the ring of computable reals.

*Proof sketch.* A computable real is standardly defined as a computable sequence of rationals $(q_n)_{n \ge 1}$ with $|q_m - q_n| \le 2^{-k}$ whenever $m,n \ge N(k)$ for a computable modulus $N$. This is exactly the closure of $\mathbb{Q}$ under "every effectively convergent sequence has an effective limit." $\square$

The strata $E_3$–$E_5$ we treat at the level of definitions and conjectures, not theorems; this is stated honestly as a limitation (Section 6).

### 3.3 Distinguishability budgets

To compare strata quantitatively we fix a *resource budget* $b$: the number of binary distinctions (bits) an observer may spend. Under each operator we count the number of mutually distinguishable states the operator can produce within budget $b$.

- Tallying ($E_0$): with $b$ binary distinctions one can encode at most the tally counts $0, 1, \ldots, b$ if each bit is spent as "one more mark or stop"—we formalize the tally protocol as: each distinction either adds a mark or terminates, giving $b+1$ states.
- Positional enclosure ($E_1$): each binary distinction is a digit position, giving $2^{b}$ states.
- $p$-adic enclosure ($E_4$) at depth $k$: distinguishing modulo $p^k$ gives $p^{k}$ residue classes; with budget $b$ bits one can address $p^{k}$ classes provided $k \log_2 p \le b$.

The information-loss ratio between adjacent strata is then $\rho_{i}(b) = |D_{i}(b)| / |D_{i-1}(b)|$, where $D_i(b)$ is the distinguishable-state set of stratum $i$ at budget $b$.

## 4. Analysis

We now carry out the explicit derivations. Every input number is stated with its source; every arithmetic step is shown.

**Derivation 1 (tally vs. positional state counts).** Inputs: budget $b = 10$ binary distinctions (chosen as a concrete round value; the derivation is parametric in $b$).

Tally protocol ($E_0$): each of the $b$ distinctions is binary—add a mark, or stop. The number of reachable states is the number of possible stopping points:
$$|D_0(b)| = b + 1.$$
For $b = 10$: $|D_0(10)| = 10 + 1 = 11$.

Positional protocol ($E_1$): each distinction is one bit of a binary string of length $b$, so
$$|D_1(b)| = 2^{b}.$$
For $b = 10$: $2^{10} = 1024$.

Loss ratio:
$$\rho_1(10) = \frac{|D_1(10)|}{|D_0(10)|} = \frac{1024}{11} \approx 93.0909\ldots$$
We compute: $11 \times 93 = 1023$, so $1024/11 = 93 + 1/11 \approx 93.0909$.

In general, $\rho_1(b) = 2^{b}/(b+1)$, which grows exponentially in $b$: the enclosure operator $E_1$ extracts exponentially more distinguishable states from the same budget of binary distinctions than the tally operator $E_0$. This is our first quantitative signature of the claim that strata are *increasingly refined acts of distinction*.

**Derivation 2 ($p$-adic depth budget).** Inputs: prime $p = 2$ (the smallest prime, chosen for concreteness), budget $b = 10$ bits.

The residue ring $\mathbb{Z}/2^{k}\mathbb{Z}$ has $2^{k}$ elements. The budget constraint is $k \log_2 2 \le b$, i.e., $k \le 10$. So the deepest reachable enclosure is $k = 10$, with
$$|D_4(10; p=2)| = 2^{10} = 1024$$
residue classes. For $p = 3$: $k \log_2 3 \le 10$ gives $k \le 10/\log_2 3$. Since $\log_2 3 \approx 1.58496$ (because $2^{1.58496} \approx 3$; more precisely $2^{1.58} = 2.9933\ldots$, $2^{1.585} = 3.0011\ldots$, so $\log_2 3 \in (1.584, 1.585)$), we get $k \le 10/1.58496 \approx 6.309$, hence $k = 6$ and
$$|D_4(10; p=3)| = 3^{6} = 729.$$
Check: $3^{7} = 2187$ and $7 \times 1.58496 = 11.09 > 10$, confirming $k = 6$ is maximal.

**Derivation 3 (number of completions of $\mathbb{Q}$).** Input: Ostrowski's theorem, as invoked in [9], which classifies the nontrivial absolute values on $\mathbb{Q}$ as the real absolute value and the $p$-adic absolute values for each prime $p$. The set of primes is countably infinite (standard; the tally stratum $S_0 = \mathbb{N}$ already supplies infinitely many indices, and the standard enumeration $2, 3, 5, 7, \ldots$ is its image). Therefore the number of inequivalent completions of $\mathbb{Q}$ is
$$1 \;(\text{real}) \;+\; \aleph_0 \;(\text{$p$-adic, one per prime}) \;=\; \aleph_0.$$
This is the formal content of the adelic thesis in [9]: discarding $\mathbb{R}$ alone is not enough; the physically meaningful simultaneous enclosure is the restricted product
$$\mathbb{A} = \mathbb{R} \times \prod_{p}{}' \mathbb{Q}_p,$$
where the restricted product (the prime on $\prod$) means that all but finitely many factors lie in $\mathbb{Z}_p$. The count of channels is $\aleph_0 + 1$, of which the continuum-only observer uses exactly one.

**Derivation 4 (loss of the $E_3$ projection).** The tree-like limit structure preceding $E_3$ can be modeled minimally as the full binary tree of depth $d$. Inputs: branching factor $2$ (binary tree, chosen for minimality), depth $d$ (parametric). The number of leaves is
$$L(d) = 2^{d}.$$
A lossy projection to a smooth continuum that retains only the "leftmost path plus depth" information retains $d + 1$ distinguishable positions (one per level, plus the root), by the same counting as Derivation 1. The loss ratio is
$$\rho_3(d) = \frac{d+1}{2^{d}}.$$
For $d = 10$: $\rho_3(10) = 11/1024 \approx 0.01074$, i.e., the projection discards all but about $1.074 \times 10^{-2}$ of the branch information. Note the structural echo of Derivation 1: the ratio $2^{b}/(b+1)$ appears again, inverted, because $E_3$ is the *lossy* direction of the same distinction asymmetry that $E_1$ exploits.

**Derivation 5 (congruence stratum as filtration).** From [2], the congruence
$$\sum_{k=1}^{p-1}\frac{H_k^2}{k^2} \equiv \frac{4}{5}\,p\,B_{p-5} \pmod{p^2}$$
is a statement resolved at $p$-adic depth $k = 2$. From [7], the analogous conjecture space extends to depth $k = 3$ (modulo $p^3$). The number of residue classes distinguished at depth $k$ is $p^{k}$: for $p = 7$ (the minimum prime in [2]'s theorem), depth $2$ distinguishes $7^{2} = 49$ classes; depth $3$ distinguishes $7^{3} = 343$ classes. The per-depth gain is
$$\frac{7^{3}}{7^{2}} = 7,$$
i.e., each increment of $p$-adic depth multiplies distinguishable classes by exactly $p$—the divisibility enclosure refines distinctions linearly in the exponent, in contrast to the exponential-in-budget growth of the positional enclosure (Derivation 1).

## 5. Results

We report only the quantities computed in Section 4, plus clearly labeled projections.

**R1 (State-count separation, computed).** At budget $b = 10$ binary distinctions: tallying yields $|D_0(10)| = 11$ states; positional enclosure yields $|D_1(10)| = 2^{10} = 1024$ states; the ratio is $\rho_1(10) = 1024/11 \approx 93.09$. Parametrically, $\rho_1(b) = 2^{b}/(b+1)$.

**R2 ($p$-adic budget, computed).** At budget $b = 10$: for $p = 2$, maximal depth $k = 10$ with $2^{10} = 1024$ classes; for $p = 3$, maximal depth $k = 6$ with $3^{6} = 729$ classes (using $\log_2 3 \approx 1.58496$).

**R3 (Completion count, computed).** By Ostrowski's theorem as invoked in [9], $\mathbb{Q}$ has $1 + \aleph_0 = \aleph_0$ inequivalent completions; a continuum-only observer accesses $1$ of them.

**R4 (Tree-projection loss, computed).** For the full binary tree of depth $d = 10$, a leftmost-path-plus-depth projection retains $11$ of $2^{10} = 1024$ leaf-paths' worth of branch information, a retention fraction $\rho_3(10) = 11/1024 \approx 1.074 \times 10^{-2}$.

**R5 (Congruence filtration gain, computed).** At $p = 7$: depth $2$ gives $49$ classes, depth $3$ gives $343$ classes, per-depth gain factor $7$.

**Projection P1 (labeled projection).** *Assumption:* the state-count pattern of R1 extends to the higher strata with each operator $E_i$ extracting at least the positional count $2^{b}$ and strictly more for $i \ge 2$ (since convergence and phase distinctions add continuous families). *Projection:* for $b = 10$, $|D_2(10)| \ge 1024$, with no finite upper bound from the budget alone because a single computable real already encodes an infinite bit stream; we therefore project $|D_2(10)| = \infty$ (countably infinite) under this assumption. *Uncertainty:* this projection depends entirely on the unproven assumption that continuous distinctions are budget-free at the level of state counting; if measurement precision is itself budgeted (each bit of precision costs one distinction), the count collapses back to $2^{b}$, and the correct model is an open question we return to in Section 6.

## 6. Discussion

**Limitations.** The recovery theorems (Theorems 1–3) are elementary; their content is the *uniform reading*, not mathematical novelty. Strata $E_3$–$E_5$ are defined but not proved to recover $\mathbb{C}$, $\mathbb{Q}_p$, and $\mathbb{A}$ in the same strict sense; for $\mathbb{Q}_p$ and $\mathbb{A}$ the recovery is standard mathematics (Ostrowski-type classification, restricted products), but our claim that these arise from "distinction operations" is at present an interpretive identification, not a theorem. The state-count model of Section 3.3 is deliberately crude: it fixes a bit budget and counts reachable states, ignoring cost of composition, error rates, and the observer's dynamics.

**Failure modes.** Three are salient. (i) *Underdetermination:* many distinct operator sequences could generate the same number system; the noncanonical number systems of [6]—where infinitely many digit sets without $0$ give finite expansions for every integer when $|b| \ge 4$—show that even within one stratum the generating act is far from unique. If underdetermination is pervasive, the "the progression is derivable from the acts" claim weakens to "the acts are compatible with the progression," which is much less interesting. (ii) *Circularity:* our counting arguments presuppose $\mathbb{N}$ and $2^{b}$, i.e., presuppose the first stratum while using it to evaluate all strata. A critic can argue the hierarchy is therefore not derivational but descriptive. (iii) *The continuum budget problem:* as flagged in P1, whether continuous distinctions cost budget is exactly the question on which the framework's quantitative content stands or falls; both answers are internally consistent, so the framework currently underdetermines its own key parameter.

**What would falsify the claims.** The central testable claim—that the progression $\mathbb{N} \to \mathbb{Q} \to \mathbb{R} \to \mathbb{C} \to \mathbb{Q}_p \to \mathbb{A}$ is forced by increasingly refined distinction acts—would be falsified by exhibiting a natural distinction operation that generates a number system *outside* the progression (e.g., a field of characteristic $p$ arising from an equally primitive act), or by showing that the same progression arises from operations with no distinction-like reading. The idempotence-first claim of [12]—that $1+1=2$ presupposes distinguishability and that $\mathbb{Z}$ is reconstructible from a "!" modality—is already labeled conjecture with falsifiability conditions in that work; our Theorem 1 inherits those conditions. The adelic thesis of [9]—that the physically accessible base field is $\mathbb{Q}$, with all $p$-adic completions physically meaningful by Ostrowski's theorem—would be falsified by a successful fundamental physics that is genuinely non-adelic, i.e., in which no $p$-adic channel is operative even in principle.

**Against ourselves.** The strongest internal objection is that the hierarchy may be an artifact of *narrative* ordering: we chose the strata after seeing the number systems, then found acts that "generate" them. The congruence literature ([2], [4], [7]) shows the $p$-adic stratum is rich, but richness of a stratum does not show the stratum is *prior* to or *generative of* its objects. Similarly, the stratified $\beta$-numbers of [3] give a rigorous scale-by-scale enclosure theory in the Carnot setting, but importing that rigor into our $E_3$ is future work, not an accomplished analogy. Finally, the cognitive grounding from [11]—anti-Platonism, the symbol–concept distinction, ultrametric formalization of grounding metaphors—supports the *plausibility* of operational origins but does not constrain the mathematics; a formalist could accept every theorem here and reject the operational story wholesale.

**Open questions.** (1) Can $E_3$ be given a definition, modeled on scale-by-scale enclosure statistics as in [3], under which "lossy projection of a tree recovers the continuum" becomes a theorem? (2) Is there a natural category whose objects are the strata $S_{-1}, \ldots, S_5$ and whose morphisms record exactly the loss ratios $\rho_i$ computed here? (3) Does the per-depth gain factor $p$ (R5) versus the exponential-in-budget gain $2^{b}$ (R1) reflect a genuine dichotomy between archimedean and non-archimedean refinement, or an artifact of the budget model? (4) What is the correct budgeted model of continuous distinction (P1)?

## 7. Conclusion

We have sketched a stratified hierarchy of distinction operations over a Laws-of-Form-style mark, formalized the first three strata with elementary recovery theorems, defined the remaining three, and computed explicit distinguishability and information-loss profiles: an exponential separation $\rho_1(b) = 2^{b}/(b+1)$ between tallying and positional enclosure ($\approx 93.09$ at $b = 10$), a per-depth multiplicative gain $p$ in the congruence stratum, a retention fraction $\approx 1.074 \times 10^{-2}$ for the lossy tree-to-continuum projection at depth $10$, and a count of $\aleph_0$ completions of $\mathbb{Q}$ under Ostrowski's theorem as invoked in the adelic physics program. The framework builds directly on the measurement-stratigraphy program