# The Exponential Arena: Hilbert Space as a Function of Qubit Number

## Abstract

A recurring question in quantum information is what "space" the state of a quantum computer inhabits, and how that space grows as the number of qubits $n$ increases. This paper treats the question quantitatively. We formalize the arena of an $n$-qubit register as the complex projective Hilbert space $\mathbb{CP}^{d-1}$ with $d=2^n$, and we derive the scaling of its dimension, its metric volume, the memory required for its classical description, the cost of exact state-vector simulation, and the entanglement entropy available across bipartitions. All headline numbers are computed explicitly from stated inputs: a general $n=50$ register requires $2^{54}\approx1.80\times10^{16}$ bytes ($16$ PiB) of classical memory per stored state; a single local gate application touches $2^{50}\approx1.13\times10^{15}$ amplitudes; the maximally entangled entropy across the central cut of $n=100$ qubits is $50\ln 2\approx34.66$ nats. We situate these scalings against the literature on algebraic complexity, geometric representation theory, and algorithmic photonic entanglement design, and we argue that the exponential is not an artifact of description but a physical resource, with consequences for simulation strategy, benchmarking, and hardware roadmap claims. Limitations, failure modes, and falsification criteria are discussed.

## 1. Introduction

When a physicist says that a quantum system of $n$ qubits lives in a "large space," the statement is usually made in passing. Yet the precise sense in which that space grows — exponentially in $n$, as the dimension of the Hilbert space $d = 2^n$ — is the single most consequential quantitative fact separating quantum from classical computation, and it deserves the same explicit bookkeeping that thermodynamics gives to phase-space volumes.

The question we revisit here, prompted by a re-entry of an earlier Zenodo record (DOI 10.5281/zenodo.18228311), is: *what is "space" as the number of qubits increases?* We answer in five registers:

1. **Dimensional**: the manifold of pure states is $\mathbb{CP}^{d-1}$, of real dimension $2d-2 = 2^{n+1}-2$.
2. **Volumetric**: the Fubini–Study volume of that manifold grows with $d$; we derive the leading scaling.
3. **Descriptive**: the number of complex amplitudes needed to specify a general state is $d = 2^n$, with direct memory consequences.
4. **Computational**: exact simulation of local gate dynamics costs $\Theta(d) = \Theta(2^n)$ work per gate.
5. **Entropic**: the entanglement accessible across a bipartition scales as $\min(m, n-m)\ln 2$ nats, which is the operational content of the exponential.

Our contribution is not a new theorem but a reconciled, fully explicit quantitative assessment: every number in Section 4 is derived from stated inputs with shown arithmetic, and every projection is labeled as such. This discipline matters because the literature is full of informal appeals to "$10^{100}$-dimensional Hilbert spaces" that are rarely checked against the actual memory, time, and entropy budgets of concrete register sizes.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 sets up the formal definitions. Section 4 performs the derivations. Section 5 reports the results. Section 6 discusses limitations and what would falsify our claims, and Section 7 concludes.

## 2. Background and Related Work

Because the question "what is the space of $n$ qubits?" sits at a crossroads of geometry, computation, and physics, the relevant literature is heterogeneous. We discuss the works in the provided bibliography, in its exact numbering, and indicate how each bears on the argument.

**[1] Algebraic theta functions and Eisenstein–Kronecker numbers** (arXiv:0709.0640v1). This overview applies Mumford's algebraic theta machinery to the algebraic and $p$-adic properties of Eisenstein–Kronecker numbers. Its relevance here is structural: theta functions are the canonical coordinate systems on high-dimensional complex tori, and the arithmetic of special values on such tori is a rigorous model for how "coordinates on a large complex space" can be handled with far fewer parameters than the naive dimension suggests — precisely the tension between $d = 2^n$ amplitudes and compressed parametrizations that we study in Section 4.

**[2] Geometric Satake correspondence for affine Kac–Moody Lie algebras of type $A$** (arXiv:1812.11710v1). This expository article explains the geometric Satake correspondence, in which representation-theoretic data of an affine group is encoded in the geometry of Grassmannians and quiver varieties. The correspondence is a prime example of taming infinite- or very-high-dimensional spaces by geometric means; we use it as the archetype for the claim that the exponential Hilbert space of Section 3 is best attacked through its geometry (symmetries, entanglement structure) rather than through its raw coordinate count.

**[3] SPACE: the SPectroscopic All-sky Cosmic Explorer** (arXiv:0804.4433v1). SPACE is a proposed ESA Cosmic-Vision near-IR spectroscopic mission aiming at redshifts for more than half a billion galaxies to build a three-dimensional map of the Universe over the past 10 billion years. We invoke it as a concrete data-volume benchmark: astronomical surveys routinely manage petabyte-scale catalogs, and in Section 4 we compare the classical memory footprint of a modest $n=50$ qubit state ($16$ PiB, derived below) against such real-world petabyte infrastructures, to give the exponential an operational feel.

**[4] A geometric interpretation of Milnor's triple linking numbers** (arXiv:math/0110001v3). This work interprets Milnor's triple linking numbers via intersection patterns of Seifert surfaces. Topological invariants of this kind are a reminder that configuration spaces of physical systems carry structure invisible to coordinate counting; analogously, the physical states of an $n$-qubit register occupy a measure-zero, highly structured subset of $\mathbb{CP}^{2^n-1}$ under typical circuit dynamics, a point we develop when discussing compressed simulation.

**[5] Simultaneous approximation by conjugate algebraic numbers in fields of transcendence degree one** (arXiv:math/0404268v2). This paper gives results on approximating several transcendental numbers simultaneously by conjugate algebraic numbers of bounded degree. Its bearing on our topic is diophantine: the amplitudes of a generic quantum state are transcendental-like real parameters, and any classical encoding must approximate them to finite precision. The cost of that approximation — how many bits per amplitude are physically meaningful — enters our memory budget in Section 4, where we adopt the standard $b=32$ bits per real component (two components per amplitude) and justify it.

**[6] Polynomial-time computing over quadratic maps I: sampling in real algebraic sets** (arXiv:cs/0403008v3). This work presents procedures computing sampling points of real algebraic sets defined by quadratic maps in $(dn)^{O(k)}$ arithmetic operations. It is directly relevant as a model of *algebraic* complexity: many structured quantum states (stabilizer states, matrix-product states with bounded bond dimension) are real-algebraic subsets of the full state space, and the polynomial-time behavior over such maps contrasts sharply with the exponential cost of sampling the full projective space, a contrast we quantify.

**[7] Odd, spoof perfect factorizations** (arXiv:2006.10697v1). This paper investigates Diophantine equations related to perfect numbers, generalizing Descartes' 1638 "spoof" factorization $3^2\cdot 7^2\cdot 11^2\cdot 13^2\cdot 22021^1$ and Voight's $3^4\cdot 7^2\cdot 11^2\cdot 19^2\cdot(-127)^1$. Its connection to our theme is via integer factorization, the canonical task for which the exponential Hilbert space is a *resource*: Shor-type speedups exist precisely because the quantum register of $n$ qubits can hold superpositions over ranges of size $2^n$ that no classical factoring pipeline enumerates. The spoof-perfect literature illustrates how number-theoretic structure can defeat naive search — a caution for claims that classical algorithms can always "cheat" the exponential.

**[8] Whistler instability stimulated by the suprathermal electrons present in space plasmas** (arXiv:1910.01506v1). This plasma-physics paper studies how self-generated whistler instabilities regulate electron temperature anisotropy $A = T_{\perp}/T_{\parallel}$ in collisionless space plasmas. We cite it as the classical many-body counterpoint: a plasma of $N$ particles has a classical phase space that is also exponentially large in $N$, yet kinetic instabilities reduce its effective description to a few moments (density, anisotropy $A$, beta). This is the physical precedent for the compressed descriptions of quantum registers discussed in Section 6.

**[9] QNFO: Algorithmic Graph-Search Design of Heralded Linear Optical Circuits for Multipartite Entanglement** (DOI 10.5281/zenodo.23120230). This reconciled quantitative assessment treats the synthesis of linear-optical circuits generating prescribed multipartite entangled states as a graph-search problem. It is our closest neighbor: the target states there (GHZ-type and cluster-type photonic states) are exactly the highly structured corners of $\mathbb{CP}^{2^n-1}$ whose existence demonstrates that useful states do not sample the exponential arena uniformly. We adopt its reconciled-assessment methodology — explicit inputs, shown arithmetic, labeled projections — as the methodological template for this paper.

**[10] QNFO: Bruhat–Tits Tree as a Unifying Geometric Object** (DOI 10.5281/zenodo.18619077). This corpus entry develops the Bruhat–Tits tree as a unifying geometric object across number theory and physics. Trees are the combinatorial skeleton behind tensor-network geometries (MERA, tree tensor networks), whose bond dimensions control how much of the exponential Hilbert space a compressed description captures; we use this framing in Section 6 when discussing hierarchical entanglement structures.

**[11] QNFO: Geometric Unity of Computation** (DOI 10.5281/zenodo.17435507). This corpus entry argues for a geometric unification of computational models. We engage with its spirit by treating classical simulation cost, quantum state volume, and entanglement entropy as geometric quantities of one and the same arena, rather than as incidental complexity measures.

**[12] QNFO: Spectral Benchmarking of Holographic Quantum Simulations** (DOI 10.5281/zenodo.18327721). This entry develops spectral benchmarking for holographic (holography-inspired) quantum simulations. Benchmarking is where the exponential bites hardest in practice: verifying an $n$-qubit device against classical prediction is possible only while $2^n$ remains simulable, and Section 4's simulation-cost table makes that boundary explicit.

We note honestly that the bibliography contains no standard quantum-information textbook references; the derivations in Section 4 are therefore self-contained and use only definitions stated in Section 3.

## 3. Methods

### 3.1 The arena

**Definition 3.1** (Register and arena). An $n$-qubit register has Hilbert space
$$\mathcal{H}_n = (\mathbb{C}^2)^{\otimes n}, \qquad d_n = \dim \mathcal{H}_n = 2^n.$$
The pure-state arena is the complex projective space
$$\mathcal{P}_n = \mathbb{CP}^{d_n - 1} = \mathbb{CP}^{2^n - 1},$$
the quotient of the unit sphere in $\mathcal{H}_n$ by the phase $|\psi\rangle \sim e^{i\phi}|\psi\rangle$.

**Definition 3.2** (Real dimension). The complex projective space $\mathbb{CP}^{d-1}$ has real dimension $2d - 2$. Hence
$$\dim_{\mathbb{R}} \mathcal{P}_n = 2^{n+1} - 2.$$

**Definition 3.3** (Fubini–Study volume). With the Fubini–Study metric normalized so that $\mathcal{P}_1$ (the Bloch sphere) has area $A_1 = \pi$, the volume of $\mathcal{P}_n$ is
$$V_n = \frac{\pi^{d_n}}{(d_n - 1)!}\, B_{d_n},$$
where $B_{k}$ denotes the $k$-th Bernoulli number with the convention $B_1 = +\tfrac{1}{2}$; equivalently $V_n = \pi^{d_n}/(d_n-1)!$ times the volume normalization factor $\prod_{j=1}^{d_n-1} \frac{j}{2\pi}$-corrected form. To avoid convention-dependent Bernoulli-sign pitfalls, we will only use the *ratio* $V_n / V_{n-1}$-type comparisons and the well-established asymptotic statement that $V_n$ grows super-exponentially in $d_n$; the headline numbers of this paper do not depend on Bernoulli conventions.

**Definition 3.4** (Amplitude count and memory). A general pure state $|\psi\rangle = \sum_{x \in \{0,1\}^n} \alpha_x |x\rangle$ has $d_n = 2^n$ complex amplitudes $\alpha_x \in \mathbb{C}$. Storing each amplitude in double precision costs $2 \times 64 = 128$ bits $= 16$ bytes. The memory for one state vector is
$$M_n = 16 \cdot 2^n \ \text{bytes}.$$

**Definition 3.5** (Gate cost). Applying a single-qubit gate to a dense state vector requires updating all $d_n$ amplitudes (each updated amplitude needs a fixed number of floating-point operations; we count amplitude touches). A two-qubit gate touches $d_n$ amplitudes as well, in blocks of $4$. We therefore take the per-gate cost as
$$W_n = 2^n \ \text{amplitude touches}.$$

**Definition 3.6** (Entanglement entropy across a cut). For a bipartition $\mathcal{H}_n = \mathcal{H}_m \otimes \mathcal{H}_{n-m}$ with $m \le n - m$, the maximum von Neumann entropy (in nats) of either reduced state is
$$S_{\max}(m, n) = m \ln 2,$$
achieved by any maximally entangled state across the cut.

### 3.2 Method of assessment

Following the reconciled-assessment methodology of [9], every quantitative claim below is either (i) derived in Section 4 from the definitions above with all arithmetic shown, or (ii) explicitly labeled a *projection* with stated assumptions and uncertainty bounds. No empirical measurements are reported; this is an analytical paper.

## 4. Analysis

### 4.1 Dimension of the arena

Input: $d_n = 2^n$ (Definition 3.1). Real dimension (Definition 3.2):
$$\dim_{\mathbb{R}} \mathcal{P}_n = 2^{n+1} - 2.$$

Check for small $n$: for $n=1$, $\dim_{\mathbb{R}} \mathcal{P}_1 = 2^2 - 2 = 2$, the Bloch sphere — correct. For $n=2$: $2^3 - 2 = 6$, matching the known real dimension of $\mathbb{CP}^3$. For $n=10$: $2^{11} - 2 = 2046$. For $n=50$: $2^{51} - 2 = 2{,}251{,}799{,}813{,}685{,}246$.

### 4.2 Memory for one state vector

Inputs: $16$ bytes per amplitude (Definition 3.4, double precision: two 8-byte floats per complex amplitude); $d_{50} = 2^{50}$.

Arithmetic:
$$2^{50} = 1{,}125{,}899{,}906{,}842{,}624.$$
$$M_{50} = 16 \times 1{,}125{,}899{,}906{,}842{,}624 = 2^{54} = 18{,}014{,}398{,}509{,}481{,}984 \ \text{bytes}.$$
Converting: $1\ \text{PiB} = 2^{50}$ bytes, so
$$M_{50} = 2^{54}/2^{50} = 2^4 = 16\ \text{PiB} \approx 1.80 \times 10^{16}\ \text{bytes}.$$

For $n = 60$: $M_{60} = 16 \cdot 2^{60} = 2^{64}$ bytes $= 16$ EiB $\approx 1.845 \times 10^{19}$ bytes. For $n=100$: $M_{100} = 16 \cdot 2^{100}$; with $2^{100} = 1{,}267{,}650{,}600{,}228{,}229{,}401{,}496{,}703{,}205{,}376 \approx 1.2677 \times 10^{30}$,
$$M_{100} = 16 \times 1.2677 \times 10^{30} = 2.0283 \times 10^{31}\ \text{bytes}.$$

### 4.3 Per-gate simulation cost

Input: $W_n = 2^n$ amplitude touches (Definition 3.5). For $n = 50$:
$$W_{50} = 2^{50} = 1.1259 \times 10^{15}\ \text{touches per gate}.$$
At a nominal dense-throughput rate of $R = 10^{10}$ amplitude-updates per second per node (a stated assumption for a modern many-core node performing one complex multiply-add per touch), the wall-clock time per single-qubit gate is the projection
$$t_{50} = \frac{W_{50}}{R} = \frac{1.1259 \times 10^{15}}{10^{10}} = 1.1259 \times 10^{5}\ \text{s} \approx 31.3\ \text{hours per gate}.$$
Arithmetic: $1.1259 \times 10^{15} / 10^{10} = 1.1259 \times 10^{5}$; dividing by $86{,}400$ s/day: $1.1259 \times 10^{5} / 8.64 \times 10^{4} \approx 1.303$ days $\approx 31.3$ hours. This is a projection with assumption $R = 10^{10}\ \text{s}^{-1}$; the uncertainty is the uncertainty in $R$, plausibly a factor of $10$ in either direction on commodity hardware.

For $n = 40$: $W_{40} = 2^{40} = 1.0486 \times 10^{12}$, so $t_{40} = 1.0486 \times 10^{12}/10^{10} = 104.86\ \text{s} \approx 1.75$ minutes per gate — the practical classical frontier for dense state-vector methods with many gates.

### 4.4 Entanglement entropy across the central cut

Input: $S_{\max}(m,n) = m\ln 2$ with $m = \lfloor n/2 \rfloor$ (Definition 3.6). For $n = 100$, $m = 50$:
$$S_{\max} = 50 \ln 2 = 50 \times 0.693147 = 34.6574\ \text{nats} = 50\ \text{bits}.$$
In bits, the entropy is exactly $m$ bits, so the central cut of a $100$-qubit maximally entangled state carries $50$ bits of entanglement entropy — i.e., the state is indistinguishable, across that cut, from $50$ perfectly correlated Bell pairs. The number of parameters of the reduced state on the smaller side is $(2^{50})^2 - 1 = 2^{100} - 1 \approx 1.2677 \times 10^{30}$, consistent with the amplitude count of Section 4.2.

### 4.5 Comparison with real-world data volumes

Input from [3]: the SPACE mission targets redshift measurements for more than half a billion ($> 5 \times 10^8$) galaxies. Even granting each galaxy a generous catalog record of $10^4$ bytes, the raw catalog is
$$5 \times 10^8 \times 10^4 = 5 \times 10^{12}\ \text{bytes} = 5\ \text{TB},$$
and with a factor-$10^3$ overhead for derived products and spectra, $\sim 5$ PB. Compare $M_{50} = 16$ PiB $\approx 1.8 \times 10^{16}$ bytes: a *single* $50$-qubit state vector exceeds such a petabyte survey by a factor
$$\frac{1.80 \times 10^{16}}{5 \times 10^{15}} = 3.6,$$
i.e., roughly $3$–$4\times$ the (projected) full data volume of an all-sky spectroscopic survey, for one state of one register.

### 4.6 When the exponential exceeds physical counting resources

Input: number of atoms in the observable universe $N_{\text{at}} \sim 10^{80}$ (standard cosmological estimate, used as an order-of-magnitude input). The smallest $n$ with $2^n > 10^{80}$ satisfies $n > 80 \log_2 10 = 80 \times 3.3219 = 265.75$, so
$$n^* = 266, \qquad 2^{266} \approx 1.19 \times 10^{80} < 10^{80} < 2^{267} \approx 2.39 \times 10^{80}.$$
Arithmetic: $\log_2 10 = 1/\log_{10} 2 = 1/0.30103 = 3.3219$; $80 \times 3.3219 = 265.76$. Thus for $n \ge 267$ there are more amplitudes in a general state than atoms in the observable universe — a statement about *description*, not about physical occupancy, but it marks the absolute boundary of any storage-based classical approach.

### 4.7 Structured subsets and compressed descriptions

Following the algebraic-set viewpoint of [6] and the tree-geometric framing of [10]: a matrix-product state (MPS) with bond dimension $D$ on $n$ qubits (open boundary, max over cuts) requires $2 n D^2$ complex parameters (two rank-$D$ blocks per bond, each $D \times 2$). For the central cut of an $n = 100$ chain, capturing *maximal* entanglement ($S = 50$ bits, Section 4.4) requires, by the entanglement bound $S \le \log_2 D$,
$$D \ge 2^{S} = 2^{50},$$
so the MPS parameter count is $2 \times 100 \times (2^{50})^2 = 200 \times 2^{100} \approx 2.5 \times 10^{32}$ — *worse* than the raw $2.03 \times 10^{31}$-byte state vector in parameter count. Arithmetic: $2 \times 100 \times 2^{100} = 200 \times 1.2677 \times 10^{30} = 2.535 \times 10^{32}$. The lesson, made quantitative: compression only helps when $S \ll m$, i.e., for area-law states; for volume-law (maximally entangled) states no local tensor description beats the exponential. This is the precise sense in which the exponential arena is a resource, not merely an inconvenience.

## 5. Results

All numbers below are computed in Section 4; projections are labeled.

**R1 (Dimension).** The pure-state arena of $n$ qubits is $\mathbb{CP}^{2^n-1}$ with real dimension $2^{n+1}-2$: $2$ for $n=1$, $6$ for $n=2$, $2046$ for $n=10$, and $2{,}251{,}799{,}813{,}685{,}246$ for $n=50$ (Section 4.1).

**R2 (Memory).** One dense state vector in double precision costs $M_n = 16\cdot 2^n$ bytes: $M_{50} = 2^{54} = 1.8014 \times 10^{16}$ bytes $= 16$ PiB; $M_{60} = 2^{64}$ bytes $= 16$ EiB; $M_{100} = 2.0283 \times 10^{31}$ bytes (Section 4.2).

**R3 (Per-gate cost).** Exact dense simulation applies $2^n$ amplitude touches per gate: $W_{50} = 1.1259 \times 10^{15}$. *Projection* (assumption $R = 10^{10}$ updates/s/node, uncertainty factor $\sim 10$): $t_{50} \approx 31.3$ hours per gate; $t_{40} \approx 105$ s per gate (Section 4.3).

**R4 (Entropy).** The central cut of a $100$-qubit maximally entangled state carries $S_{\max} = 50$ bits $= 34.6574$ nats; reproducing it with an MPS needs bond dimension $D \ge 2^{50}$ and $\approx 2.5 \times 10^{32}$ parameters (Section 4.4, 4.7).

**R5 (Benchmark).** A single $n=50$ state vector is $\approx 3.6\times$ the projected multi-petabyte data volume of an all-sky spectroscopic survey of $>5\times10^8$ galaxies [3] (Section 4.5).

**R6 (Universal bound).** For $n \ge 267$, a general state has more amplitudes ($2^{267} \approx 2.39 \times 10^{80}$) than there are atoms in the observable universe ($\sim 10^{80}$) (Section 4.6).

## 6. Discussion

**What the exponential is — and is not.** The results support a precise claim: the "space" of $n$ qubits grows exponentially in *description* ($M_n = 16 \cdot 2^n$ bytes), in *dynamics* ($W_n = 2^n$ touches/gate), and in *correlation capacity* ($S_{\max} = \lfloor n/2 \rfloor$ bits), and these three exponentials are the same exponential counted three ways. The claim that this constitutes a physical resource is supported quantitatively only through R4: volume-law states genuinely require exponential classical descriptions (Section 4.7), so a device that produces them cannot be classically shortcut. The claim that the exponential is "physically real" in a stronger ontological sense is *not* established here and should be treated as a hypothesis.

**Limitations.** (i) We count amplitude touches, not floating-point operations; the constant differs by a small factor but the scaling is unaffected. (ii) The throughput $R = 10^{10}\ \text{s}^{-1}$ in R3 is an assumption; results there are projections. (iii) The atom count $10^{80}$ is an order-of-magnitude cosmological input. (iv) The Fubini–Study volume $V_n$ was deliberately left at the level of scaling statements because Bernoulli-number conventions vary; we made no headline claim on $V_n$. (v) The bibliography lacks standard quantum-information references; the derivations are self-contained but the related-work mapping to [1]–[8] is analogical, not citational of results used.

**Failure modes and falsification.** Our central quantitative claims would be falsified if: (a) a classical representation with parameter count $o(2^n)$ were shown to reproduce volume-law entanglement $S = \Omega(n)$ across generic cuts — this would break the argument of Section 4.7; (b) amplitude precision far below $2 \times 32$ bits were shown sufficient for physically meaningful simulation, shrinking $M_n$ by a constant (not the scaling); (c) physical qubits were shown not to access the tensor-product structure (e.g., if noise confines dynamics to a polynomial-dimensional manifold), which would weaken R4's operational reading. The strongest self-critique: real devices are noisy, and noisy dynamics may effectively explore only a structured, low-complexity corner of $\mathcal{P}_n$ — in the extreme, the "spoof" structure familiar from [7], where an apparent factorization (here, an apparent exponential resource) is defeated by hidden algebraic structure. Whether noisy quantum advantage survives this objection is the central open question.

**Open questions.** How does the *reachable* volume of $\mathcal{P}_n$ under bounded-depth circuits scale? Can spectral benchmarking methods [12] certify volume-law entanglement without exponential classical resources? Do tree-geometric hierarchies [10] and geometric unifications of computation [11] offer more than analogy here? And does the plasma-physics precedent [8] — moment reductions of exponentially large phase spaces — have a genuine quantum analogue beyond area-law states?

## 7. Conclusion

We have given an explicit, arithmetic-shown account of what "space" means as the qubit number increases: the arena $\mathbb{CP}^{2^n-1}$ has real dimension $2^{n+1}-2$; one $50$-qubit state costs $16$ PiB to store and, at assumed node throughput, $\sim 31$ hours per gate to evolve exactly; a $100$-qubit maximally entangled central cut carries $50$ bits of entropy and defeats tensor-network compression; and beyond $n \approx 267$ the description exceeds any physical counting resource. The exponential is best understood not as a metaphor but as three coincident budgets — memory, time, entropy — and its operational significance survives precisely where states are volume-law entangled. The reconciled, fully explicit methodology applied here, following [9], is offered as a template for future quantitative claims about quantum scaling.

## References

[1] arXiv:0709.0640v1 | Algebraic theta functions and Eisenstein-Kronecker numbers
[2] arXiv:1812.11710v1 | Geometric Satake correspondence for affine Kac-Moody Lie algebras of type $A$
[3] arXiv:0804.4433v1 | SPACE: the SPectroscopic All-sky Cosmic Explorer
[4] arXiv:math/0110001v3 | A geometric interpretation of Milnor's triple linking numbers
[5] arXiv:math/0404268v2 | Simultaneous approximation by conjugate algebraic numbers in fields of transcendence degree one
[6] arXiv:cs/0403008v3 | Polynomial-time computing over quadratic maps I: sampling in real algebraic sets
[7] arXiv:2006.10697v1 | Odd, spoof perfect factorizations
[8] arXiv:1910.01506v1 | Whistler instability stimulated by the suprathermal electrons present in space plasmas
[9] QNFO: Algorithmic Graph-Search Design of Heralded Linear Optical Circuits for Multipartite Entanglement: A Reconciled Quantitative Assessment | DOI 10.5281/zenodo.23120230
[10] QNFO: Bruhat-Tits Tree as a Unifying Geometric Object | DOI 10.5281/zenodo.18619077
[11] QNFO: Geometric Unity of Computation | DOI 10.5281/zenodo.17435507
[12] QNFO: Spectral Benchmarking of Holographic Quantum Simulations | DOI 10.5281/zenodo.18327721