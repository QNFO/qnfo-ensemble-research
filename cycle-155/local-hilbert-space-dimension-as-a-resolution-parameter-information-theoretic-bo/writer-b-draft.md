# Local Hilbert-Space Dimension as a Resolution Parameter: Information-Theoretic Bounds for Qudit Quantum Cellular Automata as Substrates of Emergent Holographic Geometry

## Abstract

Discrete models of quantum gravity lack a computable criterion for when their emergent geometry becomes semiclassical, and the system sizes at which quantum cellular automata (QCA) show holographic entanglement structure remain unreachable by exact simulation. We ask whether enlarging the local Hilbert space from qubits to qudits lowers the system size $N$ at which continuum-like behavior appears. We develop the analytical framework for qudit QCA with local dimension $d$: we derive the exact scaling of Hilbert-space dimension $d^{N}$, the maximum cut entanglement $S_{\max}=\min(|A|,|B|)\log_{2}d$, the site-count equivalence $N_{d}=N_{q}/\log_{2}d$ between qudit and qubit chains at matched information capacity, and the per-gate simulation overhead $d^{2}/4$ at matched Hilbert dimension. These bounds give concrete numbers: a $d=3$ chain of 16 sites carries the entropy capacity of a 26-site qubit chain (a 36.9% site saving) at 2.25× the per-gate simulation cost, and a $d=4$ chain of 12 sites matches a 24-site qubit chain at 4× cost. We propose a falsifiable protocol comparing Ryu-Takayanagi-style entropy curves across $d$ at matched capacity. The central conjecture — that emergence thresholds scale as $1/\log_{2}d$ — is stated as a projection with explicit assumptions, and the smallest simulation that would confirm or refute it is specified.

## 1. Introduction

Researchers building discrete models of quantum gravity face a concrete, unresolved problem: they cannot compute, for a given discrete substrate, at what system size its emergent geometry stops looking like a lattice and starts looking like a smooth manifold. In the holographic program, the bulk geometry of a region is encoded in the entanglement structure of its boundary degrees of freedom, so the question becomes operational: at what system size $N$ does the entanglement entropy of a discrete quantum system follow the area-law-geodesic scaling that signals a semiclassical bulk? For qubit quantum cellular automata — lattices of finite-dimensional quantum systems evolving under local unitary dynamics — exact simulation is bounded by state vectors of dimension $2^{N}$, and candidate holographic behavior has only been certified at sizes of order twelve qubits [9]. Larger qubit chains, where a genuine continuum limit could be observed, exceed classical memory: a 40-qubit state vector requires $2^{40}$ complex amplitudes. The field is therefore stuck between toy sizes too small to show geometry and continuum sizes too large to simulate.

This gap has a cost. Without a tunable parameter that moves the emergence threshold to smaller $N$, every investigation of emergent geometry in locally unitary dynamics is confined to the regime where finite-size effects dominate, and no statement about the approach to smooth-manifold behavior can be tested. If local Hilbert-space dimension $d$ acts as a resolution parameter — so that a $d$-level chain reaches continuum-like entanglement scaling at a system size shrinking as $1/\log_{2}d$ — then the accessible simulation window opens dramatically: the same classical computer that simulates 28 qubits exactly can simulate 14 four-level sites, and the entanglement structure at those two sizes carries identical information capacity. The decision that changes is which automata a theorist screens for holographic behavior, and how small a prototype must be before a claim about emergent geometry is testable at all.

The physical motivation for treating $d$ as a resolution knob is independent of simulation convenience. In the p-adic pre-geometric program, the continuum manifold of general relativity is replaced by a discrete hierarchical substrate precisely because the continuum description breaks down at the Planck scale [10]; the open question in that program is how a computable discrete substrate generates smooth effective geometry. In stochastic and classical cellular automata, the trade-off between alphabet size and neighborhood size is structural: the number of states can be decreased at the cost of a larger neighborhood, and conversely the number of inputs can be decreased by enlarging the alphabet [6]. Quantum mechanically, the analogous trade-off has never been quantified for geometric emergence: no prior work derives how the system size needed for semiclassical entanglement scaling depends on the local dimension $d$.

This paper does not claim to have simulated qudit QCA at holographic scale. It derives the exact information-theoretic bounds that any such simulation must satisfy, quantifies the simulation cost of testing the conjecture, and specifies the smallest experiment that would confirm or refute it. The contributions are:

- Derivation of the exact entropy-capacity equivalence between qudit and qubit chains, $N_{d}=N_{q}/\log_{2}d$, with worked numbers for $d=3$ and $d=4$ (Section 4.2).
- Derivation of the per-gate classical simulation overhead $d^{2}/4$ at matched Hilbert-space dimension, showing that qudit enlargement is polynomially, not exponentially, more expensive (Section 4.3).
- Derivation of the mutual-information and Ryu-Takayanagi-style scaling bounds $I(A:B)\leq 2\min(|A|,|B|)\log_{2}d$ and $S(L)\leq L\log_{2}d$ that define the observable signatures of the conjecture (Section 4.4).
- A projection, with stated assumptions, that the emergence threshold scales as $N^{\ast}(d)\propto 1/\log_{2}d$, giving candidate thresholds $N^{\ast}\approx 20$ (d=2), $13$ (d=3), $10$ (d=4) at a 5% discretization criterion (Section 4.5, Section 5).
- Specification of the minimal falsification protocol: exact state-vector simulation at $d\in\{2,3,4\}$, $N\leq 14$, comparing entropy-curve convergence at matched Hilbert dimension (Sections 5 and 7).

## 2. Background and Related Work

Classical cellular automata research supplies the structural vocabulary for the quantum setting, and several of its results constrain what a qudit QCA program can assume.

The classification of one-dimensional automata is itself a difficult and partially undecidable problem. The survey of elementary cellular automata classifications [1] records that Culik II and Yu proved in 1988 that classifications of this kind are undecidable, while the same survey tabulates Wolfram's four behavioral classes — uniform, periodic, chaotic, and complex — over the 256 elementary rules, with 8 rules in class I. It also shows that composing a chaotic rule with a memory function can convert chaotic behavior into complex behavior. For the present program this is a warning and an opportunity: behavioral class in a qudit QCA cannot be inferred from $d$ alone, but rule transformations that shift class suggest that structured rule families, not exhaustive search, are the way to navigate the $d^{d^{k}}$-sized rule spaces of higher-dimensional local rules.

Rule-space size is quantified explicitly in the iso-rule paradigm of [2], which gives the rule-table size of a generic CA with $v$ states and $k$ inputs as $S_{r}=v^{k}$ and shows that structured families (totalistic, outer-totalistic, iso-rules) shrink this to $S_{k}=(v+k-1)!/(k!\times(v-1)!)$ and smaller, with the general ordering $S_{r}>S_{i}>S_{k}>S_{t}$. The same work argues that isotropy — equivalent dynamics in all directions — is the proper canvas for logical universality in CA. Both points transfer directly: a generic two-input qudit rule with $d=3$ has $S_{r}=3^{2}=9$ table entries, but the semigroup-structured subfamily studied in [6] contains only 18 rules, and imposing isotropy on a qudit lattice restricts the search in the same way the iso-rule paradigm restricts the binary case.

The trade-off between alphabet size and neighborhood size is stated as a theorem-adjacent fact in [6]: for one-dimensional CA the number of states and the number of inputs are not independent, since states can be traded against inputs in either direction. That work then proves that all 18 ternary CA rules induced by semigroups of order 3 are solvable, with explicit solution formulae $f^{n}(x_{0},\ldots,x_{n})=x_{0}\odot x_{1}\odot\cdots\odot x_{n}$ for idempotent semigroups, and shows these formulae compute expected values and block probabilities along orbits under Bernoulli initial conditions. This is the strongest existing analytical handle on $d=3$ automata, and Section 4.5 uses the same idea — closed-form orbit statistics — as the analytical complement to simulation in the large-$d$ limit.

Decidability results bound what can be proven about QCA phase spaces. The work on decidability of one-dimensional CA [3] establishes, building on Sutner's result that the first-order theory of the phase space $\mathcal{S}_{\mathcal{A}}=(Q^{\mathbb{Z}},\longrightarrow)$ is decidable, that the graphs of one-dimensional CA are $\omega$-automatic, and recalls that injectivity and surjectivity were shown decidable by Amoroso and Patt. For the qudit program this means that structural questions about the phase space — reversibility above all, which a unitary QCA requires — remain algorithmically decidable as $d$ grows, so the enlargement of the local Hilbert space does not push the foundational questions past decidability.

Stochastic and asynchronous variants matter because any simulated qudit QCA will face noise and update-scheduling choices. The decomposition theory of stochastic CA [4] shows that a stochastic CA admits a cell-wise probability distribution representation and a continuous-CA (CCA) formulation based on a polynomial representation of the discrete rule, allowing the averaged behavior to be uncovered without sampling; it also notes that mean-field techniques apply to long-term behavior. The asynchronous survey [5] defines $\alpha$-asynchronous updating, in which each cell applies the rule with probability $\alpha$ per step, and reports that asynchrony can break the complexity of a rule and render it simpler to study. Both results shape the noise model of Section 3: qudit QCA diagnostics should be computed on the averaged (density-matrix or dephased) dynamics, and update asynchrony is a control variable, not just a nuisance.

On the physics side, the nonequilibrium study of probabilistic CA [7] states plainly that there is no derivation of PCA dynamics from more microscopic physical rules, and entertains the reversal: that PCA are more fundamental and standard physical descriptions must be derived from them. It also shows that detailed balance is not naturally installed for parallel-updating PCA because simultaneous neighbor updates can prevent gradient flow, and constructs the entropy-production measure $J_{i,n}(\sigma)=\log\frac{p_{i}(\sigma_{n}(i)|\sigma_{n-1})}{p_{i}(\sigma_{n-1}(i)|\sigma_{n})}$. A unitary QCA is the quantum analogue of the reversible, parallel-updating case, and the same tension — no energy function, no detailed balance — carries over, which is why Section 3 works with entanglement measures rather than Hamiltonian variational principles.

That CA dynamics can produce physically useful emergent behavior at all is demonstrated at applied scale in [8], which simulates granular flow in an hourglass on a 61×61 grid using a probabilistic CA with a modified Margolus neighborhood, reporting a few milliseconds per iteration and usable performance up to 4k resolution. The Margolus block-partition construction used there is also the standard way to build exactly unitary, reversible lattice dynamics, and its millisecond-scale cost on a classical machine is the practical precedent for the simulation-cost analysis of Section 4.3.

Within the quantum CA literature proper, the closest existing result is the twelve-qubit Fredkin-gate QCA study [9], which asks whether local unitary dynamics can generate the non-local information storage that holographic quantum error correction requires. It establishes a zero-versus-nonzero diagnostic contrast: Fredkin-class dynamics delocalize information across the chain at every erasure scale tested, while transport-class dynamics collapse to zero segment correlations at the first erasure, and it packages this as a decoder-free erasure-screening pipeline runnable on a laptop. That work is bounded by twelve qubits and by the proxy status of mutual information — exactly the size ceiling this paper's resolution parameter is designed to lower.

Finally, the broader QNFO program supplies the pre-geometric context. The p-adic spacetime toolkit [10] develops computable methods for a Bruhat-Tits-tree substrate, reports that a discrete Wheeler-DeWitt equation converged and that emergent time was mapped via thermodynamic RG flow, and frames the continuum manifold as mathematically exhausted at the Planck scale. The holographic optimization framework [11] proposes a structural duality between surface-area minimization in biological branching networks and spacetime-volume minimization in quantum circuits, reporting a biological fractal dimension $\mu\approx 2.51$ and a cross-domain correlation $r\approx 0.98$. The constructal-determinism synthesis [12] argues that deterministic, computationally dense substrates (with local computational index $LCI\approx 1.83$) on fractal invariant sets generate the observed stochasticity of quantum mechanics, with hidden variables in an ultrametric topology. These three works motivate the specific question studied here — how discrete substrates generate smooth effective geometry — but none of them addresses local Hilbert-space dimension as a control parameter; that gap is what this paper fills.

## 3. Methods

### 3.1 Model definition

We define a qudit quantum cellular automaton (QCA) as follows. The system is a one-dimensional chain of $N$ sites, each carrying a local Hilbert space $\mathcal{H}_{i}\cong\mathbb{C}^{d}$ with $d\in\{2,3,4,\ldots\}$; the total Hilbert space is

$$\mathcal{H}_{N}^{(d)}=\bigotimes_{i=1}^{N}\mathcal{H}_{i},\qquad \dim\mathcal{H}_{N}^{(d)}=d^{N}.$$

The dynamics is a translationally invariant local unitary: in one automaton time step, every site is updated by a two-site unitary $U_{d}$ acting on $(\mathcal{H}_{i},\mathcal{H}_{i+1})$, applied in a brickwork (Margolus-style) partition that alternates even and odd bonds between steps, following the block-partition construction used for reversible classical CA in [8]. A single time step is therefore

$$\mathcal{U}^{(d)}=\left(\mathbb{I}^{\otimes}U_{d}\right)\left(U_{d}\mathbb{I}^{\otimes}\right),$$

with the two factors acting on alternating bond partitions. Exact unitarity of the block partition guarantees reversibility, which the decidability results of [3] confirm is an algorithmically checkable property of the phase space at any $d$.

The two-site gate $U_{d}$ is an element of $U(d^{2})$. We do not fix a single gate; the protocol screens gate families, prioritizing conditional-swap (Fredkin-generalized) gates because the twelve-qubit study [9] certified that the Fredkin class, unlike transport class, delocalizes information across erasures — the redundancy signature that holographic error correction requires.

### 3.2 Observables

Three information-theoretic observables are computed on $\mathcal{H}_{N}^{(d)}$, all defined without reference to any decoder, following the decoder-free diagnostic philosophy of [9]:

1. **Cut entanglement entropy.** For a bipartition $A|B$ with $|A|$ contiguous sites, $S(A)=-\mathrm{Tr}\,\rho_{A}\log_{2}\rho_{A}$, bounded as derived in Section 4.1.
2. **Interval entropy curve.** $S(L)$ for intervals of length $L=1,\ldots,\lfloor N/2\rfloor$; the Ryu-Takayanagi correspondence predicts, in a semiclassical bulk, a curve that is linear at small $L$ and saturates, with the linear slope set by the central charge in CFT duals. Here the discrete analogue is the slope $\log_{2}d$ derived in Section 4.4.
3. **Mutual information.** $I(A:B)=S(A)+S(B)-S(A\cup B)$, the erasure-robustness proxy used in [9], with the bound derived in Section 4.4.

### 3.3 Noise and update model

Two perturbations are part of the protocol because the classical literature shows they change behavior qualitatively. First, dephasing noise on individual sites converts the pure state to a mixture; the averaged dynamics is then analyzed with the cell-wise probability and continuous-CA machinery of [4], which computes averaged behavior without sampling. Second, asynchronous update is introduced as the parameter $\alpha$, the per-step probability that each site participates in the update, following the $\alpha$-asynchronous scheme defined in [5]; $\alpha=1$ recovers the synchronous QCA. The survey [5] documents that asynchrony can break rule complexity, so $\alpha$ is swept rather than fixed.

### 3.4 Matched-capacity comparison design

The central methodological rule is that chains of different $d$ are only compared at matched information capacity, i.e., matched total Hilbert-space dimension $d^{N}=2^{N_{q}}$, because a $d=4$ chain of $N$ sites trivially carries more entropy than a qubit chain of the same $N$; an unmatched comparison would confound local dimension with system size. The equivalence $N_{q}=N\log_{2}d$ is derived in Section 4.2 and governs all cross-$d$ comparisons in this paper.

## 4. Analysis

Every input number in this section is either a definition of the model of Section 3, a value cited from a specific source, or an explicitly stated assumption. All arithmetic is shown.

### 4.1 Hilbert-space dimension and entropy capacity

The dimension of the total Hilbert space is $d^{N}$ by definition of the tensor product. For $N=12$ sites (the largest size for which a qubit QCA has been exactly characterized [9]):

$$d=2:\; 2^{12}=4096.$$
$$d=3:\; 3^{12}=531441.$$
$$d=4:\; 4^{12}=(2^{2})^{12}=2^{24}=16777216.$$

The ratio of qudit to qubit dimension at fixed $N$ is

$$\frac{3^{12}}{2^{12}}=\frac{531441}{4096}=129.7463\ldots,\qquad \frac{4^{12}}{2^{12}}=\frac{16777216}{4096}=4096.$$

The maximum entanglement entropy of a bipartition $A|B$ is the logarithm of the smaller Schmidt rank, which is $\min(|A|,|B|)$ qudit levels:

$$S_{\max}(A)=\min(|A|,|B|)\,\log_{2}d.$$

The per-site entropy capacity is $\log_{2}d$ bits. Numerically, using $\log_{2}3=\ln 3/\ln 2=1.0986123/0.6931472=1.5849625$:

$$\log_{2}2=1,\qquad \log_{2}3=1.5849625,\qquad \log_{2}4=2.$$

So each $d=3$ site carries 1.585 bits of entanglement capacity and each $d=4$ site carries 2 bits, against 1 bit for a qubit.

### 4.2 Site-count equivalence at matched capacity

Matching total entropy capacity between a qubit chain of $N_{q}$ sites and a $d$-level chain of $N_{d}$ sites requires $N_{q}\log_{2}2=N_{d}\log_{2}d$, hence

$$N_{d}=\frac{N_{q}}{\log_{2}d}.$$

Worked examples, rounding up to whole sites:

- $N_{q}=24$, $d=3$: $N_{d}=24/1.5849625=15.1424\ldots$, so $N_{d}=16$ sites. Site saving: $1-15.1424/24=0.3691$, i.e. 36.9% fewer sites (16 vs 24 after rounding).
- $N_{q}=24$, $d=4$: $N_{d}=24/2=12$ sites exactly, a 50% site saving.
- $N_{q}=28$, $d=4$: $N_{d}=14$ sites.

Equivalently, a $d=3$ chain of $N=16$ sites has capacity $16\times 1.5849625=25.36$ qubit-equivalent bits, matching a 25–26 site qubit chain; a $d=4$ chain of $N=14$ has capacity $28$ bits, matching 28 qubits exactly.

### 4.3 Classical simulation cost at matched dimension

Exact state-vector simulation stores $d^{N}$ complex amplitudes. At double precision (16 bytes per amplitude), the memory is $16\,d^{N}$ bytes. At matched Hilbert dimension $d^{N}=2^{N_{q}}$, memory is identical across $d$ by construction; the difference is the per-gate cost.

Applying a two-site gate $U_{d}$ (a $d^{2}\times d^{2}$ matrix) to the state vector requires, for each of the $d^{N-2}$ configurations of the remaining sites, one $d^{2}\times d^{2}$ matrix-vector product of cost $(d^{2})^{2}=d^{4}$ multiply-adds:

$$C_{d}(N)=d^{N-2}\cdot d^{4}=d^{N+2}.$$

For a qubit chain, $C_{2}(N_{q})=2^{N_{q}+2}$. At matched dimension $d^{N}=2^{N_{q}}$ the cost ratio is

$$\frac{C_{d}}{C_{2}}=\frac{d^{N+2}}{2^{N_{q}+2}}=\frac{d^{2}}{4}.$$

Numerically:

$$d=3:\;\frac{9}{4}=2.25,\qquad d=4:\;\frac{16}{4}=4.$$

This is the paper's key cost result: at equal information content, a qudit simulation costs a constant factor 2.25 (d=3) or 4 (d=4) more per gate than the equivalent qubit simulation — polynomial in $d$, not exponential in $N$. Concretely, the $d=4$, $N=14$ chain has $2^{28}=268435456$ amplitudes, requiring $16\times 268435456=4294967296$ bytes $=4.295$ GB of memory — the same memory as a 28-qubit state vector, with 4× the per-gate arithmetic.

For orientation, the largest exactly characterized QCA study to date used twelve qubits [9]; its state vector is $2^{12}=40