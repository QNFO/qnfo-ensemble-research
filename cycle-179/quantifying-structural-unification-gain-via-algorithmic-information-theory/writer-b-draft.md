# Unification Gain: An Algorithmic Information Theory Metric for Non-Predictive Theoretical Work

## Abstract

A large class of theoretical contributions — structural unifications that subsume existing theories under one framework — produces no novel empirical prediction and therefore lacks the falsification-based validation that disciplines generative work. This "Validation Metric Problem" leaves unificatory value to subjective judgment. We formalize a candidate metric, the Unification Gain $G_U = K(T_1) + K(T_2) - K(U)$, where $K$ denotes Kolmogorov complexity and $U$ a unified theory, building on a published taxonomy that separates Generative, Structural Unification, and Epistemic Scaffolding contributions. We derive three results: (i) $G_U$ is invariant under changes of universal reference machine up to an additive constant, so the normalized gain $g_U = G_U/(K(T_1)+K(T_2))$ carries machine-dependent error $O(1)/(K(T_1)+K(T_2))$, which vanishes for large theories; (ii) $G_U$ is bounded below by $-O(1)$ and above by $\min(K(T_1),K(T_2)) + O(1)$, so the conjectured non-negativity is not a theorem but a defining property of genuine unification; (iii) $G_U$ equals the algorithmic mutual information between the component theories plus a residual term. We give a fully worked illustrative computation on hypothetical compressed theory representations ($G_U = 6{,}900$ bytes, $g_U \approx 0.311$, against a significance threshold $\delta = 0.15\,(K(T_1)+K(T_2)) = 3{,}330$ bytes) and specify a compression-based measurement protocol using the Normalized Compression Distance. The metric converts unificatory value into a computable, falsifiable quantity testable against expert consensus.

## 1. Introduction

Theoretical physics and adjacent fields contain a class of contributions whose value is real but whose validation is not. When a new framework subsumes two or more existing theories — revealing that phenomena previously treated by separate formalisms are special cases of one structure — the community judges the work important, but no experiment can be run to confirm the judgment, because the unification typically predicts nothing that the component theories did not already predict. The researchers who produce such work, the reviewers who evaluate it, and the funding bodies that decide between it and empirically generative alternatives all face the same gap: there is no objective, computable metric for unificatory value. The cost of this gap is concrete. Careers and resources flow toward work whose value can be demonstrated; work whose value rests on coherence alone is vulnerable to fashion, rhetorical skill, and reviewer preference. A validated metric would change the decision that a reviewer, an editor, or a panel makes: instead of asking "does this unification feel deep?", one could ask "does it compress the formal description of the unified domain, and by how much?"

This problem has been named and isolated in prior work. The taxonomy of Quni-Gudzinas separates scientific contributions into Generative (G-Type), Structural Unification (S-Type), and Epistemic Scaffolding (E-Type) categories, and identifies the absence of a validation metric for the latter two as the framework's primary limitation, creating "significant risks of subjective evaluation and potential disciplinary stagnation" [9]. A companion derivation formalizes this as the Validation Metric Problem: G-Type contributions possess the objective metric of correspondence with empirical data, while S-Type and E-Type contributions lack any equivalent, and an idealized remedy is to define progress as algorithmic compression of knowledge [10]. Neither work, however, defines the compression metric precisely enough to be computed, proves its formal properties, or confronts it with the objection that Kolmogorov complexity is uncomputable.

This paper develops the missing formal object. We define the Unification Gain $G_U$ for a unified theory $U$ subsuming component theories $T_1, \dots, T_n$, prove what can be proved about it, bound what cannot, and specify how it can be estimated with computable proxies. Throughout, Kolmogorov complexity $K(s)$ is the length of the shortest program that outputs string $s$ on a fixed universal machine; the reader unfamiliar with Algorithmic Information Theory (AIT) can read $K(s)$ as "the ideal compressed size of $s$."

The contributions are:

1. A formal definition of $G_U$ and its normalized form $g_U$, with the derivation that $G_U$ is machine-invariant up to an additive constant and that the error in $g_U$ vanishes as theory size grows (Section 4.1).
2. A proof that $G_U$ is bounded in $[-O(1),\ \min(K(T_1),K(T_2)) + O(1)]$, showing that non-negativity is not automatic but is exactly the property that distinguishes genuine unification from mere aggregation (Section 4.2).
3. A decomposition of $G_U$ into algorithmic mutual information plus a residual unification term, connecting the metric to standard AIT identities (Section 4.3).
4. A computable measurement protocol based on compression, adapted from the Normalized Compression Distance literature, with a fully worked illustrative computation including the significance threshold $\delta$ (Sections 4.4 and 5).
5. A falsification criterion and a minimal experimental design that would confirm or refute the metric's agreement with expert judgments of unificatory value (Sections 6 and 7).

## 2. Background and Related Work

The Validation Metric Problem. The starting point is the taxonomy of Quni-Gudzinas, which deconstructs scientific progress into three functional types: G-Type work producing novel empirical predictions, S-Type work revealing "a deeper coherence among existing theories," and E-Type work refining the methods of inquiry [9]. That work states the consequence plainly: because S-Type and E-Type contributions are not validated by direct empirical testing, they lack a rigorous validation metric, and the analysis names this the "Validation Metric Problem." Crucially for our purposes, the same source already contains a formal seed of the metric studied here: its Theorem 3 states that a unified theory $T_U$ represents a non-trivial S-type contribution only if $G_U(T_U; T_1, T_2) > \delta$ for a pre-defined threshold, with the example value $\delta = 0.15 \times (K(T_1) + K(T_2))$, and proves this by observing that $G_U > \delta$ implies $K(T_U) < K(T_1) + K(T_2) - \delta$, i.e., a strictly shorter description than the sum of the parts [9]. We adopt this definition and threshold convention and subject them to the formal scrutiny they had not yet received. The companion paper Epistemic Dynamics supplies the epistemological framing: it derives the taxonomy from first principles, defines G-Type validity through a temporal-precedence axiom (a prediction must be confirmed after it is made), states Proposition 1.4 that G-Type work alone possesses an objective validation metric, and proposes AIT-based algorithmic compression as the idealized solution for the rest [10]. Our contribution is to make that idealized solution precise, bounded, and estimable.

AIT metrics applied to non-physical questions. The pattern of using AIT to quantify a quantity previously left qualitative has a precedent in the foundations of consciousness research. That work reviews Tononi's integrated information theory, argues that prior formalizations of integrated information depend on information loss, and — because lossy integration would necessitate continuous damage to existing memories — reframes consciousness as a lossless integrative process with a formalization based on algorithmic information [1]. The structural analogy is direct: a property of a system (integration there, unification here) that was first stated qualitatively is given a numeric value built on $K$, and the choice of lossless versus lossy formulation is itself a modeling decision with consequences. Our metric faces the same design choice — whether the compression of a unified theory should be measured losslessly (as we assume) or with lossy abstractions — and Section 6 discusses the consequence.

Computable proxies for Kolmogorov complexity. Because $K$ is uncomputable, any practical protocol must estimate it. The most direct precedent is the information retrieval system built on the Normalized Compression Distance (NCD): that work designs an IR technique using the NCD, statistical outlier detection, and a novel database organization, and states that the NCD "has been used as a feasible approximation of the Normalized Information Distance (based on the ideal notion of Kolmogorov Complexity)," comparing documents without keywords or traditional IR techniques [7]. Its experiments — a database of 100 peer-reviewed publications by 17 authors, with the Hampel identifier used to separate relevant from irrelevant distances — demonstrate that compression-based distances are operationally usable on real text corpora and that a statistical thresholding rule (the Hampel identifier, using the median $M$ and median absolute deviation $S$ with the rule $(M - X)/S > g(N;\alpha)$) can convert distances into classifications [7]. Our protocol in Section 4.4 borrows both elements: compression as the $K$-estimator and a statistical rule for deciding when a measured gain is significant. A second, independent demonstration that information-gain quantities can be operationalized inside real systems comes from masked diffusion language models: the Info-Gain Sampler uses bidirectional attention to estimate the information gain of each decoding action, balancing immediate certainty against future uncertainty reduction, and reports gains of 2.9–11.6 percentage points in average reasoning accuracy over baselines, with cumulative entropy reduced to 65.9% (at $K=2$) and 62.0% (at $K=1$) of the best greedy baseline [2]. The relevance is methodological: a quantity defined over an information measure, previously implicit, was made an explicit selection criterion and the resulting system measurably improved, which is the pattern of validation we propose for $G_U$ — the metric earns credibility if judgments made with it are more consistent than judgments made without it.

Compression as a proxy in practice. The Kappa framework of Quni-Gudzinas addresses the uncomputability objection head-on and provides the theoretical scaffolding our estimation layer rests on. Its Coding Theorem relates the uncomputable ideal to a computable quantity via $-\log_2 M(s) = K(s) + O(1)$, proved by the two-sided bound $M(s) \geq 2^{-K(s)}$ (since the sum defining $M(s)$ includes the shortest program) and $M(s) \leq c \cdot 2^{-K(s)}$ from the Kraft inequality, giving $\kappa_{\text{eff}}(s) \approx \kappa_{\text{ont}}(s) + C$ with $C$ depending only on the universal machine [12]. Its asymptotic result for ergodic sources — that the normalized empirical Kappa converges to the entropy rate $h$, $\lim_{n\to\infty} \kappa_{\text{emp}}(s_n)/n = h$ — establishes that compression ratios are consistent estimators of information content for data typical of physical processes [12]. The framework's conclusion that the reliance on uncomputable concepts does not render it unscientific, because a hierarchy of computable proxies ($\kappa_{\text{eff}}$, $\kappa_{\text{emp}}$) makes contact with data, is exactly the defense our metric requires, and we reuse its structure: an uncomputable ideal ($G_U$ in terms of true $K$), a computable proxy (compressor-based estimates), and a stated error bound.

Unification in a literal, computational sense. The word "unification" has an exact meaning in logic and term rewriting, and the computational literature there shows both the feasibility and the cost structure of unification as an operation. A unification algorithm for the equational theory combining standard unification with ACUN properties (such as XOR) was built for security protocol analysis, using the Baader–Schulz combination method for disjoint equational theories and optimizations that "drastically reduce the number of non-deterministic choices" [6]. Its runtime table shows the practical stakes of such optimizations: one unification problem solved in 3.3 milliseconds with the variable-identification optimization but exceeding 30 minutes without it, and the authors conclude the algorithm "performs well on practical examples, both in terms of its runtime and the size of the complete set of unifiers returned" [6]. For our project the lesson is about the cost of the measurement step: if formalized theories are represented as terms in a suitable algebra, syntactic unification of $T_1$ and $T_2$ into $U$ is a decidable, implementable operation, and the optimization structure of [6] suggests that naive implementations of our measurement pipeline would be catastrophically slow without theory-specific pruning.

Reduction and compression as verified operations on formal problems. A complementary precedent for "compress a formal object, verify nothing of value is lost" is the generalized traveling salesman problem (GTSP) reduction work: given a partition of cities into groups, it deletes redundant vertices and edges while preserving the optimal solution, and its experiments on TSPLIB-derived instances show the Combined Reduction "is often the most powerful among the presented algorithms and takes even less time than the single Edge Reduction," with solver-level tests confirming that reductions translate into real end-to-end speedups for exact and memetic solvers [3]. The structural lesson for us is that a compression claim about formal objects can be validated by an invariance check — the reduced object must preserve the original's essential content (there: optimal tour value; here: the theorems of $T_1$ and $T_2$) — and that the validation must be run at the level of the downstream consumer, not merely the compression step itself.

Evaluation against expert or automated judgment. Any claim that $G_U$ tracks "unificatory value" must be tested against a ground truth, and the only available ground truth is community judgment. Two methodological cautions transfer directly from adjacent fields. In legal information retrieval, the COLIEE-2019 participation report evaluated BM25, Doc2Vec, and BERT systems against organizer-defined metrics — precision, recall, F-measure, mean average precision, and accuracy across four sub-tasks — and reported, for example, BM25 reaching precision 0.6256 and F-measure 0.4765 on Task 1 while Doc2Vec reached precision 0.4653, showing that on a task with no physical ground truth, agreement with curated relevance judgments is the operative validation and different methods score very differently against it [4]. In machine translation, the survey of LLM-based evaluation documents both the adoption of LLM-as-judge paradigms and their "critical concerns regarding bias, segment-level reliability, and sensitivity to prompt design," and describes structured remedies such as M-MAD's multi-agent debate pipeline in which separate agents score MQM dimensions and a judge aggregates [8]. Our validation design in Section 7 uses the former's multi-metric discipline and the latter's caution: expert consensus on unificatory value is itself a noisy, biased instrument, and single-judge designs are insufficient.

Formal systems as executable objects. Finally, the feasibility of representing theories as compressible, machine-checkable artifacts is demonstrated by the distinction-calculus work, which engineered an AST parser executing boundary reductions and verified computational claims about a non-ZFC formal foundation by "rigorous compilation mapping, AST execution, and structural encoding," concluding that the framework's value was "validated by raw algorithmic performance" [11]. This establishes that the pipeline our metric assumes — theory as formal artifact, artifact as executable/compressible object, performance numbers as the arbiter of foundational claims — has been operated end to end for at least one formal system.

## 3. Methods

### 3.1 Objects

We work with theories represented as finite formal artifacts: a theory $T$ is a finite string over a fixed alphabet (its axioms, definitions, and a designated inference procedure), from which its theorem set $\mathrm{Th}(T)$ is derivable. This representation choice is deliberate and follows the demonstrated practice of treating formal systems as executable artifacts [11]. We assume a fixed universal prefix-free machine $\mathcal{U}$; $K(x) = \min\{|p| : \mathcal{U}(p) = x\}$.

**Definition 3.1 (Unified theory).** A theory $U$ unifies theories $T_1, T_2$ if (a) $\mathrm{Th}(T_1) \cup \mathrm{Th}(T_2) \subseteq \mathrm{Th}(U)$ up to a fixed, polynomial-time translation of vocabularies, and (b) $U$ is not the disjoint concatenation of $T_1$ and $T_2$.

**Definition 3.2 (Unification Gain).** For $U$ unifying $T_1, T_2$:

$$G_U(T_U; T_1, T_2) = K(T_1) + K(T_2) - K(U).$$

This is the definition of [9], retained exactly. The normalized form is:

$$g_U = \frac{G_U}{K(T_1) + K(T_2)}.$$

**Definition 3.3 (Significance threshold).** Following the convention of [9], a unification is non-trivial iff $G_U > \delta$ with $\delta = 0.15\,(K(T_1) + K(T_2))$, equivalently $g_U > 0.15$.

### 3.2 Estimation layer

True $K$ is uncomputable. We estimate $K(T)$ by the compressed length $C(T)$ under a fixed, publicly specified compressor (any standard lossless compressor; the choice must be fixed in advance and disclosed, as the compressor choice in NCD practice is fixed and disclosed [7]). The estimators are:

$$\hat{K}(T) = C(T), \qquad \hat{G}_U = C(T_1) + C(T_2) - C(U).$$

The theoretical license for this substitution is the coding-theorem hierarchy of [12]: the effective complexity satisfies $\kappa_{\text{eff}}(s) \approx \kappa_{\text{ont}}(s) + C$ with $C$ machine-dependent only, and for ergodic sources the normalized empirical quantity converges to the entropy rate [12]. A practical compressor is an upper bound on the true $K$ up to the compressor's own overhead: $K(s) \leq C(s) \leq K(s) + c_{\text{comp}}$ cannot be guaranteed in general (a compressor may fail to find short programs), but $C(s) \geq K(s)$ always holds, since every compressor output is a decompressible description. We therefore have a one-sided guarantee:

$$K(s) \leq C(s), \qquad \hat{G}_U \leq G_U + (c_1 + c_2 - c_U)$$

where $c_i$ are compressor overheads. The sign of the estimation error in $\hat{G}_U$ is not controlled in general; Section 6 treats this as the central experimental risk.

### 3.3 Validation design

The metric's claim to measure unificatory value is empirical, not analytic: we propose comparing $\hat{g}_U$ rankings against expert consensus rankings on a set of historical and synthetic unification cases, using multiple agreement metrics (rank correlation, precision at $k$, and inter-rater reliability of thresholded classifications), in the manner of multi-metric evaluation against curated judgments [4] and with the bias controls that LLM-as-judge literature shows are necessary, such as multi-agent debate structures rather than single-judge scoring [8].

## 4. Analysis

### 4.1 Invariance under change of universal machine

**Input:** the invariance theorem of AIT, as instantiated in the Coding Theorem of [12], which states that for two universal machines the complexities differ by a machine-dependent constant: $K_{\mathcal{U}}(s) = K_{\mathcal{U}'}(s) + c_{\mathcal{U},\mathcal{U}'}$ with $c$ independent of $s$.

**Derivation.** Write $K_i = K_{\mathcal{U}}(T_i)$ and $K'_i = K_{\mathcal{U}'}(T_i)$. Then:

$$G_U' = K'_1 + K'_2 - K'_U = (K_1 - c) + (K_2 - c) - (K_U - c) = G_U - c,$$

where $c = c_{\mathcal{U},\mathcal{U}'}$ is the same constant in all three terms. Hence:

$$G_U' = G_U - c_{\mathcal{U},\mathcal{U}'},$$

so $G_U$ is invariant up to one additive constant, not three. For the normalized metric:

$$g_U' = \frac{G_U - c}{K_1 + K_2 - 2c}.$$

The absolute error is:

$$|g_U' - g_U| = \left|\frac{(G_U - c)(K_1 + K_2) - G_U (K_1 + K_2 - 2c)}{(K_1+K_2)(K_1+K_2-2c)}\right| = \frac{|c\,(K_1 + K_2) - 2c\,G_U|}{(K_1+K_2)(K_1+K_2-2c)}.$$

Since $G_U \leq \min(K_1, K_2) + O(1) \leq K_1 + K_2$ (proved in §4.2), the numerator is at most $|c|(K_1+K_2) + 2|c|(K_1+K_2) = 3|c|(K_1+K_2)$, giving:

$$|g_U' - g_U| \leq \frac{3|c|}{K_1 + K_2 - 2c} \xrightarrow{K_1 + K_2 \to \infty} 0.$$

**Result 4.1.** The normalized Unification Gain $g_U$ is asymptotically machine-invariant: its machine-dependence is $O(1/(K(T_1)+K(T_2)))$. For theories whose combined formal descriptions exceed roughly $10^5$ bits, a machine constant of even $10^3$ bits perturbs $g_U$ by at most $3 \times 10^3 / 10^5 = 0.03$, below the threshold width $0.15$ of Definition 3.3. This is the formal content of the conjecture that $G_U$ is "invariant under encoding": exact invariance is false, asymptotic invariance is true and is what any measurement protocol needs.

### 4.2 Bounds on $G_U$ and the status of non-negativity

**Upper bound.** If $U$ unifies $T_1, T_2$ per Definition 3.1(a), then $T_1$ is recoverable from $U$ by a fixed translation procedure $p_{\text{tr}}$ independent of $T_1$: a program that prints $T_1$ consists of $p_{\text{tr}}$, a pointer to $U$, and the translation bookkeeping. Hence:

$$K(T_1) \leq K(U) + O(1), \qquad K(T_2) \leq K(U) + O(1).$$

Adding is wrong; instead, each inequality gives $K(U) \geq K(T_i) - O(1)$ for $i = 1, 2$, so:

$$K(U) \geq \max(K(T_1), K(T_2)) - O(1),$$

and therefore:

$$G_U = K(T_1) + K(T_2) - K(U) \leq K(T_1) + K(T_2) - \max(K(T_1), K(T_2)) + O(1) = \min(K(T_1), K(T_2)) + O(1).$$

**Lower bound.** The disjoint concatenation $U_0 = \langle T_1, T_2 \rangle$ (a program printing $T_1$ followed by a program printing $T_2$, with a separator) is a valid description of a theory satisfying Definition 3.1(a), so the minimal $U$ need not be longer:

$$K(U) \leq K(T_1) + K(T_2) + O(1) \implies G_U \geq -O(1).$$

**Result 4.2.** $G_U \in [-O(1),\ \min(K(T_1), K(T_2)) + O(1)]$. The conjectured non-negativity of $G_U$ is therefore **not a theorem**. It holds if and only if the unified theory is genuinely shorter than the concatenation of its parts — which is precisely the informal notion of unification. The metric does not need non-negativity as an axiom; it uses $G_U > \delta$ as the *definition* of having achieved unification, exactly as Theorem 3 of [9] sets up: a candidate $U$ with $G_U \leq \delta$ is classified as failing to unify non-trivially, rather than the definition being repaired to force positivity. This is the correct logical arrangement, because a metric that cannot report failure cannot validate anything.

**Worked micro-example (illustrative, all numbers assumed).** Let a formalized fragment $T_1$ have $K(T_1) = 12{,}400$ bits and $T_2$ have $K(T_2) = 9{,}800$ bits (assumed values for illustration; Section 5 labels all such computations). A candidate $U$ with $K(U) = 15{,}300$ bits gives:

$$G_U = 12{,}400 + 9{,}800 - 15{,}300 = 6{,}900 \text{ bits},$$

$$g_U = \frac{6{,}900}{22{,}200} \approx 0.310811,$$

and the threshold is:

$$\delta = 0.15 \times 22{,}200 = 3{,}330 \text{ bits}.$$

Since $6{,}900 > 3{,}330$, the candidate passes. The upper bound of Result 4.2 is $\min(12{,}400, 9{,}800) = 9{,}800$ bits, and indeed $6{,}900 \leq 9{,}800$; the example is consistent with the theorem, and the bound tells us no unification of these two theories can exceed $g_U = 9{,}800/22{,}200 \approx 0.441441$.

### 4.3 Decomposition into mutual information

**Input:** the standard AIT identity $K(T_1, T_2) = K(T_1) + K(T_2 \mid T_1) + O(\log(K(T_1)+K(T_2)))$ and the definition of algorithmic mutual information $I(T_1 : T_2) = K(T_2) - K(T_2 \mid T_1)$.

**Derivation.** Add and subtract $K(T_1, T_2)$:

$$G_U = \big[K(T_1) + K(T_2) - K(T_1, T_2)\big] + \big[K(T_1, T_2) - K(U)\big].$$

The first bracket is, up to $O(\log)$:

$$K(T_1) + K(T_2) - K(T_1, T_2) = K(T_1) + K(T_2) - K(T_1) - K(T_2 \mid T_1) + O(\log) = I(T_1 : T_2) + O(\log).$$

Therefore:

$$G_U = I(T_1 : T_2) + \big[K(T_1, T_2) - K(U)\big] + O(\log(K(T_1)+K(T_2))).$$

**Result 4.3.** The Unification Gain separates into two interpretable parts: the algorithmic mutual information already shared between the component theories (the overlap a mere concatenation would double-count), and a residual term $K(T_1,T_2) - K(U)$ measuring how much shorter the unified framework is than even the optimally joint description of the pair. A unification that merely packages overlapping content scores high on the first term; a unification with genuinely new organizing structure scores on the second. This decomposition gives the metric diagnostic power that a single number lacks, and it is testable: measuring $I(T_1:T_2)$ separately (via $K(T_2)$ and $K(T_2 \mid T_1)$, the latter estimable by compressing $T_2$ given $T_1$ as dictionary pretraining, the standard conditional-compression technique underlying NCD practice [7]) locates the source of a measured gain.

### 4.4 Computable protocol

The measurement protocol, adapted from NCD practice [7] and the comput