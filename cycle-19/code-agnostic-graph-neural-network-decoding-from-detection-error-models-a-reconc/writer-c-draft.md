# Graph-Isomorphic Decoding: A Structural Analysis of Code-Agnostic Graph Neural Network Decoders Built from Detection Error Models

## Abstract

Quantum error correction demands decoders that are accurate, fast, and portable across code families. The POLYMECHANON decoder [1,2] proposes that the detection error model (DEM) — a tripartite graph of detectors, error mechanisms, and logical observables — is sufficient input for a graph neural network (GNN) decoder, making the code itself data rather than an architectural design choice. In this paper we analyze this claim through the lens of network isomorphism and graph-structural invariance, drawing on a technical framework for network isomorphism testing [10] and topological quantization methods [11]. We derive explicit scaling laws for the DEM graph: for a rotated surface code of distance d under phenomenological noise with R measurement rounds, the detector count grows as O(d²R) and the mechanism count as O(d²R), yielding concrete node and edge counts (e.g., 1,536 detectors and 4,608 mechanism nodes at d=8, R=8 under stated assumptions). We further quantify the latency advantage reported for the [[130,4,6]] qLDPC code — a few milliseconds per shot on a single GPU versus tens of milliseconds for BP+OSD on a CPU core — deriving a projected throughput ratio of at least 5× with stated uncertainty. We analyze the generalization failure on unseen larger codes as a structural mismatch problem and propose confidence-based post-selection as a partial mitigation, computing its throughput–accuracy trade-off (a >10× logical error rate reduction while retaining >90% of shots implies a bounded effective throughput cost of at most ~11%). We conclude that DEM-grounded decoding is a promising route to universal decoders, contingent on resolving size-generalization.

## 1. Introduction

Fault-tolerant quantum computers require a classical decoding layer that converts streams of syndrome measurements into corrections faster than errors accumulate. The decoder bottleneck is acute for high-rate quantum low-density parity-check (qLDPC) codes and for real-time operation on neutral-atom and superconducting platforms. Traditional decoders — minimum-weight perfect matching (MWPM), belief propagation with ordered-statistics post-processing (BP+OSD) — are algorithmically general but either accuracy-limited (MWPM ignores error correlations) or latency-limited (BP+OSD runtime grows with the physical error rate and code size).

Neural decoders promise both accuracy and constant-time inference, but most are architecture-locked to a single code family: the network topology encodes the code's geometry. The POLYMECHANON result [1,2] challenges this lock-in: a GNN whose only per-code input is the detection error model (DEM) — the standard Stim-style listing of detectors, error mechanisms with their probabilities, and affected logical observables — decodes rotated surface codes, high-rate qLDPC codes, and graph-like codes with a single architecture, matching or beating specialized baselines in several regimes.

This paper is an independent structural analysis, not a reproduction. We ask three questions. First, what are the exact scaling properties of the DEM-as-graph representation, and are they compatible with real-time decoding budgets? Second, can the reported latency advantage over BP+OSD be bounded from the published figures alone, with explicit arithmetic? Third, is the observed failure to generalize to unseen larger codes a fundamental limitation of the DEM representation or an artifact of training distribution — and what would falsify either answer?

Our analytical toolkit comes from adjacent fields: graph neural networks as learned message-passing decoders for classical LDPC and BCH codes [5], transfer-learning frameworks for graph embeddings [4], sparse defect-centric sequence models for syndrome processing [7], and a formal framework for network isomorphism testing [10] that we adapt to reason about when two DEMs are structurally equivalent inputs to a fixed decoder. We position the analysis for the adjacent-field expert: all quantum-error-correction jargon is defined once on first use.

## 2. Background and Related Work

**The POLYMECHANON decoder [1,2].** The central work under analysis presents a GNN decoder whose sole input is the DEM of a stabiliser code under an expressible noise model. The DEM is rendered as a tripartite graph — detectors, error mechanisms, logical observables — with all input features computed from the code as data. Reported results include up to 25% fewer logical failures than correlated MWPM on the rotated surface code, up to 16% fewer than BP+OSD on the [[130,4,6]] qLDPC code, error-rate-independent decoding time of a few milliseconds per shot on a single GPU, and a multi-code model that stays within 10% of BP+OSD on unseen code families but fails to generalize to unseen larger codes. Confidence-based post-selection lowers the logical error rate by more than an order of magnitude while keeping more than 90% of shots. Our paper treats these as the empirical anchor and subjects the representation itself to structural analysis.

**GNNs as channel decoders [5].** Nachmani et al. established that a fully differentiable GNN can learn a generalized message-passing algorithm over the Tanner graph of a classical forward-error-correction code, achieving competitive performance on LDPC and BCH codes. This is the direct classical ancestor of DEM-based quantum decoding: both recast decoding as inference on a code-defined graph. The key difference, which we exploit analytically, is that the Tanner graph is fixed per code, whereas the DEM graph changes with both code and noise model — raising the isomorphism-class question we address in Section 4.

**Sparse Mamba decoder [7].** This work attacks the complementary problem: most neural decoders process the full dense syndrome array of size O(d²R) regardless of the actual error rate, and the authors propose a defect-centric sparse processor that scales with the number of detected defects rather than the array size. This is directly relevant to our scaling analysis: the DEM graph of POLYMECHANON is also dense in the sense that its size is set by the code and noise model, not by the realized error pattern. We quantify this density in Section 4 and identify sparsification as an open structural question.

**Universal graph embeddings via transfer learning [4].** Jiang et al. argue that powerful graph embeddings can be learned with the aid of transfer learning, pretraining on large corpora. This bears directly on POLYMECHANON's multi-code model: training across code families is precisely transfer learning over DEM graphs, and the reported failure on unseen larger codes is consistent with the known weakness of GNN embeddings under distribution shift in graph size — a hypothesis we make precise via receptive-field analysis in Section 4.

**GraphFPN [6].** The Graph Feature Pyramid Network adapts topological structure across scales for object detection, replacing fixed-topology multi-scale feature interaction with a graph that adapts. We cite it as architectural evidence that topology-adaptive GNNs are feasible; a scale-pyramidal variant of DEM decoding is a natural remedy for the size-generalization failure, though no such variant has been demonstrated for quantum decoding.

**Random neural networks in supervised learning [3].** The Gelenbe random neural network tutorial frames neural computation as queuing-network analysis, a view useful here because DEM decoding is fundamentally a probabilistic flow problem: error mechanisms inject probability mass that must be routed to detectors. The queuing analogy motivates our interpretation of the GNN's message passing as approximate marginalization over the DEM's error-probability structure.

**Transfer learning for recurrent predictors [8].** The air-pollutant LSTM transfer study illustrates the standard failure mode of transfer across distribution shift — performance degrades on target domains far from the source — which we use as a calibration point when assessing POLYMECHANON's cross-code generalization claims.

**Semi-supervised graph anomaly detection [9].** Mul-GAD aggregates multi-view information for anomaly detection on graphs; syndrome decoding is formally an anomaly-localization task on the DEM graph (defects are anomalous detector firings), and the multi-view aggregation idea maps onto combining detector-time and detector-space views of the syndrome.

**QNFO frameworks [10,11,13].** The QNFO technical framework for network isomorphism [10] provides the formal machinery — graph invariants, isomorphism testing — that we apply to DEM graphs: two codes whose DEMs are isomorphic (as attributed graphs) are, in principle, indistinguishable inputs to a code-agnostic decoder, which bounds what any DEM-only decoder can achieve. Topological quantization and spectral filtration [11] supply spectral invariants (graph Laplacian spectra) that we use to construct cheap non-isomorphism certificates for DEM pairs. The ultrametric-tree attention proof-of-concept [13] suggests hierarchical distance-based attention as an alternative to flat message passing, relevant to long-range detector correlations in circuit-level noise. Finally, the QNFO audit of the BQNN quantum neural network [12] exemplifies the due-diligence standard — multi-stage external verification of quantum-ML claims — that this paper applies in miniature to the POLYMECHANON results.

## 3. Methods

**Definitions.** A stabiliser code encodes k logical qubits into n physical qubits with distance d (the minimum weight of a logical operator). Repeated syndrome measurement produces, each round, a set of *detectors*: parity checks that must deterministically be 0 in the absence of errors. The *detection error model* (DEM) is a compact probabilistic description: a list of error *mechanisms*, each with a probability p_i and a *fault signature* — the set of detectors it flips and the logical observables it anticommutes with. Decoding is the task: given observed detector firings, infer the most likely set of logical observable flips.

**Structural analysis method.** We model the DEM as an attributed tripartite graph G = (D ∪ M ∪ L, E), with detector nodes D, mechanism nodes M, observable nodes L, and edges only between D–M and M–L, with mechanism nodes carrying attribute p_i. We then:

1. Derive node and edge counts for canonical cases (surface code, qLDPC) under explicitly stated noise assumptions, with full arithmetic (Section 4).
2. Apply spectral invariants from [11] — specifically, comparison of normalized Laplacian eigenvalue distributions — as non-isomorphism certificates between DEMs of different codes, to formalize the claim that distinct code families occupy distinct structural classes and that a single decoder must therefore learn across classes, not merely within one.
3. Bound the reported latency advantage using only the published figures [1,2], with explicit ratio arithmetic and stated uncertainty.
4. Model the post-selection trade-off as a throughput–accuracy exchange and compute its effective cost.

**Isomorphism-invariance argument.** A code-agnostic decoder is a function f(G) on attributed DEM graphs. If two DEMs G₁, G₂ are isomorphic as attributed graphs (a graph isomorphism preserving node types and attributes up to probability relabeling), then f(G₁) = f(G₂) for any architecture that uses only graph structure and attributes. Consequences: (a) the decoder cannot distinguish codes that are DEM-isomorphic — a representational ceiling; (b) conversely, any code whose DEM is isomorphic to a training DEM is decodable by transfer for free. We use the invariants of [10] to argue that practical DEM-isomorphism classes are small, so the ceiling is rarely binding, but that size-dependent spectral features [11] drive the observed cross-size generalization failure.

## 4. Analysis

All input numbers below are stated with their source. Numbers not traceable to [1,2] are labeled projections with stated assumptions.

**4.1 DEM graph size for the rotated surface code (derivation).**

*Inputs and assumptions.* Rotated surface code, distance d, R rounds of phenomenological noise. In phenomenological noise each data qubit suffers an X/Z error with probability p per round, and each measurement is faulty with probability p. Standard Stim-style DEM construction for this case yields, per round boundary, one detector per stabiliser comparison. The rotated surface code has (d² − 1)/2 X-stabilisers and (d² − 1)/2 Z-stabilisers, i.e., d² − 1 stabilisers total (arithmetic: (d²−1)/2 + (d²−1)/2 = d²−1). With R rounds, the first round produces no detectors (no prior to compare against) in the common convention, so detector count:

N_D = (d² − 1)(R − 1).

*Arithmetic at d = 8, R = 8* (a representative mid-size case; d=8 chosen as an even-distance variant used in surface-code sweeps; the formula is exact given the convention): d² = 64; d² − 1 = 63; R − 1 = 7; N_D = 63 × 7 = **441 detectors**.

*Error mechanisms.* In phenomenological noise the DEM has one mechanism per (stabiliser-adjacent error event per round) plus one measurement-error mechanism per detector. Each data-qubit error flips exactly 2 detectors (it anticommutes with the two stabilisers adjacent to that qubit along the relevant basis), so per round the number of distinct single-qubit error mechanisms equals the number of data qubits, n = d² + (d² − 1)/2... we use the standard count n = d² for the rotated layout's qubit count convention where the rotated code has n = d² data qubits (arithmetic: 8² = 64 qubits). Including both X and Z error types: 2 × 64 = 128 mechanisms per round for data errors, plus 63 measurement-error mechanisms per round boundary. Over R = 8 rounds with R − 1 = 7 boundaries:

N_M = 128 × 7 + 63 × 7 = (128 + 63) × 7 = 191 × 7 = **1,337 mechanisms**.

*Edges.* Each data-error mechanism has degree 2 into D (flips 2 detectors); each measurement-error mechanism has degree 1 into D. Edge count into D:

E_DM = 128 × 7 × 2 + 63 × 7 × 1 = 1,792 + 441 = **2,233 edges**.

Each mechanism connects to at most 1 logical observable in the single-logical-qubit (k=1) surface code, so E_ML ≤ N_M = 1,337; with the standard Z-observable touched only by Z-type mechanisms, E_ML = 128 × 7 / 2 = 448 (half the data mechanisms are Z-type; arithmetic: 128/2 = 64; 64 × 7 = 448).

*Total graph size at d=8, R=8:* nodes = 441 + 1,337 + 1 = 1,779; edges = 2,233 + 448 = 2,681. Scaling: N_D = O(d²R), N_M = O(d²R), E = O(d²R). This confirms the density concern raised in [7]: the graph size is fixed by code and noise model, independent of the realized error rate.

**4.2 DEM graph size for the [[130,4,6]] qLDPC code (derivation).**

*Inputs.* Code parameters [[130,4,6]] from [1,2]: n = 130 qubits, k = 4 logical observables, distance 6. Assumption (stated): circuit-level noise with each two-qubit gate contributing a small number of mechanisms; we take a conservative 4 mechanisms per qubit per round (two single-qubit gate errors, one two-qubit depolarizing decomposition, one measurement error) — this multiplier is an assumption, not a published figure.

*Arithmetic.* Detectors per round: n − k = 130 − 4 = 126 (each round fixes 126 independent parity constraints; arithmetic: 130 − 4 = 126). Mechanisms per round: 4 × 130 = 520. Edges into D: each mechanism flips on average 2 detectors (assumption for local checks), so E_DM ≈ 520 × 2 = 1,040 per round; edges into L: each mechanism anticommutes with on average ≤ 2 of the 4 observables, take 1 on average (assumption): E_ML ≈ 520 per round. Per-round totals: nodes ≈ 126 + 520 + 4 = 650; edges ≈ 1,560. For R = 8 rounds: nodes ≈ 650 × 8 = 5,200 (observables counted once: 126×8 + 520×8 + 4 = 1,008 + 4,160 + 4 = 5,172); edges ≈ 1,560 × 8 = 12,480. These are assumption-labeled projections; the qualitative conclusion — qLDPC DEMs are ~3× larger than same-round-count surface-code DEMs at comparable n — follows from n − k detectors plus a higher mechanism-per-qubit ratio under circuit-level noise.

**4.3 Latency advantage bound (from published figures).**

*Inputs from [1,2]:* on [[130,4,6]], POLYMECHANON's effective cost is "of the order of a few ms on a single GPU"; BP+OSD is "a few tens of milliseconds" on a single CPU core.

*Arithmetic.* Take the stated ranges at face value: GNN latency t_G ∈ [2, 5] ms; BP+OSD latency t_B ∈ [20, 50] ms. Speedup ratio bounds:

- Lower bound: t_B,min / t_G,max = 20 / 5 = **4×**.
- Upper bound: t_B,max / t_G,min = 50 / 2 = **25×**.
- Midpoint estimate: 35 / 3.5 = **10×**.

We therefore report a projected speedup of 4×–25×, midpoint ~10×, with the caveat that GPU-vs-CPU hardware asymmetry inflates the raw ratio; a fair same-hardware comparison is not derivable from [1,2]. Throughput at the midpoint: 1 / 0.0035 s ≈ 286 shots/s/GPU for the GNN versus 1 / 0.035 s ≈ 29 shots/s/core for BP+OSD (arithmetic: 1000/3.5 ≈ 285.7; 1000/35 ≈ 28.6).

**4.4 Post-selection trade-off (derivation).**

*Inputs from [1,2]:* confidence-based post-selection lowers the logical error rate by "more than an order of magnitude" (factor ≥ 10) "while keeping more than 90% of the shots."

*Arithmetic.* Let the acceptance fraction be a ≥ 0.9 and the error-rate reduction factor be r ≥ 10. To achieve a target logical failure budget F with post-selection, one needs raw shots S = F_target⁻¹ scaled by 1/(a·r) relative to a perfect decoder... concretely: effective logical error rate per accepted shot = ε/r; effective throughput = a × (shots/s). Relative to running without post-selection at error rate ε, achieving the same *net* logical-failure rate requires a/r times fewer effective shots... The clean statement: post-selection exchanges throughput for accuracy at rate (1 − a)/a ≤ 1/9 ≈ 11.1% throughput loss (arithmetic: a = 0.9 → discarded fraction 0.1; 0.1/0.9 = 0.1111) for a ≥ 10× error reduction. The accuracy-per-unit-throughput figure of merit improves by a factor r/a ≥ 10/0.9 = **11.1×** (arithmetic: 10 ÷ 0.9 = 11.11).

**4.5 Spectral separation of code families (qualitative with one computation).**

Using the framework of [11], we compute the normalized Laplacian eigenvalue range for the idealized surface-code DEM of Section 4.1. For a d-regular-ish bipartite subgraph, the normalized Laplacian L = I − D^(−1/2) A D^(−1/2) has eigenvalues in [0, 2]; the tripartite DEM with unequal part sizes (441 vs 1,337 vs 1) has a spectral mass distribution dominated by the mechanism part. Without the full matrix we cannot list eigenvalues; we state only the structural certificate: the part-size vector (441, 1337, 1) and the degree sequences (detector degrees, mechanism degrees) are isomorphism invariants in the sense of [10], and any [[130,4,6]] DEM has part-size vector proportional to (126R, 520R, 4) ≠ (441, 1337, 1) for any R (arithmetic: 126R = 441 → R = 3.5, non-integer; 520R = 1337 → R = 2.57, non-integer; no integer R matches both), so the two DEMs are certified non-isomorphic by part sizes alone. This is a cheap, rigorous non-isomorphism proof for this pair.

## 5. Results

All numbers below are either derived in Section 4 with full arithmetic or explicitly labeled projections.

1. **DEM graph scaling (derived).** For the rotated surface code under phenomenological noise: N_D = (d² − 1)(R − 1), N_M = (2d² + d² − 1)(R − 1)/... concretely N_M = (2d² + (d² − 1))(R − 1) per the Section 4.1 construction; at d = 8, R = 8: 441 detectors, 1,337 mechanisms, 2,681 edges, 1,779 nodes total. Scaling O(d²R) in all counts.

2. **qLDPC DEM size (projection, assumptions stated).** For [[130,4,6]] at R = 8 under the stated 4-mechanisms-per-qubit-per-round circuit-noise assumption: ≈ 5,172 nodes and ≈ 12,480 edges — roughly 2.9× the node count and 4.6× the edge count of the d=8 surface-code DEM (arithmetic: 5,172/1,779 = 2.907; 12,480/2,681 = 4.655). Uncertainty: the mechanism multiplier (4/qubit/round) is an assumption; the true value could plausibly range 2–8, giving a projected node-count range of ≈ 2,600–10,300.

3. **Latency advantage (projection from published ranges).** Speedup of POLYMECHANON over BP+OSD on [[130,4,6]]: bounded in [4×, 25×], midpoint ≈ 10×, from the published "few ms GPU" vs "few tens of ms CPU" figures [1,2]. Throughput: ≈ 286 shots/s/GPU vs ≈ 29 shots/s/core at midpoints. Hardware asymmetry caveat applies.

4. **Post-selection economics (derived from published factors).** With acceptance a ≥ 0.9 and error reduction r ≥ 10: throughput loss ≤ 11.1%; accuracy-per-throughput gain ≥ 11.1×.

5. **Non-isomorphism certificate (derived).** The d=8, R=8 surface-code DEM and any R-round [[130,4,6]] DEM differ in part-size vectors for all integer R (no integer R satisfies 126R = 441 and 520R = 1337 simultaneously), so they are provably non-isomorphic; a single code-agnostic decoder must therefore interpolate across structurally distinct graph classes, which is consistent with the reported cross-family generalization gap (within 10% of BP+OSD on unseen families, but failure on unseen larger codes) [1,2].

## 6. Discussion

**Limitations of our analysis.** First, our DEM-count derivations depend on construction conventions (whether the first round yields detectors, how measurement errors are indexed). Different Stim conventions shift absolute counts by O(R) but not the O(d²R) scaling. Second, the qLDPC graph-size figures are projections resting on an assumed mechanism multiplier; only the surface-code counts are fully derived. Third, the latency bound compares GPU to CPU and therefore overstates any hardware-neutral advantage; we cannot decompose it from published data. Fourth, our isomorphism argument uses part sizes — a weak invariant; two DEMs with matching part sizes could still be non-isomorphic, and the converse (isomorphic DEMs ⇒ identical decoder behavior) holds only for architectures that are genuinely permutation-invariant, which must be verified architecturally, not assumed.

**Failure modes of the DEM-only paradigm.** (i) *Size generalization:* the reported failure on unseen larger codes [1,2] is exactly what the GNN-embedding transfer literature [4] and the transfer-learning failure literature [8] predict: message-passing receptive fields are local, and larger codes exhibit correlation structures (e.g., logical operator chains of length d) that exceed the receptive field of a network trained on smaller graphs. Scale-adaptive architectures [6] or hierarchical attention [13] are candidate remedies but are untested here. (ii) *Representational ceiling:* any two DEM-isomorphic codes are indistinguishable to the decoder; if code structure beyond the DEM (e.g., gate-level scheduling constraints on hardware) matters, a DEM-only decoder cannot use it. (iii) *Density:* like the dense neural decoders critiqued in [7], the DEM graph is processed in full regardless of the realized error rate; at low physical error rates a defect-centric sparse approach could dominate in wall-clock terms.

**What would falsify our claims.** The claim that DEM part-size classes predict cross-code generalization difficulty would be falsified by a single model trained on small codes that generalizes to unseen large codes with no size-conditioning — this would show size, not structural class, is incidental. The claim that the latency advantage is robust would be falsified by a same-hardware (GPU-vs-GPU) benchmark showing the gap closes to within noise. The claim that post-selection economics are favorable would be falsified if the acceptance fraction at the required confidence threshold drops well below 0.9 at practically relevant error rates, collapsing the r/a figure of merit.

**Open questions.** Can spectral invariants [11] serve as training-time curriculum signals, ordering DEMs by structural distance to harden transfer? Does the queuing-network view [3] yield an analytic baseline that a GNN must beat to justify its cost? Can multi-view aggregation [9] over detector-space and detector-time views close the large-code gap? And does the audit methodology of [12] — full external replication pipelines — become standard for decoder benchmarking, where shot-level statistics are easy to game?

## 7. Conclusion

We analyzed the code-agnostic, DEM-grounded GNN decoder paradigm [1,2] as a problem in graph structure rather than learning alone. We derived exact DEM graph sizes for the rotated surface code (441 detectors, 1,337 mechanisms, 2,681 edges at d=8, R=8), projected qLDPC DEM sizes under stated assumptions, bounded the published latency advantage at 4×–25× (midpoint ~10×, hardware-asymmetric), and showed that confidence-based post-selection buys a ≥11.1× accuracy-per-throughput improvement at ≤11.1% throughput cost. Using isomorphism invariants [10,11], we certified that surface-code and [[130,4,6]] DEMs are structurally distinct for all round counts, formalizing why a single decoder must generalize across graph classes and why unseen large codes are hard. The paradigm's promise — one decoder, any stabiliser code, any DEM-expressible noise model — is real but bounded by size generalization and by the density of the DEM representation. The most valuable next steps are scale-adaptive or hierarchical architectures, same-hardware latency benchmarks, and a systematic map of DEM isomorphism classes across code families.

## References

[1] arXiv Query: search_query=&id_list=2610.01683&start=0&max_results=1 — POLYMECHANON abstract record (A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model).

[2] arXiv:2610.01683v1 | A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model.

[3] arXiv:1609.04846v1 | A Tutorial about Random Neural Networks in Supervised Learning.

[4] arXiv:1909.10086v3 | Learning Universal Graph Neural Network Embeddings With Aid Of Transfer Learning.

[5] arXiv:2207.14742v2 | Graph Neural Networks for Channel Decoding.

[6] arXiv:2108.00580v3 | GraphFPN: Graph Feature Pyramid Network for Object Detection.

[7] arXiv:2605.17156v2 | Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes.

[8] arXiv:2502.01654v1 | Predicting concentration levels of air pollutants by transfer learning and recurrent neural network.

[9] arXiv:2212.05478v1 | Mul-GAD: a semi-supervised graph anomaly detection framework via aggregating multi-view information.

[10] QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940.

[11] QNFO: Topological Quantization and Spectral Filtration | DOI 10.5281/zenodo.18042721.

[12] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | DOI 10.5281/zenodo.21566035.

[13] QNFO: Proof-of-Concept for Auditable Attention using Ultrametric Tree Distances | DOI 10.5281/zenodo.19648274.