# Transmon Leakage as an Empirical Test of Digital Ontology: A Projection-Cost Scaling Law for Bosonic Qubits

## Abstract

Digital ontology ("it from bit") holds that discrete binary degrees of freedom are fundamental. If that were literally true of physical hardware, a qubit substrate would natively confine to two levels; observed leakage would be an anomaly rather than a structural necessity. We propose the opposite reading: transmon leakage is the measurable cost of projecting an infinite-dimensional continuous bosonic Hilbert space (phase and charge degrees of freedom) onto a discrete two-dimensional computational subspace, and its magnitude constitutes empirical evidence that continuous degrees of freedom are ontologically prior to bits. We derive a scaling law for the leakage probability per gate under the transmon cosine Hamiltonian, $p_{\mathrm{leak}} \approx \Omega^2/(4\alpha^2)$, where $\Omega$ is the drive strength on the computational transition and $\alpha$ is the anharmonicity, using only a two-state rotating-frame diagonalization with every arithmetic step shown. Combining this with the qudit truncation dimension $d \approx 12$ and base projection entropy $S_{\mathrm{Base}} = \ln(d/2) \approx 1.79$ nats from the QNFO Rosetta framework, we obtain a projection entropy of $\approx 2.585$ bits per gate and a cumulative $\approx 2585$ bits per logical operation at the documented $10^2$–$10^3$ error-correction overhead. We state a falsifiable prediction: bosonic modalities (transmon, fluxonium, cat qubits) must exhibit systematically nonzero, anharmonicity-scaled leakage, while natively two-level fermionic spin qubits must approach zero leakage at equal gate fidelities. All numerical overhead comparisons are labeled projections with stated assumptions.

## 1. Introduction

The "it from bit" thesis, in its strong form, asserts that the fundamental constituents of physics are discrete informational units, and that continuum behavior is emergent bookkeeping. Taken seriously as a claim about engineered quantum hardware, this thesis makes a prediction that is rarely stated explicitly: a physical system whose essential nature is a bit should not possess spurious higher levels that the bit description must constantly fight against. The superconducting transmon is the sharpest possible test case. Its computational space is declared to be two-dimensional, yet its physical Hamiltonian — a charge degree of freedom in a cosine potential — generates an infinite ladder of bosonic oscillator levels, of which the "qubit" uses the bottom two. Every gate, every idling period, and every coupler interaction can and does populate levels $\lvert 2\rangle, \lvert 3\rangle, \dots$; this population is called leakage and is treated in the literature as an error source to be mitigated [4].

This paper reframes leakage. If bits were ontologically fundamental, the projection from the physical Hilbert space to the qubit space would be free — there would be nothing to project onto. The fact that leakage is nonzero, gate-dependent, and systematically worse for platforms whose native degrees of freedom are more strongly bosonic is exactly what one expects if the continuous degrees of freedom (phase, charge, field amplitude) are prior and the bit is a forced, lossy discretization imposed on top. Leakage rate then becomes an empirical probe of projection cost: a measurable quantity that tracks how violently a continuous bosonic system is being squeezed into a discrete map.

Our contributions are:

1. A fully derived scaling law, $p_{\mathrm{leak}} \approx \Omega^2/(4\alpha^2)$, relating per-gate leakage to drive strength $\Omega$ and anharmonicity $\alpha$ of the transmon cosine Hamiltonian, with the diagonalization shown step by step in Section 4.
2. A connection between this law and the Approximation Entropy framework of the QNFO Rosetta program [9], [12], which quantifies the irreducible cost of translating continuous bosonic physics into discrete digital computation and identifies the transmon as a qudit of dimension $d \approx 12$ rather than a qubit.
3. A projected leakage budget for error-corrected operation, obtained by combining the derived scaling law with the documented quantum error-correction overhead of $10^2$–$10^3$ physical operations per logical operation [10], with all assumptions stated.
4. A falsifiable modality-level prediction: bosonic platforms (transmon, fluxonium, cat qubits) must show systematically higher leakage than fermionic spin qubits at comparable gate fidelities, with the ratio governed by the anharmonicity scaling.

The paper is organized as follows. Section 2 reviews the supplied literature, distinguishing the directly relevant leakage and digital-physics works from tangential entries whose relevance is analogical only. Section 3 sets out the formal model. Section 4 performs all derivations with explicit arithmetic. Section 5 reports results, separating derived quantities from labeled projections. Section 6 discusses limitations, failure modes, and what would falsify the thesis. Section 7 concludes.

## 2. Background and Related Work

We discuss all twelve supplied bibliography entries. Because several entries are tangential to the core physics, we state plainly what each entry's supplied summary supports and mark the relevance as analogical where it is.

**Directly relevant work.** Reference [4] (arXiv:2607.00688v1, "Leakage Mobility and Passive Leakage Removal in Transmons with Tunable Couplers") is the closest experimental anchor for our thesis. Its summary states that qubit leakage is a noticeable source of errors for quantum computing, that in quantum processors leakage excitations traveling between qubits generate correlated errors and perturb gate implementations, and that leakage mobility can be exploited to create dedicated leakage removal pathways and removal units, with the aim of quantitatively characterizing leakage mobility to guide processor architecture design. This is significant for us in two ways: first, it confirms that leakage is a recognized, quantitatively studied phenomenon rather than a marginal artifact; second, the fact that leakage *propagates* between qubits — it is mobile — reinforces our reading of leakage as excitation in the underlying continuous bosonic manifold, which does not respect the qubit/qubit bookkeeping boundary. The summary supplied gives no numerical leakage rates, so we use [4] only for the qualitative facts stated above.

Reference [9] (QNFO, "Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0," DOI 10.5281/zenodo.21486780) supplies the conceptual framework this paper tests empirically. Its summary states that V2.0 corrects V1.0: the transmon spectrum *is* discrete (under a Planck-quantization reading), so binary truncation is a radix error rather than a physics error; the transmon is a qudit with $d \approx 12$, not a qubit; and the base projection entropy is $S_{\mathrm{Base}} = \ln(d/2) \approx 1.79$ nats. We adopt the qudit dimension and the entropy formula as given inputs from [9] and compute their consequences in Section 4. We note that our own derivation in Section 3 treats the cosine Hamiltonian's level ladder as effectively unbounded over the experimentally relevant drive range, which is consistent with [9]'s point that the *binary* truncation, not the spectrum, is the approximation.

Reference [12] (QNFO, "The Two-Level Lie: The Transmon Is Not a Qubit — And the Entire Field Knows It," DOI 10.5281/zenodo.21484345) is the polemical antecedent of this paper. Its summary states that v2.0 adds Part II, "The Approximation Entropy," described as a meta-mathematical framework quantifying the irreducible cost of translating continuous bosonic physics to discrete digital computation, and that it introduces the Rosetta Constant, the Trotter Wall, and the Fractal Wall theorem together with a falsifiable calorimetry experimental proposal. Our contribution differs in kind: where [12] proposes calorimetry (heat as the signature of projection cost), we propose leakage statistics (population in the discarded levels as the signature), which is directly observable in standard gate-set tomography and randomized-benchmarking data of the kind characterized in [4].

Reference [10] (QNFO, "The Physics of Computation: Fundamental Limits and the Honest Boundaries of Post-Classical Computing," DOI 10.5281/zenodo.22753039) supplies the overhead figure we use in our projections. Its summary states that it examines fundamental physical limits on computation — the Landauer bound, the Margolus-Levitin theorem, the Bremermann limit, and the Bekenstein bound — and shows that quantum error-correction overhead of $10^2$–$10^3$ physical operations per logical operation multiplies thermodynamic cost. We take the $10^2$–$10^3$ overhead range as a sourced input and combine it with our derived leakage law in Section 4.

Reference [11] (QNFO, "No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems," DOI 10.5281/zenodo.21451776) is the pedagogical bridge between the qubit-ontology critique and working physics. Its summary states that it explains what control pulses actually manipulate and what readout measures, across superconducting transmon, trapped-ion, and spin qubit platforms, and that it includes an electrical seesaw analogy and a self-referential metrology formalization. This matters for our framing: our scaling law is a statement about what control pulses *actually* manipulate — the full bosonic ladder, not the declared two levels — and [11] is the supplied source that articulates this control/readout gap across the three modalities our falsifiable prediction spans.

**Tangential entries (analogical relevance only).** Reference [1] (arXiv:1910.11775v2, "Physics Briefing Book") describes the European Particle Physics Strategy Update (EPPSU) process, in which the community is first invited to submit proposals for projects to be realised on near-, mid-, and longer-term horizons, with national and laboratory inputs as important elements. Its relevance here is methodological: it exemplifies how large-scale physics programs consolidate community input into strategic direction, the process by which a leakage-as-ontology research program would need to be championed. The supplied summary contains no physics content relevant to transmons.

Reference [2] (arXiv:hep-ex/9605011v1, "Physics and Technology of the Next Linear Collider") presents expectations for the design and physics program of an $e^+e^-$ linear collider at center-of-mass energy 500 GeV – 1 TeV, reviews the experiments to be carried out there, and argues for the machine's key role in exploring physics beyond the Standard Model, showing feasibility of construction. Its relevance is as a precedent for large facility-scale design documents that commit to a specific discretization of nature's degrees of freedom (bunches, bits of detector data); the summary supports no quantum-computing claims.

Reference [3] (arXiv:2107.08351v2, "A Novel Approach to Analyze Fashion Digital Archive from Humanities") concerns building digital fashion image archives to analyze everyday style trends from a humanities perspective over extended periods. Its relevance is a loose analogy — the lossy digitization of continuous cultural artifacts into discrete archives mirrors the lossy digitization of continuous Hilbert spaces — and we flag it as such; the summary supports no physics content.

Reference [5] (arXiv:1205.6363v1, "What Should Developers Be Aware Of?") presents an empirical study on the directives of API documentation of object-oriented libraries — natural-language statements making developers aware of usage constraints and guidelines. The analogy is to hardware abstraction layers: the "qubit" is an API declared to users, and leakage is what happens when the underlying implementation does not honor the documented contract. The summary supports only this analogy.

Reference [6] (arXiv:2107.11742v1, "MHD analysis on the physical designs of CFETR and HFRC") concerns magnetohydrodynamic assessment and analysis for the China Fusion Engineering Test Reactor and the Huazhong Field Reversed Configuration, representative of low-density steady-state and high-density pulsed pathways to fusion. Its relevance is as an example of design-stage physics assessment of competing engineering pathways, parallel to our modality-level comparison of qubit platforms; the summary supports no qubit-specific content.

Reference [7] (arXiv:2309.07064v2, "A Comprehensive Analysis of the Role of Artificial Intelligence and Machine Learning in Modern Digital Forensics and Incident Response") gives an in-depth analysis of AI/ML integration in digital forensics, noting the field is in nascent stages. Its relevance is limited to the observation that young fields benefit from systematic assessments of what their measurements actually capture — the same self-referential metrology concern as [11]; the summary supports no further detail.

Reference [8] (arXiv:cs/0508065v1, "Representing Digital Assets using MPEG-21 Digital Item Declaration") surveys XML-based approaches to representing compound digital assets, including METS, IMS Content Packaging, and XFDU developed by CCSDS Panel 2, and the MPEG-21 Digital Item Declaration. It supplies a formalism for declaring discrete structure over compound content — formally analogous to declaring a two-dimensional computational subspace over a compound Hilbert space — and nothing more.

We emphasize: only [4], [9], [10], [11], [12] carry substantive weight in our argument; [1], [2], [3], [5], [6], [7], [8] are cited for completeness of the supplied corpus and for explicitly-labeled analogies.

## 3. Methods

### 3.1 The transmon Hamiltonian and its level ladder

The transmon is a Cooper-pair box operated at reduced charge dispersion. Its Hamiltonian is

$$H = 4E_C(\hat{n} - n_g)^2 - E_J \cos\hat{\varphi},$$

where $\hat{n}$ is the Cooper-pair number operator, $\hat{\varphi}$ the superconducting phase operator (with $[\hat{\varphi}, \hat{n}] = i$), $E_C$ the charging energy, $E_J$ the Josephson energy, and $n_g$ an offset charge. In the transmon regime $E_J/E_C \gg 1$, the eigenvalues approximate those of a weakly anharmonic oscillator:

$$E_m \approx -E_J + \sqrt{8 E_J E_C}\left(m + \tfrac{1}{2}\right) - E_C\,\frac{6m^2 + 6m + 3}{12}, \qquad m = 0, 1, 2, \dots$$

The $0 \to 1$ transition frequency is $\omega_{01} = \sqrt{8E_JE_C}/\hbar - E_C/\hbar$, and the anharmonicity — the detuning of the $1 \to 2$ transition from the $0 \to 1$ transition — is

$$\alpha \equiv \omega_{12} - \omega_{01} = -\frac{E_C}{\hbar}.$$

The ladder continues indefinitely: for any finite truncation dimension $d$, there exist levels $m \geq d$ that the declared qubit (or qudit of dimension $d$, per [9]) discards. The computational subspace is $\mathcal{H}_{\mathrm{comp}} = \mathrm{span}\{\lvert 0\rangle, \lvert 1\rangle\}$, and the projection $\Pi: \mathcal{H} \to \mathcal{H}_{\mathrm{comp}}$ is the operation whose cost we propose to measure.

### 3.2 Leakage as off-resonant admixture

A control pulse driving the $0 \to 1$ transition with Rabi frequency $\Omega$ does not act only on $\mathcal{H}_{\mathrm{comp}}$; it couples $\lvert 1\rangle$ to $\lvert 2\rangle$ off-resonantly, with detuning $\alpha$. This is the microscopic mechanism by which the forced two-dimensional map leaks population into the discarded manifold. We model the minimal leaking sector as a driven two-state system on $\{\lvert 1\rangle, \lvert 2\rangle\}$ and derive the admixture exactly in the rotating-wave approximation (Section 4). The same structure recurs at every rung: a drive resonant with rung $m \to m+1$ admixes rung $m+2$, so the leakage mechanism is scale-invariant across the ladder — the "fractal" character noted in [12].

### 3.3 Projection entropy and truncation dimension

Following [9], we take the transmon to be a qudit of effective dimension $d \approx 12$ (the dimension over which the oscillator approximation remains experimentally faithful before the cosine potential's level structure deviates strongly from harmonic), and the base entropy cost of the binary projection to be

$$S_{\mathrm{Base}} = \ln\!\left(\frac{d}{2}\right) \ \text{nats per gate}.$$

This is a sourced input, not a derivation of ours; we compute its numerical value and consequences in Section 4.

### 3.4 Overhead coupling

Following [10], we take the quantum error-correction overhead to be $N_{\mathrm{phys}} \in [10^2, 10^3]$ physical operations per logical operation. Each physical operation is an occasion for leakage; the cumulative projection entropy per logical operation is then $N_{\mathrm{phys}} \cdot S_{\mathrm{Base}}$, and the cumulative leakage probability budget scales with $N_{\mathrm{phys}} \cdot p_{\mathrm{leak}}$. Both combinations are computed in Section 4 as labeled projections.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Input inventory

| Quantity | Value | Source |
|---|---|---|
| Truncation dimension $d$ | $12$ | [9], summary: "Transmon is a qudit (d~12), not a qubit" |
| Base projection entropy formula | $S_{\mathrm{Base}} = \ln(d/2)$ | [9], summary: "$S\_Base = \ln(d/2)$ ~ 1.79 nats" |
| QEC overhead $N_{\mathrm{phys}}$ | $10^2$–$10^3$ physical ops per logical op | [10], summary: "quantum error-correction overhead (1e2-1e3 physical operations per logical operation)" |
| Anharmonicity | $\alpha = -E_C/\hbar$ | derived in Section 3.1 from the transmon spectrum |
| Drive detuning on rung 2 | $\Delta = \alpha$ | definition of anharmonicity |

No experimental leakage rates are available in the supplied corpus ([4]'s summary gives none), so all comparisons to hardware are projections with stated assumptions.

### 4.2 Derivation of the leakage scaling law

Consider the driven pair $\{\lvert 1\rangle, \lvert 2\rangle\}$ in the frame rotating at the drive frequency $\omega_{01}$. The drive couples $\lvert 1\rangle \leftrightarrow \lvert 2\rangle$ with matrix element $\Omega/2$ (the factor $1/2$ being the standard rotating-wave decomposition of a dipole drive $\Omega\cos\omega t$), and the state $\lvert 2\rangle$ is detuned by $\alpha$. In the rotating-wave approximation the effective Hamiltonian is

$$H_{\mathrm{eff}} = \begin{pmatrix} 0 & \Omega/2 \\ \Omega/2 & \alpha \end{pmatrix},$$

in units where $\hbar = 1$. Diagonalize: the eigenvalues satisfy

$$\lambda_{\pm} = \frac{\alpha}{2} \pm \frac{1}{2}\sqrt{\alpha^2 + \Omega^2}.$$

The dressed eigenstate connected adiabatically to $\lvert 1\rangle$ (the lower one for $\alpha > 0$; for the transmon $\alpha < 0$ and the labeling flips, but the admixture magnitude is identical) has mixing angle $\theta$ with

$$\tan 2\theta = \frac{\Omega}{\alpha}, \qquad p_{\mathrm{leak}} = \sin^2\theta = \frac{1 - \cos 2\theta}{2} = \frac{1}{2}\left(1 - \frac{\alpha}{\sqrt{\alpha^2 + \Omega^2}}\right).$$

For $\lvert\Omega\rvert \ll \lvert\alpha\rvert$, expand $\sqrt{\alpha^2 + \Omega^2} = \lvert\alpha\rvert\sqrt{1 + \Omega^2/\alpha^2} \approx \lvert\alpha\rvert\left(1 + \frac{\Omega^2}{2\alpha^2}\right)$, giving

$$p_{\mathrm{leak}} \approx \frac{1}{2}\cdot\frac{\Omega^2}{2\alpha^2} = \frac{\Omega^2}{4\alpha^2}.$$

This is the scaling law: **leakage probability per gate scales as the square of the ratio of drive strength to anharmonicity.** Two consequences follow immediately. First, leakage is quadratic in gate speed: faster gates (larger $\Omega$ at fixed gate time target) pay quadratically. Second, leakage is inversely quadratic in anharmonicity: platforms with smaller $\lvert\alpha\rvert$ (more harmonic, more bosonic) leak more at equal gate speed — which is precisely the ontological ordering we propose to test, since a natively two-level (fermionic spin) system has no rung 2 at all and the admixture amplitude is identically zero.

### 4.3 Numerical evaluation of the projection entropy

From [9]: $d = 12$, $S_{\mathrm{Base}} = \ln(d/2)$.

$$S_{\mathrm{Base}} = \ln\!\left(\frac{12}{2}\right) = \ln 6.$$

Compute: $\ln 6 = \ln 2 + \ln 3 = 0.693147 + 1.098612 = 1.791759$ nats.

This matches the $\approx 1.79$ nats stated in [9]. In bits:

$$S_{\mathrm{Base}} = \frac{1.791759}{\ln 2} = \frac{1.791759}{0.693147} = 2.58497 \ \text{bits} \approx 2.585 \ \text{bits per gate}.$$

(Arithmetic check: $0.693147 \times 2.585 = 1.791785$, consistent with $1.791759$ to within rounding at the sixth decimal; we quote $2.585$ bits.)

### 4.4 Cumulative projection entropy per logical operation (projection)

Assumption (sourced): $N_{\mathrm{phys}}$ physical operations per logical operation, $N_{\mathrm{phys}} \in [10^2, 10^3]$ [10]. Assumption (stated): each physical operation incurs the base projection entropy $S_{\mathrm{Base}}$.

Lower end ($N_{\mathrm{phys}} = 10^2$):

$$S_{\mathrm{tot}} = 10^2 \times 1.791759 = 179.1759 \ \text{nats} = \frac{179.1759}{0.693147} = 258.497 \ \text{bits}.$$

Upper end ($N_{\mathrm{phys}} = 10^3$):

$$S_{\mathrm{tot}} = 10^3 \times 1.791759 = 1791.759 \ \text{nats} = \frac{1791.759}{0.693147} = 2584.97 \ \text{bits}.$$

So the digital map discards on the order of $2.6 \times 10^2$ to $2.6 \times 10^3$ bits of projection entropy per protected logical operation. These are projections under the stated per-gate entropy assumption, not measurements.

### 4.5 Leakage budget under a threshold-style constraint (projection)

Assumption (stated, and labeled as an assumption because the supplied corpus contains no measured threshold): suppose the tolerable leakage-induced logical error contribution per logical operation is $\epsilon_{\mathrm{L}} = 10^{-4}$, a round number chosen for illustration. Then the per-gate leakage must satisfy

$$N_{\mathrm{phys}} \cdot p_{\mathrm{leak}} < \epsilon_{\mathrm{L}} \quad \Rightarrow \quad p_{\mathrm{leak}} < \frac{\epsilon_{\mathrm{L}}}{N_{\mathrm{phys}}}.$$

Lower overhead ($N_{\mathrm{phys}} = 10^2$):

$$p_{\mathrm{leak}} < \frac{10^{-4}}{10^2} = 10^{-6}.$$

Upper overhead ($N_{\mathrm{phys}} = 10^3$):

$$p_{\mathrm{leak}} < \frac{10^{-4}}{10^3} = 10^{-7}.$$

Inverting the scaling law $p_{\mathrm{leak}} = \Omega^2/(4\alpha^2)$ for the drive-strength constraint:

$$\frac{\Omega}{\lvert\alpha\rvert} < 2\sqrt{p_{\mathrm{leak}}}.$$

For $p_{\mathrm{leak}} = 10^{-6}$: $\Omega/\lvert\alpha\rvert < 2\sqrt{10^{-6}} = 2 \times 10^{-3} = 0.002$.
For $p_{\mathrm{leak}} = 10^{-7}$: $\Omega/\lvert\alpha\rvert < 2\sqrt{10^{-7}} = 2 \times 3.16228 \times 10^{-4} = 6.32456 \times 10^{-4} \approx 0.00063$.

(Arithmetic: $\sqrt{10^{-7}} = 10^{-3.5} = 3.16228 \times 10^{-4}$; doubling gives $6.32456 \times 10^{-4}$.)

Interpretation: under these assumed budgets, the drive on the computational transition must be weaker than the anharmonicity by a factor of roughly $5 \times 10^2$ to $1.6 \times 10^3$. Since gate rate scales with $\Omega$, this makes the tension between gate speed and leakage explicit and quantitative: the cost of the bit map is paid either as leakage (at practical drive strengths) or as slowed gates (to suppress it).

### 4.6 Modality-level scaling prediction

The scaling law $p_{\mathrm{leak}} \propto \lvert\alpha\rvert^{-2}$, combined with the structure of the native Hilbert space, yields the falsifiable ordering:

- **Spin qubits** (fermionic): native Hilbert space is two-dimensional; there is no rung 2, so the admixture amplitude is identically zero and $p_{\mathrm{leak}}^{\mathrm{spin}} = 0$ in the ideal model (any observed leakage is due to extrinsic degrees of freedom, e.g., motional or charge noise, not intrinsic projection cost).
- **Transmons** (bosonic, weakly anharmonic): $p_{\mathrm{leak}} = \Omega^2/(4\alpha^2) > 0$, with $\lvert\alpha\rvert$ small in absolute frequency terms relative to strongly anharmonic cousins.
- **Fluxonium and cat qubits** (bosonic, differently shaped ladders): nonzero leakage with a modality-specific effective $\alpha_{\mathrm{eff}}$; the prediction is that the measured leakage rates across these platforms collapse onto the curve $\Omega^2/(4\alpha_{\mathrm{eff}}^2)$ when plotted against the appropriate anharmonicity scale.

This ordering — bosonic platforms systematically exceed fermionic ones, with magnitude governed by $\lvert\alpha\rvert^{-2}$ — is the paper's central falsifiable claim.

## 5. Results

We separate **derived** quantities (computed in Section 4 from stated inputs) from **projections** (computed under explicitly stated assumptions not independently sourced).

**Derived:**

- R1. Leakage scaling law: $p_{\mathrm{leak}} \approx \Omega^2/(4\alpha^2)$ per gate, valid for $\lvert\Omega\rvert \ll \lvert\alpha\rvert$ (Section 4.2, full diagonalization shown).
- R2. Anharmonicity of the transmon: $\alpha = -E_C/\hbar$ (Section 3.1, from the cosine-Hamiltonian spectrum).
- R3. Base projection entropy: $S_{\mathrm{Base}} = \ln 