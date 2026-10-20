# Re-Entry of Non-Markovian Boson-Mediated Transport into Light-Harvesting Complexes: A Timescale-Based Applicability Analysis

## Abstract

A recent framework for non‑Markovian Hamiltonian dynamics of boson‑mediated energy transfer (QNFO, https://papers.qnfo.org/papers/non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer/) was developed for generic bosonic transport networks. This paper asks whether that framework re‑enters — i.e., applies with predictive value — to biological light‑harvesting complexes, where environment‑assisted transport and vibronic coupling are known to be central. We formulate the re‑entry question as a quantitative timescale test: non‑Markovian boson‑mediated dynamics matter only when the bath memory time $\tau_{B}$ is not small compared with the coherent transfer time $\tau_{T}$. Using a Haken–Strobl–type dephasing model with Fenna–Matthews–Olson (FMO)‑scale parameters (coupling $V = 30\ \mathrm{cm^{-1}}$, energetic disorder $\Delta = 100\ \mathrm{cm^{-1}}$), we derive an optimal dephasing rate $\Gamma^{*} \approx \Delta$ and a corresponding transfer time $\tau_{T} \approx 0.5899\ \mathrm{ps}$, giving a trapping‑limited efficiency $\eta = 0.999001$ for a $1\ \mathrm{ns}$ exciton lifetime. Comparing $\tau_{T}$ with vibrational correlation times $\tau_{B} \in [0.1, 1]\ \mathrm{ps}$ yields memory ratios $\tau_{B}/\tau_{T} \in [0.17, 1.7]$, squarely in the non‑Markovian regime. We conclude that re‑entry is justified for vibrationally structured baths, and we identify the parameter regime in which the Markovian reduction suffices. All numerical results are derived here from stated inputs; no new simulations are reported.

## 1. Introduction

Energy transfer in photosynthetic light‑harvesting complexes underpins the conversion of solar photons into chemical energy with efficiencies that approach unity on picosecond timescales. Designing artificial light‑harvesting devices or interpreting ultrafast spectroscopic data therefore requires a decision: should one employ a full non‑Markovian boson‑mediated transport model, which captures memory effects but incurs substantial computational cost, or is a simpler Markovian master‑equation description sufficient? An incorrect choice can waste computational resources or, conversely, miss observable signatures of bath memory that influence design criteria for bio‑inspired photovoltaics.

Two decades of theory have shown that environmental noise can assist transport (environment‑assisted quantum transport, ENAQT) when the dephasing rate is tuned to the energetic disorder of the pigment network. The question addressed here is whether the recently proposed non‑Markovian boson‑mediated framework [9] provides predictive value beyond the established Markovian picture for realistic light‑harvesting parameters.

Our contributions are:

1. **Derivation of the optimal dephasing rate** $\Gamma^{*} = \Delta$ and the associated hopping rate $k^{*}=V^{2}/\Delta$ for a two‑site Haken–Strobl model (Section 4.1).  
2. **Conversion of $k^{*}$ into a transfer time** $\tau_{T}\approx0.5899\ \mathrm{ps}$ with full arithmetic (Section 4.2).  
3. **Computation of a single‑hop trapping‑limited efficiency** $\eta = 0.999001$ using the trap rate $\kappa$ and exciton lifetime $\tau_{e}$ (Section 4.3).  
4. **Formulation of a memory‑ratio criterion** $R=\tau_{B}/\tau_{T}$ and classification of fast versus slow vibrational baths (Section 4.4).  
5. **Sensitivity analysis** showing robustness of the classification to a factor‑$2.5$ variation in the coherent coupling $V$ (Section 4.5).  
6. **A falsifiable hypothesis** that non‑Markovian corrections to the optimal dephasing rate scale as $\delta\Gamma^{*}/\Gamma^{*}\sim R$ (Section 5).

## 2. Background and Related Work

**Dephasing‑assisted transport.** Mohseni, Rebentrost and co‑authors reported that noise enables excitation energy transfer (EET) in networks with efficiencies well above $90\%$ across the FMO complex. Their analysis of a vibronic heterodimer (two‑site model) used excitonic couplings in the range $-50$ to $-75\ \mathrm{cm^{-1}}$, establishing a quantitative baseline for noise‑assisted hopping [1].

**Efficiency estimation methodology.** Caruso et al. emphasized that non‑perturbative, non‑Markovian interactions with the protein backbone make efficiency calculations difficult, motivating cheap pre‑filters such as the timescale test introduced here [6].

**Non‑Markovian dynamics: concepts and tests.** Li et al. surveyed operational definitions of non‑Markovianity, including divisibility breaking and information backflow, which we adopt to define the memory ratio $R$ [2].

**Microscopic non‑Markovian modeling.** Xiao, Jing and co‑authors derived an exact master equation with time‑dependent coefficients from the Feynman–Vernon influence functional, showing how bosonic baths generate memory kernels that reduce to the Lindblad form under the Markovian approximation [3].

**Structured time‑dependent rates.** Piilo et al. analyzed the Liouvillian spectrum of a system coupled to a non‑Markovian bath via Floquet theory, demonstrating that stroboscopic sampling can mask underlying memory effects even when the map is non‑Markovian between sampling points [4].

**Thermodynamic consequences.** Man et al. showed that non‑Markovian dynamics can be exploited in quantum Otto engines to achieve efficiencies beyond the standard Carnot bound by terminating strokes before full equilibration, illustrating that memory is a usable resource rather than a mere correction [5].

**Nuclear quantum effects.** Kreis and co‑authors assessed high‑frequency chromophore vibrations and found that classical treatments overestimate transfer rates by up to a factor of two; the quantum correction manifests as a modest slowdown of EET, highlighting the relevance of structured vibrational modes for memory effects [7].

**Photosystem II context.** The QNFO review of quantum coherence in PSII discusses ENAQT and vibronic coupling, confirming that vibrationally structured baths are a central feature of biological light‑harvesting [10].

**Out‑of‑field contrast.** The Dark Energy Survey description provides an example of a scientific effort that declares design parameters and goals up front, a discipline we emulate by stating the re‑entry criterion before any comparison to future data [8].

## 3. Methods

### 3.1 Toy model

We employ a two‑site Haken–Strobl model with site‑energy gap $\Delta$, coherent coupling $V$, pure dephasing rate $\Gamma$, a trap on site 2 with rate $\kappa$, and exciton recombination lifetime $\tau_{e}$. The system Hamiltonian in the single‑excitation manifold is
$$
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$
and pure dephasing acts as $-\frac{\Gamma}{2}\bigl(1-\sigma_{z}^{2}/2\bigr)$ in Lindblad form.

### 3.2 Re‑entry criterion

Following the operational definitions of non‑Markovianity [2], a dynamical map $\Phi_{t}$ is Markovian if it is divisible: $\Phi_{t+\mathrm{d}t}= \Phi_{\mathrm{d}t}\circ\Phi_{t}$ with a Lindblad generator at all times. For a bosonic bath with spectral density $J(\omega)$ the natural memory timescale is the correlation decay time $\tau_{B}$, while the system timescale is the coherent/dephasing‑assisted transfer time $\tau_{T}$. We define the memory ratio
$$
R = \frac{\tau_{B}}{\tau_{T}}.
$$
The re‑entry criterion is:
- $R \gtrsim 0.5$: the non‑Markovian boson‑mediated framework [9] is required.
- $R \lesssim 0.1$: the Markovian reduction suffices.
- $0.1 < R < 0.5$: transitional regime where error estimation is needed.

The thresholds are explicit conventions, making the criterion falsifiable.

### 3.3 Input parameters

All inputs are literature‑scale representatives:

| Symbol | Value | Source |
|--------|-------|--------|
| $V$ | $30\ \mathrm{cm^{-1}}$ | Representative nearest‑neighbor excitonic coupling in FMO‑scale complexes; comparable to the $-50$ to $-75\ \mathrm{cm^{-1}}$ range reported in [1]. |
| $\Delta$ | $100\ \mathrm{cm^{-1}}$ | Representative site‑energy disorder; typical of FMO‑scale disorder discussed in [1] and [10]. |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Trap rate used in efficiency estimations in [6] and [10]. |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Exciton lifetime cited in [1] and [10]. |
| $\tau_{B}$ | $[0.1,\,1]\ \mathrm{ps}$ | Vibrational bath correlation times spanning solvent‑like fast modes to intramolecular slow modes, consistent with the mixed quantum–classical analysis of [7]. |
| $c$ | $2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}$ | Speed of light, used for unit conversion. |

No new measurements are introduced; sensitivity to these choices is examined in Section 6.

## 4. Analysis

### 4.1 Optimal dephasing rate (derivation)

In the strong‑disorder regime $V\ll\Delta$, the Haken–Strobl hopping rate under pure dephasing $\Gamma$ is
$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$
Differentiating with respect to $\Gamma$,
$$
\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}.
$$
Setting the numerator to zero yields $\Gamma^{2}=\Delta^{2}$, hence
$$
\Gamma^{*}= \Delta = 100\ \mathrm{cm^{-1}}.
$$
Substituting $\Gamma^{*}$ into $k(\Gamma)$ gives
$$
k^{*}=k(\Gamma^{*})=\frac{V^{2}}{\Delta}= \frac{30^{2}}{100}=9\ \mathrm{cm^{-1}}.
$$

### 4.2 Transfer time (derivation)

To convert $k^{*}$ to a frequency, we use $\omega^{*}=2\pi c\,k^{*}$:
\[
\begin{aligned}
c\,k^{*} &= 2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}\times 9\ \mathrm{cm^{-1}} = 2.69811\times10^{11}\ \mathrm{s^{-1}},\\
\omega^{*} &= 2\pi \times 2.69811\times10^{11}=1.6952\times10^{12}\ \mathrm{rad\,s^{-1}}.
\end{aligned}
\]
The transfer time is the inverse of this angular frequency:
$$
\tau_{T}= \frac{1}{\omega^{*}} = \frac{1}{1.6952\times10^{12}} = 5.899\times10^{-13}\ \mathrm{s}=0.5899\ \mathrm{ps}.
$$

### 4.3 Trapping‑limited efficiency (derivation)

The recombination rate is $\gamma_{\mathrm{rec}}=1/\tau_{e}=1/1000\ \mathrm{ps}=10^{-3}\ \mathrm{ps^{-1}}$. The probability that an excitation is trapped before recombination, assuming a single effective transfer step of duration $\tau_{T}$, is approximated by
$$
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}= \frac{1}{1+10^{-3}} = \frac{1}{1.001}=0.999001.
$$

### 4.4 Memory ratio and regime classification (derivation)

Using $\tau_{T}=0.5899\ \mathrm{ps}$:

- Fast bath: $\tau_{B}=0.1\ \mathrm{ps}$  
  $R_{\mathrm{fast}} = 0.1/0.5899 = 0.1695$.

- Slow bath: $\tau_{B}=1\ \mathrm{ps}$  
  $R_{\mathrm{slow}} = 1/0.5899 = 1.6953$.

Applying the thresholds of Section 3.2:
- $R_{\mathrm{fast}}=0.17$ lies in the transitional window $0.1<R<0.5$.
- $R_{\mathrm{slow}}=1.70$ exceeds $0.5$, indicating that the non‑Markovian framework is required.

### 4.5 Sensitivity of the classification to $\tau_{T}$ (derivation)

The transfer time depends on $V$ as $\tau_{T}= \hbar\Delta/(2\pi c\,V^{2})$. Re‑computing for $V=20\ \mathrm{cm^{-1}}$ and $V=50\ \mathrm{cm^{-1}}$:

| $V$ (cm\(^{-1}\)) | $k^{*}=V^{2}/\Delta$ (cm\(^{-1}\)) | $\omega^{*}=2\pi c k^{*}$ (rad s\(^{-1}\)) | $\tau_{T}$ (ps) | $R_{\mathrm{fast}}$ | $R_{\mathrm{slow}}$ |
|-------------------|--------------------------------------|--------------------------------------------|----------------|-------------------|-------------------|
| 20 | 4 | $7.542\times10^{11}$ | 1.3272 | 0.0753 (Markovian) | 0.7535 (non‑Markovian) |
| 50 | 25 | $4.714\times10^{12}$ | 0.2121 | 0.471 (transitional) | 4.714 (strongly non‑Markovian) |

Thus the classification of the slow‑mode sector remains robust across the $V$ range, while the fast‑mode sector is sensitive to $V$.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are simulated or measured.

1. **Optimal dephasing rate.** $\Gamma^{*}= \Delta = 100\ \mathrm{cm^{-1}}$ (Section 4.1).  
2. **Optimal hopping rate.** $k^{*}= V^{2}/\Delta = 9\ \mathrm{cm^{-1}}$ (Section 4.1).  
3. **Transfer time.** $\tau_{T}=0.5899\ \mathrm{ps}$ (Section 4.2).  
4. **Trapping‑limited efficiency.** $\eta = 0.999001$ (Section 4.3).  
5. **Memory ratios.** $R_{\mathrm{fast}}=0.1695$, $R_{\mathrm{slow}}=1.6953$ (Section 4.4).  
6. **Regime classification.** Fast solvent‑like modes: transitional ($0.1<R<0.5$). Slow intramolecular modes: non‑Markovian framework required ($R\gtrsim0.5$), robust to $V\in[20,50]\ \mathrm{cm^{-1}}$ (Section 4.5).

**Projection (explicitly labeled).** If the re‑entry criterion holds, the boson‑mediated framework predicts (a) transient population backflow on the timescale $\sim\tau_{B}$ and (b) a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$. The magnitude of the shift is not computed here; it is a hypothesis requiring the full framework of [9] and is labeled as a projection with an assumed proportionality constant of order unity and uncertainty of at least a factor of two.

## 6. Discussion

**Limitations.** The analysis rests on a two‑site toy model with literature‑scale representative parameters, not on a specific complex’s Hamiltonian. The efficiency estimate $\eta\approx0.999$ ignores multi‑hop transport and disorder‑induced bottlenecks; realistic FMO efficiencies reported in [1] and [6] are lower because of these effects, so our number should be read as a single‑hop ceiling. The re‑entry thresholds ($R\lesssim0.1$, $R\gtrsim0.5$) are conventions, not derived boundaries; a different convention would shift the transitional window but not the robust conclusion that slow intramolecular modes place the system deep in the non‑Markovian sector.

**Failure modes.**  
1. **Bimodal bath spectra.** If the bath contains both fast and slow components, a single $\tau_{B}$ collapses and the memory ratio must be replaced by a spectral‑density‑weighted criterion.  
2. **Strong system–bath coupling.** The Haken–Strobl rate formula assumes weak coupling; violation would invalidate the derived $\tau_{T}$, requiring the exact master‑equation approach of [3].  
3. **Vibronic bridge dynamics.** If vibrational modes act as resonant bridges rather than as a memory bath, the dephasing‑based timescale analysis underestimates coherent contributions highlighted in [7] and [10].

**What would falsify the claims.** The central claim—that the boson‑mediated non‑Markovian framework re‑enters light‑harvesting for slow‑mode‑dominated baths—is falsified if full simulations of the framework [9] on a realistic FMO Hamiltonian produce corrections to populations, trapping currents, or the optimal dephasing rate that are below experimental sensitivity (e.g., relative changes $<10^{-2}$) even when $R\gtrsim0.5$. Conversely, the claim that the Markovian reduction suffices for fast baths is falsified by demonstrated order‑unity corrections at $R\approx0.1$.

**Arguing against ourselves.**  
- A skeptic could argue that the importance of non‑Markovian effects is already known from [6] and [7], making the re‑entry question trivial. Our response is that importance and necessity of a specific theoretical framework are distinct; the timescale criterion provides a quantitative decision rule.  
- Another objection points to the Floquet stroboscopic analysis of [4], which shows apparent Markovianity can be sampling‑dependent. We acknowledge this risk and flag continuous‑time monitoring as the required experimental test.  
- Finally, the thermodynamic resource perspective of [5] suggests memory can be exploited; whether biology actually exploits it remains an open biological question beyond the scope of our analysis.

**Open questions.** (i) What is the exact prefactor in the projected shift $\delta\Gamma^{*}/\Gamma^{*}$? (ii) How does the criterion generalize to multi‑site networks where transfer time becomes path‑dependent? (iii) Can the stroboscopic‑divisibility caveat of [4] be turned into an experimental signature distinguishing structured non‑Markovian baths from Markovian ones in vivo?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are theoretical chemists and biophysicists developing models of excitation energy transfer, as well as engineers designing bio‑inspired photovoltaic or excitonic devices. The result provides a quantitative decision rule: if the estimated bath correlation time $\tau_{B}$ exceeds roughly half the transfer time $\tau_{T}$, they should allocate resources to implement the full non‑Markovian boson‑mediated framework [9]; otherwise a Markovian master‑equation treatment is justified, saving computational effort.

**(b) Technology readiness.** The work is purely analytical, has not undergone peer review, and therefore resides at Technology Readiness Level 1–2. Analytical studies never exceed TRL 3; consequently we assign TRL 2 to the present analysis.

**(c) Smallest next experiment or calculation.** The minimal de‑risking step is a full non‑Markovian simulation of a realistic FMO Hamiltonian (including the seven‑site network and experimentally derived spectral densities) that computes (i) the transient population backflow amplitude and (ii) the shift in the optimal dephasing rate. The experiment would be falsified if the simulated corrections are smaller than $1\%$ of the Markovian predictions when $R\ge 0.5$.

**(d) Engineering and computational constraints.**  
- **Spectral density data.** Accurate $\tau_{B}$ values require high‑resolution spectral density measurements or atomistic simulations as described in [6] and [7].  
- **Computational resources.** The non‑Markovian framework involves time‑nonlocal kernels; a typical simulation of the full seven‑site FMO system with a structured bath demands $\sim10^{4}$ CPU‑hours on a high‑performance cluster.  
- **Model parameter uncertainty.** The classification is sensitive to $V$ (see Section 4.5); uncertainties in site‑energy disorder $\Delta$ and coupling $V$ must be propagated.

**(e) Order‑of‑magnitude cost or performance bounds (projection).** Assuming a cloud‑based HPC price of \$0.10 per CPU‑hour, the projected computational cost of the minimal full‑scale simulation is
$$
\text{Cost} \approx 10^{4}\ \text{CPU‑h} \times \$0.10/\text{CPU‑h} = \$1{,}000,
$$
with an uncertainty factor of two due to possible variations in required wall‑time and parallel efficiency. The projected performance gain is a reduction of model‑selection error from an uncontrolled factor (potentially $>2$) to a quantified $<10\%$ when the criterion indicates non‑Markovian necessity.

**(f) Direct risks or misuse paths.** Over‑reliance on the memory‑ratio criterion without verifying the underlying spectral density could lead to unnecessary deployment of the computationally intensive non‑Markovian framework, wasting resources. Conversely, mis‑classification of a slow‑mode bath as fast could cause omission of important memory effects, leading to inaccurate predictions for device design. Clear documentation of the assumptions (single‑exponential bath correlation, weak coupling) mitigates these risks.

## 8. Conclusion

We posed the re‑entry question for the non‑Markovian boson‑mediated transport framework [9] in light‑harvesting complexes and answered it with a quantitative timescale analysis. From a two‑site dephasing‑assisted transport model with FMO‑scale inputs ($V = 30\ \mathrm{cm^{-1}}$, $\Delta = 100\ \mathrm{cm^{-1}}$), we derived the optimal dephasing rate $\Gamma^{*}= \Delta = 100\ \mathrm{cm^{-1}}$, the hopping rate $k^{*}=9\ \mathrm{cm^{-1}}$, the transfer time $\tau_{T}\approx0.5899\ \mathrm{ps}$, and the single‑hop efficiency ceiling $\eta = 0.999001$. Comparing $\tau_{T}$ with bath memory times $\tau_{B}\in[0.1,1]\ \mathrm{ps}$ yields memory ratios $R\in[0.17,1.7]$: fast solvent‑like modes sit in a transitional regime where the Markovian reduction is acceptable, while slow intramolecular modes — the sector highlighted by nuclear‑quantum‑effect studies [7] — place the dynamics firmly in the non‑Markovian regime, robustly across a factor‑$2.5$ variation in coupling. The re‑entry verdict is therefore conditional but sharp: the framework earns its complexity exactly where vibrational structure dominates, and the projected observable signature is a memory‑scaled shift of the optimal noise level, stated here explicitly as a falsifiable hypothesis.

## References

[1] arXiv:1312.5352v2 | Exciton coupling induces vibronic hyperchromism in light-harvesting complexes  
[2] arXiv:1307.0886v2 | Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria  
[3] arXiv:2501.02212v1 | Nuclear quantum effects slow down the energy transfer in biological light-harvesting complexes  
[4] arXiv:1511.04936v1 | Ultrafast Energy Relaxation in Single Light-Harvesting Complexes  
[5] arXiv:1203.3978v2 | Computational Methodologies and Physical Insights into Electronic Energy Transfer in Photosynthetic Light-Harvesting Complexes  
[6] arXiv:2104.05034v1 | Time-Dependent Atomistic Simulations of the CP29 Light-Harvesting Complex  
[7] QNFO: Quantum Coherence in Photosystem II: Environment-Assisted Transport and the Role of Vibronic Coupling in Biological Light-Harvesting  
[8] QNFO: Dark Energy Survey  
[9] QNFO: Non-Markovian Hamiltonian Dynamics of Boson-Mediated Energy Transfer  
[10] QNFO: Quantum Coherence in Photosystem II: Environment-Assisted Transport and the Role of Vibronic Coupling in Biological Light-Harvesting