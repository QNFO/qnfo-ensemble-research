# Time as Bruhat‑Tits Tree Depth: Discrete $p$‑Adic Temporal Ordering and Tree‑Geodesic Causality

## Abstract

Physical time is modeled as the integer depth $d\in\mathbb{N}$ of a vertex in a rooted $(p\!+\!1)$‑regular Bruhat‑Tits tree, identified with the $p$‑adic valuation $v_{p}(x)$. This replaces the continuum real line with a discrete ultrametric coordinate. The gap addressed is the lack of a mathematically exact framework that yields discreteness, partial ordering, and acyclic causality from first principles. We derive exact combinatorial counts for vertex numbers, comparable pairs, and future‑cone sizes, and we prove the impossibility of causal cycles. For $p=2$ and depth $D=10$ we obtain $V_{10}=3070$ events, $C_{10}=27651$ ordered pairs, a comparability fraction $f_{10}\approx5.8696\times10^{-3}$, mean depth $\bar d\approx9.0068$, and future‑cone size $C(5)=62$. These results show that ordered pairs become exponentially rare with depth. The model’s practical impact is to provide a rigorously solvable skeleton for theories that seek a non‑Archimedean temporal substrate, and it supplies concrete falsification criteria for experimental or observational tests.

## 1. Introduction

Quantum‑gravity researchers and relativistic cosmologists face a concrete decision problem: the standard real‑valued time parameter $t\in\mathbb{R}$ underlies both quantum evolution and relativistic causality, yet no operational procedure resolves intervals below the Planck scale, and the total‑order assumption blocks attempts to reconcile discrete quantum dynamics with continuous spacetime. If time were instead a discrete depth coordinate on a Bruhat‑Tits tree, the Planck‑scale root would anchor a fundamental tick $t_{0}$, partial ordering would emerge from tree ancestry, and causality would be guaranteed acyclic by construction. This would change the design of quantum‑gravity models, allowing them to replace the continuum hypothesis with a combinatorial geometry that automatically enforces discreteness, partial order, and causal consistency.

**Contributions.**
1. Formal definition of tree‑depth time and its basic properties (Section 3).  
2. Exact combinatorial derivations of vertex counts, comparable‑pair statistics, and future‑cone sizes (Section 4).  
3. Mapping of these results onto existing Bruhat‑Tits‑tree literature, establishing precedents for sub‑tree causality and $p$‑adic field limits (Section 2).

## 2. Background and Related Work

**[1]** develops the notion of a *branch*—a sub‑tree of the Bruhat‑Tits tree defined by maximal orders containing a given suborder. This provides a precedent for treating the causal past of an event as a well‑defined subtree of ancestors.

**[2]** constructs a BTZ‑type black‑hole geometry on the Bruhat‑Tits tree and shows that a novel “exponential function” on $\mathbb{Q}_{p}$ enables a local diffeomorphism between the deformed tree and the pure tree. This demonstrates that gravitational‑like causal structures can be encoded on tree geometry.

**[3]** proves that a three‑state $p$‑adic Potts model on a Cayley tree of order two exhibits a phase transition if and only if $p=3$. The analysis supplies exact recursive equations for Gibbs measures on regular trees, illustrating that statistical mechanics on such trees admits closed‑form solutions.

**[4]** embeds hierarchical dendrograms into Bruhat‑Tits trees and shows that any finite hierarchical clustering can be represented as a subtree of $\mathscr{T}_{\mathbb{Q}_{p}}$. This establishes the representational adequacy of the tree for partially ordered event sets.

**[5]** defines transfer (characteristic) maps from Bruhat‑Tits trees to Bruhat‑Tits buildings via $p$‑adic colligations. These maps illustrate how local tree‑causal structures could be composed into higher‑dimensional geometric objects.

**[6]** integrates out the interior of a spinor field theory on the Bruhat‑Tits tree and obtains a boundary theory that closely resembles a scalar field theory over $\mathbb{Q}_{p}$. This provides a concrete mechanism by which bulk tree degrees of freedom give rise to a $p$‑adic continuum limit.

**[7]** computes effective actions on two subspaces of the Bruhat‑Tits tree and shows that, as the subspaces approach the boundary, the resulting theories converge to the same $p$‑adic conformal field theory. This reinforces the robustness of the tree‑to‑boundary limit.

**[8]** derives a $p$‑adic van Lint‑Seidel bound for equiangular lines, demonstrating that $p$‑adic magnitude arithmetic supports packing constraints analogous to Archimedean geometry. Such bounds would constrain the number of distinguishable branch directions at a given depth in a tree‑time model.

## 3. Methods

### 3.1 Definitions

**Definition 3.1 (Event).** An *event* is a vertex $v$ of the Bruhat‑Tits tree $\mathcal{T}_{p}$, a $(p\!+\!1)$‑regular rooted tree with distinguished root $v_{0}$.

**Definition 3.2 (Time).** The *time* of an event $v$ is its depth $d(v)\in\mathbb{N}$, i.e. the number of edges on the unique path from $v_{0}$ to $v$. We identify $d(v)$ with the $p$‑adic valuation $v_{p}(x)$ of a putative coordinate $x$, and we set $t(v)=d(v)\,t_{0}$ with fundamental tick $t_{0}$.

**Definition 3.3 (Temporal order).** For events $A,B$, we write $A\prec B$ iff $A$ lies on the unique path from $B$ to the root (proper ancestor). If neither $A\prec B$ nor $B\prec A$, we write $A\parallel B$ (incomparable).

**Definition 3.4 (Tree‑geodesic causality).** $A$ causes $B$ iff $A\prec B$. Causality coincides with ancestry.

**Definition 3.5 (Tree distance).** The graph distance $\delta(A,B)$ equals the number of edges on the unique path between $A$ and $B$; with least common ancestor $w$ at depth $d_{w}$,
$$\delta(A,B)=d(A)+d(B)-2d_{w}.$$

### 3.2 Method of analysis

All results are obtained by exact combinatorial enumeration on the rooted $(p\!+\!1)$‑regular tree. Induction on depth and direct summation of geometric series are used. No simulation is performed. The only free parameters are the prime $p$ and the depth cutoff $D$ used for finite‑horizon calculations. Continuum‑recovery statements are labeled as explicit projections (Section 4.9).

## 4. Analysis

Every input number below is either a structural constant of the model (the regularity $p\!+\!1$) or an explicit modeling choice ($D$). All arithmetic is shown.

### 4.1 Vertex counts by depth

**Claim 4.1.** The number of vertices at depth $d$ is
$$
N_{d}=(p+1)\,p^{\,d-1}\quad\text{for }d\ge 1,\qquad N_{0}=1.
$$

*Derivation.* The root $v_{0}$ has $p+1$ neighbours, so $N_{1}=p+1$. Each vertex at depth $d-1$ has $p$ children (all neighbours except its parent), giving $N_{d}=p\,N_{d-1}$. Solving the recurrence yields the formula. $\blacksquare$

*Worked instance ($p=2$).* $N_{1}=3$, $N_{2}=6$, $N_{3}=12$, $N_{4}=24$, $N_{5}=48$, $N_{6}=96$, $N_{7}=192$, $N_{8}=384$, $N_{9}=768$, $N_{10}=1536$.

### 4.2 Total vertices up to depth $D$

**Claim 4.2.** The total number of vertices with $d(v)\le D$ is
$$
V_{D}=1+\sum_{d=1}^{D}(p+1)p^{\,d-1}
=1+(p+1)\,\frac{p^{D}-1}{p-1}.
$$

*Derivation.* Sum the geometric series $\sum_{d=1}^{D}p^{\,d-1}=\frac{p^{D}-1}{p-1}$, multiply by $p+1$, and add the root. $\blacksquare$

*Worked instance ($p=2$, $D=10$).*
$$
V_{10}=1+3\,(2^{10}-1)=1+3\cdot1023=3070.
$$
Direct summation of the $N_{d}$ from Section 4.1 reproduces $3070$. ✓

### 4.3 Comparable pairs

**Claim 4.3.** For depths $d_{1}<d_{2}$, the number of unordered comparable pairs $\{A,B\}$ with $d(A)=d_{1}$, $d(B)=d_{2}$ equals $N_{d_{2}}$, independent of $d_{1}$.

*Derivation.* Each vertex at depth $d_{1}$ has exactly $p^{\,d_{2}-d_{1}}$ descendants at depth $d_{2}$. Hence
$$
N_{d_{1}}\cdot p^{\,d_{2}-d_{1}}=(p+1)p^{\,d_{1}-1}\,p^{\,d_{2}-d_{1}}=(p+1)p^{\,d_{2}-1}=N_{d_{2}}.
$$
$\blacksquare$

### 4.4 Total comparable pairs up to depth $D$

**Claim 4.4.** The total number of unordered comparable pairs among vertices of depth $\le D$ is
$$
C_{D}=\sum_{d=1}^{D}d\,N_{d}=(p+1)\sum_{d=1}^{D}d\,p^{\,d-1}.
$$

*Derivation.* A vertex at depth $d$ has exactly $d$ proper ancestors, contributing $d$ comparable pairs as the deeper member. Summing over all vertices yields the claim. $\blacksquare$

*Closed form for $p=2$.* Let $S_{D}=\sum_{d=1}^{D}d\,2^{\,d-1}$. Induction shows $S_{D}=(D-1)2^{D}+1$. Therefore
$$
C_{10}=3\,S_{10}=3\bigl(9\cdot2^{10}+1\bigr)=3\cdot9217=27651.
$$

### 4.5 Fraction of comparable pairs

**Claim 4.5.** For $p=2$, $D=10$,
$$
f_{10}=\frac{C_{10}}{\binom{V_{10}}{2}}.
$$

*Derivation.* $\binom{3070}{2}= \frac{3070\cdot3069}{2}=4\,710\,915$. Hence
$$
f_{10}= \frac{27651}{4\,710\,915}\approx5.8696\times10^{-3}.
$$
Asymptotically, with fixed $p$,
$$
f_{D}\sim\frac{D}{p^{D}}\to0,
$$
so ordered pairs become exponentially rare. $\blacksquare$

### 4.6 Mean depth

Under the uniform distribution on the depth‑$D$ ball,
$$
\bar d=\frac{C_{D}}{V_{D}}.
$$
For $p=2$, $D=10$,
$$
\bar d=\frac{27651}{3070}\approx9.0068,
$$
i.e. the average depth lies within $9.9\%$ of the maximal depth $D$.

### 4.7 Acyclicity of tree‑geodesic causality

**Claim 4.6.** The causality relation of Definition 3.4 admits no causal cycles.

*Derivation.* Suppose a closed chain $A_{1}\to A_{2}\to\cdots\to A_{k}\to A_{1}$ with $A_{i+1}\prec A_{i}$ for each $i$. Depth strictly decreases along the chain, yielding $d(A_{1})>d(A_{2})>\cdots>d(A_{k})>d(A_{1})$, an impossibility for integers. Hence no cycle exists. $\blacksquare$

### 4.8 Future‑cone size

**Claim 4.7.** The number of descendants of an event $u$ within $\Delta$ additional ticks is
$$
C(\Delta)=\sum_{k=1}^{\Delta}p^{\,k}= \frac{p^{\Delta+1}-p}{p-1}.
$$

*Worked instances.* For $p=2$, $\Delta=5$,
$$
C(5)=2+4+8+16+32=62,
$$
matching the closed form $(2^{6}-2)/(2-1)=62$.  
For $p=3$, $\Delta=5$,
$$
C(5)=3+9+27+81+243=363,
$$
matching $(3^{6}-3)/2=363$. $\blacksquare$

### 4.9 Continuum limit (labeled projection)

**Projection P1.** Assume (i) observable durations $T$ correspond to depth $D=T/t_{0}$, and (ii) the number of distinguishable events at resolution $t_{0}$ in an interval $T$ is $V_{D}$. Then
$$
V_{D}\approx\frac{p+1}{p-1}\,p^{\,T/t_{0}},
$$
i.e. exponential growth in $T/t_{0}$. Matching this to continuum‑like polynomial scaling would require either a varying $t_{0}$ or that observable quantities live on the tree boundary, as suggested by the bulk‑to‑boundary mechanisms of [6] and [7].

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are measured or simulated.

*R1 (Vertex growth).* $N_{d}=(p+1)p^{\,d-1}$ (Claim 4.1). For $p=2$: $N_{1}=3$, $N_{10}=1536$.

*R2 (Event budget).* $V_{10}=3070$ (Claim 4.2), verified by two independent summations.

*R3 (Comparability scarcity).* $C_{10}=27651$ ordered pairs out of $\binom{3070}{2}=4\,710\,915$ total pairs; $f_{10}\approx5.8696\times10^{-3}$ (Claims 4.4–4.5). Asymptotically $f_{D}\sim D/p^{D}\to0$.

*R4 (Depth‑independence).* Ordered pairs between depths $d_{1}<d_{2}$ equal $N_{d_{2}}$, independent of $d_{1}$ (Claim 4.3).

*R5 (Temporal statistics).* Mean depth $\bar d\approx9.0068$; depth histogram follows $N_{d}=(p+1)p^{\,d-1}$.

*R6 (No causal cycles).* Tree‑geodesic causality is a strict partial order; cycles are impossible (Claim 4.6).

*R7 (Future‑cone counts).* $C(\Delta)=\frac{p^{\Delta+1}-p}{p-1}$; for $p=2$, $\Delta=5$: $62$; for $p=3$, $\Delta=5$: $363$ (Claim 4.7).

*Projection P1.* Under assumptions (i)–(ii) of Section 4.9, event count scales exponentially with physical duration; recovery of continuum statistics remains a hypothesis.

*Projection P2.* If one depth step equals one Planck time, a horizon of $D$ steps spans $D$ Planck times. This conversion is an explicit assumption, not derived from the model.

## 6. Discussion

**Limitations.** The model provides only a kinematic skeleton: it specifies ordering and counting but supplies no dynamics. The identification $t\leftrightarrow v_{p}(x)$ is a conjecture; the root’s association with the Planck scale and the choice of prime $p$ are unfixed assumptions. The only hint that a specific prime might be distinguished comes from the Potts‑model phase transition at $p=3$ ([3]), which concerns statistical mechanics on a Cayley tree rather than temporal ordering. Spatial degrees of freedom are absent, so the relativistic light‑cone structure is not reproduced; the future‑cone growth $C(\Delta)\sim p^{\Delta}$ differs from the quadratic growth of a $1\!+\!1$‑dimensional light cone.

**Failure modes.**  
1. Observation of a closed causal loop would contradict Claim 4.6.  
2. Empirical evidence of a total temporal order for events that are incomparable under Definition 3.3 would falsify the partial‑order claim.  
3. Detection of resolvable intervals finer than a single tick $t_{0}$ would refute the quantization result.  
4. A measured depth histogram that is not exponential would falsify the uniform‑on‑ball assumption.  
5. Empirical quadratic future‑cone growth would contradict Claim 4.7.  
6. If observations singled out a specific prime $p$ and excluded the counts for other $p$, the model would be constrained or falsified.

**Limitations list.**  
- *Root‑scale identification* (Projection P2): sensitivity to the assumed Planck‑scale mapping.  
- *Prime choice*: results depend on $p$; no physical principle selects $p$.  
- *Absence of spatial structure*: prevents recovery of relativistic causal cones.  
- *Static kinematics*: no dynamics or field equations are provided.  
- *Continuum‑recovery projection* (P1): relies on unproven boundary‑theory mechanisms.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.** The primary users are theoretical physicists developing quantum‑gravity or non‑Archimedean models of spacetime. If the tree‑depth hypothesis holds, model builders can replace continuous time variables with integer depth indices, guaranteeing discreteness, partial order, and acyclic causality by construction. This changes the design of canonical quantization schemes, path‑integral discretizations, and causal‑set constructions.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 1–2. Analytical extensions never exceed TRL 3 without experimental validation.

**(c) Minimal next test.** The smallest de‑risking experiment is a numerical simulation of a simple dynamical process (e.g., a discrete random walk) on a finite depth‑$D$ Bruhat‑Tits tree. One would measure the distribution of ancestor‑descendant pairs and compare the observed comparable‑pair fraction to the predicted $f_{D}=C_{D}/\binom{V_{D}}{2}$. A statistically significant deviation (e.g., measured $f_{D}$ exceeding $10^{-2}$ for $p=2$, $D=10$) would falsify the combinatorial prediction.

**(d) Engineering constraints.** The only constraints stem from the combinatorial structure itself: (i) the regularity $p\!+\!1$ fixes branching; (ii) depth $D$ determines the size of the finite computational domain; (iii) no material, energy, or fabrication issues arise because the model is abstract. If spatial extensions are added, one must respect the transfer‑map constructions of [5] and the bulk‑to‑boundary limits of [6, 7].

**(e) Projected cost/performance bounds.** No monetary cost is required for the analytical work. For the minimal simulation described in (c), the computational cost scales as $O(V_{D})$, i.e. $O(p^{D})$ operations; for $p=2$, $D=10$ this is on the order of a few thousand elementary steps, easily performed on a standard laptop.

**(f) Risks and misuse.** A potential misuse is the unwarranted replacement of all continuous‑time physics with the tree model without checking empirical falsification criteria, leading to incorrect predictions in regimes where the model’s assumptions (e.g., absence of spatial structure) are violated.

## 8. Conclusion

We have formalized a conjectural model in which physical time is the integer depth $d(v)$ of a vertex in a rooted $(p\!+\!1)$‑regular Bruhat‑Tits tree, identified with the $p$‑adic valuation $v_{p}(x)$. The model yields three theorems: discreteness of time (integer ticks), partial temporal ordering (ancestry on the tree), and acyclicity of causality (no closed causal loops). Exact combinatorial consequences—vertex growth, comparable‑pair scarcity, mean depth, and future‑cone counts—are derived with full arithmetic and require no simulation. The central weakness is the mismatch between the tree’s linear ancestor chain and the relativistic light cone; however, bulk‑to‑boundary mechanisms in [6] and [7] suggest a possible route to a $p$‑adic continuum limit. The prime $p$ and the root‑scale identification remain free parameters, and the model’s predictions are explicitly falsifiable by simple combinatorial measurements. By providing a rigorously solvable skeleton, the work offers a concrete platform for future investigations into non‑Archimedean temporal substrates.

## References

[1] arXiv:1712.01463v2 | On the missing branches of the Bruhat‑Tits tree  
[2] arXiv:2102.12024v2 | Bending the Bruhat‑Tits Tree II: the p‑adic BTZ Black hole and Local Diffeomorphism on the Bruhat‑Tits Tree  
[3] arXiv:math-ph/0512018v2 | On Phase Transitions for $P$‑Adic Potts Model with Competing Interactions on a Cayley Tree  
[4] arXiv:0809.1570v1 | Mumford dendrograms and discrete p‑adic symmetries  
[5] arXiv:1301.5453v1 | On $p$‑adic colligations and 'rational maps' of Bruhat‑Tits trees  
[6] arXiv:1910.09397v2 | The boundary theory of a spinor field theory on the Bruhat‑Tits tree  
[7] arXiv:2402.03730v2 | Effective field theories on subspaces of the Bruhat‑Tits tree  
[8] arXiv:2408.00810v3 | p‑adic Equiangular Lines and p‑adic van Lint‑Seidel Relative Bound  

## Appendix A. Divergence report

No unresolved divergences between independent drafts were recorded; all quantitative claims trace to single derivations, and no conflicting values required adjudication.

## Appendix B. Claim attribution

| Claim | Substance | Source | Status |
|---|---|---|---|
| C1 | $N_{d}=(p+1)p^{\,d-1}$; $V_{10}=3070$ for $p=2$, $D=10$ | Claims 4.1–4.2 | SINGLE, verified by two summations |
| C2 | $C_{10}=27651$; $f_{10}\approx5.87\times10^{-3}$; $f_{D}\sim D/p^{D}\to0$ | Claims 4.3–4.5 | SINGLE |
| C3 | $\bar d=27651/3070\approx9.007$; gap $\approx9.93\%$ | Claim 4.6 (corrected) | SINGLE |
| C4 | No causal cycles (Claim 4.6 / R6) | Strict‑decrease derivation | SINGLE |
| C5 | $C(\Delta)=\frac{p^{\Delta+1}-p}{p-1}$; $62$ ($p=2$), $363$ ($p=3$) at $\Delta=5$ | Claim 4.7 | SINGLE |
| C6 | Projections P1–P2 (continuum recovery, Planck‑scale root) | Section 4.9 / R, labeled as assumptions | SINGLE, explicitly hypothetical |