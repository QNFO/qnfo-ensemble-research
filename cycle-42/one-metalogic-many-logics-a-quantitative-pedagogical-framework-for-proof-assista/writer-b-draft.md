# One Metalogic, Many Logics: A Quantitative Case Study of the LogiKEy Methodology for Teaching Logic to Mixed Cohorts

## Abstract

Teaching logic to mixed groups of computer science, mathematics, and philosophy students is difficult because each cohort brings different expectations, and because the standard curriculum fragments into isolated courses on propositional logic, modal logic, epistemic logic, deontic logic, and higher-order metaphysics. The LogiKEy methodology addresses this by using classical higher-order logic (HOL) as a universal metalogic: object logics are encoded as semantical embeddings inside a single proof assistant (Isabelle/HOL), so that students learn, experiment with, and compare logics in one environment. This paper reconstructs the pedagogical core of the methodology as a graded sequence of classroom examples — liars-and-truth-tellers, the Wise Men puzzle, Boolos's curious inference, Chisholm's paradox, and Gödel's ontological argument — and supplies explicit quantitative analyses of each transition. We compute the exhaustive consistency check for a three-islander liar puzzle (8 assignments, 1 survivor), the model-size dynamics of a public-announcement epistemic puzzle ($8 \to 7 \to 6 \to 4$ worlds), the space of dyadic deontic conditionals over three atoms (256 Boolean antecedents), and the tower growth $2^{2^{2}} = 16$, $2^{16} = 65536$, $\approx 10^{19728}$ that motivates a higher-order metalogic. We argue that these computed checkpoints, rather than anecdote, are what make the methodology teachable, and we discuss limitations, failure modes, and falsifiability.

## 1. Introduction

A logic classroom with only computer science students can assume comfort with formalism and an interest in verification; a classroom with only philosophy students can assume interest in argument analysis but not in type theory. A mixed classroom — computer science, mathematics, and philosophy students together — inherits all of the difficulties and none of the homogeneity. Two failure modes are common. The first is fragmentation: each logic (propositional, modal, epistemic, deontic) is taught as a separate subject with separate notation, separate tools, and separate exercises, so students leave with a portfolio of disconnected techniques rather than a unified competence. The second is monotony: a single logic (usually classical first-order) is taught as if it exhausted the field, leaving philosophy students without the non-classical logics their discipline demands and computer science students without the modelling resources (agents, knowledge, obligation, action) their discipline increasingly uses.

The LogiKEy methodology [1], [2] proposes a third way: logico-pluralism on a single technical substrate. Classical higher-order logic (HOL) serves as a universal metalogic. Each object logic — classical or non-classical — is encoded by defining its semantics in HOL: possible worlds become HOL individuals, accessibility relations become HOL relations on those individuals, modal operators become HOL functions quantifying over worlds. Through such semantical embeddings, one proof assistant (e.g. Isabelle/HOL, with its automated theorem provers and counter-model finders) becomes a single laboratory in which students define logics, prove their metatheorems, and compare their expressive power.

This paper's contribution is to make the quantitative spine of that pedagogy explicit. Each transition in the graded example sequence of [1] is motivated by a limitation of the preceding representation; we show that these limitations can be exhibited with concrete, checkable arithmetic — counts of valuations, model sizes, search spaces, and proof-length growth — so that the motivation for each new logic is not rhetorical but computational. Section 2 situates the approach in the literature. Section 3 formalizes the embedding scheme. Section 4 carries out the derivations with every input number stated. Section 5 reports the results. Section 6 discusses limitations and what would falsify the pedagogical claims, and Section 7 concludes.

## 2. Background and Related Work

The LogiKEy papers themselves [1], [2] report over a decade of use in courses, summer schools, and tutorials, and present the graded sequence of examples from the liars-and-truth-tellers puzzle through Gödel's ontological argument. They also rebut the objection that embedding everything in classical HOL is monism rather than pluralism: the object logics remain genuinely distinct — their theorems, their valid inferences, and their counter-models differ — even though their semantics are uniformly definable in HOL. Our paper accepts their framework and adds explicit quantitative checkpoints to each transition.

The broader question of logic's future role across disciplines is addressed in [3], where four authors speculate on the development of mathematical logic in the twenty-first century across recursion theory, proof theory, model theory, and set theory. Their emphasis on proof theory and "logic for computer science" as a driving area supports the LogiKEy bet that proof-assistant literacy is a transferable skill rather than a specialist niche.

On the teaching of modal logic specifically, [4] argues for an agenda motivated by central problems of philosophy and language rather than by mathematical issues alone. This is directly relevant to the LogiKEy sequence: the transition from propositional to modal logic in [1] is driven by a puzzle about truth-telling and knowledge, not by Kripke completeness theorems, in line with [4]'s recommendation that philosophical motivation lead.

The problem of heterogeneous student populations is studied in [5], which examines teaching logic to information systems students and argues that, rather than excluding logic from their curriculum, contents and methodology must be significantly adapted to practitioner needs. The LogiKEy methodology can be read as one systematic answer to [5]'s challenge: the adaptation is not a watered-down syllabus but a uniform tool-based environment in which students with different backgrounds enter through different object logics.

An alternative re-foundation of logic is computability logic, presented in [6] as a formal theory of computability — formulas as interactive computational problems, truth as existence of a winning algorithmic strategy — in contrast to classical logic as a theory of truth. Its development into applied theories is carried forward in [8]. Computability logic illustrates the space of proposals against which the LogiKEy choice of HOL-as-metalogic must be measured: where computability logic changes what the logical operators mean, LogiKEy keeps the metalogic fixed and varies the embedded semantics. A course built on LogiKEy could in principle embed a game semantics of the [6], [8] style as one more object logic, which is itself evidence for the flexibility of the HOL substrate.

Genuine logical pluralism inside the algebraic tradition is exemplified by [7], which studies logics defined by imposing a variable inclusion condition on a given consequence relation $\vdash$, showing that the algebraic counterpart is obtained by Plonka sums of matrix models and yielding Hilbert-style axiomatizations. Such non-classical consequence relations are exactly the kind of object logic that the semantical-embedding approach can host: a matrix semantics is a set-theoretic structure, hence definable in HOL.

The deontic stage of the LogiKEy sequence (Chisholm's paradox, standard then dyadic deontic logic) connects to [9], which introduces the temporal deontic STIT logic TDS, proving soundness and completeness with respect to relational frames without utilitarian commitments. [9] demonstrates that deontic logic remains an active research frontier with new modelling resources (agency, time); a LogiKEy-style course can present TDS as a further embedding, showing students that the sequence they climbed does not end at dyadic deontic logic.

Finally, a heterodox research program questions the Boolean substrate itself: [11] argues that Boolean logic reifies the void (the unmarked state) into falsity, committing a category error, and proposes a distinction-logic reconstruction labeled as conjecture; [12] argues that $1+1=2$ presupposes distinguishable marks and that idempotence ($AA=A$) is primitive; [13] develops the calculus of re-entrant distinctions into a treatise on self-reference; and [10] collects this continuum-critique program. Whatever their ultimate merit, these works are useful in a LogiKEy classroom precisely as embedded dissent: a heterodox logic is a good stress test of the claim that the HOL metalogic is neutral ground on which competing logics can be defined and compared.

## 3. Methods

### 3.1 Semantical embeddings in HOL

The technical core is the following. Fix classical HOL with a domain of possible worlds $W$ (a HOL type $w$). An object modal logic with box operator is embedded by:

$$\Box_{r} \varphi \;=\; \lambda w.\, \forall v.\, r\, w\, v \Rightarrow \varphi\, v$$

where $r : w \to w \to \mathbb{B}$ is a HOL relation and $\varphi : w \to \mathbb{B}$ is a HOL predicate on worlds (a proposition is a set of worlds). Different choices of constraints on $r$ (serial, reflexive, transitive, Euclidean, equivalence) yield different object logics (D, T, S4, S5), all inside the same metalogic. Epistemic logic adds an agent index: $r_a$ for each agent $a$ from a finite set $A$, with knowledge $K_a \varphi = \Box_{r_a} \varphi$; under S5 constraints each $r_a$ is an equivalence relation partitioning $W$. Dynamic epistemic logic adds event models acting on the current model. Deontic logic replaces worlds-with-obligation by either a deontic accessibility $r_{ob}$ (standard) or a dyadic conditional $\mathcal{O}(\psi \mid \varphi)$ selecting ideal $\varphi$-worlds (dyadic). None of this requires new tooling: each definition is a HOL constant, each metatheorem a HOL theorem, each counter-model a HOL-computable structure.

### 3.2 Method of this paper

For each stage of the graded sequence of [1], we identify a quantitative invariant that (i) can be computed exactly from stated inputs by elementary arithmetic, and (ii) exhibits the limitation that motivates the transition to the next logic. We deliberately restrict every claim in Section 5 to numbers derived in Section 4; where we extrapolate beyond the computation, the claim is labeled a projection with its assumptions stated.

## 4. Analysis

### 4.1 Stage 1: Liars and truth-tellers — exhaustive consistency in propositional logic

**Input (from the puzzle structure of [1]).** Three islanders $a, b, c$; each is either a truth-teller ($T$) or a liar ($L$). Statements: $a$ says "$b$ is a truth-teller"; $b$ says "$a$ and $c$ are of different types"; $c$ says "$a$ is a liar". Consistency condition: an islander of type $T$ asserts only truths; an islander of type $L$ asserts only falsehoods.

**Encoding.** Let $x_a, x_b, x_c \in \{T, L\}$. The three consistency constraints are:

$$x_a = (x_b = T), \qquad x_b = (x_a \neq x_c), \qquad x_c = (x_a = L)$$

**Exhaustive check.** The search space has $2^3 = 8$ assignments. We evaluate each:

1. $(T,T,T)$: constraint 1: $T = (T{=}T) = T$ ✓. Constraint 2: $T = (T \neq T) = F$ ✗. Eliminated.
2. $(T,T,L)$: constraint 1: $T = T$ ✓. Constraint 2: $T = (T \neq L) = T$ ✓. Constraint 3: $L = (T{=}L) = F$ ✓. **Survives.**
3. $(T,L,T)$: constraint 1: $T = (L{=}T) = F$ ✗. Eliminated.
4. $(T,L,L)$: constraint 1: $T = F$ ✗. Eliminated.
5. $(L,T,T)$: constraint 1: $L = T$ ✗. Eliminated.
6. $(L,T,L)$: constraint 1: $L = T$ ✗. Eliminated.
7. $(L,L,T)$: constraint 1: $L = (L{=}T) = F$ ✓. Constraint 2: $L = (L \neq T) = T$ ✗. Eliminated.
8. $(L,L,L)$: constraint 1: $L = F$ ✓. Constraint 2: $L = (L \neq L) = F$ ✓. Constraint 3: $L = (L{=}L) = T$ ✗. Eliminated.

Exactly one of $8$ assignments survives: $(x_a, x_b, x_c) = (T, T, L)$. The elimination rate is $7/8 = 0.875$.

**Pedagogical point (quantified).** For $n$ islanders the search space is $2^n$; a truth table for $n = 10$ already needs $2^{10} = 1024$ rows checked by hand. This exhaustion of hand-checking is the computed limitation that motivates automation — and, once statements about *knowing* appear, modal logic.

### 4.2 Stage 2: The Wise Men puzzle — model dynamics under public announcement

**Input (from the puzzle structure of [1]).** Three agents $a, b, c$; each wears a black ($B$) or white ($W$) hat; each sees the others' hats but not their own; the king publicly announces "at least one hat is black". All three hats are in fact black. Knowledge is S5: agent $i$'s alternatives at a world differ from it only in coordinate $i$.

**Model size before announcements.** Hat assignments form the set $\{B, W\}^3$, so $|W_0| = 2^3 = 8$ worlds.

**Announcement 0 (king):** "at least one black" eliminates the all-white world $WWW$. Remaining: $|W_1| = 8 - 1 = 7$.

**Announcement 1 ($a$ says "I don't know"):** $a$ knows $a$'s color iff all remaining $a$-alternatives agree on $a$. Agent $a$'s alternatives at $w$ flip coordinate $a$. $a$ would know only if $b = W$ and $c = W$: the alternatives are $WWB$ and $WWW$; $WWW$ is already eliminated, so in $WWB$ agent $a$ would know ($a = B$). The truthful announcement "I don't know" eliminates $WWB$:

$$|W_2| = 7 - 1 = 6 \quad (\text{remaining: } BBB, BBW, BWB, BWW, WBB, WBW)$$

**Announcement 2 ($b$ says "I don't know"):** $b$ would know iff $b$'s remaining alternatives agree on $b$. At $BBW$: alternatives $BBW, WWB$; $WWB$ is eliminated, so $b$ would know $b = B$. At $WBW$: alternatives $WBW, WWW$; $WWW$ eliminated, so $b$ would know $b = W$. The announcement eliminates $BBW$ and $WBW$:

$$|W_3| = 6 - 2 = 4 \quad (\text{remaining: } BBB, BWB, BWW, WBB)$$

**Agent $c$'s inference.** At the actual world $BBB$, agent $c$'s alternatives are $BBB$ and $BBW$. Since $BBW \notin W_3$, the only remaining $c$-alternative is $BBB$, so $c$ knows $c = B$. The model-size trajectory is:

$$8 \to 7 \to 6 \to 4$$

and the information gain of the two ignorance announcements is a reduction from $7$ to $4$ candidate worlds, i.e. a shrinkage factor of $7/4 = 1.75$.

**Pedagogical point (quantified).** The knowledge operator $K_c$ is not an extra axiom but a definable quantifier over an equivalence class; the numbers $8, 7, 6, 4$ are computed by the students themselves in the embedding, and the counter-model finder can display the four surviving worlds. This is the computed motivation for dynamic epistemic logic, which packages "announcement as model transformation" as a first-class operator.

### 4.3 Stage 3: Boolos's curious inference — what a higher-order metalogic buys

**Input (from [1]'s use of Boolos's example).** Boolos's curious inference is a first-order argument whose proof in first-order arithmetic must, for the instance with $n$ leading universal quantifier iterations, grow like a tower of exponentials, while in second-order logic (a fragment of HOL) a short uniform proof exists. The recurrence for the first-order proof length $L_n$ is:

$$L_0 = 1, \qquad L_{n+1} = 2^{L_n}$$

**Computation.**

- $L_1 = 2^{L_0} = 2^1 = 2$
- $L_2 = 2^{L_1} = 2^2 = 4$
- $L_3 = 2^{L_2} = 2^4 = 16$
- $L_4 = 2^{L_3} = 2^{16} = 65536$
- $L_5 = 2^{L_4} = 2^{65536}$. In powers of ten: $\log_{10}\left(2^{65536}\right) = 65536 \times \log_{10}(2) = 65536 \times 0.30103 = 19728.3$ (using $\log_{10}(2) = 0.30103$; check: $65536 \times 0.3 = 19660.8$ and $65536 \times 0.00103 = 67.5$; $19660.8 + 67.5 = 19728.3$). Hence $L_5 \approx 10^{19728}$.

**Pedagogical point (quantified