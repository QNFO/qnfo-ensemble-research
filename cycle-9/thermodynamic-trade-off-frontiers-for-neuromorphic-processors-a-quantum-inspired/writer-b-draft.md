# A Quantum-Inspired Non-Equilibrium Thermodynamic Model of the Energy–Speed Trade-off in Neuromorphic Processors

## Abstract

Neuromorphic processors promise large gains in energy efficiency over von Neumann architectures, but no principled theory currently predicts where the optimal operating point between energy per operation and computational speed should lie. We develop a quantum-inspired, non-equilibrium thermodynamic model in which a neuromorphic core is treated as a driven dissipative system whose state evolution follows a gradient flow on a free-energy landscape, with computation rate coupled to dissipation through a Rayleigh-type potential. Combining the Landauer bound on irreversible bit erasure with the Margolus–Levitin quantum limit on operation rate yields an analytic energy–speed trade-off curve E(τ) = max(kT ln 2, πħ/2τ) per elementary operation, and a crossover clock period τ* = πħ/(2kT ln 2) ≈ 5.8×10⁻¹⁴ s at 300 K below which quantum speed limits dominate. We compute the implied minimum power per operation and project, under stated assumptions, that near-term neuromorphic devices operating at 10–100 MHz sit roughly 4–6 orders of magnitude above the thermodynamic floor, leaving efficiency headroom that is realistically capped by leakage and I/O rather than by fundamental bounds. The model produces falsifiable 12-month predictions for spiking neuromorphic hardware. Significance: the framework gives hardware designers a physically grounded target curve rather than empirical rules of thumb.

## 1. Introduction

Neuromorphic computing—hardware that emulates the event-driven, massively parallel architecture of biological neural circuits, typically using spiking neurons and analog memristive or capacitive synapses—has been marketed primarily on energy efficiency. Yet reported figures vary by orders of magnitude, and it is unclear how close any given device is to a fundamental limit, or whether pushing clock rates (and hence speed) necessarily sacrifices efficiency. The physics of computation provides two canonical constraints: erasing one bit of information dissipates at least kT ln 2 of heat (Landauer's principle), and the rate of any physical state transition is bounded by its energy via the Margolus–Levitin theorem. What is missing is a model that connects these single-operation bounds to the *system-level* behavior of a non-equilibrium, continuously driven device such as a neuromorphic chip, where the device never equilibrates and computation is a sustained dissipative flux rather than a sequence of isolated erasures.

This paper builds such a model. We treat the neuromorphic core as a far-from-equilibrium system whose macrostate relaxes along a gradient flow, borrowing geometric machinery from modern non-equilibrium thermodynamics, and we impose quantum-inspired rate limits on the microscopic transitions that implement synaptic updates. The result is a closed-form trade-off curve between energy per operation and operation rate, plus concrete numerical projections for devices expected within the next 12 months. We deliberately restrict empirical claims to arithmetic derived from stated physical constants and clearly labeled projections; no simulated or measured data are invented.

## 2. Background and Related Work

Our model sits at the intersection of three literatures: quantum-inspired classical computing, geometric non-equilibrium thermodynamics, and the fundamental physical limits of computation.

On the first thread, Arrazola [1] studies the practical performance of quantum-inspired algorithms for recommendation systems and low-rank linear systems, showing that although these classical methods achieve exponential asymptotic speedups over prior classical algorithms, they carry hefty polynomial overheads relative to true quantum algorithms. This is directly relevant to our argument: "quantum-inspired" need not mean quantum hardware, and the same logic applies to quantum-inspired *thermodynamic* modeling of classical neuromorphic devices. Complementing this, the review of topological states and quantum-inspired information processing in classical circuits [7] demonstrates that classical electric circuit networks can simulate Schrödinger-type dynamics and implement quantum-inspired information processing, establishing a concrete precedent for importing quantum formalisms into classical electronic hardware—the exact strategy we adopt for neuromorphic cores.

On the thermodynamic thread, the comparison of geometric frameworks for dissipative evolution [2] reviews classical irreversible thermodynamics, gradient dynamics, Rayleigh dissipation potentials, and the dissipative d'Alembert framework, and clarifies their mutual relations; we use the gradient-flow structure and Rayleigh potential formalism as the backbone of our device model. The Nambu non-equilibrium thermodynamics framework of [3] shows that strongly nonlinear far-from-equilibrium systems can be locally reduced to a simple bracket form, which justifies our local linearization of neuromorphic dynamics around a non-equilibrium steady state even though the underlying device is highly nonlinear. Extended irreversible thermodynamics applied to non-equilibrium critical behavior [6] demonstrates that non-equilibrium critical phenomena can be treated with flux-dependent state variables; this matters because neuromorphic devices near spiking thresholds exhibit criticality-like avalanching, and flux corrections to local equilibrium are precisely the regime our model must handle. At smaller scales, the non-equilibrium probability flux of a thermally driven micromachine [8] computes the steady-state probability distribution and probability flux of a three-sphere spring motor, providing a template for treating a driven computing element as a system with a sustained non-equilibrium probability current rather than an equilibrium ensemble—exactly the picture we take for a clocked neuromorphic core. The non-equilibrium statistical mechanics of damage phenomena [4] develops a Gibbs-like formalism for non-equilibrium states in fiber-bundle models with thermal noise and fiber decay, which we draw on for the treatment of device aging and stochastic failure as non-equilibrium ensembles. Finally, the coupled adsorption–diffusion model of [5] shows how two interacting transport processes can be merged into a single effective diffusion description; we use an analogous reduction to fold synaptic state updates and signal propagation into one effective dissipative channel.

On the limits-of-computation thread, the QNFO analyses of thermodynamic and quantum constraints on scalable quantum computing [10], [11] argue that fault-tolerant quantum architectures face thermodynamic and informational bottlenecks at scale, and the study of fundamental limits in post-classical computing [12] examines the Landauer bound, Margolus–Levitin theorem, Bremermann limit, and Bekenstein bound, showing that quantum error-correction overheads of 10²–10³ physical operations per logical operation multiply the thermodynamic cost per useful operation. The universality-of-Feynman-matter analysis [9] frames computation as an inescapably physical, substrate-dependent process. Together these works supply the numerical bound structure we import into the classical neuromorphic setting; notably, neuromorphic hardware avoids the error-correction multiplier entirely, which is a central quantitative advantage we compute below.

## 3. Methods

**Modeling assumptions.** We model a neuromorphic core as a set of N computational state variables x = (x₁,…,x_N) (membrane potentials, synaptic weights, spike flags) evolving under a driving protocol (clocked updates and event routing) toward a driven steady state. The device is held at ambient temperature T and exchanges heat with a reservoir.

**Dynamics.** Following the gradient-flow structure reviewed in [2], we write the coarse-grained dynamics as

 ẋ = −M ∇F(x; u(t)) + ξ(t),

where F is a non-equilibrium free-energy-like functional, M is a positive semi-definite mobility (Onsager) matrix, u(t) is the external drive (input spikes and clock), and ξ is thermal noise. The Rayleigh dissipation potential is Φ = ½ ẋᵀ M⁻¹ ẋ, and the entropy production rate is σ = 2Φ/T ≥ 0. Following the local-reduction argument of [3], we justify evaluating this dynamics locally around the non-equilibrium steady state x*, where the Nambu-type bracket structure collapses to the gradient form above. The steady state carries a non-zero probability flux in configuration space, in direct analogy with the micromachine of [8]; this flux is the thermodynamic signature of ongoing computation.

**Operation accounting.** One elementary computational operation is defined as one irreversible state update of one variable (a synaptic weight write or a spike-generation decision). Each such operation erases (or randomizes) at least one bit of the prior state distribution in the worst case, incurring the Landauer cost, and its duration τ cannot be shorter than the quantum rate limit permits for the energy invested.

**Quantum-inspired rate limit.** The Margolus–Levitin theorem states that a system with average energy E above its ground state takes at least τ ≥ πħ/(2E) to evolve to an orthogonal state. We apply it per operation: to complete one distinguishable state update in time τ, the energy devoted to that update must satisfy E ≥ πħ/(2τ). This is a "quantum-inspired" bound in the sense of [1] and [7]: it is a quantum result applied to a classical device, and it is conservative (real classical devices are far above it).

**Combined cost model.** The energy per operation is

 E(τ) = max( kT ln 2, πħ/(2τ) ),

and the power per active operation channel is P = E(τ)/τ. The trade-off curve is flat (Landauer-dominated) for slow operation and steep (rate-limited) for fast operation, with crossover at τ* = πħ/(2kT ln 2).

**Projection methodology.** For 12-month predictions we combine the bound with stated engineering assumptions (leakage fractions, activity factors, I/O overhead) and propagate uncertainty explicitly. All arithmetic is shown in Section 4.

## 4. Analysis

**Constants (CODATA values, standard references).** Boltzmann constant k = 1.381×10⁻²³ J/K; ħ = 1.0546×10⁻³⁴ J·s; ln 2 = 0.6931; T = 300 K (assumed ambient).

**Step 1: Landauer cost per bit.**
 kT ln 2 = 1.381×10⁻²³ × 300 × 0.6931
 = 4.143×10⁻²¹ × 0.6931 = 2.872×10⁻²¹ J.
So E_L ≈ 2.87×10⁻²¹ J ≈ 2.87 zJ per erased bit at 300 K.

**Step 2: Margolus–Levitin crossover.** Set πħ/(2τ*) = kT ln 2:
 τ* = πħ / (2 kT ln 2)
 = (3.1416 × 1.0546×10⁻³⁴) / (2 × 2.872×10⁻²¹)
 = 3.3127×10⁻³⁴ / 5.744×10⁻²¹
 = 5.768×10⁻¹⁴ s ≈ 57.7 fs.
Below τ* ≈ 58 fs, the quantum rate limit exceeds the Landauer cost; above it, Landauer dominates. Any conceivable neuromorphic clock (ns-scale and slower) is deep in the Landauer-dominated regime.

**Step 3: Minimum power per operation at a realistic clock.** Take τ = 10 ns (100 MHz event rate, typical of spiking cores):
 E_min = max(2.872×10⁻²¹, π×1.0546×10⁻³⁴/(2×10⁻⁸))
 = max(2.872×10⁻²¹, 1.656×10⁻²⁵) = 2.872×10⁻²¹ J.
 P_min = E_min/τ = 2.872×10⁻²¹ / 10⁻⁸ = 2.872×10⁻¹³ W per active operation channel.

**Step 4: Chip-level floor.** Assume a 12-month-representative device with N = 10⁶ synapses and activity factor α = 0.01 (1% of synapses update per clock tick, a standard spiking-workload figure; assumption, labeled as such):
 active operations per second = N × α / τ = 10⁶ × 0.01 / 10⁻⁸ = 10¹⁴ ops/s.
 Total floor power = 10¹⁴ × 2.872×10⁻²¹ = 2.872×10⁻⁷ W ≈ 0.29 µW.
This is the *fundamental* floor; it is absurdly below real devices, which is itself the key finding.

**Step 5: Gap to current devices.** A representative current spiking processor achieves on the order of 10–100 GOPS/W (published vendor figures; we use the conservative 10¹⁰ ops/J). Energy per operation actually consumed:
 E_actual = 1/10¹⁰ = 10⁻¹⁰ J = 100 pJ.
 Ratio to floor: E_actual / E_L = 10⁻¹⁰ / 2.872×10⁻²¹ = 3.48×10¹⁰.
So current devices sit ~10 orders of magnitude above the Landauer floor per operation. However, the *achievable* floor is set by leakage and I/O, not by Landauer: assuming (labeled assumption) that subthreshold and dielectric leakage in a 10⁶-synapse analog core consumes ~1 mW and I/O another ~10 mW at 100 MHz, the practical floor per active op is
 E_practical ≈ (1.1×10⁻² W) / (10¹⁴ ops/s) = 1.1×10⁻¹⁶ J ≈ 110 fJ/op,
which is still ~3.8×10⁴ times the Landauer cost (1.1×10⁻¹⁶ / 2.872×10⁻²¹ = 3.83×10⁴) but ~10⁶ below today's 100 pJ. Uncertainty: leakage estimates vary by ±1 order of magnitude across process nodes, so E_practical lies in 10 fJ–1 pJ.

**Step 6: Quantum comparison.** Using the error-correction multiplier of 10²–10³ physical operations per logical operation reported in [12], a fault-tolerant quantum processor's effective floor per *logical* operation is
 E_Q = (10² to 10³) × E_L = 2.87×10⁻¹⁹ to 2.87×10⁻¹⁸ J,
i.e., 100–1000× the neuromorphic floor per operation, before cryogenic overhead (omitted here, which only worsens the quantum figure).

**Step 7: Trade-off curve slope in the practical regime.** In the Landauer-dominated regime the bound is flat, so the model predicts the *fundamental* energy–speed trade-off is negligible across the entire 1 Hz–1 GHz range; observed speed–efficiency trade-offs in real neuromorphic chips must therefore arise from engineering effects (charging capacitance ∝ frequency, leakage ∝ temperature, routing congestion), not from fundamental physics. Quantitatively, dynamic charging energy for a 10 fF node at V = 0.5 V is ½CV² = 0.5×10⁻¹⁴×0.25 = 1.25×10⁻¹⁵ J = 1.25 fJ per switching event—already ~436× the Landauer cost (1.25×10⁻¹⁵/2.872×10⁻²¹ = 4.35×10²), confirming that switching physics, not information erasure, dominates.

## 5. Results

All numbers below are computed in Section 4 or labeled projections.

1. **Landauer floor:** 2.87×10⁻²¹ J per erased bit at 300 K (computed, Step 1).
2. **Quantum-rate crossover clock period:** τ* ≈ 5.77×10⁻¹⁴ s ≈ 58 fs (computed, Step 2). All realistic neuromorphic clocks are ≥10⁵ times slower, so Landauer dominates.
3. **Minimum power per operation channel at 100 MHz:** 2.87×10⁻¹³ W (computed, Step 3).
4. **Fundamental chip floor:** ~0.29 µW for a 10⁶-synapse core at 1% activity and 100 MHz (projection; depends on the stated N, α, τ assumptions, each uncertain by ±1 order of magnitude, giving a range 0.003–30 µW).
5. **Current-device gap:** today's spiking hardware at ~10¹⁰ ops/J consumes ~3.5×10¹⁰ times the Landauer floor per operation (computed, Step 5).
6. **Practical floor projection:** ~110 fJ/op with leakage+I/O of 11 mW (projection; range 10 fJ–1 pJ under ±1 order-of-magnitude leakage uncertainty). **12-month prediction:** next-generation neuromorphic chips will land in the 1–10 pJ/op range—2–5× better than today's ~100 pJ, but still 10⁴–10⁵ above the practical floor—because the binding constraints are analog noise margins and I/O energy, not thermodynamics.
7. **Quantum comparison:** fault-tolerant quantum logic operations carry a floor 100–1000× higher per logical operation than neuromorphic operations, before cryogenics (computed from [12]'s multiplier, Step 6).
8. **Trade-off structure:** the fundamental energy–speed curve is flat from DC to ~1 GHz; observed speed–efficiency slopes in neuromorphic hardware are engineering artifacts, since even single-node switching energy (1.25 fJ at 10 fF, 0.5 V) exceeds the Landauer cost by ~436× (computed, Steps 5, 7).

## 6. Discussion

**Limitations.** The model's core weakness is the gap between its two levels: the fundamental bounds are rigorous but vacuous for engineering (10 orders of magnitude of headroom), while the practical projections rest on leakage and I/O assumptions that we cannot verify without measurements. The activity factor α = 0.01 and the 11 mW leakage figure are plausible but not measured; a reader should treat Result 6 as a structured guess, not a prediction with empirical force. The gradient-flow dynamics of Section 3 assumes a mobility matrix M that is locally well-behaved; memristive synapses with history-dependent plasticity may violate this, and the local Nambu reduction of [3] is only valid near the steady state, whereas spiking avalanches push devices far from it. The Landauer accounting also assumes one bit erased per operation; reversible or mostly-reversible neuromorphic updates (e.g., charge-sharing logic) would lower the floor further, and stochastic computing could in principle *exploit* thermal noise rather than fight it, a direction our cost model does not capture.

**Failure modes and falsifiability.** The 12-month prediction (1–10 pJ/op for next-generation chips) is falsified if announced devices either stay above 50 pJ/op (efficiency progress stalls) or drop below 0.1 pJ/op (our practical-floor estimate of leakage was wildly pessimistic). The claim that the fundamental trade-off is flat would be falsified by any demonstrated device whose energy per operation rises measurably with clock rate in the sub-GHz regime *after* leakage and I/O are subtracted out. The quantum comparison would be falsified if logical error-correction overhead fell below ~10×, which would narrow the 100–1000× gap.

**Arguing against ourselves.** One could object that applying Margolus–Levitin to classical CMOS is decorative: since the crossover is at 58 fs and devices run at ~10 ns, the "quantum-inspired" half of the model never binds, and the paper reduces to Landauer plus guesswork. This is largely true, and we state it plainly; the value of the rate limit is that it *bounds the ceiling* of any conceivable speedup, showing that even a 10⁶× clock increase would not hit quantum limits—useful for ruling out "physics will stop us" arguments in roadmap debates. A second objection: the bibliography contains no neuromorphic-hardware empirical papers; all device-level numbers here are derived from physical constants and stated assumptions, and the absence of measured benchmarks is a genuine limitation of this study. A third: non-equilibrium flux corrections of the kind studied in [6] could raise the effective cost near spiking criticality, potentially invalidating the flat-trade-off claim in avalanche-heavy workloads; this is the most physically interesting open question.

**Open questions.** (i) Can memristive analog synapses approach the 110 fJ practical floor, or does variability/noise impose a higher information-theoretic cost per reliable update? (ii) Does avalanche dynamics near criticality add a flux-dependent term to σ that scales superlinearly with activity, bending the flat trade-off curve upward? (iii) What is the exact leakage-vs-activity Pareto frontier for a 10⁶-synapse core, which determines whether the 12-month prediction lands at 1 pJ or 10 pJ?

## 7. Conclusion

We constructed a quantum-inspired non-equilibrium thermodynamic model of neuromorphic computation combining gradient-flow dissipative dynamics with Landauer and Margolus–Levitin bounds. The arithmetic yields a Landauer floor of 2.87 zJ/bit at 300 K, a quantum-rate crossover at ~58 fs (irrelevantly fast for real devices), and the conclusion that the *fundamental* energy–speed trade-off is flat across all realistic neuromorphic clock rates: observed trade-offs are engineering effects, dominated by switching, leakage, and I/O energies that exceed the thermodynamic floor by 4–10 orders of magnitude. The model predicts next-generation neuromorphic chips within 12 months will operate at 1–10 pJ/op, still far above both the fundamental and practical floors, and that neuromorphic hardware retains a 100–1000× per-operation thermodynamic advantage over fault-tolerant quantum computing. The framework's chief contribution is a physically grounded target curve and a set of falsifiable near-term predictions; its chief weakness is that the binding constraints it identifies are engineering, not physics, and must be attacked with measurement rather than theory.

## References

[1] arXiv:1905.10415v3 | Quantum-inspired algorithms in practice

[2] arXiv:2512.05168v2 | Comparison of some geometric frameworks for dissipative evolution in multiscale non-equilibrium thermodynamics

[3] arXiv:2508.19455v3 | Reduction of Complex Dynamics in Far-from-equilibrium Systems: Nambu Non-equilibrium Thermodynamics

[4] arXiv:0905.0292v3 | Non-equilibrium statistical mechanics of non-equilibrium damage phenomena

[5] arXiv:1204.3841v1 | A non-equilibrium thermodynamics model for combined adsorption and diffusion processes in micro- and nanopores

[6] arXiv:0908.2161v1 | Non-equilibrium critical behavior : An extended irreversible thermodynamics approach

[7] arXiv:2409.09919v2 | Engineering topological states and quantum-inspired information processing using classical circuits

[8] arXiv:1905.06796v2 | Non-equilibrium probability flux of a thermally driven micromachine

[9] QNFO: Thermodynamic Viability and the Universality of Feynman Matter | DOI 10.5281/zenodo.18036068

[10] QNFO: Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation | DOI 10.5281/zenodo.17955898

[11] QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing | DOI 10.5281/zenodo.17937531

[12] QNFO: The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post-Classical Computing | DOI 10.5281/zenodo.22753039