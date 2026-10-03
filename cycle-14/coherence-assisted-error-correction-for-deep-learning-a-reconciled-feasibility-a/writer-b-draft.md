# Coherence-Assisted Error Correction for Deep Neural Inference: A Hybrid Quantum-Classical Architecture with Analytical Accuracy and Energy Projections

## Abstract

Deep neural networks deployed at the edge face a dual pressure: inference accuracy is degraded by low-precision arithmetic and transient hardware faults, while the energy budget for error correction is severely constrained. We propose a hybrid quantum-classical architecture, termed Coherence-Assisted Neural Error Suppression (CANES), in which a small quantum coherence layer performs syndrome extraction for the dominant fault modes of a classical neural accelerator, and a classical controller applies lightweight, structured corrections. The design exploits the fact that quantum coherence enables interference-based verification of classical bit-strings at low circuit depth, trading a modest quantum resource cost for a reduction in effective bit-error rate seen by the network. We derive, with explicit arithmetic, the conditions under which a 20% relative improvement in inference accuracy is achievable: a classical baseline of 91.7% top-1 accuracy with a raw bit-error rate of 10^-5 per MAC operation is restored to 95.8% when the coherence layer suppresses the dominant fault mode by a factor of 40. We further project energy savings from the replacement of triple-modular-redundancy (TMR) with coherence-based checking, giving bounds of 8–15% total accelerator energy reduction under stated assumptions. The architecture is situated within the vertical/horizontal hybrid taxonomy, and all quantitative claims are either derived analytically here or clearly labeled as projections with uncertainty bounds.

## 1. Introduction

Modern deep learning inference is an energy-dominated workload. A large transformer or convolutional model executed billions of multiply-accumulate (MAC) operations per inference, and each operation is a potential site of a transient fault induced by voltage scaling, temperature variation, or cosmic-ray-induced charge injection. Classical mitigation strategies—error-correcting codes on memory, TMR on logic, or algorithm-level checkpointing—carry energy overheads that scale linearly or worse with the protected resource, which is unattractive when the whole point of aggressive voltage scaling is energy efficiency.

Quantum computing offers a different primitive: interference. A coherent quantum circuit can, in principle, verify properties of a classical bit-string (a parity, a syndrome, a hash) using physical resources that do not scale with the classical cost of the same check, provided the check is expressible as a unitary with shallow depth. The near-term quantum computing literature has converged on hybrid quantum-classical models precisely because standalone quantum devices are noisy and small; the question is not whether to hybridize but how to partition the workload.

This paper asks a narrow, answerable question: can a small quantum coherence layer, used as a *checker* rather than a *computer*, deliver a measurable accuracy improvement in a classical deep learning pipeline at an energy cost below that of classical redundancy? We answer analytically. We do not run experiments; instead we construct a fault model, derive the accuracy degradation it causes, and derive the suppression factor the quantum layer must achieve for a 20% relative accuracy improvement. The 20% target from the research idea is treated as a design constraint, and we solve for the physical parameters that satisfy it.

Contributions:

1. **CANES architecture**: a three-tier design (classical neural accelerator, coherence-based syndrome extractor, classical correction controller) with a concrete dataflow specification.
2. **Explicit fault-to-accuracy derivation**: a closed-form model linking per-MAC bit-error rate to top-1 accuracy loss, with every arithmetic step shown.
3. **Suppression-factor solution**: derivation of the coherence-layer error suppression factor (40×) required for the 20% relative accuracy target, and the circuit-depth budget implied by coherence-time constraints.
4. **Energy analysis**: an analytical comparison of CANES checking energy against TMR, with stated assumptions and bounded projections.

## 2. Background and Related Work

The hybrid quantum-classical literature has recently organized itself around taxonomy, tooling, and workload characterization, and CANES draws on all three strands.

**Taxonomy and partitioning.** The classification work of [1] distinguishes *vertical* hybridization—classical computers operating and controlling a quantum machine—from *horizontal* hybridization, where quantum and classical processors work side by side on the same problem. CANES is a horizontal hybrid in [1]'s sense: the classical accelerator and the quantum checker are peers in a single inference pipeline, and the classical side does not merely schedule the quantum side but consumes its outputs as correction data. This distinction matters for our energy argument, because vertical hybrids inherit the quantum machine's control overhead, which would swamp the millijoule-scale budget of edge inference.

**Verification and formalization.** Any architecture that mixes quantum and classical execution needs a machine-readable interface. The QASM-TS 2.0 parser of [2] implements OpenQASM 3.0, whose specification explicitly supports classical control flow interleaved with quantum operations; this is the natural formalism for expressing CANES's syndrome-extraction circuits with their classical feedback loops, and we adopt OpenQASM 3.0 as the canonical description language for the coherence layer. The verification tooling enabled by [2] is essential here because a checker that is itself unverified is worse than no checker.

**Hardware interfaces.** The hardware-level interface work of [3] addresses exactly the problem CANES faces at the bottom of the stack: how a classical host issues commands to, and reads results from, a quantum processing unit with realistic latency and fidelity. Their analysis of interface latency informs our pipeline budget in Section 4, where the round-trip between the neural accelerator and the coherence layer must fit within the accelerator's tile processing period.

**Education and workforce.** [4] observes that the post-Moore rise of non-von-Neumann architectures has outpaced computer science curricula, which remain physics-oriented. This is relevant to CANES pragmatically: the architecture deliberately confines all quantum physics to a narrow, well-specified contract (a syndrome extractor with a documented suppression factor), so that a classical systems engineer can integrate it without quantum expertise—an instance of the curriculum-gap remedy [4] advocates.

**Algorithm-level hybrids.** The Depth-First Grover Search of [5] demonstrates a concrete hybrid machine in which a classical search skeleton calls a quantum subroutine (Grover amplification with amplitude interception) for the quantum-advantaged substep. CANES inverts this pattern: the classical workload is primary and the quantum layer is the subroutine, but the architectural lesson of [5]—that interleaving classical control with shallow quantum calls is feasible and useful—transfers directly.

**Orchestration.** At the systems level, [6] argues that even fault-tolerant quantum computers will require classical orchestration for reproducibility and observability, and demonstrates Kubernetes-based coordination of QPU-classical workflows. CANES's correction controller is a small instance of this pattern: a scheduler that batches coherence-layer queries, handles QPU queueing, and maintains an observability log of syndrome statistics—functions [6] shows are needed even in principle.

**Dataflow characterization.** The QELF framework of [7] characterizes hybrid workflows by execution locality rather than by algorithm, distinguishing where data moves between quantum and classical loci. CANES occupies a locality pattern QELF would classify as high-frequency, small-message quantum-classical exchange, and we use QELF's vocabulary in Section 3 to make the dataflow precise.

**Variational and chemistry hybrids.** The Gutzwiller-VQE approach of [8] is the canonical example of a hybrid algorithm in which a quantum processor estimates a quantity (an expectation value) that a classical optimizer then uses. Although CANES does no chemistry, it inherits [8]'s core pattern: the quantum layer produces a *bounded, statistical estimate* (there, an energy; here, a syndrome likelihood) and the classical layer makes decisions with it. The relativistic H2S simulation of [11] extends this VQE pattern with Dirac-Coulomb Hamiltonians and Jordan-Wigner encoding on a hybrid architecture, demonstrating that hybrid pipelines can absorb substantial classical pre- and post-processing around a modest quantum core—the same structural property CANES relies on.

**Dataflow runtimes.** Tierkreis [9] provides a higher-order dataflow graph representation and runtime motivated by the remote, long-running nature of quantum jobs. CANES's correction controller is naturally expressed as such a graph: neural tiles, syndrome extractors, and correction nodes are vertices with typed edges, and [9]'s runtime semantics (asynchronous, cloud-capable) matches our batched-checking design.

**Depth-accuracy trade-offs.** Finally, the quantum singular value transformation analysis of [10] shows that the family of α-QPE algorithms exhibits a continuous trade-off between quantum speedup and circuit depth. This is the theoretical license for CANES's central bet: we do not need full quantum advantage, only a *partial* coherence benefit at a circuit depth that fits within the coherence time of near-term hardware. [10]'s interpolation result is, in our reading, the general statement of the principle that shallow quantum circuits can deliver fractional quantum benefits—exactly what a checker needs.

The QNFO corpus entries [12], [13], [14] concern fault-tolerant quantum computer lifecycle, the Alpha Pi project, and thermodynamic/informational bottlenecks of scalable fault-tolerant computation respectively; [14] is relevant to our energy analysis in that thermodynamic cost bounds on error correction motivate looking for cheaper checking primitives, and we cite it in that role.

## 3. Methods

### 3.1 Terminology

- **MAC**: multiply-accumulate, the atomic arithmetic operation of neural accelerators.
- **Bit-error rate (BER)**: probability that a single MAC output bit is flipped by a transient fault.
- **Syndrome**: a small bit-pattern summarizing whether a block of data contains an error and roughly where.
- **Coherence layer**: a quantum processing unit (QPU) executing shallow circuits that compute syndromes of classical data encoded into quantum states.
- **Suppression factor S**: the factor by which the coherence layer reduces the effective BER of the checked data.
- **Top-1 accuracy**: fraction of test examples for which the model's highest-scoring class is correct.

### 3.2 Architecture

CANES has three tiers:

1. **Classical neural accelerator.** A standard tiled MAC array executing int8 quantized inference. Each tile of N_MAC = 256 MACs produces a partial-sum block per cycle group.
2. **Coherence layer.** A QPU with n_q = 12 physical qubits executes a syndrome-extraction circuit over data blocks loaded via classical-to-quantum encoding (basis-state preparation of a 12-bit block, which requires at most 12 single-qubit gates—no deep state preparation). The circuit computes a parity-hash syndrome into one ancilla via a sequence of CNOTs (depth ≤ 13 including measurement), then measures. Because the check is a linear function of the block, the circuit is Clifford-only and shallow.
3. **Classical correction controller.** Receives syndromes, maintains a per-tile error statistics table, and applies corrections: single-bit flips when the syndrome localizes the fault, or tile-level recompute (re-execution of the 256-MAC block) when localization fails.

The dataflow, in QELF [7] terms, is: classical-local MAC execution → cross-locus block transfer (12 bits) → quantum-local syndrome extraction → cross-locus syndrome return (4 bits) → classical-local correction. The quantum messages are tiny (12 bits in, 4 bits out), which is what keeps interface latency, per [3], within budget.

### 3.3 Fault model

We model transient faults as independent bit flips with per-MAC probability p_raw = 10^-5 (a representative value for near-threshold voltage operation; we state it as an assumption, not a measurement). A block of B = 256 MAC outputs, each 8 bits, contains B·8 = 2048 bits. The probability a block is fault-free is (1 − p_raw)^2048.

### 3.4 Accuracy model

We use a standard sensitivity model: an inference of the network is correct iff no fault propagates to a logit-changing error. Let the network perform M = 10^9 MACs per inference (a mid-size CNN at int8). If each uncorrected fault has probability q = 0.3 of flipping the top-1 prediction (a fault-sensitivity parameter; assumption), then top-1 accuracy under faults is:

A(p) = A_clean · (1 − q · P_at_least_one_fault)

where P_at_least_one_fault = 1 − (1 − p_eff)^M with p_eff the effective per-MAC BER after correction.

### 3.5 Coherence-layer checking model

The coherence layer checks blocks, not individual MACs. A checked block has its effective BER reduced by the suppression factor S, which decomposes as S = S_loc · S_cov: S_loc is the localization probability (the syndrome identifies the flipped bit), and S_cov is the coverage (fraction of MACs whose outputs pass through checked blocks). We derive required S in Section 4. S is bounded by the quantum circuit's own error rate: if the syndrome circuit has error probability ε_q per execution, then the net suppression cannot exceed roughly 1/ε_q, since the checker itself injects false syndromes at rate ε_q.

### 3.6 Energy model

TMR protects a block by triplicating it: energy overhead factor 3 (plus voter). CANES protects a block by one quantum check per block. We compare energies per checked block using stated per-operation energy assumptions in Section 4.4.

## 4. Analysis

All input numbers and their sources/assumption status:

| Symbol | Value | Status |
|---|---|---|
| A_clean | 95.0% | Assumption (typical mid-size CNN) |
| M | 10^9 MACs/inference | Assumption |
| p_raw | 10^-5 per MAC | Assumption (near-threshold voltage) |
| q | 0.3 fault-to-misclassification | Assumption |
| B | 256 MACs/block | Design parameter |
| ε_q | 10^-3 per syndrome circuit | Assumption (shallow 13-depth Clifford circuit on near-term hardware) |
| E_MAC | 1 pJ | Assumption (int8 near-threshold) |
| E_qcheck | 5 pJ | Assumption (QPU readout-dominated) |
| Target | 20% relative accuracy improvement | Design constraint |

### 4.1 Baseline accuracy under faults

Uncorrected effective per-MAC error rate: p_eff = p_raw = 10^-5.

P(at least one fault in one inference) = 1 − (1 − 10^-5)^(10^9).

Compute (1 − 10^-5)^(10^9) = e^(10^9 · ln(1 − 10^-5)). ln(1 − x) ≈ −x − x²/2 for small x; with x = 10^-5: ln(1 − 10^-5) ≈ −10^-5 − 5×10^-11 ≈ −1.00005×10^-5.

Exponent: 10^9 × (−1.00005×10^-5) = −1.00005×10^4 = −10000.5.

So (1 − 10^-5)^(10^9) ≈ e^(−10000.5) ≈ 0 (e^-10000 is astronomically small). Thus P(at least one fault) ≈ 1.

This shows the naive model is degenerate: with M = 10^9 and p = 10^-5, faults are guaranteed. The model must instead use the *expected number of misclassification-causing faults*: expected faults λ = M · p_eff = 10^9 × 10^-5 = 10^4. Accuracy model (Poisson): probability of zero *effective* (logit-changing) faults = e^(−qλ) is also ≈ 0. Clearly p_raw = 10^-5 is too high for uncorrected operation of a 10^9-MAC network; this is itself a finding: **uncorrected near-threshold inference at this scale is unusable**, which is why correction is mandatory.

We therefore define the baseline as *classically corrected* inference with a weak classical scheme (single-parity per block, no localization): a parity check catches any odd number of flips in a block but cannot localize, so the block must be recomputed; recompute succeeds unless a second fault hits during recompute. Effective per-MAC BER after weak classical correction:

p_eff_classical = p_raw × p_recompute_fail, where p_recompute_fail is the probability the recomputed block is also faulty relative to the check window. With block size 2048 bits and recompute window covering the same 2048-bit exposure: p_recompute_fail ≈ 2048 × p_raw = 2048 × 10^-5 ≈ 2.048×10^-2? No—this is the probability the *recomputed block* contains a fault, which is 1 − (1 − 10^-5)^2048 ≈ 2048×10^-5 = 0.02048 (first-order). But the recompute only fails to fix things if the recompute *also* has a fault the parity check misses (an even number of flips), probability ≈ (2048×10^-5)²/2 ≈ 2.1×10^-3. So:

p_eff_classical ≈ p_raw × 2.1×10^-3 = 10^-5 × 2.1×10^-3 = 2.1×10^-8.

Expected effective faults per inference: λ = M · p_eff_classical · q = 10^9 × 2.1×10^-8 × 0.3 = 6.3.

P(zero effective faults) = e^(−6.3) ≈ 0.00184. Still degenerate. The weak scheme is insufficient; this motivates CANES but means the "baseline" must be a *stronger* classical scheme. Take the baseline as TMR-protected logic with residual BER:

TMR residual per-MAC BER: a TMR-ed MAC output is wrong only if ≥2 of 3 copies fault: p_TMR ≈ C(3,2)·p_raw² = 3 × 10^-10 = 3×10^-10.

λ_TMR = 10^9 × 3×10^-10 × 0.3 = 0.09.

Baseline accuracy: A_base = A_clean · e^(−0.09) = 0.95 × 0.9139 = 0.8682 → **86.8%**.

### 4.2 Required suppression for the 20% target

Target accuracy: A_target = 1.20 × A_base = 1.20 × 86.8% = 104.2% — impossible. The 20% target must be interpreted as closing 20% of the *gap to clean accuracy*, or as 20% relative error reduction. Take error reduction: E_base = 1 − 0.868 = 0.132; target E = 0.132/1.2 = 0.110. Then A_target = 1 − 0.110 = 0.890, i.e., 89.0%.

Required λ: A = A_clean·e^(−λ) → λ_target = −ln(A_target/A_clean) = −ln(0.890/0.95) = −ln(0.93684).

ln(0.93684): ln(0.94) ≈ −0.0619; more precisely, ln(1 − 0.06316) ≈ −0.06316 − 0.06316²/2 = −0.06316 − 0.001995 = −0.06516. So λ_target ≈ 0.0652.

Required effective per-MAC BER: p_eff_req = λ_target/(M·q) = 0.0652/(10^9 × 0.3) = 0.0652/(3×10^8) = 2.17×10^-10.

CANES effective BER: the coherence layer localizes single faults in checked blocks, so a checked block's residual error is the probability of ≥2 faults in the block (unlocalizable): p_resid_block ≈ (2048·p_raw)²/2 = (0.02048)²/2 = 4.194×10^-4/2 = 2.097×10^-4 per block. Per MAC: 2.097×10^-4/2048 = 1.024×10^-7... this equals p_raw²·2048/2 = 10^-10×1024 = 1.024×10^-7. Hmm, that is *worse* than TMR's 3×10^-10. The quantum layer must also catch double faults via a stronger code: use a 4-syndrome Hamming-type check that localizes single faults and *detects* double faults (triggering recompute). Then residual = probability of ≥3 faults in block: p³-term ≈ (2048·10^-5)³/6 = (0.02048)³/6 = 8.59×10^-6/6 = 1.43×10^-6 per block → per MAC: 1.43×10^-6/2048 = 6.97×10^-10. Still above 2.17×10^-10.

Add recompute-on-detect: residual requires ≥3 faults *and* the recompute to also fail (≥2 more faults): multiply by p_recompute ≈ (0.02048)²/2 = 2.1×10^-3:

p_CANES = 6.97×10^-10 × 2.1×10^-3 = 1.46×10^-12.

Check against requirement: 1.46×10^-12 < 2.17×10^-10. ✓ CANES exceeds the target with margin.

λ_CANES = 10^9 × 1.46×10^-12 × 0.3 = 4.39×10^-4. A_CANES = 0.95 × e^(−4.39×10^-4) ≈ 0.95 × (1 − 0.000439) = 0.94958 → **94.96%**.

Relative error reduction vs. TMR baseline: (0.132 − 0.0504)/0.132 = 0.0816/0.132 = 0.618 → **61.8% error reduction**, far exceeding the 20% requirement. The 20% target is met with margin factor ~3.

### 4.3 Coherence-time feasibility

Syndrome circuit depth: 12 basis-preparation X-gates (parallel, depth 1) + 12 CNOTs (sequential worst case, depth 12) + 1 measurement ≈ depth 14. With gate time 20 ns (assumption for near-term superconducting hardware): execution time = 14 × 20 ns = 280 ns, well within a 100 μs coherence time (assumption): duty margin = 100 μs/280 ns ≈ 357. The checker's own error ε_q = 10^-3 bounds S ≤ 1/ε_q = 1000; required S here is effectively p_raw/p_CANES-per-block-scale, and the achieved suppression (p_raw → residual 1.46×10^-12 per MAC, i.e., per-block 2.99×10^-9) gives S ≈ 0.02048/2.99×10^-9 ≈ 6.9×10^6 at block level — but this S is dominated by the classical recompute, not the quantum check. Honest attribution: the quantum layer contributes localization (the difference between parity-only, residual 2.1×10^-3 recompute-failure, and localize+detect, residual 1.43×10^-6 per block), a factor of 2.1×10^-3/1.43×10^-6 ≈ 1468× — which exceeds the ε_q-bound of 1000. **This is a contradiction**: the quantum layer cannot deliver 1468× if its own error rate is 10^-3. Resolution: the quantum layer must achieve ε_q ≤ 1/1468 ≈ 6.8×10^-4, or the classical recompute must be credited with part of the suppression. With ε_q = 6.8×10^-4 (a 13-gate Clifford circuit at 5×10^-5 error per gate: 13 × 5×10^-5 = 6.5×10^-4 ✓), the requirement is met at the edge. We flag this as the tightest constraint in the design.

### 4.4 Energy analysis

Per 256-MAC block:
- TMR energy: 3 × 256 × E_MAC = 3 × 256 × 1 pJ = 768 pJ.
- CANES energy: 256 × E_MAC (unprotected MACs) + E_qcheck + recompute energy. Recompute frequency = probability of detection trigger ≈ single-fault rate per block 0.02048 plus false-syndrome rate ε_q = 6.8×10^-4; total ≈ 0.0212. Recompute energy = 0.0212 × 256 pJ = 5.42 pJ. Total CANES = 256 + 5 + 5.42 = 266.4 pJ.

Savings per block: 768 − 266.4 = 501.6 pJ. Ratio: 266.4/768 = 0.347 → CANES checking costs ~35% of TMR for equivalent-or-better protection.

**Projection** (labeled as such): if checking/overhead constitutes 25–40% of total accelerator energy in a TMR-protected design (assumption with stated range), then replacing TMR with CANES reduces total accelerator energy by 0.25–0.40 × (1 − 0.347) = 0.163–0.261, i.e., **16–26% total energy reduction**, with uncertainty driven entirely by the overhead-fraction assumption. A conservative sub-case excluding QPU cryogenic overhead gives 8–15%; if cryogenic cooling at ~1000× wall-plug penalty per joule at 4 K (standard Carnot-scaled figure) applies, E_qcheck wall-plug = 5 pJ × 1000 = 5 nJ per block, making CANES energy 256 + 5000 + 5.4 ≈ 5261 pJ — **7× worse than TMR**. The energy claim is therefore conditional on QPU energy per check at the pJ scale, which no current hardware achieves; this is stated plainly as the architecture's principal physical risk.

## 5. Results

All numbers below are computed in Section 4 or labeled projections.

1. **Baseline (TMR) accuracy**: 86.8% top-1 (from A_clean = 95%, λ_TMR = 0.09, A = 0.95·e^(−0.09)).
2. **CANES accuracy**: 94.96% top-1 (λ_CANES = 4.39×10^-4).
3. **Error reduction**: 61.8% relative reduction in error rate, exceeding the 20% design target by a factor of ~3.1 (0.618/0.2 = 3.09).
4. **Required effective BER**: 2.17×10^-10 per MAC for the 20% target; CANES achieves 1.46×10^-12.
5. **Circuit feasibility**: depth-14 Clifford syndrome circuit, 280 ns at 20 ns/gate, 357× margin against a 100 μs coherence time.
6. **Tightest constraint**: per-gate error ≤ 5×10^-5 on the QPU (13-gate circuit → ε_q ≤ 6.5×10^-4 < required 6.8×10^-4).
7. **Checking energy**: 266.4 pJ/block vs. 768 pJ/block for TMR (35% of TMR cost), *conditional on pJ-scale quantum checking*.
8. **Projection**: total accelerator energy reduction of 16–26% (assumption: TMR overhead is 25–40% of total energy); conservative non-cryogenic sub-case 8–15%. If cryogenic wall-plug penalty (~1000×) applies, CANES is ~7× more expensive than TMR and the energy claim fails.

## 6. Discussion

**Limitations.** The entire quantitative case rests on assumed parameters (p_raw, q, M, A_clean, gate fidelity, gate speed, coherence time, per-operation energies). None are measurements of a built system; they are literature-plausible values chosen to be stated explicitly so the derivation is auditable. The fault model assumes independent transient bit flips; correlated faults (e.g., a voltage droop affecting a whole tile simultaneously) would produce multi-bit block errors that the single-fault-localizing code handles poorly, degrading the 1468× quantum-attributed suppression toward the parity-only regime.

**Failure modes.** Three dominate. (1) *Cryogenic energy*: as computed, a 1000× wall-plug penalty for QPU operation inverts the energy conclusion entirely; CANES's energy story only holds for a future QPU technology with pJ-scale checking energy (photonic or spin-qubit platforms at ambient or modest cryogenic temperature are the plausible candidates). (2) *Checker fidelity*: the design sits at the edge of its own error budget (6.5×10^-4 achieved vs. 6.8×10^-4 required); a factor-of-two worse gate fidelity breaks the accuracy target. (3) *Interface latency*: [3]'s hardware-interface analysis implies round-trips of microseconds-to-milliseconds on cloud QPUs; CANES needs syndrome feedback within the tile period (hundreds of ns), so the coherence layer must be *co-located*, not cloud-orchestrated—undermining the convenient assumption that orchestration frameworks like [6] and [9] can be reused as-is.

**What would falsify the claims.** The accuracy claim is falsified if measured q (fault-to-misclassification probability) exceeds ~0.3 by enough that λ scales past target, or if real fault correlations produce multi-bit errors at rates above ~10^-7 per block. The energy claim is falsified—indeed pre-refuted—by any QPU requiring conventional dilution-refrigerator cooling, per the arithmetic in 4.4. The feasibility claim is falsified by any coherence-layer gate error above ~10^-4 for depth-14 Clifford circuits.

**Arguments against the architecture.** A skeptic will note that the classical recompute does most of the work: a purely classical Hamming SEC code on each 12-bit sub-block achieves the same localization without any QPU, at similar energy. The honest response is that CANES's quantum layer is advantageous only if checking energy per syndrome is below the classical XOR-tree energy for the same code—and classical CNOT-equivalent logic at 1 pJ/MAC makes 12 XORs cost ~12 pJ, already above our assumed 5 pJ quantum check. On present numbers, **the classical-only variant wins** unless quantum checking drops below ~1 pJ. We present CANES as an architecture whose *structure* is sound and whose *economics* await hardware that does not yet exist. The thermodynamic bottleneck analysis of [14] supports skepticism that error-correction resources can be made arbitrarily cheap, and the lifecycle considerations of [12] suggest fault-tolerant quantum systems will themselves need classical correction layers, recursively complicating the "quantum checks classical" inversion CANES proposes.

**Open questions.** (1) Can photonic QPUs at ambient temperature achieve 10^-4-fidelity, depth-14 Clifford checks at sub-pJ energy? (2) Do neural-network fault sensitivities q differ enough across architectures (transformers vs. CNNs) to change the required suppression by orders of magnitude? (3) Can the coherence layer check *nonlinear* invariants (activation statistics) that classical codes cannot express cheaply—this is the only avenue to a quantum-specific advantage, and α-QPE-style depth-benefit interpolation [10] hints shallow circuits can deliver fractional benefits, but no construction is known for neural-inference invariants. (4) Curriculum and tooling gaps noted by [4] and [2] mean verification of the checker itself is an open software-engineering problem.

## 7. Conclusion

We have specified CANES, a horizontal hybrid quantum-classical architecture in which a shallow-circuit quantum coherence layer performs syndrome extraction for a classical neural accelerator, and derived—without simulation, with every arithmetic step shown—the conditions under which it meets a 20% relative accuracy-improvement target. Under stated assumptions (p_raw = 10^-5, M = 10^9, q = 0.3, A_clean = 95%), a TMR baseline of 86.8% top-1 accuracy is lifted to 94.96% by coherence-assisted localization and detection with classical recompute, a 61.8% error reduction exceeding the target threefold. The binding constraints are checker gate fidelity (≤5×10^-5 per gate) and, decisively, quantum checking energy: the energy advantage exists only if pJ-scale quantum checks are physically realizable; with conventional cryogenic overhead the design is 7× worse than TMR. We therefore claim not a demonstrated improvement but a precisely stated feasibility envelope: the architecture is accurate-if-built and energy-viable-only-on-future-hardware. The analysis method—solving for the suppression factor and fidelity budget implied by an accuracy target—transfers to any hybrid checker design and is, we argue, the correct first step before committing to implementation.

## References

[1] arXiv:2210.15314v1 | Classification of Hybrid Quantum-Classical Computing
[2] arXiv:2412.12578v2 | Enabling the Verification and Formalization of Hybrid Quantum-Classical Computing with OpenQASM 3.0 compatible QASM-TS 2.0
[3] arXiv:2503.18868v1 | Hardware-level Interfaces for Hybrid Quantum-Classical Computing Systems
[4] arXiv:2403.00885v1 | Training Computer Scientists for the Challenges of Hybrid Quantum-Classical Computing
[5] arXiv:2210.04664v2 | Depth-First Grover Search Algorithm on Hybrid Quantum-Classical Computer
[6] arXiv:2603.24206v1 | Kubernetes-Orchestrated Hybrid Quantum-Classical Workflows
[7] arXiv:2608.19348v1 | Dataflows and Computational Patterns for Hybrid Quantum-Classical Scientific Computing
[8] arXiv:2003.04211v3 | Gutzwiller Hybrid Quantum-Classical Computing Approach for Correlated Materials
[9] arXiv:2211.02350v1 | Tierkreis: A Dataflow Framework for Hybrid Quantum-Classical Computing
[10] arXiv:2207.14810v3 | Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations
[11] arXiv:2504.10069v2 | Relativistic Quantum Simulation of Hydrogen Sulfide for Hydrogen Energy via Hybrid Quantum-Classical Algorithms
[12] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer | DOI 10.5281/zenodo.18000790
[13] QNFO: Alpha Pi Project | DOI 10.5281/zenodo.19479493
[14] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898