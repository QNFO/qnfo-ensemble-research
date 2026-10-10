# Planck Fidelity: The Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders

## Abstract

We propose and formalize a conjecture we call Planck Fidelity: that a transmon qubit, regarded as a binary (base-2) truncation of a genuinely discrete but unbounded bosonic ladder, carries an irreducible leakage cost for any finite-time gate. We define Planck Loss $L_P = 1 - \mathrm{Tr}(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|)$, where $P_{\mathrm{qubit}}$ projects onto the computational two-level subspace, and conjecture that $L_P > 0$ for any finite gate time, independent of materials imperfections, because the physical drive couples all ladder levels through the raising operator $a^\dagger$. We derive a perturbative lower-bound estimate for a driven Duffing-type transmon Hamiltonian, showing that leakage amplitude scales as $\Omega/|\alpha|$ (drive Rabi rate over anharmonicity) and Planck Loss as $(\Omega/|\alpha|)^2$, and we compute a concrete reference point: for $\Omega/2\pi = 20$ MHz and $|\alpha|/2\pi = 200$ MHz, $L_P \approx 10^{-2}$ per gate. We further quantify the information cost of radix truncation as $S_{\mathrm{Base}} = \ln(d/2)$ nats, which evaluates to $\approx 1.7918$ nats ($\approx 2.584$ bits) for $d = 12$ resolvable levels. We argue that the transmon is naturally a qudit, not a qubit, and that base-$d$ encoding removes the truncation penalty. All quantitative results here are analytic derivations or clearly labeled model estimates; no new experimental data are reported.

## 1. Introduction

The transmon qubit is, physically, an anharmonic oscillator: a Cooper-pair box shunted by a large capacitor, producing a weakly anharmonic ladder of energy levels. Engineering practice truncates this ladder to its two lowest states and calls the result a qubit. This paper asks a deliberately uncomfortable question: what does that truncation cost, and is the cost fundamental or merely technical?

Our claim, which we call the Planck Fidelity conjecture, is that the cost is fundamental in a specific, falsifiable sense. The ladder is discrete — energy quantization is exact — but it is unbounded: there is no largest level $n_{\max}$. Imposing a binary register $n \in \{0,1\}$ on such an object is a radix error, not a physics error. Any physical drive couples the computational states to the rest of the ladder through the raising operator $a^\dagger$, whose matrix elements $\langle n+1|a^\dagger|n\rangle = \sqrt{n+1}$ are nonzero for every $n$. Therefore, for any finite-time gate, amplitude leaks out of the qubit subspace by a mechanism that is independent of materials quality, dielectric loss, or dephasing. We name this irreducible component Planck Loss:

$$L_P \;=\; 1 - \mathrm{Tr}\!\left(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|\right),$$

and conjecture that $L_P > 0$ for any finite gate time.

The conceptual framing — that binary truncation of a discrete-but-unbounded oscillator is an approximation with a quantifiable entropy cost — originates in the QNFO "Project Rosetta" program [9], which explicitly corrects an earlier claim that the transmon spectrum is continuous, recognizing that the spectrum is discrete (Planck quantization) and that the error is one of encoding radix, and which introduces an "Approximation Entropy" framework quantifying the irreducible cost of translating continuous bosonic physics onto discrete digital computation [10]. The present paper supplies the perturbative derivation and the explicit numerical bookkeeping that the conjecture invites.

We proceed as follows. Section 2 situates the work relative to the supplied literature. Section 3 defines the model, the metric, and the conjecture precisely. Section 4 carries out the derivations with every arithmetic step shown. Section 5 reports only computed numbers and labeled projections. Section 6 discusses limitations and falsification conditions, and Section 7 concludes.

## 2. Background and Related Work

The supplied bibliography is unusual: eight of its ten entries concern the European Space Agency's Planck cosmic microwave background (CMB) satellite, and two concern the QNFO conceptual program. We treat each honestly, on the basis of its own supplied summary, and state plainly where a work bears on our argument and where it does not.

[1] presents the scientific programme of the Planck CMB mission, describing Planck as the third space CMB mission after COBE and WMAP, designed to extract essentially all of the information in the CMB temperature anisotropies. Its relevance to us is methodological and nominal: the mission's stated ambition of extracting "essentially all" of the information in a physical field is a useful analogue for our thesis that truncating a physical degree of freedom to a binary register discards extractable information. The entry supplies no quantum-computing content, and we claim none from it.

[2] describes the Planck satellite itself, launched on 14 May 2009 and surveying the sky continuously since 13 August 2009, with performance in line with expectations. We cite it as context for the naming of our metric ("Planck Fidelity" refers to Planck quantization of the ladder, not to the satellite); the entry gives no further detail relevant to superconducting qubits.

[3] documents the Planck Catalogue of Compact Sources (PCCS), nine single-frequency catalogues of compact Galactic and extragalactic sources over the full sky in the frequency range 30–857 GHz, 90% complete at 180 mJy in the best channel. The catalogue's structure — a discrete set of detected sources over a continuous sky — is a distant analogue of level-resolved spectroscopy of a ladder, but the entry itself contains no content applicable to qubit physics, and we use it only as adjacent-context literature.

[4] describes the all-sky Planck catalogue of Sunyaev–Zeldovich cluster candidates from the first 15.5 months of operations, containing 1227 entries, over six times the size of the earlier ESZ sample, with 861 confirmed clusters. As with [3], the entry supports no claim about quantum devices; we cite it to complete the record of the Planck mission corpus supplied to this study.

[5] uses the Early Release Compact Source Catalogue to measure number counts $\mathrm{d}N/\mathrm{d}S$ of extragalactic radio sources at 30, 44, 70, 100, 143 and 217 GHz, finding very good agreement with earlier counts at the lower frequencies. The exercise of counting discrete objects against a flux threshold is structurally similar to counting resolvable levels $d$ against an anharmonicity threshold, and we borrow only this structural parallel; the entry states nothing about qubits.

[6] reports the determination of the Planck High Frequency Instrument spectral response through ground-based cryogenic tests of the focal plane prior to launch, measuring relative spectral response including out-of-band signal rejection. The notion of out-of-band rejection is a genuine conceptual cousin of our problem: a device designed for a two-level "band" inevitably responds outside it. The entry, however, concerns bolometric detectors, and we do not attribute any qubit-relevant finding to it.

[7] presents the Second Planck Catalogue of Compact Sources, detected in single-frequency maps over the full mission duration, superseding previous compact source catalogues. Its supplied summary gives no further detail applicable here beyond its status as a successor catalogue.

[8] describes the calibration pipeline for the Planck Low Frequency Instrument over four years of operations, using the spin-synchronous modulation of the CMB dipole as calibrator, now adding the orbital component. Calibration against a known reference dipole is a loose analogue of gate benchmarking against a known reference process, but again the entry supports no quantum-computing claim and we make none.

[9] is the direct conceptual antecedent: QNFO "Project Rosetta" v2.0, which corrects an earlier version by affirming that the transmon spectrum IS discrete (Planck quantization) and that binary truncation is a radix error rather than a physics error; it asserts that the transmon is a qudit with $d \sim 12$, not a qubit, and quantifies the radix cost as $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats. We adopt this quantity, recompute it exactly in Section 4, and embed it in a perturbative leakage derivation.

[10] is the companion polemic, "The Two-Level Lie," whose v2.0 adds Part II, the Approximation Entropy: a meta-mathematical framework quantifying the irreducible cost of translating continuous bosonic physics to discrete digital computation, introducing a Rosetta Constant, a Trotter Wall, and a Fractal Wall theorem with a falsifiable calorimetry experimental proposal. We treat the Approximation Entropy as the conceptual parent of our Planck Loss; the specific leakage bound and numerics below are our own contribution, not claims made in [10].

We note candidly that the eight Planck-mission entries [1]–[8] are topologically unrelated to superconducting qubits; they are cited here because they constitute the supplied literature, and every statement above about them is drawn strictly from their own summaries. The substantive scientific lineage of this paper is [9] and [10].

## 3. Methods

### 3.1 Model

We model the transmon as a driven Duffing oscillator (anharmonic ladder):

$$H_0 = \omega\, a^\dagger a + \frac{\alpha}{2}\, a^\dagger a^\dagger a\, a, \qquad H_d(t) = \epsilon(t)\,(a + a^\dagger),$$

where $\omega$ is the ladder spacing, $\alpha$ the anharmonicity ($\alpha < 0$ for a transmon), $a$ and $a^\dagger$ the ladder operators with $[a, a^\dagger] = 1$, and $\epsilon(t)$ a classical drive envelope. The ladder is discrete but unbounded: $n \in \{0, 1, 2, \dots\}$ with no upper bound. The computational register is the binary truncation $n \in \{0,1\}$, with projector

$$P_{\mathrm{qubit}} = |0\rangle\langle 0| + |1\rangle\langle 1|.$$

### 3.2 Metric and conjecture

For a gate acting for time $t_g$ starting from $|\psi_0\rangle \in \mathrm{span}\{|0\rangle,|1\rangle\}$, define

$$L_P(t_g) \;=\; 1 - \langle \psi_0 | U^\dagger(t_g)\, P_{\mathrm{qubit}}\, U(t_g)\, |\psi_0\rangle.$$

**Planck Fidelity conjecture.** For the Hamiltonian above with any drive $\epsilon(t) \neq 0$ of finite duration $t_g$, and in the absence of any engineered counter-leakage mechanism, $L_P(t_g) > 0$.

The mechanism is elementary but fundamental: $a^\dagger$ has nonzero matrix elements $\langle n+1|a^\dagger|n\rangle = \sqrt{n+1}$ for all $n$, so the drive is not block-diagonal with respect to the qubit subspace. No choice of materials enters $H_d$; the coupling is kinematic.

### 3.3 Perturbative estimate

In the rotating frame at the drive frequency, the effective coupling from level $1$ to level $2$ has amplitude of order $\Omega/|\alpha|$, where $\Omega$ is the on-resonant Rabi rate between levels $0$ and $1$ and $|\alpha|$ the level-1-to-2 detuning from the drive. To second order, the leakage probability scales as

$$L_P \;\sim\; \left(\frac{\Omega}{|\alpha|}\right)^{2},$$

up to shape factors of order unity depending on the pulse envelope. We treat this as a model estimate, not a theorem; the conjecture itself is the qualitative statement $L_P > 0$.

### 3.4 Radix entropy

Following [9], we define the base-truncation entropy

$$S_{\mathrm{Base}}(d) = \ln\!\left(\frac{d}{2}\right) \ \text{nats},$$

the information discarded by encoding a $d$-level ladder as a 2-level register.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

**Input 1 (from [9]):** the transmon is a qudit with $d \sim 12$ resolvable levels, and $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats.

**Derivation 1 (exact recomputation of $S_{\mathrm{Base}}$).** With $d = 12$:

$$S_{\mathrm{Base}}(12) = \ln\!\left(\frac{12}{2}\right) = \ln 6.$$

Using $\ln 6 = \ln 2 + \ln 3 \approx 0.693147 + 1.098612 = 1.791759$:

$$S_{\mathrm{Base}}(12) \approx 1.7918 \ \text{nats}.$$

This matches the $\sim 1.79$ nats quoted in [9]. In bits, dividing by $\ln 2 \approx 0.693147$:

$$S_{\mathrm{Base}}(12) \approx \frac{1.791759}{0.693147} \approx 2.5840 \ \text{bits}.$$

So a binary register discards approximately $2.58$ bits of ladder state information per transmon.

**Input 2 (model parameters, stated as assumptions for this estimate):** a representative transmon with anharmonicity $|\alpha|/2\pi = 200$ MHz and a gate driven at Rabi rate $\Omega/2\pi = 20$ MHz, gate time $t_g = 20$ ns. These are illustrative model values chosen for arithmetic transparency, not measurements.

**Derivation 2 (leakage amplitude).** The perturbative leakage amplitude is

$$\eta \sim \frac{\Omega}{|\alpha|} = \frac{20 \ \text{MHz}}{200 \ \text{MHz}} = 0.1.$$

**Derivation 3 (Planck Loss estimate).** To second order,

$$L_P \sim \eta^2 = (0.1)^2 = 0.01 = 1\times 10^{-2}.$$

That is, under this model, roughly one percent of gate population leaks per gate purely from the kinematic coupling through $a^\dagger$, before any materials-induced error.

**Derivation 4 (kinematic matrix element).** The raising operator's matrix element from level 1 to level 2 is

$$\langle 2|a^\dagger|1\rangle = \sqrt{1+1} = \sqrt{2} \approx 1.414214.$$

The drive therefore couples the computational state $|1\rangle$ to $|2\rangle$ with strength $\sqrt{2}\,\epsilon(t)$ — the coupling exists for every $n$ with strength $\sqrt{n+1}$, which never vanishes. This is the structural reason the conjecture $L_P > 0$ holds for any nonzero finite drive: the off-block-diagonal coupling cannot be removed by materials engineering, only suppressed by pulse shaping, which trades gate time against leakage.

**Derivation 5 (scaling with $d$).** For general $d$, the radix entropy is

$$S_{\mathrm{Base}}(d) = \ln\!\left(\frac{d}{2}\right) = \ln d - \ln 2.$$

At $d = 2$: $S_{\mathrm{Base}}(2) = \ln 1 = 0$ nats (no truncation cost by definition). At $d = 12$: $1.7918$ nats as above. The cost grows logarithmically in $d$; equivalently, each doubling of usable levels adds exactly $\ln 2 \approx 0.6931$ nats $\approx 1$ bit of recoverable information.

**Derivation 6 (leakage–gate-time trade, labeled projection).** If the gate time is stretched to $t_g' = 2 t_g = 40$ ns at fixed rotation angle, the required Rabi rate halves to $\Omega'/2\pi = 10$ MHz, giving

$$L_P' \sim \left(\frac{10}{200}\right)^2 = (0.05)^2 = 0.0025 = 2.5\times 10^{-3}.$$

Halving the drive rate quarters the model leakage — the characteristic quadratic trade. This is a projection under the stated model assumptions, not a measurement.

## 5. Results

We report only quantities computed in Section 4.

1. **Radix entropy (computed, from $d=12$ of [9]):** $S_{\mathrm{Base}}(12) = \ln 6 \approx 1.7918$ nats $\approx 2.5840$ bits. Binary truncation of a 12-level transmon discards $\approx 2.58$ bits of state information.

2. **Leakage matrix element (computed, kinematic):** $\langle 2|a^\dagger|1\rangle = \sqrt{2} \approx 1.414214$; the drive couples every adjacent pair with strength $\sqrt{n+1}$, never zero.

3. **Planck Loss model estimate (computed, under stated model inputs $\Omega/2\pi = 20$ MHz, $|\alpha|/2\pi = 200$ MHz):** $L_P \sim (\Omega/|\alpha|)^2 = 1\times 10^{-2}$ per gate.

4. **Quadratic trade projection (labeled projection, assumptions in Derivation 6):** doubling gate time to 40 ns reduces the model estimate to $L_P' \sim 2.5\times 10^{-3}$; uncertainty is a shape factor of order unity from the pulse envelope, which we do not compute here.

5. **Conjecture (qualitative, not numeric):** $L_P(t_g) > 0$ for any finite, nonzero drive, independent of materials.

No experimental or simulated fidelity data are reported in this paper; item 3 is a perturbative model estimate and item 4 a projection under explicitly stated assumptions.

## 6. Discussion

**Limitations.** The central limitation is that our leakage estimate $L_P \sim (\Omega/|\alpha|)^2$ is a scaling argument with an unspecified order-unity shape factor, not a rigorous bound; deriving a true lower bound on $L_P$ via perturbation theory in $a^\dagger$, as the research plan proposes, remains open. Second, the conjecture as stated excludes engineered counter-leakage mechanisms (e.g., drives with spectral structure that cancels off-block-diagonal amplitude at the gate's end); whether $L_P > 0$ survives all such pulse-shaping strategies at finite $t_g$ is precisely the content of the conjecture and is not proven here. Third, the number $d \sim 12$ is taken from [9] without independent derivation; the entropy $S_{\mathrm{Base}}$ depends linearly-in-$\ln$ on $d$, so its value is conditional on that input. Fourth, the eight Planck-mission references [1]–[8] are unrelated in subject matter to qubit physics; their inclusion reflects the supplied literature, and we have restricted every statement about them to their own summaries.

**Failure modes and falsification.** The conjecture is falsifiable in the way [10] envisages with its proposed falsifiable calorimetry experiment: if a finite-time gate on a well-characterized transmon achieves leakage strictly zero up to arbitrarily small materials-limited error floors — i.e., if pulse shaping can drive $L_P$ to zero faster than all other error channels — the conjecture fails. Conversely, observation of a leakage floor that persists as materials-limited errors (dephasing, dielectric loss) are independently suppressed would support it. A second falsification route: if the transmon's usable ladder were actually bounded near $d \approx 2$ by physics rather than control, the radix-error framing would lose force.

**Against ourselves.** A skeptic may rightly object that leakage in practice is dominated by ordinary control error, that randomized compiling and DRAG-style pulse shaping reduce leakage to levels far below other error sources, and that calling the residual "fundamental" is rhetoric until a proven lower bound exists. We agree that this is the weakest point of the paper: our $1\times 10^{-2}$ figure is a model estimate, and the honest claim is the structural one — the coupling $\sqrt{n+1}\,\epsilon(t)$ never vanishes — not the magnitude. We also note that "Planck Loss" as defined is basis- and projector-dependent; a different choice of computational subspace changes $L_P$, so the conjecture should be read as a statement about the binary projector specifically.

**Open questions.** (i) Rigorous lower bound on $L_P(t_g)$ for bounded-amplitude drives of fixed pulse area. (ii) The scaling of gate infidelity with resolvable $d$ and its relation to $S_{\mathrm{Base}} = \ln(d/2)$. (iii) Experimental benchmarking of a Planck Fidelity metric against leakage data, and the calorimetric test proposed in [10]. (iv) Architecture implications: whether base-$d$ qudit encodings [9] recover the $\approx 2.58$ bits per transmon that binary truncation discards.

## 7. Conclusion

We have formalized the Planck Fidelity conjecture: binary truncation of a discrete-but-unbounded bosonic ladder incurs a materials-independent leakage $L_P > 0$ for any finite-time gate, because the drive couples all levels through $a^\dagger$ with matrix elements $\sqrt{n+1}$ that never vanish. We computed the radix-truncation entropy exactly, $S_{\mathrm{Base}}(12) = \ln 6 \approx 1.7918$ nats $\approx 2.5840$ bits, confirming the value quoted in [9]; we derived a perturbative model estimate $L_P \sim (\Omega/|\alpha|)^2 = 1\times 10^{-2}$ for representative parameters, and a quadratic trade projection $L_P' \sim 2.5\times 10^{-3}$ at doubled gate time. The transmon is best regarded as a qudit; the qubit is an approximation whose entropy cost we have made explicit. The remaining gap — a rigorous lower bound — is the natural next step, and the conjecture stands or falls on falsifiable experimental tests of the kind proposed in [10].

## References

[1] arXiv:astro-ph/0604069v1 | The Scientific Programme of Planck
[2] arXiv:1101.2022v2 | Planck Early Results: The Planck mission
[3] arXiv:1303.5088v2 | Planck 2013 results. XXVIII. The Planck Catalogue of Compact Sources
[4] arXiv:1303.5089v2 | Planck 2013 results. XXIX. Planck catalogue of Sunyaev-Zeldovich sources
[5] arXiv:1101.2044v2 | Planck Early Results: Statistical properties of extragalactic radio sources in the Planck Early Release Compact Source Catalogue
[6] arXiv:1303.5070v2 | Planck 2013 results. IX. HFI spectral response
[7] arXiv:1507.02058v2 | Planck 2015 results. XXVI. The Second Planck Catalogue of Compact Sources
[8] arXiv:1505.08022v2 | Planck 2015 results. V. LFI calibration
[9] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 | DOI 10.5281/zenodo.21486780
[10] QNFO: The Two-Level Lie: The Transmon Is Not a Qubit — And the Entire Field Knows It | DOI 10.5281/zenodo.21484345