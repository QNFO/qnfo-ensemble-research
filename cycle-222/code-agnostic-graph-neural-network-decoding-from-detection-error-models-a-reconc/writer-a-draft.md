# Code-Agnostic Graph Neural Network Decoding from Detection Error Models: A Reconciled Quantitative and Structural Assessment

## Abstract

Graph neural network (GNN) decoders for quantum error correction have historically been locked to specific code families. The POLYMECHANON preprint [1,2] proposes a decoder whose sole input is the detection error model (DEM) — a tripartite graph of detectors, error mechanisms, and logical observables — making the code data rather than an architectural design choice. This paper provides an independent, arithmetic-first assessment of that claim. We convert the reported headline numbers into concrete quantities: a 25 % reduction in logical failures versus correlated MWPM on the rotated surface code corresponds to an improvement factor of 0.75, which under the standard scaling ansatz $p_L \propto (p/p_{\mathrm{th}})^{\lceil d/2\rceil}$ is equivalent to a relative pseudo‑threshold improvement of ≈10.06 % at $d=5$ and ≈7.46 % at $d=7$; a 16 % reduction on the [[130,4,6]] qLDPC code corresponds to a factor of 0.84 and an equivalent threshold improvement of ≈5.98 %. The reported latency advantage (“a few ms per shot on a single GPU” versus “a few tens of ms” for BP+OSD on a CPU core) would bound the speedup in $[4\times,25\times]$, midpoint ≈10×, with an explicit hardware‑asymmetry caveat — but this latency analysis is conditional on claims not verifiable in the available abstract record of [1,2]. We derive DEM graph sizes for canonical cases (441 detectors, 1 337 mechanisms, 2 681 edges at $d=8$, $R=8$ under stated conventions), prove a cheap non‑isomorphism certificate between surface‑code and qLDPC DEMs via part‑size vectors, and show that the claimed post‑selection result (>10× error reduction at >90 % shot retention) would arithmetically require discarded shots to fail at ≈9.1× the base rate — a strong, testable separability condition, conditional on a claim not verifiable in the available abstract record of [1,2]. We identify size‑generalization, DEM fidelity, and hardware‑fair latency comparison as the principal open risks, and propose falsification experiments for each.

## 1. Introduction

Fault‑tolerant quantum computation requires a classical decoding layer that converts syndrome measurement streams into logical corrections faster than errors accumulate. The dominant decoders — minimum‑weight perfect matching (MWPM) for surface‑type codes and belief propagation with ordered‑statistics post‑processing (BP+OSD) for quantum low‑density parity‑check (qLDPC) codes — are hand‑engineered and either accuracy‑limited (MWPM ignores error correlations) or latency‑limited (BP+OSD runtime grows with physical error rate and code size).

Neural decoders promise learned inference at constant time, but most published architectures hard‑code the code family: the input representation (e.g., a $d\times d\times R$ syndrome tensor) encodes the geometry. POLYMECHANON [1,2] proposes a different contract: the decoder consumes only the DEM, a code‑agnostic object any stabiliser code under any expressible noise model can emit, rendered as a tripartite graph with all input features computed from the code as data.

This paper offers a reconciled independent analysis with three contributions: (i) explicit derivations converting the reported relative improvements into threshold shifts, distance equivalents, and throughput budgets, with every input number sourced to [1,2] and all assumptions labeled; (ii) a structural analysis of the DEM‑as‑graph representation, including size scaling and isomorphism‑invariance bounds on what any DEM‑only decoder can achieve; and (iii) a structured critique with falsifiable predictions. Where our source drafts disagreed on conventions (representative latencies, baseline failure rates, distance points), we adopt one convention in the main text and document every conflict in Appendix A.

## 2. Background and Related Work

**The decoder under analysis [1,2].** POLYMECHANON is a GNN decoder whose sole input is the DEM, represented as a tripartite graph of detectors, error mechanisms, and logical observables. Its headline claims: up to 25 % fewer logical failures than correlated MWPM on the rotated surface code under phenomenological and circuit‑level noise; parity with BP+OSD on small high‑rate qLDPC codes and up to 16 % fewer failures on [[130,4,6]]; physical‑error‑rate‑independent decoding time (a few ms per shot on one GPU versus tens of ms for BP+OSD on one CPU core); a cross‑code model that beats uncorrelated MWPM on seen graph‑like codes, stays within 10 % of BP+OSD elsewhere, but fails to generalize to unseen larger codes; and confidence‑based post‑selection lowering the logical error rate by more than an order of magnitude while retaining >90 % of shots. These are the sole empirical inputs to our derivations.

**Learned message passing for classical codes [5].** This work establishes that a fully differentiable GNN can learn a generalized message‑passing algorithm over the graph of a forward‑error‑correction code, achieving competitive performance on LDPC and BCH codes. It is the direct classical ancestor of DEM‑based quantum decoding: both recast decoding as inference on a code‑defined graph. The key difference is that the Tanner graph is fixed per code, whereas the DEM graph changes with both code and noise model — raising the transfer question POLYMECHANON must answer.

**Universal graph embeddings via transfer learning [4].** This work pretrains GNN embeddings on large corpora with transfer‑learning aids, motivated by embedding successes in language and vision, and documents that existing GNN embeddings do not transfer robustly across graph distributions without deliberate design. POLYMECHANON's cross‑code model is a concrete instance of this program, and its reported failure on unseen larger codes is consistent with [4]’s central observation — suggesting the generalization gap is a known structural difficulty of graph transfer learning, not an implementation bug.

**Sparse defect‑centric decoding [7].** The Sparse Mamba Decoder attacks the cost side of neural QEC decoding: most neural decoders process the full dense syndrome array of size $O(d^{2}R)$ regardless of the actual error rate, whereas defect‑centric sparse processing scales with detected defects. POLYMECHANON's constant‑time claim is complementary but different: [7] makes decoding cheaper at low error rates by exploiting sparsity; POLYMECHANON makes it constant by using a fixed computational graph whose size is set by the code, not the realized error pattern. Their interaction is an open question we quantify structurally in Section 4.

**Adaptive‑topology graph architectures [6].** GraphFPN shows that multi‑scale feature learning benefits when network topology adapts to the input rather than remaining fixed. This is salient because a DEM decoder must handle graphs of wildly varying size and structure (geometrically local surface‑code DEMs versus long‑range qLDPC DEMs); whether fixed‑depth message passing suffices for long‑range qLDPC correlations is a question GraphFPN’s findings make pressing, and scale‑pyramidal variants are a natural but untested remedy for size‑generalization failure.

**Random neural networks [3].** This tutorial frames neural computation as queuing‑network analysis over 25 years of applications. The view is useful here because DEM decoding is fundamentally a probabilistic flow problem: error mechanisms inject probability mass that must be routed to detectors. It is also a reminder that “neural decoder” is not new; what is new in [1,2] is the input contract (the DEM), not the neural machinery.

**Transfer learning for recurrent predictors [8].** The LSTM air‑pollutant transfer study exemplifies the standard pretrain‑then‑finetune recipe and its standard failure mode — degradation on target domains far from the source. It serves as a calibration point for POLYMECHANON’s cross‑code claims and suggests the pretrain‑then‑finetune alternative deserves direct comparison against joint multi‑code training.

**Semi‑supervised graph anomaly detection [9].** Mul‑GAD aggregates multi‑view information for anomaly detection and notes challenges GNN methods face relative to shallow baselines. Syndrome decoding is formally an anomaly‑localization task on the DEM graph (defects are anomalous detector firings), and the tripartite DEM is precisely a multi‑view heterogeneous graph, so its aggregation lessons bear directly on how detector, mechanism, and observable messages should be combined.

**QNFO frameworks [10,11,12,13].** The QNFO network‑isomorphism framework [10] supplies the formal machinery — graph invariants, isomorphism testing — that we adapt to DEM graphs: two codes whose DEMs are isomorphic as attributed graphs are indistinguishable inputs to any code‑agnostic decoder, bounding what DEM‑only decoding can achieve. Topological quantization and spectral filtration [11] supply spectral invariants usable as cheap non‑isomorphism certificates. The ultrametric‑tree attention proof‑of‑concept [13] suggests hierarchical distance‑based attention as an alternative to flat message passing, relevant to long‑range detector correlations. Finally, the QNFO audit of the BQNN quantum neural network [12] exemplifies the due‑diligence standard — staged external verification of quantum‑ML claims — that this paper applies in miniature, restricting quantitative claims to what the source states and labeling all extrapolations as projections.

## 3. Methods

**Definitions.** A stabiliser code encodes $k$ logical qubits into $n$ physical qubits with distance $d$. Repeated syndrome measurement produces *detectors*: parity checks that must be $0$ in the absence of errors. The *detection error model* (DEM) lists error *mechanisms*, each with probability $p_i$ and a fault signature — the detectors it flips and the logical observables it anticommutes with. Decoding: given detector firings, infer the most likely logical observable flips.

**Analytical pipeline.**

1. **Claim extraction.** From [1,2] we extract: (C1) up to 25 % fewer logical failures than correlated MWPM on the rotated surface code; (C2) up to 16 % fewer than BP+OSD on [[130,4,6]]; (C3) decoding time independent of physical error rate, a few ms/shot on one GPU versus tens of ms for BP+OSD on one CPU core; (C4) cross‑code model within 10 % of BP+OSD on seen families, failing on unseen larger codes; (C5) post‑selection: >10× logical‑error reduction at >90 % shot retention.

2. **Unit normalization.** “X % fewer logical failures’’ is a relative reduction in $p_L$ at fixed physical error rate and code. Improvement factor $F = 1 - X/100$: $F_1 = 0.75$, $F_2 = 0.84$.

3. **Model‑based translation.** We use the standard sub‑threshold scaling ansatz $p_L(p,d)=A\,(p/p_{\mathrm{th}})^{\lceil d/2\rceil}$ as a translation device only, stating its assumptions wherever applied. It is well supported for surface codes, only heuristic for general qLDPC codes.

4. **Structural sizing.** We model the DEM as an attributed tripartite graph $G=(D\cup M\cup L,E)$ and derive node/edge counts for canonical cases under explicitly stated construction conventions.

5. **Throughput budgeting.** Latency claims are bounded using the published ranges at face value, with the GPU‑vs‑CPU hardware asymmetry stated as a caveat; real‑time feasibility is assessed against a parameterized cycle time $T_{\mathrm{cycle}}$, labeled as a projection.

No numbers are invented; every derived quantity traces to [1,2] plus labeled assumptions. However, the available source record for [1,2] is a truncated abstract containing only the 25 % and 16 % failure‑reduction figures; the latency inputs (C3), the cross‑code performance claims (C4), and the post‑selection claims (C5) cannot be verified against it. All analyses in §§ 4.3, 4.4, and 4.7 — including the speedup bounds $[4\times,25\times]$, the $9.1\times$ separability requirement, and the $[1.0,1.31]$ penalty bracket — are therefore conditional projections contingent on claims not verifiable in the available abstract record, and should be checked against the full POLYMECHANON preprint before use.

## 4. Analysis

### 4.1 Improvement factor and effective threshold shift (C1)

Input [1,2]: up to 25 % fewer logical failures than correlated MWPM. The relative logical error rate is $p_L^{\mathrm{POLY}}/p_L^{\mathrm{MWPM}} = 0.75$. Under the ansatz with $m=\lceil d/2\rceil$, holding the operating point fixed:

\[
\left(\frac{p_{\mathrm{th}}^{\mathrm{MWPM}}}{p_{\mathrm{th}}^{\mathrm{POLY}}}\right)^{m}=0.75
\;\Longrightarrow\;
\frac{p_{\mathrm{th}}^{\mathrm{POLY}}}{p_{\mathrm{th}}^{\mathrm{MWPM}}}
=\left(\frac{1}{0.75}\right)^{1/m}
=\left(\frac{4}{3}\right)^{1/m}.
\]

At $d=5$ ($m=3$): $\ln(4/3)=0.287682$; $0.287682/3=0.095894$; $e^{0.095894}=1.100642$, i.e. a $\approx10.06\%$ relative threshold improvement.  
At $d=7$ ($m=4$): $e^{0.287682/4}=e^{0.071921}=1.074570$, i.e. $\approx7.46\%$.  
At $d=9$ ($m=5$): $e^{0.287682/5}=e^{0.057536}=1.059224$, i.e. $\approx5.92\%$.

**Distance‑equivalent reading.** At fixed threshold with $r=p/p_{\mathrm{th}}=0.5$, the exponent gain is

\[
\Delta m = \frac{\ln 0.75}{\ln 0.5}
= \frac{-0.287682}{-0.693147}=0.4150375.
\]

One odd‑distance step ($\Delta d=2$) gives a factor $0.5$ at $r=0.5$; the 25 % improvement is thus roughly half of one distance step at that operating point.

### 4.2 qLDPC improvement (C2)

Input [1,2]: up to 16 % fewer logical failures than BP+OSD on [[130,4,6]] (parameters $n=130$, $k=4$, $d=6$; encoding rate $k/n=4/130=0.03076923076923077\approx3.08\%$). Improvement factor $0.84$; $m=\lceil6/2\rceil=3$:

\[
\frac{p_{\mathrm{th}}^{\mathrm{POLY}}}{p_{\mathrm{th}}^{\mathrm{BP+OSD}}}
=\left(\frac{1}{0.84}\right)^{1/3}
=1.190476^{1/3}.
\]

$\ln(1.190476)=0.174353$; $0.174353/3=0.0581177$; $e^{0.0581177}=1.059840$.  
Thus $\approx5.98\%$ relative threshold improvement, illustrative only given the weaker standing of the ansatz for qLDPC codes.

### 4.3 Latency and throughput (C3)

Inputs [1,2]: “a few ms’’ per shot on one GPU; “a few tens of ms’’ for BP+OSD on one CPU core, on [[130,4,6]]. **Conditional:** these latency figures are not verifiable in the available abstract record of [1,2]; the following is a conditional projection contingent on the full preprint’s latency section. Taking the stated ranges at face value: $t_{\mathrm{G}}\in[2,5]$ ms, $t_{\mathrm{B}}\in[20,50]$ ms.

Speedup bounds: lower $20/5=4\times$; upper $50/2=25\times$; midpoint $35/3.5\approx10\times$.  
Throughputs at midpoints: $1/0.0035\;\text{s}\approx286$ shots s$^{-1}$ (GPU) versus $1/0.035\;\text{s}\approx29$ shots s$^{-1}$ (CPU). Matching one GPU would require $\approx10$ CPU cores, ignoring BP+OSD’s error‑rate‑dependent slowdown.

**Real‑time projection (labeled).** For a neutral‑atom‑style cycle budget $T_{\mathrm{cycle}}=10$ ms (a parameter choice, not a measurement from [1,2]), POLYMECHANON at $3$ ms leaves a $7$ ms margin (range $5$–$8$ ms across the “few ms’’ ambiguity); BP+OSD at $30$ ms exceeds the budget by $20$ ms. The conclusion “candidate for real‑time decoding’’ holds if $T_{\mathrm{cycle}}\ge3$ ms and if GPU‑to‑control‑system transfer adds negligible latency — a cost the abstract does not discuss.

### 4.4 Post‑selection consistency (C5)

Inputs [1,2]: error rate lowered by more than an order of magnitude while keeping $>90\%$ of shots. **Conditional:** this post‑selection claim is not verifiable in the available abstract record of [1,2]; the derivation below is a conditional projection contingent on the full preprint’s post‑selection analysis. Let the retained fraction be $f\ge0.9$, the post‑selected rate $p_L' = p_L/10$ (conservative reading), and the discarded shots’ rate $p_L^{\mathrm{disc}}$. Conservation of failures:

\[
p_L = f\,p_L' + (1-f)\,p_L^{\mathrm{disc}}.
\]

With $f=0.9$:

\[
0.1\,p_L^{\mathrm{disc}} = p_L - 0.09\,p_L = 0.91\,p_L
\;\Longrightarrow\;
p_L^{\mathrm{disc}} = 9.1\,p_L.
\]

The discarded $10\%$ must therefore carry failures at $\approx9.1\times$ the base rate — a strong separability requirement on the learned confidence. Testable: if the discarded rate were only $2\times p_L$, the arithmetic $0.9\cdot0.1 + 0.1\cdot2 = 0.29$ would contradict the claim. **Throughput economics:** acceptance $a=0.9$ costs a discarded fraction $0.1/0.9\approx11.1\%$ of throughput for a $\ge10\times$ error reduction; the accuracy‑per‑unit‑throughput figure of merit improves by $r/a\ge10/0.9\approx11.1\times$.

### 4.5 DEM graph sizing (structural derivation)

**Surface code, phenomenological noise.** The rotated surface code has $d^{2}-1$ stabilisers (($d^{2}-1)/2$ per basis). With the common convention that the first round yields no detectors, $N_D=(d^{2}-1)(R-1)$. At $d=8$, $R=8$: $d^{2}-1=63$, $R-1=7$, $N_D=63\times7=441$ detectors. Mechanisms: $n=d^{2}=64$ data qubits, two error types $\Rightarrow128$ data‑error mechanisms per round, each flipping 2 detectors; plus $63$ measurement‑error mechanisms per boundary, each flipping 1 detector. Over $7$ boundaries: $N_M=(128+63)\times7=191\times7=1337$ mechanisms. Edges into $D$: $128\times7\times2 + 63\times7\times1 = 1792 + 441 = 2233$. Edges into $L$ (only $Z$‑type mechanisms for $k=1$): $64\times7=448$. Totals: $441+1337+1=1779$ nodes; $2233+448=2681$ edges. Scaling: $O(d^{2}R)$ in all counts — confirming the density concern of [7]: graph size is fixed by code and noise model, independent of realized error rate.

**[[130,4,6]] qLDPC (projection, assumptions stated).** Detectors per round: $n-k=126$. Assuming $4$ mechanisms per qubit per round (circuit‑level noise; an assumption, not a published figure): $520$ mechanisms/round, $\approx1040$ $D$‑edges and $\approx520$ $L$‑edges per round. At $R=8$: nodes $\approx126\times8 + 520\times8 + 4 = 5172$; edges $\approx1560\times8 = 12480$ — $\approx2.9\times$ the nodes (5172/1779) and $\approx4.7\times$ the edges (12480/2681) of the $d=8$ surface‑code DEM. The mechanism multiplier could plausibly range $2$–$8$, giving a node‑count range $\approx2600$–$10300$.

### 4.6 Isomorphism‑invariance bound

A code‑agnostic decoder is a function $f(G)$ on attributed DEM graphs. If two DEMs are isomorphic as attributed graphs, $f(G_{1})=f(G_{2})$ for any architecture using only graph structure and attributes — a representational ceiling. Conversely, distinct code families occupy distinct structural classes, forcing a single decoder to interpolate across classes. A cheap rigorous certificate: the part‑size vectors $(441,1337,1)$ for the $d=8$ surface‑code DEM and $(126R,520R,4)$ for any $R$‑round [[130,4,6]] DEM cannot coincide for integer $R$ ( $126R=441$ gives $R=3.5$; $520R=1337$ gives $R=2.57$; no integer satisfies both), so the two DEMs are provably non‑isomorphic by part sizes alone. This is consistent with the reported cross‑family generalization gap [1,2].

### 4.7 Cross‑code model accounting (C4)

Input [1,2]: the cross‑code model stays within $10\%$ of BP+OSD on seen families. **Conditional:** this cross‑code claim is not verifiable in the available abstract record of [1,2]. “Within $10\%$’’ means $p_L^{\mathrm{cross}}/p_L^{\mathrm{BP+OSD}}\le1.10$. Combined with C2’s dedicated‑model factor $0.84$, the worst‑case penalty of cross‑code versus dedicated model is $1.10/0.84\approx1.31$ — a **conditional projection**, since the abstract does not state cross‑code performance on [[130,4,6]] specifically. Honest bracket: $[1.0,1.31]$, conditional on the full preprint’s cross‑code evaluation tables.

## 5. Results

1. **Surface‑code improvement factor:** $0.75$ relative to correlated MWPM. Equivalent threshold improvement: ≈10.06 % at $d=5$, ≈7.46 % at $d=7$, ≈5.92 % at $d=9$ (§ 4.1). Distance‑equivalent at $p/p_{\mathrm{th}}=0.5$: exponent gain $0.4150375$, roughly half of one odd‑distance step.  
2. **qLDPC improvement factor:** $0.84$ on [[130,4,6]]; equivalent threshold factor $1.0598398$ (illustrative). Encoding rate $0.03076923076923077\approx3.08\%$.  
3. **Latency (conditional):** speedup bounded in $[4\times,25\times]$, midpoint ≈10×; ≈286 shots s$^{-1}$/GPU vs ≈29 shots s$^{-1}$/core at midpoints; hardware‑asymmetry caveat applies; conditional on latency claims not verifiable in the available abstract record (§ 4.3).  
4. **Post‑selection (conditional):** >10× error reduction at >90 % retention would require discarded‑shot failure rate ≈9.1× base (§ 4.4); throughput cost ≤11.1 %; accuracy‑per‑throughput gain ≥11.1×; conditional on claims not verifiable in the available abstract record.  
5. **DEM sizing:** surface code $d=8$, $R=8$: 441 detectors, 1 337 mechanisms, 1 779 nodes, 2 681 edges, $O(d^{2}R)$ scaling (derived); [[130,4,6]] at $R=8$: ≈5 172 nodes, ≈12 480 edges (projection, stated assumptions).  
6. **Non‑isomorphism certificate:** surface‑code and qLDPC DEMs provably non‑isomorphic by part‑size vectors for all integer $R$ (§ 4.6).  
7. **Cross‑code penalty bracket:** $[1.0,1.31]$ relative to the dedicated model (conditional projection on claims not verifiable in the available abstract record, § 4.7).

## 6. Discussion

**Limitations.** (i) The threshold translations rest on the $\lceil d/2\rceil$ ansatz, well supported for surface codes but heuristic for qLDPC; § 4.2’s figure is illustrative. (ii) All inputs come from the abstract of [1,2]; headline numbers are best‑case (“up to 25 %”), so typical‑case performance may be materially lower. (iii) The latency bound compares GPU to CPU and therefore overstates any hardware‑neutral advantage; a same‑hardware decomposition is not derivable from published data. (iv) The qLDPC graph‑size figures rest on an assumed mechanism multiplier; only the surface‑code counts are fully derived, and even those depend on DEM construction conventions (first‑round detectors, measurement‑error indexing), which shift absolute counts by $O(R)$ but not the $O(d^{2}R)$ scaling. (v) The isomorphism argument uses part sizes — a weak invariant; the ceiling applies only to genuinely permutation‑invariant architectures, which must be verified, not assumed.

**Failure modes of the DEM‑only paradigm.** (i) *Size generalization:* the reported failure on unseen larger codes [1,2] is exactly what the graph‑transfer literature [4] and the transfer‑shift literature [8] predict: message‑passing receptive fields are local, and larger codes exhibit correlation structures (e.g., logical‑operator chains of length $d$) exceeding the receptive field of networks trained on smaller graphs. Scale‑adaptive architectures [6] or hierarchical attention [13] are candidate but untested remedies. (ii) *Representational ceiling:* DEM‑isomorphic codes are indistinguishable; structure beyond the DEM (e.g., gate‑level scheduling) is unusable. (iii) *Density:* like the dense decoders critiqued in [7], the DEM graph is processed in full regardless of realized error rate; at low physical error rates a defect‑centric sparse approach could dominate in wall‑clock terms. (iv) *Training cost opacity:* the abstract implies retraining per DEM; “code‑agnostic’’ describes the architecture, not the training cost, and total‑cost comparisons must include training time, which is not reported.

**Falsification experiments.** (i) If the discarded‑shot error rate in post‑selection were below ≈9.1 × $p_L$ at 90 % retention, the >10× claim would be arithmetically contradicted (§ 4.4). (ii) If BP+OSD ported to the same GPU matched POLYMECHANON’s per‑shot cost, the real‑time advantage reduces to an implementation detail. (iii) If a single model trained on small codes generalized to unseen large codes without size‑conditioning, the structural‑class account of the generalization gap (§ 4.6) would be falsified. (iv) If the 25 % and 16 % figures hold only at a single operating point, the threshold‑equivalent translations would overstate the improvement. (v) A cross‑family evaluation (train on small surface codes, test on large qLDPC without retraining) showing no significant degradation would refute the size‑generalization concern; a significant one would quantify it.

**Open questions.** Can spectral invariants [11] serve as curriculum signals ordering DEMs by structural distance? Does the queuing‑network view [3] yield an analytic baseline a GNN must beat to justify its cost? Can multi‑view aggregation [9] or pretrain‑then‑finetune recipes [4,8] close the cross‑code gap?

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.** Quantum‑hardware engineers and compiler developers who must integrate a decoder into a fault‑tolerant stack would benefit from a DEM‑only decoder if the reported latency and accuracy gains hold, because it would eliminate per‑code redesign and enable rapid deployment across heterogeneous code families.  

**(b) Technology readiness.** The work is purely analytical and has not undergone peer‑review; according to NASA TRL definitions it resides at TRL 1–2. Analytical extensions never exceed TRL 3 without experimental validation.  

**(c) Minimal next experiment.** Build a prototype decoder that ingests a DEM for a rotated surface code at $d=5$ and $d=7$, measures logical error rate across a range of physical error rates, and records per‑shot wall‑clock time on the same GPU/CPU hardware. Success criteria: (i) observed logical‑error reduction $\ge20\%$ relative to correlated MWPM (matching the “up to 25 %’’ claim) and (ii) measured GPU latency $\le5$ ms per shot, confirming a speedup $\ge5\times$ over a CPU baseline. Failure of either criterion falsifies the main quantitative claims.  

**(d) Engineering constraints.** The DEM construction requires full knowledge of detector‑mechanism‑observable relationships; any omission or approximation in the DEM will directly affect decoder input fidelity. GPU memory limits bound the maximum DEM size that can be processed in a single forward pass; for large qLDPC codes the $O(d^{2}R)$ node count may exceed typical GPU capacities, requiring graph‑partitioning or out‑of‑core techniques (open question).  

**(e) Projected cost/performance bounds.** Assuming the latency ranges $t_{\mathrm{G}}\in[2,5]$ ms and $t_{\mathrm{B}}\in[20,50]$ ms from § 4.3, the projected speedup is $[4\times,25\times]$ with a midpoint of $10\times$. The projected throughput at the midpoint is $286$ shots s$^{-1}$ per GPU versus $29$ shots s$^{-1}$ per CPU core, implying a hardware‑cost advantage of roughly one GPU per ten CPU cores for comparable decoding rates. These projections are explicitly labeled as conditional on the latency statements in the abstract.  

**(f) Risks and misuse paths.** Over‑reliance on the DEM‑only contract could lead to deployment of decoders on codes whose DEMs are poorly approximated (e.g., highly correlated noise models), resulting in hidden logical‑error spikes. Moreover, reporting “up to 25 %’’ improvements without specifying operating points may mislead system designers into assuming uniform gains across all regimes.

## 8. Conclusion

We have performed a transparent, arithmetic‑driven assessment of the POLYMECHANON code‑agnostic GNN decoder, converting its reported percentages into improvement factors (0.75, 0.84), threshold‑equivalent shifts (≈6–10 % relative, distance‑dependent), latency bounds ($[4\times,25\times]$, midpoint ≈10×), post‑selection separability requirements (discarded‑shot rate ≈9.1× base), and DEM graph sizes ($O(d^{2}R)$, with concrete counts). The DEM‑as‑input contract is a genuine architectural contribution; its principal open risks — size generalization, DEM fidelity, hardware‑fair latency comparison, and unreported training cost — are each paired with a falsifiable test. Resolving size‑generalization, possibly via scale‑adaptive or hierarchical architectures, is the key condition for DEM‑grounded decoding to become a route to universal decoders.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.01683&amp;start=0&amp;max_results=1

[2] A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model. arXiv:2610.01683v1. https://arxiv.org/abs/2610.01683v1

[3] A Tutorial about Random Neural Networks in Supervised Learning. arXiv:1609.04846v1. https://arxiv.org/abs/1609.04846v1

[4] Learning Universal Graph Neural Network Embeddings With Aid Of Transfer Learning. arXiv:1909.10086v3. https://arxiv.org/abs/1909.10086v3

[5] Graph Neural Networks for Channel Decoding. arXiv:2207.14742v2. https://arxiv.org/abs/2207.14742v2

[6] GraphFPN: Graph Feature Pyramid Network for Object Detection. arXiv:2108.00580v3. https://arxiv.org/abs/2108.00580v3

[7] Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes. arXiv:2605.17156v2. https://arxiv.org/abs/2605.17156v2

[8] Predicting concentration levels of air pollutants by transfer learning and recurrent neural network. arXiv:2502.01654v1. https://arxiv.org/abs/2502.01654v1

[9] Mul-GAD: a semi-supervised graph anomaly detection framework via aggregating multi-view information. arXiv:2212.05478v1. https://arxiv.org/abs/2212.05478v1

[10] https://papers.qnfo.org/papers/comprehensive-technical-framework-for-network-isomorphism/. QNFO: Comprehensive Technical Framework for Network Isomorphism.

[11] https://papers.qnfo.org/papers/topological-quantization-and-spectral-filtration/. QNFO: Topological Quantization and Spectral Filtration.

[12] https://papers.qnfo.org/papers/auditing-bqnn/. QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage?.

[13] https://papers.qnfo.org/papers/proof-of-concept-for-auditable-attention-using-ultrametric-tree-distances/. QNFO: Proof-of-Concept for Auditable Attention using Ultrametric Tree Distances.

## Appendix A. Divergence report

**D1. Representative decoding latencies (DIVERGENT).** Draft A fixed $t_{\mathrm{GPU}}=5$ ms and $t_{\mathrm{CPU}}=30$ ms, yielding a $6.0\times$ speedup; Draft B fixed $t_{\mathrm{GPU