# Superposition as a Projection Artifact of Discrete Tree Geometry: What Branch Counting Can and Cannot Derive

## Abstract

Quantum superposition is standardly treated as ontological: a system genuinely occupies multiple states until measurement. An alternative conjecture holds that superposition is an artifact of projecting a single definite path through a discrete, depth-organized tree of configurations onto a continuous, resolution-limited measurement basis, with the wavefunction as a coarse-grained epistemic summary and collapse as Bayesian updating. This paper tests the conjecture's central quantitative demand: that the Born rule emerge from how coarse-grained branch volumes scale with tree depth. We construct an explicit binary-tree model, derive the branch-volume measure, and show by direct arithmetic that uniform branch counting yields probabilities linear in volume fractions, that a quadratic (Born-form) measure fails normalization for any nontrivial split, and that reproducing $p_i=|a_i|^2$ requires the volume assignment itself to encode $|a_i|^2$, reducing the claimed derivation to a restatement. We further prove a structural requirement: non-negative coarse-graining measures cannot reproduce interference terms, so any empirically adequate tree must carry phase as ontological structure. We derive the CHSH bound $|S|\le 2$ for local deterministic tree assignments, confirming the model must be nonlocal or contextual. The conjecture survives as a coherent research program only in a restricted form: a phase-carrying, contextual tree ontology whose volume dynamics, not its counting, must derive the Born rule.

## 1. Introduction

The measurement problem costs physics in a specific way. Physicists teaching and using quantum mechanics must maintain, without a settled basis, a dual dynamics in which systems evolve unitarily between measurements and stochastically during them. Engineers designing quantum computers must budget for decoherence and error correction without knowing whether the continuous state space underlying their models is fundamental or emergent; the resource overheads are large, with surface-code architectures requiring physical-to-logical qubit ratios of roughly 1000:1 as reported in the ultrametric-tree analysis of quantum fragility [11]. Philosophers and foundations researchers spend sustained effort comparing interpretations that are empirically equivalent by construction. If superposition were shown to be a projection artifact of a discrete hidden structure — a single definite path through a tree of configurations, coarse-grained by a resolution-limited measurement basis — then the measurement problem would dissolve into Bayesian updating, the interpretations would unify under one ontology, and the design target for quantum hardware would shift from managing continuous amplitudes to managing discrete hierarchical state.

Who faces this problem directly: the quantum foundations community, which lacks any empirical lever to separate Copenhagen, many-worlds, and hidden-variable readings; and, downstream, quantum computing engineers, whose error-correction budgets assume the continuous Hilbert-space formalism is exactly fundamental. What blocks progress today is that no hidden-variable model has derived the Born rule from its own structure rather than postulating it, and no such model reproduces interference without importing the quantum formalism wholesale. A derivation of $p_i=|a_i|^2$ from branch volumes would change the field's decision landscape: it would convert an interpretational dispute into a testable structural claim.

This paper takes the conjecture seriously as a mathematical program and subjects its central demand to explicit derivation. The conjecture, as stated in the source research notes, is that quantum superposition is not ontological but an artifact of projecting a single, definite path through a discrete, depth-organized tree of configurations onto a continuous, resolution-limited measurement basis; that the wavefunction is a coarse-grained epistemic summary; that collapse is Bayesian updating; and that the Born rule should emerge from how coarse-grained branch volumes scale with tree depth. The program sits within a broader effort, visible in discrete differential geometry, to build discrete equivalents of smooth geometric notions and to treat consistency conditions as integrability constraints [1]; and within an information-ontological framework in which quantum states are data structures and the Hamiltonian extracts hierarchical depth of information within a state [9].

The contributions are:

- A derivation of the branch-volume measure for a depth-$d$ binary tree and proof that uniform counting gives $p_i=f_i$ linear in volume fraction, with the arithmetic showing a quadratic Born-form measure violates normalization for every nontrivial volume split (Section 4).
- A proof that the Born rule cannot be derived from branch counting alone: reproducing $p_i=|a_i|^2$ requires the coarse-grained volume assignment to already encode $|a_i|^2$, which reduces the conjecture's central claim to a circularity unless volume dynamics supplies the missing input (Section 4).
- A derivation that non-negative coarse-graining measures cannot reproduce interference cross terms, with the two-path arithmetic showing a required cross term of magnitude $2|a_1 a_2|$ and sign-dependent cancellation; this forces phase to be ontological in any adequate tree model (Section 4).
- A derivation of the CHSH local bound $|S|\le 2$ for deterministic tree assignments, establishing that the model must be nonlocal or contextual to match quantum predictions (Section 4).
- An assessment of the conjecture's empirical anchors and falsifiers, including metre-scale superposition experiments [4] and discrete-time quantum-walk realizations [7] (Sections 5–7).

## 2. Background and Related Work

The program of replacing continuous geometric structure with discrete structure that reproduces continuum limits has a precise mathematical precedent. Discrete differential geometry, as formulated by Bobenko and Suris, aims at the development of discrete equivalents of the notions and methods of smooth surface theory, and reports that progress in the discrete setting has led to a better understanding of fundamental structures underlying classical differential geometry and integrable systems theory [1]. Their treatment of conjugate nets — maps $f:\mathbb{R}^m\to\mathbb{R}^N$ with $\partial_i\partial_j f\in\mathrm{span}(\partial_i f,\partial_j f)$ — and orthogonal nets shows that discrete analogues can be consistency-preserving in a strong sense. This supports the tree conjecture's methodological bet: a discrete hierarchy can underwrite a continuous formalism if the discrete structure satisfies the right consistency conditions. It also raises the bar: the tree model must exhibit an analogous consistency property, not merely a qualitative resemblance to Hilbert space.

Recent work in relativistic quantum information supplies evidence that superposition components behave as distinct classical contexts. In the analysis of superpositions of thermalisations, a quantum probe interacting with a superposition of environment states fails to thermalise because, for each amplitude, the probe interacts with a different set of field modes — for spatial superpositions of accelerated motions, modes localised in different Rindler wedges — and these mode sets are incommensurate, producing non-Planckian distributions; thermality is recovered when the involved modes are orthogonal or identical [2]. This is directly relevant to the tree conjecture: it shows that each branch of a superposition carries its own coherent classical context, which is the behavior a coarse-graining model must reproduce if each tree branch is to act as a definite configuration with its own effective environment.

The quantum reference frame literature strengthens the epistemic reading the conjecture requires. Work on spacetime quantum reference frames shows that when a particle's position or velocity is in superposition, the proper time displayed by its internal clock is also in superposition from an external perspective, and that every quantum particle can equally serve as a reference frame with no preferred frame singled out [5]. If even proper time — the classical anchor of relativistic description — is frame-relative and superposition-dependent, the notion of a single definite path through configuration space becomes perspectival rather than absolute, which is the structure the projection-artifact conjecture needs. Similarly, the quantum conformal symmetry result maps a Klein-Gordon field on a superposition of conformally related spacetimes to a field with a superposition of mass parameters on a fixed spacetime, via an operator $\hat{\mathcal{S}}$, establishing an equivalence between a superposition-of-spacetimes situation and one with a definite classical spacetime [3]. This is a concrete existence proof that "superposition of $X$" can be re-represented as definite structure with modified parameters — exactly the representational move the tree conjecture makes for superposition of configurations.

Experimental anchors bound what any tree model must reproduce. The metre-scale superposition work reports optical pulses placing a freely falling Bose-Einstein condensate into a superposition over macroscopic separations, in the line of Kovachy et al.'s experiment [4]. A tree ontology in which the definite path is fundamental must explain why interference persists at metre scale, where any coarse-graining artifact explanation must show the measurement basis, not the ontology, limits resolution. Discrete-time quantum walks provide the closest physical realization of tree-like dynamics: the standard one-dimensional DTQW evolves a walker $|x\rangle$ with a coin under a time-independent unitary $U=TS_c(\psi)$, and an experiment has implemented this in linear optics with walker positions encoded in non-orthogonal polarization states $|k\rangle_p=\cos\theta_k|H\rangle+e^{i\phi_k}\sin\theta_k|V\rangle$, reporting photon loss of about 70% after every two steps due to beam-splitter leakage [7]. Two features matter here: the walk is genuinely discrete-time and tree-branching in structure, and the experiment's encoding method reconstructs an $n$-dimensional state $\sum_k a_k|k\rangle$ from a two-dimensional qubit, demonstrating that a low-dimensional system can carry the information of a high-dimensional superposition — a physical instance of the coarse-graining/reconstruction relation the conjecture posits.

On the formal side, noncommutative projective geometry offers a template for how coarse-graining can be mathematically rigorous: the Serre correspondence defines the noncommutative projective scheme as a quotient category $\mathrm{QGr}\,R = \mathrm{Gr}\,R/\mathrm{Tors}\,R$, recovering geometric structure from a category of modules modulo those vanishing at large degree [8]. The analogy for the tree model is direct: the wavefunction would be an object of a quotient of the full tree structure by an equivalence relation (the measurement resolution), and the question is whether the quotient carries a linear structure reproducing Hilbert space. The parametrized quantum circuit literature supplies quantitative constraints on how much of quantum state space discrete structures can reach: the effective quantum geometry of PQCs shows the parameter dimension $D_{\mathrm{C}}$ reaches the maximal value $2^{N+1}-2$ for $N$ qubits, with the quantum Fisher information spectrum developing a pronounced tail of small eigenvalues near the transition depth $p_{\mathrm{c}}$ [6]. Any tree model claiming to reproduce the $N$-qubit state space must therefore match an exponentially large accessible manifold, not a polynomial one.

Finally, the QNFO corpus supplies the ontological framing the conjecture inherits. The Unified Theory of Non-Archimedean Ontology models reality as informational data structures in which every quantum state functions as a unit of data storage and the Hamiltonian extracts hierarchical depth within a state, and it explicitly rejects many-worlds as an extravagant ontological leap that misunderstands the structure of existence [9]. The Alpha Pi project identifies the continuous real-number field underlying standard quantum mechanics as the source of quantum fragility — the smooth Bloch sphere admits infinitesimal thermal drifts that accumulate into errors — and pivots to a discrete ultrametric hierarchy, listing testable signatures including deviations from standard quantum mechanics at ultra-low energies, anomalies in few-particle interference patterns in ultracold atomic systems, and modified tunneling rates in mesoscopic devices [11]. The epistemic character of the wavefunction-as-summary is anticipated by the map-territory analysis in Principia Ontologica, which argues that cognitive and scientific frameworks are data-compression heuristics, that confusing the representation with the referenced entity produces categorical errors, and that self-reference structurally limits any observer's claim to a perfectly objective viewpoint [12]. The universal superposition principle articulated in the waves treatise — that the total state at every point is the sum of co-existing wave patterns, with interference as the geometry this addition sculpts [10] — marks the precise target the tree model must reach: linear addition with phase, not merely coexistence of branches.

## 3. Methods

We model the conjecture's ontology as a rooted tree $\mathcal{T}_{b,d}$ with constant branching factor $b$ and depth $d$. Each node at depth $k$ represents a configuration cell; each leaf at depth $d$ represents a maximally refined configuration in the ontology. A definite path is a map $\gamma:\{0,\dots,d\}\to\mathcal{T}_{b,d}$ with $\gamma(k)$ at depth $k$ and $\gamma(k+1)$ a child of $\gamma(k)$. The measurement basis is modeled as a partition $\Pi$ of the leaf set $L(\mathcal{T}_{b,d})$ into $m$ equivalence classes $C_1,\dots,C_m$, with $m$ set by the resolution of the measurement apparatus. The wavefunction is modeled as a summary object over $\Pi$, and collapse as Bayesian conditioning of the summary on the observed class.

The analysis proceeds in four derivations, each using only counting arguments and explicit arithmetic:

1. **Volume measure.** Define the coarse-grained volume of class $C_i$ as $f_i = |C_i|/|L|$, where $|L| = b^d$. Derive the probability measure that uniform branch counting induces and test it against the Born rule target $p_i = |a_i|^2$.
2. **Normalization test.** For a candidate measure $p_i = f_i^\gamma$, determine which exponents $\gamma$ satisfy $\sum_i p_i = 1$ for all partitions, and what this requires of the amplitude-volume relation.
3. **Interference test.** For a two-class partition with amplitudes $a_1, a_2$, compute the quantum-predicted class probability and compare with the maximum any non-negative measure on leaves can assign, locating exactly which term fails.
4. **Locality test.** For a deterministic assignment of outcomes $\pm 1$ at each leaf to four measurement settings, enumerate the structure of the CHSH combination and derive its bound.

We do not simulate dynamics; the derivations are structural constraints that any dynamical completion of the tree model must satisfy. Where a number depends on an assumption not fixed by the conjecture, we state the assumption inline and label the resulting figure a projection.

## 4. Analysis

### 4.1 Tree counts and the volume measure

For the tree $\mathcal{T}_{b,d}$, the number of nodes at depth $k$ is $b^k$ by direct induction: depth 0 has $b^0 = 1$ node (the root), and each node at depth $k$ has $b$ children, so depth $k+1$ has $b \cdot b^k = b^{k+1}$ nodes. The leaf set therefore has

$$|L| = b^d.$$

For the binary case $b=2$ and depth $d=100$:

$$|L| = 2^{100} = \left(2^{10}\right)^{10} = 1024^{10}.$$

Using $\log_{10} 2 = 0.30102999566$, we get $100 \times 0.30102999566 = 30.102999566$, so

$$2^{100} = 10^{30.102999566} \approx 1.2676506 \times 10^{30}.$$

A depth-100 binary tree has approximately $1.27 \times 10^{30}$ leaves. This number matters for feasibility: any method that enumerates leaves individually is computationally infeasible at even modest depths, so the coarse-graining map must exploit self-similarity of the tree rather than leaf-level access.

The coarse-grained volume of class $C_i$ is

$$f_i = \frac{|C_i|}{b^d}, \qquad \sum_{i=1}^{m} f_i = \frac{\sum_i |C_i|}{b^d} = \frac{b^d}{b^d} = 1.$$

Uniform branch counting — the measure in which each leaf contributes equal weight — induces the class probability

$$p_i = f_i.$$

This is linear in volume. The Born rule target is $p_i = |a_i|^2$. The two agree only if $f_i = |a_i|^2$, i.e., only if the volume fraction itself encodes the squared amplitude. We examine in Section 4.2 whether a nonlinear counting measure can bridge the gap.

### 4.2 Normalization: the exponent test

Suppose the conjecture's "branch volumes scale with tree depth" is implemented as a power-law measure

$$p_i = f_i^\gamma$$

for some exponent $\gamma$, with the amplitude identified as linear in volume, $|a_i| \propto f_i$. Normalization requires

$$\sum_{i=1}^{m} f_i^\gamma = 1$$

for every partition. Test the simplest nontrivial case: two classes with $f_1 = f_2 = \tfrac{1}{2}$ (a symmetric split, as in a balanced double-slit scenario).

- $\gamma = 1$: $\sum_i f_i = \tfrac{1}{2} + \tfrac{1}{2} = 1$. Normalized, but gives $p_i = f_i$, so the Born rule holds only if $|a_i|^2 = f_i$ — the volume assignment already carries the answer.
- $\gamma = 2$: $\sum_i f_i^2 = \left(\tfrac{1}{2}\right)^2 + \left(\tfrac{1}{2}\right)^2 = \tfrac{1}{4} + \tfrac{1}{4} = \tfrac{1}{2} \neq 1$. **Fails normalization.**
- $\gamma = \tfrac{1}{2}$: $\sum_i f_i^{1/2} = \sqrt{\tfrac{1}{2}} + \sqrt{\tfrac{1}{2}} = 2 \times 0.7071067 = 1.4142136 \neq 1$. **Fails normalization.**

The quadratic case fails generally, not just for the symmetric split. For any $f_i \geq 0$ with $\sum_i f_i = 1$ and more than one nonzero $f_i$:

$$\sum_i f_i^2 < \left(\sum_i f_i\right)^2 = 1,$$

because the cross terms $2 f_i f_j$ for $i \neq j$ are strictly positive when at least two $f_i$ are nonzero. Equality $\sum_i f_i^2 = 1$ holds if and only if exactly one $f_i = 1$ and the rest vanish — the degenerate case with no superposition at all.

**Result 1.** No power-law measure $p_i = f_i^\gamma$ with $\gamma \neq 1$ is normalized for all partitions, and $\gamma = 1$ yields the Born rule only when the volume fractions are assigned as $f_i = |a_i|^2$ in the first place. The Born rule therefore cannot emerge from branch counting alone; the conjecture's derivation burden shifts entirely to the dynamics that fixes the volume assignment $f_i = |a_i|^2$.

This is the paper's central structural finding, and it sharpens rather than merely refutes the conjecture: a tree ontology remains viable only if its branch-volume dynamics — not its combinatorics — produces volume fractions equal to squared amplitudes.

### 4.3 Interference: the phase test

The quantum prediction for a two-path scenario with amplitudes $a_1, a_2$ and a measurement distinguishing "same class" from "different class" outcomes is

$$p_{\mathrm{QM}} = |a_1 + a_2|^2 = |a_1|^2 + |a_2|^2 + 2\,\mathrm{Re}(a_1^* a_2).$$

Take the symmetric real case $a_1 = a_2 = \tfrac{1}{\sqrt{2}}$:

$$p_{\mathrm{QM}} = \left(\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}\right)^2 = \left(\sqrt{2}\right)^2 = 2,$$

before normalization to the detector's acceptance; the cross term is

$$2\,\mathrm{Re}(a_1^* a_2) = 2 \times \frac{1}{\sqrt{2}} \times \frac{1}{\sqrt{2}} = 2 \times \frac{1}{2} = 1,$$

which equals the sum of the diagonal terms $\tfrac{1}{2} + \tfrac{1}{2} = 1$. The cross term is as large as the entire diagonal contribution.

Now take the opposite phase, $a_1 = \tfrac{1}{\sqrt{2}}$, $a_2 = -\tfrac{1}{\sqrt{2}}$:

$$p_{\mathrm{QM}} = \left(\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}\right)^2 = 0,$$

while the diagonal terms are unchanged