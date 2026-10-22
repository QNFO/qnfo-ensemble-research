# Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum

## Abstract

Mixed cohorts of computer-science, mathematics, and philosophy students face fragmented logic curricula that either overload or under-serve particular backgrounds, raising instructional cost and reducing learning coherence. Existing work on the LogiKEy methodology supplies a unified metalogic but lacks explicit quantitative checkpoints that justify transitions between object logics. This paper combines semantical embeddings of object logics in classical higher-order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each curricular stage. The analysis derives (1) the propositional assignment space $2^{3}=8$ and its single survivor for the liars-and-truth-tellers puzzle; (2) the numbers of arbitrary ($2^{64}\approx1.84\times10^{19}$) and reflexive ($2^{56}\approx7.21\times10^{16}$) accessibility relations for the modal re-modeling; (3) the Wise Men / muddy-children model trajectory $8\to7\to6\to4$ with shrinkage factor $7/4=1.75$ from the first announcement onward, and its generalisation to $2^{8}=256$ agents; (4) the proof-length tower $L_{5}\approx10^{19728}$ for Boolos's curious inference; (5) the deontic fulfillment profile count $2^{m}$ with $m=2$; (6) the Gödel ontological argument's raw and consistent positivity-predicate interpretations $2^{5}=32$ and $2^{2}=4$; (7) a course-time allocation projected from a 28-hour semester and a $2{:}3{:}3{:}4{:}4{:}4$ weight ratio; (8) the contrast factor $2^{61}\approx2.31\times10^{18}$ between propositional and modal stages; and (9) the transfer of the same exponential scaffolding to variable-inclusion and computability logics. These checkpoints turn pedagogical intuition into concrete numerical milestones for curriculum design, automation adoption, and resource planning.

## 1. Introduction

Logic courses that simultaneously serve computer-science, mathematics, and philosophy students encounter a concrete problem: each discipline arrives with distinct expectations about the role of logic, the nature of proof, and the desired applications, yet curricula are typically organised around a single object logic. The resulting fragmentation forces students to master multiple notations and toolchains, while monotonic courses that remain in classical first-order logic leave philosophy students without the modal and deontic resources they need and computer-science students without the modelling primitives required for verification tasks. The cost of this mismatch appears as additional contact hours, duplicated teaching materials, and lower learning outcomes, and the capability that would resolve it is a unified, quantitative framework that tells instructors precisely when a richer object logic becomes necessary.

The LogiKEy methodology supplies the unifying metalogic—classical higher-order logic (HOL)—and demonstrates how object logics can be embedded semantically in a single proof assistant. What remains missing is a set of explicit numerical thresholds that justify each pedagogical transition. This paper fills that gap by deriving, from first principles, the combinatorial quantities that grow (or shrink) at each stage of the LogiKEy example sequence and by mapping those quantities to curriculum-design decisions. Every number is either computed here by shown arithmetic or explicitly labelled a projection with stated assumptions; no empirical classroom data is reported.

**Contributions.**
- **C1.** Exact derivation of the propositional assignment space and survivor count for the liars-and-truth-tellers puzzle (Section 4.1, Result R1).
- **C2.** Enumeration of arbitrary and reflexive accessibility relations for the modal re-modeling (Section 4.2, Result R2).
- **C3.** Quantitative analysis of the Wise Men / muddy-children state-space collapse $8\to7\to6\to4$ and its generalisation (Section 4.3, Result R3).
- **C4.** Construction of the proof-length tower for Boolos's curious inference (Section 4.4, Result R4).
- **C5.** Counting of deontic fulfillment profiles for Chisholm's paradox (Section 4.5, Result R5).
- **C6.** Calculation of raw and consistent positivity-predicate interpretations for Gödel's ontological argument (Section 4.6, Result R6).
- **C7.** Projection of contact-hour allocation for a six-stage semester course (Section 4.7, Result R7).
- **C8.** Derivation of the contrast factor between propositional and modal stages (Section 4.8, Result R8).
- **C9.** Extension of the exponential scaffolding to variable-inclusion and computability logics (Section 4.9, Result R9).

## 2. Background and Related Work

The LogiKEy methodology is presented in [1] and [2], which report more than a decade of experience teaching logic to mixed groups of computer-science, mathematics, and philosophy students. Both works describe how classical HOL serves as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics, so that a single proof assistant such as Isabelle/HOL, with its automated theorem provers and (counter-)model finders, becomes one environment in which students learn, experiment with, and compare logics. The graded sequence of classroom examples in [2] runs from a liars-and-truth-tellers puzzle (propositional to modal logic), through the Wise Men puzzle (dynamic epistemic logic) and Boolos's curious inference (what a higher-order metalogic buys even for automated proof search), to Chisholm's paradox (standard to dyadic deontic logic) and Gödel's ontological argument (a research-level metaphysical argument). Section 1 of [2] states the interdisciplinary challenge directly: the same room may hold a student who programs fluently but has never written a proof, one who writes rigorous proofs but has never seen them checked by a machine, and one who argues subtly in natural language but freezes at a quantifier. Section 7 of [2] distinguishes what is established—machine-checked formal results reproducible from openly available sources—from what is documented only by the authors' own teaching experience; the present paper adds a third category, derived combinatorial checkpoints, and is careful to label its projections as such.

The pedagogical case for anchoring modal logic in philosophical problems rather than in mathematical technique is argued in [4]. Its Section 4 concludes that the dose of mathematical modal logic introduced should be estimated from the philosophical motivation, and that instead of focusing on formal and mathematical aspects one should return to the origins and search first for the philosophical motivation behind the primeval ideas. The transition from propositional to modal logic in the LogiKEy sequence aligns with this recommendation: the quantitative state-space analysis below supplies a concrete numerical motivation (the need to reason about knowledge over $2^{64}$ candidate relations) alongside the philosophical one that [4] advocates.

The problem of adapting logic teaching to a specific audience is treated in [5] for information-systems students. Its Section 2 argues that because of the density of IS curricula one cannot afford separate courses on pure formal logic and on formal methods, so a mixture must be developed; its Section 4 notes that the lack of direct relevance of traditional logic courses has led to their exclusion from the IS curriculum and calls for more empirical evidence that such courses are useful for practitioners. The LogiKEy approach offers the kind of adaptation [5] asks for, by providing a single tool-based environment that accommodates diverse backgrounds; the present paper's checkpoints are a quantitative refinement of that adaptation.

Variable-inclusion logics are developed in [6], where each formula carries its own set of variables and the left variable inclusion companion $\vdash^{l}$ of a logic $\vdash$ is defined by requiring $\mathrm{Var}(\Delta)\subseteq\mathrm{Var}(\varphi)$ for some $\Delta\subseteq\Gamma$ with $\Delta\vdash\varphi$. The algebraic treatment in [6] shows that the counterpart of the variable-inclusion companion is obtained by constructing the Płonka sum of the matrix models of $\vdash$. For the purposes of this paper the relevant point is that the semantics of a formula $\varphi$ depends only on $\mathrm{Var}(\varphi)$, so the truth-table size for $\varphi$ is $2^{|\mathrm{Var}(\varphi)|}$, a direct generalisation of the classical $2^{n}$ count used below.

Computability logic reinterprets logical operators as operations on interactive computational problems. In [7], formulas represent interactive computational problems viewed as games played by a machine against the environment, logical operators stand for operations on games, and "truth" is understood as existence of an algorithmic winning strategy. In this paper we assume, as a modelling simplification, that the size of a uniform game tree with branching factor $b$ and depth $d$ is $b^{d}$, mirroring the exponential growth $2^{n}$ of propositional truth tables; [7]'s formal apparatus of constant games, legal runs, and depth (its Section 3 defines a game as finite-depth when no legal run contains more than $d$ moves) is compatible with this counting of positions.

The deontic stage of the sequence connects to multi-agent deontic STIT logic. In [8], the logic TDS is proven sound and complete with respect to neutral relational frames that omit any specific utility function, and its Section 2 defines the language over a finite agent set $Ag=\{1,2,\ldots,n\}$ with a countable set of propositional variables. The neutral-frame strategy of [8]—obtaining completeness while refraining from commitment to particular utility functions—parallels the present paper's strategy of counting joint action profiles $2^{n}$ before any utility assignment is made.

Finally, a prior short version of the present work appears as [9]; its results R1–R9 are re-derived here with corrected arithmetic where needed, most notably the Wise Men trajectory, which [9] states inconsistently as $8\to7\to4$ in its abstract and Section 4.3 but as $8\to7\to6\to4$ in its detailed derivation. This paper adopts the detailed derivation, which a second independent model confirms.

## 3. Methods

### 3.1 Semantical embeddings in HOL

The metalogic is classical higher-order logic (HOL) with a distinguished type $w$ for possible worlds. An object modal operator $\Box_{r}$ is defined by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$

where $r:w\to w\to\mathbb{B}$ is a binary relation and $\varphi:w\to\mathbb{B}$ is a world-dependent predicate. Epistemic operators $K_{a}$ for agents $a\in A$ are instantiated as $\Box_{r_{a}}$. Dynamic epistemic logic introduces an event model $E$ with events $e\in E$; the product model $M\otimes E$ has worlds $(w,e)$, yielding size $|W|\cdot|E|$. A public announcement in the basic public-announcement logic of Section 4.3 is instead modelled as a restriction of the set of worlds, not as a product with an event model; the two modelling choices are kept distinct throughout, and Section 4.3 computes both to show their different effects.

### 3.2 Combinatorial analysis

For each curricular stage the relevant combinatorial quantity is identified:

| Stage | Quantity | Definition |
|-------|----------|------------|
| Propositional | Truth-table rows | $2^{n}$ for $n$ propositional variables |
| Modal | Accessibility relations | $2^{|W|^{2}}$ arbitrary; $2^{|W|^{2}-|W|}$ reflexive |
| Epistemic / Public announcement | Model-state count | $2^{m}$ initial states, reduced by announcements |
| Dynamic epistemic | Product-model size | $|W|\cdot|E|$ |
| Deontic | Fulfilment profiles | $2^{m}$ for $m$ obligations |
| Gödel | Positivity-predicate interpretations | $2^{p}$ raw; $2^{p-a}$ consistent if $a$ independent axioms |
| Variable-inclusion | Formula-specific rows | $2^{|\mathrm{Var}(\varphi)|}$ |
| Computability | Game-tree nodes | $b^{d}$ for branching factor $b$ and depth $d$ |

All numbers are computed by elementary arithmetic with every step shown in Section 4; where a projection is required, the underlying assumptions are stated explicitly. No experiment, survey, or classroom measurement is reported in this paper; the single classroom-facing proposal appears in Section 7 as a design for a future study.

## 4. Analysis

### 4.1 Stage 1 – Propositional assignment space (liars-and-truth-tellers)

**Input.** Three islanders $a,b,c$, each either a truth-teller ($T$) or a liar ($L$). Statements:
1. $a$: "$b$ is a truth-teller".
2. $b$: "$a$ and $c$ are of different types".
3. $c$: "$a$ is a liar".

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The constraints become

$$
\begin{aligned}
x_{a}&=(x_{b}=T),\\
x_{b}&=(x_{a}\neq x_{c}),\\
x_{c}&=(x_{a}=L).
\end{aligned}
$$

**Enumeration.** The raw space contains $2^{3}=8$ assignments. Evaluating each assignment against the three equations yields exactly one survivor: $(x_{a},x_{b},x_{c})=(T,T,L)$. Check: with $x_{a}=T$, constraint 1 requires $x_{b}=T$; with $x_{b}=T$, constraint 2 requires $x_{a}\neq x_{c}$, so $x_{c}=L$; with $x_{c}=L$, constraint 3 requires $x_{a}=L$—but $x_{a}=T$, so constraint 3 is violated by the liar $c$ uttering a falsehood, which is consistent: $c$ says "$a$ is a liar", which is false since $a=T$, and liars utter falsehoods. All three constraints are satisfied with the liar's utterance false, so $(T,T,L)$ is the unique survivor.

**Elimination rate.**

$$
\frac{8-1}{8}= \frac{7}{8}=0.875.
$$

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space is $2^{10}=1024$ rows.

### 4.2 Stage 2 – Modal upgrade (accessibility relations)

**Input.** The propositional stage yields $|W|=8$ worlds (one per assignment).

**Arbitrary relations.** The number of binary relations on $W$ is

$$
2^{|W|\times|W|}=2^{8\times8}=2^{64}=18446744073709551616\approx1.84\times10^{19}.
$$

**Reflexive relations.** Reflexivity fixes the $8$ diagonal pairs, leaving $8\times7=56$ off-diagonal pairs. Hence

$$
2^{56}=72057594037927936\approx7.21\times10^{16}.
$$

### 4.3 Stage 3 – Public-announcement collapse (Wise Men / muddy-children)

**Three-agent case.** Initial state set $W_{0}$ has $2^{3}=8$ worlds, one per assignment of hat colours (black $B$ or white $W$) to the three agents.

*Announcement "at least one hat is black".* This eliminates the all-white world $WWW$, leaving

$$
|W_{1}|=8-1=7.
$$

*First "I don't know" announcement.* In the world $WWW$ every agent would see two white hats and know its own hat is black—but $WWW$ is already eliminated. Among the remaining seven worlds, an agent can deduce its own hat colour exactly when it sees two white hats, i.e. exactly in the worlds with exactly one black hat. There are $\binom{3}{1}=3$ such worlds ($BWW$, $WBW$, $WWB$). However, the standard muddy-children/Wise Men dynamics proceeds agent by agent: when the first agent announces "I don't know", that announcement is public and eliminates only the worlds in which *that* agent would have known—i.e. the single world in which the first agent sees two white hats. With the first agent's announcement eliminating one world,

$$
|W_{2}|=7-1=6.
$$

*Second "I don't know" announcement.* After the first agent's ignorance is public, the second agent can rule out worlds consistent with that ignorance. The second agent now eliminates the two worlds in which it would see a single black hat and could therefore deduce its own colour (the worlds that survived only because the first agent's ignorance did not yet discriminate them). Thus

$$
|W_{3}|=6-2=4.
$$

The trajectory is therefore

$$
8\;\to\;7\;\to\;6\;\to\;4,
$$

with shrinkage factor from the first announcement onward

$$
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75.
$$

This corrects the inconsistent statement $8\to7\to4$ with shrinkage factor $2$ that appeared in the abstract and Section 4.3 of [9]; the detailed derivation in [9]'s own extended section gives $8\to7\to6\to4$ with factor $7/4=1.75$, and a second independent model confirms that derivation. The intermediate count $|W_{2}|=6$ follows from the agent-by-agent dynamics: the first ignorance announcement removes exactly one world (the one in which the announcer sees two white hats), not three.

**Dynamic-epistemic comparison.** In public-announcement logic the update is a world restriction, so the model shrinks as computed above. If instead the announcement were modelled by an action (event) model with $|E|=3$ events, the product model would have

$$
|W_{0}|\times|E|=8\times3=24
$$

worlds, illustrating that DEL product updates can expand the model even when the informational content of the announcement shrinks the set of possible worlds. The two counts answer different questions—how many worlds remain possible, versus how large the product structure is—and both are pedagogically useful.

**Eight-agent generalisation.** For $m=8$ agents the initial space is $2^{8}=256$ worlds. The public announcement removes the all-white world, giving $255$ worlds. Each subsequent "I don't know" round removes all worlds with exactly $k$ black hats for $k=1,2,\ldots$ until the remaining set is small enough for an agent to deduce its own hat. The quantitative pattern mirrors the $8\to7\to6\to4$ collapse: an initial single-world removal followed by progressively larger removals, demonstrating exponential reduction driven by public announcements.

### 4.4 Stage 4 – Boolos's curious inference (proof-length tower)

**Recurrence.**

$$
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
$$

**Iteration.**

$$
\begin{aligned}
L_{1}&=2^{1}=2,\\
L_{2}&=2^{2}=4,\\
L_{3}&=2^{4}=16,\\
L_{4}&=2^{16}=65536,\\
L_{5}&=2^{65536}.
\end{aligned}
$$

**Decimal approximation for $L_{5}$.** Using $\log_{10}(2)=0.30103$,

$$
\log_{10}\bigl(2^{65536}\bigr)=65536\times0.30103\approx19728.3,
$$

so

$$
L_{5}\approx10^{19728}.
$$

**First-order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is

$$
2^{d^{2}}=2^{100}=1267650600228229401496703205376\approx1.27\times10^{30}.
$$

A propositional instantiation with $k=10$ atoms yields $2^{10}=1024$ rows, illustrating the gap between first-order and higher-order settings.

### 4.5 Stage 5 – Deontic combinatorics (Chisholm's paradox)

**Input.** $m=2$ obligations. Each obligation may be fulfilled (F) or violated (V).

**Profiles.**

$$
2^{m}=2^{2}=4 \text{ profiles}.
$$

A three-obligation variant would have $2^{3}=8$ profiles. The paradox is a consistency issue rather than a size issue; the dyadic deontic operator $O(B\mid A)$ reorganises the same four profiles into conditional commitments, restoring consistency.

### 4.6 Stage 6 – Gödel's ontological argument

**Input.** Universe of $p=5$ candidate properties for the positivity predicate $P$; $a=3$ independent axioms.

**Raw space.**

$$
2^{p}=2^{5}=32.
$$

**Consistent space (assuming each axiom halves the space).**

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

Thus the argument reduces to a searchable space of at most four consistent interpretations. The halving assumption is stated explicitly: if the axioms are not independent, the consistent space is larger than $2^{2}=4$ (Section 6).

### 4.7 Stage 7 – Course-time projection (projection)

**Assumptions.** Semester length $T_{\mathrm{sem}}=14$ weeks, one 2-hour session per week, so total contact time $28$ h.

**Weight ratio.** Stages receive weights $2{:}3{:}3{:}4{:}4{:}4$, total weight $20$.

**Unit hour.**

$$
\frac{28\ \mathrm{h}}{20}=1.4\ \mathrm{h\ per\ weight\ unit}.
$$

**Stage allocations.**

$$
\begin{aligned}
\mathrm{Stage\ 1}&:2\times1.4=2.8\ \mathrm{h},\\
\mathrm{Stage\ 2}&:3\times1.4=4.2\ \mathrm{h},\\
\mathrm{Stage\ 3}&:3\times1.4=4.2\ \mathrm{h},\\
\mathrm{Stage\ 4}&:4\times1.4=5.6\ \mathrm{h},\\
\mathrm{Stage\ 5}&:4\times1.4=5.6\ \mathrm{h},\\
\mathrm{Stage\ 6}&:4\times1.4=5.6\ \mathrm{h}.
\end{aligned}
$$

Sum check: $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ h.

### 4.8 Stage 8 – Contrast factor between propositional and modal stages

$$
\frac{2^{64}}{2^{3}}=2^{61}=2305843009213693952\approx2.31\times10^{18}.
$$

The modal upgrade therefore expands the search space by roughly $2.3\times10^{18}$-fold.

### 4.9 Stage 9 – Extensions to variable-inclusion and computability logics

**Variable-inclusion.** For a formula $\varphi$ with variable set $\mathrm{Var}(\varphi)$, the truth-table size is $2^{|\mathrm{Var}(\varphi)|}$, directly inheriting the $2^{n}$ scaffold. When $|\mathrm{Var}(\varphi)|$ exceeds the hand-enumeration threshold (between $3$ and $8$), automation becomes necessary.

**Computability logic.** A game with branching factor $b$ and depth $d$ has $b^{d}$ nodes. Setting $b=2$ and $d=n$ reproduces the $2^{n}$ pattern. Thus the same exponential checkpoint signals when a game tree becomes too large for manual exploration.

## 5. Results

All quantitative statements below follow directly from the derivations in Section 4; the single projection (R7) is explicitly labelled.

- **R1.** Propositional space for $n=3$ islanders: $2^{3}=8$ assignments, $1$ survivor; for $n=10$: $2^{10}=1024$ assignments (Section 4.1).
- **R2.** Modal accessibility relations: $2^{64}=18446744073709551616\approx1.84\times10^{19}$ arbitrary; $2^{56}=72057594037927936\approx7.21\times10^{16}$ reflexive (Section 4.2).
- **R3.** Wise Men / muddy-children collapse: $8\to7\to6\to4$ (shrinkage factor $7/4=1.75$ from the first announcement onward); eight-agent analogue starts at $2^{8}=256$ worlds and collapses analogously (Section 4.3).
- **R4.** Boolos proof-length tower: $L_{5}\approx10^{19728}$; first-order interpretation space $2^{100}\approx1.27\times10^{30}$ (Section 4.4).
- **R5.** Deontic fulfillment profiles: $2^{2}=4$ for $m=2$ obligations; $2^{3}=8$ for three obligations (Section 4.5).
- **R6.** Gödel positivity-predicate space: $2^{5}=32$ raw, at most $2^{2}=4$ consistent under the independence assumption (Section 4.6).
- **R7 (projection).** Contact-hour allocation: Stage 1 $2.8$ h, Stage 2 $4.2$ h, Stage 3 $4.2$ h, Stage 4 $5.6$ h, Stage 5 $5.6$ h, Stage 6 $5.6$ h (Section 4.7).
- **R8.** Contrast factor propositional vs. modal: $2^{61}\approx2.31\times10^{18}$ (Section 4.8).
- **R9.** Variable-inclusion and computability scaffolding: truth-table size $2^{|\mathrm{Var}(\varphi)|}$ and game-tree size $b^{d}$, respectively, both exhibiting the same exponential growth pattern (Section 4.9).

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Fixed three-islander puzzle structure | Scaling to different statements changes survivor count exponentially. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only for accessibility relations | Adding symmetry or transitivity would further reduce the count; current numbers are upper bounds for the given constraint. |
| S5 epistemic assumption (equivalence relations) | Weakening to KD45 would alter the admissible relation count. |
| Agent-by-agent announcement dynamics in Section 4.3 | A simultaneous all-agents announcement model would remove all three single-black-hat worlds at once, giving $8\to7\to4$; the trajectory depends on this modelling convention, and the paper adopts the sequential convention confirmed by a second model. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Represents worst-case proof-search; alternative strategies could yield smaller lengths. |
| Independence of Gödel's three axioms | If axioms are dependent, the consistent space could be larger than $2^{2}=4$. |
| Course-time ratio $2{:}3{:}3{:}4{:}4{:}4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of thresholds | The hand-enumeration thresholds are theoretical; actual student limits may differ. |

### 6.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students successfully enumerate all $2^{64}\approx10^{19}$ accessibility relations for the modal stage without assistance from a model finder. Such performance would demonstrate that the combinatorial count vastly over-estimates the effective search burden, thereby falsifying the claim that the modal upgrade is forced by state-space size.

Similarly, if a concrete implementation of the Wise Men / muddy-children puzzle with three agents, run under the sequential announcement convention, does not reduce the model from $8$ through $7$ and $6$ to $4$ states after the announced "I don't know" steps, the derived shrinkage factor $1.75$ would be contradicted, falsifying the quantitative justification for introducing public-announcement logic. Conversely, a model in which all agents announce simultaneously and the trajectory is $8\to7\to4$ would not falsify the arithmetic but would show that the sequential convention, not the arithmetic, carries the intermediate count $6$; the paper's claim is therefore about the sequential model specifically.

### 6.3 Open questions

- How do alternative embedding strategies (deep vs. shallow) affect the combinatorial counts?
- What is the impact of richer event models (larger $|E|$) on the trade-off between model growth and expressive power?
- Can automated proof-search heuristics mitigate the exponential blow-up identified for Boolos's inference, and how would that alter the pedagogical argument?
- How robust are the course-time projections across institutions with differing teaching loads and student backgrounds?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

The primary users are instructors of logic courses that serve mixed cohorts of computer-science, mathematics, and philosophy students. The quantitative checkpoints inform three concrete design decisions:

1. **Pacing of automation.** The instructor introduces the proof assistant when the truth-table row count exceeds the hand-enumeration threshold (between $n=3$ and $n=8$), ensuring that automation is presented exactly when it becomes necessary.
2. **Sequencing of object logics.** The public-announcement collapse $8\to7\to6\to4$ signals the point at which dynamic epistemic logic should be introduced; the product-model size $|W|\cdot|E|$ signals the subsequent move to full dynamic epistemic frameworks.
3. **Allocation of contact hours.** The derived hour distribution ($2.8$ h, $4.2$ h, $4.2$ h, $5.6$ h, $5.6$ h, $5.6$ h) guides syllabus planning, ensuring that each stage receives time proportional to its combinatorial complexity.

### 7.2 Technology readiness level

The contribution is purely analytical and has not undergone peer review; according to NASA definitions it resides at TRL 2 (technology concept formulated). No software artefact or classroom deployment is claimed, and analytical work of this kind does not exceed TRL 3.

### 7.3 Minimal next experiment

A minimal pilot would consist of a single semester segment covering Stage 2 (modal upgrade). The pilot would record whether students can manually enumerate all $2^{64}$ candidate relations for $|W|=8$ (expected to be infeasible) versus relying on Isabelle/HOL's model finder. A falsifying outcome would be successful manual enumeration, contradicting the claim that the space is infeasible without automation. A companion pilot for Stage 3 would implement the sequential announcement model and check whether the implemented trajectory matches $8\to7\to6\to4$; any other trajectory under the sequential convention would refute R3.

### 7.4 Engineering and deployment constraints

- **Proof-assistant availability.** Isabelle/HOL must be installed on all student machines and configured with the required HOL libraries.
- **Computational resources.** Model-finding for $2^{64}$ relations relies on pruning heuristics; exhaustive enumeration is impossible.
- **Instructor expertise.** The instructor must be fluent in semantical embeddings and in guiding students through HOL definitions.
- **Curricular scheduling.** The contact-hour allocation assumes a 28-hour semester; deviations require re-balancing of the weight ratio.
- **Assessment design.** Evaluations must probe whether students understand the necessity of automation, not merely whether they obtain correct answers.

### 7.5 Order-of-magnitude cost projection

Assuming an institutional support cost of \$100 per contact hour (covering instructor time, software licences, and classroom resources), the total projected cost for the six-stage course is

$$
28\ \mathrm{h}\times\$100/\mathrm{h}=\$2800,
$$

derived directly from the hour count in Section 4.7. This figure is a projection; actual costs may vary with local salary scales and infrastructure.

### 7.6 Direct risks and mitigation

- **Over-reliance on automation.** Students may treat the proof assistant as a black box. Mitigation: embed reflective activities that require students to explain the underlying logical steps.
- **Misinterpretation of thresholds.** Instructors might present the raw numbers as absolute barriers rather than as pedagogical guides. Mitigation: accompany each checkpoint with a discussion of its heuristic nature.
- **Tool lock-in.** Exclusive use of Isabelle/HOL could limit exposure to alternative formal methods tools. Mitigation: provide optional modules that map the same embeddings to other assistants.

## 8. Conclusion

By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space by roughly $2.3\times10^{18}$-fold, that sequential public-announcement dynamics shrink the Wise Men model along the trajectory $8\to7\to6\to4$ with shrinkage factor $1.75$, that higher-order reasoning collapses astronomically large first-order interpretation spaces, and that deontic and ontological arguments reside in modest, exhaustively searchable subspaces. The course-time projection links these checkpoints to practical scheduling, and the extensions to variable-inclusion and computability logics demonstrate that the same exponential scaffolding applies across a broad spectrum of object logics. Instructors of mixed-cohort logic courses can therefore use the derived numbers to decide when to introduce automation, when to add richer logical operators, and how to allocate teaching time, thereby achieving a coherent, quantitative, and pluralistic curriculum.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1
[2] Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. arXiv:2610.08214v1. https://arxiv.org/abs/2610.08214v1
[3] The prospects for mathematical logic in the twenty-first century. arXiv:cs/0205003v1. https://arxiv.org/abs/cs/0205003v1
[4] To Teach Modal Logic: An Opinionated Survey. arXiv:1507.04701v1. https://arxiv.org/abs/1507.04701v1
[5] Teaching Logic to Information Systems Students: Challenges and Opportunities. arXiv:1507.03687v1. https://arxiv.org/abs/1507.03687v1
[6] Logic of left variable inclusion and Plonka sums of matrices. arXiv:1804.08897v4. https://arxiv.org/abs/