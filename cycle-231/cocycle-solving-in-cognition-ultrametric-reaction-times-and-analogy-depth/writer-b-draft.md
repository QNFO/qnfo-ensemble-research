# Cocycle Solving on Associative Webs: Ultrametric Reaction Times and a Cross-Ratio Measure of Analogy Depth

## Abstract

Belief maintenance in human cognition is usually modeled as constraint relaxation over associative networks with Euclidean or graph-theoretic geometry, leaving unexplained how locally inconsistent updates are resolved into globally coherent belief states. This paper develops the hypothesis, introduced in recent quantitative work on cognitive architecture, that the brain maintains beliefs by enforcing a cocycle (flatness) condition over an associative web, so that semantic distance is ultrametric rather than Euclidean. We formalize the claim in three parts. First, we derive reaction-time predictions from an ultrametric semantic tree: with a stated set of parameters, retrieval between concepts whose least common ancestor sits $k$ levels up the tree is predicted to take $300 + 50k$ milliseconds, giving 350 ms for adjacent categories and 800 ms for maximally separated ones. Second, we show that a cocycle constraint on edge weights admits exactly two local resolution modes, node rejection and global rewarping, with computed violation magnitudes (for example $7/32 \approx 0.219$ on a three-node triangle), and we map these onto the two classical dissonance-reduction behaviors. Third, we define analogy difficulty as the logarithmic depth of the projective cross-ratio relating two domains, and compute a worked prediction of a 40.6 ms difficulty difference between two analogy items. The framework converts cognitive dissonance and belief revision into topological constraint satisfaction and yields falsifiable, quantitative reaction-time and difficulty predictions testable against semantic priming and analogy data.

## 1. Introduction

Clinical psychologists, cognitive modelers, and designers of belief-revision systems all face the same operational problem: a person or an artificial agent holds a web of beliefs, receives a locally inconsistent input, and must resolve the inconsistency quickly, and current models cannot predict how long the resolution will take or which resolution mode will be chosen. In cognitive psychology, semantic priming experiments measure reaction times (RTs) to related and unrelated word pairs, and analogy tasks such as $A{:}B{::}C{:}D$ measure solution latency and error rate; the field lacks a first-principles function that maps the hierarchical relation between stimulus concepts to a predicted latency. In belief-revision engineering, the same structure appears as an inconsistency-handling problem: when a new fact contradicts stored facts, a system must choose between discarding the new fact and restructuring a large part of the knowledge base, and the cost of each choice is rarely quantified in advance. What is missing on both sides is a hard geometric foundation: a condition that, when enforced, makes global consistency automatic and makes difficulty computable from structure alone.

The cost of this gap is concrete. Without a structural difficulty measure, analogy items for assessments and experiments are selected by intuition; without a principled account of the two dissonance-reduction modes, models of attitude change cannot predict whether a person will reject a message or reorganize their belief system. If the result of this paper holds, a designer of an analogy test could compute item difficulty from the hierarchical depth of the item's concepts before any pilot data are collected, and a modeler of belief revision could predict the resolution mode from the magnitude of a single scalar violation.

The starting point is a hypothesis stated in recent quantitative work on cognitive architecture: the brain functions as a macroscopic algebraic solver of the cocycle condition, maintaining global topological consistency across a hierarchical (Bruhat-Tits-type) tree, and simulated neural replicas built on this principle show non-trivial ultrametric clustering, with statistical tests that decisively rejected a Euclidean baseline ($p < 0.001$) and retrieval dynamics that produce power-law retrieval times mirroring p-adic diffusion [9]. This paper takes that hypothesis seriously as a quantitative commitment and works out its measurable consequences. The mathematical setting is the ultrametric, a distance $d$ satisfying the strong triangle inequality $d(x,y) \leq d(x,z) \lor d(z,y)$, where $\lor$ is the maximum operator [1]; ultrametric distances arise naturally on the leaves of rooted trees [8] and have been used to model mental processes, where "mental topology is ultrametric" [6], to model anomaly and change in data by induced ultrametric hierarchies [5], and to model contagion-like spread with infection probability proportional to $1/d(x,y)$ [7].

The contributions of this paper are:

1. A reaction-time law for ultrametric semantic retrieval, $\mathrm{RT}(k) = \tau_0 + \tau_1 k$ in the tree-depth difference $k$ between concepts, with fully worked numerical predictions (350 ms to 800 ms under stated parameters), derived in Section 4 and reported in Section 5.
2. A proof-style demonstration that a cocycle (flatness) constraint on an associative web admits exactly two local resolution modes, node rejection and global rewarping, with computed violation magnitudes, derived in Section 4 and mapped to dissonance-reduction behavior in Section 5.
3. A definition of analogy depth as the logarithmic depth of the projective cross-ratio of four concept coordinates, with a worked prediction of a 40.6 ms difficulty difference between two analogy items, derived in Section 4 and reported in Section 5.
4. A falsification analysis stating which empirical observation would refute each result, given in Section 6.

## 2. Background and Related Work

The strong triangle inequality defines an ultrametric: a metric $d$ on a set $X$ with $d(x,y) \leq d(x,z) \lor d(z,y)$ for all $x,y,z$ [1]. Muranov's paper proves ultrametric versions of three classical theorems: the Arens-Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki-Tychonoff characterization of compactness, using free modules over commutative rings and a $0$-dimensional Michael continuous selection theorem in place of the paracompact selection theorem [1]. For this paper, the embedding and extension results matter because they guarantee that ultrametric semantic spaces are not exotic: an ultrametric on a concept set can be embedded, extended, and characterized with the same generality as an ordinary metric, so the cognitive model inherits a complete metric toolkit.

Ultrametric spaces have a canonical combinatorial representation. The comb construction assigns to a function $f : I \to [0,\infty)$ on a compact interval the distance $\bar{d}_f(s,t) = \sup_{(s \wedge t, s \vee t)} f$, which is ultrametric on $\{f = 0\}$, and Theorem 3.1 of that work establishes that every compact ultrametric space with a suitable measure is globally isometric to such a comb metric space, with the measure carried to Lebesgue measure [8]. This isometry is the technical bridge for Section 3: it lets us treat a semantic hierarchy either as a rooted tree or as a one-dimensional coordinate system, and the one-dimensional picture is what makes a projective cross-ratio well-defined for analogy items.

Ultrametric Cantor sets supply the scale-invariant machinery. Raut and Datta study a family of Cantor sets endowed with a scale-invariant ultrametric built from "relative infinitesimals" and an inversion rule, and prove that the associated valuation is given by an appropriate Cantor function, so that the valuation is both scale and reparametrisation invariant [4]. Their inversion rule, in which increments among infinitesimals are accomplished by inversions rather than translations, is the precedent for Section 4's treatment of belief updates as multiplicative (cocycle) operations rather than additive ones: a cocycle condition $g_{ij} g_{jk} = g_{ik}$ is exactly the statement that composition of updates follows the group law of the weights, not an additive accumulation.

On the modeling side, Murtagh shows how to move from data to an ultrametric model: correspondence analysis endows a cross-tabulation (for example, film-script scenes crossed by words) with a $\chi^2$ metric, the points are mapped to a Euclidean space, and a hierarchy associated with an ultrametric is induced on them, so that a scene quite different from immediately previous scenes is incorporated into the hierarchy at a high level and can be read off as a changepoint or anomaly [5]. This pipeline is directly reusable for the empirical half of the present program: given behavioral or text data from a person, the same correspondence-analysis-to-hierarchy pipeline can extract that person's ultrametric semantic tree, whose depths then feed the reaction-time law of Section 4.

The ultrametric model of mind has a history. Murtagh's review develops Ignacio Matte Blanco's principles of symmetric and asymmetric being through ultrametric topology, citing the position that "mental topology is ultrametric" (Anashin and Khrennikov) and noting Lauro-Grotto's observation that ultrametricity can "be used as a means to generate mental representations that hold in their inner structure all the contradictory aspects of experience and present a smooth surface allowing a kind of 'easy handling' by mental processes" [6]. The contradictory-aspects point anticipates this paper's dissonance analysis: an ultrametric ball structure holds opposed concepts at controlled distances, and the cocycle condition of Section 4 is the mechanism that keeps those distances mutually consistent.

Ultrametrics also support dynamical processes. An ultrametric SIR model of epidemic spread clusters individuals by average time of infectious contact, defines the ultrametric distance $d(x,y)$ as a ratio of observation time to a minimum boundary value of contact times within the minimal cluster, and makes the model assumption that the per-unit-time infection probability of a susceptible individual $x$ by an infected individual $y$ is proportional to $1/d(x,y)$ [7]. We adopt the same inverse-distance activation law for semantic priming in Section 4, with the interpretation that a prime activates a target with strength proportional to the inverse of their ultrametric semantic distance; the epidemic model's conclusion that changing the ultrametric structure changes the spread [7] has the direct cognitive analogue that rewarping the semantic tree changes retrieval dynamics, which is the rewarping resolution mode of Section 4.

On the neurobiological side, the cortico-centric view of cognition, in which the thalamus is a relay at the start of a feedforward hierarchy from V1 through V2, MT/IT, and prefrontal cortex, has been challenged by evidence that most afferents to thalamic relay nuclei (90-95%) are not from the sensory organs, and that the thalamus, lacking local excitatory connections, is optimized for capturing state information distributed across multiple cortical nodes during context-dependent task switching [2]. This matters for the implementation story of Section 7: a global consistency condition over a distributed web needs a node that reads state across many cortical areas and modulates them, which is precisely the cortico-thalamo-cortical loop role that the emerging paradigm assigns to the thalamus [2]. The present paper's cocycle solver is a computational abstraction of such a loop.

Finally, complexity measures for embodied perception provide the human-factors template for validating a structural difficulty measure. A recent framework categorizes visuospatial complexity attributes into quantitative, structural, dynamic, auditory, and interactive groups, applies the model to build a benchmark dataset for complexity-based scene analysis in human-centered autonomous driving and to design a VR driving study, and plans a human-subject study in which participants rank systematically parameterized stimuli so that computational complexity measures can be aligned with human perceptual experience [3]. Section 7 adopts the same validation pattern for analogy depth: parameterize analogy items by computed depth, collect human difficulty ratings, and align the two.

The immediate predecessor is the QNFO quantitative simulation work, which proposes that the brain functions as a macroscopic algebraic solver of the cocycle condition maintaining global topological consistency across a Bruhat-Tits tree, models the brain's state space as such a tree, and reports that simulated neural replicas exhibit non-trivial ultrametric clustering with triangle-inequality-distribution tests that decisively rejected the Euclidean baseline ($p < 0.001$), rapid convergence to a globally consistent state, and power-law retrieval times mirroring p-adic diffusion [9]. That work establishes the architecture; it does not, however, derive closed-form reaction-time predictions, enumerate the dissonance resolution modes, or define an analogy difficulty measure. Those three gaps are filled here.

## 3. Methods

### 3.1 Semantic space as a rooted tree with an ultrametric

We model an associative web as a finite rooted tree $T$ with leaf set $X$ of concepts. Each edge is assigned a length, and the ultrametric distance between two concepts $x, y \in X$ is

$$d(x,y) = \rho^{-k(x,y)},$$

where $k(x,y)$ is the number of levels between the leaves and their least common ancestor, and $\rho > 1$ is the branching-scale parameter. This is the standard ultrametric on the leaves of a rooted tree: as noted in the comb-representation literature, a sphere centered at the root of any rooted tree is ultrametric, and the tree spanned by a sphere and the root is the coalescent structure of phylogenetics [8]. The strong triangle inequality $d(x,y) \leq d(x,z) \lor d(z,y)$ holds because the least common ancestor of $x$ and $y$ is a descendant of (or equal to) the least common ancestors of $x,z$ and $z,y$; the largest of the three distances is always attained at least twice, which is the defining ultrametric property [1].

### 3.2 The cocycle condition

Following the hypothesis that the brain maintains beliefs by solving the cocycle condition [9], we attach to each ordered pair $(i,j)$ of concepts a multiplicative consistency weight $g_{ij} = \rho^{-k(i,j)} = d(i,j)$, with $g_{ij} = g_{ji}$ and $g_{ii} = 1$. The cocycle (flatness) condition is

$$g_{ij}\, g_{jk} = g_{ik} \quad \text{for all triples } (i,j,k).$$

A belief state is flat when this holds on every triangle; a violation

$$\varepsilon(i,j,k) = \left| g_{ij}\, g_{jk} - g_{ik} \right|$$

is the formal counterpart of cognitive dissonance on the triple. The solver's task is to drive all $\varepsilon$ to zero, either by changing a node weight (node rejection) or by changing the tree itself (global rewarping); Section 4.3 shows these are the only two local modes.

### 3.3 Reaction-time model

We assume the retrieval latency between concepts $x$ and $y$ decomposes into a fixed component and a depth component:

$$\mathrm{RT}(x,y) = \tau_0 + \tau_1\, k(x,y),$$

with $\tau_0$ the baseline latency for adjacent categories and $\tau_1$ the per-level cost. For priming, we adopt the inverse-distance activation law used in the ultrametric SIR model, where per-unit-time transition probability is proportional to $1/d(x,y)$ [7]: a prime at distance $k$ from the target contributes a latency reduction

$$\Delta(k) = \Delta_{\max}\left(1 - \rho^{-k}\right),$$

with $\Delta_{\max}$ the maximal priming benefit. All four parameters ($\rho$, $\tau_0$, $\tau_1$, $\Delta_{\max}$) are stated assumptions, not measurements; Section 6 treats their estimation as the first empirical task.

### 3.4 Analogy depth via the cross-ratio

An analogy item $A{:}B{::}C{:}D$ involves four concepts. Using the comb isometry [8], we assign each concept a real coordinate $t$ equal to the depth of the smallest ultrametric ball containing it, so the four concepts lie on the projective line. The cross-ratio is

$$\lambda = \frac{(t_1 - t_3)(t_2 - t_4)}{(t_1 - t_4)(t_2 - t_3)},$$

which is invariant under projective transformations of the coordinates. We define the analogy depth

$$H(\lambda) = \left| \ln \left| \frac{\lambda}{1 - \lambda} \right| \right|,$$

and predict analogy solution latency as $\mathrm{RT}_{\text{an}} = \tau_0 + \tau_1 H(\lambda)$, by the same per-unit cost $\tau_1$ as the retrieval law. The logarithmic form makes $H$ invariant under the inversion $\lambda \mapsto 1/\lambda$ and symmetric under the classical cross-ratio permutations, as required of a projective invariant.

### 3.5 Validation design

Three tests follow the idea's program. (1) Reaction times: measure RTs in a semantic priming paradigm for word pairs spanning computed tree depths $k = 1, \dots, L$, fit $\tau_0, \tau_1$, and test linearity in $k$. (2) Belief revision: simulate a web with a cocycle constraint, induce violations, and log which resolution mode the solver takes as a function of violation magnitude; the behavioral prediction is that small violations are resolved by node rejection and large ones by rewarping. (3) Analogy: collect difficulty ratings and latencies for $A{:}B{::}C{:}D$ items parameterized by computed $H(\lambda)$, following the parameterized-stimulus alignment method of the visuospatial complexity framework [3].

## 4. Analysis

Every input number in this section is either a stated assumption of the model or a value computed from one. No empirical measurement is introduced.

### 4.1 Tree parameters and the retrieval law

**Assumptions.** Binary tree, $\rho = 2$; depth of the tree $L = 10$ levels; $\tau_0 = 300$ ms; $\tau_1 = 50$ ms per level. These are chosen to be in the plausible range of semantic decision latencies (several hundred milliseconds) and are labeled as assumptions throughout.

The retrieval law gives, for depth difference $k$:

$$\mathrm{RT}(k) = 300 + 50\,k \ \text{ms}.$$

Worked values:

- $k = 1$: $\mathrm{RT} = 300 + 50 \cdot 1 = 350$ ms.
- $k = 2$: $\mathrm{RT} = 300 + 50 \cdot 2 = 400$ ms.
- $k = 5$: $\mathrm{RT} = 300 + 50 \cdot 5 = 550$ ms.
- $k = 10$: $\mathrm{RT} = 300 + 50 \cdot 10 = 800$ ms.

The predicted dynamic range across the full tree is $800 - 350 = 450$ ms, which is large enough to detect with standard behavioral methods.

**Priming benefit.** With $\Delta_{\max} = 100$ ms (assumption) and $\rho = 2$:

$$\Delta(k) = 100\left(1 - 2^{-k}\right).$$

- $k = 1$: $\Delta = 100(1 - 0.5) = 50.0$ ms.
- $k = 2$: $\Delta = 100(1 - 0.25) = 75.0$ ms.
- $k = 3$: $\Delta = 100(1 - 0.125) = 87.5$ ms.
- $k = 10$: $\Delta = 100(1 - 2^{-10}) = 100(1 - 0.0009765625) = 99.90234375$ ms.

The primed latency for a pair at depth $k$ is $\mathrm{RT}_{\text{primed}}(k) = 300 + 50k - 100(1 - 2^{-k})$. For $k = 3$: $300 + 150 - 87.5 = 362.5$ ms. For $k = 10$: $300 + 500 - 99.90234375 = 700.09765625$ ms. The model therefore predicts that priming compresses the depth-RT function: the unprimed slope is $50$ ms per level, while the primed function grows more slowly at small $k$ because the benefit saturates. Concretely, the primed difference between $k=1$ and $k=3$ is $362.5 - (300 + 50 - 50) = 362.5 - 300 = 62.5$ ms, against an unprimed difference of $450 - 350 = 100$ ms for the same pair of depths.

### 4.2 Ultrametricity check on the model space

For any three leaves, the strong triangle inequality must hold. Take three leaves with pairwise least-common-ancestor depths $k_{12} = 2$, $k_{23} = 3$, $k_{13} = 2$. Then $d_{12} = 2^{-2} = 0.25$, $d_{23} = 2^{-3} = 0.125$, $d_{13} = 2^{-2} = 0.25$. Check: $d_{12} = 0.25 \leq \max(d_{13}, d_{32}) = \max(0.25, 0.125) = 0.25$. Holds with equality, as it must in an ultrametric: the two largest of the three distances are equal ($0.25 = 0.25$). This equality-of-the-two-largest property is the operational signature that distinguishes ultrametric from Euclidean geometry, and it is the statistic whose distribution rejected the Euclidean baseline at $p < 0.001$ in the predecessor simulation study [9].

### 4.3 Cocycle violations and the two resolution modes

Take the same triple with weights $g_{12} = 0.25$, $g_{23} = 0.125$, $g_{13} = 0.25$. The cocycle condition requires $g_{12} g_{23} = g_{13}$:

$$g_{12}\, g_{23} = 0.25 \times 0.125 = 0.03125 = \tfrac{1}{32}, \qquad g_{13} = 0.25 = \tfrac{8}{32}.$$

Violation:

$$\varepsilon = \left| \tfrac{1}{32} - \tfrac{8}{32} \right| = \tfrac{7}{32} = 0.21875.$$

The flatness condition can be restored in exactly two local ways, because the constraint $g_{ij} g_{jk} = g_{ik}$ on a triangle has three terms and the solver may repair either factor on the left or the single term on the right; repairing the right-hand term while keeping the tree structure is node rejection, and repairing it by changing the tree depth is global rewarping.

**Mode 1: node rejection.** Keep $g_{12} = 1/4$ and $g_{13} = 1/4$ and change $g_{23}$ so that $g_{12} g_{23} = g_{13}$:

$$g_{23}^{\text{new}} = \frac{g_{13}}{g_{12}} = \frac{1/4}{1/4} = 1, \qquad k_{23}^{\text{new}} = -\log_2(1) = 0.$$

The rejected node is pulled to distance $1$ (identity weight), i.e., the inconsistent relation is severed: the concept pair $(2,3)$ is treated as unrelated. The cost is the loss of one associative link.

**Mode 2: global rewarping.** Keep $g_{12} = 1/4$ and $g_{23} = 1/8$ and change $g_{13}$:

$$g_{13}^{\text{new}} = g_{12}\, g_{23} = \tfrac{1}{32}, \qquad k_{13}^{\text{new}} = -\log_2\!\left(\tfrac{1}{32}\right) = 5.$$

The whole tree must be rewarped so that concepts 1 and 3 now sit 5 levels apart instead of 2, because in a tree ultrametric every pairwise depth is determined by the branching structure. The cost is a structural change propagating to every triple containing $\{1,3\}$.

**Mode selection rule.** Node rejection changes one edge weight; rewarping changes the depth of one pair and, through the tree constraint, the depths of all pairs whose least common ancestor moves. If a node participates in $m$ triples, rewarping touches $O(m)$ constraints while rejection touches $O(1)$. The model therefore predicts: for a violation small enough that the required rewarp moves the pair by few levels ($\Delta k$ small), rewarping is cheap; for a violation requiring a large $\Delta k$, or when the pair participates in many other flat triples, rejection is cheaper. In the worked example, rewarping moves $k_{13}$ from 2 to 5, a change of $\Delta k = 3$ levels, and the predicted processing cost under the retrieval law is $\tau_1 \Delta k = 50 \times 3 = 150$ ms of additional resolution latency, against a rejection cost of one severed link. This gives the dissonance-reduction mapping: rejecting the new belief corresponds to node rejection (severing the inconsistent link), while restructuring the belief system corresponds to global rewarping.

### 4.4 Analogy depth: worked computation

**Item 1 (deep).** Coordinates $t_1 = 0$, $t_2 = 1$, $t_3 = 3$, $t_4 = 4$:

$$\lambda_1 = \frac{(0 - 3)(1 - 4)}{(0 - 4)(1 - 3)} = \frac{(-3)(-3)}{(-4)(-2)} = \frac{9}{8} = 1.125.$$

$$1 - \lambda_1 = 1 - \tfrac{9}{8} = -\tfrac{1}{8}, \qquad \frac{\lambda_1}{1 - \lambda_1} = \frac{9/8}{-1/8} = -9, \qquad H_1 = |\ln 9| = \ln 9 \approx 2.19722.$$

Predicted latency: $\mathrm{RT}_{\text{an},1} = 300 + 50 \times 2.19722 = 300 + 109.861 = 409.861$ ms.

**Item 2 (shallow).** Coordinates $t_1 = 0$, $t_2 = 1$, $t_3 = 2$, $t_4 = 3$:

$$\lambda_2 = \frac{(0 - 2)(1 - 3)}{(0 - 3)(1 - 2)} = \frac{(-2)(-2)}{(-3)(-1)} = \frac{4}{3} \approx 1.33333.$$

$$1 - \lambda_2 = -\tfrac{1}{3}, \qquad \frac{\lambda_2}{1 - \lambda_2} = \frac{4/3}{-1/3} = -4, \qquad H_2 = \ln 4 \approx 1.38629.$$

Predicted latency: $\mathrm{RT}_{\text{an},2} = 300 + 50 \times 1.38629 = 300 + 69.315 = 369.315$ ms.

**Predicted difficulty difference.**

$$\Delta \mathrm{RT}_{\text{an}} = 50 \times (\ln 9 - \ln 4) = 50 \times \ln\!\left(\tfrac{9}{4}\right) = 50 \times \ln(2.25) = 50 \times 0.81093 = 40.547 \ \text{ms}.$$

The deep item is predicted to take about 40.5 ms longer than the shallow item, under the stated $\tau_1 = 50$ ms per unit of logarithmic depth.

### 4.5 Consistency of the analogy measure with the tree

The cross-ratio construction is legitimate on this space because the comb isometry theorem guarantees that a compact ultrametric space with a non-atomic measure charging every ball is globally isometric to a comb metric space carrying Lebesgue measure [8]; the coordinates $t$ are exactly the comb-interval coordinates. The scale-invariance precedent of the Cantor-set valuation, which is both scale and reparametrisation invariant [4], is mirrored by $H(\lambda)$: under a common rescaling $t_i \mapsto c\, t_i$ the cross-ratio is unchanged, so analogy depth does not depend on the absolute calibration of the semantic coordinate, only on the relational structure. This is the property that makes the measure transferable across individuals whose trees differ in absolute depth.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions ($\rho = 2$, $L = 10$, $\tau_0 = 300$ ms, $\tau_1 = 50$ ms, $\Delta_{\max} = 100$ ms); they are model predictions, not measurements.

**R1 (Retrieval law).** Predicted retrieval latency is linear in tree-depth difference: $\mathrm{RT}(k) = 300 + 50k$ ms, giving 350 ms ($k=1$), 400 ms ($k=2$), 550 ms ($k=5$), and 800 ms ($k=10$), a dynamic range of 450 ms across the tree.

**R2 (Priming compression).** With inverse-distance activation, the priming benefit is $\Delta(k) = 100(1 - 2^{-k})$ ms: 50.0 ms at $k=1$, 75.0 ms at $k=2$, 87.5 ms at $k=3$, and 99.90234375 ms at $k=10$. Priming compresses the depth-latency function: the predicted primed difference between depths 1 and 3 is 62.5 ms against an unprimed difference of 100 ms.

**R3 (Ultrametric signature).** On the model tree, the two largest of any three pairwise distances are equal (worked check: $0.25 = 0.25$ for the triple with depths $2, 3, 2$). This equality statistic is the model's discriminator against Euclidean geometry, consistent with the predecessor simulation's rejection of the Euclidean baseline at $p < 0.001$ on triangle-inequality distributions [9].

**R4 (Two resolution modes).** A cocycle violation of magnitude $\varepsilon = 7/32 = 0.21875$ on the worked triangle admits exactly two local repairs: node rejection, setting $g_{23} = 1$ ($k_{23} = 0$), severing one link; or global rewarping, setting $g_{13} = 1/32$ ($k_{13} = 5