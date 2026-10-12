# Ultrametric Quantum Error Correction on Bruhat-Tits Trees: Energy Barriers, Threshold Bounds, and the Quantization Question

## Abstract

We study a conjectured passive fault-tolerance scheme in which logical qubits are encoded on a Bruhat-Tits (ultrametric) tree, with the claim that the energy barrier grows as $E_{\mathrm{barrier}}(d) = 2^d$ in tree depth $d$, yielding error thresholds exceeding those of actively syndrome-measured surface codes. The motivating evidence is a classical simulation reporting zero logical errors at $40\%$ physical error rates for depth $d \geq 3$ under majority-vote decoding on classical bits. We formalize the encoding, derive explicit majority-vote failure probabilities, and show that the reported zero-error observation is consistent with a logical error floor of order $3 \times 10^{-4}$ per run at $95\%$ confidence for $10^4$ trials, so the classical result alone does not establish an arbitrarily low error rate. We then derive a conservative union-bound threshold model for a binary tree geometry, obtaining a projected threshold $p_{\mathrm{th}}(d) = 4\,\varepsilon^{2^{1-d}}$ on the per-branch error probability for target logical failure $\varepsilon$, which approaches $0.25$ as $d$ grows; under a depolarizing convention this projects to $3 \times 0.0079 \approx 0.024$ at $d=3$ and $0.60$ at $d=7$. We identify the central open question: whether the strong triangle inequality confines quantum errors under superposition, entanglement, and coherent noise, or whether the observed advantage is a classical decoding artifact. We propose quantum Monte Carlo and tensor-network tests and state falsification criteria.

## 1. Introduction

Quantum error correction (QEC) protects fragile superposition states from decoherence, and its discovery transformed quantum information from an academic curiosity into a developing engineering discipline [6]. The dominant architectural paradigm — surface codes and related topological codes — achieves high thresholds but requires continuous active syndrome extraction, whose measurement overhead and latency are themselves error sources. A passive scheme, in which the geometry of the encoding itself suppresses logical errors without measurement, would be architecturally transformative if it could be quantized without loss.

This paper examines a specific conjecture: that encoding logical qubits on a Bruhat-Tits tree — the infinite $(q+1)$-regular tree associated to a local field, whose natural metric is ultrametric — yields passive fault tolerance with a geometric threshold theorem, and that the energy barrier scales as

$$E_{\mathrm{barrier}}(d) = 2^d$$

in tree depth $d$. The conjecture is motivated by a classical simulation, reported in the author's notebook notes, in which majority-vote decoding on classical bits embedded in a depth-$d \geq 3$ tree produced zero logical errors at $40\%$ physical error rates. Ultrametricity — the strong triangle inequality $d(x,z) \leq \max\{d(x,y),\,d(y,z)\}$ — is the hypothesized mechanism: in an ultrametric space there are no "midpoints" between distant points, so error paths cannot accumulate gradually along geodesics.

The central question, which we sharpen but do not resolve, is whether this confinement survives quantization. Classical majority vote acts on bits; quantum errors act linearly on amplitudes, and a superposition of error paths can interfere. The strong triangle inequality is a statement about distances between classical configurations; whether it constrains operator propagation on a Hilbert space is precisely what must be proven or simulated.

Our contributions are:

1. A formalization of tree-encoded majority-vote decoding and exact computation of its failure probabilities, showing that the reported classical result is real but bounded ($p_L \approx 0.290$ per block at $p = 0.4$ for one level, dropping to $\approx 0.0043$ after three concatenation levels).
2. A statistical reinterpretation of "zero logical errors" as a confidence bound, not a proof of vanishing error rate.
3. A conservative union-bound threshold model for the binary tree, giving the projected threshold curve $p_{\mathrm{th}}(d) = 4\,\varepsilon^{2^{1-d}}$ with full arithmetic.
4. A precise statement of the quantization problem — depolarizing, coherent, and entanglement-mediated noise on tree-encoded qubits — and a proposed simulation program with falsification criteria.

## 2. Background and Related Work

We review the supplied bibliography, which constrains what is and is not known about the ingredients of the conjecture.

[1] (arXiv:1311.2485v2, *Continuous-time quantum error correction*) investigates continuous-time QEC in which both noise and correction are continuous processes, based on continuous weak measurements and feedback from the point of view of the subsystem principle, which concerns where protected quantum information resides. This is directly relevant to passive schemes: a tree encoding that suppresses errors by geometry alone is a natural candidate for continuous-time protection without discrete syndrome rounds, and the subsystem principle offers a language for stating which degrees of freedom carry the logical qubit.

[2] (arXiv:1610.04013v1, *Entanglement-Assisted Quantum Error-Correcting Codes*) provides a self-contained introduction to entanglement-assisted QEC codes. Entanglement-assisted constructions use shared entanglement between encoder and decoder to relax code-construction constraints; for a tree encoding spanning a distributed system, assisted entanglement across branches is one mechanism by which quantum correlations could either help correction or, adversarially, propagate correlated errors across the ultrametric hierarchy.

[3] (arXiv:1712.01463v2, *On the missing branches of the Bruhat-Tits tree*) develops, for a local field $k$ and the two-by-two matrix algebra $A$ over $k$, a theory for computing the set of maximal orders in $A$ containing a given suborder; this set is a sub-tree of the Bruhat-Tits tree called the branch of the order, and branches have been used to study the global selectivity problem and to compute local embeddings. This is the arithmetic backbone of our geometry: it establishes the Bruhat-Tits tree as a concrete combinatorial object attached to local fields, and the "branch" construction suggests that logical code spaces could be identified with order-theoretic sub-trees, with the missing-branch structure controlling which error operators connect distinct logical sectors.

[4] (arXiv:quant-ph/0602157v1, *An Introduction to Error-Correcting Codes: From Classical to Quantum*) surveys QEC and notes, citing Preskill's claim that the 21st century would be the golden age of quantum error correction, that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes, while classical error control methods are well developed and offer lessons. This frames exactly our methodological stance: the tree scheme begins as a classical code, and the entire open question is the transfer of classical guarantees across the classical-to-quantum gap this survey identifies.

[5] (arXiv:quant-ph/0304016v2, *Quantum Computing and Error Correction*) introduces the main ideas of QEC — encoding, syndrome extraction, error operators, code construction — and shows that general noise and relaxation of a set of two-state quantum systems can always be understood as a combination of Pauli operators acting on the system, with each code correcting a subset of these errors. This Pauli decomposition is the workhorse of our Section 3 noise model: any analysis of whether ultrametric confinement survives quantization can be reduced, at the discrete level, to the propagation of Pauli errors through the tree.

[6] (arXiv:0811.3734v1, *Quantum error correction beyond qubits*) addresses the need to protect quantum superposition states from decoherence noise and treats QEC beyond the qubit setting, noting that the discovery of QEC turned quantum information into a developing field. Tree encodings naturally embed qudits and continuous-variable-like structures at internal nodes; the beyond-qubits framing supports generalizing the majority-vote tree to non-binary alphabets matched to the $(q+1)$-regularity of the Bruhat-Tits tree.

[7] (arXiv:1307.5892v4, *Error suppression and error correction in adiabatic quantum computation II: non-equilibrium dynamics*) starts from the premise that while adiabatic quantum computing has some robustness to noise, encoding, error suppression, and error correction are believed required to scale, derives a model for the dynamics of encoded AQC, and analyzes non-equilibrium behavior. Energy-barrier arguments of the kind conjectured here ($E_{\mathrm{barrier}}(d) = 2^d$) are the native currency of adiabatic protection; this work supplies the dynamical framework in which a barrier-scaling claim must ultimately be tested, since a static barrier only helps if the dynamics does not tunnel or thermally activate over it faster than the computation runs.

[8] (arXiv:2504.19833v1, *Quantum Error Correction in Quaternionic Hilbert Spaces*) proposes quaternion-based QEC strategies by extending quantum mechanics into quaternionic Hilbert spaces, defining quaternionic analogues of Pauli operators and gates with inner-product preservation, and giving an encoding scheme mapping logical qubits into quaternionic systems. This is an example of altering the underlying number-theoretic structure of the Hilbert space itself; our proposal is structurally analogous in replacing the Archimedean geometry of standard codes with an ultrametric (non-Archimedean) geometry.

[11] (*QNFO: The Ultrametric Foundation*) argues that positional notation is inherently an ultrametric tree of nested cycles, that the Archimedean line is a derived abstraction, and that recovering the native ultrametric resolves cascading errors across mathematics, physics, and quantum computing. This supplies the conceptual motivation for treating ultrametric hierarchy as computationally primary rather than incidental. [12] (*QNFO: Quantum Laws of Form*) consolidates quantum correspondences to Spencer-Brown's distinction-based construction of logic and physics, identifying open problem categories and extensions; it is cited as the project context in which distinction-tree encodings are being explored. Entries [9] and [10] (QNFO: Alpha Pi Project; QNFO: Ultrametric Quantum Gravity and Computation) are supplied without summary text, so no substantive claim is drawn from them here; they are listed as project-context references only.

No entry in the supplied bibliography contains a threshold theorem for ultrametric geometries, a quantum Monte Carlo study of tree codes, or a proof that the strong triangle inequality confines quantum error operators. The gap this paper targets is therefore genuine.

## 3. Methods

### 3.1 Encoding

Let $T_d$ denote the finite binary tree of depth $d$: a root, and every node at depth $< d$ having two children, giving $2^d$ leaves. A classical bit $b \in \{0,1\}$ is encoded by writing $b$ on every leaf; the logical information is the equivalence class of leaf configurations under leaf-wise bit flips on a minority. Decoding is majority vote over the $2^d$ leaves. The quantum proposal, not yet validated, is to encode a logical qubit in the $2^{d+1}$-dimensional leaf Hilbert space via a repetition-like map $|0\rangle_L \mapsto |0\rangle^{\otimes 2^d}$, $|1\rangle_L \mapsto |1\rangle^{\otimes 2^d}$, with the ultrametric distance on leaf configurations supplied by the Bruhat-Tits tree metric of [3]: for a local field $k$, the Bruhat-Tits tree is the building associated to $\mathrm{PGL}_2(k)$, and distances between vertices are ultrametric, satisfying

$$d_{\mathrm{BT}}(x,z) \leq \max\{d_{\mathrm{BT}}(x,y),\, d_{\mathrm{BT}}(y,z)\}.$$

### 3.2 Noise models

Following the Pauli-reduction of [5], we model discrete noise as independent Pauli errors. For the classical analysis we use an independent bit-flip channel with flip probability $p$ per leaf. For the quantum projections we use the depolarizing channel

$$\mathcal{E}_p(\rho) = (1-p)\,\rho + \frac{p}{3}\left(X\rho X + Y\rho Y + Z\rho Z\right),$$

so each non-identity Pauli occurs with probability $p/3$. Coherent noise is modeled as a systematic unitary rotation $e^{-i\theta Z/2}$ per leaf, deferred to Discussion.

### 3.3 Barrier model

The conjectured barrier $E_{\mathrm{barrier}}(d) = 2^d$ is interpreted as follows: a logical operator must act non-trivially on a set of leaves connecting two logical sectors; in the binary tree the minimal such connecting set at depth $d$ has weight $2^{d-1}+1$ (a strict majority of the $2^d$ leaves), and we take the barrier to be the minimal error weight, scaled as $2^d$. Under a thermal bath at temperature $T$ with per-leaf attempt rate $\Gamma_0$, the activated logical failure rate is modeled as

$$\Gamma_L(d) \leq \Gamma_0\, 2^{2^d}\, e^{-E_{\mathrm{barrier}}(d)/k_B T},$$

where $2^{2^d}$ is the number of majority-type error sets (union bound). This is deliberately conservative and is a projection, not a measurement.

## 4. Analysis

All inputs below are stated with their sources; all arithmetic is shown.

**Input 1.** Physical error rate $p = 0.4$ (author's notebook notes, classical simulation conditions).

**Input 2.** Majority-vote block size $n = 7$ (one concatenation level above the minimal odd block; used to expose the arithmetic transparently).

**Input 3.** Simulation trial count for the confidence bound: we analyze the reported "zero logical errors" claim for a generic run of $N = 10^4$ trials, since the notebook does not state $N$; this is an assumption, declared as such.

**Input 4.** Target logical failure probability for threshold projections: $\varepsilon = 10^{-6}$ (chosen convention; declared as such).

### 4.1 Exact majority-vote failure probability at $p = 0.4$, $n = 7$

The failure probability is

$$p_L^{(1)} = \sum_{k=4}^{7} \binom{7}{k}\, p^k (1-p)^{7-k}, \qquad p = 0.4.$$

Terms:

- $k=4$: $\binom{7}{4} = 35$; $0.4^4 = 0.0256$; $0.6^3 = 0.216$; product $35 \times 0.0256 \times 0.216 = 35 \times 0.0055296 = 0.193536$.
- $k=5$: $\binom{7}{5} = 21$; $0.4^5 = 0.01024$; $0.6^2 = 0.36$; product $21 \times 0.01024 \times 0.36 = 21 \times 0.0036864 = 0.0774144$.
- $k=6$: $\binom{7}{6} = 7$; $0.4^6 = 0.004096$; $0.6^1 = 0.6$; product $7 \times 0.004096 \times 0.6 = 7 \times 0.0024576 = 0.0172032$.
- $k=7$: $\binom{7}{7} = 1$; $0.4^7 = 0.0016384$; product $0.0016384$.

Sum:

$$p_L^{(1)} = 0.193536 + 0.0774144 + 0.0172032 + 0.0016384 = 0.289792.$$

So one level of majority vote at $p = 0.4$ fails with probability $\approx 0.290$ — better than the bare $0.4$, but far from zero. The reported "zero logical errors" therefore cannot correspond to a single level at $n=7$; it must reflect deeper concatenation or larger blocks, which motivates the next computation.

### 4.2 Concatenation dynamics

Treat the output of level 1 as the input to level 2 (majority vote of 7 corrected bits, errors now independent with $q = p_L^{(1)} = 0.289792$):

$$p_L^{(2)} = \sum_{k=4}^{7} \binom{7}{k} q^k (1-q)^{7-k}.$$

Compute with $q = 0.289792$, $1-q = 0.710208$:

- $q^2 = 0.289792^2 = 0.08397939$; $q^4 = 0.08397939^2 = 0.00705254$; $q^5 = q^4 \cdot q = 0.00204385$; $q^6 = 0.00059231$; $q^7 = 0.00017166$.
- $(1-q)^3 = 0.710208^3$: $0.710208^2 = 0.50439540$; $\times\,0.710208 = 0.35823302$. $(1-q)^2 = 0.50439540$.
- $k=4$: $35 \times 0.00705254 \times 0.35823302 = 35 \times 0.00252613 = 0.08841455$.
- $k=5$: $21 \times 0.00204385 \times 0.50439540 = 21 \times 0.00103093 = 0.02164953$.
- $k=