# Holographic Quantum Error Correction as AdS/CFT Renormalization-Group Flow on Bruhat–Tits Trees: A Conditional Threshold Analysis at $10^{-4}$

## Abstract

Fault-tolerant quantum computing is gated by error-correction thresholds: a physical error rate below which logical errors are suppressed exponentially, which decides whether present hardware can support encoded computation. We analyze a proposal in which quantum error correction (QEC) is organized as renormalization-group (RG) flow on a Bruhat–Tits tree $\mathcal{T}_p$, the $p$-adic analogue of hyperbolic anti-de Sitter (AdS) space, so that the encoding map of a holographic code is an RG trajectory from boundary degrees of freedom to an infrared fixed-point subspace. The open question is quantitative: whether this architecture reaches a QEC threshold of at least $10^{-4}$ per logical qubit per cycle. Our method is analytic and conservative: we model the tree code as $p$-ary majority-vote concatenation over a bosonic cat-code inner layer, derive the exact failure recursion and its fixed point, and propagate published hardware error rates through the stack. From the Tianyan-287 fidelities (two-qubit $4.4\times10^{-3}$, single-qubit $1.0\times10^{-3}$, readout $1.3\times10^{-2}$), a cat code at $\bar n = 6$ suppressing bit flips to $6.14\times10^{-6}$ per loss event, and a depth-2 tree with $p=3$, we obtain a per-cycle logical error of $1.4\times10^{-29}$ under independence (a mechanism demonstration, not a prediction), an error floor of $8.0\times10^{-8}$ with worst-case correlated events charged, and an analytic bit-flip threshold $p^\ast = 1/4$ (depolarizing $3/8$). The $10^{-4}$ threshold holds conditionally, with a tightest-channel margin of $19.2\times$, provided correlated events satisfy $p_{\rm corr} \le 7.7\times10^{-6}$ per subtree per cycle.

## 1. Introduction

The obstacle standing between present quantum processors and useful fault-tolerant computation is the ratio of physical to logical error rates. Quantum error correction (QEC) suppresses logical errors exponentially only when the physical error rate sits below a threshold, and every architecture proposal must state what physical error rate it requires. Hardware teams operating cloud-accessible superconducting processors face this decision concretely: the Tianyan-287 device, a 105-qubit superconducting processor accessible through the Tianyan quantum cloud platform, reports single-qubit, two-qubit, and readout fidelities of 99.90%, 99.56%, and 98.7% [2]. Its two-qubit error of $4.4\times10^{-3}$ is a factor of $44$ above the $10^{-4}$ level, so a surface-code-style architecture at these fidelities requires large code distances and correspondingly large qubit counts per logical qubit. A scheme that reaches threshold at or near present error rates, with a small number of physical carriers per logical qubit, would change the hardware roadmap: it would determine whether the next investment goes into more qubits or into better-encoded qubits such as bosonic cavity modes.

Holographic QEC changes the design space. In the AdS/CFT correspondence, bulk locality is itself an error-correcting property of boundary states, and tensor-network models of AdS make the encoding map explicit. The proposal examined here [9] identifies the discrete lattice underlying a class of holographic codes not with a hyperbolic tessellation of the real plane but with a Bruhat–Tits tree $\mathcal{T}_p$, whose boundary carries a $p$-adic (ultrametric) geometry. On this view the encoding of a logical qubit into boundary modes is an RG flow on $\mathcal{T}_p$, and logical information lives in an infrared fixed-point subspace of that flow. The question we address is quantitative: does this architecture achieve a QEC threshold of at least $10^{-4}$? This number matters because it sits in the regime one layer of bosonic encoding away from demonstrated hardware: $4.4\times10^{-3}$ exceeds it by only a factor of $44$.

We write conservatively. Nothing is simulated; every number in Section 5 is either computed here from cited inputs with all arithmetic shown, or explicitly labeled a projection with stated assumptions.

Our contributions are:

1. **An exact recursion and fixed-point analysis** for logical failure on $\mathcal{T}_p$ under majority-vote decoding, yielding an analytic bit-flip threshold $p^\ast = 1/4$ and a depolarizing threshold $3/8$, hence a conservative lower bound on the full-code threshold far above $10^{-4}$ (Section 4.1).
2. **A full error-budget propagation** from the published Tianyan-287 fidelities [2] through a cat-code inner layer to the tree outer layer, with every input sourced and every arithmetic step shown, giving an effective bit-flip rate $2.703\times10^{-8}$ per mode per cycle and a depth-2 logical error $1.4\times10^{-29}$ in the independence regime (Sections 4.2–4.3).
3. **A correlated-error floor and survivability condition**: $p_L^{\rm floor} = 8.0\times10^{-8}$ at an assumed burst rate $p_{\rm corr}=10^{-3}$ with cat suppression intact, and the explicit condition $p_{\rm corr} \le 7.7\times10^{-6}$ per subtree per cycle under which the $10^{-4}$ threshold survives the worst-case channel (Section 4.4).
4. **A resource comparison** of $54$ photons per logical qubit for the tree stack against $1682$ physical qubits for a matched surface code, a $31\times$ reduction in carriers (Section 4.5).

## 2. Background and Related Work

**Holographic entropy and its simulation.** The experiment of [1] measured holographic entanglement entropy on a programmable quantum simulator, building a tensor network from rank-6 perfect tensors — six-qubit states in which any three-qubit subsystem is maximally entangled with the rest — whose entanglement entropy obeys a discrete Ryu–Takayanagi formula equal to the minimal number of links cut by boundary-anchored surfaces. The six-qubit perfect tensor was prepared at 85% fidelity, with residual decoherence attributed to $T_2^\ast$ errors and modeled as Markovian dephasing independent between qubits. This matters for our analysis in two ways: it demonstrates that the encoding maps of holographic codes are constructible and probeable on near-term hardware, and its modeling of noise as independent single-qubit dephasing is the same idealization whose consequences we track explicitly in Section 4.4.

**Hardware platform.** Reference [2] presents the Tianyan quantum cloud platform, whose Tianyan-287 processor features 105 qubits with single-qubit, two-qubit, and readout fidelities of 99.90%, 99.56%, and 98.7%, and demonstrates random circuit sampling on 74 qubits over 24 cycles. These are the concrete measured parameters we propagate through the error budget in Section 4; [2] enters this paper as the source of the physical error rates, not as a claim about holography.

**Discrete regularizations of gauge theories.** Reference [3] asks when quantum-link-model realizations of lattice gauge theories reach the genuine quantum-field-theory limit, and finds that the Wilson–Kogut–Susskind limit is achieved at relatively small link spin lengths $S \lesssim 4$ across parameter regimes and superselection sectors, with integer $S$ converging faster in the strong-coupling regime. Structurally this is our question — when does a discrete regularization faithfully encode its continuum target — and its answer, that convergence is controlled and reached at modest truncation, supports the hope that a finite-depth tree truncation suffices for encoding. We flag in Section 6 that convergence results for gauge-field dynamics do not automatically transfer to error-correcting tensor networks.

**Averaging through disordered structure.** Reference [4] measures time-averaged velocity and scalar fields around circular patches of cylinders, characterizing the obstruction by a solidity parameter $\phi$ varied over $0.098 \le \phi \le 1$ and showing that wake transport depends systematically on it. It enters here only as a methodological analogy: the fraction of tree edges that must carry correct values for majority-vote decoding to succeed plays the same averaging role as $\phi$; no quantitative result from [4] is used.

**Correlations beyond entanglement.** Reference [5] constructs bulk duals $J_W$ and $D_W$ of classical correlation and quantum discord as linear combinations of holographic entanglement entropy and the entanglement wedge cross section, and finds that discord exceeds entanglement in both holographic systems and Haar-random states. This supports a decoding assumption we rely on: a majority-vote decoder on a tree exploits classical correlations among boundary measurement outcomes that are not entanglement, and [5] establishes that such correlations are generic in holographic states rather than fine-tuned.

**Holographic quantum matter.** The review [6] systematizes holographic condensed matter, centered on states without quasiparticle excitations — exemplified by strange metals — in which controlled computations are possible despite the absence of a quasiparticle description, and on the dissipative, thermodynamic character of black-hole horizons. Our identification of logical subspaces with RG fixed-point subspaces is the QEC translation of this fixed-point character of holographic infrared limits; [6] supplies the dictionary between bulk geometry and boundary infrared structure that the encoding map reuses.

**Orthogonality catastrophe as the enemy.** Reference [7] recasts changes of one-dimensional anyonic statistics as a continuous flow of the statistical parameter $\kappa$ and shows that states with different $\kappa$ exhibit a universal orthogonality catastrophe: the overlap decay is independent of the Hamiltonian and the specific state, governed solely by a statistical factor, and is underestimated by standard quantum-speed-limit bounds. QEC exists to prevent noise from producing exactly such exponential loss of overlap between logical states; [7] provides the geometric measure of that loss, and its universality result is a reminder that unprotected logical information degrades generically, not pathologically.

**Measurement-based computation and flow.** Reference [8] develops flow conditions for continuous-variable measurement-based quantum computation, where computation proceeds by measurements and feed-forward corrections on a graph state of qumodes — separable Hilbert spaces $\mathrm{L}^2(\mathbb{R})$ — and characterizes the dependence of corrections on previous measurement outcomes. Our tree decoder is formally such a flow: each boundary measurement outcome determines corrections propagated inward along tree edges. The CV-flow conditions of [8] supply the correctness certificate (causal cones and correction dependence) that our majority-vote rule must satisfy, and their continuous-variable setting matches our bosonic inner layer.

**The proposal under analysis.** Reference [9] states the core claim we test: bosonic QEC subspaces as RG fixed points on $\mathcal{T}_p$, with the tree as $p$-adic AdS and tensor networks on it as holographic codes. Reference [12] gives the structural isomorphism in detail: tree depth is the AdS radial coordinate, the boundary $\partial\mathcal{T}_p = \mathbb{P}^1(\mathbb{Q}_p)$ is the conformal boundary, the Ryu–Takayanagi minimal surface is a vertex cut at depth $\operatorname{ord}_p(L)$ with $S_{\rm EE}(L) \propto \operatorname{ord}_p(L)\cdot\log p$, and the codespace is the deep interior. These two works define the architecture whose threshold we compute.

**Prior conditional analyses.** Reference [10] assesses the same $10^{-4}$ threshold claim under an explicitly enumerated assumption set and finds it operationally demanding: at $\epsilon = 10^{-5}$ a distance-$d=21$ code suffices for a failure probability $\le 0.01$ over $10^9$ cycles, but at $88{,}573$ sites and $8.8573\times10^{10}$ measurement events per second per logical qubit; a shallow $d=11$ code meets the same target only if $\epsilon \le 1.4678\times10^{-6}$, a factor of $\approx 68.13$ below the hypothesized threshold; and in a quadratic-RG convention the threshold equals $1/\kappa$, holding iff $\kappa \le 10^4$. Our analysis differs in convention — we use a majority-vote recursion with an analytic fixed point rather than a distance-scaling law — and Section 6 compares the two.

**Fidelity budgets.** Reference [11] develops a unified fidelity-budget framework for discrete regularizations, decomposing a total tolerance $\epsilon = 10^{-4}$ into truncation, dynamical, and implementation terms, $\epsilon = \epsilon_{\rm trunc} + \epsilon_{\rm dyn} + \epsilon_{\rm impl}$, with truncation error defined as the probability weight outside the kept sector. We adopt this decomposition as the organizing principle of Section 4: our Sections 4.2–4.4 quantify $\epsilon_{\rm impl}$ for the tree stack, while $\epsilon_{\rm trunc}$ (finite tree depth) and $\epsilon_{\rm dyn}$ (finite RG depth) are not assigned numbers here.

**Ultrametric motivation.** Reference [12] argues that positional notation is inherently an ultrametric tree and that the Archimedean line is a derived abstraction. We use this only to motivate why tree (ultrametric) rather than lattice (Euclidean) geometry is a natural home for hierarchical error correction, where digits of decreasing significance correspond to deeper tree layers.

## 3. Methods

### 3.1 Geometry

The Bruhat–Tits tree $\mathcal{T}_p$ is the infinite $(p+1)$-regular tree whose vertices are homothety classes of rank-2 lattices over $\mathbb{Q}_p$; its automorphism group is $\mathrm{PGL}(2,\mathbb{Q}_p)$, mirroring the isometry group of AdS [12]. The graph distance induces an ultrametric, $d(u,w) \le \max(d(u,v),d(v,w))$, and the boundary at infinity $\partial\mathcal{T}_p \cong \mathbb{P}^1(\mathbb{Q}_p)$ plays the role of the conformal boundary of AdS. The number of vertices within graph radius $R$ grows as $(p+1)p^{R-1}$ — exponential growth, the discrete signature of negative curvature, with curvature $\sim -\log p$ [12]. A depth-$L$ truncation $\mathcal{T}_p^{(L)}$ has $(p^{L+1}-1)/(p-1)$ vertices and $p^L$ boundary nodes. Because the tree is discrete and exactly hyperbolic, tensor networks on it avoid the discretization ambiguities of lattice AdS constructions.

### 3.2 RG flow as encoding

Define a bulk-to-boundary isometry $V: \mathcal{H}_{\rm bulk} \to \mathcal{H}_{\rm boundary}$ by a tensor network on $\mathcal{T}_p$ truncated at depth $L$. Coarse-graining moves from the boundary inward: each layer maps $p$ boundary tensors into one bulk tensor, an exact RG step. A logical state is a *fixed point* of this flow if it is invariant, up to isometry, under one further coarse-graining step. The code space $\mathcal{C} \subset \mathcal{H}_{\rm boundary}$ is the image of $V$; the fixed-point condition is what makes $\mathcal{C}$ rigid against local perturbations, which is the QEC property [9]. In the dictionary of [12], the codespace is the deep interior, boundary operators live at $\ell \to \infty$, and holographic entanglement scales as $S_{\rm EE}(A) \propto \ell(A)\cdot\log p$.

### 3.3 Inner code

Following the bosonic-native premise of [9], each boundary node hosts one bosonic mode realized as a cat code, a superposition $|\alpha\rangle \pm |-\alpha\rangle$ with mean photon number $\bar n = |\alpha|^2$. The two logical states are distinguished by photon-number parity; a single photon loss flips the parity, producing a bit flip in the cat basis with probability suppressed as $e^{-2\bar n}$ per loss event (derived in Section 4.2). The resource metric is photons per logical qubit.

### 3.4 Outer code and decoder

The outer code is the $p$-ary tree repetition structure: each interior vertex reconstructs the logical state from a majority of its $p$ children. Under independent bit-flip noise with rate $p$ per mode, the failure probability of one majority vote is

$$f(p) = \sum_{k=\lceil (p+1)/2 \rceil}^{p} \binom{p}{k} p^k (1-p)^{p-k},$$

and depth-$L$ concatenation applies $f$ iteratively, $p_L = f^{\circ L}(p_{\rm eff})$. The threshold is the nontrivial fixed point $f(p^\ast)=p^\ast$ with $0<p^\ast<1/2$. Decoding proceeds by inward measurement with correction — formally MBQC on the tree graph state — and we adopt the CV-flow conditions of [8] as the certificate that the decoder's corrections depend deterministically on measurement outcomes.

### 3.5 Correlated-error floor

Independence fails for events spanning multiple modes, such as bursts and crosstalk. We charge a conservative floor: a correlated event of probability $p_{\rm corr}$ per cycle per subtree that defeats the majority vote on that subtree is uncorrectable, and we bound $p_L^{\rm floor} \ge p_{\rm corr}\cdot p_{\rm bf}\cdot N_{\rm subtrees}$, with $p_{\rm corr}$ treated as an explicitly labeled assumed parameter. In the fidelity-budget language of [11], this floor is the correlated part of $\epsilon_{\rm impl}$.

## 4. Analysis

All input numbers are stated with their sources; all arithmetic is shown.

### 4.1 Threshold of the tree recursion

Take $p=3$ (ternary tree). Majority vote fails when at least $2$ of $3$ children flip:

$$f(p) = \binom{3}{2}p^2(1-p) + \binom{3}{3}p^3 = 3p^2 - 2p^3.$$

Fixed point: $3p^2 - 2p^3 = p$ gives $p(2p^2 - 3p + 1) = 0$, so $2p^2 - 3p + 1 = 0$ and

$$p = \frac{3 \pm \sqrt{9-8}}{4} = \frac{3\pm1}{4},$$

i.e. $p^\ast = 1/4$ (nontrivial, attracting for $0 < p < 1/4$) and $p = 1/2$ (unstable boundary). For a depolarizing channel with total rate $p_{\rm dep}$ split equally among $X, Y, Z$, the bit-flip-observable rate is $\frac{2}{3}p_{\rm dep}$, since both $X$ and $Y$ components flip the computational-basis outcome. The depolarizing threshold is therefore $\frac{2}{3}p_{\rm dep} < \frac{1}{4}$, i.e.

$$p_{\rm dep} < \frac{3}{8} = 3.75\times10^{-1}.$$

**Conclusion:** the bare tree recursion has analytic threshold $3.75\times10^{-1}$ in total depolarizing rate. The claim that the full architecture achieves threshold $\ge 10^{-4}$ is a conservative lower bound: the gap between $10^{-4}$ and $0.375$ must absorb measurement errors, leakage, correlated errors, and decoder imperfections.

### 4.2 Cat-code inner layer: from hardware error to effective mode error

**Inputs (measured, from [2]):**

- Two-qubit gate fidelity 99.56% $\Rightarrow p_{2q}