# Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum (Version 2.2.0)

## Abstract

Mixed cohorts of computer-science, mathematics, and philosophy students face fragmented logic curricula that either overload or under-serve particular backgrounds, raising instructional cost and reducing learning coherence. The LogiKEy methodology supplies a unified metalogic—classical higher-order logic (HOL) hosting object logics through semantical embeddings—but published treatments stop short of explicit numerical checkpoints that justify each transition between object logics. This paper combines semantical embeddings in HOL with elementary combinatorial analysis of the state spaces that arise at each curricular stage. The analysis derives (1) the propositional assignment space $2^{3}=8$ with a single survivor for the liars-and-truth-tellers puzzle; (2) $2^{64}\approx1.84\times10^{19}$ arbitrary and $2^{56}\approx7.21\times10^{16}$ reflexive accessibility relations for the modal re-modeling; (3) the Wise Men / muddy-children model trajectory $8\to7\to6\to4$ with shrinkage factor $7/4=1.75$ from the first announcement onward, and its generalisation to $2^{8}=256$ initial worlds for eight agents; (4) the proof-length tower $L_{5}\approx10^{19\,728}$ for Boolos's curious inference; (5) the deontic fulfillment profile count $2^{m}$ with $m=2$; (6) the Gödel ontological argument's raw and consistent positivity-predicate interpretations $2^{5}=32$ and $2^{2}=4$; (7) a contact-hour allocation projected from a 28-hour semester and a $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$ weight ratio; and (8) the contrast factor $2^{61}\approx2.31\times10^{18}$ between the propositional and modal stages. These checkpoints turn pedagogical intuition into concrete numerical milestones that inform curriculum design, automation adoption, and resource planning for pluralistic logic teaching.

## 1. Introduction

Logic courses that simultaneously serve computer-science, mathematics, and philosophy students encounter a concrete problem: each discipline arrives with distinct expectations about the role of logic, the nature of proof, and the desired applications, yet curricula are typically organised around a single object logic. The same classroom may hold a student who programs fluently but has never written a proof, one who writes rigorous proofs but has never seen them checked by a machine, and one who argues subtly in natural language but freezes at a quantifier—a situation described directly in the LogiKEy report on proof-assistant-based logic teaching [2]. The resulting fragmentation forces students to master multiple notations and toolchains, while monotonic courses that remain in classical first-order logic leave philosophy students without the modal and deontic resources they need and computer-science students without the modelling primitives required for verification tasks. The cost of this mismatch appears as additional contact hours, duplicated teaching materials, and lower learning outcomes, and the capability that would resolve it is a unified, quantitative framework that tells instructors precisely when a richer object logic becomes necessary.

The LogiKEy methodology supplies the unifying metalogic—classical higher-order logic (HOL)—and demonstrates how object logics can be embedded semantically in a single proof assistant such as Isabelle/HOL, whose automated theorem provers and (counter-)model finders become part of one environment in which students learn, experiment with, and compare logics [1, 2]. What remains missing is a set of explicit numerical thresholds that justify each pedagogical transition. This paper fills that gap by deriving, from first principles, the combinatorial quantities that grow (or shrink) at each stage of the LogiKEy example sequence and by mapping those quantities to curriculum-design decisions. Every derivation is elementary and reproducible; the single projection (contact-hour allocation) is labelled as such with its assumptions stated.

**Contributions.**
* **C1.** Exact derivation of the propositional assignment space and survivor count for the liars-and-truth-tellers puzzle (Section 4.1, Result R1).
* **C2.** Enumeration of arbitrary and reflexive accessibility relations for the modal re-modeling (Section 4.2, Result R2).
* **C3.** Quantitative analysis of the Wise Men / muddy-children state-space collapse, with the corrected trajectory $8\to7\to6\to4$, and its generalisation to eight agents (Section 4.3, Result R3).
* **C4.** Construction of the proof-length tower for Boolos's curious inference (Section 4.4, Result R4).
* **C5.** Counting of deontic fulfillment profiles for Chisholm's paradox (Section 4.5, Result R5).
* **C6.** Calculation of raw and consistent positivity-predicate interpretations for Gödel's ontological argument (Section 4.6, Result R6).
* **C7.** Projection of contact-hour allocation for a six-stage semester course (Section 4.7, Result R7).
* **C8.** Derivation of the contrast factor between propositional and modal stages (Section 4.8, Result R8).
* **C9.** Extension of the exponential scaffolding to variable-inclusion and computability logics (Section 4.9, Result R9).

## 2. Background and Related Work

The LogiKEy methodology is presented in [1] and [2], which report more than a decade of experience teaching logic to mixed groups of computer-science, mathematics, and philosophy students. Both works state the central design: classical HOL, with quantification over functions and predicates and $\lambda$-abstraction, serves as a universal metalogic in which object logics are encoded by defining their semantics, so that a single proof assistant with automated theorem provers and (counter-)model finders becomes one environment for learning and comparing logics. Their graded sequence of classroom examples—liars-and-truth-tellers, Wise Men, Boolos's curious inference, Chisholm's paradox, Gödel's ontological argument—each transition motivated by a limitation of the preceding representation, is exactly the sequence whose state spaces this paper quantifies. Their conclusion distinguishes what is established (machine-checked formal results and the methodological claim that one metalogic carries all of them) from what is documented only by teaching experience (that a mixed cohort can run such a course); the present paper adds a third layer, quantitative checkpoints, that is neither machine-checked theorem nor classroom anecdote but derivable arithmetic.

The pedagogical problem of heterogeneous audiences is not unique to the LogiKEy setting. The survey of logic teaching for information-systems students [5] documents that logic plays a practically non-existent role in IS curricula even though it is a recognised mathematical requirement in computer science, and argues that a significant adaptation of contents and teaching methodologies is required rather than exclusion; it also reports that dense curricula cannot afford separate courses on pure formal logic and on formal methods, so a mixture must be developed. This supports the LogiKEy premise, adopted here, that a single adapted environment serving mixed backgrounds is preferable to parallel tracks, and it supplies the practical pressure—curriculum density—that makes quantitative pacing decisions valuable.

For the modal stage specifically, the opinionated survey [4] argues that the teaching of modal logic should be reoriented: the dose of mathematical modal logic introduced should be estimated from the philosophical problems modal logic was built to clarify, with the mathematics instrumental rather than the sole motive of concern. The transition from propositional to modal logic in the LogiKEy sequence aligns with this recommendation, and the quantitative state-space analysis of Section 4.2 supplies a concrete complement to it: the philosophical motivation (the need to reason about knowledge and necessity) arrives together with a numerical justification (the explosion from $2^{3}$ assignments to $2^{64}$ candidate relations) for bringing automation into the classroom at that point.

The proof-theoretic stage connects to a broader agenda set out in [3], whose panel-derived survey of mathematical logic's prospects includes a section by Sam Buss on proof theory and logic for computer science that presents a three-fold view of proof-theoretic work by goals and closes with an exhortation for mathematical logicians to pay more attention to applications of logic in computer science. The proof-length tower of Section 4.4 sits squarely in the proof-theory-for-computer-science quadrant of that view: proof-length blow-up is precisely the phenomenon that makes automated proof search, rather than hand proof, the pedagogically honest presentation of Boolos's curious inference.

Variable-inclusion logics are treated algebraically in [6], which defines, for an arbitrary propositional logic $\vdash$, substitution-invariant consequence relations $\vdash^{l}$ and $\vdash^{r}$ satisfying left and right variable inclusion principles, with $\vdash^{l}\varphi$ requiring a subset $\Delta\subseteq\Gamma$ whose variables are contained in those of $\varphi$; the paper shows that the algebraic counterpart of the variable-inclusion companion is obtained by constructing the Plonka sum of the matrix models of $\vdash$. For the present paper the relevant point is the object-level notion $\mathrm{Var}(\varphi)$, the set of variables really occurring in a formula, which makes truth-table size formula-relative: Section 4.9 uses $2^{|\mathrm{Var}(\varphi)|}$ as the direct generalisation of the classical $2^{n}$ count.

Computability logic reinterprets logical operators as operations on interactive computational problems: formulas represent games played by a machine against the environment, and truth means existence of an algorithmic winning strategy [7]. That work develops the program toward applied theories, defining notions such as finite-depth games, where depth is the smallest integer $d$ bounding the number of moves in a legal run. Section 4.9 assumes, as a modelling simplification stated explicitly there, that a game tree with uniform branching factor $b$ and depth $d$ has $b^{d}$ nodes, mirroring the exponential growth $2^{n}$ of propositional truth tables; the game-theoretic semantics of [7] is what makes such a tree-size quantity the natural complexity measure for that logic.

The deontic stage draws on the neutral temporal deontic STIT logic of [8], which introduces the multi-agent logic TDS over a language with a finite agent set $Ag=\{1,2,\ldots,n\}$ and proves it sound and complete with respect to relational frames that employ no utility functions, subsequently showing how such neutral frames transform into frames with utility assignments while preserving truth. Two points carry over to this paper: the agent-indexed counting in Section 4.5 (fulfillment profiles over $m$ obligations) and the STIT-style observation that a finite agent set with binary choices yields $2^{n}$ joint profiles, which Section 6.4 connects to the $2^{3}=8$ worlds of the propositional stage.

Finally, a prior short version of the present work appears as [9]; the analysis here corrects and extends that version, most notably replacing its Wise Men trajectory $8\to7\to4$ with the derivation $8\to7\to6\to4$ given in Section 4.3 and Section 6.1.

## 3. Methods

### 3.1 Semantical embeddings in HOL

The metalogic is classical higher-order logic (HOL) with a distinguished type $w$ for possible worlds. An object modal operator $\Box_{r}$ is defined by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$

where $r:w\to w\to\mathbb{B}$ is a binary relation on worlds and $\varphi:w\to\mathbb{B}$ is a world-valued predicate. This is the shallow semantical embedding pattern by which the LogiKEy methodology turns HOL into a host for other logics [2]: the modal connective simply becomes a function on world-dependent propositions. Epistemic operators $K_{a}$ for agents $a\in A$ are instantiated as $\Box_{r_{a}}$, one relation per agent. Dynamic epistemic logic introduces an event model $E$ with events $e\in E$; the product model $M\otimes E$ has worlds $(w,e)$, so its size is $|W|\cdot|E|$. Public announcements in this paper are modelled semantically, as restrictions of the world set of $M$ itself, and the product-update construction is invoked only in Section 6.1 as a contrast case with $|E|=3$.

### 3.2 Combinatorial analysis

For each curricular stage the relevant combinatorial quantity is identified:

| Stage | Quantity | Definition |
|-------|----------|------------|
| Propositional | Truth-table rows | $2^{n}$ for $n$ propositional variables |
| Modal | Accessibility relations | $2^{|W|^{2}}$ arbitrary; $2^{|W|^{2}-|W|}$ reflexive |
| Epistemic / Public announcement | Model-state count | $2^{m}$ initial states, reduced by announcements |
| Dynamic epistemic | Product-model size | $|W|\cdot|E|$ |
| Deontic | Fulfilment profiles | $2^{m}$ for $m$ obligations |
| Gödel | Positivity-predicate interpretations | $2^{p}$ raw; $2^{p-a}$ consistent if $a$ independent axioms each halve the space |
| Variable-inclusion | Formula-specific rows | $2^{|\mathrm{Var}(\varphi)|}$ |
| Computability | Game-tree nodes | $b^{d}$ for branching factor $b$ and depth $d$ |

All numbers are computed by elementary arithmetic in Section 4, with every input stated and every step shown; where a projection is required (Section 4.7), the underlying assumptions are stated explicitly and the result is labelled a projection. The Wise Men derivation follows the standard public-announcement-logic semantics: each announcement is a model restriction that removes exactly those worlds in which the announcing agent could determine its own hat, and the trajectory is recomputed world by world in Section 6.1 so that the headline numbers of Section 4.3 and the detailed derivation agree.

## 4. Analysis

### 4.1 Stage 1 – Propositional assignment space (liars-and-truth-tellers)

**Input.** Three islanders $a,b,c$, each either a truth-teller ($T$) or a liar ($L$). Statements:
1. $a$: "$b$ is a truth-teller".
2. $b$: "$a$ and $c$ are of different types".
3. $c$: "$a$ is a liar".

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. A truth-teller's statement is true and a liar's false, so the constraints are

$$
\begin{aligned}
x_{a}&=(x_{b}=T),\\
x_{b}&=(x_{a}\neq x_{c}),\\
x_{c}&=(x_{a}=L).
\end{aligned}
$$

**Enumeration.** The raw space contains $2^{3}=8$ assignments. Checking each: if $x_{a}=L$ then constraint 1 forces $x_{b}=L$, constraint 3 forces $x_{c}=T$, and constraint 2 then requires $x_{a}\neq x_{c}$, i.e. $L\neq T$, which holds; but constraint 1 with $x_{a}=L$ requires $x_{b}\neq T$, consistent—however constraint 2 with $(x_{a},x_{b},x_{c})=(L,L,T)$ gives $x_{b}=(L\neq T)=T$, contradicting $x_{b}=L$. So no assignment with $x_{a}=L$ survives. If $x_{a}=T$, constraint 1 forces $x_{b}=T$; constraint 3 forces $x_{c}=L$; constraint 2 requires $x_{b}=(x_{a}\neq x_{c})=(T\neq L)=T$, which holds. Exactly one survivor: $(x_{a},x_{b},x_{c})=(T,T,L)$.

**Elimination rate.**

$$
\frac{8-1}{8}= \frac{7}{8}=0.875.
$$

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space is $2^{10}=1\,024$ rows, past comfortable hand enumeration.

### 4.2 Stage 2 – Modal upgrade (accessibility relations)

**Input.** The propositional stage yields $|W|=8$ worlds (one per assignment).

**Arbitrary relations.** A binary relation on $W$ is a subset of $W\times W$, and $|W\times W|=8\times8=64$, so the number of relations is

$$
2^{|W|\times|W|}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
$$

**Reflexive relations.** Reflexivity fixes the $8$ diagonal pairs as necessarily present, leaving $8\times7=56$ off-diagonal pairs free. Hence

$$
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}.
$$

### 4.3 Stage 3 – Public-announcement collapse (Wise Men / muddy-children)

**Three-agent case.** Initial state set $W_{0}$ has $2^{3}=8$ worlds (one per colour assignment).

*Announcement "at least one hat is black"* eliminates the all-white world, leaving

$$
|W_{1}|=8-1=7.
$$

*First "I don't know" announcement.* In the world with exactly one black hat, the two agents wearing white each see one black and one white hat and would know their own hat is black; the black-hatted agent sees two white hats and would know its own hat is black. All three single-black-hat worlds are therefore ruled out *for some agent*, but the announcement is made by a specific agent, and an agent's "I don't know" only eliminates worlds that that agent could distinguish. In the world $WWB$ (only $c$ black), agent $a$ sees two white hats and would know its own colour; $a$'s announcement of ignorance therefore eliminates $WWB$ alone:

$$
|W_{2}|=7-1=6.
$$

*Second "I don't know" announcement.* After $a$'s announcement, agent $b$ can use it: in the worlds $BBW$ and $WBW$, $b$ sees a single black hat on the other visible agent and, combined with $a$'s announced ignorance, can deduce its own colour; $b$'s announcement of ignorance eliminates both:

$$
|W_{3}|=6-2=4.
$$

Thus the trajectory is

$$
8\;\to\;7\;\to\;6\;\to\;4,
$$

with shrinkage factor from the first announcement onward

$$
\frac{|W_{1}|}{|W_{3}|}=\frac{7}{4}=1.75.
$$

The full world-by-world derivation, including the identification of the four surviving worlds, is given in Section 6.1; the trajectory stated here and there is the same derivation, and the earlier published value $8\to7\to4$ (which dropped the intermediate $6$) is superseded by it.

**Eight-agent generalisation.** For $m=8$ agents the initial space is $2^{8}=256$ worlds. The public announcement removes the all-white world, giving $255$ worlds. Each subsequent "I don't know" round removes all worlds in which the announcing agent, given prior announcements, could deduce its own hat; in the standard muddy-children induction the process peels off worlds layer by layer until the remaining set is small enough for each agent to infer its own colour. The quantitative pattern mirrors the $8\to7\to6\to4$ collapse: a sequence of public announcements each removing a computable layer of worlds, demonstrating exponential reduction driven by iterated knowledge gain. The exact per-round counts for $m=8$ depend on the announcement order and are left as an open computational exercise (Section 7.3); what is derived exactly here is the initial count $2^{8}=256$ and the first step $256-1=255$.

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
L_{4}&=2^{16}=65\,536,\\
L_{5}&=2^{65\,536}.
\end{aligned}
$$

**Decimal approximation for $L_{5}$.** Using $\log_{10}(2)=0.30103$,

$$
\log_{10}\bigl(2^{65\,536}\bigr)=65\,536\times0.30103=19\,728.30308,
$$

so

$$
L_{5}\approx10^{19\,728}.
$$

**First-order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations of that predicate is

$$
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}.
$$

A propositional instantiation with $k=10$ atoms yields $2^{10}=1\,024$ rows, illustrating the gap between first-order and propositional settings.

### 4.5 Stage 5 – Deontic combinatorics (Chisholm's paradox)

**Input.** $m=2$ obligations. Each obligation may be fulfilled (F) or violated (V).

**Profiles.**

$$
2^{m}=2^{2}=4\ \text{profiles}.
$$

A three-obligation variant would have $2^{3}=8$ profiles. The paradox is a consistency issue rather than a size issue: the dyadic deontic operator $O(B\mid A)$ reorganises the same four profiles into conditional commitments, restoring consistency. The agent-indexed counting of the STIT framework [8], where a finite agent set $Ag=\{1,\ldots,n\}$ with binary choices yields $2^{n}$ joint profiles, is developed in Section 6.4.

### 4.6 Stage 6 – Gödel's ontological argument

**Input.** Universe of $p=5$ candidate properties for the positivity predicate $P$; $a=3$ independent axioms, each assumed to halve the space of admissible interpretations.

**Raw space.**

$$
2^{p}=2^{5}=32.
$$

**Consistent space (under the halving assumption).**

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

Under this assumption the argument reduces to a searchable space of at most four consistent interpretations. The halving assumption is a modelling idealisation: if the axioms are not independent, the consistent space is larger than $2^{2}=4$ (Section 7.1).

### 4.7 Stage 7 – Course-time projection (projection)

**Assumptions.** Semester length $T_{\text{sem}}=14$ weeks, one 2-hour session per week, so total contact time $28$ h. These are the paper's own assumptions, stated as such.

**Weight ratio.** Stages receive weights $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$; total weight $2+3+3+4+4+4=20$.

**Unit hour.**

$$
\frac{28\ \text{h}}{20}=1.4\ \text{h per weight unit}.
$$

**Stage allocations.**

$$
\begin{aligned}
\text{Stage 1}&:2\times1.4=2.8\ \text{h},\\
\text{Stage 2}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 3}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 4}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 5}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 6}&:4\times1.4=5.6\ \text{h}.
\end{aligned}
$$

Sum check: $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ h.

### 4.8 Stage 8 – Contrast factor between propositional and modal stages

$$
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18}.
$$

The modal upgrade therefore expands the space of candidate structures by a factor of $2^{61}\approx2.31\times10^{18}$ relative to the propositional assignment space.

### 4.9 Stage 9 – Extensions to variable-inclusion and computability logics

**Variable-inclusion.** For a formula $\varphi$ with variable set $\mathrm{Var}(\varphi)$ as defined in the algebraic treatment of variable-inclusion logics [6], the truth-table size is $2^{|\mathrm{Var}(\varphi)|}$, directly inheriting the $2^{n}$ scaffold. When $|\mathrm{Var}(\varphi)|$ exceeds the hand-enumeration threshold (between $3$ and $8$), automation becomes necessary; a worked example with $|\mathrm{Var}(\varphi)|=5$ is given in Section 6.2.

**Computability logic.** Computability logic treats formulas as interactive games between a machine and its environment, with truth as existence of an algorithmic winning strategy [7]. We assume, as a stated modelling simplification, that a game tree with uniform branching factor $b$ and depth $d$ has $b^{d}$ nodes. Setting $b=2$ and $d=n$ reproduces the $2^{n}$ pattern; worked numbers for $b=2,3$ and $d=4$ appear in Section 6.3. The same exponential checkpoint signals when a game tree becomes too large for manual exploration.

## 5. Results

All quantitative statements below follow directly from the derivations in Section 4; the single projection (R7) is explicitly labelled.

* **R1.** Propositional space for $n=3$ islanders: $2^{3}=8$ assignments, $1$ survivor, elimination rate $7/8=0.875$; for $n=10$: $2^{10}=1\,024$ assignments (Section 4.1).
* **R2.** Modal accessibility relations: $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary; $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive (Section 4.2).
* **R3.** Wise Men / muddy-children collapse: $8\to7\to6\to4$, with shrinkage factor $7/4=1.75$ from the first announcement onward; eight-agent analogue starts at $2^{8}=256$ worlds and drops to $255$ after the first public announcement (Section 4.3).
* **R4.** Boolos proof-length tower: $L_{5}\approx10^{19\,728}$; first-order interpretation space $2^{100}\approx1.27\times10^{30}$ (Section 4.4).
* **R5.** Deontic fulfillment profiles: $2^{2}=4$ for $m=2$ obligations; $2^{3}=8$ for three obligations (Section 4.5).
* **R6.** Gödel positivity-predicate space: $2^{5}=32$ raw, $2^{2}=4$ consistent under the stated halving assumption (Section 4.6).
* **R7 (projection).** Contact-hour allocation: Stage 1 $2.8$ h, Stage 2 $4.2$ h, Stage 3 $4.2$ h, Stage 4 $5.6$ h, Stage 5 $5.6$ h, Stage 6 $5.6$ h, under the assumptions of Section 4.7 (Section 4.7).
* **R8.** Contrast factor propositional vs. modal: $2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18}$ (Section 4.8).
* **R9.** Variable-inclusion and computability scaffolding: truth-table size $2^{|\mathrm{Var}(\varphi)|}$ and assumed game-tree size $b^{d}$, both exhibiting the same exponential growth pattern (Section 4.9).

## 6. Extended Derivations and Worked Examples

### 6.1 Detailed derivation of the Wise Men / muddy-children trajectory

The three-agent Wise Men puzzle is modelled in an S5 epistemic setting (agents have equivalence relations over worlds). The initial world set is

$$
|W_{0}| = 2^{3}=8 .
$$

Label worlds by the black-hatted agents: $WWW$, $BWW$, $WBW$, $WWB$, $BBW$, $BWB$, $WBB$, $BBB$.

The king's public announcement "at least one hat is black" eliminates the all-white world, giving

$$
|W_{1}| = 8-1 = 7 .
$$

Each subsequent "I don't know" announcement removes exactly those worlds in which the announcing agent would be able to infer its own hat colour. For agent $a$: in the world $WWB$, $a$ sees two white hats and, after the king's announcement, knows its own hat is black; in every other surviving world $a$ sees at least one black hat and cannot determine its own colour. Agent $a$'s announcement of ignorance therefore eliminates the single world $WWB$:

$$
|W_{2}| = 7-1 = 6 .
$$

Agent $b$ now reasons with both announcements. In the world $BBW$, $b$ sees exactly one black hat (on $a$); if $b$'s own hat were white, the world would be $WBW$, in which $a$ would have seen two white hats and known its colour—contradicting $a$'s announced ignorance. So $b$ deduces its hat is black in $BBW$. In the world $WBW$, $b$ sees exactly one black hat (on $c$); if $b$'s own hat were white, the world would be $WWB$, which $a$'s announcement has already eliminated. So $b$ deduces its hat is black in $WBW$ as well. Agent $b$'s announcement of ignorance eliminates both worlds:

$$
|W_{3}| = 6-2 = 4 .
$$

The four surviving worlds are $BWB$, $WBB$, $BBB$, and $BWW$; in each, every agent still sees at least one black hat other than possibly its own in a way consistent with both ignorance announcements, and the third agent $c$ can now proceed analogously. The shrinkage factor from the first announcement onward is

$$
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75 .
$$

This trajectory $8\to7\to6\to4$ is the derivation of record for this paper; it supersedes the shorter trajectory $8\to7\to4$ reported in the prior version [9], whose first step incorrectly removed all three single-black-hat worlds at once rather than only the world distinguishable by the announcing agent.

As a contrast case for the dynamic-epistemic stage: if the king's public announcement were modelled by an action model with three events ($|E|=3$) instead of by a semantic restriction, the product model would have

$$
|W_{0}|\times|E| = 8\times3 = 24
$$

worlds before any restriction, illustrating that product update can expand the model even as the informational content of the announcement shrinks the set of reachable states. The numbers above follow directly from the combinatorial counting described in Section 4.3 and are consistent with the philosophical motivation for introducing dynamic epistemic logic given in [4], which argues that modal logic should be taught from its philosophical motivations rather than from its mathematics alone.

### 6.2 Variable-inclusion truth-table example

Variable-inclusion logics assign a distinct set of propositional variables $\mathrm{Var}(\varphi)$ to each formula $\varphi$, in the sense of the set of variables really occurring in $\varphi$ defined in [6]. The truth-table size for $\varphi$ is

$$
2^{|\mathrm{Var}(\varphi)|}.
$$

Consider a formula $\varphi$ that mentions exactly five distinct variables, e.g.

$$
\varphi \;=\; (p_{1}\land p_{2})\;\lor\;(p_{3}\rightarrow(p_{4}\leftrightarrow p_{5})).
$$

Here $|\mathrm{Var}(\varphi)|=5$, so the truth-table contains

$$
2^{5}=32
$$

rows. If a student attempts to enumerate the table by hand, the workload already exceeds the comfortable manual limit identified in Section 4.1 (the liars-and-truth-tellers puzzle becomes unwieldy at $n=10$, where $2^{10}=1\,024$ rows). This concrete example demonstrates the quantitative checkpoint that justifies the transition from propositional to variable-inclusion logics, in the setting of the left variable-inclusion companion $\vdash^{l}$ defined in [6] and within the broader outlook on logic education in [3].

### 6.3 Computability-logic game-tree calculation

Computability logic interprets logical operators as operations on interactive games, with truth as existence of an algorithmic winning strategy [7]. A game tree with uniform branching factor $b$ and depth $d$—the depth of a game being, as in [7], the smallest integer bounding the number of moves in a legal run—is assumed here to have

$$
b^{d}
$$

nodes. Take the canonical branching factor $b=2$ (binary choices) and depth $d=4$ (four rounds of interaction). The node count is

$$
2^{4}=16 .
$$

If the branching increases to $b=3$ while $d=4$, the tree size becomes

$$
3^{4}=81 .
$$

These numbers are obtained by elementary exponent