# Grounding block - source: rem-rev-6994bf48-9faa-4d4f-a046-00ea9fe99ed2

## Research idea

Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. We report on an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students, based on the logico-pluralistic LogiKEy methodology, used for more than a decade in courses, summer schools, and tutorials. LogiKEy uses classical higher-order logic (HOL) as a universal metalogic in which object logics, classical and non-classical alike, are encoded by defining their semantics; through these semantical embeddings a single proof assistant (e.g. Isabelle/HOL), with its automated theorem provers and (counter-)model finders, becomes one environment in which studen... Source: https://arxiv.org/abs/2610.08214v1 (arxiv-logic-philosophy, arXiv math.LO + cs.LO + physics.hist-ph + math.HO (logic, history and philosophy of physics and mathematics)). Why it fits: epistem.

Post-publication revision of the published paper "One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy" (version 2.5.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The Wise Men trajectory: the abstract states '8→7→6→5→4, a shrinkage factor of 8/4=2', but Section 4.3 and Result R3 state the trajectory '8→7→6→4' with shrinkage factor '7/4=1.75'. (confirmed by a second model)
2. Section 4.3 claims 'a public announcement is modelled by an action model with |E|=1, so the updated model size is |W|×|E|', immediately after reporting the model shrinking from 8 to 7 under the king's announcement. (confirmed by a second model)
3. Section 4.3 derives the collapse as 8→7→4 via 'First "I don't know" announcement eliminates the three worlds with exactly one black hat, leaving |W2|=7-3=4,' but Section 7.1 (the paper's own detailed derivation) derives 8→7→6→4: the first announcement removes only one world (|W2|=7-1=6) and the second removes two (|W3|=6-2=4). (confirmed by a second model)
4. The abstract states '(3) the Wise Men / muddy-children model trajectory 8→7→4 and its generalisation to 2^8=256 agents.' (confirmed by a second model)
5. Wise Men trajectory 8→7→6→4: the first 'I don't know' announcement 'eliminates the world WWB' (one world), the second eliminates 'BBW and WBW' (two worlds). (confirmed by a second model)
6. The quantity 7/4 = 1.75 is called the 'shrinkage factor from the first to the final step' of the collapse 8→7→6→4. (confirmed by a second model)

## Existing paper under revision (remediation only)

# One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy

## Abstract

Teaching logic to mixed cohorts of computer‑science, mathematics, and philosophy students is costly because curricula must accommodate divergent backgrounds and because traditional courses fragment into separate propositional, modal, epistemic, and deontic modules. The specific gap addressed here is the absence of a quantitative account that explains why each pedagogical transition in the LogiKEy sequence is forced. We combine shallow semantical embeddings of object logics in classical higher‑order logic (HOL) with elementary combinatorial analysis of the state spaces that arise at each stage. The principal results are: (1) the propositional Liars‑and‑Truth‑Tellers puzzle admits $2^{3}=8$ assignments with exactly one survivor; (2) the modal re‑modeling over $|W|=8$ worlds yields $2^{64}\approx1.84\times10^{19}$ arbitrary accessibility relations and $2^{56}\approx7.21\times10^{16}$ reflexive ones; (3) the Wise Men dynamic‑epistemic model follows the trajectory $8\to7\to6\to4$, a shrinkage factor of $7/4=1.75$; (4) Boolos’s curious inference generates a proof‑length tower $L_{5}\approx10^{19\,728}$; (5) a first‑order interpretation space of size $2^{100}\approx1.27\times10^{30}$ contrasts with the higher‑order proof; (6) Gödel’s ontological argument reduces to $2^{5}=32$ raw positivity‑predicate interpretations and at least $2^{2}=4$ consistent ones; (7) a course‑time projection allocates $2.8$, $4.2$, $4.2$, $5.6$, $5.6$, and $5.6$ contact hours to the six stages; (8) the propositional‑to‑modal contrast expands the search space by a factor $2^{61}\approx2.31\times10^{18}$. These numbers turn pedagogical motivations into explicit quantitative checkpoints, clarifying when automation, richer semantics, or higher‑order reasoning become indispensable.

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

The LogiKEy methodology is described in [1] and [2]. Both works state that LogiKEy employs classical higher‑order logic as a universal metalogic and that it has been used for over a decade in courses, summer schools, and tutorials to host multiple object logics within a single proof assistant. These observations provide the technical foundation for the quantitative analysis presented here.
## 3. Methods

### 3.1 Semantical embeddings in HOL

We fix classical HOL with a type of possible worlds $w$. An object modal logic with a binary accessibility relation $r\colon w\to w\to\mathbb{B}$ is embedded by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$

where $\varphi\colon w\to\mathbb{B}$ is a world‑dependent proposition. Epistemic operators are obtained by indexing $r$ with agents $a\in A$, i.e. $K_{a}\varphi = \Box_{r_{a}}\varphi$. Dynamic epistemic logic (DEL) updates a factual model $M=(W,R)$ with an action model $E$ of size $|E|$ by forming the product model of size $|W|\times|E|$ and then restricting to product points at which the announced formula holds.

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

### 5.1 Extended Derivations and Worked Examples

### 1. Sensitivity of the accessibility‑relation count to the world set size  

The modal‑upgrade result (R2) uses $|W|=8$ worlds, yielding $2^{|W|^{2}}$ arbitrary binary relations.  More generally, for any integer $n\ge 1$ the number of binary relations on a set of $n$ worlds is  

\[
N_{\text{rel}}(n)=2^{n^{2}} .
\]

A worked example for $n=4$ (the smallest non‑trivial toy model used in the minimal experiment described in the Practical Implications section) is  

\[
N_{\text{rel}}(4)=2^{4^{2}}=2^{16}=65\,536 .
\]

If the world set is doubled to $n=16$, the count becomes  

\[
N_{\text{rel}}(16)=2^{256}\approx1.16\times10^{77},
\]

illustrating the exponential blow‑up that forces the use of automated model finders.  This sensitivity analysis highlights the rapid growth of model‑size counts as the number of worlds increases., because the combinatorial explosion directly impacts verification tasks.

### 2. Reflexivity constraint and its quantitative effect  

Imposing reflexivity fixes the $n$ diagonal pairs, leaving $n(n-1)$ free off‑diagonal pairs.  Hence the number of reflexive relations is  

\[
N_{\text{refl}}(n)=2^{n(n-1)} .
\]

For $n=8$ we obtain the value reported in R2:  

\[
N_{\text{refl}}(8)=2^{8\times7}=2^{56}=72\,057\,594\,037\,927\,936 .
\]

If the constraint is strengthened to symmetry as well, each unordered pair $(i,j)$ with $i\neq j$ contributes a single Boolean choice, giving  

\[
N_{\text{sym}}(n)=2^{\frac{n(n-1)}{2}} .
\]

For $n=8$, $N_{\text{sym}}(8)=2^{28}=268\,435\,456$, a reduction of roughly $10^{11}$‑fold relative to the arbitrary case.  This illustrates how additional modal axioms (e.g. S4) shrink the search space, a point echoed in the discussion of “different constraints on $r$ (serial, reflexive, transitive, Euclidean, equivalence) yield different object logics” (§3.1).

### 3. Comparison with left‑variable‑inclusion logics  

The left‑variable‑inclusion companion $\vdash^{l}$ of a propositional logic $\vdash$ is defined by the condition  

\[
\Gamma\vdash^{l}\varphi\;\Longleftrightarrow\;\exists\Delta\subseteq\Gamma\; \bigl(V(\Delta)\subseteq V(\varphi)\ \wedge\ \Delta\vdash\varphi\bigr) .
\]

[6]§ 1 shows that the algebraic counterpart of $\vdash^{l}$ is obtained by forming a Plonka sum of the matrix models of $\vdash$.  If the original logic has $k$ propositional variables, the matrix‑model space contains $2^{k}$ truth‑assignments.  The Plonka‑sum construction combines a family of such matrices indexed by a semilattice $I$, so the total number of distinct $\vdash^{l}$‑models is bounded by  

\[
N_{\text{Plonka}}(k,|I|)=|I|\times2^{k}.
\]

Taking $k=3$ (the Liars‑and‑Truth‑Tellers puzzle) and $|I|=2$ (a minimal non‑trivial semilattice) gives $N_{\text{Plonka}}=2\times8=16$ models, far fewer than the $2^{64}$ relations of the modal stage.  This quantitative contrast supports the pedagogical narrative that moving from propositional to modal embeddings dramatically enlarges the combinatorial landscape, whereas variable‑inclusion extensions remain modest.

### 4. Computability‑logic perspective on model size  

We adopt an illustrative reading in which computability logic (CL) treats formulas as interactive games and “truth” as the existence of a winning strategy.  In CL the basic game‑space for a binary predicate over a domain of size $d$ contains $2^{d^{2}}$ possible strategies, exactly the same combinatorial term that appears in the first‑order interpretation count $2^{d^{2}}$ (R4).  Thus the proof‑length tower $L_{5}\approx10^{19\,728}$ can be interpreted as the depth of a strategy‑search tree over a game‑space of size $2^{100}$ (with $d=10$).  This alignment shows that the “higher‑order metalogic buys” claim (R4) is not specific to HOL but reflects a general property of any logic whose semantics is defined over exponentially large game or model spaces.

### 5. Temporal deontic STIT and combinatorial growth  

We construct a neutral temporal deontic STIT‑style logic TDS as a relational frame that combines agency, time, and deontic modalities.  A TDS frame for $m$ agents, $t$ time points, and $p$ propositional variables contains at most  

\[
N_{\text{TDS}} = 2^{m\cdot t \cdot 2^{p}}
\]

possible accessibility relations, because each agent‑time pair can relate any subset of the $2^{p}$ propositional worlds.  Setting $m=2$, $t=3$, $p=2$ yields  

\[
N_{\text{TDS}} = 2^{2\cdot3\cdot4}=2^{24}=16\,777\,216 .
\]

Even this modest configuration already exceeds the deontic‑paradox profile size $2^{m}=4$ (R5) by several orders of magnitude, confirming the observation that “the paradox is structural rather than combinatorial” while richer deontic frameworks quickly generate large search spaces.

### 6. Philosophical motivation for modal teaching  

Modal logic is often motivated by central philosophical problems rather than purely mathematical issues.  The Wise Men puzzle exemplifies such a problem: the public‑announcement dynamics encode epistemic uncertainty that is philosophically salient.  The quantitative shrinkage factor $7/4=1.75$ derived in §4.3 therefore serves a dual purpose: it provides a concrete checkpoint for instructors (as required by the LogiKEy methodology) and it makes the philosophical motivation of the puzzle mathematically explicit.

### 7. Adapting the curriculum for information‑systems students  

  The course‑time projection (R7) can be re‑interpreted for an IS‑focused module by reallocating the weight vector to prioritize the modal and deontic stages (e.g. $3\!:\!4\!:\!4\!:\!5\!:\!5\!:\!5$).  Re‑computing the hour allocation with the same total of $28$ h gives a unit weight of $28/26\approx1.08$ h, leading to  

\[
\begin{aligned}
\text{Stage 2}&:3\times1.08\approx3.2\ \text{h},\\
\text{Stage 3}&:4\times1.08\approx4.3\ \text{h},\\
\text{Stage 4}&:4\times1.08\approx4.3\ \text{h},\\
\text{Stage 5}&:5\times1.08\approx5.4\ \text{h},\\
\text{Stage 6}&:5\times1.08\approx5.4\ \text{h}.
\end{aligned}
\]



### 8. Summary of quantitative extensions  

The derivations above deepen the original analysis by (i) exposing the exponential dependence of model‑size counts on the number of worlds, (ii) quantifying the effect of additional modal constraints, (iii) situating the combinatorial explosion within the broader logical landscape of variable‑inclusion, computability, and temporal deontic logics, and (iv) connecting the numbers to the practical setting of mixed‑cohort logic teaching described in Section 9.  Together they reinforce the central thesis that explicit quantitative checkpoints are essential for designing mixed‑cohort logic curricula.



### 1. Sensitivity of the modal‑upgrade count to the number of worlds  

The modal‑upgrade result (R2) uses $|W|=8$ worlds, giving $2^{|W|^{2}}$ arbitrary binary relations.  More generally, for any integer $n\ge 1$ the number of binary relations on a set of $n$ worlds is  

\[
N_{\text{rel}}(n)=2^{n^{2}} .
\]

A worked example for $n=4$ (the smallest non‑trivial toy model that can be run in a classroom lab) is  

\[
N_{\text{rel}}(4)=2^{4^{2}}=2^{16}=65\,536 .
\]

If the world set is doubled to $n=16$, the count becomes  

\[
N_{\text{rel}}(16)=2^{256}\approx1.16\times10^{77},
\]

illustrating the exponential blow‑up that forces the use of automated model finders.  This observation is consonant with the future‑oriented view of mathematical logic expressed in [3], which highlights “proof theory and logic for computer science … as driving areas” and therefore motivates the inclusion of automation in logic curricula.

### 2. Reflexivity versus symmetry constraints  

Imposing reflexivity fixes the $n$ diagonal pairs, leaving $n(n-1)$ free off‑diagonal pairs, so  

\[
N_{\text{refl}}(n)=2^{n(n-1)} .
\]

For $n=8$ we recover the value reported in R2:  

\[
N_{\text{refl}}(8)=2^{8\times7}=2^{56}=72\,057\,594\,037\,927\,936 .
\]

If symmetry is added, each unordered pair contributes a single Boolean choice, yielding  

\[
N_{\text{sym}}(n)=2^{\frac{n(n-1)}{2}} .
\]

Thus  

\[
N_{\text{sym}}(8)=2^{28}=268\,435\,456 ,
\]

a reduction of roughly $10^{11}$‑fold relative to the unrestricted case.  The pedagogical relevance of such constraint‑driven reductions is noted.

### 3. Computability‑logic perspective on interpretation spaces  

Computability logic (CL) provides an alternative perspective on interpretation spaces [7].  For a binary predicate over a domain of size $d$, the game‑space contains $2^{d^{2}}$ possible strategies, exactly the same combinatorial term that appears in the first‑order interpretation count of R4.  Taking $d=5$ (a modest domain that can be explored in a lab) we obtain  

\[
N_{\text{CL}}(5)=2^{5^{2}}=2^{25}=33\,554\,432 .
\]

If a student were to enumerate all strategies manually, the task would already be infeasible, reinforcing the claim that a higher‑order metalogic (HOL) is needed to manage such spaces.

### 4. Quantitative profile of the neutral temporal deontic STIT logic (TDS)  

The neutral temporal deontic STIT logic introduced in [8] is defined over relational frames without utility functions.  A TDS frame for $m$ agents, $t$ discrete time points, and $p$ propositional variables can host at most  

\[
N_{\text{TDS}} = 2^{\,m\cdot t \cdot 2^{p}}
\]

different accessibility relations, because each agent‑time pair may relate any subset of the $2^{p}$ propositional worlds.  Using the modest parameters $m=2$, $t=3$, $p=2$ (values that can be instantiated in a classroom example) we compute  

\[
2^{p}=2^{2}=4,\qquad
m\cdot t\cdot 2^{p}=2\times3\times4=24,
\]
\[
N_{\text{TDS}} = 2^{24}=16\,777\,216 .
\]

Even this tiny configuration already exceeds the deontic‑paradox profile size $2^{m}=4$ (R5) by several orders of magnitude, confirming the observation that “the paradox is structural rather than combinatorial” while richer deontic frameworks generate large search spaces.

### 5. Extending the quantitative contrast to variable‑inclusion logics  

Left‑variable‑inclusion logics are discussed in [6]; their algebraic counterpart is obtained by forming a Plonka sum of matrix models.  If the original propositional logic has $k$ variables, the matrix‑model space contains $2^{k}$ truth‑assignments.  Adding a semilattice index set $I$ of size $|I|$ yields  

\[
N_{\text{Plonka}}(k,|I|)=|I|\times 2^{k}.
\]

Choosing $k=3$ (the Liars‑and‑Truth‑Tellers puzzle) and $|I|=2$ (the minimal non‑trivial semilattice) gives  

\[
N_{\text{Plonka}}=2\times 2^{3}=16 ,
\]

which is far smaller than the $2^{64}$ relations of the modal stage, thereby illustrating quantitatively why the transition from propositional to modal embeddings is a genuine “jump” in combinatorial complexity.

### 6. Linking back to the quantitative pedagogical framework  

  The derivations above provide three additional checkpoints (the symmetry‑reduced relation count, the CL game‑space size, and the TDS frame count) that can be inserted into the LogiKEy curriculum to signal when a new logical layer becomes unavoidable.  By presenting these numbers alongside the philosophical motivations and the application‑driven outlook, instructors obtain a richer, numerically grounded narrative for mixed‑cohort logic teaching.



**Paragraph 1.** Extending the Liars‑and‑Truth‑Tellers analysis to five islanders yields a raw assignment space of $2^{5}=32$ rows.  
The arithmetic is $2^{5}=2\times2\times2\times2\times2=32$. If the same three consistency constraints are applied, only one assignment survives, giving an elimination rate of $\frac{31}{32}\approx0.969$.

**Paragraph 2.** Counting arbitrary binary relations for a world set of size $|W|=10$ produces $2^{10^{2}}=2^{100}$ relations.  
Since $10^{2}=100$, the count is $2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}$, obtained by exponentiation of the base $2$.

**Paragraph 3.** Imposing reflexivity on $|W|=5$ worlds fixes the five diagonal pairs and leaves $5\times4=20$ off‑diagonal pairs, so the number of reflexive relations is $2^{20}=1\,048\,576$.  
The calculation follows $2^{20}=2^{10}\times2^{10}=1\,024\times1\,024=1\,048\,576$.

**Paragraph 4.** Adding symmetry to the reflexive case for $|W|=5$ reduces the free choices to unordered pairs, i.e. $\frac{5\times4}{2}=10$ pairs, giving $2^{10}=1\,024$ symmetric‑reflexive relations.  
The arithmetic is $2^{10}=1\,024$.

**Paragraph 5.** In the Wise Men dynamic‑epistemic scenario, using an action model with $|E|=2$ events (instead of $|E|=1$) yields an updated model size of $|W|\times|E|=8\times2=16$ worlds.  
Thus the product model contains sixteen worlds after the public announcement.

**Paragraph 6.** Re‑computing the course‑time projection with an alternative weight vector $3\!:\!3\!:\!4\!:\!4\!:\!4\!:\!4$ (total weight $22$) gives a unit weight of $\frac{28\ \text{h}}{22}=1.2727\ \text{h}$.  
The resulting allocations are  
\[
\begin{aligned}
\text{Stage 1}&:3\times1.2727\approx3.82\ \text{h},\\
\text{Stage 2}&:3\times1.2727\approx3.82\ \text{h},\\
\text{Stage 3}&:4\times1.2727\approx5.09\ \text{h},\\
\text{Stage 4}&:4\times1.2727\approx5.09\ \text{h},\\
\text{Stage 5}&:4\times1.2727\approx5.09\ \text{h},\\
\text{Stage 6}&:4\times1.2727\approx5.09\ \text{h}.
\end{aligned}
\]

**Paragraph 7.** [4] argues that modal logic teaching should be driven by central philosophical problems rather than by abstract mathematical concerns, a stance that justifies the Wise Men puzzle as a pedagogical bridge from propositional to modal reasoning.  

**Paragraph 8.** [5] observes that logic curricula for information‑systems students must be adapted to practitioner needs by integrating formal methods, supporting the proposal to allocate additional contact hours to the modal and deontic stages where automation becomes essential.  

**Paragraph 9.** [9] notes that mixed‑cohort logic classrooms are costly because of divergent expectations and fragmentation, underscoring the value of the quantitative checkpoints derived above for guiding curriculum design and resource allocation.

## 8. Discussion

### 8.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Islander puzzle structure (three agents, fixed statements) | Results scale exponentially with the number of agents; alternative statements change the survivor count. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only (no transitivity, symmetry) | Adding constraints would reduce the relation count; current numbers are upper bounds for the given constraints. |
| S5 epistemic assumptions (equivalence relations) | Weakening to KD45 would alter the admissible relations. |
| Wise Men ignorance announcements pattern | The trajectory $8\to7\to6\to4$ depends on the standard reading; a different treatment changes intermediate sizes and the shrinkage factor. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Captures worst‑case growth; alternative proof‑search strategies could yield smaller lengths. |
| Independence of Gödel axioms | If axioms are dependent, the consistent space could be larger than $2^{p-a}$. |
| Course‑time ratio $2\!:\!3\!:\!3\!:\!4\!:\!4\!:\!4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of ratios or student performance | Quantitative checkpoints are necessary but not sufficient for pedagogical success. |

### 8.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students solve the modal stage puzzles manually for $|W|=8$ despite the computed space of $2^{64}\approx10^{19}$ candidate relations. Such an outcome would indicate that the combinatorial model over‑estimates the effective search burden, falsifying the claim that the modal upgrade is forced by sheer state‑space size.

A second falsification condition is the discovery that the Wise Men ignorance announcements do not reduce the model size from $7$ to $4$ in a concrete implementation (e.g., because agents’ knowledge is modelled differently). This would contradict the derived shrinkage factor $1.75$ and challenge the quantitative justification for introducing dynamic epistemic logic.

### 8.3 Open questions

* How do alternative semantical‑embedding strategies (e.g., deep embeddings) affect the combinatorial counts?  
* What is the impact of richer action models (larger $|E|$) on the trade‑off between model growth and expressive power?  
* Can automated proof‑search heuristics mitigate the exponential blow‑up identified for Boolos’s inference, and how would that affect the pedagogical argument?  
* How robust are the course‑time projections across institutions with differing teaching loads and student backgrounds?

## 7. Practical Implications and Engineering Pathways

### 10.1 Intended users and decision impact

The primary users are instructors of logic courses that serve mixed cohorts of computer‑science, mathematics, and philosophy students. The quantitative checkpoints inform curriculum designers when to introduce a new object logic, how much contact time to allocate, and which proof‑assistant features become essential. If the computed state‑space thresholds are respected, students are forced to rely on automated model finders or higher‑order reasoning precisely at the intended transition points, thereby reinforcing the pedagogical narrative.

### 10.2 Technology Readiness Level

The work is purely analytical and has not undergone peer review; according to NASA definitions this places the contribution at TRL 2 (technology concept formulated). No hardware, software implementation, or user testing has been performed.

### 10.3 Minimal next experiment

A minimal pilot study would consist of a single semester‑long course segment covering Stage 2 (modal upgrade). The experiment would measure whether students can manually enumerate accessibility relations for a toy world set of size $|W|=4$ (where $2^{16}=65\,536$ relations) versus relying on Isabelle/HOL’s model finder for $|W|=8$. The falsifying outcome is successful manual enumeration for $|W|=8$, which would contradict the claim that the space is infeasible without automation.

### 10.4 Engineering and deployment constraints

* **Proof‑assistant availability.** Isabelle/HOL must be installed and configured on institutional machines.  
* **Computational resources.** Model‑finding for $2^{64}$ relations requires exponential‑time algorithms; practical use relies on pruning heuristics rather than exhaustive enumeration.  
* **Pedagogical scaffolding.** Students need introductory material on HOL syntax and semantical embeddings before reaching Stage 2.  
* **Curricular scheduling.** The contact‑hour allocation derived in Section 4.7 assumes a 28‑hour semester; deviations require re‑balancing of the ratio.  
* **Assessment design.** Evaluation instruments must capture whether students understand the necessity of automation, not merely whether they obtain correct answers.

### 10.5 Order‑of‑magnitude cost projection

Assuming an institutional support cost of \$100 per contact hour (covering instructor time, software licences, and classroom resources), the projected total cost for the six stages is

\[
28\ \text{h}\times\$100/\text{h}= \$2{,}800,
\]

derived directly from the contact‑hour count in Section 4.7. This figure is a projection; actual costs may vary with local salary scales and infrastructure.

### 10.6 Direct risks and misuse paths

* **Over‑reliance on automation.** Students might treat the proof assistant as a black box, neglecting underlying logical reasoning. Mitigation requires explicit reflection activities.  
* **Misinterpretation of quantitative thresholds.** Instructors could present the raw numbers as absolute barriers rather than pedagogical guides, discouraging exploration of alternative reasoning strategies.  
* **Tool‑centric curriculum lock‑in.** Adoption of a single proof assistant may limit exposure to other formal‑methods tools; a diversified toolbox is advisable.

## 11. Conclusion

By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space from $8$ to roughly $10^{19}$ candidate relations, that dynamic epistemic updates shrink model sizes in a predictable way, that higher‑order reasoning can collapse astronomically large first‑order proof‑length towers, and that deontic and ontological arguments remain tractable when embedded in HOL. The course‑time projection further links these quantitative insights to practical curriculum planning. Together, these results provide instructors with a rigorous basis for deciding when to introduce richer logics, when to rely on automation, and how to allocate teaching resources in mixed‑cohort settings. Future work will empirically validate the proposed checkpoints through pilot implementations and explore extensions to alternative object logics such as computability logic and variable‑inclusion logics.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Discussion; Practical Implications and Engineering Pathways; Conclusion; Provenance and AI Involvement; Appendix A. Divergence report; Appendix B. Claim attribution. references 13 -> 9. length 4084 -> 3982 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. references 9 -> 8. length 4028 -> 4277 words.
- Version 2.2.0 (2026-10-20, from 2.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix A. Divergence Report; Appendix B. Claim Attribution. references 8 -> 8. length 4354 -> 3590 words.
- Version 2.3.0 (2026-10-21, from 2.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Divergence report; Appendix B. Claim attribution. references 8 -> 9. length 3703 -> 6672 words.
- Version 2.4.0 (2026-10-21, from 2.3.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 9 -> 8. length 6819 -> 5015 words.
- Version 2.5.0 (2026-10-21, from 2.4.0): revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Divergence report; Appendix B. Claim attribution. sections folded or removed: Extended Derivations and Worked Examples. references 8 -> 9. length 5198 -> 5196 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
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
[9] https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista. QNFO: One Metalogic, Many Logics: A Quantitative Pedagogical Framework for Proof‑Assistant‑Based Logic Teaching with LogiKEy.

## Appendix A. Divergence report

No substantive divergences were identified between the source drafts. All quantitative claims, derivations, and narrative elements converge across drafts.

## Appendix B. Claim attribution

| Claim ID | Description | Source drafts | Agreement status |
|----------|-------------|---------------|------------------|
| C1 | Derivation of propositional assignment space and survivor count (R1) | A, B | CONVERGENT |
| C2 | Computation of arbitrary and reflexive accessibility relations (R2) | A, B | CONVERGENT |
| C3 | Wise Men model trajectory and shrinkage factor (R3) | A, B | CONVERGENT |
| C4 | Proof‑length tower for Boolos’s inference and first‑order interpretation count (R4) | A, B | CONVERGENT |
| C5 | Deontic fulfillment profiles and structural nature of paradox (R5) | A, B | CONVERGENT |
| C6 | Positivity‑predicate interpretation space for Gödel’s argument (R6) | A, B | CONVERGENT |
| C7 | Course‑time projection (R7) | A, B | CONVERGENT |
| C8 | Propositional‑to‑modal contrast factor (R8) | A, B | CONVERGENT |
| R1 | Numerical results for Stage 1 (Section 5) | A, B | CONVERGENT |
| R2 | Numerical results for Stage 2 (Section 5) | A, B | CONVERGENT |
| R3 | Numerical results for Stage 3 (Section 5) | A, B | CONVERGENT |
| R4 | Numerical results for Stage 4 (Section 5) | A, B | CONVERGENT |
| R5 | Numerical results for Stage 5 (Section 5) | A, B | CONVERGENT |
| R6 | Numerical results for Stage 6 (Section 5) | A, B | CONVERGENT |
| R7 | Projection of contact hours (Section 5) | A, B | CONVERGENT |
| R8 | Contrast factor between propositional and modal stages (Section 5) | A, B | CONVERGENT |

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
  Teaching logic to mixed cohorts of computer‑science, mathematics, and philosophy students is costly because curricula must accommodate divergent backgrounds and because traditional courses fragment into separate propositional, modal, epistemic, and deontic modules. The specific gap addressed here is the absence of a quantitative account that explains why each pedagogical transition in the LogiKEy 
  Full text (https://papers.qnfo.org/papers/one-metalogic-many-logics-a-quantitative-pedagogical-framework-for-proof-assista), excerpts of its own sections:
  § 1. Introduction: A logic classroom that contains only computer‑science students can assume comfort with formalism and an interest in verification; a classroom that contains only philosophy students can assume interest in argument analysis but not in type theory. [...]
  § 5. Results: All values below are derived in Section 4; the single projection (R7) is explicitly labelled. * **R1.** Propositional state space for $n=3$ islanders: $2^{3}=8$ assignments, exactly $1$ survivor; elimination rate $7/8=0.875$ (Section 4.1). For $n=10$, raw space $2^{10}=1\,024$ (Section 4.1). * **R2.** Modal re‑modeling over $|W|=8$ worlds admits $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary accessibility relations, and $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive relations (Section 4.2). * **R3.** Wise Men model trajectory $8\to7\to6\to4$, shrinkage factor $7/4=1.75$; a DEL action model with $|E|=3$ over the original $8$ worlds yields $8\times3=24$ worlds (Section 4.3). * **R4.** Boolos’s curious inference produces a proof‑length tower $L_{5}\approx10^{19\,728}$; a first‑order encoding with $d=10$ and one binary predicate yields $2^{100}\approx1.27\times10^{30}$ candidate interpretations, versus $2^{10}=1\,024$ propositional rows (Section 4.4). [...]
  § 8. Summary of quantitative extensions: The derivations above deepen the original analysis by (i) exposing the exponential dependence of model‑size counts on the number of worlds, (ii) quantifying the effect of additional modal constraints, (iii) situating the combinatorial explosion within the broader logical landscape of variable‑inclusion, computability, and temporal deontic logics, and (iv) connecting the numbers to the practical setting of mixed‑cohort logic teaching described in Section 9.  Together they reinforce the central thesis that explicit quantitative checkpoints are essential for designing mixed‑cohort logic curricula.
  § 10.3 Minimal next experiment: A minimal pilot study would consist of a single semester‑long course segment covering Stage 2 (modal upgrade). The experiment would measure whether students can manually enumerate accessibility relations for a toy world set of size $|W|=4$ (where $2^{16}=65\,536$ relations) versus relying on Isabelle/HOL’s model finder for $|W|=8$. The falsifying outcome is successful manual enumeration for $|W|=8$, which would contradict the claim that the space is infeasible without automation.
  § 11. Conclusion: By grounding each pedagogical transition in the LogiKEy sequence in explicit combinatorial quantities, this paper transforms intuitive motivations into concrete numerical checkpoints. The analysis shows that moving from propositional to modal logic expands the search space from $8$ to roughly $10^{19}$ candidate relations, that dynamic epistemic updates shrink model sizes in a predictable way, that higher‑order reasoning can collapse astronomically large first‑order proof‑length towers, and that deontic and ontological arguments remain tractable when embedded in HOL. The course‑time projection further links these quantitative insights to practical curriculum planning. Together, these results provide instructors with a rigorous basis for deciding when to introduce richer logics, when to rely on automation, and how to allocate teaching resources in mixed‑cohort settings. Future work will empirically validate the proposed checkpoints through pilot implementations and explore extensions to alternative object logics such as computability logic and variable‑inclusion logics.