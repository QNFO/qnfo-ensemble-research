# Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and Capability versus Intention

## Abstract

In the graph model for conflict resolution (GMCR), a decision maker (DM) either moves the conflict to another state or does nothing; every action that leaves the state unchanged is silently classified as inaction. Yet announcements, exercises, leaks, and selective disclosures leave the physical state unchanged while altering what other DMs believe about which moves are available and which moves others would want to make. We formalize such state-preserving actions by augmenting each state with the DMs' epistemic states: a physical move changes the physical state, a state-preserving action changes only the epistemic state, and inaction is the absence of any transition. Actions generate evidence through observer-specific interpretation maps, evaluated in a four-valued logic that separates evidence for and against each perceived move. We prove directionality results: evidence for a move can only enable perceived moves, evidence against can only disable them, two of the four reduction operators discard one kind of evidence, and contradictory assessments are absorbing under monotone accumulation. Combined with monotonicity of stability in move sets, this fixes the direction in which any action shifts a DM's stability judgements and characterizes when actions enable provocation or deterrence. Capability assessments affect all sanction-based stability concepts and, on a DM's own side, Nash stability; intention assessments affect only sequential stability. A worked four-state model shows general metarationality collapsing four states into one stability class while sequential stability separates them, and that disabling a single sanction move expands the sequentially stable set from $3$ to $4$ states.

## 1. Introduction

The graph model for conflict resolution [1] models a conflict as a directed graph whose vertices are states and whose colored edges are the moves available to each decision maker (DM). The classical definitions are deliberately spare: at any state, a DM either moves along one of her arcs to a successor state or does nothing. Inaction, however, is left implicit. Any "action" that leaves the state unchanged is therefore, by definition, doing nothing.

This spareness hides a class of strategically central behaviors. A trade association's public announcement that it *could* retaliate, a military exercise conducted near a border, a leak of internal correspondence, a selective disclosure of one clause of a draft agreement — none of these changes the physical state of the world, yet each changes what other DMs believe about which moves are available (capability) and which moves others would want to make (intention). Treating them as inaction makes them invisible to the model precisely when they are doing the most work.

We introduce **state-preserving actions** as first-class citizens. The device is an augmentation of each physical state with the DMs' epistemic states. A physical move changes the physical component; a state-preserving action changes only the epistemic component; inaction is the absence of a transition in either component. Actions generate evidence, and evidence is interpreted observer-specifically: the same announcement may be read as a credible threat by one DM and as noise by another.

Our epistemic bookkeeping is four-valued, building on the Quasi-Closed World Graph Model (QCW-GMCR) [3] and on four-valued state definitions for conflict analysis [6]. For each DM $i$ and each move $m$ that $i$ believes another DM might make, the observer's assessment is one of four values: supported ($T$), refuted ($F$), contradictory ($T \wedge F$), or undecided ($N$). This separates evidence for from evidence against, which is essential because the two kinds act in opposite directions: evidence for a move can only enable it in the observer's perceived model, evidence against can only disable it.

The contribution is threefold. First, a formal framework in which state-preserving actions, physical moves, and inaction are distinct, with observer-specific interpretation maps. Second, structural results: directionality of evidence, the behavior of the four reduction operators, absorption of contradiction under monotone accumulation, and the induced monotonicity of stability judgements in the perceived move sets — which together fix the direction in which any action moves a DM's stability conclusions and characterize when actions can enable provocation or deterrence. Third, a distinction between capability assessments, which affect all sanction-based stability concepts and, on the DM's own side, Nash stability, and intention assessments, which affect only sequential stability. A worked example in the style of the 1995 DVD format negotiation illustrates why general metarationality cannot distinguish phases of such a conflict while sequential stability can.

## 2. Background and Related Work

The graph model for conflict resolution [1] is the base formalism: states, DMs, oriented arcs of moves, and preference rankings, with stability concepts (Nash, general metarationality, symmetric metarationality, sequential stability) defined on top. The present work extends [1] by splitting the implicit "do nothing" into inaction proper and state-preserving epistemic action; the extension is conservative in that when no state-preserving actions occur, all classical definitions are recovered verbatim.

The four-valued substrate comes from two lines of the author's earlier work. The QCW-GMCR paper [3] extends GMCR with Belnap's four-valued logic [3] to represent option-level epistemic ambiguity, with compositional propagation of four-valued option assignments and a machine-checked Lean 4 formalization; our epistemic states and reduction operators are the move-level analogue of its option-level machinery, and the Lean formalization suggests the present extension is similarly mechanizable. The state-definition paper [6] argues that describing a state purely as a combination of strategies is insufficient for a functioning decision framework when DMs hold uncertain or partial descriptions; our augmentation of physical states with epistemic states is a direct answer to that critique at the level of moves rather than options.

Several adjacent literatures supply methodological analogies. The quantum semigroup actions paper [4] studies continuous actions of a quantum semigroup on a finite quantum space and shows such actions factor through the quantum Bohr compactification; the structural lesson we borrow is that a one-parameter family of state-preserving transformations acting on a state space can be analyzed through the invariant structure it preserves — here, the physical state is the invariant and the epistemic state is what the semigroup of announcements and disclosures acts upon. The G-CSEA algorithm [5] extracts conflict sets causing infeasibility in pseudo-Boolean workforce-scheduling models via graph search; its discipline of isolating minimal conflicting subsets of constraints parallels our reduction operators, which isolate which evidence items actually bear on a perceived move. The generalized Turán paper [7] develops counting tools $\mathrm{ex}(n, T, F)$ for clique counts in $F$-free graphs; we use counting of the same flavor — though at elementary scale — when we enumerate reachable epistemic states as a product over perceived moves. The 3D graph drawing paper [8] proves bend and angle bounds for low-degree graphs; it is a reminder that representation choices for graph models (here, augmenting vertices with epistemic labels rather than thickening edges) carry provable consequences for what is readable. The cosmic-ray measurement paper [9] reports a flux measurement above $10^{17.2}\,\mathrm{eV}$ with explicit detector, photo-tube, and atmospheric calibrations; its separation of raw events from observer-calibrated interpretation is the exact template for our observer-specific interpretation maps, in which the same physical event yields different evidence for different DMs.

Finally, the QNFO corpus situates the motivation. The statements-to-questions poster [10] argues that conflict often begins with speech hardened into statements that conceal their enabling assumptions, and proposes AI as epistemic repair infrastructure; state-preserving actions give that diagnosis a game-theoretic substrate, since an announcement is precisely an action that reshapes the epistemic layer without touching the physical one. Agentic Collapse [11] documents failure modes of autonomous agents under degraded epistemic environments, relevant to our absorbing-contradiction result as a model of epistemic lock-in. Impact of Cognitive Linearity on Epistemic Modeling [12] studies how linear cognitive processing distorts epistemic models, motivating our monotone accumulation assumption as a deliberately linear — and therefore falsifiable — idealization. Mechanistic-Ethics [13] grounds normative evaluation in mechanism rather than outcome, echoing our separation of capability (what a DM can do) from intention (what a DM would want), which is itself an ethical as much as a strategic distinction.

## 3. Methods

### 3.1 Base model

A graph model [1] is a tuple $G = (S, \{A_i\}_{i \in N}, \{\succ_i\}_{i \in N})$ where $S$ is a finite state set, $N$ is the finite DM set, $A_i \subseteq S \times S$ is DM $i$'s move relation, and $\succ_i$ is DM $i$'s strict preference order on $S$. Write $R_i(s) = \{s' \in S : (s, s') \in A_i\}$ for the moves reachable by $i$ from $s$.

### 3.2 Epistemic augmentation

Fix an observer DM $o$. For each opponent $j \neq o$ and each potential move $m \in S \times S$ of $j$, the observer maintains a four-valued assessment:

$$a_o(m) \in \{T, F, N, B\},$$

where $T$ means supported (the move is believed available and intended), $F$ refuted, $N$ undecided, and $B$ both (contradictory evidence). We split each assessment into a capability component $a_o^{c}(m)$ (is the move available?) and an intention component $a_o^{w}(m)$ (would $j$ want to make it?). The observer's perceived move set is:

$$R_j^{o}(s) = \{m = (s, s') : a_o^{c}(m) \in \{T, B\}\}.$$

A state of the augmented model is a pair $\sigma = (s, \mathbf{a}_o)$ with $s \in S$ the physical state and $\mathbf{a}_o$ the profile of assessments. Transitions come in three kinds:

1. **Physical move** by DM $i$: $(s, \mathbf{a}_o) \to (s', \mathbf{a}_o)$ with $(s, s') \in A_i$; the epistemic component is unchanged.
2. **State-preserving action** by DM $i$: $(s, \mathbf{a}_o) \to (s, \mathbf{a}_o')$ with $s' = s$ and $\mathbf{a}_o' \neq \mathbf{a}_o$; only the epistemic component changes.
3. **Inaction**: no transition.

An **interpretation map** $\iota_o : E \to \mathcal{P}(\{T, F\})$ assigns to each evidence item $e$ in a global evidence stream $E$ the bits it supplies to observer $o$; the same $e$ may supply $T$ to one observer and $F$ to another.

### 3.3 Accumulation and reduction

Assessments update by monotone accumulation: each observer accumulates evidence bits per move, with $T$-bits and $F$-bits counted separately. A **reduction operator** $\rho$ maps the pair of accumulated counts $(p_m, n_m)$ for move $m$ to a four-valued assessment. The four canonical operators are:

$$\rho_1(p_m, n_m) = \begin{cases} T & p_m > 0,\ n_m = 0 \\ F & p_m = 0,\ n_m > 0 \\ B & p_m > 0,\ n_m > 0 \\ N & p_m = 0,\ n_m = 0 \end{cases}$$

(uses both kinds); $\rho_2(p_m, n_m) = T$ if $p_m > 0$ else $N$ (ignores evidence against); $\rho_3(p_m, n_m) = F$ if $n_m > 0$ else $N$ (ignores evidence for); and $\rho_4(p_m, n_m) = N$ always (ignores both). Thus two of the four operators, $\rho_2$ and $\rho_3$, ignore one kind of evidence entirely, and $\rho_4$ ignores both.

### 3.4 Stability concepts

For DM $o$ at physical state $s$ with perceived move sets $\{R_j^{o}\}$:

- **Nash stability** [1]: $s$ is Nash stable for $o$ if no move $o$ herself can make leads to a state $o$ prefers.
- **General metarationality (GMR)** [1]: $s$ is GMR-stable for $o$ if for every move $o$ can make to $s'$, some opponent $j$ has a response from $s'$ to a state $o$ likes less than $s$ (a sanction).
- **Sequential stability (SEQ)** [1]: as GMR, but the sanctioning response must itself be a move the opponent would make — formally, the response must terminate in a state that is sequentially stable for the opponent. SEQ therefore asks not merely whether a sanction *could* occur but whether it *would*.

## 4. Analysis

### 4.1 Directionality of evidence

**Proposition 1 (Enable/disable directionality).** Under accumulation with any operator $\rho \in \{\rho_1, \rho_2, \rho_3\}$, adding a $T$-bit for move $m$ can only change $a_o^{c}(m)$ from $\{N, F\}$ toward $\{T, B\}$, never the reverse; adding an $F$-bit can only change it toward $\{F, B\}$, never toward $\{T, N\}$.

*Proof.* By inspection of the operator tables in Section 3.3: for $\rho_1$, the assessment as a function of $(p_m, n_m)$ moves monotonically in the lattice $N \prec T, F \prec B$ as $p_m$ or $n_m$ crosses $0$; increasing $p_m$ never decreases the $T$-component and increasing $n_m$ never decreases the $F$-component. For $\rho_2$ the assessment depends only on $p_m$, so $F$-bits leave it unchanged and $T$-bits can only move $N \to T$; symmetrically for $\rho_3$. Since $R_j^{o}(s)$ includes $m$ iff $a_o^{c}(m) \in \{T, B\}$, and the $T$-component is monotone in $p_m$, evidence for $m$ can only grow $R_j^{o}$ and evidence against can only shrink it. $\square$

**Proposition 2 (Absorption of contradiction).** Under $\rho_1$ with monotone accumulation (counts never decrease), any move $m$ for which both a $T$-bit and an $F$-bit arrive has $a_o(m) = B$ at that moment and forever after, since $p_m > 0$ and $n_m > 0$ remain true under any further accumulation.

*Proof.* Once $p_m \geq 1$ and $n_m \geq 1$, monotonicity gives $p_m \geq 1$ and $n_m \geq 1$ at all later times, and $\rho_1(p_m, n_m) = B$ whenever both counts are positive. $\square$

### 4.2 Counting reachable epistemic states

Consider an observer tracking $k = 3$ perceived candidate moves of a single opponent, each independently in $\{T, F, N, B\}$ under $\rho_1$. The number of reachable epistemic profiles is:

$$|\{T, F, N, B\}|^{k} = 4^{3} = 64.$$

Of these, the profiles containing a contradiction on at least one move — the absorbing states of Proposition 2 — number:

$$4^{3} - 3^{3} = 64 - 27 = 37,$$

since contradiction-free profiles restrict each coordinate to $\{T, F, N\}$, giving $3^{3} = 27$. Thus $37/64 = 0.578125$ of the epistemic state space is absorbing under monotone accumulation: a majority of the observer's possible epistemic conditions are terminal once contradiction is admitted.

### 4.3 Worked stability model

We construct a minimal model in the style of the 1995 DVD format negotiation [1], with two DMs: DM 1 (a technology alliance) and DM 2 (the computer industry group). States $S = \{s_1, s_2, s_3, s_4\}$; moves:

$$A_1 = \{(s_1, s_2), (s_2, s_1)\}, \qquad A_2 = \{(s_1, s_3), (s_3, s_1), (s_2, s_4), (s_4, s_2)\}.$$

Preferences: DM 1 ranks $s_4 \succ_1 s_1 \succ_1 s_2 \succ_1 s_3$; DM 2 ranks $s_3 \succ_2 s_2 \succ_2 s_4 \succ_2 s_1$.

**Nash stability for DM 1.** From $s_1$, DM 1's only move is to $s_2$, and $s_1 \succ_1 s_2$, so no improving move: $s_1$ is Nash stable. From $s_2$, DM 1 can move to $s_1 \succ_1 s_2$: not stable. From $s_3$ and $s_4$, DM 1 has no moves in $A_1$: stable by vacuity. Nash stable set for DM 1:

$$\mathrm{Nash}_1 = \{s_1, s_3, s_4\}, \qquad |\mathrm{Nash}_1| = 3.$$

**GMR for DM 1.** From $s_2$, DM 1's move to $s_1$ can be sanctioned: DM 2 responds $(s_1, s_3) \in A_2$, and $s_3$ is DM 1's worst state, so the sanction hurts DM 1. Hence $s_2$ is GMR-stable. From $s_1$: no improving move, stable. From $s_3, s_4$: no moves, stable. Therefore:

$$\mathrm{GMR}_1 = \{s_1, s_2, s_3, s_4\}, \qquad |\mathrm{GMR}_1| = 4.$$

GMR collapses all four states into one stability class: DM 2 can always sanction, so every unilateral departure by DM 1 is deterred in the GMR sense. This is the formal content of the observation in [1] that general metarationality cannot distinguish the phases of the DVD negotiation, since the computer industry group could always sanction.

**SEQ for DM 1.** The sanction at $s_2$ requires DM 2 to move $(s_1, s_3)$. Is $s_3$ a credible terminal for DM 2? At $s_3$, DM 2's only move is $(s_3, s_1)$, and $s_3 \succ_2 s_1$, so DM 2 has no improving move from $s_3$; $s_3$ is Nash stable for DM 2, hence sequentially stable. The sanction is therefore credible, and $s_2$ is **not** SEQ-stable for DM 1:

$$\mathrm{SEQ}_1 = \{s_1, s_3, s_4\}, \qquad |\mathrm{SEQ}_1| = 3.$$

Sequential stability, which asks whether the computer industry group *would* sanction rather than merely whether it *could*, separates the phases that GMR merges.

### 4.4 Epistemic disturbance on the worked model

Now let a state-preserving action by DM 2 — say, a public statement casting doubt on its willingness to fight — generate, for observer DM 1, an $F$-bit against the capability of DM 2's sanctioning move $m^{\ast} = (s_1, s_3)$. By Proposition 1, this can only disable $m^{\ast}$ in DM 1's perceived model: $R_2^{1}(s_1)$ shrinks from $\{(s_1, s_3)\}$ to $\varnothing$. Recomputing SEQ for DM 1 in the perceived model: from $s_2$, the move to $s_1$ now meets no available sanction, so $s_2$ becomes SEQ-stable:

$$\mathrm{SEQ}_1^{\text{post}} = \{s_1, s_2, s_3, s_4\}, \qquad |\mathrm{SEQ}_1^{\text{post}}| = 4.$$

The expansion is $|\mathrm{SEQ}_1^{\text{post}}| - |\mathrm{SEQ}_1| = 4 - 3 = 1$ state, a relative increase of $1/3 \approx 0.333$. Conversely, an action generating a $T$-bit for $m^{\ast}$ (an exercise demonstrating capability) can only confirm the sanction and shrink or hold the stable set; in this model it holds it at $3$, since $s_2$ was already excluded. This is the sense in which the direction of an action's effect on stability judgements is fixed by the direction of the evidence it supplies.

### 4.5 Capability versus intention

In the worked model, the disturbance in Section 4.4 was a **capability** assessment: it removed a move from $R_2^{1}$ and thereby removed a sanction from consideration, affecting the sanction-based concepts GMR and SEQ alike (had the $F$-bit arrived before GMR was evaluated, $s_2$ would have been GMR-unstable too, since the only sanctioning response would have been unavailable). An **intention** assessment — evidence about whether DM 2 *would want* to play an available $m^{\ast}$ — leaves $R_2^{1}$ intact and therefore leaves GMR untouched, but changes SEQ, whose credibility test consults the opponent's willingness. Capability assessments thus affect all sanction-based stability concepts, and on the DM's own side also Nash stability (evidence about one's own available moves changes one's own move set); intention assessments affect only sequential stability.

## 5. Results

All numbers below are computed in Section 4 from the stated model; none are empirical measurements.

- **R1 (Epistemic state space).** With $k = 3$ perceived candidate moves and four-valued assessments, the observer's epistemic state space has $4^{3} = 64$ profiles, of which $64 - 27 = 37$ are absorbing contradictory profiles under monotone accumulation with $\rho_1$; the absorbing fraction is $37/64 = 0.578125$.
- **R2 (Reduction operators).** Of the four canonical reduction operators, exactly two ($\rho_2$, $\rho_3$) ignore one kind of evidence and one ($\rho_4$) ignores both; only $\rho_1$ is evidence-complete.
- **R3 (Stability separation).** In the four-state DVD-style model, the Nash and SEQ stable sets for DM 1 coincide at size $|\mathrm{SEQ}_1| = |\mathrm{Nash}_1| = 3$, while GMR yields $|\mathrm{GMR}_1| = 4$: general metarationality cannot distinguish the conflict's phases, sequential stability can.
- **R4 (Disturbance effect).** A state-preserving action supplying one $F$-bit against the sanction move $m^{\ast} = (s_1, s_3)$ expands DM 1's sequentially stable set from $3$ to $4$ states, an increase of $1$ state, i.e., a relative expansion of $1/3 \approx 0.333$; a $T$-bit for $m^{\ast}$ leaves the set at $3$.
- **R5 (Projection, stated assumptions).** For a model with $k$ perceived candidate moves, the absorbing contradictory fraction under $\rho_1$ is $(4^{k} - 3^{k})/4^{k} = 1 - (3/4)^{k}$, assuming independent per-move accumulation. For $k = 3$ this reproduces R1 ($1 - 27/64 = 0.578125$); for $k = 10$ it projects to $1 - (3/4)^{10} = 1 - 0.0576\ldots \approx 0.9424$, so in larger models nearly the whole epistemic space is absorbing once contradiction is possible. The projection assumes independence of per-move evidence streams; correlated evidence would alter it.

## 6. Discussion

**Limitations.** The worked model is deliberately minimal: four states, two DMs, hand-chosen preferences chosen to exhibit the GMR/SEQ separation. Real conflicts, including the actual 1995 DVD negotiation, have richer move structures, and the qualitative claim that GMR merges phases while SEQ separates them is demonstrated here only on the constructed instance, not established as a theorem for all DVD-like models. The monotone accumulation assumption is a linear idealization in the spirit of the critique in [12]: real DMs revise, discount, and forget evidence, and any of these would break Proposition 2's absorption result. The independence assumption behind the R5 projection is strong; correlated leaks or announcements would reduce the absorbing fraction.

**Failure modes.** If an observer's interpretation map is mis-calibrated — the analogue of an uncorrected atmospheric calibration in [9] — evidence directionality (Proposition 1) still holds relative to the map, but the map itself may invert the strategic meaning of an action; the framework diagnoses this only if the analyst models the mis-calibration explicitly. The capability/intention split assumes these are cleanly separable assessments; in practice a leak may carry both kinds of evidence at once, and the reduction operators then route it to both components, which the current formalism permits but does not analyze.

**What would falsify the claims.** Proposition 1 would fail if a reduction operator allowed $T$-evidence to disable a move; any counterexample would be a non-monotone operator outside our canonical four, which would itself be worth cataloguing. The claim that intention assessments leave GMR untouched would fail if GMR's sanction test were reformulated to include credibility, which some GMCR variants do; our claim is relative to the classical definitions of [1]. The absorbing-fraction projection would fail empirically if real evidence streams are strongly negatively correlated across moves.

**Open questions.** Can the Lean 4 methodology of [3] mechanize Propositions 1 and 2? Does the semigroup-structure viewpoint of [4] yield a compactification theorem for families of state-preserving actions? How do the conflict-set extraction techniques of [5] transfer to extracting minimal evidence sets responsible for a stability flip? And can the epistemic-repair framing of [10] be given a formal counterpart as a sequence of state-preserving actions designed to move observers out of absorbing contradictory states — noting that Proposition 2 shows ordinary accumulation cannot do so, so repair must act on the accumulation rule itself, a point with ethical dimension in the sense of [13] and failure-mode urgency in the sense of [11].

## 7. Conclusion

State-preserving actions — announcements, exercises, leaks, selective disclosures — are neither moves nor inaction, and classical GMCR [1] renders them invisible. By augmenting states with four-valued epistemic assessments in the lineage of [3] and [6], we made them first-class: they change only the epistemic component, act through observer-specific interpretation maps, and move stability judgements in a fixed direction fixed by evidence directionality. Contradiction is absorbing under monotone accumulation — $37$ of $64$ epistemic profiles at $k = 3$, and by projection $1 - (3/4)^{k}$ in general — so epistemic lock-in is the generic condition, not the exception. The capability/intention distinction maps cleanly onto the stability hierarchy: capability affects all sanction-based concepts and one's own Nash stability; intention affects only sequential stability. The DVD-style example shows why this matters: where general metarationality sees one undifferentiated phase ($|\mathrm{GMR}_1| = 4$), sequential stability sees structure ($|\mathrm{SEQ}_1| = 3$), and a single state-preserving action can move the boundary ($|\mathrm{SEQ}_1^{\text{post}}| = 4$). Conflict analysis that cannot represent the speech acts that shape beliefs is analysis of the wrong object; this paper supplies the missing representational layer and its first structural theorems.

## References

[1] arXiv Query: search_query=&id_list=2610.11690&start=0&max_results=1 — Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention (source abstract).

[2] arXiv:2610.11690v1 | Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention.

[3] arXiv:2609.11174v2 | A Four-Valued Graph Model for Conflict Resolution: Core Framework and a Machine-Checked Formalization in Lean 4.

[4] arXiv:0810.0596v3 | On quantum semigroup actions on finite quantum spaces.

[5] arXiv:2509.13203v1 | G-CSEA: A Graph-Based Conflict Set Extraction Algorithm for Identifying Infeasibility in Pseudo-Boolean Models.

[6] arXiv:2207.11733v1 | State Definition for Conflict Analysis with Four-valued Logic.

[7] arXiv:2311.15289v2 | Counting cliques without generalized theta graphs.

[8] arXiv:1009.0045v1 | Optimal 3D Angular Resolution for Low-Degree Graphs.

[9] arXiv:astro-ph/020