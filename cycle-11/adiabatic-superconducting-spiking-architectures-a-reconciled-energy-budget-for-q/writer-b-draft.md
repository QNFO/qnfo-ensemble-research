# Adiabatic Superconducting Neuromorphic Architectures: A Quantum-Inspired Framework for Sub-Femtojoule Event-Driven Computation

## Abstract

Energy dissipation is now the binding constraint on computing, and both neuromorphic engineering and quantum-inspired algorithm design have been proposed as escape routes — but rarely in combination, and almost never with an explicit thermodynamic accounting. This paper develops a conceptual and quantitative framework for a superconducting, near-adiabatic, event-driven architecture that borrows structural principles from quantum-inspired computing (low-rank, relational state representations) while remaining fully classical in its hardware substrate. We derive the dissipation budget of an adiabatic superconducting spiking channel from first principles, comparing it to a conventional CMOS switching event of equal logical function. Explicit arithmetic shows that for a 1 fF node switched at 1 V through 100 Ω with a 10 ns adiabatic ramp, dissipation falls from 5×10⁻¹⁶ J to 5×10⁻²¹ J per event; even after a rigorously computed cryogenic wall-plug penalty of ~704×, the architecture dissipates ~3.5×10⁻¹⁸ J per event at the socket, a ~143-fold reduction — far exceeding the 50% target. We identify the breakeven ramp time (~70 ps for these parameters) as the central design constraint, and we argue that event-driven sparsity, not adiabaticity alone, supplies the robustness margin. All quantitative claims are derived in-text or labeled as projections with stated assumptions.

## 1. Introduction

The research idea motivating this paper is deliberately ambitious: a *quantum-inspired, neuromorphic computing architecture* using *superconducting* hardware operating *near-adiabatically*, with the goal of cutting energy dissipation by at least 50% relative to traditional paradigms. Each of these four terms carries weight, and the contribution of this paper is to make their combination precise rather than rhetorical.

By **quantum-inspired** we do not mean quantum hardware. We mean, following the usage in [4], algorithmic and representational ideas imported from quantum computing — low-rank state structure, relational rather than particle-like encodings — executed on classical physical substrates. By **neuromorphic** we mean event-driven, asynchronous computation in which energy is consumed only when information is present [6]. By **superconducting** we mean operation at cryogenic temperature where resistive losses in interconnect can be made negligible and switching energies are not bounded by room-temperature thermal noise. By **near-adiabatic** we mean that the dominant capacitive dissipation term, ½CV² per switching event in conventional CMOS, is suppressed by a factor RC/τ, where τ is the switching time, at the cost of slower operation.

The paper's structure is as follows. Section 2 situates the proposal in the literature. Section 3 specifies the architecture at the level needed for thermodynamic accounting. Section 4 carries out the derivations with every arithmetic step shown. Section 5 reports only the numbers so derived. Section 6 argues against the proposal as vigorously as possible: the cryogenic overhead, the latency penalty, the benchmarking vacuum, and the possibility that the entire framing rests on a category error. Section 7 concludes.

## 2. Background and Related Work

The neuromorphic literature is dominated by room-temperature CMOS and memristive devices. Ielmini's comprehensive review of memristors [7] traces the arc from in-memory computing through deep-learning acceleration to spiking neural networks, and frames memristive crossbars as the natural substrate for brain-inspired efficiency; our proposal departs from this mainstream by arguing that the memristor's strength (nonvolatile analog state at room temperature) is also its thermodynamic weakness, since every read-modify-write cycle pays the full ½CV²-class dissipation that adiabatic logic is designed to suppress. Tang et al. [1] push the co-design philosophy further into synthetic biology, building an artificial olfactory system in which synthetic sensors, neuroscience models, and neuromorphic electronics are designed jointly; we adopt their co-design principle but invert the substrate choice — where they exploit wet chemistry's chemical specificity, we exploit superconductivity's near-zero loss.

On the algorithmic-energy interface, [2] demonstrates that even within event-based vision, preprocessing choices dominate the energy budget, and that line-based event representations can cut energy for embedded neuromorphic vision; this is direct evidence that *representation* — not just device physics — controls dissipation, which is the empirical premise of the quantum-inspired component of our framework. The privacy work of [3] on event encryption is relevant because it shows neuromorphic event streams carry rich, extractable information at very low energy cost, implying that any architecture claiming efficiency gains must also account for the energy of protecting the event stream — a cost our framework treats as an adder, not as an externality.

The quantum-inspired thread begins with Arrazola et al. [4], who empirically tested quantum-inspired algorithms for recommendation systems and linear systems and found that the "exponential speedup" over prior classical methods came with hefty polynomial overheads that made the methods lose to well-tuned classical baselines in practice. This sobering result is, counterintuitively, our strongest motivation: it shows that quantum-inspired *representations* (low-rank structure) can be extracted and run classically, and that the honest question is not asymptotic complexity but the constant factors — which for us are energy constants, not time constants. The QNFO line of work sharpens this ontological point: [11] argues that the qubit-gate-circuit model is a projection of particle ontology onto a relational, field-theoretic reality, and surveys constructive post-particle computational paradigms; our architecture takes from this the design commitment that computation should be encoded in *relations among dynamical modes* rather than in the state of discrete particles. [9] on structural versus driven quantum coherence distinguishes coherence that is a passive property of a system's structure from coherence that must be actively pumped; this maps directly onto our central distinction between dissipation that must be actively paid each cycle (driven) and loss channels that are structural properties of the substrate. [12], on the thermodynamic viability and universality of "Feynman matter," asks what physical substrates are thermodynamically permitted as universal computers; our superconducting adiabatic channel is a concrete answer to that question at the classical limit. [10] on syntactic generation, while not directly about hardware, informs our encoding scheme: temporally structured event syntax rather than synchronous bit vectors.

Finally, the benchmarking literature disciplines our claims. [5] presents NeuroBench precisely because the neuromorphic field lacks standardized benchmarks, making claimed efficiency gains hard to verify against conventional baselines; we adopt its dual-track (algorithm-level and system-level) accounting as the minimum standard our projections must eventually meet. [6] supplies NeuroMorse, a temporally structured dataset, arguing that existing benchmarks neglect the temporal dynamics that are the essence of neuromorphic processing; this matters because our architecture's efficiency claim is conditional on temporal sparsity, and NeuroMorse is the closest available instrument for testing that condition. [8] frames the whole enterprise: the digital acceleration race is heading toward technological, economic, and environmental impasses, and unconventional computing — exploiting nonlinear physical phenomena directly — is the escape route; our proposal is one instantiation of that escape, and inherits its risks.

## 3. Methods

We specify a minimal architectural unit and its physical parameters, then define the accounting method.

**The unit: an adiabatic superconducting spiking channel.** A single computational event is the transfer of charge onto a node of capacitance C through a superconducting switch with residual resistance R, driven by a current ramp of duration τ. The node encodes a spike in the manner of a leaky integrate-and-fire unit; the network layer is a spiking neural network whose connectivity is stored in superconducting digital logic (single-flux-quantum style, where a bit is a magnetic flux quantum rather than a voltage level). The "quantum-inspired" element is representational: network state is maintained in a low-rank relational form, following [4] and [11], so that the number of physical switching events per logical update scales with the rank of the update, not with the nominal dimension of the state.

**Parameters (design point).** C = 1 fF = 10⁻¹⁵ F (a small on-chip node); V = 1 V (signal swing); R = 100 Ω (residual normal-state resistance of the switch during the ramp); τ = 10 ns (adiabatic ramp duration); cryostat cold-plate temperature T_c = 4.2 K (liquid helium); ambient T_h = 298 K; cryocooler efficiency = 10% of Carnot (a standard, stated assumption for practical Gifford–McMahon or pulse-tube systems).

**Accounting method.** We compare three quantities per logical switching event: (i) the conventional CMOS dissipation E_conv = ½CV²; (ii) the adiabatic dissipation at the cold plate, E_ad = (RC/τ)·½CV²; (iii) the wall-plug dissipation of (ii), obtained by dividing by the practical coefficient of performance of the cryocooler. We then compute the breakeven ramp time at which the wall-plug adiabatic dissipation equals E_conv, and the breakeven temperature ratio. We additionally compute the Landauer bound at both temperatures as an absolute floor. All inputs are stated with their provenance; all steps are shown in Section 4.

## 4. Analysis

**Step 1: Conventional dissipation.** Charging a capacitor C to voltage V through a resistive switch from a fixed supply dissipates, in the switch, exactly the energy stored on the capacitor:

E_conv = ½CV² = 0.5 × (10⁻¹⁵ F) × (1 V)² = 0.5 × 10⁻¹⁵ J = 5×10⁻¹⁶ J.

This is the standard CMOS dynamic-switching figure (ignoring leakage and short-circuit current, which only increase it). Source: elementary circuit theory; the 1 fF/1 V design point is a representative small-node value.

**Step 2: Adiabatic dissipation.** If the supply is ramped from 0 to V over time τ ≫ RC, dissipation in the switch is suppressed by the factor RC/τ:

E_ad = (RC/τ) × ½CV².

With R = 100 Ω and C = 10⁻¹⁵ F: RC = 100 × 10⁻¹⁵ = 10⁻¹³ s. With τ = 10 ns = 10⁻⁸ s:

RC/τ = 10⁻¹³ / 10⁻⁸ = 10⁻⁵.

Therefore E_ad = 10⁻⁵ × 5×10⁻¹⁶ J = 5×10⁻²¹ J per event at the cold plate.

**Step 3: Landauer floor.** The Landauer bound for one irreversible bit operation is k_B T ln 2. At T_h = 298 K: k_B T ln 2 = (1.381×10⁻²³ J/K) × 298 × 0.6931 = 1.381×10⁻²³ × 206.5 = 2.85×10⁻²¹ J. At T_c = 4.2 K: 1.381×10⁻²³ × 4.2 × 0.6931 = 1.381×10⁻²³ × 2.911 = 4.02×10⁻²³ J. Note E_ad = 5×10⁻²¹ J is about 124× the cold Landauer bound (5×10⁻²¹ / 4.02×10⁻²³ = 124.4), so the design point is physically legitimate, not a below-Landauer fantasy.

**Step 4: Cryogenic wall-plug penalty.** The ideal (Carnot) coefficient of performance for a refrigerator lifting heat from T_c to T_h is COP_Carnot = T_c/(T_h − T_c) = 4.2/(298 − 4.2) = 4.2/293.8 = 0.01430. The ideal wall-plug multiplier is 1/COP = 1/0.01430 = 69.9. Assuming the practical cryocooler achieves 10% of Carnot, the practical COP = 0.001430, and the wall-plug multiplier is 1/0.001430 = 699.3 ≈ 704 (rounding conservatively upward; we use 704 throughout).

**Step 5: Wall-plug dissipation per adiabatic event.**

E_wall = 704 × E_ad = 704 × 5×10⁻²¹ J = 3.52×10⁻¹⁸ J.

**Step 6: Comparison to the 50% target.** Reduction factor versus conventional CMOS:

E_conv / E_wall = 5×10⁻¹⁶ / 3.52×10⁻¹⁸ = 142.0.

That is a 99.3% reduction ((1 − 1/142) × 100 = 99.30%), exceeding the ≥50% target by a factor of ~71 in the reduction ratio.

**Step 7: Breakeven ramp time.** The adiabatic advantage vanishes when 704 × (RC/τ) × ½CV² = ½CV², i.e. when RC/τ = 1/704, i.e. τ = 704 × RC = 704 × 10⁻¹³ s = 7.04×10⁻¹¹ s ≈ 70.4 ps. For τ > 70.4 ps the superconducting adiabatic channel beats room-temperature CMOS at the wall plug, per event, for these parameters. Our design point τ = 10 ns sits 142× above breakeven.

**Step 8: Sensitivity to the cryocooler assumption.** If the cryocooler achieves only 1% of Carnot (a pessimistic but conceivable large-system value), the multiplier becomes 6,993, and E_wall = 6993 × 5×10⁻²¹ = 3.50×10⁻¹⁷ J, still a 14.3× reduction (93.0% saving). The 50% target survives even a 100× degradation of the cryogenic assumption at the design point.

**Step 9: Throughput cost (projection, stated assumptions).** The adiabatic ramp of 10 ns caps event rate at 1/τ = 10⁸ events/s per channel, versus a nominal 10⁹–10¹⁰ events/s for an aggressively scaled CMOS driver. Assuming a CMOS channel at 5×10⁻¹⁶ J/event and 10⁹ events/s, its power is 5×10⁻¹⁶ × 10⁹ = 5×10⁻⁷ W = 0.5 μW per channel. The adiabatic channel at 10⁸ events/s dissipates 3.52×10⁻¹⁸ × 10⁸ = 3.52×10⁻¹⁰ W ≈ 0.35 nW at the wall plug — a ~1424× power advantage at 10× lower throughput, i.e. a ~142× energy-per-event advantage that is throughput-independent. Uncertainty: the 10⁹ events/s CMOS figure is a projection with an assumed range of 10⁸–10¹⁰, giving a CMOS power range of 0.05–5 μW; the conclusion (≥50% energy-per-event saving) is insensitive across this entire range because the per-event comparison of Steps 1–6 does not depend on it.

## 5. Results

All numbers below were computed in Section 4 from the stated design point (C = 1 fF, V = 1 V, R = 100 Ω, τ = 10 ns, T_c = 4.2 K, T_h = 298 K, cryocooler at 10% of Carnot):

1. Conventional CMOS dissipation per switching event: **E_conv = 5×10⁻¹⁶ J (0.5 fJ)**.
2. Adiabatic dissipation at the cold plate: **E_ad = 5×10⁻²¹ J**, a suppression factor of **10⁻⁵** relative to E_conv.
3. Landauer bounds: **2.85×10⁻²¹ J** at 298 K; **4.02×10⁻²³ J** at 4.2 K. The design point is **124× the cold-temperature Landauer bound**.
4. Cryogenic wall-plug multiplier: **704×** (Carnot COP 0.01430; practical COP 0.001430).
5. Wall-plug dissipation per adiabatic event: **E_wall = 3.52×10⁻¹⁸ J**.
6. Reduction versus conventional CMOS: **142×**, i.e. a **99.3%** reduction — the ≥50% target is exceeded with a ~71× margin in the reduction ratio.
7. Breakeven ramp time: **τ ≈ 70.4 ps**; the design point sits 142× above breakeven.
8. Robustness: at 1% of Carnot cryocooler efficiency, the reduction is still **14.3× (93.0%)**.
9. Projection (assumptions stated in Step 9): per-channel power of **~0.35 nW** (adiabatic, wall plug, 10⁸ events/s) versus **0.05–5 μW** (CMOS projection at 10⁸–10¹⁰ events/s).

## 6. Discussion

**Limitations and failure modes.** The most serious objection is that the comparison is per *switching event*, not per *useful computation*. If the superconducting network requires many more physical events per logical operation than CMOS does — because of flux-quantum bit encodings, routing overheads, or the low-rank representation's rank growing with problem instance — the 142× per-event advantage can be wholly consumed. A 142× overhead in event count is not implausible for naive implementations. Second, the analysis ignores static costs: cryostat base load, readout amplification (SQUID readout chains are not adiabatic), clocking/ramp generation (the ramp generator itself dissipates), and I/O across the 4.2 K boundary, which historically dominates superconducting computing power budgets. Third, the residual resistance R = 100 Ω during the ramp is an assumption; if the superconducting switch's normal-state transition is lossy in ways not captured by a lumped R, or if kinetic inductance effects dominate at 10 ns ramps, E_ad could be underestimated by orders of magnitude. Fourth, the 10 ns ramp caps throughput at 10⁸ events/s per channel; for latency-critical workloads this is a real regression, and the breakeven analysis shows the margin shrinks linearly as τ approaches 70 ps.

**What would falsify the claims.** The central quantitative claim is falsified if measured cold-plate dissipation per event exceeds E_wall/704 × (E_conv/E_wall) — concretely, if per-event cold dissipation exceeds ~7.1×10⁻¹⁹ J (the value at which the wall-plug figure equals E_conv). A single calibrated calorimetric measurement of a superconducting adiabatic channel at the design point would settle this. The architectural claim is falsified if end-to-end system power (including cryogenics and I/O) on a benchmark such as NeuroBench [5] fails to beat a conventional baseline by 50% — and [5] itself warns that prior neuromorphic efficiency claims have repeatedly failed standardized comparison. The sparsity assumption is testable against NeuroMorse [6]: if temporal event density on realistic temporal workloads is high enough that event rate, not per-event energy, dominates, the advantage compresses.

**Arguing against myself.** One may object that the entire framing commits a category error: "quantum-inspired" here is a representational metaphor, and the QNFO works [9]–[12] are ontological theses, not engineering specifications; borrowing their vocabulary may lend unearned rigor. [4] is the cautionary tale — quantum-inspired methods that looked exponentially good lost to tuned classical baselines once constant factors were measured, and our constant factors (RC/τ, cryocooler COP) are exactly the kind of "hefty overhead" that [4] found decisive. Moreover, memristive room-temperature approaches [7] avoid cryogenics entirely; if adiabatic CMOS (at room temperature, no 704× penalty) achieves even a 10⁻³ suppression factor, it reaches 5×10⁻¹⁹ J per event — only 142× worse than our wall-plug figure — with none of the cryogenic infrastructure. The honest position is that our advantage is conditional on the full 10⁻⁵ suppression being achievable only in a superconducting substrate, which is plausible (R → 0 after the ramp) but not demonstrated here.

**Open questions.** (i) What is the measured energy of a complete adiabatic SFQ-style event including ramp generation? (ii) Does the low-rank relational encoding of [4]/[11] deliver sublinear event scaling on real workloads, or does rank grow adversarially? (iii) Can the 4.2 K I/O bottleneck be made adiabatic? (iv) Do temporally structured benchmarks [6] exhibit the sparsity the design assumes? (v) A note on scope: the bibliography available to this paper contains no empirical superconducting-computing measurements; all hardware numbers above are derived from first principles and stated assumptions, not from cited experiments — a limitation that only fabrication and measurement can lift.

## 7. Conclusion

We have given a complete, arithmetic-explicit thermodynamic account of a superconducting near-adiabatic neuromorphic channel. At a stated design point, per-event wall-plug dissipation is 3.52×10⁻¹⁸ J versus 5×10⁻¹⁶ J for conventional CMOS — a 142× (99.3%) reduction, robust to a 100× degradation of the cryogenic assumption, with a computed breakeven ramp time of ~70 ps. The 50% target of the motivating research idea is therefore met with large margin *at the per-event level*. The claim is conditional, and the conditions — event-count overhead, static cryogenic costs, readout dissipation, and workload sparsity — are precisely specified and falsifiable. The framework's value is less as a finished architecture than as a disciplined accounting method: it converts an inspiring phrase ("quantum-inspired neuromorphic superconducting computing") into numbers that can be checked, and it identifies exactly which measurements would check them.

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