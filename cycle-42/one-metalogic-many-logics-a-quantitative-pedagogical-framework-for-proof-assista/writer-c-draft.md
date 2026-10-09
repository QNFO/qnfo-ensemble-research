# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof-Assistant-Based Logic Teaching with LogiKEy

## Abstract

We develop a quantitative pedagogical framework for teaching logic to mixed cohorts of computer science, mathematics, and philosophy students using the LogiKEy methodology, in which classical higher-order logic (HOL) serves as a universal metalogic and object logics—classical and non-classical alike—are introduced through semantical embeddings in a single proof assistant such as Isabelle/HOL. Our contribution is to complement the qualitative, example-driven curriculum design of LogiKEy with explicit combinatorial analysis of its graded example sequence: liars-and-truth-tellers puzzles, the Wise Men puzzle, Boolos's curious inference, Chisholm's paradox, and Gödel's ontological argument. For each stage we derive, with full arithmetic, the size of the relevant search or model space, showing how representational choices change these quantities by orders of magnitude and thereby motivate each transition in the curriculum. We further derive a projection for course-time allocation under stated assumptions. We argue that the quantitative lens supports the methodological claim that embedding object logics in HOL is pedagogical pluralism rather than monism, and we identify failure modes, falsification conditions, and open questions for empirical validation.

## 1. Introduction

Teaching logic to a mixed audience is notoriously difficult: computer science students want executable reasoning tools, mathematics students want rigor and generality, and philosophy students want engagement with genuine philosophical puzzles. The LogiKEy methodology [1], [2] addresses this by using classical higher-order logic (HOL) as a universal metalogic: object logics are encoded by defining their semantics inside a proof assistant (typically Isabelle/HOL), so that one environment—with its automated theorem provers and (counter-)model finders—becomes the laboratory in which students learn, experiment with, and compare logics.

The LogiKEy paper presents a graded sequence of classroom examples, each transition motivated by a limitation of the preceding representation: a liars-and-truth-tellers puzzle leads from propositional to modal logic; the Wise Men puzzle leads to dynamic epistemic logic; Boolos's curious inference illustrates what a higher-order metalogic buys even for automated proof search; Chisholm's paradox moves into deontic logic and then dyadic deontic logic; and Gödel's ontological argument reaches research-level metaphysics [2].

What the existing treatment lacks—and what this paper supplies—is a quantitative account of *why* these transitions are pedagogically forced. Our central observation is that each representational upgrade in the sequence changes a measurable quantity: the size of the state space a student must search, the number of models a model finder must enumerate, or the number of assumptions a proof must manage. When these quantities are computed explicitly, the motivation for each logical enrichment becomes a number rather than an intuition. We derive these numbers with full arithmetic in Section 4, report them in Section 5, and use them in Section 6 to defend the pluralism claim and to state falsification conditions.

Throughout, "semantical embedding" means a shallow embedding: the syntax and semantics of an object logic are defined as HOL constants and functions, so that the object logic's theorems become HOL theorems about the embedding, without generating a new object-level deductive system. "Kripke model" means a tuple $\mathcal{M} = (W, R_1, \ldots, R_n, V)$ of worlds $W$, accessibility relations $R_i$, and a valuation $V$.

## 2. Background and Related Work

The LogiKEy methodology itself is presented in [1] and [2], which report over a decade of use in courses, summer schools, and tutorials; [2] is the full paper and [1] the associated arXiv record. Both emphasize the pedagogical case for proof assistants and the graded example sequence that we analyze quantitatively here.

On the question of *what* to teach, [3] surveys the prospects for mathematical logic in the twenty-first century across recursion theory, proof theory, model theory, and set theory, and argues that the boundaries between these areas—and between logic and computer science—are increasingly porous. This supports the LogiKEy premise that a single course should expose students to multiple logics rather than one canonical system. [4] argues for teaching modal logic from a philosophy-first agenda, motivated by central problems of philosophy and language rather than by mathematical issues; our framework is complementary: the quantitative state-space analysis of Section 4 gives philosophy students a concrete handle on why modal operators are needed, while preserving the philosophical motivation [4] demands. [5] documents the opposite end of the audience spectrum: in Information Systems curricula logic plays a practically non-existent role, and significant adaptation of content and methodology is required; this confirms that mixed-cohort teaching cannot assume a uniform background, strengthening the case for a single tool-based environment that scales across backgrounds.

On alternative reconceptions of logic, [6] develops computability logic as a formal theory of computability rather than truth, understanding computational problems as games and logical operators as operations on them; [8] extends this program toward applied theories. These works illustrate, from a different direction, the logico-pluralistic thesis that "logic" is not one fixed system—a thesis LogiKEy operationalizes pedagogically by making pluralism concrete inside one metalogic. [7] studies logics defined by imposing a variable inclusion condition on a given consequence relation $\vdash$, with Plonka sums of matrices as the algebraic counterpart; this shows that even the internal structure of a single consequence relation can fragment into a family of logics, reinforcing the need for environments in which such families can be compared systematically. [9] introduces the neutral temporal deontic STIT logic TDS, proving soundness and completeness with respect to relational frames without utilitarian commitments; this is directly relevant to the deontic stage of the LogiKEy sequence, since it demonstrates how deontic notions can be modeled with explicitly controlled commitments—an exercise students can reproduce as an embedding.

Finally, the QNFO corpus offers critique-first reconstructions of logical foundations: [10] collects the Continuum Critique Trilogy; [11] argues that Boolean logic reifies the void (the unmarked state) into falsity, proposing a distinction-logic reconstruction labeled as conjecture; [12] argues that $1 + 1 = 2$ presupposes distinguishable marks and that idempotence $AA = A$ is primitive; and [13] develops a calculus of re-entrant distinctions generating the constants $e$ and $\pi$. We treat these as speculative alternatives whose status—conjecture with falsifiability conditions, by their own description [11], [12]—illustrates precisely the kind of pluralistic landscape a LogiKEy-style course can host: a student can embed such a distinction-logic in HOL and test its consequences against the classical baseline, rather than debate it informally.

## 3. Methods

Our method is combinatorial analysis of the LogiKEy example sequence [2]. For each curricular stage we identify the representational choice, define the associated search or model space, and compute its cardinality exactly. The stages and their formal objects are:

1. **Propositional stage (liars and truth-tellers).** A puzzle with $n$ islanders, each either a knight (truth-teller) or knave (liar). An assignment is a function $\sigma : \{1, \ldots, n\} \to \{K, N\}$; the raw state space is $\{K, N\}^n$ with cardinality $2^n$. Each uttered statement $S_i$ imposes a constraint; the solver searches the constrained space.

2. **Modal stage.** The same puzzle is re-modeled with a Kripke model $\mathcal{M} = (W, R, V)$, where uncertainty about who is what is represented by accessibility between worlds. We count possible accessibility relations over $|W|$ worlds.

3. **Dynamic epistemic stage (Wise Men puzzle).** Epistemic models for $n$ agents over $|W|$ worlds, and the product-update rule of dynamic epistemic logic (DEL), where a factual model of size $|W|$ is updated by an action model of size $|E|$, yielding a product model of size $|W| \cdot |E|$.

4. **Higher-order stage (Boolos's curious inference).** We contrast the propositional/first-order encoding, where automated search operates over a finite assignment space of $2^k$ rows for $k$ atoms, with the higher-order encoding where comprehension principles compress the search.

5. **Deontic stage (Chisholm's paradox).** With $m$ prima facie obligations, each either fulfilled or violated, we count the combinatorics of the $2^m$ fulfillment profiles and show how dyadic deontic logic restructures the space.

6. **Metaphysical stage (Gödel's ontological argument).** We count the axiomatic commitments: with $a$ axioms over a positive-property predicate, we compute the number of property assignments consistent with a single axiom as a function of the property universe size $p$.

For course-planning we additionally derive a labeled projection of time allocation (Section 4.7), with all assumptions stated. All arithmetic is shown in Section 4; Section 5 reports only those computed values or clearly labeled projections.

## 4. Analysis

### 4.1 Propositional state space (liars and truth-tellers)

Input: $n = 3$ islanders (the minimal nontrivial puzzle size used in classroom presentations of the sequence [2]). Each islander is a knight or a knave, so the raw assignment space has

$$|\{K, N\}^3| = 2^3 = 8$$

assignments. Each statement $S_i$ uttered by islander $i$ imposes one binary constraint: for a knight, $S_i$ must be true; for a knave, $S_i$ must be false. In the worst case each constraint is independent and halves the space, so after all three statements the consistent set has size at most

$$2^{3 - 3} = 2^0 = 1$$

assignment, and in the best case (degenerate statements) remains $2^3 = 8$. The pedagogical point, made quantitative: propositional logic suffices only when the constraint structure is statically known; the *reasoning about who knows what* is invisible in the 8-row space, which motivates the modal upgrade.

### 4.2 Modal state space

Input: the same puzzle re-modeled with $|W| = 8$ worlds (one per propositional assignment, from Section 4.1) and a single epistemic agent (the puzzle solver). The number of distinct binary accessibility relations on a set of $|W| = 8$ worlds is

$$2^{|W| \cdot |W|} = 2^{8 \times 8} = 2^{64} = 18{,}446{,}744{,}073{,}709{,}551{,}616 \approx 1.84 \times 10^{19}.$$

If we restrict to reflexive relations (knowledge, as standard in epistemic logic, requires reflexivity), the diagonal pairs $(w, w)$ are fixed, leaving $8 \times 7 = 56$ off-diagonal pairs, so

$$2^{56} = 72{,}057{,}594{,}037{,}927{,}936 \approx 7.21 \times 10^{16}$$

reflexive relations. The jump from $8$ (Section 4.1) to $2^{64} \approx 1.84 \times 10^{19}$ candidate models is the quantitative signature of the modal upgrade: the student's modeling resources have expanded from truth values to *entire relations*, and the proof assistant's model finder becomes essential precisely because manual search over $10^{19}$ candidates is impossible.

### 4.3 Dynamic epistemic product update (Wise Men puzzle)

Input: the standard Wise Men puzzle has $n = 3$ agents and, in its epistemic encoding, a factual model with $|W| = 8$ worlds (as in Section 4.1, since each wise man's spot is white or black, $2^3 = 8$ configurations). The public announcement "at least one of you has a white spot" eliminates the all-black world, and the successive "I do not know" announcements eliminate further worlds. After the first announcement the model has

$$|W| - 1 = 8 - 1 = 7$$

worlds. In DEL, an action model with $|E|$ events updates a factual model of $|W|$ worlds to a product model of size

$$|W_{\text{new}}| = |W| \cdot |E|.$$

For the announcement action modeled with a single event ($|E| = 1$) restricted to the $7$ surviving worlds, the updated model has size $7 \times 1 = 7$; the elimination is represented by the accessibility restriction, not by world creation. The quantitative lesson: public announcements *shrink* models ($8 \to 7$), whereas private or more complex actions with $|E| > 1$ can *grow* them; e.g., an action model with $|E| = 3$ events over the original $|W| = 8$ worlds yields $8 \times 3 = 24$ worlds. Students thus see, numerically, why dynamic epistemic logic needs richer machinery than static epistemic logic.

### 4.4 Higher-order compression (Boolos's curious inference)

Input: Boolos's curious inference, in its propositional abstraction, involves a schema whose automated first-order proof search is famously intractable, while the higher-order encoding with comprehension succeeds quickly [2]. We compute the propositional baseline: if the schema is instantiated with $k = 10$ atoms, a truth-table search enumerates

$$2^{10} = 1024$$

rows. For a first-order encoding with a domain of size $d = 10$ and a binary predicate, the number of possible interpretations of the predicate is

$$2^{d^2} = 2^{100} \approx 1.27 \times 10^{30}$$

(since $2^{100} = (2^{10})^{10} = 1024^{10}$; numerically $2^{100} = 1{,}267{,}650{,}600{,}228{,}229{,}401{,}496{,}703{,}205{,}376 \approx 1.27 \times 10^{30}$). A model finder that searches interpretations exhaustively faces $\approx 1.27 \times 10^{30}$ candidates. The higher-order encoding, by contrast, quantifies over predicates directly and lets comprehension axioms constrain the search; the quantitative contrast between $2^{100} \approx 1.27 \times 10^{30}$ candidate first-order interpretations and the comprehension-constrained higher-order search is what "a higher-order metalogic buys" in practice [2]. We do not report empirical prover timings, as none are computed here; the claim we make is the combinatorial one above.

### 4.5 Deontic combinatorics (Chisholm's paradox)

Input: Chisholm's paradox, in its canonical form, involves $m = 2$ obligations (the standard presentation: a man's duty to go to his neighbor's assistance and his duty to tell them he will come; we use the general $m$-obligation form with $m = 2$ for the canonical case). Each obligation is either fulfilled or violated, giving

$$2^m = 2^2 = 4$$

fulfillment profiles. The paradox arises because the standard monotonic deontic operator $O$ forces, from $O A$ and $O B$ and the factual violation of $A$, an inconsistent set of commitments; the number of inconsistent profiles derivable under the classical $O$ is what motivates the dyadic operator $O(B/A)$ (obligation $B$ under condition $A$). With the dyadic operator, the $4$ profiles are reorganized as conditional commitments attached to each violation state, and consistency is restored profile by profile. For the general case with $m$ obligations, the profile space is $2^m$; for $m = 3$ (a three-obligation classroom variant), $2^3 = 8$ profiles. The quantitative observation: the paradox is not a growth problem (the space stays at $2^m$) but a *consistency* problem—dyadic deontic logic changes the structure, not the size, of the space, which is exactly why the transition must be motivated philosophically rather than computationally.

### 4.6 Axiomatic commitments (Gödel's ontological argument)

Input: Gödel's ontological argument, as embedded in the LogiKEy sequence [2], posits a positive-property predicate $P$ and a small set of axioms (typically $a = 3$ core axioms in classroom presentations: $P$-positivity axiom, the axiom that a property is positive iff its negation is not positive, and the God-like-property axiom). Given a universe of $p = 5$ candidate properties (the classroom-sized property universe), the number of possible interpretations of $P$ over the property universe is

$$2^p = 2^5 = 32.$$

Each axiom eliminates some interpretations; if each of the $a = 3$ axioms is independent and halves the space, the consistent set has size at least

$$2^{p - a} = 2^{5 - 3} = 2^2 = 4$$

interpretations. The pedagogical point, made quantitative: even a research-level metaphysical argument, when embedded in HOL, reduces to a small, checkable space of property interpretations ($32$ raw, at least $4$ consistent under the stated independence assumption), which the proof assistant's model finder can enumerate exhaustively. This is the sense in which the embedding "brings it to a research-level argument" while keeping it classroom-manageable [2].

### 4.7 Course-time projection (labeled projection)

Assumption set (stated explicitly, not measured): a semester course of $T_{\text{sem}} = 14$ weeks with one $2$-hour session per week gives $14 \times 2 = 28$ contact hours. If the six stages of Section 3 are allocated in the ratio $2 : 3 : 3 : 4 : 4 : 4$ (reflecting increasing sophistication, per the graded sequence [2]), the total ratio weight is $2 + 3 + 3 + 4 + 4 + 4 = 20$, so each weight unit is

$$\frac{28}{20} = 1.4 \text{ hours},$$

and the stage allocations are $2 \times 1.4 = 2.8$, $3 \times 1.4 = 4.2$, $3 \times 1.4 = 4.2$, $4 \times 1.4 = 5.6$, $4 \times 1.4 = 5.6$, and $4 \times 1.4 = 5.6$ hours respectively. Sum check: $2.8 + 4.2 + 4.2 + 5.6 + 5.6 + 5.6 = 28.0$ hours. This is a projection under stated assumptions, not an empirical measurement; actual LogiKEy course timings are not reported in quantitative form in [2].

## 5. Results

All values below are computed in Section 4 with shown arithmetic; the single projection (R7) is labeled as such.

- **R1.** The propositional state space for $n = 3$ islanders is $2^3 = 8$ assignments, reducible to as few as $1$ under three independent statement constraints (Section 4.1).
- **R2.** The modal re-modeling over $|W| = 8$ worlds admits $2^{64} = 18{,}446{,}744{,}073{,}709{,}551{,}616 \approx 1.84 \times 10^{19}$ arbitrary accessibility relations, or $2^{56} \approx 7.21 \times 10^{16}$ reflexive ones (Section 4.2).
- **R3.** The Wise Men factual model shrinks from $|W| = 8$ to $7$ worlds under the first public announcement; a DEL action model with $|E| = 3$ events over the original $8$ worlds yields $8 \times 3 = 24$ worlds (Section 4.3).
- **R4.** A first-order encoding with domain size $d = 10$ and one binary predicate presents $2^{100} \approx 1.27 \times 10^{30}$ candidate interpretations to automated search; the propositional abstraction with $k = 10$ atoms has $2^{10} = 1024$ rows (Section 4.4).
- **R5.** Chisholm's paradox with $m = 2$ obligations has $2^2 = 4$ fulfillment profiles; a three-obligation variant has $2^3 = 8$; the paradox is structural (consistency), not combinatorial (size) (Section 4.5).
- **R6.** Gödel's ontological argument over a $p = 5$-property universe has $2^5 = 32$ interpretations of the positivity predicate $P$, reduced to at least $2^{5-3} = 4$ under three independent axioms (Section 4.6).
- **R7 (projection).** Under the stated assumptions of Section 4.7 ($28$ contact hours, allocation ratio $2:3:3:4:4:4$), the six stages receive $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ hours respectively; uncertainty is dominated by the assumed ratio, which we have not validated empirically.

The headline quantitative contrast is R1 vs. R2: the modal upgrade expands the student's search space from $8$ to $\approx 1.84 \times 10^{19}$, a factor of

$$\frac{2^{64}}{2^3} = 2^{61} \approx 2.31 \times 10^{18}$$

(checked: $2^{61} = 2{,}305{,}843{,}009{,}213{,}693{,}952 \approx 2.31 \times 10^{18}$), which is precisely why the proof assistant's model finder, not pencil and paper, must carry the modal stage.

## 6. Discussion

**Limitations.** Our analysis is combinatorial, not empirical: we compute sizes of search and model spaces but do not measure student learning outcomes, prover runtimes, or actual course timings. The independence assumptions in Sections 4.1, 4.4, and 4.6 (each constraint halving the space) are upper-bound-friendly idealizations; real puzzle constraints are rarely independent, so the true consistent sets may be larger than our minima. The property universe size $p = 5$ in Section 4.6 is a classroom convenience, not a claim about Gödel's argument as studied in the literature. The time-allocation projection R7 rests on an unvalidated ratio.

**Failure modes.** If a classroom puzzle's constraint structure is highly redundant, the propositional stage may already collapse to a unique solution with negligible search, undercutting the quantitative motivation for the modal upgrade. Conversely, if the modal stage is taught with tiny models ($|W| = 2$ or $3$), the $2^{64}$ figure overstates what students actually face, and the pedagogical force of R2 diminishes. The dyadic-deontic transition (R5) is motivated structurally, not numerically; a course designer relying on our quantitative lens alone would miss it.

**What would falsify our claims.** The central claim—that each LogiKEy transition is accompanied by a quantitative jump that motivates it—would be falsified if a stage transition could be exhibited where the relevant search or model space *shrinks* or stays constant while the transition is still pedagogically necessary for reasons our framework cannot capture. We have partially conceded this for R5 (deontic): the space stays at $2^m$, so our framework explains the dyadic transition only qualitatively. The pluralism claim—that HOL embedding is pedagogical pluralism rather than monism—would be falsified if it could be shown that the embedding practice systematically privileges classical reasoning in ways that distort students' understanding of non-classical logics (e.g., by making classical validity the default notion of theoremhood); we know of no quantitative test of this, and it remains open.

**Arguing against ourselves.** A critic may say the combinatorial numbers are trivia: no student ever enumerates $2^{64}$ models, so the number motivates tooling, not understanding. We reply that the number explains *why the tool is non-optional*, which is itself a pedagogical lesson about the relationship between logic and computation. A stronger objection: the QNFO-style critique-first programs [11], [12], [13] suggest that even the classical HOL metalogic rests on contestable primitives (e.g., the reification of the void into falsity [11]); if that critique is right, the LogiKEy "universal metalogic" is universal only relative to a contested foundation. Our response is that the embedding methodology is precisely the right arena for such contests—a distinction-logic [11] can be embedded and tested—but we concede this is a programmatic response, not a demonstration. Finally, the computability-logic tradition [6], [8] and the variable-inclusion fragment construction of [7] show that the space of logics is far richer than the six stages we quantify; our framework covers the LogiKEy sequence, not the whole logico-pluralistic landscape.

**Open questions.** (i) Do the computed space sizes correlate with measured student difficulty? (ii) Can the deontic stage be given a quantitative motivation, e.g., by counting inconsistent derivations rather than profiles? (iii) Does the portability of the approach beyond Isabelle [2] preserve the quantitative profile, given different prover architectures?

## 7. Conclusion

We have supplied a quantitative complement to the LogiKEy methodology for teaching logic with proof assistants [1], [2]. By computing, with full arithmetic, the state spaces, model counts, and axiomatic commitment spaces associated with each stage of the graded example sequence—from $8$ propositional assignments through $2^{64} \approx 1.84 \times 10^{19}$ modal accessibility relations, $8 \to 7$ and $8 \times 3 = 24$ dynamic epistemic model sizes, $2^{100} \approx 1.27 \times 10^{30}$ first-order interpretations, $2^m$ deontic fulfillment profiles, and $32 \to 4$ ontological-argument property interpretations—we have shown that the pedagogical transitions in the sequence are, in most cases, accompanied by measurable jumps in representational capacity. The quantitative lens makes the case for proof-assistant-based, logico-pluralistic teaching sharper: the tool is not a convenience but a necessity once the search spaces exceed human enumeration, and the single metalogic is the price of a unified laboratory in which pluralism is practiced rather than proclaimed. Empirical validation of the correlation between these computed quantities and learning outcomes remains the principal open task.

## References

[1] arXiv Query: search_query=&id_list=2610.08214&start=0&max_results=1 — Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology (abstract record).

[2] arXiv:2610.08214v1 | Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology.

[3] arXiv:cs/0205003v1 | The prospects for mathematical logic in the twenty-first century.

[4] arXiv:1507.04701v1 | To Teach Modal Logic: An Opinionated Survey.

[5] arXiv:1507.03687v1 | Teaching Logic to Information Systems Students: Challenges and Opportunities.

[6] arXiv:cs/0404023v2 | Propositional computability logic I.

[7] arXiv:1804.08897v4 | Logic of left variable inclusion and Plonka sums of matrices.

[8] arXiv:0805.3521v4 | Towards applied theories based on computability logic.

[9] arXiv:1907.03265v4 | A Neutral Temporal Deontic STIT Logic.

[10] QNFO: The Continuum Critique Trilogy | DOI 10.5281/zenodo.21691415.

[11] QNFO: The Void Is Not False: Recovering the Unmarked State in Logic from the Calculus of Indications | DOI 10.5281/zenodo.21916970.

[12] QNFO: The Idempotent Core: Quantity as Broken Distinction and the Hidden Assumptions of Arithmetic and Algebra | DOI 10.5281/zenodo.21916939.

[13] QNFO: The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference | DOI 10.5281/zenodo.21964453.