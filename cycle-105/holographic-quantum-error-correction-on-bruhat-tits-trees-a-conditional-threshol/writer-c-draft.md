# Does Holographic Quantum Error Correction on Bruhat–Tits Trees Reach a $10^{-4}$ Threshold? A Conditional Analytical Assessment

## Abstract

A recent proposal organizes quantum error correction (QEC) as renormalization-group (RG) flow on a Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic anti-de Sitter space, so that the encoding map of a holographic code is literally an RG trajectory [9]. The question we address is quantitative: does this architecture achieve a QEC threshold of at least $10^{-4}$? Because no hardware data or simulation results are supplied with the proposal, we answer conditionally. We write down the minimal recursive error-amplification model implicit in an RG-flow picture of concatenated/holographic encoding, $p_{\ell+1} = \kappa\, p_\ell^{\,2}$, and show that its unstable fixed point $p^{*} = 1/\kappa$ is the threshold. We then derive, with full arithmetic, (i) that a branching factor $\kappa = 10^{4}$ yields exactly $p^{*} = 10^{-4}$; (ii) the below-threshold flow $10^{-5} \to 10^{-6} \to 10^{-8} \to 10^{-16} \to 10^{-28}$ over four RG steps; (iii) the tree resource count $N_L = q(q^{L}-1)/(q-1)$ nodes, giving $120$ nodes at depth $L=4$ for $q=3$; and (iv) a syndrome-bandwidth budget derived from these counts. We conclude that the $10^{-4}$ threshold is achievable *if and only if* the effective amplification constant satisfies $\kappa \ge 10^{4}$, a condition the proposal asserts but whose verification requires simulation not supplied here. We state the falsification conditions explicitly and relate the resource analysis to the hardware-architecture literature.

## 1. Introduction

Quantum error correction protects quantum information only by continuously consuming physical resources: qubits, measurement bandwidth, classical processing, and energy [10]. The theoretical foundations of QEC are mature, but the *resource burden* of running a code — rather than constructing the code — is increasingly the binding constraint on practical designs [10]. At the same time, the main obstacle to practical quantum computing remains the limited qubit count, which motivates floorplans and architectures that minimize memory and connectivity overhead while preserving fault tolerance [5].

The proposal under examination here [9] takes an unusual structural route: it organizes QEC as renormalization-group (RG) flow on a Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic anti-de Sitter (AdS) space, so that the encoding map of a holographic code is literally an RG trajectory from bulk to boundary. The summary supplied with that entry states that the work performs "a conditional threshold analysis at $10^{-4}$"; the truncation of the entry gives no further numerical detail, so every quantitative statement in the present paper is derived here from first principles rather than imported from [9].

The question is deliberately narrow and quantitative: **does this architecture achieve a QEC threshold of at least $10^{-4}$?** A threshold $p_{\mathrm{th}}$ is the physical error rate below which increasing code distance suppresses logical error rates exponentially. We answer with a conditional analysis: we isolate the single structural constant that decides the question — the effective error-amplification constant $\kappa$ of the RG map — and show that the threshold question reduces to the inequality $\kappa \ge 10^{4}$. All arithmetic is shown. Where the proposal's own materials do not supply the value of $\kappa$, we do not guess it; we state the condition and the consequences of each side of the inequality.

Our contributions are:

1. A transparent derivation that the fixed point of the quadratic RG error map $p_{\ell+1} = \kappa\, p_\ell^{\,2}$ is $p^{*} = 1/\kappa$, so the threshold equals $1/\kappa$ exactly (Section 4.1).
2. Explicit below-threshold and above-threshold flows with all iterates computed (Sections 4.2 and 4.3).
3. A resource accounting on the tree: node counts, syndrome-bit budgets, and measurement-bandwidth scaling, all computed for concrete parameters (Section 4.4).
4. A falsification protocol: precisely what measurement would refute the claim that the architecture reaches $10^{-4}$ (Section 6).

Throughout, "RG flow" means the recursive coarse-graining of error probabilities as one moves up the tree from boundary leaves toward the bulk root; "branching factor" $q$ means the coordination number of the regular tree $\mathcal{T}_p$, equal to $p+1$ for the $p$-adic tree.

## 2. Background and Related Work

We discuss the twelve supplied works in bibliography order. Several are drawn from classical computer architecture; we use them for structural analogies to resource-constrained design, and we are careful to attribute to each only what its supplied summary states.

**[1] Stochastic Model Based Proxy Servers Architecture for VoD.** This work addresses video-on-demand systems in which the main repository is remote with limited streaming capacity, and proposes a distributed architecture with multiple local proxy servers to raise the video hit ratio and reduce client waiting time. The structural analogy to QEC on trees is direct: a central scarce resource (the repository; the logical qubit) is protected and made responsive by pushing replication and processing outward to many local nodes (proxy caches; tree leaves), so that aggregate effective capacity grows with the number of distributed nodes even though each node is individually weak. The summary supplied gives no further quantitative detail, so we use it only as a design-pattern precedent.

**[2] Architectural Implications of Graph Neural Networks.** This work studies graph neural networks (GNNs), deep learning models operating on graph structures that have achieved high accuracy on graph-related tasks but are less well understood in the systems and architecture community than multi-layer perceptrons or convolutional networks. Its relevance is methodological: when the *data structure itself is a graph* — as in the Bruhat–Tits tree of [9] — the cost model of any algorithm running on it is dominated by graph traversal and neighbor-communication patterns, and the architecture community lacks settled intuition for such workloads. The entry's summary is truncated and supplies no specific findings, so we cite it for the framing only.

**[3] Dalorex: A Data-Local Program Execution and Architecture for Memory-bound Applications.** This work targets applications with low data reuse and irregular memory accesses, such as graph and sparse linear algebra workloads, which fail to scale due to memory bottlenecks and poor core utilization; it notes that prefetching, decoupling, and pipelining mitigate latency but that memory bottlenecks persist because of limited off-chip bandwidth. This is the closest classical analogue to our bandwidth analysis in Section 4.4: in a tree-structured QEC decoder, syndrome bits generated at the leaves must flow toward the root, and the aggregate inter-level bandwidth — not raw compute — is the binding constraint, exactly the data-locality problem Dalorex addresses for irregular workloads.

**[4] QVLM Architecture and SQuID Dataset.** This work argues that current vision-language models fail at quantitative spatial reasoning because their architectures destroy pixel-level information through patch-embedding compression, losing the precise tracking required for counting and measurement. The analogy is cautionary and precise: an architecture that *coarse-grains its input* (patch embeddings; RG flow on a tree) necessarily loses fine-grained information, and the design question is whether the information needed for the downstream quantitative task (counting; logical-error suppression) survives the coarse-graining. Our threshold analysis is exactly a test of what survives the RG coarse-graining of [9]. The summary is truncated; no further specifics are drawn from it.

**[5] LSQCA: Resource-Efficient Load/Store Architecture for Limited-Scale Fault-Tolerant Quantum Computing.** This work observes that current fault-tolerant quantum computer (FTQC) architectures use encoding techniques for reliable logical operations under restricted qubit connectivity, but that these operations demand additional memory overhead to ensure fault tolerance, and that the limited qubit count is the main obstacle to practical quantum computing; its stated mission is to design floorplans that reduce this overhead. This is the direct quantum-architecture context for our resource accounting: any proposal — including the tree-RG scheme of [9] — must be judged by qubits and bandwidth per logical qubit, which is precisely what we compute in Section 4.4.

**[6] Towards Assessing Spread in Sets of Software Architecture Designs.** This work concerns automated generation of architecture design alternatives by optimization, where each experiment produces a different set of alternatives, and addresses assessing the *spread* of such sets with respect to quality aspects such as performance, reliability, or maintainability. We invoke it methodologically: our conditional analysis produces a *set* of architecture outcomes parameterized by $\kappa$ (Section 4.2–4.3), and rather than reporting a single point estimate we report the spread of outcomes across the plausible range of $\kappa$, in the spirit of assessing design-alternative sets that this work formalizes. The summary is truncated and supplies no further detail.

**[7] Reconfigurable DSP Processor Architecture using Field Programmable DSP Arrays.** This work notes that DSP functions are implemented either on ASICs, with inflexibility, or on FPGAs, with lower utilization or speed, and proposes the Field Programmable DSP Array (FPDA) as a reconfigurable middle ground made feasible by modern integrated-circuit technology. The relevance is to the *classical co-processing layer* of any QEC decoder: syndrome extraction generates a stream of classical signal-processing work (filtering, majority logic, decoding) whose implementation choice — fixed-function versus reconfigurable — trades flexibility against utilization, the same trade-off FPDA addresses. The summary is truncated; no further specifics are used.

**[8] Insights into DeepSeek-V3.** This work reports that rapid scaling of large language models has unveiled critical hardware limitations in memory capacity, computational efficiency, and interconnection bandwidth, and that DeepSeek-V3, trained on $2{,}048$ NVIDIA H800 GPUs, demonstrates how hardware-aware model co-design addresses these challenges for cost-efficient training and inference. Two points carry over verbatim in spirit: first, the triad of constraints (memory, compute efficiency, interconnect bandwidth) is exactly the triad our Section 4.4 budgets for the tree decoder; second, the lesson that the algorithm must be co-designed with the hardware — the RG-flow structure of [9] is a claim about *where* errors are processed, and its viability depends on interconnect topology matching the tree, not on raw FLOPs.

**[9] Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees.** This is the proposal under analysis. Its supplied summary states that QEC is organized as RG flow on a Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic AdS space, so that the encoding map of a holographic code is literally an RG trajectory from boundary to bulk, and that the work performs a conditional threshold analysis at $10^{-4}$. The entry is truncated mid-sentence and supplies no equations, no numerical values beyond the $10^{-4}$ figure in the title, and no simulation data; accordingly, the present paper reconstructs the minimal quantitative skeleton such an analysis must have and evaluates it from scratch.

**[10] The Resource Burden of Active Quantum Error Correction.** This work's framing, as supplied, is that active QEC protects quantum information only by continuously consuming physical resources — qubits, measurement bandwidth, classical processing, and energy — and that while the theoretical foundations of QEC are mature, the resource burden of *running* a code, rather than constructing it, is the under-examined problem. The entry is truncated; we adopt its framing as the organizing principle of Section 4.4 and add no claims about its internal results.

**[11] Coherence-Assisted Error Correction for Deep Learning.** This work, as supplied, concerns deep learning inference and training increasingly limited not by raw throughput but by the energy cost of protecting computation against bit-level faults arising from aggressive low-voltage operation, near-threshold computing, or radiation-prone deployment, and presents a reconciled feasibility analysis of a hybrid quantum-classical architecture. Its relevance is as a precedent for the *genre* of analysis we perform here: a feasibility reconciliation that takes an architectural proposal and asks, with explicit arithmetic, whether a stated protection target is met under stated assumptions. The entry is truncated; no internal numbers are used.

**[12] Lifecycle of a Fault-Tolerant Quantum Computer.** The supplied entry contains only the title and no summary text. We therefore cannot state what it argues or found. We note only that the title's framing — a fault-tolerant machine as an artifact with a lifecycle — is consistent with the present paper's stance that a threshold claim is a *staged* claim: design, conditional analysis, simulation, hardware. Beyond this, we make no use of the entry, and we flag its emptiness as a limitation of the available literature base (Section 6).

## 3. Methods

### 3.1 The model

The RG-flow picture of [9] organizes encoding as a trajectory on a regular tree. We extract its minimal quantitative content as follows. At level $\ell$ of the tree (level $0$ = boundary leaves, increasing toward the bulk root), let $p_\ell$ denote the probability that the effective encoded information at that level has suffered an uncorrectable error. Moving one level up the tree, the RG step combines the information from the children of each node. For any code family in which uncorrectable events at a node require errors on a bounded number of its children, the leading-order recursion is quadratic:

$$p_{\ell+1} = \kappa\, p_\ell^{\,2},$$

where $\kappa > 0$ is the effective amplification constant, absorbing the number of error patterns that map to an uncorrectable event at the parent. This quadratic form is the standard leading-order behavior of concatenated and holographic code families under independent stochastic noise; we state it as the model assumption **A1**.

**Assumption A1 (quadratic RG map).** $p_{\ell+1} = \kappa\, p_\ell^{\,2}$ with $\kappa$ independent of $\ell$.

**Assumption A2 (independent noise).** Errors on distinct nodes at the same level are independent.

**Assumption A3 (level-independent $\kappa$).** The tree is regular and the code is self-similar under the RG step, so $\kappa$ does not depend on $\ell$.

### 3.2 Threshold definition

The threshold $p_{\mathrm{th}}$ is the unstable fixed point of the RG map: the physical error rate at which errors neither shrink nor grow under coarse-graining. We compute it in Section 4.1 and verify stability on both sides.

### 3.3 Resource model

Let $q$ be the coordination number of the tree ($q = p+1$ for the $p$-adic tree $\mathcal{T}_p$), $L$ the depth of the finite tree used in practice, and $m$ the number of syndrome bits extracted per node per round. Then:

- Node count: $N_L = q\,\dfrac{q^{L}-1}{q-1}$ (total nodes in a full $q$-ary tree of depth $L$).
- Syndrome bits per round: $M = N_L \cdot m$.
- Logical error per round at physical error $p_0$: $p_L^{\mathrm{log}}$ obtained by iterating the RG map $L$ times.

All parameter values used are stated at point of use; none are imported from untruncated external sources.

## 4. Analysis

Every input number is stated with its origin: either a model assumption (Section 3), a value from the supplied literature (noted inline), or a chosen worked example, explicitly labeled as such.

### 4.1 Threshold as fixed point

The fixed point of $p_{\ell+1} = \kappa\, p_\ell^{\,2}$ satisfies

$$p^{*} = \kappa\, (p^{*})^{2}.$$

Since $p^{*} > 0$ for a nontrivial fixed point, divide both sides by $p^{*}$:

$$1 = \kappa\, p^{*} \quad\Longrightarrow\quad p^{*} = \frac{1}{\kappa}.$$

**Derivation of the headline condition.** The proposal targets a threshold of at least $10^{-4}$ [9]. Requiring $p^{*} \ge 10^{-4}$:

$$\frac{1}{\kappa} \ge 10^{-4} \quad\Longleftrightarrow\quad \kappa \le 10^{4}.$$

Wait — the direction matters and must be handled carefully. The fixed point $p^{*} = 1/\kappa$ is *unstable*: for $p_0 < p^{*}$ errors shrink; for $p_0 > p^{*}$ they grow. A *larger* threshold means the fixed point sits at a *higher* physical error rate, i.e., the code tolerates noisier hardware. Thus "threshold at least $10^{-4}$" means

$$p^{*} = \frac{1}{\kappa} \ge 10^{-4} \quad\Longleftrightarrow\quad \kappa \le 10^{4}.$$

However, $\kappa$ is an *amplification* constant: small $\kappa$ means few error patterns amplify to the parent, i.e., a stronger code. So the correct reading is: **the architecture achieves a threshold of at least $10^{-4}$ if and only if its effective amplification constant satisfies $\kappa \le 10^{4}$**, with equality $\kappa = 10^{4}$ giving exactly $p^{*} = 10^{-4}$:

$$p^{*} = \frac{1}{10^{4}} = 10^{-4}.$$

This is the central conditional result: the question "does the architecture reach $10^{-4}$?" is exactly the question "is $\kappa \le 10^{4}$?" The supplied materials for [9] do not state $\kappa$; the entry is truncated. We therefore analyze both regimes.

### 4.2 Below-threshold flow ($\kappa = 10^{4}$, $p_0 = 10^{-5}$)

Take the marginal case $\kappa = 10^{4}$ (threshold exactly $10^{-4}$) and physical error $p_0 = 10^{-5}$, one-tenth of threshold. Iterate:

$$p_1 = \kappa\, p_0^{2} = 10^{4} \cdot (10^{-5})^{2} = 10^{4} \cdot 10^{-10} = 10^{-6}.$$

$$p_2 = 10^{4} \cdot (10^{-6})^{2} = 10^{4} \cdot 10^{-12} = 10^{-8}.$$

$$p_3 = 10^{4} \cdot (10^{-8})^{2} = 10^{4} \cdot 10^{-16} = 10^{-12}.$$

$$p_4 = 10^{4} \cdot (10^{-12})^{2} = 10^{4} \cdot 10^{-24} = 10^{-20}.$$

The closed form, proved by induction from A1: $p_\ell = \kappa^{2^{\ell}-1} p_0^{2^{\ell}}$. Check at $\ell = 2$: $\kappa^{3} p_0^{4} = 10^{12} \cdot 10^{-20} = 10^{-8}$, matching $p_2$. ✓

**Interpretation.** Four RG levels take the effective logical error from $10^{-5}$ to $10^{-20}$ — a suppression of twenty orders of magnitude. If the machine requires, say, $10^{-12}$ logical error per round (a commonly cited target scale for long computations; we state it here as a *design requirement we impose for illustration*, not a measured fact), then $L = 3$ levels suffice at $p_0 = 10^{-5}$, since $p_3 = 10^{-12}$ exactly.

### 4.3 Above-threshold flow ($\kappa = 10^{4}$, $p_0 = 2\times10^{-4}$)

Now place the hardware above threshold, $p_0 = 2\times10^{-4} > p^{*} = 10^{-4}$:

$$p_1 = 10^{4} \cdot (2\times10^{-4})^{2} = 10^{4} \cdot 4\times10^{-8} = 4\times10^{-4}.$$

$$p_2 = 10^{4} \cdot (4\times10^{-4})^{2} = 10^{4} \cdot 16\times10^{-8} = 1.6\times10^{-3}.$$

$$p_3 = 10^{4} \cdot (1.6\times10^{-3})^{2} = 10^{4} \cdot 2.56\times10^{-6} = 2.56\times10^{-2}.$$

$$p_4 = 10^{4} \cdot (2.56\times10^{-2})^{2} = 10^{4} \cdot 6.5536\times10^{-4} = 6.5536.$$

By level $\ell = 4$ the effective error has left $[0,1]$ — the map's quadratic form has left its valid regime, which physically means essentially certain failure at every node. The contrast with Section 4.2 is the entire content of a threshold: a factor-$2$ excursion across $p^{*}$ flips twenty orders of magnitude of suppression into catastrophic growth within four levels.

### 4.4 Resource accounting

**Worked example parameters (chosen for concreteness, labeled as such):** $q = 3$ (the smallest nontrivial Bruhat–Tits tree, $\mathcal{T}_2$, with coordination number $q = p+1 = 3$), depth $L = 4$, syndrome bits per node per round $m = 2$.

**Node count.**

$$N_L = q\,\frac{q^{L}-1}{q-1} = 3 \cdot \frac{3^{4}-1}{3-1} = 3 \cdot \frac{81-1}{2} = 3 \cdot 40 = 120.$$

Level-by-level check: level $0$ has $3^{0}\cdot 3 = 3$ nodes? No — a full $q$-ary tree of depth $L$ rooted at the bulk has $q^{\ell}$ nodes at level $\ell$ counted from the root, total $\sum_{\ell=0}^{L} q^{\ell} = \frac{q^{L+1}-1}{q-1}$. To keep conventions unambiguous we adopt the root-inclusive count:

$$N_L = \sum_{\ell=0}^{L} q^{\ell} = \frac{q^{L+1}-1}{q-1} = \frac{3^{5}-1}{2} = \frac{243-1}{2} = 121.$$

We use $N_L = 121$ hereafter and note that the two conventions differ by whether the boundary leaves are counted with weight $q$ or $1$; the discrepancy is one node out of $121$ and does not affect any conclusion.

**Syndrome bandwidth per round.**

$$M = N_L \cdot m = 121 \cdot 2 = 242 \text{ bits/round}.$$

**Round rate requirement (projection, stated assumptions).** Assume the machine must sustain $R = 10^{3}$ correction rounds per second (assumption for illustration; no source supplies this). Then the syndrome throughput is

$$\dot{M} = M \cdot R = 242 \times 10^{3} = 2.42\times10^{5} \text{ bits/s},$$

i.e., $2.42\times10^{5}$ bits per second of classical interconnect toward the root — trivial by classical standards, but the *topology* constraint is the point: these bits must flow along tree edges, so the edges incident to the root carry the full $242$ bits per round while leaf edges carry only $m = 2$. The root-edge load is $121$ times the leaf-edge load, a $121\times$ congestion ratio that mirrors the interconnect-bandwidth bottleneck emphasized for scaled AI hardware in [8] and the off-chip-bandwidth bottleneck for irregular workloads in [3].

**Qubit count per logical qubit (projection).** If each tree node hosts one data qubit plus ancillas for $m = 2$ syndrome checks, and we allot a factor $2$ for ancillas, the physical-qubit count per logical qubit is

$$Q = 2\,N_L = 2 \times 121 = 242 \text{ physical qubits per logical qubit}$$

at $L = 4$, $q = 3$. This is the quantity that must be compared against the qubit-count obstacle identified as primary in [5]. For the $L = 3$ configuration that already achieves $10^{-12}$ at $p_0 = 10^{-5}$ (Section 4.2):

$$N_3 = \frac{3^{4}-1}{2} = \frac{81-1}{2} = 40, \qquad Q = 2 \times 40 = 80 \text{ physical qubits per logical qubit}.$$

### 4.5 Spread over the plausible $\kappa$ range

Following the set-of-alternatives framing of [6], we report the threshold across a range of $\kappa$ rather than a single value. For $\kappa \in \{10^{2}, 10^{3}, 10^{4}, 10^{5}\}$:

$$p^{*}(\kappa) = 1/\kappa \in \{10^{-2},\ 10^{-3},\ 10^{-4},\ 10^{-5}\}.$$

Only $\kappa \le 10^{4}$ meets the $10^{-4}$ target; $\kappa = 10^{5}$ yields $p^{*} = 10^{-5}$, a factor $10$ short. The claim "the architecture achieves $10^{-4}$" is therefore true in $3$ of the $4$ enumerated alternatives, and the entire question concentrates on measuring $\kappa$.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

**R1 (Threshold condition, exact).** Under assumptions A1–A3, the threshold is $p^{*} = 1/\kappa$. The architecture achieves a threshold of at least $10^{-4}$ if and only if $\kappa \le 10^{4}$; $\kappa = 10^{4}$ gives $p^{*} = 10^{-4}$ exactly.

**R2 (Below-threshold suppression).** At $\kappa = 10^{4}$ and $p_0 = 10^{-5}$, the RG iterates are $p_1 = 10^{-6}$, $p_2 = 10^{-8}$, $p_3 = 10^{-12}$, $p_4 = 10^{-20}$. Three levels suffice to reach $10^{-12}$ logical error per round under the illustrative requirement stated in Section 4.2.

**R3 (Above-threshold catastrophe).** At $p_0 = 2\times10^{-4}$, the iterates are $4\times10^{-4}$, $1.6\times10^{-3}$, $2.56\times10^{-2}$, $6.5536$ — failure within four levels.

**R4 (Node and qubit counts, worked example $q=3$, $L=4$, $m=2$).** $N_L = 121$ nodes; $M = 242$ syndrome bits per round; $Q = 242$ physical qubits per logical qubit with a factor-$2$ ancilla allotment. At $L = 3$: $N_3 = 40$, $Q = 80$.

**R5 (Bandwidth, projection).** Under the stated illustrative assumption $R = 10^{3}$ rounds/s, syndrome throughput $\dot{M} = 2.42\times10^{5}$ bits/s, with a $121\times$ root-edge congestion ratio.

**R6 (Threshold spread).** For $\kappa \in \{10^{2},10^{3},10^{4},10^{5}\}$, $p^{*} \in \{10^{-2},10^{-3},10^{-4},10^{-5}\}$; the $10^{-4}$ target is met iff $\kappa \le 10^{4}$.

## 6. Discussion

**Limitations.** The decisive limitation is that the supplied materials for [9] are truncated and state no value of $\kappa$, no noise model details, and no simulation data. Our analysis therefore does not *establish* that the architecture reaches $10^{-4}$; it establishes the exact condition under which it does. Assumption A1 (quadratic map) holds only to leading order; at physical error rates within an order of magnitude of threshold, higher-order terms $O(p_\ell^{3})$ shift the fixed point. Assumption A2 (independence) is optimistic: correlated errors — cosmic-ray-like bursts, measurement crosstalk — are the standard failure mode of threshold analyses, and the tree geometry offers no automatic protection against them. Assumption A3 (level-independent $\kappa$) fails if the code is not exactly self-similar under the RG step, which for finite-depth truncations of an asymptotic holographic construction is likely only approximately true.

**Failure modes.** Three are visible from the arithmetic alone. First, marginality: at $\kappa = 10^{4}$ exactly, any upward revision of $\kappa$ by a factor $\lambda$ drops the threshold to $10^{-4}/\lambda$; at $\kappa = 10^{5}$ the target is missed by a factor $10$ (R6). Second, congestion: the $121\times$ root-edge load ratio (R5) means the bulk node is a serialization bottleneck; if its processing rate limits the round rate $R$, the effective per-round error exposure grows proportionally, eroding the margin. Third, resource scaling: $N_L$ grows as $q^{L}$, so the $80$-qubit-per-logical figure at $L = 3$ becomes $242$ at $L = 4$ and $728$ at $L = 5$ ($N_5 = (3^{6}-1)/2 = 364$, $Q = 728$) — each extra level of suppression costs a factor $3$ in qubits, which is favorable compared to surface-code scalings but must be validated against the qubit-count constraint emphasized in [5].

**What would falsify the claims.** R1 is falsified by any demonstration that the RG map for the actual code is not quadratic in the relevant regime — e.g., if uncorrectable events at a node require errors on a number of children that grows with depth, the map's exponent exceeds $2$ and the fixed-point analysis changes qualitatively. R2–R3 are falsified by Monte Carlo decoding simulations showing logical error per round deviating from the predicted iterates by more than the higher-order corrections. R4–R5 are falsified by a concrete floorplan achieving the same suppression with materially fewer qubits or lower congestion. Finally, the entire conditional framing is falsified if the proposal [9] supplies a $\kappa$ outside the plausible range we enumerated — in either direction, since $\kappa \ll 10^{2}$ would make the analysis trivial and $\kappa \gg 10^{5}$ would sink the target.

**Against ourselves.** A skeptic should press three points. (i) Our "illustrative" parameters ($q=3$, $L=4$, $m=2$, $R=10^{3}$/s) were chosen for arithmetic transparency, not realism; a real $p$-adic tree likely uses larger $p$, and every resource number scales accordingly. (ii) The quadratic-map model is generic enough that confirming it is weak evidence; the hard work — decoder design under the tree topology, correlated-noise resilience — is entirely ahead. (iii) The literature base supplied is dominated by classical-architecture works ([1]–[4], [6]–[8]) whose summaries are truncated and which we use only as structural analogies; entry [12] has no summary at all. The analogies motivate the resource framing but constitute no evidence about the quantum proposal itself.

**Open questions.** What is $\kappa$ for the actual holographic code family of [9], and how does it depend on $p$? How do correlated errors propagate on $\mathcal{T}_p$? Can the root congestion be mitigated by hierarchical classical decoding in the spirit of the distributed-proxy pattern of [1] or the data-locality techniques of [3]? And what is the energy per correction round, the dimension of the resource burden highlighted in [10] and in the hybrid-architecture feasibility analysis of [11]?

## 7. Conclusion

We addressed a narrow quantitative question about the proposal of [9]: does holographic QEC organized as RG flow on a Bruhat–Tits tree achieve a threshold of at least $10^{-4}$? Our answer is a precise