# Emergent Minkowski Spacetime from Bruhat–Tits Tree Forests: Boundary Geometry, Causal Order, and the Scaling-Limit Problem

## Abstract

Deriving the dimensionality and Lorentzian signature of spacetime from non-geometric, combinatorial data remains an unsolved problem in quantum gravity, and existing programmes either postulate a background or recover spacetime only through dynamics whose continuum limit is not controlled. This paper formalizes a specific conjecture: that a product of $D$ Bruhat–Tits trees $T_{p_i}$, with one tree's directed edges supplying a causal order, admits a scaling limit isometric to $(D-1,1)$-dimensional Minkowski spacetime, and that consistency conditions could single out $D=10$ or $11$. We construct the product boundary $\partial F = \prod_i \mathbb{P}^1(\mathbb{Q}_{p_i})$, compute its combinatorial and metric data explicitly, and prove at the level of covering arithmetic that the product boundary carries a well-defined covering dimension $D$ and a natural causal partial order whose forward cones contain exactly $p^n$ directed geodesic branches at depth $n$. We derive the scaling-limit obstruction quantitatively: the relative resolution between adjacent levels is $1/p$, so the $p \to \infty$ limit is required for any Archimedean-like continuum, and we show this limit is singular for every fixed finite $p$. The principal computed results are the vertex, boundary-cell, and cone-count formulas with worked values (e.g., $3070$ vertices to depth $10$ for $p=2$; cone size $1024$ at depth $10$), the covering-dimension identity $\dim = D$, and the level-resolution ratio $1/p$. The dimension-selection step ($D=10$ versus any other $D$) is shown to be unresolved; we state what computation would falsify the conjecture.

## 1. Introduction

Theoretical physicists who build quantum-gravity theories face a decision that no current framework resolves from first principles: how many spacetime dimensions the fundamental theory should have, and why the low-energy world is Lorentzian rather than Euclidean or ultrametric. String theory answers by consistency (anomaly cancellation fixes the critical dimension), but it does so against a fixed, background Minkowski or curved spacetime that is inserted by hand; loop quantum gravity takes spacetime to be dynamical but must then explain how classical spacetime with its metric re-emerges from non-spatiotemporal quantum structure, a problem analyzed in detail for canonical quantum gravity by [6]. The cost of leaving this unresolved is concrete: without a derivation of dimensionality and signature from pre-geometric data, model builders cannot distinguish fundamental dimensions from compactified artifacts, cannot justify the continuum manifold assumption that produces non-renormalizable ultraviolet divergences when quantized (the tension motivating $p$-adic pre-geometric substrates as described in [8]), and cannot evaluate whether the Archimedean real line — which [10] argues is an inherited mathematical convention rather than an experimental necessity, since every measurement yields a rational number to finite precision — is the correct base field for fundamental physics.

If the conjecture studied here holds, that decision changes. A product of Bruhat–Tits trees — the incidence graphs of lattices over $p$-adic fields, which are purely combinatorial, non-Archimedean objects — would supply a background-independent lattice on which spacetime dimension, Lorentzian signature, and the light-cone structure all emerge from tree combinatorics and a scaling limit, with extra trees interpretable as compactified dimensions. The organizing principle would be the adelic one advocated in [7] and [10]: by Ostrowski's theorem, the completions of $\mathbb{Q}$ comprise the real place and the $p$-adic places, and a non-anthropocentric physics should treat all places as candidate building blocks rather than privileging $\mathbb{R}$.

This paper does not prove the conjecture. It does something prior and necessary: it constructs the objects precisely, derives every quantity that the tree combinatorics fixes uniquely, identifies exactly where the derivation of Lorentzian signature and of the critical dimension $D=10$ or $11$ currently fails, and states the falsification conditions. The contributions are:

- A construction of the forest product and its boundary $\partial F = \prod_i \mathbb{P}^1(\mathbb{Q}_{p_i})$, with explicit vertex-count, boundary-cell, and Haar-measure formulas and worked numerical values (Section 4, Sections 4.1–4.3).
- A proof by covering arithmetic that the product boundary has covering dimension exactly $D$ in the tree (ultrametric) metric, and a derivation of the causal partial order from one tree's directed edges with exact forward-cone counts $p^n$ at depth $n$ (Section 4, Sections 4.4–4.5).
- A quantitative statement of the scaling-limit obstruction: the adjacent-level resolution ratio $1/p$ and the singularity of the $p \to \infty$ limit for fixed finite $p$, which is the precise point where the derivation of an Archimedean Lorentzian metric currently breaks (Section 4, Section 4.6).
- A falsification analysis: which computation, if it returned a particular answer, would refute the emergent-Minkowski claim (Section 6).

## 2. Background and Related Work

This section positions the conjecture against eight bodies of work, citing each for specific results its full text states.

**Lorentzian geometry from observer data.** [1] studies accelerated observers in Minkowski spacetime and the controversial definition of rigid motion; its §II writes the Frenet–Serret equations for a worldline $x^{\mu}(s)$ with curvatures $k_1, k_2, k_3$, and its §III.1 expresses the metric tensor in an accelerated observer's proper coordinate system in terms of those curvatures. The relevance is structural: Minkowski spacetime is characterized not only by its isometry group but by what observer-carried data (a curve and its curvatures) suffice to reconstruct the metric. An emergent-spacetime programme must reproduce this reconstruction property in the continuum limit; if the forest limit yields a metric that cannot be written in a Frenet–Serret-like curvature form for accelerated worldlines, the limit is not Minkowski. We use [1] as the target characterization of the claimed limit.

**Non-Archimedean balls and packing.** [2] investigates lattice packings of Minkowski balls and domains in the Banach spaces $\mathbb{B}^2_p$ with norms $|x|^p + |y|^p$, dividing domains into Minkowski, Davis, and Chebyshev–Cohn classes by the value of $p$ relative to a threshold $p_0$, and — importantly for us — studies direct systems of Minkowski domains and critical lattices under doubling maps, $\mathbb{B}^2_p \ni D_p \to 2D_p \to 2^2 D_p \to \cdots$, whose limits are analyzed as direct-system limits. This is the closest existing template for our scaling limit: [2] treats a continuum-relevant limit of non-Archimedean-adjacent objects as a direct system with explicit structure maps, and its classification of behavior by $p$-ranges shows that qualitative geometry can change discontinuously with the prime. Our $p \to \infty$ analysis inherits this lesson: properties of the forest boundary need not converge monotonically in $p$.

**$p$-adic fractal strings and boundary geometry.** [3] develops the local theory of complex dimensions for $p$-adic fractal strings. Its §2.1 defines the $p$-adic absolute value $|x|_p = p^{-v}$ for $x = p^v a/b$ and the strong triangle inequality $|x+y|_p \le \max\{|x|_p, |y|_p\}$, and its §2.2 decomposes any bounded open $\Omega \subseteq \mathbb{Q}_p$ canonically into disjoint balls $B(a_j, p^{-n_j}) = a_j + p^{n_j}\mathbb{Z}_p$. The paper obtains explicit tube formulas for tubular neighborhoods of $p$-adic fractal strings in terms of complex dimensions, with geometric oscillations visible in the volume formula. This supplies the exact geometric toolkit for our boundary $\mathbb{P}^1(\mathbb{Q}_p)$: the boundary of the Bruhat–Tits tree is a Cantor-like set whose cylinder decomposition is precisely the ball decomposition of [3] §2.2, and whose Minkowski dimension is computable by the same covering arithmetic that [3] applies to fractal strings. Our Section 4.3 covering count is the tree-side counterpart of [3]'s tube analysis.

**Strings in curved backgrounds and consistency.** [4] surveys classical and quantum string propagation in black-hole and cosmological spacetimes. Its §2 gives the $2+1$ BH-AdS metric of Bañados et al. with horizons $r_{\pm} = \sqrt{\tfrac{Ml^2}{2} \pm \tfrac{l}{2}\sqrt{M^2 l^2 - J^2}}$, and its §6 concludes that classical string motion in anti de Sitter spacetime is stable (oscillatory with real frequencies, bounded size and energy, well-defined mass operator for any wave number $n$), in contrast with de Sitter spacetime where string size and energy become unbounded for large de Sitter radius. This stability contrast is the concrete face of the consistency conditions our conjecture invokes: a candidate emergent background must support a well-defined, stable string spectrum, and [4] shows that this property already discriminates sharply between backgrounds that look superficially similar. Any $D$ selected by forest consistency must pass the [4]-type test in the resulting background.

**Tree formalisms and derivation structure.** [5] defines feature-based regular tree grammars and a translation from feature-based tree adjoining grammars that preserves derivation structures; its §2 encodes the derivation trees of a TAG as the language of a regular tree grammar, and its §5 notes that derivation-tree languages, being regular, are far simpler to manipulate than derived-tree languages, enabling reachability computations between elementary trees. The methodological transfer is direct: our forest is a set of trees with a composition structure (gluing trees into a forest, taking products, quotienting by automorphisms), and [5] demonstrates that keeping the derivation (combinatorial) tree as the primary object — rather than the "derived" geometric object — makes reachability and consistency checks decidable. Our consistency conditions (Section 3) are analogously posed on the combinatorial side.

**The emergence problem in quantum gravity.** [6] investigates how spacetime is lost and regained in approaches that take the fundamental structure to be non-spatiotemporal. Its §2.1 explains that LQG recasts GR as a Hamiltonian system with constraints, forcing a foliation into $(3+1)$ dimensions with a dynamical three-space evolving in time, and its §5 concludes that the project of analyzing the emergence of spacetime from quantum theories of gravity addresses foundational questions about inter-theory relations necessary for progress. Our conjecture is a specific instance of the programme [6] describes — regaining classical spacetime from non-spatiotemporal structure — with the difference that our fundamental structure is ultrametric-combinatorial rather than quantum-geometric, and our emergence mechanism is a metric scaling limit rather than semiclassical decoherence.

**The adelic organizing principle.** [7] proposes refactoring fundamental physics around invariant patterns under transformations, arguing in its §3.1 via Ostrowski's theorem that the ways of completing $\mathbb{Q}$ are exhaustively classified — the real place and the $p$-adic places — so that "the real numbers are not special; they are the Archimedean place among an infinite family of non-Archimedean, ultrametric completions," and that a non-anthropocentric physics would formulate laws invariantly across all completions. Its §9 concludes with a framework making falsifiable predictions (modified photon dispersion at the Planck scale, log-periodic oscillations in the dark matter power spectrum, anomalous black hole echo timings). Our forest conjecture supplies the geometric substrate that [7]'s invariant-pattern thesis motivates but does not construct: the trees are the non-Archimedean places made into geometry.

**Computational realization.** [8] develops and validates a computational toolkit for $p$-adic spacetime theories based on the Bruhat–Tits tree, presenting Python-based methods including graph Laplacian generators for $p$-adic lattices, properly weighted Monte Carlo algorithms for thermodynamic relaxation on trees, and a $p$-adic wavelet transform for boundary data; its §7.1 reports that a discrete Wheeler–DeWitt equation converged, that emergent time was mapped via thermodynamic RG flow, and that wavelet analysis of mock CMB data yielded detection of $p$-adic scaling symmetries. This matters to us in two ways: it establishes that the Bruhat–Tits tree substrate is computationally tractable with existing methods, and its boundary-data wavelet pipeline is exactly the instrument our Section 7 proposes for the first falsification test on the forest boundary.

**Epistemological framing.** [9] argues that human understanding operates through representational models rather than direct apprehension, that cognitive frameworks are compression heuristics, and (its §1.3) that self-reference is a structural condition of inquiry, formalized by Gödel's incompleteness theorems. We invoke this only for a methodological caution that bears on our falsification analysis: the continuum Minkowski spacetime we aim to recover is itself a representational model, and the scaling limit must be characterized by intrinsic, checkable properties (dimension, signature, cone structure) rather than by resemblance.

**The base-field question.** [10] argues that the choice of $\mathbb{R}$ as the base field of physics is an unjustified assumption: its §2.1 states that there is no experimental measurement distinguishing a real number from a rational approximation, that every simulation operates on finite-precision rationals, and its §3.1 states Ostrowski's theorem as a proven result anchoring the claim that $\mathbb{R}$ and every $\mathbb{Q}_p$ are equally legitimate completions, so "physics has arbitrarily restricted itself to the $\infty$-place." Our conjecture takes the $p$-adic completions as fundamental and the real continuum as the limit to be derived, which is the geometric inversion of the situation [10] describes.

## 3. Methods

**Objects.** Fix distinct primes $p_1, \dots, p_D$. For each $p_i$, let $T_{p_i}$ denote the Bruhat–Tits tree of $\mathrm{PGL}_2(\mathbb{Q}_{p_i})$: the infinite $(p_i+1)$-regular tree whose vertices are homothety classes of $\mathbb{Z}_{p_i}$-lattices in $\mathbb{Q}_{p_i}^2$ and whose edges join classes differing by a single reduction step. The forest is the disjoint union $F = \bigsqcup_{i=1}^{D} T_{p_i}$; the forest product is the Cartesian product of vertex sets with the product of path-distance metrics. The boundary of each tree is $\partial T_{p_i} \cong \mathbb{P}^1(\mathbb{Q}_{p_i})$, the set of ends (infinite geodesic rays from a chosen root), and the product boundary is

$$\partial F = \prod_{i=1}^{D} \mathbb{P}^1(\mathbb{Q}_{p_i}).$$

**Causal order.** Choose one tree, $T_{p_1}$, and a root $o_1$. Orient every edge of $T_{p_1}$ away from $o_1$; this orients $\partial T_{p_1}$ as a total order compatible with the tree's end structure and induces the directed-edge causal order on the forest: for boundary points $x = (x_1, \dots, x_D)$ and $y = (y_1, \dots, y_D)$, define $y \succeq x$ iff the directed path structure of $T_{p_1}$ places $y_1$ in the forward (away-from-root) direction of $x_1$. The remaining $D-1$ coordinates are spatial. This is the conjecture's mechanism for generating signature $(D-1,1)$: one tree contributes time, the rest contribute space.

**Metrics.** On $\partial T_{p_i}$ fix the visual metric $d_i$ normalized so that a cylinder (the set of ends passing through a given vertex at depth $n$) has diameter $p_i^{-n}$; this is the standard visual metric and matches the ball radii $p^{-n_j}$ of the canonical ball decomposition in [3] §2.2. The product metric is $d(x,y) = \max_i d_i(x_i, y_i)$.

**Consistency conditions.** The conjecture's selection mechanism for $D$ is posed as three conditions on the scaling limit: (i) anomaly cancellation for string amplitudes computed as adelic integrals over $\partial F$; (ii) a supersymmetric continuum limit; (iii) gauge symmetry from the automorphism groups of the compact-tree products, whose root lattices should match string-theory gauge groups. These conditions are stated, not solved; Section 4 derives what the combinatorics fixes and Section 6 analyzes what remains.

**Scaling limit.** The continuum limit is taken as $p_i \to \infty$ (or by prime mixing, i.e., simultaneous refinement across several primes), with the level depth $n$ scaled so that the cylinder diameter $p^{-n}$ tends to zero. The claim to be tested is that the metric completion of $(\partial F, d)$ together with the causal order $\succeq$ is isometric to $(D-1,1)$-Minkowski spacetime with its standard causal order.

## 4. Analysis

All inputs in this section are structural (tree regularity, the visual-metric normalization of Section 3, and the $p$-adic absolute value $|x|_p = p^{-v}$ of [3] §2.1); no empirical data are used. Every number below is computed from these inputs with the arithmetic shown.

### 4.1 Vertex counts

By construction, $T_p$ is $(p+1)$-regular: the root $o$ has $p+1$ neighbors, and every other vertex has $p$ neighbors not one step closer to the root. Therefore the number of vertices at depth $n \ge 1$ is

$$N_n = (p+1)\,p^{\,n-1},$$

since each of the $p+1$ depth-$1$ vertices heads a subtree in which every vertex has exactly $p$ forward children, giving $p^{\,n-1}$ vertices at depth $n$ per branch. The total number of vertices up to depth $n$ is

$$V_n = 1 + \sum_{k=1}^{n} (p+1)p^{k-1} = 1 + (p+1)\,\frac{p^{n}-1}{p-1}.$$

Worked values. For $p=2$, $n=10$:

$$V_{10} = 1 + 3 \cdot \frac{2^{10}-1}{2-1} = 1 + 3 \cdot 1023 = 1 + 3069 = 3070.$$

For $p=3$, $n=5$:

$$V_5 = 1 + 4 \cdot \frac{3^5-1}{3-1} = 1 + 4 \cdot \frac{242}{2} = 1 + 4 \cdot 121 = 485.$$

For $p=5$, $n=3$:

$$V_3 = 1 + 6 \cdot \frac{125-1}{4} = 1 + 6 \cdot 31 = 187.$$

These counts are the finite-stage approximants to the boundary; the scaling limit replaces them by the cylinder decomposition of [3] §2.2.

### 4.2 Boundary cells and Haar measure

The set of ends passing through a fixed depth-$n$ vertex is a cylinder of visual diameter $p^{-n}$; under the standard probability measure on $\partial T_p$ (each forward branch at the root carrying weight $1/(p+1)$ and each subsequent branch weight $1/p$, so that the weights sum to $1$), a depth-$n$ cylinder has measure

$$\mu(C) = \frac{1}{p+1} \left(\frac{1}{p}\right)^{n-1}.$$

Check of normalization for $p=2$, $n=1$: there are $N_1 = 3$ cylinders, each of measure $1/3$; total $3 \cdot \tfrac13 = 1$. For $n=2$: $N_2 = 3 \cdot 2 = 6$ cylinders each of measure $\tfrac13 \cdot \tfrac12 = \tfrac16$; total $6 \cdot \tfrac16 = 1$. In general,

$$N_n \cdot \mu(C_n) = (p+1)p^{n-1} \cdot \frac{1}{(p+1)p^{n-1}} = 1,$$

as required. This measure coincides with the Haar measure on $\mathbb{P}^1(\mathbb{Q}_p)$ under the standard identification, for which a ball $a + p^n \mathbb{Z}_p$ (in the affine chart) has measure proportional to $p^{-n}$, matching the ball radii in [3] §2.2.

### 4.3 Covering dimension of the boundary

Cover $\partial T_p$ by its $N_n = (p+1)p^{n-1}$ depth-$n$ cylinders, each of diameter $\delta_n = p^{-n}$. The covering dimension is

$$\dim \partial T_p = \lim_{n \to \infty} \frac{\log N_n}{\log (1/\delta_n)} = \lim_{n \to \infty} \frac{\log\!\big((p+1)p^{n-1}\big)}{n \log p}.$$

Compute the numerator explicitly:

$$\log\!\big((p+1)p^{n-1}\big) = \log(p+1) + (n-1)\log p.$$

Hence

$$\dim \partial T_p = \lim_{n \to \infty} \frac{(n-1)\log p + \log(p+1)}{n \log p} = \lim_{n \to \infty} \left(1 - \frac{1}{n} + \frac{\log(p+1)}{n \log p}\right) = 1.$$

Numerical check for $p=2$, $n=10$: numerator $= 9 \log 2 + \log 3 = 9(0.693147) + 1.098612 = 6.238326 + 1.098612 = 7.336938$; denominator $= 10 \log 2 = 6.931472$; ratio $= 7.336938 / 6.931472 = 1.058487$, already within $5.9\%$ of the limit $1$, and the excess term $\log(3)/(10 \log 2) = 1.098612/6.931472 = 0.158487$ decays as $1/n$.

For the product boundary $\partial F = \prod_{i=1}^{D} \mathbb{P}^1(\mathbb{Q}_{p_i})$ with the max-metric, an $\varepsilon$-cover is obtained by covering each factor at level $n_i$ with $p_i^{-n_i} \le \varepsilon$, i.e., $n_i = \lceil \log_{p_i}(1/\varepsilon) \rceil$. The covering number satisfies

$$N(\varepsilon) = \prod_{i=1}^{D} (p_i+1)\,p_i^{\,n_i - 1}, \qquad \log N(\varepsilon) = \sum_{i=1}^{D} \big(\log(p_i+1) + (n_i-1)\log p_i\big).$$

With $n_i \log p_i = \log(1/\varepsilon) + O(1)$ as $\varepsilon \to 0$, each factor contributes $\log(1/\varepsilon) + O(1)$, so

$$\dim \partial F = \lim_{\varepsilon \to 0} \frac{\log N(\varepsilon)}{\log(1/\varepsilon)} = \frac{D \log(1/\varepsilon) + O(1)}{\log(1/\varepsilon)} = D.$$

This is the first substantive result: the product boundary has covering dimension exactly $D$, one per tree, with no free parameter. The count of coordinates is fixed by combinatorics alone.

### 4.4 Causal cones

Orient $T_{p_1}$ away from its root. The forward cone of the root at depth $n$ consists of all vertices at depth $n$, of which there are $N_n = (p_1+1)p_1^{\,n-1}$. The forward cone of a vertex $v$ at depth $n \ge 1$ consists of the vertices at depth $n+k$ reachable from $v$ without backtracking; since each such vertex has exactly $p_1$ forward children, the cone at depth $n+k$ has exactly

$$|C_k(v)| = p_1^{\,k}$$

vertices. Worked values: $p_1 = 2$, $k = 10$: $|C_{10}| = 2^{10} = 1024$. For $p_1 = 5$, $k=4$: $|C_4| = 5^4 = 625$. For $p_1 = 3$, $k=7$: $|C_7| = 3^7 = 2187$.

The causal order $\succeq$ of Section 3 is the partial order generated by these directed geodesics. Its key structural property, visible directly from the counts, is branching: the forward cone of any event contains $p_1^k$ distinct events at depth $k$, and the backward cone (toward the root) is a chain — each vertex has exactly one parent. Thus the causal structure is a tree order: unique past, exponentially branching future. This is qualitatively Minkowski-like in one respect (the past light cone of an event is a single generator in this model, and the future branches) but quantitatively different from the continuum light cone, whose cross-sections grow polynomially ($k^{D-2}$ in $D$ dimensions from the volume of spheres), not exponentially. We return to this discrepancy in Section 4.6 and Section 6; it is the sharpest quantitative obstruction we derive.

### 4.5 Product measure of spacetime cells

A cell of the product boundary at levels $(n_1, \dots, n_D)$ has product measure

$$\mu(C_{n_1} \times \cdots \times C_{n_D}) = \prod_{i=1}^{D} \frac{1}{(p_i+1)p_i^{\,n_i-1}}.$$

Worked value for $D=4$, all $p_i = 2$, all $n_i = 3$: each factor is $1/(3 \cdot 4) = 1/12$, so the cell measure is $(1/12)^4 = 1/2076 \approx 4.816955 \times 10^{-4}$. For $D=10$, all $p_i = 2$, all $n_i = 3$: $(1/12)^{10} = 12^{-10}$. Compute: $12^2 = 144$, $12^4 = 20736$, $12^5 = 248832$, $12^{10} = 248832