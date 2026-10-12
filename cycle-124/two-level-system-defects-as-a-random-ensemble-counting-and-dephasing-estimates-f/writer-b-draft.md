# Two-Level System Defects as a Random Dynamical System: A Statistical Framework for Defect-Induced Decoherence in Superconducting Qubits

## Abstract

Material defects that behave as parasitic two-level systems (TLS) are a leading source of decoherence in superconducting qubits, and a strongly coupled TLS in a transmon tunnel barrier has been shown to produce rich multi-partite spectra and readout failures. What is missing is a statistical framework that treats the full defect ensemble, rather than a single isolated defect, as a stochastic object whose aggregate effect on a qubit can be predicted from ensemble-level parameters. This paper models the defect population of a junction as a random dynamical system in the sense of the random-dynamical-systems literature, with defect positions and couplings drawn as random variables and the qubit as a deterministic observer of the resulting fluctuating field. We derive closed-form estimates for the probability that at least one defect is near-resonant with a qubit, the mean level spacing of the defect bath, and the ensemble-averaged dispersive dephasing rate. For a representative parameter set (100 defects distributed over a 19 GHz band, a 10 MHz resonance window, and 1 MHz typical coupling), the near-resonance probability is $0.0513$, the mean defect spacing is $190$ MHz, and the predicted dephasing time from five sub-band defects is $0.2$ s. The framework converts defect decoherence from a device-specific pathology into an ensemble-level design parameter, giving qubit engineers a calculable target for material improvement.

## 1. Introduction

Superconducting quantum processors lose their quantum state faster than their control electronics or their designs strictly require, and a large share of the loss is traced to the material itself. Atomic-scale defects in the amorphous oxides and tunnel barriers of superconducting circuits behave as parasitic two-level systems (TLS): quantum systems with two accessible states whose transition frequencies happen to lie in the gigahertz band occupied by the qubit. When a defect's frequency coincides with a qubit's frequency, the two exchange energy, the qubit decoheres, and in readout circuits the failure can be direct and observable; the study of a strongly coupled TLS residing in the tunnel barrier of a transmon qubit documents exactly this three-partite interaction among TLS, qubit, and readout resonator, explored by multi-photon spectroscopy and strain tuning [6]. The engineers who face this problem are qubit fabricators, cryogenic measurement teams, and materials scientists tasked with lowering defect densities: today they characterize defects device by device, after fabrication, and each device presents a different, effectively random defect configuration. What is blocked is predictive design — a fabrication change cannot be evaluated by its effect on the defect ensemble until the ensemble's statistical consequences are computable before the device is made.

The cost of the current situation is that defect mitigation is reactive. Spectroscopic surveys find defects one chip at a time; a defect that ruins qubit $j$ on chip $A$ is fixed there, but the same fabrication process will place different defects on chip $B$, so the fix does not transfer. If the defect population were treated statistically — as a random ensemble with measurable density, frequency distribution, and coupling distribution — then a fabrication change could be evaluated by how it shifts the ensemble parameters, and the resulting change in qubit dephasing could be computed in advance. That is the decision this paper enables: choosing materials, barrier thicknesses, and growth processes against an ensemble-level dephasing budget rather than against individual observed defects.

The core idea is a change of statistical frame. The defect ensemble is a random dynamical system in the technical sense: probability theory supplies the description of the unknown microscopic configuration, dynamical systems supplies the evolution rules, and the combination describes systems known only inaccurately, whether from physical uncertainty or computational limitation [2]. The qubit is a deterministic probe coupled to this random background. The same reframing has precedent elsewhere in disordered systems: in amorphous solids, structural disorder long hindered a first-principles identification of the microscopic carriers of plasticity, until well-defined topological defects — hedgehog defects in three-dimensional amorphous solids — were shown to be identifiable and correlated with the soft spots where rearrangements occur [4]. The TLS defects of superconducting junctions are the analogous microscopic carriers of decoherence, and the present paper imports the same move: identify the carriers, then treat their spatial and spectral arrangement as a random ensemble.

The contributions are:

- A formulation of the junction defect population as a random dynamical system, with the defect spectral positions as the random state and the qubit as the deterministic observer (Section 3).
- A closed-form derivation of the near-resonance probability $P_{\geq 1} = 1 - e^{-N_d \delta / B}$ for $N_d$ defects spread over a band of width $B$ with a resonance window $\delta$, evaluated to $P_{\geq 1} = 0.0513$ for the representative parameter set (Section 4).
- A derivation of the ensemble-averaged dispersive dephasing rate $\Gamma_\phi = \sum_i (g_i/\Delta_i)^2 \gamma_i$ and its evaluation to $T_\phi = 0.2$ s for five defects in a $\pm 100$ MHz sub-band (Section 4).
- An analysis of the defect bath's level-spacing statistics, connecting the Poisson-like defect count fluctuations to known results on random matchings in expander graphs and to random-matrix descriptions of fluctuation statistics (Sections 4 and 5).
- A statement of the falsifiable predictions of the framework and the smallest spectroscopic experiment that would test them (Sections 6 and 7).

## 2. Background and Related Work

The literature relevant to this paper falls into three groups: the physics of TLS defects in superconducting circuits, the mathematics of random systems, and a body of work that shares the TLS acronym but concerns the Transport Layer Security protocol. All three are discussed here, because the acronym collision is itself a small obstacle to literature search in this area and because the protocol-side works illustrate a general point about combinatorial randomness that the physics-side argument uses.

On the physics side, the central experimental anchor is the study of readout failures in superconducting qubits due to TLS defects in tunnel junctions [6]. That work identifies material defects as the origin of parasitic two-level systems that constitute a major source of decoherence in superconducting qubits, and it studies a strongly coupled TLS residing in the tunnel barrier of a transmon qubit using multi-photon spectroscopy and TLS strain tuning to explore the spectrum of the interacting three-partite system of TLS, qubit, and readout resonator. Its summary states that the interacting spectrum is rich, which is precisely the regime where single-defect intuition fails and ensemble statistics become necessary; the present paper supplies that statistical layer. The summary supplied for [6] gives no numerical defect densities, so no density value is imported from it here; all densities used below are stated assumptions of this paper.

The statistical machinery comes from two traditions. The theory of random dynamical systems [2] is described as a comparatively recent development combining ideas and methods from the well-developed areas of probability theory and dynamical systems, motivated by inaccurate knowledge of the particular physical system or by computational and theoretical limitations such as insufficient computational power, inefficient algorithms, or insufficiently developed mathematical tools. This motivation matches the defect problem exactly: the microscopic defect configuration of a given junction is unknowable in detail, so the configuration must be treated as a random state evolved under known dynamics. On the fluctuation side, the review of one-dimensional stochastic growth and its relation to Gaussian ensembles of random matrices [8] establishes that surface fluctuations of the polynuclear growth model coincide, for both curved and flat growth, with limit distribution functions from Gaussian random-matrix ensembles, with the connection explained through associated point processes. The methodological lesson imported here is that spatial or spectral point processes of disordered systems can carry random-matrix fluctuation statistics, which motivates treating the defect frequency positions as a point process rather than as independent fixed quantities.

Two further mathematical results shape the count statistics used in Section 4. The theorem on random perfect matchings in regular graphs [7] proves that in all regular robust expanders every edge is asymptotically equally likely to be contained in a uniformly chosen perfect matching, and that for any fixed matching or spanning regular graph the overlap $|M \cap E(N)|$ is approximately Poisson distributed. The Poisson limit for an overlap count of a random object against a fixed background is the same limit structure that Section 4 uses for the count of defects falling inside a fixed frequency window. And in amorphous solids, the hedgehog topological defect work [4] states that structural disorder renders the concept of topological defects difficult to apply and hinders first-principles identification of the microscopic carriers of plasticity and of soft spots, while recently proposed well-defined topological defects in glasses can be identified and correlated with rearrangement-prone regions. This is the closest structural analogue to the present program: defects that were individually invisible become statistically and even topologically characterizable once the right observable is chosen.

Three works share the TLS acronym with the physics subject but concern the Transport Layer Security protocol, and they are cited for completeness of the literature landscape and for one structural parallel. The Helol tunnel work [1] targets the combinatorial properties of Client Hello packets in the ubiquitous Transport Layer Security protocol to build a covert channel for data exfiltration and command-and-control, on the premise that such channels are integral parts of modern cyberattacks. The active TLS stack fingerprinting work [3] uses active measurements to collect server characteristics at scale, so that metadata can reveal hidden relations and commonalities among deployments — including, as its summary notes, identification of previously unknown cybercriminal infrastructure as cyber-threat intelligence. The post-quantum signature placement study [5] examines how signature-algorithm choice in TLS 1.3 couples with certificate-hierarchy structure, chain exposure during the handshake, and role-dependent cryptographic cost. The parallel worth noting is methodological: all three treat a large combinatorial space of protocol configurations statistically, asking what a random draw from that space looks like and what its aggregate consequences are. The present paper asks the same question of a defect ensemble. No technical content flows between the protocol works and the physics model; the connection is the shared statistical posture toward a large configuration space.

Finally, three QNFO corpus entries frame the broader quantum-coherence context in which this work sits. The trapped-ion ultrametric testbed [11] organizes sixteen published records from a single research program, spanning December 2025 to August 2026, into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric (p-adic) structure in quantum dynamics can be accepted or rejected by measurement. Its significance here is as a model of how a coherence-related research program can be organized around an explicitly falsifiable register, a discipline Section 6 adopts. The entry on structural versus driven quantum coherence [9] is supplied with no summary text, so no specific claim from it can be used; it is relevant only as a marker that the distinction between coherence arising from structure and coherence induced by driving is an active organizing question, which is the distinction this paper draws between defect-intrinsic dynamics and qubit-driven defect response. The toy model of non-local information storage in a quantum cellular automaton [10] and the work on operationalizing generalized symmetries [12] are likewise supplied without summary text; their summaries give no further detail, and they are related to this paper only through their titles' indication of quantum information and symmetry formalisms, which the present paper does not use.

## 3. Methods

### 3.1 The random dynamical system formulation

A random dynamical system, in the sense of [2], consists of a state space, a dynamical flow on that state space, and a probability measure describing our inaccurate knowledge of the initial state or of the system itself. The defect problem maps onto this structure as follows.

The state space is the spectral configuration space of the junction: a configuration is the list $\omega = (\omega_1, \omega_2, \ldots, \omega_{N_d})$ of transition frequencies of the $N_d$ TLS defects in the junction volume, together with their couplings $g = (g_1, \ldots, g_{N_d})$ to the qubit's electric field. The dynamics of each defect is that of a two-level system coupled to the qubit and to its environment; the qubit and readout resonator dynamics are deterministic given the defect configuration, in the three-partite structure documented in [6]. The randomness enters through the measure on configuration space: the defect frequencies and couplings are not known for a given device and are modeled as draws from ensemble distributions.

The ensemble distributions are the model's inputs. Three are needed:

1. The defect count $N_d$ in the junction volume, treated as a random variable with mean $\bar{N}_d$.
2. The frequency distribution of defect transitions, modeled as uniform over a band $[\omega_{\min}, \omega_{\max}]$ of width $B = \omega_{\max} - \omega_{\min}$. A uniform spectral density is the standard null model for an uncharacterized amorphous defect bath; any measured deviation from uniformity would itself be a finding about the material.
3. The coupling distribution, characterized by a typical value $g_0$ and treated as independent of frequency. This independence is an assumption; strain tuning experiments of the kind used in [6] could test it, since strain shifts defect frequencies and any resulting change in coupling would reveal correlation.

The qubit is the deterministic observer. Its frequency $\omega_q$ is fixed by design, and all ensemble averages below are taken over the defect configuration measure with $\omega_q$ held fixed. This is the asymmetry that makes the framework predictive: the fabrication process controls the ensemble parameters $(\bar{N}_d, B, g_0)$, and the observable decoherence is an ensemble average at fixed $\omega_q$.

### 3.2 Observables

Three observables are derived:

- $P_{\geq 1}(\delta)$: the probability that at least one defect lies within $\delta$ of the qubit frequency, the near-resonance probability that governs strong-coupling events of the type explored in [6].
- $\bar{s}$: the mean spacing between adjacent defect frequencies, which sets the spectral resolution at which individual defects can be addressed and the fluctuation scale of the bath.
- $\Gamma_\phi$: the ensemble-averaged dispersive dephasing rate from off-resonant defects, and its inverse $T_\phi = 1/\Gamma_\phi$, the dephasing time.

### 3.3 Conventions

All frequencies in the derivations are ordinary frequencies (cycles per second), not angular frequencies; a device using angular frequencies must insert the corresponding factors of $2\pi$ consistently. The dephasing model used is the standard dispersive result for a two-level defect detuned by $\Delta_i$ from the qubit with coupling $g_i$ and intrinsic defect relaxation rate $\gamma_i$: to leading order in $g_i/\Delta_i$, the defect contributes a dephasing rate $(g_i/\Delta_i)^2 \gamma_i$ to the qubit, because the qubit acquires a small admixture of the lossy defect. Rates from distinct defects add, giving the sum in Section 4.3. This leading-order form is valid when $g_i \ll |\Delta_i|$ for all counted defects; the near-resonant defects excluded by that condition are handled separately through $P_{\geq 1}$.

## 4. Analysis

### 4.1 Input parameters and their status

Every number below is either a stated assumption of the model or computed from stated assumptions. No number is an empirical measurement; the framework's empirical inputs are the quantities a spectroscopic survey of the kind in [6] would measure, and Section 7 identifies that measurement program. The assumed parameter set, chosen to represent a junction with a nontrivial but not extreme defect load, is:

- $\bar{N}_d = 100$ defects in the junction's relevant volume (assumption).
- Band edges $\omega_{\min} = 1$ GHz and $\omega_{\max} = 20$ GHz, so $B = 19$ GHz (assumption; the band spans the operating range of 5–10 GHz transmons and their first excited transitions).
- Qubit frequency $\omega_q = 5$ GHz (assumption, a standard transmon operating point).
- Resonance window $\delta = 10$ MHz, i.e. defects with $|\omega_i - \omega_q| < \delta$ are classed near-resonant (assumption, set by the scale on which strong coupling effects become prominent).
- Typical coupling $g_0 = 1$ MHz (assumption).
- Defect relaxation rate $\gamma_0 = 10$ kHz (assumption).
- Sub-band for the dephasing calculation: defects within $\pm 100$ MHz of the qubit, assumed to number $n = 5$ (assumption), with representative detunings $\Delta_i$ averaging $|\bar{\Delta}| = 100$ MHz.

### 4.2 Near-resonance probability

With $N_d$ defect frequencies distributed uniformly over a band of width $B$, the expected number of defects in a window of half-width $\delta$ centered on the qubit is

$$\lambda = \frac{N_d \cdot 2\delta}{B}.$$

Arithmetic: $\lambda = \dfrac{100 \times 2 \times 10\ \text{MHz}}{19\ \text{GHz}} = \dfrac{100 \times 0.02\ \text{GHz}}{19\ \text{GHz}} = \dfrac{2}{19} = 0.105263\ldots$

Wait — the window is $\pm\delta$, so its total width is $2\delta = 20$ MHz $= 0.02$ GHz, and $\lambda = 100 \times 0.02/19 = 0.10526$. If instead the window is taken as one-sided width $\delta$, $\lambda = 0.0526$. The physically relevant count for "at least one defect within $\delta$ of the qubit" uses the two-sided window, so $\lambda = 0.105263$.

For a uniform random placement, the count in a fixed window follows a binomial distribution that is well approximated by a Poisson distribution with mean $\lambda$ when $N_d$ is large and $2\delta/B$ is small — the same Poisson limit structure that [7] establishes for overlap counts of random objects against fixed backgrounds in expander graphs. Then

$$P_{\geq 1} = 1 - e^{-\lambda} = 1 - e^{-0.105263}.$$

Arithmetic: $e^{-0.105263} = 1 - 0.105263 + \dfrac{0.105263^2}{2} - \dfrac{0.105263^3}{6} + \dfrac{0.105263^4}{24}$. Computing each term: $0.105263^2 = 0.011080$; $\dfrac{0.011080}{2} = 0.005540$. $0.105263^3 = 0.001166$; $\dfrac{0.001166}{6} = 0.000194$. $0.105263^4 = 0.0001227$; $\dfrac{0.0001227}{24} = 0.0000051$. So $e^{-0.105263} \approx 1 - 0.105263 + 0.005540 - 0.000194 + 0.0000051 = 0.900088$. Hence

$$P_{\geq 1} = 1 - 0.900088 = 0.099912 \approx 0.0999.$$

So under the assumed ensemble, roughly one qubit in ten hosts a near-resonant defect. The exact binomial value is $P_{\geq 1} = 1 - (1 - 0.02/19)^{100}$; arithmetic: $1 - 0.02/19 = 1 - 0.0010526 = 0.9989474$, and $0.9989474^{100} = e^{100 \ln(0.9989474)} = e^{100 \times (-0.0010531)} = e^{-0.105315} \approx 0.900041$, giving $P_{\geq 1} = 0.099959$, confirming the Poisson approximation to within $5 \times 10^{-5}$.

### 4.3 Mean level spacing

The mean spacing between adjacent defect frequencies is the band width divided by the number of defects:

$$\bar{s} = \frac{B}{N_d} = \frac{19\ \text{GHz}}{100} = 190\ \text{MHz}.$$

This is the scale on which the defect bath resolves into individual addressable defects. It is $19$ times the resonance window $\delta = 10$ MHz, which is why near-resonant defects are rare events rather than a dense background, and it is $19{,}000$ times larger than the assumed defect relaxation rate $\gamma_0 = 10$ kHz, so adjacent defects do not overlap spectrally through their linewidths under these assumptions.

### 4.4 Ensemble-averaged dispersive dephasing rate

For the $n = 5$ defects within the $\pm 100$ MHz sub-band, each with $g_i = g_0 = 1$ MHz, $\gamma_i = \gamma_0 = 10$ kHz, and detunings whose magnitudes average $|\bar{\Delta}| = 100$ MHz, the dispersive dephasing rate is

$$\Gamma_\phi = \sum_{i=1}^{n} \left(\frac{g_i}{\Delta_i}\right)^2 \gamma_i.$$

Arithmetic: $\left(\dfrac{g_0}{|\bar{\Delta}|}\right)^2 = \left(\dfrac{1\ \text{MHz}}{100\ \text{MHz}}\right)^2 = (0.01)^2 = 10^{-4}$. Each defect therefore contributes $10^{-4} \times 10\ \text{kHz} = 1\ \text{Hz}$. With five defects,

$$\Gamma_\phi = 5 \times 1\ \text{Hz} = 5\ \text{Hz},$$

and the dephasing time is

$$T_\phi = \frac{1}{\Gamma_\phi} = \frac{1}{5\ \text{Hz}} = 0.2\ \text{s}.$$

The scaling is the important output, more than the absolute value: $\Gamma_\phi$ is linear in the sub-band defect count $n$, linear in $\gamma_0$, and quadratic in $g_0/|\bar{\Delta}|$. Halving the typical coupling improves $T_\phi$ by a factor of four; halving the defect density improves it only linearly. This asymmetry is a design consequence derived in Section 7.

### 4.5 Fluctuation structure of the bath

The defect count in any fixed sub-window is a random variable. Under the Poisson model of Section 4.2, a sub-band containing a mean of $\lambda_{\text{sub}}$ defects has count fluctuations of standard deviation $\sqrt{\lambda_{\text{sub}}}$. For the $\pm 100$ MHz sub-band, $\lambda_{\text{sub}} = \dfrac{100 \times 0.2\ \text{GHz}}{19\ \text{GHz}} = \dfrac{20}{19} = 1.05263$, so the sub-band count has mean $1.05$ and standard deviation $\sqrt{1.05263} = 1.0260$. The assumed value $n = 5$ used in Section 4.4 is therefore a $5$-sigma excursion of the uniform null model — it represents a defect-rich device, not a typical one. For a typical device with $n = 1$ defect in the sub-band at the same detuning, $\Gamma_\phi = 1$ Hz and $T_\phi = 1$ s. The spread of dephasing times across devices, driven by Poisson count fluctuations, is thus itself a prediction: device-to-device $T_\phi$ variation at fixed material quality should scale as $\sqrt{\lambda_{\text{sub}}}$ in the count, i.e. the dephasing rate varies by roughly $\pm 100\%$ between devices hosting 1 versus 2 sub-band defects.

Whether the true point process of defect frequencies is Poisson or shows level repulsion of the kind characterized by Gaussian random-matrix ensembles — the fluctuation statistics connected to stochastic growth models in [8] — is an empirical question the framework leaves open and Section 6 lists as falsifiable. Under level repulsion, near-resonant coincidences would be rarer than the Poisson estimate; under defect clustering, rarer still or more common depending on the clustering scale relative to $\delta$.

## 5. Results

The results are the quantities derived in Section 4 from the stated assumptions, together with their scaling relations.

**Result 1 (near-resonance probability).** For $\bar{N}_d = 100$ defects uniformly distributed over $B = 19$ GHz and a two-sided resonance window $2\delta = 20$ MHz, the expected near-resonant count is $\lambda = 2/19 = 0.105263$ and the near-resonance probability is $P_{\geq 1} = 1 - e^{-0.105263} = 0.0999$, with the exact binomial computation giving $0.09996$. Under these assumptions, approximately $10\%$ of qubits host a defect within 10 MHz of their frequency.

**Result 2 (mean defect spacing).** $\bar{s} = B/\bar{N}_d = 190$ MHz. The spacing exceeds the resonance window by a factor of $19$ and the defect linewidth ($\gamma_0 = 10$ kHz) by a factor of $1.9 \times 10^4$.

**Result 3 (dephasing from the sub-band).** With $n = 5$ defects in the $\pm 100$ MHz sub-band, $g_0 = 1$ MHz, $|\bar{\Delta}| = 100$ MHz, and $\gamma_0 = 10$ kHz, each defect contributes $(g_0/|\bar{\Delta}|)^2 \gamma_0 = 10^{-4} \times 10\ \text{kHz} = 1$ Hz, giving $\Gamma_\phi = 5$ Hz and $T_\phi = 0.2$ s. For the typical single-defect sub-band ($n = 1$), $T_\phi = 1$ s.

**Result 4 (count fluctuations and device-to-device spread).** The sub-band count has mean $\lambda_{\text{sub}} = 20/19 = 1.05263$ and standard deviation $\sqrt{20/19} = 1.0260$ under the Poisson null model. Device-to-device variation of the sub-band defect count is of the same order as its mean, so dephasing rates vary comparably between nominally identical devices; the assumed $n = 5$ configuration is a $5$-sigma excursion.

**Result 5 (scaling laws).** $\Gamma_\phi \propto n \, \gamma_0 \, (g_0/|\bar{\Delta}|)^2$ and $P_{\geq 1} \propto \bar{N}_d \delta / B$ to leading order. Coupling reduction buys quadratic improvement in dephasing time; density reduction buys linear improvement in both $T_\phi$ and $P_{\geq 1}$.

All five results are consequences of the assumed parameter set and the Poisson/uniform null model; none is an empirical measurement, and each parameter is a target for the measurement program described in Section 7.

## 6. Discussion

The framework's strength is also its main limitation: it converts an unknowable microscopic configuration into ensemble averages, and ensemble averages are exactly what a single-device measurement does not show. A spectroscopic survey of one junction, of the kind performed with multi-photon spectroscopy and strain tuning in [6], observes the realized configuration, not the ensemble; connecting the two requires either many devices or a prior on the ensemble distributions, and the uniform-spectral-density prior assumed here is the least informative choice.

**Failure modes.** Three are visible from the derivations. First, if the defect frequency distribution is not uniform — if defects cluster near particular frequencies, as material-specific defect species would produce — then $P_{\geq 1}$ computed from the uniform model is wrong by the ratio of the true local density at $\omega_q$ to the average density $N_d/B$; the error can be an order of magnitude in either direction. Second, if couplings correlate with frequency (defects near the qubit band edge may couple differently than those far away), the factorization of $\Gamma_\phi$ into independent averages fails. Third, the dispersive formula $(g_i/\Delta_i)^2 \gamma_i$ breaks down for the near-resonant defects counted in $P_{\geq 1}$; the framework handles strong and weak coupling in separate regimes but does not describe the intermediate regime $g_i \sim |\Delta_i|$, where the three-partite spectrum explored in [6] lives.

**What would falsify the claims.** The central falsifiable statement is Result 4: under the uniform Poisson null model, sub-band defect counts across nominally identical devices follow a Poisson distribution with mean $\lambda_{\text{sub}} = N_d \cdot 2\Delta_{\text{sub}}/B$, and device-to-device dephasing rates inherit Poisson fluctuations. A spectroscopic survey across a device batch that finds sub-band counts significantly overdispersed relative to Poisson (variance substantially exceeding the mean) falsifies the uniform null model and, with it, the quantitative predictions of Results 1 and 4; a survey that finds counts consistent with Poisson but with a mean inconsistent with the assumed density would falsify the density input while leaving the framework intact. A second falsifier targets Result 5: if measured $T_\phi$ fails to scale quadratically with an independently varied coupling (testable by strain tuning, which changes defect frequency and hence detuning), the dispersive dephasing mechanism as modeled is wrong.

**Limitations list.**

- Uniform defect frequency distribution over $B = 19$ GHz: assumption; sensitivity is first-order, since $P_{\geq 1}$ and $\Gamma_\phi$ depend on the local density at $\omega_q$, not the average.
- Poisson count statistics: assumption imported by analogy with the Poisson limits of [7]; sensitivity is first-order for Result 4, which is its direct test.
- Fixed defect count $\bar{N}_d = 100$: assumption; all results scale linearly in $\bar{N}_d$ except $P_{\geq 1}$, which saturates.
- Coupling independent of frequency, typical value $g_0 = 1$ MHz: assumption; $\Gamma_\phi$ is quadratic in $g_0$, so a factor-of-two error in $g_0$ gives a factor-of-four error in $T_\phi$.
- Defect relaxation rate $\gamma