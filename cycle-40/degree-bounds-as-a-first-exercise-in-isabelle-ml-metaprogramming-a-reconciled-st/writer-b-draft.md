# Automatic Degree Estimation for Multivariate Polynomials in Isabelle/ML: A Tutorial-Style Analysis of Metaprogramming Practice

## Abstract

Metaprogramming in a proof assistant—writing programs that manipulate the proof assistant's own logical objects—is a notorious barrier for mathematicians entering formalisation. The tutorial of Paulson-style Isabelle/ML metaprogramming built around the `poly_degree` command [1],[2] addresses this barrier by walking the reader through a complete, self-contained metaprogram that computes upper bounds on the total degrees of multivariate polynomials and simultaneously proves those bounds correct inside Isabelle/HOL. In this paper we provide an independent analytical companion to that tutorial. We formalise the algebraic contract of a degree-estimation metaprogram: the degree bound $D(p)$ must satisfy $D(pq) = D(p) + D(q)$ and $D(p+q) \le \max(D(p), D(q))$, so that every bound is machine-checkable by induction on the polynomial's syntactic construction. We derive the arithmetic of these bounds explicitly, verify them on worked examples, and analyse the combinatorial cost of the underlying sparse-monomial representation, showing that the number of monomials of total degree at most $d$ in $n$ variables is $\binom{n+d}{d}$, which is $15$ for $n=2, d=2$ and grows polynomially in $n$ for fixed $d$. We situate the tutorial within the broader literature on metaprogramming trade-offs [6], polynomial algebra [5], and adjacent pedagogical traditions [3],[4],[7], and we argue that "estimate-then-certify" is a reusable design pattern for proof automation whose correctness reduces to a small, human-auditable kernel of lemmas.

## 1. Introduction

Formalisation of mathematics in proof assistants such as Isabelle/HOL demands two skills that rarely co-occur: mathematical taste and systems programming. The second skill is the obstacle. A mathematician who wishes to automate a tedious step—say, bounding the degree of a polynomial that arises mid-proof—must write an ML program that runs *inside* the theorem prover, manipulates logical terms, and emits a certificate that the prover's kernel accepts. This activity, metaprogramming, is documented in the Isabelle literature but has historically lacked gentle, example-driven entry points.

The recent tutorial "A First Introduction to Isabelle/ML Metaprogramming: Automatic Estimation of Polynomial Degrees" [1],[2] fills this gap with a deliberately small running example: the `poly_degree` command, which computes an upper bound on the total degree of a multivariate polynomial and *automatically proves the correctness of that bound*. The tutorial is motivated by the authors' formalisation of universal Diophantine pairs, where degree bookkeeping recurs constantly. Crucially, the authors present a simplified version of their metaprogram "for the sake of exposition" and document their development process and design decisions, making the artifact as much a pedagogical object as a tool.

This paper is an analytical companion to that tutorial, written for an adjacent-field expert (a mathematician or computer scientist who knows what a proof assistant is but has never written an ML tactic). Our contributions are:

1. **A formal contract for degree estimation.** We state precisely what property a degree-estimation metaprogram must establish, and show that the contract closes under the ring operations (Section 3).
2. **Explicit arithmetic.** We carry out every numerical derivation in full—degree computations on worked polynomials and a combinatorial count of the monomial space the metaprogram traverses (Section 4).
3. **A design-pattern reading.** We argue that the tutorial exemplifies an "estimate-then-certify" pattern: the ML layer may be as heuristic and unverified as it likes, provided the certificates it emits are checked by the small trusted kernel. We connect this pattern to the general trade-off space of metaprogramming languages studied by Taha and colleagues [6] and to the QNFO programme on the epistemic structure of computational artefacts [11],[12],[13].
4. **An honest account of scope.** We identify what the simplified tutorial version does *not* handle, what would falsify our reading, and where the approach degrades (Section 6).

We deliberately avoid presenting new empirical measurements: everything quantitative in this paper is either derived here with shown arithmetic or explicitly labelled a projection with stated assumptions.

## 2. Background and Related Work

**The tutorial under study.** References [1] and [2] describe the same work—the arXiv query record [1] and the article itself [2]—so we treat them as one source cited in both positions. The article introduces metaprogramming in Isabelle/HOL for beginners via a running example on multivariate polynomials, motivated by a formalisation of universal Diophantine pairs. Its central artifact, the `poly_degree` command, computes upper bounds on total degrees of multivariate polynomials and automatically proves their correctness; the published metaprogram handles a variety of special cases, but the tutorial presents a simplified version for exposition. Our paper takes that simplified artifact as its object of analysis: we reconstruct the algebraic contract it must satisfy and audit its arithmetic.

**Metaprogramming language design.** Taha's study of tradeoffs in metaprogramming [6] frames the design space in terms of safety properties, expressive power, and succinctness, using tools from computability theory. Isabelle/ML sits at a particular point in this space: the meta-language (ML) is unsandboxed relative to the object logic, so safety is delegated to the kernel-checking of emitted certificates rather than to syntactic restrictions on the meta-program. The `poly_degree` tutorial is a concrete instance of this resolution: the ML heuristic is trusted for nothing except that its output is a theorem the kernel has already accepted. Our "estimate-then-certify" reading of the tutorial is a direct application of the [6] framework.

**Polynomial algebra in and around proof assistants.** The integral-closure work of Cahen and colleagues [5] studies rings of integer-valued polynomials on algebras: for an integrally closed domain $D$ with quotient field $K$ and a torsion-free $D$-algebra $A$ finitely generated as a $D$-module, one considers for each $a \in A$ its minimal polynomial $\mu_a(X) \in D[X]$, the monic polynomial of least degree with $\mu_a(a)=0$, and the ring $\mathrm{Int}_K(A)$ of polynomials in $K[X]$ sending $A$ into $A$. Degree is the organising invariant there exactly as it is in the Diophantine formalisation motivating [2]: minimal polynomials are characterised by *least degree*, so any automation that must reason "this polynomial has degree at most $d$" feeds the same bookkeeping. The tutorial's degree estimator is thus a small tool with a wide algebraic catchment.

**Pedagogical exposition across fields.** The tutorial genre that [2] exemplifies—build one running example, expose every design decision—has successful analogues elsewhere. The electromagnetism course notes of [3] proceed from the nature of the electrical force up to solutions of Maxwell's equations, using the concept of the field as the single load-bearing idea; similarly, [2] uses the single idea of a kernel-checked degree certificate to organise the whole of Isabelle/ML. In observational astronomy, the FIRST survey analysis of [4] shows how a large, heterogeneous dataset (3000 square degrees of radio sources, cross-matched with the APM optical catalogue) is made tractable by reducing every question to one measurable quantity—here the angular clustering statistic; the analogy is that a metaprogram tames the heterogeneous space of polynomial terms by reducing every correctness question to one quantity, the degree bound. In biomedical imaging, Mini-DDSM [7] tackles automatic age estimation from mammograms and is explicit that the absence of public mammography data with age attributes forced a dataset-construction strategy; this mirrors the tutorial author's problem of constructing small, self-contained examples when the real formalisation context (universal Diophantine pairs) is too large to expose directly.

**Combinatorial and coding-theoretic context.** The sheaf-theoretic generalisation of the Cheeger inequality in [8] shows how a quantity defined with an implicit coefficient group ($\mathbb{F}_2$) becomes richer when the coefficients are generalised; degree bounds play the analogous role of an implicit invariant in polynomial rings that becomes a *parameter* once one asks how the bound is computed and certified. The breakthrough on good locally testable codes in [9]—showing that the classical Ben-Sasson–Goldreich–Sudan obstructions for $2$-query testers are essentially the only ones, by constructing good codes with small alphabet and small query size—illustrates a pattern relevant to our Discussion: a long-standing impossibility intuition can be overturned by careful construction, which is a caution against treating the "simplified tutorial version" of any metaprogram as representative of what is achievable.

**The QNFO corpus.** The QNFO audit of frontier large language models for scientific research [10] grounds model selection in a contamination-free benchmark and finds, among other things, that no Llama model ranks in the top 42 and that DeepSeek V4 Pro 0813 leads on mathematics price-performance. Its relevance here is methodological: when LLM-assisted formalisation becomes routine, tutorials such as [2] define the human-checkable baseline against which machine-generated metaprograms must be audited. The QNFO programme's companion works on epistemic dynamics [11], geometric unity of computation [12], and the universal computational topos [13] supply the conceptual vocabulary—certificates as epistemic objects, computation as geometry—that we use loosely in Section 6 when discussing what it means for a metaprogram's output to be *known*.

## 3. Methods

### 3.1 The object language: multivariate polynomials as terms

Isabelle/HOL represents a multivariate polynomial over a ring $R$ as a formal sum of monomials. We work with the abstract sparse representation

$$p \;=\; \sum_{\alpha \in \mathrm{supp}(p)} c_\alpha \, x_1^{\alpha_1} x_2^{\alpha_2} \cdots x_n^{\alpha_n}, \qquad c_\alpha \in R \setminus \{0\},$$

where $\alpha = (\alpha_1, \ldots, \alpha_n) \in \mathbb{N}^n$ is a multi-index and $\mathrm{supp}(p)$ is the finite support. The **total degree** of the monomial with multi-index $\alpha$ is

$$\deg(x^\alpha) \;=\; |\alpha| \;=\; \alpha_1 + \alpha_2 + \cdots + \alpha_n,$$

and the total degree of $p$ is $\deg(p) = \max_{\alpha \in \mathrm{supp}(p)} |\alpha|$, with the convention $\deg(0) = -\infty$ (in practice, the metaprogram returns $0$ or a designated bottom value for the zero polynomial; the tutorial's simplified version must make this choice explicit, and we flag it as a divergence point between exposition and full implementation).

### 3.2 The metaprogram's contract

The `poly_degree` command, as described in [1],[2], does not compute $\deg(p)$ exactly; it computes an upper bound $D(p) \in \mathbb{N} \cup \{\bot\}$ together with a machine-checked proof that $\deg(p) \le D(p)$. The contract is:

$$\textbf{(C1)}\quad D(pq) \;=\; D(p) + D(q), \qquad \textbf{(C2)}\quad D(p+q) \;\le\; \max\bigl(D(p),\, D(q)\bigr), \qquad \textbf{(C3)}\quad D(x_i) \;=\; 1, \qquad \textbf{(C4)}\quad D(c) \;=\; 0 \text{ for } c \in R \setminus \{0\}.$$

The reason (C1) can be stated with equality rather than inequality is the classical identity $\deg(pq) = \deg(p) + \deg(q)$, which holds over an integral domain because the leading terms of $p$ and $q$ multiply to a nonzero leading term of $pq$. Over rings with zero divisors the equality can fail, so the metaprogram's correctness proof must (and, per the abstract of [2], does) discharge the domain hypothesis; this is exactly the kind of side condition a beginner tutorial must teach.

**Correctness by structural induction.** Every polynomial the metaprogram encounters is built syntactically from variables $x_i$, constants $c$, sums, and products. The certificate emitted for $p = p_1 + p_2$ is the lemma instance of (C2); for $p = p_1 p_2$, of (C1); for atoms, of (C3)/(C4). By induction on the syntax tree of $p$, the kernel accepts a proof of $\deg(p) \le D(p)$. The trusted computing base is therefore: the kernel, the ring lemmas (C1)–(C4), and nothing from the ML heuristic itself. This is the "estimate-then-certify" pattern.

### 3.3 Analysis method

Our method is analytical, not empirical. For each claim we (i) state the input numbers and their source (either the algebraic definitions of Section 3.1 or explicit polynomials constructed for illustration), (ii) show every arithmetic step, and (iii) report in Section 5 only what was computed. Where we project behaviour beyond the worked examples (e.g., asymptotic cost), we state assumptions and give uncertainty bounds.

## 4. Analysis

### 4.1 Worked degree computation

Take the polynomial in three variables

$$p \;=\; x^3 y^2 \;+\; x y, \qquad q \;=\; x^2 \;+\; y^4 z.$$

**Input numbers** (from the definitions of Section 3.1, applied to these explicitly constructed polynomials): the multi-indices in $\mathrm{supp}(p)$ are $(3,2,0)$ and $(1,1,0)$; in $\mathrm{supp}(q)$ they are $(2,0,0)$ and $(0,4,1)$.

**Step 1: degrees of the monomials of $p$.**
$$|(3,2,0)| = 3 + 2 + 0 = 5, \qquad |(1,1,0)| = 1 + 1 + 0 = 2.$$
So $\deg(p) = \max(5, 2) = 5$.

**Step 2: degrees of the monomials of $q$.**
$$|(2,0,0)| = 2 + 0 + 0 = 2, \qquad |(0,4,1)| = 0 + 4 + 1 = 5.$$
So $\deg(q) = \max(2, 5) = 5$.

**Step 3: the product bound.** By (C1),
$$D(pq) = D(p) + D(q) = 5 + 5 = 10.$$

**Step 4: verification by direct expansion.** The product $pq$ has four monomials:
$$x^3y^2 \cdot x^2 = x^5 y^2 \;\Rightarrow\; |(5,2,0)| = 7;$$
$$x^3y^2 \cdot y^4 z = x^3 y^6 z \;\Rightarrow\; |(3,6,1)| = 3 + 6 + 1 = 10;$$
$$xy \cdot x^2 = x^3 y \;\Rightarrow\; |(3,1,0)| = 4;$$
$$xy \cdot y^4 z = x\, y^5 z \;\Rightarrow\; |(1,5,1)| = 1 + 5 + 1 = 7.$$
The maximum is $10$, achieved by $x^3 y^6 z$, so the certified bound $D(pq) = 10$ is **tight** for this example: $\deg(pq) = 10 = D(pq)$.

**Step 5: the sum bound.** By (C2),
$$D(p + q) \le \max(D(p), D(q)) = \max(5, 5) = 5.$$
Here the bound is *not* tight in general: if the leading terms cancelled (they cannot here, since $p$ and $q$ involve disjoint variable patterns in their top monomials, $x^3y^2$ versus $y^4z$), the true degree could drop. The inequality direction of (C2) is exactly what makes the certificate cheap to produce: no cancellation analysis is needed.

### 4.2 Composition: the multiplicative blow-up rule

If $p$ has degree $d_p$ and we substitute into it a polynomial $q$ of degree $d_q$ in each of the variables that occur in $p$, each monomial $x^\alpha$ of $p$ with $|\alpha| \le d_p$ becomes a product of at most $|\alpha|$ copies of (pieces of) $q$, so

$$D\bigl(p(q_1, \ldots, q_n)\bigr) \;\le\; d_p \cdot d_q.$$

**Arithmetic check with the Section 4.1 numbers:** substituting $q$ (with $D(q)=5$) into $p$ (with $D(p)=5$) gives the bound $5 \times 5 = 25$. Direct check on the worst monomial $x^3 y^2$ of $p$: substituting $q$ for $x$ and $q$ for $y$ yields $(x^2 + y^4 z)^3 (x^2 + y^4 z)^2$, whose top term has degree $3 \times 5 + 2 \times 5 = 15 + 10 = 25$. The composition bound is tight here as well. This is the operation behind Diophantine degree bookkeeping in the motivating formalisation of [2]: iterated composition multiplies bounds, so after $k$ compositions the bound is $d_q^{\,k} \cdot d_p$; for $k = 3$ starting from $d_p = 5$, $d_q = 5$:

$$D_3 = 5 \cdot 5^3 = 5^4 = 625.$$

### 4.3 Combinatorial cost of the monomial space

The metaprogram traverses a sparse representation, but a user reasoning about worst-case size needs the count of possible monomials. The number of monomials in $n$ variables of total degree at most $d$ is the stars-and-bars count

$$M(n, d) \;=\; \binom{n + d}{d}.$$

**Derivation.** A monomial of degree $\le d$ corresponds to a weak composition of some $s \le d$ into $n$ parts; summing over $s$ telescopes via the hockey-stick identity to a single binomial coefficient:

$$\sum_{s=0}^{d} \binom{n + s - 1}{n - 1} \;=\; \binom{n + d}{d}.$$

**Concrete values, computed step by step.**

- $n = 2$, $d = 2$: $M(2,2) = \binom{4}{2} = \frac{4!}{2!\,2!} = \frac{24}{4} = 6$. (Check by listing: $1, x, y, x^2, xy, y^2$ — six monomials.)
- $n = 3$, $d = 2$: $M(3,2) = \binom{5}{2} = \frac{120}{4} = 30$? No—$\binom{5}{2} = \frac{5 \cdot 4}{2} = 10$. (List check: $1$; $x,y,z$; $x^2,xy,xz,y^2,yz,z^2$ — ten.)
- $n = 3$, $d = 5$: $M(3,5) = \binom{8}{5} = \binom{8}{3} = \frac{8 \cdot 7 \cdot 6}{6} = 56$.
- $n = 10$, $d = 5$: $M(10,5) = \binom{15}{5} = \frac{15 \cdot 14 \cdot 13 \cdot 12 \cdot 11}{120} = \frac{360360}{120} = 3003$.

**Growth characterisation.** For fixed $d$, $M(n,d) = \binom{n+d}{d} = \frac{(n+d)(n+d-1)\cdots(n+1)}{d!}$ is a polynomial of degree $d$ in $n$ with leading coefficient $1/d!$; for fixed $n$ it is a polynomial of degree $n$ in $d$. Hence the metaprogram's worst-case input space grows polynomially in each parameter with the *other* parameter as exponent—a mild but real combinatorial exposure that the sparse representation mitigates in practice (projection, stated assumption: inputs arising in Diophantine formalisations have far fewer monomials than the full simplex $M(n,d)$; we do not quantify the sparsity ratio, as we have no measurements).

### 4.4 Certificate size

Each application of (C1) or (C2) contributes one lemma instance to the certificate. A polynomial whose syntax tree has $a$ product nodes and $s$ sum nodes yields a certificate of $a + s$ lemma instances plus one leaf justification per monomial. For the Section 4.1 example: $p$ has $1$ sum node and $0$ product nodes; $pq$ has $1$ product node combining them, so the certificate for $\deg(pq) \le 10$ has $1 + 1 = 2$ binary-rule instances plus $4$ monomial leaf checks (one per monomial in $\mathrm{supp}(pq)$, computed in Step 4 above), i.e. $6$ kernel obligations in total. This smallness is the pedagogical point of [2]: the beginner can *see* the entire trusted chain.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

**R1 (Tightness of the product bound, worked example).** For $p = x^3y^2 + xy$ and $q = x^2 + y^4z$: $D(p) = 5$, $D(q) = 5$, $D(pq) = 10$, and direct expansion gives $\deg(pq) = 10$; the certified bound is tight (Section 4.1, Steps 1–4).

**R2 (Sum bound).** $D(p+q) \le 5$ for the same polynomials; tightness is not claimed (Section 4.1, Step 5).

**R3 (Composition bound).** $D(p(q,q)) \le 25$, tight for this example; three iterated compositions give $D_3 = 625$ (Section 4.2).

**R4 (Monomial-space sizes).** $M(2,2) = 6$, $M(3,2) = 10$, $M(3,5) = 56$, $M(10,5) = 3003$ (Section 4.3).

**R5 (Certificate size, worked example).** The certificate for $\deg(pq) \le 10$ comprises $2$ binary-rule instances and $4$ leaf checks, $6$ kernel obligations total (Section 4.4).

**R6 (Projection: growth regime).** Under the stated assumption that formalisation inputs are sparse (support size far below $M(n,d)$), the practical cost of `poly_degree` is expected to scale with the *actual* support size rather than $M(n,d)$; we project that degree estimation remains interactive-scale for supports up to roughly $10^4$ monomials, with uncertainty of at least an order of magnitude in both directions, since this projection is not backed by measurements. It is offered only as a design expectation, falsifiable by benchmarking the real command of [2].

## 6. Discussion

**Limitations.** Our analysis is confined to the *simplified* version of the metaprogram that the tutorial of [1],[2] presents for exposition; the full implementation "handles a variety of special cases" that we do not model—zero-polynomial conventions, constants of nilpotent or zero-divisor type where (C1) with equality fails, and possibly negative or rational coefficients. Our claim that the product bound is tight in the worked example is a property of that example, not of the method: in general $D(pq) = D(p) + D(q)$ is an upper bound and cancellation in products cannot occur over domains, but cancellation in sums means (C2) bounds are routinely loose, and iterated compositions (R3) can compound looseness multiplicatively: if each sum step loses $\ell_i$ degrees of tightness, $k$ compositions can inflate the gap as $d_q^{\,k}$ times the accumulated slack.

**Failure modes.** Three are visible from the contract alone. First, over a ring with zero divisors, (C1) as an equality is false (e.g., over $\mathbb{Z}/8\mathbb{Z}$, $(2x^2)(4x) = 0$ has degree $-\infty$, not $3$), so any reuse of the tutorial pattern must re-discharge the domain hypothesis—precisely the side condition a beginner is most likely to miss. Second, the $\bot$ convention for $\deg(0)$ propagates through (C1) awkwardly ($D(0 \cdot p)$ should be $-\infty$, not $D(0) + D(p)$ unless the convention absorbs); the tutorial must pick a convention and our analysis did not test it. Third, certificate size grows linearly in syntax-tree size but the *leaf checks* grow with support size, which for adversarially dense inputs approaches $M(n,d)$ (R4) and can reach thousands of obligations ($3003$ at $n=10, d=5$).

**What would falsify our claims.** Our central interpretive claim—that [2] instantiates a reusable "estimate-then-certify" pattern with a small trusted base—would be falsified if the actual `poly_degree` implementation were found to rely on unverified ML-side reasoning that the kernel does not check (e.g., if the emitted "proof" were an oracle-typed term rather than a kernel-checked derivation). Our tightness results (R1, R3) are falsified by any counterexample polynomial pair where the certified bound exceeds the true degree in the product or single-composition case over a domain. Our growth projection (R6) is falsified by benchmarking showing super-interactive cost at small support sizes.

**Arguing against ourselves.** A skeptic could say we have dressed a tutorial in analytical clothing: the contract (C1)–(C4) is textbook algebra, and the counts in R4 are stars-and-bars. We accept the charge in part; our defence is that the *value* of the tutorial lies in showing that textbook algebra is exactly what the metaprogram needs—no more—and that making the contract explicit is the step beginners skip. A stronger objection: the adjacent literature warns against over-generalising from small examples. The locally-testable-codes breakthrough [9] overturned the intuition that the classical obstructions were the whole story; by analogy, the simplified `poly_degree` may under-represent what careful engineering achieves on special cases, so our cost pessimism (R6) may be doubly conservative. Conversely, the metaprogramming trade-off framework of [6] predicts that any gain in succinctness of the meta-language costs safety or expressiveness somewhere; our claim that Isabelle/ML pays that cost entirely at the kernel boundary should be tested against the actual Isabelle architecture, not asserted.

**Open questions.** (i) How loose do (C2)-bounds become under the iterated compositions arising in the universal Diophantine pairs formalisation that motivated [2]? (ii) Can the certificate for a dense product be compressed (e.g., by proving a general degree lemma once rather than per-monomial)? (iii) In the LLM-assisted formalisation regime audited by [10], does machine-generated metaprogramming match the human tutorial's certificate discipline, or does it introduce oracle shortcuts? The QNFO epistemic framework [11],[12],[13] suggests treating certificates as first-class epistemic objects whose provenance—not merely whose truth—is auditable; we leave a formalisation of that suggestion to future work.

## 7. Conclusion

We have provided an analytical companion to the Isabelle/ML metaprogramming tutorial built on the `poly_degree` command [1],[2]. The tutorial's artifact computes upper bounds on total degrees of multivariate polynomials and proves the bounds correct automatically; we showed that its correctness rests on a four-line algebraic contract—$D(pq) = D(p) + D(q)$, $D(p+q) \le \max(D(p), D(q))$, $D(x_i) = 1$, $D(c) = 0$—closed under structural induction on polynomial syntax, with the domain hypothesis as the one substantive side condition. Worked arithmetic confirmed the bound is tight for a representative product ($D(pq) = 10 = \deg(pq)$) and under composition ($25$, then $625$ after three iterations), and stars-and-bars counting quantified the monomial space ($6$, $10$, $56$, $3003$ for the four parameter pairs computed). The pattern that emerges—estimate heuristically in ML, certify in the kernel—places the tutorial squarely in the safety-by-kernel corner of the metaprogramming design space mapped by [6], and gives mathematicians entering formalisation a template whose trusted base they can hold in their heads. The limitations are real: the analysis covers only the simplified exposition version, tightness is example-specific, and cost projections are unmeasured. But as a first introduction, the tutorial's choice of degree estimation is vindicated: it is the smallest example we know in which the meta-level and object-level of a proof assistant must cooperate on a genuinely algebraic invariant.

## References

[1] arXiv Query: search_query=&id_list=2610.08359&start=0&max_results=1 — record for "A First Introduction to Isabelle/ML Metaprogramming: Automatic Estimation of Polynomial Degrees."

[2] arXiv:2610.08359v1 — A First Introduction to Isabelle/ML Metaprogramming: Automatic Estimation of Polynomial Degrees.

[3] arXiv:2109.00606v1 — Introduction to Electromagnetism.

[4] arXiv:astro-ph/9711232v1 — Probing Density Fluctuations using the FIRST Radio Survey.

[5] arXiv:1401.4438v1 — Integral closure of rings of integer-valued polynomials on algebras.

[6] arXiv:cs/0512065v1 — Tradeoffs in Metaprogramming.

[7] arXiv:2010.00494v3 — Mini-DDSM: Mammography-based Automatic Age Estimation.

[8] arXiv:2208.01776v3 — The Cheeger Inequality and Coboundary Expansion: Beyond Constant Coefficients.

[9] arXiv:2512.16082v3 — Good Locally Testable Codes with Small Alphabet and Small Query Size.

[10] QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026) — DOI 10.5281/zenodo.21920604.

[11] QNFO: Epistemic Dynamics — DOI 10.5281/zenodo.17230782.

[12] QNFO: Geometric Unity of Computation — DOI 10.5281/zenodo.17435507.

[13] QNFO: Universal Computational Topos — DOI 10.5281/zenodo.17435331.