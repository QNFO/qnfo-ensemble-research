# Re-Entry of Non-Markovian Boson-Mediated Transport into Light-Harvesting Complexes: A Timescale-Based Applicability Analysis

## Abstract

Photosynthetic antennae transfer excitation energy with near-unity efficiency on sub-picosecond timescales, and modelers must decide whether the computationally expensive non-Markovian boson-mediated framework is required or a cheaper Markovian dephasing master equation suffices. The published applicability analysis of this decision used a coupling range wider than the experimentally reported values, a dimensionally inconsistent transfer-time formula, an incorrect Lindblad dephasing term, and an unsupported analogy to urban multiplex networks. This revision adopts the experimentally reported coupling and site-energy-difference ranges for the FMO BChl 3–4 dimer ($V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$), uses the dimensionally consistent expression $\tau_{T}=\Delta/(2\pi cV^{2})$, and writes the dephasing generator in the standard Lindblad form. For the representative point $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$ the transfer time is $\tau_{T}=0.2336\ \mathrm{ps}$ and the single-hop trapping efficiency is $\eta=0.999001$. The memory ratio $R=\tau_{B}/\tau_{T}$ spans $R_{\mathrm{fast}}\in[0.26,0.96]$ for fast baths ($\tau_{B}=0.1\ \mathrm{ps}$, an assumption informed by sub-100 fs single-molecule relaxation times) and $R_{\mathrm{slow}}\in[2.6,9.6]$ for slow baths ($\tau_{B}=1\ \mathrm{ps}$, assumed), placing all slow-mode scenarios in the non-Markovian sector and fast baths in a range that straddles the transitional threshold. We formulate a falsifiable hypothesis that the optimal dephasing rate shifts by $\delta\Gamma^{*}/\Gamma^{*}\sim R$ when $R\gtrsim0.5$. The corrected memory-ratio rule gives modelers an analytically derived guideline for allocating computational effort in excitation-energy-transfer modeling.

## 1. Introduction

Photosynthetic organisms convert sunlight into chemical free energy after funneling excitation through pigment networks with efficiencies approaching $100\%$ on sub-picosecond excitation-energy-transfer (EET) timescales [2]. Every computational study of this process faces a concrete methodological decision with real costs on both sides: implement the full non-Markovian boson-mediated framework, which retains bath memory at the price of time-nonlocal kernels and large numerical effort, or use a Markovian dephasing master equation, which is cheap but discards physics exactly when bath correlation times approach the transfer time. Choosing wrongly either wastes high-performance-computing allocations or produces transfer rates and optimal dephasing conditions that are quantitatively wrong, which in turn misguides design parameters for bio-inspired light-harvesting devices and the interpretation of ultrafast spectra. A validated, analytically derived decision rule would let a modeler allocate compute where memory effects matter and skip them where they do not.

Two decades of theory establish that environmental noise can assist rather than hinder transport. Dephasing-assisted transport (DAT) raises EET efficiencies well above $90\%$ across the Fenna–Matthews–Olson (FMO) complex within a fully Markovian treatment, and the mechanisms—suppression of destructive interference and dephasing-broadened site overlap—are worked out analytically for fully connected networks [2, 8]. On the experimental side, single-molecule pump–probe spectroscopy resolves sub-100 fs energy relaxation in individual light-harvesting complexes [7], so fast solvent-like bath components with correlation times of order $0.1\ \mathrm{ps}$ are consistent with measured relaxation, not inferred from bulk averages. Mixed quantum–classical simulations show that treating high-frequency chromophore vibrations quantum-mechanically instead of classically slows transfer rates by less than a factor of two for biologically relevant parameters at $300\ \mathrm{K}$ [6]. The target framework whose applicability we assess is the non-Markovian boson-mediated description, in which structured phonon fields are proposed to direct exciton transport and claimed to sustain efficiencies above $95\%$ [10].

This paper is a post-publication revision of a prior applicability analysis [9]. The published version contained six reported defects, each of which we checked against its own derivations and the sources:

1. The claim that the sensitivity box $V\in[20,75]\ \mathrm{cm^{-1}}$ is "the full experimentally reported range" is **incorrect**. The source for the dimer parameters reports excitonic coupling between BChl 3 and 4 of about $-50$ to $-75\ \mathrm{cm^{-1}}$ and a transition energy difference from about $110$ to $180\ \mathrm{cm^{-1}}$ [4]. The lower coupling bound is therefore $50\ \mathrm{cm^{-1}}$, not $20\ \mathrm{cm^{-1}}$; this revision uses $V\in[50,75]\ \mathrm{cm^{-1}}$ throughout.
2. The transfer-time formula $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$ is **dimensionally inconsistent**: with $V$ and $\Delta$ as wavenumbers, $\hbar\Delta/(2\pi cV^{2})$ carries units of $\mathrm{J\cdot s\cdot cm}$, not time. The corrected formula is $\tau_{T}=\Delta/(2\pi cV^{2})$ (Section 4.2).
3. The published abstract's statement that "$R=\tau_{B}/\tau_{T}$ spans 0.17–1.70" is **incorrect**; the correct ranges over the reported box are $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$ (Section 4.4). The accompanying characterization of fast baths as lying "in a transitional window" is imprecise: the fast-bath range straddles the $R=0.5$ threshold, so fast baths are transitional for part of the box and near-non-Markovian for the rest.
4. The published Section 6.2 cited a study of urban transportation multiplex networks [3] as "mirroring" the $R$-sensitivity result. That work develops an overlap census method and clusters 15 cities by multimodal profile [3]; it makes no claim about exciton transport, and the mirroring claim is **removed**.
5. The published abstract's ranges $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$ **agree** with the derivation in Section 4.4 and are retained unchanged.
6. The Lindblad dephasing term written as $-\frac{\Gamma}{2}(1-\sigma_{z}^{2}/2)$ is **incorrect**: since $\sigma_{z}^{2}=\mathbb{1}$ for the Pauli operator, this expression reduces to a scalar multiple of the identity and generates no dynamics. The standard pure-dephasing generator $\frac{\Gamma}{2}(\sigma_{z}\rho\sigma_{z}-\rho)$ is used instead (Section 3.1).

**Contributions.**
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two-site Haken–Strobl model, with the derivative shown explicitly (Section 4.1).
2. Correction of the transfer-time formula to $\tau_{T}=\Delta/(2\pi cV^{2})$, with a dimensional check, and its evaluation over the experimentally reported box, giving $\tau_{T}\in[0.1038,0.3822]\ \mathrm{ps}$ and $\tau_{T}=0.2336\ \mathrm{ps}$ at the representative point (Section 4.2).
3. Computation of the single-hop trapping-limited efficiency $\eta=0.999001$ under stated assumptions for the trap and recombination rates (Section 4.3).
4. Recomputation of the memory ratios over the reported box, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, with a corner-extremality argument (Section 4.4).
5. A corrected regime classification: within the reported box no bath in the range $\tau_{B}\in[0.1,1]\ \mathrm{ps}$ falls in the Markovian sector, slow baths are non-Markovian everywhere, and fast baths straddle the transitional threshold (Section 5).
6. A falsifiable projection that the non-Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\sim R$, with its tension against the sub-twofold rate effects found for vibrational quantization [6] (Sections 5 and 6).

## 2. Background and Related Work

**Transient thermal-grating forward modeling.** Transient thermal grating (TTG) experiments probe material properties and heat-transport dynamics at small spatiotemporal scales through the temporal response to a spatially periodic excitation; quantitative interpretation of the measured transient requires a forward model that consistently connects energy deposition, subsequent transport, and the detected signal [1]. This requirement is the measurement-side analogue of the problem addressed here: a transport model applied outside its validity regime produces a forward model whose output is quantitatively wrong even if its structure is right. The memory-ratio criterion proposed below is a validity test of exactly this kind for the boson-mediated EET forward model.

**Noise-assisted transport in FMO.** Reference [2] provides physically intuitive mechanisms for the effect of noise on EET and, using a hybrid basis of excitons and sites, develops a detailed picture of how dephasing-assisted transport enables energy transfer with efficiencies well above $90\%$ across the FMO complex. Its network model treats the coherent tunneling amplitudes $v_{j,l}$ as free parameters, and its conclusion states that the identification of transport-suppressing pathways is made without reference to the noise model, so any noise model that enhances transport must suppress the inefficient paths and enhance the direct relaxation channels [2]. This model-independence of the DAT mechanism is the reason a Markovian baseline remains the correct null hypothesis against which any non-Markovian framework must demonstrate added value.

**Exciton-coupling magnitudes for the FMO dimer.** Reference [4] studies vibronic exciton dimers with parameters mimicking the FMO complex and reports that BChl 3 and 4 have the lowest site energies, that the transition energy difference is proposed to be from about $110$ to $180\ \mathrm{cm^{-1}}$, and that the excitonic coupling between these two molecules is negative with values from about $-50$ to $-75\ \mathrm{cm^{-1}}$. The same work reports vibrational modes near $180\ \mathrm{cm^{-1}}$ with a total Huang–Rhys factor of 0.03 in the lowest-energy BChl of FMO, and finds that Huang–Rhys factors obtained from fluorescence spectroscopy of coupled pigments need corrections that can reach 100% depending on coupling strength and detuning [4]. We adopt the absolute values $V\in[50,75]\ \mathrm{cm^{-1}}$ and $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ as the experimentally reported parameter box, and the 100% correction finding as a caution that spectroscopically derived vibronic parameters carry model-dependent uncertainty.

**Atomistic energy funneling.** Reference [5] constructs an atomistic model of the green sulfur bacterium light-harvesting complex containing 3988 pigments—chlorosome rolls of 1620 and 2160 BChl $c$ sites, a 64-site baseplate, and six FMO trimers of 144 BChl $a$ sites—and solves a quantum master equation including coherent, dephasing and relaxation processes. Its conclusion reports that resonant energy transfer is maximized by the multichromophoric excitonic coupling across chlorosome, baseplate and FMO, that different initial-excitation scenarios differ qualitatively only within 500 fs, and that all results converge within the overall 10 ps timescale without adversely affecting transfer efficiency [5]. The 10 ps convergence timescale confirms that the dimer-level transfer times computed here ($0.1$–$0.4\ \mathrm{ps}$) sit well inside the window where the funnel operates, and the 500 fs qualitative-divergence window is comparable to the transfer times at the slow corner of our box.

**Quantum nuclear effects on rates.** Reference [6] compares classical and quantum treatments of vibrational motion in LH2, FMO and LHCII at $300\ \mathrm{K}$ using mixed quantum–classical theory. Its discussion concludes that the main difference is not the direction of energy flow but the rate: treating vibrations classically yields the correct long-time equilibrium but generally overestimates the transfer rate, and for biologically relevant parameter regimes the quantum effect on the rate is benign (less than a factor 2) [6]. This bounds from above the size of any quantum correction to Markovian rates that high-frequency vibrations produce by themselves, and it sets the scale against which the projection $\delta\Gamma^{*}/\Gamma^{*}\sim R$ must be judged: for $R\sim3$–$10$ the projection predicts corrections well beyond a factor 2, so the hypothesis is genuinely falsifiable.

**Ultrafast single-molecule spectroscopy.** Reference [7] applies a single-molecule pump–probe technique (SM2P) to LH2 complexes and demonstrates that ultrafast energy relaxation can be observed in individual complexes, with the fastest processes in the sub-100 fs range; the relaxation-time distribution changes with excitation wavelength and is explained qualitatively by the energetic disorder of the LH2 pigments at the values commonly used in bulk modeling [7]. Single-complex resolution matters for the present analysis because bulk averaging can mask complex-to-complex variation in effective relaxation times; the sub-100 fs scale motivates our assumption $\tau_{B}=0.1\ \mathrm{ps}$ for the fast bath component.

**Multiplex-network metrics in other domains.** Reference [3] proposes the overlap census method, which extracts a multimodal profile from a city's multiplex transportation network, applies it to 15 cities, and finds six clusters of cities with similar profiles that explain more than 90% of the variance. This is a layered-transport analysis in urban mobility, a domain with no direct connection to exciton dynamics. The published version of this paper cited [3] as mirroring the $R$-sensitivity result; that claim is retracted here. The only defensible use of [3] in this context is methodological: layered systems can be characterized by scalar profile metrics, and $R=\tau_{B}/\tau_{T}$ is such a scalar metric for the exciton–bath layer pair. No quantitative mirroring is claimed.

**Fundamental role of noise-assisted transport.** Reference [8] analyzes transport assisted by dephasing in dissipative networks and derives exact analytical solutions for uniformly coupled fully connected networks; in the noiseless, dissipationless case it shows that destructive interference limits total transfer to $p_{\mathrm{sink}}(\infty)=1/(N-1)$, and its concluding remarks identify the key mechanisms as suppression of destructive interference by dephasing noise and static disorder, and enhanced site overlap through dephasing-broadened lines [8]. The two-site optimal-dephasing result derived in Section 4.1, $\Gamma^{*}=\Delta$, is the $N=2$ instance of the broadened-overlap mechanism: dephasing at the rate of the energetic mismatch maximizes the spectral overlap of the two sites.

**The boson-mediated non-Markovian framework.** Reference [10] proposes a "boson–fermion signaling" framework in which bosonic fields (phonons) act as structured signals that direct fermionic excitons through the energy landscape, formulated as a non-Markovian Hamiltonian dynamics; it reports simulations in which a phonon field tuned to specific resonances guides excitons with efficiency above $95\%$, and it maps the same principle to driven bosonic fields in superconducting pairing [10]. This framework is the target whose applicability we assess. Its efficiency claim rests on structured, resonant phonon fields, which is precisely the regime where bath memory times matter; the memory-ratio test developed below quantifies when that regime is reached for experimentally reported parameters.

**The prior applicability analysis.** Reference [9] is the published version under revision. It formulated the memory-ratio criterion $R=\tau_{B}/\tau_{T}$ with thresholds at $R\approx0.1$ and $R\approx0.5$, but, as detailed in Section 1, it overstated the coupling range, used a dimensionally inconsistent transfer-time formula, reported incorrect abstract-level $R$ ranges, drew an unsupported analogy to urban multiplex networks, and wrote the dephasing generator incorrectly. The present paper keeps the criterion and thresholds—which are conventions and remain serviceable—and repairs the derivations, the parameter box, the generator, and the external analogies.

## 3. Methods

### 3.1 Toy model

We adopt a two-site Haken–Strobl Hamiltonian in the single-excitation manifold,

$$
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$

where $\sigma_{z}$ and $\sigma_{x}$ are Pauli operators in the site basis, $\Delta$ is the site-energy difference, and $V$ is the excitonic coupling. The system is subject to pure dephasing at rate $\Gamma$ and a trap on site 2 with rate $\kappa$. The corrected Lindblad dephasing generator is

$$
\mathcal{L}_{\phi}[\rho]=\frac{\Gamma}{2}\left(\sigma_{z}\rho\sigma_{z}-\rho\right),
$$

which damps the off-diagonal density-matrix element $\rho_{12}$ at rate $\Gamma$. (The published version wrote $-\frac{\Gamma}{2}(1-\sigma_{z}^{2}/2)$; since $\sigma_{z}^{2}=\mathbb{1}$, that expression is a multiple of the identity, generates no dephasing, and is corrected here.) The total master equation is

$$
\dot{\rho}=-i[H_{S},\rho]+\mathcal{L}_{\phi}[\rho]+\kappa\,\mathcal{D}_{2}[\rho],
$$

where $\mathcal{D}_{2}[\rho]$ removes population from site 2 at rate $\kappa$.

### 3.2 Re-entry criterion

We define the memory ratio

$$
R=\frac{\tau_{B}}{\tau_{T}},
$$

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the transfer time derived in Section 4.2. Thresholds are set as

- $R\lesssim0.1$: Markovian reduction suffices.
- $0.1<R<0.5$: transitional regime; error estimation required.
- $R\gtrsim0.5$: non-Markovian framework required.

These thresholds are conventions chosen so that the criterion is falsifiable; Section 6 discusses their sensitivity.

### 3.3 Input parameters

| Symbol | Value | Status |
|--------|-------|--------|
| $V$ | $[50,75]\ \mathrm{cm^{-1}}$ | Reported excitonic coupling magnitude for the FMO BChl 3–4 pair (absolute value of the reported $-50$ to $-75\ \mathrm{cm^{-1}}$) [4] |
| $\Delta$ | $[110,180]\ \mathrm{cm^{-1}}$ | Reported transition energy difference for BChl 3–4 [4] |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Assumption (trap rate; no source in the bibliography states this value) |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Assumption (exciton lifetime; no source in the bibliography states this value) |
| $\tau_{B}$ | $[0.1,\,1]\ \mathrm{ps}$ | $\tau_{B}=0.1\ \mathrm{ps}$ is an assumption informed by the sub-100 fs relaxation resolved in single complexes [7]; $\tau_{B}=1\ \mathrm{ps}$ for slow intramolecular modes is an assumption |
| $c$ | $2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}$ | Speed of light for wavenumber-to-frequency conversion |

All parameters are either taken from the cited literature or stated as explicit assumptions. The trap rate and exciton lifetime enter only the single-hop efficiency of Section 4.3, which is therefore an assumption-based ceiling rather than a measured quantity.

## 4. Analysis

### 4.1 Optimal dephasing rate

In the strong-disorder limit $V\ll\Delta$, the Haken–Strobl hopping rate under pure dephasing $\Gamma$ is

$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$

This is the standard adiabatic-elimination result: the dephasing-broadened linewidth of each site is $\Gamma$, and the transfer rate between two sites detuned by $\Delta$ follows a Lorentzian overlap. Setting $\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=0$:

$$
\frac{\mathrm{d}}{\mathrm{d}\Gamma}\left(\frac{2V^{2}\Gamma}{\Gamma^{2}+\Delta^{2}}\right)
=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-\Gamma\cdot 2\Gamma}{(\Gamma^{2}+\Delta^{2})^{2}}
=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}.
$$

The numerator vanishes at $\Gamma^{2}=\Delta^{2}$, and since $\Gamma>0$,

$$
\Gamma^{*}=\Delta.
$$

The second derivative at $\Gamma^{*}$ is negative ($\Delta^{2}-\Gamma^{2}$ changes sign from positive to negative as $\Gamma$ crosses $\Delta$), confirming a maximum. Thus the optimal dephasing rate equals the energetic disorder, which is the two-site expression of the broadened-overlap mechanism identified for general networks in [8].

### 4.2 Transfer time

Substituting $\Gamma^{*}$ into $k(\Gamma)$ gives the optimal hopping rate

$$
k^{*}=k(\Gamma^{*})=\frac{2V^{2}\Delta}{2\Delta^{2}}=\frac{V^{2}}{\Delta}.
$$

A wavenumber $k^{*}$ in $\mathrm{cm^{-1}}$ corresponds to an ordinary frequency $c\,k^{*}$ in $\mathrm{s^{-1}}$ and to an angular frequency $\omega^{*}=2\pi c\,k^{*}$. Taking the transfer time as the inverse angular frequency,

$$
\tau_{T}=\frac{1}{\omega^{*}}=\frac{\Delta}{2\pi c V^{2}}.
$$

**Dimensional check.** $[\Delta]=\mathrm{cm^{-1}}$, $[c]=\mathrm{cm\,s^{-1}}$, $[V^{2}]=(\mathrm{cm^{-1}})^{2}$, so

$$
\left[\frac{\Delta}{2\pi cV^{2}}\right]=\frac{\mathrm{cm^{-1}}}{\mathrm{cm\,s^{-1}}\cdot(\mathrm{cm^{-1}})^{2}}=\mathrm{s}.
$$

The formula is dimensionally consistent. The published expression $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$ carries units $\mathrm{J\,s}\cdot\mathrm{cm^{-1}}/(\mathrm{cm\,s^{-1}}\cdot(\mathrm{cm^{-1}})^{2})=\mathrm{J\,s\,cm}$, which is not a time; it is corrected here.

**Representative point.** $(V,\Delta)=(50,110)\ \mathrm{cm^{-1}}$:

$$
V^{2}=50^{2}=2500\ \mathrm{(cm^{-1})^{2}},
$$
$$
2\pi c V^{2}=2\pi\times2.9979\times10^{10}\times2500=4.709