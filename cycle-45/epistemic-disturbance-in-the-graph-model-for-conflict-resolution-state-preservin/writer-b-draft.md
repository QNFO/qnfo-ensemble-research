# Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention

## Abstract

In the graph model for conflict resolution (GMCR), a decision maker (DM) either moves the conflict to another state or does nothing, and every action that leaves the state unchanged is silently classified as inaction. Yet announcements, exercises of rights, leaks, and selective disclosures leave the physical state unchanged while changing what other DMs believe about which moves are available and which moves others would want to make. We introduce such state-preserving actions by augmenting each state with the DMs' epistemic states: a physical move changes the physical state, a state-preserving action changes only the epistemic state, and inaction is the absence of any transition. Actions generate evidence through observer-specific interpretation maps into a four-valued logic that separates evidence for and against each move. We prove three structural results: evidence for a move can only enable perceived moves and evidence against can only disable them; two of the four evidence-reduction operators discard one polarity of evidence entirely; and contradictory assessments are absorbing under monotone evidence accumulation. Combined with monotonicity of stability in move sets, this fixes the direction in which any action shifts a DM's stability judgements and separates capability assessments, which affect all sanction-based stability concepts and the DM's own Nash stability, from intention assessments, which affect only sequential stability. A worked model with $8$ physical states and $512$ augmented states, and a reconstruction of the 1995 DVD format negotiation, illustrate the framework.

## 1. Introduction

The graph model for conflict resolution (GMCR) represents a conflict as a directed graph whose vertices are states and whose colored, directed arcs are the moves available to each decision maker (DM) [1], [2]. In the basic definitions, a DM's action set at a state $q$ consists of the arcs leaving $q$ in the DM's color, together with the implicit option of doing nothing. This convention is elegant but hides an assumption: that every action which leaves the state unchanged *is* doing nothing.

The assumption fails for a large and strategically important class of actions. When a firm announces that it will support a format, when a patent holder exercises a licensing right, when a document is leaked, or when a party selectively discloses part of its position, the physical state of the conflict does not change. But no reasonable analyst would call these inaction: they change what other DMs believe about which moves are available (capability) and which moves others would want to make (intention). We call these **state-preserving actions**, or **epistemic disturbances**: transitions that leave the physical state fixed and alter only the epistemic state.

Modeling such actions requires three distinctions that the standard GMCR does not draw. First, the distinction between a physical move, a state-preserving action, and genuine inaction. Second, the distinction between evidence for a claim and evidence against it, which we carry over from the four-valued Quasi-Closed World Graph Model (QCW-GMCR) [3] and its treatment of state definitions [6]. Third, the distinction between an observer's assessment of what another DM *can* do and what that DM *would want* to do; we show these two assessment types propagate differently through the stability definitions.

The paper's contributions are:

1. A formal augmentation of GMCR states with epistemic components, in which state-preserving actions are first-class transitions and inaction is the absence of a transition (Section 3).
2. Structural results on evidence flow: polarity confinement (evidence for only enables, evidence against only disables), the blindness of two of the four reduction operators, and the absorbing character of contradiction under monotone accumulation (Section 4).
3. A separation theorem in spirit: capability assessments affect all sanction-based stability concepts (general metarationality, symmetric metarationality, sequential stability) and, on the assessing DM's own side, Nash stability; intention assessments affect only sequential stability (Sections 4 and 5).
4. A fully computed toy model and a qualitative reconstruction of the 1995 DVD format negotiation, in which general metarationality cannot distinguish the negotiation's phases because the computer industry group could always sanction, while sequential stability, which asks whether it *would*, can (Sections 4 and 5).

The broader motivation connects to work on epistemic repair in conflictual discourse, where hardened statements conceal the assumptions that make them possible and what one side takes as perception the other experiences as accusation [10], and to analyses of how agentic and cognitive-linear modeling choices shape epistemic outcomes [11], [12], [13].

## 2. Background and Related Work

**The graph model and its epistemic gap.** The foundational framework [1] defines GMCR states, oriented move arcs per DM, and the family of solution concepts from Nash stability through general metarationality (GMR), symmetric metarationality (SMR), and sequential stability (SEQ). The present paper's point of departure [2] is the observation that the basic definitions leave inaction implicit, so that announcements, exercises, leaks, and selective disclosures are misclassified as inaction; it proposes augmenting states with DMs' epistemic states so that a physical move changes the physical state, a state-preserving action changes only the epistemic state, and inaction is the absence of a transition, with actions generating evidence through observer-specific interpretation maps. We adopt this framework and supply explicit derivations of its counting consequences and stability-monotonicity results.

**Four-valued extensions.** The QCW-GMCR [3] extends GMCR with Belnap's four-valued logic, in which each proposition carries a pair of truth values: evidence for ($T$), evidence against ($F$), both ($\top$, contradiction), or neither ($\bot$, ignorance). That work pairs the framework with a machine-checked Lean 4 formalization, establishing that the core definitions are internally consistent; our Section 4 results on reduction operators and absorbing contradiction are stated so as to be formalizable in the same style. The state-definition problem for four-valued conflict analysis is treated in [6], which argues that a state cannot simply be the outcome of a strategy combination when option-level epistemic ambiguity is present; our augmented state space (physical state plus epistemic assessments) is a direct answer to the question that work raises.

**Adjacent formal literatures.** Several works in the source corpus are methodologically adjacent rather than substantively overlapping, and we cite them to delimit scope. The study of continuous semigroup actions on finite quantum spaces that preserve a faithful state [4] shares, at the level of pure structure, our theme of transformations that preserve a designated object (there, a state of a $\mathrm{C}^*$-algebra; here, the physical state of a conflict) while acting on complementary structure; no technical result transfers. The G-CSEA algorithm for extracting conflict sets from pseudo-boolean models [5] addresses infeasibility diagnosis in constrained scheduling, a different notion of "conflict" from strategic conflict, but its graph-based set-extraction viewpoint is analogous to our interpretation maps, which extract, for each observer, the set of moves supported by evidence. The generalized Turán counting problem for graphs excluding generalized theta graphs [7], the angular-resolution problem for low-degree graph drawings [8], and the cosmic-ray flux measurement by the High Resolution Fly's Eye experiment [9] are included in the corpus for bibliographic completeness; none bears on GMCR, and we do not draw on their results. Their presence usefully marks the boundary of this paper's claims: our results are about the interaction of evidence polarity with move-set perception, not about graph enumeration, drawing, or physical measurement.

**Epistemic repair context.** The QNFO program on statements and questions [10] frames human conflict as beginning with speech hardened into statements that conceal enabling assumptions; state-preserving actions are a formal analogue of such statements inside a game-theoretic model. The QNFO notes on agentic collapse [11], cognitive linearity and epistemic modeling [12], and mechanistic ethics [13] supply the surrounding research program in which observer-specific interpretation of evidence, rather than objective fact, is the operative quantity; the present paper gives that viewpoint a precise home inside GMCR stability analysis.

## 3. Methods

### 3.1 Augmented states

Let $N=\{1,\dots,n\}$ be the DMs. For each DM $i\in N$, let $O_i$ be the set of options controlled by $i$, with $k_i=|O_i|$. A **physical state** is a binary assignment to every option: $s\in\{0,1\}^{K}$ where $K=\sum_{i\in N}k_i$, so the physical state set $S$ has

$$|S| = 2^{K}.$$

An **epistemic assessment** by observer $j$ of a proposition $p$ (typically "DM $i$ can take move $m$" or "DM $i$ wants to take move $m$") is an element of Belnap's four values

$$\mathcal{V}=\{T, F, \bot, \top\},$$

where $T$ means evidence for only, $F$ evidence against only, $\top$ evidence for and against (contradiction), and $\bot$ no evidence either way. Observer $j$'s **epistemic state** $e_j$ assigns a value in $\mathcal{V}$ to each capability proposition and each intention proposition relevant to $j$'s deliberation. The **augmented state** is the pair $(s, (e_1,\dots,e_n))$.

A **physical move** by DM $i$ changes $s$ and leaves every $e_j$ fixed. A **state-preserving action** $a$ by DM $i$ leaves $s$ fixed and updates at least one $e_j$ ($j\neq i$ or $j=i$) via an **interpretation map**

$$\iota_j(a, s) : \mathcal{V}^{P} \to \mathcal{V}^{P},$$

where $P$ is the set of propositions observer $j$ tracks. **Inaction** is the absence of any transition: no change to $s$ and no change to any $e_j$. The three are now distinct by construction.

### 3.2 Evidence accumulation and reduction

Evidence accumulates monotonically: each observer $j$ maintains, for each proposition $p$, two disjoint evidence sets $E^{+}_{j,p}$ and $E^{-}_{j,p}$ (supporting and opposing), and an action or move adds elements to these sets but never removes them. The current assessment is

$$v_{j,p} = \begin{cases} T & \text{if } E^{+}_{j,p}\neq\emptyset,\ E^{-}_{j,p}=\emptyset,\\ F & \text{if } E^{+}_{j,p}=\emptyset,\ E^{-}_{j,p}\neq\emptyset,\\ \top & \text{if } E^{+}_{j,p}\neq\emptyset,\ E^{-}_{j,p}\neq\emptyset,\\ \bot & \text{if } E^{+}_{j,p}=\emptyset,\ E^{-}_{j,p}=\emptyset. \end{cases}$$

A **reduction operator** $\rho$ maps an assessment $v\in\mathcal{V}$ to a binary verdict on whether the move is perceived as available (for capability propositions) or as intended (for intention propositions). The four standard operators are:

$$\rho_{\mathrm{for}}(v)=1 \iff v\in\{T,\top\},\qquad \rho_{\mathrm{against}}(v)=1 \iff v\in\{F,\bot\}^{-1},$$

more precisely $\rho_{\mathrm{against}}(v)=0 \iff v\in\{F,\top\}$ (the move is disabled when there is evidence against, regardless of supporting evidence), and the two single-polarity-blind operators $\rho_{\mathrm{for\text{-}blind}}$ (ignores $E^{-}$, so $\top$ and $T$ coincide and $F$ and $\bot$ coincide) and $\rho_{\mathrm{against\text{-}blind}}$ (ignores $E^{+}$, so $\top$ and $F$ coincide and $T$ and $\bot$ coincide).

### 3.3 Stability concepts

For observer $j$ evaluating DM $i$'s stability at augmented state $(s,e)$, the **perceived move set** of $i$ is

$$M^{\rho}_{j,i}(s,e) = \{ m : \rho(v_{j,\mathrm{cap}(i,m)}) = 1 \},$$

a subset of $i$'s objectively available moves. Stability is then evaluated exactly as in standard GMCR [1], [2], with $M^{\rho}_{j,i}$ in place of the true move set. We use Nash stability (no unilateral improvement), GMR (every unilateral move of $i$ can be sanctioned by some counter-move of the others), SMR (the sanction survives $i$'s counter-response), and SEQ (every sanctioning counter-move is itself credible, i.e., not sanctionable in turn).

## 4. Analysis

### 4.1 Toy model: state counting

Take $n=2$ DMs with $k_1=2$ (options $a_1,a_2$ for DM 1) and $k_2=1$ (option $b_1$, a sanction, for DM 2). Then $K=k_1+k_2=3$ and the number of physical states is

$$|S| = 2^{K} = 2^{3} = 8.$$

Observer 2 (DM 2) tracks capability propositions for DM 1's two options, giving $4^{k_1}=4^{2}=16$ possible capability-assessment profiles, and one intention proposition for DM 1, giving $4^{1}=4$ intention values. DM 2's epistemic state therefore has

$$|E_2| = 4^{2}\times 4 = 16\times 4 = 64$$

possible values, and the augmented state space has

$$|S|\times|E_2| = 8\times 64 = 512$$

augmented states. (DM 1's own epistemic state is held fixed in this analysis; including it would multiply the space by $|E_1|$.)

### 4.2 Reduction operators collapse profiles onto move sets

Under any of the four reduction operators, DM 2's perceived move set for DM 1 is determined option-by-option, so the number of distinct perceived move sets is at most

$$2^{k_1} = 2^{2} = 4.$$

Since there are $4^{k_1}=16$ assessment profiles, the average number of profiles collapsing onto each perceived move set is

$$\frac{4^{k_1}}{2^{k_1}} = \frac{16}{4} = 4.$$

For the polarity-blind operators the collapse is exact and uniform: $\rho_{\mathrm{for\text{-}blind}}$ identifies $\top$ with $T$ and $\bot$ with $F$, so each of the $4$ move sets has exactly $2^{k_1}=4$ preimage profiles (each option contributes $2$ of its $4$ values to one verdict). This is the precise sense in which two of the four operators ignore one kind of evidence: $\rho_{\mathrm{for\text{-}blind}}$ cannot distinguish $T$ from $\top$ (it discards the opposing evidence inside $\top$), and $\rho_{\mathrm{against\text{-}blind}}$ cannot distinguish $\top$ from $F$ (it discards the supporting evidence inside $\top$).

### 4.3 Polarity confinement

**Proposition (polarity confinement).** Fix an observer $j$ and a monotone reduction operator $\rho$ (verdict non-decreasing in $E^{+}$ and non-increasing in $E^{-}$). If a state-preserving action adds only supporting evidence ($E^{+}$ grows, $E^{-}$ fixed), then every move perceived before is perceived after: $M^{\rho}_{j,i}$ can only grow. If the action adds only opposing evidence, $M^{\rho}_{j,i}$ can only shrink.

*Proof.* Monotonicity of $\rho$ in $E^{+}$ means $\rho(v)=1$ and $E^{+}\subseteq E^{+\prime}$ (with $E^{-}$ fixed) implies $\rho(v')=1$ where $v'$ is the assessment from $(E^{+\prime},E^{-})$; hence no move leaves $M^{\rho}_{j,i}$. Dually, monotone non-increase in $E^{-}$ means adding opposing evidence never turns $\rho(v)=1$ into $\rho(v')=0$'s complement: no move enters $M^{\rho}_{j,i}$. $\square$

Consequently, evidence for a move can only enable perceived moves and evidence against can only disable them, which fixes the direction in which any state-preserving action moves a DM's stability judgements once stability is monotone in move sets.

### 4.4 Absorbing contradiction

**Proposition (absorption).** Under monotone accumulation, once $v_{j,p}=\top$ (both $E^{+}_{j,p}\neq\emptyset$ and $E^{-}_{j,p}\neq\emptyset$), no subsequent evidence changes $v_{j,p}$: contradiction is absorbing.

*Proof.* Accumulation only adds elements to $E^{+}_{j,p}$ and $E^{-}_{j,p}$. If both are nonempty at some time, both remain nonempty at all later times, since sets only grow. The defining condition for $\top$ is exactly both-nonempty, so $v_{j,p}=\top$ persists. $\square$

### 4.5 Stability monotonicity and the capability/intention separation

Stability is monotone in move sets in the following sense. Write $\mathrm{Nash}_i(q)$ for the predicate "DM $i$ is Nash stable at $q$". Nash stability for DM $i$ requires that $i$ have no improving unilateral move, so enlarging $i$'s own perceived move set can only destroy $i$'s Nash stability, and enlarging the *others'* perceived move sets leaves $i$'s Nash stability untouched (Nash stability involves no sanctions). Hence:

- **Capability assessments of others' moves** enter only through sanction counter-move sets, so they affect GMR, SMR, and SEQ; they do not affect $i$'s own Nash stability. **Capability assessments of $i$'s own moves** enter $i$'s own move set and therefore affect $i$'s Nash stability as well.
- **Intention assessments** enter only through the credibility filter of SEQ (whether a sanctioning counter-move would actually be taken), so they affect only SEQ.

Concretely in the toy model: DM 1 has $k_1=2$ options, so from any physical state DM 1 has

$$2^{k_1}-1 = 2^{2}-1 = 3$$

unilateral moves (any nonempty change of the two bits). DM 2's GMR stability at a state $q$ depends on whether each of DM 2's moves is countered by one of these $3$ moves *as perceived by DM 2*, i.e., on DM 2's capability assessment of $a_1,a_2$; DM 2's SEQ stability additionally depends on the intention assessment of DM 1. The intention assessment takes one of $4$ values; under the intention reduction operator $\rho_{\mathrm{for}}$, the counter-move is perceived credible iff the value lies in $\{T,\top\}$, which is $2$ of the $4$ values, so the fraction of intention-assessment values that flip DM 2's SEQ verdict relative to GMR is

$$\frac{|\{T,\top\}|}{|\mathcal{V}|} = \frac{2}{4} = 0.5.$$

Similarly, among the $2^{k_1}=4$ perceived move sets for DM 1, the number containing a specific move $m$ (say the move on option $a_1$) is $2^{k_1-1}=2$, i.e., $2/4=0.5$ of all perceived move sets; a state-preserving action that shifts DM 2's capability reading of $a_1$ from disabled to enabled therefore moves DM 2 from $2$ of the $4$ move-set equivalence classes into the other $2$.

### 4.6 Hedging

Suppose DM 2 hedges between two candidate types of DM 1, holding assessments $v^{(1)}_{j,p}$ and $v^{(2)}_{j,p}$ for a proposition $p$. If DM 2 reads contradiction ($\top$) as enabled (via $\rho_{\mathrm{for}}$), the hedged perceived move set is the union of the two type-conditional sets and can only be larger than either; if DM 2 reads $\top$ as disabled (via $\rho_{\mathrm{against}}$), the hedged set is the intersection and can only be smaller. Since SEQ stability of DM 2 is monotone in DM 1's perceived counter-move set (more credible counters make DM 2's moves less stable), hedging with the $\rho_{\mathrm{for}}$ reading weakly shrinks DM 2's sequentially stable set, and hedging with the $\rho_{\mathrm{against}}$ reading weakly expands it. In the toy model this is exactly the $2$-of-$4$ move-set split computed in Section 4.5.

### 4.7 The DVD negotiation, quantified structure

In the 1995 DVD format negotiation, the salient DMs are the two format camps and the computer industry group, whose option $b_1$ is a sanction (e.g., withholding support or demanding licensing terms). Model the computer industry group as controlling $k_2=1$ sanction option, so from any state it has $2^{1}-1=1$ unilateral move. General metarationality asks only whether the sanction *exists* as an available counter-move. Because the group's capability to sanction was never in doubt — the capability assessment is $T$ under every reduction operator, since the option was physically available throughout — GMR returns the same stability verdict in both phases of the negotiation: it cannot distinguish them. Sequential stability asks whether the group *would* take the sanction, i.e., its intention assessment; when that assessment crosses from $\{F,\bot\}$ to $\{T,\top\}$ — a change in $2$ of the $4$ assessment values, i.e., a fraction $2/4=0.5$ of the intention scale — the SEQ verdict flips. This is the formal content of the claim that GMR cannot distinguish the DVD phases while SEQ can.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

**R1 (State-space sizes).** For the toy model with $k_1=2$, $k_2=1$: $|S|=2^{3}=8$ physical states; $|E_2|=4^{2}\times4=64$ epistemic states for DM 2; $8\times64=512$ augmented states.

**R2 (Profile collapse).** The $4^{2}=16$ capability-assessment profiles collapse onto at most $2^{2}=4$ perceived move sets, with $16/4=4$ profiles per move set on average, and exactly $4$ preimages per move set for each polarity-blind operator.

**R3 (Operator blindness).** $\rho_{\mathrm{for\text{-}blind}}$ identifies $\top$ with $T$ and $\bot$ with $F$; $\rho_{\mathrm{against\text{-}blind}}$ identifies $\top$ with $F$ and $T$ with $\bot$. Each discards one polarity of evidence inside contradictory assessments.

**R4 (Polarity confinement and absorption).** Supporting evidence can only enable perceived moves; opposing evidence can only disable them; $\top$ is absorbing under monotone accumulation (Section 4.3–4.4, proved).

**R5 (Stability separation).** Capability assessments of others affect GMR, SMR, SEQ; capability assessments of the DM's own moves additionally affect the DM's Nash stability; intention assessments affect only SEQ. In the toy model, DM 1 has $2^{2}-1=3$ unilateral moves from any state; the SEQ/GMR divergence occurs on $2$ of $4$ intention values (fraction $0.5$).

**R6 (Hedging direction).** Hedging with a contradiction-as-enabled reading weakly shrinks the observer's sequentially stable set; with a contradiction-as-disabled reading, weakly expands it (Section 4.6).

**R7 (DVD reconstruction, structural projection).** Under the stated modeling assumption that the computer industry group's sanction capability was assessed $T$ throughout (one option, $2^{1}-1=1$ unilateral move), GMR yields identical verdicts across both negotiation phases, while SEQ flips when the intention assessment crosses $\{F,\bot\}\to\{T,\top\}$, a change spanning $2/4=0.5$ of the four-valued intention scale. This is a model-based reconstruction, not an empirical claim about the historical negotiation beyond its qualitative public record as characterized in [2].

## 6. Discussion

**Limitations.** The framework assumes that evidence sets are only appended to, never retracted. Real epistemic dynamics include retraction (a leak is discredited, an announcement withdrawn); under retraction, polarity confinement (R4) fails, and a state-preserving action could both enable and disable perceived moves. The absorption result (R4) then becomes a liability: an observer who accumulates contradictory evidence is stuck at $\top$ forever, which is arguably realistic for sunk evidence but prevents modeling evidence resolution. A retraction-aware extension would need a decay or discounting mechanism, and all monotonicity-based results would need restatement.

**Failure modes.** The separation result (R5) depends on the exact syntax of the stability definitions: it holds for Nash, GMR, SMR, and SEQ as standardly defined, but any variant that filters unilateral moves by intention (not only sanctions) would let intention assessments leak into Nash-type concepts. The toy-model counting assumes observers track exactly the options of the other DM; if observers hold assessments about counterfactual or unavailable moves, the profile counts $4^{k_i}$ change. The DVD reconstruction is a structural projection: it assumes the capability assessment was uniformly $T$, which matches the qualitative historical record as summarized in [2] but is not established by measurement; if the computer industry group's capability had itself been in doubt at some phase, GMR could in principle distinguish the phases too, and the claimed GMR/SEQ contrast would weaken.

**What would falsify the claims.** Polarity confinement would be falsified by a monotone-accumulation model and reduction operator in which adding supporting evidence disables a perceived move — we conjecture no such operator satisfies the non-decreasing-in-$E^{+}$ definition, but a counterexample operator outside our monotone class would confine the result to that class. The capability/intention separation would be falsified by a stability definition in the standard family whose credibility filter consults capability rather than intention, or whose sanction check consults intention rather than capability. The collapse count (R2) would be falsified by an operator under which distinct perceived move sets number more than $2^{k_i}$; since verdicts are binary per option, this would require non-option-local reduction, i.e., operators that read assessments jointly across options.

**Open questions.** First, the dynamic layer: how do state-preserving actions compose, and is there a normal form for sequences of disturbances equivalent to a single one? Second, the retraction-aware extension mentioned above. Third, the machine-checked formalization of the polarity-confinement and absorption propositions in the Lean 4 framework of [3] is straightforward in outline but not yet carried out here. Fourth, the connection to epistemic repair in discourse [10] suggests empirical questions — which real-world announcements function as capability disturbances versus intention disturbances — that this formal framework motivates but does not answer.

**Arguing against ourselves.** One might object that state-preserving actions are already representable in standard GMCR by re-defining states to include beliefs, making the contribution notational. The reply is that the re-definition must then also re-derive which stability concepts are sensitive to which belief components; without the polarity confinement and reduction-operator analysis, the augmented model is a larger state space with no new structure. The value of the framework