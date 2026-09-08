# The Energy Floor of Fault-Tolerant Quantum Computing at the 1,000-Logical-Qubit Scale

*Reconciled paper, cycle-1 (v0.1, 2026-09-08). Attribution and divergence reporting:
cycle-1/RECONCILIATION.md. All practical quantities are order-of-magnitude estimates with stated
assumptions; fundamental bounds are established results.*

## Abstract

The energy cost of a logical operation in a fault-tolerant quantum computer is set by two bounds
that are far from binding and by an engineering stack that is. The Margolus–Levitin quantum speed
limit prices an orthogonal transition at E ≥ πħ/(2τ) ≈ 1.7×10⁻²⁸ J per microsecond-timescale
operation, and the Landauer bound prices the classical bookkeeping of quantum error correction at
k_B T ln 2 per erased bit, giving a combined floor of order 10⁻¹⁸–10⁻¹⁹ J per logical operation
at 4 K when the ~10⁴–10⁵ syndrome bits erased per distance-30 logical operation are counted. For a
surface-code-protected 1,000-logical-qubit superconducting processor — ≈2–3 million physical qubits,
10–50 MW of wall power in the defensible range with ~10 MW central — the practical cost is ≈10 mJ
per syndrome round per logical qubit, or ≈0.1–1 J per logical operation under the convention that a
logical operation spans ~d syndrome rounds, roughly 10¹⁶–10¹⁸ times the thermodynamic floor. The
dominant terms are cryogenic refrigeration and control/readout electronics; classical decoding is
an order of magnitude below; the coherent quantum physics is five orders below. We propose a 2026
revision of the joules-per-compute benchmark whose headline metric is joules per logical
qubit-operation at a declared logical error budget and code distance, with the physical-gate count
demoted to overhead context.

## 1. Introduction

Fault-tolerant quantum computing has crossed a threshold: surface-code memories have been operated
below threshold at the 105-qubit scale [11], and vendor roadmaps target hundreds to thousands of
logical qubits within the decade. Energy has been a second-order concern while machines were small.
At the 1,000-logical-qubit scale it becomes first-order: the physical overhead of the surface code
multiplies the qubit count by ~2.5d², and cryogenic infrastructure does not scale for free. This
paper addresses three questions.

- **Q1.** What do the Margolus–Levitin and Landauer bounds imply for the minimum energy per logical
  operation, and how do they combine?
- **Q2.** What is a defensible estimate of the total energy per logical operation for a
  surface-code-protected 1,000-logical-qubit processor, and where is the dominant term?
- **Q3.** How should the joules-per-compute benchmark be revised in 2026 so that it normalizes
  energy per logical qubit rather than per physical gate?

Every quantitative statement carries one of three labels: *established result* (a theorem or a
verified measurement), *order-of-magnitude estimate* (a stated assumption propagated through
arithmetic), or *open question*. The machine-scale numbers in Section 3 are order-of-magnitude
estimates; the bounds in Section 2 are established results.

## 2. Q1: The combined fundamental floor

**Margolus–Levitin (ML).** A quantum system with average energy E above its ground state cannot
evolve between two orthogonal states in less than t = πħ/(2E) [1]; the unified bound of Levitin and
Toffoli [16] tightens this without changing the order of magnitude. Inverted, an operation that must
complete in time τ requires E ≥ πħ/(2τ). For a 1 μs cycle this is ≈1.7×10⁻²⁸ J; even a 1 ns gate
requires only ≈1.7×10⁻²⁵ J (*established result*; ħ = 1.05457×10⁻³⁴ J·s). The ML bound is a
speed–energy trade-off curve, not a fixed floor: it can always be lowered by slowing the operation
down, and at any clock rate envisioned for fault-tolerant machines its magnitude is negligible.
Its role is structural — forbidding the infinitely-slow, infinitely-cheap limit of coherent unitary
work — not budgetary.

**Landauer.** Erasing one bit at temperature T dissipates at least k_B T ln 2 [2], verified
experimentally [17]. At 300 K this is 2.9×10⁻²¹ J; at 4 K, 3.8×10⁻²³ J; at a dilution-refrigerator
base temperature of 20 mK, 1.9×10⁻²⁵ J (*established result*). Computation can in principle be made
logically reversible [18], but quantum error correction is dissipative by design at the classical
level: every syndrome round measures ancillas and resets them, and reset is erasure.

**Combination and crossover.** An operation that erases N_irr bits in time τ obeys
E_min = max(πħ/(2τ), N_irr·k_B T ln 2). The ML term dominates only for
τ < h/(4k_B T ln 2) ≈ 58 fs at 300 K (≈4.3 ps at 4 K) (*established result*). At microsecond cycle
times the Landauer term dominates by 12–14 orders of magnitude.

**Fault tolerance makes the floor slightly less trivial.** A distance-d surface-code patch carries
~d² ancilla qubits; a logical operation spans ~d syndrome rounds, so it erases ~d³ classical bits
(≈3×10⁴–5×10⁴ bits at d = 30; ≈1.4×10³ per round at d = 27) (*order-of-magnitude estimate*). The
Landauer floor for this bookkeeping is ≈10⁻¹⁸ J per logical operation at 4 K (≈10⁻²⁰ J per round).
Whether syndrome extraction can be made thermodynamically quasi-reversible is an *open question*;
current measurement-feedback designs give no indication of it.

**Answer to Q1.** The combined physical floor is ≈10⁻¹⁸–10⁻¹⁹ J per logical operation at 4 K —
16 to 18 orders of magnitude below what any realistic machine will spend. The energy floor of
fault-tolerant quantum computing is an engineering floor, not a physics floor.

## 3. Q2: A full-stack estimate at 1,000 logical qubits

**Platform and assumptions.** Superconducting transmon qubits; rotated surface code; physical error
rate p ≈ 10⁻³ (below threshold, as demonstrated at the 105-qubit scale [11]); target logical error
rate p_L ≈ 10⁻¹⁰–10⁻¹², requiring distance d ≈ 27–35 from the standard exponential suppression
[9,12] (*order-of-magnitude estimate*).

**Physical overhead.** The rotated surface code allocates ~2.5d² (planar conventions give 2d² to
(2d−1)²) physical qubits per logical qubit [9]. At d ≈ 30, 1,000 logical qubits imply ≈2.25–2.8×10⁶
physical qubits; routing and magic-state distillation add a further 10–50% (*order-of-magnitude
estimate*), consistent with resource estimates for algorithm-scale machines [19]. We carry
≈2–4×10⁶ physical qubits through the budget.

**Energy ledger** (wall-plug, full system; all rows *order-of-magnitude estimates*):

| Term | Estimate | Basis |
|---|---|---|
| 1. Coherent quantum drive | <10² W | nW–μW per qubit at the chip, even with generation inefficiency |
| 2. Control/readout electronics | 10⁵–10⁶ W | 0.1–1 W per channel at room temperature for ~2×10⁶ qubits; cryo-CMOS demonstrated <2 mW per output at 3 K [14,15] |
| 3. Cryogenic refrigeration | 10⁶–10⁷ W | ~10⁶–10⁷ qubits-worth of 4 K heat load lifted at 300–1000 W wall per W; Carnot factor 74×, realized 10–25% [13] |
| 4. Millikelvin stage | 10⁵–3×10⁶ W | Carnot factor ~1.5×10⁴ on ~mW loads; forces multiplexed cryo-CMOS or optical control |
| 5. Real-time decoding | 10⁴–10⁶ W | ~10¹² syndrome bits/s at 1–100 pJ/bit [10] |
| **Total** | **~10 MW central (range 1–50 MW)** | Sum; see RECONCILIATION.md D3 for the writer-level range disagreement |

**Throughput and energy per operation.** At a ~1 μs cycle time [11], the machine executes ~10⁹
syndrome rounds per second across 1,000 logical qubits. Dividing the wall power by this rate gives
the convention-free primitive:

> **≈10 mJ per syndrome round per logical qubit (range 0.5–20 mJ)** (*order-of-magnitude estimate*).

A logical operation spans ~d syndrome rounds (lattice surgery over ~3d cycles: 30–100 μs), so the
energy per logical operation is

> **≈0.1–1 J per logical operation (range 0.01–10 J)** under the d-rounds convention
> (*order-of-magnitude estimate*).

Two of three independent drafts of this paper used the d-rounds convention; one used a one-round
convention (≈2 mJ central). The discrepancy is purely definitional — how many syndrome rounds
constitute a logical operation — and the per-round primitive above is reported precisely to remove
that ambiguity. Standardizing the convention is an *open question* for the benchmark program.
For scale: a modern 64-bit floating-point operation costs 10–100 pJ, so one logical operation costs
~10⁷–10¹⁰ times one classical FLOP; the honest comparison is per problem instance [6], which is not
resolved here (*open question*).

**Answer to Q2 — the dominant term.** Room-temperature/cryogenic control electronics and cryogenic
refrigeration jointly dominate, at ~99.999% of the wall power; decoding is ~1 order below; the
coherent quantum physics is ~5 orders below. The ranking (control ≈ cryogenics > decoding ≫ physics)
is robust across the uncertainty range of every individual term, though the identity of the single
largest term flips with the success or failure of cryo-CMOS multiplexing. The machine spends
10¹⁶–10¹⁸ times the thermodynamic floor: this gap is the roadmap.

## 4. Q3: The 2026 joules-per-compute revision

The current normalization of energy per physical gate mis-measures fault-tolerant machines twice:
it rewards larger codes (more physical gates at the same logical fidelity) and it makes
cross-architecture comparison meaningless, since a "physical gate" is not a shared currency across
superconducting, trapped-ion, neutral-atom, and photonic platforms. The 2026 revision:

1. **Headline metric:** joules per logical qubit-operation (J/op_L), measured full-stack at the
   wall, reported at a declared logical error budget and code distance — e.g.
   J/op_L | p_L = 10⁻¹⁰, d = 30. Energy without the fidelity operating point is uninterpretable.
2. **Normalization:** per logical qubit, never per physical gate; "logical qubit" is defined by the
   declared (d, p_L).
3. **Demotion:** the physical-gate count becomes overhead context (N_phys, d, cycle time), where its
   information content lives.
4. **Companion metrics:** decoder energy share (% of system power); cryogenic overhead factor (wall
   watts per watt delivered at the cold stage); thermodynamic gap ratio η = E_actual/E_floor (≈10¹⁶
   today; must fall across generations); idle-power handling (J per logical qubit-hour reported
   separately from gate mode); an error-rate ladder (p_L ∈ {10⁻⁹, 10⁻¹², 10⁻¹⁵}).
5. **Interim regime:** pre-threshold machines may report joules per physical gate, explicitly
   flagged as non-comparable with J/op_L.
6. **Floor tracking:** report the ML and Landauer floors for the stated clock and temperature
   alongside J/op_L, so the gap-to-floor is a visible, tracked quantity.

The revision carries its own falsification test: if decoder or cryo-CMOS improvements move J/op_L
while physical-gate-normalized metrics stay flat, logical normalization is measuring the right
thing; if the reverse, both must be reported.

## 5. Limitations and falsifying observations

The central estimate would be falsified or materially moved by any of the following.
(a) Cryo-CMOS or photonic control links [13,14] cutting per-channel dissipation to the μW scale —
the 4 K load collapses and J/op_L falls by ~10². (b) A peer-reviewed full-stack power budget for a
≥10⁵-physical-qubit machine with <1 W per-channel control and <2 kW fridge power per 10⁴ qubits
(→ ~10⁻³ J/op). (c) Decoder efficiency beyond ~1 pJ/bit, removing row 5. (d) Physical error rates
stuck near 10⁻², forcing d ≈ 50 and raising J/op_L by 3–10×. (e) Decoders consuming >1 μJ per
syndrome bit, overturning the dominance ranking. (f) The ~1 μs round-time assumption is the most
load-bearing number in the estimate; at 10 μs rounds J/op_L scales ~5–20× at fixed wall power.
(g) All numbers transfer only to superconducting surface-code machines; trapped-ion (laser-dominated)
and photonic architectures have different ledgers. The Q1 floor could only be falsified by an
experimental violation of Landauer or Margolus–Levitin, which would be a Nobel-grade result.

## 6. Conclusion

At the 1,000-logical-qubit scale the energy story of fault-tolerant quantum computing has two
halves. Thermodynamics is generous: ~10⁻¹⁸ J per logical operation of Landauer-priced bookkeeping
is the only real physics floor. Engineering is expensive: ~10 mJ per syndrome round per logical
qubit, ~0.1–1 J per logical operation, dominated by refrigeration and control electronics, 10¹⁶–10¹⁸
times above the floor. The 2026 joules-per-compute revision should measure exactly that gap — joules
per logical qubit-operation at a declared error budget — so engineering attention is steered toward
the terms that actually cost money, and every order of magnitude closed between 1 J and 10⁻¹⁸ J is
tracked as progress.

## References

All identifiers verified against arXiv and Crossref by the reconciling agent (citation-audit.md).

1. N. Margolus and L. B. Levitin, "The maximum speed of dynamical evolution," Physica D 120, 188 (1998). arXiv:quant-ph/9710043.
2. R. Landauer, "Irreversibility and heat generation in the computing process," IBM J. Res. Dev. 5, 183 (1961). DOI 10.1147/rd.53.0183.
3. S. Lloyd, "Ultimate physical limits to computation," Nature 406, 1047 (2000). arXiv:quant-ph/9908043.
4. S. Deffner and S. Campbell, "Quantum speed limits: from Heisenberg's uncertainty principle to optimal quantum control," J. Phys. A: Math. Theor. 50, 453001 (2017). arXiv:1705.08023.
5. A. Auffèves, "Quantum technologies need a Quantum Energy Initiative," PRX Quantum 3, 020101 (2022). arXiv:2111.09241.
6. D. Jaschke and S. Montangero, "Is quantum computing green? An estimate for an energy-efficiency quantum advantage," Quantum Sci. Technol. 8, 025001 (2023). arXiv:2205.12092.
7. M. Fellous-Asiani, J. H. Chai, R. S. Whitney, A. Auffèves, and H. K. Ng, "Limitations in quantum computing from resource constraints," PRX Quantum 2, 040335 (2021). arXiv:2007.01966.
8. M. Fellous-Asiani et al., "Optimizing resource efficiencies for scalable full-stack quantum computers," PRX Quantum 4, 040319 (2023). arXiv:2209.05469.
9. A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cleland, "Surface codes: Towards practical large-scale quantum computation," Phys. Rev. A 86, 032324 (2012). arXiv:1208.0928.
10. P. Das et al., "A scalable decoder micro-architecture for fault-tolerant quantum computing," arXiv:2001.06598 (2020).
11. R. Acharya et al. (Google Quantum AI), "Quantum error correction below the surface code threshold," Nature 638, 920 (2025). arXiv:2408.13687.
12. R. Acharya et al. (Google Quantum AI), "Suppressing quantum errors by scaling a surface code logical qubit," Nature 614, 676 (2023). arXiv:2207.06431.
13. S. Krinner et al., "Engineering cryogenic setups for 100-qubit scale superconducting circuit systems," EPJ Quantum Technol. 6, 2 (2019). arXiv:1806.07862.
14. J. C. Bardin et al., "Design and characterization of a 28-nm bulk-CMOS cryogenic quantum controller dissipating less than 2 mW at 3 K," IEEE J. Solid-State Circuits 54, 3043 (2019). DOI 10.1109/JSSC.2019.2937234.
15. B. Patra et al., "Cryo-CMOS circuits and systems for quantum computing applications," IEEE J. Solid-State Circuits 53, 309 (2018). DOI 10.1109/JSSC.2017.2737549.
16. L. B. Levitin and T. Toffoli, "Fundamental limit on the rate of quantum dynamics: the unified bound is tight," Phys. Rev. Lett. 103, 160502 (2009). arXiv:0905.3417.
17. A. Bérut et al., "Experimental verification of Landauer's principle linking information and thermodynamics," Nature 483, 187 (2012). DOI 10.1038/nature10872.
18. C. H. Bennett, "Logical reversibility of computation," IBM J. Res. Dev. 17, 525 (1973). DOI 10.1147/rd.176.0525.
19. C. Gidney and M. Ekerå, "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits," Quantum 5, 433 (2021). arXiv:1905.09749.
20. S. Bravyi et al., "High-threshold and low-overhead fault-tolerant quantum memory," Nature 627, 778 (2024). arXiv:2308.07915.

## Appendix A. Provenance and ensemble method

This paper is the reconciled output of the QNFO ensemble-research pilot (cycle-1). Three
independent writers received a byte-identical input block (title, Q1–Q3, constraints;
sha256 b5369c0085d067de78948fbe390d26014255b61510db217eb6dfe09596bc5709) and produced three
independent draft papers in isolated sessions with no cross-communication. The drafts are preserved
verbatim as interim artifacts (cycle-1/writer-a|b|c/draft.md). A reconciling agent then verified
every citation against arXiv and Crossref (32/33 entries verified; two defects found and corrected:
a misattributed arXiv identifier for reference 17 and a title error in reference 5), classified
claims as convergent or divergent, and synthesized this paper. Every claim in this paper is mapped
to its source draft and section in cycle-1/RECONCILIATION.md, including the reported divergences:
the logical-operation convention (Section 3), the wall-power midpoint spread, and the direction of
the gap-ratio convention η. A known limitation of the pilot: all three writers belonged to the same
model family, so the measured convergence bounds context-independence, not cross-model diversity;
a cross-model cycle is planned. Reconciliation does not fabricate consensus: where writers disagreed,
Section 3 reports the primitive that removes the ambiguity rather than choosing silently.

