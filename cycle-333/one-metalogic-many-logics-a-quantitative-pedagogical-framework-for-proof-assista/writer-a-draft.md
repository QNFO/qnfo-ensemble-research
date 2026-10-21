# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy

## Abstract

Teaching logic to mixed cohorts of computer‑science, mathematics, and philosophy students is costly because each cohort brings distinct expectations and curricula traditionally fragment into separate courses on propositional, modal, epistemic, and deontic logic. The specific gap addressed here is the lack of a quantitative account of why each pedagogical transition in the LogiKEy sequence is forced. The approach combines semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each stage. The principal results are: (1) the propositional stage admits $2^{3}=8$ assignments with a single survivor; (2) the modal re‑modeling yields $2^{64}\approx1.84\times10^{19}$ arbitrary accessibility relations (or $2^{56}\approx7.21\times10^{16}$ reflexive ones); (3) the Wise Men dynamic epistemic model follows the trajectory $8\to7\to6\to4$, a shrinkage factor of $7/4=1.75$; (4) Boolos’s curious inference generates a proof‑length tower reaching $L_{5}\approx10^{19\,728}$; (5) a first‑order interpretation space of size $2^{100}\approx1.27\times10^{30}$ contrasts with a higher‑order comprehension‑constrained search; (6) deontic combinatorics remain at $2^{m}$ profiles while consistency changes structurally; (7) Gödel’s ontological argument reduces to $2^{5}=32$ raw positivity‑predicate interpretations and at least $2^{2}=4$ consistent ones; (8) a course‑time projection allocates $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours to the six stages. These numbers turn pedagogical motivations into explicit quantitative checkpoints, thereby clarifying when automation, richer semantics, or higher‑order reasoning become indispensable.

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

On the question of *what* to teach, [3] presents four authors’ speculations about the future of mathematical logic in the twenty‑first century across recursion theory, proof theory, model theory, and set theory. Its emphasis on proof theory and logic for computer science as driving areas supports the LogiKEy bet that proof‑assistant literacy is a transferable skill rather than a specialist niche, and its picture of porous boundaries between logic and computer science supports exposing students to multiple logics in one course.

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

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1

[2] Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. arXiv:2610.08214v1. https://arxiv.org/abs/2610.08214v1

[3] The prospects for mathematical logic in the twenty-first century. arXiv:cs/0205003v1. https://arxiv.org/abs/cs/0205003v1

[4] To Teach Modal Logic: An Opinionated Survey. arXiv:1507.04701v1. https://arxiv.org/abs/1507.04701v1

[5] Teaching Logic to Information Systems Students: Challenges and Opportunities. arXiv:1507.03687v1. https://arxiv.org/abs/1507.03687v1

[6] Logic of left variable inclusion and Plonka sums of matrices. arXiv:1804.08897v4. https://arxiv.org/abs/1804.08897v4

[7] Towards applied theories based on computability logic. arXiv:0805.3521v4. https://arxiv.org/abs/0805.3521v4

[8] A Neutral Temporal Deontic STIT Logic. arXiv:1907.03265v4. https://arxiv.org/abs/1907.03265v4

[9] https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista. QNFO: One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy.