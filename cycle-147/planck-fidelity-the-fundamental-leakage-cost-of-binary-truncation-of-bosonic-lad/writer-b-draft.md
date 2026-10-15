# Planck Fidelity: The Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders

## Abstract

Superconducting transmon qubits are weakly anharmonic oscillators whose spectra form discrete but unbounded ladders of energy eigenstates; the binary register $n \in \{0,1\}$ is imposed on this ladder by truncation, not by physics. Because every physical drive contains the raising operator $a^\dagger$, whose matrix elements $\sqrt{n+1}$ never vanish, any finite-time gate populates levels outside the computational subspace. We formalize this as the Planck Loss $L_P = 1 - \mathrm{Tr}(P_{\mathrm{qubit}}|\psi\rangle\langle\psi|)$ and conjecture that $L_P > 0$ for any finite-time gate, independent of materials quality — a fundamental cost of base-2 encoding on a base-$d$ physical object. We derive the harmonic-limit second-order leakage $L_P^{(2)} = \theta^4/2$, which evaluates to $3.0440341$ for a $\pi$-pulse and therefore signals perturbative breakdown; with anharmonicity we obtain the first-order bound $L_2 = 8(\Omega/|\alpha|)^2 \sin^2(\alpha T_g/2)$, giving a gate-averaged leakage of $1.0 \times 10^{-2}$ at $\Omega/|\alpha| = 0.05$, and the exact three-level peak $P_{2,\max} = 2r^2/(1+2r^2) = 1.96 \times 10^{-2}$ at $r = 0.1$. We compute the radix-truncation entropy $S_{\mathrm{Base}}(12) = \ln 6 = 1.7917595$ nats $= 2.5849625$ bits, a discarded-information fraction of $72.1\%$ of the ladder's $\ln 12$ content. The results reframe the qubit as a radix approximation and motivate qudit (base-$d$) architectures and a falsifiable leakage-floor test programme.

## 1. Introduction

Every superconducting quantum processor today runs on a convention, and the convention has a price that no one has put on the invoice. The transmon — the workhorse circuit of the superconducting quantum computing industry — is a weakly anharmonic oscillator: its energy eigenstates form a ladder $|n\rangle$, $n = 0, 1, 2, \dots$, that is discrete because physical action is quantized but unbounded because no term in its Hamiltonian terminates the ladder. The hardware resolves many rungs of this ladder. The qubit register uses two of them. The projector $P_{\mathrm{qubit}} = |0\rangle\langle 0| + |1\rangle\langle 1|$ is declared to be the system, and everything above rung $n = 1$ is declared "leakage."

This declaration is not free. The drive that implements any gate contains the raising operator $a^\dagger$, which by construction couples $|n\rangle$ to $|n+1\rangle$ with matrix element $\sqrt{n+1}$ for every $n$. A finite-time gate therefore always populates levels outside the binary subspace, no matter how clean the materials, how low the dielectric loss, or how long the coherence time. We call the resulting population loss Planck Loss,

$$L_P = 1 - \mathrm{Tr}\!\left(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|\right) = \sum_{n \geq 2} |c_n|^2, \qquad |\psi\rangle = \sum_{n \geq 0} c_n |n\rangle,$$

and conjecture that $L_P > 0$ for any finite gate time, as a property of the encoding rather than of the fabrication.

The stakes are concrete. Gate-error budgets in superconducting processors are compiled from materials-limited channels — dephasing, relaxation, control noise — plus a leakage line item that is treated as a tunable control artifact, suppressible by pulse shaping. If the conjecture of this paper holds, that bookkeeping is wrong at a structural level: a strictly positive leakage floor exists for any finite-time binary gate, and the correct engineering response is not to chase it to zero but to change the radix of the register. A designer who accepts the result stops optimizing two-level pulses against an unreachable zero and starts asking how much of the ladder's capacity a base-$d$ register would recover. The decision that changes is the radix decision, and the capability it unlocks is the roughly $2.58$ bits per oscillator that binary truncation discards, quantified in Section 4.3.

The name "Planck" is chosen deliberately. The quantization of physical action — the fact that the oscillator ladder is discrete with fixed spacing — is the reason a truncation is possible at all and the reason its cost is quantifiable. The European Space Agency's Planck satellite, named for the same physicist, was launched on 14 May 2009 and has been surveying the sky stably and continuously since 13 August 2009 [2]; its scientific programme was designed to extract essentially all of the information in the cosmic microwave background temperature anisotropies, because only a small fraction of the information available in the CMB had been extracted by prior missions [1]. That programme — extract all of the information a quantized physical channel carries, rather than a conventionally selected subset of it — is precisely the attitude we argue quantum hardware should adopt toward the bosonic ladder.

Our contributions are:

1. A perturbative derivation of the harmonic-limit leakage $L_P^{(2)} = \theta^4/2$ for a driven transmon Hamiltonian, with all arithmetic shown, showing perturbative breakdown for a $\pi$-pulse (Section 4.1).
2. A first-order leakage bound $L_2 = 8(\Omega/|\alpha|)^2 \sin^2(\alpha T_g/2)$ and an exact three-level leakage formula, evaluated with explicit arithmetic at stated operating points (Section 4.2).
3. An information-theoretic accounting of the binary truncation as an approximation entropy $S_{\mathrm{Base}} = \ln(d/2)$, evaluated for a qudit of dimension $d = 12$ as $\ln 6 = 1.7917595$ nats $= 2.5849625$ bits, together with the discarded-information fraction $f_{\mathrm{disc}} = 0.721125$ (Section 4.3).
4. A definition of the Planck Fidelity benchmark metric $F_P$ and a falsifiability analysis of the conjecture $L_P > 0$, including the escape routes that would defeat it (Sections 3.5 and 4.4).

Throughout, "leakage" means population outside the computational subspace; "radix" means the base of the logical register ($2$ for a qubit, $d$ for a qudit); "nats" means logarithms in base $e$.

## 2. Background and Related Work

The literature base for this paper divides into two groups: the Planck CMB mission papers [1]–[8], which we use as methodological and conceptual analogies (flagged explicitly each time), and the QNFO line of work [9]–[11], which is the direct scientific lineage of the truncation-cost thesis.

[1] The Scientific Programme of Planck states that for 40 years the cosmic microwave background has been the most important source of information about the geometry and contents of the Universe, that only a small fraction of the information available in the CMB has been extracted to date, and that Planck, the third space CMB mission after COBE and WMAP, is designed to extract essentially all of the information in the CMB temperature anisotropies. The design philosophy — extract all the information the quantized field carries, not a conventionally truncated subset — is the exact analogue of our thesis that a register should match the physical Hilbert-space dimension rather than a chosen binary slice of it.

[2] Planck Early Results: The Planck mission records that the Planck satellite was launched on 14 May 2009, has been surveying the sky stably and continuously since 13 August 2009, carries 74 detectors sensitive to frequencies between approximately 25 and 1000 GHz, and that after its first year the major elements of the satellite's performance exceeded their original technical requirements. We use it as the factual anchor for the mission whose name we borrow, and for the demonstration that a quantized physical channel can be operated continuously against its full design capacity rather than a nominal subset.

[3] The Planck Catalogue of Compact Sources (PCCS) describes nine single-frequency catalogues of compact Galactic and extragalactic sources detected over the entire sky in the first 15 months of operations, covering 30–857 GHz, with reliability above 80% by construction and 90% completeness at 180 mJy in the best channel; its source tables list, for example, 5675 full-sky sources at 143 GHz and 24381 at 857 GHz. The catalogue is itself an act of truncation: sources below a sensitivity threshold are declared outside the registered set, exactly as levels above $n = 1$ are declared outside the qubit. The stated completeness figure is a quantitative model for what a truncation threshold costs in coverage — a number the catalogue states rather than hides, which is the reporting practice we demand for transmon leakage.

[4] The Planck catalogue of Sunyaev-Zeldovich sources presents an all-sky catalogue of clusters and cluster candidates derived over the first 15.5 months, containing 1227 entries — over six times the size of the Planck Early SZ sample — of which 861 are confirmed clusters, with the remainder classified as new candidates at high, medium, and low reliability (366 in total, per its validation table). The candidate-versus-confirmed distinction (1227 versus 861) illustrates the general accounting problem of separating registered signal from registered-but-unvalidated excess, structurally the same bookkeeping as separating computational population from leakage population: both require that the unvalidated excess be counted and reported, not discarded.

[5] The statistical study of extragalactic radio sources uses the Early Release Compact Source Catalogue to measure number counts $\mathrm{d}N/\mathrm{d}S$ at 30, 44, 70, 100, 143 and 217 GHz, finding counts at 30, 44 and 70 GHz in good agreement with WMAP at nearby frequencies and showing that the de Zotti et al. (2005) model over-predicts the counts at 143 GHz by a factor of about 2.0 and at 217 GHz by about 2.6. Counting population above a flux threshold is the direct statistical analogue of counting population above the truncation rung of a ladder; the paper's demonstration that a model can mispredict thresholded counts by factors of order 2 is a caution we adopt: a truncation-dependent observable must be measured against the untruncated object, not against a model of it.

[6] The HFI spectral response paper reports that the High Frequency Instrument spectral response was determined through ground-based tests of the focal plane in a cryogenic environment prior to launch, the goal being to measure the relative spectral response including out-of-band signal rejection, and that out-of-band rejection was verified through comparisons with HFI zodiacal light observations, where any out-of-band sky signal received would be evident in the data. Out-of-band rejection is the instrumental counterpart of leakage suppression: a detector nominally assigned to one frequency band inevitably responds outside it, and the honest engineering response is to measure and quantify that response rather than declare it zero. This is precisely the epistemic stance we demand for transmon leakage.

[7] The Second Planck Catalogue of Compact Sources is a catalogue of compact sources detected in single-frequency maps over the full mission duration and supersedes previous versions of the Planck compact source catalogues; its validation section reports that no clearly significant discrepancies in positions or flux densities were found apart from a possible 6% or 1–1.5$\sigma$ difference in the noisy 44 GHz map. The act of superseding an earlier truncated catalogue with a longer-integration, more complete one — while quantifying the residual discrepancies against external data — models our central methodological recommendation: re-baseline the register against the full physical object, then quantify what the earlier truncation missed.

[8] The LFI calibration paper describes the pipeline used to calibrate Low Frequency Instrument timelines into thermodynamic temperatures over four years of uninterrupted operations, using the spin-synchronous modulation of the CMB dipole as calibrator, and reports an improvement by a factor of 3 in calibration accuracy relative to the 2013 release, reaching 0.20% to 0.35% depending on frequency. A calibration pipeline that converts raw physical signal into a declared unit system, with a known reference and a stated accuracy, is the structural template for our Planck Fidelity metric: a declared fidelity figure is meaningful only relative to a stated reference subspace, and the accuracy of the reference itself must be quantified.

[9] QNFO: Planck Fidelity: Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders is the most technically developed antecedent of this paper. It derives the first-order leakage bound $L_2 = 8(\Omega/|\alpha|)^2 \sin^2(\alpha T_g/2)$, the exact three-level results $P_{2,\max} = 2r^2/(1+2r^2)$ and $\overline{P}_2 = r^2/(1+2r^2)$, and evaluates them at illustrative parameters $f_\Omega = 20$ MHz, $f_\alpha = 200$ MHz, obtaining $P_{2,\max} = 0.019608$, a $\pi$-pulse duration $t_\pi = 25$ ns, and a gate-averaged perturbative leakage $\overline{L_2} = 0.01$ at $\Omega/|\alpha| = 0.05$ with a numerical scaling check confirming the quadratic dependence (doubling the ratio multiplies the leakage by 4). It also computes $S_{\mathrm{Base}} = \ln 6 = 1.791759$ nats $= 2.584963$ bits for $d = 12$, a discarded-information fraction $f_{\mathrm{disc}} = 0.721125$ of the $\ln 12 = 2.484906$-nat content, and $\log_2 12 = 3.584963$. Its discussion states explicitly that the strict-positivity claim is a model-class result holding for finite-time, finite-amplitude drives of the stated $a^\dagger$-form under the rotating-wave approximation, and that shaped envelopes can null the first-order leakage at isolated, measure-zero parameter points. We adopt its leakage formulas and re-derive their evaluation with full arithmetic in Section 4.2, and we adopt its honesty about the model-class scope of the conjecture.

[10] QNFO: Planck Fidelity: The Fundamental Leakage Cost of Binary Truncation of Bosonic Ladders is the immediate predecessor of the present text. It states the harmonic-limit result $c_2^{(2)} = -\theta^2/\sqrt{2}$ and $L_P^{(2)} = \theta^4/2$, evaluating to $3.0440341$ for a $\pi$-pulse and signaling perturbative breakdown; it states the anharmonic projection $L_P^{(\mathrm{est})} \approx (\Omega/\alpha)^2$ with values $1.0 \times 10^{-2}$, $2.5 \times 10^{-3}$, and $4.0 \times 10^{-2}$ at $\Omega/\alpha = 0.1$, $0.05$, and $0.2$; and its discussion concedes that the prefactor is pulse-shape dependent, that no rigorous operator lower bound on $L_P$ is derived, and that a skeptic could accept the structural claim while denying practical significance if engineered counter-sequences suppress leakage below materials-limited error rates. We carry forward its harmonic-limit derivation (Section 4.1), treat its $(\Omega/\alpha)^2$ estimate as superseded by the more explicit bound of [9] (Section 4.2), and preserve its self-critical framing in Section 6.

[11] QNFO: Project Rosetta v2.0 is the conceptual source of the radix-error framing. With its "Planck-Radix Correction" it corrects an earlier version by affirming that the transmon spectrum IS discrete (Planck quantization), so that binary truncation is a radix error, not a physics error; it asserts that the transmon is a qudit of dimension $d \sim 12$, not a qubit; and it defines $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats as the base-encoding entropy cost. Its statement of results tabulates a Translation Calorimeter as a falsifiable measurement of the approximation entropy $S_A$, a Rosetta Constant $R = k_B T \ln(1/\alpha_r)$, and a decomposition $S_{\mathrm{Total}} = S_{\mathrm{Obs}} + S_{\mathrm{Base}} + S_{\mathrm{Arch}} + S_{\mathrm{Alg}} + S_{\mathrm{Trot}}$; its discussion proposes three paths forward — analog bosonic simulation, fermionic native-discrete platforms, and hybrid architectures with bounded approximation entropy at the interface. We adopt the quantity $S_{\mathrm{Base}}$, re-derive its value with explicit arithmetic in Section 4.3, and design our falsifiability analysis (Section 4.4) to be compatible in spirit with its calorimetric protocol.

## 3. Methods

### 3.1 Model

We model the transmon as a weakly anharmonic oscillator,

$$H_0 = \hbar\,\omega\, a^\dagger a + \frac{\hbar\,\alpha}{2}\, a^\dagger a^\dagger a\, a,$$

where $\omega$ is the ladder spacing, $\alpha$ the anharmonicity (the detuning of the $|1\rangle \leftrightarrow |2\rangle$ transition from $\omega$), and $a$, $a^\dagger$ the ladder operators satisfying $a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$. A classical drive of envelope $\varepsilon(t)$ couples all adjacent levels:

$$H_{\mathrm{drv}}(t) = \hbar\,\varepsilon(t)\,\left(a\,e^{i\omega_d t} + a^\dagger e^{-i\omega_d t}\right),$$

with drive frequency $\omega_d$. The computational (qubit) subspace is $\mathcal{H}_q = \mathrm{span}\{|0\rangle, |1\rangle\}$ with projector $P_{\mathrm{qubit}} = |0\rangle\langle 0| + |1\rangle\langle 1|$, and Planck Loss for a state $|\psi\rangle$ is

$$L_P = 1 - \mathrm{Tr}\!\left(P_{\mathrm{qubit}}\,|\psi\rangle\langle\psi|\right) = \sum_{n \geq 2} |c_n|^2.$$

### 3.2 Metric and conjecture

For a gate acting for time $t_g$ starting from $|\psi_0\rangle \in \mathcal{H}_q$, define $L_P(t_g) = 1 - \langle \psi_0 | U^\dagger(t_g)\, P_{\mathrm{qubit}}\, U(t_g)\, |\psi_0\rangle$.

**Planck Fidelity conjecture.** For the Hamiltonian above with any drive $\varepsilon(t) \neq 0$ of finite duration $t_g$, and in the absence of any engineered counter-leakage mechanism, $L_P(t_g) > 0$.

The mechanism is elementary but fundamental: $a^\dagger$ has nonzero matrix elements $\langle n+1|a^\dagger|n\rangle = \sqrt{n+1}$ for all $n$, so the drive is not block-diagonal with respect to the qubit subspace. No choice of materials enters $H_{\mathrm{drv}}$; the coupling is kinematic. Following [9], we state the scope honestly: the strict-positivity claim is a model-class result, holding for finite-time, finite-amplitude drives of the stated $a^\dagger$-form under the rotating-wave approximation, not for all conceivable Hamiltonians, and shaped envelopes can null the first-order leakage at isolated, measure-zero parameter points.

### 3.3 Perturbative leakage estimates

We use two complementary estimates, both from [9] and re-derived in Section 4.2. First, a first-order bound on the population of $|2\rangle$ for a gate of duration $T_g$:

$$L_2 = 8\left(\frac{\Omega}{|\alpha|}\right)^2 \sin^2\!\left(\frac{\alpha T_g}{2}\right),$$

where $\Omega$ is the drive Rabi amplitude. Second, the exact three-level solution for the $|0\rangle, |1\rangle, |2\rangle$ subsystem under a resonant drive, with $r = \Omega/|\alpha|$:

$$P_{2,\max} = \frac{2r^2}{1 + 2r^2}, \qquad \overline{P}_2 = \frac{r^2}{1 + 2r^2},$$

where $P_{2,\max}$ is the peak leakage population and $\overline{P}_2$ its time average. In the harmonic limit ($\alpha \to 0$) neither estimate applies, and we compute the second-order amplitude directly in Section 4.1.

### 3.4 Approximation entropy of the radix

Following [11], we define the base-encoding entropy cost of imposing a binary register on a $d$-level ladder as

$$S_{\mathrm{Base}}(d) = \ln\!\left(\frac{d}{2}\right) \ \text{nats},$$

the information by which the physical ladder exceeds the binary register. For $d = 2$, $S_{\mathrm{Base}} = 0$; for the transmon qudit with $d \approx 12$ as asserted in [11], we compute $S_{\mathrm{Base}}$ explicitly in Section 4.3, together with the discarded-information fraction of [9].

### 3.5 Planck Fidelity benchmark metric

We define the Planck Fidelity of a gate acting on input $|\psi_k\rangle$ as

$$F_P = 1 - \overline{L_P}, \qquad \overline{L_P} = \frac{1}{N}\sum_{k=1}^{N} \sum_{n \geq 2} |\langle n| U(T) |\psi_k\rangle|^2,$$

where $T$ is the gate time, $U(T)$ the full (untruncated) evolution operator, and the average runs over a set of $N$ input states spanning $\mathcal{H}_q$. The metric differs from a standard qubit gate fidelity in that the reference evolution $U(T)$ is evaluated on the full ladder, so that leakage is counted as error by construction rather than absorbed into a truncated simulation. The calibration-pipeline analogy of [8] applies: $F_P$ is meaningful only relative to the declared reference subspace $P_{\mathrm{qubit}}$, which must be stated with the metric, just as the LFI calibration is stated relative to the dipole reference with a quoted accuracy of 0.20% to 0.35%.

### 3.6 Simulation protocol (specified, not executed)

The protocol we specify, and whose scalings we project in Section 5, is: (1) truncate the ladder at $d$ levels for $d \in \{2, 3, \dots, 16\}$; (2) simulate a standard gate pulse; (3) record $L_P$ and the Shannon entropy of the population outside the binary subspace; (4) test the scaling of the information cost against $\ln(d/2)$. No numerical simulation results are reported in this paper; only analytic estimates and clearly labeled projections.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Second-order leakage amplitude in the harmonic limit

**Inputs.** Pulse area $\theta$ (model parameter, Section 3.3); ladder matrix elements $\langle n+1|a^\dagger|n\rangle = \sqrt{n+1}$ (from the definition of $a^\dagger$).

**Derivation.** Starting from $|0\rangle$, two applications of the raising operator reach $|2\rangle$. In second-order perturbation theory the amplitude is

$$c_2^{(2)} = \frac{(-i\theta)^2}{2!}\,\langle 2 | (a^\dagger)^2 | 0 \rangle.$$

Now $\langle 2|(a^\dagger)^2|0\rangle = \langle 2|a^\dagger|1\rangle\,\langle 1|a^\dagger|0\rangle = \sqrt{2}\cdot 1 = \sqrt{2}$, and $2! = 2$, so

$$c_2^{(2)} = \frac{-\theta^2}{2}\cdot\sqrt{2} = -\frac{\theta^2}{\sqrt{2}}.$$

**Leakage probability.**

$$L_P^{(2)} = |c_2^{(2)}|^2 = \frac{\theta^4}{2}.$$

**Numerical evaluation for a $\pi$-pulse.** A $\pi$-pulse has $\theta = \pi/2$ (so that $\sin^2\theta = 1$). Then

$$\theta = \frac{\pi}{2} = 1.5707963\ldots, \qquad \theta^2 = 2.4674011\ldots, \qquad \theta^4 = (2.4674011)^2 = 6.0880682\ldots,$$

$$L_P^{(2)} = \frac{6.0880682}{2} = 3.0440341.$$

This exceeds unity, which signals the breakdown of second-order perturbation theory in the harmonic limit: with zero anharmonicity, a resonant drive does not merely leak — it transfers population up the ladder without bound, and the perturbative series diverges. The correct reading of the calculation is qualitative but sharp: **in the harmonic limit there is no finite-$\theta$ pulse that keeps $L_P$ small; the binary register is incompatible with the physics.** Perturbation theory is valid only when anharmonicity detunes the higher rungs, to which we now turn.

### 4.2 Anharmonic leakage: first-order bound and exact three-level result

**Inputs (assumptions, stated explicitly).** (A1) The drive Rabi amplitude is $\Omega$ and the anharmonic detuning is $\alpha$, both in the same angular-frequency units; we write $r = \Omega/|\alpha|$. (A2) The first-order bound of [9], $L_2 = 8r^2 \sin^2(\alpha T_g/2)$, applies under the rotating-wave approximation with levels $n \geq 3$ neglected. (A3) Illustrative operating points, not measurements: $r = 0.05$ for the perturbative bound and $r = 0.1$ for the exact three-level result, following the illustrative parameter sets of [9].

**Derivation 1: perturbative bound.** With $r = 0.05$ and worst-case gate timing $\alpha T_g/2 = \pi/2$ (so $\sin^2(\pi/2) = 1$):

$$L_2 = 8 \times (0.05)^2 \times 1 = 8 \times 0.0025 = 0.02.$$

The perturbative validity check of [9] is $8r^2 = 0.02 \ll 1$, satisfied. The corresponding Planck Fidelity is $F_P = 1 - 0.02 = 0.98$. Gate-averaging $\sin^2$ over uniformly distributed gate times gives mean $\sin^2 = 1/2$:

$$\overline{L_2} = 8 \times 0.0025 \times \frac{1}{2} = 0.01, \qquad \overline{F_P} = 0.99.$$

**Scaling check.** Doubling $r$ from $0.05$ to $0.10$ gives $\overline{L_2} = 8 \times 0.01 \times 0.5 = 0.04$; the ratio $0.04/0.01 = 4 = 2^2$ confirms the quadratic scaling numerically.

**Derivation 2: exact three-level peak.** With $r = 0.1$ (equivalently $f_\Omega = 20$ MHz, $f_\alpha = 200$ MHz as in [9], giving $r = 20/200 = 0.1$ and $r^2 = 0.01$):

$$P_{2,\max} = \frac{2 \times 0.01}{1 + 2 \times 0.01} = \frac{0.02}{1.02} = 0.0196078\ldots \approx 1.96 \times 10^{-2},$$

$$\overline{P}_2 = \frac{0.01}{1.02} = 0.0098039\ldots \approx 9.80 \times 10^{-3}.$$

**Pulse duration.** The resonant $\pi$-pulse duration at $f_\Omega = 20$ MHz is

$$t_\pi = \frac{1}{2 f_\Omega} = \frac{1}{2 \times 20 \times 10^{6}\,\mathrm{s}^{-1}} = 2.5 \times 10^{-8}\,\mathrm{s} = 25\,\mathrm{ns},$$

as computed in [9].

**Sensitivity.** Because both estimates are quadratic in $r$, halving the drive amplitude reduces the leakage by a factor of 4 and doubling it increases the leakage by a factor of 4, as the scaling check shows explicitly. The prefactor $8$ and the $\sin^2$ timing factor are fixed by the model of [9]; the true coefficient for a shaped pulse could differ, an uncertainty we carry into Section 6. **These are model estimates under assumptions (A1)–(A3), not measurements.**

### 4.3 Approximation entropy and discarded information for the transmon qudit

**Inputs.** $d = 12$ (the transmon qudit dimension asserted in [11]); $\ln$ denotes the natural logarithm.

**Derivation 1: $S_{\mathrm{Base}}$.**

$$S_{\mathrm{Base}}(12) = \ln\!\frac{12}{2} = \ln 6.$$

Computing: $\ln 6 = \ln 2 + \ln 3 = 0.6931472 + 1.0986123 = 1.7917595$ nats.

This matches the value $S_{\mathrm{Base}} = \ln(d/2) \sim 1.79$ nats stated in [11] and the $1.791759$-nat figure computed in [9]. Converted to bits:

$$S_{\mathrm{Base}}(12)\big|_{\mathrm{bits}} = \frac{1.7917595}{\ln 2} = \frac{1.7917595}{0.6931472} = 2.5849625 \ \text{bits}.$$

**Derivation 2: discarded-information fraction.** The full ladder carries $\ln 12$ nats:

$$\ln 12 = \ln 4 + \ln 3 = 1.3862944 + 1.0986123 = 2.4849067 \ \text{n