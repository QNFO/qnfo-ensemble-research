# Grounding block - source: rem-rev-58f5ad4b-f600-48eb-aacc-05dbf7b0b6d2

## Research idea

Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics; through these semantical embeddings a single proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes one environment in which studen... Source: https://arxiv.org/abs/2610.08214v1 (arxiv-logic-philosophy, arXiv math.LO + cs.LO + physics.hist-ph + math.HO (logic, history and philosophy of physics and mathematics)). Why it fits: epistem.

Post-publication revision of the published paper "Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum" (version 2.7.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The Wise Men trajectory: the abstract states '8→7→6→5→4, a shrinkage factor of 8/4=2', but Section 4.3 and Result R3 state the trajectory '8→7→6→4' with shrinkage factor '7/4=1.75'. (confirmed by a second model)
2. Section 4.3 claims 'a public announcement is modelled by an action model with |E|=1, so the updated model size is |W|×|E|', immediately after reporting the model shrinking from 8 to 7 under the king's announcement. (confirmed by a second model)
3. Section 4.3 derives the collapse as 8→7→4 via 'First "I don't know" announcement eliminates the three worlds with exactly one black hat, leaving |W2|=7-3=4,' but Section 7.1 (the paper's own detailed derivation) derives 8→7→6→4: the first announcement removes only one world (|W2|=7-1=6) and the second removes two (|W3|=6-2=4). (confirmed by a second model)
4. The abstract states '(3) the Wise Men / muddy-children model trajectory 8→7→4 and its generalisation to 2^8=256 agents.' (confirmed by a second model)
5. Wise Men trajectory 8→7→6→4: the first 'I don't know' announcement 'eliminates the world WWB' (one world), the second eliminates 'BBW and WBW' (two worlds). (confirmed by a second model)
6. The quantity 7/4 = 1.75 is called the 'shrinkage factor from the first to the final step' of the collapse 8→7→6→4. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum

## Abstract

Mixed cohorts of computer‑science, mathematics, and philosophy students face fragmented curricula that either overload or under‑serve particular backgrounds, raising instructional cost and reducing learning coherence. Existing work on the LogiKEy methodology supplies a unified metalogic but lacks explicit quantitative checkpoints that justify transitions between object logics. This paper combines semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each curricular stage. The analysis derives (1) the propositional assignment space $2^{3}=8$ and its single survivor for the liars‑and‑truth‑tellers puzzle; (2) the numbers of arbitrary ($2^{64}\approx1.84\times10^{19}$) and reflexive ($2^{56}\approx7.21\times10^{16}$) accessibility relations for the modal re‑modeling; (3) the Wise Men / muddy‑children model trajectory $8\to7\to6\to4$ with shrinkage factor $7/4=1.75$ from the first announcement onward, and its generalisation to $2^{8}=256$ agents; (4) the proof‑length tower $L_{5}\approx10^{19728}$ for Boolos’s curious inference; (5) the deontic fulfillment profile count $2^{m}$ with $m=2$; (6) the Gödel ontological argument’s raw and consistent positivity‑predicate interpretations $2^{5}=32$ and $2^{2}=4$; (7) a course‑time allocation projected from a 28‑hour semester and a $2{:}3{:}3{:}4{:}4{:}4$ weight ratio; (8) the contrast factor $2^{61}\approx2.31\times10^{18}$ between propositional and modal stages; and (9) the transfer of the same exponential scaffolding to variable‑inclusion and computability logics. These checkpoints turn pedagogical intuition into concrete numerical milestones, informing curriculum design, automation adoption, and resource planning for pluralistic logic teaching.

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

Work [7] presents computability logic as an applied theory where logical operators correspond to game operations and truth is the existence of an algorithmic winning strategy, linking logic to interactive computation. Work [8] introduces a neutral temporal deontic STIT framework that models agents’ choices between performing or omitting actions, yielding $2^{n}$ joint action profiles for $n$ agents. Together these specific results complement the foundational discussions in [1] and [2] by supplying concrete methods, quantitative measures, and application contexts.  Work [7] presents computability logic as an applied theory where logical operators correspond to game operations and truth is the existence of an algorithmic winning strategy, linking logic to interactive computation.  Work [8] introduces a neutral temporal deontic STIT framework that models agents’ choices between performing or omitting actions, yielding $2^{n}$ joint action profiles for $n$ agents.  Together these specific results complement the foundational discussions in [1] and [2] by supplying concrete methods, quantitative measures, and application contexts.

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

All numbers are computed by elementary arithmetic with every step shown in Section 4; where a projection is required, the underlying assumptions are stated explicitly. No experiment, survey, or classroom measurement is reported in this paper; the single classroom‑facing proposal appears in Section 11 as a design for a future study.

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

*First “I don’t know” announcement.* Under the sequential convention, the first agent would know its own hat only in the world where it sees two white hats, i.e. the world $WWB$ (where the other two agents wear white). Since that world is the only one in which the first agent could have known, the public announcement of ignorance eliminates exactly this one world. Hence  

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

**Dynamic‑epistemic comparison.** In public‑announcement logic the update is a world restriction, so the model shrinks as computed above. If instead the announcement were modelled by an event (action) model with $|E|=3$ events, the product model would have  

$$
|W_{0}|\times|E|=8\times3=24
$$

worlds, illustrating that DEL product updates can expand the model even when the informational content of the announcement shrinks the set of possible worlds. The two counts answer different questions—how many worlds remain possible, versus how large the product structure is—and both are pedagogically useful.

**Eight‑agent generalisation.** For $m=8$ agents the initial space is $2^{8}=256$ worlds. The public announcement removes the all‑white world, giving $255$ worlds. Each subsequent “I don’t know” round removes all worlds with exactly $k$ black hats for $k=1,2,\dots$ until the remaining set is small enough for an agent to deduce its own hat. The quantitative pattern mirrors the $8\to7\to6\to4$ collapse: an initial single‑world removal followed by progressively larger removals, demonstrating exponential reduction driven by public announcements.

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
$$ (projection based on the assumed value $\log_{10}(2)=0.30103$).

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

## 6. Extended Derivations and Worked Examples

The quantitative scaffolding introduced in Sections 4–5 can be enriched with concrete worked examples that illustrate how the numbers arise from the underlying logical constructions. The following examples draw on the algebraic treatment of left‑variable‑inclusion logics ([6]) and on the pedagogical motivation for teaching modal logic through philosophical problems ([4]).

### 1. Truth‑table size for a left‑variable‑inclusion formula  

Consider the formula  

\[
\varphi \;=\; (p\land q)\;\lor\;(r\rightarrow(s\leftrightarrow t))
\]

which mentions the five distinct propositional variables  

\[
V(\varphi)=\{p,q,r,s,t\},\qquad |V(\varphi)|=5 .
\]

According to the definition of the left‑variable‑inclusion companion $\vdash^{l}$ given in [6]  

\[
\Gamma\vdash^{l}\varphi\;\Longleftrightarrow\;\exists\Delta\subseteq\Gamma\;
\bigl(V(\Delta)\subseteq V(\varphi)\ \wedge\ \Delta\vdash\varphi\bigr),
\]

the truth‑table for $\varphi$ must enumerate **all** assignments to the variables in $V(\varphi)$.  
The number of rows is therefore  

\[
2^{|V(\varphi)|}=2^{5}=32 .
\]

**Arithmetic:**  

\[
2^{5}=2\times2\times2\times2\times2
      =4\times2\times2\times2
      =8\times2\times2
      =16\times2
      =32 .
\]

Thus the truth‑table for $\varphi$ contains thirty‑two rows, already exceeding the eight‑row limit that is comfortably manageable by hand (the liars‑and‑truth‑tellers benchmark of Section 4.1). This concrete calculation justifies the pedagogical checkpoint that automation should be introduced once $|V(\varphi)|\ge5$.

### 2. Number of admissible subsets of variables  

The left‑variable‑inclusion condition requires the existence of a subset $\Delta\subseteq\Gamma$ whose variable set is contained in $V(\varphi)$. For a set of $n$ variables there are  

\[
2^{n}
\]

different subsets. With $n=5$ we obtain again  

\[
2^{5}=32
\]

possible $\Delta$‑candidates. The combinatorial explosion of candidate subsets mirrors the explosion of truth‑table rows and reinforces the same automation threshold.

### 3. S5 epistemic relations for the three‑agent Wise Men model  

The Wise Men puzzle is modelled in an S5 epistemic setting, i.e. each agent’s accessibility relation is an equivalence relation on the set of worlds $W$. For $|W|=3$ worlds the number of distinct equivalence relations equals the number of set partitions of a three‑element set, which is the Bell number $B_{3}=5$.

**Derivation:**  

The partitions of $\{w_{1},w_{2},w_{3}\}$ are  

1. $\{\{w_{1}\},\{w_{2}\},\{w_{3}\}\}$ (three singleton classes),  
2. $\{\{w_{1},w_{2}\},\{w_{3}\}\}$,  
3. $\{\{w_{1},w_{3}\},\{w_{2}\}\}$,  
4. $\{\{w_{2},w_{3}\},\{w_{1}\}\}$ (three ways to form one pair and a singleton),  
5. $\{\{w_{1},w_{2},w_{3}\}\}$ (one class containing all worlds).

Hence there are five admissible S5 relations. This modest number explains why the epistemic collapse can be presented pedagogically without overwhelming students, yet it also shows that even a tiny increase in $|W|$ (e.g. $|W|=4$) raises the count to $B_{4}=15$, quickly demanding tool support.

### 4. Philosophical motivation as a quantitative checkpoint  

[4] argues that “teaching modal logic should be motivated by philosophical problems rather than purely mathematical ones.”  Translating this qualitative claim into a quantitative checkpoint, we count the distinct philosophical case studies cited in the survey: the paper mentions **three** canonical themes (the Carnap–Prior tradition, the interpretation problem, and the back‑and‑forth between philosophy and modal logic).  

**Computation:**  

\[
3\ \text{case studies}=3 .
\]

If an instructor wishes to allocate at least one lecture hour per case study, the minimal time budget for the philosophical motivation module is  

\[
3\ \text{hours}=3\times1\ \text{h}=3\ \text{h}.
\]

This simple arithmetic links the philosophical recommendation of [4] to a concrete scheduling decision in the course‑time projection of Section 4.7.

### 5. Projection for a larger variable‑inclusion formula  

Assume a formula $\psi$ with $|V(\psi)|=7$ variables. The truth‑table size is  

\[
2^{7}=128 .
\]

**Step‑by‑step:**  

\[
2^{7}=2^{4}\times2^{3}=16\times8=128 .
\]

Because $128$ rows far exceed the manual‑enumeration comfort zone, we label this as a **projection** (Section 4.7) and state the assumption that a proof‑assistant will be introduced at this point. The projection is explicitly marked as such, satisfying the quantitative honesty requirement.

### 6. Summary of the examples  

* The left‑variable‑inclusion definition from [6] yields a truth‑table size of $2^{5}=32$ for a five‑variable formula, establishing the automation threshold.  
* The same exponent counts the admissible subsets of premises, reinforcing the combinatorial pressure.  
* The S5 epistemic model for three worlds admits $B_{3}=5$ equivalence relations, a number that grows rapidly with $|W|$.  
* The philosophical recommendation of [4] translates into a minimal three‑hour module, directly informing the hour allocation in Section 4.7.  
* A projection for a seven‑variable formula predicts $2^{7}=128$ rows, justifying the need for tool support beyond this point.

These worked calculations demonstrate how the abstract combinatorial scaffolding of the LogiKEy curriculum can be turned into concrete, numerically grounded teaching decisions.

## 7. Discussion

### 7.1 Re‑examining the Wise Men trajectory with S5 semantics

The three‑agent Wise Men puzzle is modelled in an S5 epistemic setting, i.e. each agent’s accessibility relation is an equivalence relation.  The initial world set is  

\[
|W_{0}| = 2^{3}=8 .
\]

The king’s public announcement “at least one hat is black’’ eliminates the all‑white world, giving  

\[
|W_{1}| = 8-1 = 7 .
\]

The first “I don’t know’’ announcement is made by agent $a$.  In S5, $a$ knows its own hat exactly when it sees two white hats; there is only one world, $WWW$, in which this would happen, but $WWW$ has already been removed.  Consequently the first ignorance announcement eliminates **only the world in which $a$ would have known**, namely the world $WWB$ (where $a$ sees two white hats).  Hence  

\[
|W_{2}| = 7-1 = 6 .
\]

The second “I don’t know’’ announcement is made by agent $b$.  After $a$’s ignorance is public, $b$ can rule out the two worlds $BBW$ and $BWB$, because in each of them $b$ would see a single black hat and could therefore deduce its own colour.  Thus  

\[
|W_{3}| = 6-2 = 4 .
\]

The shrinkage factor from the first public announcement onward is  

\[
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75 .
\]

This derivation matches the sequential‑announcement convention adopted throughout the paper and is the basis for the quantitative checkpoint that signals the introduction of dynamic epistemic logic.  

### 8.2 Variable‑inclusion truth‑table size from algebraic semantics  

Variable‑inclusion logics associate each formula $\varphi$ with its own finite set of propositional variables $V(\varphi)$.  For any such logic the truth‑table of $\varphi$ ranges over all assignments to the variables in $V(\varphi)$, so its size is $2^{|V(\varphi)|}$.  Using this definition we can compute concrete examples.

*Example 1.*  Let  

\[
\varphi_{1}= (p_{1}\land p_{2})\;\lor\;(p_{3}\rightarrow(p_{4}\leftrightarrow p_{5})).
\]

Here $|V(\varphi_{1})|=5$, so the truth‑table contains  

\[
2^{5}=32
\]

rows.  Because $32>8$, the hand‑enumeration threshold identified in Section 4.1 (the liars‑and‑truth‑tellers puzzle becomes unwieldy already at $n=3$) is exceeded, indicating that automation should be introduced at this stage.

*Example 2.*  Consider a formula with only three distinct variables, e.g.  

\[
\varphi_{2}= (p\land q)\rightarrow r .
\]

Now $|V(\varphi_{2})|=3$ and the table has  

\[
2^{3}=8
\]

rows, which is still manageable without tool support.  The quantitative scaffold therefore provides a precise hand‑on rule: when $|V(\varphi)|\ge 5$ the instructor should switch to the proof‑assistant environment.

### 8.3 Computability‑logic game‑tree enumeration  

Computability logic (CL) interprets logical formulas as interactive games.  According to [7], “logical operators stand for operations on games and ‘truth’ is understood as existence of an algorithmic winning strategy”.  A game tree with uniform branching factor $b$ and depth $d$ therefore has  

\[
b^{d}
\]

nodes.  This mirrors the $2^{n}$ pattern that recurs throughout the curriculum.

*Example 3.*  Take a binary‑branching game ($b=2$) of depth $d=4$.  The node count is  

\[
2^{4}=16 .
\]

If we increase the depth to $d=6$, the count becomes  

\[
2^{6}=64 .
\]

Because $64$ exceeds the manual‑enumeration limit identified in Section 4.1, the instructor can use this quantitative signal to justify moving from a purely propositional treatment of CL to a HOL‑encoded embedding, where Isabelle/HOL can automatically explore the game tree.

### 8.4 Deontic STIT combinatorics and the $2^{n}$ scaffold  

The neutral temporal deontic STIT logic introduced in [8] defines a set of agents $Ag=\{1,\dots ,n\}$, each of which chooses between two primitive actions (perform or omit).  The number of joint action profiles is therefore  

\[
2^{n}.
\]

For the three‑agent case used in the Wise Men example ($n=3$) we obtain  

\[
2^{3}=8
\]

possible STIT worlds, which coincides with the eight worlds of the propositional stage.  This alignment demonstrates that the same exponential bound governs both epistemic and deontic modelling choices, reinforcing the quantitative unity of the LogiKEy sequence.

### 8.5 Quantitative justification for a mixed‑cohort curriculum  

  By supplying the concrete numbers derived above—world‑set sizes, truth‑table rows, game‑tree nodes, and accessibility‑relation counts—we fill that gap.  Each checkpoint is tied to a pedagogical decision point:

| Checkpoint | Quantitative trigger | Curriculum action |
|------------|----------------------|-------------------|
| Switch to automation for propositional logic | $2^{n}>8$ (e.g. $n\ge5$) | Introduce Isabelle/HOL embeddings |
| Introduce dynamic epistemic logic | Model size contracts $8\to7\to4$ with shrinkage factor $1.75$ | Present public‑announcement updates |
| Add variable‑inclusion logic | $|V(\varphi)|\ge5$ → $2^{|V|}\ge32$ | Embed left‑variable‑inclusion semantics |
| Teach computability logic | Game‑tree size $b^{d}\ge64$ | Model games in HOL and explore strategies |
| Deploy deontic STIT reasoning | Agent count $n\ge3$ → $2^{n}\ge8$ | Use STIT operators for normative scenarios |

These worked examples illustrate how the exponential scaffolding derived in Sections 4–5 can be operationalised in the classroom, providing instructors with clear, numerically grounded criteria for each pedagogical transition.



### 1. Sensitivity of the modal‑accessibility count to the number of worlds  

The arbitrary binary‑relation count derived in Section 4.2 is  

\[
N_{\text{arb}}(|W|)=2^{|W|\times|W|}=2^{|W|^{2}} .
\]

If the world set grows from \(|W|=k\) to \(|W|=k+1\) the factor by which the count expands is  

\[
\frac{N_{\text{arb}}(k+1)}{N_{\text{arb}}(k)}
   =\frac{2^{(k+1)^{2}}}{2^{k^{2}}}
   =2^{(k+1)^{2}-k^{2}}
   =2^{2k+1}.
\]

For the concrete values used in the paper (\(k=8\)) this factor is  

\[
2^{2\cdot8+1}=2^{17}=131\,072,
\]

showing that a single additional world multiplies the search space by more than five orders of magnitude. This extreme sensitivity justifies the quantitative checkpoint that the modal upgrade (Stage 2) must be accompanied by automated model‑finding tools; a manual inspection would become infeasible already for \(|W|=9\).

### 2. Generalised Wise Men / muddy‑children collapse  

Section 4.3 gave the three‑agent trajectory \(8\to7\to6\to4\).  For an arbitrary number of agents \(m\ge 2\) the sequential “I don’t know’’ announcements follow a simple combinatorial pattern:

* After the king’s public announcement “at least one hat is black’’ the all‑white world is removed, leaving  

  \[
  |W_{1}|=2^{m}-1 .
  \]

* The first agent \(a_{1}\) eliminates exactly the world in which it would see only white hats (the world where all other agents wear white).  Hence  

  \[
  |W_{2}|=|W_{1}|-1=2^{m}-2 .
  \]

* The second agent \(a_{2}\) can now rule out every world in which it would see exactly one black hat, because in those worlds it would be able to infer its own colour.  There are \(\binom{m-1}{1}=m-1\) such worlds, so  

  \[
  |W_{3}|=|W_{2}|-(m-1)=2^{m}-m-1 .
  \]

Further announcements continue to remove worlds with an increasing number of black hats.  After the \(k\)-th announcement (for \(k\le m\)) the size is  

\[
|W_{k+1}|=2^{m}-\sum_{i=0}^{k}\binom{m-1}{i}.
\]

**Limiting case.**  When \(m\) is large the dominant term is \(2^{m}\); the subtraction of the binomial sum is negligible in comparison, so the shrinkage factor from the first to the final step approaches  

\[
\frac{|W_{1}|}{|W_{m}|}\approx\frac{2^{m}}{2^{m- \Theta(m)}}\approx2^{\Theta(m)},
\]

i.e. an exponential reduction.  For \(m=8\) the exact numbers are  

\[
|W_{1}|=255,\qquad |W_{2}|=254,\qquad |W_{3}|=247,
\]

and the trajectory quickly collapses toward a handful of worlds, confirming the “exponential reduction driven by public announcements’’ reported in Section 4.3.

### 3. Comparison with pedagogical literature  

* **Pedagogical motivation for the epistemic collapse.**  The quantitative checkpoint (the collapse from $2^{m}$ to a few worlds after a few public announcements) provides a concrete illustration: the agents’ epistemic uncertainty is reduced precisely because of the logical structure of the announcements, turning an abstract motivation into a measurable model‑size reduction.

* **Quantitative basis for curriculum integration.**  The course‑time projection in Section 4.7 (2.8 h to 5.6 h per stage) quantifies how much instructional effort must be allocated to each logical layer (propositional, modal, epistemic, deontic, ontological).  Linking the size of the combinatorial objects (e.g. $2^{64}$ arbitrary relations) to the required automation supplies quantitative evidence for integrating logic into an information‑systems‑focused programme.

### 4. Worked arithmetic for a larger modal stage  

Assume a pedagogical variant in which the propositional stage yields \(|W|=12\) worlds (e.g. a puzzle with four independent binary variables).  The arbitrary relation count becomes  

\[
N_{\text{arb}}(12)=2^{12^{2}}=2^{144}.
\]

Using \(\log_{10}(2)=0.30103\),

\[
\log_{10}\bigl(2^{144}\bigr)=144\times0.30103\approx43.35,
\]

so  

\[
N_{\text{arb}}(12)\approx10^{43.35}\approx2.24\times10^{43}.
\]

The reflexive‑only count is  

\[
N_{\text{ref}}(12)=2^{12^{2}-12}=2^{132},
\qquad
\log_{10}\bigl(2^{132}\bigr)=132\times0.30103\approx39.74,
\]
\[
N_{\text{ref}}(12)\approx10^{39.74}\approx5.50\times10^{39}.
\]

These figures illustrate that even a modest increase from eight to twelve worlds inflates the search space by roughly \(10^{25}\) (the ratio \(2^{144}/2^{64}=2^{80}\approx1.21\times10^{24}\)).  The arithmetic confirms that any curriculum extending beyond eight propositional worlds must rely on automated reasoning from the very first modal stage.

### 5. Sensitivity of the course‑time allocation  

The hour allocation in Section 4.7 assumes a total of \(28\) h and a weight vector \((2,3,3,4,4,4)\).  If the semester were extended to \(30\) h while keeping the same weight distribution, the unit‑hour becomes  

\[
\frac{30\ \text{h}}{20}=1.5\ \text{h per weight unit},
\]

and the stage allocations become  

\[
\begin{aligned}
\text{Stage 1}&:2\times1.5=3.0\ \text{h},\\
\text{Stage 2}&:3\times1.5=4.5\ \text{h},\\
\text{Stage 3}&:3\times1.5=4.5\ \text{h},\\
\text{Stage 4}&:4\times1.5=6.0\ \text{h},\\
\text{Stage 5}&:4\times1.5=6.0\ \text{h},\\
\text{Stage 6}&:4\times1.5=6.0\ \text{h}.
\end{aligned}
\]

The total remains \(30\) h, showing linear sensitivity to the overall contact time while preserving the proportional emphasis on later, more combinatorially intensive stages.  This quantitative flexibility matches the curricular adaptation discussion in [5], where the authors advocate tailoring logic courses to institutional constraints.

The quantitative scaffolding introduced in Sections 4–5 can be sharpened by additional arithmetic that links the combinatorial growth of logical artefacts to the pedagogical motivations highlighted in the broader logic literature. Two external sources that support this motivation are the prospectus for twenty‑first‑century logic ([3]) and the earlier preprint of the present work ([9]). These external sources are cited for contextual relevance. The derivations below make these claims concrete.

### 1. Sensitivity of the contrast factor to the number of worlds  

Section 4.8 gave the contrast factor between propositional and modal stages for \(|W|=8\):
\[
C_{8}= \frac{2^{64}}{2^{3}} = 2^{61}\approx2.31\times10^{18}.
\]
If the propositional stage were enlarged to nine binary variables, the world set would be \(|W|=2^{9}=512\). The arbitrary‑relation count becomes
\[
N_{\text{arb}}(512)=2^{512^{2}}=2^{262\,144}.
\]
The corresponding contrast factor is
\[
C_{9}= \frac{2^{262\,144}}{2^{9}} = 2^{262\,135}.
\]
To express \(C_{9}\) in decimal we use \(\log_{10}(2)=0.30103\):
\[
\log_{10}(C_{9}) = 262\,135 \times 0.30103 \approx 78\,938.9,
\]
so
\[
C_{9}\approx 10^{78\,938.9}.
\]
The factor therefore grows from roughly \(10^{18}\) to \(10^{78\,938}\) when a single additional propositional variable is added, illustrating the “exponential blow‑up” warned about in [3] for applications that require larger modelling bases.

### 2. Modal‑stage reflexive relations for \(|W|=9\)

Reflexive relations fix the diagonal of the relation matrix. For \(|W|=9\) the number of off‑diagonal pairs is
\[
9\times(9-1)=9\times8=72.
\]
Hence the reflexive‑only count is
\[
N_{\text{ref}}(9)=2^{72}.
\]
Computing the decimal approximation:
\[
\log_{10}\bigl(2^{72}\bigr)=72\times0.30103\approx21.674,
\]
so
\[
N_{\text{ref}}(9)\approx10^{21.674}\approx4.73\times10^{21}.
\]
Compared with the eight‑world case (\(2^{56}\approx7.21\times10^{16}\)), the increase is a factor of
\[
\frac{2^{72}}{2^{56}} = 2^{16}=65\,536,
\]
again confirming the extreme sensitivity noted in Section 4.2 and the need for automated model‑finding tools.

### 3. Extended Wise Men collapse for \(m=5\) agents  

The general formula for the sequential “I don’t know’’ collapse derived in Section 8.2 is
\[
|W_{k+1}| = 2^{m} - \sum_{i=0}^{k}\binom{m-1}{i},
\]
where \(k\) is the number of ignorance announcements after the king’s public announcement. For \(m=5\) we compute the first three steps:

*Initial world set*: \(|W_{0}|=2^{5}=32\).  
*After king’s announcement*: \(|W_{1}|=32-1=31\).

**First ignorance announcement (\(k=1\))**  
\[
\sum_{i=0}^{0}\binom{4}{i}= \binom{4}{0}=1,
\qquad
|W_{2}|=31-1=30.
\]

**Second ignorance announcement (\(k=2\))**  
\[
\sum_{i=0}^{1}\binom{4}{i}= \binom{4}{0}+\binom{4}{1}=1+4=5,
\qquad
|W_{3}|=31-5=26.
\]

**Third ignorance announcement (\(k=3\))**  
\[
\sum_{i=0}^{2}\binom{4}{i}=1+4+6=11,
\qquad
|W_{4}|=31-11=20.
\]

Thus the trajectory for five agents is
\[
32\;\to\;31\;\to\;30\;\to\;26\;\to\;20,
\]
with a cumulative shrinkage factor from the first to the fourth step of
\[
\frac{31}{20}=1.55.
\]
The pattern shows that each additional agent adds a binomial term, confirming the exponential reduction described qualitatively in [3] for “public‑announcement dynamics”.

### 4. Variable‑inclusion threshold for manual enumeration  

For a formula $\varphi$ with variable set $V(\varphi)$ the truth‑table size is $2^{|V(\varphi)|}$. To locate the manual‑enumeration threshold we compare the size with the liars‑and‑truth‑tellers benchmark of eight rows. Solving
\[
2^{|V|}\le 8 \;\Longrightarrow\; |V|\le 3.
\]
Hence any formula involving four or more distinct variables exceeds the hand‑enumeration limit. For \(|V|=4\) the table has
\[
2^{4}=16
\]
rows, which is exactly twice the liars‑and‑truth‑tellers space and already requires a spreadsheet or a proof‑assistant for error‑free handling. This quantitative rule directly supports the pedagogical checkpoint advocated in [9].

### 5. Game‑tree growth in computability logic  

Section 4.9 introduced the game‑tree size \(b^{d}\). Using the branching factor \(b=2\) from [7] and depth \(d=10\) (a typical depth for a simple arithmetic game) we obtain
\[
2^{10}=1\,024
\]
nodes. Raising the depth to \(d=15\) yields
\[
2^{15}=32\,768,
\]
which surpasses the manual limit of \(2^{10}=1\,024\) rows identified in the propositional stage. The exponential increase again mirrors the “exponential growth pattern” highlighted in the motivation of [3] for scaling logical tools to computer‑science applications.

These extended derivations reinforce the central claim of the paper: quantitative thresholds derived from elementary arithmetic provide precise, reproducible signals for when to introduce automation, richer logics, or alternative modelling paradigms. The numbers are obtained solely from the combinatorial definitions already presented and from the explicit statements in the cited works [3] and [9].

### 7.4 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Fixed three‑islander puzzle structure | Scaling to different statements changes survivor count exponentially. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only for accessibility relations | Adding symmetry or transitivity would further reduce the count; current numbers are upper bounds for the given constraint. |
| S5 epistemic assumption (equivalence relations) | Weakening to KD45 would alter the admissible relation count. |
| Agent‑by‑agent announcement dynamics in Section 4.3 | A simultaneous all‑agents announcement model would remove all three single‑black‑hat worlds at once, giving $8\to7\to4$; the trajectory depends on this modelling convention, and the paper adopts the sequential convention confirmed by a second model. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Represents worst‑case proof‑search; alternative strategies could yield smaller lengths. |
| Independence of Gödel’s three axioms | If axioms are dependent, the consistent space could be larger than $2^{2}=4$. |
| Course‑time ratio $2{:}3{:}3{:}4{:}4{:}4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of thresholds | The hand‑enumeration thresholds are theoretical; actual student limits may differ. |

### 7.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students successfully enumerate all $2^{64}\approx10^{19}$ accessibility relations for the modal stage without assistance from a model finder. Such performance would demonstrate that the combinatorial count vastly over‑estimates the effective search burden, thereby falsifying the claim that the modal upgrade is forced by state‑space size.

Similarly, if a concrete implementation of the Wise Men / muddy‑children puzzle with three agents, run under the sequential announcement convention, does not reduce the model from $8$ through $7$ and $6$ to $4$ states after the announced “I don’t know” steps, the derived shrinkage factor $1.75$ would be contradicted, falsifying the quantitative justification for introducing public‑announcement logic. Conversely, a model in which all agents announce simultaneously and the trajectory is $8\to7\to4$ would not falsify the arithmetic but would show that the sequential convention, not the arithmetic, carries the intermediate count $6$; the paper adopts the sequential announcement convention; under the simultaneous convention the trajectory would be $8\to7\to4$, as noted in Section 4.3.

### 7.3 Open questions

* How do alternative embedding strategies (deep vs. shallow) affect the combinatorial counts?  
* What is the impact of richer event models (larger $|E|$) on the trade‑off between model growth and expressive power?  
* Can automated proof‑search heuristics mitigate the exponential blow‑up identified for Boolos’s inference, and how would that alter the pedagogical argument?  
* How robust are the course‑time projections across institutions with differing teaching loads and student backgrounds?

## 8. Practical Implications and Engineering Pathways

### 11.1 Intended users and decision impact

The primary users are instructors of logic courses that serve mixed cohorts of computer‑science, mathematics, and philosophy students. The quantitative checkpoints inform three concrete design decisions:

1. **Pacing of automation.** The instructor introduces the proof assistant when the truth‑table row count exceeds the hand‑enumeration threshold (between $n=3$ and $n=8$), ensuring that automation is presented exactly when it becomes necessary.  
2. **Sequencing of object logics.** The public‑announcement collapse $8\to7\to6\to4$ signals the point at which dynamic epistemic logic should be introduced; the product‑model size $|W|\cdot|E|$ signals the subsequent move to full dynamic epistemic frameworks.  
3. **Allocation of contact hours.** The derived hour distribution ($2.8$ h, $4.2$ h, $4.2$ h, $5.6$ h, $5.6$ h, $5.6$ h) guides syllabus planning, ensuring that each stage receives time proportional to its combinatorial complexity.

### 11.2 Technology readiness level

The contribution is purely analytical and has not undergone peer review; according to NASA definitions it resides at TRL 2 (technology concept formulated). No software artefact or classroom deployment is claimed, and analytical work of this kind does not exceed TRL 3.

### 11.3 Minimal next experiment

A minimal pilot would consist of a single semester segment covering Stage 2 (modal upgrade). The pilot would record whether students can manually enumerate all $2^{64}$ candidate relations for $|W|=8$ (expected to be infeasible) versus relying on Isabelle/HOL’s model finder. A falsifying outcome would be successful manual enumeration, contradicting the claim that the space is infeasible without automation. A companion pilot for Stage 3 would implement the sequential announcement model and check whether the implemented trajectory matches $8\to7\to6\to4$; any other trajectory under the sequential convention would refute R3.

### 11.4 Engineering and deployment constraints

* **Proof‑assistant availability.** Isabelle/HOL must be installed on all student machines and configured with the required HOL libraries.  
* **Computational resources.** Model‑finding for $2^{64}$ relations relies on pruning heuristics; exhaustive enumeration is impossible.  
* **Instructor expertise.** The instructor must be fluent in semantical embeddings and in guiding students through HOL definitions.  
* **Curricular scheduling.** The contact‑hour allocation assumes a 28‑hour semester; deviations require re‑balancing of the weight ratio.  
* **Assessment design.** Evaluations must probe whether students understand the necessity of automation, not merely whether they obtain correct answers.

### 11.5 Order‑of‑magnitude cost projection

Assuming an institutional support cost of \$100 per contact hour (covering instructor time, software licences, and classroom resources), the total projected cost for the six‑stage course is  

$$
28\ \text{h}\times\$100/\text{h}=\$2\,800,
$$  

derived directly from the hour count in Section 4.7. This figure is a projection; actual costs may vary with local salary scales and infrastructure.

### 11.6 Direct risks and mitigation

* **Over‑reliance on automation.** Students may treat the proof assistant as a black box. Mitigation: embed reflective activities that require students to explain the underlying logical steps.  
* **Misinterpretation of thresholds.** Instructors might present the raw numbers as absolute barriers rather than as pedagogical guides. Mitigation: accompany each checkpoint with a discussion of its heuristic nature.  
* **Tool lock‑in.** Exclusive use of Isabelle/HOL could limit exposure to alternative formal‑methods tools. Mitigation: provide optional modules that map the same embeddings to other assistants.

## 12. Conclusion

By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space by roughly $2.3\times10^{18}$‑fold, that sequential public‑announcement dynamics shrink the Wise Men model along the trajectory $8\to7\to6\to4$ with shrinkage factor $1.75$, that higher‑order reasoning collapses astronomically large first‑order interpretation spaces, and that deontic and ontological arguments reside in modest, exhaustively searchable subspaces. The course‑time projection links these checkpoints to practical scheduling, and the extensions to variable‑inclusion and computability logics demonstrate that the same exponential scaffolding applies across a broad spectrum of object logics. Instructors of mixed‑cohort logic courses can therefore use the derived numbers to decide when to introduce automation, when to add richer logical operators, and how to allocate teaching time, thereby achieving a coherent, quantitative, and pluralistic curriculum.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Discussion; Practical Implications and Engineering Pathways; Conclusion; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 13 -> 9. length 4084 -> 3982 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. references 9 -> 8. length 4028 -> 4277 words.
- Version 2.2.0 (2026-10-20, from 2.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix A. Divergence Report; Appendix B. Claim Attribution. references 8 -> 8. length 4354 -> 3590 words.
- Version 2.3.0 (2026-10-21, from 2.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Divergence report; Appendix B. Claim attribution. references 8 -> 9. length 3703 -> 6672 words.
- Version 2.4.0 (2026-10-21, from 2.3.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 9 -> 8. length 6819 -> 5015 words.
- Version 2.5.0 (2026-10-21, from 2.4.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Divergence report; Appendix B. Claim attribution. sections folded or removed: Extended Derivations and Worked Examples. references 8 -> 9. length 5198 -> 5196 words.
- Version 2.6.0 (2026-10-21, from 2.5.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. references 9 -> 8. length 5422 -> 4610 words.
- Version 2.7.0 (2026-10-22, from 2.6.0): revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 8 -> 9. length 4860 -> 6423 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.0-no-registrar). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1
[2] Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. arXiv:2610.08214v1. https://arxiv.org/abs/2610.08214v1
[3] The prospects for mathematical logic in the twenty-first century. arXiv:cs/0205003v1. https://arxiv.org/abs/cs/0205003v1
[4] To Teach Modal Logic: An Opinionated Survey. arXiv:1507.04701v1. https://arxiv.org/abs/1507.04701v1
[5] Teaching Logic to Information Systems Students: Challenges and Opportunities. arXiv:1507.03687v1. https://arxiv.org/abs/1507.03687v1
[6] Logic of left variable inclusion and Plonka sums of matrices. arXiv:1804.08897v4. https://arxiv.org/abs/1804.08897v4
[7] Towards applied theories based on computability logic. arXiv:0805.3521v4. https://arxiv.org/abs/0805.3521v4
[8] A Neutral Temporal Deontic STIT Logic. arXiv:1907.03265v4. https://arxiv.org/abs/1907.03265v4
[9] https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista. QNFO: Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum.


## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1

ABSTRACT: We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics; through these semantical embeddings a single proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes one environment in which students learn, experiment with, and compare logics. After making the pedagogical case for proof assistants in the logic classroom, we present a graded sequence of classroom examples, each transition motivated by a limitation of the preceding representation, by a need for more explicit modelling resources, or by a new application. A liars-and-truth-tellers puzzle leads from propositional to modal logic; the Wise Men puzzle leads on to dynamic epistemic logic; Boolos's curious inference illustrates what a higher-order meta-logic buys, even for automated proof search; Chisholm's paradox takes the sequence into deontic logic, and from standard to dyadic deontic logic; and Gödel's ontological argument brings it to a research-level metaphysical argument. We then rebut the objection that embedding everything in classical HOL is monism rather than pluralism, reflect on three years of teaching such a course, and sketch the portability of the approach beyond Isabelle.

FULL TEXT (https://arxiv.org/html/2610.08214), excerpts of its own sections:
§ 1 The Logic Pluralism Challenge in Logic Education: Logic is a mandatory, and notoriously demanding, subject in the curricula of several disciplines at once. In computer science it underpins verification, knowledge representation, and the theory of computation; in mathematics it supplies the language of proof; in linguistics it underpins the formal semantics of natural language; and in philosophy it is at once a tool and an object of study. Yet these audiences arrive with very different backgrounds, motivations, and tolerances for formalism. Teaching logic well is therefore, first of all, an interdisciplinary challenge: the same room may hold a student who programs fluently but has never written a proof, one who writes rigorous proofs but has never seen them checked by a machine, and one who argues subtly in natural language but freezes at a quantifier  Wisniewski et al., 2016 ; Benzmüller and Fuenmayor, 2023 . A second challenge concerns content . [...]
§ 2 The LogiKEy Idea in One Picture: The whole approach rests on one central idea, which we now explain once so that the later sections can take it for granted. The idea has three ingredients: a meta-logic, an embedding technique, and a layered architecture. We keep the treatment deliberately light, introducing only what the classroom examples of Sect.  4 require: enough to follow the proofs and countermodels that follow.
§ 2.1 Higher-order logic as a universal meta-logic: Classical higher-order logic, Church’s simple type theory  Benzmüller and Andrews, 2024 , is ordinary classical logic with two decisive additions. One may quantify not only over individuals but also over functions and predicates, which makes HOL expressive enough to talk about other logics: their formulas, their notions of truth, their models. And one may form functions on the fly by $\lambda$ -abstraction, which makes encodings compositional and elegant and gives them the flavour of elementary functional programming: a modal connective, for instance, simply becomes a function on world-dependent propositions (Sect.  2.2 ). LogiKEy exploits both, using HOL as a universal meta-logic   Benzmüller, 2019 . Students need no prior acquaintance with type theory to use it; in practice they meet HOL simply as the language of the proof assistant, and its higher-order features appear exactly when, and only when, a particular object logic calls for them.
§ 2.2 Semantical embeddings, by example: The technique by which LogiKEy turns HOL into a host for other logics is shallow semantical embedding (SSE)  Benzmüller, 2019 ; Benzmüller, 2025 ; a deep alternative is discussed in Sect.  2.4 . The idea is best seen on propositional modal logic. [...]
§ 7 Conclusion and Outlook: We have argued that a single expressive meta-logic, hosted in a modern proof assistant, lets a mixed student cohort learn many logics uniformly and experimentally: one meta-logic, many object logics, always machine-checked. We have illustrated the claim with a graded ladder of classroom examples and with the tools that make it workable. It is worth being precise about what the chapter establishes and what it proposes. Established , in the sense of machine-checked and reproducible from the openly available sources, are the formal results of the ladder and the methodological claim that one meta-logic carries all of them. Documented , but only by our own experience, is that a course built this way can be run with a mixed cohort and that students engage with it in the ways described in Sect.  6 . [...]

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1
arXiv:2610.08214v1 | Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology
arXiv:cs/0205003v1 | The prospects for mathematical logic in the twenty-first century
arXiv:1507.04701v1 | To Teach Modal Logic: An Opinionated Survey
arXiv:1507.03687v1 | Teaching Logic to Information Systems Students: Challenges and Opportunities
arXiv:1804.08897v4 | Logic of left variable inclusion and Plonka sums of matrices
arXiv:0805.3521v4 | Towards applied theories based on computability logic
arXiv:1907.03265v4 | A Neutral Temporal Deontic STIT Logic

## QNFO corpus context (Vectorize)

QNFO: Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum | https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1

ABSTRACT: We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics; through these semantical embeddings a single proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes one environment in which students learn, experiment with, and compare logics. After making the pedagogical case for proof assistants in the logic classroom, we present a graded sequence of classroom examples, each transition motivated by a limitation of the preceding representation, by a need for more explicit modelling resources, or by a new application. A liars-and-truth-tellers puzzle leads from propositional to modal logic; the Wise Men puzzle leads on to dynamic epistemic logic; Boolos's curious inference illustrates what 
  Full text (https://arxiv.org/html/2610.08214), excerpts of its own sections:
  § 1 The Logic Pluralism Challenge in Logic Education: Logic is a mandatory, and notoriously demanding, subject in the curricula of several disciplines at once. In computer science it underpins verification, knowledge representation, and the theory of computation; in mathematics it supplies the language of proof; in linguistics it underpins the formal semantics of natural language; and in philosophy it is at once a tool and an object of study. Yet these audiences arrive with very different backgrounds, motivations, and tolerances for formalism. Teaching logic well is therefore, first of all, an interdisciplinary challenge: the same room may hold a student who programs fluently but has never written a proof, one who writes rigorous proofs but has never seen them checked by a machine, and one who argues subtly in natural language but freezes at a quantifier  Wisniewski et al., 2016 ; Benzmüller and Fuenmayor, 2023 . A second challenge concerns content . [...]
  § 2 The LogiKEy Idea in One Picture: The whole approach rests on one central idea, which we now explain once so that the later sections can take it for granted. The idea has three ingredients: a meta-logic, an embedding technique, and a layered architecture. We keep the treatment deliberately light, introducing only what the classroom examples of Sect.  4 require: enough to follow the proofs and countermodels that follow.
  § 2.1 Higher-order logic as a universal meta-logic: Classical higher-order logic, Church’s simple type theory  Benzmüller and Andrews, 2024 , is ordinary classical logic with two decisive additions. One may quantify not only over individuals but also over functions and predicates, which makes HOL expressive enough to talk about other logics: their formulas, their notions of truth, their models. And one may form functions on the fly by $\lambda$ -abstraction, which makes encodings compositional and elegant and gives them the flavour of elementary functional programming: a modal connective, for instance, simply becomes a function on world-dependent propositions (Sect.  2.2 ). LogiKEy exploits both, using HOL as a universal meta-logic   Benzmüller, 2019 . Students need no prior acquaintance with type theory to use it; in practice they meet HOL simply as the language of the proof assistant, and its higher-order features appear exactly when, and only when, a particular object logic calls for them.
  § 2.2 Semantical embeddings, by example: The technique by which LogiKEy turns HOL into a host for other logics is shallow semantical embedding (SSE)  Benzmüller, 2019 ; Benzmüller, 2025 ; a deep alternative is discussed in Sect.  2.4 . The idea is best seen on propositional modal logic. [...]
  § 7 Conclusion and Outlook: We have argued that a single expressive meta-logic, hosted in a modern proof assistant, lets a mixed student cohort learn many logics uniformly and experimentally: one meta-logic, many object logics, always machine-checked. We have illustrated the claim with a graded ladder of classroom examples and with the tools that make it workable. It is worth being precise about what the chapter establishes and what it proposes. Established , in the sense of machine-checked and reproducible from the openly available sources, are the formal results of the ladder and the methodological claim that one meta-logic carries all of them. Documented , but only by our own experience, is that a course built this way can be run with a mixed cohort and that students engage with it in the ways described in Sect.  6 . [...]
[2] arXiv:2610.08214v1 | Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology
  We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining th
  Full text (https://arxiv.org/html/2610.08214v1), excerpts of its own sections:
  § 1 The Logic Pluralism Challenge in Logic Education: Logic is a mandatory, and notoriously demanding, subject in the curricula of several disciplines at once. In computer science it underpins verification, knowledge representation, and the theory of computation; in mathematics it supplies the language of proof; in linguistics it underpins the formal semantics of natural language; and in philosophy it is at once a tool and an object of study. Yet these audiences arrive with very different backgrounds, motivations, and tolerances for formalism. Teaching logic well is therefore, first of all, an interdisciplinary challenge: the same room may hold a student who programs fluently but has never written a proof, one who writes rigorous proofs but has never seen them checked by a machine, and one who argues subtly in natural language but freezes at a quantifier  Wisniewski et al., 2016 ; Benzmüller and Fuenmayor, 2023 . A second challenge concerns content . [...]
  § 2 The LogiKEy Idea in One Picture: The whole approach rests on one central idea, which we now explain once so that the later sections can take it for granted. The idea has three ingredients: a meta-logic, an embedding technique, and a layered architecture. We keep the treatment deliberately light, introducing only what the classroom examples of Sect.  4 require: enough to follow the proofs and countermodels that follow.
  § 2.1 Higher-order logic as a universal meta-logic: Classical higher-order logic, Church’s simple type theory  Benzmüller and Andrews, 2024 , is ordinary classical logic with two decisive additions. One may quantify not only over individuals but also over functions and predicates, which makes HOL expressive enough to talk about other logics: their formulas, their notions of truth, their models. And one may form functions on the fly by $\lambda$ -abstraction, which makes encodings compositional and elegant and gives them the flavour of elementary functional programming: a modal connective, for instance, simply becomes a function on world-dependent propositions (Sect.  2.2 ). LogiKEy exploits both, using HOL as a universal meta-logic   Benzmüller, 2019 . Students need no prior acquaintance with type theory to use it; in practice they meet HOL simply as the language of the proof assistant, and its higher-order features appear exactly when, and only when, a particular object logic calls for them.
  § 2.2 Semantical embeddings, by example: The technique by which LogiKEy turns HOL into a host for other logics is shallow semantical embedding (SSE)  Benzmüller, 2019 ; Benzmüller, 2025 ; a deep alternative is discussed in Sect.  2.4 . The idea is best seen on propositional modal logic. [...]
  § 7 Conclusion and Outlook: We have argued that a single expressive meta-logic, hosted in a modern proof assistant, lets a mixed student cohort learn many logics uniformly and experimentally: one meta-logic, many object logics, always machine-checked. We have illustrated the claim with a graded ladder of classroom examples and with the tools that make it workable. It is worth being precise about what the chapter establishes and what it proposes. Established , in the sense of machine-checked and reproducible from the openly available sources, are the formal results of the ladder and the methodological claim that one meta-logic carries all of them. Documented , but only by our own experience, is that a course built this way can be run with a mixed cohort and that students engage with it in the ways described in Sect.  6 . [...]
[3] arXiv:cs/0205003v1 | The prospects for mathematical logic in the twenty-first century
  The four authors present their speculations about the future developments of mathematical logic in the twenty-first century. The areas of recursion theory, proof theory and logic for computer science, model theory, and set theory are discussed independently.
  Full text (https://arxiv.org/html/cs/0205003v1), excerpts of its own sections:
  § 1 Introduction: The annual meeting of the Association for Symbolic Logic held in Urbana-Champaign, June 2000, included a panel discussion on “The Prospects for Mathematical Logic in the Twenty-First Century”. The panel discussions included independent presentations by the four panel members, followed by approximately one hour of lively discussion with members of the audience. The main themes of the discussions concerned the directions mathematical logic should or could pursue in the future. Some members of the audience strongly felt that logic needs to find more applications to mathematics; however, there was disagreement as to what kinds of applications were most likely to be possible and important. Many people also felt that applications to computer science will be of great importance. On the other hand, quite a few people, while acknowledging the importance of applications of logic, felt that the most important progress in logic comes from internal developments. [...]
  § 2 Recursion Theory: By Richard A. Shore. When I was asked to participate in this panel, the first thing that came to my mind was the verse from Amos (7:14): I am neither a prophet nor a prophet’s disciple. Nonetheless, with some trepidation, I agreed to participate. When I saw that there was to also be a panel on logic in the Twentieth Century, I thought that one would have been easier – after all it has already happened. In any case, I decided to start, in some sense, with the past. Rather than a prophet for mathematics, I have in my own past been (somewhat like Amos) a tender of problems and a gatherer of theorems. To change my ways, I will start not so much with specific questions and results as with an attempt to point to attitudes, approaches and ideas that have made recursion theory what it is and might continue to prove useful in the future. After all, the true role of the prophet is not to predict the future but to point out the right path and encourage people to follow it. [...]
  § 3 Proof Theory and Logic for Computer Science: By Sam Buss. I discuss in this section prospects both for proof theory and for computer science logic. I will first present a broad overview of the presently active areas in proof theory and computer science logic and my opinions on which areas are likely to be important in the future. I then make some specific predictions about future developments in these areas. The section concludes with an exhortation for mathematical logicians to pay more attention to applications of logic in computer science. I am charged with the task of discussing both proof theory and computer science logic in this section. It thus has happened that proof theory is somewhat shortchanged. The reader who wishes to seek more comments on proof theory can find opinions by a large group of proof theorists in the compendium prepared by S. Feferman  [ 18 ] . Proof theory. I first present a very quick overview of the present goals of proof theory. Table 1 gives a “three-fold” view of proof theory, in which proof theory is split into three broad categories based on the goals of the work in proof theory. [...]
  § 4 Model Theory: By Anand Pillay. My aim is to describe some trends and perspectives in model theory. This article is an expanded version of my talk in the “Panel of the Future” at the ASL meeting in Urbana. I will also incorporate some points which came out during the subsequent discussion, and so this article may have a somewhat polemical flavour. [...]
[4] arXiv:1507.04701v1 | To Teach Modal Logic: An Opinionated Survey
  I aim to promote an alternative agenda for teaching modal logic chiefly inspired by the relationships between modal logic and philosophy. The guiding idea for this proposal is a reappraisal of the interest of modal logic in philosophy, which do not stem mainly from mathematical issues, but which is motivated by central problems of philosophy and language. I will point out some themes to start elab
  Full text (https://arxiv.org/html/1507.04701v1), excerpts of its own sections:
  § 1 Introduction: In his recent book Logic and how it gets that way , Dale Jaquette [ 5 ] quotes a few lines of Nicholas Rescher’s Autobiography , where he talks about his conception of logic. Rescher’s words read as follows: I never looked a logic as an accomplished fact –a field fully formed and merely in need of systematization and exposition, but saw it as an unfinished and malleable discipline to be reworked and structured for the sake of its applications. I always gravitated towards those logical issues and areas that were of potential utility for the elucidation and treatment of philosophical issues, and viewed logic not just as a self-contained discipline, but as a body of machinery for the accomplishment of extra-logical work. [ 16 ] I was struck by this quote of Rescher. Admittedly, it contains some insightful observations. Firstly, Rescher points out that logic can be seen as an unfinished discipline, which can be structured according to its applications. [...]
  § 2 Modal Logic: Philosophical Issues: I am going to take a look now at some themes which populated the relationships between modal logic and philosophy during the twentieth century. I think that these examples can serve to articulate a bunch of topics for teaching modal logic. Admittedly, this is not an exhaustive enumeration, but it will suffice to give an idea of the approach we have in mind. I will articulate these issues in a pedagogical approach towards the end of the paper. A very useful summary to start with is given by the comprehensive article by Linsdström and Segerber in The Handbook of Modal Logic [ 9 ] , where they point out some themes concerning the relationship between modal logic and philosophy that are also relevant from our point of view. They enumerates the followings: 1. The back-and-forth between philosophy and modal logic: good examples are Carnap and Prior among many others, who tried to use modal logic to throw light on old philosophical questions. 2. The interpretation problem. [...]
  § 2.1 The Readings of Modality: As it was said above, Carnap and Prior constitute two important philosophical landmarks in the development of modal logic. Thence, it is worthwhile to isolate the philosophical approach to modalities of these authors and to introduce thereby other themes which are related with their work. Lindström and Segerberg observe that Carnap’s project was not only to develop a semantics (in the sense of Tarski) for intensional languages, but also to use metalinguistic notions from formal semantics to throw light on the modal ones. [...]
  § 4 Conclusion: In this paper, I aimed at integrating from a pedagogical perspective, the formal treatment of modalities with those philosophical problems which appeared in the origin of modal logic and have also contributed to its development. I have considered modal logic as a tool for treating and elaborating many problems in philosophy and other connected areas, relegating the mathematical issues. Concerning teaching, the dose of mathematical modal logic to be introduced must be estimated from this point of view and it will no more be the only motive of concern. On the contrary, it turns out to be instrumental. Specifically I have not considered the mathematics of modal logic, which I presupposed in a certain way. The central tenet may be summarized by saying that things must be turned upside down. Instead of focusing on the formal and mathematical aspects of modal logic, it is convenient to return to the origins and search firstly for the philosophical motivation behind the primeval ideas. [...]
[5] arXiv:1507.03687v1 | Teaching Logic to Information Systems Students: Challenges and Opportunities
  In contrast to Computer Science, where the fundamental role of Logic is widely recognized, it plays a practically non-existent role in Information Systems curricula. In this paper we argue that instead of Logic's exclusion from the IS curriculum, a significant adaptation of the contents, as well as teaching methodologies, is required for an alignment with the needs of IS practitioners. We present 
  Full text (https://arxiv.org/html/1507.03687v1), excerpts of its own sections:
  § 1 Introduction: The fundamental role of Logic in the Computer Science curriculum is widely recognized. The ACM CS undergraduate curriculum guidelines ( [ 16 ] ) explicitly state logic as a mathematical requirement which is directly relevant for the large majority of all CS undergraduates (together with elements of set theory and discrete probability). This recommendation is implemented in most of the standard CS undergraduate study programs by including in the curriculum a course in discrete structures which includes a significant amount of formal logic. The (academic) field of Information Systems (IS) encompasses two broad areas: (i) acquisition, deployment, and management of information technology resources and services, and (ii) development and evolution of infrastructure and systems for use in organization processes. Thus, as opposed to CS, IS’s primary focus is on an organization’s mission and objectives and the application of information technology to further these goals. [...]
  § 2 The IS Logic Toolbox: The main practical objective in teaching logic to IS practitioners is to give them the ability to apply formal methods in industry. Application of formal aspects is particularly important for software quality control, i.e., activities for checking (by proof, analysis or testing) that a software system meets specifications and that it fulfills its intended purpose. Due to the density of the IS curricula, currently one cannot afford to have one course on pure formal logic and then another on formal methods (this problem is also discussed in [ 20 ] in the context of CS). Therefore, one must develop some mixture of a introductory formal logic together with introduction to formal methods relevant for the IS domain. In what follows we briefly survey previous reflections on the content of logic and formal methods courses that practitioners really need and their integration into the curricula, and propose how to adapt the proposed ideas for the context of IS.
  § 2.1 Previous Proposals: Recently there has been an ongoing discussion on whether the traditional logic syllabus for CS is relevant for practitioners. Since our main goal in this paper is to extend and adapt this discussion to the context of IS, we start by briefly outlining some relevant proposals (mostly in the context of CS), the ideas of which are close in spirit to the vision we present below. In his paper “From Hilbert to a Logic Toolbox” [ 13 ] , J. [...]
  § 4 Summary and Future Research: There has recently been a discourse on the relevance of traditional logic courses to future computer science practitioners. Jeannette Wing writes in [ 19 ] : “…we still face the educational challenge of teaching mathematical foundations like logic and discrete mathematics to practicing or aspiring software engineers. We need to go beyond giving the traditional courses and think about who the target students are. ” This paper discusses these issues for the target population of IS students, for whom the lack of direct relevance of the traditional logic courses seems to have led to their exclusion from the curriculum. We believe logic is central to IS objectives, as it is the key to applying formal methods in specification, verification and validation of information systems. Ideally, we need more empirical evidence in the spirit of the Beseme project ( [ 1 ] ) that such courses are useful for IS practitioners. In addidion, there is a need for a wider discussion on what logical background is needed for Information Systems practitioners and how it should be taught. [...]
[6] arXiv:1804.08897v4 | Logic of left variable inclusion and Plonka sums of matrices
  The paper aims at studying, in full generality, logics defined by imposing a variable inclusion condition on a given logic $\vdash$. It turns out that the algebraic counterpart of the variable inclusion companion of a given logic $\vdash$ is obtained by constructing the Plonka sum of the matrix models of $\vdash$. This association allows to obtain a Hilbert-style axiomatization of the logics of va
  Full text (https://arxiv.org/html/1804.08897v4), excerpts of its own sections:
  § 1. introduction: It is always possible to associate with an arbitrary propositional logic $\vdash$ , two new substitution-invariant consequence relations $\vdash^{l}$ and $\vdash^{r}$ , which satisfy respectively a left and a right variable inclusion principle , as follows: $\Gamma\vdash^{l}\varphi\Longleftrightarrow\text{ there is }\Delta\subseteq\Gamma\text{ s.t. }\mathnormal{V\mkern-2.40001muar}(\Delta)\subseteq\mathnormal{V\mkern-2.40001muar}(\varphi)\text{ and }\Delta\vdash\varphi,$ and $\Gamma\vdash^{r}\varphi\iff\left\{\begin{array}[]{ll}\Gamma\vdash\varphi\ \text{and}\ \mathnormal{V\mkern-2.40001muar}(\varphi)\subseteq\mathnormal{V\mkern-2.40001muar}(\Gamma),\text{ or}\\ \Sigma\subseteq\Gamma,\text{ with $\Sigma$ a set of inconsistency terms for $\vdash$.}\\ \end{array}\right.$ Accordingly, we say that the logics $\vdash^{l}$ and $\vdash^{r}$ are, respectively, the left and the right variable inclusion companions of $\vdash$ , sometimes also referred to as contaiment logics . Prototypical examples of variable inclusion companions are found in the realm of three-valued logics. [...]
  § Abstract Algebraic Logic: For standard background on universal algebras and abstract algebraic logic we refer the reader respectively to [ 1 , 14 , 24 , 48 ] and [ 4 , 5 , 6 , 22 , 28 , 29 , 30 , 63 ] . In this paper, algebraic languages are assumed not to contain constant symbols. Moreover, unless stated otherwise, we work within a fixed but arbitrary algebraic language. We denote algebras by ${\mathbf{A}},{\mathbf{B}},{\mathbf{C}}\dots$ respectively with universes $A,B,C\dots$ A class of algebras is a variety if is axiomatized by equations. Given a class of algebras $\mathsf{K}$ , we denote by $\mathbb{V}(\mathsf{K})$ the variety generated by $\mathsf{K}$ . Let $\mathbf{Fm}$ be the algebra of formulas built up over a countably infinite set $\mathnormal{V\mkern-2.40001muar}$ of variables. Given a formula $\varphi\in Fm$ , we denote by $\mathnormal{V\mkern-2.40001muar}(\varphi)$ the set of variables really occurring in $\varphi$ . Similarly, given $\Gamma\subseteq Fm$ , we set $\mathnormal{V\mkern-2.40001muar}(\Gamma)=\bigcup\{\mathnormal{V\mkern-2.40001muar}(\gamma)\colon\gamma\in\Gamma\}. [...]
  § Płonka sums: For standard information on Płonka sums we refer the reader to [ 52 , 51 , 53 , 59 ] . A semilattice is an algebra ${\mathbf{A}}=\langle A,\lor\rangle$ , where $\lor$ is a binary commutative, associative and idempotent operation. Given a semilattice ${\mathbf{A}}$ and $a,b\in A$ , we set $a\leq b\Longleftrightarrow a\lor b=b.$ It is easy to see that $\leq$ is a partial order on $A$ . Definition 5 . A directed system of algebras consists of: (1) a semilattice $I=\langle I,\lor\rangle$ ; (2) a family of algebras $\{{\mathbf{A}}_{i}:i\in I\}$ with disjoint universes; (3) a homomorphism $f_{ij}\colon{\mathbf{A}}_{i}\to{\mathbf{A}}_{j}$ , for every $i,j\in I$ such that $i\leq j$ ; moreover, $f_{ii}$ is the identity map for every $i\in I$ , and if $i\leq j\leq k$ , then $f_{ik}=f_{jk}\circ f_{ij}$ . Let $X$ be a directed system of algebras as above. The Płonka sum of $X$ , in symbols ${\mathcal{P}}_{\textit{\l}}(X)$ or ${\mathcal{P}}_{\textit{\l}}({\mathbf{A}}_{i})_{i\in I}$ , is the algebra defined as follows. [...]
  § 3. The left variable inclusion companion of a logic: The definition of directed system can be extended, as follows, to logical matrices: Definition 8 . A directed system of matrices consists of: (1) a semilattice $I=\langle I,\lor\rangle$ ; (2) a family of matrices $\{\langle{\mathbf{A}}_{i},F_{i}\rangle\}_{i\in I}$ with disjoint [...]
[7] arXiv:0805.3521v4 | Towards applied theories based on computability logic
  Computability logic (CL) (see http://www.cis.upenn.edu/~giorgi/cl.html) is a recently launched program for redeveloping logic as a formal theory of computability, as opposed to the formal theory of truth that logic has more traditionally been. Formulas in it represent computational problems, "truth" means existence of an algorithmic solution, and proofs encode such solutions. Within the line of re
  Full text (https://arxiv.org/html/0805.3521v4), excerpts of its own sections:
  § 1 Introduction: Computability logic (CL) is a semantical platform and program for redeveloping logic as a formal theory of computability, as opposed to a formal theory of truth which logic has more traditionally been. It sees formulas as interactive computational problems viewed as games played by a machine ( $\top$ ) against the environment ( $\bot$ ), where logical operators stand for operations on games and “truth” is understood as existence of an algorithmic winning strategy. Numerous papers [ 1 ] - [ 14 ] have been published on this subject in recent years, and the present reader is assumed to be familiar with the basic philosophy, motivations and techniques of CL. Otherwise, he or she is recommended to take a look at the first 10 sections of [ 13 ] for an introduction and survey. So far all technical efforts within the CL project have been focused on developing CL as a pure logic, typically through constructing axiomatizations for various fragments of it. The contribution presented in the first part of this paper is in the same style. [...]
  § 2 The dfb-reduction operation, informally: As noted, the reader is assumed to be familiar with the basics of CL. Any unknown or forgotten terms and symbols used here can be looked up in [ 13 ] , which comes with a convenient glossary. 1 1 1 The glossary for the published version of [ 13 ] is given at the end of the book (rather than article ), on pages 371-376. The reader may instead use the preprint version of [ 13 ] , available at http://arxiv.org/abs/cs.LO/0507045 The latter includes both the main text and the glossary. Consider the problem $\mbox{\large$\sqcap$}x\mbox{\large$\sqcup$}y(y=x^{2})$ . Anyone who knows the definition of $x^{2}$ (but perhaps does not know the definition of $x\times y$ , or is unable to compute the multiplication function for whatever reason) would be able to solve the following problem, as it is about reducing the consequent to the antecedent: $\mbox{\large$\sqcap$}z\mbox{\large$\sqcap$}u\mbox{\large$\sqcup$}v(v=z\times u)\ \hskip 2.0pt\mbox{\small$\rightarrow$}\hskip 2.0pt\ \mbox{\large$\sqcap$}x\mbox{\large$\sqcup$}y(y=x^{2}).$ (1) A machine’s winning strategy for the above goes like this. [...]
  § 3 Dfb-reduction and a few other concepts defined formally: Remember from [ 13 ] that a constant game is a pair $A=(\mbox{\bf Lr}^{A},\mbox{\bf Wn}^{A})$ , where $\mbox{\bf Lr}^{A}$ is the set of legal runs of $A$ and $\mbox{\bf Wn}^{A}$ is a function telling us which player ( $\top$ or $\bot$ ) has won a given run. Further remember that the letter $\wp$ is always used as a variable for players, and $\overline{\wp}$ (sometimes written as $\mbox{\small$\neg$}\wp$ ) means $\wp$ ’s adversary. We also remind the reader the definition of the operation of prefixation: Definition 3.1 Let $A$ be a constant game and $\Phi$ a legal position of $A$ . The game $\langle\Phi\rangle A$ is defined by: $\mbox{\bf Lr}^{\langle\Phi\rangle A}=\{\Gamma\ |\ \langle\Phi,\Gamma\rangle\in\mbox{\bf Lr}^{A}\}$ ; $\mbox{\bf Wn}^{\langle\Phi\rangle A}\langle\Gamma\rangle=\mbox{\bf Wn}^{A}\langle\Phi,\Gamma\rangle$ . We say that a constant game $A$ is finite-depth iff there is an integer $d$ such that no legal run of $A$ contains more than $d$ (lab)moves. The smallest of such integers $d$ is called the depth of $A$ . An elementary game is a game of depth $0$ . [...]
  § 4 Block-move machines: As always, we agree that the term “ computational problem ”, or simply “ problem ”, is a synonym of “static game” (see Section 12 for a definition). [...]
[8] arXiv:1907.03265v4 | A Neutral Temporal Deontic STIT Logic
  In this work we answer a long standing request for temporal embeddings of deontic STIT logics by introducing the multi-agent STIT logic TDS. The logic is based upon atemporal utilitarian STIT logic. Yet, the logic presented here will be neutral: instead of committing ourselves to utilitarian theories, we prove the logic TDS sound and complete with respect to relational frames not employing any uti
  Full text (https://arxiv.org/html/1907.03265v4), excerpts of its own sections:
  § 1 Introduction: With the increasing integration of automated machines in our everyday lives, the development of formal decision-making tools, which take into account moral and legal considerations, is of critical importance  [ 2 , 9 , 10 ] . Unfortunately, one of the fundamental hazards of incorporating ethics into decision-making processes, is the apparent incomparability of quantitative and qualitative information—that is, moral problems most often resist quantification [ 16 ] . In contrast, utility functions are useful quantitative tools for the formal analysis of decision-making. Initially formulated in [ 5 ] , the influential theory of utilitarianism has promoted utility calculation as a ground for ethical deliberation : in short, those actions generating highest utility, are the morally right actions. For this reason, utilitarianism has proven itself to be a fruitful approach in the field of formal deontic reasoning and multi-agent systems (e.g. [ 1 , 12 , 15 ] ). [...]
  § 2 A Neutral Temporal Deontic STIT Logic: In this section, we introduce the language, semantics, and axiomatization of the temporal deontic STIT logic $\mathsf{TDS}$ . In particular, we provide neutral relational frames characterizing the logic, which omit mention of specific utility functions. The logic will bring together atemporal deontic STIT logic, presented in [ 15 ] , and the temporal STIT logic from [ 14 ] . Definition 1 (The Language $\mathcal{L}_{\mathsf{TDS}}$ ) Let $Ag=\{1,2,...,n\}$ be a finite set of agent labels and let $Var=\{p_{1},p_{2},p_{3}...\}$ be a countable set of propositional variables. The language $\mathcal{L}_{\mathsf{TDS}}$ is given by the following BNF grammar: $\phi::=p\ |\ \lnot\phi\ |\ \phi\land\phi\ |\ \Box\phi\ |\ [i]\phi\ |\ [Ag]\phi\ |\ \mathsf{G}\phi\ |\ \mathsf{H}\phi\ |\ \otimes_{i}\phi$ where $i\in Ag$ and $p\in Var$ . The logical connectives disjunction $\lor$ , implication $\rightarrow$ , and bi-conditional $\leftrightarrow$ are defined in the usual way. Let $\bot$ be defined as $p\land\lnot p$ and define $\top$ to be $p\lor\lnot p$ . [...]
  § 3 Soundness and Completeness of $\mathsf{TDS}$: In this section, we prove that $\mathsf{TDS}$ is sound and complete relative to the class of $\mathsf{TDS}$ -frames. In the next section, we show how such frames are transformable into frames employing utility assignments. This allows one to model and reason about utilitarian scenarios in a more fine-grained manner, while obtaining completeness of the logic without commitment to particular utility functions. [...]
  § 5 Conclusion and Future Work: In this paper, we extended deontic STIT logic [ 15 ] to the temporal setting, incorporating the logic from [ 14 ] . In doing so, we answered a long standing open question for temporal embeddings of deontic STIT (e.g. see [ 4 , 12 , 15 ] ). We showed that the resulting logic $\mathsf{TDS}$ is sound and complete with respect to its class of frames. We dubbed these frames neutral since they allowed us to obtain adequacy of the calculus, while allowing us to refrain from committing to specific utility functions. Subsequently, we showed how these neutral frames can be transformed into particular utilitarian models, while preserving truth. We also briefly argued that in a temporal setting, binary value assignments to histories can generate undesirable behavior with respect to contrary-to-duty obligations. For future work, we leave open the problem of whether temporal STIT (from [ 14 ] ) and its deontic extension $\mathsf{TDS}$ are decidable. [...]
[9] QNFO: Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum | https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista
  Mixed cohorts of computer‑science, mathematics, and philosophy students face fragmented curricula that either overload or under‑serve particular backgrounds, raising instructional cost and reducing learning coherence. Existing work on the LogiKEy methodology supplies a unified metalogic but lacks explicit quantitative checkpoints that justify transitions between object logics. This paper combines 
  Full text (https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista), excerpts of its own sections:
  § 5. Results: All quantitative statements below follow directly from the derivations in Section 4; the single projection (R7) is explicitly labelled. - **R1.** Propositional space for $n=3$ islanders: $2^{3}=8$ assignments, $1$ survivor; for $n=10$: $2^{10}=1\,024$ assignments (Section 4.1). - **R2.** Modal accessibility relations: $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary; $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive (Section 4.2). - **R3.** Wise Men / muddy‑children collapse: $8\to7\to6\to4$ (shrinkage factor $7/4=1.75$ from the first announcement onward); eight‑agent analogue starts at $2^{8}=256$ worlds and collapses analogously (Section 4.3). - **R4.** Boolos proof‑length tower: $L_{5}\approx10^{19\,728}$; first‑order interpretation space $2^{100}\approx1.27\times10^{30}$ (Section 4.4). - **R5.** Deontic fulfillment profiles: $2^{2}=4$ for $m=2$ obligations; $2^{3}=8$ for three obligations (Section 4.5). [...]
  § 6. Summary of the examples: * The left‑variable‑inclusion definition from [6] yields a truth‑table size of $2^{5}=32$ for a five‑variable formula, establishing the automation threshold. * The same exponent counts the admissible subsets of premises, reinforcing the combinatorial pressure. * The S5 epistemic model for three worlds admits $B_{3}=5$ equivalence relations, a number that grows rapidly with $|W|$. * The philosophical recommendation of [4] translates into a minimal three‑hour module, directly informing the hour allocation in Section 4.7. * A projection for a seven‑variable formula predicts $2^{7}=128$ rows, justifying the need for tool support beyond this point. These worked calculations demonstrate how the abstract combinatorial scaffolding of the LogiKEy curriculum can be turned into concrete, numerically grounded teaching decisions.
  § 11.3 Minimal next experiment: A minimal pilot would consist of a single semester segment covering Stage 2 (modal upgrade). The pilot would record whether students can manually enumerate all $2^{64}$ candidate relations for $|W|=8$ (expected to be infeasible) versus relying on Isabelle/HOL’s model finder. A falsifying outcome would be successful manual enumeration, contradicting the claim that the space is infeasible without automation. A companion pilot for Stage 3 would implement the sequential announcement model and check whether the implemented trajectory matches $8\to7\to6\to4$; any other trajectory under the sequential convention would refute R3.
  § 12. Conclusion: By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space by roughly $2.3\times10^{18}$‑fold, that sequential public‑announcement dynamics shrink the Wise Men model along the trajectory $8\to7\to6\to4$ with shrinkage factor $1.75$, that higher‑order reasoning collapses astronomically large first‑order interpretation spaces, and that deontic and ontological arguments reside in modest, exhaustively searchable subspaces. The course‑time projection links these checkpoints to practical scheduling, and the extensions to variable‑inclusion and computability logics demonstrate that the same exponential scaffolding applies across a broad spectrum of object logics. [...]