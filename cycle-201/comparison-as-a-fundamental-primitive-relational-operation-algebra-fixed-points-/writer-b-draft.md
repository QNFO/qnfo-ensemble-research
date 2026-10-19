# Comparison as a Primitive Relational Operation: A Minimal Algebra, Its Fixed Points, and an Information-Free Limit

## Abstract

A long-standing question in the foundations of physics is whether the relational structure that pervades quantum mechanics, gauge theory, and general relativity can be traced to a single primitive operation. The specific gap addressed here is formal: no existing framework defines a minimal algebra whose only primitive is pairwise comparison and then checks which familiar physical structures survive as fixed points of iterated comparison. We define a comparison algebra $\mathcal{C}_{N}$ over a finite distinction space of $2^{N}$ states, in which a state is nothing but the record of its pairwise comparison outcomes, and we derive four results with explicit arithmetic. First, the comparison count grows as $M = 2^{N}(2^{N}-1)/2$, reaching $523{,}776$ comparisons for $N = 10$ and $5.4976 \times 10^{11}$ for $N = 20$, so unconstrained comparison is exponentially expensive. Second, a bit-budget theorem shows that $k$ binary comparisons reduce an observer's residual uncertainty from $N$ bits to at least $N - k$ bits, so the information-free limit obtained by suspending all comparison is well defined at $H_{0} = N$ bits of residual entropy. Third, the fixed point of iterated hierarchical comparison is ultrametric, with $2^{l}$ nested balls at depth $l$ and $2^{L}-1 = 1023$ internal nodes at $L = 10$, providing a mechanism by which hierarchical geometry emerges from comparison alone. Fourth, resolving one state completely costs at least $E = N\,k_{B}T\ln 2 = 2.871 \times 10^{-20}\,\mathrm{J}$ at $T = 300\,\mathrm{K}$ for $N = 10$, tying the algebra to thermodynamic bounds. The framework unifies relational readings of physics under one primitive and yields a falsifiable claim: any physical law must be expressible in comparative form.

## 1. Introduction

Physicists designing experiments at the quantum-classical boundary, and researchers in quantum-gravity programs that build spacetime from entanglement, face a recurring conceptual cost: every framework they use carries a separate account of what a measurement is, what a relation is, and what an observer does. A measurement theory for one formalism does not transfer to another; entanglement-based spacetime programs and relational interpretations of quantum mechanics each reconstruct physical structure from their own primitives, and no shared primitive exists that would let results move between them. Today this blocks, for example, translating a relational statement about quantum events into a statement about emergent geometry without re-deriving the bridge by hand each time. If a single primitive operation could be shown to generate measurement structure, relational facts, and geometric fixed points at once, the design decision that changes is which structures a theory-builder is entitled to posit: only comparison-derived ones, with everything else required to emerge as a fixed point.

The conjecture examined in this paper is that comparison — correlation, relation, ratio — is the single primitive operation underlying physical structure, and that an observer differs from a physical system only in being able to suspend or resume the operation. The practical stake is a unification of three research programs that currently share vocabulary but not formalism: relational quantum mechanics, in which facts are relative to interacting systems [2]; entanglement- and relation-based reconstructions of spacetime; and operational criteria for what counts as physically real [12]. The conjecture also makes a sharp, falsifiable claim: no physical law should be expressible without comparative structure. If that claim holds, a theory-builder can reject any proposed law whose statement cannot be cast as a comparison; if it fails, the unification collapses.

The strategy is deliberately minimal. Rather than beginning with spacetime or with Hilbert space, we begin with a finite set of states and a single binary operation that compares two states and returns an outcome. We then ask which familiar structures — counting, entropy, metric geometry, scale-free distributions — appear as fixed points or necessary consequences of iterating that operation. The finite-distinction setting follows the construction of distinction spaces over $N$-bit records with an ultrametric $d_{u}$, in which maintaining a distinction means an observer can reliably re-identify which side of a binary partition the world is on [11]. The thermodynamic side follows the operational criterion that a quantity is physically real only if a finite protocol can approximate it with a computable modulus of convergence, together with the Landauer cost of erasing a bit, $k_{B}T\ln 2$ [12]. The philosophical motivation for putting relational or mental structure before material substance is discussed in the fundamentality-reversal program [5], and the concept of physical law itself — the separation of dynamical laws from initial conditions, and laws as differential equations that compare neighboring configurations — is reviewed in [8].

This paper is analytical and foundational. It derives counting bounds, an entropy budget, an energy bound, and a fixed-point characterization; it does not report simulations or measurements. Its claims are therefore at the level of mathematical structure, and their empirical content is confined to the falsifiability criterion stated in Section 6.

The contributions are:

- A minimal comparison algebra $\mathcal{C}_{N}$ over $2^{N}$ states, with the comparison-count bound $M = 2^{N}(2^{N}-1)/2$ computed explicitly for $N = 10$ and $N = 20$ (Section 4.1).
- A bit-budget theorem showing that $k$ binary comparisons reduce residual uncertainty to at least $N - k$ bits, which makes the suspended-comparison, information-free limit well defined at $H_{0} = N$ bits (Section 4.2).
- A fixed-point result: iterated hierarchical comparison closes onto an ultrametric geometry with $2^{l}$ nested balls at depth $l$, computed for $L = 10$ (Section 4.3).
- A thermodynamic lower bound on complete resolution, $E = N\,k_{B}T\ln 2 = 2.871 \times 10^{-20}\,\mathrm{J}$ at $T = 300\,\mathrm{K}$, $N = 10$ (Section 4.4).
- A falsifiability criterion for the claim that all physical law is comparative, tested against the structure of laws as reviewed in [8] (Section 6).

## 2. Background and Related Work

The relational reading of quantum mechanics is the closest existing position to the conjecture. [2] argues that quantum theory points to an ontology of relations, and states that in the relational interpretation an eigenvalue of a self-adjoint operator corresponds to an element of reality — a fact or event about a physical system in interaction — while subjectivity, agents, and mind play no role. [2] further documents that this relationality is not confined to quantum theory: gauge degrees of freedom are handles for interactions with other systems, and even particles in quantum field theory are relative rather than absolute entities, with a structural analogy between the relations of quantum mechanics and those of spacetime. The present paper adopts [2]'s relational facts as the target output of the comparison operation: a comparison outcome is the minimal formal object corresponding to a relational fact. What [2] leaves open, and what this paper supplies, is a single algebraic primitive from which such facts can be generated and counted.

The concept of physical law provides the test bed for the falsifiability claim. [8] reviews the separation of dynamical laws from initial conditions, quoting Wigner's formulation that the regularities science uncovers are the laws of nature while the unspecified elements are initial conditions, and notes that fundamental laws are expressible as differential equations up to second order in space and time. [8] also presents the Einstein field equations $R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^{4}}T_{\mu\nu}$ as equations that describe spacetime itself rather than living on a given spacetime, and raises the problem of time — time is absolute in quantum mechanics but dynamical in general relativity — as the obstacle to combining the two. A differential equation is comparative in a precise sense: it equates a function's value at a point with a limit of differences against neighboring points, and a tensor equation compares geometric objects evaluated at the same event. Section 6 uses this structure from [8] to state what it would take for a law to be non-comparative.

The database theory of ontological queries supplies a formal template for projecting a theory back onto what a substrate can answer. [1] studies ontological queries — queries evaluated against an ontology on top of a relational database — and develops query rewriting, the compilation of an ontological query into an equivalent direct query against the underlying database, together with optimization of the compiled queries; the reasoning tasks in the well-known decidable fragments of OWL are typically $2\textsc{-exptime}$-complete, and the rewriting approach was implemented in the prototype system Nyaya over a Datalog engine extended to existential head variables. In this paper's setting, the comparison algebra plays the role of the ontology and the record of retained comparison outcomes plays the role of the database: any question an observer asks must be compiled down to comparisons actually performed, and the counting bounds of Section 4.1 are the cost of that compilation.

The operational-reality criterion constrains what the algebra may treat as physically meaningful. [12] proposes that a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence yielding measurement-distinguishable predictions, argues that a theory predicting uncomputable quantities is operationally vacuous and untestable, and derives the resource connection: if measuring a quantity $Q$ to precision $\varepsilon$ requires $\mu(-\log_{2}\varepsilon)$ steps at $E$ joules per step, the total energy cost is $E \cdot \mu(n)$, connecting the criterion to Landauer's principle, under which erasing a bit costs $k_{B}T\ln 2$ in thermodynamic entropy. Section 4.4 applies exactly this resource accounting to the comparison operation itself.

The finite-distinction framework gives the state space. [11] defines a distinction space $D_{N} = (S_{N}, d_{u})$ with $S_{N} = \{0,1\}^{N}$ and an ultrametric $d_{u}$ satisfying $d_{u}(x_{i},x_{j}) \leq \max\{d_{u}(x_{i},x_{k}), d_{u}(x_{k},x_{j})\}$, realizes the geometry by a $b$-ary tree of depth $L$ with $N = L\log_{2}b$ and $|S_{N}| = b^{L} = 2^{N}$, and proves that the number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$. [11] also borrows the rewrite-then-optimize split of [1] as the template for projecting existence claims onto a substrate. The present paper takes $D_{N}$ as the arena on which the comparison operation acts and derives the ultrametric as a fixed point rather than assuming it.

The critique of prescriptive law motivates treating comparison, rather than law, as primitive. [10] argues that the concept of "laws of nature" as immutable, objective prescriptions is an inadequate foundation, reviewing van Fraassen's dismantling of the metaphysical superstructure built on regularities and the failure of necessitarian accounts that ground lawhood in truths holding across a family of possible worlds. If lawhood as an ontological category is untenable, the regularities themselves — which are comparative structures par excellence — become the primary objects, which is the position this paper formalizes.

The fundamentality-reversal program supplies the conceptual precedent for placing observer-side structure first. [5] argues that in a regime containing powerful technology or quantum effects, the orthodox arrow from physical world to first-person perspective can be reversed: the author describes a "proof of principle" theory that starts with the "self" and shows that an emergent notion of "world" follows. The consciousness-related element of the present conjecture — that an observer can toggle comparison on and off — is stated here as a hypothesis aligned with [5]'s reversal, not as a derived result; Section 6 marks it as such.

Scale-free fixed points of iterated dynamics give an existence proof that simple iterated interactions converge to power-law structure. [3] shows, through a size-structured multispecies population model with allometric scaling of growth and mortality, that predator-prey dynamics can drive a plankton assemblage toward a power-law relationship between cell mass and abundance, with the near-power-law equilibrium acting as an attractor when enough species are present. [4] analyzes the stability of the power-law steady state of marine size spectra — abundance as a power law of body mass with exponent approximately $-2$ — via a jump-growth equation and McKendrick-von Foerster approximations, finding a continuous spectrum of eigenvalues and setting the predator search exponent $\alpha$ so that $\alpha = \gamma - 1$ at steady-state exponent $\gamma$. These works demonstrate the general pattern this paper conjectures for comparison dynamics: iteration of a local interaction rule can possess a scale-free fixed point. They are used as an analogy for the fixed-point program of Section 4.3, not as evidence about physics.

Two further works in the surrounding literature could not be used for specific claims because their available content does not state methods or results bearing on this paper's argument; they are therefore not cited further.

## 3. Methods

### 3.1 The comparison algebra

We work in a finite distinction space $D_{N} = (S_{N}, d_{u})$ in the sense of [11]: $S_{N} = \{0,1\}^{N}$ is the set of $N$-bit distinction records, with $|S_{N}| = 2^{N}$ states, and $d_{u}$ is an ultrametric. A binary comparison is a map

$$
\kappa : S_{N} \times S_{N} \to \{0,1\},
$$

which returns $1$ if the two records differ on the coordinate being probed and $0$ otherwise. A comparison outcome is the pair $(x_{i}, x_{j}, \kappa(x_{i},x_{j}))$; this is the formal counterpart of a relational fact in the sense of [2]. A comparison record of an observer is the set $R_{k} = \{(i_{m}, j_{m}, o_{m})\}_{m=1}^{k}$ of $k$ retained outcomes.

The algebra $\mathcal{C}_{N}$ has one primitive operation (comparison), one composition rule (a comparison whose inputs are themselves comparison outcomes, i.e., comparing records), and one closure condition: a structure is admissible in $\mathcal{C}_{N}$ only if it is definable by a finite Boolean formula over comparison outcomes, mirroring the admissibility condition of [11] over base coordinates.

### 3.2 Iteration and fixed points

Define the iteration operator $\Phi$ on comparison records: $\Phi(R_{k}) = R_{k} \cup \{\text{one new comparison, or one comparison of two existing outcomes}\}$. A fixed point of iterated comparison is a record $R^{*}$ with $\Phi(R^{*}) = R^{*}$, i.e., a closed structure in which every further comparison either reproduces an existing outcome or is a comparison of outcomes already in $R^{*}$. We study which structures — equivalence relations, ultrametrics, power-law distributions — can be such fixed points.

### 3.3 The information-free limit

The conjecture's second element is that suspending comparison — removing all relational updates — yields a well-defined, information-free limit. We formalize this as the entropy of the observer's posterior over $S_{N}$ given a comparison record $R_{k}$, under a uniform prior, and we show the limit $k \to 0$ exists and equals maximal residual entropy.

### 3.4 Assumptions

We assume: (i) the state space is finite with $|S_{N}| = 2^{N}$, following [11]; (ii) each comparison returns one binary outcome and is erasure-free at the level of the record but subject to Landauer cost when the observer discards an outcome, following [12]; (iii) the prior over states is uniform, so that initial entropy is exactly $N$ bits; (iv) temperature $T = 300\,\mathrm{K}$ for all numerical energy bounds, as a room-temperature reference value. Assumptions (iii) and (iv) are the paper's own and are not taken from the cited works.

## 4. Analysis

### 4.1 Counting comparison outcomes

The number of unordered pairwise comparisons among $|S_{N}| = 2^{N}$ states is

$$
M(N) = \binom{2^{N}}{2} = \frac{2^{N}(2^{N}-1)}{2}.
$$

Derivation for $N = 10$: $2^{10} = 1024$, so

$$
M(10) = \frac{1024 \times 1023}{2} = \frac{1{,}047{,}552}{2} = 523{,}776.
$$

Derivation for $N = 20$: $2^{20} = 1{,}048{,}576$, so

$$
M(20) = \frac{1{,}048{,}576 \times 1{,}048{,}575}{2} = \frac{2^{40} - 2^{20}}{2} = \frac{1{,}099{,}511{,}627{,}776 - 1{,}048{,}576}{2} = \frac{1{,}099{,}510{,}579{,}200}{2} = 549{,}755{,}289{,}600 \approx 5.4976 \times 10^{11}.
$$

The comparison count grows as $M(N) \sim 2^{2N-1}$, i.e., doubly exponentially in the bit-depth $N$ per observer generation, while the state count grows as $2^{N}$. The ratio of comparisons to states is

$$
\frac{M(N)}{2^{N}} = \frac{2^{N}-1}{2},
$$

which equals $(1024-1)/2 = 511.5$ at $N = 10$: an observer performing all pairwise comparisons does $511.5$ times more work than the number of states would suggest. This is the first structural result: unconstrained comparison is exponentially expensive, so any physical implementation of the primitive must be selective, which is precisely the role the rewrite-then-optimize discipline of [1] plays for ontological queries.

For context on the expressive side, [11] proves that the number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$. At $N = 10$ this is $2^{1024}$; since $\log_{10} 2 = 0.30103$, we get $\log_{10}(2^{1024}) = 1024 \times 0.30103 = 308.25$, so

$$
2^{1024} \approx 1.80 \times 10^{308}.
$$

The predicate space is astronomically larger than the comparison space $M(10) = 5.24 \times 10^{5}$, so only a vanishing fraction of admissible existence claims can be grounded by direct pairwise comparison. This gap between $2^{2^{N}}$ admissible predicates and $O(2^{2N})$ grounded comparisons is the quantitative form of the re-entry problem discussed in [11]: most existence claims an algebra can formulate are not ones its primitive can verify.

### 4.2 The bit-budget theorem and the information-free limit

**Theorem 1 (Bit budget).** Let the prior over $S_{N}$ be uniform, so the initial entropy is $H_{0} = \log_{2}|S_{N}| = N$ bits. Any record $R_{k}$ of $k$ binary comparison outcomes leaves residual posterior entropy

$$
H_{k} \geq N - k \ \text{bits},
$$

with equality when the $k$ outcomes are independent.

*Proof.* Each comparison outcome is a binary random variable, hence carries at most $1$ bit of information about the state. Information cannot increase under conditioning, so $H_{k} \geq H_{0} - I(\text{state}; R_{k})$ and $I(\text{state}; R_{k}) \leq \sum_{m=1}^{k} H(o_{m}) \leq k$ bits. Therefore $H_{k} \geq N - k$. $\square$

Consequences:

1. **Complete resolution requires at least $N$ comparisons.** To identify one state among $2^{N}$, the residual entropy must drop to $0$, so $k \geq N$. For $N = 10$, at least $10$ independent binary comparisons are needed; fewer cannot single out a state, by the pigeonhole principle applied to the at most $2^{k}$ distinguishable classes the outcomes define.

2. **The information-free limit is well defined.** Suspending comparison entirely, $k = 0$, gives $H_{0} = N$ bits: the observer retains no relational facts and its posterior is the uniform prior. This is the precise sense in which "removing relational updates" yields an information-free state — not a contradiction or a vacuum, but the maximal-entropy limit $H_{0} = N$. For $N = 10$, that limit is $10$ bits of residual uncertainty over $1024$ states.

3. **Partial suspension is graded.** The conjecture that an observer can "toggle" comparison maps onto moving along the line $H_{k} = N - k$: each suspended comparison raises residual entropy by at most one bit, each resumed comparison lowers it by at most one bit. The toggle is a move on a one-bit-per-step entropy ladder, which is the quantitative content of the consciousness hypothesis stated in Section 1 and marked as a hypothesis, not a derivation.

### 4.3 The ultrametric fixed point of iterated comparison

Let comparisons be organized hierarchically: the observer first compares states on coarse partitions, then refines. Realizing $S_{N}$ as a $b$-ary tree of depth $L$ with $N = L \log_{2} b$ and $b^{L} = 2^{N}$ leaves, as in [11], a comparison at depth $l$ distinguishes between the $b^{l}$ nodes at that depth.

**Proposition 2 (Hierarchical closure).** The fixed point of iterated hierarchical comparison is an ultrametric: the induced distance $d_{u}(x_{i}, x_{j})$ = depth of the shallowest common ancestor satisfies $d_{u}(x_{i},x_{j}) \leq \max\{d_{u}(x_{i},x_{k}), d_{u}(x_{k},x_{j})\}$, and the balls at depth $l$ number $b^{l}$ and are nested.

*Proof sketch.* Two states $x_{i}, x_{j}$ share their shallowest common ancestor with $x_{k}$'s relation to either: among three leaves of a tree, two always share a shallower common ancestor than either shares with the third, which is exactly the strong triangle inequality. Nesting follows because a ball at depth $l$ (the set of leaves below one node) is contained in exactly one ball at depth $l - 1$. $\square$

Numerical illustration at $b = 2$, $L = N = 10$: the number of internal nodes, hence nontrivial comparison classes, is

$$
\sum_{l=1}^{10} 2^{l} = 2^{11} - 2 = 2046,
$$

and the number of balls at depth $l$ is $2^{l}$, from $2$ at the root to $1024$ at the leaves. The total count of internal nodes is $2^{L} - 1 = 1023$ if the root itself is counted once rather than summed per level with the root excluded; we use the per-level sum $2046$ when counting all directed parent-child comparison edges and $1023$ when counting nodes. The fixed point of iterated comparison is therefore not a Euclidean metric but a hierarchy — depth of distinction, not metric distance, carries the content, exactly as in the finite-distinction geometry of [11]. This is the paper's mechanism for "geometry from comparison": metric-like structure emerges as the ultrametric fixed point, and coarser, approximately translational geometries would have to appear as further coarse-grainings of this hierarchy, which we do not demonstrate here.

### 4.4 Thermodynamic cost of comparison

Following the resource accounting of [12] — measuring a quantity to precision requiring $\mu(n)$ steps at $E$ joules per step costs $E \cdot \mu(n)$, with Landauer's bound $k_{B}T\ln 2$ per bit erasure — the minimal thermodynamic cost of fully resolving one state is the cost of processing $N$ comparison bits:

$$
E_{\min} = N \, k_{B} T \ln 2.
$$

Numerical evaluation at $N = 10$, $T = 300\,\mathrm{K}$, $k_{B} = 1.380649 \times 10^{-23}\,\mathrm{J\,K^{-1}}$:

$$
k_{B}T = 1.380649 \times 10^{-23} \times 300 = 4.141947 \times 10^{-21}\,\mathrm{J},
$$
$$
k_{B}T\ln 2 = 4.141947 \times 10^{-21} \times 0.693147 = 2.870949 \times 10^{-21}\,\mathrm{J},
$$
$$
E_{\min} = 10 \times 2.870949 \times 10^{-21} = 2.870949 \times 10^{-20}\,\mathrm{J} \approx 2.871 \times 10^{-20}\,\mathrm{J}.
$$

This is a lower bound: it counts only the irreducible erasure cost of the $N$ outcome bits, not the cost of the physical interactions that realize each comparison. The bound scales linearly in $N$ for complete resolution of one state, but quadratically-exponentially for the full comparison graph, since $M(N) \sim 2^{2N-1}$ comparisons at $\geq k_{B}T\ln 2$ each would cost $\geq 2^{2N-1} k_{B}T\ln 2$; at $N = 20$ that projection is $\geq 5.4976 \times 10^{11} \times 2.871 \times 10^{-21} \approx 1.578 \times 10^{-9}\,\mathrm{J}$ per complete pairwise sweep of a $2^{20}$-state space (projection, assuming one bit-erasure per comparison at $T = 300\,\mathrm{K}$).

### 4.5 Scale-free fixed points as a precedent

The fixed-point program of Section 4.3 has a precedent in iterated ecological dynamics. [3] demonstrates that predator-prey dynamics with allometric scaling drive a multispecies assemblage toward a power-law abundance-mass relation that acts as an attractor, and [4] establishes the local stability of the power-law steady state of marine size spectra — exponent approximately $-2$ in abundance density — through a continuous eigenvalue spectrum of the jump-growth equation and its McKendrick-von Foerster approximations, with the constraint $\alpha = \gamma - 1$ linking predator search exponent $\alpha$ to steady-state exponent $\gamma$. The analogy is structural: a local iterated interaction rule (there, predation; here, comparison) can possess a scale-free fixed point that attracts the dynamics. We conjecture, but do not prove, that comparison-update rules with scale-free outcome statistics possess analogous power-law fixed points; this is the open computational question of Section 6.

## 5.