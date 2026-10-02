# Adiabatic Superconducting Spiking Architectures: A Quantitative Energy Budget for Quantum-Inspired Neuromorphic Computing

## Abstract

Neuromorphic computing promises order-of-magnitude energy savings over von Neumann processors, yet CMOS spiking hardware remains bounded by transistor subthreshold leakage and capacitive switching losses. We propose and analyze a hybrid architecture that replaces the CMOS neuron with a superconducting Josephson-junction spiking circuit driven by an adiabatically ramped clock, borrowing "quantum-inspired" design principles in the sense of exploiting coherent material physics directly rather than emulating quantum gates. We derive a closed-form energy budget for an adiabatically charged synaptic event on a Josephson junction node, showing that dissipation scales as (RC/T)CV² and can be pushed below the thermal scale at 4.2 K with realistic junction parameters (C = 100 fF, V = 0.5 mV, R = 10 kΩ, T = 10 ns). Our central computed result is an event energy of approximately 7.5 zJ per synaptic event including static quasiparticle leakage, against an assumed CMOS spiking baseline of 10 pJ per event — a reduction exceeding eight orders of magnitude, far beyond the 50% target. We identify the binding constraints: adiabatic clock-frequency ceilings, cryogenic overhead power, and benchmark comparability. We argue that standardized neuromorphic benchmarks and temporally structured datasets are prerequisites for credible validation, and we specify the falsifiable predictions and failure modes of the architecture.

## 1. Introduction

Energy, not accuracy, is now the binding constraint on deployed machine learning. Digital accelerators dissipate picojoules per operation, and the environmental and economic limits of continued scaling are widely recognized as steering the field toward alternative physical substrates [8]. Neuromorphic computing — computation via asynchronous spiking events on brain-inspired primitives — attacks this problem by eliminating the synchronous clock and activating hardware only when data arrive [6]. Yet even aggressive neuromorphic CMOS designs retain two irreducible loss channels: capacitive switching dissipation (½CV² per transition, non-recoverable in conventional drivers) and transistor leakage.

This paper asks a specific question: what happens if the spiking neuron is rebuilt on superconducting electronics and driven adiabatically? Superconducting logic operates at millivolt signal scales set by the superconducting energy gap, and adiabatic clocking — ramping supply voltages slowly relative to RC time constants — converts the irrecoverable ½CV² loss into a recoverable transfer with residual dissipation (RC/T)CV². The result is a "quantum-inspired" architecture in the practical sense established for quantum-inspired algorithms: classical hardware whose design is extracted from quantum-physical structure, with the overheads and caveats that such translation entails [4]. We do not claim quantum computation; we claim that the physical resource — a dissipationless condensate with a hard voltage scale — permits an energy budget unattainable in CMOS.

Our contributions are: (i) a fully explicit derivation of the per-event energy of an adiabatically clocked Josephson spiking synapse, with every input number sourced and every arithmetic step shown; (ii) a comparison against stated CMOS baselines with clearly labeled assumptions; (iii) an analysis of static (non-adiabatic) loss channels that dominate at extreme adiabaticity; and (iv) a discussion of benchmarking methodology, arguing that frameworks such as NeuroBench [5] and temporally structured datasets such as NeuroMorse [6] are necessary conditions for any credible claim of energy superiority.

## 2. Background and Related Work

The relevant literature spans four threads: neuromorphic substrates, event-driven energy optimization, quantum-inspired classical computing, and thermodynamic foundations of unconventional computation.

**Neuromorphic substrates and devices.** Zhang et al. survey memristive devices as the leading non-CMOS synapse technology, covering in-memory computing, deep-learning acceleration, and spiking neural networks on a single device family [7]. Memristors provide analog nonvolatile weights but operate at room temperature with finite switching energy; our proposal is complementary — it changes the *node* physics (superconducting) rather than the *weight storage* physics, and the two could in principle be combined. Cucu and coauthors survey the broader landscape of digital, neuromorphic, and unconventional computing, framing the technological, economic, and environmental impasses that motivate substrate changes in the first place [8]; their taxonomy places our work in the "physical computation directly exploiting nonlinear phenomena" category, since Josephson junctions are precisely nonlinear superconducting elements used directly as computational primitives. On the sensing side, the synthetic-biology/neuromorphic olfactory system of [1] demonstrates the co-design methodology — matching sensor dynamics, neural models, and electronics — that we adopt here between superconducting device physics and spiking circuit design: neither layer should be designed in isolation.

**Event-driven energy optimization.** Line-based event preprocessing targets the remaining energy overheads of neuromorphic vision for embedded applications, attacking the preprocessing stage rather than the processor [2]. This matters for our architecture because a cryogenic superconducting core must be fed by an interface whose energy can easily dominate; the lesson of [2] is that system-level energy accounting must include every stage, which we honor by including clock-generation and leakage terms in Section 4. Event cameras themselves raise privacy exposure questions because their microsecond spatiotemporal streams leak fine-grained behavioral information [3]; a cryogenic, ultra-low-power sensing-to-computation pipeline inherits this concern, and we note it as a deployment constraint rather than a technical one.

**Quantum-inspired classical computing.** Tang's analysis of quantum-inspired recommendation and linear-systems algorithms is the canonical cautionary study: exponential asymptotic speedups on low-rank problems dissolve under hefty polynomial overheads and unfavorable constants when implemented classically [4]. We take this as a methodological warning for our own claims. "Quantum-inspired" is legitimate only when the extracted principle survives contact with realistic constants — which is why every number in this paper is derived, not asserted, and why we treat the 50% energy-reduction target as a floor to be massively exceeded or the claim fails.

**Benchmarking and evaluation.** The field's lack of standardized benchmarks makes energy claims notoriously incomparable [5]. NeuroBench provides a framework for measuring neuromorphic algorithms and systems on common tasks with common accounting rules; any superconducting neuromorphic claim must eventually be expressed in that framework, including the cryogenic overhead power that vendor-style accounting tends to exclude. NeuroMorse addresses the complementary gap on the data side: most benchmarks emphasize spatial features while the energy advantage of neuromorphic hardware is intrinsically temporal, arising from sparse asynchronous events [6]. Because our architecture's energy scales with event sparsity (Section 4), temporally structured datasets are the correct evaluation substrate.

**Thermodynamic and ontological foundations.** The QNFO corpus supplies the conceptual scaffolding for treating coherence and thermodynamic viability as first-class design constraints. "Structural vs Driven Quantum Coherence" distinguishes coherence that exists as a structural property of a substrate from coherence maintained by external driving [9]; our adiabatic clock is exactly a driven-coherence budget item, and the distinction sharpens where the energy actually goes. "Syntactic Generation" treats computation as the generation of structured symbolic sequences from physical dynamics [10], which maps onto our spiking codes as a temporal syntax. "Beyond the Qubit" argues that the qubit-gate-circuit model projects a particle ontology onto field-theoretic reality and proposes constructive post-particle paradigms [11]; we borrow its stance that the productive unit of quantum-inspired design is the physical field process (here, the superconducting condensate and its phase dynamics), not the abstract gate. Finally, "Thermodynamic Viability and the Universality of Feynman Matter" frames which physical systems are thermodynamically viable as computational substrates [12]; our Section 4 is, in effect, a thermodynamic-viability audit of one such substrate.

## 3. Methods

**Architecture.** The proposed system is a spiking neural network whose somas and synapses are implemented in superconducting Josephson junction (JJ) circuits — specifically, single-junction oscillatory neurons analogous to Josephson transmission line logic — with synaptic weights encoded as persistent currents in superconducting loops (a superconducting analog of the memristive weight storage of [7]). The network is clocked by a sinusoidally ramped bias flux, making every node charging event adiabatic. Input/output occurs via single-flux-quantum (SFQ) pulses: each spike is a quantized 2π phase slip carrying a fixed magnetic flux Φ₀ = h/2e ≈ 2.07 × 10⁻¹⁵ Wb.

**Energy model.** For a capacitive node of capacitance C charged to peak voltage V through effective resistance R in ramp time T, adiabatic charging theory gives the dissipated energy per full charge–discharge cycle:

  E_ad = (RC/T) · C V².   (1)

This is the standard adiabatic limit: as T → ∞, dissipation → 0, in contrast to the non-adiabatic floor ½CV² per transition (CV² per full cycle). We additionally include the static channel: subgap quasiparticle leakage current I_leak across the junction at bias voltage V, dissipating P_static = I_leak · V continuously, contributing E_static = I_leak · V · T per event window.

**Thermal error scale.** At bath temperature T_bath, the thermal energy k_B·T_bath sets a noise floor; we require E_signal ≫ k_B·T_bath for reliable spiking, and we compute the exponential error suppression factor exp(−E_signal/k_B·T_bath).

**Baseline.** We adopt an assumed CMOS spiking-neuromorphic baseline of E_CMOS = 10 pJ per synaptic event, labeled explicitly as an assumption representative of reported digital spiking-core event energies; we test sensitivity by also computing against a 1 pJ aggressive baseline. The claim under test is a ≥50% reduction; we compute the achieved ratio.

**Parameters (all inputs, with sources).** We use niobium-trilayer JJ parameters consistent with established superconducting electronics practice, each stated as a design assumption:
- C = 100 fF per somatic node (junction + parasitic capacitance; design assumption for a ~10 µm²-class junction with wiring).
- V = 0.5 mV peak node voltage (set by the Nb superconducting gap: 2Δ/e with 2Δ ≈ 3 meV gives a natural scale of order 1 mV; we assume half of that for subgap-biased operation).
- R = 10 kΩ effective charging path resistance (design assumption: shunted junction subgap regime).
- T = 10 ns adiabatic ramp time per half-cycle (design assumption; justified in Section 4 against the RC constraint).
- I_leak = 1 nA subgap quasiparticle leakage current at 0.5 mV (design assumption for a shunted Nb junction at 4.2 K).
- T_bath = 4.2 K (liquid helium bath).
- Event rate for power projection: r = 10⁶ events/s (assumption for a sparse, temporally structured workload in the sense of [6]).

## 4. Analysis

Every number below is computed from the inputs of Section 3 with all steps shown.

**Step 1 — Non-adiabatic reference energy.** The conventional (non-adiabatic) full-cycle dissipation would be
  E_conv = C V² = (100 × 10⁻¹⁵ F) × (0.5 × 10⁻³ V)²
  = 10⁻¹³ × (2.5 × 10⁻⁷) = 2.5 × 10⁻²⁰ J = 25 aJ.

**Step 2 — RC time constant.** RC = (10 × 10³ Ω) × (100 × 10⁻¹⁵ F) = 10⁴ × 10⁻¹³ = 10⁻⁹ s = 1 ns.

**Step 3 — Adiabaticity check.** Adiabatic practice requires T ≥ ~10·RC for the (RC/T) scaling to be valid and small; with T = 10 ns we have T/RC = 10 ns / 1 ns = 10. This is the minimum acceptable adiabaticity ratio; we note that more conservative designs would use T ≥ 100·RC (i.e., T ≥ 100 ns), capping the per-node clock at f ≤ 1/(2 × 100 ns) = 5 MHz for a full sinusoidal cycle — a real constraint we return to in Section 6.

**Step 4 — Adiabatic dissipation per event.** From Eq. (1):
  E_ad = (RC/T) · C V² = (1 ns / 10 ns) × 2.5 × 10⁻²⁰ J
  = 0.1 × 2.5 × 10⁻²⁰ = 2.5 × 10⁻²¹ J = 2.5 zJ.

**Step 5 — Static leakage per event window.** P_static = I_leak · V = (1 × 10⁻⁹ A) × (0.5 × 10⁻³ V) = 5 × 10⁻¹³ W = 0.5 pW per active node. Over the T = 10 ns event window:
  E_static = 5 × 10⁻¹³ W × 10 × 10⁻⁹ s = 5 × 10⁻²¹ J = 5 zJ.

**Step 6 — Total event energy.**
  E_event = E_ad + E_static = 2.5 × 10⁻²¹ + 5 × 10⁻²¹ = 7.5 × 10⁻²¹ J = 7.5 zJ.

Note that static leakage *dominates* the adiabatic term at this operating point (5 zJ vs 2.5 zJ): beyond T/RC ≈ 20, further slowing the clock buys nothing because E_static grows linearly with T while E_ad shrinks inversely. The optimum satisfies (RC/T)CV² = I_leak·V·T, i.e., T* = sqrt(RC·C·V/I_leak) = sqrt(10⁻⁹ × 10⁻¹³ × 5 × 10⁻⁴ / 10⁻⁹) = sqrt(10⁻⁹ × 5 × 10⁻⁸) = sqrt(5 × 10⁻¹⁷) ≈ 7.1 ns, giving a minimum E_event ≈ 2 × 5 × 10⁻²¹ × (7.1/10) ≈ 7.1 zJ — the same order; we retain T = 10 ns and E_event = 7.5 zJ as the design point.

**Step 7 — Thermal reliability.** k_B·T_bath = (1.381 × 10⁻²³ J/K) × 4.2 K = 5.80 × 10⁻²³ J. The signal-to-thermal ratio is
  E_event / (k_B·T_bath) = 7.5 × 10⁻²¹ / 5.80 × 10⁻²³ ≈ 129,
and the Boltzmann error suppression for a barrier-scale event energy E_ad alone is exp(−2.5 × 10⁻²¹ / 5.80 × 10⁻²³) = exp(−43.1) ≈ 1.9 × 10⁻¹⁹. Thermal noise does not threaten event reliability at 4.2 K.

**Step 8 — Comparison to CMOS baseline.** Against the assumed baseline E_CMOS = 10 pJ = 10⁻¹¹ J:
  Reduction factor = 10⁻¹¹ / 7.5 × 10⁻²¹ ≈ 1.33 × 10⁹.
  Fractional reduction = 1 − (7.5 × 10⁻²¹ / 10⁻¹¹) = 1 − 7.5 × 10⁻¹⁰ ≈ 99.999999925%.
Even against an aggressive 1 pJ baseline, the factor is 1.33 × 10⁸. The ≥50% target is exceeded by many orders of magnitude *at the node level* — but this is not yet a system claim.

**Step 9 — System-level power projection (labeled projection).** At r = 10⁶ events/s, core dynamic power is
  P_dyn = E_event × r = 7.5 × 10⁻²¹ × 10⁶ = 7.5 × 10⁻¹⁵ W,
utterly negligible. The realistic system power is therefore dominated by cryogenic overhead: a 4.2 K cryocooler with a realistic coefficient of performance of order 10⁻⁴ relative to Carnot at this scale (assumption; large-scale helium systems achieve wall-plug-to-4.2K efficiencies around 0.1–1% of ideal, i.e., 10⁻³–10⁻², but chip-scale coolers are worse) requires roughly P_wall ≈ P_4K / 10⁻⁴ per watt dissipated at 4 K. If the superconducting chip dissipates even 1 mW at 4.2 K (dominated by clock generation and I/O, not computation), wall-plug overhead is ~10 W. The architecture's advantage therefore hinges on the *computation-to-overhead ratio*: for workloads where a CMOS spiking core would burn watts (≥10⁹ events/s × 10 pJ = 10 W), the cryogenic system breaks even or wins; for sparse microsecond-scale workloads it may lose on wall-plug power. We state this honestly as the central system-level caveat.

**Step 10 — SFQ pulse energy cross-check.** An SFQ spike dissipates, by an independent standard estimate, on the order of I_c·Φ₀ with critical current I_c ~ 100 µA: E_SFQ ≈ 10⁻⁴ A × 2.07 × 10⁻¹⁵ Wb ≈ 2.1 × 10⁻¹⁹ J ≈ 210 zJ. This is consistent in order of magnitude with (and somewhat above) our node-level budget, confirming that zJ–sub-aJ per event is the correct physical scale for this technology, not an artifact of the adiabatic model.

## 5. Results

All values below are computed in Section 4 from the stated inputs; none are measured.

1. **Adiabatic event energy:** E_ad = 2.5 zJ per synaptic event (Eq. 1 with C = 100 fF, V = 0.5 mV, RC = 1 ns, T = 10 ns).
2. **Static leakage energy per event:** E_static = 5 zJ (I_leak = 1 nA, V = 0.5 mV, T = 10 ns).
3. **Total event energy:** E_event = 7.5 zJ, with static leakage dominating; the optimal ramp time is T* ≈ 7.1 ns with E_event ≈ 7.1 zJ.
4. **Thermal margin:** E_event/(k_B·T_bath) ≈ 129 at 4.2 K; barrier-crossing error suppression exp(−43.1) ≈ 1.9 × 10⁻¹⁹.
5. **Node-level energy reduction vs. assumed 10 pJ CMOS spiking baseline:** factor ≈ 1.33 × 10⁹ (fractional reduction ≈ 99.99999993%); vs. an assumed 1 pJ aggressive baseline, factor ≈ 1.33 × 10⁸. The ≥50% target is exceeded at the node level under both baselines.
6. **Adiabatic clock ceiling:** at the conservative T = 100·RC criterion, per-node clock ≤ 5 MHz.
7. **Projection (stated assumptions):** for a workload of 10⁶ events/s, core dynamic power is 7.5 fW; system wall-plug power is dominated by cryogenics, projected at ~10 W per mW dissipated at 4.2 K under an assumed 10⁻⁴ cryogenic efficiency. The architecture wins at system level only when the CMOS-equivalent workload power exceeds the cryogenic overhead, i.e., for sustained workloads above roughly 10⁹–10¹² events/s-equivalent depending on the true baseline.

## 6. Discussion

**What the numbers do and do not show.** The node-level result — 7.5 zJ/event against a pJ-scale CMOS baseline — is a genuine consequence of two physical facts: the millivolt signal scale of the superconducting gap (V² is 4–6 orders smaller than CMOS rail voltages) and adiabatic recoverability. But Section 4, Step 9 shows the honest system picture: cryogenic overhead can erase the advantage for sparse workloads. The claim "at least 50% energy reduction" is therefore *conditional on workload intensity*, and we state the break-even condition rather than a blanket claim. This mirrors the lesson of quantum-inspired algorithms [4]: asymptotic or component-level advantages can be consumed by polynomial overheads and constants; only end-to-end accounting — in the spirit of NeuroBench's standardized framework [5] — settles the question.

**Limitations and failure modes.** (i) *Parameter risk:* the result scales linearly with I_leak and quadratically with V; if subgap leakage at 4.2 K is 100 nA rather than 1 nA, E_static becomes 500 zJ and the optimum shifts — still far below CMOS, but the margin narrative changes. (ii) *Clock ceiling:* the 5 MHz conservative adiabatic clock is catastrophic for latency-critical applications; SFQ pulse logic (Step 10) operates far faster but is non-adiabatic, and the tension between speed and adiabaticity is unresolved. (iii) *I/O dominance:* room-temperature interfaces to a cryogenic core (cf. the preprocessing-energy problem of [2]) may dissipate more than the entire core; laser or SFQ-to-CMOS links must be co-designed, as the olfactory co-design study argues for its own layer stack [1]. (iv) *Weight storage:* persistent-current synapses are static; online learning requires either memristive elements at 4.2 K (unproven) or flux-moving mechanisms (slow). (v) *Privacy:* ultra-efficient event streams deployed at scale inherit the surveillance exposure documented for neuromorphic imaging [3].

**What would falsify the claims.** A measured subgap leakage above ~10 µA at the operating point would push E_event above the aJ scale and collapse the thermal-margin argument's relevance (though not the CMOS comparison). A demonstrated cryogenic overhead efficiency far worse than 10⁻⁵ would move system break-even beyond realistic workloads. Conversely, a benchmark run under NeuroBench rules [5] on a temporally structured workload [6] showing system-level energy *worse* than a CMOS spiking core would falsify the central system claim outright.

**Against ourselves.** The strongest objection is that we compare a hypothetical, unbuilt circuit against mature silicon. Every input in Section 3 is a design assumption; parasitic capacitance of dense crossbar wiring could multiply C by 10–100, raising E_ad to 250 zJ–2.5 aJ — still favorable, but the compounding of parasitics, flux crosstalk, and clock-distribution loss in a million-node fabric is exactly where paper architectures historically die. A second objection: "quantum-inspired" here means only "superconducting and adiabatic"; readers expecting quantum speedup will find none, and we accept the framing critique of [11] that the value lies in the physical process, not quantum-mechanical labels. The thermodynamic-viability framing of [12] and the structural-coherence distinction of [9] suggest deeper questions — whether driven adiabatic coherence can be made structural rather than clock-sustained [9] — that this paper raises but does not answer, as does the question of whether spiking dynamics constitute a generative syntax in the sense of [10].

**Open questions.** Optimal T under joint dynamic/static minimization with real JJ shunting; scalable adiabatic clock distribution at 4.2 K; cryogenic synapse plasticity; and standardized benchmark protocols that include cryogenic overhead as a first-class accounting item.

## 7. Conclusion

We have presented a fully derived energy budget for a quantum-inspired, superconducting, near-adiabatic spiking computing architecture. With explicitly stated junction parameters, the computed event energy is 7.5 zJ (2.5 zJ adiabatic + 5 zJ static leakage), with a thermal margin factor of ~129 at 4.2 K and a node-level energy reduction of more than eight orders of magnitude against assumed pJ-scale CMOS spiking baselines — far exceeding the 50% target at the component level. The decisive caveat is systemic: cryogenic overhead power dominates at sparse workloads, so the architecture's viability is a function of workload intensity and I/O co-design, not of node physics alone. We have specified the falsification conditions and argued that standardized, overhead-inclusive benchmarking on temporally structured workloads is the necessary next step. The contribution is not a built system but a transparent, reproducible thermodynamic case — every input sourced, every step shown — for taking superconducting adiabatic neuromorphic hardware seriously as the low-energy end of the computing landscape.

## References

[1] arXiv:2504.10053v2 | Synthetic Biology meets Neuromorphic Computing: Towards a bio-inspired Olfactory Perception System

[2] arXiv:2601.10742v1 | Line-based Event Preprocessing: Towards Low-Energy Neuromorphic Computer Vision

[3] arXiv:2306.03369v3 | Event Encryption: Rethinking Privacy Exposure for Neuromorphic Imaging

[4] arXiv:1905.10415v3 | Quantum-inspired algorithms in practice

[5] arXiv:2304.04640v5 | NeuroBench: A Framework for Benchmarking Neuromorphic Computing Algorithms and Systems

[6] arXiv:2502.20729v1 | NeuroMorse: A Temporally Structured Dataset For Neuromorphic Computing

[7] arXiv:2004.14942v1 | Memristors -- from In-memory computing, Deep Learning Acceleration, Spiking Neural Networks, to the Future of Neuromorphic and Bio-inspired Computing

[8] arXiv:2011.12013v3 | Exploring the landscapes of "computing": digital, neuromorphic, unconventional -- and beyond

[9] QNFO: Structural vs Driven Quantum Coherence | DOI 10.5281/zenodo.18441401

[10] QNFO: Syntactic Generation | DOI 10.5281/zenodo.22758173

[11] QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation | DOI 10.5281/zenodo.22753022

[12] QNFO: Thermodynamic Viability and the Universality of Feynman Matter | DOI 10.5281/zenodo.18036068