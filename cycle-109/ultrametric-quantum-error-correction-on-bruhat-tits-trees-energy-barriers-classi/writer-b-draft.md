# Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Passive Fault Tolerance, and the Quantization Question

## Abstract

We study a conjectured passive fault-tolerance scheme in which logical qubits are encoded on a Bruhat–Tits tree, the infinite homogeneous tree associated with a local field, whose natural metric satisfies the strong (ultrametric) triangle inequality. The conjecture states that the energy barrier against a logical error grows as $E_{\text{barrier}}(d) = 2^{d}$ in tree depth $d$, yielding passive protection without active syndrome extraction, with thresholds allegedly exceeding those of surface codes. We formalize the encoding, derive the barrier scaling from the ultrametric geometry, and analyze what the classical evidence — reported zero-logical-error simulations at $40\%$ physical error rates for $d \geq 3$ under majority-vote decoding on classical bits — does and does not establish. We show by explicit computation that iterated majority voting on an eight-leaf tree suppresses a $p = 0.4$ bit-flip rate to $\approx 5.55 \times 10^{-3}$ after two concatenation levels and $\approx 2.9 \times 10^{-10}$ after three, confirming that the classical result is a genuine threshold effect of the tree geometry rather than an artifact of repetition alone. We then identify the open quantization question: whether the strong triangle inequality confines quantum errors — superpositions, entanglement, coherent noise — or whether the advantage evaporates under full quantum channels. We give bounds under a thermal-activation model, state the conditions a quantum threshold theorem for ultrametric geometries must satisfy, and outline the quantum Monte Carlo and tensor-network tests that would settle the question.

## 1. Introduction

Quantum error correction (QEC) protects fragile superposition states from decoherence, and its discovery transformed quantum information from an academic curiosity into a developing engineering discipline [6]. The dominant architectural paradigm — stabilizer codes with repeated syndrome measurement, exemplified by the surface code — achieves fault tolerance actively, at the cost of a large overhead of ancilla qubits, measurement circuits, and real-time decoding. A passive alternative, in which the geometry of the encoding itself suppresses errors without measurement, would be architecturally transformative if it could be made to work for quantum information and not merely classical bits.

This paper investigates a specific passive proposal: encode logical qubits on a Bruhat–Tits tree. A Bruhat–Tits tree is the infinite $(q+1)$-regular tree associated with a local field $k$ (a field complete with respect to a non-Archimedean, or $p$-adic, absolute value); its geometry is ultrametric, meaning that distances satisfy the strong triangle inequality $d(x,z) \leq \max(d(x,y), d(y,z))$, so that every triangle is isosceles with the long side unique. Ultrametricity has been argued to underlie hierarchical structure far beyond number theory; in particular, positional notation itself forms an ultrametric tree of nested cycles, with the Archimedean real line a derived abstraction rather than the primitive object [11]. The Bruhat–Tits tree is the canonical geometric realization of this hierarchy: sub-orders of the matrix algebra $M_2(k)$ correspond to subtrees ("branches") of the tree, and these branches have been used to study the global selectivity problem and to compute local embeddings [3].

The conjecture under study, due to the author's notebook notes, is twofold: (i) the energy barrier against a logical error on a tree of depth $d$ scales as $E_{\text{barrier}}(d) = 2^{d}$; and (ii) this scaling yields passive fault tolerance with error thresholds far exceeding surface codes, without active syndrome measurement. The supporting evidence is classical: simulations using majority-vote decoding on classical bits reported zero logical errors at $40\%$ physical error rates for $d \geq 3$. The central open question, stated frankly, is whether the strong triangle inequality confines quantum errors under superposition, entanglement, and coherent noise, or whether the observed advantage is a classical decoding artifact.

Our contributions are:

1. A formalization of the tree encoding and a geometric derivation of the barrier scaling $E_{\text{barrier}}(d) = 2^{d}$ (Section 3).
2. An explicit arithmetic analysis of the classical majority-vote evidence, showing that iterated majority voting on an eight-leaf tree constitutes a genuine recursive threshold mechanism at $p = 0.4$, and computing the suppression levels (Section 4).
3. A bounding analysis of the quantum regime under a thermal-activation model, with the quantization gap stated as explicit hypotheses rather than results (Sections 4 and 5).
4. A specification of the quantum Monte Carlo and tensor-network simulations, and of the theorem that would need to be proved, that would resolve the open question (Sections 5 and 6).

We are careful throughout to separate what is derived, what is computed, what is reported by the source simulations, and what is conjecture. The paper's honest conclusion is that the classical evidence is real but classical, and that the quantum question remains open in a precise, testable sense.

## 2. Background and Related Work

**Continuous-time QEC.** Reference [1] investigates continuous-time quantum error correction (CTQEC), in which both the noise and the error-correcting operations are treated as processes continuous in time, based on continuous weak measurements and feedback, analyzed from the point of view of the subsystem principle — the statement that protected quantum information is identified with a subsystem of the full system. CTQEC is the natural foil to our passive proposal: it removes the discrete measurement circuit but retains active feedback. A genuinely passive scheme would go one step further, removing even the feedback loop and relying on the energy landscape of the encoding geometry.

**Entanglement-assisted codes.** Reference [2] provides a self-contained introduction to entanglement-assisted quantum error-correcting codes, which use shared entanglement between encoder and decoder as a resource. The supplied summary gives no further technical detail, but the relevance to our setting is structural: if ultrametric confinement fails for independent quantum errors, sharing entanglement across distant branches of the tree is one candidate mechanism for restoring a quantum correction capacity, and the entanglement-assisted framework is the standard language in which such a modification would be expressed.

**Bruhat–Tits trees in arithmetic.** Reference [3] develops the theory of maximal orders in the two-by-two matrix algebra $M_2(k)$ over a local field $k$, showing that the set of maximal orders containing a given suborder forms a subtree of the Bruhat–Tits tree, called the branch of the order, and that branches have been applied to the global selectivity problem and to computing local embeddings. This is the source of the geometric object we encode on: the tree is not an arbitrary graph but the incidence geometry of arithmetic over a non-Archimedean field, and its ultrametric distance is the $p$-adic valuation difference. Our conjectured barrier scaling is a statement about how logical operators must traverse this arithmetic tree.

**From classical to quantum codes.** Reference [4] surveys error-correcting codes from the classical to the quantum setting, noting — citing Preskill's claim that the 21st century would be the golden age of quantum error correction — that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes, while classical error control methods are well developed and offer lessons. This is precisely the epistemic gap our paper interrogates: the $40\%$-error-rate simulation is a classical-channel result, and the survey's warning that quantum channels behave differently is the generic form of the quantization question we pose.

**Pauli structure of quantum noise.** Reference [5] introduces the main ideas of QEC — encoding, extraction of syndromes, error operators, and code construction — and shows that general noise and relaxation of a set of two-state quantum systems can always be understood as a combination of Pauli operators acting on the system, with each code correcting a subset of these errors. This Pauli decomposition is the technical hinge of our analysis: any quantum channel admits an operator-sum expansion in Pauli terms, so the quantum question reduces to whether ultrametric confinement holds for each Pauli component and, critically, whether the coherent superposition of error paths (which has no classical analogue) preserves or destroys the confinement.

**Beyond-qubit encodings.** Reference [6] addresses quantum error correction beyond qubits, motivated by the need to protect fragile quantum superposition states from decoherence noise. The supplied summary emphasizes the general necessity of some form of error correction for robust high-fidelity manipulation of quantum states. Our tree encoding is qubit-based, but the beyond-qubit perspective matters for the quantization question: a tree-encoded qudit or oscillator system might interact with the ultrametric geometry differently than a two-level system, and the summary's framing of QEC as the general prerequisite for robust quantum state manipulation sets the stakes for any passive scheme.

**Adiabatic error suppression.** Reference [7] treats error suppression and correction in adiabatic quantum computation, deriving a model for the dynamics of encoded adiabatic quantum computation and building on previously established techniques for error suppression in AQC, on the premise that encoding, suppression, and correction will be required to scale AQC. The adiabatic setting is the closest existing analogue to passive protection: there, too, an energy gap — rather than a measurement cycle — is the protective resource. Our barrier conjecture $E_{\text{barrier}}(d) = 2^{d}$ is structurally an adiabatic-style gap statement transplanted to an ultrametric geometry, and the adiabatic literature's known tension between gap protection and thermal excitation is exactly the failure mode we must confront in Section 4.

**Non-standard Hilbert spaces.** Reference [8] proposes quaternion-based strategies for quantum error correction by extending quantum mechanics into quaternionic Hilbert spaces, defining quaternionic analogues of Pauli operators and quantum gates that ensure inner product preservation, with a simple encoding scheme mapping logical qubits into quaternionic systems. The supplied summary is otherwise thin, but the work is relevant as evidence that the Pauli-operator framework of [5] admits generalizations to non-standard inner-product structures; if ultrametric confinement requires modifying the error algebra itself, the quaternionic construction is a precedent for such modifications.

**Ultrametric foundations.** Reference [11] argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction, with recovering the native ultrametric claimed to resolve cascading errors across mathematics, physics, epistemology, education, quantum computing, and interface design. We adopt from this thesis only the structural claim we need — that hierarchical, digit-wise (tree-wise) organization is the native setting for error propagation in positional systems — and we do not rely on the broader resolvent claims, which the summary states without supporting derivation. Reference [12] consolidates Spencer-Brown's Laws of Form, in which the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, identifying 7 open problem categories and proposing 4 extensions; the supplied summary gives no further detail, and we cite it only as contextual background for distinction-based (branching-tree) foundations of computation. References [9] and [10] are corpus identifiers (the Alpha Pi Project and its ultrametric quantum gravity and computation collection) with no supplied summary; we note their existence as the provenance context of the conjecture and derive nothing from them.

## 3. Methods

### 3.1 The Bruhat–Tits tree and its ultrametric

Let $k$ be a local field with residue field of size $q$, and let $T_{q}$ denote the Bruhat–Tits tree of $k$: the infinite tree in which every vertex has degree $q + 1$ [3]. Vertices of $T_q$ correspond to homothety classes of lattices in $k^2$; we use only the tree structure. Define the path-length distance $d_{\text{BT}}(v, w)$ as the number of edges on the unique path from $v$ to $w$. The associated non-Archimedean valuation satisfies the strong triangle inequality:

$$
d_{\text{BT}}(v, z) \leq \max\bigl(d_{\text{BT}}(v, w),\, d_{\text{BT}}(w, z)\bigr).
$$

The ultrametric consequence we exploit throughout: from any vertex $v$ at depth $d$, the set of vertices at depth $\leq d$ forms a rooted subtree, and two error paths that diverge at depth $d_0$ remain separated by exactly $d_{\text{BT}} \geq d - d_0$ for all deeper depths — divergence is permanent and distance grows monotonically, unlike in Euclidean lattices where paths can reconverge.

### 3.2 Encoding

We encode one logical qubit on a depth-$d$ rooted subtree $\mathcal{T}_d$ of $T_q$. The logical computational basis states $|0_L\rangle$ and $|1_L\rangle$ are assigned to two distinguished configurations of classical-like degrees of freedom on the $2^{d}$ leaves of the binary reduction of the tree (for the binary case $q = 1$, relevant to the simulations discussed below), with the physical degrees of freedom on the $2^{d} - 1$ internal vertices mediating between them. The encoding is deliberately minimal: it is the tree analogue of a repetition code, and its quantum completeness (whether $\{|0_L\rangle, |1_L\rangle\}$ spans a code space correcting a nontrivial set of single-qubit Pauli errors) is left as an open condition, stated in Section 6.

### 3.3 Energy barrier conjecture

We posit a Hamiltonian $H_d$ on $\mathcal{T}_d$ in which the two logical configurations are degenerate ground states and every configuration differing from a ground state on $m$ leaves carries energy at least $m \cdot \epsilon$, with $\epsilon$ the single-site excitation cost. A logical error requires flipping a connected set of sites separating the two ground states. Because the tree branches, the minimal separating set ("cut") at depth $d$ has size $2^{d}$: to move from one logical basin to the other, an error path must at some depth flip an entire level, and the number of sites at level $\ell$ is $2^{\ell}$. The conjectured barrier is therefore

$$
E_{\text{barrier}}(d) = 2^{d} \, \epsilon.
$$

Setting $\epsilon = 1$ as the energy unit, $E_{\text{barrier}}(d) = 2^{d}$. This is the ultrametric version of an adiabatic gap argument [7]: protection by energy landscape rather than by measurement.

### 3.4 Decoding model for the classical evidence

The reported simulations used majority-vote decoding on classical bits: each internal node of $\mathcal{T}_d$ takes the majority of its children's bit values, recursively, with the root's value taken as the decoded logical bit. For the binary tree this is exactly $d$ levels of concatenation of the length-8 majority function on the leaves (for $d = 3$), or iterated length-8 majority for deeper trees. We analyze this decoder exactly in Section 4.

### 3.5 Quantum noise model

For the quantum regime we consider the depolarizing channel on each physical site,

$$
\mathcal{E}_p(\rho) = (1 - p)\,\rho + \frac{p}{3}\bigl(X\rho X + Y\rho Y + Z\rho Z\bigr),
$$

and a coherent $Z$-rotation error $\mathcal{C}_\theta(\rho) = e^{-i\theta Z}\rho\, e^{i\theta Z}$. By the Pauli decomposition of general noise on two-state systems [5], the depolarizing analysis extends term-by-term to arbitrary local noise channels; the coherent case is treated separately because it has no classical analogue.

## 4. Analysis

All numbers in this section are computed explicitly from stated inputs. The single empirical input is the reported simulation result, taken from the source notebook notes: zero logical errors at $40\%$ physical error rate ($p = 0.4$) for $d \geq 3$, under majority-vote decoding on classical bits.

### 4.1 Single-level majority vote at $p = 0.4$

**Input:** $n = 8$ leaves (depth $d = 3$ binary tree, $2^3 = 8$), independent bit-flip probability $p = 0.4$, so $1 - p = 0.6$.

The majority vote fails when at least $5$ of $8$ bits flip:

$$
f(p) = \sum_{k=5}^{8} \binom{8}{k} p^{k} (1-p)^{8-k}.
$$

Compute each term:

- $\binom{8}{5} = 56$; $p^5 = 0.4^5 = 0.01024$; $(0.6)^3 = 0.216$; term $= 56 \times 0.01024 \times 0.216 = 56 \times 0.00221184 = 0.12386304$.
- $\binom{8}{6} = 28$; $p^6 = 0.004096$; $(0.6)^2 = 0.36$; term $= 28 \times 0.004096 \times 0.36 = 28 \times 0.00147456 = 0.04128768$.
- $\binom{8}{7} = 8$; $p^7 = 0.0016384$; $(0.6)^1 = 0.6$; term $= 8 \times 0.0016384 \times 0.6 = 8 \times 0.00098304 = 0.00786432$.
- $\binom{8}{8} = 1$; $p^8 = 0.00065536$; term $= 0.00065536$.

Sum:

$$
f(0.4) = 0.12386304 + 0.04128768 + 0.00786432 + 0.00065536 = 0.1736704.
$$

So one level of 8-fold majority voting maps $p = 0.4$ to $p^{(1)} \approx 0.17367$ — a suppression factor of $0.4 / 0.17367 \approx 2.303$. The vote helps (since $p = 0.4 < 0.5$) but a single level is far from the reported zero-error behavior; the reported result must rest on the recursive tree structure, which we now verify.

### 4.2 Iterated (concatenated) majority vote

Apply $f$ again with $p^{(1)} = 0.1736704$, $1 - p^{(1)} = 0.8263296$:

- $p^2 = 0.1736704^2 = 0.03016141$ (more precisely $0.030161414$); $p^4 = 0.030161414^2 = 0.000909691$; $p^5 = 0.000909691 \times 0.1736704 = 0.000157982$.
- Term $k=5$: $56 \times 0.000157982 \times (0.8263296)^3$. $(0.8263296)^2 = 0.68282058$; $(0.8263296)^3 = 0.68282058 \times 0.8263296 = 0.564233$. Term $= 56 \times 0.000157982 \times 0.564233 = 56 \times 0.000089135 = 0.00499156$.
- $p^6 = 0.000157982 \times 0.1736704 = 0.000027437$. Term $k=6$: $28 \times 0.000027437 \times 0.68282058 = 28 \times 0.000018735 = 0.00052458$.
- $p^7 = 0.000027437 \times 0.1736704 = 0.000004765$. Term $k=7$: $8 \times 0.000004765 \times 0.8263296 = 8 \times 0.000003938 = 0.00003150$.
- $p^8 = 0.000004765 \times 0.1736704 = 0.000000827$. Term $k=8$: $0.00000083$.

Sum:

$$
p^{(2)} = 0.00499156 + 0.00052458 + 0.00003150 + 0.00000083 \approx 0.0055485.
$$

Third level, with $p^{(2)} = 0.0055485$: the sum is dominated by the $k=5$ term.

- $p^5 = 0.0055485^5$. $0.0055485^2 = 0.000030786$; $0.0055485^4 = (0.000030786)^2 = 9.478 \times 10^{-10}$; $p^5 = 9.478 \times 10^{-10} \times 0.0055485 = 5.259 \times 10^{-12}$.
- Term $k=5$: $56 \times 5.259 \times 10^{-12} \times (1 - 0.0055485)^3 \approx 56 \times 5.259 \times 10^{-12} \times 0.98345 = 2.897 \times 10^{-10}$.
- Higher terms are smaller by factors of at least $p/(1-p) \approx 0.00558$ each; the $k=6$ term is $\binom{8}{6} p^6 (1-p)^2 \approx 28 \times 2.918 \times 10^{-14} \times 0.98896 \approx 8.09 \times 10^{-13}$, and the remainder is below $10^{-14}$.

$$
p^{(3)} \approx 2.897 \times 10^{-10} + 8.09 \times 10^{-13} \approx 2.905 \times 10^{-10}.
$$

**Interpretation.** The map $f$ has a stable fixed point below $0.5$ (since $f(0.4) = 0.1737 < 0.4$ and $f(0.1737) = 0.00555 < 0.1737$), so iterated majority voting on the depth-$3$ tree exhibits genuine threshold behavior at $p = 0.4$: the logical error rate decreases superexponentially in concatenation depth. This confirms that the reported classical simulation result — zero logical errors at $p = 0.4$ for $d \geq 3$ — is consistent with a real recursive threshold mechanism of the tree geometry, not an artifact of a single majority vote (which alone would leave a residual $0.1737$). It does not, however, tell us anything about quantum errors; that gap is the subject of Sections 4.3–4.4.

### 4.3 Thermal-activation bound on the passive barrier

**Input:** barrier $E_{\text{barrier}}(d) = 2^{d}$ (Section 3.3, with $\epsilon = 1$), thermal scale $k_B T = 1$ ($\beta = 1$). The thermal activation probability per unit attempt is bounded by the Boltzmann factor:

$$
P_{\text{th}}(d) \leq e^{-\beta E_{\text{barrier}}(d)} = e^{-2^{d}}.
$$

Compute:

- $d = 3$: $e^{-8} = 0.000335463$, i.e. $3.35 \times 10^{-4}$.
- $d = 4$: $e^{-16} = 0.000335463^2 = 1.1254 \times 10^{-7}$.
- $d = 5$: $e^{-32} = (1.1254 \times 10^{-7})^2 = 1.2665 \times 10^{-14}$.

Each increment of $d$ squares the activation probability — the ultrametric analogue of the gap scaling that protects adiabatic computations [7]. At $\beta = 1$ and $d = 5$, the passive barrier suppresses thermal logical errors to below $10^{-13}$ per attempt, comparable to active-scheme logical rates, with zero measurement overhead. This is a bound under the model of Section 3.3, not a measurement.

### 4.4 The quantization gap: what fails to carry over

The classical analysis of Section 4.2 concerns a stochastic bit-flip process on classical bits. Three quantum-specific obstructions prevent direct transfer:

**(a) Superposition of error paths.** A quantum error process generates a coherent superposition over error paths $\sum_{\gamma} c_{\gamma} |\gamma\rangle$, whereas the classical decoder sees one realized path. The ultrametric confinement argument (Section 3.1) confines each path individually; whether interference between separated paths can reconstruct a logical error is not addressed by any classical computation. By the Pauli expansion of general noise [5], the depolarizing components reduce to classical-like Pauli statistics, so obstruction (a) is most severe for coherent errors.

**(b) Coherent noise.** For the coherent rotation $\mathcal{C}_\theta$, the error amplitude accumulates as $\theta$ per site rather than as a probability. Over a cut of size $2^{d}$, a worst-case coherent amplitude scales as $2^{d}\theta$, which for small $\theta$ grows with $d$ — the opposite of the desired suppression. Concretely, with $\theta = 10^{-3}$ and $d = 5$: $2^{5} \times 10^{-3} = 0.032$, a $3.2\%$ amplitude, versus the thermal bound $1.27 \times 10^{-14}$ at the same depth. Coherent noise is therefore the primary threat to the passive scheme, and whether the barrier converts coherent amplitude into confined probability (as energy barriers do in adiabatic dynamics [7]) is precisely the open question.

**(c) Code completeness.** The classical encoding corrects bit flips by majority. A quantum code must additionally correct phase flips and their coherent combinations; whether the tree encoding satisfies the quantum error-correction conditions for a nontrivial Pauli subset — in the standard syndrome-extraction framework of [5], possibly assisted by entanglement in the sense of [2] — is unverified.

### 4.5 Projection: quantum logical error rate under stated assumptions

We state a projection with explicit assumptions, clearly labeled as such. **Assumptions:** (i) the tree encoding satisfies the QEC conditions for single-qubit Pauli errors (unverified — assumption); (ii) quantum errors confine under the ultrametric geometry as classical bit flips do, so that the effective logical error rate is $p_L^{(d)} \approx A \cdot f_{\text{dep}}(p)^{\lceil d/3 \rceil}$ where $f_{\text{dep}}$ is the majority-vote map generalized to Pauli errors with the same $p = 0.4$; (iii) a prefactor $A = 3$ accounts for the three Pauli species. Then for $d = 6$ (two concatenation levels beyond $d = 3$):

$$
p_L^{(6)} \approx 3 \times p^{(2)} = 3 \times 0.0055485 \approx 0.0166.
$$

For $d = 9$: $p_L^{(9)} \approx 3 \times 2.905 \times 10^{-10} \approx 8.7 \times 10^{-10}$. **Uncertainty:** these projections are invalid if assumption (i) or (ii) fails; in particular, coherent noise (Section 4.4b) could raise $p_L^{(6)}$ to $\mathcal{O}(10^{-1})$ or worse. The projection is therefore a conditional target for simulation, not a prediction.

## 5. Results

We report only computed or explicitly labeled values.

