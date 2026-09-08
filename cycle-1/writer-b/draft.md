# The Energy Floor of Fault-Tolerant Quantum Computing at the 1,000-Logical-Qubit Scale

**Abstract.** We analyze the energy cost of fault-tolerant quantum computing (FTQC) at the 1,000-logical-qubit scale by combining two complementary bounds — the Margolus–Levitin quantum speed limit and the Landauer bound — with an order-of-magnitude engineering estimate for a surface-code-protected superconducting processor. We find that the physical floors are far from binding. The Margolus–Levitin bound permits operation at energies of order 1e-30 J per logical operation at realistic logical clock rates, and the Landauer cost of the classical bookkeeping that quantum error correction necessarily performs is of order 1e-18 to 1e-16 J per logical operation. A defensible practical estimate is instead roughly 0.1–10 J per logical operation — 16 to 18 orders of magnitude above the thermodynamic floors — with the dominant term residing in classical infrastructure: cryogenic control electronics and their cooling overhead. We conclude by proposing a 2026 revision of the joules-per-compute benchmark that normalizes energy per logical qubit-operation and reports a Landauer-overhead ratio, replacing the physical-gate count as the headline metric.

## 1. Introduction

Whether fault-tolerant quantum computing can deliver an *energy* advantage, and not merely an asymptotic computational one, is an open and under-measured question. Machine-level comparisons are typically made in gate counts and wall-clock time, while the joules-per-compute (JPC) benchmark program asks the sharper question: how many joules does one unit of useful computation cost, and how does that number evolve across generations? At the 1,000-logical-qubit scale — the size at which error-corrected machines become candidates for practically interesting workloads — the energy question is inseparable from the error-correction overhead question, because the physical resources that consume energy scale with the *physical* qubit count, not the logical one.

This paper addresses three questions. First, what does the Margolus–Levitin (ML) theorem imply for the minimum energy per logical operation in a fault-tolerant quantum computer, and how does it combine with the Landauer bound? Second, what is a defensible estimate of the total energy per logical operation for a surface-code-protected 1,000-logical-qubit processor, and where is the dominant term? Third, how should the joules-per-compute benchmark be revised in 2026 so that it normalizes energy per logical qubit rather than per physical gate?

A methodological note applies to the whole paper. The environment in which this draft was produced blocked all tool access, so no citation could be verified live. Every bracketed reference is therefore marked [UNVERIFIED - needs parent check]; the parent ensemble must confirm each arXiv ID or DOI before this draft is used further. Every quantitative claim in Section 3 is our own order-of-magnitude estimate with stated assumptions, and is labeled as such. No number has been fabricated; where we do not know, we say so with a range.

## 2. Physical floors: Margolus–Levitin and Landauer

### 2.1 The Margolus–Levitin bound

The ML theorem [UNVERIFIED - needs parent check: N. Margolus and L. B. Levitin, "The maximum speed of dynamical evolution", Physica D 120, 188–195 (1998), arXiv:quant-ph/9710043] states that a quantum system with average energy E (measured relative to its ground state) cannot evolve between two orthogonal states in time shorter than t_min = πħ/(2E). Rearranged, an operation of duration τ requires average energy E ≥ πħ/(2τ). Two structural points matter for our purposes.

First, the ML bound is a *speed limit*, not a fixed energy floor: it couples energy to time, so the minimum energy can be lowered by slowing the operation down. A "floor" in the sense of a time-independent minimum does not follow from ML alone. Second, the magnitudes involved are extremely small at any clock rate envisioned for FTQC. A surface-code logical Clifford gate at code distance d ≈ 30 takes roughly d syndrome cycles, or ≈ 30 μs at a ≈ 1 μs cycle time; the ML floor for such an operation is E ≥ πħ/(2 · 3e-5 s) ≈ 5.5e-30 J (established result; arithmetic verified in this draft). Even a 1 ns gate has a floor of only ≈ 1.7e-25 J. The ML bound is therefore never the binding constraint in any realistic FTQC energy budget: its role is structural, forbidding the "infinitely slow, infinitely cheap" limit of coherent unitary work and bounding the energy-time trade-off if all dissipative overhead were someday eliminated. (A tighter, unified bound on the rate of quantum dynamics is given by Levitin and Toffoli [UNVERIFIED - needs parent check: L. B. Levitin and T. Toffoli, Phys. Rev. Lett. 103, 160502 (2009)]; the tightening does not change our conclusion.)

### 2.2 The Landauer bound

Landauer's principle [UNVERIFIED - needs parent check: R. Landauer, "Irreversibility and heat generation in the computing process", IBM J. Res. Dev. 5(3), 183–191 (1961), DOI 10.1147/rd.53.0183] sets E ≥ kT ln 2 per irreversibly erased bit of information. Computation can in principle be made logically reversible [UNVERIFIED - needs parent check: C. H. Bennett, "Logical reversibility of computation", IBM J. Res. Dev. 17(6), 525–532 (1973), DOI 10.1147/rd.176.0525], but quantum error correction is irreversibly *dissipative by design at the classical level*: every stabilizer measurement projects the register and destroys syndrome information; measurement outcomes, decoder state, digital-to-analog converter resets, and amplifier bias records are all erased classical information. The quantum part of the computation could, in principle, be engineered quasi-reversibly; the classical bookkeeping cannot avoid erasure without abandoning the measurement-feedback structure of QEC itself.

The bit count matters. A distance-d surface-code patch contains roughly 2d² physical qubits (data plus ancilla). Each syndrome round measures of order d² stabilizers, and a logical operation is executed over of order d rounds, so one logical operation erases on the order of d³ to 2d³ classical bits. For d = 30 this is ≈ 3e4–5e4 bits per logical operation. At a 4 K operating stage this costs ≈ (5e4)(3.8e-23 J) ≈ 2e-18 J per logical operation; at room temperature ≈ (5e4)(2.9e-21 J) ≈ 1.5e-16 J (established bound; arithmetic verified in this draft). This is the Landauer floor for the bookkeeping that FTQC inherently performs.

### 2.3 Combining the two bounds

The two bounds combine as

  E_min(logical op) = max( πħ/(2τ) ,  kT ln 2 · N_irr ),

where τ is the logical-operation duration and N_irr the number of irreversibly erased classical bits it entails. For fault-tolerant operation the second term dominates the first by roughly 12–14 orders of magnitude, because error correction erases macroscopic amounts of classical information at nonzero temperature while the coherent evolution itself is near the quantum speed limit. The honest answer to Q1 is therefore: the Margolus–Levitin theorem does *not* set a practical energy floor for FTQC — it is a time–energy trade-off curve that is never the binding constraint — while Landauer, applied to the classical bookkeeping of error correction rather than to the quantum evolution itself, gives a floor of order 1e-18–1e-16 J per logical operation. The striking consequence is that the combined physical floor is ~16–18 orders of magnitude below what any realistic machine will spend (Section 3): the energy floor of fault-tolerant quantum computing is an *engineering* floor, not a physics floor. This is the central message of the paper, and it is the reason the benchmark revision in Section 4 is needed. An open question worth recording: whether any architecture can make syndrome extraction thermodynamically quasi-reversible; current measurement-feedback designs give no indication of it.

## 3. Practical energy at the 1,000-logical-qubit scale

### 3.1 Overhead accounting for the surface code

All estimates in this section are order-of-magnitude, with assumptions stated inline; none are verified against sources (environmental tool block).

The scale-setting quantity is the physical qubit count. At a physical error rate p ≈ 1e-3 — plausibly below threshold, consistent with the below-threshold operation demonstrated at p ≈ 1.4e-3 with distance-7 surface code patches [UNVERIFIED - needs parent check: Google Quantum AI and Collaborators, "Quantum error correction below the surface code threshold", Nature 638, 920–926 (2025), arXiv:2408.13687] — reaching a logical error rate p_L ≈ 1e-12 per operation requires code distance d ≈ 25–35 (our estimate, from the standard exponential-in-d suppression of logical error below threshold). With N_phys = 2d² per logical qubit, 1,000 logical qubits imply N_phys ≈ 1.3–2.4e6 physical qubits (d = 25–35). This single number propagates through every energy term below, because control, wiring, and cooling all scale with physical qubits, while the useful output scales with logical qubits. This d² overhead is precisely what a per-physical-gate benchmark would conceal and a per-logical-operation benchmark would expose.

### 3.2 Energy budget

Table 1 (all rows are our order-of-magnitude estimates):

| Term | Estimate | Basis / assumption |
|---|---|---|
| 1. Delivered quantum dissipation | 1e-6–1e-3 W | Microwave drive ~-60 dBm per qubit, duty-cycled; absorbed drive power, negligible by design |
| 2. Cryogenic control electronics at 3–4 K | ≈ 9 kW at 3–4 K | 1–10 mW per physical-qubit channel × 1.8e6 qubits; cryo-CMOS controllers have demonstrated <2 mW per output at 3 K [UNVERIFIED: J. C. Bardin et al., IEEE J. Solid-State Circuits 54(11), 3043–3060 (2019), DOI 10.1109/JSSC.2019.2937234] |
| 3. Cooling the 3–4 K stage | 3–20 MW wall | 300–1000 W wall per W lifted at 4 K (Carnot factor 75, realized 10–25%); pulse-tube coolers deliver ~1.35 W at 4.2 K for ~7–9 kW input [UNVERIFIED: S. Krinner et al., "Engineering cryogenic setups for 100-qubit scale superconducting circuit systems", EPJ Quantum Technol. 6, 2 (2019), arXiv:1806.07862] |
| 4. mK-stage thermal load of control wiring | 0.3–3 MW wall | ~N_phys lines × 0.1–1 μW per line → 0.2–2 W at 20 mK; Carnot factor 300/0.02 ≈ 1.5e4, realized 1–10% |
| 5. Real-time decoding | 1 kW–1 MW | Syndrome traffic ≈ N_L·d² per μs ≈ 1e12 bits/s; 1–100 pJ/bit for classical decoders [UNVERIFIED: P. Das et al., "A scalable decoder micro-architecture for fault-tolerant quantum computing", arXiv:2001.06598] |
| 6. Readout amplification (HEMTs/paramps at 4 K) | 10–100 W wall | mW-scale cryogenic dissipation × cooling overhead; small relative to rows 2–4 |
| **Total** | **≈ 10–50 MW wall (midpoint ≈ 20 MW)** | Sum of ranges |

### 3.3 Energy per logical operation and the dominant term

Throughput: a logical Clifford gate costs of order d syndrome cycles ≈ 30 μs; with pipelining and realistic parallelism overheads (lattice surgery, routing), an effective 3–30 kHz of logical operations per logical qubit is defensible, giving 3e6–3e7 logical operations per second across 1,000 logical qubits. Dividing the wall-power range by this throughput range gives **0.1–10 J per logical operation, with an order-of-magnitude midpoint of ≈ 1 J** (our estimate). The answer to Q2: the dominant term is the cryogenic control electronics plus the cooling needed to remove their heat — classical infrastructure, rows 2–4 of Table 1. The delivered quantum dissipation (row 1) is negligible by 9–12 orders of magnitude; the decoder (row 5) is significant but secondary. The gap to the Landauer floor of Section 2.2 is ≈ 1e16–1e18 — the machine spends roughly 10^16 times more energy than thermodynamics requires for the information it erases. For scale: a modern GPU or CPU delivers of order 1e-13–1e-10 J per floating-point operation, so one logical operation of a 1,000-logical-qubit machine at today's extrapolated engineering costs roughly 1e10–1e13 times more energy than one classical FLOP (with the important caveat that the operations are not interchangeable units; the gap is nonetheless the single most important number any benchmark of this technology must expose and track).

## 4. Revising the joules-per-compute benchmark (2026)

Q3 asks for the revision. Six concrete proposals:

1. **Headline metric: J/QLOP** — joules per logical operation, normalized per logical qubit, at a *declared* logical error rate p_L and code distance d. Reporting energy without the fidelity operating point is as meaningless as reporting a classical result without precision.
2. **Sustained companion: J per logical qubit-second**, plus throughput in QLOP/s. This catches idle power, duty cycle, and the cost of simply *holding* 1,000 logical qubits alive — which at ~10 kW per logical qubit of wall power is not a rounding error.
3. **Efficiency index: the Landauer-overhead ratio** η = E_actual / (kT ln 2 · N_irr). For our Section 3 estimate, η ≈ 1e16–1e18. This ratio should *fall* across generations and across vendors; it is the honest measure of how far the technology is from its physical floor and gives the benchmark a theory-anchored, technology-neutral yardstick.
4. **Mandatory five-way cost breakdown**: (a) delivered quantum drive, (b) control electronics, (c) cooling by temperature stage, (d) classical decoding, (e) other infrastructure. Without the breakdown, J/QLOP is a black box that cannot be audited or improved.
5. **Demote the physical-gate count to secondary context.** The physical-gate count conflates the d² code-overhead scaling with genuine progress: a machine with a worse decoder and higher p needs a larger d and reports *more* physical gates at the same logical fidelity, which a per-physical-gate benchmark perversely rewards. Normalizing per logical operation rewards exactly the improvements — better decoders, lower physical error rates, smaller code distances — that reduce energy.
6. **Report across an error-rate ladder** (p_L ∈ {1e-9, 1e-12, 1e-15}) so that systems at different logical-fidelity operating points are not compared as if equivalent.

The physical-gate count does not disappear: it remains reported as overhead context (N_phys, d, cycle time), which is where its information content lives.

## 5. Falsifiability and limitations

Concrete observations that would falsify or materially move the estimate: (i) if cryo-CMOS per-channel power falls to ~μW, or photonic/optical control links eliminate cryogenic control electronics [UNVERIFIED - needs parent check: F. Lecocq et al., "Control and readout of a superconducting qubit using a photonic link", Nature 591, 575–579 (2021)], rows 2–4 of Table 1 collapse and the estimate drops by 1–2 orders of magnitude; (ii) if decoder efficiency falls below ~1 pJ/bit, row 5 becomes negligible; (iii) if cooling efficiency approaches 10% of Carnot at millikelvin temperatures, row 4 drops by an order; conversely, (iv) if magic-state distillation serializes throughput, the effective energy per *useful* logical operation could rise 10–100× above our midpoint; and (v) the entire Section 3 assumes a superconducting surface-code platform — trapped-ion machines (lasers, no millikelvin cryogenics) and photonic fusion-based architectures have materially different dominant terms, and no number here transfers to them. Every quantity in Section 3 is an order-of-magnitude estimate; the only results stated with high confidence are the physics floors of Section 2, which are also the least decision-relevant. The most important limitation is integrity-related: all citations are unverified due to a tool-access block, and the parent ensemble must verify each before external use.

## 6. Conclusion

The energy floor of fault-tolerant quantum computing at the 1,000-logical-qubit scale is not a physics bound — the Margolus–Levitin and Landauer limits combine to roughly 1e-18–1e-16 J per logical operation — but an engineering reality: order 0.1–10 J per logical operation, dominated by cryogenic control electronics and their cooling overhead, roughly 10^16 times above the thermodynamic floor. The consequence for the joules-per-compute benchmark is direct: measure joules per logical operation at declared fidelity, expose the Landauer-overhead ratio, and make the physical-gate count a footnote where it belongs.

## References

All entries unverified due to tool-access block; parent ensemble must confirm each ID/DOI.

1. N. Margolus and L. B. Levitin, "The maximum speed of dynamical evolution", Physica D 120, 188–195 (1998). arXiv:quant-ph/9710043. [UNVERIFIED]
2. R. Landauer, "Irreversibility and heat generation in the computing process", IBM J. Res. Dev. 5(3), 183–191 (1961). DOI 10.1147/rd.53.0183. [UNVERIFIED]
3. C. H. Bennett, "Logical reversibility of computation", IBM J. Res. Dev. 17(6), 525–532 (1973). DOI 10.1147/rd.176.0525. [UNVERIFIED]
4. Google Quantum AI and Collaborators, "Quantum error correction below the surface code threshold", Nature 638, 920–926 (2025). arXiv:2408.13687. [UNVERIFIED]
5. Google Quantum AI, "Suppressing quantum errors by scaling a surface code logical qubit", Nature 614, 676–681 (2023). arXiv:2207.06431. [UNVERIFIED]
6. M. Fellous-Asiani, J. H. Chai, R. S. Whitney, A. Auffèves, H. K. Ng, "Limitations in Quantum Computing from Resource Constraints", PRX Quantum 2, 040335 (2021). arXiv:2007.01966. [UNVERIFIED]
7. S. Krinner et al., "Engineering cryogenic setups for 100-qubit scale superconducting circuit systems", EPJ Quantum Technol. 6, 2 (2019). arXiv:1806.07862. [UNVERIFIED]
8. P. Das, C. A. Pattison, S. Manne, D. Carmean, K. Svore, M. Qureshi, N. Delfosse, "A scalable decoder micro-architecture for fault-tolerant quantum computing", arXiv:2001.06598. [UNVERIFIED]
9. J. C. Bardin et al., "Design and characterization of a 28-nm bulk-CMOS cryogenic quantum controller dissipating less than 2 mW at 3 K", IEEE J. Solid-State Circuits 54(11), 3043–3060 (2019). DOI 10.1109/JSSC.2019.2937234. [UNVERIFIED]
10. B. Patra et al., "Cryo-CMOS circuits and systems for quantum computing applications", IEEE J. Solid-State Circuits 53(1), 309–321 (2018). DOI 10.1109/JSSC.2017.2737549. [UNVERIFIED]
11. L. B. Levitin and T. Toffoli, "Fundamental limit on the rate of quantum dynamics: the unified bound is tight", Phys. Rev. Lett. 103, 160502 (2009). [UNVERIFIED]
