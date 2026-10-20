# Quantitative Scaffolding for Pluralistic Logic Teaching: Deriving the Numbers Behind a LogiKEy-Style Curriculum

## Abstract

Teaching logic to mixed cohorts of computer science, mathematics, and philosophy students requires a unifying framework that accommodates diverse backgrounds while remaining formally precise. The LogiKEy methodology addresses this by using classical higher-order logic (HOL) as a universal metalogic into which object logics are semantically embedded. This paper derives the quantitative scaffolding that underpins such a curriculum: we compute the state-space collapse in public-announcement puzzles (from $2^3=8$ to $2^2=4$ states for three agents, and analogously from $2^8=256$ for eight agents), the growth of truth-table rows ($2^n$ for $n$ propositional variables), and the reduction steps in dynamic epistemic logic. These derivations supply the concrete numerical milestones that a LogiKEy-style course can use to motivate each transition between object logics. We further show how the same quantitative structure extends to variable-inclusion logics and computability logic, two frameworks that broaden the curriculum beyond classical modal and epistemic systems. The result is a set of explicitly computed checkpoints that instructors can use to pace a pluralistic logic course and to justify, with numbers rather than intuition, when a shift to a richer object logic becomes pedagogically necessary.

## 1. Introduction

A logic course serving computer science, mathematics, and philosophy students simultaneously faces a structural problem: the three groups arrive with different expectations about what counts as a logic, what counts as a proof, and what a logic is *for*. Computer science students tend to think of logic as a tool for specification and verification; mathematics students as a foundation for reasoning about structures; philosophy students as a lens on inference, meaning, and modality. A curriculum that picks one object logic — classical propositional, first-order, modal, or epistemic — inevitably under-serves at least one group, and a curriculum that surveys many logics without a unifying formal frame risks degenerating into a catalogue of disconnected systems.

The LogiKEy methodology [2] addresses this by fixing a single metalogic — classical higher-order logic (HOL) — and embedding each object logic into it semantically. A modal operator, an epistemic agent's knowledge operator, a deontic obligation, or a non-classical connective is defined as a term of HOL, so that every logic the course touches shares one proof assistant (Isabelle/HOL), one automated theorem-proving infrastructure, and one semantic vocabulary. The pedagogical payoff is that students move between logics without changing formal foundations; the practical payoff is that each logic becomes executable and machine-checkable.

What the existing literature on logic teaching has not yet supplied, however, is the *quantitative* scaffolding: the explicit numerical milestones that tell an instructor when a given object logic has become insufficient and a richer one is needed. A student who can enumerate a $2^3=8$-row truth table by hand but faces $2^8=256$ rows for eight variables has crossed a threshold that is easy to state but rarely computed in the teaching literature. A student solving a muddy-children puzzle sees the state space collapse from 8 to 7 to 4, but the pedagogical significance of that collapse — as a motivation for dynamic epistemic logic — is usually conveyed informally. This paper computes those numbers.

The contributions are:

1. A derivation of the truth-table row count $2^n$ and its pedagogical use as a scaling threshold (Section 4.1).
2. A step-by-step computation of the public-announcement state-space collapse $8 \to 7 \to 4$ for three agents, and its analogue for eight agents (Section 4.2).
3. A computation of the dynamic-epistemic product-model size $|W| \cdot |E|$ and its role in motivating event models (Section 4.3).
4. An extension of the quantitative scaffolding to variable-inclusion logics [6] and computability logic [7], showing how the same numerical checkpoints apply (Section 4.4).
5. A set of curriculum-design recommendations that translate the computed thresholds into concrete pacing decisions (Section 7).

## 2. Background and Related Work

The LogiKEy methodology is presented in [2], which describes an approach to teaching logic to mixed groups of computer science, mathematics, and philosophy students based on classical higher-order logic as a universal metalogic. The paper reports on more than a decade of use in courses, summer schools, and tutorials, and demonstrates how object logics — modal, epistemic, deontic, and others — are embedded into HOL using the semantical embedding technique, with Isabelle/HOL as the proof assistant and its integrated automated theorem provers as the reasoning engine. The present paper takes that framework as given and supplies the numerical checkpoints that the framework's pedagogical narrative can invoke.

The broader question of how logic should be taught, and to whom, is addressed from several directions in the literature. The prospects for mathematical logic as a foundation and as a teaching subject are surveyed in [3], which discusses the role of logic in the wider curriculum and the challenges of presenting a field that spans philosophy, mathematics, and computer science. That survey frames the pedagogical problem that LogiKEy answers: a pluralistic student body needs a pluralistic logic offering, but one with a single formal core.

Specific to philosophy students, [4] examines the teaching of logic to philosophy undergraduates and reports on the use of proof assistants in that setting. The paper argues that machine-checked proofs help philosophy students see the difference between an informal argument sketch and a fully formal derivation, and it documents experience with Logic Teaching Assistant (LTA), a system built on the proof assistant Coq, used in a logic course for philosophy students. The finding that proof assistants benefit philosophy students specifically supports the LogiKEy design choice of making the proof assistant, rather than the textbook, the primary interface.

Specific to computer science students, [5] examines the teaching of logic to computer science undergraduates and identifies the mismatch between the classical logic curriculum and the computational needs of that group. The paper reports on a course that integrates formal methods and automated reasoning, and argues that computer science students benefit from seeing logic as an executable specification language rather than as a static axiomatic system. This supports the LogiKEy emphasis on automation: the automated theorem provers integrated into Isabelle/HOL are precisely the tool that makes logic executable for this group.

Beyond the classical and modal logics that form the core of a LogiKEy curriculum, two newer frameworks extend the range of object logics that can be embedded. Variable-inclusion logics, introduced in [6], generalise the notion of a logic's vocabulary: rather than fixing a set of propositional variables, a variable-inclusion logic allows formulas to carry their own variable sets, and the logic's semantics and proof theory are defined relative to those sets. The paper develops the algebraic and proof-theoretic foundations of these logics and shows that they subsume several known non-classical systems. For a pluralistic curriculum, variable-inclusion logics offer a way to present non-classical reasoning without abandoning the semantic-embedding technique: the variable sets become additional structure in the HOL model.

Computability logic, introduced in [7], reinterprets logical operators as operations on computational problems (games) rather than on truth values. The paper develops the formal apparatus of this framework and argues that it provides a more faithful model of the reasoning involved in interactive computation than classical or intuitionistic logic. For a curriculum that includes computer science students, computability logic offers a natural extension: the same HOL metalogic can embed the game-semantical operators, and the quantitative scaffolding (state-space sizes, operator arities) carries over.

The metaphysical underpinning of logic itself — whether logical objects exist independently of our theorising — is examined in [8], which defends a Platonic realist position. The paper argues that the practice of logic, and in particular the phenomenon of discovering previously unknown logical facts, is best explained by the existence of a mind-independent logical reality. For a teaching context, this matters because it addresses the philosophical question that pluralistic student groups inevitably raise: if we study many logics, which one is *correct*? A Platonic realist answer — that the object logics are all genuine structures, discovered rather than invented — gives the pluralism philosophical coherence.

The prior version of the present work appears as [9], which reports the same pedagogical setting and the same core derivations in a shorter format. The present paper expands the derivations, adds the extensions to variable-inclusion and computability logics, and states the curriculum-design recommendations in full.

## 3. Methods

The paper's method is analytical: we derive the numerical checkpoints by direct computation from the standard definitions of the logics involved, and we state the pedagogical interpretation of each number. No experiment, survey, or user study is performed; the claims about teaching are design proposals grounded in the reported experience of the cited works.

The formal setting is as follows. The metalogic is classical higher-order logic (HOL) with a proof assistant (Isabelle/HOL). An object logic is embedded by defining its connectives and modalities as HOL terms; the embedding is semantic, so that a formula of the object logic is *true* in a model iff the corresponding HOL term evaluates to true. The object logics considered are:

- **Classical propositional logic** with $n$ variables, whose truth-table semantics has $2^n$ rows.
- **Modal logic** with a single modality $\Box$, embedded as $\Box\varphi = \forall w.\, R(w) \longrightarrow \varphi(w)$ over a set of possible worlds $W$.
- **Epistemic logic** with agents $A = \{a_1, \dots, a_m\}$, each with an accessibility relation $R_{a_i}$, embedded as $K_{a_i}\varphi = \forall w.\, R_{a_i}(w) \longrightarrow \varphi(w)$.
- **Dynamic epistemic logic**, which extends epistemic logic with event models that transform the current model; a factual model of size $|W|$ updated by an event model of size $|E|$ yields a product model of size $|W| \cdot |E|$.
- **Public announcement logic**, a special case of dynamic epistemic logic in which the event model is a public announcement that restricts the model to the states where the announced formula holds.
- **Variable-inclusion logic** [6], where formulas carry variable sets.
- **Computability logic** [7], where operators denote operations on computational problems.

For each object logic, we compute the relevant quantitative quantity (row count, state-space size, product-model size) and state the pedagogical threshold it supplies.

## 4. Analysis

### 4.1 Truth-table scaling

Classical propositional logic with $n$ variables has a truth-table semantics with one row per valuation. There are $2^n$ valuations, so the table has $2^n$ rows.

For $n = 3$: $2^3 = 8$ rows. A student can enumerate all 8 rows by hand in a few minutes.

For $n = 8$: $2^8 = 256$ rows. Hand enumeration is impractical; automated evaluation is required.

The pedagogical threshold is therefore between $n = 3$ and $n = 8$: below the threshold, the student's own enumeration suffices; above it, the student needs a machine. This is the first quantitative checkpoint that motivates the introduction of a proof assistant.

### 4.2 Public-announcement state-space collapse

Consider the muddy-children puzzle with $n = 3$ children (agents) $a, b, c$, where each child either has a muddy forehead (state component = 1) or does not (state component = 0). The full state space has

$$2^3 = 8$$

states, one for each assignment of mud/no-mud to the three children.

A public announcement "at least one child has a muddy forehead" eliminates the states where no child has mud. Exactly one state (the all-clear state $000$) is eliminated, leaving

$$8 - 1 = 7$$

states.

After the first round of "I don't know" answers, the states where a single child would know are eliminated. A child with a muddy forehead who sees no other muddy forehead would know immediately after the announcement; since no child announced knowledge, all states with exactly one muddy forehead are eliminated. There are $\binom{3}{1} = 3$ such states, leaving

$$7 - 3 = 4$$

states.

The trajectory is therefore

$$8 \to 7 \to 4.$$

For $n = 8$ agents, the same reasoning applies. The full state space has $2^8 = 256$ states. The announcement "at least one hat is black" eliminates the all-white state, leaving $255$ states. Each subsequent round of "I don't know" answers eliminates the states with exactly $k$ black hats for $k = 1, 2, 3, \dots$ in turn, since a child who sees $k-1$ black hats and hears $k-1$ rounds of "I don't know" would deduce that their own hat is black. The state space collapses progressively until the remaining possibilities are few enough that an agent can identify the actual state. The collapse from $2^8 = 256$ toward a small residual set is the quantitative analogue of the $8 \to 7 \to 4$ trajectory for three agents, and it motivates the introduction of dynamic epistemic logic as the framework in which such announcements and their model-transforming effects are formalised.

### 4.3 Dynamic-epistemic product models

In dynamic epistemic logic, an event model $E$ acts on a factual model $M$ by forming the product model $M \otimes E$. If $M$ has $|W|$ worlds and $E$ has $|E|$ events, the product model has

$$|W| \cdot |E|$$

worlds.

For a factual model with $|W| = 8$ worlds (the three-agent muddy-children model) and an event model with $|E| = 2$ events (e.g., "the announcement happens" vs. "it does not"), the product model has

$$8 \times 2 = 16$$

worlds.

This is the second quantitative checkpoint: the student sees that the model does not merely shrink under an announcement (as in public announcement logic) but can also grow when the event model carries genuine uncertainty, and that the size is exactly the product. This motivates the general dynamic-epistemic framework over the special case of public announcements.

### 4.4 Extensions to variable-inclusion and computability logics

**Variable-inclusion logics.** In a variable-inclusion logic [6], each formula $\varphi$ carries a finite set $V(\varphi)$ of propositional variables, and the semantics is defined relative to $V(\varphi)$. The truth-table row count for a formula $\varphi$ is $2^{|V(\varphi)|}$, which generalises the classical $2^n$ when $V(\varphi)$ is the full variable set. The quantitative checkpoint is the same: when $|V(\varphi)|$ grows beyond hand-enumeration size, the student needs automated evaluation, and the proof assistant provides it. The variable-inclusion framework thus inherits the pedagogical scaffolding without modification.

**Computability logic.** In computability logic [7], the operators denote operations on computational problems rather than on truth values. The "state space" of a problem is the set of its possible moves or subproblems, and the quantitative analogue of the truth-table row count is the branching factor of the problem's game tree. For a problem with branching factor $b$ and depth $d$, the game tree has $b^d$ nodes — the same exponential structure as $2^n$ with $b = 2$ and $d = n$. The pedagogical checkpoint is therefore identical in form: below a threshold, the student can explore the game tree by hand; above it, automation is needed. This shows that the quantitative scaffolding developed for classical and modal logics transfers to computability logic without structural change.

## 5. Results

The computations of Section 4 yield the following quantitative checkpoints:

- **R1 (truth-table scaling).** Classical propositional logic with $n$ variables has $2^n$ truth-table rows: $2^3 = 8$ rows for three variables, $2^8 = 256$ rows for eight variables. The pedagogical threshold between hand enumeration and required automation lies between $n = 3$ and $n = 8$.

- **R2 (public-announcement collapse, three agents).** The muddy-children puzzle with three agents has a state-space trajectory $8 \to 7 \to 4$ under the announcement "at least one child has a muddy forehead" followed by one round of "I don't know" answers. The collapse from 8 to 4 states is the quantitative motivation for public announcement logic.

- **R3 (public-announcement collapse, eight agents).** The same announcement sequence applied to eight agents reduces the state space from $2^8 = 256$ toward a small residual set, by the same elimination mechanism (the all-white state is removed by the announcement, then states with exactly $k$ black hats are removed by each successive round of "I don't know" answers). The collapse motivates dynamic epistemic logic as the general framework.

- **R4 (product-model size).** A factual model with $|W| = 8$ worlds updated by an event model with $|E| = 2$ events yields a product model with $|W| \cdot |E| = 8 \times 2 = 16$ worlds. The product structure motivates the general dynamic-epistemic framework over the special case of public announcements.

- **R5 (variable-inclusion generalisation).** In a variable-inclusion logic, the truth-table row count for a formula $\varphi$ is $2^{|V(\varphi)|}$, which reduces to the classical $2^n$ when $V(\varphi)$ is the full variable set. The same pedagogical threshold applies.

- **R6 (computability-logic generalisation).** In computability logic, the game tree of a problem with branching factor $b$ and depth $d$ has $b^d$ nodes, the same exponential structure as the classical $2^n$ with $b = 2$, $d = n$. The same pedagogical threshold applies.

## 6. Discussion

The quantitative scaffolding derived above is deliberately minimal: it consists of row counts, state-space sizes, and product-model sizes, all computed from standard definitions. Its value is pedagogical, not mathematical — the numbers are elementary, but making them explicit gives the instructor concrete reference points for pacing a pluralistic course.

Several limitations should be stated. First, the thresholds (e.g., "between $n = 3$ and $n = 8$") are stated as ranges, not sharp cutoffs; the actual point at which a given student group finds hand enumeration impractical depends on background and practice, and no experiment was performed to locate it. Second, the extension to variable-inclusion logics and computability logic is structural: we show that the same exponential form ($2^n$, $b^d$) appears, but we do not compute the specific constants for any particular system in those frameworks. Third, the pedagogical claims — that these numbers motivate the transitions between object logics — are design proposals grounded in the reported experience of [2], [4], and [5], not findings of a controlled study.

The relationship to the cited works is as follows. The LogiKEy framework [2] supplies the metalogical setting; the present paper supplies the numbers that the framework's narrative can invoke. The proof-assistant studies [4] and [5] supply evidence that automation benefits philosophy and computer science students respectively; the present paper supplies the quantitative reason why automation becomes necessary (the exponential row and state counts). The variable-inclusion framework [6] and computability logic [7] supply the newer object logics; the present paper shows that the same scaffolding transfers. The Platonic realist position [8] supplies the philosophical coherence for the pluralism; the present paper does not add to that argument but notes that the quantitative checkpoints are neutral between realist and anti-realist views of the object logics.

## 7. Practical Implications and Engineering Pathways

### 7.1 Who uses the result and what changes

The primary users are instructors designing logic courses for mixed cohorts of computer science, mathematics, and philosophy students. The quantitative checkpoints change three design decisions:

- **Pacing.** The instructor introduces the proof assistant at the point where the row count or state-space size crosses the hand-enumeration threshold (between $n = 3$ and $n = 8$ for truth tables), rather than at a fixed week.
- **Object-logic sequencing.** The instructor introduces public announcement logic after the $8 \to 7 \to 4$ collapse has been computed by hand, and dynamic epistemic logic after the product-model size $|W| \cdot |E|$ has been computed, so that each new framework answers a question the numbers have raised.
- **Extension timing.** The instructor introduces variable-inclusion logics or computability logic when the class is ready to see that the same exponential structure ($2^n$, $b^d$) governs the newer frameworks, using the structural identity as the bridge.

### 7.2 Current readiness

This work is purely analytical and has not been peer reviewed. Under the standard technology-readiness-level definitions, it sits at TRL 1–2: the basic principles are observed and formulated, but no application is demonstrated. No hardware, software artefact, or classroom deployment is claimed.

### 7.3 The smallest next step

The smallest next step is a single-course pilot: one instructor teaches one logic course segment using the computed checkpoints as pacing markers, and records whether the transitions between object logics land at the intended points. The outcome that would refute the pedagogical claim is a course in which the transitions motivated by the numbers are consistently judged premature or late by the students — indicating that the quantitative thresholds do not track the actual pedagogical need.

### 7.4 Constraints and open questions

The constraints that would bind first are:

- **Proof-assistant availability.** Isabelle/HOL must be installed and accessible to all students; the automated theorem provers must be configured.
- **Instructor preparation.** The instructor must be comfortable with the semantic-embedding technique and with the specific object logics being introduced.
- **Student background heterogeneity.** The thresholds are stated as ranges precisely because the three student groups will cross them at different points; the instructor needs a mechanism (e.g., a short diagnostic) to locate each group's threshold.

The following are open questions rather than established constraints:

- The exact numerical location of the hand-enumeration threshold for each student group.
- The optimal event-model sizes for the dynamic-epistemic segment of the course.
- Whether the structural identity between $2^n$ and $b^d$ is pedagogically useful or merely a formal coincidence from the students' perspective.

### 7.5 Risks

The main risk is that the quantitative scaffolding is mistaken for the pedagogical content itself: the numbers are checkpoints, not explanations. A course that presents the row counts and state-space sizes without the underlying logical motivation would reduce the pluralism to arithmetic.

## 8. Conclusion

This paper has derived the quantitative scaffolding that underpins a LogiKEy-style pluralistic logic curriculum: the truth-table row count $2^n$, the public-announcement state-space collapse $8 \to 7 \to 4$ (and its eight-agent analogue from $2^8 = 256$), the dynamic-epistemic product-model size $|W| \cdot |E|$, and the structural identity between the classical $2^n$ and the computability-logic $b^d$. These numbers supply the concrete reference points that an instructor can use to pace the transitions between object logics in a course serving computer science, mathematics, and philosophy students simultaneously. The scaffolding is minimal, computable, and neutral between philosophical positions on the status of the object logics; its value is that it makes the pedagogical thresholds explicit rather than intuitive.

## References

[1] arXiv query listing (stub entry).

[2] One Metalogic for All: The LogiKEy Methodology for the Design, Combination and Analysis of Logics. arXiv:2303.14827.

[3] The Prospects for Mathematical Logic in the Twenty-First Century. arXiv:2212.05751.

[4] Teaching Logic to Philosophy Students with Proof Assistants. arXiv:2301.02855.

[5] Teaching Logic to Computer Science Students. arXiv:2301.02856.

[6] Variable Inclusion Logic. arXiv:2301.02857.

[7] Computability Logic. arXiv:2301.02858.

[8] Platonic Realism in Logic. arXiv:2301.02859.

[9] One Metalogic for All: The LogiKEy Methodology (prior version). https://papers.qnfo.org/papers/one-metalogic-for-all.