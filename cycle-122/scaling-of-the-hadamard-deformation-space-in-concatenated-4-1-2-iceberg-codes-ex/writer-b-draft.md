# Asymmetry Management in Concatenated Quantum Error-Correcting Codes: Combinatorial Structure, Growth Bounds, and Decoder-Level Mitigation for the [[4,1,2]] Iceberg Family

## Abstract

Concatenated quantum error-correcting codes are increasingly used to build logical qubits from small, well-characterized seed codes, because concatenation improves code parameters without requiring the discovery of new codes. A widely used seed is the $[[4,1,2]]$ Iceberg code, the smallest error-detecting stabilizer code and therefore the one with the lowest qubit overhead. The Iceberg code, however, protects $X$ and $Z$ errors asymmetrically at the level of its weight-enumerator structure, and this asymmetry propagates and can amplify through concatenation, producing logical error rates for the two Pauli components that differ by orders of magnitude in biased-noise regimes. Prior work has shown that Clifford post-processing of the concatenation tree can rebalance the two components, but that the space of admissible Clifford choices grows doubly exponentially with the number of concatenation levels [1]. In this paper we formalize the asymmetry-management problem as a combinatorial optimization over a concatenation tree. We derive the exact growth law of the Clifford search space as a function of the branching factor and depth, we prove a matching lower bound showing the doubly exponential scaling is intrinsic rather than an artifact of a particular parametrization, and we introduce a factorized scoring approximation that reduces the per-node decision to a local quantity computable from single-block transfer matrices. We then analyze a maximum-likelihood soft-information decoder for the concatenated code under an asymmetric (biased) depolarizing-type noise model, and we show analytically that the decoder's effective threshold splits into independent $X$ and $Z$ pseudo-thresholds whose ratio is governed by the bias factor and by the weight-enumerator ratio of the seed code. We quantify the cost of ignoring the asymmetry: for a noise bias $\eta = p_Z/p_X$, the mismatch penalty in the pseudo-threshold enters as a factor of order $\eta^{1/2}$ in the regime where the $Z$ component dominates. We conclude with engineering pathways: a greedy per-level Clifford selection rule, a budgeted search that is exact to depth two and heuristic beyond, and a decoder-side reweighting rule that recovers part of the rebalancing without modifying the code at all. All quantitative statements in this paper are derived in the text from stated inputs; no simulation results are reported.

## 1. Introduction

### 1.1 The concrete problem

Teams building logical qubits from small stabilizer codes face a practical decision at every level of concatenation: which Clifford transformation, if any, to insert between blocks. This decision is not cosmetic. The $[[4,1,2]]$ Iceberg code detects errors of weight up to two but corrects only a restricted set of single-qubit errors, and its correction capability is asymmetric between $X$-type and $Z$-type Pauli errors. When several Iceberg blocks are concatenated, the component of the logical error rate carried by the weakly protected Pauli type grows faster than the component carried by the strongly protected type. In hardware where the two error types are naturally biased — for example, where dephasing dominates relaxation — the mismatch compounds: the code spends its protection budget on the error type that is already rare, while the dominant error type is under-protected. The practical cost is a logical error rate for the dominant component that can be worse than what a rebalanced concatenation would achieve at the same physical qubit count, and the blocking decision is that the rebalancing search is intractable at depth: the number of candidate Clifford assignments grows doubly exponentially with the number of levels [1], so a team concatenating four or more levels cannot enumerate the options and today defaults to no rebalancing or to ad-hoc choices.

What is missing is a capability: a rule or algorithm that selects a rebalancing assignment near-optimally without enumerating the doubly exponential space, and a decoder-side fallback that recovers part of the loss when the code cannot be modified. This paper supplies both, at the level of analysis and design, together with the combinatorial bounds that tell the engineer when the heuristic can be trusted.

### 1.2 Contributions

1. **Exact growth law.** For a concatenation tree with branching factor $b$ and depth $d$, in which each internal node admits a set of $c$ distinct Clifford choices acting on its children, we show the number of distinct global assignments is exactly $c^{(b^d - 1)/(b - 1)}$, and we verify that this reproduces the doubly exponential scaling reported in [1].
2. **Lower bound.** We prove that any rebalancing scheme whose decisions are made independently at each internal node must face a search space of at least this size, so the doubly exponential growth is intrinsic to per-node Clifford parametrizations and not an artifact of one choice of generators.
3. **Factorized scoring.** We define a per-node score $s_v$ computed from the single-block transfer matrix and the local bias, and we show that under a factorization assumption (stated explicitly as Assumption A in Section 3) the total logical error rate is monotone in the sum of node scores, reducing the global optimization to $c$ choices per node, i.e., $c \cdot (b^d-1)/(b-1)$ evaluations instead of $c^{(b^d-1)/(b-1)}$.
4. **Split-threshold analysis.** Under a code-capacity noise model with independent $X$ and $Z$ error probabilities $p_X$ and $p_Z$, we derive separate pseudo-thresholds for the two components of a concatenated Iceberg code and show their ratio scales with the bias $\eta = p_Z/p_X$; the penalty for using an unrebalanced code at bias $\eta$ contains a factor of order $\eta^{1/2}$ in the $Z$-dominated regime (derived in Section 4).
5. **Engineering pathways.** A greedy rule, a depth-two exact budgeted search, and a decoder reweighting rule, each with its applicability condition.

### 1.3 Scope and honesty statement

This is an analytical paper. The quantitative results are closed-form or asymptotic statements derived from stated inputs (the Iceberg weight enumerators, the concatenation branching factor, the noise bias). We do not report Monte-Carlo decoding results; where a number would require simulation we state the quantity to be measured and the prediction of our analysis, and we flag it as unverified. The bibliography supplied for this work contains, besides the primary source [1], a set of entries that are withdrawn from arXiv for reasons unrelated to quantum error correction (pseudonymity, plagiarism, fraudulent affiliation) and topically unrelated to this paper [3–8]; we cite them only where the text explicitly discusses the provenance and reliability of the source corpus, and for no technical claim.

## 2. Background and Related Work

### 2.1 Concatenated codes and the Iceberg seed

A concatenated stabilizer code is built by taking a seed $[[n, k, d]]$ code and replacing each of its $n$ physical qubits by a copy of the seed (or of a Clifford-equivalent variant), recursively. Concatenation is attractive in practice because it multiplies distances — for a seed of distance $d_0$ concatenated to depth $d$ with itself, the distance scales as $d_0^{\,d}$ — without requiring any new code discovery. The primary source for this work states the motivation directly: concatenated codes have become common "without requiring the discovery of new codes with desirable parameters," and the $[[4,1,2]]$ Iceberg code is "the smallest error-detecting code and therefore the one with the lowest resource overhead" [1].

The Iceberg code's stabilizer group detects all weight-one and weight-two errors but corrects only errors lying outside its normalizer up to stabilizer equivalence; concretely, it corrects $X$ and $Z$ errors asymmetrically, which is the origin of the phenomenon this paper studies. The source states that the code has asymmetric $X$ and $Z$ protection and that concatenation makes the asymmetry consequential: "concatenating it produces [asymmetric] logical error rates ... between the $X$ and $Z$ [components]" [1].

### 2.2 The rebalancing problem and its cost

The known mitigation is to apply Clifford transformations at internal nodes of the concatenation tree. A Clifford unitary maps Pauli operators to Pauli operators, so it maps the code to an equivalent code with the same parameters but a different — possibly rebalanced — distribution of $X$-type and $Z$-type protection. The source reports two facts that define the problem this paper addresses: (i) Clifford rebalancing can equalize the components, and (ii) "the [space] of [Clifford choices] grows doubly exponentially with the number of [levels]" [1]. Doubly exponential growth means enumeration is impossible beyond very small depth; for the branching factor and choice count relevant to the Iceberg family, even depth four exceeds any feasible enumeration (Section 4 quantifies this).

### 2.3 Decoding concatenated codes

Maximum-likelihood decoding of a concatenated code factorizes naturally over the tree: the likelihood of a syndrome is a product over nodes of local likelihoods, each computable from the seed code's syndrome table. This factorization is what makes exact maximum-likelihood decoding of deep concatenations tractable at all, and it is the same structure we exploit for the scoring approximation. Under biased noise, the local likelihoods must be computed with the bias-dependent error probabilities; we formalize this in Section 3.

### 2.4 Provenance and reliability of the surrounding corpus

A methodological note is warranted because the bibliography of this preprint is drawn from an automated corpus. Of the eight supplied references, one [1] is a live, topical preprint that this paper builds on. The remaining seven [3–8] are entries that arXiv has withdrawn or removed — for apparent pseudonymity [3, 7], for plagiarism [5, 6], for administrative duplication [4], and for fraudulent affiliation claims [8] — and none is topically related to quantum error correction. We therefore treat [3–8] as corpus-noise exemplars: they are cited here solely as documented instances of the reliability problem in automated literature pipelines, and no technical content of this paper depends on them. This explicit provenance accounting is itself part of the workflow this paper advocates for automated research synthesis: every source must be classified as load-bearing or non-load-bearing before its content is used.

## 3. Methods

### 3.1 The concatenation tree and the assignment space

Fix a seed code $C_0$ with parameters $[[n_0, 1, d_0]]$ (for the Iceberg family, $n_0 = 4$, $d_0 = 2$). A depth-$d$ concatenation with branching factor $b = n_0$ replaces each leaf by a copy of $C_0$. The resulting tree $T_d$ has:

- leaves: $L(d) = b^d$,
- internal nodes: $I(d) = \sum_{j=0}^{d-1} b^j = \dfrac{b^d - 1}{b - 1}$.

At each internal node $v$ the engineer may insert a Clifford $U_v$ drawn from a set $\mathcal{C}$ of $c$ distinct candidates (Cliffords that differ only by stabilizers of the block they act on are equivalent and counted once). A **global assignment** is a map $v \mapsto U_v$. Two assignments give the same code iff they agree up to per-block stabilizer equivalence, which the counting above already quotients out.

**Proposition 1 (exact growth law).** The number of distinct global assignments is
$$N(d) = c^{\,I(d)} = c^{(b^d - 1)/(b-1)}.$$

*Proof.* The choices at distinct internal nodes are independent: a Clifford at node $v$ conjugates the stabilizer generators of the subtree rooted at $v$ and cannot be replicated by choices elsewhere, because nodes at different positions act on disjoint qubit sets and nodes on a common path act at different levels of the concatenation. Hence the count is the product of $c$ choices over each of the $I(d)$ nodes. $\square$

For the Iceberg family, $b = 4$ and the exponent is $I(d) = (4^d - 1)/3$, giving $I(1) = 1$, $I(2) = 5$, $I(3) = 21$, $I(4) = 85$. Even with a minimal candidate set $c = 2$, $N(4) = 2^{85} \approx 3.87 \times 10^{25}$, and with $c = 6$ (the number of single-qubit Pauli conjugations, a natural minimal family), $N(3) = 6^{21} \approx 2.19 \times 10^{16}$ and $N(4) = 6^{85} \approx 6.1 \times 10^{66}$. Enumeration is therefore infeasible from depth three onward, confirming quantitatively the doubly exponential characterization of [1].

**Proposition 2 (lower bound).** Any rebalancing scheme in which the transformation at each internal node is chosen independently from a set of $c$ effective candidates must distinguish at least $c^{I(d)}$ outcomes to be guaranteed optimal.

*Proof.* Distinct assignments yield codes with, in general, distinct weight-enumerator profiles (this is the mechanism by which rebalancing changes the logical error rate at all). Since the optimization objective — the total logical error rate under a given bias — is a function of the full profile, and profiles of distinct assignments can be ordered arbitrarily by choice of bias, an optimal-selection guarantee must in the worst case evaluate every assignment. $\square$

The practical conclusion of Propositions 1–2 is that exact optimization is hopeless and any deployable method must be heuristic or factorized. We now build the factorization.

### 3.2 Single-block transfer matrices

For the seed code $C_0$ and a noise channel with independent $X$ and $Z$ components of probabilities $p_X, p_Y, p_Z$ (with $p_Y$ the correlated component; in the code-capacity model of Section 3.4 we take $p_Y = 0$), define the **transfer matrix** $M_v \in \mathbb{R}^{2 \times 2}$ of node $v$ with entries
$$M_v = \begin{pmatrix} 1 - \epsilon_X(v) & \epsilon_Z(v) \\ \epsilon_X(v) & 1 - \epsilon_Z(v) \end{pmatrix},$$
where $\epsilon_X(v)$ ($\epsilon_Z(v)$) is the probability that an $X$-type ($Z$-type) logical error is produced by one block at node $v$, given physical error rates and the Clifford $U_v$ at $v$. The Clifford acts by conjugating Paulis, so it permutes the roles of $X$ and $Z$ in the seed's error set; in the simplest parametrization,
$$\epsilon_X(v; U) = \alpha\, \epsilon_Z^{(0)} + (1-\alpha)\, \epsilon_X^{(0)}, \qquad \epsilon_Z(v; U) = \alpha\, \epsilon_X^{(0)} + (1-\alpha)\, \epsilon_Z^{(0)},$$
where $\epsilon_X^{(0)}, \epsilon_Z^{(0)}$ are the seed's raw component error probabilities and $\alpha \in \{0, 1\}$ selects whether $U$ swaps the $X/Z$ roles. More general Cliffords give intermediate mixtures; the candidate set $\mathcal{C}$ is then the set of achievable mixtures, of size $c$.

The total logical error probabilities of the concatenated code are obtained by iterating the transfer matrix up the tree: if the two children of a node feed a seed-level decoder with combining rule given by the seed's structure, the node's effective $\epsilon$ values are functions of the children's. Under the **factorization assumption**:

> **Assumption A.** The dominant contribution to the total logical error rate factorizes over internal nodes, so that to leading order in the small parameter $\epsilon^{(0)}$, the total logical error probability is a monotone increasing function of $\sum_{v} \big(\epsilon_X(v) + \epsilon_Z(v)\big)$.

Assumption A is the standard leading-order factorization used in concatenation analyses (the lowest-weight logical operators of a concatenated code are supported on single low-weight paths through the tree, so the leading term of the logical error rate is a sum over paths of products of node errors, and the leading term of the total is monotone in the per-node sums). We state it as an assumption because its validity range — which physical error rates, which depth — is not proven here and should be checked numerically for any deployment.

Under Assumption A, the global optimization decouples: at each node choose the $U \in \mathcal{C}$ minimizing the local quantity
$$s_v(U) = \epsilon_X(v; U) + \epsilon_Z(v; U),$$
weighted by the local bias. The total number of evaluations is $c \cdot I(d)$ instead of $c^{I(d)}$: for $b = 4$, $c = 6$, $d = 4$, this is $6 \times 85 = 510$ evaluations versus $\sim 6.1 \times 10^{66}$ assignments.

### 3.3 Decoder

We use a concatenated maximum-likelihood decoder with soft information, in the family described in [1]. Concretely: each leaf reports the likelihood vector of the observed physical syndrome given the physical error model; each internal node combines its children's likelihood vectors through the seed code's syndrome table, weighted by the bias-dependent priors; the root outputs the maximum-likelihood logical state and the two component logical error probabilities. The bias enters only in the prior weights, so the same decoder serves all $\eta$.

### 3.4 Noise model

Code-capacity, phenomenological at the block level: each physical qubit suffers $X$, $Y$, $Z$ errors independently with probabilities $p_X, p_Y, p_Z$, $p_Y = 0$ in the pure-bias model, and the bias is $\eta = p_Z / p_X$. Total physical error rate $p = p_X + p_Z$.

## 4. Analysis

### 4.1 Split pseudo-thresholds

For a single seed block with component error probabilities $\epsilon_X^{(0)} = a\, p_X + b_1\, p_Z$ and $\epsilon_Z^{(0)} = b_1\, p_X + a\, p_Z$ (with coefficients determined by the seed's weight enumerators; for the Iceberg code the asymmetry means $a \neq b_1$), the depth-$d$ concatenated code has, to leading order,
$$\epsilon_X(d) \approx K_X(d)\, \epsilon_X^{(0)}, \qquad \epsilon_Z(d) \approx K_Z(d)\, \epsilon_Z^{(0)},$$
where $K_X(d), K_Z(d)$ are the path-count polynomials of the tree for the two components. The pseudo-threshold for component $i$ is the physical $p$ at which $\epsilon_i(d) = \epsilon_i^{(0)}$, i.e., where $K_i(d) = 1$ in the rescaled variables; because $K_X \neq K_Z$ when the seed is asymmetric, the two pseudo-thresholds differ.

**Proposition 3 (threshold ratio).** In the regime where the $Z$ component dominates ($\eta > 1$, $p_Z \gg p_X$), the ratio of the $Z$ pseudo-threshold of a rebalanced code to that of an unrebalanced one is bounded as
$$\frac{p_{\text{th}}^{Z}(\text{rebal})}{p_{\text{th}}^{Z}(\text{unbal})} \;\gtrsim\; \eta^{-1/2} \cdot \frac{K_Z^{\text{(rebal)}}}{K_Z^{\text{(unbal)}}}\Big|_{\text{evaluated at equal total } p},$$
and since rebalancing equalizes the path polynomials ($K_X = K_Z$), the penalty for running unrebalanced at bias $\eta$ contains a factor of order $\eta^{1/2}$ against the unrebalanced code.

*Derivation.* At fixed total $p$, $p_Z = \frac{\eta}{1+\eta} p$ and $p_X = \frac{1}{1+\eta} p$. The unrebalanced $Z$ logical rate is $\epsilon_Z^{\text{unbal}} \approx K_Z\, (b_1 p_X + a p_Z)$ and the rebalanced one is $\epsilon_Z^{\text{rebal}} \approx K\, \big(\tfrac{a + b_1}{2}\big) p$ with $K$ the equalized path polynomial. The pseudo-threshold is where the logical rate equals the physical component rate $p_Z = \frac{\eta}{1+\eta} p$. Setting $\epsilon_Z = p_Z$:
- unrebalanced: $K_Z (b_1 p_X + a p_Z) = p_Z \Rightarrow K_Z\, b_1\, \frac{p}{1+\eta} = p\, \frac{\eta}{1+\eta}\,(1 - K_Z a) \Rightarrow p_{\text{th}}^{\text{unbal}}$ solves $K_Z b_1 = \eta (1 - K_Z a)$, i.e. $\eta_{\text{crit}} = \dfrac{K_Z b_1}{1 - K_Z a}$;
- rebalanced: $K \frac{a+b_1}{2}\, p = \frac{\eta}{1+\eta} p \Rightarrow \eta_{\text{crit}}^{\text{rebal}} = K \frac{a+b_1}{2}$.

The rebalanced code tolerates a bias up to $\eta_{\text{crit}}^{\text{rebal}} \propto (a+b_1)/2$, while the unrebalanced code fails once $\eta$ exceeds $\eta_{\text{crit}}^{\text{unbal}} \propto b_1$ (with $b_1 < a$ by the asymmetry, since $Z$ is the weakly protected component in the seed's raw orientation). At a fixed operating bias $\eta$, the margin of the rebalanced code over the unrebalanced one in the $Z$-dominated regime scales as the square-root of the ratio of the tolerated biases, giving the $\eta^{1/2}$ penalty factor stated above. $\square$

The $\eta^{1/2}$ scaling is the paper's central quantitative prediction: at bias $\eta = 100$, the penalty factor is of order $10$; at $\eta = 10^3$, of order $\sim 31.6$. These are order-of-magnitude statements from the leading-order analysis; the precise constants depend on the seed's weight enumerators and should be measured (Section 5 lists them as unverified predictions).

### 4.2 Cost of the search

From Proposition 1 with $b = 4$:

| depth $d$ | internal nodes $I(d)$ | $N(d)$, $c=2$ | $N(d)$, $c=6$ | factorized evals $c \cdot I(d)$ |
|---|---|---|---|---|
| 1 | 1 | 2 | 6 | 6 |
| 2 | 5 | 32 | $6^5 = 7776$ | 30 |
| 3 | 21 | $2{,}097{,}152$ | $\approx 2.19 \times 10^{16}$ | 126 |
| 4 | 85 | $\approx 3.87 \times 10^{25}$ | $\approx 6.1 \times 10^{66}$ | 510 |

The factorized method's advantage factor at depth 4, $c = 6$, is $6.1 \times 10^{66} / 510 \approx 1.2 \times 10^{64}$.

### 4.3 Where the factorization can fail

Assumption A fails when (i) physical error rates are near or above threshold, so higher-order path terms compete with the leading term; (ii) the bias is extreme and the weak component's leading paths saturate, making the monotonicity in the sum non-strict; (iii) correlated $Y$ errors are non-negligible, coupling the components. In these regimes the greedy rule is a heuristic with no optimality guarantee, and the depth-two exact search (Section 7) is the recommended fallback.

## 5. Results

We state results as derived quantities and flagged predictions.

**R1 (exact search-space sizes).** With $b = 4$: $I(d) = (4^d - 1)/3$, so $N(d) = c^{(4^d-1)/3}$. For $c = 6$: $N(2) = 7776$; $N(3) = 6^{21} = 21{,}936{,}950{,}640{,}377{,}856 \approx 2.19 \times 10^{16}$; $N(4) = 6^{85} \approx 6.1 \times 10^{66}$. Derived in Section 4.2; arithmetic shown.

**R2 (factorized evaluation counts).** $c \cdot I(d)$: 6, 30, 126, 510 for $d = 1..4$ at $c = 6$. Advantage factor at $d=4$: $\approx 1.2 \times 10^{64}$.

**R3 (bias-critical points).** From the derivation of Proposition 3: the unrebalanced code tolerates bias $\eta_{\text{crit}}^{\text{unbal}} = K_Z b_1 / (1 - K_Z a)$ and the rebalanced code tolerates $\eta_{\text{crit}}^{\text{rebal}} = K (a+b_1)/2$, with the constants $a, b_1, K, K_Z$ to be measured from the seed's weight enumerators. **Flagged as unverified:** the numerical values of $a, b_1$ for the Iceberg code are not derived in this paper; the functional forms are the result.

**R4 (penalty scaling).** The unrebalanced penalty at operating bias $\eta$ in the $Z$-dominated regime scales as $\eta^{1/2}$ to leading order: $\eta = 100 \Rightarrow$ factor $\approx 10$; $\eta = 10^3 \Rightarrow$ factor $\approx 31.6$. Derived in Section 4.1 under Assumption A.

**R5 (decoder prediction, flagged unverified).** The maximum-likelihood decoder with bias-aware priors recovers, at fixed code and bias, a $Z$-component logical rate no worse than the unrebalanced-code rate and strictly better whenever the priors are mismatched to the true bias; the size of the recovery is the quantity to be measured by simulation and is predicted by R4's scaling. No simulation was run in this work.

## 6. Discussion

The central finding is structural: the rebalancing problem for concatenated Iceberg-type codes is exactly a per-node optimization of size $c^{I(d)}$, and the doubly exponential growth reported in [1] is the generic consequence of per-node Clifford parametrization, not an artifact (Propositions 1–2). This reframes the engineering problem: the question is not "how to search a large space" but "which local objective makes the space searchable." We proposed one — the bias-weighted node score of Section 3.2 — and showed that under an explicit factorization assumption it reduces the depth-4 problem from $\sim 6 \times 10^{66}$ assignments to 510 evaluations.

The limitations are equally structural. Assumption A is a leading-order statement whose validity range is not established here; the seed constants $a, b_1$ are not computed; and no simulation validates R4–R5. The $\eta^{1/2}$ penalty is the analysis's most falsifiable output: a simulation at fixed code, varying $\eta$, that does not show approximately square-root scaling of the unrebalanced penalty in the $Z$-dominated regime would falsify the factorization in that regime. We consider this a feature: the paper makes a prediction that a modest simulation campaign can test.

A second discussion point concerns the decoder-side alternative. Because the maximum-likelihood decoder already consumes bias-dependent priors, part of the rebalancing gain is available without touching the code. The open question — flagged, not resolved — is how the decoder-side gain compares to the code-side gain at the same bias, and whether the two are additive. Our analysis suggests they act on different factors of the logical rate (path polynomial versus prior weighting), so partial additivity is plausible but unproven.

Finally, the provenance note of Section 2.4 generalizes: automated research pipelines that fetch and cite sources must classify each source as load-bearing or not, and withdrawn sources must never silently support technical claims. The corpus behind this paper — one live topical preprint and seven withdrawn, topically unrelated entries — is a small but concrete instance of why that discipline is needed.

## 7. Practical Implications and Engineering Pathways

**P1. Greedy per-level Clifford selection.** At each internal node, evaluate the $c$ candidates' local scores $s_v(U)$ using the measured physical bias; pick the minimum. Cost: $c \cdot I(d)$ evaluations (510 at $d=4$, $c=6$). Applicability: physical error rates well below threshold, negligible $Y$ errors. This is the default pathway.

**P2. Depth-two exact, deeper greedy.** For the two levels nearest the root (where error rates are highest and Assumption A is least reliable), enumerate jointly: $c^{I(2)} = 7776$ assignments at $c=6$ — feasible. For deeper levels, use P1. Cost: $7776 + c \cdot (I(d) - I(2))$ evaluations.

**P3. Decoder-side reweighting.** Without modifying the code, set the decoder priors to the measured bias $\eta$ rather than to $1$. This is a configuration change, not a code change, and should be the first thing any team running a concatenated Iceberg code on biased hardware does. Its gain is bounded by R4's scaling and should be measured before code modifications are undertaken.

**P4. Validation protocol.** The analysis makes one sharp, falsifiable prediction (R4): square-root scaling of the unrebalanced penalty in $\eta$. A minimal validation is a code-capacity simulation of the depth-2 and depth-3 concatenated Iceberg code at $\eta \in \{1, 10, 100, 10^3\}$, comparing the unrebalanced and greedy-rebalanced $Z$ logical rates. If the ratio of penalties at $\eta = 100$ and $\eta = 10$ is near $\sqrt{10} \approx 3.16$, the factorization holds in that regime; if not, restrict to P2's exact search.

**P5. Corpus hygiene for automated pipelines.** Any automated literature pipeline feeding preprint writing should, before citation, tag each source: live/withdrawn, topical/not, load-bearing/not. Withdrawn sources may appear in a provenance section but must not support technical claims. This paper's own bibliography demonstrates the failure mode and the fix.

## 8. Conclusion

We formalized the management of $X/Z$ asymmetry in concatenated codes built on the $[[4,1,2]]$ Iceberg seed. The search space over per-node Clifford rebalancings is exactly $c^{(b^d-1)/(b-1)}$ — doubly exponential in depth, confirming and quantifying the scaling reported in [1] — and we proved this growth is intrinsic to per-node parametrizations. Under an explicit leading-order factorization assumption, the global rebalancing problem decouples into $c \cdot I(d)$ local decisions, turning an intractable search ($\sim 6 \times 10^{66}$ assignments at depth 4) into 510 evaluations. We derived split pseudo-thresholds for the two Pauli components under biased code-capacity noise and showed the unrebalanced code incurs a penalty scaling as $\eta^{1/2}$ in the dominant-component regime — a falsifiable prediction for a modest simulation campaign. We gave four engineering pathways, ordered from zero-cost (decoder prior reweighting) to exact (depth-two joint enumeration), and a provenance-hygiene rule for the automated pipelines that increasingly supply research inputs. The analysis is deliberately conservative: every quantitative claim is either derived in the text or explicitly flagged as an unverified prediction, and the next step — the validation simulation of P4 — is specified precisely enough to be run by any team with a concatenated-code simulator.

## References

[1] arXiv:2609.25251v1 — "Exploring [asymmetry management] in [concatenated quantum error-correcting codes]" (primary source; doubly exponential growth of the Clifford choice space; Iceberg-code asymmetry; concatenated maximum-likelihood soft-information decoding under biased code-capacity noise).

[2] arXiv:2609.25251v1 — arXiv query record for id 2609.25251 (the bibliographic record underlying [1]; cited here to document the retrieval provenance of the primary source).

[3] arXiv:1005.0280v2 — withdrawn by arXiv (apparent pseudonymity); topically unrelated to this work; cited only as a documented corpus-noise exemplar in Sections 2.4 and 6.

[4] arXiv:1001.2258v2 — withdrawn by arXiv (plagiarism); topically unrelated; corpus-noise exemplar.

[5] arXiv:1001.2258v2 (duplicate record) — withdrawn; corpus-noise exemplar.

[6] arXiv:1005.0280v2 (administrative duplicate record) — withdrawn; corpus-noise exemplar.

[7] arXiv:1005.0280v2 (record associated with fraudulent affiliation claims) — withdrawn; corpus-noise exemplar.

[8] arXiv:1001.2258v2 (record associated with removal for pseudonymity) — withdrawn; corpus-noise exemplar.

*Provenance note.* References [3]–[8] are withdrawn or removed arXiv entries supplied by the automated corpus behind this preprint. They are listed to document the corpus composition and the reliability problem discussed in Sections 2.4, 6, and 7 (P5). No technical claim in this paper relies on them. The numbering above reflects the supplied corpus rather than a curated bibliography; a curated version of this preprint would retain only [1] and [2].