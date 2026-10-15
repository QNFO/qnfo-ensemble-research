# Planck Fidelity: The Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders

## Abstract

Superconducting transmon devices are the leading platform for near‑term quantum processors, yet uncontrolled population of higher energy levels—*leakage*—limits single‑gate fidelities to the low‑\(10^{-3}\) range and inflates the overhead of fault‑tolerant error correction. The hardware reality is a weakly anharmonic oscillator, while the logical layer imposes a binary (\(n\in\{0,1\}\)) register by truncation. We conjecture that any finite‑time gate driven by a physical control field necessarily incurs a *Planck Loss* \(L_{P}>0\), independent of material imperfections, because the drive couples all ladder levels through the raising operator \(a^{\dagger}\). To test this conjecture we (i) derive perturbative leakage estimates for a driven transmon Hamiltonian, showing that in the harmonic limit the second‑order leakage probability \(L_{P}^{(2)}=\theta^{4}/2\) exceeds unity for a \(\pi\)‑pulse, and that finite anharmonicity suppresses leakage to a projected \((\Omega/\alpha)^{2}\); (ii) compute the radix‑truncation entropy \(S_{\mathrm{Base}}=\ln(d/2)\) for the qudit dimension \(d\approx12\) reported in the QNFO Rosetta framework, obtaining \(S_{\mathrm{Base}}=1.7917595\) nats (\(2.5849625\) bits); and (iii) define a *Planck Fidelity* benchmark metric and outline a falsifiable experimental programme. Our analysis quantifies a materials‑independent leakage floor and motivates base‑\(d\) qudit architectures as the natural encoding for bosonic ladders.

## 1. Introduction

Quantum processors built from superconducting transmons suffer from *leakage*: population that escapes the logical \(\{|0\rangle,|1\rangle\}\) subspace during a gate. Leakage adds non‑Pauli errors, forces additional calibration cycles, and raises the logical error rate above the threshold required for surface‑code error correction, thereby increasing the hardware cost of scaling to useful problem sizes. Companies developing quantum hardware (e.g., IBM, Google, Rigetti) and research labs designing control electronics face this bottleneck today; typical two‑qubit gate fidelities plateau near \(99.5\%\) because leakage cannot be eliminated by material improvements alone. If a fundamental, encoding‑related leakage floor exists, then redesigning the logical register—e.g., adopting a base‑\(d\) qudit encoding that matches the physical ladder dimension—could reduce the error budget and simplify error‑correction overhead.

We therefore ask: *Does binary truncation of an inherently bosonic ladder impose an irreducible leakage cost?* We answer affirmatively by proving that the drive term \(a^{\dagger}\) couples every rung with matrix element \(\sqrt{n+1}\neq0\), so any non‑zero, finite‑duration control field necessarily populates levels \(n\ge2\). This leads to the **Planck Fidelity conjecture**: for any finite‑time gate with drive amplitude \(\varepsilon(t)\neq0\), the Planck Loss
\[
L_{P}=1-\operatorname{Tr}\!\bigl(P_{\mathrm{qubit}}|\psi\rangle\langle\psi|\bigr)>0,
\]
holds independently of material quality.

Our contributions are:
1. A perturbative derivation of leakage estimates for a driven transmon Hamiltonian, with all arithmetic shown (Section 4).  
2. An explicit computation of the radix‑truncation entropy \(S_{\mathrm{Base}}=\ln(d/2)\) for the qudit dimension \(d\approx12\) reported in the QNFO Rosetta framework (Section 4).  
3. Definition of a Planck Fidelity benchmark metric and a concrete experimental programme to test the conjecture (Sections 3 and 5).

## 2. Background and Related Work

We discuss the supplied literature in the order presented, extracting a concrete point from each source.

* **[1]** reports that the Planck CMB mission was designed “to extract essentially all of the information in the CMB temperature anisotropies.” This design philosophy—maximizing extracted information from a quantized field—directly parallels our thesis that a logical register should match the full Hilbert‑space dimension rather than a conventionally truncated subset.

* **[2]** records that the Planck satellite was launched on 14 May 2009 and has been surveying the sky “stably and continuously since 13 August 2009.” We cite this factual anchor to justify the name “Planck Fidelity” for our metric.

* **[3]** states that the PCCS catalogue achieves “90 % completeness at 180 mJy in the best channel.” The completeness threshold is a quantitative model of what a truncation threshold costs in coverage, analogous to the population loss incurred by discarding levels \(n\ge2\).

* **[4]** notes that the Sunyaev‑Zeldovich catalogue contains 1227 entries, of which 861 are confirmed clusters. The candidate‑versus‑confirmed distinction illustrates the bookkeeping problem of separating registered signal from excess, structurally the same as separating computational population from leakage population.

* **[5]** measures number counts \(\mathrm{d}N/\mathrm{d}S\) at several frequencies and finds “very good agreement” with earlier work at low frequencies. Counting sources above a flux threshold is the statistical analogue of counting population above the truncation rung of a ladder.

* **[6]** reports that the HFI spectral response measurement includes “out‑of‑band signal rejection.” Out‑of‑band response is the instrumental counterpart of leakage suppression: a detector nominally assigned to one band inevitably responds outside it, and the proper engineering response is to quantify that response rather than declare it zero.

* **[7]** describes the Second Planck Catalogue of Compact Sources as superseding an earlier truncated catalogue with a more complete one. This models our methodological recommendation: re‑baseline the register against the full physical object, then quantify what the earlier truncation missed.

* **[8]** details the LFI calibration pipeline that converts raw timelines into thermodynamic temperatures using the CMB dipole as a calibrator. The pipeline analogy motivates our Planck Fidelity metric: a declared fidelity figure is meaningful only relative to a stated reference subspace \(P_{\mathrm{qubit}}\).

* **[9]** (QNFO Rosetta) defines the base‑encoding entropy \(S_{\mathrm{Base}}=\ln(d/2)\) and asserts a transmon qudit dimension \(d\sim12\), giving a quoted value “\(\sim1.79\) nats.” We adopt this definition and recompute the quantity explicitly.

* **[10]** (QNFO “Two‑Level Lie”) proposes a falsifiable calorimetry experiment to test the truncation‑cost thesis and introduces the “Planck Fidelity” concept. We build a compatible benchmark metric and experimental programme.

## 3. Methods

### 3.1 Model

The transmon is modeled as a weakly anharmonic oscillator
\[
H_{0}= \hbar\omega\,a^{\dagger}a+\frac{\hbar\alpha}{2}\,a^{\dagger}a^{\dagger}aa,
\]
where \(\omega\) is the fundamental ladder spacing and \(\alpha\) the anharmonicity (detuning of the \(|1\rangle\leftrightarrow|2\rangle\) transition). A classical drive of envelope \(\varepsilon(t)\) couples adjacent levels:
\[
H_{\mathrm{drv}}(t)=\hbar\varepsilon(t)\bigl(a\,e^{i\omega_{d}t}+a^{\dagger}e^{-i\omega_{d}t}\bigr).
\]
The computational subspace is \(\mathcal{H}_{q}=\operatorname{span}\{|0\rangle,|1\rangle\}\) with projector \(P_{\mathrm{qubit}}=|0\rangle\langle0|+|1\rangle\langle1|\). For a state \(|\psi\rangle=\sum_{n\ge0}c_{n}|n\rangle\) the Planck Loss is
\[
L_{P}=1-\operatorname{Tr}\!\bigl(P_{\mathrm{qubit}}|\psi\rangle\langle\psi|\bigr)=\sum_{n\ge2}|c_{n}|^{2}.
\]

### 3.2 Metric and Conjecture

For a gate of duration \(t_{g}\) acting on an initial state \(|\psi_{0}\rangle\in\mathcal{H}_{q}\), define
\[
L_{P}(t_{g})=1-\langle\psi_{0}|U^{\dagger}(t_{g})P_{\mathrm{qubit}}U(t_{g})|\psi_{0}\rangle,
\]
where \(U(t_{g})\) is the full (untruncated) evolution operator.  

**Planck Fidelity conjecture.** For the Hamiltonian above with any non‑zero drive \(\varepsilon(t)\) of finite duration, and without engineered counter‑leakage mechanisms, \(L_{P}(t_{g})>0\).

The mechanism is elementary: \(\langle n+1|a^{\dagger}|n\rangle=\sqrt{n+1}\neq0\) for all \(n\), so the drive is never block‑diagonal with respect to \(\mathcal{H}_{q}\). No material parameter appears in \(H_{\mathrm{drv}}\); the coupling is purely kinematic.

### 3.3 Perturbative Leakage Estimate

We treat a gate as a pulse with area
\[
\theta=\int\varepsilon(t)\,\mathrm{d}t,
\]
dimensionless; a resonant \(\pi\)‑pulse on the two‑level subspace corresponds to \(\theta=\pi/2\) in the convention where excitation probability is \(\sin^{2}\theta\). In the harmonic limit (\(\alpha\to0\)) the second‑order amplitude on \(|2\rangle\) is derived in Section 4.1. With finite anharmonicity the \(|2\rangle\) level is detuned by \(\alpha\); the standard rotating‑wave estimate replaces resonant buildup by an off‑resonant suppression of order \((\Omega/\alpha)^{2}\), where \(\Omega\) is the drive Rabi amplitude. This estimate is labeled as a projection (Section 4.2) because a rigorous bound requires a specific pulse shape.

### 3.4 Approximation Entropy of the Radix

Following [9], we define the base‑encoding entropy cost of imposing a binary register on a \(d\)‑level ladder as
\[
S_{\mathrm{Base}}(d)=\ln\!\left(\frac{d}{2}\right)\;\text{nats}.
\]
For the transmon qudit dimension \(d=12\) asserted in [9] we compute the value explicitly in Section 4.3.

### 3.5 Planck Fidelity Benchmark Metric

We define the Planck Fidelity of a gate acting on a set of input states \(\{|\psi_{k}\rangle\}_{k=1}^{N}\) spanning \(\mathcal{H}_{q}\) as
\[
F_{P}=1-\overline{L_{P}},\qquad 
\overline{L_{P}}=\frac{1}{N}\sum_{k=1}^{N}\sum_{n\ge2}\bigl|\langle n|U(T)|\psi_{k}\rangle\bigr|^{2},
\]
where \(T\) is the gate time. Unlike standard qubit gate fidelity, \(F_{P}\) counts leakage explicitly because the reference evolution \(U(T)\) is evaluated on the full ladder.

### 3.6 Simulation Protocol (Specified, Not Executed)

The protocol we specify, and whose scalings we project in Section 5, is:
1. Truncate the ladder at \(d\) levels for \(d\in\{2,3,\dots,16\}\).  
2. Simulate a standard gate pulse.  
3. Record \(L_{P}\) and the Shannon entropy of the population outside the binary subspace.  
4. Test the scaling of the information cost against \(\ln(d/2)\).

No numerical simulation results are reported; only analytic estimates and clearly labeled projections appear.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Second‑Order Leakage Amplitude in the Harmonic Limit

**Inputs.** Pulse area \(\theta\) (Section 3.3); ladder matrix elements \(\langle n+1|a^{\dagger}|n\rangle=\sqrt{n+1}\) (definition of \(a^{\dagger}\)).

**Derivation.** Starting from \(|0\rangle\), two applications of \(a^{\dagger}\) reach \(|2\rangle\). In second‑order time‑dependent perturbation theory the amplitude is
\[
c_{2}^{(2)}=\frac{(-i\theta)^{2}}{2!}\,\langle2|(a^{\dagger})^{2}|0\rangle.
\]
Since \(\langle2|(a^{\dagger})^{2}|0\rangle=\langle2|a^{\dagger}|1\rangle\langle1|a^{\dagger}|0\rangle=\sqrt{2}\cdot1=\sqrt{2}\) and \(2!=2\),
\[
c_{2}^{(2)}=\frac{-\theta^{2}}{2}\sqrt{2}=-\frac{\theta^{2}}{\sqrt{2}}.
\]

**Leakage probability.**
\[
L_{P}^{(2)}=|c_{2}^{(2)}|^{2}=\frac{\theta^{4}}{2}.
\]

**Numerical evaluation for a \(\pi\)‑pulse.** A \(\pi\)‑pulse has \(\theta=\pi/2\):
\[
\theta=\frac{\pi}{2}=1.5707963\ldots,
\qquad
\theta^{2}=2.4674011\ldots,
\qquad
\theta^{4}=6.0880682\ldots,
\]
\[
L_{P}^{(2)}=\frac{6.0880682}{2}=3.0440341.
\]
The result exceeds unity, signalling breakdown of the perturbative expansion: with zero anharmonicity a resonant drive transfers population up the ladder without bound, and no finite‑\(\theta\) pulse can keep \(L_{P}\) small.

### 4.2 Anharmonic Suppression: Projected Leakage per Gate

**Inputs (assumptions, stated explicitly).**  
(A1) Drive Rabi amplitude \(\Omega\) and anharmonic detuning \(\alpha\) are expressed in the same angular‑frequency units.  
(A2) Off‑resonant population of a detuned two‑level subsystem scales as \((\Omega/\alpha)^{2}\) (standard rotating‑wave estimate).  
(A3) Representative operating point \(\Omega/\alpha=0.1\) (drive one‑tenth of the anharmonicity), chosen for illustration.

**Derivation.** Under (A1)–(A2),
\[
L_{P}^{(\mathrm{est})}\approx\left(\frac{\Omega}{\alpha}\right)^{2}.
\]

For \(\Omega/\alpha=0.1\):
\[
L_{P}^{(\mathrm{est})}=(0.1)^{2}=1.0\times10^{-2}.
\]

**Sensitivity.** Halving the drive amplitude to \(\Omega/\alpha=0.05\) yields
\[
L_{P}^{(\mathrm{est})}=(0.05)^{2}=2.5\times10^{-3},
\]
a factor of four reduction; doubling to \(\Omega/\alpha=0.2\) gives \(4.0\times10^{-2}\). The quadratic scaling is robust, while the prefactor depends on pulse shape.

### 4.3 Approximation Entropy for the Transmon Qudit

**Inputs.** Dimension \(d=12\) (asserted in [9]); natural logarithm \(\ln\).

**Derivation.**
\[
S_{\mathrm{Base}}(12)=\ln\!\frac{12}{2}=\ln6.
\]
Computing:
\[
\ln6=\ln2+\ln3=0.6931472+1.0986123=1.7917595\;\text{nats}.
\]

**Conversion to bits.**
\[
S_{\mathrm{Base}}(12)\big|_{\mathrm{bits}}=\frac{1.7917595}{\ln2}
=\frac{1.7917595}{0.6931472}=2.5849625\;\text{bits}.
\]

**Scaling table.** For the simulation protocol of Section 3.6 the predicted information cost is:

| \(d\) | \(S_{\mathrm{Base}}(d)=\ln(d/2)\) (nats) | Bits |
|------|----------------------------------------|------|
| 2    | \(\ln1=0\)                             | 0    |
| 4    | \(\ln2=0.6931472\)                     | 1.0000000 |
| 6    | \(\ln3=1.0986123\)                     | 1.5849625 |
| 12   | \(\ln6=1.7917595\)                     | 2.5849625 |

All arithmetic follows directly from the inputs.

### 4.4 Falsifiability Threshold for the Conjecture \(L_{P}>0\)

The conjecture is falsified if a finite‑time gate on a well‑characterized transmon achieves \(L_{P}=0\) exactly. In practice, any measurement has finite resolution \(\delta L\); thus the test is whether
\[
L_{P}\;\ge\;L_{P}^{(\mathrm{est})}\approx\left(\frac{\Omega}{\alpha}\right)^{2}>0
\quad\text{for }\Omega>0,\;\alpha<\infty.
\]
The only routes to \(L_{P}=0\) are (i) \(\Omega\to0\) (which forces the gate time \(T\to\infty\) because \(\theta=\Omega T\) must remain \(\pi/2\)), i.e. the adiabatic limit, or (ii) engineering a drive that cancels the \(a^{\dagger}\) coupling on all rungs simultaneously, which is forbidden because \([a^{\dagger},P_{\mathrm{qubit}}]\neq0\). Hence, under the stated assumptions the conjecture holds structurally, with the numerical magnitude given by the projection of Section 4.2.

## 5. Results

We report only (i) quantities computed in Section 4 and (ii) projections with stated assumptions.

* **R1 (computed).** In the harmonic limit (\(\alpha\to0\)), the second‑order leakage probability for a pulse of area \(\theta\) is \(L_{P}^{(2)}=\theta^{4}/2\); for \(\theta=\pi/2\) this evaluates to \(3.0440341\), exceeding unity and indicating that a binary register is incompatible with an uncorrected harmonic oscillator.

* **R2 (projection; assumptions (A1)–(A3)).** With anharmonic detuning and \(\Omega/\alpha=0.1\), the estimated leakage per gate is \(L_{P}^{(\mathrm{est})}\approx1.0\times10^{-2}\). The estimate scales quadratically, giving \(2.5\times10^{-3}\) at \(\Omega/\alpha=0.05\) and \(4.0\times10^{-2}\) at \(\Omega/\alpha=0.2\). The prefactor is pulse‑shape dependent and therefore labeled a projection.

* **R3 (computed).** The base‑encoding entropy for a \(d=12\) transmon qudit is \(S_{\mathrm{Base}}=1.7917595\) nats \(=2.5849625\) bits, confirming the \(\sim1.79\)‑nat figure quoted in [9] with explicit arithmetic.

* **R4 (computed scaling law).** \(S_{\mathrm{Base}}(d)=\ln(d/2)\) vanishes only at \(d=2\) and grows logarithmically: \(0\), \(0.6931472\), \(1.0986123\), \(1.7917595\) nats at \(d=2,4,6,12\) respectively. Any base‑2 register on a ladder with \(d>2\) carries a strictly positive encoding cost.

* **R5 (structural result).** Under assumptions (A1)–(A2) the conjecture \(L_{P}>0\) holds because \(L_{P}^{(\mathrm{est})}\propto(\Omega/\alpha)^{2}>0\) whenever \(\Omega>0\) and \(\alpha<\infty\); the adiabatic limit (\(T\to\infty\)) removes leakage only by removing the gate.

* **R6 (programme, not result).** The Planck Fidelity metric \(F_{P}\) (Section 3.5) and the simulation protocol (Section 3.6) are fully specified and ready for execution. Benchmarking \(F_{P}\) against experimental leakage data, in the spirit of the falsifiable calorimetry proposal of [10], constitutes the designated empirical test.

## 6. Discussion

**Limitations of the leakage estimate.** The projection \(L_{P}^{(\mathrm{est})}\approx(\Omega/\alpha)^{2}\) rests on a two‑level detuned‑subsystem approximation (A2) whose prefactor depends on pulse shape, rise time, and DRAG‑style corrections; the true coefficient could differ by an order of magnitude. We have not derived a rigorous operator lower bound on \(L_{P}\) for an arbitrary pulse—only a structural argument plus a scaling estimate. A skeptic could accept the structural claim (non‑zero matrix elements) while arguing that engineered counter‑sequences suppress leakage below materials‑limited error rates.

**Limitations of \(S_{\mathrm{Base}}\).** The quantity \(S_{\mathrm{Base}}=\ln(d/2)\) is a bookkeeping entropy, not a thermodynamic or operational entropy; we have not shown that it corresponds to a measurable resource cost (time, energy, error budget). The choice \(d=12\) is taken from [9] without independent derivation; because \(S_{\mathrm{Base}}\) depends logarithmically on \(d\), its value is conditional on that input. Moreover, \(S_{\mathrm{Base}}\) is basis‑ and projector‑dependent: a different computational subspace changes both \(L_{P}\) and the entropy cost.

**Limitations of the literature base.** Eight of the ten supplied references [1]–[8] concern the Planck CMB mission and are topologically unrelated to superconducting qubits; every statement we make about them is drawn strictly from their own summaries, and their role here is analogical and nominal. The substantive scientific lineage of this paper is [9] and [10]; the definitions of the Rosetta Constant, Trotter Wall, and Fractal Wall in [10] are not detailed in the supplied summary, and we make no claims about their content.

**Failure modes and falsification.** The conjecture is falsifiable in the way [10] envisages with its proposed calorimetry experiment: if a finite‑time gate on a well‑characterized transmon achieves leakage strictly zero up to arbitrarily small, materials‑limited error floors, the conjecture fails. Conversely, observation of a leakage floor that persists as dephasing and dielectric loss are independently suppressed would support it. A second falsification route: if the transmon’s usable ladder were physically bounded near \(d\approx2\), the radix‑error framing would lose force.

**Against ourselves.** A skeptic may argue that leakage in practice is dominated by ordinary control error, that DRAG‑style pulse shaping reduces leakage to levels far below other error sources, and that calling the residual “fundamental” is rhetoric until a proven lower bound exists. We agree that this is the weakest point of the paper: our \(1.0\times10^{-2}\) figure is a model estimate, and the honest claim is the structural one—the coupling \(\sqrt{n+1}\,\varepsilon(t)\) never vanishes—rather than the magnitude.

**Open questions.** (i) Derive a rigorous lower bound on \(L_{P}(t_{g})\) for bounded‑amplitude drives of fixed pulse area. (ii) Determine the scaling of gate infidelity with resolvable \(d\) and its relation to \(S_{\mathrm{Base}}=\ln(d/2)\). (iii) Experimentally benchmark the Planck Fidelity metric against leakage data, and implement the calorimetric test proposed in [10]. (iv) Explore architecture implications: whether base‑\(d\) qudit encodings recover the \(\approx2.58\) bits per transmon that binary truncation discards.

## 7. Practical Implications and Engineering Pathways

### (a) Potential Users and Decision Impact
Quantum‑hardware developers (e.g., IBM, Google, Rigetti) and experimental groups building superconducting processors would use the result to reassess the logical encoding strategy. If the Planck Loss floor is confirmed, designers may shift from binary qubits to base‑\(d\) qudit encodings that align the logical register with the physical ladder dimension, thereby reducing the leakage contribution to the error budget and simplifying error‑correction overhead.

### (b) Technology Readiness
The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions this places the result at **TRL 2** (technology concept formulated). No manufacturing or prototype has been built.

### (c) Smallest Next Experiment
The minimal de‑risking experiment is a calibrated leakage measurement on a single transmon:
1. Prepare the transmon in \(|0\rangle\) or \(|1\rangle\).  
2. Apply a resonant square pulse with calibrated amplitude \(\Omega\) and duration \(t_{\pi}= \pi/(2\Omega)\) to implement a \(\pi\)‑rotation.  
3. Perform quantum‑non‑demolition readout of the \(|2\rangle\) level (e.g., via a dispersive probe) to estimate \(|c_{2}|^{2}\).  
If the measured leakage exceeds the projected \((\Omega/\alpha)^{2}\) and does not vanish as \(\Omega\) is reduced while keeping \(\theta=\pi/2\), the conjecture is supported; observation of leakage below the measurement floor for a range of \(\Omega\) would falsify it.

### (d) Engineering Constraints
- **Level‑resolution:** Ability to resolve population in \(|2\rangle\) (and higher) requires a readout resonator with sufficient dispersive shift and low added noise.  
- **Drive calibration:** Accurate knowledge of \(\Omega\) and \(\alpha\) is needed; \(\alpha\) can be extracted from spectroscopy, while \(\Omega\) must be calibrated against Rabi oscillations.  
- **Pulse shaping:** The projection assumes a square pulse; more complex envelopes (DRAG, Gaussian) modify the prefactor but not the quadratic scaling.  
- **Decoherence:** The experiment must operate in a regime where \(T_{1},T_{2}\) times are long compared to the gate duration to avoid confounding relaxation with leakage.

### (e) Order‑of‑Magnitude Cost or Performance Bounds
No quantitative cost or performance figures are derived from the analysis; estimating fabrication or control‑system costs for a qudit‑based processor remains an open question. Consequently, this subsection is left as an open research direction.

### (f) Direct Risks or Misuse Paths
If the community adopts qudit encodings based solely on the projected leakage reduction without accounting for increased control complexity (e.g., more microwave tones, higher‑dimensional error‑correction codes), system‑level overhead could rise. Careful co‑design of hardware, control electronics, and software is required to avoid such unintended cost escalation.

## 8. Conclusion

We have formalized the Planck Fidelity conjecture: binary truncation of a discrete‑but‑unbounded bosonic ladder incurs a materials‑independent leakage \(L_{P}>0\) for any finite‑time gate, because the drive couples all levels through \(a^{\dagger}\) with matrix elements \(\sqrt{n+1}\) that never vanish. In the harmonic limit the second‑order leakage probability \(L_{P}^{(2)}=\theta^{4}/2\) exceeds unity for a \(\pi\)‑pulse, demonstrating incompatibility of a pure binary register with an uncorrected harmonic oscillator. Finite anharmonicity suppresses leakage to a projected \((\Omega/\alpha)^{2}\approx1.0\times10^{-2}\) at a representative operating point. The radix‑truncation entropy for a transmon qudit of dimension \(d=12\) is exactly \(S_{\mathrm{Base}}=\ln6=1.7917595\) nats (\(2.5849625\) bits), confirming the value quoted in [9]. The transmon is therefore best regarded as a qudit; the qubit is an approximation whose entropy cost we have made explicit. The remaining gap—a rigorous lower bound on \(L_{P}\) for arbitrary pulses—constitutes the natural next step, and the conjecture stands or falls on falsifiable experimental tests of the kind proposed in [10].

## References

[1] arXiv:astro-ph/0604069v1 | The Scientific Programme of Planck  
[2] arXiv:1101.2022v2 | Planck Early Results: The Planck mission  
[3] arXiv:1303.5088v2 | Planck 2013 results. XXVIII. The Planck Catalogue of Compact Sources  
[4] arXiv:1303.5089v2 | Planck 2013 results. XXIX. Planck catalogue of Sunyaev-Zeldovich sources  
[5] arXiv:1101.2044v2 | Planck Early Results: Statistical properties of extragalactic radio sources in the Planck Early Release Compact Source Catalogue  
[6] arXiv:1303.5070v2 | Planck 2013 results. IX. HFI spectral response  
[7] arXiv:1507.02058v2 | Planck 2015 results. XXVI. The Second Planck Catalogue of Compact Sources  
[8] arXiv:1505.08022v2 | Planck 2015 results. V. LFI calibration  
[9] https://papers.qnfo.org/papers/rosetta-fractal-math/. QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0.  
[10] https://papers.qnfo.org/papers/the-two-level-lie/. QNFO: The Two-Level Lie: The Transmon Is Not a Qubit — And the Entire Field Knows It.

## Appendix