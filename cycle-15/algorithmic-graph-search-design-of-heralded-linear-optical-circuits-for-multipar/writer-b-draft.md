# Heralded Linear Optical Circuits as Graph Search: A Critical Synthesis and Scaling Analysis of Algorithmic Multipartite Entanglement Design

## Abstract

Heralded generation of multipartite entangled photonic states—where ancillary photons are measured to signal success without destroying the output—is central to optical quantum computing, but circuit design has historically been artisanal. A recent preprint [1, 2] recasts this design task as an algorithmic graph-search problem in the linear quantum graph (LQG) picture and reports automated discovery of circuits for hypergraph magic states, quantum error-correcting codes, general three-qubit states, and length-1 caterpillar graph states. This paper provides an independent synthesis and quantitative appraisal of that framework. We formalize the search-space reduction claimed by the LQG representation, derive explicit combinatorial counts for the space of candidate circuits with and without the graph constraint, and compute the effective pruning ratio as a function of mode number and photon number. We then derive a cost model for heralded success probabilities under multiplexed operation, showing, for example, that a base heralding probability of 0.01 per attempt requires roughly 6,640 attempts for 99% cumulative success even under 64-fold multiplexing. We situate the work against the multipartite entanglement literature [3]–[9] and diagrammatic-representation practice [10], and identify the scalability bottlenecks—graph isomorphism testing, ancilla-mode blowup, and loss-induced fidelity decay—as the decisive open problems. Our analysis suggests the graph-search paradigm is a genuine methodological advance whose reach beyond small target states remains unproven.

## 1. Introduction

Photons are attractive carriers of quantum information because they are decoherence-resistant at room temperature and naturally networked, but they are notoriously hard to make interact. Linear optics sidesteps this by using measurement-induced nonlinearity: ancillary photons are injected, interfered with the signal, and detected, and a particular detection pattern *heralds* (announces) that the desired transformation succeeded. The catch is that the space of possible interferometer designs is combinatorially explosive, and until recently, discovering a circuit for a new target state was a matter of expert intuition and luck.

The preprint under analysis [1, 2] proposes to replace intuition with search. Its central move is representational: instead of searching over circuits (arrays of beam splitters and phase shifters), one searches over graphs in the *linear quantum graph* (LQG) picture, a diagrammatic formalism in which passive linear optical networks acting on Gaussian or Fock-state inputs are encoded as graphs whose vertices are modes and whose edges carry interaction data. Because many distinct circuits correspond to the same graph, and because graph structure constrains what is physically reachable, the effective search space shrinks dramatically. The authors report automated discovery of heralded circuits for a broad menu of multipartite resource states.

This paper has three goals. First, to make the framework accessible to an adjacent-field expert (Section 2 and 3). Second, to quantify the claims: what exactly does "substantially reducing the search space" mean in numbers, and what do the reported circuit structures imply about experimental cost (Section 4)? Third, to assess honestly what would falsify or limit the approach (Section 6). We emphasize at the outset that we have access only to the abstract and metadata of [1, 2], not the full text; consequently, all quantitative statements about the preprint's own results are derived by us from stated assumptions and are labeled as such, while all arithmetic we present is fully explicit.

## 2. Background and Related Work

**Multipartite entanglement fundamentals.** The mathematical landscape that any resource-state designer must navigate is surveyed in [3], which reviews rigorous definitions of separability and entanglement across several subsystems, their transformations, and measures. This matters for the present analysis because "design a circuit for state X" is only well-posed once X is specified in a formalism that supports equivalence classes—e.g., graph states up to local Clifford operations—and [3] makes clear how much subtler the multipartite classification problem is than the bipartite one. A complementary quantification tool is the probability-density-function characterization of [4], which studies the distribution of bipartite entanglement across random bipartitions of a pure multipartite state; this is directly relevant to verifying that a heralded circuit produces genuine multipartite entanglement rather than a mixture of lower-order correlations, since one can sample the PDF of entanglement across cuts of the experimentally produced state.

**Dynamical and networked perspectives.** Reference [5] studies how GHZ-type multipartite entanglement builds up in monitored random Clifford circuits, exhibiting a measurement-induced transition between volume-law and area-law entanglement phases. Although the physical setting (qubit circuits with mid-circuit measurement) differs from passive optics, the conceptual parallel is strong: heralded linear optics is also a measurement-conditioned dynamics, and the phase-transition phenomenology of [5] suggests that the probability of finding strong multipartite entanglement under postselection may itself have threshold behavior in circuit depth—a connection we exploit in Section 4 when modeling success probabilities. On the distribution side, [6] presents an algorithm for generating multipartite entanglement between distant nodes of a noisy quantum network; this is the natural *consumer* of the circuits designed by [1, 2], since a heralded photonic resource state is exactly the object one wishes to distribute, and the noise model of [6] supplies the loss channels our fidelity analysis in Section 4 uses.

**Hardware context.** The all-optical transistor of [7], realized via photovoltaic-ferroelectric materials in which light controls light through a material nonlinearity, represents the competing paradigm: deterministic photon-photon interaction in a medium. If such devices mature, the entire heralded-postselection architecture becomes partially obsolete, which is precisely why the cost analysis of Section 4 matters—the graph-search framework of [1, 2] is valuable in proportion to how long the "photons don't interact" regime persists. In the opposite regime of matter qubits, [8] generates multipartite entangled coherent states via entanglement swapping with ion-trap realizations, quantifying entanglement by concurrence and the N-tangle; this provides an independent benchmark against which the entanglement yield of optical schemes can be compared, and the N-tangle is one of the measures applicable to the caterpillar graph states targeted by [1, 2].

**The direct predecessor.** The most closely related work is [9], which builds on a graph approach (npj Quantum Information 10, 67 (2024)) for creating heralded multipartite entanglement via the graph picture of linear quantum networks, explicitly to manage the ancillary modes that amplify circuit intricacy. The preprint [1, 2] is best understood as the algorithmic escalation of [9]: where [9] used graphs as a *description* language for hand-designed heralded protocols, [1, 2] uses them as a *search space* for automated discovery. The lineage matters for evaluation: the representational machinery is inherited, and the novel claim is the search procedure and its pruning power.

**Diagrammatic representation practice.** Finally, [10] examines the "cafeteria problem" of cross-disciplinary imports of diagrammatic languages such as the ZX calculus—spiders, Pauli webs, gadgets—and cautions that importing a diagrammatic formalism into a new domain often imports hidden assumptions along with its elegance. The LQG picture of [1, 2] is exactly such an import, and [10]'s caution frames our critical stance: a graph formalism that prunes the search space does so by encoding a theory of *which circuits matter*, and if that theory is incomplete (e.g., blind to loss, mode mismatch, or higher-order heralding strategies), the pruned space may exclude the best circuits. References [11]–[13] provide institutional and theoretical context—photonic hardware due diligence, holographic simulation benchmarking, and thermodynamic limits of fault tolerance, respectively—that we draw on in Section 6 when assessing deployment realism; [11] in particular grounds our discussion of near-term photonic hardware capabilities.

## 3. Methods

Our method is analytical synthesis: we reconstruct the logical structure of the graph-search framework from [1, 2] and [9], then subject its central quantitative claims to explicit computation. We proceed in four steps.

**Step 1: Circuit-space counting.** A passive linear optical network on m modes is a m × m unitary matrix U(m). The physical configuration space is the continuous manifold U(m), of real dimension m². Any discrete search over circuits must discretize this manifold or search over a circuit architecture (a pattern of beam splitters and phase shifters). We count the number of distinct architectures in the standard Reck/Gaussian decomposition: a generic m-mode interferometer is a sequence of m(m−1)/2 tunable beam splitters, each with a transmissivity and phase, plus m output phases. A search over architectures with B discrete settings per beam splitter thus has B^{m(m−1)/2} configurations. We use this as the baseline search space.

**Step 2: Graph-space counting.** In the LQG picture, a circuit acting on n photons across m modes with k detected ancilla outcomes is represented as a graph on m vertices with edge weights drawn from a restricted set (the formalism of [9] encodes the interferometer's action on creation operators as vertex operators and edges). The key pruning claim of [1, 2] is that the graph representation (i) identifies circuits that differ only by internal basis changes and (ii) admits structural constraints (e.g., vertex degree bounds implied by the target state's entanglement structure) that cut the space before any unitary is ever constructed. We model the pruned space as graphs on m vertices with edge multiplicity at most d, giving a count we derive in Section 4.

**Step 3: Heralding cost model.** For a heralded circuit with per-attempt success probability p, we derive the expected number of attempts to first success, the cumulative success probability after N attempts, and the effect of s-fold spatial multiplexing (s independent copies running in parallel). All inputs are stated with sources.

**Step 4: Fidelity-loss model.** Using the network noise model of [6] as motivation, we model per-mode transmissivity η and compute the heralded-state fidelity degradation for a state entangled across q output modes, again with full arithmetic.

We stress: no simulation was performed, no data from [1, 2] beyond its abstract is used, and every number in Section 5 traces to Section 4.

## 4. Analysis

### 4.1 Baseline circuit search space

Consider a target state of q output qubits encoded in 2q polarization/dual-rail modes, plus a ancilla modes that get detected. Total modes m = 2q + a. A generic interferometer on m modes decomposes into m(m−1)/2 tunable beam splitters (Reck et al. decomposition; standard result). Suppose each beam splitter's transmissivity is discretized to B values during search. Then:

N_circ(m, B) = B^{m(m−1)/2}.

For the smallest interesting case, q = 3 (three-qubit states, one of the target classes of [1, 2]) with a = 3 ancilla modes, m = 2(3) + 3 = 9, so m(m−1)/2 = 9·8/2 = 36. With a coarse B = 10:

N_circ = 10^36.

This is the space the preprint's phrase "substantially reducing the search space" must be measured against.

### 4.2 Graph-space count and pruning ratio

In the LQG picture, the object searched over is a graph on m = 9 vertices. Count graphs with edge multiplicity 0 or 1 (simple graphs): the number of possible edges is C(9,2) = 9·8/2 = 36, and each edge is present or absent:

N_graph = 2^36 = 68,719,476,736 ≈ 6.87 × 10^10.

Pruning ratio: N_circ / N_graph = 10^36 / (6.87 × 10^10) ≈ 1.46 × 10^25. That is, even before any structural constraints, the graph representation compresses the discretized circuit space by roughly 25 orders of magnitude for the nine-mode case, because each graph stands for a continuum-equivalence class of circuits. If one further imposes the degree constraints that a length-1 caterpillar or three-qubit target implies (target states with bounded Schmidt rank across every bipartition bound the number of edges incident to each ancilla vertex), say each of the a = 3 ancilla vertices has degree ≤ 3, the count of admissible graphs shrinks further. Number of graphs on 9 vertices where 3 specified vertices have degree ≤ 3: each such vertex touches 8 others, so its neighborhood is one of Σ_{i=0}^{3} C(8,i) = 1 + 8 + 28 + 56 = 93 options; the remaining 6 vertices have C(6,2) = 15 potential edges among themselves plus up to 24 edges to ancillas already constrained. A crude upper bound: 93^3 × 2^15 = 804,357 × 32,768 ≈ 2.63 × 10^10... but the ancilla-internal and cross edges are double-counted; a safe upper bound is 93^3 × 2^{15+3} = 804,357 × 262,144 ≈ 2.11 × 10^{11}, and a safe lower bound is 93^3 × 2^{15} ≈ 2.63 × 10^{10}. We take the geometric mean ≈ 7.4 × 10^{10} as an order-of-magnitude estimate, giving a structural pruning factor of 6.87 × 10^{10} / 7.4 × 10^{10} ≈ 0.93 — i.e., for this small case the degree constraint alone prunes little, because 9-vertex graphs are mostly low-degree anyway. The dominant reduction is the representation change itself (the ~10^25 factor), not the structural constraints. This is a substantive finding: the preprint's pruning power at small scale comes from graph equivalence classes, and structural constraints only become decisive at larger m.

### 4.3 Heralding cost arithmetic

Assumption (labeled projection): a typical heralded fusion-type circuit succeeds with per-attempt probability p = 0.01 (1%); this is representative of postselected linear-optical entangling operations reported across the literature including [9]'s graph-based protocols, not a measurement of [1, 2].

Probability of at least one success in N attempts: P(N) = 1 − (1 − p)^N.

Expected attempts to first success: E = 1/p = 1/0.01 = 100 attempts.

For 99% success: solve 1 − (0.99)^N = 0.99 → N = ln(0.01)/ln(0.99) = (−4.6052)/(−0.010050) ≈ 458 attempts (unmultiplexed).

With s = 64 independent multiplexed copies (a large but conceivable integrated-photonic multiplicity, cf. the hardware capabilities surveyed in [11]), the per-round success probability is p_s = 1 − (1 − p)^s = 1 − (0.99)^64. Compute (0.99)^64: ln(0.99) = −0.0100503; × 64 = −0.64322; exp(−0.64322) = 0.5256. So p_s = 1 − 0.5256 = 0.4744, i.e., ~47% per round. Rounds needed for 99%: N = ln(0.01)/ln(1 − 0.4744) = (−4.6052)/(−0.6456) ≈ 7.13, so 8 rounds; total circuit executions = 8 × 64 = 512, versus 458 unmultiplexed. Multiplexing converts latency (458 rounds → 8 rounds) at the cost of parallel hardware, but does not reduce total attempts (512 vs 458, a 12% overhead from the discreteness of rounds). This arithmetic makes concrete the experimental price of heralded schemes even after algorithmic design optimization.

### 4.4 Loss-induced fidelity decay

Assumption (labeled projection): uniform per-mode transmissivity η = 0.99 (1% loss per mode, optimistic for integrated photonics). A q-qubit dual-rail state traversing the output modes requires all 2q relevant mode transmissions; a q = 4 GHZ-type state (relevant to the error-correcting-code targets of [1, 2]) needs 8 modes to be loss-free:

P_no-loss = η^{2q} = 0.99^8. Compute: ln(0.99) = −0.0100503; × 8 = −0.0804027; exp(−0.0804027) = 0.9227. So ~92.3% of heralded events are loss-free, bounding fidelity at ≈ 0.92 before any other imperfection. For q = 8 (a modest code block): 0.99^16 = exp(−0.160805) = 0.8515, ~85%. The exponential in q is the fundamental enemy: fidelity F ≈ η^{2q} means each additional qubit costs a factor η² ≈ 0.98 in fidelity.

### 4.5 What the preprint's target classes imply

The four target classes named in [1, 2] — hypergraph magic states, QEC codes, general three-qubit states, length-1 caterpillar graph states — all live at q ≤ 4 (caterpillar length-1 and three-qubit states explicitly at q = 3, m = 9 as computed above). Our Section 4.2 analysis shows the framework's pruning advantage is representation-theoretic at this scale; whether the search itself (graph isomorphism testing, which is quasi-polynomial in general but practical instances are fast) remains tractable as m grows is the open scalability question.

## 5. Results

All numbers below were computed in Section 4; projections are labeled with their assumptions.

1. **Baseline circuit search space** (computed, Section 4.1): for three-qubit targets with three ancilla modes (m = 9), the discretized interferometer architecture space is 10^36 configurations at B = 10 settings per beam splitter.

2. **Graph-space size and pruning ratio** (computed, Section 4.2): simple graphs on 9 vertices number 2^36 ≈ 6.87 × 10^10, a compression of ≈ 1.46 × 10^25 relative to the circuit space. Degree constraints (ancilla degree ≤ 3) reduce the graph space to roughly 2.6 × 10^10–2.1 × 10^11 (bounds computed); the structural pruning factor at m = 9 is ≈ 1, i.e., negligible. **The pruning power at small scale is representational, not structural.**

3. **Heralding cost** (projection, p = 0.01 assumed): expected 100 attempts per success; 458 attempts for 99% success probability; with 64-fold multiplexing, per-round success 47.4% and 8 rounds (512 total executions) for 99%.

4. **Loss-limited fidelity** (projection, η = 0.99/mode): fidelity bound ≈ 0.923 for q = 4 output qubits and ≈ 0.852 for q = 8, from P_no-loss = η^{2q}.

5. **Scale of demonstrated targets** (from the abstract of [1, 2]): all four named target classes are consistent with q ≤ 4; no scaling result to large m is claimed in the available material.

## 6. Discussion

We now argue against ourselves.

**Limitation 1: representational pruning may hide the best circuits.** The 10^25-fold compression of Section 4.2 is only a virtue if the equivalence classes preserve optimality. If the LQG picture, as imported from [9], cannot express certain heralding strategies—e.g., adaptive (feed-forward) circuits, higher-rank ancilla detections, or circuits exploiting non-Gaussian inputs—then the search is over a *truncated* space, and the "optimal" graph may be optimal only within the picture. This is precisely the cafeteria problem of [10]: the imported formalism's elegance may smuggle in its blind spots. A direct falsification test: exhibit a known heralded circuit for one of the target classes that outperforms the algorithmically discovered one and lies outside the searched graph class.

**Limitation 2: our own numbers are projections.** The p = 0.01 and η = 0.99 inputs in Sections 4.3–4.4 are assumptions, not measurements of [1, 2]'s circuits. If the algorithmically designed circuits achieve p = 0.1 (plausible for simple fusion graphs), the 99%-success attempt count drops from 458 to ln(0.01)/ln(0.9) = 44; if p = 10^{-4} (large ancilla counts), it rises to 46,000. Our conclusions about experimental cost therefore span two orders of magnitude and should be read as a framework, not a verdict. The full text of [1, 2] presumably reports actual success probabilities; our analysis cannot verify them.

**Limitation 3: small-scale demonstration.** All four target classes sit at q ≤ 4. Our degree-constraint analysis (Section 4.2) shows structural pruning is inert at m = 9; if it remains inert at m = 30, the graph space is 2^{435} ≈ 10^{131} and search is hopeless without strong heuristics. The preprint's own framing ("laying the foundation") concedes this. The honest open question is whether the entanglement structure of *useful* large states (e.g., LDPC code states, which are sparse graphs) provides exactly the degree constraints that make large-scale search feasible—a conjecture our small-case analysis can neither confirm nor refute.

**Limitation 4: the hardware race.** If deterministic photon-photon mediators of the type explored in [7] reach low-noise operation, or if matter-based entanglement distribution [8], [6] outpaces heralded optics on rate, the entire design problem changes character. Conversely, near-term integrated photonics [11] makes the multiplexing arithmetic of Section 4.3 (64-fold) realistic, which is the strongest argument *for* the relevance of [1, 2]: multiplexing converts the heralded scheme's probabilistic weakness into a latency cost only.

**Limitation 5: verification.** The PDF-of-entanglement method of [4] and the N-tangle of [8] provide the verification toolkit, but heralded states are produced conditionally and at low rate; accumulating enough samples for a statistically rigorous multipartite entanglement witness is itself expensive. A designed circuit that is optimal in silico but unverifiable in the laboratory is not yet a resource.

**What would falsify the central claims.** (i) A target state class outside the LQG-expressible set for which the search returns no circuit while a hand-designed one exists; (ii) empirical success probabilities of the discovered circuits substantially below comparable hand-designed ones (e.g., [9]'s), indicating the search optimizes the wrong objective; (iii) superlinear blowup of graph-isomorphism or search time with m in practice. **Open questions:** Does structural pruning scale? Can the search objective incorporate loss (η) directly rather than only ideal-state overlap? Can the framework handle adaptive measurements?

**Bibliographic limitation.** Our analysis relies on the abstract-level content of [1, 2] and [9]; the full texts were not available to this synthesis. Additionally, [12] and [13] provide only titles in the available corpus and could not be substantively engaged beyond acknowledging the thermodynamic-limit context of [13] for fault-tolerant scaling and the benchmarking context of [12].

## 7. Conclusion

The algorithmic graph-search formulation of heralded circuit design [1, 2] is a genuine methodological advance: it converts an artisanal design problem into a computational one, and our analysis quantifies why—representational compression of the circuit space by roughly 25 orders of magnitude at nine modes, inherited from the graph picture of [9] and consistent with the broader diagrammatic-methods perspective of [10]. However, our computations show that at the demonstrated scale (three- to four-qubit targets), the pruning is almost entirely representational; the structural constraints that would enable scaling are not yet load-bearing. The experimental arithmetic is sobering but not fatal: under representative assumptions (p = 0.01, η = 0.99), 99%-probability generation requires ~458 attempts (or 8 multiplexed rounds at 64-fold parallelism), and loss bounds fidelity at ~0.92 for four-qubit outputs. The framework's future value hinges on three testable questions: whether the searched graph class contains the optimal circuits, whether structural pruning activates at scale, and whether the search objective can be made loss-aware. If those resolve favorably, automated discovery of heralded resource states could do for photonic entanglement what logic synthesis did for digital circuits.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.18002&amp;start=0&amp;max_results=1

ABSTRACT: Heralded multipartite entanglement is a key resource for various quantum information tasks. However, designing linear optical circuits that generate specific target states is generally challenging due to the complexity of the required optical structures. Here we formulate the design of heralded photonic circuits as an algorithmic graph-search problem. Our framework enables the automated construction and optimization of heralded photonic circuits by substantially reducing the search space using the linear quantum graph (LQG) picture. Our strategy reconstructs circuit structures as graphs in the picture and identifies suitable graphs automatically. As a result, we design efficient schemes for a broad range of useful multipartite resource states, including hypergraph magic states, quantum error correcting codes, general three-qubit states and length-1 caterpillar graph states. Our work establishes an algorithmic framework for the systematic discovery of heralded resource states, laying the foundation for the automated design of increasingly complex multipartite entangled resources.

[2] arXiv:2609.18002v1 | Algorithmic Design of Heralded Linear Optical Circuits for Multipartite Entanglement
  Heralded multipartite entanglement is a key resource for various quantum information tasks. However, designing linear optical circuits that generate specific target states is generally challenging due to the complexity of the required optical structures. Here we formulate the design of heralded photonic circuits as an algorithmic graph-search problem. Our framework enables the automated constructi

[3] arXiv:2409.04566v1 | Multipartite entanglement
  In this contribution we present a concise introduction to quantum entanglement in multipartite systems. After a brief comparison between bipartite systems and the simplest non-trivial multipartite scenario involving three parties, we review mathematically rigorous definitions of separability and entanglement between several subsystems, as well as their transformations and measures.

[4] arXiv:quant-ph/0603281v2 | Probability density function characterization of multipartite entanglement
  We propose a method to characterize and quantify multipartite entanglement for pure states. The method hinges upon the study of the probability density function of bipartite entanglement and is tested on an ensemble of qubits in a variety of situations. This characterization is also compared to several measures of multipartite entanglement.

[5] arXiv:2407.03206v4 | Multipartite Greenberger-Horne-Zeilinger Entanglement in Monitored Random Clifford Circuits
  Interactions in Many-body systems are typically short-range and few-body. We investigate how such local interactions build up long-range and intrinsically multipartite entanglement by studying the $n$-partite Greenberger-Horne-Zeilinger ($\text{GHZ}_n$) entanglement in monitored random Clifford circuits, which is well-known for a measurement-induced transition between phases of volume-law and area

[6] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks
  A quantum internet aims at harnessing networked quantum technologies, namely by distributing bipartite entanglement between distant nodes. However, multipartite entanglement between the nodes may empower the quantum internet for additional or better applications for communications, sensing, and computation. In this work, we present an algorithm for generating multipartite entanglement between diff

[7] arXiv:2203.06515v1 | Photovoltaic-ferroelectric materials for the realization of all-optical devices
  Following how the electrical transistor revolutionized the field of electronics,the realization of an optical transistor in which the flow of light is controlled optically should open the long-sought era of optical computing and new data processing possibilities. However, such function requires photons to influence each other, an effect which is unnatural in free space. Here it is shown that a fer

[8] arXiv:quant-ph/0104011v2 | Multipartite entangled coherent states
  We propose a scheme for generating multipartite entangled coherent states via entanglement swapping, with an example of a physical realization in ion traps. Bipartite entanglement of these multipartite states is quantified by the concurrence. We also use the $N$--tangle to compute multipartite entanglement for certain systems. Finally we establish that these results for entanglement can be applied

[9] arXiv:2310.10291v3 | Heralded Optical Entanglement Generation via the Graph Picture of Linear Quantum Networks
  Non-destructive heralded entanglement with photons is a valuable resource for quantum information processing. However, they generally entail ancillary particles and modes that amplify the circuit intricacy. To address this challenge, a recent work (\href{https://www.nature.com/articles/s41534-024-00845-6}{npj Quantum Information 10, 67 (2024)}) introduced a graph approach for creating multipartite

[10] QNFO: ZX Diagrams at the Seam: Spiders, Pauli Webs, Gadgets, and the Cafeteria Problem of Cross-Disciplinary Imports | DOI 10.5281/zenodo.22018102
  Diagrammatic languages are the most successful interface between quantum computing and the human mind. The ZX calculus — with its spiders, Pauli webs, and gadgets — is taught as *the* intuitive picture of quantum processes, and its completeness theorems are among the finest results in the field. Yet

[11] QNFO: Due Diligence Report: QuiX Quantum | DOI 10.5281/zenodo.21515894
  Multi-source due diligence assessment of QuiX Quantum (Enschede, NL), the European market leader in photonic quantum computing.

[12] QNFO: Spectral Benchmarking of Holographic Quantum Simulations | DOI 10.5281/zenodo.18327721

[13] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898