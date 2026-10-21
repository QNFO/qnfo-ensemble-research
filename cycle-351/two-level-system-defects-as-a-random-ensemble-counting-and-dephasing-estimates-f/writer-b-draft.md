# Two-Level System Defects as a Random Ensemble: Counting and Dephasing Estimates for Superconducting Qubits

## Abstract

Parasitic two-level system (TLS) defects in the amorphous tunnel barriers of superconducting qubits are a major identified source of decoherence, yet device designers lack closed-form estimates linking defect density and junction geometry to the probability that a device is degraded and to the resulting dephasing rate. This paper models the defect population of a Josephson junction as a random ensemble — a random dynamical system in which defect positions and frequencies are random variables and the qubit is a deterministic observer — and derives two complementary closed-form results. A Poisson counting argument gives the probability that a junction hosts a strongly coupled defect: for an assumed density of $10^{24}\ \mathrm{m^{-3}}$, a barrier volume of $4\times 10^{-23}\ \mathrm{m^{3}}$, and a fractional coupling window of $2\times 10^{-3}$, the mean count is $\lambda = 0.08$ and the single-junction probability is $P_1 = 0.0769$; on a 100-junction chip the expected count is 8 and the affected-chip probability is $0.99966$. A dephasing calculation for off-resonant defects gives $\Gamma_\varphi = 5\ \mathrm{s^{-1}}$ ($T_\varphi = 0.2\ \mathrm{s}$) for a five-defect sub-band configuration, and $T_\varphi = 800\ \mu\mathrm{s}$ under a telegraph-noise model for a switching defect. The results convert defect decoherence from a device-by-device pathology into an ensemble-level design parameter with an explicit falsification register.

## 1. Introduction

Superconducting quantum processors lose coherence faster than their control electronics or circuit designs require, and a large share of the loss is traced to the materials of the device itself. Atomic-scale defects in the amorphous oxides and tunnel barriers of superconducting circuits behave as parasitic two-level systems (TLS): quantum systems with two accessible states whose transition frequencies lie in the gigahertz band occupied by the qubit. When a defect resides in the tunnel barrier of a Josephson junction and couples strongly to the qubit mode, it produces readout failures and spectral features visible in multi-photon spectroscopy and shiftable by strain tuning; the experimental study of a strongly coupled TLS in a transmon tunnel barrier documents exactly this three-partite interaction among TLS, qubit, and readout resonator, including avoided level crossings observed in both the single-photon $|0\rangle\rightarrow|1\rangle$ transition at 6.2 GHz and the two-photon $|0\rangle\rightarrow|2\rangle$ transition at 6.08 GHz [6]. The people who face this problem are qubit device engineers, process-integration teams, and cryogenic measurement groups: every fabrication run produces junctions whose coherence is limited by an uncontrolled defect population, and the yield of high-coherence devices is set in part by how often a defect lands close enough in frequency and space to matter. The stakes extend beyond superconducting processors: any quantum architecture that must allocate physical hardware against decoherence carries a comparable burden, and analyses of quantum fragility argue that error-correction overheads such as physical-to-logical qubit ratios of order 1000:1 for surface codes already strain resources [10]. A predictive defect statistic would reduce one input to that overhead directly.

Today that likelihood is treated empirically, device by device. A defect that ruins qubit $j$ on chip $A$ is characterized there, but the same fabrication process places different defects on chip $B$, so the fix does not transfer. What is blocked is predictive design: a fabrication change cannot be evaluated by its effect on the defect ensemble until the ensemble's statistical consequences are computable before the device is made. If the defect population is treated statistically — as a random ensemble with measurable density, frequency distribution, and coupling distribution — then three decisions change. Fabrication teams can set a target defect density from a required device yield. Architects can budget coherence margins per junction rather than per chip. Spectroscopy campaigns can be sized in advance, because the expected number of strongly coupled defects per chip follows from the same parameters.

The core idea is a change of statistical frame. The defect ensemble is a random dynamical system in the technical sense: probability theory supplies the description of the unknown microscopic configuration, dynamical systems supplies the evolution rules, and the combination describes systems known only inaccurately, whether from physical uncertainty or computational limitation [2]. The qubit is a deterministic probe coupled to this random background. The same reframing has precedent in disordered materials: in amorphous solids, structural disorder long hindered first-principles identification of the microscopic carriers of plasticity, until well-defined topological defects — hedgehog defects in three-dimensional amorphous solids — were shown to be identifiable and correlatable with soft spots [4]. The TLS defects of superconducting junctions are the analogous microscopic carriers of decoherence, and this paper imports the same move: name the carriers, then treat their spatial and spectral arrangement as a random ensemble.

The contributions are:

- A formulation of the junction defect population as a random dynamical system, with defect spectral positions as the random state and the qubit as the deterministic observer (Section 3).
- A closed-form derivation of the near-resonance probability $P_{\geq 1} = 1 - e^{-\lambda}$ under two parameterizations — spectral counting and spatio-spectral counting — evaluated with all arithmetic shown to $P_{\geq 1} = 0.0999$ and $P_1 = 0.0769$ respectively, with a chip-level extension giving $P_{\mathrm{chip}} = 0.99966$ for 100 junctions (Section 4).
- A derivation of the ensemble-averaged dispersive dephasing rate $\Gamma_\varphi = \sum_i (g_i/\Delta_i)^2 \gamma_i$, evaluated to $T_\varphi = 0.2\ \mathrm{s}$ for five sub-band defects, and a telegraph-noise dephasing rate $\Gamma_\varphi = \varepsilon^2/(8\gamma)$, evaluated to $T_\varphi = 800\ \mu\mathrm{s}$ (Section 4).
- A sensitivity analysis showing that the counting result moves by an order of magnitude per tenfold change in defect density, and that the dephasing rate is quadratic in coupling (Section 4).
- A falsification register: the specific spectroscopy observations that would refute the counting model and the noise model, and a list of the assumptions on which each number rests (Sections 6 and 7).

## 2. Background and Related Work

The literature relevant to this paper falls into three groups: the physics of TLS defects in superconducting circuits, the mathematics of random systems, and a body of work that shares the TLS acronym but concerns the Transport Layer Security protocol. All three are discussed here, because the acronym collision is itself a practical obstacle to literature search in this area and because the protocol-side works illustrate a general point about statistical treatment of large configuration spaces.

On the physics side, the central experimental anchor is the study of readout failures in superconducting qubits due to TLS defects in tunnel junctions [6]. That work identifies material defects as the origin of parasitic two-level systems that constitute a major source of decoherence in superconducting qubits, and it studies a strongly coupled TLS residing in the tunnel barrier of a transmon qubit using multi-photon spectroscopy and TLS strain tuning to explore the spectrum of the interacting three-partite system of TLS, qubit, and readout resonator. Its discussion reports that the parasitic TLS-resonator interaction detunes the resonator frequency by an amount of similar size to the dispersive shift used for qubit readout, and thus spoils the measurement, and that the resonator may inherit excess energy relaxation from TLS with typical quality factors below 5000. Its appendix records Manhattan-style junction areas of about 200 nm × 220 nm and mechanical strain of order $10^{-6}$ per applied Volt on the piezo actuator, with the investigated sample showing $T_1 \approx 1$–$2\ \mu\mathrm{s}$ while other qubits on the same chip reached up to $28\ \mu\mathrm{s}$. The junction geometry and the strain-tuning protocol from [6] are used directly in this paper: the area fixes the order of magnitude of the barrier volume, and strain tuning supplies the identification method for individual strongly coupled defects. The interacting spectrum is reported as rich, which is precisely the regime where single-defect intuition fails and ensemble statistics become necessary; the present paper supplies that statistical layer. All densities used below are stated assumptions of this paper, not measurements.

The statistical machinery comes from two traditions. The theory of random dynamical systems [2] combines ideas and methods from probability theory and dynamical systems, motivated by inaccurate knowledge of the particular physical system or by computational and theoretical limitations such as insufficient computational power, inefficient algorithms, or insufficiently developed mathematical tools. Its formalism models random perturbations of a base transformation $T_0$ through transition probabilities $\{p(\cdot\mid x)\}$ on the state space, with stationary measures defined by $\mu(A)=\int p(A\mid x)\,d\mu(x)$, and it recalls the multiplicative ergodic theorem for products of independent random matrices, which yields ordered random Lyapunov exponents $\lambda_1\geq\lambda_2\geq\dots$. This motivation matches the defect problem exactly: the microscopic defect configuration of a given junction is unknowable in detail, so the configuration must be treated as a random state evolved under known dynamics. On the fluctuation side, the review of one-dimensional stochastic growth and its connection to Gaussian ensembles of random matrices [8] establishes that for the polynuclear growth (PNG) model — a member of the KPZ universality class with dynamical exponent $z=3/2$ — the scaling functions of surface fluctuations for both curved and flat growth coincide with limit distribution functions from Gaussian random-matrix ensembles, with the connection explained through point processes associated to the model; the PNG droplet converges in probability to the limit shape $2\sqrt{1-\tau^{2}}$. The methodological lesson imported here is that spatial or spectral point processes of disordered systems can carry non-trivial fluctuation statistics, which motivates treating the defect frequency positions as a point process rather than as independent fixed quantities.

Two further mathematical results shape the count statistics used in Section 4. The theorem on random perfect matchings in regular graphs [7] proves that in all regular robust expanders every edge is asymptotically equally likely to be contained in a uniformly chosen perfect matching, with $\mathbb{P}[e\in M]=(1\pm n^{-1/8})d^{-1}$ for a $d$-regular graph on $n$ vertices, and that for any fixed matching or spanning regular graph $N$ in $G$ the overlap $|M\cap E(N)|$ is approximately Poisson distributed, with the proof reducing the count to $Y\sim\mathrm{Po}(\lambda)$ for $\lambda = d^{-1}|N|$. The Poisson limit for an overlap count of a random object against a fixed background is the same limit structure that Section 4 uses for the count of defects falling inside a fixed spatial-and-frequency window, although the physical setting of independent point defects is far simpler than the expander-graph setting and needs no expansion properties. And in amorphous solids, the hedgehog topological defect work [4] states that structural disorder renders the concept of topological defects difficult to apply and hinders first-principles identification of the microscopic carriers of plasticity and of soft spots, while recently proposed well-defined topological defects in glasses can be identified and correlated with rearrangement-prone regions. Its method defines a hedgehog topological charge $Q=\frac{1}{4\pi}\int_{\Sigma}d^{2}x\ \vec{s}\cdot(\partial_{1}\vec{s}\times\partial_{2}\vec{s})$ for a unit vector field, applies the algorithm to the eigenvector and displacement fields of a simulated 3D polymer glass, and finds that the number of hedgehog defects scales at low frequency as $N_{\mathrm{HTD}}\propto\omega^{2}$, correlating with the Debye density of states $D(\omega)\propto\omega^{2}$, with a strong tendency to form oppositely charged monopole/anti-monopole pairs. This is the closest structural analogue to the present program: defects that were individually invisible become statistically and even topologically characterizable once the right observable is chosen. If TLS defects are eventually identified with such structural objects, the defect density $\rho$ used in this paper stops being a fit parameter and becomes predictable from glass structure; until then it remains an input to be measured.

Three works share the TLS acronym with the physics subject but concern the Transport Layer Security protocol, and they are cited for one structural parallel. The Helol tunnel work [1] targets the combinatorial properties of Client Hello packets in the Transport Layer Security protocol to build a covert channel for data exfiltration and command-and-control, and evaluates it by computing throughput distributions from fingerprint datasets — 3907 SNI strings from crawled traffic and 364 common application JA3 fingerprints — showing significant throughput gains over the comparable SNICat channel in median and upper quartiles, with evasion of Next-Generation Firewalls. The active TLS stack fingerprinting work [3] uses active measurements with ten empirically optimized probes to fingerprint TLS servers at scale, and reports detection of new command-and-control servers added to blocklists with precision higher than 99%, CDN detection precision ranging from 85% (Akamai and Alibaba) to more than 99% (Cloudflare and Fastly), and 351 IP addresses identified serving CDN content outside the CDN's own autonomous system. The post-quantum signature placement study [5] examines how signature-algorithm choice in TLS 1.3 couples with certificate-hierarchy structure, and its campaign results identify a single decisive variable: the operational discontinuity appears as soon as SLH-DSA is moved into the handshake-exposed server leaf certificate, while hierarchy depth by itself is not a cost verdict. The parallel worth noting is methodological: all three treat a large combinatorial space of protocol configurations statistically, asking what a random draw from that space looks like and which aggregate variable dominates the outcome. The present paper asks the same question of a defect ensemble, seeking the aggregate variable (defect density times geometry times spectral window) that dominates yield. No technical content flows between the protocol works and the physics model; the connection is the shared statistical posture toward a large configuration space, and the disambiguation itself matters because a defect-density literature search that mixes the two senses of TLS will retrieve the wrong corpus entirely.

Finally, two entries frame this paper's own context. An earlier version of this analysis [9] states the same program — modeling the defect population as a random ensemble, with the counting result $P_1 = 0.0769$ and chip-level probability $0.99966$ under the assumptions used here, and a falsification register built on non-Poisson count distributions — and the present paper is that analysis restated with its arithmetic and source discussion completed. The Alpha Pi project [10] begins from the engineering challenge that quantum states decohere rapidly due to environmental noise, argues that the fragility stems from the continuous real-number field underlying standard quantum mechanics, and catalogs the resource burdens of active error correction, including surface-code physical-to-logical ratios of order 1000:1 and a signal-processing ceiling beyond which no classical filtering can eliminate fundamental quantum back-action. Its relevance here is as a statement of why reducing decoherence at the material level matters: every reduction in the defect-driven dephasing budget relaxes the error-correction overhead that [10] identifies as unsustainable.

## 3. Methods

### 3.1 The random dynamical system formulation

A random dynamical system, in the sense of [2], consists of a state space, a dynamical flow on that state space, and a probability measure describing inaccurate knowledge of the state or of the system itself. The defect problem maps onto this structure as follows. The state space is the configuration space of the junction: a configuration is the list of transition frequencies $\omega = (\omega_1, \ldots, \omega_{N_d})$ of the $N_d$ TLS defects in the junction volume, together with their couplings $g = (g_1, \ldots, g_{N_d})$ to the qubit's electric field. Conditional on the configuration, the qubit and readout resonator dynamics are deterministic, in the three-partite structure documented in [6]. The randomness enters through the measure on configuration space: defect frequencies, positions, and couplings are not known for a given device and are modeled as draws from ensemble distributions.

Three ensemble distributions are needed as inputs:

1. The defect count $N_d$ in the junction volume, treated as a random variable with mean $\bar{N}_d$ (or, equivalently, a spatial density $\rho$).
2. The frequency distribution of defect transitions, modeled as uniform over a band of width $\Delta_0$. A uniform spectral density is the standard null model for an uncharacterized amorphous defect bath; any measured deviation from uniformity would itself be a finding about the material.
3. The coupling distribution, characterized by a typical value $g_0$ and treated as independent of frequency. This independence is an assumption; strain tuning of the kind used in [6] could test it, since strain shifts defect frequencies and any resulting change in coupling would reveal correlation.

The qubit is the deterministic observer. Its frequency $\omega_q$ is fixed by design, and all ensemble averages below are taken over the defect configuration measure with $\omega_q$ held fixed. This asymmetry is what makes the framework predictive: the fabrication process controls the ensemble parameters $(\rho, \Delta_0, g_0)$, and the observable decoherence is an ensemble average at fixed $\omega_q$.

### 3.2 Counting model

Defects are modeled as point entities distributed independently and uniformly at random with number density $\rho$ inside a barrier of area $A$ and thickness $d$, so the barrier volume is

$$V = A\,d.$$

Each defect has a transition frequency drawn uniformly from a band of width $\Delta_0$. A defect is called *strongly coupled* if two conditions hold: it lies inside the barrier volume $V$, where electric-field participation and therefore coupling are largest, and its transition frequency lies within $\pm\Gamma$ of the qubit frequency. The fractional frequency window is

$$f_\Gamma = \frac{2\Gamma}{\Delta_0}.$$

Because positions and frequencies are independent and uniform, the expected number of strongly coupled defects in one junction is

$$\lambda = \rho\,V\,f_\Gamma = \rho\,A\,d\,\frac{2\Gamma}{\Delta_0},$$

and the count $N$ is Poisson distributed with mean $\lambda$:

$$\Pr(N = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad \Pr(N \geq 1) = 1 - e^{-\lambda}.$$

The Poisson assignment is the structural analogue of the approximately Poisson overlap counts proved for random matchings against fixed regular subgraphs [7]; here independence of defect placement makes the argument elementary. An equivalent purely spectral parameterization uses a total defect number $\bar{N}_d$ spread over a band $B$: the expected count in a two-sided frequency window of width $2\delta$ is $\lambda = \bar{N}_d \cdot 2\delta / B$, with the same Poisson law. For a chip of $N_j$ junctions with independent defect populations, the total count is Poisson with mean $N_j\lambda$, and

$$P_{\mathrm{chip}} = 1 - e^{-N_j\lambda}.$$

### 3.3 Dephasing models

Two dephasing mechanisms are treated, corresponding to two regimes.

*Dispersive dephasing (off-resonant defects).* For a defect detuned by $\Delta_i$ from the qubit with coupling $g_i$ and intrinsic defect relaxation rate $\gamma_i$, the qubit acquires a small admixture of the lossy defect; to leading order in $g_i/\Delta_i$ the defect contributes a dephasing rate

$$\Gamma_\varphi^{(\mathrm{disp})} = \sum_{i=1}^{n} \left(\frac{g_i}{\Delta_i}\right)^2 \gamma_i.$$

Rates from distinct defects add. This form is valid when $g_i \ll |\Delta_i|$ for all counted defects; near-resonant defects are handled separately by the counting model.

*Telegraph-noise dephasing (switching defect).* A TLS that switches stochastically between its two states shifts the qubit frequency by a state-dependent amount. In the classical-noise approximation, the qubit frequency is perturbed by a random telegraph process $\xi(t)$ taking values $\pm\varepsilon/2$ with switching rate $\gamma$ per direction, so the autocorrelation function is

$$C(\tau) = \langle \xi(t)\,\xi(t+\tau)\rangle = \frac{\varepsilon^2}{4}\,e^{-2\gamma|\tau|}.$$

For a qubit at the noise's zero-frequency crossing, the pure-dephasing rate in the long-time limit is the time integral of the correlation function:

$$\Gamma_\varphi^{(\mathrm{tn})} = \int_0^\infty C(\tau)\,d\tau = \frac{\varepsilon^2}{4}\cdot\frac{1}{2\gamma} = \frac{\varepsilon^2}{8\gamma},$$

with dephasing time $T_\varphi = 1/\Gamma_\varphi$. This is the standard filter-function result at zero detuning for classical two-state noise; it is exact within the classical-noise and weak-coupling approximations stated here.

All frequencies in the derivations are ordinary frequencies (cycles per second), not angular frequencies; a device using angular frequencies must insert the corresponding factors of $2\pi$ consistently.

### 3.4 Parameter values

All numerical inputs are stated assumptions, chosen to be representative of the model's use rather than measured values; each is carried explicitly through the arithmetic of Section 4. The assumed barrier area is of the same order as the 200 nm × 220 nm Manhattan-style junction areas reported in [6], which correspond to $4.4\times 10^{-14}\ \mathrm{m^{2}}$.

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
| Total defects (spectral model) | $\bar{N}_d$ | $100$ |
| Spectral band (spectral model) | $B$ | $19\ \mathrm{GHz}$ |
| Qubit frequency | $\omega_q$ | $5\ \mathrm{GHz}$ |
| Resonance window (spectral model) | $\delta$ | $10\ \mathrm{MHz}$ |
| Typical coupling (dispersive) | $g_0$ | $1\ \mathrm{MHz}$ |
| Defect relaxation rate (dispersive) | $\gamma_0$ | $10\ \mathrm{kHz}$ |
| Sub-band defect count (dispersive) | $n$ | $5$ |

## 4. Analysis

### 4.1 Barrier volume

Inputs: $A = 2\times 10^{-14}\ \mathrm{m^{2}}$ and $d = 2\times 10^{-9}\ \mathrm{m}$ (Section 3.4 assumptions; the area corresponds to a junction of order $0.1\ \mu\mathrm{m}\times 0.2\ \mu\mathrm{m}$, consistent with the 200 nm × 220 nm junctions of [6]).

$$V = A\,d = \left(2\times 10^{-14}\right)\times\left(2\times 10^{-9}\right)\ \mathrm{m^{3}} = 4\times 10^{-23}\ \mathrm{m^{3}}.$$

### 4.2 Fractional coupling window

Inputs: $\Gamma = 10^{6}\ \mathrm{s^{-1}}$, $\Delta_0 = 10^{9}\ \mathrm{s^{-1}}$ (Section 3.4).

$$f_\Gamma = \frac{2\Gamma}{\Delta_0} = \frac{2\times 10^{6}}{10^{9}} = 2\times 10^{-3}.$$

### 4.3 Single-junction defect probability (spatio-spectral model)

Inputs: $\rho = 10^{24}\ \mathrm{m^{-3}}$, $V = 4\times 10^{-23}\ \mathrm{m^{3}}$ (Section 4.1), $f_\Gamma = 2\times 10^{-3}$ (Section 4.2).

Step 1 — mean count:

$$\lambda = \rho\,V\,f_\Gamma = 10^{24}\times 4\times 10^{-23}\times 2\times 10^{-3}.$$

Step 2 — arithmetic: $10^{24}\times 4\times 10^{-23} = 40$; then $40\times 2\times 10^{-3} = 0.08$.

$$\lambda = 0.08.$$

Step 3 — probability of at least one strongly coupled defect:

$$P_1 = 1 - e^{-\lambda} = 1 - e^{-0.08}.$$

Step 4 — arithmetic: expanding, $e^{-0.08} = 1 - 0.08 + 0.0032 - 0.00008533 + 0.00000171 = 0.92311638$, so

$$P_1 = 1 - 0.92311638 = 0.07688362 \approx 0.0769.$$

Under these assumptions, roughly one junction in thirteen hosts a strongly coupled TLS.

### 4.4 Chip-level extension

Inputs: $N_j = 100$ (Section 3.4), $\lambda = 0.08$ (Section 4.3).

Step 1 — chip mean count: $\lambda_{\mathrm{chip}} = N_j\,\lambda = 100\times 0.08 = 8$.

Step 2 — probability at least one junction is affected: $P_{\mathrm{chip}} = 1 - e^{-8}$.

Step 3 — arithmetic: $e^{-8} = e^{-4}\times e^{-4} \approx 0.01831564\times 0.01831564 \approx 0.00033546$, so

$$P_{\mathrm{chip}} = 1 - 0.00033546 = 0.99966454 \approx 0.99966.$$

Step 4 — standard deviation of the chip count: for a Poisson variable the standard deviation is the square root of the mean, $\sigma_{\mathrm{chip}} = \sqrt{8} \approx 2.8284$.

A 100-junction chip under these assumptions is essentially certain to contain strongly coupled defects, with chip-to-chip count fluctuation of order $\pm 3$.

### 4.5 Spectral counting model and near-resonance probability

Inputs: $\bar{N}_d = 100$ defects uniformly distributed over $B = 19\ \mathrm{GHz}$; two-sided resonance window $2\delta = 20\ \mathrm{MHz} = 0.02\ \mathrm{GHz}$ (Section 3.4).

Step 1 — expected near-resonant count:

$$\lambda = \frac{\bar{N}_d\cdot 2\delta}{B} = \frac{100\times 0.02\ \mathrm{GHz}}{19\ \mathrm{GHz}} = \frac{2}{19} = 0.10526316.$$

Step 2 — Poisson approximation: $P_{\geq 1} = 1 - e^{-0.10526316}$. Arithmetic: $e^{-0.10526316} = 1 - 0.10526316 + 0.00554018 - 0.00019435 + 0.00000512 = 0.90008779$, so

$$P_{\geq 1} = 1 - 0.90008779 = 0.09991221 \approx 0.0999.$$

Step 3 — exact binomial check: $P_{\geq 1} = 1 - (1 - 0.02/19)^{100}$. Arithmetic: $1 - 0.02/19 = 0.99894737$; $\ln(0.99894737) = -0.00105319$; $100\times(-0.00105319) = -0.105319$; $e^{-0.105319} = 0.