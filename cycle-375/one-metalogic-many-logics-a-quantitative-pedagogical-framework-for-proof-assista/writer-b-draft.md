# Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum

## Abstract

Mixed cohorts of computer‑science, mathematics, and philosophy students face fragmented curricula that either overload or under‑serve particular backgrounds, raising instructional cost and reducing learning coherence. Existing work on the LogiKEy methodology supplies a unified metalogic but lacks explicit quantitative checkpoints that justify transitions between object logics. This paper combines semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each curricular stage. The analysis derives (1) the propositional assignment space $2^{3}=8$ and its single survivor for the liars‑and‑truth‑tellers puzzle; (2) the numbers of arbitrary ($2^{64}\approx1.84\times10^{19}$) and reflexive ($2^{56}\approx7.21\times10^{16}$) accessibility relations for the modal re‑modeling; (3) the Wise Men / muddy‑children model trajectory $8\to7\to6\to4$ with shrinkage factor $7/4=1.75$ from the first announcement onward, and its generalisation to $2^{8}=256$ agents; (4) the proof‑length tower $L_{5}\approx10^{19\,728}$ for Boolos’s curious inference; (5) the deontic fulfillment profile count $2^{m}$ with $m=2$; (6) the Gödel ontological argument’s raw and consistent positivity‑predicate interpretations $2^{5}=32$ and $2^{2}=4$; (7) a course‑time allocation projected from a 28‑hour semester and a $2{:}3{:}3{:}4{:}4{:}4$ weight ratio; (8) the contrast factor $2^{61}\approx2.31\times10^{18}$ between propositional and modal stages; and (9) the transfer of the same exponential scaffolding to variable‑inclusion and computability logics. These checkpoints turn pedagogical intuition into concrete numerical milestones, informing curriculum design, automation adoption, and resource planning for pluralistic logic teaching.

## 1. Introduction

Logic courses that simultaneously serve computer‑science, mathematics, and philosophy students encounter a concrete problem: each discipline arrives with distinct expectations about the role of logic, the nature of proof, and the desired applications, yet curricula are typically organised around a single object logic. The resulting fragmentation forces students to master multiple notations and toolchains, while monotonic courses that remain in classical first‑order logic leave philosophy students without the modal and deontic resources they need and computer‑science students without the modelling primitives required for verification tasks. The cost of this mismatch appears as additional contact hours, duplicated teaching materials, and lower learning outcomes, and the capability that would resolve it is a unified, quantitative framework that tells instructors precisely when a richer object logic becomes necessary.

The LogiKEy methodology supplies the unifying metalogic—classical higher‑order logic (HOL)—and demonstrates how object logics can be embedded semantically in a single proof assistant. What remains missing is a set of explicit numerical thresholds that justify each pedagogical transition. This paper fills that gap by deriving, from first principles, the combinatorial quantities that grow (or shrink) at each stage of the LogiKEy example sequence and by mapping those quantities to curriculum‑design decisions. Every number is either computed here by shown arithmetic or explicitly labelled a projection with stated assumptions; no empirical classroom data is reported.

**Contributions.**  
* **C1.** Exact derivation of the propositional assignment space and survivor count for the liars‑and‑truth‑tellers puzzle (Section 4.1, Result R1).  
* **C2.** Enumeration of arbitrary and reflexive accessibility relations for the modal re‑modeling (Section 4.2, Result R2).  
* **C3.** Quantitative analysis of the Wise Men / muddy‑children state‑space collapse $8\to7\to6\to4$ and its generalisation (Section 4.3, Result R3).  
* **C4.** Construction of the proof‑length tower for Boolos’s curious inference (Section 4.4, Result R4).  
* **C5.** Counting of deontic fulfillment profiles for Chisholm’s paradox (Section 4.5, Result R5).  
* **C6.** Calculation of raw and consistent positivity‑predicate interpretations for Gödel’s ontological argument (Section 4.6, Result R6).  
* **C7.** Projection of contact‑hour allocation for a six‑stage semester course (Section 4.7, Result R7).  
* **C8.** Derivation of the contrast factor between propositional and modal stages (Section 4.8, Result R8).  
* **C9.** Extension of the exponential scaffolding to variable‑inclusion and computability logics (Section 4.9, Result R9).

## 2. Background and Related Work

The LogiKEy methodology is introduced in [1] and further elaborated in [2]; both works describe how classical HOL serves as a universal metalogic and report more than a decade of experience embedding propositional, modal, epistemic, and deontic logics in Isabelle/HOL. The pedagogical case for proof‑assistant‑based logic teaching is made in [1] through a graded sequence of examples in which a liars‑and‑truth‑tellers puzzle leads from propositional to modal logic and the Wise Men puzzle leads on to dynamic epistemic logic, with Boolos’s curious inference illustrating further limits.

Work [7] presents computability logic as an applied theory where logical operators correspond to game operations and truth is the existence of an algorithmic winning strategy, linking logic to interactive computation. Work [8] introduces a neutral temporal deontic STIT framework that models agents’ choices between performing or omitting actions, yielding $2^{n}$ joint action profiles for $n$ agents. Together these specific results complement the foundational discussions in [1] and [2] by supplying concrete methods, quantitative measures, and application contexts. Work [3] surveys prospects for mathematical logic in the twenty‑first century and highlights the importance of quantitative awareness when scaling logical formalisms. Work [4] argues for teaching modal logic through philosophically motivated case studies, providing a qualitative motivation that we translate into quantitative checkpoints. Work [5] discusses challenges of teaching logic to information‑systems students, underscoring the need for curriculum‑wide quantitative guidance. Work [6] defines left variable‑inclusion logics and shows that truth‑table size is $2^{|V(\varphi)|}$, directly supporting our variable‑inclusion checkpoint.

## 3. Methods

### 3.1 Semantical embeddings in HOL

The metalogic is classical higher‑order logic (HOL) with a distinguished type $w$ for possible worlds. An object modal operator $\Box_{r}$ is defined by  

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$  

where $r:w\to w\to\mathbb{B}$ is a binary relation and $\varphi:w\to\mathbb{B}$ is a world‑valued predicate. Epistemic operators $K_{a}$ for agents $a\in A$ are instantiated as $\Box_{r_{a}}$. Dynamic epistemic logic introduces an event model $E$ with events $e\in E$; the product model $M\otimes E$ has worlds $(w,e)$, yielding size $|W|\cdot|E|$.

### 3.2 Combinatorial analysis

For each curricular stage the relevant combinatorial quantity is identified:

| Stage | Quantity | Definition |
|-------|----------|------------|
| Propositional | Truth‑table rows | $2^{n}$ for $n$ propositional variables |
| Modal | Accessibility relations | $2^{|W|^{2}}$ arbitrary; $2^{|W|^{2}-|W|}$ reflexive |
| Epistemic / Public announcement | Model‑state count | $2^{m}$ initial states, reduced by announcements |
| Dynamic epistemic | Product‑model size | $|W|\cdot|E|$ |
| Deontic | Fulfilment profiles | $2^{m}$ for $m$ obligations |
| Gödel | Positivity‑predicate interpretations | $2^{p}$ raw; $2^{p-a}$ consistent if $a$ independent axioms |
| Variable‑inclusion | Formula‑specific rows | $2^{|\mathrm{Var}(\varphi)|}$ |
| Computability | Game‑tree nodes | $b^{d}$ for branching factor $b$ and depth $d$ |

All numbers are computed by elementary arithmetic with every step shown in Section 4; where a projection is required, the underlying assumptions are stated explicitly. No experiment, survey, or classroom measurement is reported in this paper; the single classroom‑facing proposal appears in Section 7 as a design for a future study.

## 4. Analysis

### 4.1 Stage 1 – Propositional assignment space (liars‑and‑truth‑tellers)

**Input.** Three islanders $a,b,c$, each either a truth‑teller ($T$) or a liar ($L$). Statements:  
1. $a$: “$b$ is a truth‑teller”.  
2. $b$: “$a$ and $c$ are of different types”.  
3. $c$: “$a$ is a liar”.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The constraints become  

$$
\begin{aligned}
x_{a}&=(x_{b}=T),\\
x_{b}&=(x_{a}\neq x_{c}),\\
x_{c}&=(x_{a}=L).
\end{aligned}
$$

**Enumeration.** The raw space contains $2^{3}=8$ assignments. Evaluating each assignment against the three equations yields exactly one survivor: $(x_{a},x_{b},x_{c})=(T,T,L)$.  

**Elimination rate.**  

$$
\frac{8-1}{8}= \frac{7}{8}=0.875.
$$

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space is $2^{10}=1\,024$ assignments.

### 4.2 Stage 2 – Modal upgrade (accessibility relations)

**Input.** The propositional stage yields $|W|=8$ worlds (one per assignment).  

**Arbitrary relations.** The number of binary relations on $W$ is  

$$
2^{|W|\times|W|}=2^{8\times8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
$$

**Reflexive relations.** Reflexivity fixes the $8$ diagonal pairs, leaving $8\times7=56$ off‑diagonal pairs. Hence  

$$
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}.
$$

### 4.3 Stage 3 – Public‑announcement collapse (Wise Men / muddy‑children)

**Three‑agent case.** Initial state set $W_{0}$ has $2^{3}=8$ worlds, one per assignment of hat colours (black $B$ or white $W$) to the three agents.

*Announcement “at least one hat is black”.* This eliminates the all‑white world $WWW$, leaving  

$$
|W_{1}|=8-1=7.
$$

*First “I don’t know” announcement.* Under the sequential convention, the first agent would know its own hat only in the world where it sees two white hats, i.e. the world $WWB$. Since that world is the only one in which the first agent could have known, the public announcement of ignorance eliminates exactly this one world. Hence  

$$
|W_{2}|=7-1=6.
$$

*Second “I don’t know” announcement.* After the first agent’s ignorance is public, the second agent can rule out worlds consistent with that ignorance. The second agent now eliminates the two worlds in which it would see a single black hat and could therefore deduce its own colour. Thus  

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

**Dynamic‑epistemic comparison.** In public‑announcement logic the update is a world restriction, so the model shrinks as computed above. If instead the announcement were modelled by an action (event) model with $|E|=3$ events, the product model would have  

$$
|W_{0}|\times|E|=8\times3=24
$$

worlds, illustrating that DEL product updates can expand the model even when the informational content of the announcement shrinks the set of possible worlds. The two counts answer different questions—how many worlds remain possible, versus how large the product structure is—and both are pedagogically useful.

**Eight‑agent generalisation.** For $m=8$ agents the initial space is $2^{8}=256$ worlds. The public announcement removes the all‑white world, giving $255$ worlds. Each subsequent “I don’t know’’ round removes all worlds with exactly $k$ black hats for $k=1,2,\dots$ until the remaining set is small enough for an agent to deduce its own hat. The quantitative pattern mirrors the $8\to7\to6\to4$ collapse: an initial single‑world removal followed by progressively larger removals, demonstrating exponential reduction driven by public announcements.

### 4.4 Stage 4 – Boolos’s curious inference (proof‑length tower)

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
\log_{10}\bigl(2^{65\,536}\bigr)=65\,536\times0.30103\approx19\,728.3,
$$

so  

$$
L_{5}\approx10^{19\,728}
$$ 

(projection based on the assumed value $\log_{10}(2)=0.30103$).

**First‑order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is  

$$
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}.
$$

A propositional instantiation with $k=10$ atoms yields $2^{10}=1\,024$ rows, illustrating the dramatic gap between first‑order and higher‑order settings.

### 4.5 Stage 5 – Deontic combinatorics (Chisholm’s paradox)

**Input.** $m=2$ obligations. Each obligation may be fulfilled (F) or violated (V).  

**Profiles.**  

$$
2^{m}=2^{2}=4\ \text{profiles}.
$$

A three‑obligation variant would have $2^{3}=8$ profiles. The paradox is a consistency issue rather than a size issue; the dyadic deontic operator $O(B\mid A)$ reorganises the same four profiles into conditional commitments, restoring consistency.

### 4.6 Stage 6 – Gödel’s ontological argument

**Input.** Universe of $p=5$ candidate properties for the positivity predicate $P$; $a=3$ independent axioms.  

**Raw space.**  

$$
2^{p}=2^{5}=32.
$$

**Consistent space (assuming each axiom halves the space).**  

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

Thus the argument reduces to a searchable space of at most four consistent interpretations.

### 4.7 Stage 7 – Course‑time projection (projection)

**Assumptions.** Semester length $T_{\text{sem}}=14$ weeks, one $2$‑hour session per week $\Rightarrow$ total contact time $28$ h.  

**Weight ratio.** Stages receive weights $2{:}3{:}3{:}4{:}4{:}4$, total weight $20$.  

**Unit hour.**  

$$
\frac{28\ \text{h}}{20}=1.4\ \text{h per weight unit}.
$$

**Stage allocations.**  

$$
\begin{aligned}
\text{Stage 1}&:2\times1.4=2.8\ \text{h},\\
\text{Stage 2}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 3}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 4}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 5}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 6}&:4\times1.4=5.6\ \text{h}.
\end{aligned}
$$

Sum check: $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ h.

### 4.8 Stage 8 – Contrast factor between propositional and modal stages

$$
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18}.
$$

The modal upgrade therefore expands the search space by roughly $2.3\times10^{18}$‑fold.

### 4.9 Stage 9 – Extensions to variable‑inclusion and computability logics

**Variable‑inclusion.** For a formula $\varphi$ with variable set $\mathrm{Var}(\varphi)$, the truth‑table size is $2^{|\mathrm{Var}(\varphi)|}$, directly inheriting the $2^{n}$ scaffold. When $|\mathrm{Var}(\varphi)|$ exceeds the hand‑enumeration threshold (between $3$ and $8$), automation becomes necessary.

**Computability logic.** A game with branching factor $b$ and depth $d$ has $b^{d}$ nodes. Setting $b=2$ and $d=n$ reproduces the $2^{n}$ pattern. Thus the same exponential checkpoint signals when a game tree becomes too large for manual exploration.

## 5. Results

All quantitative statements below follow directly from the derivations in Section 4; the single projection (R7) is explicitly labelled.

- **R1.** Propositional space for $n=3$ islanders: $2^{3}=8$ assignments, $1$ survivor; for $n=10$: $2^{10}=1\,024$ assignments (Section 4.1).  
- **R2.** Modal accessibility relations: $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary; $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive (Section 4.2).  
- **R3.** Wise Men / muddy‑children collapse: $8\to7\to6\to4$ (shrinkage factor $7/4=1.75$ from the first announcement onward); eight‑agent analogue starts at $2^{8}=256$ worlds and collapses analogously (Section 4.3).  
- **R4.** Boolos proof‑length tower: $L_{5}\approx10^{19\,728}$; first‑order interpretation space $2^{100}\approx1.27\times10^{30}$ (Section 4.4).  
- **R5.** Deontic fulfillment profiles: $2^{2}=4$ for $m=2$ obligations; $2^{3}=8$ for three obligations (Section 4.5).  
- **R6.** Gödel positivity‑predicate space: $2^{5}=32$ raw, at most $2^{2}=4$ consistent under the independence assumption (Section 4.6).  
- **R7 (projection).** Contact‑hour allocation: Stage 1 $2.8$ h, Stage 2 $4.2$ h, Stage 3 $4.2$ h, Stage 4 $5.6$ h, Stage 5 $5.6$ h, Stage 6 $5.6$ h (Section 4.7).  
- **R8.** Contrast factor propositional vs. modal: $2^{61}\approx2.31\times10^{18}$ (Section 4.8).  
- **R9.** Variable‑inclusion and computability scaffolding: truth‑table size $2^{|\mathrm{Var}(\varphi)|}$ and game‑tree size $b^{d}$, respectively, both exhibiting the same exponential growth pattern (Section 4.9).

## 6. Discussion

### 6.1 Re‑examining the Wise Men trajectory with S5 semantics

The three‑agent Wise Men puzzle is modelled in an S5 epistemic setting, i.e. each agent’s accessibility relation is an equivalence relation.  The initial world set is  

$$
|W_{0}| = 2^{3}=8 .
$$

The king’s public announcement “at least one hat is black’’ eliminates the all‑white world, giving  

$$
|W_{1}| = 8-1 = 7 .
$$

The first “I don’t know’’ announcement is made by agent $a$.  In S5, $a$ knows its own hat exactly when it sees two white hats; there is only one world, $WWW$, in which this would happen, but $WWW$ has already been removed.  Consequently the first ignorance announcement eliminates **only the world in which $a$ would have known**, namely the world $WWB$ (where $a$ sees two white hats).  Hence  

$$
|W_{2}| = 7-1 = 6 .
$$

The second “I don’t know’’ announcement is made by agent $b$.  After $a$’s ignorance is public, $b$ can rule out the two worlds $BBW$ and $BWB$, because in each of them $b$ would see a single black hat and could therefore deduce its own colour.  Thus  

$$
|W_{3}| = 6-2 = 4 .
$$

The shrinkage factor from the first public announcement onward is  

$$
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75 .
$$

This derivation matches the sequential‑announcement convention adopted throughout the paper and is the basis for the quantitative checkpoint that signals the introduction of dynamic epistemic logic.  

### 6.2 Variable‑inclusion truth‑table size from algebraic semantics  

Variable‑inclusion logics associate each formula $\varphi$ with its own finite set of propositional variables $V(\varphi)$.  For any such logic the truth‑table of $\varphi$ ranges over all assignments to the variables in $V(\varphi)$, so its size is $2^{|V(\varphi)|}$.  

*Example 1.*  Let  

$$
\varphi \;=\; (p_{1}\land p_{2})\;\lor\;(p_{3}\rightarrow(p_{4}\leftrightarrow p_{5})).
$$

Here $|V(\varphi)|=5$, so the truth‑table contains  

$$
2^{5}=32
$$

rows. Because $32>8$, the hand‑enumeration threshold identified in Section 4.1 (the liars‑and‑truth‑tellers benchmark of $8$ rows) is exceeded, indicating that automation should be introduced at this stage.

### 6.3 Computability‑logic game‑tree enumeration  

Computability logic (CL) interprets logical formulas as interactive games.  According to [7], “logical operators stand for operations on games and ‘truth’ is understood as existence of an algorithmic winning strategy”.  A game tree with uniform branching factor $b$ and depth $d$ therefore has  

$$
b^{d}
$$

nodes.  This mirrors the $2^{n}$ pattern that recurs throughout the curriculum.

*Example.*  Take a binary‑branching game ($b=2$) of depth $d=4$.  The node count is  

$$
2^{4}=16 .
$$

If we increase the depth to $d=6$, the count becomes  

$$
2^{6}=64 .
$$

Because $64$ exceeds the manual‑enumeration limit identified in Section 4.1, the instructor can use this quantitative signal to justify moving from a purely propositional treatment of CL to a HOL‑encoded embedding, where Isabelle/HOL can automatically explore the game tree.

### 6.4 Deontic STIT combinatorics and the $2^{n}$ scaffold  

The neutral temporal deontic STIT logic introduced in [8] defines a set of agents $Ag=\{1,\dots ,n\}$, each of which chooses between two primitive actions (perform or omit).  The number of joint action profiles is therefore  

$$
2^{n}.
$$

For the three‑agent case used in the Wise Men example ($n=3$) we obtain  

$$
2^{3}=8
$$

possible STIT worlds, which coincides with the eight worlds of the propositional stage.  This alignment demonstrates that the same exponential bound governs both epistemic and deontic modelling choices, reinforcing the quantitative unity of the LogiKEy sequence.

### 6.5 Quantitative justification for a mixed‑cohort curriculum  

By supplying the concrete numbers derived above—world‑set sizes, truth‑table rows, game‑tree nodes, and accessibility‑relation counts—we fill the gap identified in the introduction.  Each checkpoint is tied to a pedagogical decision point:

| Checkpoint | Quantitative trigger | Curriculum action |
|------------|----------------------|-------------------|
| Switch to automation for propositional logic | $2^{n}>8$ (e.g. $n\ge5$) | Introduce Isabelle/HOL embeddings |
| Introduce dynamic epistemic logic | Model size contracts $8\to7\to4$ with shrinkage factor $1.75$ | Present public‑announcement updates |
| Add variable‑inclusion logic | $|V(\varphi)|\ge5$ → $2^{|V|}\ge32$ | Embed left‑variable‑inclusion semantics |
| Teach computability logic | Game‑tree size $b^{d}\ge64$ | Model games in HOL and explore strategies |
| Deploy deontic STIT reasoning | Agent count $n\ge3$ → $2^{n}\ge8$ | Use STIT operators for normative scenarios |

These worked examples illustrate how the abstract combinatorial scaffolding introduced in Sections 4–5 can be operationalised in the classroom, providing instructors with clear, numerically grounded criteria for each pedagogical transition.

### 6.6 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Fixed three‑islander puzzle structure | Scaling to different statements changes survivor count exponentially. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only for accessibility relations | Adding symmetry or transitivity would further reduce the count; current numbers are upper bounds for the given constraint. |
| S5 epistemic assumption (equivalence relations) | Weakening to KD45 would alter the admissible relation count. |
| Sequential “I don’t know’’ announcement dynamics in Section 4.3 | A simultaneous all‑agents announcement model would yield $8\to7\to4$; the paper adopts the sequential convention confirmed by a second model. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Represents worst‑case proof‑search; alternative strategies could yield smaller lengths. |
| Independence of Gödel’s three axioms | If axioms are dependent, the consistent space could be larger than $2^{2}=4$. |
| Course‑time ratio $2{:}3{:}3{:}4{:}4{:}4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of thresholds | The hand‑enumeration thresholds are theoretical; actual student limits may differ. |

### 6.7 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students successfully enumerate all $2^{64}\approx10^{19}$ accessibility relations for the modal stage without assistance from a model finder. Such performance would demonstrate that the combinatorial count vastly over‑estimates the effective search burden, thereby falsifying the claim that the modal upgrade is forced by state‑space size.

Similarly, if a concrete implementation of the Wise Men / muddy‑children puzzle with three agents, run under the sequential announcement convention, does not reduce the model from $8$ through $7$ and $6$ to $4$ states after the announced “I don’t know’’ steps, the derived shrinkage factor $1.75$ would be contradicted, falsifying the quantitative justification for introducing public‑announcement logic. A model in which all agents announce simultaneously and the trajectory is $8\to7\to4$ would not falsify the arithmetic but would show that the sequential convention, not the arithmetic, carries the intermediate count $6$; the paper adopts the sequential convention, so any deviation under that convention would refute Result R3.

### 6.8 Open questions

* How do alternative embedding strategies (deep vs. shallow) affect the combinatorial counts?  
* What is the impact of richer event models (larger $|E|$) on the trade‑off between model growth and expressive power?  
* Can automated proof‑search heuristics mitigate the exponential blow‑up identified for Boolos’s inference, and how would that alter the pedagogical argument?  
* How robust are the course‑time projections across institutions with differing teaching loads and student backgrounds?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

The primary users are instructors of logic courses that serve mixed cohorts of computer‑science, mathematics, and philosophy students. The quantitative checkpoints inform three concrete design decisions:

1. **Pacing of automation.** The instructor introduces the proof assistant when the truth‑table row count exceeds the hand‑enumeration threshold (between $n=3$ and $n=8$), ensuring that automation is presented exactly when it becomes necessary.  
2. **Sequencing of object logics.** The public‑announcement collapse $8\to7\to6\to4$ signals the point at which dynamic epistemic logic should be introduced; the product‑model size $|W|\cdot|E|$ signals the subsequent move to full dynamic epistemic frameworks.  
3. **Allocation of contact hours.** The derived hour distribution ($2.8$ h, $4.2$ h, $4.2$ h, $5.6$ h, $5.6$ h, $5.6$ h) guides syllabus planning, ensuring that each stage receives time proportional to its combinatorial complexity.

### 7.2 Technology readiness level

The contribution is purely analytical and has not undergone peer review; according to NASA definitions it resides at TRL 2 (technology concept formulated). No software artefact