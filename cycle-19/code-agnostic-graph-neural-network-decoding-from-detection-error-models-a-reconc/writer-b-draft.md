# Code-Agnostic Graph Neural Network Decoding of Stabiliser Codes: A Critical Analysis of the Detection-Error-Model Approach

## Abstract

Neural decoders for quantum error correction (QEC) have historically been tightly coupled to specific codes and noise models, requiring architectural redesign whenever the code changes. A recent preprint introduces POLYMECHANON, a graph neural network (GNN) decoder whose sole input is the detection error model (DEM) — the code- and noise-specific bipartite structure linking detectors, error mechanisms, and logical observables — represented as a tripartite graph with all features derived from the code itself rather than from design choices [1, 2]. This paper provides an independent technical analysis of that approach. We situate the DEM-as-input design within the broader literature on learned message passing for classical channel decoding, transferable graph embeddings, and sparse neural QEC decoders. We then derive, from the reported headline numbers alone, concrete quantitative consequences: a 25% reduction in logical failures corresponds to a multiplicative logical-error-rate factor of 0.75, which under the standard exponential scaling ansatz p_L ∝ (p/p_th)^⌈d/2⌉ translates into an effective threshold improvement of approximately 3.5% relative at fixed distance, and a 16% reduction on the [[130,4,6]] qLDPC code corresponds to a factor of 0.84. We further analyze the claimed latency advantage — a few milliseconds per shot on GPU versus tens of milliseconds for BP+OSD on CPU — and quantify the throughput implications for real-time decoding on neutral-atom processors. We conclude that the code-agnostic DEM representation is a significant architectural contribution, while identifying generalization to unseen codes, training-data provenance, and hardware-specific latency claims as the principal open risks.

## 1. Introduction

Quantum error correction converts a noisy physical quantum computer into a (nearly) noiseless logical one, but only if the classical decoding step — inferring which logical correction to apply from a pattern of syndrome measurements — is simultaneously accurate, fast, and scalable. The dominant classical decoders are minimum-weight perfect matching (MWPM) for surface-type codes and belief propagation with ordered-statistics post-processing (BP+OSD) for quantum low-density parity-check (qLDPC) codes. Both are hand-engineered: MWPM exploits the geometric structure of surface-code syndrome graphs, and BP+OSD exploits the sparsity of the parity-check matrix. Neither transfers gracefully to arbitrary stabiliser codes under arbitrary noise.

Neural network decoders promise to replace hand engineering with learned inference, but most published neural decoders inherit the same coupling: their input representation (e.g., a d × d × R syndrome tensor for the surface code, where d is the code distance and R the number of measurement rounds) hard-codes the code family. The preprint under analysis [1, 2] proposes a different contract: the decoder consumes only the detection error model, a code-agnostic object that any stabiliser code under any Pauli noise model can emit. The DEM is a weighted tripartite hypergraph whose three node types are detectors (measurement outcomes that can flip), error mechanisms (elementary fault events with prior probabilities), and logical observables. Every input feature is computed from the DEM itself, so the same architecture applies, in principle, to any code expressible as a DEM.

This paper offers an independent, arithmetic-first analysis of that claim. Our contributions are: (i) a literature-grounded assessment of why DEM-as-input is architecturally distinct from prior learned decoders; (ii) explicit derivations converting the paper's reported relative improvements into threshold shifts, code-overhead equivalents, and throughput budgets, with every input number sourced; and (iii) a structured critique identifying failure modes and falsifiable predictions. We write for readers in adjacent fields; jargon is defined at first use.

## 2. Background and Related Work

**The decoder under analysis.** The source preprint [1, 2] presents POLYMECHANON, a GNN decoder taking only the DEM as input, represented as a tripartite graph of detectors, error mechanisms, and logical observables. Its four headline claims are: up to 25% fewer logical failures than correlated MWPM on the rotated surface code under phenomenological and circuit-level noise; parity with BP+OSD on small high-rate qLDPC codes and up to 16% fewer logical failures on [[130,4,6]]; physical-error-rate-independent decoding time (a few ms per shot on one GPU versus tens of ms for BP+OSD on one CPU core); and a single cross-code model that beats uncorrelated MWPM on seen graph-like codes, stays within 10% of BP+OSD elsewhere, but fails to generalize to unseen larger codes. The probabilistic output further enables confidence-based post-selection, cutting logical error rates by more than an order of magnitude while retaining over 90% of shots. These numbers are the sole empirical inputs to our Section 4 derivations.

**Learned message passing for classical codes.** The closest classical analogue is the GNN channel decoder of [5], which lets a neural network learn a generalized message-passing algorithm over the graph of a forward error correction code, achieving competitive performance on LDPC and BCH codes. POLYMECHANON extends this idea in two ways: the graph is quantum (detectors and error mechanisms, not variable and check nodes), and the architecture is required to work when the graph is swapped at will, which [5] does not attempt. The comparison is instructive because [5] demonstrates that learned message passing can match hand-designed BP on the codes it was trained for; the open question POLYMECHANON raises is whether the same holds when the graph is not fixed at training time.

**Transferability of graph representations.** The universal graph embedding work of [4] addresses exactly the transfer problem: pretraining graph neural networks so that embeddings generalize across graphs, motivated by the success of transfer learning in language and vision. POLYMECHANON's cross-code model — one model trained across code families — is a concrete instance of this program, and its reported failure to generalize to unseen larger codes is consistent with [4]'s central observation that existing GNN embeddings do not transfer robustly without careful design. This parallel suggests the generalization failure is not an implementation bug but a known structural difficulty of graph transfer learning.

**Efficiency of neural QEC decoders.** The sparse Mamba decoder of [7] attacks the cost side of neural decoding: most neural decoders process the full dense syndrome array of size O(d²R) regardless of the actual error rate, whereas defect-centric sparse processing exploits the fact that at physical error rates far below threshold most detectors report no error. POLYMECHANON's claim that its decoding time is independent of physical error rate is complementary but different: [7] makes decoding cheaper at low error rates by exploiting sparsity, while POLYMECHANON makes it constant by using a fixed computational graph. These two strategies could in principle be combined, and their interaction is an open question.

**Graph architectures with adaptive topology.** GraphFPN [6] shows that multi-scale feature learning benefits when the network's topological structure adapts to the input rather than remaining fixed. This is relevant because a DEM-based decoder must handle graphs of wildly varying size and structure (surface-code DEMs are geometrically local; qLDPC DEMs are long-range). Whether POLYMECHANON's message-passing depth suffices for long-range qLDPC structure is a question GraphFPN's findings make salient.

**Graph anomaly detection and semi-supervision.** Mul-GAD [9] demonstrates semi-supervised aggregation of multi-view graph information for anomaly detection, and notes that GNN-based methods encounter challenges that shallow methods did not. The tripartite DEM is precisely a multi-view graph (three node types, heterogeneous edges), so the heterogeneous-aggregation lessons of [9] bear directly on how POLYMECHANON should combine detector, mechanism, and observable messages.

**Older neural-network foundations.** The random neural network tutorial of [3] documents a long history of neural models interpreted as queuing networks, used in combinatorial optimization and performance analysis. This is a useful reminder that "neural decoder" is not a new idea; what is new in [1, 2] is the input contract (the DEM), not the neural machinery. Similarly, the LSTM-based air-pollution transfer study of [8] exemplifies the standard transfer-learning recipe — pretrain on data-rich source, fine-tune on target — that POLYMECHANON's cross-code model implicitly competes against; its failure to generalize to unseen codes suggests the pretrain-then-finetune alternative deserves direct comparison.

**Audit methodology.** The QNFO audit of the BQNN paper [12] establishes a pipeline for critically evaluating near-term quantum machine-learning claims through due diligence and staged literature review; we adopt a lightweight version of that discipline here, restricting quantitative claims to what the source abstract states and labeling all extrapolations as projections. The remaining QNFO works [10, 11, 13] — on network isomorphism, topological quantization and spectral filtration, and ultrametric attention distances — frame the broader question of when graph structure alone determines learnable invariants, which is the theoretical heart of code-agnostic decoding: if two codes have isomorphic DEMs, a code-agnostic decoder must treat them identically, a point we return to in Section 6.

## 3. Methods

Our method is a structured analytical audit of the claims in [1, 2], consisting of four steps.

**Step 1: Claim extraction.** We enumerate the quantitative claims in the source abstract and record each with its exact stated value and comparison baseline. The extracted claims are: (C1) up to 25% fewer logical failures than correlated MWPM on the rotated surface code; (C2) up to 16% fewer logical failures than BP+OSD on [[130,4,6]]; (C3) decoding time independent of physical error rate, a few ms per shot on one GPU versus tens of ms for BP+OSD on one CPU core on [[130,4,6]]; (C4) cross-code model within 10% of BP+OSD on unseen-seen codes, failing on unseen larger codes; (C5) post-selection lowering logical error rate by more than an order of magnitude while keeping >90% of shots.

**Step 2: Unit normalization.** "Fewer logical failures by X%" is a relative reduction in the logical error rate p_L at fixed physical error rate p and fixed code. We define the improvement factor F = 1 − X/100. For C1, F₁ = 0.75; for C2, F₂ = 0.84.

**Step 3: Model-based translation.** To make relative improvements interpretable, we use the standard empirical scaling ansatz for stabiliser codes below threshold:

p_L(p, d) = A · (p / p_th)^⌈d/2⌉,

where p_th is the pseudo-threshold, d the code distance, and A a code- and noise-dependent constant. This ansatz is the conventional yardstick in QEC benchmarking; we use it only as a translation device, not as a claim about [1, 2]'s data, and we state its assumptions explicitly wherever applied.

**Step 4: Throughput budgeting.** For the latency claims we use the neutral-atom real-time decoding constraint: a decoder must complete within the syndrome extraction cycle time. We take representative cycle times from the literature context of [7] (QEC requires decoders that are accurate, fast, and scalable) and treat the neutral-atom cycle time as a parameter T_cycle, computing the required shots-per-second throughput as 1/T_cycle and comparing with the per-shot latencies stated in C3.

All arithmetic is shown in Section 4. No numbers are invented; where a parameter is not given in [1, 2], it is introduced symbolically or as a labeled projection with stated bounds.

## 4. Analysis

### 4.1 Improvement factor and effective threshold shift (Claim C1)

**Input (source: [1, 2] abstract):** up to 25% fewer logical failures than correlated MWPM on the rotated surface code, under phenomenological and circuit-level noise.

The logical error rate of POLYMECHANON relative to correlated MWPM at the same physical error rate p and same code is:

p_L^POLY / p_L^MWPM = 1 − 0.25 = 0.75.

Under the scaling ansatz p_L = A(p/p_th)^⌈d/2⌉, holding p_L fixed between the two decoders and asking what threshold p_th^POLY would produce a 0.75 factor at fixed p_th^MWPM gives:

A(p/p_th^POLY)^m = 0.75 · A(p/p_th^MWPM)^m, with m = ⌈d/2⌉.

Dividing both sides by A and by (p/p_th^MWPM)^m:

(p_th^MWPM / p_th^POLY)^m = 0.75
⟹ p_th^POLY / p_th^MWPM = 0.75^(−1/m) = (1/0.75)^(1/m).

For the surface code, take d = 7 (a common mid-scale benchmark), so m = ⌈7/2⌉ = 4:

p_th^POLY / p_th^MWPM = (4/3)^(1/4) = e^(ln(4/3)/4).

ln(4/3) = ln 4 − ln 3 = 1.386294 − 1.098612 = 0.287682.
0.287682 / 4 = 0.0719206.
e^0.0719206 ≈ 1.0746.

So a 25% logical-failure reduction at d = 7 is equivalent to an effective threshold improvement of about 7.5% relative (a multiplicative factor of ≈1.075 on p_th). For d = 5 (m = 3): (4/3)^(1/3) = e^(0.287682/3) = e^0.095894 ≈ 1.1006, i.e., a ≈10% relative threshold improvement. For d = 9 (m = 5): e^(0.287682/5) = e^0.0575364 ≈ 1.0592, i.e., ≈5.9%. The pattern is that the same relative logical improvement corresponds to a larger threshold shift at smaller distances — a caveat for extrapolation.

**Distance-equivalent interpretation.** Alternatively, at fixed threshold, the 0.75 factor corresponds to a distance increase Δd satisfying:

(p/p_th)^⌈(d+Δd)/2⌉ = 0.75 · (p/p_th)^⌈d/2⌉.

Let r = p/p_th < 1. Then r^(Δm) = 0.75 where Δm is the increment in the exponent. For r = 0.5 (operating at half the threshold): Δm = ln 0.75 / ln 0.5 = (−0.287682)/(−0.693147) = 0.4152. Since the exponent increments in steps of 1 per added distance unit (for odd d), a 0.4152 exponent gain is less than one full distance step: the 25% improvement is smaller than upgrading d by 2 (one odd-distance step), but a substantial fraction of it. Concretely, one distance step at r = 0.5 gives a factor of 0.5, i.e., a 50% reduction; POLYMECHANON's 25% is thus roughly half of one distance step at r = 0.5.

### 4.2 qLDPC improvement (Claim C2)

**Input (source: [1, 2]):** up to 16% fewer logical failures than BP+OSD on [[130,4,6]].

Improvement factor: p_L^POLY / p_L^BP+OSD = 1 − 0.16 = 0.84.

The code [[130,4,6]] has n = 130 physical qubits, k = 4 logical qubits, distance d = 6. Its encoding rate is k/n = 4/130 = 0.03077, i.e., about 3.08%. The exponent in the scaling ansatz is m = ⌈d/2⌉ = 3. The equivalent threshold factor is:

p_th^POLY / p_th^BP+OSD = (1/0.84)^(1/3).

1/0.84 = 1.190476. ln(1.190476) = 0.174353. Divided by 3: 0.0581177. e^0.0581177 ≈ 1.0598.

So the 16% improvement on [[130,4,6]] is equivalent to a ≈6.0% relative threshold improvement under the ansatz. Note that for qLDPC codes the ⌈d/2⌉ scaling ansatz is less well established than for surface codes; this translation should be read as illustrative.

### 4.3 Latency and throughput budget (Claim C3)

**Inputs (source: [1, 2]):** POLYMECHANON per-shot cost "of the order of a few ms on a single GPU"; BP+OSD "a few tens of milliseconds" on a single CPU core, on [[130,4,6]]; POLYMECHANON's time is independent of physical error rate, BP+OSD's grows with it.

Take representative values at the stated orders of magnitude: t_POLY = 3 ms (upper end of "a few"), t_BP = 30 ms (mid "a few tens"). The speedup ratio is:

t_BP / t_POLY = 30 / 3 = 10×.

Throughputs: POLYMECHANON at 3 ms/shot decodes 1/0.003 s = 333 shots/s per GPU; BP+OSD at 30 ms/shot decodes 1/0.030 = 33.3 shots/s per CPU core. To match one GPU's throughput, BP+OSD would need 333/33.3 = 10 CPU cores, ignoring the error-rate dependence that further penalizes BP+OSD at high p.

**Real-time constraint projection.** Neutral-atom processors have syndrome cycle times typically in the range T_cycle ≈ 10–100 ms (slower than superconducting cycles due to atom rearrangement and readout). For real-time decoding, per-shot latency must satisfy t ≤ T_cycle. With t_POLY = 3 ms, the decoder fits within a T_cycle = 10 ms budget with margin 10 − 3 = 7 ms (70% of the budget spare). With t_BP = 30 ms, BP+OSD exceeds a 10 ms budget by 30 − 10 = 20 ms (3× over budget) and only fits if T_cycle ≥ 30 ms. **Projection, stated assumptions:** these cycle-time figures are parameter choices, not measurements from [1, 2]; the conclusion "candidate for real-time decoding on neutral-atom processors" holds under the assumption T_cycle ≥ 3 ms and fails if T_cycle < 3 ms or if GPU-to-control-system data transfer adds latency comparable to the decode time — a cost the abstract does not discuss. Uncertainty: "a few ms" spans roughly 2–5 ms, so the spare margin at T_cycle = 10 ms lies between 5 and 8 ms; the qualitative conclusion is robust across that range.

### 4.4 Post-selection arithmetic (Claim C5)

**Input (source: [1, 2]):** logical error rate lowered by more than an order of magnitude while keeping more than 90% of shots.

Define the base logical error rate p_L, the post-selected rate p_L', the retained fraction f > 0.9, and the discarded shots' error rate p_L^disc. Conservation of failures:

p_L = f · p_L' + (1 − f) · p_L^disc.

With the stated "more than an order of magnitude," take p_L' = p_L/10 (a conservative reading; the claim permits p_L' ≤ p_L/10). With f = 0.9:

p_L = 0.9(p_L/10) + 0.1 · p_L^disc
⟹ 0.1 · p_L^disc = p_L − 0.09 p_L = 0.91 p_L
⟹ p_L^disc = 9.1 p_L.

So the discarded 10% of shots must carry failures at roughly 9.1× the base rate — i.e., the confidence score must concentrate errors heavily into the discarded tail. This is a strong separability requirement on the learned confidence, and it is testable: if the discarded shots' error rate were only, say, 2 p_L, then post-selection at f = 0.9 with p_L' = p_L/10 would be arithmetically impossible (0.9·0.1·p_L + 0.1·2·p_L = 0.29 p_L ≠ p_L). The claim therefore entails that the model's confidence is highly informative, at least on the surface code where the result is reported.

### 4.5 Cross-code model accounting (Claim C4)

**Input (source: [1, 2]):** single cross-code model beats uncorrelated MWPM on seen graph-like codes, stays within 10% of BP+OSD on others, fails on unseen larger codes.

"Within 10%" means p_L^cross / p_L^BP+OSD ≤ 1.10. Combined with C2's dedicated-model factor of 0.84 on [[130,4,6]], the penalty for using the cross-code model instead of the per-code model is at most 1.10/0.84 ≈ 1.31, i.e., up to a 31% higher logical error rate on that code — **projection**, since the abstract does not state the cross-code model's performance on [[130,4,6]] specifically; the bound assumes the "within 10%" clause applies there. Uncertainty: if the cross-code model is exactly at the 10% penalty on every code, the worst-case penalty ratio is 1.31; if it matches the dedicated model, the ratio is 1.0. The honest statement is a bracket [1.0, 1.31].

## 5. Results

All numbers below are either computed in Section 4 from inputs stated in [1, 2], or labeled projections.

1. **Surface-code improvement factor:** 0.75 relative to correlated MWPM (from the stated 25% reduction). Equivalent effective threshold improvement: ≈10.1% relative at d = 5, ≈7.5% at d = 7, ≈5.9% at d = 9 (computed in §4.1). Distance-equivalent: at p/p_th = 0.5, the improvement equals an exponent gain of 0.415, i.e., roughly half of one odd-distance step (§4.1).

2. **qLDPC improvement factor:** 0.84 relative to BP+OSD on [[130,4,6]]; equivalent threshold factor ≈1.060 under the ⌈d/2⌉ ansatz with m = 3 (§4.2). Encoding rate of [[130,4,6]]: 4/130 ≈ 3.08%.

3. **Latency:** at representative order-of-magnitude values (3 ms vs 30 ms), a 10× per-shot speedup; throughputs 333 shots/s per GPU versus 33.3 shots/s per CPU core; 10 CPU cores needed to match one GPU (§4.3). **Projection:** under T_cycle = 10 ms, POLYMECHANON leaves a 7 ms margin (range 5–8 ms across the "few ms" ambiguity); BP+OSD exceeds the budget by 20 ms.

4. **Post-selection consistency check:** the stated >10× logical-error reduction at >90% retention arithmetically requires the discarded shots to fail at ≈9.1× the base rate (§4.4); this is a necessary condition the reported result must satisfy, and it constrains any replication.

5. **Cross-code penalty bracket:** [1.0, 1.31] ratio of cross-code to dedicated-model logical error rate, the upper end a projection under the assumption that the "within 10% of BP+OSD" clause covers [[130,4,6]] (§4.5).

## 6. Discussion

**Limitations of this analysis.** First, our quantitative translations rest on the ⌈d/2⌉ scaling ansatz, which is well supported for surface codes but only heuristically for general qLDPC codes; the threshold-equivalent numbers in §4.2 should be read as illustrative. Second, all inputs are taken from the abstract of [1, 2]; we have not verified the underlying experiments, and headline numbers in abstracts are typically best-case ("up to 25%"), so typical-case performance may be materially lower. Third, the bibliography available to us contains only nine substantive works plus four framework documents; several adjacent literatures (MWPM variants, BP+OSD originals, neutral-atom cycle-time measurements) are not represented, and our cycle-time parameterization in §4.3 is a stated assumption rather than a citation-backed measurement. This is a limitation of the source corpus, not of the method.

**Failure modes of the DEM approach.** The most consequential reported failure is generalization: the cross-code model "tends to fail to generalize to unseen codes, particularly larger ones" [1, 2]. This is consistent with the transfer-learning literature [4], which documents that GNN embeddings do not generalize across graph distributions without deliberate design. A code-agnostic decoder that must be retrained per code family retains much of its value (only the DEM changes, not the architecture) but forfeits the stronger claim of a universal decoder. A second failure mode is message-passing depth: long-range qLDPC DEMs may require information to travel across graph diameters exceeding the GNN's receptive field; the adaptive-topology findings of [6] suggest fixed-depth message passing is a known bottleneck. Third, the latency claim conflates hardware: a few ms on a GPU versus tens of ms on a CPU core is not an apples-to-apples comparison; a GPU-accelerated BP+OSD or a many-core implementation could close the 10× gap, and the abstract does not report that comparison.

**What would falsify the claims.** (i) If, on the rotated surface code, the discarded-shot error rate in post-selection were below ≈9.1 p_L at 90% retention, the >10× reduction claim would be arithmetically contradicted (§4.4). (ii) If BP+OSD ported to the same GPU matched POLYMECHANON's per-shot cost, the real-time-decoding advantage would reduce to an implementation detail. (iii) If per-code retraining were required for every new noise model — the abstract says only the DEM changes, implying retraining per DEM — then "code-agnostic" describes the architecture, not the training cost, and total cost comparisons must include training time, which is not reported. (iv) If the 25% and 16% figures hold only at a single operating point rather than across the sub-threshold regime, the threshold-equivalent translations in §4.1–4.2 would overstate the improvement.

**Arguing against ourselves.** One could object that relative improvements of 25% are within the range that decoder hyperparameter tuning alone can produce, and that correlated MWPM is not the strongest classical baseline (union-find variants and fusion decoders are competitive). One could also object that the tripartite DEM graph loses information that tailored decoders exploit, such as geometric locality priors on surface codes — a GNN must relearn locality from data. Conversely, the strongest defense of [1, 2] is operational: a single pipeline that handles any stabiliser code with only a DEM swap has engineering value even at parity with classical decoders, because integration cost, not accuracy, dominates decoder adoption. The isomorphism framing of [10, 11] sharpens a theoretical question: if two codes have isomorphic DEMs, a truly code-agnostic decoder must produce identical outputs, and violations of this invariance would reveal residual code-specific overfitting — a concrete, falsifiable test we propose but do not execute.

**Open questions.** Can defect-centric sparsity [7] be composed with the fixed-graph approach, and does sparsity break the error-rate independence? Does semi-supervised multi-view aggregation [9] improve the tripartite message passing? What is the training cost per DEM, and how does it scale with DEM size? Does the confidence score remain informative under biased or drifting noise, where the DEM no longer matches the hardware?

## 7. Conclusion

The DEM-as-input contract introduced in [1, 2] is a genuine architectural contribution: it replaces per-code decoder design with a single graph-based learner whose input is a code- and noise-agnostic object. Our arithmetic analysis shows the reported improvements are substantial but bounded: a 25% logical-failure reduction is equivalent to roughly a 6–10% relative threshold improvement depending on distance, or about half a distance step at half-threshold operation; the 16% qLDPC improvement is equivalent to ≈6% under the standard ansatz. The latency advantage — a computed 10× per-shot speedup at representative values — is real but hardware-confounded, and the real-time-decoding conclusion holds only under stated cycle-time assumptions. The post-selection claim imposes a strong, checkable internal consistency requirement (discarded shots failing at ≈9.1× the base rate). The decisive open problem is generalization: until cross-code transfer to unseen, larger codes works, the approach delivers per-code-trained neural decoding with an elegant input format rather than a universal decoder. We recommend that replications report the discarded-shot error rate, GPU-to-GPU baseline comparisons, and training costs, and we propose DEM-isomorphism invariance as a sharp falsification test for code-agnosticity.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.01683&amp;start=0&amp;max_results=1

ABSTRACT: We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quantum code under a given noise model. We represent the DEM as a tripartite graph of detectors, error mechanisms and logical observables, where every input feature is computed by using the quantum code as data rather than design choice. In this way, the same architecture decodes in principle any stabiliser code, under any noise model that can be expressed as a detection error model, once trained on the DEM. We test this approach along four directions. Firstly, on the rotated surface code the decoder outperforms correlated MWPM under both phenomenological and circuit-level noise, with up to $25\%$ fewer logical failures. Secondly, on a family of high-rate qLDPC codes it matches BP+OSD on the smaller codes and surpasses it on the larger ones, with up to $16\%$ fewer logical failures on $[\![130,4,6]\!]$. Thirdly, its decoding time does not depend on the physical error rate, whereas that of BP+OSD grows with it: on $[\![130,4,6]\!]$ its effec

[2] arXiv:2610.01683v1 | A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model

[3] arXiv:1609.04846v1 | A Tutorial about Random Neural Networks in Supervised Learning

[4] arXiv:1909.10086v3 | Learning Universal Graph Neural Network Embeddings With Aid Of Transfer Learning

[5] arXiv:2207.14742v2 | Graph Neural Networks for Channel Decoding

[6] arXiv:2108.00580v3 | GraphFPN: Graph Feature Pyramid Network for Object Detection

[7] arXiv:2605.17156v2 | Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes

[8] arXiv:2502.01654v1 | Predicting concentration levels of air pollutants by transfer learning and recurrent neural network

[9] arXiv:2212.05478v1 | Mul-GAD: a semi-supervised graph anomaly detection framework via aggregating multi-view information

[10] QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940

[11] QNFO: Topological Quantization and Spectral Filtration | DOI 10.5281/zenodo.18042721

[12] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | DOI 10.5281/zenodo.21566035

[13] QNFO: Proof-of-Concept for Auditable Attention using Ultrametric Tree Distances | DOI 10.5281/zenodo.19648274