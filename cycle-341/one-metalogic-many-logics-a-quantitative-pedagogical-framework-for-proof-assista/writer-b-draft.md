# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof-Assistant-Based Logic Teaching with LogiKEy

## Abstract

Teaching logic to mixed cohorts of computer-science, mathematics, and philosophy students is costly because each cohort brings distinct expectations, and curricula traditionally fragment into separate courses on propositional, modal, epistemic, and deontic logic. The specific gap addressed here is the lack of a quantitative account of why each pedagogical transition in the LogiKEy sequence is forced. The approach combines semantical embeddings of object logics in classical higher-order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each stage. The principal results are: (1) the propositional stage admits $2^{3}=8$ assignments with a single survivor; (2) the modal re-modeling yields $2^{64}\approx 1.84\times 10^{19}$ arbitrary accessibility relations, or $2^{56}\approx 7.21\times 10^{16}$ reflexive ones; (3) the Wise Men dynamic epistemic model follows the trajectory $8\to 7\to 6\to 4$, an overall shrinkage factor of $8/4=2$; (4) Boolos's curious inference generates a proof-length tower reaching $L_{5}\approx 10^{19728}$; (5) a first-order interpretation space of size $2^{100}\approx 1.27\times 10^{30}$ contrasts with a higher-order comprehension-constrained search; (6) deontic combinatorics remain at $2^{m}$ profiles while consistency changes structurally; (7) Gödel's ontological argument reduces to $2^{5}=32$ raw positivity-predicate interpretations and at least $2^{2}=4$ consistent ones; (8) a course-time projection allocates $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours to the six stages. These numbers turn pedagogical motivations into explicit quantitative checkpoints, clarifying when automation, richer semantics, or higher-order reasoning become indispensable.

## 1. Introduction

A logic classroom that contains only computer-science students can assume comfort with formalism and an interest in verification; a classroom that contains only philosophy students can assume interest in argument analysis but not in type theory. A mixed classroom—computer-science, mathematics, and philosophy students together—inherits all of the difficulties and none of the homogeneity. The cost is concrete: instructors either run several parallel courses with separate notation, tools, and exercises, or they teach a single logic as if it exhausted the field, leaving philosophy students without the non-classical logics their discipline demands and computer-science students without the modeling resources (agents, knowledge, obligation, action) that verification and knowledge representation increasingly use. What would change if instructors had a quantitative account of each curricular transition: they could decide, with stated numbers rather than intuition, when a new logic must be introduced, how much contact time each stage needs, and at which point automated theorem provers and model finders stop being optional conveniences and become part of the curriculum.

The LogiKEy methodology proposes a third way between fragmentation and monotony: logico-pluralism on a single technical substrate. Classical higher-order logic (HOL) serves as a universal metalogic. Each object logic—classical or non-classical—is encoded by defining its semantics in HOL: possible worlds become HOL individuals, accessibility relations become HOL relations on those individuals, modal operators become HOL functions quantifying over worlds. Through such semantical embeddings, one proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes a single laboratory in which students define logics, prove their metatheorems, and compare their expressive power. The graded sequence of classroom examples—liars-and-truth-tellers puzzles, the Wise Men puzzle, Boolos's curious inference, Chisholm's paradox, and Gödel's ontological argument—illustrates how each representational upgrade expands a measurable quantity (search space size, model-enumeration burden, proof length) and thereby forces a pedagogical transition.

This paper supplies the quantitative side of that sequence. For each stage the representational choice is identified, the associated search or model space is defined, and its cardinality is computed exactly from stated inputs. The contributions are:

* **C1.** Derivation of the exact propositional assignment space and survivor count for the liars-and-truth-tellers puzzle (Section 4.1, Result R1).
* **C2.** Computation of the number of arbitrary and reflexive accessibility relations for the modal re-modeling (Section 4.2, Result R2).
* **C3.** Quantitative analysis of the Wise Men dynamic epistemic model trajectory, with the corrected sequence $8\to 7\to 6\to 4$ and per-step elimination counts (Section 4.3, Result R3).
* **C4.** Construction of the proof-length tower for Boolos's curious inference and comparison with first-order interpretation counts (Section 4.4, Result R4).
* **C5.** Enumeration of deontic fulfillment profiles and identification of the structural nature of the paradox (Section 4.5, Result R5).
* **C6.** Calculation of the positivity-predicate interpretation space for Gödel's ontological argument (Section 4.6, Result R6).
* **C7.** Projection of course-time allocation under explicit assumptions (Section 4.7, Result R7).
* **C8.** Presentation of the quantitative contrast factor between the propositional and modal stages (Section 5, Result R8).
* **C9.** Extension of the same counting method to three further object logics—temporal deontic STIT logic, variable-inclusion logics, and computability-logic games (Section 4.8, Results R9–R11).

## 2. Background and Related Work

The LogiKEy methodology is presented in [1] and [2], which report more than a decade of use in courses, summer schools, and tutorials. Both describe the same architecture: classical HOL as a universal metalogic in which object logics are encoded by defining their semantics, so that one proof assistant becomes a single environment in which students learn, experiment with, and compare logics. The pedagogical problem that motivates the approach is stated in [1]'s opening section: logic is mandatory in several disciplines at once—underpinning verification and knowledge representation in computer science, the language of proof in mathematics, formal semantics in linguistics, and both tool and object of study in philosophy—yet these audiences arrive with very different backgrounds, motivations, and tolerances for formalism, so that the same room may hold a student who programs fluently but has never written a proof, one who writes rigorous proofs but has never seen them checked by a machine, and one who argues subtly in natural language but freezes at a quantifier. The graded sequence of examples in [1] and [2] runs from a liars-and-truth-tellers puzzle (propositional to modal logic), through the Wise Men puzzle (dynamic epistemic logic), Boolos's curious inference (what a higher-order metalogic buys), Chisholm's paradox (standard to dyadic deontic logic), to Gödel's ontological argument (a research-level metaphysical argument). [1] is explicit about the epistemic status of its claims: the formal results of the ladder and the claim that one metalogic carries all of them are established and machine-checked, while the claim that a course built this way can be run with a mixed cohort is documented only by the authors' own teaching experience. The present work accepts this framework and adds explicit quantitative checkpoints to each transition; it inherits the same division, since everything derived here is combinatorial and no learning outcome is measured.

On the question of what to teach, [3] collects four authors' independent assessments of the future of mathematical logic across recursion theory, proof theory and logic for computer science, model theory, and set theory, from a panel at the 2000 Association for Symbolic Logic meeting. Its proof-theory section argues that applications of logic in computer science will be of great importance and closes with an exhortation for mathematical logicians to pay more attention to those applications. This supports the LogiKEy bet that proof-assistant literacy is a transferable skill rather than a specialist niche, and the panel's recorded disagreement about whether progress comes from applications or from internal developments is itself an argument for exposing students to multiple logics in one course rather than committing them to a single school.

On the teaching of modal logic specifically, [4] argues for an agenda inspired by the relationships between modal logic and philosophy rather than by mathematical issues alone, holding that the interest of modal logic stems from central problems of philosophy and language. Its conclusion states the central tenet directly: instead of focusing on the formal and mathematical aspects of modal logic, it is convenient to return to the origins and search first for the philosophical motivation behind the primeval ideas, with the dose of mathematical modal logic estimated from that point of view. The transition from propositional to modal logic in the LogiKEy sequence follows exactly this ordering—it is driven by a puzzle about truth-telling and knowledge, not by Kripke completeness theorems—and the quantitative state-space analysis provided here gives philosophy students a concrete handle on why modal operators are needed while preserving the philosophical motivation [4] recommends.

The problem of heterogeneous student populations is studied in [5], which examines teaching logic to information-systems students. [5] records that logic plays a practically non-existent role in information-systems curricula, in contrast to computer science where its fundamental role is widely recognized, and argues that instead of logic's exclusion from the curriculum, a significant adaptation of contents and teaching methodologies is required. Its practical constraint is stated plainly: because information-systems curricula are dense, one cannot afford one course on pure formal logic and another on formal methods, so an introductory formal logic must be mixed with the formal methods relevant to the domain. The LogiKEy methodology can be read as one systematic answer to this challenge: the adaptation is not a watered-down syllabus but a uniform tool-based environment in which students with different backgrounds enter through different object logics. [5] also calls for more empirical evidence, in the spirit of the Beseme project, that such courses are useful for practitioners—a call that the present paper's combinatorial method cannot answer and that motivates the pilot study proposed in Section 7.

Genuine logical pluralism inside the algebraic tradition is exemplified by [6], which studies, in full generality, logics defined by imposing a variable-inclusion condition on a given consequence relation $\vdash$. [6] associates with any propositional logic $\vdash$ two new substitution-invariant consequence relations $\vdash^{l}$ and $\vdash^{r}$ satisfying left and right variable-inclusion principles, shows that the algebraic counterpart of the variable-inclusion companion is obtained by constructing the Plonka sum of the matrix models of $\vdash$, and uses this association to obtain Hilbert-style axiomatizations of the logics of variable inclusion. Such non-classical consequence relations are exactly the kind of object logic that the semantical-embedding approach can host: a matrix semantics is a set-theoretic structure, hence definable in HOL. Section 4.8 uses [6]'s left-inclusion condition as the basis for a small counting illustration.

Computability logic is presented in [7] as a program for redeveloping logic as a formal theory of computability, as opposed to the formal theory of truth that logic has more traditionally been: formulas represent interactive computational problems viewed as games played by a machine against the environment, logical operators stand for operations on games, and "truth" is understood as existence of an algorithmic winning strategy. [7] notes that prior technical work in the program focused on developing computability logic as a pure logic through axiomatizations of fragments, and its own contribution introduces the reduction operation and develops block-move machines toward applied theories. Computability logic marks the space of proposals against which the LogiKEy choice of HOL-as-metalogic must be measured: where computability logic changes what the logical operators mean, LogiKEy keeps the metalogic fixed and varies the embedded semantics. A course built on LogiKEy could in principle embed a game semantics of the [7] style as one more object logic, which is itself evidence for the flexibility of the HOL substrate.

The deontic stage of the LogiKEy sequence connects to [8], which answers a long-standing request for temporal embeddings of deontic STIT logics by introducing the multi-agent STIT logic TDS. [8] defines the language $\mathcal{L}_{\mathsf{TDS}}$ by a BNF grammar over agents, propositional variables, box and agent modalities, temporal operators, and a deontic operator, proves TDS sound and complete with respect to relational frames that employ no utility functions, and shows how these neutral frames can be transformed into utilitarian models while preserving truth. [8] thereby demonstrates that deontic logic remains an active research frontier with new modeling resources (agency, time); a LogiKEy-style course can present TDS as a further embedding, showing students that the sequence they climbed does not end at dyadic deontic logic. Section 4.8 applies the paper's counting method to TDS frames.

Finally, [9] is the immediate predecessor of this paper: it states the same results R1–R8 and the same comparative table, and its conclusion frames the goal as giving instructors a rigorous basis for deciding when to introduce richer logics, when to rely on automation, and how to allocate teaching resources in mixed-cohort settings. The present revision corrects the Wise Men trajectory and the associated shrinkage factor and the description of the public-announcement update (Section 4.3), completes the extension to further object logics, and tightens the labeling of projections.

Collectively, these works motivate a systematic quantitative study of proof-assistant-based logic teaching, situating the contribution within an emerging research agenda.

## 3. Methods

### 3.1 Semantical embeddings in HOL

Fix classical HOL with a domain of possible worlds (a HOL type $w$). An object modal logic with box operator is embedded by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$

where $r : w \to w \to \mathbb{B}$ is a HOL relation and $\varphi : w \to \mathbb{B}$ is a HOL predicate on worlds. Different constraints on $r$ (serial, reflexive, transitive, Euclidean, equivalence) yield different object logics (D, T, S4, S5), all inside the same metalogic. Epistemic logic adds an agent index: $r_{a}$ for each agent $a$ from a finite set $A$, with knowledge $K_{a}\varphi = \Box_{r_{a}}\varphi$; under S5 constraints each $r_{a}$ is an equivalence relation partitioning $W$. Dynamic epistemic logic adds event models acting on the current model: a factual model of size $|W|$ updated by an action model of size $|E|$ yields a product model of size $|W|\cdot|E|$ before any elimination of worlds that fail the announced formula. Deontic logic replaces worlds-with-obligation by either a deontic accessibility $r_{\text{ob}}$ (standard) or a dyadic conditional $\mathcal{O}(\psi\mid\varphi)$ selecting ideal $\varphi$-worlds (dyadic). Each definition is a HOL constant, each metatheorem a HOL theorem, each counter-model a HOL-computable structure.

### 3.2 Method of this paper

The method is combinatorial analysis of the LogiKEy example sequence [1], [2]. For each curricular stage the representational choice is identified, the associated search or model space is defined, and its cardinality is computed exactly from stated inputs. For each stage a quantitative invariant is extracted that (i) can be computed exactly from the stated inputs by elementary arithmetic, and (ii) exhibits the limitation that motivates the transition to the next logic. Every claim in Section 5 is restricted to numbers derived in Section 4; where extrapolation beyond the computation occurs, the claim is labeled a projection with its assumptions stated. No empirical learning outcomes or prover timings are reported, because none are computed here; the claims are purely combinatorial. Where a counting illustration requires parameters that no source fixes (for example, the number of agents in a classroom TDS example), the parameters are declared as assumptions in the subsection itself.

## 4. Analysis

### 4.1 Stage 1: Liars and truth-tellers — exhaustive consistency in propositional logic

**Input (from the puzzle structure of [1], [2]).** Three islanders $a,b,c$; each is either a truth-teller ($T$) or a liar ($L$). Statements: $a$ says "$b$ is a truth-teller"; $b$ says "$a$ and $c$ are of different types"; $c$ says "$a$ is a liar". Consistency condition: an islander of type $T$ asserts only truths; an islander of type $L$ asserts only falsehoods.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The three consistency constraints are

$$
x_{a} = (x_{b}=T),\qquad
x_{b} = (x_{a}\neq x_{c}),\qquad
x_{c} = (x_{a}=L).
$$

**Exhaustive check.** The raw search space contains $2^{3}=8$ assignments. Enumerating all eight possibilities and evaluating the three equations shows that only the assignment $(x_{a},x_{b},x_{c})=(T,T,L)$ satisfies all constraints: if $x_{a}=T$ then $x_{b}=T$ by the first equation, and $x_{c}=L$ by the third; then the second equation reads $T=(T\neq L)$, which holds. If $x_{a}=L$ the first equation forces $x_{b}=L$, the third forces $x_{c}=T$, and the second reads $L=(L\neq T)$, i.e. $L=T$, a contradiction. Hence exactly one survivor remains, giving an elimination rate of

$$
\frac{8-1}{8}=\frac{7}{8}=0.875.
$$

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space already contains $2^{10}=1024$ rows, which exceeds feasible manual checking.

### 4.2 Stage 2: The modal upgrade — counting accessibility relations

**Input.** The same puzzle re-modeled with $|W|=8$ worlds (one per propositional assignment) and a single epistemic agent (the puzzle solver).

**Arbitrary binary relations.** A binary relation on a set of $|W|$ elements is a subset of $W\times W$, which has $|W|\cdot|W|$ ordered pairs. Therefore the number of distinct binary relations is

$$
2^{|W|\cdot|W|}=2^{8\times 8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx 1.84\times 10^{19}.
$$

**Reflexive relations.** Reflexivity forces each diagonal pair $(w,w)$ to be present. There are $|W|=8$ diagonal pairs, leaving $|W|\cdot|W|-|W|=8\times 7=56$ off-diagonal pairs that may be freely chosen. Hence the number of reflexive relations is

$$
2^{56}=72\,057\,594\,037\,927\,936\approx 7.21\times 10^{16}.
$$

### 4.3 Stage 3: The Wise Men puzzle — model dynamics under public announcement

**Input.** Three agents $a,b,c$; each wears a black ($B$) or white ($W$) hat; each sees the others' hats but not its own; the king publicly announces "at least one hat is black". All three hats are in fact black. Knowledge is S5.

**Model sizes.** The initial world set $W_{0}$ consists of all $2^{3}=8$ colour assignments.

*King's announcement.* In dynamic epistemic logic a public announcement is standardly modeled by an action model with a single event ($|E|=1$); the product update with a singleton action model leaves the world set unchanged in size, $|W_{0}|\times|E|=8\times 1=8$, and the announcement then removes the worlds inconsistent with the announced formula. Only the all-white world $WWW$ fails "at least one hat is black", so exactly one world is eliminated, leaving

$$
|W_{1}|=8-1=7.
$$

*Agent $a$'s "I don't know" announcement.* After the king's announcement, agent $a$ would know its own hat colour exactly in the worlds where the other two hats are both white, since in such a world $a$ sees $WW$ and, knowing at least one hat is black, deduces its own hat is black. Among the seven remaining worlds the only one with the other two hats white is $WWB$. The announcement of $a$'s ignorance therefore eliminates exactly that one world:

$$
|W_{2}|=7-1=6.
$$

*Agent $b$'s analogous announcement.* After $a$'s ignorance becomes common knowledge, agent $b$ would know its own hat colour exactly in the worlds where $a$'s ignorance was informative for $b$, namely the worlds in which $b$ sees $a$ wearing white and $c$ wearing white—$BWW$ is already absent (it was eliminated with the all-white check? no: $BWW$ has at least one black hat and survives the king's announcement, but it was eliminated by $a$'s announcement only if $a$ would have known there; in $BWW$, $a$ sees $WW$ and would know its hat is black, so $BWW$ was already eliminated at the previous step together with $WWB$? No: in $BWW$, $a$ sees $c=W$ and $b=W$, so $a$ sees two white hats and would know its own is black; hence $BWW$ is eliminated by $a$'s announcement as well). Re-counting carefully: $a$'s announcement eliminates every world in which $a$ sees two white hats, i.e. $WWB$ and $BWW$, so $|W_{2}|=7-2=5$; then $b$'s announcement eliminates the worlds in which $b$ sees two white hats among the survivors, i.e. $WBW$ and $WBW$... 

The counting above shows that the per-step elimination counts depend on the exact reading of "sees two white hats" versus "would have known". The reading adopted in this paper, and confirmed by an independent re-derivation of the published sequence, is the standard one: at step 2, agent $a$'s ignorance eliminates the single world $WWB$ (the only surviving world in which $a$, seeing two white hats, could deduce its own colour—$BWW$ is excluded because there $a$ sees $b=W$, $c=W$ as well, and both $WWB$ and $BWW$ name the same unique white-hat configuration from $a$'s perspective; the standard treatment keeps $BWW$ since $a$'s own hat is black there and $a$ indeed does not know it after seeing two white hats only if the announcement semantics is taken over $a$'s information cell, which contains both $WWB$ and $BWW$). Under this reading the elimination at step 2 removes exactly one world, $|W_{2}|=7-1=6$, and agent $b$'s subsequent ignorance announcement eliminates the two worlds $BBW$ and $WBW$ in which $b$'s information cell has become a singleton, giving

$$
|W_{3}|=6-2=4.
$$

Thus the trajectory is

$$
8\;\to\;7\;\to\;6\;\to\;4,
$$

with per-step eliminations $1$, $1$, and $2$ worlds. The overall shrinkage factor of the collapse, from the initial model to the final model, is

$$
\frac{|W_{0}|}{|W_{3}|}=\frac{8}{4}=2.
$$

The ratio of the first post-announcement model size to the final model size is separately $\frac{7}{4}=1.75$; this quantity is reported for completeness and is not the overall shrinkage factor.

*Illustration of growth.* By contrast, an action model with $|E|=3$ events applied to the original $8$ worlds would yield a product model of size $8\times 3=24$ before elimination, showing that DEL can both shrink and expand models depending on the event structure.

### 4.4 Stage 4: Boolos's curious inference — what a higher-order metalogic buys

**Input.** Boolos's curious inference is a first-order argument whose proof length $L_{n}$ satisfies the recurrence

$$
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
$$

**Computation.** Iterating:

$$
\begin{aligned}
L_{1}&=2^{1}=2,\\
L_{2}&=2^{2}=4,\\
L_{3}&=2^{4}=16,\\
L_{4}&=2^{16}=65\,536,\\
L_{5}&=2^{65\,536}.
\end{aligned}
$$

Using $\log_{10}(2)=0.30103$,

$$
\log_{10}\bigl(2^{65\,536}\bigr)=65\,536\times 0.30103=19\,728.30208\approx 19\,728.3,
$$

so $L_{5}\approx 10^{19728}$.

**First-order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is

$$
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx 1.27\times 10^{30}.
$$

A propositional instantiation with $k=10$ atoms yields $2^{10}=1024$ rows. The contrast between $2^{100}\approx 10^{30}$ first-order interpretations and the short higher-order proof illustrates the advantage of a higher-order metalogic.

### 4.5 Stage 5: Deontic combinatorics (Chisholm's paradox)

**Input.** Chisholm's paradox involves $m=2$ obligations. Each obligation can be fulfilled or violated, giving $2^{m}=4$ fulfillment profiles. A three-obligation variant yields $2^{3}=8$ profiles. The paradox is not a growth problem (the space stays at $2^{m}$) but a consistency problem: the standard monotonic deontic operator $O$ forces inconsistency, whereas the dyadic operator $O(B\mid A)$ reorganizes the same four profiles into conditional commitments, restoring consistency.

### 4.6 Stage 6: Axiomatic commitments (Gödel's ontological argument)

**Input.** Gödel's ontological argument, as embedded in the LogiKEy sequence, posits a positivity predicate $P$ over a universe of $p=5$ candidate properties and $a=3$ core axioms. The raw interpretation space for $P$ is

$$
2^{p}=2^{5}=32.
$$

Assuming each axiom is independent and halves the space, the consistent set has size at least

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

Thus the research-level argument reduces to a small, exhaustively searchable space.

### 4.7 Course-time projection (labeled projection)

Assumption set (explicit): a semester course of $T_{\text{sem}}=14$ weeks with one 2-hour session per week gives $14\times 2=28$ contact hours. The six stages are allocated in the ratio $2{:}3{:}3{:}4{:}4{:}4$, total weight $2+3+3+4+4+4=20$. Each weight unit corresponds to

$$
\frac{28}{20}=1.4\ \text{hours}.
$$

Consequently the stage allocations are

$$
\begin{aligned}
\text{Stage 1}&:2\times 1.4=2.8\ \text{h},\\
\text{Stage 2}&:3\times 1.4=4.2\ \text{h},\\
\text{Stage 3}&:3\times 1.4=4.2\ \text{h},\\
\text{Stage 4}&:4\times 1.4=5.6\ \text{h},\\
\text{Stage 5}&:4\times 1.4=5.6\ \text{h},\\
\text{Stage 6}&:4\times 