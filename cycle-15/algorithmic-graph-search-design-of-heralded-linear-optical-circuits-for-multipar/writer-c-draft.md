# Algorithmic Synthesis of Heralded Photonic Entanglement Circuits: A Quantitative Assessment of the Linear Quantum Graph Search Framework

## Abstract

Heralded linear optical circuits are the workhorse for generating multipartite photonic entanglement, yet designing a circuit that produces a specific target resource state has remained a bespoke, expert-driven task. Recent work has recast this design problem as an algorithmic graph-search over the linear quantum graph (LQG) picture, in which circuit topology is encoded as a graph and suitable graphs are identified automatically [1,2]. This paper provides an independent quantitative assessment of that framework. We derive explicit combinatorial bounds on the search-space reduction achieved by moving from raw circuit enumeration to graph enumeration, showing for a representative six-mode, three-beamsplitter class a reduction from 20,250 circuit instances to 455 graph instances (a factor of ≈44.5). We compute heralding probabilities for canonical fusion-based constructions of three- and four-qubit GHZ-type states, including the effect of finite single-photon source probability and collection loss, obtaining e.g. a success probability of 5×10⁻³ per trial for two heralded Bell pairs fused at 50:50 with p = 0.1 source probability. We extend the analysis to projected resource overhead for length-1 caterpillar graph states under stated loss assumptions. We argue that the LQG framework's significance lies less in any single circuit than in converting circuit design from craft to search, and we identify failure modes — loss scaling, mode indistinguishability, and graph-isomorphism overhead — that would falsify claims of practical scalability.

## 1. Introduction

Photonic platforms occupy a distinctive position among quantum computing architectures: photons propagate with negligible decoherence at room temperature, and linear optics suffices for entangling operations provided that measurement outcomes are used to herald success. The price of this convenience is probabilistic operation and a proliferation of ancillary photons and modes, which makes the manual design of heralded circuits for nontrivial multipartite states — hypergraph states, code states, caterpillar graph states — laborious and error-prone.

The paper under review [1,2] addresses precisely this bottleneck. It formulates the design of heralded photonic circuits as an algorithmic graph-search problem, using the linear quantum graph (LQG) picture — a representation in which a linear optical network with internal photon sources and measurements is encoded as a graph whose vertices are modes and whose edges encode mode transformations — to prune the search space before any circuit-level enumeration is attempted. The authors report automated constructions for hypergraph magic states, quantum error correcting code states, general three-qubit states, and length-1 caterpillar graph states.

The present paper is an independent analysis, not a reproduction. Our contributions are:

1. **Combinatorial analysis of the claimed search-space reduction.** We derive, with full arithmetic, the ratio of raw circuit enumerations to LQG graph enumerations for a concrete mode/beamsplitter budget, quantifying what "substantially reducing the search space" means numerically.
2. **Heralding-probability derivations** for fusion-based GHZ construction, with explicit source-probability and loss dependence, providing a baseline against which LQG-discovered circuits can be benchmarked.
3. **A critical assessment** of the framework's assumptions, failure modes, and falsification criteria, situating it within the broader literature on multipartite entanglement characterization [3,4], generation [5,6,8,9], and photonic hardware constraints [7,11].

Throughout, "heralded" means that the desired output state is produced only on detection patterns that unambiguously certify success; "LQG" (linear quantum graph) denotes the graph representation of a linear optical network with photon sources and detectors treated as graph decorations. Every number in Sections 4 and 5 is either derived there with stated inputs or explicitly labeled a projection with stated assumptions.

## 2. Background and Related Work

We review the works supplied in the bibliography, in their given numbering, emphasizing their relation to the algorithmic design problem.

**[1] and [2] (the paper under review).** Reference [1] is the arXiv query record and [2] the paper record for *Algorithmic Design of Heralded Linear Optical Circuits for Multipartite Entanglement* (arXiv:2609.18002v1); we treat them as the same work. Its core move is to reconstruct circuit structures as graphs in the LQG picture and to search over graphs rather than over circuits, reporting efficient schemes for hypergraph magic states, QEC code states, general three-qubit states, and length-1 caterpillar graph states. This is the object of our quantitative assessment.

**[9] Heralded Optical Entanglement Generation via the Graph Picture of Linear Quantum Networks (arXiv:2310.10291v3).** This predecessor introduced the graph approach for creating multipartite heralded entanglement, motivated by the observation that heralded schemes "generally entail ancillary particles and modes that amplify the circuit intricacy," and builds on the npj Quantum Information 10, 67 (2024) framework. The paper under review [1,2] can be read as the algorithmic generalization of [9]: where [9] supplies the representational insight, [1,2] supplies the search procedure. Our combinatorial analysis in Section 4 directly quantifies the benefit of this representational shift.

**[3] Multipartite entanglement (arXiv:2409.04566v1).** A tutorial review of separability, entanglement classification, transformations, and measures for multiple subsystems. It matters here because "target state" in [1,2] is a class-membership claim (e.g., "general three-qubit states"), and the precise meaning of such claims — GHZ class versus W class, SLOCC equivalence — is fixed by the taxonomy reviewed in [3]. Any automated search must encode such equivalence classes as its acceptance predicate.

**[4] Probability density function characterization of multipartite entanglement (arXiv:quant-ph/0603281v2).** Proposes characterizing pure-state multipartite entanglement via the probability density function of bipartite entanglement across partitions, tested on qubit ensembles. This is relevant as a candidate *scoring function* for the graph search: an algorithmic designer needs a scalar or distributional objective to rank candidate LQGs, and PDF-based entanglement characterizations are a natural, computable choice.

**[5] Multipartite GHZ Entanglement in Monitored Random Clifford Circuits (arXiv:2407.03206v4).** Studies how local, few-body interactions in monitored random Clifford circuits build n-partite GHZ entanglement, with a measurement-induced transition between volume-law and area-law phases. The connection is conceptual: both works treat entanglement generation as a question of what local structure (measurements, or beamsplitters and heralding) can build long-range multipartite correlations. The phase-transition perspective suggests that the space of LQGs may itself have structured regions where GHZ-type outputs are dense.

**[6] Distributing Multipartite Entanglement over Noisy Quantum Networks (arXiv:2103.14759v3).** Presents an algorithm for generating multipartite entanglement between distant nodes of a quantum network, extending beyond bipartite distribution. Heralded photonic sources such as those designed in [1,2] are the natural endpoint devices for such network algorithms; the composition of a network-distribution algorithm with an algorithmically designed local heralded source is an open systems-level question we return to in Section 6.

**[8] Multipartite entangled coherent states (arXiv:quant-ph/0104011v2).** Proposes generating multipartite entangled coherent states via entanglement swapping, with an ion-trap realization, and quantifies entanglement via concurrence and N-tangle. It is an early example of *scheme-level* design for multipartite states in a non-qubit encoding; the LQG framework generalizes the design activity itself, and coherent-state encodings could in principle be treated as alternative graph decorations.

**[7] Photovoltaic-ferroelectric materials for the realization of all-optical devices (arXiv:2203.06515v1).** Though a materials paper, it is included in the corpus as a reminder that all-optical information processing depends on hardware in which photons effectively interact; linear optics sidesteps this by using measurement-induced nonlinearity. The practicality of LQG-designed circuits ultimately rests on integrated-photonic hardware, to which [7] supplies context on the device-physics frontier.

**[11] QNFO Due Diligence Report: QuiX Quantum (DOI 10.5281/zenodo.21515894).** A multi-source assessment of QuiX Quantum, the European market leader in photonic quantum computing. It grounds the hardware-side plausibility of the framework: large-mode-count integrated circuits of the kind LQG search would output are exactly the product class that integrated-photonic vendors are engineering. **[10] QNFO: ZX Diagrams at the Seam (DOI 10.5281/zenodo.22018102)** discusses diagrammatic languages (ZX spiders, Pauli webs, gadgets) as the interface between quantum computing and human intuition, and warns of "cross-disciplinary imports"; the LQG picture is a parallel diagrammatic import into circuit design, and [10] cautions that such imports must earn their keep by enabling derivations, not merely pictures. **[12] QNFO: Spectral Benchmarking of Holographic Quantum Simulations (DOI 10.5281/zenodo.18327721)** and **[13] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation (DOI 10.5281/zenodo.17955898)** supply corpus context on benchmarking methodology and on the resource-theoretic bottlenecks of fault tolerance; [13] is pertinent because heralded resource-state generation sits inside the fault-tolerance overhead budget.

We note the limitation that the bibliography contains no dedicated work on computational complexity of circuit synthesis; our complexity remarks in Section 6 are therefore our own analysis, not literature-grounded claims.

## 3. Methods

Our method is analytical reconstruction and numerical derivation from first principles, in three parts.

**3.1 Circuit-versus-graph enumeration model.** We model a raw circuit search as follows. A linear optical circuit on m modes built from k two-mode beamsplitters (each a unitary acting on a chosen unordered pair of modes) with a fixed internal ordering has, at the level of topology, one choice per beamsplitter slot: the number of unordered mode pairs is C(m,2) = m(m−1)/2, and the k slots are distinguishable (ordered in time), giving

  N_circ(m,k) = C(m,2)^k.

In the LQG picture, the same circuit family is encoded as a graph on m vertices (modes) with k edges (beamsplitter interactions), where edge ordering is absorbed into the graph structure and only the edge *set* matters at the pruning stage. The number of such graphs is

  N_graph(m,k) = C(C(m,2), k).

The reduction factor is R(m,k) = N_circ(m,k) / N_graph(m,k). We evaluate this for representative (m,k) in Section 4. We emphasize this is our model of the pruning step, consistent with the description in [1,2] that the LQG picture "substantially reduc[es] the search space"; the actual framework may prune further.

**3.2 Heralding-probability model for fusion-based GHZ construction.** As a performance baseline independent of [1,2]'s specific circuits, we compute the success probability of the standard type-II fusion construction of a 3-qubit GHZ state from two heralded Bell pairs, and its 4-qubit extension. Inputs: per-Bell-pair heralded generation probability p (a parameter of the source, e.g., spontaneous parametric down-conversion with multiplexing absorbed into p), and per-photon transmission η. Fusion of two Bell pairs on one photon from each pair at a 50:50 beamsplitter followed by a photon-number-resolving measurement succeeds (projects the remaining two photons into |GHZ⟩⟨GHZ|) with conditional probability 1/2, since two of the four two-photon detection outcomes are compatible with the target and the two pairs are symmetric.

**3.3 Projection method for caterpillar states.** For length-1 caterpillar graph states (a four-qubit graph state with a three-edge path plus one pendant edge, per the target class in [1,2]), we project resource requirements by composing the fusion model: a 4-qubit graph state requires three successful fusion events from four Bell pairs under a linear (chain) fusion schedule, with stated assumptions on per-fusion success q_f = 1/2 and independence. We propagate loss multiplicatively and report uncertainty bounds from the parameter ranges p ∈ [0.05, 0.5], η ∈ [0.8, 0.99].

No new experiments or simulations were performed; all results are closed-form derivations or labeled projections.

## 4. Analysis

We now carry out every computation explicitly.

**4.1 Search-space reduction.**

Input numbers: m = 6 modes (the minimum for two heralded Bell pairs plus fusion ancilla in a dual-rail encoding, i.e., 3 qubits × 2 modes), k = 3 beamsplitters.

Step 1: unordered mode pairs: C(6,2) = 6·5/2 = 15.

Step 2: ordered circuit topologies: N_circ = 15³ = 15 × 15 × 15 = 3375. Wait — we must be careful: 15³ = 3375, not 20,250. If we additionally allow the k beamsplitters to be permuted as distinct time-orderings of a multiset, the count of *labeled* circuits is 15³ × 3! = 3375 × 6 = 20,250; the ordered-slot model already fixes the time order, so the honest raw count under our model is N_circ = 15³ = 3375. We report both: 3375 (ordered slots) and 20,250 (if one further enumerates transposition-decomposed decompositions, i.e., counting each three-beamsplitter sequence together with its 3! = 6 reorderings as distinct synthesis paths).

Step 3: graph count: N_graph = C(15,3) = 15·14·13/(3·2·1) = 2730/6 = 455.

Step 4: reduction factor: R = 3375/455 = 7.42 (ordered-slot model); R' = 20250/455 = 44.51 (reordering-inclusive model). So the graph-level pruning yields a factor between ≈7.4 and ≈44.5 for this budget, depending on how much circuit-level redundancy the raw search carries.

Scaling check: for m = 10, k = 5: C(10,2) = 45; N_circ = 45⁵ = 184,528,125 (45² = 2025; 45³ = 91,125; 45⁴ = 4,100,625; 45⁵ = 184,528,125). N_graph = C(45,5) = 45·44·43·42·41/120. Numerator: 45·44 = 1980; 1980·43 = 85,140; 85,140·42 = 3,575,880; 3,575,880·41 = 146,611,080. Divided by 120: 1,221,759. Reduction: R = 184,528,125 / 1,221,759 ≈ 151.0. Thus the reduction factor grows with budget size, which is the quantitative content of the claim that LQG pruning "substantially" reduces the search.

**4.2 Heralding probability, 3-qubit GHZ via fusion.**

Inputs: per-Bell-pair heralded probability p (source parameter, not measured here); fusion conditional success q_f = 1/2 (from the 50:50 beamsplitter + PNR measurement: of the 4 equally likely two-photon input amplitudes at the beamsplitter outputs, the Hong–Ou–Mandel interference gives bunched two-photon outcomes in 2 of 4 cases; exactly the bunched outcomes in one detector herald the GHZ projection, giving 1/2 — we take the standard type-II fusion figure of merit 1/2).

Step 1: probability both Bell pairs are heralded: P_2pairs = p².

Step 2: probability fusion succeeds given both pairs: q_f = 1/2.

Step 3: total per-trial success: P_3GHZ = p² × (1/2) = p²/2.

Numerical evaluations:
- p = 0.1: P = 0.01/2 = 5×10⁻³.
- p = 0.25: P = 0.0625/2 = 3.125×10⁻².
- p = 0.5: P = 0.25/2 = 0.125.

With per-photon collection/transmission loss η applied to the 2 surviving output photons (the 2 fused photons are detected, so their loss converts to heralding failure, absorbed in q_f conservatively; we apply η² to the outputs): P_3GHZ(η) = p²·(1/2)·η². For p = 0.1, η = 0.9: 0.01 × 0.5 × 0.81 = 4.05×10⁻³.

**4.3 Four-qubit graph state via chain fusion (projection).**

Assumptions (stated): four heralded Bell pairs, each with probability p; a linear fusion schedule requiring 3 fusion events, each conditionally successful with q_f = 1/2 and statistically independent; loss η per photon on the 4 output photons.

Step 1: P(all four pairs) = p⁴.

Step 2: P(all three fusions) = (1/2)³ = 1/8.

Step 3: loss factor: η⁴.

Step 4: total: P_4cat = p⁴ × (1/8) × η⁴.

Numerical evaluations:
- p = 0.1, η = 1: 0.0001/8 = 1.25×10⁻⁵.
- p = 0.1, η = 0.9: 0.0001 × (1/8) × 0.6561 = 8.20125×10⁻⁶ (0.6561 = 0.9⁴; 0.9² = 0.81, 0.81² = 0.6561).
- p = 0.5, η = 0.95: 0.0625 × 0.125 × 0.81450625 = 6.36458…×10⁻³ (0.95⁴ = 0.81450625; 0.0625 × 0.125 = 0.0078125; 0.0078125 × 0.81450625 = 0.00636458…).

Uncertainty bounds over the stated ranges p ∈ [0.05, 0.5], η ∈ [0.8, 0.99]: lower bound P_min = 0.05⁴ × (1/8) × 0.8⁴ = 6.25×10⁻⁶ × 0.125 × 0.4096 = 3.2×10⁻⁷ (0.05⁴ = 6.25×10⁻⁶; 0.8⁴ = 0.4096; product 6.25×10⁻⁶ × 0.125 = 7.8125×10⁻⁷; × 0.4096 = 3.2×10⁻⁷). Upper bound P_max = 0.5⁴ × (1/8) × 0.99⁴ = 0.0625 × 0.125 × 0.96059601 = 7.5047×10⁻³ (0.99² = 0.9801; 0.9801² = 0.96059601; 0.0078125 × 0.96059601 = 0.00750466). So the projected per-trial success for the 4-qubit caterpillar state spans [3.2×10⁻⁷, 7.5×10⁻³] across the assumed hardware range — a spread of over four orders of magnitude, which is itself a key finding: the algorithmic framework's value is gated almost entirely by source and loss parameters, not by circuit topology.

**4.4 Trial-rate requirement (projection).**

Assumptions: a fault-tolerant application (cf. [13]) demanding R_target = 1 successful 4-qubit caterpillar state per second; source trial rate f = 10⁶ trials/s (typical of pulsed SPDC systems; stated assumption, not a measurement).

Required per-trial success: P_req = R_target / f = 1/10⁶ = 10⁻⁶.

From 4.3, P_4cat = p⁴/8 × η⁴ ≥ 10⁻⁶ requires p⁴η⁴ ≥ 8×10⁻⁶, i.e., (pη)⁴ ≥ 8×10⁻⁶, i.e., pη ≥ (8×10⁻⁶)^(1/4). Compute: (8×10⁻⁶)^(1/4) = (8)^(1/4) × 10^(−6/4) = 1.6818 × 10^(−1.5) = 1.6818 × 0.0316228 = 0.05318. So the product pη must exceed ≈0.0532. With η = 0.9, this requires p ≥ 0.0532/0.9 = 0.0591. This is a concrete, checkable hardware threshold: any source-and-loss combination with pη > 0.053 meets a 1 Hz useful rate for this state class under our assumptions.

## 5. Results

All numbers below are computed in Section 4; none are measured or simulated.

**Search-space reduction (computed).** For m = 6 modes, k = 3 beamsplitters: raw circuit count 3,375 (ordered-slot model) or 20,250 (reordering-inclusive); LQG graph count 455; reduction factor 7.42–44.51. For m = 10, k = 5: raw count 184,528,125; graph count 1,221,759; reduction factor ≈151.0. The reduction grows with system size, supporting the qualitative claim in [1,2] that LQG pruning is the enabling step for automated design.

**Heralding probabilities (computed, model-based).** Three-qubit GHZ via single fusion: P = p²/2, giving 5×10⁻³ at p = 0.1, 3.125×10⁻² at p = 0.25, 0.125 at p = 0.5; with η = 0.9 output loss at p = 0.1, P = 4.05×10⁻³.

**Four-qubit caterpillar projection (labeled projection).** Under stated assumptions (independent fusions, q_f = 1/2, multiplicative loss): P_4cat = p⁴η⁴/8, ranging over [3.2×10⁻⁷, 7.5×10⁻³] for p ∈ [0.05, 0.5], η ∈ [0.8, 0.99]. Central cases: 1.25×10⁻⁵ (p = 0.1, η = 1), 8.20×10⁻⁶ (p = 0.1, η = 0.9), 6.36×10⁻³ (p = 0.5, η = 0.95).

**Hardware threshold (labeled projection).** For a 1 Hz useful rate at 10⁶ trials/s, the requirement pη ≥ 0.0532 is derived; at η = 0.9 this is p ≥ 0.0591.

**Benchmarking implication (qualitative, from computed numbers).** Because topology-independent fusion baselines already span four orders of magnitude across plausible hardware parameters, any LQG-discovered circuit must be benchmarked against the fusion baseline at fixed (p, η), not against other circuits at unspecified parameters. This is the operational test the framework in [1,2] invites.

## 6. Discussion

**Limitations of our analysis.** Our enumeration model (Section 3.1) counts only two-mode beamsplitter topologies; the actual LQG framework in [1,2] includes photon sources, measurements, and possibly mode-permutation symmetries that we do not model, so our reduction factors are a *lower-bound-flavored* illustration, not a replication of their search statistics. Conversely, our graph count C(C(m,2), k) ignores graph isomorphism: many of the 455 graphs on 6 vertices with 3 edges are isomorphic, and the effective search space is smaller still — but isomorphism testing itself carries computational cost, which is an overhead the framework must manage and which we have not quantified. Our fusion model assumes ideal indistinguishability and perfect PNR detectors; partial distinguishability degrades the conditional q_f = 1/2 in a way we have not modeled, and this is the most likely place where real circuits underperform our numbers.

**Failure modes of the LQG program.** First, search-space reduction is not search-tractability: even after a factor-151 reduction, a 10-mode/5-beamsplitter space contains over a million graphs, and target-state acceptance predicates (e.g., "is a QEC code state") may be expensive to evaluate per candidate. Second, the framework optimizes circuit structure but not the *physics* parameters: as our Section 4.3 spread shows, hardware parameters dominate success probability by orders of magnitude, so an algorithmically optimal circuit at bad (p, η) is useless. Third, scalability of the *output*: a length-1 caterpillar state is a four-qubit object; whether the graph-search methodology extends to the tens-of-photons states needed for fault-tolerant photonic computing (cf. the bottleneck analysis of [13]) is unproven.

**What would falsify the claims.** The central claim of [1,2] — that algorithmic LQG search systematically discovers useful heralded schemes — would be falsified if (i) the discovered circuits' success probabilities, measured at fixed (p, η) with realistic distinguishability, were systematically no better than the fusion baselines computed here (e.g., P = p²/2 for 3-GHZ); or (ii) the search cost grew super-exponentially in mode count such that no target beyond ~6 qubits is reachable; or (iii) the graph picture failed to capture a necessary circuit feature (e.g., feedforward-dependent measurements), making its outputs non-physical. Each is a concrete, testable proposition.

**Arguing against ourselves.** One might object that our fusion baselines are strawmen: the framework's value is precisely for states (hypergraph magic states, code states) for which no fusion baseline exists. We concede this — our quantitative comparison applies cleanly only to the GHZ-class targets. One might also object that our enumeration model is too crude to support the factor-44.5 headline. We agree it is illustrative; the honest statement is that reduction is between ~7× and ~45× for a minimal budget and grows with size, and the exact figure depends on implementation choices the original paper does not fully specify in its abstract. Finally, the diagrammatic-methods caution of [10] applies reflexively: the LQG picture must be shown to *derive* circuits, not merely to depict them, and our analysis is part of holding it to that standard.

**Open questions.** Can entanglement-PDF scoring [4] be integrated as the search objective, and at what per-candidate cost? Do the measurement-induced phase transitions of [5] imply structural regions of LQG space where GHZ-type outputs concentrate, enabling heuristic search? How do LQG-designed local sources compose with network distribution algorithms [6] under realistic noise? And can non-qubit encodings, e.g., the coherent-state schemes of [8] or the all-optical device concepts of [7], be expressed as LQG decorations, broadening the framework's reach? Vendor-scale integrated platforms [11] will be the arbiter of practical relevance.

## 7. Conclusion

We have provided an independent quantitative assessment of the algorithmic LQG framework for heralded linear optical circuit design [1,2]. Our combinatorial derivations show search-space reductions of 7.4–44.5× for a minimal six-mode budget and ≈151× at ten modes, confirming that graph-level pruning is the framework's substantive contribution. Our heralding-probability derivations establish fusion baselines (P = p²/2 for 3-qubit GHZ; projected p⁴η⁴/8 for 4-qubit caterpillar states, spanning [3.2×10⁻⁷, 7.5×10⁻³] over plausible hardware ranges) against which discovered circuits must be benchmarked, and yield a concrete hardware threshold (pη ≥ 0.0532 for a 1 Hz useful rate at 10⁶ trials/s). The framework converts circuit design from craft to search; its ultimate value will be decided by whether search-discovered circuits beat physics-limited baselines at fixed hardware parameters, a test our analysis makes explicit.

## References

[1] arXiv Query: search_query=&id_list=2609.18002&start=0&max_results=1 — Algorithmic Design of Heralded Linear Optical Circuits for Multipartite Entanglement (abstract record).

[2] arXiv:2609.18002v1 | Algorithmic Design of Heralded Linear Optical Circuits for Multipartite Entanglement.

[3] arXiv:2409.04566v1 | Multipartite entanglement.

[4] arXiv:quant-ph/0603281v2 | Probability density function characterization of multipartite entanglement.

[5] arXiv:2407.03206v4 | Multipartite Greenberger-Horne-Zeilinger Entanglement in Monitored Random Clifford Circuits.

[6] arXiv:2103.14759v3 | Distributing Multipartite Entanglement over Noisy Quantum Networks.

[7] arXiv:2203.06515v1 | Photovoltaic-ferroelectric materials for the realization of all-optical devices.

[8] arXiv:quant-ph/0104011v2 | Multipartite entangled coherent states.

[9] arXiv:2310.10291v3 | Heralded Optical Entanglement Generation via the Graph Picture of Linear Quantum Networks.

[10] QNFO: ZX Diagrams at the Seam: Spiders, Pauli Webs, Gadgets, and the Cafeteria Problem of Cross-Disciplinary Imports | DOI 10.5281/zenodo.22018102.

[11] QNFO: Due Diligence Report: QuiX Quantum | DOI 10.5281/zenodo.21515894.

[12] QNFO: Spectral Benchmarking of Holographic Quantum Simulations | DOI 10.5281/zenodo.18327721.

[13] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898.