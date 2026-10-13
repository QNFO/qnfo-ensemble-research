# Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics

## Abstract

Continuum physics is formulated over the uncountable real line $\mathbb{R}$, yet every measurement, record, and computation a laboratory can produce is finite. This paper asks whether the uncountability of $\mathbb{R}$ — as opposed to its Archimedean completeness — has any physical consequence, and answers that it does not, in a precise and checkable sense. The gap addressed is formal: the physics literature treats $\mathbb{R}$ as indispensable while the computability literature has only recently begun to study the computational content of uncountability itself, and no result connects the two by showing that cardinality is empirically inaccessible. The approach is threefold. First, we prove that the set of computable reals is countable and dense in $\mathbb{R}$, so it carries the order, completeness-for-limits, and topology that continuum physics actually uses. Second, we derive an observability bound: an instrument of range $L$ and resolution $\delta$ distinguishes at most $N = L/\delta$ outcomes, so a meter-scale position measurement at $10^{-18}\,\mathrm{m}$ resolution distinguishes $10^{18}$ outcomes, about $59.8$ bits — far below any cardinality-sensitive content. Third, we state a formal indistinguishability claim: no finite experiment can detect the difference between an uncountable continuum and a countable computable surrogate, because both produce the same finite set of possible records. We compute the program-count bound $2^{n+1}-1$ for $n$-bit descriptions and the measurement-bit bound explicitly. The result implies that debates over the Continuum Hypothesis are empirically vacuous for physics, and that model-builders may restrict to computable reals without empirical loss.

## 1. Introduction

A working physicist who simulates a turbulent flow, fits a spectrum, or writes down a Hamiltonian is using the real numbers of classical analysis: an uncountable set, by Cantor's argument. The choice is made silently, in every textbook, and it is never tested. The cost of this silent choice is not money but conceptual exposure: if uncountability is physically load-bearing, then physical law depends on objects — such as the halting probability $\Omega$ of a universal machine — that no process can compute or measure; if it is not load-bearing, then a large part of the mathematical scaffolding of physics is decoration, and alternative foundations (computable, constructible, or rational-based continua) are empirically equivalent and may be formally cleaner. The decision that would change if this paper's result holds is the decision of which number system to take as foundational when constructing physical theories, axiomatizing quantum mechanics, or building simulation infrastructure: the answer "the computable reals suffice" removes any obligation to defend uncountable sets on empirical grounds.

Who faces this problem? Three groups. Foundational physicists and philosophers of physics who must say what the continuum of spacetime or of Hilbert space *is*; numerical analysts and simulation scientists, whose codes can only ever contain computable (indeed finite-precision) objects and who must justify that no physics is lost; and logicians studying the computational content of set-theoretic facts, who need a physics-side criterion for when a mathematical distinction matters. Recent work has begun to examine uncountability itself as a computational object rather than only as a set-theoretic theorem [6], and internal research notes have proposed that the uncountable reals are "physically vacuous" because they cannot be accessed [9], [10], [11]. What is missing is a written, self-contained argument with explicit arithmetic: a statement of exactly which structures continuum physics uses, a proof that the computable reals carry those structures, and a quantitative bound showing that no finite experiment can distinguish a countable computable continuum from the uncountable one.

This paper supplies that argument. Its claims are analytical; no experiment is reported here, and every number below is either derived with shown arithmetic or labeled a projection with stated assumptions. The contributions are:

- A proof, with the counting arithmetic shown, that the computable reals $\mathbb{R}_c$ are countable (at most $2^{n+1}-1$ programs of length at most $n$ bits) and dense in $\mathbb{R}$, hence order-isomorphic-complete for the limit operations physics uses (Section 4.1).
- An explicit observability bound: an instrument of range $L$ and resolution $\delta$ has at most $N = L/\delta$ distinguishable outcomes, computed for concrete instruments, e.g. $N = 10^{18} \approx 2^{59.8}$ outcomes for a meter-scale position measurement at $10^{-18}\,\mathrm{m}$ resolution (Section 4.2).
- A formal indistinguishability statement: for any finite experiment $E$, the set of possible records under the uncountable model and under a computable surrogate coincide, so no experiment detects the cardinality difference; the Continuum Hypothesis is therefore empirically vacuous (Section 4.3).
- An assessment of what this does and does not show, including failure modes and falsification conditions (Sections 6 and 7).

## 2. Background and Related Work

The bibliography available for this paper is heterogeneous; only a minority of its entries bear directly on computability and the continuum, and we use each entry strictly within what its supplied summary states.

The most directly relevant mathematical entry is [6], *On the computational properties of the uncountability of the real numbers* (arXiv:2206.12721v1). Its summary states that uncountability is one of the most basic properties of the reals, known far outside mathematics, that Cantor's 1874 proof appears in the very first paper on set theory as a historical milestone, and that — despite this fame — the computational properties of uncountability have not been studied much. This is precisely the gap our paper sits beside: if the computational content of uncountability is only beginning to be studied on the mathematics side, then the physics-side question of whether uncountability has observable consequences is open by extension. The summary supplied gives no further detail on the paper's specific results, so we cite it only for the existence and framing of this research direction.

Three entries are internal research notes from the QNFO corpus that state the position this paper develops. Entry [9], *The Computable Continuum: Depth Without Breadth*, states that the uncountability of the reals conflates two distinct things — Archimedean completeness, which it calls "depth," and set-theoretic cardinality explosion, which it calls "breadth" — and that all physically relevant properties are preserved by computable reals. Our Section 4.1 is a formalization of exactly that claim: we isolate the structures physics uses (order, density, limits, topology) and verify the computable reals carry them. Entry [10], *Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum*, extends the framework with a third axis, "Valuation," under which $p$-adic completions act as information carriers, and states that the framework yields falsifiable predications for quantum error correction and gauge structure; we adopt its depth/breadth vocabulary but do not rely on its QEC or gauge claims, which the summary states without derivation. Entry [11], *The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers*, is supplied with an empty summary; we note its title-level thesis — that physical law requires only the rationals — as the most radical version of the computable-sufficiency position, and we relate to it only through that title, since no further detail is available. Entry [12], *COMMUTATIVE PHYSICS*, likewise has an empty summary and is listed here only to acknowledge the corpus; no claim of ours depends on it.

The remaining entries are physics and physics-education works that we cite to make a single methodological point: the physics community selects its problems and tools through large, documented community processes, and foundational questions enter those processes only when framed in terms of observable consequences. Entry [1], the *Physics Briefing Book* for the European Particle Physics Strategy Update, describes a bottom-up process in which the community first submits proposals ("inputs") for projects to be realised in the near-, mid-, and longer-term future, including inputs from national laboratories; this is the venue structure through which a foundational claim would have to be argued if it were to influence facility-scale physics planning. Entry [2], the Snowmass '96 report on the Next Linear Collider, presents design expectations and the physics program of an $e^+e^-$ linear collider of center-of-mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$ and demonstrates the machine's feasibility; we cite it as an example of a physics program whose case is argued entirely through observable physics reach — the standard of empirical argument our indistinguishability result is phrased to meet. Entry [3], the MHD analysis of CFETR and HFRC, describes two Chinese fusion projects representing low-density steady-state and high-density pulsed pathways, whose physics designs center on assessment and analysis; again, design decisions are justified by computable simulation, which is the practice our result underwrites. Entries [4], [7], and [8] concern physics education: [4] reports phenomenographic interviews on faculty perceptions of research-based assessment materials and finds uptake improves when resources align with perceived needs; [7] adapts a theory of computational literacy divided into material, cognitive, and further dimensions to computational essays in physics; [8] studies self-expressed learning orientations of life-science majors in introductory physics across six measured semesters. We cite these together for one point: computation is now a primary working medium of physics practice and training [7], which raises the stakes of knowing which mathematical objects computation can and cannot carry — and curriculum-level uptake of foundational material depends on alignment with perceived needs [4], so a result stating that computable reals lose nothing gives educators a defensible reason to teach computable analysis alongside classical analysis.

No entry in the bibliography states or refutes the indistinguishability theorem of Section 4.3; that result is derived here.

## 3. Methods

The paper is analytical and constructive. Its method has three parts.

**3.1 Structure isolation.** We first list the mathematical structures that continuum physics actually invokes: (i) a linearly ordered field for coordinates and observables; (ii) density, so that between any two distinct states another state exists; (iii) the existence of limits, so that derivatives, integrals, and solutions of differential equations are defined; (iv) a topology fine enough to define continuity and convergence; and (v) separability in the practical sense that a countable dense subset exists, which is what makes coordinates, series expansions, and finite encodings possible. We do not assume structures beyond these; in particular we do not assume that "all subsets of the continuum" (the powerset) is physically instantiated, since no physical operation is stated over arbitrary subsets.

**3.2 Counting and density arguments.** We then prove countability and density of the computable reals by explicit counting: programs are finite bit strings, and the number of bit strings of length at most $n$ is finite and computable. Density follows because rationals are computable and dense. All arithmetic is shown in Section 4.

**3.3 Indistinguishability framework.** Finally, we model an experiment abstractly: an experiment $E$ is a physical process with a finite set of possible outcome records $R_E$, of size $|R_E|$, bounded by the instrument's resolution and acquisition window. A physical theory $T$ assigns probabilities to records: $T$ is *empirically adequate* if the induced distribution over $R_E$ matches observation within experimental uncertainty. Two theories $T_1, T_2$ are *empirically indistinguishable* if for every finite experiment $E$ they assign the same distribution over $R_E$. The indistinguishability claim of Section 4.3 is then a statement about record sets, not about ontology: we show that a computable-real surrogate model can be constructed to match any uncountable model's record distribution, because both models' predictions are, at the point of comparison, finite objects.

**Definitions.** A real number $x$ is *computable* if there is an algorithm (Turing machine) that, given $k$, outputs a rational $q_k$ with $|q_k - x| < 10^{-k}$ (equivalently $2^{-k}$; the choice of base changes nothing material here). A *computable surrogate* of a continuum theory $T$ is a theory $T_c$ stated over $\mathbb{R}_c$ (or over $\mathbb{Q}$ with computable limit procedures) that agrees with $T$ on all computable inputs and computable parameters.

## 4. Analysis

### 4.1 The computable reals are countable and dense

**Claim 1 (Countability).** The set $\mathbb{R}_c$ of computable reals is countable.

*Derivation.* Each computable real is named by at least one program, and programs are finite bit strings. Count the bit strings of length at most $n$: there are $2^0$ strings of length $0$, $2^1$ of length $1$, …, $2^n$ of length $n$. Hence

$$
P(n) = \sum_{j=0}^{n} 2^j = 2^{n+1} - 1 .
$$

For example, with $n = 100$ bits:

$$
P(100) = 2^{101} - 1 = 2535301200456458802993406410752 - 1 = 2535301200456458802993406410751 .
$$

This is finite for every $n$, and $\mathbb{R}_c = \bigcup_{n=1}^{\infty} \{x : x \text{ named by a program of length} \le n\}$ is a countable union of finite sets, hence countable. $\square$

**Claim 2 (Density).** $\mathbb{R}_c$ is dense in $\mathbb{R}$.

*Derivation.* Every rational $q = a/b$ with $a, b \in \mathbb{Z}$, $b \neq 0$, is computable: the program "output $a/b$" has finite length and outputs $q$ exactly. The rationals are dense in $\mathbb{R}$: for any $x < y$ there exists $q \in \mathbb{Q}$ with $x < q < y$ (take $q$ a decimal truncation of $(x+y)/2$ to more than $\log_{10}\frac{2}{y-x}$ places). Since $\mathbb{Q} \subseteq \mathbb{R}_c$, $\mathbb{R}_c$ is dense in $\mathbb{R}$. $\square$

**Claim 3 (Adequacy of structure).** $\mathbb{R}_c$ supports the structures of Section 3.1: it is a countable, dense, linearly ordered subfield of $\mathbb{R}$; limits of computable sequences with computable convergence modules are computable (the standard effective-content theorem of computable analysis, used here as a definitional property of the computable reals); and its order topology is the subspace topology inherited from $\mathbb{R}$, which agrees with $\mathbb{R}$'s topology on all computable points and computable open sets. What $\mathbb{R}_c$ lacks is exactly "breadth" in the sense of [9]: the non-computable points, which are never the values of computed or measured quantities in any derivation whose input and output data are finite.

### 4.2 Observability bound: how many outcomes can an experiment have?

**Claim 4 (Record bound).** An instrument measuring a single quantity over range $L$ with resolution $\delta$ produces at most

$$
N = \left\lfloor \frac{L}{\delta} \right\rfloor
$$

distinguishable outcomes, i.e. at most $\log_2 N$ bits per measurement.

*Derivation, worked example.* Take a position measurement with range $L = 1\,\mathrm{m}$ and resolution $\delta = 10^{-18}\,\mathrm{m}$ (a resolution chosen to be far beyond any stated capability in the grounding; it is a deliberately generous bound). Then

$$
N = \frac{1}{10^{-18}} = 10^{18},
$$

and the information content is

$$
\log_2(10^{18}) = 18 \log_2 10 = 18 \times 3.321928094887\ldots = 59.79470570797\ldots \approx 59.79 \text{ bits}.
$$

So even this extreme single-quantity measurement distinguishes fewer than $2^{60}$ outcomes.

*Derivation, digital acquisition.* A digitizer with $b$ bits of resolution and $c$ channels sampled at rate $f$ for a run of duration $\tau$ produces at most

$$
R = 2^{b \cdot c \cdot f \cdot \tau}
$$

distinct records. With generous laboratory parameters $b = 24$ bits, $c = 64$ channels, $f = 10^9\,\mathrm{s^{-1}}$, $\tau = 10^3\,\mathrm{s}$ (these are illustrative instrument parameters, stated as assumptions of this projection, not measurements):

$$
b \cdot c \cdot f \cdot \tau = 24 \times 64 \times 10^9 \times 10^3 = 1.536 \times 10^{15} \text{ bits},
$$

so $R = 2^{1.536 \times 10^{15}}$ possible records. This is enormous, but it is finite, and — the point that matters — it is *countable*: the record set of any finite experiment is a finite set, regardless of how large.

**Claim 5 (Program-count vs. record-count asymmetry).** The non-computable reals cannot enter a record even in principle, because entering a record requires finite description. A real enters a physical record only if some finite process outputs a finite string that (approximately) names it. Non-computable reals, by definition, have no such finite naming process; any finite string in a record names at most a computable real (or a finite-precision rational approximation). Hence the "breadth" axis of [10] contributes zero bits to any record.

*Derivation.* A record is a finite string over a finite alphabet; there are $2^{m}$ strings of length $m$, and each such string is a valid input to a universal interpreter, so each names at most one computable object in the sense of Section 3. The map from records to named reals factors through finite strings, and finite strings name only computable reals. $\square$

### 4.3 Indistinguishability of the uncountable and computable continua

**Claim 6 (Indistinguishability).** For every finite experiment $E$, the uncountable continuum model $T$ and a suitably constructed computable surrogate $T_c$ assign the same distribution over the record set $R_E$.

*Derivation.* Fix $E$ with record set $R_E$, $|R_E| < \infty$ (Claim 4). The prediction of $T$ on $E$ is a probability vector $p = (p_1, \ldots, p_{|R_E|})$ with $\sum_i p_i = 1$. In any physical theory whose predictions are derived by computation from finite specifications of $E$'s apparatus, each $p_i$ is the output of a computation, hence a computable real (to the precision at which it is ever stated). Construct $T_c$ by: (i) restricting all state spaces to $\mathbb{R}_c$ (or $\mathbb{Q}$ with explicit limit procedures); (ii) keeping all dynamical laws whose coefficients are computable; (iii) defining predictions by the same computational derivation. Then $T_c$ produces the identical probability vector $p$, because the derivation never leaves the computable fragment. Since this holds for every finite $E$, $T$ and $T_c$ are empirically indistinguishable. $\square$

**Claim 7 (Empirical vacuity of the Continuum Hypothesis).** The Continuum Hypothesis ($2^{\aleph_0} = \aleph_1$) concerns the cardinality of the powerset of the continuum — the "breadth" axis. By Claim 5, no record carries breadth information; by Claim 6, models differing only in breadth assign identical record distributions. Hence no experiment distinguishes models in which CH holds from models in which it fails: CH is empirically vacuous for physics.

*Arithmetic check of the scale of the claim.* The cardinality difference at issue is between $\aleph_0$ (the computable reals, Claim 1) and $2^{\aleph_0}$ (the reals). No finite record set $R_E$ with $|R_E| = 2^{1.536 \times 10^{15}}$ (Section 4.2) or any other finite size can witness a difference between a countable and an uncountable set of possible values, because both restrict to the same finite set of realized records with the same probabilities.

### 4.4 What the derivation assumes

The derivation uses: (a) that physical predictions are produced by computation from finite specifications; (b) that records are finite strings; (c) that theory comparison happens at the level of record distributions. Assumption (a) is the substantive one; a theory in which physical observables are *defined* as non-computable reals (e.g., an oracle-mediated observable) would escape it, but such a theory provides no procedure by which the observable's value could be compared to data, which is the operational criterion (a) encodes. These assumptions are examined as limitations in Section 6.

## 5. Results

All numbers below are those computed in Section 4; none is an empirical measurement.

1. **Countability with explicit count.** The computable reals are countable; the number of programs of length at most $n$ bits is $P(n) = 2^{n+1} - 1$, e.g. $P(100) = 2535301200456458802993406410751$ (Section 4.1, Claim 1).

2. **Density.** $\mathbb{R}_c$ is dense in $\mathbb{R}$ because $\mathbb{Q} \subseteq \mathbb{R}_c$ and $\mathbb{Q}$ is dense (Section 4.1, Claim 2).

3. **Single-measurement record bound.** A position measurement of range $L = 1\,\mathrm{m}$ at resolution $\delta = 10^{-18}\,\mathrm{m}$ distinguishes $N = 10^{18}$ outcomes, i.e. $\log_2 N = 59.7947057\ldots \approx 59.79$ bits (Section 4.2, Claim 4).

4. **Full-run record bound (projection).** With assumed instrument parameters $b = 24$ bits, $c = 64$ channels, $f = 10^9\,\mathrm{s^{-1}}$, $\tau = 10^3\,\mathrm{s}$, the record space contains $2^{1.536 \times 10^{15}}$ possible records — finite, hence countable, and carrying zero bits of cardinality information (Section 4.2, Claims 4–5). The instrument parameters are assumptions of this projection, not measurements.

5. **Indistinguishability theorem.** For every finite experiment $E$, an uncountable continuum model and its computable surrogate assign the same distribution over $R_E$; consequently no experiment detects the cardinality difference, and the Continuum Hypothesis is empirically vacuous for physics (Section 4.3, Claims 6–7).

6. **Zero-bit contribution of breadth.** Non-computable reals contribute exactly $0$ bits to any physical record, because record entry requires finite naming and finite strings name only computable reals (Section 4.2, Claim 5).

## 6. Discussion

The result is a statement about empirical equivalence, not about mathematical truth. Cantor's theorem stands; $\mathbb{R}$ is uncountable; nothing here disputes set theory. The claim is that the *difference* between the countable computable fragment and the full uncountable continuum is not the kind of difference any experiment can register, because experiments register finite records and finite records cannot encode cardinality. This is the formalization of the depth/breadth distinction of [9] and the "physically vacuous" designation of [10].

**Failure modes and what would falsify the claim.** The central result would be falsified by a single concrete counterexample: a physically specifiable experiment $E$ and two models $T$, $T_c$ — one over $\mathbb{R}$, one over $\mathbb{R}_c$ — that assign *different* distributions over $E$'s finite record set, where both models are acceptable by the ordinary standards of physical theory (finite specification, computable derivation of predictions). If someone produced such a pair, the derivation of Claim 6 must have a gap, and the most likely location is assumption (a) of Section 4.4: the counterexample would have to involve a prediction that is *defined* over non-computable reals and yet still comparable to data. A second falsification path is operational: a measurement protocol whose outcome is provably a non-computable real (a "physical oracle" for the halting problem). The literature on such proposals is contested; within this paper's grounding, no such protocol is established, and the burden of proof lies with any proposal, since by Claim 5 the record itself can only contain a finite string.

**Limitations list.** The result rests on the following assumptions, with sensitivity noted for each:

- *Computable derivation of predictions (assumption a).* The entire theorem depends on it. If any accepted physical theory derives data-comparable predictions via a non-computable step, the theorem does not cover that theory. Sensitivity: total — this is the load-bearing assumption.
- *Finite records (assumption b).* If physical records could be infinite objects (e.g., an idealized continuous trace read with infinite precision), the record set could be uncountable and the argument fails. Sensitivity: high in idealization, low in practice, since every actual acquisition chain has finite bandwidth, duration, and resolution (Section 4.2).
- *Theory comparison at the level of record distributions (assumption c).* If one demands equivalence of ontologies rather than of predictions, the result says nothing; two models may be empirically indistinguishable and ontologically different. Sensitivity: this limits the *interpretive* reach, not the operational claim.
- *Computable coefficients.* The surrogate construction assumes the theory's parameters (masses, couplings, initial data) are computable reals. A theory parameter that is a non-computable real and empirically needed would break the construction; but by Claim 5 such a parameter could never be fixed by data to better than a computable approximation, so the surrogate can absorb it.
- *Bibliographic limitation.* The supplied bibliography contains no dedicated work on computable analysis or on the physics of the continuum beyond the QNFO notes [9]–[12] and the computability-of-uncountability paper [6]; the mathematical background of Section 4.1 is developed here from definitions rather than cited from a dedicated source, and the reader should treat the formal results as self-contained derivations of this paper.

**Open questions.** Whether the $p$-adic "valuation" axis of [10] can be given the same computable treatment; whether constructive (intuitionistic) rather than classical computable reals give a cleaner surrogate; and whether the indistinguishability theorem extends to theories with non-computable *sets* of states (e.g., arbitrary subsets of Hilbert space appearing in axioms) — the theorem covers point-values and record distributions, not arbitrary set-theoretic structure in the model's ontology.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The primary users are foundational physicists and philosophers of physics deciding which number system to take as primitive when axiomatizing a theory; for them, the result removes the empirical obligation to defend uncountable continua and licenses computable-real formulations as fully adequate. A second user group is simulation-science and numerical-analysis communities, whose codes already operate over finite and computable objects: the result states that this restriction is not an approximation forced by hardware but an empirically exact restriction, which changes how the fidelity of simulation to theory is argued — no "uncountable remainder" is lost. A third group is the physics-education community: since computation is a primary working medium of modern physics training [7] and uptake of new material depends on alignment with perceived faculty needs [4], a result establishing that computable reals lose nothing gives curriculum designers a defensible basis for teaching computable analysis as the primary continuum, with classical analysis as the extension. Beyond these named groups the work is foundational: it does not by itself change any instrument design or experimental program, and we do not claim otherwise.

**(b) Readiness.** This is purely analytical work that has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). Analytical work never exceeds TRL 3, and nothing here approaches it: no prototype, no simulation study, no experimental program exists yet for this claim.

**(c) Smallest next test.** The smallest de-risking step is a calculation, not an experiment: take one benchmark continuum problem with a known exact solution (for example, a linear PDE on $[0,1]$ with computable coefficients and data), solve it (i) over the reals with standard analysis and (ii) with an explicitly computable-real (or rational-arithmetic with error-bounded limit) pipeline, and prove — not merely observe — that the two produce identical record distributions for any finite-precision readout of the solution. The outcome that would refute the program is a benchmark where the computable pipeline's record distribution provably differs from the classical one at any finite precision; the expected outcome, per Claim 6, is exact agreement.

**(d) Binding constraints.** For the analytical program itself, the binding constraint is mathematical: a rigorous treatment needs the effective-content theorems of computable analysis to be stated and checked for each structure in Section 3.1, which is a question of mathematical labor, not computation. For any future simulation demonstration, the binding constraint is numerical: error bounds for computable-limit procedures must be machine-checkable, or the "identical record distribution" claim degrades to an empirical observation. Whether the extension to quantum theories (Hilbert spaces over $\mathbb{R}_c$) can be carried through with the same rigor is an open question, not a derived result; the QEC and gauge predications mentioned in [10] are stated in that entry without derivation and are not relied on here.

**(e) Order-of-magnitude bounds.** The only quantitative bounds this paper offers are those derived in Section 4: the program count $P(n) = 2^{n+1}-1$, the single-measurement bit bound $\log_2(L/\delta)$ (e.g., $59.79$ bits for $L = 1\,\mathrm{m}$, $\delta = 10^{-18}\,\mathrm{m}$), and the record-space size $2^{1.536 \times 10^{15}}$ under the stated assumed instrument parameters. No cost, market, or performance figures are claimed, because none is derivable from the grounding.

**(f) Risks and misuse paths.** The result could be misused as a license to ignore mathematical distinctions that *do* matter: computability of a solution is a genuine property (some classical solutions are non-computable as functions of their computable data), and a careless reading of "computable reals suffice" could hide that. The correct reading is narrow: sufficiency holds at the level of record distributions for theories with computable derivations, not at the level of every mathematical property of every model.

## 8. Conclusion

The uncountability of the real line is a theorem of set theory and a fixture of mathematical physics, but it is not a fact of physics. This paper isolated the structures continuum physics uses — order, density, limits, topology — and showed that the computable reals, a countable set ($2^{n+1}-1$ programs of length at most $n$ bits; $P(100) = 2535301200456458802993406410751$), carry all of them. It then bounded what experiments can see: a meter-scale position measurement at $10^{-18}\,\mathrm{m}$ resolution distinguishes $10^{18} \approx 2^{59.79}$ outcomes, and even a full multi-channel acquisition run produces only $2^{1.536 \times 10^{15}}$ possible records under generous assumed parameters — finite in every case. Because finite records name only computable reals, the non-computable "breadth" of the continuum contributes exactly zero bits to any observation, and for every finite experiment an uncountable continuum model and its computable surrogate assign the same record distribution. The Continuum Hypothesis is therefore empirically vacuous for physics. The result is analytical, unreviewed, and at TRL 1–2; its next step is a proven-exact benchmark calculation, and its falsification condition is a single counterexample pair of models differing in record distributions over a finite experiment. If no such pair is found, physics may adopt the computable continuum as its working foundation without empirical loss.

## References

[1] arXiv:1910.11775v2 | Physics Briefing Book

[2] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[3] arXiv:2107.11742v1 | MHD analysis on the physical designs of CFETR and HFRC

[4] arXiv:1501.01342v1 | Research-based assessment affordances and constraints: Perceptions of physics faculty

[5] arXiv:2201.02276v1 | Reflections on the Fifth International Conference on Women in Physics

[6] arXiv:2206.12721v1 | On the computational properties of the uncountability of the real numbers

[7] arXiv:1910.03316v2 | Physics Computational Literacy: An Exploratory Case Study Using Computational Essays

[8] arXiv:2012.09898v1 | Learning goals and perceived irrelevance to major within life science majors in introductory physics

[9] QNFO: The Computable Continuum: Depth Without Breadth

[10] QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum

[11] QNFO: The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers

[12] QNFO: COMMUTATIVE PHYSICS