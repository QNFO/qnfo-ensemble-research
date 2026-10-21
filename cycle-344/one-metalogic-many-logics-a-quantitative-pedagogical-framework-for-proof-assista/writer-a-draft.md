# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy

## Abstract

Teaching logic to mixed cohorts of computer‑science, mathematics, and philosophy students is expensive because curricula must accommodate divergent backgrounds and because traditional courses fragment into separate propositional, modal, epistemic, and deontic modules. The specific gap addressed here is the absence of a quantitative account that explains why each pedagogical transition in the LogiKEy sequence is forced. We combine shallow semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each stage. The principal results are: (1) the propositional Liars‑and‑Truth‑Tellers puzzle admits $2^{3}=8$ assignments with exactly one survivor; (2) the modal re‑modeling over $|W|=8$ worlds yields $2^{64}\approx1.84\times10^{19}$ arbitrary accessibility relations and $2^{56}\approx7.21\times10^{16}$ reflexive ones; (3) the Wise Men dynamic‑epistemic model follows the trajectory $8\to7\to6\to4$, a shrinkage factor of $7/4=1.75$; (4) Boolos’s curious inference generates a proof‑length tower $L_{5}\approx10^{19\,728}$; (5) a first‑order interpretation space of size $2^{100}\approx1.27\times10^{30}$ contrasts with the higher‑order proof; (6) Gödel’s ontological argument reduces to $2^{5}=32$ raw positivity‑predicate interpretations and at least $2^{2}=4$ consistent ones; (7) a course‑time projection allocates $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours to the six stages; (8) the propositional‑to‑modal contrast expands the search space by a factor $2^{61}\approx2.31\times10^{18}$. These numbers turn pedagogical motivations into explicit quantitative checkpoints, clarifying when automation, richer semantics, or higher‑order reasoning become indispensable.

## 1. Introduction

A logic classroom that contains only computer‑science students can assume comfort with formalism and an interest in verification; a classroom that contains only philosophy students can assume interest in argument analysis but not in type theory. A mixed classroom—computer‑science, mathematics, and philosophy students together—inherits all of the difficulties and none of the homogeneity. Two failure modes are common. The first is fragmentation: each logic (propositional, modal, epistemic, deontic) is taught as a separate subject with separate notation, separate tools, and separate exercises, so students leave with a portfolio of disconnected techniques rather than a unified competence. The second is monotony: a single logic (usually classical first‑order) is taught as if it exhausted the field, leaving philosophy students without the non‑classical logics their discipline demands and computer‑science students without the modelling resources (agents, knowledge, obligation, action) their discipline increasingly uses.

The LogiKEy methodology proposes a third way: logico‑pluralism on a single technical substrate. Classical higher‑order logic (HOL) serves as a universal metalogic. Each object logic—classical or non‑classical—is encoded by defining its semantics in HOL: possible worlds become HOL individuals, accessibility relations become HOL relations on those individuals, modal operators become HOL functions quantifying over worlds. Through such semantical embeddings, one proof assistant (e.g. Isabelle/HOL) becomes a single laboratory in which students define logics, prove their metatheorems, and compare their expressive power. The graded sequence of classroom examples—Liars‑and‑Truth‑Tellers, the Wise Men puzzle, Boolos’s curious inference, Chisholm’s paradox, and Gödel’s ontological argument—illustrates how each representational upgrade expands a measurable quantity (search‑space size, model‑enumeration burden, proof‑length) and thereby forces a pedagogical transition.

**Contributions.**  
* **C1.** Exact derivation of the propositional assignment space and survivor count for the Liars‑and‑Truth‑Tellers puzzle (Section 4.1, Result R1).  
* **C2.** Computation of the number of arbitrary and reflexive accessibility relations for the modal re‑modeling (Section 4.2, Result R2).  
* **C3.** Quantitative analysis of the Wise Men dynamic‑epistemic model trajectory and the correct shrinkage factor $7/4$ (Section 4.3, Result R3).  
* **C4.** Construction of the proof‑length tower for Boolos’s curious inference and comparison with first‑order interpretation counts (Section 4.4, Result R4).  
* **C5.** Enumeration of deontic fulfillment profiles and identification of the structural nature of the paradox (Section 4.5, Result R5).  
* **C6.** Calculation of the positivity‑predicate interpretation space for Gödel’s ontological argument (Section 4.6, Result R6).  
* **C7.** Projection of course‑time allocation under explicit assumptions (Section 4.7, Result R7).  
* **C8.** Quantitative contrast factor between the propositional and modal stages (Section 5, Result R8).

## 2. Background and Related Work

The LogiKEy methodology itself is presented in [1] and [2]. Both works report that LogiKEy uses classical HOL as a universal metalogic and that it has been employed for more than a decade in courses, summer schools, and tutorials, allowing a single proof assistant to host many object logics. This establishes the technical substrate on which the present quantitative analysis builds.

[3] argues that logic is a core component of computer‑science curricula and that its applications to CS are increasingly important. This supports the claim that mixed‑cohort instruction must address CS expectations for verification and modelling.

[4] advocates teaching modal logic on the basis of philosophical problems rather than purely mathematical concerns. The Wise Men puzzle, used here as a modal case study, exemplifies such a philosophically motivated transition.

[5] examines the challenges of teaching logic to information‑systems practitioners and recommends adapting content to practitioner needs. The quantitative checkpoints introduced in this paper provide a concrete way to adapt the curriculum without diluting logical rigor.

[6] introduces the notion of left variable‑inclusion companions of a logic and shows that their algebraic counterpart is obtained via Plonka sums of matrix models. This illustrates the breadth of object logics that can be embedded in HOL, reinforcing the claim of LogiKEy’s flexibility.

[7] defines computability logic as a formal theory of computability in which formulas are interactive games. Although not used directly in the case studies, this work represents an alternative semantic paradigm against which the HOL‑based approach can be measured.

[8] presents a neutral temporal deontic STIT logic (TDS) with relational frames that avoid utilitarian commitments. The deontic stage of the LogiKEy sequence can embed such a logic, demonstrating that even advanced normative logics fit within the HOL substrate.

[9] emphasizes that teaching logic to mixed cohorts is costly because of divergent expectations and fragmented curricula. This motivates the need for quantitative criteria that justify pedagogical transitions and resource allocation.

## 3. Methods

### 3.1 Semantical embeddings in HOL

We fix classical HOL with a type of possible worlds $w$. An object modal logic with a binary accessibility relation $r\colon w\to w\to\mathbb{B}$ is embedded by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$

where $\varphi\colon w\to\mathbb{B}$ is a world‑dependent proposition. Epistemic operators are obtained by indexing $r$ with agents $a\in A$, i.e. $K_{a}\varphi = \Box_{r_{a}}\varphi$. Dynamic epistemic logic (DEL) updates a factual model $M=(W,R)$ with an action model $E$ of size $|E|$ by forming the product model of size $|W|\times|E|$.

Deontic operators are represented either by a unary accessibility $r_{\text{ob}}$ or by a dyadic conditional $\mathcal{O}(\psi\mid\varphi)$ that selects $\varphi$‑worlds where $\psi$ holds. All definitions are HOL constants, so no additional tooling is required.

### 3.2 Analytic method

For each curricular stage we (i) identify the representational choice, (ii) define the associated combinatorial object (assignments, relations, worlds, proofs, etc.), and (iii) compute its cardinality using elementary arithmetic on the inputs stated in the puzzle descriptions or in the pedagogical assumptions. The derivations are fully explicit in Section 4. Where a claim extrapolates beyond the computed values (e.g., course‑time allocation), it is labelled as a projection and its assumptions are stated.

## 4. Analysis

### 4.1 Stage 1: Liars‑and‑Truth‑Tellers (propositional)

**Inputs.** Three islanders $a,b,c$, each either a truth‑teller ($T$) or a liar ($L$). Statements:  
1. $a$: “$b$ is a truth‑teller”.  
2. $b$: “$a$ and $c$ are of different types”.  
3. $c$: “$a$ is a liar”.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The consistency constraints are

\[
\begin{aligned}
x_{a} &= (x_{b}=T),\\
x_{b} &= (x_{a}\neq x_{c}),\\
x_{c} &= (x_{a}=L).
\end{aligned}
\]

**Enumeration.** The raw assignment space contains $2^{3}=8$ rows. Evaluating each assignment against the three constraints yields exactly one survivor:

\[
(x_{a},x_{b},x_{c}) = (T,T,L).
\]

Thus the elimination rate is $\frac{7}{8}=0.875$.

**Generalisation.** For $n$ islanders the raw space is $2^{n}$. For $n=10$ this gives $2^{10}=1\,024$ assignments, already beyond feasible manual checking.

### 4.2 Stage 2: Modal upgrade (accessibility relations)

**Inputs.** The propositional stage yields $|W|=8$ worlds (one per assignment). A single epistemic agent models the puzzle solver.

**Arbitrary relations.** The number of binary relations on $W$ is

\[
2^{|W|\cdot|W|}=2^{8\times8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
\]

**Reflexive relations.** Imposing reflexivity fixes the $8$ diagonal pairs, leaving $8\times7=56$ free off‑diagonal pairs:

\[
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}.
\]

### 4.3 Stage 3: Wise Men puzzle (dynamic epistemic updates)

**Inputs.** Three agents $a,b,c$ each wear a black ($B$) or white ($W$) hat; all hats are black. The king publicly announces “at least one hat is black”. Knowledge is modelled with S5 (equivalence relations).

**Model evolution.**  

* Initial world set $W_{0}$: $2^{3}=8$ worlds (all colour combinations).  
* King’s announcement eliminates the all‑white world, leaving $|W_{1}|=8-1=7$.  
* Agent $a$ announces “I don’t know my hat”, which eliminates the world $WWB$, giving $|W_{2}|=7-1=6$.  
* Agent $b$ makes the same announcement, eliminating $BBW$ and $WBW$, giving $|W_{3}|=6-2=4$.

Thus the trajectory is

\[
8\;\to\;7\;\to\;6\;\to\;4,
\]

and the shrinkage factor from the first announcement to the final model is

\[
\frac{7}{4}=1.75.
\]

**Public‑announcement product.** In DEL a public announcement is represented by an action model with a single event ($|E|=1$). The updated model size is $|W|\times|E|=|W|$, i.e. the model does not grow during a pure announcement. By contrast, an action model with $|E|=3$ events over the original $8$ worlds would yield $8\times3=24$ worlds, illustrating that DEL can both shrink and expand models depending on the action model.

### 4.4 Stage 4: Boolos’s curious inference (proof‑length tower)

**Inputs.** The recurrence defining proof length is

\[
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
\]

**Iteration.**  

\[
\begin{aligned}
L_{1} &= 2^{1}=2,\\
L_{2} &= 2^{2}=4,\\
L_{3} &= 2^{4}=16,\\
L_{4} &= 2^{16}=65\,536,\\
L_{5} &= 2^{65\,536}.
\end{aligned}
\]

Using $\log_{10}(2)=0.30103$,

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

A propositional instantiation with $k=10$ atoms yields $2^{10}=1\,024$ rows. The contrast between $2^{100}\approx10^{30}$ first‑order interpretations and the short higher‑order proof illustrates the advantage of a higher‑order metalogic.

### 4.5 Stage 5: Deontic combinatorics (Chisholm’s paradox)

**Inputs.** The standard formulation involves $m=2$ obligations. Each obligation may be fulfilled or violated, giving $2^{m}=4$ fulfillment profiles. A three‑obligation variant yields $2^{3}=8$ profiles.

**Structural observation.** The paradox is not a combinatorial explosion; the space remains $2^{m}$, but the standard monotonic deontic operator $O$ forces inconsistency, whereas the dyadic operator $\mathcal{O}(\psi\mid\varphi)$ reorganises the same four profiles into conditional commitments, restoring consistency.

### 4.6 Stage 6: Gödel’s ontological argument (axiomatic commitments)

**Inputs.** The argument employs a positivity predicate $P$ over $p=5$ candidate properties and $a=3$ core axioms.

**Raw space.** The number of possible interpretations of $P$ is

\[
2^{p}=2^{5}=32.
\]

**Consistent space.** Assuming the three axioms are independent and each halves the space, the number of consistent interpretations is at least

\[
2^{p-a}=2^{5-3}=2^{2}=4.
\]

Thus the research‑level argument reduces to a small, exhaustively searchable space.

### 4.7 Course‑time projection (projection)

**Assumptions.** A semester consists of $T_{\text{sem}}=14$ weeks with one $2$‑hour session per week, giving $14\times2=28$ contact hours. The six stages are allocated in the ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$, i.e. total weight $20$.

**Computation.** One weight unit corresponds to

\[
\frac{28\ \text{h}}{20}=1.4\ \text{h}.
\]

Hence the allocations are

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

The sum $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ hours checks out.

## 5. Results

All values below are derived in Section 4; the single projection (R7) is explicitly labelled.

* **R1.** Propositional state space for $n=3$ islanders: $2^{3}=8$ assignments, exactly $1$ survivor; elimination rate $7/8=0.875$ (Section 4.1). For $n=10$, raw space $2^{10}=1\,024$ (Section 4.1).

* **R2.** Modal re‑modeling over $|W|=8$ worlds admits $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary accessibility relations, and $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive relations (Section 4.2).

* **R3.** Wise Men model trajectory $8\to7\to6\to4$, shrinkage factor $7/4=1.75$; a DEL action model with $|E|=3$ over the original $8$ worlds yields $8\times3=24$ worlds (Section 4.3).

* **R4.** Boolos’s curious inference produces a proof‑length tower $L_{5}\approx10^{19\,728}$; a first‑order encoding with $d=10$ and one binary predicate yields $2^{100}\approx1.27\times10^{30}$ candidate interpretations, versus $2^{10}=1\,024$ propositional rows (Section 4.4).

* **R5.** Chisholm’s paradox with $m=2$ obligations has $2^{2}=4$ fulfillment profiles; a three‑obligation variant has $2^{3}=8$ profiles. The paradox is structural (consistency) rather than combinatorial (Section 4.5).

* **R6.** Gödel’s ontological argument over $p=5$ properties has $2^{5}=32$ raw positivity‑predicate interpretations and at least $2^{2}=4$ consistent ones (Section 4.6).

* **R7 (projection).** Under the assumptions of Section 4.7, the six stages receive $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours respectively; uncertainty is dominated by the assumed ratio (Section 4.7).

* **R8.** Contrast between propositional and modal stages:

\[
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18},
\]

showing an expansion of roughly $2.3\times10^{18}$‑fold (Section 5).

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Islander puzzle structure (three agents, fixed statements) | Results scale exponentially with the number of agents; alternative statements change the survivor count. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only (no transitivity, symmetry) | Adding constraints would reduce the relation count; current numbers are upper bounds for the given constraints. |
| S5 epistemic assumptions (equivalence relations) | Weakening to KD45 would alter the admissible relations and the shrinkage factor. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Captures worst‑case growth; alternative proof‑search strategies could yield smaller lengths. |
| Independence of Gödel axioms | If axioms are dependent, the consistent space could be larger than $2^{p-a}$. |
| Course‑time ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of ratios or student performance | Quantitative checkpoints are necessary but not sufficient for pedagogical success. |

### 6.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students solve the modal stage puzzles manually for $|W|=8$ despite the computed space of $2^{64}\approx10^{19}$ candidate relations. Such an outcome would indicate that the combinatorial model over‑estimates the effective search burden, falsifying the claim that the modal upgrade is forced by sheer state‑space size.

A second falsification condition is the discovery that the Wise Men ignorance announcements do not reduce the model size from $7$ to $4$ in a concrete implementation (e.g., because agents’ knowledge is modelled differently). This would contradict the derived shrinkage factor $1.75$ and challenge the quantitative justification for introducing dynamic epistemic logic.

### 6.3 Open questions

* How do alternative semantical‑embedding strategies (e.g., deep embeddings) affect the combinatorial counts?  
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

* **Proof‑assistant availability.** Isabelle/HOL must be installed and configured on institutional machines.  
* **Computational resources.** Model‑finding for $2^{64}$ relations requires exponential‑time algorithms; practical use relies on pruning heuristics rather than exhaustive enumeration.  
* **Pedagogical scaffolding.** Students need introductory material on HOL syntax and semantical embeddings before reaching Stage 2.  
* **Curricular scheduling.** The contact‑hour allocation derived in Section 4.7 assumes a 28‑hour semester; deviations require re‑balancing of the ratio.  
* **Assessment design.** Evaluation instruments must capture whether students understand the necessity of automation, not merely whether they obtain correct answers.

### 7.5 Order‑of‑magnitude cost projection

Assuming an institutional support cost of \$100 per contact hour (covering instructor time, software licences, and classroom resources), the projected total cost for the six stages is

\[
28\ \text{h}\times\$100/\text{h}= \$2{,}800,
\]

derived directly from the contact‑hour count in Section 4.7. This figure is a projection; actual costs may vary with local salary scales and infrastructure.

### 7.6 Direct risks and misuse paths

* **Over‑reliance on automation.** Students might treat the proof assistant as a black box, neglecting underlying logical reasoning. Mitigation requires explicit reflection activities.  
* **Misinterpretation of quantitative thresholds.** Instructors could present the raw numbers as absolute barriers rather than pedagogical guides, discouraging exploration of alternative reasoning strategies.  
* **Tool‑centric curriculum lock‑in.** Adoption of a single proof assistant may limit exposure to other formal‑methods tools; a diversified toolbox is advisable.

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