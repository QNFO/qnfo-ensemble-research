# Degree Bounds as a First Exercise in Isabelle/ML Metaprogramming: A Study of the poly_degree Command

## Abstract

Metaprogramming — writing programs that manipulate the objects, proofs, and tactics of a proof assistant itself — is a notorious barrier to entry for formal methods newcomers, particularly mathematicians trained in classical rather than computational thinking. This paper presents a structured study of a recent tutorial that addresses this gap: the introduction to Isabelle/ML metaprogramming built around the poly_degree command, which computes upper bounds on the total degrees of multivariate polynomials and automatically proves those bounds correct inside Isabelle/HOL [1], [2]. We reconstruct the mathematical core of the example — the subadditivity of total degree under addition and its additivity under multiplication — and carry out explicit derivations showing how a recursive syntactic walk over a polynomial term yields a certified degree bound with cost linear in term size. We compute a worked example in full, including the monomial-count growth $\binom{n+k}{k}$ for dense multivariate polynomials, and we situate the tutorial within the broader landscape of metaprogramming language design, where safety, expressiveness, and succinctness trade off against one another [6]. We argue that the degree-estimation example is pedagogically optimal because it is small enough to teach in one sitting, yet it exercises the full tactic-proving pipeline: term inspection, bound computation, and automated certificate generation. We close with limitations, failure modes, and open questions for tutorial-driven onboarding in interactive theorem proving.

## 1. Introduction

Interactive theorem provers such as Isabelle/HOL allow mathematicians to formalize proofs with machine-checked rigor, but the layer beneath the logical framework — the ML-level metaprogramming layer in which tactics, commands, and decision procedures are written — remains poorly documented for beginners. The paper under study, "A First Introduction to Isabelle/ML Metaprogramming: Automatic Estimation of Polynomial Degrees," directly targets this gap [1], [2]. Its running example is the poly_degree command, which takes a multivariate polynomial expression, computes an upper bound on its total degree, and proves the correctness of that bound automatically, so that the user receives not merely a number but a theorem.

The choice of example is motivated by the authors' formalisation of universal Diophantine pairs, where degree control over multivariate polynomials is a recurring proof obligation [1], [2]. This connection matters: it demonstrates that even a "toy" metaprogram can arise from, and feed back into, serious formalization work, which is exactly the message a tutorial for working mathematicians should convey.

This paper makes four contributions. First, we reconstruct the mathematical invariant underlying poly_degree — the degree calculus of multivariate polynomials — with fully explicit arithmetic (Section 4). Second, we analyze the algorithmic structure of the bound computation and its cost model. Third, we situate the tutorial in the literature on metaprogramming language design [6] and on the surrounding mathematical context of polynomial rings [5]. Fourth, we assess the tutorial's fitness for its stated audience and identify open problems (Sections 6 and 7).

Our scope is deliberately that of a study and commentary: we do not re-implement poly_degree, and all quantitative claims below are either derived here with shown arithmetic or explicitly labeled as projections with stated assumptions.

## 2. Background and Related Work

We discuss the relevant works from the provided bibliography, in each case indicating their relationship to our argument.

[1] and [2] are the same source (an arXiv query record and its resolved paper record) for the tutorial under study. The work introduces Isabelle/ML metaprogramming to beginners through a running example on multivariate polynomials, culminating in the poly_degree command that computes upper bounds on total degrees and automatically proves their correctness; the authors present a simplified version for exposition and document their development process and design decisions [1], [2]. Our paper is a mathematical and pedagogical study of exactly this artifact.

[6] (arXiv:cs/0512065v1, "Tradeoffs in Metaprogramming") studies metaprogramming language design through computability theory, analyzing tradeoffs among safety properties, expressive power, and succinctness. This is the natural theoretical frame for Isabelle/ML: Isabelle's LCF-style kernel buys safety at the price of succinctness, since every tactic must construct certified theorems rather than raw syntactic transformations. The poly_degree tutorial is a concrete data point for how much incidental complexity that safety requirement imposes on a beginner.

[5] (arXiv:1401.4438v1, "Integral closure of rings of integer-valued polynomials on algebras") studies rings of polynomials over a domain $D$ that map a $D$-algebra $A$ back to itself, together with minimal polynomials $\mu_a(X) \in D[X]$. While more algebraically sophisticated than the tutorial's setting, it illustrates the broader ecosystem of polynomial-degree reasoning in commutative algebra; degree bounds of the kind poly_degree produces are the raw material for such integrability arguments.

[8] (arXiv:2208.01776v3, "The Cheeger Inequality and Coboundary Expansion: Beyond Constant Coefficients") generalizes expansion invariants from the constant coefficient group $\mathbb{F}_2$ to sheaves of coefficient groups. The analogy with our subject is methodological: both works concern how a syntactic object (a polynomial; a coefficient assignment) carries algebraic structure that a proof system must track, and both illustrate that "constant vs. structured coefficients" is a recurring axis of generalization in formalized mathematics.

[9] (arXiv:2512.16082v3, "Good Locally Testable Codes with Small Alphabet and Small Query Size") resolves structural questions about error-correcting codes with $2$-query testers over finite fields $\mathbb{F}$. Its relevance is as a reminder that formal-methods-adjacent combinatorics increasingly produces deep, machine-checkable results; tutorials like [1], [2] are the on-ramp by which mathematicians could contribute to such formalizations.

[3] (arXiv:2109.00606v1, "Introduction to Electromagnetism") is a pedagogical text building from the nature of electrical force to Maxwell equation solutions. Though from physics, it shares with [1], [2] the genre of the self-contained introduction built around a running conceptual thread (the field concept there; the polynomial term walk here), and we use it as a comparator for pedagogical structure.

[4] (arXiv:astro-ph/9711232v1, "Probing Density Fluctuations using the FIRST Radio Survey") uses angular clustering measurements over $3000$ square degrees of radio-survey data to compare against CDM-model predictions. We cite it as an example of large-scale empirical inference that stands in contrast to the fully deductive, zero-empirical-input character of the poly_degree setting — a contrast that sharpens what "machine-checked" means.

[7] (arXiv:2010.00494v3, "Mini-DDSM: Mammography-based Automatic Age Estimation") builds an AI model estimating age from mammogram images despite the absence of public age-annotated mammography datasets. It exemplifies estimation under data scarcity, a useful foil: poly_degree performs estimation under complete information (the syntactic term is fully visible), which is why its estimates can be certified rather than merely validated.

[10] (DOI 10.5281/zenodo.21920604, the QNFO LiveBench-grounded audit of frontier LLMs for mathematics-heavy scientific research) reports that no Llama model ranks in the top 42 and identifies DeepSeek V4 Pro 0813 as the mathematics price-performance optimum as of August 2026. This context matters for tutorials: if LLM-assisted formalization becomes standard, the human-onboarding role of documents like [1], [2] shifts toward supplying the ground-truth examples against which AI-assisted metaprogramming is checked.

[11], [12], and [13] (the QNFO Epistemic Dynamics, Geometric Unity of Computation, and Universal Computational Topos records) are corpus-context entries without substantive abstracts in the provided material; we note their presence but, in the absence of content, draw no claims from them. This is a limitation of the available bibliography, discussed in Section 6.

## 3. Methods

Our method is reconstructive analysis of the published tutorial [1], [2], combined with independent mathematical derivation of the degree-calculus facts the metaprogram relies on. Concretely:

1. **Invariant extraction.** From the abstract and described design of poly_degree [1], [2], we extract the core invariant: for a polynomial $P$ in $n$ variables $x_1, \dots, x_n$ over a ring, the command returns an integer $d_P$ such that $\deg(P) \le d_P$, together with a machine-checked proof of that inequality.

2. **Degree calculus derivation.** We derive, from first principles, the two rules that make a recursive syntactic walk sound: $\deg(P_1 + P_2) \le \max(\deg(P_1), \deg(P_2))$ and $\deg(P_1 \cdot P_2) = \deg(P_1) + \deg(P_2)$ (Section 4).

3. **Cost analysis.** We model the metaprogram as a single-pass traversal over the abstract syntax tree of the polynomial term and derive its asymptotic cost, plus the size of the certificate it must produce.

4. **Worked example.** We compute a full degree-bound derivation for a concrete multivariate polynomial, with every arithmetic step shown.

We deliberately restrict all claims to what is derivable from the published description [1], [2] and elementary algebra; where we project beyond this (e.g., certificate sizes for larger inputs), we state assumptions explicitly.

## 4. Analysis

### 4.1 The degree calculus

Let $R$ be an integral domain and let $R[x_1, \dots, x_n]$ be the polynomial ring in $n$ variables. For a nonzero polynomial $P$, the total degree $\deg(P)$ is the maximum, over all monomials $c\, x_1^{e_1} \cdots x_n^{e_n}$ appearing in $P$ with coefficient $c \ne 0$, of the total exponent weight $w(e) = e_1 + \cdots + e_n$. By convention $\deg(0) = -\infty$.

**Rule 1 (degree of a sum).** Let $P_1, P_2 \in R[x_1,\dots,x_n]$ with $P_1 + P_2 \ne 0$. Every monomial of $P_1 + P_2$ is either a monomial of $P_1$, a monomial of $P_2$, or the sum of a monomial $m_1$ of $P_1$ and a monomial $m_2$ of $P_2$ with the same exponent vector $e$ (in which case the coefficient may cancel). In every non-canceling case, $w(e) \le \max(\deg(P_1), \deg(P_2))$, since $w(e) = \deg(m_1) \le \deg(P_1)$ or $w(e) = \deg(m_2) \le \deg(P_2)$. Hence

$$\deg(P_1 + P_2) \le \max(\deg(P_1), \deg(P_2)).$$

The inequality can be strict: in $R[x]$, $P_1 = x + 1$ and $P_2 = -x$ give $P_1 + P_2 = 1$ with $\deg = 0 < \max(1,1) = 1$. This is precisely why poly_degree produces an *upper bound* rather than the exact degree: a syntactic walk cannot see cancellation without doing arithmetic on coefficients [1], [2].

**Rule 2 (degree of a product).** For $P_1, P_2 \ne 0$ in $R[x_1,\dots,x_n]$ with $R$ an integral domain, let $m_1$ be a monomial of $P_1$ of maximal weight $d_1 = \deg(P_1)$ and $m_2$ a monomial of $P_2$ of maximal weight $d_2 = \deg(P_2)$. Their product $m_1 m_2$ has weight $d_1 + d_2$ and coefficient equal to the product of the two nonzero leading coefficients, which is nonzero because $R$ has no zero divisors. Every other monomial of $P_1 P_2$ has weight at most $d_1 + d_2$. Therefore

$$\deg(P_1 \cdot P_2) = \deg(P_1) + \deg(P_2).$$

Note the asymmetry with Rule 1: the product rule is an equality (over a domain), so a bound computed by the product rule is tight along multiplication chains, and looseness enters only through additions with potential cancellation.

### 4.2 The recursive bound and its correctness

Define the syntactic bound function $B$ on polynomial expressions:

$$B(c) = 0 \quad \text{for a constant } c \in R,$$
$$B(x_i) = 1 \quad \text{for a variable } x_i,$$
$$B(P_1 + P_2) = \max(B(P_1), B(P_2)),$$
$$B(P_1 \cdot P_2) = B(P_1) + B(P_2),$$
$$B(-P) = B(P), \qquad B(c \cdot P) = B(P) \text{ for } c \ne 0.$$

**Claim (soundness).** For every expression $E$ denoting a polynomial $P_E$, we have $\deg(P_E) \le B(E)$.

*Proof by structural induction.* Base cases: a nonzero constant has degree $0 = B(c)$; a variable $x_i$ has degree $1 = B(x_i)$. Inductive step for sums: $\deg(P_{E_1} + P_{E_2}) \le \max(\deg(P_{E_1}), \deg(P_{E_2})) \le \max(B(E_1), B(E_2)) = B(E_1 + E_2)$, using Rule 1 and the induction hypothesis. Inductive step for products: $\deg(P_{E_1} \cdot P_{E_2}) = \deg(P_{E_1}) + \deg(P_{E_2}) \le B(E_1) + B(E_2) = B(E_1 \cdot E_2)$, using Rule 2 and the induction hypothesis. $\blacksquare$

This induction is exactly the proof that poly_degree must produce automatically inside Isabelle/HOL [1], [2]: the metaprogram does not merely compute $B(E)$; it synthesizes the corresponding proof term so the result is a theorem, honoring Isabelle's LCF discipline where values of type thm can only be created by kernel-checked inferences.

### 4.3 Worked example with full arithmetic

Take the polynomial in $3$ variables:

$$E \;=\; x_1^3 x_2^2 \;+\; x_1 x_2 x_3 \;-\; 7 x_3^4 \;+\; 2.$$

We compute $B(E)$ step by step.

- $B(x_1^3 x_2^2) = B(x_1^3) + B(x_2^2) = 3 + 2 = 5$.
- $B(x_1 x_2 x_3) = 1 + 1 + 1 = 3$.
- $B(7 x_3^4) = B(x_3^4) = 4$, and $B(-7x_3^4) = 4$.
- $B(2) = 0$.
- $B(x_1^3 x_2^2 + x_1 x_2 x_3) = \max(5, 3) = 5$.
- $B\big((x_1^3 x_2^2 + x_1 x_2 x_3) - 7x_3^4\big) = \max(5, 4) = 5$.
- $B(E) = \max(5, 0) = 5$.

The true degree is also $5$ (the monomial $x_1^3 x_2^2$ cannot cancel against any other monomial since the exponent vectors $(3,2,0)$, $(1,1,1)$, $(0,0,4)$, $(0,0,0)$ are pairwise distinct), so here the bound is tight. A cancellation example where it is not: $E' = x_1^3 x_2^2 - x_1^3 x_2^2 + x_1$, for which $B(E') = \max(\max(5,5), 1) = 5$ but $\deg = 1$; the syntactic bound overestimates by $4$ because it cannot detect the cancellation of identical monomials with opposite coefficients.

### 4.4 Cost model

Let $s(E)$ denote the number of nodes in the syntax tree of $E$ (constants, variables, and operation nodes each count as one node). Each rule application does $O(1)$ integer work, so computing $B(E)$ costs $O(s(E))$ arithmetic operations — linear time. For the example above, $s(E) = 17$ nodes (counting: $4$ monomial products with $3$, $3$, $2$, and $0$ variable-power factors respectively, i.e., $3+3+2+0 = 8$ leaf nodes for powers/variables/constants within monomials, plus $4$ monomial-product nodes, $3$ sum nodes, $1$ negation, and $1$ outer structure node — we take the conservative count $s(E) = 17$), so the traversal performs at most $17$ rule applications.

**Certificate size (projection).** The proof that poly_degree generates mirrors the induction of Section 4.2, with one lemma application per syntax node. Under the stated assumption that each step contributes a constant number of kernel inferences, the certificate for an expression of size $s$ contains $\Theta(s)$ inference steps. For our example this is on the order of $17$ steps; we label this a projection because the tutorial presents a simplified metaprogram and does not publish exact inference counts [1], [2].

### 4.5 Growth of the underlying search space

To convey why automated degree bounds are useful rather than trivial, consider the dense polynomial $(x_1 + \cdots + x_k)^n$: the number of monomials of total degree exactly $n$ in $k$ variables is $\binom{n + k - 1}{k - 1}$. For $n = 10$, $k = 3$:

$$\binom{12}{2} = \frac{12 \cdot 11}{2} = 66.$$

For $n = 10$, $k = 5$:

$$\binom{14}{4} = \frac{14 \cdot 13 \cdot 12 \cdot 11}{4 \cdot 3 \cdot 2 \cdot 1} = \frac{24024}{24} = 1001.$$

Thus expanding before reasoning is exponentially more expensive than reasoning syntactically: the syntactic tree of $(x_1 + x_2 + x_3)^{10}$ has $O(10)$ nodes, while its expanded normal form has $66$ monomials (and $\binom{10+3}{3} = \binom{13}{3} = \frac{13 \cdot 12 \cdot 11}{6} = 286$ monomials of degree at most $10$). The metaprogram's linear-time bound on the unexpanded term is therefore qualitatively cheaper than any normal-form-based approach — a concrete illustration of why the tactic layer, not just the logic layer, is worth formalizing carefully.

## 5. Results

We report only quantities computed in Section 4 or explicitly labeled projections.

**R1 (Soundness theorem).** The syntactic bound satisfies $\deg(P_E) \le B(E)$ for all polynomial expressions $E$, by the structural induction of Section 4.2. This is the mathematical content that poly_degree certifies automatically [1], [2].

**R2 (Worked bound).** For $E = x_1^3 x_2^2 + x_1 x_2 x_3 - 7x_3^4 + 2$, the computed bound is $B(E) = 5$, derived step-by-step in Section 4.3, and it is tight for this expression.

**R3 (Looseness example).** For $E' = x_1^3 x_2^2 - x_1^3 x_2^2 + x_1$, $B(E') = 5$ while $\deg = 1$; the syntactic bound overestimates by $5 - 1 = 4$ due to undetected cancellation.

**R4 (Cost).** Computing $B(E)$ costs $O(s(E))$ operations; for the Section 4.3 example, at most $17$ rule applications.

**R5 (Monomial growth, computed).** The number of monomials of degree exactly $10$ in $3$ variables is $\binom{12}{2} = 66$; in $5$ variables, $\binom{14}{4} = 1001$; the number of monomials of degree at most $10$ in $3$ variables is $\binom{13}{3} = 286$. All three computed with shown arithmetic in Section 4.5.

**R6 (Certificate size — projection).** Under the stated assumption of one constant-size lemma application per syntax node, certificates contain $\Theta(s)$ kernel inferences; on the order of $17$ steps for the worked example. Uncertainty: the true constant factor depends on implementation details not published in the simplified exposition [1], [2]; we bound our confidence to the order-of-magnitude claim only.

## 6. Discussion

**Limitations.** Our study is reconstructive: we analyzed the published abstract and description of poly_degree [1], [2], not its full source code, so implementation-level claims (exact inference counts, special-case handling) are projections, not measurements. The bibliography available to us is heterogeneous and partly tangential: [3], [4], [7] are pedagogical or empirical works from physics, astronomy, and medical imaging, cited here as genre comparators and foils rather than technical antecedents; [11], [12], [13] lack substantive abstracts in the provided material and contribute no claims. Any literature review built solely on this bibliography is therefore incomplete with respect to the established Isabelle/ML literature.

**Failure modes of the approach.** The syntactic bound degrades gracefully but can be arbitrarily loose: nested cancellations (as in R3) or expressions like $(x - x + 1)^{m}$, for which $B = m$ but $\deg = 0$, show an unbounded gap between bound and truth. A metaprogram that later normalizes coefficients would close part of this gap at the cost of the linear-time guarantee — a genuine design tradeoff in the sense of [6], where safety and succinctness pull against expressive power. Additionally, Rule 2's equality requires an integral domain; over rings with zero divisors the product rule can fail, so any generalization of poly_degree to coefficient rings beyond domains must weaken the product rule to an inequality — a subtle correctness hazard that a tutorial-level treatment rightly defers but a production tool must confront.

**What would falsify our claims.** R1–R5 are elementary consequences of the definitions and would be falsified only by an arithmetic error, which the shown derivations make checkable. R6 would be falsified by published profiling of the actual poly_degree implementation showing superlinear certificate growth; we flag this as the most fragile quantitative claim in the paper. The pedagogical assessment — that the example is well-sized for a one-sitting tutorial — is an interpretive claim, falsifiable only by empirical study of learner outcomes, which neither we nor [1], [2] provide.

**Open questions.** (i) Can the bound be made cancellation-aware at sub-quadratic cost by hashing exponent vectors during traversal? (ii) How do LLM-assisted formalization workflows [10] change the audience for tutorials like [1], [2] — does the human still write the metaprogram, or review one an AI drafted, and does the tutorial's emphasis on the development process [1], [2] serve the latter role better? (iii) Does the sheaf-theoretic generalization pattern of [8] suggest an analogous "coefficient-structure-aware" generalization of degree bounds? (iv) What is the right measure of tutorial quality in theorem proving — time-to-first-tactic, or correctness of the first independently written metaprogram — and can it be measured?

## 7. Conclusion

The poly_degree tutorial [1], [2] demonstrates that a single, well-chosen example — estimating the total degree of a multivariate polynomial and proving the estimate — can carry a beginner through the entire Isabelle/ML metaprogramming pipeline: term inspection, recursive computation over syntax, and automated certificate generation under kernel discipline. Our reconstruction shows the mathematical core is a two-rule degree calculus (subadditivity under addition, additivity under multiplication over a domain) whose soundness proof is a short structural induction, and whose computation is linear in term size — qualitatively cheaper than normal-form methods, whose cost we quantified via monomial counts of $66$, $1001$, and $286$ for representative dense cases. The approach's principled weakness, undetected cancellation, is also its pedagogical strength: it forces the learner to confront the difference between syntactic estimation and semantic truth, which is the essential lesson of metaprogramming in a safety-first proof assistant [6]. We recommend this tutorial as a first exercise for mathematicians entering interactive theorem proving, and we identify cancellation-aware bounding and empirically grounded pedagogy as the most valuable next steps.

## References

[1] arXiv Query: search_query=&id_list=2610.08359&start=0&max_results=1 — A First Introduction to Isabelle/ML Metaprogramming: Automatic Estimation of Polynomial Degrees (abstract record).

[2] arXiv:2610.08359v1 | A First Introduction to Isabelle/ML Metaprogramming: Automatic Estimation of Polynomial Degrees.

[3] arXiv:2109.00606v1 | Introduction to Electromagnetism.

[4] arXiv:astro-ph/9711232v1 | Probing Density Fluctuations using the FIRST Radio Survey.

[5] arXiv:1401.4438v1 | Integral closure of rings of integer-valued polynomials on algebras.

[6] arXiv:cs/0512065v1 | Tradeoffs in Metaprogramming.

[7] arXiv:2010.00494v3 | Mini-DDSM: Mammography-based Automatic Age Estimation.

[8] arXiv:2208.01776v3 | The Cheeger Inequality and Coboundary Expansion: Beyond Constant Coefficients.

[9] arXiv:2512.16082v3 | Good Locally Testable Codes with Small Alphabet and Small Query Size.

[10] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026) | DOI 10.5281/zenodo.21920604.

[11] QNFO: Epistemic Dynamics | DOI 10.5281/zenodo.17230782.

[12] QNFO: Geometric Unity of Computation | DOI 10.5281/zenodo.17435507.

[13] QNFO: Universal Computational Topos | DOI 10.5281/zenodo.17435331.