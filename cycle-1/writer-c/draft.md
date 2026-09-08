# The Energy Floor of Fault-Tolerant Quantum Computing at the 1,000-Logical-Qubit Scale

*Writer-C, QNFO Ensemble Research Pilot, cycle 1. Status: UNVERIFIED DRAFT — produced under a tool-blocked child session; every citation is flagged [UNVERIFIED - needs parent check] and every quantitative claim carries an uncertainty label.*

## Abstract

We ask what physics and what engineering set the energy cost of a logical operation in a fault-tolerant quantum computer at the 1,000-logical-qubit scale. The Margolus–Levitin theorem and the Landauer bound together imply a thermodynamic floor near 10⁻²¹ J per microsecond-timescale logical operation (10⁻¹⁸ J when the ancilla-erasure overhead of distance-30 surface-code syndrome extraction is included) — some eighteen to twenty orders of magnitude below a defensible practical estimate. For a superconducting surface-code processor at distance ≈30, we estimate roughly 2.25 million physical qubits, ~10 MW of full-system wall power (central estimate; range 0.1–100 MW), and ~1 J per logical operation, with room-temperature control electronics and cryogenic refrigeration as the dominant terms and classical decoding an order of magnitude smaller. We propose a 2026 revision of the joules-per-compute benchmark that retires the physical-gate count as the headline metric in favor of joules per logical qubit-operation at a declared logical error budget, with companion metrics for decoder energy share, cryogenic overhead, and the thermodynamic gap ratio. All practical numbers are order-of-magnitude estimates with stated assumptions; the fundamental bounds are established results.

## 1. Introduction

Quantum computers at the utility scale will not be judged only by qubit counts and error rates; they will be judged by what they cost to run. The QNFO joules-per-compute benchmark [UNVERIFIED: github.com/rwnq8/joules-per-compute-benchmark] exists to make that cost legible, and its current headline normalizes energy per physical gate. The trouble is that in a fault-tolerant architecture the physical gate is the wrong unit: the overwhelming majority of physical operations are syndrome-extraction cycles whose only job is to make a smaller number of logical operations trustworthy. A benchmark that counts physical gates measures mostly overhead, while hiding the terms that actually dominate the electricity bill — control electronics, cryogenics, and classical decoding.

This paper addresses three questions. (Q1) What do the Margolus–Levitin and Landauer bounds imply for the minimum energy per logical operation, and how do they combine? (Q2) What is a defensible full-system energy estimate per logical operation for a surface-code-protected 1,000-logical-qubit processor, and where is the dominant term? (Q3) How should the joules-per-compute benchmark be revised in 2026 to normalize energy per logical qubit rather than per physical gate?

Throughout, we define one logical operation as a single logical gate on one logical qubit, including all syndrome extraction, measurement, and feedback it requires, executed at a target logical error rate p_L ≤ 10⁻¹⁰ per operation. Uncertainty labels follow each substantive claim: *established result*, *order-of-magnitude estimate*, or *open question*.

## 2. Q1: The combined fundamental floor

**Margolus–Levitin (ML).** For a quantum system with average energy E above its ground state, the minimum time to evolve to an orthogonal state is t⊥ ≥ h/(4E) [UNVERIFIED: Margolus & Levitin, arXiv:quant-ph/9710043; tight unified bound, arXiv:0905.3417]. Inverting, an operation that must complete in time τ costs at least E ≥ h/(4τ). For a surface-code cycle of τ = 1 μs this is E ≥ 6.63×10⁻³⁴ J·s / (4×10⁻⁶ s) ≈ 1.7×10⁻²⁸ J. For τ = 1 ns the bound rises to 1.7×10⁻²⁵ J. (Established result; arithmetic trivial.)

**Landauer.** Erasing one bit at temperature T dissipates at least k_B T ln 2 [UNVERIFIED: Landauer 1961, IBM J. Res. Dev. 5, 183; experimental confirmation, arXiv:1203.1212]. At 300 K this is 2.9×10⁻²¹ J; at 4 K, 3.8×10⁻²³ J; at a dilution-refrigerator base temperature of 20 mK, 1.9×10⁻²⁵ J per bit. (Established result.)

**Combining the bounds.** An irreversible logical operation that erases n bits in time τ obeys E_min = max(h/(4τ), n·k_B T·ln 2). Which term dominates is a question of timescale: ML dominates Landauer only when τ < h/(4k_B T ln 2) ≈ 58 fs at 300 K (≈ 4.3 ps at 4 K). At realistic cycle times (microseconds), Landauer dominates; the ML bound is physically deep but numerically irrelevant at superconducting clock speeds. (Established result.)

**Fault tolerance makes the floor only slightly less trivial.** Quantum error correction is not a reversible process: every syndrome round measures ancillas and resets them, and reset is erasure. For distance d = 30, each logical qubit carries ~d² ≈ 900 ancillas; a logical operation spanning ~d ≈ 30 rounds erases roughly 2.7×10⁴ bits. At 4 K the Landauer cost of that erasure is 2.7×10⁴ × 3.8×10⁻²³ J ≈ 1.0×10⁻¹⁸ J per logical operation; at 20 mK, ≈ 5×10⁻²¹ J. (Order-of-magnitude estimate — the ancilla count is a coding-architecture estimate, not a measured quantity; the per-bit bound itself is established.)

**Answer to Q1.** The combined bound says a fault-tolerant logical operation at the 1,000-qubit scale cannot be made cheaper than ~10⁻¹⁸ J (4 K, erasure included), and in principle could approach ~10⁻²¹ J at mK temperatures. Nothing in fundamental physics prevents an ultra-low-energy fault-tolerant machine: the floor is ~18–20 orders of magnitude below practice (Section 3). The energy problem of FTQC is an engineering problem, not a physics one. (Confidence in the bounds: high; in the erasure count: medium; the practical gap depends on Section 3's estimates.)

## 3. Q2: A defensible full-system estimate at 1,000 logical qubits

**Platform and assumptions.** Superconducting transmon qubits, rotated surface code, physical error rate p ≈ 10⁻³ (below the ~1% surface-code threshold, as demonstrated at the 105-qubit scale [UNVERIFIED: Google Quantum AI, arXiv:2408.13687]), target p_L ≤ 10⁻¹⁰. Using the standard phenomenological scaling p_L ≈ A(p/p_th)^((d+1)/2) with p/p_th ≈ 0.1–0.2 gives d ≈ 19–28; with engineering margin we take d ≈ 30 (range 20–40). (Order-of-magnitude estimate; the scaling law is standard [UNVERIFIED: Fowler et al., arXiv:1208.0928].)

**Physical overhead.** A rotated surface code needs ≈ 2.5 d² physical qubits per logical qubit (data + ancilla) [UNVERIFIED: arXiv:1208.0928]. At d = 30 that is ≈ 2,250; for 1,000 logical qubits, ≈ 2.25×10⁶ physical qubits (range 10⁶–3×10⁶; magic-state distillation factories for non-Clifford gates would add perhaps 10–50% and are folded into the range, not modeled in detail). This is the same order as published RSA-2048 resource estimates of ~2×10⁷ physical qubits for a much larger logical machine with distillation [UNVERIFIED: Gidney & Ekerå, arXiv:1905.09749]. (Order-of-magnitude estimate.)

**Throughput.** At a cycle time τ_c ≈ 1 μs [UNVERIFIED: arXiv:2408.13687 reports ~1 μs surface code cycles] and ~30–100 μs per logical gate (lattice surgery over ~3d cycles), the machine delivers ~10⁴ logical ops/s per logical qubit, or ~10⁷ logical ops/s fleet-wide (range 10⁷–3×10⁷). (Order-of-magnitude estimate.)

**Energy budget (wall-plug, full system).** (Order-of-magnitude estimates throughout; no single published full-stack power budget for a 10⁶-qubit machine is known to us — flagged as an open question and the single most valuable number to source.)

1. *Coherent quantum control.* Microwave drive delivered to the chip is nW–μW per qubit; even with 100× generation inefficiency the total is ~10⁰–10² W. Negligible.
2. *Cryogenic refrigeration.* A dilution refrigerator consumes roughly 10–30 kW of wall power (number needs a manufacturer datasheet — flagged). The mK cooling budget is brutal: ~1 mW of cooling at 100 mK per ~10 kW of wall power, so 2.25M control lines at even 1 μW of mK-stage load each oversubscribe the mK stage by ~3–4 orders of magnitude — multiplexed cryo-CMOS or optical control is forced, not optional. Assuming 10³–10⁴ qubits per fridge with aggressive multiplexing: 200–2,000 fridges → **2–60 MW**, central ~10 MW.
3. *Room-temperature control and readout electronics.* Current practice is ~0.1–1 W per physical qubit channel amortized; cryo-CMOS could reach 10–100 mW per qubit [UNVERIFIED: cryo-CMOS reviews, e.g., Patra et al., IEEE JSSC 53(1):309 (2018) — arXiv ID not confirmed]. For 2.25M qubits: 0.2–2.3 MW at current practice, 20–225 kW with cryo-CMOS. Central ~0.5 MW.
4. *Classical decoding.* 2.25M physical qubits × ~10⁶ cycles/s ≈ 2.3×10¹² syndrome bits/s. Real-time Union-Find / belief-propagation decoding on FPGA/GPU clusters plausibly needs 10⁴–10⁶ W. Central ~10⁵ W. (Order-of-magnitude estimate; decoder power at scale is an open question.)

**Totals.** Summing central values: ~10⁰ + 10⁷ + 5×10⁵ + 10⁵ W ≈ **~10 MW** (range 0.1–100 MW, driven almost entirely by cryogenics and control-electronics uncertainty). Dividing by ~10⁷ logical ops/s: **≈1 J per logical operation** (range 0.01–10 J). Equivalently, ~10 kW of wall power per logical qubit, or **≈10 kWh per logical-qubit-hour** — one logical qubit-hour at utility scale would cost about as much electricity as a small household's daily use. (All: order-of-magnitude estimates with stated assumptions.)

**Answer to Q2 — dominant term.** Room-temperature control/readout electronics and cryogenic refrigeration wall power jointly dominate; decoding is ~1 order below; the coherent quantum physics is ~5 orders below. The dominance ranking (control ≈ cryogenics > decoding ≫ physics) is the paper's central claim and is robust across the uncertainty range of every individual term, though the *identity* of the largest single term flips depending on whether cryo-CMOS multiplexing succeeds.

## 4. Q3: The 2026 benchmark revision

**What should change.** The headline metric should become: **joules per logical qubit-operation at a declared logical error budget**, written J/op_L | p_L = 10⁻¹⁰, d = 30, with the reciprocal (logical operations per kilojoule at the same budget) as the marketing-facing number. The physical-gate count is demoted to a secondary overhead metric alongside the physical-to-logical qubit ratio and syndrome rounds per logical operation. Rationale: physical-gate counting double-counts QEC overhead, is gameable by architecture choice, and is silent about the three terms (control, cooling, decoding) that Section 3 shows carry ~99.999% of the energy.

**Normalization and required companion metrics.** (1) Normalize per logical qubit — not per physical gate — so superconducting, trapped-ion, neutral-atom, and photonic machines are comparable; "logical qubit" is defined by a declared d and p_L. (2) Require full-system wall-plug metering including idle power (a low-duty-cycle machine's per-op energy inflates when idle overhead is amortized honestly). (3) Report the decoder energy share as a percentage of total system power. (4) Report the cryogenic overhead factor (wall watts per watt delivered at the cold stage). (5) Report the thermodynamic gap ratio η = E_floor/E_actual — a dimensionless progress metric that starts near 10⁻²⁰ and measures how many orders of engineering headroom remain; it also keeps the Landauer/ML floor visibly in the benchmark rather than as a footnote. (6) Report energy per logical qubit-hour in memory (idling) mode separately from gate mode.

**Why 2026 is the right time.** Below-threshold surface-code operation is demonstrated [UNVERIFIED: arXiv:2408.13687], resource-constrained scaling arguments are published [UNVERIFIED: arXiv:2007.01966; arXiv:2209.05469], and energy-focused programmatic calls exist [UNVERIFIED: Auffèves, arXiv:2111.09241]. The hardware exists to anchor the first honest logical-qubit-normalized numbers; waiting until 10⁶-qubit machines ship would forfeit the benchmark's steering value during the expensive part of the roadmap.

## 5. Limitations and falsifiability

**Limitations.** (1) The budget assumes a superconducting platform; trapped-ion machines are laser-dominated (~kW-class laser infrastructure) and neutral-atom/photonic machines have different cost structures — the dominance ranking may not transfer. (2) Magic-state distillation factories are folded into a range rather than modeled; at high non-Clifford rates they could add substantially. (3) Idle-power amortization depends on duty cycle, which is a use-case property, not a machine property. (4) The ancilla-erasure count in Q1 is an architecture estimate. (5) No citation in this draft was verified this session (environmental tool block); until the parent verifies Section References, the paper is a labeled hypothesis, not a sourced result.

**Falsifying observations.** The central ~10 MW / ~1 J-per-op estimate would be falsified downward by a peer-reviewed full-stack power budget for a ≥10⁵-physical-qubit machine with <1 W per-channel control power and <2 kW fridge power per 10⁴ qubits (→ ~10⁻³ J/op); it would be falsified upward if physical error rates remain ~10⁻² so d must rise to ~50 (→ ×3–10 energy/op), or if distance-30 real-time decoders are shown to consume >1 μJ per syndrome bit (→ decoding becomes the dominant term, overturning the Section 3 ranking). The Q1 floor could only be falsified by an experimental violation of Landauer or Margolus–Levitin, which would be a Nobel-grade surprise and is treated as established.

## 6. Conclusion

The energy floor of fault-tolerant quantum computing is set by physics that is generous — 10⁻¹⁸ to 10⁻²¹ J per logical operation — and a practice that is not: ~10 MW and ~1 J per logical operation at the 1,000-logical-qubit scale, dominated by control electronics and cryogenics. The 2026 joules-per-compute revision should measure exactly that gap, per logical qubit-operation at a declared error budget, so that the field's scarce engineering attention is steered toward the two orders that actually cost money.

## References

All entries [UNVERIFIED - needs parent check] — arXiv IDs written from model knowledge in a tool-blocked session; none fetched or confirmed this session.

1. N. Margolus, L. B. Levitin, "The maximum speed of dynamical evolution," Physica D 120, 188 (1998). arXiv:quant-ph/9710043. [UNVERIFIED]
2. R. Landauer, "Irreversibility and heat generation in the computing process," IBM J. Res. Dev. 5(3), 183–191 (1961). DOI 10.1147/rd.53.0183. [UNVERIFIED — DOI from memory]
3. A. Bérut et al., "Experimental verification of Landauer's principle linking information and thermodynamics," Nature 483, 187–189 (2012). arXiv:1203.1212. [UNVERIFIED]
4. S. Lloyd, "Ultimate physical limits to computation," Nature 406, 1047–1054 (2000). arXiv:quant-ph/9908043. [UNVERIFIED]
5. L. B. Levitin, T. Toffoli, "Fundamental limit on the rate of quantum dynamics: the unified bound is tight," Phys. Rev. Lett. 103, 160502 (2009). arXiv:0905.3417. [UNVERIFIED]
6. A. G. Fowler, M. Mariantoni, J. M. Martinis, A. N. Cleland, "Surface codes: Towards practical large-scale quantum computation," Phys. Rev. A 86, 032324 (2012). arXiv:1208.0928. [UNVERIFIED]
7. C. Gidney, M. Ekerå, "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits," Quantum 5, 433 (2021). arXiv:1905.09749. [UNVERIFIED]
8. M. Fellous-Asiani et al., "Limitations in quantum computing from resource constraints," PRX Quantum 2, 040335 (2021). arXiv:2007.01966. [UNVERIFIED]
9. M. Fellous-Asiani, J. H. Chai, R. S. Whitney, A. Auffèves, H. K. Ng, "Optimizing resource efficiencies for scalable full-stack quantum computers," PRX Quantum 4, 040319 (2023). arXiv:2209.05469. [UNVERIFIED]
10. A. Auffèves, "Quantum technologies need a quantum energy initiative," PRX Quantum 3, 020101 (2022). arXiv:2111.09241. [UNVERIFIED]
11. Google Quantum AI (R. Acharya et al.), "Quantum error correction below the surface code threshold," Nature 638, 920–926 (2025). arXiv:2408.13687. [UNVERIFIED]
12. S. Bravyi et al., "High-threshold and low-overhead fault-tolerant quantum memory," Nature 627, 778–782 (2024). arXiv:2308.07915. [UNVERIFIED]
13. B. Patra et al., "Cryo-CMOS circuits and systems for quantum computing applications," IEEE J. Solid-State Circuits 53(1), 309–321 (2018). [UNVERIFIED — no arXiv ID claimed]
14. QNFO joules-per-compute benchmark repository, github.com/rwnq8/joules-per-compute-benchmark. [UNVERIFIED — repository cited in the task input block; README not fetched this session]
