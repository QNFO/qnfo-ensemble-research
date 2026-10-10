# Planck Fidelity: The Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders

## Abstract

We propose that the transmon qubit is not a natural two-level system but an artificially truncated bosonic ladder: a Planck-quantized, effectively unbounded oscillator onto which a binary ($n \in \{0,1\}$) register has been imposed by convention. Because any physical drive couples the computational levels to higher rungs of the ladder through the raising operator $a^\dagger$, we conjecture that a quantity we call Planck Loss, $L_P = 1 - \mathrm{Tr}(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|)$, is strictly positive for any finite-time gate, independent of materials imperfections — a fundamental cost of base-2 encoding on a base-$d$ physical object. We (i) derive perturbative lower-bound estimates of $L_P$ for a driven transmon-type Hamiltonian, showing that the second-order leakage amplitude scales as $\theta^2/(2\sqrt{2})$ in the harmonic limit and is suppressed only by the anharmonicity ratio $\Omega/\alpha$ in the anharmonic case; (ii) quantify the encoding cost of binary truncation as an approximation entropy $S_{\mathrm{Base}} = \ln(d/2)$, which evaluates to $\ln 6 \approx 1.7918$ nats $\approx 2.5850$ bits for a qudit of dimension $d = 12$; and (iii) define a Planck Fidelity benchmark metric whose comparison with experimental leakage data is outlined as a testable programme. We argue that qudit (base-$d$) architectures are the natural encoding and that the qubit is a radix error, not a physics error.

## 1. Introduction

Quantum information processing has overwhelmingly adopted the base-2 register: the qubit. Yet the physical objects from which qubits are carved — superconducting islands whose Cooper-pair number is quantized, transmon modes whose energy spectrum is discrete — are not two-level systems. The transmon is a weakly anharmonic oscillator with a ladder of levels $|n\rangle$, $n = 0, 1, 2, \dots$, of which the hardware resolves many. The binary register is imposed on this ladder by truncation: the projector $P_{\mathrm{qubit}} = |0\rangle\langle 0| + |1\rangle\langle 1|$ is declared to be the system, and everything outside it is declared "leakage."

This paper takes that declaration seriously as a source of irreducible error. The claim is simple: the drive that implements any gate contains the raising operator $a^\dagger$, which by construction couples $|n\rangle$ to $|n+1\rangle$ for every $n$. A finite-time gate therefore always populates levels outside the binary subspace, no matter how good the materials are. We call the resulting population loss Planck Loss,

$$L_P = 1 - \mathrm{Tr}\!\left(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|\right),$$

and conjecture that $L_P > 0$ for any finite gate time, as a property of the encoding rather than of the fabrication.

The name is chosen deliberately. The quantization of physical action — the fact that the oscillator ladder is discrete with fixed spacing — is the reason a truncation is possible at all and the reason its cost is quantifiable. The European Space Agency's Planck satellite, named for the same physicist, was launched on 14 May 2009 and has been surveying the sky stably and continuously since 13 August 2009 [2]; its scientific programme was designed to extract essentially all of the information in the cosmic microwave background temperature anisotropies [1]. That programme — extract all of the information a quantized physical channel carries, rather than a conventionally selected subset of it — is precisely the attitude we argue quantum hardware should adopt toward the bosonic ladder.

Our contributions are:

1. A perturbative derivation of lower-bound estimates on $L_P$ for a driven transmon Hamiltonian, with all arithmetic shown (Section 4).
2. An information-theoretic accounting of the binary truncation as an approximation entropy $S_{\mathrm{Base}} = \ln(d/2)$, evaluated for a qudit of dimension $d \approx 12$ following the QNFO Rosetta framework [9],[10].
3. A definition of a Planck Fidelity benchmark metric and a concrete programme for testing the conjecture $L_P > 0$ against experimental leakage data (Sections 3 and 5).

Throughout, "leakage" means population outside the computational subspace; "radix" means the base of the logical register ($2$ for a qubit, $d$ for a qudit); "nats" means logarithms in base $e$.

## 2. Background and Related Work

We discuss the supplied literature in its given order. A caveat applies throughout: the eight arXiv entries concern the Planck CMB mission, not superconducting qubits; we cite them for what their summaries state, and use them as methodological and conceptual analogies, which we flag explicitly each time.

[1] The Scientific Programme of Planck (arXiv:astro-ph/0604069v1) states that for 40 years the cosmic microwave background has been the most important source of information about the geometry and contents of the Universe, that only a small fraction of the information available in the CMB has been extracted to date, and that Planck, the third space CMB mission after COBE and WMAP, is designed to extract essentially all of the information in the CMB temperature anisotropies. The design philosophy — extract all the information the quantized field carries, not a conventionally truncated subset — is the exact analogue of our thesis that a register should match the physical Hilbert-space dimension rather than a chosen binary slice of it.

[2] Planck Early Results: The Planck mission (arXiv:1101.2022v2) records that the European Space Agency's Planck satellite was launched on 14 May 2009 and has been surveying the sky stably and continuously since 13 August 2009, with performance well in line with expectations, and gives an overview of the history of the mission in its first year. We cite it as the factual anchor for the mission whose name we borrow; its summary supplies no further detail relevant to qubit physics.

[3] Planck 2013 results. XXVIII. The Planck Catalogue of Compact Sources (arXiv:1303.5088v2) describes the PCCS, a set of nine single-frequency catalogues of compact Galactic and extragalactic sources detected over the entire sky in the first 15 months of operations, covering 30–857 GHz with 90% completeness at 180 mJy in the best channel. The catalogue is itself an act of truncation: sources below a sensitivity threshold are declared outside the registered set, exactly as levels above $n = 1$ are declared outside the qubit. The stated completeness figure is a quantitative model for what a truncation threshold costs in coverage.

[4] Planck 2013 results. XXIX. Planck catalogue of Sunyaev-Zeldovich sources (arXiv:1303.5089v2) presents an all-sky catalogue of clusters and cluster candidates derived from Sunyaev–Zeldovich detections over the first 15.5 months, containing 1227 entries — over six times the size of the Planck Early SZ sample and the largest SZ-selected catalogue to date — of which 861 are confirmed clusters and 178 have (the summary is cut off at this point). The candidate-versus-confirmed distinction (1227 versus 861) illustrates the general accounting problem of separating registered signal from registered-but-unvalidated excess, which is structurally the same bookkeeping as separating computational population from leakage population.

[5] Planck Early Results: Statistical properties of extragalactic radio sources (arXiv:1101.2044v2) uses the Early Release Compact Source Catalogue to measure the number counts $\mathrm{d}N/\mathrm{d}S$ of extragalactic radio sources at 30, 44, 70, 100, 143 and 217 GHz, extending to the rarest and brightest sources because of the full-sky nature of the catalogue, with counts at 30, 44 and 70 GHz in very good agreement with e(xisting models; the summary is truncated). Counting population above a flux threshold is the direct statistical analogue of counting population above the truncation rung of a ladder; we use it only as this analogy.

[6] Planck 2013 results. IX. HFI spectral response (arXiv:1303.5070v2) reports that the High Frequency Instrument spectral response was determined through ground-based tests of the focal plane in a cryogenic environment prior to launch, the goal being to measure the relative spectral response including out-of-band signal rejection of all HFI detectors. Out-of-band rejection is the instrumental counterpart of leakage suppression: a detector nominally assigned to one frequency band inevitably responds outside it, and the honest engineering response is to measure and quantify that response rather than declare it zero. This is precisely the epistemic stance we demand for transmon leakage.

[7] Planck 2015 results. XXVI. The Second Planck Catalogue of Compact Sources (arXiv:1507.02058v2) is a catalogue of compact sources detected in single-frequency maps over the full mission duration and supersedes previous versions, consisting of compact sources over the entire sky with lower-frequency channels assigned to the PC (summary truncated). The act of superseding an earlier truncated catalogue with a longer-integration, more complete one models our central methodological recommendation: re-baseline the register against the full physical object, then quantify what the earlier truncation missed.

[8] Planck 2015 results. V. LFI calibration (arXiv:1505.08022v2) describes the pipeline used to calibrate Low Frequency Instrument timelines into thermodynamic temperatures over four years of uninterrupted operations, using as calibrator the spin-synchronous modulation of the CMB dipole as in the 2013 release, but now also the orbital component (summary truncated). A calibration pipeline that converts raw physical signal into a declared unit system, with a known reference, is the structural template for our Planck Fidelity metric: a declared fidelity figure is meaningful only relative to a stated reference subspace.

[9] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 (DOI 10.5281/zenodo.21486780) is the direct conceptual source of this paper. Its v2.0 applies a "Planck-Radix Correction": it corrects an earlier version by affirming that the transmon spectrum IS discrete (Planck quantization), so that binary truncation is a radix error, not a physics error; it asserts that the transmon is a qudit of dimension $d \sim 12$, not a qubit; and it defines $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats as the base-encoding entropy cost. We adopt the quantity $S_{\mathrm{Base}}$, re-derive its value with explicit arithmetic in Section 4, and formalize the accompanying leakage conjecture.

[10] QNFO: The Two-Level Lie: The Transmon Is Not a Qubit — And the Entire Field Knows It (DOI 10.5281/zenodo.21484345) adds, in its v2.0 Part II, "The Approximation Entropy," described as a meta-mathematical framework quantifying the irreducible cost of translating continuous bosonic physics to discrete digital computation, and introduces a Rosetta Constant, a Trotter Wall, and a Fractal Wall theorem with a falsifiable calorimetry experimental proposal. The supplied summary gives no further detail on the definitions of these objects; we therefore use it only as evidence that a falsifiable experimental programme for the truncation-cost thesis has been proposed, and we design our own benchmark (Section 3) to be compatible in spirit with a calorimetric test.

## 3. Methods

### 3.1 Model

We model the transmon as a weakly anharmonic oscillator,

$$H_0 = \hbar\,\omega\, a^\dagger a + \frac{\hbar\,\alpha}{2}\, a^\dagger a^\dagger a\, a,$$

where $\omega$ is the ladder spacing, $\alpha$ the anharmonicity (the detuning of the $|1\rangle \leftrightarrow |2\rangle$ transition from $\omega$), and $a$, $a^\dagger$ the ladder operators satisfying $a^\dagger|n\rangle = \sqrt{n+1}\,|n{+}1\rangle$. A classical drive of envelope $\varepsilon(t)$ couples all adjacent levels:

$$H_{\mathrm{drv}}(t) = \hbar\,\varepsilon(t)\,\left(a\,e^{i\omega_d t} + a^\dagger e^{-i\omega_d t}\right),$$

with drive frequency $\omega_d$. The computational (qubit) subspace is $\mathcal{H}_q = \mathrm{span}\{|0\rangle, |1\rangle\}$ with projector $P_{\mathrm{qubit}} = |0\rangle\langle 0| + |1\rangle\langle 1|$, and Planck Loss for a state $|\psi\rangle$ is

$$L_P = 1 - \mathrm{Tr}\!\left(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|\right) = \sum_{n \geq 2} |c_n|^2, \qquad |\psi\rangle = \sum_{n \geq 0} c_n |n\rangle.$$

### 3.2 Perturbative leakage bound

Write the gate as a unitary pulse with pulse area $\theta = \int \varepsilon(t)\,\mathrm{d}t$ (dimensionless; a $\pi$-pulse on the two-level subspace has $\theta = \pi/2$ in the Rabi convention where excitation probability is $\sin^2\theta$). Expanding the time-evolution in the interaction picture, the amplitude on level $|2\rangle$ receives, in the harmonic limit ($\alpha \to 0$, all rungs resonant), a second-order contribution

$$c_2^{(2)} = \frac{(-i\theta)^2}{2!}\,\langle 2| (a^\dagger)^2 |0\rangle = -\frac{\theta^2}{2}\cdot\frac{\sqrt{2}}{1} \cdot \frac{1}{\sqrt{2}} \;,$$

evaluated carefully below in Section 4. With finite anharmonicity $\alpha$, level $|2\rangle$ is detuned by $\alpha$ from the drive, and the standard rotating-wave estimate replaces the resonant buildup by an off-resonant suppression factor of order $(\Omega/\alpha)^2$, where $\Omega$ is the drive Rabi amplitude; we state this as a projection with explicit assumptions in Section 4, since a rigorous bound requires a specific pulse shape.

### 3.3 Approximation entropy of the radix

Following [9], we define the base-encoding entropy cost of imposing a binary register on a $d$-level ladder as

$$S_{\mathrm{Base}}(d) = \ln\!\frac{d}{2},$$

i.e., the information in nats by which the physical ladder exceeds the binary register. For $d = 2$ (an idealized two-level object) $S_{\mathrm{Base}} = 0$; for the transmon qudit with $d \approx 12$ as asserted in [9], we compute $S_{\mathrm{Base}}$ explicitly in Section 4.

### 3.4 Planck Fidelity benchmark metric

We define the Planck Fidelity of a gate acting on input $|\psi_k\rangle$ as

$$F_P = 1 - \overline{L_P}, \qquad \overline{L_P} = \frac{1}{N}\sum_{k=1}^{N} \sum_{n \geq 2} |\langle n| U(T) |\psi_k\rangle|^2,$$

where $T$ is the gate time, $U(T)$ the full (untruncated) evolution operator, and the average runs over a set of $N$ input states spanning $\mathcal{H}_q$. The metric differs from a standard qubit gate fidelity in that the reference evolution $U(T)$ is evaluated on the full ladder, so that leakage is counted as error by construction rather than absorbed into a truncated simulation. The calibration-pipeline analogy of [8] applies: $F_P$ is meaningful only relative to the declared reference subspace $P_{\mathrm{qubit}}$, which must be stated with the metric.

### 3.5 Simulation protocol (specified, not executed)

The protocol we specify, and whose scalings we project in Section 5, is: (1) truncate the ladder at $d$ levels for $d \in \{2, 3, \dots, 16\}$; (2) simulate a standard gate pulse; (3) record $L_P$ and the Shannon entropy of the population outside the binary subspace; (4) test the scaling of the information cost against $\ln(d/2)$. No numerical simulation results are reported in this paper; only analytic estimates and clearly labeled projections.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Second-order leakage amplitude in the harmonic limit

**Inputs.** Pulse area $\theta$ (model parameter, Section 3.2); ladder matrix elements $\langle n{+}1|a^\dagger|n\rangle = \sqrt{n+1}$ (from the definition of $a^\dagger$).

**Derivation.** Starting from $|0\rangle$, two applications of the raising operator reach $|2\rangle$. In second-order perturbation theory the amplitude is

$$c_2^{(2)} = \frac{(-i\theta)^2}{2!}\,\langle 2 | (a^\dagger)^2 | 0 \rangle.$$

Now $\langle 2|(a^\dagger)^2|0\rangle = \langle 2|a^\dagger|1\rangle\,\langle 1|a^\dagger|0\rangle = \sqrt{2}\cdot 1 = \sqrt{2}$, and $2! = 2$, so

$$c_2^{(2)} = \frac{-\theta^2}{2}\cdot\sqrt{2} = -\frac{\theta^2}{\sqrt{2}}.$$

Wait — we must be careful with the convention: with $\theta$ defined so that first-order excitation probability is $\sin^2\theta$, the first-order amplitude is $c_1^{(1)} = -i\theta$, hence the pulse area per application of $a^\dagger$ is $\theta$ and the two-step amplitude is $c_2^{(2)} = \frac{(-i\theta)^2}{2!}\cdot\sqrt{2} = -\frac{\theta^2\sqrt{2}}{2} = -\frac{\theta^2}{\sqrt{2}}$.

**Leakage probability.**

$$L_P^{(2)} = |c_2^{(2)}|^2 = \frac{\theta^4}{2}.$$

**Numerical evaluation for a $\pi$-pulse.** A $\pi$-pulse has $\theta = \pi/2$ (so that $\sin^2\theta = 1$). Then

$$\theta = \frac{\pi}{2} = 1.5707963\ldots, \qquad \theta^2 = 2.4674011\ldots, \qquad \theta^4 = 6.0880682\ldots,$$

$$L_P^{(2)} = \frac{6.0880682}{2} = 3.0440341.$$

This exceeds unity, which signals the breakdown of second-order perturbation theory in the harmonic limit: with zero anharmonicity, a resonant drive does not merely leak — it transfers population up the ladder without bound, and the perturbative series diverges. The correct reading of the calculation is qualitative but sharp: **in the harmonic limit there is no finite-$\theta$ pulse that keeps $L_P$ small; the binary register is incompatible with the physics.** Perturbation theory is valid only when anharmonicity detunes the higher rungs, to which we now turn.

### 4.2 Anharmonic suppression: projected leakage per gate

**Inputs (assumptions, stated explicitly).** (A1) The drive Rabi amplitude is $\Omega$ and the $|1\rangle\leftrightarrow|2\rangle$ anharmonic detuning is $\alpha$, both in the same angular-frequency units. (A2) The off-resonant suppression of population on the detuned rung is of order $(\Omega/\alpha)^2$, the standard rotating-wave estimate for a two-level detuned subsystem. (A3) A representative operating point $\Omega/\alpha = 0.1$ (i.e., the drive is one tenth of the anharmonicity), chosen for illustration; no experimental value is claimed.

**Derivation.** Under (A1)–(A2),

$$L_P^{(\mathrm{est})} \approx \left(\frac{\Omega}{\alpha}\right)^2.$$

For $\Omega/\alpha = 0.1$:

$$L_P^{(\mathrm{est})} = (0.1)^2 = 1.0 \times 10^{-2}.$$

**Sensitivity.** Because the estimate is quadratic in the assumed ratio, halving the drive amplitude to $\Omega/\alpha = 0.05$ gives

$$L_P^{(\mathrm{est})} = (0.05)^2 = 2.5 \times 10^{-3},$$

a factor of $4$ reduction; doubling to $\Omega/\alpha = 0.2$ gives $(0.2)^2 = 4.0\times 10^{-2}$. The projection is therefore robust in its scaling but uncertain in its prefactor, which depends on pulse shape — an uncertainty we carry into Section 6. **This is a projection under assumptions (A1)–(A3), not a measurement.**

### 4.3 Approximation entropy for the transmon qudit

**Inputs.** $d = 12$ (the transmon qudit dimension asserted in [9]); $\ln$ denotes natural logarithm.

**Derivation.**

$$S_{\mathrm{Base}}(12) = \ln\!\frac{12}{2} = \ln 6.$$

Computing: $\ln 6 = \ln 2 + \ln 3 = 0.6931472 + 1.0986123 = 1.7917595$ nats.

This matches the value $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats stated in [9]. Converted to bits:

$$S_{\mathrm{Base}}(12)\big|_{\mathrm{bits}} = \frac{1.7917595}{\ln 2} = \frac{1.7917595}{0.6931472} = 2.5849625 \ \text{bits}.$$

**Scaling table.** For the simulation protocol of Section 3.5, the predicted information cost is:

| $d$ | $S_{\mathrm{Base}}(d) = \ln(d/2)$ (nats) | (bits) |
|---|---|---|
| 2 | $\ln 1 = 0$ | 0 |
| 4 | $\ln 2 = 0.6931$ | 1.0000 |
| 6 | $\ln 3 = 1.0986$ | 1.5850 |
| 12 | $\ln 6 = 1.7918$ | 2.5850 |

(arithmetic: $\ln 2 = 0.6931472$, $\ln 3 = 1.0986123$; bits via division by $\ln 2 = 0.6931472$.)

### 4.4 Falsifiability threshold for the conjecture $L_P > 0$

The conjecture of Section 1 is falsified if a finite-time gate on a physical transmon achieves $L_P = 0$ exactly. Operationally, since any measurement has finite resolution $\delta L$, the conjecture is tested by the chain of bounds:

$$L_P \;\geq\; L_P^{(\mathrm{est})} \approx \left(\frac{\Omega}{\alpha}\right)^2 \;>\; 0 \quad \text{for } \Omega > 0,\ \alpha < \infty.$$

Under assumptions (A1)–(A2), $L_P^{(\mathrm{est})}$ is strictly positive for any nonzero drive over a finite time; the only escape routes are $\Omega \to 0$ (gate time $T \to \infty$, since $\theta = \Omega T$ for a square pulse, so $\Omega T = \pi/2$ forces $\Omega = \pi/(2T)$ and $L_P^{(\mathrm{est})} \approx \frac{\pi^2}{4\alpha^2 T^2} \to 0$ only as $T \to \infty$) — which is the adiabatic limit, not a finite-time gate — or a drive engineered to exactly cancel the $a^\dagger$ coupling on all rungs simultaneously, which the structure $[a^\dagger, P_{\mathrm{qubit}}] \neq 0$ forbids for a subspace-preserving pulse. We state this as a derivation of the *structure* of the conjecture, with the numerical magnitude carried by the projection of Section 4.2.

## 5. Results

We report only (i) quantities computed in Section 4 and (ii) projections with stated assumptions.

**R1 (computed).** In the harmonic limit ($\alpha \to 0$), the second-order leakage amplitude for a pulse of area $\theta$ is $c_2^{(2)} = -\theta^2/\sqrt{2}$, giving $L_P^{(2)} = \theta^4/2$; for $\theta = \pi/2$ this evaluates to $3.044$, exceeding unity and signaling perturbative breakdown — i.e., the harmonic oscillator admits no perturbatively small-leakage binary gate at all.

**R2 (projection; assumptions (A1)–(A3)).** With anharmonic detuning and $\Omega/\alpha = 0.1$, the estimated leakage per gate is $L_P^{(\mathrm{est})} \approx 1.0\times 10^{-2}$; the estimate scales as $(\Omega/\alpha)^2$, giving $2.5\times 10^{-3}$ at $\Omega/\alpha = 0.05$ and $4.0\times 10^{-2}$ at $\Omega/\alpha = 0.2$. Uncertainty: the prefactor is pulse-shape dependent and is not fixed by this paper; only the quadratic scaling is asserted.

**R3 (computed).** The base-encoding entropy of a $d = 12$ transmon qudit is $S_{\mathrm{Base}} = \ln 6 = 1.7917595$ nats $= 2.5849625$ bits, confirming the $\sim 1.79$-nat figure of [9] with explicit arithmetic.

**R4 (computed scaling law).** $S_{\mathrm{Base}}(d) = \ln(d/2)$ vanishes only at $d = 2$ and grows logarithmically: $0$, $0.6931$, $1.0986$, $1.7918$ nats at $d = 2, 4, 6, 12$ respectively. Any base-2 register on a ladder with $d > 2$ carries a strictly positive encoding cost under this definition.

**R5 (structural result).** The conjecture $L_P > 0$ for finite-time gates holds under assumptions (A1)–(A2) because $L_P^{(\mathrm{est})} \propto (\Omega/\alpha)^2 > 0$ whenever $\Omega > 0$ and $\alpha < \infty$; the adiabatic route ($T \to \infty$) removes the leakage only by removing the gate.

**R6 (programme, not result).** The Planck Fidelity metric $F_P$ of Section 3.4 and the simulation protocol of Section 3.5 are specified and ready for execution; no simulation or experimental numbers are reported here. Benchmarking $F_P$ against experimental leakage data, in the spirit of the falsifiable calorimetry proposal of [10], is the designated empirical test.

## 6. Discussion

**Limitations of the leakage estimate.** The projection $L_P^{(\mathrm{est})} \approx (\Omega/\alpha)^2$ rests on a two-level detuned-subsystem approximation (A2) whose prefactor depends on pulse shape, rise time, and DRAG-style corrections; the true coefficient could differ by an order of magnitude. We have not derived a rigorous operator lower bound on $L_P$ for a general pulse — only a structural argument plus a scaling estimate. A skeptic could accept the structural claim ($a^\dagger$ couples all rungs) while denying that the resulting leakage is practically significant, if engineered counter-sequences suppress it below materials-limited error rates.

**Limitations of $S_{\mathrm{Base}}$.** The quantity $S_{\mathrm{Base}} = \ln(d/2)$ is adopted from [9] and is a bookkeeping entropy, not a thermodynamic or operational entropy; we have not shown that it corresponds to any measurable resource cost (time, energy, error budget). The choice $d = 12$ is asserted in [9] but not derived here; a different resolved-level count changes the number ($\ln(d/2)$ at $d = 8$ gives $\ln 4 = 1.3863$ nats, at $d = 16$ gives $\ln 8 = 2.0794$ nats — arithmetic: $\ln 4 = 2\ln 2 = 1.3862944$, $\ln 8 = 3\ln 2 = 2.07