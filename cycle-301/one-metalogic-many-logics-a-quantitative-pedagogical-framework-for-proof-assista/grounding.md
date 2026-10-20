# Grounding block - source: rem-rev-f48d1ed7-8e46-46d6-88ee-460bcb439199

## Research idea

Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics; through these semantical embeddings a single proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes one environment in which studen... Source: https://arxiv.org/abs/2610.08214v1 (arxiv-logic-philosophy, arXiv math.LO + cs.LO + physics.hist-ph + math.HO (logic, history and philosophy of physics and mathematics)). Why it fits: epistem.

Post-publication revision of the published paper "One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The Wise Men trajectory: the abstract states '8→7→6→5→4, a shrinkage factor of 8/4=2', but Section 4.3 and Result R3 state the trajectory '8→7→6→4' with shrinkage factor '7/4=1.75'. (confirmed by a second model)
2. Section 4.3 claims 'a public announcement is modelled by an action model with |E|=1, so the updated model size is |W|×|E|', immediately after reporting the model shrinking from 8 to 7 under the king's announcement. (confirmed by a second model)

## Existing paper under revision (remediation only)

# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy

## Abstract

Teaching logic to mixed cohorts of computer‑science, mathematics, and philosophy students is costly because each cohort brings distinct expectations and because curricula traditionally fragment into separate courses on propositional, modal, epistemic, and deontic logic. The specific gap addressed here is the lack of a quantitative account of why each pedagogical transition in the LogiKEy sequence is forced. The approach combines semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each stage. The principal results are: (1) the propositional stage admits $2^{3}=8$ assignments with a single survivor; (2) the modal re‑modeling yields $2^{64}\approx1.84\times10^{19}$ arbitrary accessibility relations (or $2^{56}\approx7.21\times10^{16}$ reflexive ones); (3) the Wise Men dynamic epistemic model follows the trajectory $8\to7\to6\to5\to4$, a shrinkage factor of $8/4=2$; (4) Boolos’s curious inference generates a proof‑length tower reaching $L_{5}\approx10^{19\,728}$; (5) a first‑order interpretation space of size $2^{100}\approx1.27\times10^{30}$ contrasts with a higher‑order comprehension‑constrained search; (6) deontic combinatorics remain at $2^{m}$ profiles while consistency changes structurally; (7) Gödel’s ontological argument reduces to $2^{5}=32$ raw positivity‑predicate interpretations and at least $2^{2}=4$ consistent ones; (8) a course‑time projection allocates $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours to the six stages. These numbers turn pedagogical motivations into explicit quantitative checkpoints, thereby clarifying when automation, richer semantics, or higher‑order reasoning become indispensable.

## 1. Introduction

A logic classroom that contains only computer‑science students can assume comfort with formalism and an interest in verification; a classroom that contains only philosophy students can assume interest in argument analysis but not in type theory. A mixed classroom—computer‑science, mathematics, and philosophy students together—inherits all of the difficulties and none of the homogeneity. Two failure modes are common. The first is fragmentation: each logic (propositional, modal, epistemic, deontic) is taught as a separate subject with separate notation, separate tools, and separate exercises, so students leave with a portfolio of disconnected techniques rather than a unified competence. The second is monotony: a single logic (usually classical first‑order) is taught as if it exhausted the field, leaving philosophy students without the non‑classical logics their discipline demands and computer‑science students without the modelling resources (agents, knowledge, obligation, action) their discipline increasingly uses.

The LogiKEy methodology proposes a third way: logico‑pluralism on a single technical substrate. Classical higher‑order logic (HOL) serves as a universal metalogic. Each object logic—classical or non‑classical—is encoded by defining its semantics in HOL: possible worlds become HOL individuals, accessibility relations become HOL relations on those individuals, modal operators become HOL functions quantifying over worlds. Through such semantical embeddings, one proof assistant (e.g. Isabelle/HOL) becomes a single laboratory in which students define logics, prove their metatheorems, and compare their expressive power. The graded sequence of classroom examples—liars‑and‑truth‑tellers puzzles, the Wise Men puzzle, Boolos’s curious inference, Chisholm’s paradox, and Gödel’s ontological argument—illustrates how each representational upgrade expands a measurable quantity (search space size, model‑enumeration burden, proof‑length) and thereby forces a pedagogical transition.

The contributions of this paper are:

* **C1.** Derivation of the exact propositional assignment space and survivor count for the liars‑and‑truth‑tellers puzzle (Section 4.1, Result R1).  
* **C2.** Computation of the number of arbitrary and reflexive accessibility relations for the modal re‑modeling (Section 4.2, Result R2).  
* **C3.** Quantitative analysis of the Wise Men dynamic epistemic model trajectory (Section 4.3, Result R3).  
* **C4.** Construction of the proof‑length tower for Boolos’s curious inference and comparison with first‑order interpretation counts (Section 4.4, Result R4).  
* **C5.** Enumeration of deontic fulfillment profiles and identification of the structural nature of the paradox (Section 4.5, Result R5).  
* **C6.** Calculation of the positivity‑predicate interpretation space for Gödel’s ontological argument (Section 4.6, Result R6).  
* **C7.** Projection of course‑time allocation under explicit assumptions (Section 4.7, Result R7).  
* **C8.** Presentation of the quantitative contrast factor between the propositional and modal stages (Section 5, Result R8).

## 2. Background and Related Work

The LogiKEy methodology itself is presented in [1] and [2], which report more than a decade of use in courses, summer schools, and tutorials. [1] makes the pedagogical case for proof assistants in the logic classroom and presents the graded sequence of examples from the liars‑and‑truth‑tellers puzzle through Gödel’s ontological argument; [2] reports that the LogiKEy methodology has been used for more than a decade in courses, summer schools and tutorials, employing classical HOL as a universal metalogic in which object logics are encoded by defining their semantics, so that one proof assistant becomes a single environment for learning and comparing logics. The present work accepts this framework and adds explicit quantitative checkpoints to each transition.

On the question of *what* to teach, [3] presents four authors’ speculations on the future of mathematical logic in the twenty‑first century across recursion theory, proof theory, model theory, and set theory. Its emphasis on proof theory and logic for computer science as driving areas supports the LogiKEy bet that proof‑assistant literacy is a transferable skill rather than a specialist niche, and its picture of porous boundaries between logic and computer science supports exposing students to multiple logics in one course.

On the teaching of modal logic specifically, [4] argues for an agenda motivated by central problems of philosophy and language rather than by mathematical issues alone. This is directly relevant to the LogiKEy sequence: the transition from propositional to modal logic in [1] is driven by a puzzle about truth‑telling and knowledge, not by Kripke completeness theorems, in line with [4]’s recommendation that philosophical motivation lead. The quantitative state‑space analysis provided here gives philosophy students a concrete handle on why modal operators are needed while preserving the philosophical motivation identified in [4].

The problem of heterogeneous student populations is studied in [5], which examines teaching logic to information‑systems students and argues that, rather than excluding logic from their curriculum, contents and methodology must be significantly adapted to practitioner needs. The LogiKEy methodology can be read as one systematic answer to [5]’s challenge: the adaptation is not a watered‑down syllabus but a uniform tool‑based environment in which students with different backgrounds enter through different object logics.

An alternative re‑foundation of logic is computability logic, presented in [7] as a formal theory of computability—formulas as interactive computational problems modeled as games, truth as existence of a winning algorithmic strategy. Its development into applied theories is carried forward in [8]. Computability logic illustrates the space of proposals against which the LogiKEy choice of HOL‑as‑metalogic must be measured: where computability logic changes what the logical operators mean, LogiKEy keeps the metalogic fixed and varies the embedded semantics. A course built on LogiKEy could in principle embed a game‑semantics of the [6], [8] style as one more object logic, which is itself evidence for the flexibility of the HOL substrate.

Genuine logical pluralism inside the algebraic tradition is exemplified by [6], which studies logics defined by imposing a variable‑inclusion condition on a given consequence relation $\vdash$, showing that the algebraic counterpart is obtained by Plonka sums of matrix models and yielding Hilbert‑style axiomatizations. Such non‑classical consequence relations are exactly the kind of object logic that the semantical‑embedding approach can host: a matrix semantics is a set‑theoretic structure, hence definable in HOL.

The deontic stage of the LogiKEy sequence connects to [9], which introduces the neutral temporal deontic STIT logic TDS, proving soundness and completeness with respect to relational frames without utilitarian commitments. [9] demonstrates that deontic logic remains an active research frontier with new modelling resources (agency, time); a LogiKEy‑style course can present TDS as a further embedding, showing students that the sequence they climbed does not end at dyadic deontic logic.

Collectively, these works motivate a systematic quantitative study of proof‑assistant‑based logic teaching, situating the contribution within an emerging research agenda.

## 3. Methods

### 3.1 Semantical embeddings in HOL

Fix classical HOL with a domain of possible worlds (a HOL type $w$). An object modal logic with box operator is embedded by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v
$$

where $r : w \to w \to \mathbb{B}$ is a HOL relation and $\varphi : w \to \mathbb{B}$ is a HOL predicate on worlds. Different constraints on $r$ (serial, reflexive, transitive, Euclidean, equivalence) yield different object logics (D, T, S4, S5), all inside the same metalogic. Epistemic logic adds an agent index: $r_{a}$ for each agent $a$ from a finite set $A$, with knowledge $K_{a}\varphi = \Box_{r_{a}}\varphi$; under S5 constraints each $r_{a}$ is an equivalence relation partitioning $W$. Dynamic epistemic logic adds event models acting on the current model: a factual model of size $|W|$ updated by an action model of size $|E|$ yields a product model of size $|W|\cdot|E|$. Deontic logic replaces worlds‑with‑obligation by either a deontic accessibility $r_{\text{ob}}$ (standard) or a dyadic conditional $\mathcal{O}(\psi\mid\varphi)$ selecting ideal $\varphi$‑worlds (dyadic). None of this requires new tooling: each definition is a HOL constant, each metatheorem a HOL theorem, each counter‑model a HOL‑computable structure.

### 3.2 Method of this paper

The method is combinatorial analysis of the LogiKEy example sequence [1], [2]. For each curricular stage the representational choice is identified, the associated search or model space is defined, and its cardinality is computed exactly from stated inputs. For each stage a quantitative invariant that (i) can be computed exactly from stated inputs by elementary arithmetic, and (ii) exhibits the limitation that motivates the transition to the next logic is extracted. Every claim in Section 5 is restricted to numbers derived in Section 4; where extrapolation beyond the computation occurs, the claim is labeled a projection with its assumptions stated. No empirical learning outcomes or prover timings are reported, because none are computed here; the claims are purely combinatorial.

## 4. Analysis

### 4.1 Stage 1: Liars and truth‑tellers — exhaustive consistency in propositional logic

**Input (from the puzzle structure of [1]).** Three islanders $a,b,c$; each is either a truth‑teller ($T$) or a liar ($L$). Statements: $a$ says “$b$ is a truth‑teller”; $b$ says “$a$ and $c$ are of different types”; $c$ says “$a$ is a liar”. Consistency condition: an islander of type $T$ asserts only truths; an islander of type $L$ asserts only falsehoods.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The three consistency constraints are

$$
x_{a} = (x_{b}=T),\qquad
x_{b} = (x_{a}\neq x_{c}),\qquad
x_{c} = (x_{a}=L).
$$

**Exhaustive check.** The search space has $2^{3}=8$ assignments. Evaluation yields exactly one survivor, $(x_{a},x_{b},x_{c})=(T,T,L)$. The elimination rate is $7/8=0.875$.

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space already contains $2^{10}=1024$ rows, which exceeds feasible manual checking.

### 4.2 Stage 2: The modal upgrade — counting accessibility relations

**Input.** The same puzzle re‑modelled with $|W|=8$ worlds (one per propositional assignment) and a single epistemic agent (the puzzle solver). The number of distinct binary accessibility relations on a set of $|W|$ worlds is

$$
2^{|W|\cdot|W|}=2^{8\times8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
$$

If reflexivity is imposed (standard for knowledge), the diagonal pairs are fixed, leaving $8\times7=56$ off‑diagonal pairs, so

$$
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}
$$

reflexive relations.

### 4.3 Stage 3: The Wise Men puzzle — model dynamics under public announcement

**Input.** Three agents $a,b,c$; each wears a black ($B$) or white ($W$) hat; each sees the others’ hats but not its own; the king publicly announces “at least one hat is black”. All three hats are in fact black. Knowledge is S5.

**Model sizes.** Initial world set $W_{0}$ has $2^{3}=8$ worlds. The king’s announcement eliminates the all‑white world, leaving $|W_{1}|=7$. Agent $a$’s “I don’t know” announcement eliminates the world $WWB$, yielding $|W_{2}|=6$. Agent $b$’s analogous announcement eliminates $BBW$ and $WBW$, yielding $|W_{3}|=4$. The trajectory is

$$
8\;\to\;7\;\to\;6\;\to\;4,
$$

a shrinkage factor of $7/4=1.75$ from the first announcement onward. In dynamic epistemic logic (DEL) a public announcement is modelled by an action model with $|E|=1$, so the updated model size is $|W|\times|E|$. By contrast, an action model with $|E|=3$ events over the original $8$ worlds would yield $8\times3=24$ worlds, illustrating that DEL can both shrink and grow models.

### 4.4 Stage 4: Boolos’s curious inference — what a higher‑order metalogic buys

**Input.** Boolos’s curious inference is a first‑order argument whose proof length $L_{n}$ satisfies the recurrence

$$
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
$$

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

**First‑order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is

$$
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}.
$$

A propositional instantiation with $k=10$ atoms yields $2^{10}=1\,024$ rows. The contrast between $2^{100}\approx10^{30}$ first‑order interpretations and the short higher‑order proof illustrates what a higher‑order metalogic buys.

### 4.5 Stage 5: Deontic combinatorics (Chisholm’s paradox)

**Input.** Chisholm’s paradox involves $m=2$ obligations. Each obligation can be fulfilled or violated, giving $2^{m}=4$ fulfillment profiles. A three‑obligation variant yields $2^{3}=8$ profiles. The paradox is not a growth problem (the space stays at $2^{m}$) but a consistency problem: the standard monotonic deontic operator $O$ forces inconsistency, whereas the dyadic operator $O(B\mid A)$ reorganises the same four profiles into conditional commitments, restoring consistency.

### 4.6 Stage 6: Axiomatic commitments (Gödel’s ontological argument)

**Input.** Gödel’s ontological argument, as embedded in the LogiKEy sequence, posits a positivity predicate $P$ over a universe of $p=5$ candidate properties and $a=3$ core axioms. The raw interpretation space for $P$ is

$$
2^{p}=2^{5}=32.
$$

Assuming each axiom is independent and halves the space, the consistent set has size at least

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

Thus the research‑level argument reduces to a small, exhaustively searchable space.

### 4.7 Course‑time projection (labeled projection)

Assumption set (explicit): a semester course of $T_{\text{sem}}=14$ weeks with one $2$‑hour session per week gives $14\times2=28$ contact hours. The six stages are allocated in the ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$, total weight $20$. Each weight unit corresponds to

$$
\frac{28}{20}=1.4\ \text{hours}.
$$

Consequently the stage allocations are

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

The sum check $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ hours holds.

## 5. Results

All values below are computed in Section 4 with shown arithmetic; the single projection (R7) is labeled as such.

* **R1.** The propositional state space for $n=3$ islanders is $2^{3}=8$ assignments, of which exactly $1$ survives the three consistency constraints (elimination rate $7/8=0.875$); for $n=10$ islanders the raw space is $2^{10}=1\,024$ (Section 4.1).

* **R2.** The modal re‑modeling over $|W|=8$ worlds admits $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary accessibility relations, or $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive ones (Section 4.2).

* **R3.** The Wise Men factual model follows the trajectory $8\to7\to6\to4$ under the king’s announcement and two ignorance announcements, a shrinkage factor of $7/4=1.75$; a DEL action model with $|E|=3$ events over the original $8$ worlds yields $8\times3=24$ worlds (Section 4.3).

* **R4.** Boolos’s curious inference generates a proof‑length tower $L_{1}=2$, $L_{2}=4$, $L_{3}=16$, $L_{4}=65\,536$, $L_{5}\approx10^{19\,728}$; a first‑order encoding with domain size $d=10$ and one binary predicate presents $2^{100}\approx1.27\times10^{30}$ candidate interpretations, versus $2^{10}=1\,024$ propositional rows (Section 4.4).

* **R5.** Chisholm’s paradox with $m=2$ obligations has $2^{2}=4$ fulfillment profiles; a three‑obligation variant has $2^{3}=8$ profiles. The paradox is structural (consistency) rather than combinatorial (size) (Section 4.5).

* **R6.** Gödel’s ontological argument over a $p=5$‑property universe has $2^{5}=32$ raw interpretations of the positivity predicate $P$, reduced to at least $2^{5-3}=4$ consistent interpretations under three independent axioms (Section 4.6).

* **R7 (projection).** Under the stated assumptions of Section 4.7, the six stages receive $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours respectively; uncertainty is dominated by the assumed ratio, which is not empirically validated (Section 4.7).

* **R8.** The quantitative contrast between the propositional and modal stages is

$$
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18},
$$

showing that the modal upgrade expands the search space by roughly $2.3\times10^{18}$‑fold.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Islander puzzle structure (three agents, fixed statements) | Results scale exponentially with the number of agents; the exact survivor count changes with alternative statements. |
| World set size $|W|=8$ derived from the propositional stage | Larger propositional spaces would increase $|W|$ and thus the accessibility‑relation count $2^{|W|^{2}}$ dramatically. |
| Reflexivity constraint only (no transitivity, etc.) | Imposing additional constraints (e.g., symmetry) would reduce the relation count further; the presented numbers are upper bounds for the given constraints. |
| S5 epistemic assumptions (equivalence relations) | Weakening to KD45 would alter the number of admissible relations; the current count assumes full equivalence. |
| Boolos proof‑length recurrence $L_{n+1}=2^{L_{n}}$ | The recurrence captures the worst‑case growth; alternative proof‑search strategies could yield smaller lengths. |
| Independence of Gödel axioms | If axioms are not independent, the reduction factor $2^{p-a}$ would be an over‑estimate of the consistent space. |
| Course‑time ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$ | Different pedagogical emphases would change the hour allocation; the projection is sensitive to this ratio. |
| No empirical validation of the ratios or of student performance | The quantitative checkpoints are necessary but not sufficient for pedagogical success. |

### 6.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students successfully solve the modal stage puzzles without any assistance from a model‑finder, despite the computed space of $2^{64}\approx10^{19}$ candidate relations. Such an outcome would indicate that the combinatorial model over‑estimates the effective search burden, thereby falsifying the claim that the modal upgrade is forced by sheer state‑space size.

Another falsification condition is the discovery that the Wise Men ignorance announcements do not reduce the model size from $7$ to $4$ in a concrete implementation (e.g., because agents’ knowledge is modelled differently). This would contradict the derived shrinkage factor $1.75$ and challenge the quantitative justification for introducing dynamic epistemic logic.

### 6.3 Open questions

* How do alternative semantical‑embedding choices (e.g., deep embeddings) affect the combinatorial counts?  
* What is the impact of richer action models (larger $|E|$) on the trade‑off between model growth and expressive power?  
* Can automated proof‑search heuristics mitigate the exponential blow‑up identified for Boolos’s inference, and how would that affect the pedagogical argument?  
* How robust are the course‑time projections across institutions with differing teaching loads and student backgrounds?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

The primary users are instructors of logic courses that serve mixed cohorts of computer‑science, mathematics, and philosophy students. The quantitative checkpoints inform curriculum designers when to introduce a new object logic, how much contact time to allocate, and which proof‑assistant features become essential. If the computed state‑space thresholds are respected, students are forced to rely on automated model finders or higher‑order reasoning precisely at the intended transition points, thereby reinforcing the pedagogical narrative.

### 7.2 Technology Readiness Level

The work is purely analytical and has not undergone peer review; according to NASA definitions this places the contribution at TRL 2 (technology concept formulated). No hardware, software implementation, or user testing has been performed.

### 7.3 Minimal next experiment

A minimal pilot study would consist of a single semester‑long course segment covering Stage 2 (modal upgrade). The experiment would measure whether students can manually enumerate accessibility relations for a toy world set of size $|W|=4$ (where $2^{16}=65\,536$ relations) versus relying on Isabelle/HOL’s model finder for $|W|=8$. The falsifying outcome is successful manual enumeration for $|W|=8$, which would contradict the claim that the space is infeasible without automation.

### 7.4 Engineering and deployment constraints

* **Proof‑assistant availability:** Isabelle/HOL must be installed and configured on institutional machines.  
* **Computational resources:** Model‑finding for $2^{64}$ relations requires exponential‑time algorithms; practical use relies on pruning heuristics rather than exhaustive enumeration.  
* **Pedagogical scaffolding:** Students need introductory material on HOL syntax and semantical embeddings before reaching Stage 2.  
* **Curricular scheduling:** The contact‑hour allocation derived in Section 4.7 assumes a 28‑hour semester; deviations require re‑balancing of the ratio.  
* **Assessment design:** Evaluation instruments must capture whether students understand the necessity of automation, not merely whether they obtain correct answers.

### 7.5 Order‑of‑magnitude cost projection

Assuming an institutional support cost of \$100 per contact hour (covering instructor time, software licences, and classroom resources), the projected total cost for the six stages is

$$
28\ \text{hours}\times\$100/\text{hour}= \$2{,}800,
$$

derived directly from the contact‑hour count in Section 4.7. This figure is a projection; actual costs may vary with local salary scales and infrastructure.

### 7.6 Direct risks and misuse paths

* **Over‑reliance on automation:** Students might treat the proof assistant as a black box, neglecting underlying logical reasoning. Mitigation requires explicit reflection activities.  
* **Misinterpretation of quantitative thresholds:** Instructors could present the raw numbers as absolute barriers rather than pedagogical guides, discouraging exploration of alternative reasoning strategies.  
* **Tool‑centric curriculum lock‑in:** Adoption of a single proof assistant may limit exposure to other formal methods tools; a diversified toolbox is advisable.

## 8. Conclusion

By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space from $8$ to roughly $10^{19}$ candidate relations, that dynamic epistemic updates shrink model sizes in a predictable way, that higher‑order reasoning can collapse astronomically large first‑order proof‑length towers, and that deontic and ontological arguments remain tractable when embedded in HOL. The course‑time projection further links these quantitative insights to practical curriculum planning. Together, these results provide instructors with a rigorous basis for deciding when to introduce richer logics, when to rely on automation, and how to allocate teaching resources in mixed‑cohort settings. Future work will empirically validate the proposed checkpoints through pilot implementations and explore extensions to alternative object logics such as computability logic and variable‑inclusion logics.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Discussion; Practical Implications and Engineering Pathways; Conclusion; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 13 -> 9. length 4084 -> 3982 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.7-terminal-hard-review-selfclose). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
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
[9] https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista. QNFO: One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof-Assistant-Based Logic Teaching with LogiKEy.

## Appendix A. Divergence report

*No divergent claims were identified among the independent drafts; all substantive claims converged.*

## Appendix B. Claim attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|-----------------|-----------|
| C1 | A, B | Convergent |
| C2 | A, B | Convergent |
| C3 | A, B | Convergent |
| C4 | A, B | Convergent |
| C5 | A, B | Convergent |
| C6 | A, B | Convergent |
| C7 | A, B | Convergent |
| C8 | A, B | Convergent |

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

QNFO: One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy | https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista

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
[9] QNFO: One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy | https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista
  Teaching logic to mixed cohorts of computer‑science, mathematics, and philosophy students is costly because each cohort brings distinct expectations and because curricula traditionally fragment into separate courses on propositional, modal, epistemic, and deontic logic. The specific gap addressed here is the lack of a quantitative account of why each pedagogical transition in the LogiKEy sequence 
  Full text (https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista), excerpts of its own sections:
  § 1. Introduction: A logic classroom that contains only computer‑science students can assume comfort with formalism and an interest in verification; a classroom that contains only philosophy students can assume interest in argument analysis but not in type theory. A mixed classroom—computer‑science, mathematics, and philosophy students together—inherits all of the difficulties and none of the homogeneity. Two failure modes are common. The first is fragmentation: each logic (propositional, modal, epistemic, deontic) is taught as a separate subject with separate notation, separate tools, and separate exercises, so students leave with a portfolio of disconnected techniques rather than a unified competence. The second is monotony: a single logic (usually classical first‑order) is taught as if it exhausted the field, leaving philosophy students without the non‑classical logics their discipline demands and computer‑science students without the modelling resources (agents, knowledge, obligation, action) their discipline increasingly uses. [...]
  § 5. Results: All values below are computed in Section 4 with shown arithmetic; the single projection (R7) is labeled as such. * **R1.** The propositional state space for $n=3$ islanders is $2^{3}=8$ assignments, of which exactly $1$ survives the three consistency constraints (elimination rate $7/8=0.875$); for $n=10$ islanders the raw space is $2^{10}=1\,024$ (Section 4.1). * **R2.** The modal re‑modeling over $|W|=8$ worlds admits $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary accessibility relations, or $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive ones (Section 4.2). * **R3.** The Wise Men factual model follows the trajectory $8\to7\to6\to4$ under the king’s announcement and two ignorance announcements, a shrinkage factor of $7/4=1.75$; a DEL action model with $|E|=3$ events over the original $8$ worlds yields $8\times3=24$ worlds (Section 4.3). [...]
  § 7.3 Minimal next experiment: A minimal pilot study would consist of a single semester‑long course segment covering Stage 2 (modal upgrade). The experiment would measure whether students can manually enumerate accessibility relations for a toy world set of size $|W|=4$ (where $2^{16}=65\,536$ relations) versus relying on Isabelle/HOL’s model finder for $|W|=8$. The falsifying outcome is successful manual enumeration for $|W|=8$, which would contradict the claim that the space is infeasible without automation.
  § 8. Conclusion: By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space from $8$ to roughly $10^{19}$ candidate relations, that dynamic epistemic updates shrink model sizes in a predictable way, that higher‑order reasoning can collapse astronomically large first‑order proof‑length towers, and that deontic and ontological arguments remain tractable when embedded in HOL. The course‑time projection further links these quantitative insights to practical curriculum planning. Together, these results provide instructors with a rigorous basis for deciding when to introduce richer logics, when to rely on automation, and how to allocate teaching resources in mixed‑cohort settings. Future work will empirically validate the proposed checkpoints through pilot implementations and explore extensions to alternative object logics such as computability logic and variable‑inclusion logics.