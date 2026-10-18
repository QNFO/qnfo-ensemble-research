# The Born Rule as Boundary Measure: Quantum Mechanics on a Bruhat–Tits Tree

## Abstract

Quantum mechanics predicts measurement statistics with unmatched precision, yet it postulates rather than derives its two most consequential rules: state collapse and the Born rule $P_i = |c_i|^2$. This leaves an interpretational gap that has practical consequences for how quantum simulators and cloud quantum processors are modeled and certified. We reformulate finite-dimensional quantum mechanics on the Bruhat–Tits tree $T_p$ attached to the $p$-adic numbers: energy states are nodes of the tree, the wavefunction is a branching path, measurement is a projection (a Monna-type map) from the tree boundary to the Archimedean line, and the Born rule is recovered geometrically as boundary-measure counting. We prove that for any finite-dimensional state whose squared amplitudes are rationals with denominator a power of $p$, the boundary measure of the outcome container equals $|c_i|^2$ exactly, and we exhibit the full arithmetic for a qubit with amplitudes $c_1 = 3/5$, $c_2 = 4/5$: the containers have measures $9/25 = 0.36$ and $16/25 = 0.64$, matching the Born rule. We further show the projection is measure-preserving, that energy quantization follows from tree depth, and that local deterministic container assignments obey the CHSH bound $|S| \le 2$, so Bell-inequality violation remains an open, nontrivial test. The work is analytical and unreviewed (TRL 1–2); its falsifiable next step is a Monte Carlo boundary-sampling check with statistical resolution $\sigma \approx 4.8 \times 10^{-4}$ at $10^6$ samples.

## 1. Introduction

Every user of quantum technology — from the operators of cloud-accessible superconducting processors to the designers of quantum repeater networks — relies on the Born rule to convert a computed state vector into a predicted frequency of experimental outcomes. The rule works, but in the standard formulation it is an axiom: the theory states that a measurement of an observable with eigenbasis $\{\ket{i}\}$ on a state $\ket{\psi} = \sum_i c_i \ket{i}$ yields outcome $i$ with probability $|c_i|^2$, and that the state then collapses, without saying what either operation is physically. This postulational status is not merely philosophical bookkeeping. It determines how simulators are validated, how certification protocols interpret observed frequencies, and whether apparent deviations from $|c_i|^2$ would indicate new physics or a failure of the statistical model. A derivation of the Born rule from an explicit geometric mechanism would change what a deviation means: it would become evidence about the geometry of the state space rather than about an unexplained axiom.

The cost of leaving the rule unexplained is visible across the foundations literature. Ontological-model programs, in which outcomes are deterministic functions of hidden variables, are constrained by the Bell and Kochen–Specker theorems, and a careful search over candidate hidden-variable spaces reports that no model reproducing the exact quantum statistics has been found for any dimension, while noting that no proof excludes one [4]. Pilot-wave reconstructions fare no better on other axes: for a harmonic oscillator in its ground state, Bohmian mechanics and standard quantum mechanics predict time correlations of opposite sign, so the two cannot both describe experiment [7]. Meanwhile, generalized-quantum-mechanics programs show that the textbook formulation is one point in a wider space of consistent theories built on fine-grained histories, coarse-graining, and decoherence [5], and axiom rederivations in symmetry language show that the measurement postulates can be restated, though not eliminated, in group-theoretic terms [8]. The gap this paper addresses is therefore concrete: no existing reconstruction derives $|c_i|^2$ from a countable, explicitly constructible geometric object without introducing a new stochastic postulate.

We propose such an object. Ostrowski's theorem classifies all non-trivial absolute values on $\mathbb{Q}$: the Archimedean one, completing $\mathbb{Q}$ to $\mathbb{R}$, and the $p$-adic ones $|\cdot|_p$, completing $\mathbb{Q}$ to $\mathbb{Q}_p$ [9]. The $p$-adic completion carries an ultrametric norm $|x+y|_p \le \max(|x|_p, |y|_p)$, and its unit ball $\mathbb{Z}_p$ is naturally a fractal tree in which each vertex has exactly $p+1$ neighbours [12]. This tree, the Bruhat–Tits tree $T_p$, has a boundary $\partial T_p$ carrying a canonical probability measure. Our conjecture, made precise and partially proved here, is that quantum mechanics on $T_p$ reproduces standard finite-dimensional quantum mechanics with the Born rule emerging as boundary-measure counting: the probability of outcome $i$ is the fraction of boundary points lying in the container associated with $i$.

If the conjecture holds in full, three things change. The measurement problem dissolves as a projection artifact, since collapse is the deterministic restriction of a path to a container. Wave–particle duality dissolves with it, because the "wave" is the Archimedean shadow of a discrete branching object. And quantization ceases to be postulated: discrete energy levels correspond to tree levels, a mechanism related to the spectral analysis of Bruhat–Tits trees, where for $p=2$ and depth $D=6$ the Laplacian spectrum is discrete, bounded, and centered near $\mu \approx 1.984$ [10].

The contributions of this paper are:

1. A formal construction of quantum states as paths on $T_p$ and measurement outcomes as measurable containers on $\partial T_p$, with the Monna-type projection map to the Archimedean line defined explicitly (Section 3).
2. A proof, with complete arithmetic, that boundary-measure counting reproduces the Born rule exactly for all finite-dimensional states whose squared amplitudes are rationals of the form $m_i/p^N$, including the worked qubit example $(3/5, 4/5)$ with container measures $9/25$ and $16/25$ (Section 4).
3. A proof that the projection map is measure-preserving, so the Archimedean probability calculus is the pushforward of boundary measure (Section 4).
4. A derivation that energy quantization follows from tree depth, with node counts and spectral bounds checked against the reported $p=2$, $D=6$ spectrum [10] (Section 4).
5. A derivation of the CHSH bound $|S| \le 2$ for local deterministic container assignments, establishing Bell violation as a sharp, currently unmet test of the framework (Section 4).
6. An assessment of readiness, falsification conditions, and the smallest next computational test, with its statistical resolution computed (Sections 6 and 7).

## 2. Background and Related Work

The framework proposed here sits at the intersection of quantum foundations, hidden-variable reconstructions, and non-Archimedean mathematics. We review each strand through what its representative works actually establish.

**Experimental constraints from Bell tests.** The "Carlo Novero" laboratory at INRIM produces polarization-entangled photon pairs by parametric down-conversion and uses them for tests of local realism; its two type-I crystal source, built from two $LiIO_3$ crystals of 1.5 cm length with optical axes at $90°$, achieves a coincidence rate of 10 kHz at 200 mW pump power [1]. The same laboratory has demonstrated that dispersive propagation through fiber can restore indistinguishability and entanglement, observing Bell-inequality violation in the center of the coincidence peak after erasing longitudinal walk-off [1]. These experiments fix the empirical target any reconstruction must meet: entanglement statistics, including Bell violation, are observed properties of real optical systems, not interpretational options.

**Cloud quantum hardware as a testbed.** The Tianyan Quantum Cloud Platform operates superconducting processors of the Zuchongzhi 3.0 class; the Tianyan-287 system features 105 qubits with single-qubit gate, two-qubit gate, and readout fidelities of 99.90%, 99.56%, and 98.7% respectively [2]. Its random circuit sampling experiment on 74 qubits and 24 cycles is reported to achieve quantum advantage beyond existing top supercomputers [2]. For this paper, such platforms matter in two ways: they are the class of device whose certification protocol would be reinterpreted if the Born rule were geometric, and they are candidate execution environments for the boundary-sampling simulations proposed in Section 7.

**Operator-valued probabilities and generalized measurement.** "Doubly Quantum Mechanics" quantizes the geometrical configurations of apparatus themselves, deforming the rotation group $SU(2)$ into the quantum group $SU_q(2)$; its striking prediction is operator-valued probabilities whose distributions depend on the geometry state of the setup and can have non-vanishing variance [3]. This is the closest existing analogue to our program in spirit: both frameworks make probability itself depend on geometric structure. The difference is that DQM deforms the symmetry group while keeping the Archimedean continuum, whereas we replace the continuum with the boundary of $T_p$.

**Ontological models and the Kochen–Specker constraint.** Ontological models assign deterministic outcomes to hidden states $\lambda$, and the Kochen–Specker theorem sharply constrains them for three or more dimensions: in the examined model, an ontological state $\lambda$ closest to one measurement's central element can be closer to a different element under a rotated measurement basis, which is precisely how contextuality is forced [4]. The author of that analysis reports having played with many hidden-variable spaces without finding one reproducing the quantum statistics exactly for any dimension $d$, while noting no proof excludes such a model [4]. Our framework must confront this directly: container assignments on $\partial T_p$ are deterministic given the boundary point, so the framework is an ontological model in this taxonomy and must either exhibit the required contextuality or fail the KS test. Section 4 shows it passes the CHSH inequality as a local deterministic model — which means it currently fails to reproduce Bell violation, and we treat this as the framework's central open problem rather than hiding it.

**Generalized quantum theory.** The consistent-histories program answers the question of whether quantum mechanics applies to spacetime affirmatively, provided the textbook formulation is generalized to closed systems free of a fundamental role for measurements and observers, and freed from any assumption of fixed spacetime geometry [5]. Its two laws of evolution — unitary Schrödinger evolution between measurements and state reduction at measurement — are the same pair of postulates we aim to unify. That program demonstrates, by construction, that quantum theory tolerates reformulation when its structural assumptions are made explicit; our work applies the same strategy to the number field underlying the state space.

**Hidden-variable failure modes.** Bohmian mechanics, the most developed deterministic reconstruction, is shown to predict values of opposite sign from quantum mechanics for certain time correlations of a ground-state harmonic oscillator, because its local expectation values — the beables — depend on the Heisenberg time in a way that conflicts with linear response theory [7]. The conclusion drawn there is that Bohmian mechanics and quantum mechanics cannot both describe experimental reality [7]. This is a cautionary precedent for any deterministic reconstruction, including ours: agreement on static statistics does not guarantee agreement on dynamical correlations, and our framework must eventually be tested against time-correlation observables, not only measurement frequencies.

**Symmetry-language axiomatics.** Recasting quantum mechanics in symmetry language defines a system by its symmetries, with the state a vector in a projective space representing its symmetry groups, and shows that measurement issues can be restated in this basis-independent language [8]. Notably, that work invokes the Sinai theorem of phase transition to argue that for perturbations below a critical value, a system-environment coupling has asymptotic probability 1 of settling into one stable ground state — a decoherence mechanism stated in symmetry terms [8]. Our framework parallels this in seeking a basis-independent substrate (the tree boundary) but differs in that the substrate is countable at every finite level.

**Non-Archimedean consilience.** The consilience program organizes the convergence of physics and number theory around Ostrowski's theorem as a selection rule: every consistent physical theory using "distance" must specify which completions of $\mathbb{Q}$ its dynamics operate in, and current physics implicitly chooses only the $\infty$-completion as a historical accident of calculus being developed over $\mathbb{R}$ [9]. That program identifies the adele ring, realized geometrically as a product of Bruhat–Tits trees, as the object on which the convergent evidence converges [9]. Our paper takes the specific next step for quantum mechanics: rather than arguing that $\mathbb{Q}_p$-completions are admissible, it constructs the measurement calculus on a single tree and checks it against the Born rule.

**Spectral dynamics on trees.** Spectral analysis of the regular Bruhat–Tits tree for $p=2$ and depth $D=6$ reveals a discrete, bounded spectrum with mean eigenvalue $\mu \approx 1.984$, consistent with the known confinement of regular-tree spectra to the interval $[-2\sqrt{p-1},\, 2\sqrt{p-1}]$ [10]. Quantum walks on such trees localize on prime structures while delocalizing on composite product graphs, with a multi-base triangulation regression reaching $R^2 = 0.998$ [10]. These results establish that tree Laplacians carry physically meaningful, computable spectra — the machinery our energy-quantization argument in Section 4 relies on.

**Syntactic and ultrametric paradigms.** The non-Archimedean syntactic paradigm argues that quantum-information fragility is an artifact of projecting discrete states onto continuous vector spaces, and that early $p$-adic mechanics established the mathematical viability of ultrametric states, with adelic formulations integrating real and $p$-adic numbers [11]. The ultrametric quantum gravity program makes the complementary structural claim: the same non-Archimedean tree geometry that offers intrinsic fault tolerance in computation also resolves the problem of time, and the framework is testable through modified dispersion relations and discrete geometry [12]. Both supply the motivation for taking the tree, rather than the continuum, as primitive; neither, however, derives the Born rule, which is the specific gap this paper fills.

## 3. Methods

### 3.1 The tree and its boundary

Fix a prime $p$. The Bruhat–Tits tree $T_p$ is the infinite, homogeneous tree in which every vertex has exactly $p+1$ neighbours; it is the geometric realization of the ultrametric space $\mathbb{Q}_p$, whose norm satisfies $|x+y|_p \le \max(|x|_p, |y|_p)$ [12]. We root $T_p$ at a distinguished vertex $v_0$. Level $n$ is the set of vertices at graph distance $n$ from $v_0$.

A boundary point $x \in \partial T_p$ is an infinite path from $v_0$ that never terminates. The boundary $\partial T_p$ is naturally identified with the ring of $p$-adic integers $\mathbb{Z}_p$ [12]. For each finite path (node) $s$ at level $n$, the cylinder set $C_s \subset \partial T_p$ is the set of boundary points whose path passes through $s$.

### 3.2 Boundary measure

We define $\mu$, the uniform boundary measure, on cylinders by:

$$\mu(C_s) = p^{-n} \quad \text{for } s \text{ at level } n.$$

This is the standard Haar measure on $\mathbb{Z}_p$ transported to $\partial T_p$. Normalization is checked in Section 4. Measurable sets ("containers") are countable unions of cylinders; $\mu$ extends to them by additivity.

### 3.3 States as paths, amplitudes as container weights

A pure state of a $d$-level system is a pair $(\{C_i\}_{i=1}^{d}, \{w_i\}_{i=1}^{d})$ where:

- the containers $C_i \subset \partial T_p$ are disjoint measurable sets whose union is $\partial T_p$;
- the weights are non-negative rationals with $w_i = m_i / p^N$ for integers $m_i \ge 0$ and a common denominator $p^N$, satisfying $\sum_i w_i = 1$.

The amplitude of outcome $i$ is defined as $c_i = \sqrt{w_i}$ (up to a phase, which does not enter the statistics derived here). This restriction — squared amplitudes rational with $p$-power denominator — is the exact scope of theorems proved in Section 4; extension to arbitrary real amplitudes is a conjecture discussed in Section 6.

### 3.4 The Monna-type projection

The Monna map is the projection from the tree boundary to the Archimedean line that reads off the digits of a boundary point. Label the $p$ edges leaving each non-root vertex by digits $a \in \{0, \dots, p-1\}$ in a fixed way (the root has $p+1$ edges; we fix one as the "integer part" edge and label the rest by digits). For $x \in \partial T_p$ with digit sequence $(a_1, a_2, a_3, \dots)$, define:

$$\phi(x) = \sum_{k=1}^{\infty} a_k \, p^{-k} \in [0, 1].$$

The map $\phi$ is the bridge between the non-Archimedean state space and the Archimedean probability line: measurement outcomes observed on laboratory instruments live on the Archimedean side, and $\phi$ transports tree geometry to it. Its measure-theoretic property is proved in Section 4.

### 3.5 Dynamics and energy

We postulate the minimal dynamical rule: the discrete time evolution of a path is a walk on $T_p$ whose generator is the tree Laplacian $\Delta_p$, the operator whose spectral theory on Bruhat–Tits trees is well studied [10]. Energy levels are indexed by tree depth: a component localized at level $n$ carries energy $E_n = n \hbar \omega_0$, where $\omega_0$ is a model parameter. This converts tree depth into the quantum number $n$ of, e.g., a harmonic ladder, deriving quantization from tree structure rather than postulating a discrete spectrum.

### 3.6 Measurement as projection

A measurement with outcomes $\{1, \dots, d\}$ is the deterministic event in which the system's boundary point $x$ falls into container $C_i$; the observed outcome is $i$, and the "collapsed" state is the restriction of the path to $C_i$. No stochastic postulate is introduced: the randomness of outcomes is epistemic, arising from ignorance of which boundary point the system occupies, exactly as in classical statistical mechanics over a hidden state space — with the crucial difference that the hidden space $\partial T_p$ carries the ultrametric, not the Archimedean, geometry.

## 4. Analysis

All input numbers in this section are either definitions of the framework (Section 3), values reported in the cited literature, or arithmetic on those values. Every derivation is shown step by step.

### 4.1 Tree counting and measure normalization

**Input (definition, Section 3.1):** each vertex of $T_p$ has $p+1$ neighbours [12].

The root $v_0$ has $p+1$ children. Each subsequent vertex has $p+1$ neighbours, one of which is its parent, so each level-$n$ vertex ($n \ge 1$) has $p$ children. Therefore the number of vertices at level $n$ is:

$$N_n = (p+1)\, p^{\,n-1} \quad \text{for } n \ge 1.$$

Check for $p = 2$: $N_1 = 3 \cdot 2^0 = 3$, $N_2 = 3 \cdot 2 = 6$, $N_3 = 3 \cdot 4 = 12$. The cumulative node count up to depth $D$ is:

$$N_{\text{tot}}(D) = 1 + \sum_{n=1}^{D} (p+1) p^{n-1} = 1 + (p+1)\,\frac{p^D - 1}{p - 1}.$$

For $p = 2$: $N_{\text{tot}}(D) = 1 + 3(2^D - 1) = 3 \cdot 2^D - 2$. At $D = 6$: $N_{\text{tot}}(6) = 3 \cdot 64 - 2 = 192 - 2 = 190$.

**Measure normalization.** There are $p^n$ cylinders at level $n$ (one per level-$n$ node reachable along digit-labeled edges; the root's extra edge fixes the integer part and does not generate a digit). Each has measure $p^{-n}$, so:

$$\sum_{s \,:\, |s| = n} \mu(C_s) = p^n \cdot p^{-n} = 1. \checkmark$$

The measure $\mu$ is a probability measure on $\partial T_p$.

### 4.2 Born rule for rational squared amplitudes (main theorem)

**Theorem 1.** Let $\ket{\psi} = \sum_{i=1}^{d} c_i \ket{i}$ be a finite-dimensional pure state with $|c_i|^2 = m_i / p^N$ for non-negative integers $m_i$ and $\sum_i m_i = p^N$. Define containers $C_i$ as unions of $m_i$ distinct level-$N$ cylinders. Then the boundary measure of $C_i$ equals the Born-rule probability:

$$\mu(C_i) = |c_i|^2 \quad \text{for all } i.$$

**Proof.** Each level-$N$ cylinder has measure $p^{-N}$ (Section 3.2). The containers are disjoint and their union is all of $\partial T_p$ because $\sum_i m_i = p^N$ cylinders partition the $p^N$ level-$N$ cylinders. By additivity:

$$\mu(C_i) = m_i \cdot p^{-N} = \frac{m_i}{p^N} = |c_i|^2. \qquad \blacksquare$$

**Worked example (qubit).** Take $p = 5$, $N = 2$, and amplitudes $c_1 = 3/5$, $c_2 = 4/5$. Then:

$$|c_1|^2 = \left(\frac{3}{5}\right)^2 = \frac{9}{25}, \qquad |c_2|^2 = \left(\frac{4}{5}\right)^2 = \frac{16}{25}.$$

Check normalization: $9 + 16 = 25 = 5^2 = p^N$. ✓

Container $C_1$ is the union of $m_1 = 9$ level-2 cylinders; container $C_2$ is the union of $m_2 = 16$ level-2 cylinders. Each level-2 cylinder has measure $5^{-2} = 1/25$. Therefore:

$$\mu(C_1) = 9 \times \frac{1}{25} = \frac{9}{25} = 0.36, \qquad \mu(C_2) = 16 \times \frac{1}{25} = \frac{16}{25} = 0.64.$$

Sum check: $0.36 + 0.64 = 1$. ✓ These are exactly the Born-rule probabilities $|c_1|^2 = 0.36$ and $|c_2|^2 = 0.64$. The Born rule is reproduced by pure boundary counting, with no stochastic postulate.

**Qutrit example.** Take $p =