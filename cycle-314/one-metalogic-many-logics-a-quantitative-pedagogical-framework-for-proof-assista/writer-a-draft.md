# Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum

## Abstract

Mixed cohorts of computer‑science, mathematics, and philosophy students face fragmented curricula that either overload or under‑serve particular backgrounds, leading to increased instructional cost and reduced learning coherence. Existing work on the LogiKEy methodology provides a unified metalogic but lacks explicit quantitative checkpoints that justify transitions between object logics. This paper combines semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each curricular stage. The analysis derives (1) the propositional assignment space $2^{3}=8$ and its single survivor for the liars‑and‑truth‑tellers puzzle; (2) the number of arbitrary ($2^{64}\approx1.84\times10^{19}$) and reflexive ($2^{56}\approx7.21\times10^{16}$) accessibility relations for the modal re‑modeling; (3) the Wise Men / muddy‑children model trajectory $8\to7\to6\to4$ and its generalisation to $2^{8}=256$ agents; (4) the proof‑length tower $L_{5}\approx10^{19\,728}$ for Boolos’s curious inference; (5) the deontic fulfillment profile count $2^{m}$ with $m=2$; (6) the Gödel ontological argument’s raw and consistent positivity‑predicate interpretations $2^{5}=32$ and $2^{2}=4$; (7) the course‑time allocation derived from a $28$‑hour semester and a $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$ weight ratio; (8) the contrast factor $2^{61}\approx2.31\times10^{18}$ between propositional and modal stages; and (9) the transfer of the same exponential scaffolding to variable‑inclusion and computability logics. These checkpoints turn pedagogical intuition into concrete numerical milestones, informing curriculum design, automation adoption, and resource planning for pluralistic logic teaching.

## 1. Introduction

Logic courses that simultaneously serve computer‑science, mathematics, and philosophy students encounter a concrete problem: each discipline arrives with distinct expectations about the role of logic, the nature of proof, and the desired applications, yet curricula are typically organised around a single object logic. The resulting fragmentation forces students to master multiple notations and toolchains, while monotonic courses that remain in classical first‑order logic leave philosophy students without the modal and deontic resources they need and computer‑science students without the modelling primitives required for verification tasks. The cost of this mismatch appears as additional contact hours, duplicated teaching materials, and lower learning outcomes, and the capability that would resolve it is a unified, quantitative framework that tells instructors precisely when a richer object logic becomes necessary.

The LogiKEy methodology supplies the unifying metalogic—classical higher‑order logic (HOL)—and demonstrates how object logics can be embedded semantically in a single proof assistant. What remains missing is a set of explicit numerical thresholds that justify each pedagogical transition. This paper fills that gap by deriving, from first principles, the combinatorial quantities that grow (or shrink) at each stage of the LogiKEy example sequence and by mapping those quantities to curriculum‑design decisions.

**Contributions.**  
* **C1.** Exact derivation of the propositional assignment space and survivor count for the liars‑and‑truth‑tellers puzzle (Section 4.1, Result R1).  
* **C2.** Enumeration of arbitrary and reflexive accessibility relations for the modal re‑modeling (Section 4.2, Result R2).  
* **C3.** Quantitative analysis of the Wise Men / muddy‑children state‑space collapse and its generalisation (Section 4.3, Result R3).  
* **C4.** Construction of the proof‑length tower for Boolos’s curious inference (Section 4.4, Result R4).  
* **C5.** Counting of deontic fulfillment profiles for Chisholm’s paradox (Section 4.5, Result R5).  
* **C6.** Calculation of raw and consistent positivity‑predicate interpretations for Gödel’s ontological argument (Section 4.6, Result R6).  
* **C7.** Projection of contact‑hour allocation for a six‑stage semester course (Section 4.7, Result R7).  
* **C8.** Derivation of the contrast factor between propositional and modal stages (Section 4.8, Result R8).  
* **C9.** Extension of the exponential scaffolding to variable‑inclusion and computability logics (Section 4.9, Result R9).

## 2. Background and Related Work

The LogiKEy methodology is introduced in [1] and further elaborated in [2]; both works describe how classical HOL serves as a universal metalogic and report more than a decade of experience embedding propositional, modal, epistemic, and deontic logics in Isabelle/HOL. The pedagogical case for proof‑assistant‑based logic teaching is made in [1] through a graded sequence of examples ranging from the liars‑and‑truth‑tellers puzzle to Gödel’s ontological argument.

[3] argues that logic applications to computer science are a central driver of modern curricula, underscoring the relevance of integrating automated reasoning tools for CS students.  

[4] emphasizes that modal logic teaching should be motivated by philosophical problems, providing a philosophical justification for introducing epistemic operators in the curriculum.  

[5] notes that teaching logic to information‑systems students requires adapting content to practical needs, supporting the broader claim that curricula must be tailored to heterogeneous audiences.  

Variable‑inclusion logics are developed, where each formula carries its own finite set of propositional variables and the semantics is defined relative to that set. The algebraic treatment in [6] shows that the truth‑table size for a formula $\varphi$ is $2^{|V(\varphi)|}$, a direct generalisation of the classical $2^{n}$ count used in this paper.  

Computability logic reinterprets logical operators as operations on interactive computational problems (games). In this paper we assume that the size of a game tree with branching factor $b$ and depth $d$ is $b^{d}$, mirroring the exponential growth $2^{n}$ of propositional truth tables; this modelling choice follows directly from the definition of game‑tree size in [7].  

A neutral temporal deontic STIT logic provides relational frames that avoid committing to specific utility functions while supporting deontic reasoning; the construction of such frames is described in [8] and underpins our treatment of deontic combinatorics.  

Finally, a prior short version of the present work appears as [9].

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
| Variable‑inclusion | Formula‑specific rows | $2^{|V(\varphi)|}$ |
| Computability | Game‑tree nodes | $b^{d}$ for branching factor $b$ and depth $d$ |

All numbers are computed by elementary arithmetic; where a projection is required, the underlying assumptions are stated explicitly.

## 4. Analysis

### 4.1 Stage 1 – Propositional assignment space (liars‑and‑truth‑tellers)

**Input.** Three islanders $a,b,c$, each either a truth‑teller ($T$) or a liar ($L$). Statements:  
1. $a$: “$b$ is a truth‑teller”.  
2. $b$: “$a$ and $c$ are of different types”.  
3. $c$: “$a$ is a liar”.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The constraints become  

\[
\begin{aligned}
x_{a}&=(x_{b}=T),\\
x_{b}&=(x_{a}\neq x_{c}),\\
x_{c}&=(x_{a}=L).
\end{aligned}
\]

**Enumeration.** The raw space contains $2^{3}=8$ assignments. Evaluating each assignment against the three equations yields exactly one survivor: $(x_{a},x_{b},x_{c})=(T,T,L)$.  

**Elimination rate.**  

\[
\frac{8-1}{8}= \frac{7}{8}=0.875.
\]

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space is $2^{10}=1\,024$ rows.

### 4.2 Stage 2 – Modal upgrade (accessibility relations)

**Input.** The propositional stage yields $|W|=8$ worlds (one per assignment).  

**Arbitrary relations.** The number of binary relations on $W$ is  

\[
2^{|W|\times|W|}=2^{8\times8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
\]

**Reflexive relations.** Reflexivity fixes the $8$ diagonal pairs, leaving $8\times7=56$ off‑diagonal pairs. Hence  

\[
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}.
\]

### 4.3 Stage 3 – Public‑announcement collapse (Wise Men / muddy‑children)

**Three‑agent case.** Initial state set $W_{0}$ has $2^{3}=8$ worlds.  

*Announcement “at least one hat is black’’* eliminates the all‑white world, leaving  

\[
|W_{1}| = 8-1 = 7 .
\]

*First “I don’t know’’ announcement* eliminates the single world in which the announcing agent would see two white hats and could therefore infer its own hat colour, giving  

\[
|W_{2}| = 7-1 = 6 .
\]

*Second “I don’t know’’ announcement* eliminates the two worlds in which the second announcing agent would be able to infer its own hat colour, yielding  

\[
|W_{3}| = 6-2 = 4 .
\]

Thus the trajectory is  

\[
8\;\to\;7\;\to\;6\;\to\;4,
\]

with shrinkage factor from the first to the final step  

\[
\frac{7}{4}=1.75 .
\]

**Eight‑agent generalisation.** For $m=8$ agents the initial space is $2^{8}=256$ worlds. The public announcement removes the all‑white world, giving $255$ worlds. Subsequent “I don’t know’’ rounds remove worlds with exactly $k$ black hats for $k=1,2,\dots$ until the remaining set is small enough for an agent to deduce its own hat. The quantitative pattern mirrors the $8\to7\to6\to4$ collapse, demonstrating exponential reduction driven by public announcements.

**Product‑model size note.** If the public announcement were modelled by an action model with three events ($|E|=3$) instead of a single trivial event, the product model would have  

\[
|W_{0}|\times|E| = 8\times3 = 24
\]

worlds, illustrating that DEL can both shrink and expand the model size.

### 4.4 Stage 4 – Boolos’s curious inference (proof‑length tower)

**Recurrence.**  

\[
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
\]

**Iteration.**  

\[
\begin{aligned}
L_{1}&=2^{1}=2,\\
L_{2}&=2^{2}=4,\\
L_{3}&=2^{4}=16,\\
L_{4}&=2^{16}=65\,536,\\
L_{5}&=2^{65\,536}.
\end{aligned}
\]

**Decimal approximation for $L_{5}$.** Using $\log_{10}(2)=0.30103$,

\[
\log_{10}\bigl(2^{65\,536}\bigr)=65\,536\times0.30103\approx19\,728.3,
\]

so  

\[
L_{5}\approx10^{19\,728}.
\]

**First‑order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is  

\[
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}.
\]

A propositional instantiation with $k=10$ atoms yields $2^{10}=1\,024$ rows, illustrating the dramatic gap between first‑order and higher‑order settings.

### 4.5 Stage 5 – Deontic combinatorics (Chisholm’s paradox)

**Input.** $m=2$ obligations. Each obligation may be fulfilled (F) or violated (V).  

**Profiles.**  

\[
2^{m}=2^{2}=4\ \text{profiles}.
\]

A three‑obligation variant would have $2^{3}=8$ profiles. The paradox is a consistency issue rather than a size issue; the dyadic deontic operator $O(B\mid A)$ reorganises the same four profiles into conditional commitments, restoring consistency.

### 4.6 Stage 6 – Gödel’s ontological argument

**Input.** Universe of $p=5$ candidate properties for the positivity predicate $P$; $a=3$ independent axioms.  

**Raw space.**  

\[
2^{p}=2^{5}=32.
\]

**Consistent space (assuming each axiom halves the space).**  

\[
2^{p-a}=2^{5-3}=2^{2}=4.
\]

Thus the argument reduces to a searchable space of at most four consistent interpretations.

### 4.7 Stage 7 – Course‑time projection (projection)

**Assumptions.** Semester length $T_{\text{sem}}=14$ weeks, one $2$‑hour session per week $\Rightarrow$ total contact time $28$ h.  

**Weight ratio.** Stages receive weights $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$, total weight $20$.  

**Unit hour.**  

\[
\frac{28\ \text{h}}{20}=1.4\ \text{h per weight unit}.
\]

**Stage allocations.**  

\[
\begin{aligned}
\text{Stage 1}&:2\times1.4=2.8\ \text{h},\\
\text{Stage 2}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 3}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 4}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 5}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 6}&:4\times1.4=5.6\ \text{h}.
\end{aligned}
\]

Sum check: $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ h.

### 4.8 Stage 8 – Contrast factor between propositional and modal stages

\[
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18}.
\]

The modal upgrade therefore expands the search space by roughly $2.3\times10^{18}$‑fold.

### 4.9 Stage 9 – Extensions to variable‑inclusion and computability logics

**Variable‑inclusion.** For a formula $\varphi$ with variable set $V(\varphi)$, the truth‑table size is $2^{|V(\varphi)|}$, directly inheriting the $2^{n}$ scaffold. When $|V(\varphi)|$ exceeds the hand‑enumeration threshold (between $3$ and $8$), automation becomes necessary.

**Computability logic.** A game with branching factor $b$ and depth $d$ has $b^{d}$ nodes. Setting $b=2$ and $d=n$ reproduces the $2^{n}$ pattern. Thus the same exponential checkpoint signals when a game‑tree becomes too large for manual exploration.

## 5. Results

All quantitative statements below follow directly from the derivations in Section 4; the single projection (R7) is explicitly labelled.

* **R1.** Propositional space for $n=3$ islanders: $2^{3}=8$ assignments, $1$ survivor; for $n=10$: $2^{10}=1\,024$ assignments (Section 4.1).  
* **R2.** Modal accessibility relations: $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary; $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive (Section 4.2).  
* **R3.** Wise Men / muddy‑children collapse: $8\to7\to6\to4$ (shrinkage factor $1.75$); eight‑agent analogue collapses from $256$ toward a small residual set (Section 4.3).  
* **R4.** Boolos proof‑length tower: $L_{5}\approx10^{19\,728}$; first‑order interpretation space $2^{100}\approx1.27\times10^{30}$ (Section 4.4).  
* **R5.** Deontic fulfillment profiles: $2^{2}=4$ for $m=2$ obligations; $2^{3}=8$ for three obligations (Section 4.5).  
* **R6.** Gödel positivity‑predicate space: $2^{5}=32$ raw, at least $2^{2}=4$ consistent (Section 4.6).  
* **R7 (projection).** Contact‑hour allocation: Stage 1 $2.8$ h, Stage 2 $4.2$ h, Stage 3 $4.2$ h, Stage 4 $5.6$ h, Stage 5 $5.6$ h, Stage 6 $5.6$ h (Section 4.7).  
* **R8.** Contrast factor propositional vs. modal: $2^{61}\approx2.31\times10^{18}$ (Section 4.8).  
* **R9.** Variable‑inclusion and computability scaffolding: truth‑table size $2^{|V(\varphi)|}$ and game‑tree size $b^{d}$, respectively, both exhibiting the same exponential growth pattern (Section 4.9).

## 6. Extended Derivations and Worked Examples

### 7.1 Detailed derivation for the Wise Men / muddy‑children trajectory  

The three‑agent Wise Men puzzle is modelled in an S5 epistemic setting (agents have equivalence relations).  The initial world set is  

\[
|W_{0}| = 2^{3}=8 .
\]

The king’s public announcement “at least one hat is black’’ eliminates the all‑white world, giving  

\[
|W_{1}| = 8-1 = 7 .
\]

Each subsequent “I don’t know’’ announcement removes exactly those worlds in which the announcing agent would be able to infer its own hat colour.  For agent $a$ the worlds with a single black hat are $ \{\,BBW,\,BWB,\,WBB\,\}$; the announcement that $a$ does not know eliminates the world $WWB$ (the only world in which $a$ would see two white hats and thus know it must wear black).  Hence  

\[
|W_{2}| = 7-1 = 6 .
\]

Agent $b$ now eliminates the two worlds $BBW$ and $WBW$, because in each of them $b$ would see a single black hat and could therefore deduce its own colour.  Thus  

\[
|W_{3}| = 6-2 = 4 .
\]

The shrinkage factor from the first announcement onward is  

\[
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75 .
\]

If the public announcement were modelled by an action model with three events ($|E|=3$) instead of a single trivial event, the product model would have  

\[
|W_{0}|\times|E| = 8\times3 = 24
\]

worlds, illustrating that DEL can both shrink and expand the model size.  The numbers above follow directly from the combinatorial counting described in Section 4.3 and are consistent with the philosophical motivation for introducing dynamic epistemic logic given in [4] (“modal‑logic teaching motivated by philosophical problems”).

### 7.2 Variable‑inclusion truth‑table example  

Variable‑inclusion logics assign a distinct set of propositional variables $V(\varphi)$ to each formula $\varphi$.  The truth‑table size for $\varphi$ is  

\[
2^{|V(\varphi)|}.
\]

Consider a formula $\varphi$ that mentions exactly five distinct variables, e.g.  

\[
\varphi \;=\; (p_{1}\land p_{2})\;\lor\;(p_{3}\rightarrow(p_{4}\leftrightarrow p_{5})).
\]

Here $|V(\varphi)|=5$, so the truth‑table contains  

\[
2^{5}=32
\]

rows.  If a student attempts to enumerate the table by hand, the workload already exceeds the comfortable manual limit identified in Section 4.1 (the liars‑and‑truth‑tellers puzzle becomes unwieldy at $n=10$, where $2^{10}=1\,024$ rows).  This concrete example demonstrates the quantitative checkpoint that justifies the transition from propositional to variable‑inclusion logics, as discussed in the algebraic treatment of left variable inclusion in [6] and supported by the broader outlook on logic education in [3].

### 7.3 Computability‑logic game‑tree calculation  

Computability logic interprets logical operators as operations on interactive games.  A game tree with uniform branching factor $b$ and depth $d$ has  

\[
b^{d}
\]

nodes.  Take the canonical branching factor $b=2$ (binary choices) and depth $d=4$ (four rounds of interaction).  The node count is  

\[
2^{4}=16 .
\]

If we increase the branching to $b=3$ while keeping $d=4$, the tree size becomes  

\[
3^{4}=81 .
\]

These numbers are obtained by elementary exponentiation and illustrate the exponential growth pattern that mirrors the $2^{n}$ scaffold used throughout the paper.  The relevance of computability‑logic game trees for curriculum design is highlighted in [7] (“computability logic reinterprets logical operators as operations on interactive computational problems”).

### 7.4 Combinatorics of a neutral temporal deontic STIT frame  

The STIT (Seeing To It That) framework of [8] defines a language with a finite set of agents $Ag=\{1,\dots ,n\}$.  In the simplest neutral temporal deontic STIT model each agent chooses between two primitive actions: *perform* (denoted $\top$) or *omit* (denoted $\bot$).  The total number of joint action profiles is therefore  

\[
2^{n}.
\]

For the three‑agent case ($n=3$) used in the Wise Men example, the number of possible joint STIT choices is  

\[
2^{3}=8 .
\]

Each profile corresponds to a distinct world in the underlying relational frame, so the frame size matches the $8$ worlds of the propositional stage.  This alignment shows how the same exponential bound governs both epistemic and deontic modelling choices, reinforcing the quantitative unity of the LogiKEy sequence.

### 7.5 Extended proof‑length tower for Boolos’s inference  

Section 4.4 introduced the recurrence $L_{n+1}=2^{L_{n}}$ with $L_{0}=1$.  Continuing the iteration beyond $L_{5}$ yields astronomically large numbers.  The next two levels are  

\[
\begin{aligned}
L_{6} &= 2^{L_{5}} = 2^{\,2^{65\,536}} ,\\[2mm]
L_{7} &= 2^{L_{6}} = 2^{\,2^{\,2^{65\,536}}}.
\end{aligned}
\]

Using $\log_{10}(2)=0.30103$, the decimal exponent of $L_{6}$ is  

\[
\log_{10}(L_{6}) = 2^{65\,536}\times0.30103 \approx 10^{19\,728}\times0.30103 \approx 3.02\times10^{19\,728},
\]

so  

\[
L_{6}\approx 10^{\,3.02\times10^{19\,728}} .
\]

Even $L_{5}\approx10^{19\,728}$ already exceeds any feasible manual proof search, illustrating the dramatic advantage of a higher‑order metalogic that can encode such proofs compactly.  The motivation for studying proof‑length blow‑up in a pedagogical context is reinforced by the forward‑looking perspective on proof theory in [3].

These worked examples flesh out the quantitative scaffolding introduced earlier, provide concrete arithmetic that students can verify, and tie each derivation to a specific bibliographic source, thereby strengthening the theoretical underpinnings of the LogiKEy curriculum.

## 7. Discussion

### 7.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Fixed three‑islander puzzle structure | Scaling to different statements changes survivor count exponentially. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only for accessibility relations | Adding symmetry or transitivity would further reduce the count; current numbers are upper bounds for the given constraint. |
| S5 epistemic assumption (equivalence relations) | Weakening to KD45 would alter the admissible relation count. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Represents worst‑case proof‑search; alternative strategies could yield smaller lengths. |
| Independence of Gödel’s three axioms | If axioms are dependent, the consistent space could be larger than $2^{2}=4$. |
| Course‑time ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of thresholds | The hand‑enumeration thresholds are theoretical; actual student limits may differ. |

### 7.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students successfully enumerate all $2^{64}\approx10^{19}$ accessibility relations for the modal stage without assistance from a model finder. Such performance would demonstrate that the combinatorial count vastly over‑