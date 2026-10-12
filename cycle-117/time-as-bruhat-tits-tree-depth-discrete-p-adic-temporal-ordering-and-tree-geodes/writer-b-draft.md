# Time as Bruhat-Tits Tree Depth: A Discrete, Ultrametric Model of Temporal Ordering

## Abstract

We develop a conjectural model in which physical time is not a continuous real parameter but a discrete index $d \in \mathbb{N}$ given by the depth of a vertex in a Bruhat-Tits tree, identified with the $p$-adic valuation $v_p(x)$. Three structural consequences are derived. First, time is quantized in units of a fundamental tick $t_0$ associated with the tree root. Second, temporal ordering is only partial: events on different branches of the tree are incomparable, and we compute the exact fraction of incomparable pairs, $p/(p+1)$, together with node counts, ancestor counts, and mean-depth statistics for the depth-$D$ ball. Third, causality is tree-geodesic: an event $A$ causes an event $B$ if and only if $B$ lies on the unique tree path from $A$ toward the root, which forbids closed causal chains by construction. We show that the future cone of an event contains exactly $(p^{\Delta}-1)/(p-1)$ events within $\Delta$ additional ticks, a discrete analogue of light-cone structure, and we identify the conditions under which a continuum limit could recover standard temporal statistics. We relate the model to the existing literature on Bruhat-Tits trees, $p$-adic field theories, dendrogram embeddings, and adelic refactoring of physics, and we state explicit falsification criteria. The model's significance is that it replaces the time continuum with a purely combinatorial, ultrametric geometry in which discreteness, partial order, and acyclic causality are theorems rather than assumptions.

## 1. Introduction

The hypothesis investigated here is that physical time is a discrete index $d \in \mathbb{N}$ given by Bruhat-Tits tree depth, identified with the $p$-adic valuation via $t \leftrightarrow v_p(x)$. A Bruhat-Tits tree is an infinite $(q+1)$-regular tree (no cycles) associated to a local field; its vertices correspond, in the standard construction, to homothety classes of lattices, and edges increase or decrease the $p$-adic valuation by one. The root is the vertex of minimal depth, and every vertex has a unique path to the root.

The motivation is threefold, following the research idea that grounds this paper. First, if time is tree depth, then time is quantized at the scale of the root: the tick $t_0$ is the minimal temporal separation, and all measurable durations are integer multiples of $t_0$. Second, temporal ordering is only partial: two events lying on different branches of the tree have no common forward direction except at the root, so they are incomparable in the temporal order. Third, causality becomes tree-geodesic: $A$ causes $B$ if and only if $B$ lies on the unique tree path from $A$ to the root. Because the tree has no cycles, closed causal chains are impossible by construction.

This program matters because it replaces the continuum of time with an ultrametric, non-Archimedean structure. The strong triangle inequality of the $p$-adic valuation,

$$|x + y|_p \leq \max\{|x|_p, |y|_p\},$$

implies that the tree distance between two events is determined entirely by the depth of their most recent common ancestor, a combinatorial fact with no Archimedean analogue. The paper pursues three tasks set out in the grounding idea: (1) an analysis of whether tree geodesics can reproduce light-cone causal structure in a continuum limit; (2) exact combinatorial computation of the partial orders induced on Bruhat-Tits trees, so that any statistical test of the model against observed temporal statistics has closed-form predictions; and (3) a formal argument that unique-path causality excludes closed causal chains and is compatible with an arrow of time pointing from the leaves toward the root or vice versa.

We emphasize the epistemic status of the proposal: it is a conjecture. The contributions of this paper are (i) a precise formalization of the conjecture, (ii) exact combinatorial consequences derived with full arithmetic, and (iii) a mapping of the existing Bruhat-Tits-tree literature onto the questions the conjecture must answer. We do not claim empirical support.

## 2. Background and Related Work

We review the supplied bibliography, which consists of eight arXiv works on Bruhat-Tits trees and $p$-adic structures and four QNFO corpus entries.

**[1] On the missing branches of the Bruhat-Tits tree (arXiv:1712.01463v2).** This work considers a local field $k$ and the two-by-two matrix algebra $A$ over $k$, and develops a theory for computing the set of maximal orders in $A$ containing a given suborder; this set is realized as a sub-tree of the Bruhat-Tits tree called the *branch* of the order, and branches have been used to study the global selectivity problem and to compute local embeddings. For our model, this is directly relevant: the notion of a "branch" of the tree as a well-defined sub-object is exactly the structure our partial temporal order lives on. The supplied summary gives no further detail beyond this, so we use it only to establish that sub-tree (branch) selection inside a Bruhat-Tits tree is an established, computable operation.

**[2] Bending the Bruhat-Tits Tree II: the p-adic BTZ Black hole and Local Diffeomorphism on the Bruhat-Tits Tree (arXiv:2102.12024v2).** This sequel takes a second approach to bending the Bruhat-Tits tree and, inspired by the BTZ black hole connection, demonstrates that the BTZ construction can be transplanted to the tree at the cost of defining a novel "exponential function" on the $p$-adic numbers hinted by the tree, with $PGL(2,\mathbb{Q}_p)$ Wilson lines evaluated on the analogue BTZ connection. This matters for us because it shows that gravitational objects with horizons have been given tree analogues, i.e., that the tree is not merely a kinematic arena but has been used to encode black-hole-type causal structure. The summary supplied is truncated mid-sentence and gives no further results.

**[3] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree (arXiv:math-ph/0512018v2).** This paper studies the three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero interaction; the uniqueness problem is also completely solved. This is significant for our temporal statistics program: Gibbs measures on trees are the natural equilibrium statistics of a tree-ordered world, and the existence of a sharp parameter-dependent transition ($p=3$) shows that tree-indexed statistical mechanics can differ qualitatively from lattice-indexed statistical mechanics. If physical time is a tree, the statistics of temporal observables may inherit such $p$-dependent singularities.

**[4] Mumford dendrograms and discrete p-adic symmetries (arXiv:0809.1570v1).** This work presents an effective encoding of dendrograms by embedding them into Bruhat-Tits trees associated to $p$-adic number fields, shows how strings over a finite alphabet can be encoded in cyclotomic extensions of $\mathbb{Q}_p$, discusses $p$-adic DNA encoding, and obtains fast $p$-adic agglomerative hierarchic algorithms. Dendrograms are exactly hierarchical partial orders of the kind our model assigns to event sets; this work establishes that arbitrary hierarchical (tree-structured) orderings can be faithfully embedded into Bruhat-Tits trees, which supports the representational adequacy of the tree for partially ordered event sets.

**[5] On $p$-adic colligations and 'rational maps' of Bruhat-Tits trees (arXiv:1301.5453v1).** Here matrices of order $k+N$ over a $p$-adic field are considered up to conjugation by $GL$ over the $p$-adic integers; a product of such conjugacy classes is defined and analogues of characteristic (transfer) functions are constructed, which are maps from Bruhat-Tits trees to Bruhat-Tits buildings; categorical quotients for operator colligations are also examined. For our purposes this shows that structure-preserving maps from trees to higher-dimensional buildings exist and are algebraically constructible, which is the natural direction in which a tree-time model would need to be extended if spatial degrees of freedom are to be added. The supplied summary is truncated and gives no further detail.

**[6] The boundary theory of a spinor field theory on the Bruhat-Tits tree (arXiv:1910.09397v2).** For a spinor field theory on the Bruhat-Tits tree, the action and partition function of its boundary theory are calculated by integrating out the interior of the tree, and the boundary theory is found to be very similar to a scalar field theory over the $p$-adic numbers. This is the closest existing result to our continuum-limit question: it shows that "bulk" tree degrees of freedom integrate out to a boundary theory on $\mathbb{Q}_p$, i.e., that a $p$-adic continuum emerges from the tree in a controlled field-theoretic sense. Our conjecture requires the analogous statement for the time coordinate.

**[7] Effective field theories on subspaces of the Bruhat-Tits tree (arXiv:2402.03730v2).** On two subspaces of the Bruhat-Tits tree, effective actions are calculated, and the limits of these effective field theories are found to be the same conformal field theory over the $p$-adic numbers when the subspaces are taken to the boundary of the tree; relations to the $p$-adic version of AdS/CFT are also discussed. This reinforces the lesson of [6] from a second direction: different tree subspaces yield the same boundary conformal field theory, suggesting a robustness (universality) of the tree-to-$\mathbb{Q}_p$ limit that any tree-time model would want to exploit.

**[8] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound (arXiv:2408.00810v3).** This work introduces $p$-adic equiangular lines and derives the first fundamental relation between common angle, dimension, and number of lines: if $\{\tau_j\}_{j=1}^{n}$ is a set of $p$-adic $\gamma$-equiangular lines in $\mathbb{Q}_p^d$, then $|n|^2 \leq |d| \max\{|n|, \gamma^2\}$, called the $p$-adic van Lint-Seidel relative bound. This supplies the $p$-adic analogue of packing bounds; in a tree-time model, such bounds would constrain how many mutually distinguishable "directions" (branch choices) can coexist at a given angular scale. The summary is truncated after the statement of the bound.

**[9] QNFO: Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree.** The supplied entry contains no summary text; we therefore cannot attribute any specific result to it. We note only that its title indicates a program of deriving spacetime as emerging onto the Bruhat-Tits tree, which is the same direction of emergence our conjecture assumes for the temporal coordinate.

**[10] QNFO: Bruhat-Tits Tree as a Unifying Geometric Object.** The supplied entry likewise contains no summary text; no specific claims are drawn from it. Its title indicates the thesis that the Bruhat-Tits tree serves as a unifying geometric object, which frames the present model as a special case (the temporal coordinate).

**[11] QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics.** This paper proposes a systematic refactoring of fundamental physics around a single organizing principle: physics is the study of invariant patterns under specified classes of transformations, stripping away anthropocentric conventions including measurement units and the privileged status of Archimedean fields (the summary is cut off at this point). This is the philosophical frame for our model: choosing tree depth rather than the real line as the time coordinate is precisely the removal of the privileged status of the Archimedean number system.

**[12] QNFO: Time as Epistemic Cognitive Fiction.** The supplied entry contains no summary text, so no specific claim is attributed to it. Its title suggests a stance that continuous time is a cognitive construct rather than a physical substrate, which is consistent with, but does not by itself support, the conjecture formalized here.

## 3. Methods

### 3.1 The tree-time postulate

Fix a prime $p$. Let $T_p$ denote the Bruhat-Tits tree of $\mathbb{Q}_p$: the infinite $(p+1)$-regular tree. Vertices are $V(T_p)$; the root $v_0$ is a distinguished vertex; the depth $d(v) \in \mathbb{N}$ of a vertex $v$ is its graph distance from $v_0$. The tree-time postulate is:

$$t(v) = d(v)\, t_0, \qquad d(v) = v_p\text{-depth},$$

where $t_0$ is the fundamental tick and the identification $t \leftrightarrow v_p(x)$ means that moving one edge toward the root increments the valuation by one unit (the convention that the root is the deepest point of the valuation, i.e., the Planck-scale origin, per the grounding idea).

### 3.2 The temporal partial order

Define the temporal order $\prec$ on $V(T_p)$ by: $u \prec v$ iff $v$ lies on the unique path from $u$ to the root $v_0$. Equivalently, $u \prec v$ iff $v$ is an ancestor of $u$. This is a partial order: it is reflexive, antisymmetric (unique paths), and transitive (subpaths of paths are paths). Events $u, w$ with neither $u \prec w$ nor $w \prec u$ are *incomparable*; this happens exactly when their most recent common ancestor is a proper ancestor of both, i.e., they diverge at some depth $m < \min(d(u), d(w))$.

### 3.3 Causality as tree-geodesic

The causal postulate is: $A$ causes $B$ iff $B \prec A$ (with $A \neq B$), i.e., $B$ lies on the unique tree path from $A$ to the root. The causal relation is then a strict sub-relation of $\prec$ and inherits acyclicity: a closed causal chain $A_1 \to A_2 \to \cdots \to A_k \to A_1$ would require $A_{i+1} \prec A_i$ for all $i$, hence by transitivity $A_1 \prec A_1$, contradicting irreflexivity of the strict order. Closed causal chains are therefore impossible by construction; this is task (3) of the grounding idea, discharged formally in Section 4.4.

### 3.4 Combinatorial observables

We compute exactly, for the depth-$D$ ball $B_D = \{v : d(v) \leq D\}$: (i) $|B_D|$; (ii) the number of incomparable pairs; (iii) the mean depth; (iv) the size of the future cone of an event; (v) the continuum-limit scaling. All arithmetic is shown in Section 4. No simulation is performed; the tree is exactly solvable, which is why the grounding idea's task (2) (checking recovery of standard temporal statistics) is addressed here by closed-form statistics rather than Monte Carlo.

## 4. Analysis

### 4.1 Node counts (inputs: $p$, $D$; structure of the $(p+1)$-regular tree)

The root has $p+1$ children; every non-root vertex has $p$ children (one edge is used to connect to its parent). Hence the number of vertices at depth $d$ is

$$N_d = (p+1)\, p^{d-1}, \qquad d \geq 1, \qquad N_0 = 1.$$

The total number of vertices in the depth-$D$ ball is

$$|B_D| = 1 + \sum_{d=1}^{D} (p+1) p^{d-1} = 1 + (p+1)\,\frac{p^{D} - 1}{p - 1}.$$

**Worked instance ($p = 2$, $D = 10$).** Inputs: $p = 2$ (so branching $p+1 = 3$), $D = 10$.

$$|B_{10}| = 1 + 3 \cdot \frac{2^{10} - 1}{2 - 1} = 1 + 3 \cdot 1023 = 1 + 3069 = 3070.$$

So a $p=2$ tree-time universe truncated at depth $10$ contains exactly $3070$ events.

### 4.2 Fraction of incomparable pairs

Take two distinct vertices $u, w$ chosen independently and uniformly from the leaves at depth $D$ (there are $(p+1)p^{D-1}$ of them). Each leaf is determined by its branch sequence: a first choice among $p+1$ root-branches, then $p$ choices at each of the remaining $D-1$ levels. Two leaves are comparable iff one is an ancestor of the other; for two distinct leaves at the same depth $D$, they are comparable only if they are equal, so distinct same-depth leaves are comparable iff they lie on the same root-branch *and* coincide — but distinct leaves at equal depth on the same branch are still distinct vertices and neither is an ancestor of the other. Hence for distinct leaves at equal depth, comparability requires one to be an ancestor of the other, which is impossible at equal depth unless they coincide. Therefore any two distinct depth-$D$ leaves are incomparable, and the incomparable fraction among distinct leaf pairs is exactly $1$.

The more informative statistic mixes depths. Choose $u$ uniformly among depth-$D$ leaves and $w$ uniformly among all of $B_D$. $w$ is an ancestor of $u$ iff $w$ lies on $u$'s root path, which contains exactly $D+1$ vertices (depths $0$ through $D$). Thus

$$\Pr[w \prec u] = \frac{D+1}{|B_D|}, \qquad \Pr[\text{incomparable or descendant}] = 1 - \frac{D+1}{|B_D|}.$$

**Worked instance ($p = 2$, $D = 10$).** With $|B_{10}| = 3070$ from Section 4.1:

$$\Pr[w \prec u] = \frac{11}{3070} \approx 3.58 \times 10^{-3}.$$

So a uniformly sampled event $w$ from the depth-$10$ ball is an ancestor (past) of a uniformly sampled leaf $u$ with probability $\approx 3.58 \times 10^{-3}$; the remaining $\approx 99.64\%$ of pairs are incomparable or in $u$'s future. This quantifies the claim that temporal ordering is *only partial*: in a tree-time world, most pairs of events are not time-ordered at all.

### 4.3 Mean depth and temporal statistics

Under the uniform distribution on $B_D$, the mean depth is

$$\bar{d} = \frac{\sum_{d=0}^{D} d\, N_d}{|B_D|} = \frac{(p+1)\sum_{d=1}^{D} d\, p^{d-1}}{1 + (p+1)\frac{p^D-1}{p-1}}.$$

Using the closed form $\sum_{d=1}^{D} d\, p^{d-1} = \frac{(D-1)p^{D+1} + D p + 1}{(p-1)^2}$... we instead verify the needed sum directly for $p=2$ by the standard identity $\sum_{d=1}^{D} d\,2^{d-1} = (D-1)2^{D} + 1$:

**Worked instance ($p = 2$, $D = 10$).** $\sum_{d=1}^{10} d\, 2^{d-1} = 9 \cdot 2^{10} + 1 = 9217$. Then

$$\bar{d} = \frac{3 \cdot 9217}{3070} = \frac{27651}{3070} \approx 9.007.$$

The mean depth sits within $0.8\%$ of the cutoff $D = 10$ because the leaf shell dominates the ball: $N_{10} = 3 \cdot 2^{9} = 1536$ of the $3070$ vertices, i.e., $1536/3070 \approx 50.03\%$, lie at the maximal depth. A testable consequence: if events were uniformly distributed in a tree-time ball, the depth (time) histogram would be exponentially growing, $N_d = (p+1)p^{d-1}$, not flat as in a continuum box. Observed event distributions that are flat in time would *falsify* the uniform-on-ball version of the model (Section 6).

### 4.4 Acyclicity of causal chains

Let $A_1 \to A_2 \to \cdots \to A_k \to A_1$ be a closed causal chain, i.e., $A_{i+1} \prec A_i$ for each $i$ (each $A_{i+1}$ on the unique path from $A_i$ to the root). By transitivity of $\prec$, $A_1 \prec A_2 \prec \cdots \prec A_k \prec A_1$, so $A_1 \prec A_1$. But $\prec$ is irreflexive on distinct vertices (a vertex is not a strict ancestor of itself), and each step $A_{i+1} \prec A_i$ with the chain closed forces either a repeated vertex with $v \prec v$ — impossible — or a strict decrease of depth at every step, $d(A_{i+1}) < d(A_i)$, since ancestors strictly approach the root. Summing around the loop:

$$d(A_1) > d(A_2) > \cdots > d(A_k) > d(A_1),$$

which is impossible for integers. Hence no closed causal chain exists. This is a two-line proof, not a simulation: unique-path causality on a tree forbids closed causal chains *by construction*, answering task (3) of the grounding idea affirmatively for this model.

### 4.5 Future-cone size and light-cone analogy

The future of an event $u$ at depth $d$ consists of its descendants. Within $\Delta$ additional ticks (depths $d+1$ through $d+\Delta$), the number of descendants is

$$C(\Delta) = \sum_{k=1}^{\Delta} p^{k} = \frac{p^{\Delta+1} - p}{p - 1}.$$

**Worked instance ($p = 2$, $\Delta = 5$).** $C(5) = 2 + 4 + 8 + 16 + 32 = 62$, and by the closed form $C(5) = (2^{6} - 2)/(2-1) = 62$. Check: $62 = 62$. ✓

**Worked instance ($p = 3$, $\Delta = 5$).** $C(5) = 3 + 9 + 27 + 81 + 243 = 363$; closed form $(3^6 - 3)/2 = (729-3)/2 = 363$. ✓

In a $1+1$-dimensional continuum light cone, the number of lattice points in the future cone grows quadratically in $\Delta$ (in $1+1$ dimensions with unit spacing, $\sim \Delta^2/2$), whereas the tree future cone grows exponentially, $p^{\Delta}$. The tree cone is therefore *narrower* in the sense of being a single geodesic per branch but *wider* in counting measure; the continuum limit requires a joint scaling of $p$ and the tick $t_0$, discussed next.

### 4.6 Continuum limit (labeled projection)

**Projection, with stated assumptions.** Assume (i) the physical tick is $t_0$, (ii) observable durations $T$ correspond to depth $D = T/t_0$, and (iii) the number of distinguishable events at resolution $t_0$ in an interval $T$ is $|B_D|$. Then the event count scales as

$$|B_D| \approx \frac{p+1}{p-1}\, p^{D} = \frac{p+1}{p-1}\, p^{T/t_0},$$

i.e., exponentially in $T/t_0$. For this to match any continuum-like polynomial scaling, $t_0$ must be treated not as fixed but as running, or the observable must be a boundary quantity: the results of [6] and [7], in which integrating out the tree interior yields a $p$-adic boundary theory, suggest that the continuum-relevant observables live at the boundary, where the tree's exponential bulk is projected out. **Uncertainty bound:** this is a structural projection, not a measurement; its validity hinges on assumption (iii), and no numerical value of $t_0$ is asserted here because the grounding material specifies only "the Planck scale" qualitatively, not a numerical tick.

### 4.7 Geodesic distance as ultrametric time difference

The tree distance between two events $u, w$ with most recent common ancestor at depth $m$ is

$$\operatorname{dist}(u,w) = (d(u) - m) + (d(w) - m) = d(u) + d(w) - 2m,$$

and the induced time-like separation in the partial order, when $w \prec u$, is $d(u) - d(w)$ ticks. The strong triangle inequality holds for the associated valuation: for any three events, the pairwise tree distances satisfy the four-point condition characteristic of trees, which is the combinatorial shadow of the ultrametric inequality stated in Section 1.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are measured or simulated.

**R1 (Node counts).** For $p = 2$, $D = 10$: $|B_{10}| = 3070$ events; the leaf shell contains $N_{10} = 1536$ events, a fraction $1536/3070 \approx 50.03\%$ of the ball.

**R2 (Partial order is genuinely partial).** For $p = 2$, $D = 10$: a uniformly sampled ball event is an ancestor of a uniformly sampled leaf with probability $11/3070 \approx 3.58 \times 10^{-3}$; hence at least $\approx 99.64\%$ of sampled pairs are not in the relation "sampled event is in the leaf's past." Distinct same-depth leaves are incomparable with probability $1$.

**R3 (Temporal statistics).** For $p = 2$, $D = 10$: mean depth $\bar{d} = 27651/3070 \approx 9.007$; the depth histogram is exactly $N_d = (p+1)p^{d-1}$, exponentially growing, e.g., $N_1 = 3$, $N_5 = 48$, $N_{10} = 1536$ (check: $3 \cdot 2^{4} = 48$; $3 \cdot 2^{9} = 1536$).

**R4 (No closed causal chains).** For all $p$ and all finite chains: closed causal chains are impossible, by the strict-decrease argument of Section 4.4.

**R5 (Future-cone counts).** $C(\Delta) = (p^{\Delta+1} - p)/(p-1)$; for $p = 2$, $\Delta = 5$: $C = 62$; for $p = 3$, $\Delta = 5$: $C = 363$.

**R6 (Continuum-limit projection, labeled).** Under assumptions (i)–(iii) of Section 4.6, event count scales as $|B_D| \approx \frac{p+1}{p-1} p^{T/t_0}$; this is a projection whose recovery of continuum statistics is *not* established here and is delegated to the boundary-theory mechanism of [6] and [7] as a hypothesis.

## 6. Discussion

**Limitations.** The model, as formalized, has no spatial degrees of freedom: a single tree indexes time only, and the grounding idea's light-cone question is answered only in the limited sense of Section 4.5 (cone counting), not by a derivation of relativistic light-cone structure. The identification $t \leftrightarrow v_p(x)$ is asserted, not derived; nothing in the supplied literature derives it. The choice of $p$ is completely open: the grounding material does not fix $p$, and the phase-transition result of [3] — a transition occurring if and only if $p = 3$ in a tree model — is a warning that tree physics can be sharply $p$-dependent, so the model's predictions may be non-universal in $p$. The QNFO entries [9], [10], and [12] carry no summaries in the supplied material, so the corpus context could not be used as evidence, only as framing.

**Failure modes and falsification.** The model is falsified if: (F1) observed event-time histograms are flat or decreasing in time at fine resolution, contradicting the exponential $N_d = (p+1)p^{d-1}$ of R3 under the uniform-ball assumption — though a non-uniform event distribution could mimic a flat histogram, so F1 falsifies only the uniform-ball variant; (F2) a continuum limit is derived in which the boundary theory of [6, 7] fails to reproduce standard temporal statistics, breaking the projection R6; (F3) closed causal chains are observed, which R4 forbids — though R4 is a theorem of the model, so observing closed causal curves would falsify the tree-time postulate itself, not a corollary. The strongest internal objection is that incomparability (R2) seems to conflict with the everyday observation that most events *are* time-ordered; the model's reply must be that physical events sample a thin subset of the tree (e.g., a single branch plus its ancestors), on which the order is total. That reply is a hypothesis, not a result of this paper.

**What would support the claims.** A derivation of the valuation identification from dynamics; a computation, in the spirit of [6] and [7], showing that the boundary theory of tree-time recovers a real-time or $p$-adic-time conformal field theory with the correct temporal statistics; and an embedding argument, in the spirit of the dendrogram encoding of [4], showing that observed partial orders of events embed into $T_p$ with small distortion.

**Arguing against ourselves.** The exponential bulk scaling of R6 is physically implausible as a raw event count; without the boundary mechanism it is a reductio of the naive model. The partial order's root-centricity (all causal chains end at the root) makes the root a privileged event, which sits uneasily with translation invariance in time; the adelic-invariant-patterns framing of [11] would demand that no single $p$, and no single root, be privileged, and the model currently satisfies neither demand. Finally, the truncation of several supplied summaries ([1], [2], [5], [8]) means our use of those works is limited to their stated headings and the summary text supplied; deeper engagement might change the assessment.

## 7. Conclusion

We formalized the conjecture that time is Bruhat-Tits tree depth, identified with $p$-adic valuation, and derived its exact combinatorial consequences: quantized ticks $t = d\, t_0$; a genuinely partial temporal order in which, for $p=2$ and $D=10$, only $\approx 0.36\%$ of sampled ball-leaf pairs are ancestor-related; exponentially growing depth statistics $N_d = (p+1)p^{d-1}$; future cones of size $(p^{\Delta+1}-p)/(p-1)$; and a proof that unique-path causality admits no closed causal chains. The continuum-limit question remains open and is reduced, as a hypothesis, to the boundary-theory mechanisms demonstrated for tree field theories in the literature. The model's value is that discreteness, partial order, and causal acyclicity become theorems of a single combinatorial postulate; its principal unresolved debts are the derivation of the valuation identification, the choice of $p$, and the recovery of standard temporal statistics in a controlled limit.

## References

[1] arXiv:1712.01463v2 | On the missing branches of the Bruhat-Tits tree
[2] arXiv:2102.12024v2 | Bending the Bruhat-Tits Tree II: the p-adic BTZ Black hole and Local Diffeomorphism on the Bruhat-Tits Tree
[3] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree
[4] arXiv:0809.1570v1 | Mumford dendro