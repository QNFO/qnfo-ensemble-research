# Arithmetic-First Assessment of a Code-Agnostic Graph Neural Network Decoder Grounded in the Detection Error Model

## Abstract

Graph neural network (GNN) decoders for quantum error correction have historically been locked to specific code families through their input representations. The POLYMECHANON decoder [1, 2] proposes a different contract: its sole input is the detection error model (DEM) — a tripartite graph of detectors, error mechanisms, and logical observables — so that the code enters as data rather than as an architectural design choice. This paper provides an independent, arithmetic-first assessment of that claim. We convert the reported headline numbers into concrete quantities: a 25% reduction in logical failures versus correlated MWPM on the rotated surface code corresponds to an improvement factor of 0.75, equivalent under the standard scaling ansatz $p_L \propto (p/p_{\mathrm{th}})^{\lceil d/2 \rceil}$ to a relative pseudo-threshold improvement of ≈10.06% at $d = 5$ and ≈7.46% at $d = 7$; a 16% reduction on the $[[130,4,6]]$ qLDPC code gives a factor of 0.84 and an equivalent threshold improvement of ≈5.98%. The reported latency advantage bounds the speedup in $[4\times, 25\times]$ with midpoint ≈10×, subject to a GPU-versus-CPU hardware asymmetry. We derive DEM graph sizes for canonical cases (441 detectors, 1,337 mechanisms, 2,681 edges at $d = 8$, $R = 8$), prove a cheap non-isomorphism certificate between surface-code and qLDPC DEMs via part-size vectors, and show that the reported post-selection result (>10× error reduction at >90% shot retention) arithmetically requires discarded shots to fail at ≈9.1× the base rate — a strong, testable separability condition. Size generalization, DEM fidelity, and hardware-fair latency comparison emerge as the principal open risks, each paired with a falsification experiment.

## 1. Introduction

Fault-tolerant quantum computation requires a classical decoding layer that converts syndrome measurement streams into logical corrections faster than errors accumulate. The teams building this layer today face a structural bottleneck: the dominant decoders — minimum-weight perfect matching (MWPM) for surface-type codes and belief propagation with ordered-statistics post-processing (BP+OSD) for quantum low-density parity-check (qLDPC) codes — are hand-engineered per code family, and each pays a specific price. MWPM ignores error correlations and therefore leaves accuracy on the table; BP+OSD's runtime grows with the physical error rate and code size, which blocks its use as a real-time decoder on the high-rate qLDPC codes that promise the largest qubit-overhead savings. Every new code family or noise model therefore triggers a new decoder engineering effort, and the delay between designing a code and decoding it reliably is measured in engineering months.

Neural decoders promise learned inference at constant time, but most published architectures hard-code the code family: the input representation, for example a $d \times d \times R$ syndrome tensor, encodes the geometry directly into the network's shape. POLYMECHANON [1, 2] proposes a different contract: the decoder consumes only the DEM, a code-agnostic object that any stabiliser code under any expressible noise model can emit, rendered as a tripartite graph with all input features computed from the code as data. If this contract holds at scale, the decision that changes is concrete: a code designer would compile a DEM and run one training job — reported in [1, 2] to take from hours to a few days on four GPUs — instead of commissioning a bespoke decoder, and a real-time control stack could budget a fixed, error-rate-independent per-shot decoding cost.

This paper subjects that contract to an arithmetic-first assessment with three contributions:

- Explicit derivations converting the reported relative improvements into improvement factors, threshold-equivalent shifts, distance equivalents, and throughput budgets, with every input number traced to [1, 2] and every assumption labeled (Sections 4.1–4.4).
- A structural analysis of the DEM-as-graph representation, including exact node and edge counts for canonical cases, an $O(d^2 R)$ scaling law, an isomorphism-invariance ceiling on any DEM-only decoder, and a cheap non-isomorphism certificate between code families (Sections 4.5–4.6).
- A structured critique identifying size generalization, DEM fidelity, hardware-asymmetric latency comparison, and training-cost opacity as the principal risks, each paired with a falsifiable experiment (Sections 4.7 and 6).

## 2. Background and Related Work

**The decoder under analysis [1, 2].** POLYMECHANON is a GNN decoder whose sole input is the DEM, represented as a tripartite graph of detectors, error mechanisms, and logical observables, with every input feature computed using the quantum code as data rather than design choice [1, 2]. Its reported results are specific: up to 25% fewer logical failures than correlated MWPM on the rotated surface code under phenomenological and circuit-level noise; parity with BP+OSD on smaller qLDPC codes and up to 16% fewer failures on $[[130,4,6]]$; decoding time independent of physical error rate, of the order of a few ms per shot on a single GPU against a few tens of milliseconds for BP+OSD on a single CPU core on $[[130,4,6]]$; a single cross-code model that outperforms uncorrelated MWPM on graph-like codes seen during training and stays within 10% of BP+OSD on the others, while tending to fail to generalize to unseen codes, particularly larger ones; and confidence-based post-selection lowering the logical error rate by more than an order of magnitude on the surface code while keeping more than 90% of the shots. Section IV of [1, 2] defines the advantage metric $\Lambda(p) = \mathrm{LER}_{\mathrm{baseline}}(p)/\mathrm{LER}_{\mathrm{GNN}}(p)$ and its geometric mean $\Lambda$ over sub-threshold noise points, which is the quantity our improvement factors translate. Section V of [1, 2] adds that moving between codes, families, or noise models required no network change, only a new DEM and a new training run taking from hours to a few days on four GPUs. These statements are the sole empirical inputs to our derivations.

**Learned message passing for classical codes [5].** This work proposes a fully differentiable GNN architecture for channel decoding and demonstrates competitive performance on LDPC and BCH codes, letting the network learn a generalized message-passing algorithm over the graph representing the forward-error-correction code. Its authors state explicitly that the computational complexity of their decoder is high compared to BP, and they pose as an open question whether training a universal GNN decoder — one set of weights for multiple codes — is possible. POLYMECHANON is a direct answer to that question in the quantum setting, and the complexity caveat of [5] foreshadows the latency accounting we perform in Section 4.3.

**Universal graph embeddings via transfer learning [4].** This work builds a universal graph encoder (DUGnn) whose embeddings can be re-utilized across datasets by leveraging transfer learning, reporting state-of-the-art results on graph classification benchmarks and an ablation on the QM8 quantum-mechanics dataset (2,1786 compounds) where the encoder trained from scratch without the multi-task decoder achieves a validation MAE of 11.16 against 14.60 for the MPNN baseline. The relevant lesson for DEM decoding is that transferable graph representations required carefully designed components, not an off-the-shelf message-passing stack; POLYMECHANON's reported failure on unseen larger codes is the quantum instance of the transfer difficulty [4] documents.

**Sparse defect-centric decoding [7].** The Sparse Mamba Decoder (SMD) attacks the cost side of neural QEC decoding: it processes only active detection events rather than the full dense syndrome array of size $O(d^2 R)$, achieving $\mathcal{O}(k)$ complexity in the number of defects $k$, and reports outperforming MWPM, Tesseract, and Belief Matching by 40–91% at $d = 5$–$11$ under depolarizing noise with perfect stabilizers. SMD's training footprint is also concrete: roughly 7.6–7.7 M parameters trained on a single RTX 4090, with the larger SI1000 configuration (≈16 M parameters, $R = 120$) requiring an H200. POLYMECHANON's constant-time claim is complementary but different: [7] makes decoding cheaper at low error rates by exploiting sparsity, whereas [1, 2] makes it constant by using a fixed computational graph whose size is set by the code, not the realized error pattern. Their interaction is quantified structurally in Section 4.5.

**Adaptive-topology graph architectures [6].** GraphFPN shows that multi-scale feature learning benefits when network topology adapts to the input rather than remaining fixed, inheriting its graph structure from a superpixel hierarchy and outperforming fixed-topology baselines on MS-COCO detection. This is salient because a DEM decoder must handle graphs of widely varying size and structure — geometrically local surface-code DEMs versus long-range qLDPC DEMs — and whether fixed-depth message passing suffices for long-range qLDPC correlations is a question GraphFPN's findings make pressing. Scale-pyramidal variants are a natural but untested remedy for the size-generalization failure reported in [1, 2].

**Random neural networks [3].** This tutorial frames the Random Neural Network model as both a learning tool and a queuing network, covering 25 years of applications and training algorithms from gradient descent to Levenberg-Marquardt. The queuing view is useful here because DEM decoding is fundamentally a probabilistic flow problem: error mechanisms inject probability mass that must be routed to detectors. It is also a reminder that neural computation over stochastic networks is a mature field; what is new in [1, 2] is the input contract — the DEM — not the neural machinery.

**Transfer learning for recurrent predictors [8].** The LSTM air-pollutant transfer study applies the standard pretrain-then-finetune recipe to predict pollutant concentrations in Macau, exemplifying both the recipe and its standard risk — degradation on target domains far from the source. It calibrates the cross-code claims of [1, 2] and motivates a direct comparison between pretrain-then-finetune and joint multi-code training as routes to a universal DEM decoder.

**Semi-supervised graph anomaly detection [9].** Mul-GAD aggregates multi-view information for graph anomaly detection and notes that GNN-based methods face challenges relative to shallow baselines, addressing poor generalization across datasets through view-level and feature-level fusion with a theoretical justification via Venn diagrams. Syndrome decoding is formally an anomaly-localization task on the DEM graph — defects are anomalous detector firings — and the tripartite DEM is precisely a multi-view heterogeneous graph, so its aggregation lessons bear on how detector, mechanism, and observable messages should be combined.

**Prior appraisals and structural frameworks [10, 11, 12].** The QNFO reconciled assessment of POLYMECHANON [10] performs the same claim-extraction exercise we extend here, reporting the identical improvement factors (0.75, 0.84), the latency bracket $[4\times, 25\times]$, and the 9.1× discarded-shot requirement; our contribution sharpens the derivations and adds the isomorphism analysis. The QNFO network-isomorphism framework [11] supplies the formal machinery — isomorphism as exact structural equivalence under relabeling, and a layered L1–L2–L3 hierarchy from topology through dynamics — that we adapt to DEM graphs in Section 4.6: two codes whose DEMs are isomorphic as attributed graphs are indistinguishable inputs to any code-agnostic decoder. Finally, the QNFO analysis of exact maximum-likelihood decoding via rank-decomposition dynamic programming [12] exemplifies the reporting standard this paper adopts: quantitative claims of three clearly labeled kinds (exact closed-form computation, complexity arithmetic from stated bounds, and error budgets), with no new empirical measurements and cited runtimes labeled as reported. Its result that exact logical-class probabilities differ measurably from dominant-pattern estimates even on the three-qubit repetition code (0.756 versus 0.729 at $p = 0.1$) is a caution for any decoder, including DEM-only GNNs, that optimizes a surrogate of the true likelihood.

## 3. Methods

**Definitions.** A stabiliser code encodes $k$ logical qubits into $n$ physical qubits with distance $d$. Repeated syndrome measurement produces *detectors*: parity checks that must yield 0 in the absence of errors. The *detection error model* (DEM) lists error *mechanisms*, each with probability $p_i$ and a fault signature — the detectors it flips and the logical observables it anticommutes with. Decoding is the task of inferring, from detector firings, the most likely logical observable flips.

**Analytical pipeline.**

1. **Claim extraction.** From [1, 2] we extract five claims: (C1) up to 25% fewer logical failures than correlated MWPM on the rotated surface code; (C2) up to 16% fewer than BP+OSD on $[[130,4,6]]$; (C3) decoding time independent of physical error rate, a few ms per shot on one GPU versus a few tens of ms for BP+OSD on one CPU core; (C4) a cross-code model within 10% of BP+OSD on seen families, tending to fail on unseen larger codes; (C5) post-selection lowering the logical error rate by more than an order of magnitude while keeping more than 90% of shots.

2. **Unit normalization.** "X% fewer logical failures" is a relative reduction in the logical error rate $p_L$ at fixed physical error rate and code. The improvement factor is $F = 1 - X/100$, giving $F_1 = 0.75$ and $F_2 = 0.84$. In the notation of [1, 2], $F = 1/\Lambda$ at the reported operating point.

3. **Model-based translation.** We use the standard sub-threshold scaling ansatz $p_L(p, d) = A \cdot (p/p_{\mathrm{th}})^{\lceil d/2 \rceil}$ as a translation device only, stating its assumptions wherever applied. It is well supported for surface codes and only heuristic for general qLDPC codes.

4. **Structural sizing.** We model the DEM as an attributed tripartite graph $G = (D \cup M \cup L, E)$ and derive node and edge counts for canonical cases under explicitly stated construction conventions.

5. **Throughput budgeting.** Latency claims are bounded using the published ranges at face value, with the GPU-versus-CPU hardware asymmetry stated as a caveat; real-time feasibility is assessed against a parameterized cycle time $T_{\mathrm{cycle}}$, labeled as a projection.

No numbers are invented; every derived quantity traces to [1, 2] plus labeled assumptions. Where a quantity depends on a convention or parameter choice not fixed by [1, 2] — the mechanism multiplier for qLDPC DEMs, the cycle time $T_{\mathrm{cycle}}$, the operating point $r = p/p_{\mathrm{th}}$ — it is labeled a projection and its assumption stated inline.

## 4. Analysis

### 4.1 Improvement factor and effective threshold shift (C1)

Input [1, 2]: up to 25% fewer logical failures than correlated MWPM on the rotated surface code. The relative logical error rate is

$$\frac{p_L^{\mathrm{POLY}}}{p_L^{\mathrm{MWPM}}} = 1 - 0.25 = 0.75.$$

Under the ansatz with $m = \lceil d/2 \rceil$, holding the operating point $r = p/p_{\mathrm{th}}$ fixed:

$$\left(\frac{p_{\mathrm{th}}^{\mathrm{MWPM}}}{p_{\mathrm{th}}^{\mathrm{POLY}}}\right)^{m} = 0.75 \quad \Longrightarrow \quad \frac{p_{\mathrm{th}}^{\mathrm{POLY}}}{p_{\mathrm{th}}^{\mathrm{MWPM}}} = \left(\frac{1}{0.75}\right)^{1/m} = \left(\frac{4}{3}\right)^{1/m}.$$

At $d = 5$ ($m = 3$): $\ln(4/3) = 1.3862943611 - 1.0986122887 = 0.2876820724$; $0.2876820724/3 = 0.0958940241$; $e^{0.0958940241} = 1.1006424$, i.e. a ≈10.06% relative threshold improvement. At $d = 7$ ($m = 4$): $0.2876820724/4 = 0.0719205181$; $e^{0.0719205181} = 1.0745699$, i.e. ≈7.46%. At $d = 9$ ($m = 5$): $0.2876820724/5 = 0.0575364145$; $e^{0.0575364145} = 1.0592238$, i.e. ≈5.92%. The same relative improvement corresponds to a larger threshold shift at smaller distance — a caveat for extrapolating any single figure.

**Distance-equivalent reading.** At fixed threshold with $r = p/p_{\mathrm{th}} = 0.5$, the exponent gain is

$$\Delta m = \frac{\ln 0.75}{\ln 0.5} = \frac{-0.2876820724}{-0.6931471806} = 0.4150375.$$

One odd-distance step ($\Delta d = 2$) gives a factor $0.5^{\Delta m \cdot \text{(per step)}}$: since $p_L \propto r^m$, raising $m$ by 1 multiplies $p_L$ by $r = 0.5$ at this operating point. The 25% improvement (factor 0.75) is therefore roughly half of one distance step at $r = 0.5$, since $0.5^{0.415} \approx 0.75$.

### 4.2 qLDPC improvement (C2)

Input [1, 2]: up to 16% fewer logical failures than BP+OSD on $[[130,4,6]]$, so $n = 130$, $k = 4$, $d = 6$, and the encoding rate is $k/n = 4/130 = 0.0307692 \approx 3.08\%$. The improvement factor is $1 - 0.16 = 0.84$; with $m = \lceil 6/2 \rceil = 3$:

$$\frac{p_{\mathrm{th}}^{\mathrm{POLY}}}{p_{\mathrm{th}}^{\mathrm{BP+OSD}}} = \left(\frac{1}{0.84}\right)^{1/3}.$$

Arithmetic: $1/0.84 = 1.1904762$; $\ln(1.1904762) = 0.1743534$; $0.1743534/3 = 0.0581178$; $e^{0.0581178} = 1.0598398$. So the equivalent relative threshold improvement is ≈5.98%, illustrative only given the weaker standing of the ansatz for qLDPC codes.

### 4.3 Latency and throughput (C3)

Inputs [1, 2]: on $[[130,4,6]]$, the effective cost per shot is of the order of a few ms on a single GPU, against a few tens of milliseconds for BP+OSD on a single CPU core, and BP+OSD's cost grows with physical error rate while the GNN's does not. Taking the stated qualitative ranges at face value, we instantiate "a few ms" as $t_G \in [2, 5]$ ms and "a few tens of ms" as $t_B \in [20, 50]$ ms. The speedup bounds are then:

$$s_{\min} = \frac{20}{5} = 4, \qquad s_{\max} = \frac{50}{2} = 25, \qquad s_{\mathrm{mid}} = \frac{35}{3.5} = 10.$$

Throughputs at the midpoints: $1/0.0035\ \mathrm{s} \approx 285.7$ shots/s/GPU versus $1/0.035\ \mathrm{s} \approx 28.6$ shots/s/core; matching one GPU would require ≈10 CPU cores, ignoring BP+OSD's error-rate-dependent slowdown, which makes the CPU-side figure optimistic at high error rates.

**Real-time projection (labeled).** For a neutral-atom-style cycle budget $T_{\mathrm{cycle}} = 10$ ms — a parameter choice of ours, not a measurement from [1, 2], though [1, 2] names neutral-atom processors as the real-time target — POLYMECHANON at 3 ms leaves a 7 ms margin (range 5–8 ms across the "few ms" ambiguity); BP+OSD at 30 ms exceeds the budget by 20 ms. The conclusion "candidate for real-time decoding" holds if $T_{\mathrm{cycle}} \geq 3$ ms and if GPU-to-control-system transfer adds negligible latency — a cost [1, 2] does not quantify.

### 4.4 Post-selection consistency (C5)

Inputs [1, 2]: confidence-based post-selection lowers the logical error rate by more than an order of magnitude on the surface code while keeping more than 90% of the shots. Let the retained fraction be $f \geq 0.9$, the post-selected rate $p_L' = p_L/10$ (the conservative boundary of "more than an order of magnitude"), and the discarded shots' rate $p_L^{\mathrm{disc}}$. Conservation of failures:

$$p_L = f \cdot p_L' + (1 - f) \cdot p_L^{\mathrm{disc}}.$$

With $f = 0.9$: $0.1 \cdot p_L^{\mathrm{disc}} = p_L - 0.09 \cdot p_L = 0.91 \cdot p_L$, hence

$$p_L^{\mathrm{disc}} = 9.1 \cdot p_L.$$

The discarded 10% must therefore carry failures at ≈9.1× the base rate — a strong separability requirement on the learned confidence. The condition is testable: if the discarded rate were only $2 \cdot p_L$, the arithmetic $(0.9 \times 0.1 + 0.1 \times 2) \cdot p_L = 0.29 \cdot p_L \neq p_L$ would contradict the claim.

**Throughput economics.** Acceptance $a = 0.9$ costs a discarded fraction $0.1/0.9 = 0.1111$, i.e. ≈11.1% of throughput, for a ≥10× error reduction; the accuracy-per-unit-throughput figure of merit improves by $r/a \geq 10/0.9 = 11.11$, i.e. ≥11.1×.

### 4.5 DEM graph sizing (structural derivation)

**Surface code, phenomenological noise.** The rotated surface code has $d^2 - 1$ stabilisers, $(d^2-1)/2$ per basis. With the common convention that the first measurement round yields no detectors, the detector count is $N_D = (d^2 - 1)(R - 1)$. At $d = 8$, $R = 8$: $d^2 - 1 = 63$; $R - 1 = 7$; $N_D = 63 \times 7 = 441$ detectors.

Mechanisms: the code has $n = d^2 = 64$ data qubits; under phenomenological noise each data qubit contributes two error types (X and Z), giving $128$ data-error mechanisms per round, each flipping 2 detectors; plus $63$ measurement-error mechanisms per round boundary, each flipping 1 detector. Over $R - 1 = 7$ boundaries:

$$N_M = (128 + 63) \times 7 = 191 \times 7 = 1337 \text{ mechanisms}.$$

Edges into $D$: $128 \times 7 \times 2 + 63 \times 7 \times 1 = 1792 + 441 = 2233$. Edges into $L$ (for $k = 1$, Z-type mechanisms only): $64 \times 7 = 448$. Totals:

$$N_{\mathrm{nodes}} = 441 + 1337 + 1 = 1779, \qquad N_{\mathrm{edges}} = 2233 + 448 = 2681.$$

All counts scale as $O(d^2 R)$ — confirming the density concern of [7]: the graph size is fixed by code and noise model, independent of the realized error rate, so a DEM-only decoder processes the full structure even when the syndrome is nearly empty.

**$[[130,4,6]]$ qLDPC (projection, assumptions stated).** Detectors per round: $n - k = 126$. We assume 4 mechanisms per qubit per round (a circuit-level-noise multiplier of ours, not a published figure), giving $4 \times 130 = 520$ mechanisms per round, ≈1,040 D-edges and ≈520 L-edges per round. At $R = 8$:

$$N_{\mathrm{nodes}} \approx 126 \times 8 + 520 \times 8 + 4 = 1008 + 4160 + 4 = 5172,$$
$$N_{\mathrm{edges}} \approx (1040 + 520) \times 8 = 1560 \times 8 = 12480.$$

This is ≈2.9× the nodes ($5172/1779 = 2.907$) and ≈4.7× the edges ($12480/2681 = 4.655$) of the $d = 8$ surface-code DEM. The mechanism multiplier could plausibly range 2–8, giving a node-count range ≈2,600–10,300.

### 4.6 Isomorphism-invariance bound

A code-agnostic decoder is a function $f(G)$ on attributed DEM graphs. If two DEMs are isomorphic as attributed graphs — identical up to relabeling, in the sense formalized in [11] — then $f(G_1) = f(G_2)$ for any architecture that consumes only graph structure and attributes. This is a representational ceiling: DEM-isomorphic codes cannot be distinguished by any DEM-only decoder, and structure beyond the DEM (for example gate-level scheduling) is unusable by construction. Conversely, distinct code families occupy distinct structural classes, forcing a single decoder to interpolate across classes rather than specialize within one.

A cheap rigorous certificate: the part-size vectors $(|D|, |M|, |L|)$ must coincide for isomorphic tripartite graphs. For the $d = 8$ surface-code DEM the vector is $(441, 1337, 1)$; for any $R$-round $[[130,4,6]]$ DEM under our assumed multiplier it is $(126R, 520R, 4)$. These cannot coincide for integer $R$: $126R = 441$ gives $R = 3.5$ and $520R = 1337$ gives $R = 2.571$, and no single integer satisfies both equations. The two DEMs are therefore provably non-isomorphic by part sizes alone — the weakest of the invariants in the layered hierarchy of [11], yet already sufficient here. This structural separation is consistent with the reported cross-family generalization gap of [1, 2].

### 4.7 Cross-code model accounting (C4)

Input [1, 2]: the single cross-code model outperforms uncorrelated MWPM on graph-like codes seen during training and stays within 10% of BP+OSD on the others. "Within 10%" means

$$\frac{p_L^{\mathrm{cross}}}{p_L^{\mathrm{BP+OSD}}} \leq 1.10.$$

Combined with C2's dedicated-model factor 0.84, the worst-case penalty of the cross-code model versus a dedicated model on $[[130,4,6]]$-class codes is

$$\frac{1.10}{0.84} = 1.3095 \approx 1.31.$$

This is a projection: [1, 2] does not state cross-code performance on $[[130,4,6]]$ specifically, so the honest bracket is $[1.0, 1.31]$, with the lower end corresponding to the cross