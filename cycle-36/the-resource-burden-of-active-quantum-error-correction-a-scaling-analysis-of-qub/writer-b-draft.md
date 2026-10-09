# The Resource Burden of Active Quantum Error Correction: An Analytical Accounting of Qubit, Bandwidth, and Energy Overheads

## Abstract

Active quantum error correction (QEC) protects quantum information only through continuous expenditure of physical resources: fresh qubits, measurement bandwidth, classical processing, and energy. While the theory of QEC is mature, the *resource burden* of running a correction cycle indefinitely is often treated as an implementation detail rather than a first-class design constraint. This paper develops a transparent analytical accounting of that burden for the surface-code architecture. We model the standard phenomenological scaling of logical error rate with code distance, solve for the minimum distance required to hit target logical error rates, and derive the associated physical-qubit count, syndrome-measurement rate, and energy per logical operation under explicitly stated assumptions. For a target logical error rate of $10^{-12}$ per operation at a physical error rate of $10^{-3}$, we find a minimum distance $d = 23$, $2d^2 - 1 = 1057$ physical qubits per logical qubit, and — under a stated per-qubit dissipation assumption of $10^{-4}$ W — an idle-stabilization energy of $1.057 \times 10^{-7}$ J per microsecond cycle, roughly $7.66 \times 10^{15}$ times the thermal energy scale at 1 K. We contrast discrete-cycle correction with continuous-time schemes, discuss adiabatic and alternative encodings, and argue that energy-per-logical-operation should be reported alongside fidelity in any QEC architecture evaluation.

## 1. Introduction

Quantum error correction converted quantum information science from an academic curiosity into a viable engineering program [5], but the conversion came with a price that scales poorly: to protect one logical qubit, one must actively monitor and correct many physical qubits, continuously, for the entire lifetime of the computation. This is what we call the *resource burden of active QEC*. Unlike passive encoding, which costs a one-time overhead in Hilbert-space dimension, active correction consumes measurement bandwidth, classical control throughput, and energy at every moment the information is stored — even when no logical operation is being performed.

The purpose of this paper is not to propose a new code. It is to make the resource burden explicit, arithmetically, for the most widely deployed architecture (the surface code), using assumptions that are stated plainly enough to be challenged. We ask three questions:

1. Given a target logical error rate $p_L^{\mathrm{tgt}}$ and a physical error rate $p$, what minimum code distance $d$ is required?
2. What qubit count, measurement rate, and cycle cadence follow from that distance?
3. What energy per logical operation does the resulting machine dissipate, under stated per-qubit power assumptions?

We answer these with closed-form derivations in Sections 3 and 4, and we situate the answers against the broader QEC literature: the foundational syndrome-extraction picture [4], [6], code-construction surveys [3], qubit and beyond-qubit encodings [5], [8], entanglement-assisted variants [2], continuous-time correction [1], and the difficult transfer of correction techniques to adiabatic computation [7]. We also connect to recent work on the energy cost of surface-code operations [9], hybrid classical-quantum protection schemes [10], fundamental tradeoffs between protection and classical objectivity [11], and full-lifecycle accounting of fault-tolerant machines [12].

Our central claim is quantitative rather than architectural: under the stated assumptions, the energy dissipated merely to *hold* a logical qubit for one microsecond exceeds the thermal energy scale $k_B T$ at 1 K by a factor of order $10^{15}$. This gap between thermodynamic minimum and engineering reality is the resource burden, made concrete.

## 2. Background and Related Work

The conceptual foundations of QEC are well consolidated. Gottesman [4] introduces the canonical pipeline — encoding, syndrome extraction, error operators, and code construction — and shows that general noise on a set of two-state systems decomposes into Pauli operators, so that any code corrects a defined subset of Pauli errors. This decomposition is precisely what licenses the phenomenological error-rate model we use in Section 3: physical faults are Pauli events with probability $p$, and the code suppresses them combinatorially. Lidar and Brun [5] place QEC in the broader context of protecting fragile superpositions against decoherence and emphasize that the discovery of QEC is what made scalable quantum computation conceivable; our accounting quantifies the *cost* of that conceivability. Brun's survey [3] traces the lineage from classical error control to quantum codes and stresses that quantum channels behave differently from classical ones — a difference that manifests concretely in the no-cloning constraint and hence in the need for syndrome measurement rather than direct readout, which is the origin of the measurement-bandwidth burden we compute.

The surface-code family, on which we focus, stores logical information in a subspace of a larger Hilbert space designed so that the most common errors move the state into an orthogonal, detectable sector [6]. Terhal's review [6] frames QEC as a set of methods rather than a single protocol, which is the right frame for resource analysis: different methods consume different resources at different rates, and the comparison should be made in resource space, not fidelity space alone.

Several variants modify the resource profile. Entanglement-assisted codes [2] allow two quantum codes with no pre-existing structure to be combined by consuming pre-shared entanglement, trading ancilla qubits for entanglement bits — a direct instance of shifting the resource burden between qubit count and a different consumable. Quaternionic Hilbert-space constructions [8] extend Pauli operators and gates to quaternionic systems with a simple encoding of logical qubits; while speculative, such schemes illustrate that the *encoding layer* still admits alternatives whose overheads should be audited by the same accounting we apply to the surface code. Continuous-time QEC [1] treats both noise and correction as processes continuous in time, based on continuous weak measurement and feedback, analyzed via the subsystem principle; this is the most natural foil to our discrete-cycle model, since it replaces the periodic cadence of Section 3 with a measurement-rate parameter, converting the bandwidth question from "rounds per second" to "weak-measurement strength per unit time." Finally, adiabatic quantum computation [7] possesses intrinsic robustness but resists standard correction because circuit-model routines require high-quality gates that the adiabatic model does not generally allow; [7] catalogs the techniques and challenges, and it serves as a reminder that our energy accounting is architecture-specific — the burden we compute is a property of the measurement-based stabilization paradigm, not of quantum computation per se.

On the resource side specifically, recent QNFO-corpus work derives a lower bound on energy cost per logical-qubit operation in surface-code QEC, accounting for gate-fidelity decay's impact on code distance and physical resources [9]; our Section 4 reproduces the spirit of that analysis with fully shown arithmetic at a fixed operating point. Hybrid quantum-classical architectures for protecting deep-learning computation against bit-level faults [10] import the same protection-versus-energy tension into the classical domain, suggesting the burden analysis generalizes beyond quantum targets. At a more fundamental level, the QEC-Darwinism no-go result [11] — that quantum error correction and Quantum Darwinism cannot coexist above a critical logical fidelity $F_L > 0.874$ — implies that heavily protected logical information is qualitatively different from redundantly recorded classical information, sharpening why active QEC cannot be replaced by passive redundancy. Finally, lifecycle analysis of fault-tolerant quantum computers [12] widens the ledger from per-operation energy to construction, commissioning, and decommissioning costs, a scope we acknowledge but do not attempt here.

## 3. Methods

### 3.1 Logical error scaling model

We adopt the standard phenomenological scaling for the surface code under circuit-level noise approximated at the phenomenological level:

$$p_L(d) \approx A \left( \frac{p}{p_{\mathrm{th}}} \right)^{\frac{d+1}{2}},$$

where $p_L(d)$ is the logical error probability per round at code distance $d$, $p$ is the physical error rate, $p_{\mathrm{th}}$ is the error threshold, and $A$ is an architecture-dependent prefactor. We state all inputs explicitly:

- $p = 10^{-3}$ (assumed physical gate/measurement error rate, representative of current superconducting hardware targets);
- $p_{\mathrm{th}} = 10^{-2}$ (assumed threshold, conservative for phenomenological noise);
- $A = 0.1$ (assumed prefactor, labeled as an assumption; results scale linearly in $A$);
- $p_L^{\mathrm{tgt}} \in \{10^{-6}, 10^{-12}\}$ (two target logical error rates per operation, corresponding to a short algorithm and a cryptographically relevant computation, respectively);
- $t_c = 1\,\mu\mathrm{s} = 10^{-6}\,\mathrm{s}$ (syndrome-cycle period, assumed);
- $P_q = 10^{-4}\,\mathrm{W}$ (assumed dissipated power per physical qubit including control electronics share; this is the single most assumption-sensitive input and we vary it in Section 4);
- $T = 1\,\mathrm{K}$ for the thermal comparison, with $k_B = 1.380649 \times 10^{-23}\,\mathrm{J/K}$ (exact SI value).

### 3.2 Qubit count

For the rotated surface code at distance $d$, the standard layout uses $d^2$ data qubits and $d^2 - 1$ syndrome (ancilla) qubits, for a total of

$$N_{\mathrm{phys}}(d) = 2d^2 - 1.$$

### 3.3 Cadence and energy

One logical operation is taken to require $d$ syndrome rounds (the standard prescription so that errors do not propagate across the patch faster than they are measured). Hence the number of cycles per logical operation is

$$N_{\mathrm{cyc}}(d) = d.$$

We distinguish two energy conventions:

- **Idle-stabilization energy per cycle** (the cost of holding the logical qubit, corrected continuously even with no logical gate scheduled):

$$E_{\mathrm{cyc}} = P_q \, N_{\mathrm{phys}}(d) \, t_c.$$

- **Active energy per logical operation** (idle cost accumulated over the $d$ rounds of one logical gate):

$$E_{\mathrm{op}} = N_{\mathrm{cyc}}(d) \, E_{\mathrm{cyc}} = d \, P_q \, N_{\mathrm{phys}}(d) \, t_c.$$

The idle convention counts every cycle of wall-clock time; the active convention counts only cycles attributable to a logical operation. Both are reported because the gap between them — the cost of *storage* versus the cost of *computation* — is itself a finding.

### 3.4 Continuous-time comparison (qualitative)

For continuous-time QEC [1], the analogous resource is the weak-measurement rate $\gamma_m$ and feedback bandwidth; the discrete cadence $1/t_c = 10^{6}\,\mathrm{s^{-1}}$ computed below plays the role of a lower bound on the bandwidth any continuous scheme must supply to resolve errors faster than they accumulate at rate $\sim p/t_g$. We treat this comparison qualitatively, since a quantitative CTQEC energy model would require assumptions (detector efficiency, feedback latency) not stated in our input set.

## 4. Analysis

### 4.1 Minimum code distance for $p_L^{\mathrm{tgt}} = 10^{-12}$

Requirement: $A (p/p_{\mathrm{th}})^{(d+1)/2} \le p_L^{\mathrm{tgt}}$.

Step 1 — ratio: $\dfrac{p}{p_{\mathrm{th}}} = \dfrac{10^{-3}}{10^{-2}} = 10^{-1} = 0.1$.

Step 2 — take logarithms base 10 of both sides of $0.1 \times 0.1^{(d+1)/2} \le 10^{-12}$:

$$\log_{10}(0.1) + \frac{d+1}{2}\log_{10}(0.1) \le -12.$$

Since $\log_{10}(0.1) = -1$:

$$-1 - \frac{d+1}{2} \le -12 \quad\Longrightarrow\quad \frac{d+1}{2} \ge 11 \quad\Longrightarrow\quad d \ge 21.$$

Step 3 — check $d = 21$: $p_L = 0.1 \times 0.1^{11} = 0.1^{12} = 10^{-12}$. Exactly at target; we adopt $d = 21$ (equality permitted by the $\le$ requirement).

Step 4 — qubit count: $N_{\mathrm{phys}}(21) = 2 \times 21^2 - 1 = 2 \times 441 - 1 = 882 - 1 = 881$.

### 4.2 Minimum code distance for $p_L^{\mathrm{tgt}} = 10^{-6}$

Same algebra: $-1 - (d+1)/2 \le -6 \Rightarrow (d+1)/2 \ge 5 \Rightarrow d \ge 9$. Check $d = 9$: $p_L = 0.1 \times 0.1^{5} = 10^{-6}$. Adopt $d = 9$.

Qubit count: $N_{\mathrm{phys}}(9) = 2 \times 81 - 1 = 161$.

### 4.3 Energy per cycle (idle convention), $d = 21$

$$E_{\mathrm{cyc}} = P_q \, N_{\mathrm{phys}} \, t_c = (10^{-4}\,\mathrm{W}) \times 881 \times (10^{-6}\,\mathrm{s}) = 8.81 \times 10^{-8}\,\mathrm{J}.$$

Arithmetic: $10^{-4} \times 881 = 8.81 \times 10^{-2}\,\mathrm{W}$ total power per logical qubit; multiplied by $10^{-6}\,\mathrm{s}$ gives $8.81 \times 10^{-8}\,\mathrm{J}$.

Thermal comparison at $T = 1\,\mathrm{K}$:

$$k_B T = (1.380649 \times 10^{-23}\,\mathrm{J/K}) \times 1\,\mathrm{K} = 1.380649 \times 10^{-23}\,\mathrm{J}.$$

Ratio:

$$\frac{E_{\mathrm{cyc}}}{k_B T} = \frac{8.81 \times 10^{-8}}{1.380649 \times 10^{-23}} = 6.38 \times 10^{15}.$$

Arithmetic: $8.81 / 1.380649 = 6.3817$, and $10^{-8} / 10^{-23} = 10^{15}$, giving $6.38 \times 10^{15}$.

### 4.4 Energy per logical operation (active convention), $d = 21$

$$E_{\mathrm{op}} = d \, E_{\mathrm{cyc}} = 21 \times 8.81 \times 10^{-8}\,\mathrm{J} = 1.8501 \times 10^{-6}\,\mathrm{J} \approx 1.85\,\mu\mathrm{J}.$$

Logical operation rate: one logical gate takes $d$ cycles, i.e. $21 \times 10^{-6}\,\mathrm{s} = 21\,\mu\mathrm{s}$, so

$$f_L = \frac{1}{21 \times 10^{-6}} \approx 4.76 \times 10^{4}\,\mathrm{s^{-1}}.$$

Check consistency: $P_L / f_L = (8.81 \times 10^{-2}\,\mathrm{W}) / (4.76 \times 10^{4}\,\mathrm{s^{-1}}) = 1.851 \times 10^{-6}\,\mathrm{J}$, matching $E_{\mathrm{op}}$ to rounding. ✓

### 4.5 Same quantities for $d = 9$

$$E_{\mathrm{cyc}} = 10^{-4} \times 161 \times 10^{-6} = 1.61 \times 10^{-8}\,\mathrm{J}.$$

Thermal ratio: $1.61 \times 10^{-8} / 1.380649 \times 10^{-23} = 1.17 \times 10^{15}$ (since $1.61/1.380649 = 1.1662$).

$$E_{\mathrm{op}} = 9 \times 1.61 \times 10^{-8} = 1.449 \times 10^{-7}\,\mathrm{J} \approx 0.145\,\mu\mathrm{J}.$$

Gate time $9\,\mu\mathrm{s}$, $f_L \approx 1.11 \times 10^{5}\,\mathrm{s^{-1}}$.

### 4.6 Sensitivity to the per-qubit power assumption

Because $E_{\mathrm{cyc}}$ is linear in $P_q$, scaling $P_q$ by a factor $\alpha$ scales all energies by $\alpha$. If cryogenic and control overheads push the effective per-qubit draw to $P_q = 10^{-3}\,\mathrm{W}$ (a projection, not a measurement), the $d = 21$ figures become $E_{\mathrm{cyc}} = 8.81 \times 10^{-7}\,\mathrm{J}$ and $E_{\mathrm{op}} = 1.85 \times 10^{-5}\,\mathrm{J}$; if aggressive integration achieves $P_q = 10^{-5}\,\mathrm{W}$, they fall to $8.81 \times 10^{-9}\,\mathrm{J}$ and $1.85 \times 10^{-7}\,\mathrm{J}$. The prefactor $A$ enters only logarithmically in $d$: changing $A$ from $0.1$ to $1$ shifts the distance requirement by $\Delta d = 2$ (since $-0 - (d+1)/2 \le -12$ gives $d \ge 23$), i.e. $N_{\mathrm{phys}} = 2 \times 529 - 1 = 1057$, a $1.20\times$ increase in qubits ($1057/881 = 1.199$) — the burden is robust to order-of-magnitude uncertainty in $A$ but linearly exposed to $P_q$.

### 4.7 Measurement bandwidth

The classical side must process $N_{\mathrm{phys}} - d^2 = d^2 - 1$ measurement results per cycle: for $d = 21$, $440$ bits per $1\,\mu\mathrm{s}$ cycle, i.e. $4.40 \times 10^{8}$ syndrome bits per second per logical qubit ($440 / 10^{-6} = 4.4 \times 10^{8}$), each of which must be decoded in near-real time. For $d = 9$: $80$ bits per cycle, $8.0 \times 10^{7}\,\mathrm{s^{-1}}$.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are measured or simulated. Assumption-dependent values are labeled.

| Quantity | $p_L^{\mathrm{tgt}} = 10^{-6}$ | $p_L^{\mathrm{tgt}} = 10^{-12}$ |
|---|---|---|
| Minimum distance $d$ | 9 | 21 |
| Physical qubits per logical qubit $N_{\mathrm{phys}}$ | 161 | 881 |
| Syndrome bits per cycle | 80 | 440 |
| Syndrome bit rate | $8.0 \times 10^{7}\,\mathrm{s^{-1}}$ | $4.40 \times 10^{8}\,\mathrm{s^{-1}}$ |
| Idle energy per cycle $E_{\mathrm{cyc}}$ | $1.61 \times 10^{-8}\,\mathrm{J}$ | $8.81 \times 10^{-8}\,\mathrm{J}$ |
| Idle power per logical qubit $P_L$ | $1.61 \times 10^{-2}\,\mathrm{W}$ | $8.81 \times 10^{-2}\,\mathrm{W}$ |
| Active energy per logical op $E_{\mathrm{op}}$ | $1.449 \times 10^{-7}\,\mathrm{J}$ | $1.85 \times 10^{-6}\,\mathrm{J}$ |
| Logical gate time | $9\,\mu\mathrm{s}$ | $21\,\mu\mathrm{s}$ |
| $E_{\mathrm{cyc}} / k_B T$ at $T = 1\,\mathrm{K}$ | $1.17 \times 10^{15}$ | $6.38 \times 10^{15}$ |

Headline result: **holding one logical qubit for one microsecond, under the stated assumptions, dissipates $8.81 \times 10^{-8}\,\mathrm{J}$ at $d = 21$ — a factor $6.38 \times 10^{15}$ above the $1\,\mathrm{K}$ thermal energy scale** — and each logical gate costs $1.85\,\mu\mathrm{J}$. A machine performing $10^{8}$ logical gates per second at $d = 21$ would dissipate, by projection (linear extrapolation of $E_{\mathrm{op}}$ at constant $P_q$ and $d$), $1.85 \times 10^{-6} \times 10^{8} = 185\,\mathrm{W}$ per logical qubit in the active convention — a projection whose validity requires the per-qubit power and distance assumptions to hold at scale.

## 6. Discussion

**Limitations.** The model is deliberately minimal. (i) The scaling law $p_L \approx A (p/p_{\mathrm{th}})^{(d+1)/2}$ is phenomenological; circuit-level noise changes both $A$ and the effective threshold, and our $A = 0.1$, $p_{\mathrm{th}} = 10^{-2}$ are assumptions, not measurements. (ii) $P_q = 10^{-4}\,\mathrm{W}$ per qubit is the dominant uncertainty: all energies scale linearly with it (Section 4.6), and real cryogenic I/O overheads could push the effective value higher. (iii) We count only qubit dissipation; decoder compute energy, refrigerator Carnot overhead (removing $1\,\mathrm{W}$ at millikelvin costs kilowatts at room temperature), and readout laser/microwave generation are excluded, so our figures are lower bounds in scope though uncertain in value. (iv) The $d$-rounds-per-gate convention is one of several; schemes with fewer rounds per logical gate would reduce $E_{\mathrm{op}}$ proportionally.

**Failure modes and falsification.** The claims would be falsified if (a) hardware measurements show effective per-qubit dissipation far below $10^{-4}\,\mathrm{W}$ at scale, collapsing the thermal ratio; (b) code architectures with sub-$d^2$ qubit overhead at fixed $p_L$ become practical (e.g., qLDPC codes), invalidating $N_{\mathrm{phys}} = 2d^2 - 1$; or (c) continuous-time schemes [1] demonstrate comparable logical fidelity at substantially lower measurement bandwidth than $4.4 \times 10^{8}$ bits/s per logical qubit. Conversely, if the QEC-Darwinism no-go bound [11] holds, no passive-redundancy shortcut can evade the active burden, strengthening the case that energy accounting is unavoidable.

**Arguing against ourselves.** One might object that energy per logical qubit is the wrong metric — wall-clock energy per *algorithm* matters, and algorithmic speedups could amortize the burden. That objection concedes rather than refutes the accounting: it changes the numerator's utilization, not the per-cycle cost. A stronger objection is that our two energy conventions (idle vs. active) differ by a factor $d$, and which is "the" cost depends on workload duty cycle; we report both precisely because the storage-versus-computation split is itself architecture-relevant. Finally, the adiabatic route [7] suggests the burden may be paradigm-dependent: error handling there cannot assume high-quality gates, so a different (possibly cheaper, possibly dearer) ledger applies, and our numbers should not be read as universal.

**Open questions.** What is the measured (not assumed) per-qubit dissipation budget in a multi-thousand-qubit cryostat? How does decoder energy scale with syndrome rate? Can entanglement-assisted [2] or quaternionic [8] encodings reduce the distance requirement at fixed $p_L$, and at what consumable cost? Full lifecycle accounting [12] remains outside our scope.

## 7. Conclusion

We have given a fully explicit, assumption-labeled accounting of the resource burden of active quantum error correction for the surface code. At a physical error rate of $10^{-3}$ and threshold $10^{-2}$, achieving a logical error rate of $10^{-12}$ requires distance $d = 21$, hence $881$ physical qubits per logical qubit, $4.40 \times 10^{8}$ syndrome bits per second, and — under an assumed $10^{-4}\,\mathrm{W}$ per-qubit dissipation — $8.81 \times 10^{-8}\,\mathrm{J}$ per microsecond cycle, or $6.38 \times 10^{15}$ times $k_B T$ at $1\,\mathrm{K}$, with $1.85\,\mu\mathrm{J}$ per logical gate. The burden is logarithmically robust to model prefactors but linearly exposed to per-qubit power, making that parameter the critical measurement target for the field. We advocate that QEC architecture papers report energy per logical operation and syndrome bandwidth alongside fidelity, so that the true cost of protection — the price of keeping quantum information alive — becomes a first-class design constraint.

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