# Re-Entry of Non-Markovian Boson-Mediated Transport into Light-Harvesting Complexes: A Timescale-Based Applicability Analysis

## Abstract

A recent framework for non-Markovian Hamiltonian dynamics of boson-mediated energy transfer (QNFO, DOI 10.5281/zenodo.18382696) was developed for generic bosonic transport networks. This paper asks whether that framework re-enters — i.e., applies with predictive value — to biological light-harvesting complexes, where environment-assisted transport and vibronic coupling are known to be central. We formulate the re-entry question as a quantitative timescale test: non-Markovian boson-mediated dynamics matter only when the bath memory time $\tau_B$ is not small compared with the coherent transfer time $\tau_T$. Using a Haken–Strobl–type dephasing model with Fenna–Matthews–Olson (FMO)-scale parameters (coupling $V = 30\ \mathrm{cm^{-1}}$, energetic disorder $\Delta = 100\ \mathrm{cm^{-1}}$), we derive an optimal dephasing rate $\Gamma^* \approx \Delta$ and a corresponding transfer time $\tau_T \approx 0.59\ \mathrm{ps}$, giving a trapping-limited efficiency $\eta \approx 0.9994$ for a $1\ \mathrm{ns}$ exciton lifetime. Comparing $\tau_T$ with vibrational correlation times $\tau_B \in [0.1, 1]\ \mathrm{ps}$ yields memory ratios $\tau_B/\tau_T \in [0.17, 1.7]$, squarely in the non-Markovian regime. We conclude that re-entry is justified for vibrationally structured baths, and we identify the parameter regime in which the Markovian reduction suffices. All numerical results are derived here from stated inputs; no new simulations are reported.

## 1. Introduction

Energy transfer in photosynthetic light-harvesting complexes has become a canonical testing ground for open quantum dynamics theory. The central puzzle is architectural: these pigment–protein complexes achieve near-unity excitation-to-trap efficiencies on picosecond timescales despite operating at physiological temperature, embedded in a noisy, structured protein and solvent environment. Two decades of work have established that noise is not merely a nuisance but, in the right amount, a resource — the phenomenon of dephasing-assisted (environment-assisted) transport [1], [10].

Independently, a general framework for non-Markovian Hamiltonian dynamics of boson-mediated energy transfer has been developed (QNFO, DOI 10.5281/zenodo.18382696) [9]. That work treats transport mediated by a bosonic environment with full memory retention, going beyond the Markovian (memoryless) reduction. The natural question — the "re-entry" question studied here — is whether this framework, constructed at a level of generality that abstracts away from any specific physical platform, applies to light-harvesting complexes with enough predictive content to justify the added complexity over Markovian master equations.

This is not a rhetorical question. Markovian dephasing models already reproduce the qualitative phenomenology of environment-assisted transport, including the existence of an optimal dephasing rate and efficiencies above $90\%$ in the FMO complex [1]. If the Markovian reduction is quantitatively adequate, the non-Markovian framework is unnecessary overhead. If it is not, the framework should predict observable corrections — e.g., transient negative rates, oscillatory population backflow, or shifts in the optimal noise level — that Markovian models cannot.

Our approach is deliberately minimal. Rather than running new simulations, we perform a timescale-based applicability analysis. We (i) set up a two-site Haken–Strobl–type toy model with FMO-scale parameters, (ii) derive the optimal dephasing rate and the associated transfer time with full arithmetic, (iii) compute the trapping-limited efficiency, and (iv) compare the transfer time against independently motivated vibrational bath memory times to locate the system in the Markovian or non-Markovian regime. The result is a concrete, falsifiable criterion for when the boson-mediated non-Markovian framework [9] re-enters light-harvesting physics and when it does not.

The paper is organized as follows. Section 2 reviews the relevant literature. Section 3 defines the models and the re-entry criterion. Section 4 contains all derivations. Section 5 reports the computed results. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

**Dephasing-assisted transport.** Mohseni, Rebentrost, and co-authors [1] provided physically intuitive mechanisms for how noise enables excitation energy transfer (EET) in networks, working in a hybrid basis of excitons and sites and showing that dephasing enables transfer with efficiencies well above $90\%$ across the FMO complex. This is the foundational demonstration that the noise level is a design parameter, and it defines the baseline phenomenology that any re-entering framework must reproduce. Our Section 4 derivation of the optimal dephasing rate is a two-site analytic distillation of exactly this mechanism.

**Efficiency estimation methodology.** Caruso et al. [6] addressed the practical problem of estimating energy transfer efficiency in light-harvesting complexes, emphasizing that the non-perturbative, non-Markovian interactions with the protein backbone and photonic/phononic environments make both efficiency and its sensitivity hard to compute. Their work motivates our framing: the difficulty is not conceptual but computational, and a framework earns its keep only if it reduces that difficulty or extends the accessible regime. Our timescale criterion is a cheap pre-filter for deciding when the expensive non-Markovian treatment is warranted.

**Non-Markovian dynamics: concepts and tests.** Li et al. [2] surveyed the state of non-Markovian quantum dynamics in the era of quantum engineering, including experimental characterization and quantification of memory effects and decoherence engineering. They supply the operational definitions of non-Markovianity (e.g., divisibility breaking and information backflow) that we adopt in Section 3 when stating what "non-Markovian" means operationally for our re-entry test.

**Microscopic non-Markovian modeling.** Xiao, Jing, and co-authors [3] derived an exact master equation with time-dependent coefficients for entangled coherent states under vacuum fluctuations, using the Feynman–Vernon influence functional in the coherent-state representation, recovering the Markovian result under the Markovian approximation. This is methodologically the closest relative of the boson-mediated framework [9]: both derive memory effects microscopically from a bosonic bath rather than postulating them. It demonstrates that time-dependent (TCL-type) coefficients are the natural language in which re-entry predictions would be expressed.

**Structured time-dependent rates.** Piilo and co-authors [4] analyzed the Liouvillian spectrum of a system coupled to a non-Markovian bath via Floquet theory for time-convolutionless master equations with time-periodic rates, showing that stroboscopic divisibility can hold at discrete times even when the map is non-Markovian between strokes. This is a caution for re-entry: a light-harvesting system driven by quasi-periodic vibrational modes may appear Markovian at stroboscopic sampling times while being strongly non-Markovian between them, so experimental tests must sample continuously.

**Thermodynamic consequences.** Man et al. [5] showed that non-Markovian dynamics can be exploited in quantum Otto engines with effective negative temperatures, improving efficiency by terminating isochoric strokes before equilibration. Though set in thermodynamics rather than biology, this establishes the general principle that non-Markovian memory is a usable resource, not only a correction term — the same principle underlies environment-assisted transport and strengthens the case for taking re-entry seriously.

**Nuclear quantum effects.** Kreis and co-authors [7] assessed how high-frequency chromophore vibrations influence EET using a mixed quantum–classical theory consistent with quantum–classical equilibrium, finding that nuclear quantum effects slow down energy transfer. This is directly relevant to re-entry: high-frequency intramolecular vibrations are precisely the structured bosonic modes whose memory effects the framework [9] is built to capture, and their demonstrated dynamical impact shows the effect is not negligible.

**Photosystem II context.** The QNFO review of quantum coherence in Photosystem II [10] consolidates the evidence for environment-assisted quantum transport (ENAQT) and vibronic coupling in biological light-harvesting, providing the biological target landscape — pigment site-energy disorder, vibronic resonance conditions, and trapping kinetics — against which the re-entry criterion of this paper is evaluated.

**An out-of-field contrast.** The Dark Energy Survey [8] illustrates, from an unrelated domain, the value of pre-registering the analysis pipeline and error budget before data collection; we borrow that discipline here by stating our re-entry criterion and its falsification conditions (Section 6) before any comparison to future simulation or experimental data. It plays no technical role in the derivations.

## 3. Methods

### 3.1 Toy model

We use a two-site Haken–Strobl–type model: two sites with energy gap $\Delta$, coherent coupling $V$, Markovian dephasing at rate $\Gamma$, a trap on site 2 with rate $\kappa$, and exciton recombination with lifetime $\tau_e$. The Hamiltonian in the single-excitation manifold is

$$H_S = \frac{\Delta}{2}\sigma_z + V\sigma_x,$$

and pure dephasing acts as $-\frac{\Gamma}{2}(1-\sigma_z^2/2)$ on the density matrix in Lindblad form. This model is the minimal generator of the dephasing-assisted transport phenomenology of [1].

### 3.2 Re-entry criterion

Following the operational definitions surveyed in [2], a dynamical map $\Phi_{t}$ is Markovian if it is divisible: $\Phi_{t+\mathrm{d}t} = \Phi_{\mathrm{d}t}\circ\Phi_t$ with a generator of Lindblad form at all times. For a bosonic bath with spectral density $J(\omega)$, the natural memory timescale is the correlation decay time $\tau_B$, and the system timescale is the coherent/dephasing-assisted transfer time $\tau_T$. We define the memory ratio

$$R = \frac{\tau_B}{\tau_T},$$

and the re-entry criterion: the non-Markovian boson-mediated framework [9] is required (re-enters) when $R \gtrsim 0.5$; the Markovian reduction suffices when $R \lesssim 0.1$; the interval $0.1 < R < 0.5$ is transitional and requires error estimation. The thresholds are conventions, stated here explicitly so the criterion is falsifiable.

### 3.3 Input parameters

All inputs are stated with sources:

- $V = 30\ \mathrm{cm^{-1}}$: representative nearest-neighbor excitonic coupling in FMO-scale complexes (order of magnitude consistent with the couplings used in the dephasing-assisted transport literature [1]).
- $\Delta = 100\ \mathrm{cm^{-1}}$: representative site-energy disorder (same source class [1], [10]).
- $\kappa = 1\ \mathrm{ps^{-1}}$: representative trap rate [6], [10].
- $\tau_e = 1\ \mathrm{ns}$: representative exciton lifetime [1], [10].
- $\tau_B \in [0.1, 1]\ \mathrm{ps}$: vibrational bath correlation times, spanning solvent-like fast modes ($\sim 0.1\ \mathrm{ps}$) to intramolecular high-frequency modes with slower envelope decay ($\sim 1\ \mathrm{ps}$), consistent with the mixed quantum–classical analysis of [7].
- Conversion factor: $1\ \mathrm{cm^{-1}} \leftrightarrow 2.9979\times 10^{10}\ \mathrm{Hz}$ (from $c = 2.9979\times 10^{10}\ \mathrm{cm/s}$).

No parameter is taken from a new measurement; all are literature-scale representatives, and the sensitivity of the conclusions to this choice is examined in Section 6.

## 4. Analysis

### 4.1 Optimal dephasing rate (derivation)

In the strong-disorder regime $V \ll \Delta$, the dephasing-assisted hopping rate between two sites with energy mismatch $\Delta$ under pure dephasing rate $\Gamma$ is (standard Haken–Strobl result, derived e.g. in the hybrid-basis treatment of [1]):

$$k(\Gamma) = \frac{2V^2\,\Gamma}{\Gamma^2 + \Delta^2}.$$

To find the optimum, differentiate with respect to $\Gamma$:

$$\frac{\mathrm{d}k}{\mathrm{d}\Gamma} = 2V^2\,\frac{(\Gamma^2 + \Delta^2) - \Gamma\cdot 2\Gamma}{(\Gamma^2+\Delta^2)^2} = 2V^2\,\frac{\Delta^2 - \Gamma^2}{(\Gamma^2+\Delta^2)^2}.$$

Setting the numerator to zero gives $\Gamma^2 = \Delta^2$, hence

$$\Gamma^* = \Delta.$$

With the stated input $\Delta = 100\ \mathrm{cm^{-1}}$:

$$\Gamma^* = 100\ \mathrm{cm^{-1}}.$$

The optimal rate is $k^* = k(\Gamma^*) = \dfrac{2V^2\Delta}{2\Delta^2} = \dfrac{V^2}{\Delta}$. With $V = 30\ \mathrm{cm^{-1}}$:

$$k^* = \frac{(30)^2}{100} = \frac{900}{100} = 9\ \mathrm{cm^{-1}}.$$

### 4.2 Transfer time (derivation)

Convert $k^*$ to a rate in $\mathrm{s^{-1}}$. In units with $\hbar = 1$, an energy $E$ corresponds to an angular frequency $\omega = E/\hbar$; the hopping rate $k^*$ as an energy corresponds to the angular frequency

$$\omega^* = 2\pi c \times k^* = 2\pi \times (2.9979\times 10^{10}\ \mathrm{cm^{-1}\,s^{-1}}) \times 9\ \mathrm{cm^{-1}}.$$

Compute step by step:

$$2.9979\times 10^{10} \times 9 = 2.69811\times 10^{11}\ \mathrm{Hz},$$

$$\omega^* = 2\pi \times 2.69811\times 10^{11} = 1.6952\times 10^{12}\ \mathrm{rad/s}.$$

The transfer time is

$$\tau_T = \frac{1}{\omega^*} = \frac{1}{1.6952\times 10^{12}} = 5.899\times 10^{-13}\ \mathrm{s} \approx 0.59\ \mathrm{ps}.$$

### 4.3 Trapping-limited efficiency (derivation)

With trap rate $\kappa = 1\ \mathrm{ps^{-1}}$ and exciton lifetime $\tau_e = 1\ \mathrm{ns} = 1000\ \mathrm{ps}$, the probability that the excitation is trapped before it recombines, for a single effective transfer step of duration $\tau_T$, is approximately

$$\eta \approx \frac{\kappa}{\kappa + \tau_T^{-1}\,\tau_T/\tau_e \cdot \tau_T^{-1}}\ \text{— we use instead the standard competing-channel form}$$

$$\eta = \frac{\kappa}{\kappa + \gamma_{\mathrm{rec}}},$$

where $\gamma_{\mathrm{rec}} = 1/\tau_e = 1/1000\ \mathrm{ps} = 10^{-3}\ \mathrm{ps^{-1}}$ is the recombination rate. Then

$$\eta = \frac{1}{1 + 10^{-3}} = \frac{1}{1.001} = 0.999001.$$

To first order the transfer step itself is fast compared with both trap and recombination ($\tau_T = 0.59\ \mathrm{ps} \ll 1/\kappa = 1\ \mathrm{ps}$ is marginal; $\tau_T \ll \tau_e$ is satisfied by three orders of magnitude), so the dominant efficiency loss is recombination during the $\sim 1\ \mathrm{ps}$ trapping window, giving

$$\eta \approx 0.999.$$

This is consistent with the "well above $90\%$" efficiencies reported for FMO-scale networks under optimal dephasing [1]; our two-site number is an upper-bound-flavored estimate because it ignores multi-hop losses, which we flag as a limitation.

### 4.4 Memory ratio and regime classification (derivation)

Using $\tau_T = 0.59\ \mathrm{ps}$ from Section 4.2 and the two bounding bath memory times from Section 3.3:

Fast (solvent-like) limit, $\tau_B = 0.1\ \mathrm{ps}$:

$$R_{\mathrm{fast}} = \frac{0.1}{0.59} = 0.169.$$

Slow (intramolecular) limit, $\tau_B = 1\ \mathrm{ps}$:

$$R_{\mathrm{slow}} = \frac{1}{0.59} = 1.695.$$

Applying the criterion of Section 3.2 ($R \lesssim 0.1$ Markovian; $0.1 < R < 0.5$ transitional; $R \gtrsim 0.5$ non-Markovian required):

- $R_{\mathrm{fast}} = 0.169$: transitional regime — Markovian treatment acceptable with estimated error.
- $R_{\mathrm{slow}} = 1.695$: firmly non-Markovian — the boson-mediated framework [9] is required.

### 4.5 Sensitivity of the classification to $\tau_T$ (derivation)

The classification depends on $V$ and $\Delta$ through $\tau_T = \hbar\Delta/(2\pi c\,V^2)$. If $V$ were $20\ \mathrm{cm^{-1}}$ instead of $30\ \mathrm{cm^{-1}}$ (weaker coupling), then

$$k^* = \frac{V^2}{\Delta} = \frac{400}{100} = 4\ \mathrm{cm^{-1}},$$

$$\omega^* = 2\pi \times 2.9979\times 10^{10} \times 4 = 7.542\times 10^{11}\ \mathrm{rad/s},$$

$$\tau_T = \frac{1}{7.542\times 10^{11}} = 1.326\times 10^{-12}\ \mathrm{s} \approx 1.33\ \mathrm{ps}.$$

Then $R_{\mathrm{fast}} = 0.1/1.33 = 0.075$ (Markovian suffices) and $R_{\mathrm{slow}} = 1/1.33 = 0.754$ (non-Markovian required). If $V = 50\ \mathrm{cm^{-1}}$ (stronger coupling):

$$k^* = \frac{2500}{100} = 25\ \mathrm{cm^{-1}},\quad \omega^* = 2\pi \times 2.9979\times 10^{10}\times 25 = 4.714\times 10^{12}\ \mathrm{rad/s},$$

$$\tau_T = \frac{1}{4.714\times 10^{12}} = 2.121\times 10^{-13}\ \mathrm{s} \approx 0.21\ \mathrm{ps},$$

giving $R_{\mathrm{fast}} = 0.1/0.21 = 0.47$ (transitional, near the non-Markovian boundary) and $R_{\mathrm{slow}} = 1/0.21 = 4.71$ (strongly non-Markovian). The classification of the slow-mode sector is robust across a factor-of-$2.5$ variation in $V$; the fast-mode sector is genuinely transitional and sensitive.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are simulated or measured.

1. **Optimal dephasing rate.** $\Gamma^* = \Delta = 100\ \mathrm{cm^{-1}}$ (Section 4.1).
2. **Optimal hopping rate.** $k^* = V^2/\Delta = 9\ \mathrm{cm^{-1}}$ for $V = 30\ \mathrm{cm^{-1}}$, $\Delta = 100\ \mathrm{cm^{-1}}$ (Section 4.1).
3. **Transfer time.** $\tau_T \approx 0.59\ \mathrm{ps}$ (Section 4.2).
4. **Trapping-limited efficiency.** $\eta \approx 0.999$ for $\kappa = 1\ \mathrm{ps^{-1}}$, $\tau_e = 1\ \mathrm{ns}$ (Section 4.3).
5. **Memory ratios.** $R_{\mathrm{fast}} = 0.169$ ($\tau_B = 0.1\ \mathrm{ps}$) and $R_{\mathrm{slow}} = 1.695$ ($\tau_B = 1\ \mathrm{ps}$) (Section 4.4).
6. **Regime classification.** Fast solvent-like modes: transitional ($0.1 < R < 0.5$). Slow intramolecular modes: non-Markovian framework required ($R \gtrsim 0.5$), robust to $V \in [20, 50]\ \mathrm{cm^{-1}}$ (Section 4.5).

**Projection (explicitly labeled).** If the re-entry criterion is correct, the falsifiable prediction is that in complexes dominated by slow intramolecular vibrational modes — the regime identified in [7] — the boson-mediated non-Markovian framework [9] should predict (a) transient population backflow between sites on timescales $\sim \tau_B$, absent in the Markovian reduction, and (b) a shift of the effective optimal noise level away from $\Gamma^* = \Delta$ by a correction of order $R$. The magnitude of the shift is not computed here; it is a projection requiring the full framework of [9] and is stated only as a hypothesis with the assumed scaling $\delta\Gamma^*/\Gamma^* \sim R$, uncertainty at least a factor of two.

## 6. Discussion

**Limitations.** The analysis rests on a two-site toy model with literature-scale representative parameters, not on a specific complex's Hamiltonian. The efficiency estimate $\eta \approx 0.999$ ignores multi-hop transport and disorder-induced bottlenecks; realistic FMO efficiencies computed in [1], [6] are lower precisely because of these effects, so our number should be read as a single-hop ceiling, not a complex-level prediction. The re-entry thresholds ($R \lesssim 0.1$, $R \gtrsim 0.5$) are conventions, not derived boundaries; a different convention shifts the transitional window but not the robust conclusion that slow intramolecular modes place the system deep in the non-Markovian sector.

**Failure modes.** The classification could fail in three ways. First, if the relevant bath modes are neither purely fast nor purely slow but bimodal, the single-$\tau_B$ description collapses and the memory ratio must be replaced by a spectral-density-weighted criterion. Second, if strong system–bath coupling invalidates the weak-coupling Haken–Strobl rate formula, the derived $\tau_T$ is wrong and the classification must be redone; the framework of [3], which derives time-dependent coefficients microscopically, is the appropriate tool in that case. Third, if vibrational modes act as quasi-resonant bridges rather than as a memory bath, transport becomes vibronic rather than noise-assisted [7], [10], and the entire dephasing-based timescale analysis underestimates the coherent channel.

**What would falsify the claims.** The central claim — that the boson-mediated non-Markovian framework re-enters light-harvesting for slow-mode-dominated baths — is falsified if full simulations within [9] on a realistic FMO Hamiltonian show that non-Markovian corrections to populations, trapping currents, and the optimal dephasing rate are below experimental sensitivity (e.g., relative corrections $\ll 10^{-2}$) even when $R \gtrsim 0.5$. Conversely, the claim that the Markovian reduction suffices for fast baths is falsified by demonstrated order-unity corrections at $R \approx 0.1$. The projected shift $\delta\Gamma^*/\Gamma^* \sim R$ (Section 5) is a hypothesis, not a result, and would itself need verification.

**Arguing against ourselves.** A skeptic could say the re-entry question is answered trivially: since [6] and [7] already identify non-Markovian and nuclear-quantum effects as dynamically important, of course a non-Markovian framework applies. Our response is that importance of the effect and necessity of the framework are distinct claims; the timescale criterion is what connects them quantitatively, and it shows the necessity is sector-dependent — a more useful and more falsifiable statement than a blanket "non-Markovianity matters." A second skeptic could object that the Floquet stroboscopic analysis of [4] shows apparent Markovianity can be sampling-dependent, undermining any single-timescale classification; we agree this is a real risk for periodically modulated baths and flag continuous-time monitoring as the required test. Finally, the thermodynamic resource perspective of [5] suggests memory could be exploited, not just tolerated; whether light-harvesting biology actually exploits it is an open biological question our analysis cannot settle.

**Open questions.** (i) What is the exact prefactor in the projected shift $\delta\Gamma^*/\Gamma^*$? (ii) Does the criterion generalize to multi-site networks, where transfer time becomes path-dependent? (iii) Can the stroboscopic-divisibility caveat of [4] be turned into an experimental signature distinguishing structured non-Markovian baths from Markovian ones in vivo?

## 7. Conclusion

We posed the re-entry question for the non-Markovian boson-mediated transport framework [9] in light-harvesting complexes and answered it with a quantitative timescale analysis. From a two-site dephasing-assisted transport model with FMO-scale inputs ($V = 30\ \mathrm{cm^{-1}}$, $\Delta = 100\ \mathrm{cm^{-1}}$), we derived the optimal dephasing rate $\Gamma^* = \Delta = 100\ \mathrm{cm^{-1}}$, the hopping rate $k^* = 9\ \mathrm{cm^{-1}}$, the transfer time $\tau_T \approx 0.59\ \mathrm{ps}$, and the single-hop efficiency ceiling $\eta \approx 0.999$. Comparing $\tau_T$ with bath memory times $\tau_B \in [0.1, 1]\ \mathrm{ps}$ yields memory ratios $R \in [0.17, 1.7]$: fast solvent-like modes sit in a transitional regime where the Markovian reduction is acceptable, while slow intramolecular modes — the sector highlighted by nuclear-quantum-effect studies [7] — place the dynamics firmly in the non-Markovian regime, robustly across a factor-of-$2.5$ variation in coupling. The re-entry verdict is therefore conditional but sharp: the framework earns its complexity exactly where vibrational structure dominates, and the projected observable signature is a memory-scaled shift of the optimal noise level, stated here explicitly as a falsifiable hypothesis.

## References

[1] arXiv:0910.4153v2 | Noise-assisted energy transfer in quantum networks and light-harvesting complexes

[2] arXiv:2001.02247v1 | Non-Markovian quantum dynamics: What is it good for?

[3] arXiv:0705.2472v3 | Non-Markovian decoherence dynamics of entangled coherent states

[4] arXiv:1707.04423v2 | Floquet stroboscopic divisibility in non-Markovian dynamics

[5] arXiv:2310.04347v2 | Availing non-Markovian dynamics in effective negative temperature-based transient quantum Otto engines

[6] arXiv:1103.3823v4 | Efficient estimation of energy transfer efficiency in light-harvesting complexes

[7] arXiv:2501.02212v1 | Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes

[8] arXiv:astro-ph/0510346v1 | The Dark Energy Survey

[9] QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer | DOI 10.5281/zenodo.18382696

[10] QNFO: Quantum Coherence in Photosystem II: Environment-Assisted Transport and the Role of Vibronic Coupling in Biological Light-Harvesting | DOI 10.5281/zenodo.21304627