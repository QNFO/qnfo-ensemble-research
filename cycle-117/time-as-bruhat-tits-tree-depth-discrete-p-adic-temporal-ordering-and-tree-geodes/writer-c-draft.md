# Time as Bruhat-Tits Tree Depth: Discrete $p$-Adic Temporal Ordering and Tree-Geodesic Causality

## Abstract

We develop a conjectural but internally precise model in which physical time is not a continuous real parameter but a discrete depth coordinate on a Bruhat-Tits tree: an event is a vertex, and its time is the $p$-adic valuation $v_p(x)$, equivalently the tree depth $d \in \mathbb{N}$. This identification has three structural consequences that we formalize. First, time is quantized in integer steps rooted at the tree root, which we associate with the Planck scale. Second, temporal ordering is only partial: events on different branches are incomparable, so the event set carries a forest-style partial order rather than a linear one. Third, causality is tree-geodesic: $A$ causes $B$ iff $B$ lies on the unique tree path from $A$ to the root. We derive exact combinatorial consequences: the count of vertices at depth $d$ is $N_d = (p+1)p^{d-1}$, and the fraction of comparable pairs among vertices up to depth $D$ is $C_D / \binom{V_D}{2}$, which we evaluate explicitly for $p=2$, $D=10$ as $\approx 5.87 \times 10^{-3}$. We show that the unique-path property forbids causal cycles by construction, and we state, as clearly labeled projections rather than results, the conditions under which tree geodesics could reproduce light-cone structure in a continuum limit. We situate the model in the existing Bruhat-Tits literature and identify falsifiers.

## 1. Introduction

The continuum model of time — a real parameter $t \in \mathbb{R}$ with a total order — is inherited from calculus, not from measurement. At scales approaching the Planck length $\ell_{\mathrm{P}}$, no operational procedure is known that resolves time more finely, and the assumption that the real line remains the correct substrate is exactly that: an assumption. This paper takes seriously an alternative suggested by non-Archimedean geometry: that time is a discrete depth coordinate on a Bruhat-Tits tree, the combinatorial tree on which $p$-adic valuation becomes literal distance.

The core conjecture is:

$$t \;\leftrightarrow\; v_p(x), \qquad d(x) = -v_p(x) \in \mathbb{N},$$

where $v_p$ is the $p$-adic valuation on $\mathbb{Q}_p$ and $d(x)$ is the depth of the vertex representing $x$ in the Bruhat-Tits tree of $\mathrm{PGL}_2(\mathbb{Q}_p)$. The Bruhat-Tits tree is a $(p+1)$-regular tree: every vertex has exactly $p+1$ neighbors. Depth counts edges from the root. Because the tree is a tree, there is a unique path between any two vertices, and each vertex has a unique path to the root; these two facts drive everything that follows.

Three consequences are developed here:

1. **Quantization.** Depth is integer-valued, so time comes in indivisible steps; the root is the earliest possible event, which we identify provisionally with the Planck-scale origin of a causal history.
2. **Partial ordering.** Two vertices at the same depth on different branches, or on branches that diverge before either reaches the other, have no ancestor relation. Temporal order is a partial order, not a total order.
3. **Tree-geodesic causality.** We define: $A$ causes $B$ iff $B$ lies on the unique tree path from $A$ to the root. Since $A$'s path to the root is unique and finite, this relation is automatically acyclic and antisymmetric.

The paper is organized as follows. Section 2 reviews the Bruhat-Tits literature on which the model draws. Section 3 fixes definitions. Section 4 carries out the explicit combinatorial derivations, with every input number and arithmetic step shown. Section 5 reports only what was computed. Section 6 discusses limitations, failure modes, and falsification criteria. Section 7 concludes.

We stress at the outset that this is a conjectural framework paper. No experiment is proposed that has been run, and no numerical simulation is reported. What is offered is a set of exact combinatorial theorems about the proposed temporal structure, plus explicitly labeled projections about continuum recovery.

## 2. Background and Related Work

The Bruhat-Tits tree is the standard combinatorial object encoding the incidence geometry of $\mathbb{Q}_p$ and, more generally, of local fields. Several strands of existing work are directly relevant.

**Order theory on the tree.** Heyman and the present literature line on missing branches [1] studies, for a local field $k$ and the two-by-two matrix algebra $A$ over $k$, the computation of the set of maximal orders in $A$ containing a given suborder; this set forms a sub-tree of the Bruhat-Tits tree called the *branch* of the order, and branches have been used to study the global selectivity problem and to compute local embeddings. The notion of a branch — a sub-tree selected by an algebraic condition — is structurally the same object we need: in our model, the causal past of an event is precisely the branch of the tree consisting of its ancestors, and [1] supplies the precedent that such sub-trees are well-behaved and computable.

**Tree geometry and black-hole analogues.** Osipov and coauthors' bending program [2] transplants the BTZ black hole connection to the Bruhat-Tits tree, at the cost of defining a novel "exponential function" on the $p$-adic numbers hinted at by the tree, and evaluates $\mathrm{PGL}_2(\mathbb{Q}_p)$ Wilson lines on this analogue BTZ connection. This matters for us because it demonstrates that gravitational-type causal infrastructure (horizons, connections, Wilson lines) can be carried on tree geometry — a necessary precedent if tree-geodesic causality is to reproduce relativistic causal structure in any limit.

**Statistical mechanics on trees.** The $p$-adic Potts model work [3] considers a three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p=3$ for any nonzero value of the interactions, also completely solving the uniqueness problem. For our purposes this establishes that ensemble statistics on regular trees — the statistical machinery one would need to check "recovery of standard temporal statistics" over ensembles of tree-ordered events — is mathematically mature, with exact criteria (here, the $p=3$ threshold) rather than approximations.

**Hierarchies and encoding.** The Mumford dendrogram work [4] presents an effective encoding of dendrograms by embedding them into Bruhat-Tits trees associated to $p$-adic number fields, shows how strings over a finite alphabet can be encoded in cyclotomic extensions of $\mathbb{Q}_p$, discusses $p$-adic DNA encoding, and obtains fast $p$-adic agglomerative hierarchic algorithms. This is the clearest existing demonstration that ultrametric/tree hierarchies and $p$-adic arithmetic are two views of one structure — exactly the identification our temporal conjecture exploits when it equates valuation with depth.

**Transfer maps.** The colligation paper [5] considers matrices of order $k+N$ over a $p$-adic field determined up to conjugation by elements of $\mathrm{GL}$ over the $p$-adic integers, defines a product of such conjugacy classes, and constructs analogues of characteristic (transfer) functions as maps from Bruhat-Tits trees to Bruhat-Tits buildings, also examining categorical quotients for operator colligations. Transfer maps from trees to buildings are the natural language for describing how local tree-causal structure could compose into larger geometric structures; the entry supplied gives no further quantitative detail, so we use it only as evidence that tree-to-building maps are an active, well-defined formalism.

**Field theory on the tree.** The boundary spinor work [6] calculates, for a spinor field theory on the Bruhat-Tits tree, the action and partition function of its boundary theory by integrating out the interior of the tree, finding the boundary theory very similar to a scalar field theory over the $p$-adic numbers. The technique — integrating out the interior to obtain a boundary theory — is precisely the operation our continuum-limit question requires: if time is the tree interior, the emergent continuum theory would be a boundary theory, and [6] shows this operation produces recognizably $p$-adic field theories.

**Effective limits.** The subspace effective-field-theory work [7] calculates effective actions on two subspaces of the Bruhat-Tits tree and finds that the limits of these effective field theories are the same conformal field theory over the $p$-adic numbers when the subspaces are taken to the boundary of the tree, discussing relations to the $p$-adic version of AdS/CFT. This is the strongest precedent for our projection (Section 6) that a continuum-like limit of tree time, if it exists, lives on the tree boundary — the entry establishes that boundary limits of tree field theories are well-defined and universal across subspace choices.

**Convexity and counting.** The $p$-adic equiangular lines work [8] introduces $p$-adic equiangular lines and derives the first fundamental relation between common angle, dimension, and number of lines: if $\{\tau_j\}_{j=1}^{n}$ is a set of $p$-adic $\gamma$-equiangular lines in $\mathbb{Q}_p^d$, then $|n|^2 \le |d|\max\{|n|, \gamma^2\}$, called the $p$-adic van Lint-Seidel relative bound. This shows that $p$-adic magnitude arithmetic ($|\cdot|_p$) supports packing/convexity bounds analogous to the Archimedean ones — relevant because our model's quantitative predictions will be phrased in $p$-adic magnitudes.

**Programmatic context.** The QNFO corpus entries frame the broader program. Entry [11] proposes a systematic refactoring of fundamental physics around the principle that physics is the study of invariant patterns under specified classes of transformations, stripping away anthropocentric conventions including measurement units and the privileged status of Archimedean reasoning; our model is a concrete instance of that de-Archimedization applied to time. Entries [9] ("Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree") and [10] ("Bruhat-Tits Tree as a Unifying Geometric Object") carry titles indicating the same tree-centric program, but the summaries supplied for them are empty, so we can relate them to our argument only through their titles and cannot attribute any specific result to them. Entry [12] ("Time as Epistemic Cognitive Fiction") likewise has an empty supplied summary; its title suggests a skeptical stance toward the reality of continuous time that motivates, but does not support, our conjecture, and we make no claim about its contents.

## 3. Methods

### 3.1 Definitions

**Definition 3.1 (Event).** An *event* is a vertex $v$ of the Bruhat-Tits tree $\mathcal{T}_{p}$ of $\mathrm{PGL}_2(\mathbb{Q}_p)$, a $(p+1)$-regular tree with a distinguished root $v_0$.

**Definition 3.2 (Time).** The *time* of an event $v$ is its depth $d(v) \in \mathbb{N}$, the number of edges on the unique path from $v_0$ to $v$. Under the conjectured identification, $d(v) = -v_p(x)$ for the corresponding $p$-adic coordinate $x$, and the root corresponds to the Planck-scale origin.

**Definition 3.3 (Temporal order).** For events $A, B$: $A \prec B$ iff $A$ lies on the unique path from $B$ to the root (i.e., $A$ is a proper ancestor of $B$). Events neither of which is an ancestor of the other are *incomparable*, written $A \parallel B$.

**Definition 3.4 (Tree-geodesic causality).** $A$ causes $B$ iff $B$ lies on the unique tree path from $A$ to the root, i.e., iff $A \prec B$. Causality coincides with ancestry by construction.

**Definition 3.5 (Tree distance).** The graph distance $\delta(A,B)$ is the number of edges on the unique path between $A$ and $B$. For $A \prec B$, $\delta(A,B) = d(B) - d(A)$; in general $\delta(A,B) = d(A) + d(B) - 2\,d(\mathrm{lca}(A,B))$, where $\mathrm{lca}$ is the least common ancestor. This is the ultrametric-adjusted tree metric; the associated $p$-adic norm satisfies $|x - y|_p = p^{-\delta}$ under the standard valuation-to-distance correspondence.

### 3.2 Method of analysis

All results in Section 4 are exact combinatorial counts on the $(p+1)$-regular rooted tree, derived by induction and direct summation. No simulation is performed. The single free parameter of the kinematic model is the prime $p$ (the branching excess over the trunk); the depth cutoff $D$ is a modeling choice for finite-horizon computations.

## 4. Analysis

Every input number below is either a structural constant of the model (the regularity $p+1$ of the Bruhat-Tits tree, which follows from the definition of the Bruhat-Tits tree of $\mathrm{PGL}_2(\mathbb{Q}_p)$) or an explicit modeling choice ($D$, the depth cutoff). All arithmetic is shown.

### 4.1 Vertex counts by depth

**Claim 4.1.** The number of vertices at depth $d$ is
$$N_d = (p+1)\,p^{\,d-1} \quad \text{for } d \ge 1, \qquad N_0 = 1.$$

*Derivation.* The root $v_0$ has $p+1$ neighbors, so $N_1 = p+1$. Each vertex at depth $d-1$ has $p+1$ neighbors, of which one is its parent at depth $d-2$ (for $d \ge 2$), leaving $p$ children at depth $d$. Hence
$$N_d = p\,N_{d-1} = p^{\,d-1} N_1 = (p+1)\,p^{\,d-1}. \qquad \blacksquare$$

**Worked instance ($p=2$).** $N_1 = 3$, $N_2 = 3 \cdot 2 = 6$, $N_3 = 3 \cdot 4 = 12$, $N_4 = 24$, $N_5 = 48$, $N_6 = 96$, $N_7 = 192$, $N_8 = 384$, $N_9 = 768$, $N_{10} = 1536$.

### 4.2 Total vertices up to depth $D$

**Claim 4.2.** The total number of vertices with $d(v) \le D$ is
$$V_D = 1 + \sum_{d=1}^{D} (p+1)p^{\,d-1} = 1 + (p+1)\,\frac{p^{D}-1}{p-1}.$$

*Derivation.* Sum the geometric series $\sum_{d=1}^{D} p^{\,d-1} = \frac{p^D - 1}{p-1}$ and multiply by $p+1$; add the root. $\blacksquare$

**Worked instance ($p=2$, $D=10$).** Since $p-1 = 1$:
$$V_{10} = 1 + 3\,(2^{10} - 1) = 1 + 3 \cdot 1023 = 1 + 3069 = 3070.$$
Check by summing the $N_d$ from §4.1: $1 + 3 + 6 + 12 + 24 + 48 + 96 + 192 + 384 + 768 + 1536$. Partial sums: $1+3=4$; $+6=10$; $+12=22$; $+24=46$; $+48=94$; $+96=190$; $+192=382$; $+384=766$; $+768=1534$; $+1536=3070$. ✓

### 4.3 Comparable pairs

**Claim 4.3.** For depths $d_1 < d_2$, the number of unordered comparable pairs $\{A, B\}$ with $d(A) = d_1$, $d(B) = d_2$ is exactly $N_{d_2} = (p+1)p^{\,d_2-1}$, independent of $d_1$.

*Derivation.* Each vertex $A$ at depth $d_1$ has, along each of its branches, exactly $p^{\,d_2 - d_1}$ descendants at depth $d_2$ (each generation multiplies descendants by $p$). So the number of pairs is
$$N_{d_1} \cdot p^{\,d_2 - d_1} = (p+1)p^{\,d_1-1} \cdot p^{\,d_2-d_1} = (p+1)\,p^{\,d_2 - 1} = N_{d_2}. \qquad \blacksquare$$

The independence of $d_1$ is the combinatorial signature of the ultrametric: how far up the tree you are does not affect how much lies below.

### 4.4 Total comparable pairs up to depth $D$

**Claim 4.4.** The total number of unordered comparable pairs among vertices of depth $\le D$ is
$$C_D = \sum_{d=1}^{D} d\,N_d = (p+1)\sum_{d=1}^{D} d\,p^{\,d-1}.$$

*Derivation.* A vertex $B$ at depth $d$ has exactly $d$ ancestors (the vertices on its path to the root, excluding itself), so it participates in exactly $d$ comparable pairs as the deeper member. Summing over all $B$ gives $C_D = \sum_{d=1}^{D} d\,N_d$. $\blacksquare$

**Closed form for $p = 2$.** We need $S_D = \sum_{d=1}^{D} d\,2^{\,d-1}$. Verify the closed form $S_D = (D-1)2^{D} + 1$ by induction: $S_1 = 1 = (0)\cdot 2 + 1$. ✓ If $S_{D} = (D-1)2^D + 1$, then
$$S_{D+1} = S_D + (D+1)2^{D} = (D-1)2^D + 1 + (D+1)2^D = 2D \cdot 2^D + 1 = D\,2^{D+1} + 1 = ((D+1)-1)2^{D+1} + 1. \; \blacksquare$$

**Worked instance ($p=2$, $D=10$).**
$$C_{10} = 3\,S_{10} = 3\left(9 \cdot 2^{10} + 1\right) = 3(9217) = 27651.$$

### 4.5 Fraction of comparable pairs

**Claim 4.5.** For $p = 2$, $D = 10$, the fraction of event pairs that are temporally ordered is
$$f_{10} = \frac{C_{10}}{\binom{V_{10}}{2}}.$$

*Derivation.* $\binom{3070}{2} = \frac{3070 \cdot 3069}{2} = 3070 \cdot 1534.5$. Compute: $3070 \cdot 1534 = 4{,}709{,}380$; plus $3070 \cdot 0.5 = 1535$; total $4{,}710{,}915$. Then
$$f_{10} = \frac{27651}{4710915} \approx 5.870 \times 10^{-3}.$$
Check: $4710915 \times 0.00587 = 27653.07$, and $4710915 \times 0.005869 = 27648.4$; interpolating, $27651/4710915 = 0.0058695$ to seven places. So $f_{10} \approx 5.87 \times 10^{-3}$.

**Asymptotics.** For large $D$ with fixed $p$: $V_D \sim (p+1)\frac{p^D}{p-1}$ and $C_D \sim (p+1)\,D\,\frac{p^D}{p-1}$ (since $\sum_d d\,p^{\,d-1}$ up to $D$ is dominated by the last terms, growing like $D p^{D}$ times $\frac{p}{p-1}$-order constants). Hence
$$f_D \sim \frac{D\,p^{D}}{\left(p^{D}\right)^2} \cdot \frac{p-1}{p+1}\text{-order} \;\sim\; \frac{D}{p^{D}} \to 0.$$
Temporal comparability is exponentially rare in depth: most pairs of events in this model are unordered. This is the quantitative content of "time is only partially ordered."

### 4.6 Acyclicity of tree-geodesic causality

**Claim 4.6.** The causality relation of Definition 3.4 admits no causal cycles.

*Derivation.* Suppose $A$ causes $B$ and $B$ causes $A$. Then $B$ lies on $A$'s path to the root and $A$ lies on $B$'s path to the root. Paths to the root are unique, so both statements hold only if $A$ and $B$ lie on each other's unique root-paths; but a root-path is a chain of strictly decreasing depth ending at $v_0$ ($d = 0$). If $B$ is on $A$'s root-path then $d(B) < d(A)$; if $A$ is on $B$'s root-path then $d(A) < d(B)$. Contradiction. Hence the relation is a strict partial order: irreflexive ($A \not\prec A$, since $A$'s root-path excludes $A$ itself by Definition 3.3), antisymmetric, and transitive (ancestry along a tree chain is transitive). $\blacksquare$

This addresses the closed-timelike-curve concern at the kinematic level: in a tree, "going back in time" would require revisiting an ancestor, but every vertex has exactly one parent, so there is no alternative route to any ancestor — no loop exists to traverse.

### 4.7 Geodesic distance and a light-cone analogue

**Claim 4.7.** For events $A, B$ with least common ancestor $w$ at depth $d_w$:
$$\delta(A,B) = d(A) + d(B) - 2d_w.$$

*Derivation.* The unique path $A \to B$ goes $A \to w$ (length $d(A) - d_w$) then $w \to B$ (length $d(B) - d_w$); total $d(A) + d(B) - 2d_w$. $\blacksquare$

The set of events reachable "causally after" $A$ within $\Delta$ steps is the ball of radius $\Delta$ around $A$ in the tree, which contains $A$'s ancestors within $\Delta$ (the past cone) and $A$'s descendants within $\Delta$ (the future cone), but — unlike the relativistic light cone — no "sideways" events except through the common ancestor. The structural mismatch with the relativistic light cone (which is a double cone in a continuum, with a continuum of directions) is discussed in Section 6; we do not claim recovery here.

## 5. Results

We report only quantities derived in Section 4.

**R1 (Vertex growth).** On the Bruhat-Tits tree of $\mathrm{PGL}_2(\mathbb{Q}_p)$, the number of events at time-step $d$ is $N_d = (p+1)p^{\,d-1}$ (Claim 4.1). For $p = 2$: $N_1 = 3$, $N_{10} = 1536$.

**R2 (Event budget).** For $p = 2$ and horizon $D = 10$, the total event count is $V_{10} = 3070$ (Claim 4.2, verified by two independent summations).

**R3 (Comparability scarcity).** For $p = 2$, $D = 10$, the number of temporally ordered pairs is $C_{10} = 27651$ out of $\binom{3070}{2} = 4{,}710{,}915$ total pairs, a fraction $f_{10} \approx 5.87 \times 10^{-3}$ (Claims 4.4–4.5). Asymptotically $f_D \sim D/p^{D} \to 0$: in this model, almost all pairs of events are temporally incomparable.

**R4 (Depth-independence).** The number of ordered pairs between depth $d_1$ and depth $d_2 > d_1$ is $N_{d_2}$, independent of $d_1$ (Claim 4.3) — an exact ultrametric signature.

**R5 (No causal cycles).** Tree-geodesic causality is a strict partial order; causal cycles, including closed timelike curves, are impossible by construction (Claim 4.6).

**R6 (Distance formula).** $\delta(A,B) = d(A) + d(B) - 2d_w$ where $d_w$ is the depth of the least common ancestor (Claim 4.7).

**Projection P1 (not a result).** If tree-geodesic causal structure is to reproduce relativistic light-cone structure in a continuum limit, the limit must be taken at the tree boundary, in the sense of [7], where effective field theories on tree subspaces converge to a $p$-adic conformal field theory. *Assumptions:* (i) the identification $t \leftrightarrow v_p(x)$ survives the limit; (ii) the boundary theory's causal structure is governed by the $p$-adic norm as in [6]. *Uncertainty:* this is a structural conjecture supported only by the analogies recorded in Section 2; no numerical recovery of the light cone is claimed or computed here.

**Projection P2 (not a result).** If the root corresponds to the Planck scale and one depth step corresponds to one Planck time, then a horizon of $D$ steps spans $D$ Planck times; for $D = 10$ this is $10$ Planck times, an interval of order $10^{-43}$ s in conventional units only if the Planck-time conversion is assumed — we state the conversion as an assumption, not a derivation, since no input in this paper fixes the physical scale of one depth step.

## 6. Discussion

**Limitations.** The model as constructed is a kinematic skeleton: it fixes ordering and counting but assigns no dynamics. The identification $t \leftrightarrow v_p(x)$ is a conjecture, not a derivation; nothing in the combinatorics above forces the root to be the Big Bang or one depth step to be a Planck time (Projection P2 is explicitly assumption-laden). The prime $p$ is a free parameter with no observed value; the $p=3$ phase-transition threshold found in the Potts analysis [3] is the only hint in the surveyed literature that specific primes may be dynamically distinguished, and that result concerns a different model (a Potts system on a Cayley tree), not temporal ordering.

**Failure modes.** The most serious structural mismatch is with relativity. In special relativity, the causal past of an event is a continuum of directions — a solid cone — and the ordering is partial but *dense* along every timelike curve. In the tree model, the causal past of an event is a finite chain of $d$ ancestors: linear, not conical, and totally ordered internally. Claim 4.3's depth-independence and the scarcity result R3 show that most event pairs are unordered, which is cone-like in spirit; but the *shape* of the past is a chain, not a cone. If empirical causal structure requires a continuum of causal directions at every event, the single-trunk tree model fails, and one would need either a product structure (tree × internal degrees of freedom) or a building rather than a tree — the direction suggested by the tree-to-building transfer maps of [5], though the supplied summary of [5] gives no detail connecting such maps to causality.

**What would falsify the conjecture.** (i) If the boundary-limit program of [7] cannot produce a causal structure richer than the $p$-adic conformal theory it yields — i.e., if no light-cone analogue emerges at the boundary — the continuum-recovery projection P1 fails. (ii) If partial ordering with $f_D \to 0$ contradicted observed temporal statistics (e.g., if macroscopic events must be almost surely mutually ordered, as everyday experience suggests), the model would need a mechanism — not present here — that collapses incomparable branches into a common frame; the dendrogram-embedding techniques of [4] might supply such a mechanism (agglomerative merging of branches), but this is speculation. (iii) If closed timelike curves are demonstrated in the underlying physics in a way that no partial order can accommodate, Claim 4.6's acyclicity becomes a defect rather than a feature.

**Against ourselves.** The strongest internal objection: the model's exact results (R1–R6) are pure combinatorics of any $(p+1)$-regular rooted tree and say nothing specific about physics; the physical content lives entirely in the unproven identification $t \leftrightarrow v_p(x)$ and in projections P1–P2. A skeptic can accept every derivation and reject the paper's thesis. The reply is that the combinatorics is nonetheless nontrivial and predictive in structure — R3's exponential scarcity of ordering and R4's depth-independence are sharp, falsifiable-in-spirit features that a continuum time does not have — and that the boundary-limit machinery of [6,7] gives a concrete, existing mathematical route by which the conjecture could be tested. A second objection: the QNFO program entries [9,10,12] cannot be leveraged because their supplied summaries are empty; the paper's grounding in that program is therefore motivational, not evidential, and we flag this openly rather than overclaiming.

**Open questions.** What is the correct observable that distinguishes $p=2$ from $p=3$ branching in temporal statistics? Does the boundary theory of [6], being "very similar to a scalar field theory over $p$-adic numbers," support a wave equation whose characteristic surfaces are tree geodesics? Can the equiangular-line bound of [8] constrain how many mutually incomparable "causal directions" can coexist at a vertex, giving a $p$-adic analogue of cone dimension?

## 7. Conclusion

We have formalized the conjecture that time is Bruhat-Tits tree depth — a discrete, $p$-adic-valuation coordinate — and derived its exact kinematic consequences: exponential vertex growth $N_d = (p+1)p^{\,d-1}$; a partially ordered event set in which the ordered fraction among $V_{10} = 3070$ events is $\approx 5.87 \times 10^{-3}$ and vanishes as $D/p^{D}$; a provably acyclic, uniquely-geodesic causality relation with distance $\delta(A,B) = d(A) + d(B) - 2d_w$; and an ultrametric depth-independence signature. The framework's physical claims remain conjectural, and its recovery of relativistic causal structure is an explicitly labeled projection routed through the existing boundary-limit results on Bruhat-Tits tree field theories. The contribution is a precise, falsifiable combinatorial skeleton for non-Archimedean time, with the failure modes and open questions stated plainly.

## References

[1] ar