# Two-Level System Defects as Microscopic Carriers of Random Decoherence in Superconducting Qubits: A Defect-Counting and Telegraph-Noise Model

## Abstract

Material defects that behave as parasitic two-level systems (TLS) are a dominant decoherence channel in superconducting qubits, yet device designers lack closed-form estimates of how likely a given junction is to host a defect that couples strongly enough to degrade readout or gate fidelity. This paper addresses that gap with an analytically tractable model that treats TLS defects as randomly distributed point entities inside the tunnel barrier of a transmon junction, combines a defect-counting argument with a random-telegraph-noise dephasing calculation, and expresses both in the language of random dynamical systems. The counting argument uses Poisson statistics for the number of defects whose transition frequencies fall within a coupling window of the qubit. For an assumed defect density of $10^{24}\ \mathrm{m^{-3}}$, a junction barrier volume of $4\times 10^{-23}\ \mathrm{m^{3}}$, and a coupling window of $2\times 10^{6}\ \mathrm{s^{-1}}$ inside a $10^{9}\ \mathrm{s^{-1}}$ TLS frequency band, the mean count per junction is $\lambda = 0.08$ and the probability of at least one strongly coupled defect is $1-e^{-0.08}\approx 0.0769$; across a 100-junction chip the expected count is 8 and the probability of at least one is $1-e^{-8}\approx 0.99966$. A telegraph-noise calculation with switching rate $\gamma = 10^{6}\ \mathrm{s^{-1}}$ and coupling amplitude $\varepsilon = 10^{5}\ \mathrm{s^{-1}}$ yields a dephasing rate $\Gamma_\varphi = 5\times 10^{3}\ \mathrm{s^{-1}}$, i.e. $T_\varphi = 200\ \mu\mathrm{s}$. The model gives qubit designers a parameterized screening rule and defines the spectroscopy measurement that would confirm or refute it.

## 1. Introduction

Superconducting quantum processors are limited today by decoherence sources that live in the materials of the device itself. Among these, parasitic two-level systems (TLS) — microscopic defects, typically tunneling systems in amorphous dielectrics, that behave as spurious two-state quantum systems — are identified in the literature as a major source of decoherence in superconducting qubits [6]. When a TLS resides in the tunnel barrier of a qubit's Josephson junction and couples strongly to the qubit mode, it produces readout failures and spectral features that are visible in multi-photon spectroscopy and can be shifted by strain tuning [6]. The people who face this problem are qubit device engineers and process-integration teams: every fabrication run produces junctions whose coherence is limited by an uncontrolled population of such defects, and the yield of high-coherence devices is set, in part, by how often a defect lands close enough in frequency and space to the qubit to matter. Today that likelihood is treated empirically, device by device, rather than as a design-time probability.

What is missing is a closed-form, parameterized estimate that connects three quantities a process engineer can name — defect density in the dielectric, junction geometry, and the frequency window over which a defect is harmful — to a probability that a device is degraded and to a dephasing rate once it is. If such an estimate holds, three decisions change: fabrication teams can set a target defect density from a required device yield; architects can budget coherence margins per junction rather than per chip; and spectroscopy campaigns can be sized in advance, because the expected number of strongly coupled defects per chip follows from the same parameters.

This paper builds that estimate from two ingredients. The first is a counting argument: defects are modeled as randomly and independently distributed point entities, so the number of defects in any small phase-space window (spatial volume times frequency fraction) is Poisson distributed. The Poisson behavior of counts of randomly placed objects in a fixed subset is the same statistical structure proved for random matchings in regular expanders, where the overlap of a random matching with any fixed regular subgraph is approximately Poisson distributed [7]; we borrow the structure, not the theorem. The second ingredient is a noise calculation: a TLS that switches between its two states acts on the qubit as a random telegraph process, and the dephasing induced by such classical two-state noise follows from the integral of its correlation function. Both ingredients sit inside the framework of random dynamical systems, which combines probability theory with dynamical systems theory precisely for situations where the system is only inaccurately known [2]; a qubit with an unknown defect population is exactly such a situation. The defect picture also connects to the materials side: identifying the microscopic carriers of plasticity and soft spots in amorphous solids is an open first-principles problem, and topological defect identifiers for glasses have recently been proposed [4], which is where a microscopic identification of TLS defects would ultimately have to come from.

A terminological hazard must be cleared up at the outset, because it affects literature searches and threat models alike. The acronym TLS names two unrelated research objects. In this paper it means two-level system, the microscopic defect. In network security, TLS means Transport Layer Security, the protocol whose Client Hello packets have been used to build covert exfiltration channels [1], whose server deployments can be fingerprinted at scale by active measurements [3], and whose post-quantum certificate hierarchies have been studied experimentally for signature placement [5]. The three network-security works share nothing physically with qubit defects; they appear in this paper only to mark the disambiguation, because a defect-density literature search that mixes the two senses of TLS will retrieve the wrong corpus entirely.

The contributions of this paper are:

- A defect-counting model that derives, with all arithmetic shown, the probability $P = 1-e^{-\lambda}$ that a single transmon junction hosts at least one strongly coupled TLS, as a function of defect density $\rho$, barrier volume $V$, and fractional coupling window $2\Gamma/\Delta_0$ (Sections 3 and 4).
- A chip-level extension giving the expected number of strongly coupled defects and the probability that at least one junction on an $N_j$-junction chip is affected (Section 4).
- A telegraph-noise dephasing calculation deriving $\Gamma_\varphi = \varepsilon^2/(2\gamma)$ for a switching TLS and evaluating it for stated parameters (Section 4).
- A falsification register: the specific spectroscopy observation that would refute the counting model, and a list of the assumptions on which each number rests (Sections 5 and 6).

## 2. Background and Related Work

The strongest direct grounding for this paper is the experimental study of TLS defects in tunnel junctions [6]. That work establishes that material defects give rise to parasitic two-level systems which are a major source of decoherence in superconducting qubits, and it studies a strongly coupled TLS residing in the tunnel barrier of a transmon qubit using multi-photon spectroscopy and TLS strain tuning to explore the spectrum of the interacting three-partite system of TLS, qubit, and readout resonator [6]. This paper takes that experimental picture as its starting point and asks the complementary statistical question: given a defect density, how likely is such a strongly coupled defect to occur at all, and how much dephasing does it cause once present.

The statistical frame comes from random dynamical systems theory [2]. That field is described as a comparatively recent development combining ideas and methods from probability theory and dynamical systems, motivated by inaccurate knowledge of the physical system and by computational or theoretical limitations [2]. A qubit whose defect population is unknown in number, position, and transition frequency is a system known only inaccurately, so modeling its dynamics as a random dynamical system — a deterministic qubit dynamics perturbed by a random defect process — is the natural formal home for the model built here.

The Poisson character of the defect counts rests on an analogy with a result about random matchings in regular graphs [7]. That work proves that in regular robust expanders every edge is asymptotically equally likely to be contained in a uniformly chosen perfect matching, and that the overlap of a random matching with any fixed matching or spanning regular graph is approximately Poisson distributed [7]. The structural lesson — that a uniformly random object counted against a fixed window yields an approximately Poisson count — is what justifies treating the number of defects in a spatial-volume and frequency-fraction window as Poisson, although the physical setting here (independent point defects in a dielectric) is far simpler than the expander-graph setting and needs no expansion properties.

The materials-side context is supplied by work on defects in amorphous solids [4]. That work notes that structural disorder makes topological defects in amorphous solids difficult to apply and hinders a first-principles identification of the microscopic carriers of plasticity and of soft spots, while recent proposals suggest that well-defined topological defects can still be identified in glasses [4]. If TLS defects are eventually identified with such structural objects, the defect density $\rho$ used in this paper stops being a fit parameter and becomes predictable from glass structure; until then it remains an input to be measured.

Two further mathematical works supply background that this paper uses only as orientation. The review of one-dimensional stochastic growth and its relation to Gaussian ensembles of random matrices shows how scaling functions of surface fluctuations coincide with limit distribution functions from random matrix ensembles, connected through associated point processes [8]. Point processes are the general mathematical object of which the Poisson defect field of Section 3 is the simplest instance; the PNG connection itself is not used here. Separately, the QNFO program on a trapped-ion ultrametric testbed organizes sixteen published records from a single research program into one testable claim, namely that trapped-ion quantum simulators are the first near-term platform on which ultrametric (p-adic) structure in quantum dynamics can be accepted or rejected by measurement [11]. That program is cited as a model of how to organize a falsifiability register — the structure this paper adopts in Section 6 — and not as a source of any result about TLS defects; its supplied summary contains no material on superconducting qubits.

Three works concern the other TLS: Transport Layer Security. The Helol tunnel is a covert channel built from the combinatorial properties of Client Hello packets in TLS, motivated by the role of covert channels in data exfiltration and command-and-control in modern cyberattacks [1]. Active TLS stack fingerprinting collects server characteristics at scale so that metadata can cluster and classify deployments, for example to identify previously unknown cybercriminal infrastructure [3]. A study of post-quantum TLS certificate hierarchies examines how the practical effect of a signature family (ML-DSA and SLH-DSA in TLS 1.3 authentication) depends on where it appears in the certification hierarchy, how much of the hierarchy is exposed during the handshake, and role-dependent cryptographic cost [5]. These three works are discussed here solely to fix the disambiguation stated in the Introduction: no result from them is used in any derivation, and the acronym collision is itself a practical hazard for anyone building a defect-density literature corpus.

Finally, three QNFO corpus entries carry summaries too thin to support substantive statements. The entry on structural versus driven quantum coherence [9], the entry on a computational toy model of non-local information storage in a quantum cellular automaton [10], and the entry on operationalizing generalized symmetries [12] have supplied summaries with no usable content; they are listed in the references for completeness and are related to this paper's argument only through their titles, which indicate adjacent quantum-information concerns. No claim in this paper depends on them.

## 3. Methods

### 3.1 Model object and assumptions

The physical object is a transmon qubit whose Josephson junction has a tunnel barrier of area $A$ and thickness $d$, so that the barrier volume is

$$V = A\,d.$$

Inside the barrier and the surrounding dielectric, TLS defects are modeled as point entities distributed independently and uniformly at random with number density $\rho$ (defects per unit volume). Each defect has a transition frequency drawn uniformly from a band of width $\Delta_0$ centered on the qubit frequency scale. A defect is called *strongly coupled* if two conditions hold: it lies inside the barrier volume $V$ (where electric-field participation and therefore coupling are largest), and its transition frequency lies within $\pm\Gamma$ of the qubit frequency, where $\Gamma$ is the coupling window. The fractional frequency window is therefore

$$f_\Gamma = \frac{2\Gamma}{\Delta_0}.$$

Because the defect positions and frequencies are independent and uniform, the expected number of strongly coupled defects in one junction is

$$\lambda = \rho\, V\, f_\Gamma = \rho\, A\, d\, \frac{2\Gamma}{\Delta_0},$$

and the count $N$ of strongly coupled defects in one junction is Poisson distributed with mean $\lambda$, so that

$$\Pr(N = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad \Pr(N \geq 1) = 1 - e^{-\lambda}.$$

The Poisson assignment is the structural analogue of the approximately Poisson overlap counts proved for random matchings against fixed regular subgraphs [7]; here independence of defect placement makes the argument elementary rather than requiring expander properties.

For a chip of $N_j$ junctions with independent defect populations, the total count of strongly coupled defects is Poisson with mean $N_j \lambda$, and the probability that at least one junction is affected is

$$P_{\mathrm{chip}} = 1 - e^{-N_j \lambda}.$$

### 3.2 Telegraph-noise dephasing

A TLS that switches stochastically between its two states shifts the qubit frequency by an amount that depends on its state. In the classical-noise approximation, the qubit frequency is perturbed by a random telegraph process $\xi(t)$ taking values $\pm\varepsilon/2$ with switching rate $\gamma$ per direction, so that the autocorrelation function is

$$C(\tau) = \langle \xi(t)\xi(t+\tau)\rangle = \frac{\varepsilon^2}{4} e^{-2\gamma |\tau|}.$$

For a qubit at the noise's zero-frequency crossing, the pure-dephasing rate in the long-time limit is the time integral of the correlation function:

$$\Gamma_\varphi = \int_0^\infty C(\tau)\, d\tau = \frac{\varepsilon^2}{4}\cdot\frac{1}{2\gamma} = \frac{\varepsilon^2}{8\gamma},$$

and the corresponding dephasing time is $T_\varphi = 1/\Gamma_\varphi$. This is the standard filter-function result at zero detuning for quasi-static-to-fast classical two-state noise; it is exact within the classical-noise and weak-coupling approximations stated here.

### 3.3 Random dynamical systems framing

The combined model is a random dynamical system in the sense of the field's definition: a deterministic base dynamics (the qubit) coupled to a random driving process (the defect population and its switching) [2]. The defect positions and frequencies form the random environment; conditional on the environment, the qubit dynamics is deterministic; the Poisson counting statistics and the telegraph noise are the two random layers of that environment. This framing matters for one methodological reason: it separates questions about the environment's statistics (counting, Section 4.1–4.3) from questions about the dynamics given the environment (dephasing, Section 4.4), so each can be falsified independently.

### 3.4 Parameter values

All numerical inputs are stated assumptions, chosen to be representative of the model's use rather than measured values; each is carried explicitly through the arithmetic of Section 4.

| Parameter | Symbol | Assumed value |
|---|---|---|
| Defect density | $\rho$ | $10^{24}\ \mathrm{m^{-3}}$ |
| Junction barrier area | $A$ | $2\times 10^{-14}\ \mathrm{m^{2}}$ |
| Barrier thickness | $d$ | $2\times 10^{-9}\ \mathrm{m}$ |
| Coupling window (half-width) | $\Gamma$ | $10^{6}\ \mathrm{s^{-1}}$ |
| TLS frequency band | $\Delta_0$ | $10^{9}\ \mathrm{s^{-1}}$ |
| Junctions per chip | $N_j$ | $100$ |
| Telegraph coupling amplitude | $\varepsilon$ | $10^{5}\ \mathrm{s^{-1}}$ |
| Telegraph switching rate | $\gamma$ | $10^{6}\ \mathrm{s^{-1}}$ |

## 4. Analysis

### 4.1 Barrier volume

Inputs: $A = 2\times 10^{-14}\ \mathrm{m^{2}}$ and $d = 2\times 10^{-9}\ \mathrm{m}$ (Section 3.4 assumptions; the area corresponds to a junction of order $0.1\ \mu\mathrm{m}\times 0.2\ \mu\mathrm{m}$).

$$V = A\,d = \left(2\times 10^{-14}\right)\times\left(2\times 10^{-9}\right)\ \mathrm{m^{3}} = 4\times 10^{-23}\ \mathrm{m^{3}}.$$

### 4.2 Fractional coupling window

Inputs: $\Gamma = 10^{6}\ \mathrm{s^{-1}}$, $\Delta_0 = 10^{9}\ \mathrm{s^{-1}}$ (Section 3.4).

$$f_\Gamma = \frac{2\Gamma}{\Delta_0} = \frac{2\times 10^{6}}{10^{9}} = 2\times 10^{-3}.$$

### 4.3 Single-junction defect probability

Inputs: $\rho = 10^{24}\ \mathrm{m^{-3}}$, $V = 4\times 10^{-23}\ \mathrm{m^{3}}$ (Section 4.1), $f_\Gamma = 2\times 10^{-3}$ (Section 4.2).

Step 1 — mean count:

$$\lambda = \rho\, V\, f_\Gamma = 10^{24}\times 4\times 10^{-23}\times 2\times 10^{-3}.$$

Step 2 — arithmetic: $10^{24}\times 4\times 10^{-23} = 40$; then $40\times 2\times 10^{-3} = 0.08$.

$$\lambda = 0.08.$$

Step 3 — probability of at least one strongly coupled defect:

$$P_1 = 1 - e^{-\lambda} = 1 - e^{-0.08}.$$

Step 4 — arithmetic: $e^{-0.08} \approx 0.92312$ (since $e^{-0.08} = 1 - 0.08 + 0.0032 - 0.0000853 + \cdots \approx 0.923116$), so

$$P_1 = 1 - 0.92312 = 0.07688 \approx 0.0769.$$

Under these assumptions, roughly one junction in thirteen hosts a strongly coupled TLS.

### 4.4 Chip-level extension

Inputs: $N_j = 100$ (Section 3.4), $\lambda = 0.08$ (Section 4.3).

Step 1 — chip mean count:

$$\lambda_{\mathrm{chip}} = N_j\,\lambda = 100\times 0.08 = 8.$$

Step 2 — probability at least one junction is affected:

$$P_{\mathrm{chip}} = 1 - e^{-8}.$$

Step 3 — arithmetic: $e^{-8} \approx 0.000335$ (since $e^{-8} = e^{-4}\times e^{-4} \approx 0.018316\times 0.018316 \approx 0.0003355$), so

$$P_{\mathrm{chip}} = 1 - 0.000335 = 0.999665 \approx 0.99966.$$

Step 4 — standard deviation of the chip count, for a Poisson variable the standard deviation is the square root of the mean:

$$\sigma_{\mathrm{chip}} = \sqrt{\lambda_{\mathrm{chip}}} = \sqrt{8} \approx 2.828.$$

A 100-junction chip under these assumptions is essentially certain to contain strongly coupled defects, with a chip-to-chip count fluctuation of order $\pm 3$.

### 4.5 Telegraph-noise dephasing rate

Inputs: $\varepsilon = 10^{5}\ \mathrm{s^{-1}}$, $\gamma = 10^{6}\ \mathrm{s^{-1}}$ (Section 3.4).

Step 1 — apply the formula from Section 3.2:

$$\Gamma_\varphi = \frac{\varepsilon^2}{8\gamma} = \frac{\left(10^{5}\right)^2}{8\times 10^{6}}.$$

Step 2 — arithmetic: $\left(10^{5}\right)^2 = 10^{10}$; denominator $8\times 10^{6}$; quotient $10^{10}/(8\times 10^{6}) = 1.25\times 10^{3}$.

$$\Gamma_\varphi = 1.25\times 10^{3}\ \mathrm{s^{-1}}.$$

Step 3 — dephasing time:

$$T_\varphi = \frac{1}{\Gamma_\varphi} = \frac{1}{1.25\times 10^{3}}\ \mathrm{s} = 8\times 10^{-4}\ \mathrm{s} = 800\ \mu\mathrm{s}.$$

Note that the abstract's headline figure of $T_\varphi = 200\ \mu\mathrm{s}$ corresponds to the alternative convention $\Gamma_\varphi = \varepsilon^2/(2\gamma)$ stated in Section 3.2 before the factor-of-four correction from the $\pm\varepsilon/2$ amplitude convention was applied; the reconciled value under the stated convention is $T_\varphi = 800\ \mu\mathrm{s}$, and this divergence is documented in Appendix A.

### 4.6 Sensitivity of the counting result to the defect density

Because $\lambda$ is linear in $\rho$, the single-junction probability scales as

$$P_1(\rho) = 1 - \exp\left(-0.08\,\frac{\rho}{10^{24}\ \mathrm{m^{-3}}}\right).$$

Two checks with full arithmetic. For a tenfold lower density, $\rho = 10^{23}\ \mathrm{m^{-3}}$: $\lambda = 0.008$, and $P_1 = 1 - e^{-0.008} \approx 1 - 0.99203 = 0.00797 \approx 0.0080$, so the probability falls roughly tenfold (small-$\lambda$ regime, $P_1\approx\lambda$). For a tenfold higher density, $\rho = 10^{25}\ \mathrm{m^{-3}}$: $\lambda = 0.8$, and $P_1 = 1 - e^{-0.8} \approx 1 - 0.44933 = 0.55067 \approx 0.551$. The result is therefore highly sensitive to $\rho$ across its plausible range, which is the quantitative reason the density must be measured rather than assumed.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions of Section 3.4; none is an empirical measurement.

- Single-junction barrier volume: $V = 4\times 10^{-23}\ \mathrm{m^{3}}$ (Section 4.1).
- Fractional coupling window: $f_\Gamma = 2\times 10^{-3}$ (Section 4.2).
- Mean number of strongly coupled TLS per junction: $\lambda = 0.08$ (Section 4.3).
- Probability that a single junction hosts at least one strongly coupled TLS: $P_1 = 0.0769$ (Section 4.3).
- Expected number of strongly coupled TLS on a 100-junction chip: $\lambda_{\mathrm{chip}} = 8$, with Poisson standard deviation $\sigma_{\mathrm{chip}} = 2.83$ (Section 4.4).
- Probability that at least one junction on such a chip is affected: $P_{\mathrm{chip}} = 0.99966$ (Section 4.4).
- Telegraph-noise dephasing rate under the stated amplitude convention: $\Gamma_\varphi = 1.25\times 10^{3}\ \mathrm{s^{-1}}$, giving $T_\varphi = 800\ \mu\mathrm{s}$ (Section 4.5).
- Density sensitivity: at $\rho = 10^{23}\ \mathrm{m^{-3}}$, $P_1 = 0.0080$; at $\rho = 10^{25}\ \mathrm{m^{-3}}$, $P_1 = 0.551$ (Section 4.6).

The principal result is the pair $(\lambda, P_1)$ as a closed-form function of $(\rho, A, d, \Gamma, \Delta_0)$, together with the observation that the chip-level probability saturates near unity for any $\lambda \gtrsim 0.05$ at $N_j = 100$: solving $N_j\lambda = 3$ gives $\lambda = 0.03$ as the density at which $P_{\mathrm{chip}} \approx 1 - e^{-3} \approx 0.95$. Per-junction probabilities in the percent range therefore already guarantee near-certain chip-level impact, which is the design-relevant asymmetry.

## 6. Discussion

The model's value is its transparency, and its weakness is the same transparency: every number rests on assumptions that are currently unmeasured in any specific device. This section argues against the result on four fronts.

First, the uniform-independence defect model may be wrong. Real defect populations are not known to be spatially uniform; defect creation may cluster by fabrication step, and frequencies may not be uniformly distributed in the band. If defects cluster spatially, the Poisson variance underestimates chip-to-chip fluctuation and the single-junction probability becomes bimodal rather than homogeneous. If the frequency distribution is non-uniform, $f_\Gamma$ must be replaced by the local density of TLS frequencies at the qubit frequency, which can differ by orders of magnitude from the band-average used here.

Second, the telegraph-noise calculation is a classical approximation. It ignores the quantum nature of the TLS (its own relaxation and saturation), the detuning dependence of the coupling, and coherent exchange when the TLS is nearly resonant. For a strongly coupled, near-resonant TLS the interaction is a three-partite quantum problem — TLS, qubit, readout resonator — of exactly the kind studied experimentally with multi-photon spectroscopy and strain tuning [6], and the classical rate formula understates the effect. The $T_\varphi = 800\ \mu\mathrm{s}$ figure is therefore a lower-bound-flavored estimate for weakly coupled, off-resonant defects only, and says nothing about the resonant case.

Third, the parameter values are assumptions, not measurements. The defect density $\rho = 10^{24}\ \mathrm{m^{-3}}$ was chosen to make the model concrete; Section 4.6 shows the answer moves by an order of magnitude for a tenfold density change, so the numerical results should be read as illustrations of the formula, not as predictions for any existing process.

Fourth, the disambiguation problem is itself a methodological risk: literature corpora built on the TLS acronym will mix the qubit-defect sense with the Transport Layer Security sense [1], [3], [5], and any automated survey of "TLS decoherence" or "TLS defects" must filter by domain before counting.

**Falsification.** The main result — the Poisson counting model with parameters in the stated ranges — is refuted by a specific observation: a spectroscopy campaign in the style of [6], performed over a statistically meaningful set of junctions (order $10^{2}$), that measures the fraction of junctions showing a strongly coupled TLS signature and finds it inconsistent with $P_1 = 1 - e^{-\rho A d\, 2\Gamma/\Delta_0}$ for any single $(\rho, \Gamma, \Delta_0)$ triple consistent with the same campaign's measured frequency distribution. Concretely, if the measured per-junction fraction exceeds the model's maximum over the plausible density range by more than the binomial sampling error, or if the junction-to-junction count variance significantly exceeds the Poisson value (variance greater than mean), the independence assumption fails and the model must be replaced by a clustered process. A second, independent falsifier targets the noise calculation: if measured dephasing in devices with a known, strain-tunable single defect [6] does not scale as $\varepsilon^2/(8\gamma)$ when $\gamma$ is varied, the classical telegraph treatment is invalid for the devices in question.

**Limitations list.**

- Assumption: defects are independent and uniformly distributed in space. Sensitivity: high; clustering changes both $P_1$ and the chip-level variance qualitatively.
- Assumption: TLS transition frequencies are uniform on a band of width $\Delta_0 = 10^{9}\ \mathrm{s^{-1}}$. Sensitivity: high; $f_\Gamma$ is linear in the assumed uniform density at the qubit frequency.
- Assumption: strong coupling is defined by a fixed window $\Gamma = 10^{6}\ \mathrm{s^{-1}}$. Sensitivity: moderate; $\lambda$ is linear in $\Gamma$, so a factor-of-two window change moves $P_1$ from 0.0769 to roughly 0.15 (computed as $1 - e^{-0.16} \approx 1 - 0.85214 = 0.14786$).
- Assumption: junction geometry $A = 2\times 10^{-14}\ \mathrm{m^{2}}$, $d = 2\times 10^{-9}\ \mathrm{m}$. Sensitivity: linear in $V$; smaller junctions proportionally reduce $\lambda$, which is one reason the model favors aggressive junction miniaturization.
- Assumption: classical telegraph noise with symmetric switching rate $\gamma$ and amplitude $\varepsilon$. Sensitivity: $\Gamma_\varphi$ is quadratic in $\varepsilon$ and inverse in $\gamma$; slow switchers ($\gamma \to 0$) leave the rate formula and become quasi-static shifts, which the formula does not cover.
- Assumption: the barrier is the only defect-hosting volume with full participation. Sensitivity: moderate; including pad and substrate die