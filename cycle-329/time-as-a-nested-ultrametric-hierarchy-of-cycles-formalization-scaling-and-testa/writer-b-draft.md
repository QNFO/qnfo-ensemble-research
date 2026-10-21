# Time as a Nested Ultrametric Hierarchy of Cycles: A Formal Model and Its Continuum Limit

## Abstract

Physical time is conventionally modeled as a one-dimensional Archimedean continuum, yet every clock actually used in physics—the Compton/Zitterbewegung oscillation, atomic transition frequencies, molecular vibrations, orbital and cosmological periods—is a cycle, and these cycles nest: each longer clock contains very many ticks of the next shorter one. The gap addressed here is that no existing formalism treats this nesting itself as the fundamental structure of time, with the linear continuum as a derived limit. We model time as a rooted tree of nested cycles whose leaf-to-leaf path distances satisfy the ultrametric (strong triangle) inequality, define an ultrametric time distance $d(i,j)=\ln(T_{\mathrm{LCA}}/T_{\mathrm{min}})$, and derive the conditions under which the Archimedean line emerges as the limit of vanishing log-spacing between adjacent cycle levels. Using the electron Compton frequency $\omega_C = 2m_ec^2/\hbar = 1.5527\times10^{21}\ \mathrm{s^{-1}}$ as the base tick and a level ratio fixed by the fine-structure constant $\lambda=\alpha^{-1}=137.036$, we find that approximately $N=9.54$ nesting levels separate the base cycle from a one-second clock, and we derive a conjectural quantum-jump timescale $\tau_{\mathrm{jump}}=\alpha^{-1}\omega_C^{-1}=8.825\times10^{-20}\ \mathrm{s}$. The model recasts mass as tick rate, connects frozen-state hierarchies in constrained quantum dynamics to a temporal ultrametric, and specifies a falsifiable experimental program.

## 1. Introduction

Clockmakers, metrologists, and physicists who build time standards face a structural mismatch that is usually invisible because it is absorbed into convention. The SI second is realized by counting cycles of a cesium hyperfine transition; optical clocks count optical cycles; pulsar timing arrays count rotation periods; cosmology counts Hubble times. Every operational realization of "time" is a count of repetitions of some periodic process, and these periodic processes nest inside one another over at least twenty orders of magnitude of duration. Yet the theory written down on top of these clocks—the time coordinate $t\in\mathbb{R}$ of the Dirac and Schrödinger equations, of general relativity, of statistical mechanics—assumes a smooth, homogeneous, Archimedean line on which any interval can be divided into any number of equal parts. What this costs today is concrete: the measurement-accuracy community must continually certify that successive clock hierarchies (microwave, optical, nuclear) are mutually consistent without a theory of why nested cyclic standards should compose linearly at all; quantum-jump statistics in trapped ions and Rydberg arrays show waiting-time distributions with no first-principles timescale; and quantum-computing engineers must budget error correction against a continuum noise model whose microscopic origin is unknown. If time is fundamentally a nested hierarchy of cycles with ultrametric geometry, then the line is an approximation valid only when cycle durations are densely spaced on a logarithmic axis, mass becomes a tick rate rather than a parameter, and quantum jump durations acquire a predicted scale set by the base cycle and a dimensionless ratio. That would change how clock hierarchies are certified, what a quantum jump duration is expected to be, and which deviations from linear time are worth searching for.

The present work formalizes this conjecture. It is a theory-building paper: no experiment is performed here, and every number is either a derived constant of known physics or an explicitly labeled projection of the model.

The contributions are:

- A formal definition of time as a rooted ultrametric tree of nested cycles, with an explicit ultrametric distance $d(i,j)=\ln(T_{\mathrm{LCA}}/T_{\mathrm{min}})$ and proof that it satisfies the strong triangle inequality (Section 3, Section 4).
- A derivation of the base tick from the electron Compton/Zitterbewegung frequency, $\omega_C=2m_ec^2/\hbar=1.5527\times10^{21}\ \mathrm{s^{-1}}$, with full arithmetic (Section 4).
- A continuum-limit theorem sketch: the Archimedean line is recovered when the log-spacing $\ln\lambda$ between adjacent cycle levels tends to zero, with the level count to macroscopic time computed as $N\approx9.54$ for $\lambda=\alpha^{-1}$ (Section 4).
- A conjectural quantum-jump timescale $\tau_{\mathrm{jump}}=\alpha^{-1}\omega_C^{-1}=8.825\times10^{-20}\ \mathrm{s}$, derived as a projection of the model and connected to frozen-state hierarchies in kinetically constrained quantum dynamics (Sections 4 and 5).
- A falsification program: the observations and calculations that would refute the model, and the smallest next experiment (Sections 6 and 7).

## 2. Background and Related Work

Nested hierarchies and ultrametric geometry appear independently across physics, mathematics, and computation, and each appearance supplies a component the present model needs.

The closest dynamical precedent is the nested hierarchy of frozen states in quantum kinetically constrained models. [1] studies the one-dimensional XPX model $H_{\mathrm{XPX}}=\sum_j\sigma^x_{j-1}(\mathbb{1}-\sigma^z_j)\sigma^x_{j+1}+\Delta\sigma^z_j$ and shows, via a large-coupling expansion $H_{\mathrm{XPX}}=e^{-S}He^{S}$ with $H=H_{\mathrm{F}}+\Delta V$ and $[H_{\mathrm{F}},V]=0$, that classes of computational-basis states remain frozen on timescales $t\sim\Delta^{k}$, where $k$ is the smallest separation between the down-spins that facilitate dynamics. Their Discussion states that regions of space with more widely separated facilitating spins relax exponentially more slowly, and that this exponential dependence on separation emerges in a clean system regardless of integrability. This is precisely the structure a temporal ultrametric predicts—distinct classes of states with relaxation times separated by powers of a control parameter—and Section 4 maps the exponent $k$ onto a tree depth.

Ultrametricity as a consequence of a physical principle rather than an ansatz is established in the spin-glass literature. [5] uses real replicas within the Thouless–Anderson–Palmer construction for the Sherrington–Kirkpatrick model and shows that demanding thermodynamic homogeneity—scale invariance of entropy, $S(E)=k_B\ln\Gamma(E)=k_B/\nu\ln\Gamma(E)^{\nu}$—leads "in a natural way to a thermodynamically dependent ultrametric hierarchy of order parameters." Their conclusion is that real replicas lift the degeneracy of the TAP approach and that the replica-symmetric ansatz is the minimal choice when the internal structure of thermodynamic states is unknown. This supports the present paper's strategy: derive the ultrametric structure from a homogeneity or composition principle applied to time, rather than postulating it.

The geometry of ultrametric trees as moduli spaces is made precise in phylogenetics. [9] defines an ultrametric phylogenetic tree as a finite weighted tree with a distinguished root, leaves at a fixed height $h$, and the property that the leaf distance $d_T(i,j)$ equals twice the height of the most recent common ancestor; the associated metric satisfies the strong triangle inequality $d_T(x,y)\le\max\{d_T(x,z),d_T(y,z)\}$. Their $\sigma$-space generalizes the $\tau$-space parametrization of ranked topologies, of which there are $\prod_{k=2}^{n}\binom{k}{2}=(n-1)!n!/2^{n-1}$ for $n$ taxa. Section 3 adopts exactly this tree-metric correspondence, with cycle durations playing the role of edge weights.

Nested hierarchies of states with level-by-level corrections also arise in exactly solvable disorder problems. [8] derives exact ground-state energy and entropy of the two-dimensional $\pm J$ Ising spin glass through "a nested hierarchy of frustrations," each level contributing through the kernel and pseudo-determinant of effective operators via a Schur complement decomposition $\ln\det(A_n+xB_n(x))=\ln\det(A_n^{11}+xB_n^{11}(x))+\ln\det(xB_n^{00}(x)-x^2B_n^{01}(A_n^{11}+xB_n^{11}(x))^{-1}B_n^{10})$; their numerical results on a $100\times100$ lattice averaged over $10^4$ realizations show energy corrections that stabilize beyond level 1 while entropy decreases systematically with each level. This demonstrates that hierarchical decompositions can be made exact level by level, which is the computational pattern Section 4 uses for the continuum limit.

In numerical analysis, nested hierarchies with simultaneous space–time refinement are the standard machinery for multiscale evolution. [6] presents the CASTRO astrophysical solver, whose adaptive mesh refinement "uses a nested hierarchy of logically-rectangular grids with simultaneous refinement of the grids in both space and time," with subcycling in time so that fine levels take more, shorter steps within one coarse step; the number of levels is bounded by $\ell_{\mathrm{finest}}\le\ell_{\mathrm{max}}$ and can change dynamically. [4] builds a Maxwell solver on "a locally-refined nested hierarchy of rectangular grids," with a fourth-order scheme whose one-step error is $\mathcal{O}(h^5)$ and accumulated error $\mathcal{O}(h^{q-1})$, using $33^3$-node patches with factor-of-four refinement and the same $\Delta t$ across levels. Both works show that evolution equations are routinely integrated on nested time hierarchies; what they do not do is treat the hierarchy itself as time. The present model inverts this: the AMR subcycling structure is promoted from a numerical convenience to the fundamental object.

Hierarchical tree structures also organize cosmological structure. [7] introduces the Tessellation-Level-Tree on the Millennium and Millennium-II simulations, a Voronoi-based structure that "uniquely partitions the simulation particles into disjoint subsets, each associated with a local density peak," with each peak linked to a unique higher peak and characterized by a limiting density $\rho_{\mathrm{lim}}$ set by the saddle-point particle connecting it to its parent. This supplies a worked example of a physically motivated, data-driven nesting tree over twenty-plus orders of magnitude in density, analogous to what the cycle tree claims over duration.

Probabilistic limit theorems for nested fragmentation exist. [10] analyzes an infinite occupancy scheme with boxes organized in a nested hierarchy and random probabilities defined by iterated fragmentation of a unit mass, proving a multivariate functional limit theorem for cumulative occupancy counts as the number of balls grows; in their notation $T_k=-\log P_k$ and the counting functions satisfy $V_j(t)\sim c_jt^{\omega j}$ as $t\to\infty$. The regular asymptotics $V_j(t)\sim c_jt^{\omega j}$ at level $j$ is the statistical-mechanical shadow of the level-counting the present model performs deterministically.

Even in integrable systems, resolving a nested hierarchy is a nontrivial algebraic act. [2] constructs Drinfel'd factorizing twists $R_{12}=F^{-1}_{21}F_{12}$ for rational $sl(n)$ XXX models, obtaining a polarization-free representation of pseudoparticle creation operators that resolves the hierarchy of Bethe vectors; their $F$-matrix for $sl(2)$ is an explicit lower-triangular matrix built from $b(\lambda)=\lambda/(\lambda+\eta)$ and $c(\lambda)=\eta/(\lambda+\eta)$. The lesson taken here is that hierarchies hidden inside standard formalisms can be exposed by a change of representation—exactly what the cycle-tree representation attempts for time.

Finally, the conceptual frame and the conjecture itself come from the QNFO program. [12] argues that "positional notation is inherently an ultrametric tree of nested cycles" and that "the Archimedean line is a derived abstraction," introducing certainty labels that mark its central synthetic claim as the author's own conjecture, and proposes a falsification experiment building a depth-2 tree of 8 transmon qubits connected via coaxial cavities enforcing tree-only gates, compared against a 2D nearest-neighbour layout, with the claim falsified if the tree geometry yields no statistically significant improvement in logical error rate. [13] supplies the methodological warning that physics habitually reifies its mathematical constructs—mistaking "equations, parameters, fields, operators" for elements of physical reality—and argues for experiments that discriminate between competing process models rather than detecting presumed entities; the present paper treats the linear time coordinate as exactly such a reified construct and designs its falsifiers as process discriminations. [14] lists concrete experimental signatures a discrete hierarchical framework would produce, including deviations from standard quantum mechanics at ultra-low energies, anisotropies in the fine-structure constant, discrete-spacetime effects in cosmic-ray events, and modified tunneling rates in mesoscopic devices, and frames the motivation through the resource burden of surface codes with physical-to-logical qubit ratios of roughly 1000:1. [11] contributes a cautionary structural analogy: its shape-preserving shell theorem classifies all radial potentials for which a uniform spherical shell is indistinguishable from a point source up to strength renormalization and radial rescaling, showing that continuum-looking behavior can emerge exactly from an entire admissible family of underlying structures; the Archimedean line may similarly be one point in a family of ultrametric time structures that all look linear at coarse resolution.

## 3. Methods

### 3.1 The cycle tree

We define a **cycle** as a periodic process with a definite duration $T>0$. A **nested cycle system** is a rooted tree $\mathcal{T}$ whose vertices are cycles and whose edges encode containment: an edge from cycle $C_p$ (parent) to cycle $C_c$ (child) means that exactly $n_e$ periods of $C_c$ fit into one period of $C_p$, so

$$T_{C_p} = n_e\, T_{C_c}, \qquad n_e \in \mathbb{N}_{\geq 1}.$$

The root is the longest cycle in the system; the leaves are the shortest. We assume the tree is locally finite and that durations strictly decrease along any path away from the root.

### 3.2 Ultrametric distance

Following the tree-metric correspondence stated in [9], where the leaf distance equals twice the height of the most recent common ancestor, we define for two cycles $i,j$ in $\mathcal{T}$:

$$d(i,j) := \ln\frac{T_{\mathrm{LCA}(i,j)}}{T_{\min}},$$

where $T_{\mathrm{LCA}(i,j)}$ is the duration of the least common ancestor (the smallest cycle containing both $i$ and $j$) and $T_{\min}$ is a fixed reference duration (the shortest cycle in the system). We set $d(i,i)=0$. Section 4 verifies that $d$ satisfies the ultrametric strong triangle inequality.

### 3.3 Regular nesting and the level ratio

The quantitative results require a **regular** nesting: we assume a single branching ratio per level, with each level-$k$ cycle (duration $T_k$) containing exactly $\lambda$ level-$(k-1)$ cycles, so

$$T_k = \lambda\, T_{k-1}, \qquad T_k = T_0\,\lambda^{k},$$

with $T_0$ the base tick. We take $T_0 = T_C$, the electron Compton/Zitterbewegung period, and $\lambda = \alpha^{-1}$, where $\alpha$ is the fine-structure constant. Both choices are assumptions of the model, motivated by the role of the Compton frequency as the fastest known material oscillation and by the appearance of $\alpha^{-1}$ as the characteristic scale ratio in atomic physics; they are stated as assumptions, not derived.

### 3.4 Continuum limit

The Archimedean line is recovered as a limit of the cycle tree when the log-spacing between adjacent levels vanishes. We formalize this as: if the set of available cycle durations becomes dense on the logarithmic axis, i.e. $\ln\lambda \to 0$ with the number of levels per decade $1/\ln\lambda \to \infty$, then sums of ticks over any fixed macroscopic interval converge to the usual linear time integral, and the ultrametric distance $d$ converges to the absolute difference of log-durations, which is a standard embedding of an ultrametric into a line metric. The derivation and its conditions are given in Section 4.

### 3.5 What this paper does and does not do

This paper performs analytical derivation and arithmetic computation only. It runs no simulation, builds no hardware, and reports no measurement. Numbers attributed to other works are cited by reference number; all other numbers are derived in Section 4 from stated inputs or labeled as projections of the model with their assumptions.

## 4. Analysis

### 4.1 The base tick: Compton/Zitterbewegung frequency

**Input numbers.** Electron rest mass $m_e = 9.1093837\times10^{-31}\ \mathrm{kg}$; speed of light $c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$; reduced Planck constant $\hbar = 1.0545718\times10^{-34}\ \mathrm{J\,s}$; fine-structure constant $\alpha^{-1} = 137.035999$ (so $\alpha = 7.297352\times10^{-3}$). These are standard physical constants, stated here as the model's inputs.

The Zitterbewegung angular frequency of a free Dirac particle is the interference frequency between positive- and negative-energy components, $\omega_C = 2m_ec^2/\hbar$. Compute the rest energy:

$$m_ec^2 = 9.1093837\times10^{-31}\ \mathrm{kg} \times (2.99792458\times10^{8}\ \mathrm{m\,s^{-1}})^2.$$

First, $c^2 = (2.99792458\times10^{8})^2 = 8.98755179\times10^{16}\ \mathrm{m^2\,s^{-2}}$. Then

$$m_ec^2 = 9.1093837\times10^{-31} \times 8.98755179\times10^{16} = 8.1871057\times10^{-14}\ \mathrm{J}.$$

Therefore

$$\omega_C = \frac{2\times8.1871057\times10^{-14}\ \mathrm{J}}{1.0545718\times10^{-34}\ \mathrm{J\,s}} = \frac{1.6374211\times10^{-13}}{1.0545718\times10^{-34}}\ \mathrm{s^{-1}} = 1.5527680\times10^{21}\ \mathrm{s^{-1}}.$$

The base period is

$$T_C = \frac{2\pi}{\omega_C} = \frac{6.2831853}{1.5527680\times10^{21}}\ \mathrm{s} = 4.0464\times10^{-21}\ \mathrm{s}.$$

Equivalently, $\omega_C^{-1} = 1/1.5527680\times10^{21} = 6.4401\times10^{-22}\ \mathrm{s}$, and $T_C = 2\pi\times6.4401\times10^{-22} = 4.0464\times10^{-21}\ \mathrm{s}$. This is the model's base tick: the fastest cycle assigned to a material degree of freedom.

### 4.2 The ultrametric property

**Claim.** $d(i,j)=\ln(T_{\mathrm{LCA}(i,j)}/T_{\min})$ satisfies $d(i,j)\le\max\{d(i,k),d(k,j)\}$ for all cycles $i,j,k$.

**Derivation.** In a rooted tree, for any three vertices $i,j,k$, the least common ancestors satisfy: one of $\mathrm{LCA}(i,j)$, $\mathrm{LCA}(i,k)$, $\mathrm{LCA}(j,k)$ is the deepest of the three, and it coincides with one of the other two. This is the standard three-point property of rooted trees (the same property that, per [9], makes leaf path distances ultrametric). Case analysis: suppose $\mathrm{LCA}(i,j)$ is the deepest, equal to $\mathrm{LCA}(i,k)$. Then $T_{\mathrm{LCA}(i,j)} = T_{\mathrm{LCA}(i,k)} \le T_{\mathrm{LCA}(j,k)}$, since $\mathrm{LCA}(j,k)$ is an ancestor of (or equal to) $\mathrm{LCA}(i,k)$ and durations increase toward the root. Taking logarithms (monotone):

$$d(i,j) = \ln\frac{T_{\mathrm{LCA}(i,j)}}{T_{\min}} \le \ln\frac{T_{\mathrm{LCA}(j,k)}}{T_{\min}} = d(j,k) \le \max\{d(i,k),d(j,k)\}.$$

The other cases are identical by symmetry. Also $d(i,j)\ge0$ because $T_{\mathrm{LCA}}\ge T_{\min}$, and $d(i,j)=0$ iff $i=j$ (distinct cycles have distinct ancestors or are the same vertex). Hence $d$ is an ultrametric. $\blacksquare$

Interpretation: two cycles are "close in time-structure" precisely when the smallest cycle containing both is short—i.e., when they are nested deeply inside a common fast cycle. This is the opposite geometry from the line, where closeness is about position rather than containment.

### 4.3 Level count from base tick to macroscopic time

With regular nesting $T_k = T_C\,\lambda^{k}$ and $\lambda = \alpha^{-1} = 137.035999$, the level $k$ at which the cycle duration reaches a target $T_{\mathrm{target}}$ satisfies

$$k = \frac{\ln(T_{\mathrm{target}}/T_C)}{\ln\lambda}.$$

For $T_{\mathrm{target}} = 1\ \mathrm{s}$:

- $T_{\mathrm{target}}/T_C = 1/(4.0464\times10^{-21}) = 2.4713\times10^{20}$.
- $\ln(2.4713\times10^{20}) = \ln 2.4713 + 20\ln 10 = 0.90459 + 46.05170 = 46.95629$.
- $\ln\lambda = \ln 137.035999 = 4.92024$.
- $k = 46.95629 / 4.92024 = 9.5436$.

So approximately $9.54$ nesting levels—call it ten levels—separate the Compton tick from the second. This is the model's answer to why the hierarchy from quantum to human timescales is shallow: with a ratio of $137$ per level, ten levels suffice to span twenty-one orders of magnitude.

**Sensitivity.** If instead $\lambda = 2$ (a factor-of-two hierarchy, as in the factor-of-four spatial refinement of [4] applied doubly), then $k = 46.95629/\ln 2 = 46.95629/0.69315 = 67.72$ levels. The level count is therefore highly sensitive to $\lambda$ but the qualitative claim—finitely many levels—is not.

### 4.4 The continuum limit

**Claim.** As $\ln\lambda\to0$ with the tree regular, the cycle tree's tick sums converge to linear time.

**Derivation.** Fix a macroscopic interval $[0,t]$. In the regular tree, the number of level-$k$ ticks inside $[0,t]$ is $N_k(t) = \lfloor t/T_k \rfloor$. The set of level durations is $\{T_C\lambda^{k}\}$. Linear time is the statement that for any partition of $[0,t]$, the sum of interval lengths is $t$, independent of the partition. In the cycle tree, an interval is measured by counting ticks at a chosen level $k$, giving $N_k(t)\,T_k \to t$ as $T_k\to0$; this is the ordinary Riemann convergence and holds for any $\lambda$. The ultrametric-specific content is the geometry of *comparing* measurements at different levels: the discrepancy between level-$k$ and level-$(k+1)$ measurements of the same interval is bounded by one coarse tick,

$$\big|\,N_k(t)T_k - N_{k+1}(t)T_{k+1}\,\big| \le T_{k+1} = \lambda T_k.$$

As $\lambda\to1$ with $T_k\to0$ jointly, this discrepancy vanishes and the family of level-measurements becomes a single consistent additive measure on $[0,t]$: the Archimedean line. Equivalently, the log-spacing $\Delta = \ln\lambda$ between adjacent levels is the parameter whose vanishing flattens the ultrametric into a line; the ultrametric distance $d$ restricted to cycles on one branch becomes $|k-k'|\,\Delta \to |\ln T - \ln T'|$, the line metric on the logarithmic duration axis. This is the precise sense in which, following [12], "the Archimedean line is a derived abstraction": it is the $\Delta\to0$ limit of the nested-cycle measure, and any physics probed only at scales far above the level spacing $\Delta$ cannot distinguish the two.

Conversely, deviations from linear time are expected exactly where the discreteness of levels is resolvable—where a process duration is comparable to a gap between adjacent level durations. The model predicts no deviations in regimes where all relevant timescales sit deep inside one level's span.

### 4.5 Mapping to frozen-state hierarchies

[1] finds state classes frozen up to times $\Delta^{k}$, with $k$ the smallest spatial separation of facilitating spins. In the cycle-tree language, a state class frozen up to time $\Delta^{k}T_C$ occupies a subtree of depth $k$: it cannot resolve cycles shorter than its freezing time, and the hierarchy of freezing times $\{T_C\Delta^{k}\}_{k\ge0}$ is itself a regular nested cycle system with ratio $\Delta$. The ultrametric distance between two state classes is then $d = k\,\ln\Delta$, and the exponential-in-separation relaxation gradient reported in [1]'s Discussion—regions with more distant facilitating spins relaxing exponentially more slowly—is the statement that relaxation time is exponential in tree depth, i.e., linear in ultrametric distance. The model thus reads the frozen-state hierarchy as direct evidence that constrained quantum dynamics organizes its slow degrees of freedom on an ultrametric temporal skeleton.

### 4.6 Conjectural quantum-jump timescale

**Projection, with assumptions stated.** Assume (i) a quantum jump (transition between stationary states) is completed in an integer number of base ticks, and (ii) the jump duration is set by one level of the hierarchy above the base tick, i.e., the jump samples the first level whose duration exceeds the light-crossing/phase-accumulation scale of the transition, which the model takes to be scaled by $\alpha^{-1}$. Then

$$\tau_{\mathrm{jump}} = \alpha^{-1}\,\omega_C^{-1} = 137.035999 \times 6.4401\times10^{-22}\ \mathrm{s} = 8.8253\times10^{-20}\ \mathrm{s}.$$

Arithmetic: $137.035999 \times 6.4401 = 882.53$ (since $137\times6.44 = 882.28$, plus $0.035999\times6.4401 = 0.2318$, total $882.53$); hence $8.8253\times10^{-20}\ \mathrm{s}$. The next level up gives $\alpha^{-2}\omega_C^{-1} = 137.035999\times8.8253\times10^{-20} = 1.2094\times10^{-17}\ \mathrm{s}$, the orbital timescale of the ground-state Bohr atom to within the model's accuracy. This two-level ladder ($8.8\times10^{-20}\ \mathrm{s}$, $1.2\times10^{-17}\ \mathrm{s}$) is the model's concrete, falsifiable prediction for the finest structure of quantum jump durations; it is a projection of assumptions (i) and (ii), not a measurement, and no experiment known to the sources has resolved jump durations at this scale.

### 4.7 Mass as tick rate

In the model, a particle's Compton frequency $\omega = mc^2/\hbar$ is its base tick rate. Two consequences follow immediately. First, mass ratios are tick-rate ratios, so the hierarchy of particle masses is a hierarchy of base cycles and the tree's leaves are particle species. Second, the level ratio $\lambda$ is dimensionless and universal, so the tree structure is independent of which leaf (which particle) anchors it; different particles share the same ultrametric skeleton with different base ticks. The Zitterbewegung frequency computed in Section 4.1 is $2m_ec^2/\hbar$ rather than $m_ec^2/\hbar$ because the Dirac interference pairs positive- and negative-energy branches; the model takes the interference frequency as the physical tick since it is the frequency at which the particle's internal state recurs.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none is a measurement.

- **R1 (base tick).** The electron Compton/Zitterbewegung cycle has $\omega_C = 1.5527680\times10^{21}\ \mathrm{s^{-1}}$ and $T_C = 4.0464\times10^{-21}\ \mathrm{s}$ (Section 4.1).
- **R2 (ultrametricity).** The cycle-tree distance $d(i,j)=\ln(T_{\mathrm{LCA}}/T_{\min})$ satisfies the strong triangle inequality for any rooted containment tree of cycles (Section 4.2).
- **R3 (hierarchy depth).** With the assumed level ratio $\lambda=\alpha^{-1}=137.035999$, the number of nesting levels from the Compton tick to one second is $k = 9.5436$, i.e., ten levels span twenty-one orders of magnitude