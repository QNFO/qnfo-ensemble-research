# The Resource Burden of Active Quantum Error Correction: A Scaling Analysis of Qubit, Bandwidth, and Energy Overheads

## Abstract

Active quantum error correction (QEC) protects quantum information only by continuously consuming physical resources: qubits, measurement bandwidth, classical processing, and energy. While the theoretical foundations of QEC are mature, the *resource burden* of running a code—rather than constructing one—is often treated as an implementation detail. This paper develops a transparent scaling analysis of the overheads of active QEC, using the surface code as the canonical worked example. We derive closed-form expressions for the physical-qubit overhead $N_{\mathrm{phys}}(d) = 2d^2 - 1$, the syndrome-bit generation rate, and the energy per logical operation $E_L(d) = (2d^2-1)\,d\,\varepsilon_q$, where $d$ is the code distance and $\varepsilon_q$ the per-qubit per-cycle energy. With explicit arithmetic we show that reaching a target logical error rate of $10^{-12}$ at a physical error rate of $10^{-3}$ requires $d = 21$, $881$ physical qubits per logical qubit, and—under a stated per-qubit energy assumption of $10^{-9}$ J per cycle—an energy cost of $1.85 \times 10^{-5}$ J per logical operation, roughly $6.45 \times 10^{18}$ times the Landauer limit at 300 mK. We situate these results against the broader QEC literature, including continuous-time QEC, entanglement-assisted codes, and recent energy-focused analyses, and argue that resource accounting must become a first-class design criterion for fault-tolerant architectures.

## 1. Introduction

Quantum error correction is what transformed quantum information science from an academic curiosity into a viable engineering discipline [5]. The core idea—encoding logical information in a subspace of a larger Hilbert space such that the most probable errors move the state into an orthogonal, correctable subspace—is now standard textbook material [4], [6]. Yet the standard presentations concentrate on the *existence* of codes and the *conditions* under which they work. Far less attention is paid, in the same treatments, to what it *costs* to keep a code running: every logical operation is accompanied by a stream of syndrome measurements, feedback decisions, and physical gate operations whose aggregate resource demands can dominate the entire machine.

This paper addresses that gap with a deliberately simple question: given a target logical error rate, what must be spent—in qubits, in measurement bandwidth, in energy—to sustain active error correction? We answer it for the surface code, not because the surface code is optimal, but because its overheads are the most transparent and its parameters the most widely quoted, making it the natural baseline against which any alternative (continuous-time schemes [1], entanglement-assisted codes [2], adiabatic error handling [7]) should be measured.

Our contributions are:

1. Closed-form scaling laws for the qubit overhead, syndrome-bit rate, and energy per logical operation of a distance-$d$ surface code, with every constant stated explicitly (Section 3).
2. Fully worked numerical derivations for a family of target logical error rates, showing the cubic-in-$d$ growth of energy and the logarithmic scaling of $d$ itself (Section 4).
3. A comparative discussion placing these numbers against the Landauer limit, against continuous-time QEC's different resource profile [1], and against recent energy-focused lower bounds [9] (Sections 5 and 6).

We emphasize honesty about assumptions: every numerical result below is either derived with shown arithmetic from stated inputs or explicitly labeled a projection with stated assumptions. No experimental data are reported.

## 2. Background and Related Work

The literature relevant to this analysis spans foundational QEC theory, code-construction surveys, alternative QEC paradigms, and a small but growing body of resource-focused work.

**Foundations of QEC.** Gottesman [4] introduces the canonical machinery—encoding, syndrome extraction, error operators, and code construction—and shows that general noise on a set of two-state systems decomposes into Pauli operators, so that a code corrects a discrete subset of Pauli errors. This decomposition is precisely what makes the surface-code analysis of Section 3 possible: the effective logical error rate of a distance-$d$ code is controlled by the probability of uncorrectable Pauli error chains of length $\lfloor d/2 \rfloor + 1$. Terhal [6] gives a modern survey framing QEC as the design of a code subspace orthogonal to the dominant error subspaces, and emphasizes that the *most common* errors—not all errors—determine performance, which justifies the threshold-scaling ansatz we adopt. Brun's survey [3] traces the lineage from classical error control to quantum codes and highlights the structural differences (no-cloning, continuous error amplitudes) that force active, measurement-based correction rather than passive redundancy; this is the historical root of the resource burden we quantify.

**Alternative QEC paradigms.** Sarma et al. [5] broaden the view beyond qubits to qudits and other encodings, noting that robust manipulation of fragile superpositions is the universal requirement; the overhead analysis here is encoding-agnostic in its method even if its numbers are surface-code-specific. Brun et al. [7] analyze error suppression and correction in adiabatic quantum computation, where circuit-model correction routines do not transfer because high-quality gates are unavailable; their conclusion—that some form of error handling remains necessary—implies that *some* analogue of the active-correction burden exists in every paradigm, though its form differs. Aharonov et al.'s continuous-time QEC framework [1] treats both noise and correction as processes continuous in time, based on continuous weak measurement and feedback viewed through the subsystem principle; this changes the *temporal profile* of the resource burden (continuous weak measurement instead of discrete syndrome rounds) but not its existence, and we return to the comparison in Section 6. Lai et al. [2] present entanglement-assisted QEC codes, which use pre-shared entanglement between encoder and decoder to construct codes from pairs of classical codes that fail the self-orthogonality condition; entanglement assistance can reduce the qubit overhead per logical qubit but converts part of the burden into a demand for high-fidelity entanglement distribution—a resource substitution rather than a resource elimination. More speculatively, quaternionic extensions of QEC [8] define Pauli analogues and gates in quaternionic Hilbert spaces with inner-product-preserving encodings; such proposals remain far from resource quantification but illustrate the breadth of the code-design space within which overhead accounting must eventually operate.

**Resource- and energy-focused work.** Closest to our concerns, the QNFO analysis of energy cost per logical-qubit operation in surface-code QEC [9] derives a practical lower bound on energy cost accounting for gate-fidelity decay's impact on code distance and physical error rates; our Section 4 derivation is complementary in that it makes the overhead arithmetic fully explicit at a single operating point rather than bounding it. The hybrid quantum–classical feasibility analysis of coherence-assisted error correction for deep learning [10] approaches protection cost from the classical side, where bit-level fault protection under low-voltage or radiation-prone operation imposes analogous overheads—an instructive mirror showing that the protection-cost problem is not unique to quantum hardware. The QEC–Quantum Darwinism tradeoff result [11] establishes, via the no-go theorem attributed to Maity et al., that QEC and emergent classical objectivity cannot coexist above a critical logical fidelity $F_L > 0.874$; this bounds the regime in which active correction can be relaxed by letting the environment redundantly record information. Finally, the lifecycle analysis of a fault-tolerant quantum computer [12] frames the full-system resource question across the machine's operating life, of which the per-operation costs derived here are one component.

## 3. Methods

### 3.1 Model

We consider a rotated surface code of distance $d$ ($d$ odd) encoding one logical qubit. Standard layout facts, used as inputs:

- Data qubits: $d^2$.
- Syndrome (ancilla) qubits: $d^2 - 1$.
- Total physical qubits per logical qubit:
$$N_{\mathrm{phys}}(d) = 2d^2 - 1.$$

One error-correction cycle of duration $\tau_c$ extracts all $d^2 - 1$ syndrome bits. We assume a logical operation (e.g., a lattice-surgery merge-and-split or a logical gate implemented by code deformation) requires $d$ consecutive cycles, the standard scaling for time-like error protection at distance $d$.

### 3.2 Logical error rate ansatz

Below threshold, the logical error rate per logical operation follows the standard phenomenological scaling (consistent with the Pauli-error framing of [4] and the dominant-error-subspace framing of [6]):

$$p_L(d) = A \left( \frac{p}{p_{\mathrm{th}}} \right)^{(d+1)/2},$$

where $p$ is the physical (circuit-level) error rate per operation, $p_{\mathrm{th}}$ the threshold, and $A$ a prefactor of order $10^{-1}$. We take $A = 0.1$ as a stated modeling choice.

### 3.3 Resource quantities

- **Qubit overhead:** $N_{\mathrm{phys}}(d)$ above.
- **Syndrome bandwidth:** bits per logical operation
$$B(d) = d\,(d^2 - 1),$$
and bits per second $R(d) = B(d)/\tau_c$ with $\tau_c = 1\ \mu\mathrm{s} = 10^{-6}$ s (stated assumption, typical of superconducting platforms).
- **Energy per logical operation:** with $\varepsilon_q$ the energy dissipated per physical qubit per cycle (stated assumption $\varepsilon_q = 10^{-9}$ J, i.e., 1 nJ, covering control pulses, measurement, and a share of cryogenics and classical processing),
$$E_L(d) = N_{\mathrm{phys}}(d)\, d\, \varepsilon_q = (2d^2 - 1)\, d\, \varepsilon_q.$$
- **Area per logical qubit:** with pitch $a = 100\ \mu\mathrm{m} = 10^{-4}$ m (stated assumption),
$$A_{\mathrm{tile}}(d) = (d\,a)^2.$$

### 3.4 Choosing $d$ for a target

Given a target $p_L \le P$, we require
$$A \left( \frac{p}{p_{\mathrm{th}}} \right)^{(d+1)/2} \le P \quad\Longrightarrow\quad d \ge 2\,\frac{\log_{10}(P/A)}{\log_{10}(p/p_{\mathrm{th}})} - 1,$$
rounded up to the nearest odd integer. Throughout we take $p = 10^{-3}$ and $p_{\mathrm{th}} = 10^{-2}$ (stated inputs), so $\log_{10}(p/p_{\mathrm{th}}) = \log_{10}(0.1) = -1$ and the condition simplifies to $d \ge -2\log_{10}(P/A) - 1$.

## 4. Analysis

Every input number is stated here with its source: $A = 0.1$ (modeling choice, Section 3.2); $p = 10^{-3}$, $p_{\mathrm{th}} = 10^{-2}$ (stated inputs, Section 3.4); $\tau_c = 10^{-6}$ s, $\varepsilon_q = 10^{-9}$ J, $a = 10^{-4}$ m (stated assumptions, Section 3.3); $k_B = 1.380649 \times 10^{-23}$ J/K (CODATA) and $T = 0.3$ K (dilution-refrigerator base temperature, stated assumption).

### 4.1 Code distance for $P = 10^{-12}$

$$\log_{10}(P/A) = \log_{10}(10^{-12}/0.1) = \log_{10}(10^{-11}) = -11.$$
$$d \ge -2(-11) - 1 = 21.$$
Since $21$ is odd, $d^* = 21$.

### 4.2 Qubit overhead at $d = 21$

$$N_{\mathrm{phys}}(21) = 2 \times 21^2 - 1 = 2 \times 441 - 1 = 882 - 1 = 881.$$

### 4.3 Logical error rate check

$$p_L(21) = 0.1 \times (0.1)^{(21+1)/2} = 0.1 \times (0.1)^{11} = 0.1 \times 10^{-11} = 10^{-12}. \checkmark$$

### 4.4 Syndrome bandwidth at $d = 21$

$$B(21) = 21 \times (21^2 - 1) = 21 \times 440 = 9240 \text{ bits per logical operation}.$$
$$R(21) = \frac{9240}{10^{-6}\ \mathrm{s}} = 9.24 \times 10^{9} \text{ bits s}^{-1} \text{ per logical qubit}.$$

### 4.5 Energy per logical operation at $d = 21$

$$E_L(21) = 881 \times 21 \times 10^{-9}\ \mathrm{J} = 18501 \times 10^{-9}\ \mathrm{J} = 1.8501 \times 10^{-5}\ \mathrm{J}.$$

### 4.6 Comparison with the Landauer limit

The Landauer bound at temperature $T$ is $E_{\mathrm{Land}} = k_B T \ln 2$:
$$E_{\mathrm{Land}} = 1.380649 \times 10^{-23} \times 0.3 \times 0.693147 = 2.8705 \times 10^{-24}\ \mathrm{J}.$$
(The last factor: $\ln 2 = 0.693147$; product $1.380649 \times 0.3 = 0.4141947$; $\times 0.693147 = 0.28705$; hence $2.8705 \times 10^{-24}$ J.)
$$\frac{E_L(21)}{E_{\mathrm{Land}}} = \frac{1.8501 \times 10^{-5}}{2.8705 \times 10^{-24}} = 6.445 \times 10^{18}.$$

### 4.7 Area density at $d = 21$

$$A_{\mathrm{tile}}(21) = (21 \times 10^{-4}\ \mathrm{m})^2 = (2.1 \times 10^{-3}\ \mathrm{m})^2 = 4.41 \times 10^{-6}\ \mathrm{m}^2.$$
$$\rho_L = \frac{1}{4.41 \times 10^{-6}} = 2.2676 \times 10^{5} \text{ logical qubits per m}^2.$$

### 4.8 Scaling of energy with target fidelity

Since $d \approx -2\log_{10}(P/A) - 1$ and $E_L \propto d^3$, energy grows as the cube of the logarithm of the inverse target error rate. To quantify: for $P = 10^{-3}$, $\log_{10}(P/A) = \log_{10}(10^{-2}) = -2$, so $d \ge 3$, $d^* = 3$:
$$N_{\mathrm{phys}}(3) = 2 \times 9 - 1 = 17, \qquad E_L(3) = 17 \times 3 \times 10^{-9} = 5.1 \times 10^{-8}\ \mathrm{J}.$$
Ratio of energies:
$$\frac{E_L(21)}{E_L(3)} = \frac{1.8501 \times 10^{-5}}{5.1 \times 10^{-8}} = 362.8.$$
Note $21^3/3^3 = 9261/27 = 343$; the deviation from the pure $d^3$ law arises from the $-1$ term in $N_{\mathrm{phys}}(d) = 2d^2 - 1$.

### 4.9 Intermediate points (same arithmetic)

- $P = 10^{-6}$: $\log_{10}(P/A) = -5$, $d \ge 9$, $d^* = 9$. $N_{\mathrm{phys}}(9) = 2 \times 81 - 1 = 161$. $E_L(9) = 161 \times 9 \times 10^{-9} = 1.449 \times 10^{-6}$ J. $B(9) = 9 \times 80 = 720$ bits.
- $P = 10^{-9}$: $\log_{10}(P/A) = -8$, $d \ge 15$, $d^* = 15$. $N_{\mathrm{phys}}(15) = 2 \times 225 - 1 = 449$. $E_L(15) = 449 \times 15 \times 10^{-9} = 6.735 \times 10^{-6}$ J. $B(15) = 15 \times 224 = 3360$ bits.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs ($A = 0.1$, $p = 10^{-3}$, $p_{\mathrm{th}} = 10^{-2}$, $\tau_c = 10^{-6}$ s, $\varepsilon_q = 10^{-9}$ J, $a = 10^{-4}$ m, $T = 0.3$ K); none are measured.

| Target $P$ | $d^*$ | $N_{\mathrm{phys}}$ | $p_L(d^*)$ | $B(d^*)$ (bits/logical op) | $E_L(d^*)$ (J) |
|---|---|---|---|---|---|
| $10^{-3}$ | 3 | 17 | $10^{-3}$ | 24 | $5.1 \times 10^{-8}$ |
| $10^{-6}$ | 9 | 161 | $10^{-6}$ | 720 | $1.449 \times 10^{-6}$ |
| $10^{-9}$ | 15 | 449 | $10^{-9}$ | 3360 | $6.735 \times 10^{-6}$ |
| $10^{-12}$ | 21 | 881 | $10^{-12}$ | 9240 | $1.8501 \times 10^{-5}$ |

Headline results at the $P = 10^{-12}$ operating point:

1. **Qubit overhead:** $881$ physical qubits per logical qubit.
2. **Syndrome bandwidth:** $9240$ bits per logical operation, i.e., $9.24 \times 10^{9}$ bits s$^{-1}$ per logical qubit at $\tau_c = 1\ \mu$s.
3. **Energy per logical operation:** $1.8501 \times 10^{-5}$ J, which is $6.445 \times 10^{18}$ times the Landauer limit $2.8705 \times 10^{-24}$ J at 300 mK.
4. **Areal density:** $2.2676 \times 10^{5}$ logical qubits per m$^2$ at pitch $100\ \mu$m.
5. **Scaling:** energy per logical operation grows by a factor $362.8$ when the target error rate improves from $10^{-3}$ to $10^{-12}$—cubic in code distance, i.e., cubic in $\log(1/P)$.

**Labeled projection (not computed above).** If $\varepsilon_q$ were improved to $10^{-12}$ J per qubit per cycle (a speculative $10^3\times$ reduction requiring co-integrated control at millikelvin), the same arithmetic gives $E_L(21) = 881 \times 21 \times 10^{-12} = 1.8501 \times 10^{-8}$ J. The uncertainty in this projection is dominated entirely by the $\varepsilon_q$ assumption, which spans at least three orders of magnitude across proposed platforms; the qubit and bandwidth results, by contrast, depend only on the code layout and are robust.

## 6. Discussion

**What the numbers mean.** The dominant message is that active QEC converts a hardware problem (physical error rate $p$) into a *throughput and energy* problem: the classical processing layer must sustain $\sim 10^{10}$ syndrome bits per second per logical qubit, and the energy bill per logical operation is, under our assumptions, eighteen to nineteen orders of magnitude above the Landauer limit. This is consistent in spirit with the lower-bound analysis of [9], which also finds energy per logical operation to be the binding constraint once gate-fidelity decay forces larger code distances. It also echoes, on the quantum side, the protection-cost structure identified for classical deep-learning hardware in [10]: protection, not computation, dominates.

**Comparison with alternative paradigms.** Continuous-time QEC [1] replaces discrete syndrome rounds with continuous weak measurement and feedback. The bandwidth burden then becomes a continuous measurement-strength budget rather than a discrete bit rate; whether this is cheaper depends on the back-action cost of weak measurement, which our discrete model does not capture—an explicit open question. Entanglement-assisted codes [2] can reduce the number of physical data qubits per logical qubit but require pre-shared entanglement, substituting a distribution resource for a layout resource; our framework can accommodate this by replacing $N_{\mathrm{phys}}(d)$ with a modified overhead plus an entanglement-consumption term, which we have not modeled. Adiabatic error handling [7] avoids some gate-quality demands but still requires error suppression whose resource cost is not expressible in our cycle-based accounting. The QEC–Darwinism no-go result [11] warns that one cannot indefinitely offload protection onto environmental redundancy: above logical fidelity $F_L > 0.874$, the theorem asserts the two cannot coexist, so active correction cannot simply be "relaxed" at high fidelity.

**Limitations and failure modes.** (i) The ansatz $p_L(d) = A(p/p_{\mathrm{th}})^{(d+1)/2}$ with $A = 0.1$ is phenomenological; the true prefactor is code- and noise-model-dependent, and a different $A$ shifts $d^*$ by a constant offset in $\log_{10}$, changing $E_L$ by factors of order $(d'/d)^3$. (ii) The energy model $\varepsilon_q = 10^{-9}$ J per qubit per cycle is a coarse assumption; cryogenic and classical-processing shares may scale sub- or super-linearly in $N_{\mathrm{phys}}$, and a superlinear share would worsen the cubic law. (iii) We assume one logical operation costs $d$ cycles; algorithms with heavy lattice-surgery traffic could pay more. (iv) Correlated errors (cosmic rays, leakage) violate the independent-Pauli picture underlying [4] and can dominate at large $d$. (v) We treat only the surface code; qudit and oscillator encodings [5] may have different overhead exponents.

**What would falsify our claims.** A demonstrated surface-code implementation achieving $p_L \sim 10^{-12}$ with $d$ substantially below 21 at $p = 10^{-3}$—or a per-qubit cycle energy far below $10^{-9}$ J at scale—would falsify the headline numbers. A rigorous proof that the prefactor $A$ is orders of magnitude smaller than $0.1$ for realistic circuit noise would soften the cubic penalty. Conversely, confirmation of the energy lower bound of [9] at a compatible operating point would strengthen the analysis.

**Open questions.** How does the optimal tradeoff shift under continuous-time correction [1]? Can entanglement assistance [2] or non-qubit encodings [5], [8] reduce the exponent on $d$? And does the fidelity ceiling implied by [11] interact with the energy scaling to create a fundamental efficiency frontier for fault-tolerant computation, as the lifecycle framing of [12] suggests?

## 7. Conclusion

We have presented a fully explicit scaling analysis of the resource burden of active quantum error correction, using the surface code as the worked baseline. With every input stated and every arithmetic step shown, we find that a target logical error rate of $10^{-12}$ at physical error rate $10^{-3}$ demands a distance-21 code: $881$ physical qubits, $9240$ syndrome bits, and—under a stated $10^{-9}$ J per-qubit-per-cycle assumption—$1.8501 \times 10^{-5}$ J per logical operation, $6.445 \times 10^{18}$ times the Landauer limit at 300 mK. Energy grows as the cube of the code distance, hence as the cube of $\log(1/P)$: each additional three orders of magnitude in logical fidelity costs roughly a factor of $10^3$ in energy. The central lesson is methodological: resource accounting for active QEC should be presented with the same explicitness as code constructions, because the burden—not the existence—of error correction is what will decide the architecture of fault-tolerant machines.

## References

[1] arXiv:1311.2485v2 | Continuous-time quantum error correction

[2] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes

[3] arXiv:quant-ph/0602157v1 | An Introduction to Error-Correcting Codes: From Classical to Quantum

[4] arXiv:quant-ph/0304016v2 | Quantum Computing and Error Correction

[5] arXiv:0811.3734v1 | Quantum error correction beyond qubits

[6] arXiv:1910.03672v1 | Quantum Error Correction

[7] arXiv:1307.5893v3 | Error suppression and error correction in adiabatic quantum computation I: techniques and challenges

[8] arXiv:2504.19833v1 | Quantum Error Correction in Quaternionic Hilbert Spaces

[9] QNFO: A Lower Bound on Energy Cost per Logical-Qubit Operation in Surface-Code Quantum Error Correction | DOI 10.5281/zenodo.22283869

[10] QNFO: Coherence-Assisted Error Correction for Deep Learning: A Reconciled Feasibility Analysis of a Hybrid Quantum-Classical Architecture | DOI 10.5281/zenodo.23116197

[11] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | DOI 10.5281/zenodo.21964674

[12] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer | DOI 10.5281/zenodo.18000790