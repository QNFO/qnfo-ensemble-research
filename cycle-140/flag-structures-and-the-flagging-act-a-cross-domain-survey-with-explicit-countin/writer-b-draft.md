# Flag Structures and the Flagging Act: A Cross-Domain Survey with Explicit Counting Derivations and a Posed Re-Entry Problem

## Abstract

The word "flag" names a family of mathematically precise objects — chains of nested subspaces (flag varieties), nested set systems with exchange axioms (flag matroids), asymptotic-inequality certificates (flag algebras), and directional curvature invariants of Finsler spaces — and, in ordinary research practice, a marker attached to an unresolved issue. Research funders, journal editors, and integrity reviewers currently assess contested research programs with ad hoc procedures; this paper asks whether the incidence-structured mathematics of flags can make such assessments explicit and checkable. We survey ten works: six on flag-structured mathematics (flag matroids, Finsler flag curvature, formalized flag algebras, total positivity in flag varieties, standard monomial theory, and Schubert-varietal resolutions) and four on methodological and epistemic-critique contexts, including a critique program that classifies research programs by a four-element "kernel" audit and a structured assessment of non-Archimedean substrate adoption. We treat "flagging" as an epistemic operator that both carries mathematical content and performs the act of marking a claim's status. With fully shown arithmetic we derive the cardinalities of complete flag varieties over $\mathbb{F}_2$ at ranks 3–6 ($21$, $315$, $9765$, $615195$), the exact growth factor $2^{n+1}-1$, the dimension $6$ of the rank-4 complex flag variety, the ratio $13.125$ of binary flags to Coxeter chambers, upper bounds of $2080$ and $524800$ on flag-algebra certificate matrix entries at flag sizes 4 and 5, an aggregate activity bound of at most $100$ papers per year across six non-Archimedean modeling domains, and — as a clearly labeled projection — the Compton frequency scale $\nu_C \approx 1.236 \times 10^{20}\ \mathrm{Hz}$ as a characteristic scale of the Archimedean quantum continuum. A posed re-entry problem is held strictly as an open question, not a result, with explicit success and falsification criteria. The significance is methodological: incidence-structured reasoning is a shared substrate, and cross-domain audits benefit from making that substrate explicit.

## 1. Introduction

Research funders, journal editors, and research-integrity reviewers face a recurring operational problem: a large body of work — an entire research program — must be assessed for coherence, self-consistency, and evidential support, and the assessment itself must be checkable by third parties. The cost of doing this badly is concrete. A critique program examined in this paper reports that a field invested $35$ billion dollars in a hardware paradigm whose commercial viability it disputes, and argues that the failure is epistemic rather than merely engineering-bound [9]. Whether or not that diagnosis is accepted, the assessment practice it exemplifies — a program-level audit that classifies each pillar of a research program by graded membership in a defined framework, and that applies its own standards to itself — is exactly the kind of activity that institutions perform informally, without shared structure, and therefore without reproducibility. If a formal, checkable structure for such audits exists, the decision that changes is the reviewer's: instead of an unstructured narrative judgment, an auditor could issue a status assignment per claim, with a certificate for each status change that a third party can verify.

This paper develops that structure from an unexpected direction. The word "flag" names, in mathematics, a chain of nested subspaces: a complete flag in an $n$-dimensional vector space $V_n$ is a chain of subspaces
$$\{0\} = V_0 \subset V_1 \subset V_2 \subset \cdots \subset V_{n-1} \subset V_n,$$
with $\dim_{\mathbb{F}} V_k = k$; partial flags omit steps. The same incidence-chain idea — nested structure indexed by an ordered set — recurs as flag matroids [1], flag curvature in Finsler geometry [2], flag algebras in extremal combinatorics [3], flag varieties in total positivity [4], standard monomial theory [5], and bioriented flags in Schubert-varietal resolutions [6]. On the applied side, training over a defined universe of tasks [7] and posterior inference with guarantees [8] represent the methodological milieu in which certificate-based and audit-based reasoning is currently operationalized, and the critique program of [9] and the substrate assessment of [10] supply the epistemic-audit context in which the re-entry question of this paper is posed.

Our thesis is modest and defensible: flag-structured incidence data form a shared methodological substrate across the surveyed fields, and making that substrate explicit improves the quality of cross-domain audits — including the audit-shaped program of [9] — because audits are themselves incidence structures (claims nested inside arguments nested inside corpora). We support the thesis by survey, by explicit counting derivations, and by a disciplined statement of the open re-entry problem. We also state the thesis's weakest point up front: the shared word may be doing rhetorical work that the mathematics does not underwrite; Section 6 argues against ourselves on exactly this point.

The contributions are:

- A taxonomy of flag-structured objects by the triple of chain index, nesting order, and realization relation, covering all six mathematical works (Section 3.1).
- A certificate-gated flagging operator $\Phi_{\mathcal{S}}$ with three axioms, each motivated by a specific mechanism in the surveyed works (Section 3.2).
- Fully shown derivations of the cardinalities $|\mathrm{Fl}_n(\mathbb{F}_2)|$ for $n = 3,4,5,6$, the growth factor $2^{n+1}-1$, the complex dimension $\dim_{\mathbb{C}}\mathrm{Fl}_4 = 6$, the ratio $13.125$, flag-algebra certificate size bounds, and an information capacity $\log_2 3 \approx 1.58496$ bits per flag (Sections 4.1–4.7, results in Section 5).
- An aggregate activity computation of at most $100$ papers per year over six non-Archimedean modeling domains, from the domain table of [10] (Section 4.8).
- A posed re-entry problem with explicit success and falsification criteria, held at status "open question" together with the paper's own thesis under a symmetric-scrutiny axiom (Sections 4.10 and 6).

## 2. Background and Related Work

We discuss all ten works of the bibliography in their given order. Each claim below is restricted to what the cited work itself states.

**[1] Representability of Flag Matroids (arXiv:2504.00267v2).** This work provides a new axiom system for flag matroids, characterizes representability of uniform flag matroids, and gives forbidden-minor characterizations of full flag matroids representable over $\mathbb{F}_2$ and $\mathbb{F}_3$, along with equivalent characterizations of regular full flag matroids. Its background sections define a matroid as a pair $M=(E,\mathcal{I})$ satisfying the independence axioms, define uniform matroids $U_{r,n}$, and note that because all minors of a $\mathbb{K}$-representable matroid are $\mathbb{K}$-representable, the class of $\mathbb{K}$-representable matroids can be classified via a list of minimal forbidden minors. Its Section 3 defines a flag as a nested sequence of linear subspaces $(L_1,\dots,L_k)$ with $L_i \subseteq L_{i+1}$, and states that flag matroids combinatorially abstract flags in the same way that matroids abstract linear subspaces. For our taxonomy this is the purely combinatorial pole of the flag concept: the flag is axiomatized independently of any ambient vector space, and the forbidden-minor method — classifying a class by minimal excluded objects — is precisely the exclusion-style reasoning pattern our flagging operator generalizes.

**[2] Even dimensional homogeneous Finsler spaces with positive flag curvature (arXiv:1407.3582v2).** Here "flag" denotes flag curvature, a Finsler-geometric directional invariant attached to a flag (a tangent direction plus a containing plane). The paper uses the technique of Finslerian submersion to deduce a flag curvature formula for homogeneous Finsler spaces and, based on that formula, gives a complete classification of even-dimensional smooth coset spaces $G/H$ admitting $G$-invariant Finsler metrics with positive flag curvature, noting that the classification list coincides with that of the even-dimensional homogeneous Riemannian case. Its Theorem 4.2 proves that for a vector field $Y$ generating a geodesic of constant speed, the Finsler flag curvature $K^{F}(p,y,\mathbf{P})$ equals the Riemannian flag curvature $K^{g_Y}(p,\mathbf{P})$ of an associated metric for any tangent plane $\mathbf{P}$ containing $y$; its proofs work with the decomposition $\mathfrak{g}=\mathfrak{h}+\mathfrak{m}$ and show that a Cartan tensor term vanishes under the stated conditions. This is the differential-geometric pole: the flag is a point-plus-direction pair, and classification by positivity is again an exclusion-style result.

**[3] Formalizing Flag Algebras in Lean (arXiv:2607.23500v1).** Razborov's flag algebra method, as this work states, is a powerful tool for proving asymptotic inequalities in extremal graph theory, often reducing the task to finding a finite certificate by semidefinite programming. The work presents a machine-checked formalization of the method for finite simple graphs, together with a certificate-to-proof compiler that turns externally generated certificate data into algebraic proofs. Its excerpts show the formal machinery concretely: flags are defined by quotienting labeled graphs by isomorphism through an explicit setoid construction, and the main theorem is assembled from the certificate identity
$$[F] + \sum_{t} Q_{t} = c \cdot \mathbf{1} - r,$$
where the non-negativity of the $Q_t$ and of $r$ supplies the two inequalities of the target bound, instantiated in a Mantel example. This work is pivotal for our argument: it demonstrates that flag-structured combinatorial data can be compiled into machine-checkable proof objects, which is exactly the trust model an epistemic audit program such as that of [9] would want to import.

**[4] Total positivity in twisted product of flag varieties (arXiv:2211.11168v2).** The authors show that the totally nonnegative part of the twisted product of flag varieties of a Kac-Moody group admits a cellular decomposition, with the closure of each cell a topological manifold with boundary, and establish explicit parameterizations of each totally positive cell; in the special cases of double flag varieties and braid varieties, the totally nonnegative parts are regular. Its excerpts review the totally nonnegative flag variety $\mathcal{B}_{\geqslant 0}$ as the closure of $U^{-}_{\geqslant 0}B^{+}/B^{+}$ in the flag variety $\mathcal{B}=G/B^{+}$, define the twisted product $\mathcal{Z}=G\times^{B^{+}}G\times^{B^{+}}\cdots\times^{B^{+}}G/B^{+}$ with its open Richardson varieties $\mathring{\mathcal{Z}}_{v,\underline{w}}$, and prove regularity results (Proposition 4.3) under shellability hypotheses on intervals. This supplies the "positive cell" structure: flag varieties carry canonical decompositions into explicitly parameterized cells, a combinatorial indexing of the accessible regions of a geometric space.

**[5] Standard monomial theory and toric degenerations of Richardson varieties in flag varieties (arXiv:2103.16197v2).** This work studies standard monomial bases for Richardson varieties — intersections of a Schubert variety and an opposite Schubert variety — inside the flag variety. It states that writing down such a basis in general is challenging, involving computing so-called defining chains or key tableaux, but that for a family of Richardson varieties indexed by compatible permutations the authors provide a very direct and straightforward combinatorial rule. Its excerpts show the proof architecture: a set $\mathcal{T}_n$ of compatible pairs with a block structure, a closure lemma (Lemma 3.11) showing that local modifications of compatible pairs remain compatible, and a remark performing calculations for all Richardson varieties in $\mathrm{Flag}_4$. It exemplifies the algebraic pole: flags as varieties carrying canonical bases, with tractability hinging on combinatorial indexing — and the rank-4 calculations give a concrete anchor for our choice of $n=4$ in the counting derivations of Section 4.

**[6] Bioriented flags and resolutions of Schubert varieties (arXiv:1810.05604v2).** The authors use incidence relations running in two directions to construct a Kempf-Laksov type resolution for any Schubert variety of the complete flag manifold and an embedded resolution for any Schubert variety in the Grassmannian, as alternatives to the celebrated Bott-Samelson resolutions; the second process led to the introduction of W-flag varieties. Its excerpts describe the Schubert cell $S^{w}$ in $\mathrm{Fl}_{1,2,\ldots,n}(E)$ via the jump discontinuities of the function $k \mapsto \dim(\ell_i \cap F_k) - \dim(\ell_{i-1} \cap F_k)$ relative to a fixed flag $F_*$ and a complementary flag $G^*$ with $F_i \oplus G^i = E$, and note that the Kempf-Laksov resolutions are "very easy to describe via linear incidence relations." This is the geometric-representation pole and, notably, the only work whose method is explicitly bidirectional incidence — a structural echo of the two-directional audits (claim against counterclaim) that the critique program of [9] practices.

**[7] Open-Ended Learning Leads to Generally Capable Agents (arXiv:2107.12808v2).** This work creates agents that perform well beyond a single task: it defines a universe of tasks within an environment domain (XLand, a natively multi-agent 3D simulated space of procedurally generated worlds and multiplayer games) and demonstrates agents that are generally capable across that space. Its excerpts give concrete operational detail: a normalized percentile metric on an evaluation task set is used to compare agents and drive learning; because the full task space is prohibitively large, the authors construct a manageable evaluation task set that samples tasks to ensure uniform coverage of world and game features; each agent is trained using 8 TPUv3s consuming approximately 50,000 agent steps per second; and all reported results are computed on tasks held out of training. Its relevance is methodological, not topical: the "universe of tasks" framing, and the practice of evaluating on a defined, held-out subspace of it, is a model for defining the space over which an audit or a re-entry claim quantifies.

**[8] Guaranteed inference in topic models (arXiv:1512.03308v2).** This work addresses posterior inference for individual texts in topic models, which it states is particularly important with data streams but often intractable in the worst case, so that existing methods are approximate and lack guarantees. Its excerpts identify the standard inference methods (variational Bayes, collapsed variational Bayes, CVB0, collapsed Gibbs sampling) and present a novel algorithm, OPE, which the conclusion describes as the first with a theoretical guarantee on quality and a fast convergence rate; the empirical evaluation compares OPE-based learning methods (ML-OPE, Online-OPE, Streaming-OPE) against online variants of the state-of-the-art methods, finding that Online-OPE surpasses all existing methods in predictiveness and works well with short text. We read it as the statistical-guarantee pole: the demand that inference carry certificates of quality, paralleling the certificate-to-proof compiler of [3].

**[9] QNFO: The Valuation Reading of the Qubit Delusion: Is the Adelic Kernel Load-Bearing?** This work reports that The Qubit Delusion argues that the qubit-gate-circuit model of quantum computation imports a particle ontology inconsistent with quantum field theory, and that the field's failure to deliver commercially viable hardware after $35$ billion of investment is an epistemic crisis, not merely an engineering delay. The work itself describes the Adelic Core Research Program's "kernel membership" audit, which classifies research programs by their use of four kernel elements — valuation, tree boundary, Ostrowski, adeles — with grades FULL, WEAKER, or NONE; The Qubit Delusion received NONE. Its conclusion argues that at every candidate junction the valuation kernel is aesthetic rather than load-bearing, that the two programs are orthogonal, and it registers calibration predictions, including the strong claims that the Qubit Delusion's critique stands independent of the kernel and that no revision will attribute its conclusions to valuation-theoretic reasoning. This supplies the one economic figure we use ($35$ billion, taken as stated by the work and not independently verified) and the clearest existing instance of a program-level audit that reports a negative structural result about its own framework.

**[10] QNFO: When Will Non-Archimedean Geometry Displace the Real Numbers? A Structured Assessment of the Adelic Substrate Thesis.** This work observes that the real numbers are the default continuum for physical modeling — every quantum state lives in a Hilbert space over $\mathbb{C}$, every neural network optimizes over $\mathbb{R}^n$ — and that Ostrowski's theorem shows the reals are merely one of many completions of the rationals, with the $p$-adic completions satisfying the strong triangle inequality and inducing an ultrametric. It identifies two domains where non-Archimedean geometry is already the native substrate (phylogenetics, via ultrametric distance matrices, and isogeny-based cryptography), tabulates approximate activity levels across candidate domains, and concludes that the central bet — non-Archimedean substrate modeling displacing the Archimedean default in at least one domain by 2036 — faces a historical reference class in which zero of the three closest analogues (the Copernican, relativistic, and quantum revolutions) achieved mainstream adoption within a decade, and that no empirical anomaly for the Archimedean default has been identified. This is the substrate-assessment pole: a structured forecast with explicit success criteria and an explicitly stated adverse base rate, and the source of the domain-activity numbers we aggregate in Section 4.8.

## 3. Methods

### 3.1 Taxonomy by incidence data

We classify each flag-structured object by the triple $(I, \leq, \mathcal{R})$, where $I$ is the indexing set of the chain, $\leq$ the nesting order, and $\mathcal{R}$ the realization relation:

```
Object                    I (chain index)         R (realization)
--------------------------------------------------------------------
Complete flag [1],[4-6]   {1,...,n-1}             subspace chain in V_n
Flag matroid [1]          ordered set             representable over F_q
Flag curvature [2]        (point, direction)      Finsler metric on G/H
Flag algebra [3]          finite graphs           SDP certificate
Nonneg. cells [4]         Weyl combinatorics      totally positive matrices
Standard monomials [5]    compatible perms        Richardson variety basis
Bioriented flags [6]      two-direction incidence Kempf-Laksov resolution
Audit structure [9]       claims in corpus        symmetric scrutiny
```

The table's rows are justified by the surveyed works themselves: [1] defines a flag as a nested sequence of subspaces and axiomatizes its abstraction; [2] attaches curvature to a flag (direction plus plane); [3] builds flags as graph quotients feeding semidefinite certificates; [4] indexes cells by Weyl-group elements; [5] indexes bases by compatible permutation pairs; [6] runs incidence in two directions; and [9] audits a corpus by graded membership in a four-element framework.

### 3.2 The flagging operator

Let $\mathcal{S}$ be a corpus of research outputs. Define the *flagging operator*
$$\Phi_{\mathcal{S}} : \mathcal{S} \to \{R, Q, F\} \times \mathcal{D},$$
where the first component is a status in the three-element set $\{R, Q, F\}$ — $R$ = result, $Q$ = open question, $F$ = flagged for remediation — and $\mathcal{D}$ is a set of justifying documents. The operator is *certificate-gated* in the sense of [3]: a status change from $Q$ to $R$ requires a certificate that passes a mechanical or referee-level check, exactly as the certificate-to-proof compiler of [3] turns externally generated certificate data into checkable algebraic proofs via the identity $[F] + \sum_{t} Q_{t} = c \cdot \mathbf{1} - r$; a status change from $R$ to $F$ requires a documented failure mode. Three axioms, each motivated in Section 2:

- **A1 (Uniformity, after [7]).** $\Phi_{\mathcal{S}}$ is defined on all of $\mathcal{S}$; every element of the corpus carries exactly one status. The motivation is [7]'s practice of defining a universe of tasks and evaluating every agent on a common held-out evaluation set: coverage must be total and the yardstick common.
- **A2 (Symmetric scrutiny, after [9]).** The same audit standard that demotes an external claim to $F$ applies to the flagging authority's own prior outputs. The motivation is [9]'s registration of calibration predictions against its own framework, including the prediction that its own strongest claims hold — an audit that binds itself.
- **A3 (Two-directional incidence, after [6]).** Each flag carries pointers in two directions: from the flagged item to its justifying documents, and from those documents back to every item whose status they affect. The motivation is [6]'s bioriented incidence relations, which run in two directions to resolve singularities that one-directional relations do not reach.

### 3.3 Counting method

For the quantitative case study we use only the definition of a complete flag and standard finite-field counting, stated in full so every step is checkable. Let $V_n$ be an $n$-dimensional vector space over $\mathbb{F}_q$. A complete flag is built by choosing, successively, a line in $V_n$, a plane containing it, and so on; at step $k$ the number of choices is the number of lines in an $(n-k+1)$-dimensional quotient, $\frac{q^{\,n-k+1}-1}{q-1}$. Hence
$$\left| \mathrm{Fl}_n(\mathbb{F}_q) \right| = \prod_{k=1}^{n} \frac{q^k - 1}{q - 1}.$$
We take $q = 2$, the smallest nontrivial field, which is also the field over which [1] gives forbidden-minor characterizations of representable full flag matroids.

### 3.4 Projection and open-question methods

The Compton-scale quantity is treated as a labeled projection: the inputs are standard physical constants stated explicitly below, and the output is a characteristic frequency scale of the Archimedean quantum continuum whose default status [10] interrogates. No experimental claim is made. The re-entry artifact (https://papers.qnfo.org/papers/barc-codes-as-algebraically-restricted-coherent-state-constellations-geometry-se/) is treated as a black box: no content for it is available to this paper, so we define the re-entry problem operationally rather than substantively.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Cardinality of $\mathrm{Fl}_3(\mathbb{F}_2)$

Inputs: $n = 3$, $q = 2$ (Section 3.3). Formula:
$$\left| \mathrm{Fl}_3(\mathbb{F}_2) \right| = \prod_{k=1}^{3} \frac{2^k - 1}{2 - 1} = (2^1 - 1)(2^2 - 1)(2^3 - 1) = 1 \cdot 3 \cdot 7 = 21.$$

### 4.2 Cardinality of $\mathrm{Fl}_4(\mathbb{F}_2)$

Inputs: $n = 4$, $q = 2$.
$$\left| \mathrm{Fl}_4(\mathbb{F}_2) \right| = 1 \cdot 3 \cdot 7 \cdot 15 = 21 \cdot 15 = 315.$$

### 4.3 Cardinalities at ranks 5 and 6

Continuing the same recurrence:
$$\left| \mathrm{Fl}_5(\mathbb{F}_2) \right| = 315 \cdot 31 = 9765, \qquad \left| \mathrm{Fl}_6(\mathbb{F}_2) \right| = 9765 \cdot 63 = 615195.$$

### 4.4 Growth factor

From Sections 4.2 and 4.1:
$$\frac{\left| \mathrm{Fl}_4(\mathbb{F}_2) \right|}{\left| \mathrm{Fl}_3(\mathbb{F}_2) \right|} = \frac{315}{21} = 15 = 2^4 - 1,$$
and from Section 4.3:
$$\frac{\left| \mathrm{Fl}_6(\mathbb{F}_2) \right|}{\left| \mathrm{Fl}_5(\mathbb{F}_2) \right|} = \frac{615195}{9765} = 63 = 2^6 - 1.$$
Both checks confirm the general rule: passing from rank $n$ to rank $n+1$ multiplies the count by $2^{n+1} - 1$. Also, since each factor $2^j - 1 \geq 2^{\,j-1}$ for $j \geq 1$,
$$N_{\text{flag}}(2,n) \geq \prod_{j=1}^{n} 2^{\,j-1} = 2^{\,n(n-1)/2};$$
for $n = 4$ this gives $2^{6} = 64 \leq 315$, consistent with the exact value.

### 4.5 Dimension of the complex flag variety

Input (stated here as our assumption): a complete flag in $\mathbb{C}^n$ is specified by $\binom{n}{2} = n(n-1)/2$ independent parameters, so $\dim_{\mathbb{C}} \mathrm{Fl}_n = \binom{n}{2}$. For $n = 4$:
$$\dim_{\mathbb{C}} \mathrm{Fl}_4 = \binom{4}{2} = \frac{4 \cdot 3}{2} = 6.$$
The rank-4 choice is anchored in the surveyed mathematics: [5] performs calculations for all Richardson varieties in $\mathrm{Flag}_4$, and [1] gives its forbidden-minor characterizations over $\mathbb{F}_2$, the field of our counting.

### 4.6 Flags per Coxeter chamber

Input (stated here as our assumption): the chambers of the type $A_{n-1}$ Coxeter complex on $\mathrm{Fl}_n(\mathbb{C})$ are indexed by permutations, so their number is $n!$. For $n = 4$: $4! = 24$. The ratio of binary flags to chambers at $n = 4$ is
$$\frac{315}{24} = 13.125.$$
Interpretation: over $\mathbb{F}_2$ there are $13.125$ times as many complete flags as there are chambers in the complex case at the same rank.

### 4.7 Type counts for flag-algebra certificates

Inputs (stated assumptions, following the setting of [3], where flags are quotient classes of labeled graphs on a fixed number of vertices): under the assumption that flag-algebra types are labeled simple graphs on $k$ vertices, the number of labeled types is at most $T_{\text{lab}}(k) = 2^{\binom{k}{2}}$. For $k = 4$: $\binom{4}{2} = 6$, so $T_{\text{lab}}(4) = 2^{6} = 64$. For $k = 5$: $\binom{5}{2} = 10$, so $T_{\text{lab}}(5) = 2^{10} = 1024$, a growth factor of $1024/64 = 16 = 2^4$ per added vertex. Under the same assumption, the number of free scalar entries in a positive-semidefinite certificate matrix of dimension $T_{\text{lab}}(k)$ is at most
$$M(k) = \frac{T_{\text{lab}}(k)\,(T_{\text{lab}}(k) + 1)}{2}.$$
For $k = 4$: $M(4) = \frac{64 \cdot 65}{2} = \frac{4160}{2} = 2080$. For $k = 5$: $M(5) = \frac{1024 \cdot 1025}{2} = \frac{1049600}{2} = 524800$. The ratio
$$\frac{M(5)}{M(4)} = \frac{524800}{2080} = 252.3077\ldots \approx 252.31$$
illustrates the quadratic-in-dimension cost of enlarging the flag size by one vertex. These are upper bounds under the labeled assumption; the actual method of [3] quotients labeled graphs by isomorphism, so the true counts are smaller.

### 4.8 Information capacity of a three-state flag

Input (definition from Section 3.2): the status alphabet has size $|\{R, Q, F\}| = 3$. The information capacity of one flag, in bits, is
$$I_{\text{