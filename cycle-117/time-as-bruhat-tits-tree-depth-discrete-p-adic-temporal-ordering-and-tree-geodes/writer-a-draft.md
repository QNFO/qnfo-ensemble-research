# Time as Bruhat‑Tits Tree Depth: A Discrete Non‑Archimedean Model of Physical Time

## Abstract
We propose a novel representation of physical time as the depth index $d\in\mathbb{N}$ of a Bruhat‑Tits (BT) tree, identified with the $p$‑adic valuation $v_{p}(x)$. In this model the Planck‑scale quantum of time corresponds to the tree root, while causal ordering follows the unique geodesic from any event to the root. The resulting temporal structure is ultrametric, partially ordered, and combinatorial. To assess viability we (i) translate the depth index into a discrete time unit $\tau_{0}$, (ii) compute elementary combinatorial quantities (number of nodes and root‑to‑leaf paths) for a regular BT tree of branching factor $b=p+1$, and (iii) compare these discrete structures with known BT‑tree applications in $p$‑adic physics. Explicit arithmetic yields $N_{\text{nodes}}(d=5,p=2)=364$ and $N_{\text{paths}}(d=5,p=2)=243$. These results illustrate how a simple discrete depth can generate a rich causal lattice. We discuss how the model reproduces light‑cone‑like causal cones in a continuum limit, avoids closed timelike curves, and aligns with existing $p$‑adic constructions of field theories on BT trees. Limitations and open directions for embedding dynamics and observational tests are outlined.

## 1. Introduction
The conventional description of time in physics treats it as a continuous real parameter, a viewpoint that underlies both Newtonian mechanics and relativistic spacetime. Yet several approaches to quantum gravity suggest that continuity may break down at the Planck scale, prompting the search for discrete or non‑Archimedean temporal structures. The Bruhat‑Tits tree, a regular infinite graph associated with the $p$‑adic field $\mathbb{Q}_{p}$, provides a natural ultrametric geometry in which each vertex carries a depth $d$ measured from a distinguished root. The depth coincides with the $p$‑adic valuation $v_{p}(x)$ of a coordinate $x$, suggesting a direct identification of $d$ with a discrete time index.

In this work we formulate the hypothesis that physical time is precisely the BT‑tree depth, thereby replacing the real line $\mathbb{R}$ with the discrete set $\mathbb{N}$. Causality is defined combinatorially: an event $A$ can influence $B$ iff $B$ lies on the unique geodesic from $A$ to the root. This definition yields a partial order, because events on distinct branches are incomparable. The proposal has three immediate consequences:

1. **Quantization** – the smallest non‑zero interval of time is a single depth step, denoted $\tau_{0}$.
2. **Partial ordering** – events on different branches have no intrinsic temporal relation.
3. **Tree‑geodesic causality** – causal influence follows the unique path toward the root.

We explore these consequences through elementary combinatorial analysis and by situating the model within the broader $p$‑adic physics literature.

## 2. Background and Related Work
The Bruhat‑Tits tree has appeared in a variety of mathematical and physical contexts, many of which provide tools or analogies useful for a discrete temporal model.

* **[1]** investigates *branches* of the BT tree that arise as sub‑trees representing maximal orders in a matrix algebra over a local field. The notion of a *branch* as a distinguished sub‑tree directly informs our interpretation of a causal “worldline” as a path within a branch.

* **[2]** constructs a $p$‑adic analogue of the BTZ black hole on the BT tree, introducing a novel $p$‑adic exponential function. The transplantation of a geometric object onto the BT tree demonstrates that non‑trivial spacetime‑like structures can be encoded combinatorially, supporting our view that causal geometry may be realized on the tree.

* **[3]** studies a three‑state $p$‑adic Potts model on a Cayley tree of order two, reducing Gibbs‑measure analysis to a recursive equation. The use of recursive dynamics on a tree mirrors the way temporal evolution could be expressed as depth‑wise recursion in our model.

* **[4]** presents an encoding of dendrograms into BT trees associated with $p$‑adic number fields, showing that strings over a finite alphabet can be embedded via cyclotomic extensions of $\mathbb{Q}_{p}$. This demonstrates that discrete data (e.g., events) can be systematically placed on BT‑tree vertices.

* **[5]** defines *rational maps* from BT trees to Bruhat‑Tits buildings via transfer functions derived from conjugacy classes of $p$‑adic matrices. Such maps provide a formalism for transporting physical quantities defined on the tree to higher‑dimensional structures, a potential route for linking our discrete time to conventional spacetime.

* **[6]** calculates the action and partition function of a spinor field theory on the BT tree, finding a boundary theory analogous to a scalar field over $p$‑adic numbers. This indicates that field‑theoretic dynamics can be consistently formulated on the tree, a prerequisite for any physical theory based on BT‑tree time.

* **[7]** derives effective field theories on subspaces of the BT tree and shows that their limits coincide with conformal field theories over $p$‑adic numbers when the subspaces approach the tree boundary. This continuum‑limit behavior suggests a pathway for recovering familiar relativistic physics from the discrete model.

* **[8]** introduces $p$‑adic equiangular lines and establishes the inequality $|n|^{2}\le |d|\max\{|n|,\gamma^{2}\}$ relating the number of lines $n$, dimension $d$, and common angle parameter $\gamma$. Although the work focuses on linear algebra, the inequality provides a bound on the number of distinct causal directions that can be represented at a given depth, informing our combinatorial estimates.

The remaining entries ([9]–[12]) are internal QNFO manuscripts that discuss emergent spacetime, unifying geometric objects, invariant patterns, and epistemic conceptions of time. While their summaries are brief, they collectively motivate a reformulation of fundamental physics in terms of invariant structures such as the BT tree.

## 3. Methods
Our analysis proceeds in three stages:

1. **Discrete time unit definition.** We set a fundamental time quantum $\tau_{0}$ corresponding to a single depth increment $d\to d+1$ on the BT tree. All temporal intervals are integer multiples $t = d\,\tau_{0}$.

2. **Combinatorial enumeration.** For a regular BT tree with branching factor $b = p+1$, we compute:
   - The total number of vertices up to depth $d$, $N_{\text{nodes}}(d)$.
   - The number of distinct root‑to‑leaf paths of length $d$, $N_{\text{paths}}(d)$.
   These quantities are derived using elementary geometric series.

3. **Causal cone approximation.** We compare the set of vertices reachable within $k$ depth steps from a given vertex to the light‑cone structure of Minkowski spacetime, using the ultrametric property of the tree to argue for a “cone” that widens exponentially with depth.

All calculations are performed analytically; no numerical simulations are required for the present paper.

## 4. Analysis
### 4.1 Input parameters
- Branching factor: $b = p+1$. We choose $p=2$ for illustration, giving $b=3$.
- Depth of interest: $d = 5$ (five discrete time steps).

These choices are arbitrary but allow concrete arithmetic.

### 4.2 Number of vertices up to depth $d$
A regular tree with branching factor $b$ has $b^{k}$ vertices at exact depth $k$ (the root is at $k=0$). The cumulative number of vertices from the root to depth $d$ inclusive is the finite geometric series:

\[
N_{\text{nodes}}(d)=\sum_{k=0}^{d} b^{k}
= \frac{b^{d+1}-1}{b-1}.
\]

**Step‑by‑step computation for $b=3$, $d=5$:**

1. Compute $b^{d+1}=3^{6}$.
   \[
   3^{2}=9,\; 3^{3}=27,\; 3^{4}=81,\; 3^{5}=243,\; 3^{6}=729.
   \]
2. Subtract 1: $729-1=728$.
3. Divide by $b-1=3-1=2$: $728/2=364$.

Thus,
\[
N_{\text{nodes}}(5)=364.
\]

### 4.3 Number of root‑to‑leaf paths of length $d$
Each path of length $d$ corresponds to a choice of one of the $b$ outgoing edges at each of the $d$ steps, giving

\[
N_{\text{paths}}(d)=b^{d}.
\]

**Step‑by‑step computation for $b=3$, $d=5$:**

\[
3^{5}=243.
\]

Hence,
\[
N_{\text{paths}}(5)=243.
\]

### 4.4 Causal cone size
Given a vertex at depth $d_{0}$, the set of vertices that can be causally influenced within $k$ additional depth steps consists of all descendants up to depth $d_{0}+k$. Its size is therefore $N_{\text{nodes}}(k)$ as computed above, demonstrating an exponential growth analogous to the widening of a light cone.

### 4.5 Consistency with inequality from [8]
Inequality (1) from [8] reads $|n|^{2}\le |d|\max\{|n|,\gamma^{2}\}$. Interpreting $|n|$ as the number of distinct causal directions (here $N_{\text{paths}}$) and $|d|$ as the depth $d$, we can test the bound for $\gamma=1$ (a neutral choice). Substituting $|n|=243$, $|d|=5$:

\[
\max\{|n|,\gamma^{2}\} = \max\{243,1\}=243,
\]
\[
|d|\max\{\dots\}=5\times 243 = 1215,
\]
\[
|n|^{2}=243^{2}=59049.
\]

Since $59049 > 1215$, the inequality is violated for $\gamma=1$, indicating that $\gamma$ must be larger to accommodate the combinatorial explosion of directions. Solving for the minimal $\gamma$ that satisfies the inequality:

\[
|n|^{2}\le |d|\max\{|n|,\gamma^{2}\}\;\Rightarrow\;
59049 \le 5\max\{243,\gamma^{2}\}.
\]

If $\gamma^{2}\ge 243$, then $\max\{243,\gamma^{2}\}=\gamma^{2}$ and we require

\[
59049 \le 5\gamma^{2}\;\Rightarrow\;\gamma^{2}\ge \frac{59049}{5}=11809.8.
\]

Thus $\gamma\ge \sqrt{11809.8}\approx108.7$. This simple calculation illustrates how the inequality constrains the admissible angular parameter for a given depth and branching factor.

## 5. Results
- The total number of BT‑tree vertices up to depth $d=5$ with $p=2$ is **$364$**.
- The number of distinct root‑to‑leaf causal paths of length $5$ is **$243$**.
- The causal cone of a vertex expands exponentially, matching the combinatorial growth $N_{\text{nodes}}(k)=\frac{3^{k+1}-1}{2}$ for $k$ additional depth steps.
- Applying the inequality from [8] shows that a naïve angular parameter $\gamma=1$ cannot bound the $243$ directions at depth $5$; a much larger $\gamma\approx109$ is required, highlighting a tension between ultrametric branching and angular constraints.

These concrete figures demonstrate that a simple depth‑based time model yields a richly structured causal lattice, with quantitative properties that can be directly compared to existing $p$‑adic constructions.

## 6. Discussion
### 6.1 Limitations
- **Choice of $p$ and depth.** Our numerical examples fix $p=2$ and $d=5$ for tractability; different primes or deeper trees change the combinatorics dramatically. The model’s predictions therefore depend sensitively on the underlying $p$‑adic field.
- **Absence of dynamics.** We have enumerated static combinatorial quantities but have not specified dynamical laws (e.g., evolution of fields) on the tree. Incorporating the field‑theoretic results of [6] and [7] would be necessary for a complete physical theory.
- **Inequality tension.** The violation of the bound from [8] for $\gamma=1$ suggests that the simple identification of causal directions with tree paths may be too naive, or that additional geometric constraints (e.g., embedding into a building) are required.
- **Partial ordering vs. observed total order.** Empirically, macroscopic time appears totally ordered. Our model yields a partial order; reconciling the two would require a mechanism (e.g., coarse‑graining) that collapses incomparable branches at larger scales.

### 6.2 Potential falsifiers
- **Closed timelike curves.** If the tree‑geodesic causality allowed a loop (i.e., a vertex reachable from itself via a non‑trivial path), the model would be falsified. The tree’s acyclic nature precludes such loops, but any extension that introduces shortcuts must be examined.
- **Experimental signatures of discreteness.** Detectable deviations from continuous time at high‑energy experiments would support the model; their absence at scales far above the Planck regime would not falsify it, as the discreteness may be hidden.
- **Violation of inequality (1).** Empirical constraints on the number of independent causal directions at a given resolution could test the bound derived from [8].

### 6.3 Open questions
- How does one embed the discrete BT‑tree time into a Lorentzian manifold to recover special relativity in the continuum limit?
- Can the transfer‑function formalism of [5] be used to map BT‑tree observables to conventional spacetime fields?
- What is the role of the novel $p$‑adic exponential function introduced in [2] for defining temporal evolution operators?
- How does the ultrametric causal structure interact with thermodynamic arrow‑of‑time considerations discussed in the QNFO manuscripts ([9]–[12])?

## 7. Conclusion
We have articulated a concrete proposal that physical time corresponds to the depth of a Bruhat‑Tits tree, yielding a discrete, ultrametric, and partially ordered temporal framework. Elementary combinatorial analysis provides explicit numerical predictions for the size of causal neighborhoods and the number of distinct causal paths. While the model aligns with several strands of $p$‑adic physics—branch structures, field theories on trees, and rational maps—it also raises challenges, notably the need to reconcile partial ordering with observed total ordering and to satisfy geometric bounds such as those of [8]. Future work will focus on dynamical formulations, continuum limits, and potential phenomenological signatures.

## References
[1] arXiv:1712.01463v2 | On the missing branches of the Bruhat‑Tits tree  
[2] arXiv:2102.12024v2 | Bending the Bruhat‑Tits Tree II: the p‑adic BTZ Black hole and Local Diffeomorphism on the Bruhat‑Tits Tree  
[3] arXiv:math‑ph/0512018v2 | On Phase Transitions for $P$‑Adic Potts Model with Competing Interactions on a Cayley Tree  
[4] arXiv:0809.1570v1 | Mumford dendrograms and discrete p‑adic symmetries  
[5] arXiv:1301.5453v1 | On $p$‑adic colligations and 'rational maps' of Bruhat‑Tits trees  
[6] arXiv:1910.09397v2 | The boundary theory of a spinor field theory on the Bruhat‑Tits tree  
[7] arXiv:2402.03730v2 | Effective field theories on subspaces of the Bruhat‑Tits tree  
[8] arXiv:2408.00810v3 | p‑adic Equiangular Lines and p‑adic van Lint‑Seidel Relative Bound  
[9] QNFO: Formal Derivation of Emergent Spacetime to the Bruhat‑Tits Tree  
[10] QNFO: Bruhat‑Tits Tree as a Unifying Geometric Object  
[11] QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics  
[12] QNFO: Time as Epistemic Cognitive Fiction  

## Appendix A. Divergence report
No divergent claims arose among the drafts because this is the sole writer version.

## Appendix B. Claim attribution
| ID | Claim | Source | Agreement |
|----|-------|--------|-----------|
| C1 | Time is identified with BT‑tree depth $d\in\mathbb{N}$ | This draft | Single |
| C2 | Fundamental time quantum $\tau_{0}$ corresponds to one depth step | This draft | Single |
| C3 | Branching factor $b=p+1$ for a regular BT tree | This draft | Single |
| C4 | $N_{\text{nodes}}(d)=\frac{b^{d+1}-1}{b-1}$ | This draft | Single |
| C5 | For $p=2$, $d=5$, $N_{\text{nodes}}=364$ | This draft | Single |
| C6 | $N_{\text{paths}}(d)=b^{d}$ | This draft | Single |
| C7 | For $p=2$, $d=5$, $N_{\text{paths}}=243$ | This draft | Single |
| C8 | Inequality (1) from [8] imposes $\gamma\ge108.7$ for $d=5$, $p=2$ | This draft | Single |
| C9 | Causal cone size grows as $N_{\text{nodes}}(k)$ | This draft | Single |
| C10 | Partial ordering arises because branches are incomparable | This draft | Single |
| C11 | No closed timelike curves exist on an acyclic tree | This draft | Single |
| C12 | References [1]–[8] provide relevant BT‑tree constructions | This draft | Single |