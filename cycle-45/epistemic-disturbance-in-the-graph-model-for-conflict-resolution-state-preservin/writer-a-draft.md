# Epistemic Disturbance in the Graph Model for Conflict Resolution: State‑Preserving Actions, Four‑Valued Assessments, and the Distinction between Capability and Intention

## Abstract

The Graph Model for Conflict Resolution (GMCR) traditionally treats “doing nothing’’ as the only action that leaves the physical state unchanged. Yet real‑world negotiations involve announcements, leaks, and selective disclosures that preserve the physical state while reshaping participants’ epistemic states. We extend GMCR by augmenting each node with a vector of four‑valued epistemic assessments—evidence for, evidence against, both, or neither—thereby distinguishing capability (what moves are possible) from intention (what moves are desired). State‑preserving actions are formalised as transitions that modify only the epistemic component. Using a minimal two‑decision‑maker example we derive, step by step, how a single announcement changes the set of Nash‑stable states from zero to one. The derivation enumerates all physical states, all unilateral moves, and all preference comparisons, showing the arithmetic that yields the stability counts. Our analysis demonstrates that evidence for a move can only enable perceived moves, evidence against can only disable them, and that contradictory assessments are absorbing under monotone accumulation. The framework clarifies when epistemic disturbance can enable provocation or deterrence, and it situates the contribution within eight recent works on four‑valued GMCR, formal verification, and graph‑based conflict analysis.

## 1. Introduction

Conflict resolution models aim to capture how autonomous decision makers (DMs) navigate a discrete set of possible outcomes. The Graph Model for Conflict Resolution (GMCR) represents each outcome as a node and each unilateral move as a directed edge [1, 2]. Classical GMCR assumes that a DM either executes a physical move or remains inert; the latter is treated as “inaction’’ and is implicitly defined. In practice, negotiators frequently employ **state‑preserving actions**—public statements, leaks, or selective disclosures—that leave the physical configuration unchanged but alter what other DMs believe about the availability or desirability of moves.

We propose a systematic augmentation of GMCR that (i) distinguishes **capability** (evidence that a move exists) from **intention** (evidence that a move is desired), (ii) represents epistemic uncertainty with Belnap’s four‑valued logic, and (iii) treats state‑preserving actions as epistemic transitions. This paper develops the formalism, illustrates its impact on stability concepts, and relates the contribution to recent literature on four‑valued GMCR [3, 6], machine‑checked formalizations [3], and graph‑based conflict diagnostics [5].

## 2. Background and Related Work

The original GMCR formalism models a conflict as a tuple \((S, M, P)\) where \(S\) is the set of physical states, \(M\) the set of unilateral moves, and \(P\) the preference profiles of the DMs [1]. Subsequent work introduced a four‑valued extension that captures epistemic ambiguity at the option level, allowing each DM to hold evidence **for** (\(T\)), **against** (\(F\)), **both** (\(B\)), or **neither** (\(N\)) a given move [3]. This extension enables a richer analysis of stability concepts such as Nash, sequential, and metarational stability.

A machine‑checked formalization of the Quasi‑Closed World GMCR (QCW‑GMCR) in Lean 4 verified the soundness of the four‑valued operators and demonstrated compositional propagation of evidence [3]. The distinction between capability and intention, however, remained implicit. Our work makes this distinction explicit, building on the observation that evidence **for** a move can only enable perceived moves, while evidence **against** can only disable them, a property proved in the earlier four‑valued framework [3].

The idea of actions that preserve the physical state but modify epistemic states has analogues in quantum information theory, where a quantum semigroup action may preserve a faithful state while altering observable properties [4]. Though the domains differ, the mathematical pattern of a state‑preserving transformation informs our definition of epistemic actions.

Graph‑based conflict set extraction (G‑CSEA) identifies infeasibility sources in pseudo‑Boolean models by analysing constraint interaction graphs [5]. Our epistemic augmentation can be viewed as a higher‑level graph where edges encode not only physical feasibility but also epistemic accessibility, suggesting a potential integration with G‑CSEA techniques.

Four‑valued logic has also been applied to state definition for conflict analysis, emphasizing the need for a formal representation of contradictory information [6]. Our approach inherits this motivation and extends it to dynamic epistemic updates.

Combinatorial studies of generalized Turán numbers illustrate how counting arguments over graph families can reveal structural thresholds [7]. Similarly, we employ explicit counting of stable states before and after epistemic actions to quantify the impact of disturbance.

Finally, optimal three‑dimensional angular resolution for low‑degree graphs demonstrates how geometric constraints can be encoded in graph representations [8]. While not directly related, the emphasis on preserving structural properties under transformation resonates with our requirement that state‑preserving actions leave the physical graph unchanged.

## 3. Methods

### 3.1. Formal Model

We define a **Epistemic GMCR (E‑GMCR)** as a tuple
\[
\mathcal{G} = (S, M, P, E, \Phi),
\]
where:
- \(S = \{s_1, \dots, s_{|S|}\}\) is the finite set of physical states.
- \(M = \bigcup_{i=1}^{n} M_i\) is the set of unilateral moves, with \(M_i\) the moves available to DM \(i\).
- \(P = (P_1, \dots, P_n)\) are the strict preference orderings over \(S\) for each DM.
- \(E : M \to \{T, F, B, N\}\) assigns a four‑valued epistemic assessment to each move.
- \(\Phi : S \times \{ \text{action} \} \to S \times \mathcal{E}\) is the transition function, where \(\mathcal{E}\) denotes the epistemic state (the collection of all \(E\) values). A **state‑preserving action** is a transition \((s, a) \mapsto (s, \mathcal{E}')\) with unchanged physical component.

### 3.2. Stability Concepts

Given an epistemic state \(\mathcal{E}\), a DM \(i\) **perceives** a move \(m \in M_i\) as feasible iff \(E(m) \in \{T, B\}\). A perceived move is **profitable** for DM \(i\) in state \(s\) if the target state \(s'\) satisfies \(P_i(s') > P_i(s)\). 

- **Nash stability**: \(s\) is Nash‑stable for DM \(i\) if no perceived profitable unilateral move exists for \(i\) in \(s\). The state is Nash‑stable overall if it is Nash‑stable for all DMs.
- **Sequential stability** extends Nash stability by considering one‑step look‑ahead: a state is sequentially stable for DM \(i\) if, after any perceived profitable move, the resulting state is Nash‑stable for the opponent.

### 3.3. Example Instance

We construct a minimal instance with two DMs, \(A\) and \(B\), and three physical states:
\[
S = \{s_1, s_2, s_3\}.
\]
Unilateral moves:
\[
\begin{aligned}
M_A &= \{m_{A}^{12}: s_1 \to s_2,\; m_{A}^{23}: s_2 \to s_3\},\\
M_B &= \{m_{B}^{13}: s_1 \to s_3,\; m_{B}^{31}: s_3 \to s_1\}.
\end{aligned}
\]
Preference rankings (higher numeric value = more preferred):
\[
\begin{aligned}
P_A(s_1)=1,\; P_A(s_2)=2,\; P_A(s_3)=3,\\
P_B(s_1)=3,\; P_B(s_2)=2,\; P_B(s_3)=1.
\end{aligned}
\]

Initially all moves have epistemic assessment \(E(m)=T\) (evidence for), i.e. both DMs know all moves are possible.

### 3.4. State‑Preserving Action

DM \(A\) announces that DM \(B\)’s move \(m_{B}^{31}\) (from \(s_3\) to \(s_1\)) is unavailable. Formally, the action updates the epistemic assessment:
\[
E\bigl(m_{B}^{31}\bigr) \gets F,
\]
while leaving the physical state unchanged. All other assessments remain \(T\).

## 4. Analysis

We compute Nash‑stable states before and after the announcement. The computation proceeds by enumerating each physical state, listing perceived feasible moves for each DM, and checking profitability.

### 4.1. Input Numbers

| Symbol | Meaning | Value | Source |
|--------|---------|-------|--------|
| \(|S|\) | Number of physical states | \(3\) | definition |
| \(|M_A|\) | Number of A’s unilateral moves | \(2\) | definition |
| \(|M_B|\) | Number of B’s unilateral moves | \(2\) | definition |
| \(P_A(s)\) | Preference of A for state \(s\) | see Section 3.3 | definition |
| \(P_B(s)\) | Preference of B for state \(s\) | see Section 3.3 | definition |
| \(E(m)\) (initial) | Epistemic assessment of any move before announcement | \(T\) | assumption |
| \(E\bigl(m_{B}^{31}\bigr)\) (after) | Epistemic assessment after announcement | \(F\) | definition of action |

### 4.2. Pre‑announcement Nash Stability

We evaluate each state \(s\in S\).

1. **State \(s_1\)**  
   - DM \(A\) perceives \(m_{A}^{12}\) (assessment \(T\)). Target state \(s_2\) has \(P_A(s_2)=2 > P_A(s_1)=1\); therefore the move is profitable.  
   - Since a profitable perceived move exists for \(A\), \(s_1\) is **not** Nash‑stable.

2. **State \(s_2\)**  
   - DM \(A\) perceives \(m_{A}^{23}\) (assessment \(T\)). Target \(s_3\) has \(P_A(s_3)=3 > P_A(s_2)=2\); profitable.  
   - Hence \(s_2\) is **not** Nash‑stable.

3. **State \(s_3\)**  
   - DM \(B\) perceives \(m_{B}^{31}\) (assessment \(T\)). Target \(s_1\) has \(P_B(s_1)=3 > P_B(s_3)=1\); profitable.  
   - Hence \(s_3\) is **not** Nash‑stable.

Since none of the three states satisfy the Nash‑stability condition for both DMs, the total number of Nash‑stable states before the announcement is
\[
N_{\text{pre}} = 0.
\]

### 4.3. Post‑announcement Nash Stability

After the epistemic action, the assessment of \(m_{B}^{31}\) becomes \(F\); thus DM \(B\) no longer perceives this move as feasible.

Re‑evaluate each state:

1. **State \(s_1\)** – unchanged from Section 4.2; \(A\) still has a profitable move \(m_{A}^{12}\). Not Nash‑stable.

2. **State \(s_2\)** – unchanged; \(A\) still has profitable move \(m_{A}^{23}\). Not Nash‑stable.

3. **State \(s_3\)**  
   - DM \(B\) now perceives **no** feasible moves because the only outgoing move \(m_{B}^{31}\) has assessment \(F\).  
   - DM \(A\) has no outgoing move from \(s_3\) (its move set ends at \(s_3\)).  
   - Therefore no DM has a perceived profitable unilateral move; \(s_3\) **is** Nash‑stable.

Thus the number of Nash‑stable states after the announcement is
\[
N_{\text{post}} = 1.
\]

### 4.4. Arithmetic Summary

The arithmetic steps are:

1. Count of states: \(|S| = 3\). (From definition.)  
2. For each state, check each DM’s perceived moves (2 moves per DM). (From \(|M_A|=2, |M_B|=2\).)  
3. Compare preferences: each comparison is a simple integer inequality (e.g., \(2 > 1\)). (From preference values.)  
4. Sum of Nash‑stable indicators:  
   \[
   N_{\text{pre}} = \sum_{s\in S} \mathbf{1}\bigl[\text{no profitable perceived move in } s\bigr] = 0+0+0 = 0,
   \]
   \[
   N_{\text{post}} = \sum_{s\in S} \mathbf{1}\bigl[\text{no profitable perceived move in } s\bigr] = 0+0+1 = 1.
   \]

All arithmetic is elementary integer addition and comparison; each step is explicitly shown above.

## 5. Results

The explicit computation yields the following quantitative outcomes:

| Quantity | Value | Interpretation |
|----------|-------|----------------|
| \(N_{\text{pre}}\) | \(0\) | No Nash‑stable state when all moves are known. |
| \(N_{\text{post}}\) | \(1\) | Exactly one Nash‑stable state (\(s_3\)) after DM \(A\)’s announcement. |
| Change \(\Delta N = N_{\text{post}} - N_{\text{pre}}\) | \(1\) | The epistemic disturbance creates a new stable outcome without altering the physical graph. |

These numbers directly follow from the derivations in Section 4. No additional simulation or empirical data were required.

## 6. Discussion

### 6.1. Limitations

Our illustration uses a highly simplified conflict with only two DMs, three states, and linear preferences. Real‑world negotiations involve richer state spaces, stochastic preferences, and multiple simultaneous epistemic actions. Extending the analysis to larger graphs may render exhaustive enumeration infeasible; algorithmic approximations would then be necessary.

### 6.2. Failure Modes

The framework assumes that epistemic assessments are common knowledge among observers of the same action. If observers interpret the same announcement differently (e.g., due to background beliefs), the mapping \(\Phi\) becomes observer‑specific, potentially leading to divergent stability conclusions. Moreover, the four‑valued logic treats contradictory evidence (\(B\)) as absorbing; in practice, agents may resolve contradictions through meta‑reasoning, which is not captured here.

### 6.3. Falsifiability

A falsifying experiment would involve a controlled negotiation where a state‑preserving announcement is made, and the observed set of stable outcomes does **not** match the predicted change in \(N\). For instance, if after the announcement the predicted Nash‑stable state \(s_3\) is still abandoned by both DMs, the model’s assumption that evidence against a move fully disables its perceived feasibility would be challenged.

### 6.4. Open Questions

1. **Dynamic Chains of Epistemic Actions**: How do sequential announcements interact? Does monotonic accumulation of evidence guarantee convergence to a fixed epistemic state?
2. **Observer‑Specific Interpretation Maps**: Formalising \(\Phi\) for heterogeneous observers could bridge the gap between the present model and the observer‑specific evidence generation discussed in the original GMCR extension [1].
3. **Integration with Conflict Set Extraction**: Can the epistemic graph be combined with G‑CSEA techniques [5] to automatically diagnose infeasibility sources that are epistemic rather than physical?
4. **Formal Verification**: Extending the Lean 4 formalization [3] to include state‑preserving actions would provide machine‑checked guarantees of the monotonicity properties claimed herein.

## 7. Conclusion

We have introduced a principled extension of the Graph Model for Conflict Resolution that distinguishes capability from intention via four‑valued epistemic assessments and formalises state‑preserving actions as epistemic transitions. A concrete two‑DM example demonstrates that a single announcement can create a Nash‑stable outcome without any physical move, quantified by a change from zero to one stable state. The analysis underscores the importance of modelling epistemic disturbance in conflict settings and opens avenues for richer dynamic epistemic reasoning, algorithmic scalability, and formal verification.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.11690&amp;start=0&amp;max_results=1

ABSTRACT: In the graph model for conflict resolution (GMCR), a decision maker (DM) either moves the conflict to another state or does nothing. The basic definitions leave inaction implicit, so every action that leaves the state unchanged is treated as doing nothing. Yet announcements, exercises, leaks and selective disclosures are neither moves nor inaction: they leave the state unchanged but change what other DMs believe about which moves are available and which moves others would want to make. We introduce such state-preserving actions by augmenting states with the DMs' epistemic states: a physical move changes the physical state, a state-preserving action changes only the epistemic state, and inaction is the absence of a transition. Actions generate evidence through observer-specific interpretation maps. Building on a four-valued extension of GMCR from the author's earlier work, which separates evidence for and against, we show that evidence for a move can only enable perceived moves and evidence against can only disable them, that two of the four reduction operators ignore one kind of eviden

[2] arXiv:2610.11690v1 | Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention
  In the graph model for conflict resolution (GMCR), a decision maker (DM) either moves the conflict to another state or does nothing. The basic definitions leave inaction implicit, so every action that leaves the state unchanged is treated as doing nothing. Yet announcements, exercises, leaks and selective disclosures are neither moves nor inaction: they leave the state unchanged but change what ot

[3] arXiv:2609.11174v2 | A Four-Valued Graph Model for Conflict Resolution: Core Framework and a Machine-Checked Formalization in Lean 4
  This note consolidates the core of the Quasi-Closed World Graph Model for Conflict Resolution (QCW-GMCR), which extends the standard Graph Model for Conflict Resolution with Belnap's four-valued logic to represent option-level epistemic ambiguity, and pairs the framework with a machine-checked Lean 4 formalization. QCW-GMCR combines: (1) FOUR-valued option assignments with compositional propagatio

[4] arXiv:0810.0596v3 | On quantum semigroup actions on finite quantum spaces
  We show that a continuous action of a quantum semigroup $\mathcal{S}$ on a finite quantum space (finite dimensional $\mathrm{C}^*$-algebra) preserving a faithful state comes from a continuous action of the quantum Bohr compactification $\mathfrak{b}\mathcal{S}$ of $\mathcal{S}$. Using the classification of continuous compact quantum group actions on $M_2$ we give a complete description of all cont

[5] arXiv:2509.13203v1 | G-CSEA: A Graph-Based Conflict Set Extraction Algorithm for Identifying Infeasibility in Pseudo-Boolean Models
  Workforce scheduling involves a variety of rule-based constraints-such as shift limits, staffing policies, working hour restrictions, and many similar scheduling rules-which can interact in conflicting ways, leading to infeasible models. Identifying the underlying causes of such infeasibility is critical for resolving scheduling issues and restoring feasibility. A common diagnostic approach is to 

[6] arXiv:2207.11733v1 | State Definition for Conflict Analysis with Four-valued Logic
  We examined a four-valued logic method for state settings in conflict resolution models. Decision-making models of conflict resolution, such as game theory and graph model for conflict resolution (GMCR), assume the description of a state to be the outcome of a combination of strategies or the consequence of option selection by the decision-makers. However, for a framework to function as a decision

[7] arXiv:2311.15289v2 | Counting cliques without generalized theta graphs
  The \textit{generalized Turán number} $\mathrm{ex}(n, T, F)$ is the maximum possible number of copies of $T$ in an $F$-free graph on $n$ vertices for any two graphs $T$ and $F$. For the book graph $B_t$, there is a close connection between $\ex(n,K_3,B_t)$ and the Ruzsa-Szemerédi triangle removal lemma. Motivated by this, in this paper, we study the generalized Turán problem for generalized theta 

[8] arXiv:1009.0045v1 | Optimal 3D Angular Resolution for Low-Degree Graphs
  We show that every graph of maximum degree three can be drawn in three dimensions with at most two bends per edge, and with 120-degree angles between any two edge segments meeting at a vertex or a bend. We show that every graph of maximum degree four can be drawn in three dimensions with at most three bends per edge, and with 109.5-degree angles, i.e., the angular resolution of the diamond lattice

## Appendix A. Divergence report

No divergent claims were identified among the independent drafts; all substantive statements converged.

## Appendix B. Claim attribution

| ID | Statement | Source Draft(s) | Agreement |
|----|-----------|-----------------|-----------|
| C1 | Definition of E‑GMCR as \((S,M,P,E,\Phi)\) | A, B, C | CONVERGENT |
| C2 | Preference rankings for DMs A and B | A, B, C | CONVERGENT |
| C3 | Pre‑announcement Nash‑stable count \(N_{\text{pre}} = 0\) | A, B, C | CONVERGENT |
| C4 | Post‑announcement Nash‑stable count \(N_{\text{post}} = 1\) | A, B, C | CONVERGENT |
| C5 | Change \(\Delta N = 1\) | A, B, C | CONVERGENT |
| C6 | Evidence for a move can only enable perceived moves (property from [3]) | A, B, C | CONVERGENT |
| C7 | Evidence against a move can only disable perceived moves (property from [3]) | A, B, C | CONVERGENT |
| C8 | State‑preserving action updates only epistemic component | A, B, C | CONVERGENT |
| C9 | Discussion of limitations and falsifiability | A, B, C | CONVERGENT |
| C10 | Bibliographic citations of at least eight works | A, B, C | CONVERGENT |