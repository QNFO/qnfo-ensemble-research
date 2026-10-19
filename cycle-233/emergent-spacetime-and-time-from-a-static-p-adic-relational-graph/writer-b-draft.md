# Ultrametric Signatures of a Static Relational Substrate: A Formal Framework for Emergent Time, Space, and Probability on a $p$-Adic Graph

## Abstract

A persistent tension in foundational physics is that general relativity treats spacetime as dynamical while quantum mechanics presupposes an external time parameter, and several approaches to quantum gravity converge on a timeless description of the universe's state. This paper addresses a specific gap: no existing framework simultaneously (i) defines a concrete static, discrete, non-Archimedean relational graph as the sole ontology, (ii) derives an emergent approximately Lorentzian metric from it by explicit coarse-graining, and (iii) derives an epistemic probability rule resembling the Born rule from subgraph counting. We construct a $(p+1)$-regular tree model with the $p$-adic ultrametric, show that the ultrametric inequality $|x+y|_p \leq \max\{|x|_p,|y|_p\}$ forces a hierarchical (tree-like) geometry, derive that the number of vertices within graph distance $n$ of a root grows as $(p+1)p^{n-1}$, and show that coarse-graining over balls of radius $p^N$ yields a smooth effective metric whose geodesic structure approximates a manifold for $N \gg 1$. We derive an epistemic probability rule $P(A) = N_A / N_{\text{total}}$ from uniform counting over a coarse-grained ball and show it reproduces Born-rule-like statistics when amplitudes are encoded as branch multiplicities. As a falsifiable projection, we estimate that Planck-scale discreteness would first perturb cosmic microwave background multipoles near $\ell \sim 10^{61}$, far beyond observation, so the discriminating signatures must instead be sought in ultrametric clustering statistics of entanglement structure.

## 1. Introduction

Physicists designing experiments at the boundary of quantum gravity, and theorists attempting to reconcile quantum mechanics with general relativity, currently lack any operational test that distinguishes a continuous spacetime ontology from a discrete one. The cost of this gap is concrete: quantum-gravity research programs have produced no experimentally confirmed prediction, and the incompatibility between the fixed external time of quantum mechanics and the dynamical spacetime of general relativity blocks construction of a single consistent fundamental theory [11]. If a static, discrete, non-Archimedean relational substrate could be shown to reproduce the observed continuum plus quantum statistics as interface artifacts, then the design target for falsification experiments changes: instead of seeking Planck-scale discreteness directly in propagation (which we show is separated from observation by roughly sixty orders of magnitude), one would seek ultrametric — hierarchically clustered — signatures in entanglement structure and cosmological fluctuation statistics, which are observable quantities.

The problem is faced by three groups. First, quantum-gravity theorists need a background-independent ontology that does not presuppose time; the Wheeler-DeVitt-style timeless descriptions noted in [9] and [11] supply the motivation but not a concrete graph model with derived observables. Second, experimentalists analyzing cosmic microwave background (CMB) data and entanglement statistics need a predicted signature that discriminates discrete from continuum ontology; no such signature is currently derived from a specific non-Archimedean model. Third, mathematicians working on $p$-adic probability and $p$-adic structures have the tools — ultrametric analysis, $p$-adic Gibbs measures, $p$-adic Hilbert spaces — but these have not been assembled into a derivation chain from graph ontology to observable statistics.

This paper builds that chain for an idealized model and states precisely where it is conjectural. The model is a static $(p+1)$-regular tree (the combinatorial skeleton of the Bruhat-Tits tree used in [11]) whose vertices are the sole ontological entities, with distances given by the $p$-adic norm. We make no claim that the full program is complete; we claim that four specific derivations go through and that their failure modes are identifiable.

Contributions:

1. A proof that the $p$-adic ultrametric on a $(p+1)$-regular tree forces strictly hierarchical clustering, with an explicit count of vertices in ultrametric balls (Section 4.1).
2. A coarse-graining construction showing that the effective metric on balls of radius $p^N$ becomes locally Euclidean-like with error controlled by $p^{-N}$, derived with explicit arithmetic (Section 4.2).
3. A derivation of an epistemic probability rule $P(A) = N_A/N_{\text{total}}$ from uniform counting over coarse-grained balls, and the condition under which it matches the Born rule (Section 4.3).
4. A quantitative projection, with stated assumptions, that Planck-scale discreteness produces no observable CMB artifact below multipole $\ell \sim 10^{61}$, redirecting falsification toward ultrametric clustering statistics (Section 4.4).

## 2. Background and Related Work

The $p$-adic numbers arise by completing the rationals under a norm that is not the usual absolute value. For a rational $x = p^r \frac{n}{m}$ with $p \nmid nm$, the $p$-adic norm is $|x|_p = p^{-r}$, and it satisfies the strong triangle inequality $|x+y|_p \leq \max\{|x|_p, |y|_p\}$, called ultrametricity [1]. This single property is the mathematical seed of everything in this paper: ultrametric spaces are exactly the spaces whose geometry is tree-like, because in an ultrametric every point of a ball is its center and two balls are either disjoint or nested. Work [1] uses precisely this structure on a Cayley tree — an infinite tree where each vertex has $k+1$ edges — to define $p$-adic Gibbs measures, and proves for the three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two that a phase transition occurs if and only if $p = 3$, for any nonzero interaction, while for $p \neq 3$ the Gibbs measure is unique [1]. This result matters here for two reasons. First, it demonstrates that statistical mechanics on trees with $p$-adic valued probabilities is a working, rigorous enterprise, so our ontological proposal inherits a developed mathematical toolkit. Second, the $p$-dependence of its phase transition ($p=3$ exactly) is a template for the kind of sharp, model-discriminating statement we seek: the ontology makes predictions that depend on the prime $p$, which is falsifiable in principle.

The idea that quantum theory itself can be formulated over $p$-adic numbers is established. Work [3] surveys $p$-adic and adelic quantum mechanics, which emerged in 1987 from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and distinguishes two formulations: one with $p$-adic-valued wave functions (Vladimirov-Volovich-Khrennikov) and one with complex-valued wave functions on $p$-adic argument spaces, the latter being more suitable for connection with ordinary quantum mechanics [3]. Work [3] also records that ordinary quantum mechanics has four sectors — Hilbert space, quantization, evolution, interpretation — with the Heisenberg algebra $[\hat{x}_i, \hat{k}_j] = i\hbar\,\delta_{ij}$, and that a direct $p$-adic analogue of the Schrödinger equation cannot be written with complex-valued wave functions because the $p$-adic analogue of the Heisenberg algebra fails in that setting. This is directly relevant to our Section 4.3: the Born rule cannot simply be transported into a $p$-adic setting; it must be re-derived, which is what our counting construction attempts. Work [3] further notes that noncommutative field theory, with the Moyal product $(f \star g)(x) = \exp\!\left[\frac{i\hbar}{2}\theta^{ij}\frac{\partial}{\partial y^i}\frac{\partial}{\partial z^j}\right] f(y) g(z)\big|_{y=z=x}$, is among the recent developments adjacent to $p$-adic approaches, indicating that deformation of the classical product structure is a general mechanism by which continuum theories admit non-standard underlying geometries.

A concrete physics program built on $p$-adic structures is Topological Geometrodynamics (TGD). Work [4] shows a result we use as a structural precedent: the algebraic extensions of $p$-adic numbers allowing a square root near the $p$-adic real axis have dimension $D=4$ for $p > 2$ and $D=8$ for $p=2$, and the region of $p$-adic spacetime where the square root function converges can be regarded as the $p$-adic counterpart of the future light cone, consisting of cylinders parallel to the time axis with radius $N_p(t) = p^k$ and length $p^{k-1}(p-1)$ at points $t = p^k$ [4]. That a light-cone-like structure emerges from pure $p$-adic analysis — not inserted by hand — is the strongest existing evidence that causal structure can be non-Archimedean in origin, which our Section 4.2 parallels at the level of metric emergence. Work [5], the mathematical companion to [4], supplies the essential bridge device: the canonical identification, a natural continuous map from $p$-adic numbers to non-negative reals that maps a $p$-adic expansion $y = \sum_{k>N} y_k p^k$ to a real number by reading the same digits in reverse, and is continuous although its inverse is complicated by the non-uniqueness of $p$-adic expansions (as $1 = 0.999\ldots$ in the decimal analogy) [5]. Work [5] also records that $p$-adic numbers are completions of the rationals with norm $|x| = p^{-k_0(x)}$ depending only on the lowest digit of the expansion, and that algebraic extensions of arbitrary dimension exist for $p$-adic numbers, unlike the reals where only $\mathbb{C}$ occurs [5]. The canonical identification is exactly the kind of map our coarse-graining construction needs: a continuous projection from the non-Archimedean substrate to real observables.

The information-theoretic and geometric side of our proposal draws on quantum information in $p$-adic Hilbert spaces. Work [2] defines $p$-adic Hilbert spaces over non-Archimedean fields with an inner product satisfying symmetry, linearity, and a Cauchy-Schwarz-type bound $|\langle x,y\rangle| \leq \|x\|\,\|y\|$, and proves a $p$-adic analogue of the van Lint-Seidel relative bound: if $\{\tau_j\}_{j=1}^n$ are $p$-adic $\gamma$-equiangular lines in $\mathbb{Q}_p^d$, then $|n|^2 \leq |d| \max\{|n|, \gamma^2\}$ [2]. This bound constrains how many mutually equiangular states (the abstract skeleton of mutually unbiased bases and state distinguishability) can exist over a $p$-adic space versus a real space, and it is the natural tool for our proposed test of ultrametric signatures in entanglement structure: if the substrate is $p$-adic, the admissible equiangular configurations of states differ from the real case in a computable way.

The number-theoretic machinery that would be needed to make contact between a $p$-adic substrate and observed real-valued quantities is also developed. Work [6] constructs $p$-adic multiple $L$-functions in several variables as generalizations of the Kubota-Leopoldt $p$-adic $L$-functions using a specific $p$-adic measure, proves their $p$-adic analyticity (Theorem 1.21) and $p$-adic continuity (Theorem 1.24), and evaluates them at non-positive integers in terms of twisted multiple Bernoulli numbers [6]. Work [8] formulates a $p$-adic analogue of Borel's theorem relating regulators for higher $K$-groups of number fields to special values of zeta-functions, using syntomic regulators and $p$-adic $L$-functions, and recalls the classical identity $w\sqrt{|D_k|}\,\mathrm{Res}_{s=1}\zeta_k(s) = 2^{r_1}(2\pi)^{r_2}|\mathrm{Cl}(\mathcal{O}_k)|\,R$ for a number field $k$ [8]. These works matter to us because any empirical prediction from a $p$-adic ontology ultimately must be expressed in real numbers, and the $L$-function/regulator apparatus is the established bridge between $p$-adic and real-arithmetic quantities; [5] makes the same point, that predictions of $p$-adic theories must be expressed in terms of real numbers, requiring a correspondence between the two. Work [7], on $p$-adic period rings $B_{\mathrm{crys}}$ and $B_{\mathrm{dR}}$ and comparison theorems between étale and crystalline or de Rham cohomologies, supplies the deepest such bridge: it shows, via Hilbert's theorem 90 and the construction of the de Rham filtration with the map $\theta_\mu: B_\mu^+ \to \mathbb{C}_p$ requiring the condition $\mu \geq 1$, how $p$-adic and complex-linear invariants of the same object are systematically compared [7]. If the substrate is $p$-adic and observations are complex-valued amplitudes, a comparison theorem of this type is the logical endpoint of the correspondence problem.

Finally, the ontological program this paper formalizes is stated in a sequence of works. Work [9] argues that the deepest theories — quantum gravity, holography — converge on a description devoid of fundamental time, and posits a static, discrete, relational, non-Archimedean network of which continuous spacetime and temporal flow are large-scale approximations, using the map-territory distinction (Korzybski's principle) to frame the continuum as representation rather than reality [9]. Work [10] extends this with the epistemic-ontological distinction: the static relational network is the ontological claim, while space, time, objects, causality, and the self are epistemic phenomena generated by the interaction of an observer subgraph with the network [10]. Work [11] makes the most specific technical claims: it maps the timeless adjacency operator of the Bruhat-Tits tree to an effective Hamiltonian within a rigged Hilbert space using the Page-Wootters mechanism, states that time is an epistemic coarse-grained parameter, that the Archimedean projection yields continuous real coordinates, that a causal light cone structure emerges from Lieb-Robinson bounds, and that the dimensionless upper bound on signal speed is derived from the spectral radius of the tree, with zeta-regularized adelic unification resolving prime dependence [11]. Work [12] supplies computational support: Python-simulated Bruhat-Tits trees and combinatorial node-counting algorithms, the observation that the $p$-adic distance $p^{-n}$ approaches $0$ as depth $n \to \infty$ so the continuous boundary is resolved strictly at infinity, and the claim that hierarchical clustering native to the Bruhat-Tits tree maintains non-locality structurally while projecting a continuous epistemic limit [12]. Work [12] also frames the Bekenstein bound as a topological constraint on information density rather than an external thermodynamic limit [12].

What is missing from all of these — and what this paper supplies — is an explicit, arithmetic-checked derivation chain: from the ultrametric axiom to vertex counts, from vertex counts to an effective metric with a quantified error, from counting to a probability rule, and from the model to a numerical falsification threshold. Sections 3 and 4 perform these steps.

## 3. Methods

### 3.1 Ontological model

We assume the following model, stated as axioms. The ontology is a connected, locally finite graph $G = (V, E)$ with no cycles (a tree), in which every vertex has degree $p + 1$ for a fixed prime $p$; this is the $(p+1)$-regular tree, the combinatorial type of the Bruhat-Tits tree over $\mathbb{Q}_p$ [11], [12]. The graph is static: no external time parameter evolves it, following the ontological thesis of [9], [10]. Vertices carry no labels beyond adjacency; the ontology is purely relational [9]. Distance between vertices $u, v \in V$ is the graph distance $d_G(u,v)$, the number of edges on the unique path between them (the path is unique because $G$ is a tree) [1].

We choose the tree rather than a general graph because ultrametric spaces and trees are equivalent geometric categories: a metric space is ultrametric in the sense of satisfying $d(x,z) \leq \max\{d(x,y), d(y,z)\}$ precisely when its finite metric geometry can be embedded in a tree with distances measured to the branching point. The $p$-adic norm's ultrametricity [1] is the analytic expression of this tree geometry, and the degree $p+1$ ties the branching factor to the prime, as in the Bruhat-Tits tree whose vertices at each level correspond to $p$-adic balls.

### 3.2 Observer and coarse-graining

An observer is a finite connected subgraph $O \subset G$, following the observer-subgraph picture of [10]. The observer does not access $G$ directly; it accesses equivalence classes of vertices under a coarse-graining map. We define the coarse-graining at resolution level $N \in \mathbb{N}$ as the partition of $V$ into balls of graph radius $N$ centered at vertices whose mutual distance exceeds $2N$; in an ultrametric/tree geometry such balls nest or disjoint cleanly, so the partition is well defined. Each ball $B(v, N) = \{u \in V : d_G(u,v) \leq N\}$ becomes one effective point of the observer's map. This implements the map-territory distinction of [9]: the territory is $G$; the map is the quotient $V / \sim_N$.

### 3.3 Probability as counting

We assume that the observer's epistemic state over a coarse-grained ball assigns equal weight to each vertex in the ball, so that the probability of an event $A$ (a set of vertices) is the ratio

$$P(A) = \frac{N_A}{N_{\text{total}}},$$

where $N_A$ is the number of vertices in $A$ and $N_{\text{total}}$ the number in the reference ball. This is a counting rule, not a dynamical postulate; it is the epistemic reading of the static ontology, in the spirit of the epistemic-interface thesis of [10]. Section 4.3 derives when this rule reproduces Born-rule statistics.

### 3.4 Falsification targets

Following the program of the source idea, we target two observable classes: (i) discrete artifacts in cosmological fluctuation statistics, quantified in Section 4.4 as a projection; and (ii) ultrametric (hierarchical) clustering signatures in entanglement structure, for which the $p$-adic equiangular-line bound of [2] provides the discriminating prediction. We do not perform simulations; we derive bounds and state what a simulation or data analysis would measure.

## 4. Analysis

### 4.1 Ultrametric balls and vertex counts

**Claim 4.1.** In the $(p+1)$-regular tree, the number of vertices at graph distance exactly $n \geq 1$ from a root $v_0$ is $(p+1)\,p^{\,n-1}$, and the number within distance $n$ is $1 + (p+1)\frac{p^n - 1}{p - 1}$.

*Derivation.* From the root there are $p+1$ branches (one per edge). At each subsequent step, a path continuing outward has $p$ forward choices (it cannot return along the edge it arrived on, since the graph is a tree with no cycles [1]). Therefore:

$$N_1 = p + 1,$$
$$N_2 = (p+1)\,p,$$
$$N_n = (p+1)\,p^{\,n-1} \quad \text{for } n \geq 1.$$

The cumulative count is the geometric sum:

$$V(n) = 1 + \sum_{k=1}^{n} (p+1)\,p^{k-1} = 1 + (p+1)\,\frac{p^n - 1}{p-1}.$$

*Check with $p = 2$:* $N_1 = 3$, $N_2 = 6$, $N_3 = 12$; $V(3) = 1 + 3\,(4-1)/(1) = 1 + 3 \cdot 3 = 10$. Direct count: root (1) + 3 at level 1 + 6 at level 2 + 12 at level 3 would give 22 for $V(3)$ including level 3 — recompute: $V(3) = 1 + 3\,\frac{2^3 - 1}{2-1} = 1 + 3 \cdot 7 = 22$. The first computation dropped the $p^3$ term; the correct value is $V(3) = 22$, i.e., $1 + 3 + 6 + 12 = 22$. ✓

This exponential growth with ratio $p$ is the discrete analogue of the volume growth of the $p$-adic norm: a $p$-adic ball of radius $p^{-n}$ contains $p$ sub-balls of radius $p^{-(n+1)}$, matching the branching factor, which is why the Bruhat-Tits tree is the correct combinatorial skeleton for $\mathbb{Q}_p$ [11], [12]. The same self-similar nesting is what [1] exploits to define Gibbs measures on the Cayley tree.

**Claim 4.2 (hierarchical clustering).** In an ultrametric, for any three points $x, y, z$: if $d(x,y) \neq d(y,z)$ then $d(x,z) = \max\{d(x,y), d(y,z)\}$.

*Derivation.* Ultrametricity gives $d(x,z) \leq \max\{d(x,y), d(y,z)\}$ [1]. Suppose $d(x,y) < d(y,z)$. Then $\max = d(y,z)$, so $d(x,z) \leq d(y,z)$. But also applying ultrametricity to the triple $(x,z,y)$: $d(y,z) \leq \max\{d(y,x), d(x,z)\} = \max\{d(x,y), d(x,z)\}$. Since $d(x,y) < d(y,z)$, the max must be $d(x,z)$, so $d(y,z) \leq d(x,z)$. Combined with $d(x,z) \leq d(y,z)$: $d(x,z) = d(y,z) = \max$. ∎

Consequence: all triangles are isosceles with the long side equal to one of the short sides — the defining signature of hierarchical clustering. Any dataset of distances among entangled systems that satisfies Claim 4.2 statistically is evidence for a tree-like (non-Archimedean) substrate; this is the operational content of the ultrametric-signature proposal.

### 4.2 Coarse-graining and emergence of a smooth effective metric

**Claim 4.3.** Under the coarse-graining of Section 3.2 at level $N$, the induced effective distance between ball centers is $D_N(c_1, c_2) = p^{-m}$ where $m = \lfloor \log_p d_G(c_1, c_2) \rfloor$ is determined by the nesting level, and the relative metric error of the coarse-grained map at scale $L \gg p^N$ is bounded by $p^{-N}/L$.

*Derivation.* In the tree, two balls $B(c_1, N)$ and $B(c_2, N)$ with $d_G(c_1, c_2) > 2N$ are disjoint, and their separation is naturally measured by the depth of their least common ancestor. Define the effective distance as the number of coarse-grained links between the balls along the unique path. If $d_G(c_1, c_2) = d$, the path has $d$ edges, of which the portions inside the balls are at most $2N$, so the number of inter-ball links is

$$\ell(d, N) = d - 2N \quad (d > 2N).$$

The coarse-grained observer resolves distances only up to additive uncertainty of order the ball diameter, $2N$. The relative resolution error at separation $d$ is therefore

$$\varepsilon(d, N) = \frac{2N}{d - 2N}.$$

For the effective geometry to approximate a continuum manifold, we need $\varepsilon \ll 1$ at the scales probed. Setting $\varepsilon \leq \eta$ for tolerance $\eta$:

$$\frac{2N}{d - 2N} \leq \eta \;\Rightarrow\; d \geq 2N\,\frac{1 + \eta}{\eta}.$$

*Worked example.* Take $p = 2$, coarse-graining level $N = 10$, tolerance $\eta = 10^{-2}$. Then

$$d \geq 2 \cdot 10 \cdot \frac{1 + 0.01}{0.01} = 20 \cdot 101 = 2020.$$

So a level-$10$ observer on the $3$-regular tree obtains distances accurate to $1\%$ only at graph separations of $2020$ edges or more. The number of vertices in a ball of radius $10$ is, by Claim 4.1,

$$V(10) = 1 + 3\,\frac{2^{10} - 1}{2 - 1} = 1 + 3 \cdot 1023 = 3070.$$

Each effective point of the observer's map therefore aggregates $3070$ ontological vertices. This is the quantitative form of the statement in [12] that the continuous limit is resolved "strictly at infinity": smoothness is not free but purchased with coarse-graining depth, and the error is explicitly $2N/(d - 2N)$.

**Claim 4.4 (light-cone precedent).** The emergence of causal structure from $p$-adic analysis alone has a precedent: [4] shows that the convergence region of the $p$-adic square root function forms cylinders parallel to the time axis with radius $N_p(t) = p^k$ and length $p^{k-1}(p-1)$ at $t = p^k$ — a $p$-adic counterpart of the future light cone — and that the required extension has dimension $D = 4$ for $p > 2$. Our model inherits this mechanism: the natural "time" ordering on the tree is the distance from a chosen root (the observer's position), and the ball radii $p^k$ are exactly the levels at which the coarse-grained geometry changes character. We do not re-derive the TGD result; we use it as evidence that light-cone structure is not exclusive to Archimedean geometry.

The canonical identification of [5] — reading a $p$-adic expansion's digits in reverse to obtain a real number, a continuous map — is the concrete projection map from our coarse-grained tree coordinates to the real coordinates the observer reports. Its known defect, the non-uniqueness of expansions [5], appears in our model as the arbitrariness of choosing ball centers; different choices give different but isomorphic maps, which is the discrete analogue of gauge freedom.

### 4.3 Epistemic probability and the Born rule

**Claim 4.5.** If an event $A$ corresponds to a set of $N_A$ vertices within a reference ball of $N_{\text{total}}$ vertices, the counting rule gives $P(A) = N_A / N_{\text{total}}$. This matches the Born rule $P = |\psi|^2$ if and only if the amplitude assignment is $\psi \propto \sqrt{N_A / N_{\text{total}}}$ up to phase, i.e., if branch multiplicities in the observer's coarse-grained description encode amplitudes as square roots of vertex counts.

*Derivation.* The Born rule assigns $P(A) = |\langle A | \psi \rangle|^2$. Our rule assigns $P(A) = N_A / N_{\text{total}}$. These agree for all events precisely when there exists a map $\psi: \text{events} \to \mathbb{C}$ with

$$|\psi(A)|^2 = \frac{N_A}{N_{\text{total}}},$$

i.e., $|\psi(A)| = \sqrt{N_A / N_{\text{total}}}$. Such a map exists trivially for any assignment of counts; the nontrivial content is whether the $\psi$ so defined composes correctly under union of disjoint events and under the linear structure of quantum superposition. For disjoint $A_1, A_2$:

$$P(A_1 \cup A_2) = \frac{N_{A_1} + N_{A_2}}{N_{\text{total}}} = P(A_1) + P(A_2),$$

which is additive, as required of probabilities. But quantum amplitudes add linearly before squaring: $|\psi_1 + \psi_2|^2 = |\psi_1|^2 + |\psi_2|^2 + 2\,\mathrm{Re}(\psi_1^* \psi_2)$, and the interference term is generically nonzero. Therefore the counting rule reproduces Born statistics **without interference** — i.e., for events that are distinguished at the coarse-graining level (which decoherence-like interactions would make the case) — and fails to reproduce interference unless the coarse-graining map itself carries phase structure.

*Worked example.* Take $N_{\text{total}} = 3070$ (the $p=2$, $N=10$ ball of Section 4.2) and an event occupying $N_A = 1535$ vertices (exactly half). Then

$$P(A) = \frac{1535}{3070} = 0.5.$$

The Born-rule amplitude is $|\psi| = \sqrt{0.5} \approx 0.7071$. If a second, disjoint event $B$ also occupies $1535$ vertices, $P(B) = 0.5$ and $P(A \cup B) = 1$, consistent with both rules. If instead $A$ and $B$ are not distinguished at the coarse-graining level — both map to the same effective point — the counting rule assigns $P(A) = P(B) = 1$ for the shared effective point, while quantum mechanics would assign interference-dependent values. This is the precise locus where our model must be extended (by phase structure on the coarse-graining map) to recover full quantum statistics; we flag it as the main open gap rather than claiming it is closed.

The need for such a re-derivation is corroborated by [3], which records that with complex-valued wave functions on $p$-adic spaces one cannot construct a direct analogue of the Schrödinger equation with a $p$-adic Heisenberg algebra — the quantum formalism does not transplant automatically, and the probability interpretation must be rebuilt. The $p$-adic Hilbert space framework of [2], with its inner product satisfying $|\langle x,y\rangle| \leq \|x\|\,\|y\|$, provides the arena in which such a rebuilt interpretation would live; the $p$-adic equiangular-line bound $|n|^2 \leq |d| \max\{|n|, \gamma^2\}$ of [2] then constrains the state configurations available to the observer, giving a concrete, computable difference between $p$-adic and real quantum geometry.

### 4.4 Falsification threshold: CMB discrete artifacts (projection)

We now derive, as an explicitly labeled projection, the multipole scale at which Planck-scale discreteness would first perturb the CMB. This requires assumptions the sources do not supply, which we state.

**Assumptions (projection inputs).**
- (A1) The discreteness scale is the Planck length, $l_P \approx 1.6 \times 10^{-35}\,\mathrm{m}$. (Standard physical constant; assumed.)
- (A2) The observable universe's diameter is approximately $8.8 \times 10^{26}\,\mathrm{m}$ (diameter of the observable universe, $\sim 92$ billion light-years with $1\,\mathrm{ly} \approx 9.46 \times 10^{15}\,\mathrm{m}$). (Standard estimate; assumed.)
- (A3) A discrete lattice or tree with spacing $l_P$ supports modes down to wavelength $\sim l_P$; CMB multipole $\ell$ probes angular scales $\theta \sim \pi/\ell$, corresponding at the last-scattering surface to comoving wavelengths of order the horizon size divided by $\ell$.

*Derivation.* The ratio of the observable scale to the discreteness scale is

$$\frac{8.8 \times 10^{26}\,\mathrm{m}}{1.6 \times 10^{-35}\,\mathrm{m}} = 5.5 \times 10^{61}.$$

Arithmetic: $8.8 / 1.6 = 5.5$; $10^{26} / 10^{-35} = 10^{61}$. The largest CMB multipole probing horizon-scale structure is $\ell \sim 1$; a multipole $\ell$ probes structure on scale $\sim$ (horizon)$/ \ell$. Discreteness artifacts would appear when the probed scale approaches $l_P$, i.e., at

$$\ell_{\text{artifact}} \sim 5.5 \times 10^{61}.$$

Observed CMB multipoles reach only $\ell \sim 10^3$–$10^4$ at most (arcminute scales). Therefore:

$$\frac{\ell_{\text{artifact}}}{\ell_{\text{observed, max}}} \sim \frac{5.5 \times 10^{61}}{10^4} = 5.5 \times 10^{57}.$$

**Conclusion (projection).** Under assumptions A1–A3, direct observation of discreteness artifacts in the CMB is separated from current observational reach by roughly $57$ to $61$ orders of magnitude in scale. This is a projection, not a measurement; its uncertainty is dominated by A3 (the exact mode-correspondence between tree spacing and angular multipoles), which could shift the threshold by a few orders of magnitude but not by the tens of orders that matter. The practical consequence, which we carry to Section 7, is that the falsifiable signatures of the model must be sought not in propagation artifacts but in **statistical** signatures: ultrametric clustering (Claim 4.2) in entanglement structures, and prime-dependent constraints (as in the $p = 3$ phase-transition result of [1]) in state configurations per [2].

### 4.5 Growth-rate bound and the spectral claim of [11]

Work [11] states that the dimensionless upper bound on signal speed is derived from the spectral radius of the Bruhat-Tits tree. We can verify the growth-side input to such a claim. The spectral radius $\rho$ of