# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof-Assistant-Based Logic Teaching with LogiKEy (Revised)

## Abstract

Teaching logic to mixed cohorts of computer-science, mathematics, and philosophy students is costly because each cohort brings distinct expectations and because curricula traditionally fragment into separate courses on propositional, modal, epistemic, and deontic logic. The specific gap addressed here is the lack of a quantitative account of why each pedagogical transition in the LogiKEy sequence is forced. The approach combines shallow semantical embeddings of object logics in classical higher-order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each stage of the graded example sequence. The principal results are: (1) the propositional stage admits $2^{3}=8$ assignments with a single survivor; (2) the modal re-modeling yields $2^{64}\approx1.84\times10^{19}$ arbitrary accessibility relations, or $2^{56}\approx7.21\times10^{16}$ reflexive ones; (3) the Wise Men dynamic epistemic model follows the trajectory $8\to7\to6\to4$, a shrinkage factor of $7/4=1.75$ from the first announcement onward, with the shrinkage produced by semantic restriction of the product update rather than by the product itself; (4) Boolos's curious inference generates a proof-length tower reaching $L_{5}\approx10^{19\,728}$ under the stated worst-case recurrence; (5) a first-order interpretation space of size $2^{100}\approx1.27\times10^{30}$ contrasts with a higher-order comprehension-constrained search; (6) deontic combinatorics remain at $2^{m}$ profiles while the consistency problem changes structurally; (7) Gödel's ontological argument reduces to $2^{5}=32$ raw positivity-predicate interpretations and, under a stated independence assumption, an estimated minimum of $2^{2}=4$ consistent ones; (8) a course-time projection allocates $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours to the six stages. These numbers turn pedagogical motivations into explicit quantitative checkpoints, clarifying when automation, richer semantics, or higher-order reasoning become indispensable.

## 1. Introduction

A logic classroom that contains only computer-science students can assume comfort with formalism and an interest in verification; a classroom that contains only philosophy students can assume interest in argument analysis but not in type theory. A mixed classroom—computer-science, mathematics, and philosophy students together—inherits all of the difficulties and none of the homogeneity. Two failure modes are common. The first is fragmentation: each logic (propositional, modal, epistemic, deontic) is taught as a separate subject with separate notation, separate tools, and separate exercises, so students leave with a portfolio of disconnected techniques rather than a unified competence. The second is monotony: a single logic (usually classical first-order) is taught as if it exhausted the field, leaving philosophy students without the non-classical logics their discipline demands and computer-science students without the modeling resources (agents, knowledge, obligation, action) their discipline increasingly uses.

The LogiKEy methodology proposes a third way: logico-pluralism on a single technical substrate. Classical higher-order logic (HOL) serves as a universal metalogic. Each object logic—classical or non-classical—is encoded by defining its semantics in HOL: possible worlds become HOL individuals, accessibility relations become HOL relations on those individuals, modal operators become HOL functions quantifying over worlds. Through such shallow semantical embeddings, one proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes a single laboratory in which students define logics, prove their metatheorems, and compare their expressive power. The graded sequence of classroom examples—liars-and-truth-tellers puzzles, the Wise Men puzzle, Boolos's curious inference, Chisholm's paradox, and Gödel's ontological argument—illustrates how each representational upgrade expands a measurable quantity (search space size, model-enumeration burden, proof length) and thereby motivates a pedagogical transition.

This paper supplies the quantitative layer that the qualitative presentation of the sequence leaves implicit. For each stage, the representational choice is identified, the associated search or model space is defined, and its cardinality is computed exactly from stated inputs by elementary arithmetic. Where a claim goes beyond exact computation—most prominently the course-time allocation—it is labeled a projection and its assumptions are stated. No empirical learning outcomes or prover timings are reported, because none are measured here; the claims are combinatorial.

Two corrections relative to the previously published version of this analysis are incorporated throughout. First, the Wise Men model trajectory is $8\to7\to6\to4$ with shrinkage factor $7/4=1.75$ from the first announcement onward; the earlier statement of a $8\to7\to6\to5\to4$ trajectory with factor $8/4=2$ was inconsistent with the stage-by-stage derivation and is withdrawn. Second, the description of public announcement in dynamic epistemic logic has been corrected: the product update with a one-event action model does not by itself shrink the model; the shrinkage arises because the update is restricted to worlds at which the announced formula holds. Both corrections are derived in Section 4.3.

The contributions of this paper are:

* **C1.** Derivation of the exact propositional assignment space and survivor count for the liars-and-truth-tellers puzzle (Section 4.1, Result R1).
* **C2.** Computation of the number of arbitrary and reflexive accessibility relations for the modal re-modeling (Section 4.2, Result R2).
* **C3.** Corrected quantitative analysis of the Wise Men dynamic epistemic model trajectory, including the role of semantic restriction in the product update (Section 4.3, Result R3).
* **C4.** Construction of the proof-length tower for Boolos's curious inference under the stated recurrence, and comparison with first-order interpretation counts (Section 4.4, Result R4).
* **C5.** Enumeration of deontic fulfillment profiles and identification of the structural nature of Chisholm's paradox (Section 4.5, Result R5).
* **C6.** Calculation of the positivity-predicate interpretation space for Gödel's ontological argument, with the independence assumption made explicit (Section 4.6, Result R6).
* **C7.** Projection of course-time allocation under explicit assumptions (Section 4.7, Result R7).
* **C8.** Presentation of the quantitative contrast factor between the propositional and modal stages (Section 5, Result R8).

## 2. Background and Related Work

The LogiKEy methodology itself is presented in [1] and [2], which report an approach used for more than a decade in courses, summer schools, and tutorials. The source text states that LogiKEy uses classical HOL as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics, so that a single proof assistant with its automated theorem provers and (counter-)model finders becomes one environment in which students learn, experiment with, and compare logics [1]. Its account of the technical substrate explains that classical higher-order logic, Church's simple type theory, adds two decisive capabilities: quantification over functions and predicates, which makes HOL expressive enough to talk about other logics—their formulas, their notions of truth, their models—and $\lambda$-abstraction, which makes encodings compositional and gives them the flavor of elementary functional programming, so that "a modal connective, for instance, simply becomes a function on world-dependent propositions" [2]. The same text is explicit about evidential status: what is *established* is the machine-checked formal results of the example ladder and the methodological claim that one metalogic carries all of them, while the claim that a course built this way can be run with a mixed cohort is *documented only by the authors' own experience* [2]. The present work accepts this framework and adds explicit quantitative checkpoints to each transition; it likewise makes no empirical claims beyond what the combinatorics support.

On the question of *what* to teach, [3] presents four authors' speculations on the future of mathematical logic in the twenty-first century across recursion theory, proof theory, model theory, and set theory. Its record of the panel discussion notes disagreement about whether the most important progress comes from applications or from internal developments, while reporting that "quite a few people... felt that applications to computer science will be of great importance" [3]. Its proof-theory section, by Sam Buss, surveys presently active areas in proof theory and computer science logic, makes predictions about future developments, and concludes "with an exhortation for mathematical logicians to pay more attention to applications of logic in computer science" [3]. This supports the LogiKEy bet that proof-assistant literacy is a transferable skill rather than a specialist niche, and the panel's picture of contested boundaries between logic and computer science supports exposing students to multiple logics in one course rather than a single canonical syllabus.

On the teaching of modal logic specifically, [4] argues for an agenda "chiefly inspired by the relationships between modal logic and philosophy," in which the interest of modal logic does not stem mainly from mathematical issues but "is motivated by central problems of philosophy and language" [4]. Its conclusion states the central tenet as follows: "Instead of focusing on the formal and mathematical aspects of modal logic, it is convenient to return to the origins and search firstly for the philosophical motivation behind the primeval ideas," with the dose of mathematical modal logic to be estimated from that point of view [4]. This is directly relevant to the LogiKEy sequence: the transition from propositional to modal logic in [1] is driven by a puzzle about truth-telling and knowledge, not by Kripke completeness theorems, in line with [4]'s recommendation that philosophical motivation lead. The quantitative state-space analysis provided here gives philosophy students a concrete handle on why modal operators are needed while preserving the philosophical motivation identified in [4].

The problem of heterogeneous student populations is studied in [5], which examines teaching logic to information-systems students. The source argues that, in contrast to computer science where the fundamental role of logic is widely recognized, logic plays a practically non-existent role in information-systems curricula, and that "instead of Logic's exclusion from the IS curriculum, a significant adaptation of the contents, as well as teaching methodologies, is required for an alignment with the needs of IS practitioners" [5]. Its practical section observes that, due to the density of IS curricula, "one cannot afford to have one course on pure formal logic and then another on formal methods," so one must develop a mixture of introductory formal logic with formal methods relevant to the domain [5]. The LogiKEy methodology can be read as one systematic answer to this challenge: the adaptation is not a watered-down syllabus but a uniform tool-based environment in which students with different backgrounds enter through different object logics. The same source calls for more empirical evidence, in the spirit of the Beseme project, that such courses are useful for practitioners [5]; the present paper's combinatorial checkpoints are offered as design inputs for exactly such future empirical work, not as a substitute for it.

An alternative re-foundation of logic is computability logic, presented in [7] as "a semantical platform and program for redeveloping logic as a formal theory of computability, as opposed to a formal theory of truth which logic has more traditionally been," in which formulas are interactive computational problems viewed as games played by a machine against the environment, logical operators stand for operations on games, and truth is understood as existence of an algorithmic winning strategy [7]. Its development into applied theories is carried forward in the same source, which notes that prior technical efforts had focused on developing computability logic as a pure logic through axiomatizations of fragments, and which introduces the dfb-reduction operation and block-move machines as technical machinery [7]. Computability logic illustrates the space of proposals against which the LogiKEy choice of HOL-as-metalogic must be measured: where computability logic changes what the logical operators mean, LogiKEy keeps the metalogic fixed and varies the embedded semantics. A course built on LogiKEy could in principle embed a game semantics of the computability-logic style as one more object logic, which is itself evidence for the flexibility of the HOL substrate.

Genuine logical pluralism inside the algebraic tradition is exemplified by [6], which studies, in full generality, logics defined by imposing a variable inclusion condition on a given consequence relation $\vdash$. The source defines the left variable inclusion companion $\vdash^{l}$ by $\Gamma\vdash^{l}\varphi$ iff there is $\Delta\subseteq\Gamma$ with $\mathrm{Var}(\Delta)\subseteq\mathrm{Var}(\varphi)$ and $\Delta\vdash\varphi$, and states that "the algebraic counterpart of the variable inclusion companion of a given logic $\vdash$ is obtained by constructing the Plonka sum of the matrix models of $\vdash$," a construction it develops through directed systems of matrices over a semilattice, yielding Hilbert-style axiomatizations [6]. Such non-classical consequence relations are exactly the kind of object logic that the semantical-embedding approach can host: a matrix semantics is a set-theoretic structure, hence definable in HOL.

The deontic stage of the LogiKEy sequence connects to [8], which introduces the multi-agent temporal deontic STIT logic TDS, answering "a long standing request for temporal embeddings of deontic STIT logics." The logic is based on atemporal utilitarian STIT logic but is neutral: instead of committing to utilitarian theories, the authors "prove the logic TDS sound and complete with respect to relational frames not employing any utilitarian" commitments, with a language combining agency operators $[i]$, $[Ag]$, temporal operators $\mathsf{G}$, $\mathsf{H}$, and a deontic operator $\otimes_{i}$ [8]. The same source shows that these neutral frames can be transformed into frames employing utility assignments while preserving truth, allowing utilitarian scenarios to be modeled "in a more fine-grained manner, while obtaining completeness of the logic without commitment to particular utility functions" [8]. This demonstrates that deontic logic remains an active research frontier with new modeling resources (agency, time); a LogiKEy-style course can present TDS as a further embedding, showing students that the sequence they climbed does not end at dyadic deontic logic.

Finally, [9] is the previously published version of the present analysis. Its results section states the same computed quantities reproduced and corrected here, including the modal counts $2^{64}$ and $2^{56}$ and the Wise Men trajectory $8\to7\to6\to4$ with shrinkage factor $7/4=1.75$ [9]. The present revision keeps every correct quantity of [9], corrects the two inconsistencies identified between its abstract and its derivations (the trajectory and the description of the public-announcement update), and strengthens the qualification of the assumptions behind the proof-length tower and the Gödel-argument estimate.

Collectively, these works motivate a systematic quantitative study of proof-assistant-based logic teaching, situating the contribution within an emerging research agenda while marking clearly which parts of the surrounding program are machine-checked, which are documented by experience, and which—here—are combinatorial projections.

## 3. Methods

### 3.1 Semantical embeddings in HOL

Fix classical HOL with a domain of possible worlds (a HOL type $w$). An object modal logic with box operator is embedded by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v
$$

where $r : w \to w \to \mathbb{B}$ is a HOL relation and $\varphi : w \to \mathbb{B}$ is a HOL predicate on worlds. Different constraints on $r$ (serial, reflexive, transitive, Euclidean, equivalence) yield different object logics (D, T, S4, S5), all inside the same metalogic. Epistemic logic adds an agent index: $r_{a}$ for each agent $a$ from a finite set $A$, with knowledge $K_{a}\varphi = \Box_{r_{a}}\varphi$; under S5 constraints each $r_{a}$ is an equivalence relation partitioning $W$. Dynamic epistemic logic adds event models acting on the current model: the product update of a factual model of size $|W|$ by an action model of size $|E|$ yields a candidate product of size $|W|\cdot|E|$, from which the updated model retains exactly those product points $(w,e)$ at which the announcement associated with $e$ holds at $w$; the shrinkage of a public announcement is therefore produced by this semantic restriction, not by the product construction itself. Deontic logic replaces worlds-with-obligation by either a deontic accessibility $r_{\text{ob}}$ (standard) or a dyadic conditional $\mathcal{O}(\psi\mid\varphi)$ selecting ideal $\varphi$-worlds (dyadic). None of this requires new tooling: each definition is a HOL constant, each metatheorem a HOL theorem, each counter-model a HOL-computable structure.

### 3.2 Method of this paper

The method is combinatorial analysis of the LogiKEy example sequence [1], [2]. For each curricular stage the representational choice is identified, the associated search or model space is defined, and its cardinality is computed exactly from stated inputs. For each stage a quantitative invariant is extracted that (i) can be computed exactly from stated inputs by elementary arithmetic, and (ii) exhibits the limitation that motivates the transition to the next logic. Every claim in Section 5 is restricted to numbers derived in Section 4; where extrapolation beyond the computation occurs, the claim is labeled a projection with its assumptions stated. Two classes of statements require particular care and are flagged where they occur: the proof-length recurrence for Boolos's inference is a stated worst-case model, not a measured proof-search outcome; and the consistent-space estimate for Gödel's argument rests on an explicit independence assumption. No empirical learning outcomes or prover timings are reported, because none are computed here; the claims are purely combinatorial.

## 4. Analysis

### 4.1 Stage 1: Liars and truth-tellers — exhaustive consistency in propositional logic

**Input (from the puzzle structure of [1]).** Three islanders $a,b,c$; each is either a truth-teller ($T$) or a liar ($L$). Statements: $a$ says "$b$ is a truth-teller"; $b$ says "$a$ and $c$ are of different types"; $c$ says "$a$ is a liar". Consistency condition: an islander of type $T$ asserts only truths; an islander of type $L$ asserts only falsehoods.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The three consistency constraints are

$$
x_{a} = (x_{b}=T),\qquad
x_{b} = (x_{a}\neq x_{c}),\qquad
x_{c} = (x_{a}=L).
$$

**Exhaustive check.** The search space has $2^{3}=8$ assignments. Evaluation yields exactly one survivor, $(x_{a},x_{b},x_{c})=(T,T,L)$. Verification: $x_{a}=T$ requires $x_{b}=T$ — holds; $x_{b}=T$ requires $x_{a}\neq x_{c}$, i.e. $T\neq L$ — holds; $x_{c}=L$ requires $x_{a}=T$ to be false, i.e. $x_{a}=L$ — holds, since a liar's assertion "$a$ is a liar" is false exactly when $a$ is a truth-teller. The elimination rate is $7/8=0.875$.

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space already contains $2^{10}=1024$ rows, which exceeds feasible manual checking.

### 4.2 Stage 2: The modal upgrade — counting accessibility relations

**Input.** The same puzzle re-modeled with $|W|=8$ worlds (one per propositional assignment) and a single epistemic agent (the puzzle solver). The number of distinct binary accessibility relations on a set of $|W|$ worlds is

$$
2^{|W|\cdot|W|}=2^{8\times8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
$$

If reflexivity is imposed (standard for knowledge), the diagonal pairs are fixed, leaving $8\times7=56$ off-diagonal pairs, so

$$
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}
$$

reflexive relations. These are upper bounds for the given constraints: imposing symmetry or transitivity in addition would reduce the count further.

### 4.3 Stage 3: The Wise Men puzzle — model dynamics under public announcement

**Input.** Three agents $a,b,c$; each wears a black ($B$) or white ($W$) hat; each sees the others' hats but not its own; the king publicly announces "at least one hat is black". All three hats are in fact black. Knowledge is S5.

**Model sizes.** Initial world set $W_{0}$ has $2^{3}=8$ worlds. The king's announcement eliminates the all-white world $WWW$, leaving $|W_{1}|=7$. Agent $a$'s subsequent public "I don't know" announcement eliminates the worlds at which $a$ would know his hat color; given the announcement already made, $a$ would know only if the other two hats were both white, so the world $WWB$ is eliminated, yielding $|W_{2}|=6$. Agent $b$'s analogous announcement eliminates the worlds at which $b$ would know, namely $BBW$ and $WBW$, yielding $|W_{3}|=4$. The trajectory is

$$
8\;\to\;7\;\to\;6\;\to\;4,
$$

a shrinkage factor of $7/4=1.75$ from the first announcement onward. (The previously published abstract's trajectory $8\to7\to6\to5\to4$ and factor $8/4=2$ were inconsistent with this stage-by-stage derivation and are corrected here.)

**Corrected account of the update mechanism.** In dynamic epistemic logic, a public announcement is modeled by an action model with a single event, $|E|=1$. The product update of a model of size $|W|$ by this action model yields a candidate product of size $|W|\times|E|=|W|$; the updated model then retains exactly those product points at which the announced formula holds. For the king's announcement over $W_{0}$, the announced formula "at least one hat is black" holds at $7$ of the $8$ worlds, so the updated model has $7$ worlds. The shrinkage from $8$ to $7$ is thus produced by semantic restriction of the product, not by the product construction itself; stating that "the updated model size is $|W|\times|E|$" without the restriction step, as the previous version did immediately after reporting the shrinkage, conflated the two and is corrected here. By contrast, an action model with $|E|=3$ events over the original $8$ worlds yields a candidate product of $8\times3=24$ points, illustrating that DEL can both shrink and grow models depending on the event structure and the restriction.

### 4.4 Stage 4: Boolos's curious inference — what a higher-order metalogic buys

**Input.** Boolos's curious inference is a first-order argument whose proof length $L_{n}$ is modeled by the worst-case recurrence

$$
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
$$

This recurrence is a stated idealization of the growth that defeats feasible proof search in the first-order setting; it is not a measured proof-search outcome, and alternative proof-search strategies could yield smaller lengths.

**Computation.** Iterating yields

\[
\begin{aligned}
L_{1}&=2^{1}=2,\\
L_{2}&=2^{2}=4,\\
L_{3}&=2^{4}=16,\\
L_{4}&=2^{16}=65\,536,\\
L_{5}&=2^{65\,536}.
\end{aligned}
\]

Using $\log_{10}(2)=0.30103$,

$$
\log_{10}\bigl(2^{65\,536}\bigr)=65\,536\times0.30103\approx19\,728.3,
$$

so $L_{5}\approx10^{19\,728}$.

**First-order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is

$$
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}.
$$

A propositional instantiation with $k=10$ atoms yields $2^{10}=1\,024$ rows. The contrast between $2^{100}\approx10^{30}$ first-order interpretations, which a model finder must search implicitly, and the short higher-order proof illustrates what a higher-order metalogic buys: in HOL, comprehension principles make the relevant objects directly definable rather than implicitly searchable.

### 4.5 Stage 5: Deontic combinatorics (Chisholm's paradox)

**Input.** Chisholm's paradox involves $m=2$ obligations. Each obligation can be fulfilled or violated, giving $2^{m}=4$ fulfillment profiles. A three-obligation variant yields $2^{3}=8$ profiles. The paradox is not a growth problem (the space stays at $2^{m}$) but a consistency problem: the standard monotonic deontic operator $O$ forces inconsistency when the obligations interact with contrary-to-duty conditions, whereas the dyadic operator $O(B\mid A)$ reorganizes the same four profiles into conditional commitments, restoring consistency. The transition here is therefore motivated by a structural change in the consistency problem, not by a change in the size of the space—a deliberately different kind of quantitative invariant from the growth invariants of Stages 1–4.

### 4.6 Stage 6: Axiomatic commitments (Gödel's ontological argument)

**Input.** Gödel's ontological argument, as embedded in the LogiKEy sequence, posits a positivity predicate $P$ over a universe of $p=5$ candidate properties and $a=3$ core axioms. The raw interpretation space for $P$ is

$$
2^{p}=2^{5}=32.
$$

**Consistent-space estimate (labeled estimate).** If each axiom is independent and rules out exactly half of the remaining interpretations, the consistent set has size at least

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

This is an estimate conditional on the independence and halving assumptions, not an exact count: if the axioms are not independent, or if an axiom rules out fewer than half of the interpretations in some region of the space, the consistent space is larger than $2^{p-a}$, so $4$ is a lower bound under the stated assumptions and the true consistent space may be strictly larger. The pedagogical point survives the qualification: the research-level argument reduces to a small, exhaustively searchable space, in sharp contrast to the unstructured spaces of Stages 2 and 4.

### 4.7 Course-time projection (labeled projection)

Assumption set (explicit): a semester course of $T_{\text{sem}}=14$ weeks with one $2$-hour session per week gives $14\times2=28$ contact hours. The six stages are allocated in the ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$, total weight $20$. Each weight unit corresponds to

$$
\frac{28}{20}=1.4\ \text{hours}.
$$

Consequently the stage allocations are

\[
\begin{aligned}
\text{Stage 1}&:2\times1.4=2.8\ \text{h},\\
\text{Stage 2}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 3}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 4}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 5}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 6}&:4\times1.4=5.6\ \text{h}.
\end{aligned}
\]

The sum check $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ hours holds. The ratio is a design choice, not an empirically validated quantity; the projection is sensitive to it.

## 5. Results

All values below are computed in Section 4 with shown arithmetic; the single projection (R7) and the single estimate within R6 are labeled as such.

* **R1.** The propositional state space for $n=3$ islanders is $2^{3}=8$ assignments, of which exactly $1$ survives the three consistency constraints (elimination rate $7/8=0.875$); for $n=10$ islanders the raw space is $2^{10}=1\,024$ (Section 4.1).

* **R2.** The modal re-modeling over $|W|=8$ worlds admits $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary accessibility relations, or $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive ones; these are upper bounds for the stated constraints (Section 4.2).

* **R3.** The Wise Men factual model follows the trajectory $8\to7\to6\to4$ under the king's announcement and two ignorance announcements, a shrinkage factor of $7/4=1.75$ from the first announcement onward. The shrinkage is produced by semantic restriction of the product update: a one-event action model over $7$ worlds yields a candidate product of $7$ points, of which the $7$ worlds at which the announcement holds are retained. A DEL action model with $|E|=3$ events over the original $8$ worlds yields a candidate product of $8\times3=24$ points (Section 4.3).

* **R4.** Under the stated worst-case recurrence, Boolos's curious inference generates a proof-length tower $L_{1}=2$, $L_{2}=4$, $L_{3}=16$, $L_{4}=65\,536$, $L_{5}\approx10^{19\,728}$; a first-order encoding with domain size $d=10$ and one binary predicate presents $2^{100}\approx1.27\times10^{30}$ candidate interpretations, versus $2^{10}=1\,024$ propositional rows (Section 4.4).

* **R5.** Chisholm's paradox with $m=2$ obligations has $2^{2}=4$ fulfillment profiles; a three-obligation variant has $2^{3}=8$ profiles. The paradox is structural (consistency) rather than combinatorial (size) (Section 4.5).

* **R6.** Gödel's ontological argument over a $p=5$-property universe has $2^{5}=32$ raw interpretations of the positivity predicate $P$; under the explicit independence-and-halving assumptions, the consistent space is estimated at a minimum of $2^{5-3}=4$ interpretations, with the true consistent space potentially larger if the assumptions fail (Section 4.6).

* **R7 (projection).** Under the stated assumptions of Section 4.7, the six stages receive $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours respectively; uncertainty is dominated by the assumed ratio, which is not empirically validated (Section 4.7).

* **R8.** The quantitative contrast between the propositional and modal stages is

$$
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18},
$$

showing that the modal upgrade expands the search space by roughly $2.3\times10^{18}$-fold (Section 4.2, Section 4.1).

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Islander puzzle structure (three agents, fixed statements) | Results scale exponentially with the number of agents; the exact survivor count changes with alternative statements. |
| World set size $|W|=8$ derived from the propositional stage | Larger propositional spaces would increase $|W|$ and thus the accessibility-relation count $2^{|W|^{2}}$ dramatically. |
| Reflexivity constraint only (no transitivity, etc.) | Imposing additional constraints (e.g., symmetry) would reduce the relation count further; the presented numbers are upper bounds for the given constraints. |
| S5 epistemic assumptions (equivalence relations) | Weakening to KD45 would alter the number of admissible relations; the current count assumes full equivalence. |
| Wise Men elimination pattern ($WWB$; then $BBW$, $WBW$) | The trajectory $8\to7\to6\to4$ depends on the standard reading of the ignorance announcements; a different treatment of what agents know after each announcement changes the intermediate sizes and the shrinkage factor. |
| Boolos proof-length recurrence $L_{n+1}=2^{L_{n}}$ | The recurrence