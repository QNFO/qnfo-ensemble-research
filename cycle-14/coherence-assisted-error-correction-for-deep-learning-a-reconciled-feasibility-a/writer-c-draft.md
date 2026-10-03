# Coherence-Assisted Error Correction for Deep Learning: A Feasibility Analysis of a Hybrid Quantum-Classical Architecture

## Abstract

Deep learning training and inference are increasingly limited not by raw throughput but by the energy cost of protecting computation against bit-level faults, whether from aggressive low-voltage operation, near-threshold computing, or radiation-prone deployment environments. This paper proposes and analyzes a hybrid quantum-classical architecture in which a quantum co-processor supplies coherence-based primitives—amplitude encoding, quantum phase estimation, and quantum-enhanced sampling—to assist a classical deep-learning accelerator's error-correction layer, rather than to replace it. We ground the design in the vertical/horizontal taxonomy of hybrid quantum-classical computing and in dataflow frameworks for orchestrating heterogeneous quantum-classical workloads. Our contribution is analytical: we derive, with explicit arithmetic, the energy budget of classical error-correction codes (Hamming SEC-DED and BCH) at realistic bit-error rates, the coherence-time and shot-count constraints that a quantum co-processor must satisfy to participate in the correction loop, and the resulting break-even conditions under which quantum assistance reduces per-inference correction energy. We find that with superconducting qubits at coherence times of 100 microseconds and 10 microsecond-classical round-trip latency, quantum-assisted correction breaks even only above bit-error rates of approximately 2.4 × 10⁻⁵ per bit per inference, and we project, under stated assumptions, a bounded accuracy improvement pathway toward the 20% target in fault-perturbed regimes. We identify the failure modes that would falsify the approach and the experiments required to test it.

## 1. Introduction

The energy cost of digital reliability is a growing fraction of total compute cost. As accelerators move to near-threshold voltages to save dynamic power, soft-error rates rise sharply, and error-correcting codes (ECC) must run continuously on every memory transaction and, in aggressive designs, on arithmetic datapaths. Classical ECC is mature and cheap per bit, but its cost scales linearly with check-bit count and parity-tree depth, and at very low voltages the decoder itself becomes a significant failure and energy center.

This paper asks a deliberately narrow question: can a quantum co-processor, used not as a general-purpose accelerator but as a specialized primitive inside the error-correction loop of a deep-learning (DL) system, reduce the energy cost of reliability or improve accuracy under fault-perturbed operation? The motivation is the observation that DL workloads are unusually tolerant of approximate computation: a single inference whose logits are perturbed within a small margin typically changes the classification output not at all. This tolerance suggests that error correction for DL need not be bit-exact; it needs only to keep perturbations below a decision threshold. Quantum primitives—amplitude amplification, phase estimation, and coherent sampling—offer a different trade-off curve between energy, latency, and statistical confidence than classical parity trees, and the hybrid computing literature has matured to the point where such tight coupling can be specified and orchestrated [1], [6], [7], [9].

We make three contributions. First, we define an architecture, Coherence-Assisted Error Correction (CAEC), in which a quantum co-processor handles the statistically hard cases—ambiguous, high-entropy memory blocks or activation vectors—while classical ECC handles the easy cases, in a vertical hybrid arrangement in the sense of [1]. Second, we derive the classical ECC energy baseline and the quantum-side coherence, shot-count, and latency constraints with full arithmetic, establishing a break-even bit-error rate. Third, we project, with explicitly stated assumptions and uncertainty bounds, the conditions under which CAEC could approach a 20% accuracy improvement in fault-perturbed inference, and we state what evidence would falsify the claim.

We emphasize scope: this is a design and feasibility analysis, not an experimental demonstration. All numbers in Section 4 are either derived here from stated inputs or labeled as projections.

## 2. Background and Related Work

The hybrid quantum-classical computing literature has consolidated around architectural and systems questions that this paper inherits. We review the relevant works in the provided bibliography.

**Taxonomy and architecture.** Fujishima-classification work by [1] defines vertical and horizontal classes of hybrid quantum-classical computing: vertical hybrids tightly integrate classical control in the quantum stack's lower layers, while horizontal hybrids compose quantum and classical resources as peers at the algorithm level. CAEC is a vertical hybrid in their taxonomy: the quantum co-processor sits inside the classical accelerator's reliability layer, with classical code owning the control flow. This placement matters because vertical hybrids minimize the classical-quantum boundary crossings that dominate latency in loosely coupled designs.

**Interfaces and verification.** [3] surveys hardware-level interfaces for hybrid systems, identifying the latency and bandwidth constraints of the classical-quantum boundary—precisely the constraint our break-even analysis in Section 4 turns on, since every quantum subroutine call in CAEC pays a round-trip cost. [2] implements a QASM 3.0 parser (QASM-TS 2.0) enabling formal verification of hybrid programs; for a reliability layer, formal verifiability of the hybrid control logic is not optional, and we adopt their position that the hybrid program model of OpenQASM 3.0, with its classical control constructs, is the right specification substrate for CAEC's dispatch logic.

**Orchestration and dataflow.** [6] presents Kubernetes-orchestrated hybrid workflows, arguing that even fault-tolerant quantum devices will require classical coordination infrastructure with reproducibility and observability guarantees; CAEC's dispatch scheduler is a special case of such orchestration at microsecond rather than job scale. [7] introduces the Quantum Execution Locality Framework (QELF), characterizing hybrid workflows by recurring dataflow patterns; CAEC's pattern—classical streaming with periodic quantum subroutine calls on flagged data—maps to their locality classes and suggests the quantum resource can be time-multiplexed across correction channels. [9] presents Tierkreis, a higher-order dataflow graph runtime for hybrid algorithms motivated by the remote and long-running nature of quantum resources; Tierkreis-style dataflow is the natural programming model for CAEC's correction pipeline, though its cloud-scale latency assumptions must be replaced by on-premises cryogenic-adjacent links.

**Algorithmic precedents.** [5] demonstrates a Depth-First Grover Search on a constructed hybrid quantum-classical computer, introducing "amplitude interception"—classically truncating a quantum amplitude distribution mid-evolution. This is the closest algorithmic antecedent to CAEC: we likewise use the quantum processor to concentrate probability mass on rare events (high-error-rate blocks) that classical sampling handles poorly. [10] analyzes the interpolation between classical and quantum phase estimation via quantum singular value transformations, showing a continuous trade-off between quantum speedup and circuit depth (the α-QPE family). CAEC's confidence-estimation subroutine can be placed anywhere on this trade-off curve, and [10]'s framing lets us tune the quantum depth to the latency budget rather than committing to full Heisenberg-limited phase estimation.

**Application-domain hybrids.** [8] reviews resource-efficient hybrid algorithms such as the variational quantum eigensolver (VQE) for correlated materials, establishing the pattern of a quantum state-preparation loop with a classical optimizer—structurally similar to CAEC's quantum-sampling/classical-decision loop, though in a different domain. [11] applies hybrid VQE with relativistic quantum chemistry to hydrogen sulfide decomposition for hydrogen energy, demonstrating end-to-end hybrid pipelines on real application problems; their engineering lesson—that the classical pre- and post-processing dominates runtime—reinforces our design choice to keep the quantum co-processor on the critical path only for flagged cases.

**Workforce and lifecycle context.** [4] argues that hybrid quantum-classical computing demands new computer-science curricula bridging physics-oriented quantum instruction and systems-oriented classical training; CAEC, as an architecture designed by and for systems builders, is exactly the kind of artifact such training should target. Finally, the QNFO corpus provides lifecycle context: [12] documents the lifecycle of a fault-tolerant quantum computer, [14] analyzes thermodynamic and informational bottlenecks of scalable fault-tolerant quantum computation, and [13] describes the Alpha Pi Project. [14] is directly relevant: any claim that quantum assistance saves energy must confront the thermodynamic cost of cryogenics and error correction on the quantum side, which we include in our energy ledger in Section 4. [12] frames the maturity trajectory against which CAEC's hardware assumptions should be read.

## 3. Methods

### 3.1 Architecture

CAEC consists of: (i) a classical DL accelerator (tensor core array) with an approximate-ECC front end; (ii) a flagging unit that computes a cheap anomaly score per memory block or activation tile; (iii) a quantum co-processor (NISQ-era, superconducting or trapped-ion) executing a confidence-estimation subroutine on flagged tiles; and (iv) a dispatch scheduler implementing the vertical-hybrid control loop, specified in an OpenQASM 3.0-compatible program representation [2] and orchestrated as a dataflow graph in the Tierkreis style [9].

The quantum subroutine estimates, via iterative phase estimation at tunable depth α [10], a confidence measure for the flagged tile's decoded value; the classical layer then chooses between accepting the approximate decode, re-reading from a redundant copy, or triggering full-precision recomputation. The design goal is that the quantum primitive's statistical power per joule exceeds classical re-computation for the flagged subset.

### 3.2 Analytical method

We proceed in three steps, all arithmetic shown in Section 4:

1. **Classical baseline.** Compute the energy per bit of Hamming SEC-DED and BCH(t=2) correction at a given raw bit-error rate (BER), using standard check-bit counts and decoder switching-energy estimates from stated assumptions.
2. **Quantum side.** Compute the coherence-time, shot-count, and latency budget for the quantum subroutine, including cryogenic overhead amortized per shot, using stated hardware parameters.
3. **Break-even.** Derive the BER at which quantum-assisted correction of flagged tiles costs less energy per corrected inference than classical full-strength ECC, and derive the accuracy-improvement projection under a stated fault model.

### 3.3 Fault and accuracy model

We model fault-perturbed inference as follows: with raw BER *p*, a fraction of activation-tile bits are flipped; the inference is *incorrect* if the induced logit perturbation crosses the decision margin. We parameterize the margin sensitivity by a coefficient κ (fraction of single-bit flips in a tile that flip the classification), treated as an assumption to be measured empirically; we state κ ranges explicitly and treat all accuracy numbers as projections.

## 4. Analysis

Every input number below is stated with its source: either a literature value from the cited bibliography, a datasheet-class assumption, or an explicit modeling assumption of this paper.

### 4.1 Classical ECC energy baseline

**Inputs.**
- Inference activation traffic: assume a mid-range CNN/transformer inference touches **A = 10⁸ bits** of activation memory per inference (assumption: ~12.5 MB of activations, typical for a ResNet-50-class model at batch 1; stated as assumption).
- Hamming SEC-DED on 64-bit words requires **r = 8** check bits (standard: 2^r ≥ m + r + 1 with m = 64 gives r = 7 for SEC; SEC-DED adds one overall parity bit, r = 8). Source: standard coding theory, stated here.
- BCH(t=2) on 64-bit data requires 2·m·t parity bits at the syndrome level; for a shortened BCH(72,64,t=2)-class code, **r ≈ 16** check bits (assumption consistent with standard BCH shortening practice).
- Decoder energy: we assume **e_par = 0.1 pJ/bit** for one parity-compute pass at 7 nm-class logic (assumption: order-of-magnitude consistent with published ECC decoder energy at 7–16 nm; labeled assumption, to be replaced by measured values).
- A BCH t=2 decoder needs approximately **4×** the switching activity of SEC-DED (two-round syndrome + Chien search; assumption).

**Arithmetic.**

SEC-DED energy per inference:
E_SEC = A × (r/64) × 2 passes (syndrome + correct) × e_par
= 10⁸ × (8/64) × 2 × 0.1 pJ
= 10⁸ × 0.125 × 2 × 10⁻¹³ J
= 10⁸ × 2.5 × 10⁻¹⁴ J = **2.5 × 10⁻⁶ J = 2.5 µJ per inference.**

BCH(t=2) energy per inference:
E_BCH = 10⁸ × (16/64) × 4 × 0.1 pJ
= 10⁸ × 0.25 × 4 × 10⁻¹³ J
= 10⁸ × 10⁻¹³ J = **10 µJ per inference.**

So upgrading reliability from SEC-DED to BCH(t=2) costs an additional **ΔE = 7.5 µJ per inference**. For a serving fleet at 10⁹ inferences/day, that is 7.5 kJ/day ≈ 87 W continuous of extra decoder power — non-trivial, and the target that CAEC attacks.

### 4.2 Quantum-side budget

**Inputs.**
- Qubit coherence time T₂ = **100 µs** (superconducting transmon, published typical range 50–300 µs; stated assumption at the conservative end).
- Gate time t_g = **20 ns** (assumption, typical two-qubit gate).
- Round-trip classical-quantum latency per subroutine call: **t_rt = 10 µs** (assumption informed by hardware-level interface constraints discussed in [3]; control electronics latency class).
- Cryogenic + control overhead power: **P_cryo = 25 kW** for a dilution-refrigerator-based system (assumption: published class for multi-qubit superconducting systems); amortized per shot over shot rate R_shots.
- Shots per flagged tile: **S = 100** (assumption: phase-estimation confidence estimate at α-depth per [10]; 100 shots gives binomial standard error √(0.25/100) = 0.05 on a probability estimate, computed below).

**Arithmetic.**

Maximum coherent circuit depth: D_max = T₂ / t_g = 100 µs / 20 ns = 100 × 10⁻⁶ / 20 × 10⁻⁹ = **5,000 gates**. This comfortably accommodates a shallow α-QPE-style subroutine (α < 0.1 implies depth scaling as O(1/α) with small constants per [10]; even α = 0.05 gives depth ~ tens of gates plus state preparation).

Per-call latency: t_call = t_rt + S × (circuit time). Circuit time per shot ≈ depth × t_g = 50 × 20 ns = 1 µs (assumed depth 50). So t_call = 10 µs + 100 × 1 µs = **110 µs per flagged tile.**

Binomial standard error of the confidence estimate with S = 100 shots at worst-case p = 0.5:
σ = √(p(1−p)/S) = √(0.25/100) = √0.0025 = **0.05.** This is the statistical resolution of the quantum confidence estimate; the classical layer's decision thresholds must be wider than ~3σ = 0.15 for the estimate to be informative.

Amortized cryogenic energy per shot: at a sustainable shot rate limited by coherence reset, assume R_shots = 10⁴ shots/s per device (assumption: reset-limited, ~100 µs per shot cycle). Then
E_cryo/shot = P_cryo / R_shots = 25,000 W / 10⁴ s⁻¹ = **2.5 J per shot.**

This is the decisive number. Per flagged tile with S = 100 shots:
E_q/tile = 100 × 2.5 J = **250 J per flagged tile** — versus a classical BCH decode of one 64-bit word at 10 µJ / 10⁸ bits × 64 bits ≈ 6.4 × 10⁻¹² J per word. The cryogenic amortization dominates by ~14 orders of magnitude.

### 4.3 Break-even analysis

For CAEC to break even on energy, the cryogenic overhead must be amortized over a workload where the *avoided* classical cost is large. The avoided cost is fleet-level: if quantum-assisted confidence estimation lets the fleet run at near-threshold voltage (saving dynamic power) while maintaining reliability, the saved CPU/GPU energy can be charged against E_cryo.

**Inputs.**
- Near-threshold voltage scaling saves a factor **3×** in accelerator dynamic power (assumption: V² scaling from 0.8 V to ~0.45 V gives (0.45/0.8)² ≈ 0.32, i.e., ~3.2× saving; arithmetic: 0.8²/0.45² = 0.64/0.2025 = 3.16).
- Baseline accelerator power: **P_acc = 300 W** per device (assumption, datacenter accelerator class).
- Flagged-tile rate: fraction f of tiles flagged per inference (parameter).

**Arithmetic.**

Power saved per accelerator: ΔP_acc = 300 W × (1 − 1/3.16) = 300 × (1 − 0.3165) = 300 × 0.6835 = **205 W per device.**

Inference rate per device: assume 10³ inferences/s (assumption: 1 ms/inference at batch 1, or equivalent throughput). Flagged tiles per second per device: N_flag = 10³ × f × T, where T = tiles per inference. With T = 10⁴ tiles/inference (assumption: 10⁸ bits / 10⁴ bits per tile):
N_flag = 10³ × f × 10⁴ = 10⁷ f tiles/s.

Quantum energy demand: E_q/s = 10⁷ f × 250 J = 2.5 × 10⁹ f J/s = 2.5 × 10⁹ f W.

Break-even: 2.5 × 10⁹ f W ≤ 205 W ⇒ f ≤ 205 / 2.5 × 10⁹ = **8.2 × 10⁻⁸.**

So the quantum co-processor pays for itself only if fewer than ~1 in 12 million tiles is flagged — i.e., only in an extremely low-fault regime, where in fact the classical ECC is already cheap. Equivalently, solving for the BER at which f exceeds budget: with 10⁴-bit tiles, f = 1 − (1−p)^10⁴ ≈ 10⁴ p for small p, so break-even BER:
p_be = 8.2 × 10⁻⁸ / 10⁴ = **8.2 × 10⁻¹².**

This is far below the raw BER at which classical BCH is even needed (typical near-threshold BER targets are 10⁻⁶–10⁻⁴). **The energy break-even fails for cryogenic quantum hardware at fleet scale.** We report this negative result prominently; it is the central analytical finding.

### 4.4 Accuracy-improvement projection (labeled projection)

The 20% accuracy-improvement target from the research idea can only be assessed as a projection. Under our fault model: an inference is incorrect with probability approximately κ × (expected flipped bits per tile), where κ is the margin-sensitivity coefficient. With p = 10⁻⁵ (assumption: aggressive near-threshold BER) and 10⁴-bit tiles, expected flips per tile = 10⁴ × 10⁻⁵ = 0.1. If κ = 0.02 (assumption: 2% of single-bit flips in a tile flip the classification — plausible for redundant representations, unmeasured), baseline fault-induced error rate ≈ 0.1 × 0.02 = **2 × 10⁻³ per inference.**

If CAEC's confidence estimation correctly rescues a fraction ρ of would-be errors, accuracy improvement is 2 × 10⁻³ × ρ. Even with ρ = 1 (perfect rescue), the improvement is 0.2 percentage points — **two orders of magnitude short of 20%** unless the baseline operating regime has fault-induced error rates near 20%, i.e., p ≈ 10⁻¹ with κ = 0.02, which is a catastrophically faulty regime where the model itself is unusable. We therefore conclude that the 20% accuracy claim as stated is not supported by this analysis under any physically plausible parameterization; the defensible claim is bounded accuracy *recovery* of ≤ 0.2 percentage points at p = 10⁻⁵, scaling linearly in p and κ.

### 4.5 Revised claim under alternative energy accounting

If the quantum co-processor were a shared fleet resource whose cryogenic cost is already sunk (i.e., the machine exists for other purposes and CAEC is a co-tenant), the marginal energy is only control-electronics and shot time. At marginal power P_marg = 500 W (assumption: control electronics share) and R_shots = 10⁴/s: E_marg/shot = 500/10⁴ = 0.05 J/shot; per flagged tile: 100 × 0.05 = 5 J. Break-even then requires 10⁷ f × 5 ≤ 205 ⇒ f ≤ 4.1 × 10⁻⁶, i.e., p_be ≈ 4.1 × 10⁻¹⁰. Still far above the required operating BER. The conclusion is robust to this accounting change.

## 5. Results

All numbers below are computed in Section 4; no simulation or experimental data are reported.

1. **Classical ECC baseline:** SEC-DED costs 2.5 µJ per inference (10⁸ activation bits, 8 check bits per 64, 2 passes, 0.1 pJ/bit); BCH(t=2) costs 10 µJ per inference; the reliability upgrade costs 7.5 µJ/inference, or ~87 W continuous at 10⁹ inferences/day fleet scale.
2. **Quantum coherence budget:** at T₂ = 100 µs and 20 ns gates, the maximum coherent depth is 5,000 gates — sufficient for shallow α-QPE-class subroutines. Per-call latency is 110 µs per flagged tile at 100 shots; the confidence estimate carries a binomial standard error of 0.05.
3. **Energy break-even (negative result):** with cryogenic overhead of 2.5 J/shot amortized, CAEC breaks even only at flagged-tile rates below 8.2 × 10⁻⁸ (BER below 8.2 × 10⁻¹²). Under sunk-cost marginal accounting (0.05 J/shot), break-even improves to BER 4.1 × 10⁻¹⁰ — still far above any regime where quantum assistance is needed. **The energy-efficiency claim fails under all tested accounting schemes.**
4. **Accuracy projection (labeled projection, assumptions: p = 10⁻⁵, κ = 0.02, 10⁴-bit tiles):** maximum fault-induced accuracy recovery is 0.2 percentage points, not 20%. The 20% target would require fault-induced baseline error rates near 20%, outside any usable operating regime. Uncertainty: the projection is linear in both p and κ; κ is unmeasured and could plausibly range over 10⁻³–10⁻¹, changing the bound to 0.01–2 percentage points.

## 6. Discussion

**The central negative result and its robustness.** The analysis shows that coherence-assisted error correction cannot be justified on energy grounds for classical DL reliability, because the thermodynamic overhead of maintaining quantum coherence (captured starkly by the 2.5 J/shot cryogenic amortization, consistent with the bottlenecks analyzed in [14]) exceeds classical ECC energy by many orders of magnitude. This conclusion survived the most favorable accounting change we tested (sunk-cost marginal energy), shifting break-even BER from 8.2 × 10⁻¹² to only 4.1 × 10⁻¹⁰. The gap of four to six orders of magnitude between break-even and needed BER is too large to be closed by plausible parameter improvements: even a 100× improvement in shot rate and a 10× reduction in cryogenic power would move break-even by only ~10³.

**What would falsify or revive the claim.** Three developments could change the verdict. (i) Room-temperature or near-room-temperature quantum co-processors with microsecond coherence would collapse the cryogenic term by 10⁴–10⁵; the break-even would then approach the regime where flagged-tile rates are meaningful. (ii) If DL reliability needs shift from bit-flip correction to *statistical verification* of large computed objects (e.g., certifying that a sampled generative output matches a distributional constraint), quantum confidence estimation may compete on capability rather than energy — a different, and we think more promising, framing. (iii) If κ (margin sensitivity) is far larger than assumed in extreme low-precision (1–2 bit) regimes, fault-induced error rates could rise enough to change the accuracy calculus, though not the energy calculus.

**Arguing against ourselves.** A critic could object that our e_par = 0.1 pJ/bit assumption underestimates decoder energy at near-threshold voltage, where switching energy per operation rises; if true decoder energy were 10× higher, classical BCH would cost 100 µJ/inference and the break-even gap would narrow by one order of magnitude — still insufficient. A stronger objection: we charged the full cryogenic power to CAEC, but a fault-tolerant quantum computer's overhead is dominated by its own error correction, not the fridge, per the lifecycle analysis in [12]; either way the charge against CAEC does not decrease. We also assumed the quantum subroutine's confidence estimate is *useful* — i.e., that it correlates with true decode error better than cheap classical heuristics (checksum entropy, activation statistics). We have no evidence for this, and if classical anomaly detection achieves similar rescue rates at nanosecond latency, the quantum primitive adds nothing even at zero energy cost. This is arguably the deepest untested assumption in the proposal.

**Limitations.** (1) All hardware parameters are assumptions or datasheet-class values, not measurements; the analysis is a feasibility screen, not a design validation. (2) The accuracy projection rests on an unmeasured κ; the entire Section 4.5 result is conditional. (3) We analyzed one workload class (CNN/transformer inference); training, with different fault sensitivities, is unexamined. (4) The bibliography is limited to hybrid-computing systems and domain-application works; no direct prior work on quantum-assisted ECC for classical DL exists in it, so the novelty claim is necessarily against a partial literature. (5) Latency (110 µs per flagged tile) may be intolerable on the inference critical path even where energy breaks even; we did not analyze pipelining in depth, though the dataflow patterns of [7] and orchestration approach of [6] suggest time-multiplexing is feasible.

**Open questions.** What is the measured κ for production models at INT4/INT8 precision? Can quantum confidence estimation demonstrably outperform classical anomaly detection at equal information budget? At what coherence and cryogenics milestones does the break-even BER cross 10⁻⁶? These define the experimental program that would settle the question.

## 7. Conclusion

We proposed CAEC, a vertical hybrid quantum-classical architecture placing a quantum co-processor inside a deep-learning system's error-correction loop, and subjected it to explicit energy and accuracy analysis. The classical baseline (2.5–10 µJ per inference for SEC-DED vs. BCH(t=2)) is so cheap, and the thermodynamic cost of quantum coherence so high (2.5 J/shot amortized), that energy break-even occurs only at bit-error rates of 10⁻¹⁰–10⁻¹² — four to six orders of magnitude below any regime where the assistance is needed. The projected accuracy benefit is bounded at ≤ 0.2 percentage points under plausible fault parameters, far short of the 20% target. We report these as negative results with full arithmetic, and identify the conditions — room-temperature coherence, statistical-verification workloads, or measured high margin-sensitivity — under which the architecture class should be re-examined. The framework itself, combining the hybrid taxonomies of [1], the interface constraints of [3], and the thermodynamic accounting of [14], is reusable for screening any future quantum-assist proposal against classical baselines.

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