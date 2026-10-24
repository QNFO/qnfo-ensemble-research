# Re-Entry of Non-Markovian Boson-Mediated Transport into Light-Harvesting Complexes: A Timescale-Based Applicability Analysis

## Abstract

Photosynthetic antennae achieve near-unity excitation-energy-transfer (EET) efficiency on sub-picosecond timescales, yet modelers must decide whether to allocate expensive non-Markovian boson-mediated simulations or inexpensive Markovian dephasing master equations. Earlier applicability tests used parameter ranges broader than experimentally reported values, a dimensionally inconsistent transfer-time expression, and an incorrect Lindblad dephasing generator, and one version cited an urban-transport study as an analogy it does not support. We adopt the experimentally reported excitonic coupling magnitude $V\in[50,75]\ \mathrm{cm^{-1}}$ and site-energy difference $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ for the FMO bacteriochlorophyll 3–4 dimer, use the dimensionally correct transfer time $\tau_{T}=\Delta/(2\pi cV^{2})$, and use the correct pure-dephasing generator $\mathcal{L}_{\phi}[\rho]=-(\Gamma/2)[\sigma_{z},[\sigma_{z},\rho]]$. From these we derive the optimal dephasing rate $\Gamma^{*}=\Delta$, the optimal hopping rate $k^{*}=V^{2}/\Delta\in[13.89,51.14]\ \mathrm{cm^{-1}}$, a transfer-time interval $\tau_{T}\in[0.1038,0.3822]\ \mathrm{ps}$, a single-hop trapping efficiency $\eta=0.999001$, and memory-ratio windows $R_{\mathrm{fast}}\in[0.26,0.96]$ for a fast bath ($\tau_{B}=0.1\ \mathrm{ps}$) and $R_{\mathrm{slow}}\in[2.6,9.6]$ for a slow bath ($\tau_{B}=1\ \mathrm{ps}$). All realistic slow-mode scenarios therefore lie in the non-Markovian sector, while fast baths occupy a transitional window. We further state a falsifiable hypothesis that the relative shift of the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\approx R$ for $R\gtrsim0.5$. The memory-ratio rule gives modelers a quantitative, analytically derived guideline for allocating computational effort in EET modeling.

## 1. Introduction

Designers of bio-inspired photovoltaic devices and researchers interpreting ultrafast spectroscopic data both confront a concrete methodological choice: allocate high-performance-computing resources to a non-Markovian boson-mediated description that retains bath memory, or adopt a Markovian dephasing master equation that discards memory at negligible cost. The former approach can require on the order of $10^{4}$ CPU-hours (order-of-magnitude estimate) for a seven-site FMO simulation, while the latter can be executed on a laptop in minutes. An incorrect choice either wastes computational budget or yields quantitatively inaccurate transfer rates and optimal dephasing conditions, potentially leading to sub-optimal device designs or misinterpretation of experimental observables. A decision rule that predicts when memory effects are essential would reduce unnecessary computation and improve the reliability of modeling outcomes.

Two-decade-old theory shows that environmental dephasing can assist transport: noise enables energy transfer with efficiencies well above 90% across the FMO complex within a fully Markovian treatment [2], and the same mechanism has been analyzed in dissipative networks where dephasing suppresses destructive interference and broadens spectral lines to enhance site overlap [8]. Ultrafast single-molecule pump–probe spectroscopy resolves energy relaxation in individual light-harvesting complexes on sub-100-fs to picosecond timescales, motivating the assignment of a fast solvent-like bath correlation time $\tau_{B}=0.1\ \mathrm{ps}$ as a working assumption [7]. Atomistic and spectroscopic studies of the FMO bacteriochlorophyll 3–4 pair report a transition-energy difference of about 110 to 180 $\mathrm{cm^{-1}}$ and a negative excitonic coupling with magnitudes from about 50 to 75 $\mathrm{cm^{-1}}$ [4]; these reported ranges define the parameter box used here. Atomistic simulations of the full green-sulfur-bacterial light-harvesting apparatus show that energy funneled from chlorosome through baseplate and FMO to the reaction center converges within an overall timescale of 10 ps regardless of initial conditions [5], which bounds the regime in which single-step transfer times matter. Nuclear quantum effects have been shown to slow energy transfer by up to a factor of two relative to classical treatments of the vibrational motion [6], reinforcing the need to know when a classical or Markovian treatment suffices.

This paper corrects three errors that appeared in the published version under revision. First, the sensitivity analysis there described $V\in[20,75]\ \mathrm{cm^{-1}}$ as "the full experimentally reported range"; the reported range is $[50,75]\ \mathrm{cm^{-1}}$ [4], and the wider interval inflated the apparent sensitivity of the memory ratio. Second, the published transfer-time expression $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$ is dimensionally inconsistent; the correct expression is $\tau_{T}=\Delta/(2\pi cV^{2})$, as we verify dimensionally in Section 4.2. Third, the published Lindblad dephasing term $-(\Gamma/2)(1-\sigma_{z}^{2}/2)$ reduces to a multiple of the identity and generates no dephasing; the correct generator is $-(\Gamma/2)[\sigma_{z},[\sigma_{z},\rho]]$ (Section 3.1). We also retract the published claim that an urban-transportation study mirrors the memory-ratio sensitivity result: that work develops an overlap-census method for city transport networks and reports clusters of cities by mobility profile [3], and it contains no quantum-transport analogy.

**Contributions.**
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two-site Haken–Strobl model with the corrected dephasing generator, with numerical evaluation over the reported parameter box (Section 4.1).
2. Dimensional verification of the corrected transfer-time formula $\tau_{T}=\Delta/(2\pi cV^{2})$ and evaluation at the corners of the reported box, yielding $\tau_{T}\in[0.1038,0.3822]\ \mathrm{ps}$ (Section 4.2).
3. Computation of the single-hop trapping-limited efficiency $\eta=0.999001$ from assumed trap and recombination rates (Section 4.3).
4. Exhaustive computation of memory ratios over the reported box, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, and the resulting regime classification (Section 4.4).
5. A falsifiable hypothesis that the non-Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\approx R$ for $R\gtrsim0.5$, together with the conditions under which the claim would fail (Sections 5 and 6).

## 2. Background and Related Work

**Noise-assisted transport in FMO.** Reference [2] provides physically intuitive mechanisms for the effect of noise on excitation energy transfer in networks and shows, using a hybrid basis of excitons and sites, how dephasing enables energy transfer with efficiencies well above 90% across the FMO complex. Its network model treats the pigment–protein complex as sites with local energies $\hbar\omega_{j}$ and coherent tunneling amplitudes $v_{j,l}$, one site connected to the reaction center [2]. This establishes the practical relevance of dephasing-assisted transport and supplies the modeling frame in which our two-site reduction sits.

**Fundamental mechanisms of dephasing-assisted transport.** Reference [8] analyzes a fully connected network with equal hopping strengths and finds exact analytical solutions for the density matrix; in the absence of dissipation and dephasing, destructive interference limits the total transfer to the sink to $p_{\mathrm{sink}}(\infty)=1/(N-1)$. Its concluding analysis identifies the suppression of destructive interference by dephasing noise and the dephasing-broadened overlap between sites as the key mechanisms [8]. Our optimal-dephasing condition $\Gamma^{*}=\Delta$ is the two-site instance of this general mechanism.

**Reported FMO dimer parameters.** Reference [4] studies a vibronic heterodimer with parameters chosen to mimic the FMO complex and states that the transition-energy difference between bacteriochlorophylls 3 and 4 is proposed to be from about 110 to 180 $\mathrm{cm^{-1}}$, with a negative excitonic coupling from about $-50$ to $-75\ \mathrm{cm^{-1}}$; it also reports vibrational modes near 180 $\mathrm{cm^{-1}}$ with total Huang–Rhys factor 0.03 in the lowest-energy bacteriochlorophyll. These reported ranges define the parameter box $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ used throughout this paper, replacing the wider and unsupported interval $V\in[20,75]\ \mathrm{cm^{-1}}$ of the published version. The same work finds that for negative coupling most oscillator strength resides in an essentially electronic transition, so vibronic mixing does not drastically reshape the absorption spectrum in this regime [4], which supports treating the electronic dimer as the leading model.

**Atomistic energy funneling and timescales.** Reference [5] builds an atomistic model of the complete light-harvesting apparatus of green sulfur bacteria — 3988 pigments spanning chlorosome, baseplate, and six FMO trimers — solves a quantum master equation including coherent, dephasing, and relaxation processes, and finds that energy funneled to the reaction center converges within an overall timescale of 10 ps regardless of the initiating conditions. This 10 ps convergence bound contextualizes our single-step transfer times of 0.1–0.4 ps: many transfer steps fit inside the funneling time, so per-step accuracy compounds.

**Nuclear quantum effects.** Reference [6] compares classical and quantum treatments of vibrational motion in LH2, FMO, and LHCII at 300 K and concludes that the main difference is not the direction of energy flow but the rate: the transfer rate is generally overestimated classically, with the quantum effect on the rate bounded by less than a factor of two for biologically relevant parameters. This bounds the size of quantum-vibrational corrections our Markovian baseline may miss and motivates the error-tolerance threshold used in our falsification condition.

**Ultrafast single-complex spectroscopy.** Reference [7] applies a single-molecule pump–probe technique to LH2 and demonstrates that ultrafast energy relaxation can be observed in individual complexes, with relaxation-time distributions explained by energetic disorder of the pigments. Single-complex resolution of sub-picosecond relaxation motivates our working assumption of a fast solvent-like bath correlation time $\tau_{B}=0.1\ \mathrm{ps}$, which we state explicitly as an assumption of this paper rather than a measured quantity.

**Coherence and vibronic coupling in Photosystem II.** Reference [11] reviews quantum coherence in PSII light harvesting and records that two-dimensional electronic spectroscopy reveals oscillatory cross-peak signals lasting 300–660 fs at physiological temperatures in FMO, with the current consensus that vibronic (mixed electronic-vibrational) coherence is the dominant observable at room temperature, and that underdamped intramolecular modes in the 200–500 $\mathrm{cm^{-1}}$ range can produce similar spectroscopic signatures. These fs-scale coherence lifetimes are comparable to our derived transfer times, which is precisely the regime where the memory ratio $R$ approaches unity and the Markovian reduction becomes questionable.

**Boson-mediated non-Markovian framework.** Reference [10] proposes a "boson–fermion signaling" framework in which structured phonon fields direct excitons through the energy landscape, formulated as a non-Markovian Hamiltonian formalism, and reports simulated transfer efficiencies above 95%. This is the expensive framework whose applicability our memory-ratio rule is designed to test; our analysis supplies the timescale criterion under which deploying it is warranted.

**A cautionary note on analogies.** Reference [3] develops an overlap-census method that extracts a multimodal profile from a city's multiplex transportation network and applies it to 15 cities, finding six clusters that explain more than 90% of the variance. The published version of this paper cited [3] as mirroring the memory-ratio sensitivity result; that claim is retracted. The work concerns urban mobility and contains no statement about quantum transport or any memory-ratio metric, and no part of our derivation relies on it.

**Dimensional consistency in transport modeling.** Reference [1] analyzes transient thermal grating experiments, in which a spatially periodic excitation probes heat-transport dynamics at small spatiotemporal scales, and emphasizes that quantitative interpretation of the measured transient requires a forward model that consistently connects energy deposition, transport, and detection. The same discipline of dimensional and operator-level consistency applies to the transfer-time formula corrected here: a formula that mixes wavenumbers, angular frequencies, and $\hbar$ without conversion produces errors of order $2\pi$ or of $\hbar$'s units, which is exactly the class of error fixed in Section 4.2.

## 3. Methods

### 3.1 Toy model and corrected dephasing dissipator

We consider the two-site Haken–Strobl Hamiltonian in the single-excitation manifold,

$$
H_{S}=\frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$

where $\sigma_{x},\sigma_{z}$ are Pauli matrices on the two-site basis, $\Delta$ is the site-energy difference, and $V$ is the excitonic coupling. Site 2 carries a trap with rate $\kappa$.

The correct pure-dephasing Lindblad generator with jump operator $\sigma_{z}$ is

$$
\mathcal{L}_{\phi}[\rho]=-\frac{\Gamma}{2}\,[\sigma_{z},[\sigma_{z},\rho]],
$$

which leaves populations invariant and damps the coherence as $\dot{\rho}_{12}=-2\Gamma\,\rho_{12}$. This form replaces the defective term $-(\Gamma/2)(1-\sigma_{z}^{2}/2)$ of the published version: since $\sigma_{z}^{2}=\mathbb{1}$, that expression equals $-(\Gamma/4)\mathbb{1}$, a multiple of the identity that generates no dephasing at all. All downstream results of the published derivation that depended on the defective generator are rederived here with the corrected one.

### 3.2 Re-entry criterion

The memory ratio is defined as

$$
R=\frac{\tau_{B}}{\tau_{T}},
$$

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the intrinsic single-hop transfer time (Section 4.2). Thresholds are conventions chosen to render the criterion falsifiable:

- $R\lesssim0.1$: Markovian reduction suffices.
- $0.1<R<0.5$: Transitional regime; error estimation required.
- $R\gtrsim0.5$: Non-Markovian framework required.

### 3.3 Input parameters

| Symbol | Value | Source / status |
|--------|-------|-----------------|
| $V$ | $[50,75]\ \mathrm{cm^{-1}}$ | Reported in [4] (magnitudes of $-50$ to $-75$) |
| $\Delta$ | $[110,180]\ \mathrm{cm^{-1}}$ | Reported in [4] |
| $\kappa$ | $1\ \mathrm{ps^{-1}}$ | Assumption of this paper |
| $\tau_{e}$ | $1\ \mathrm{ns}$ | Assumption of this paper |
| $\tau_{B}$ | $0.1\ \mathrm{ps}$ (fast) and $1\ \mathrm{ps}$ (slow) | Assumptions; fast value motivated by the sub-100-fs relaxation resolved in [7] |
| $c$ | $2.9979\times10^{10}\ \mathrm{cm\,s^{-1}}$ | Defined constant for unit conversion |

All parameters are either taken from the cited literature or explicitly labeled as assumptions of this paper.

## 4. Analysis

### 4.1 Optimal dephasing rate and hopping rate

In the strong-disorder limit $V\ll\Delta$, adiabatic elimination of the coherences in the Haken–Strobl master equation with the corrected pure-dephasing generator yields the hopping rate

$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$

Differentiating with respect to $\Gamma$:

$$
\frac{dk}{d\Gamma}=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-2\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}
=2V^{2}\,\frac{\Delta^{2}-\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}.
$$

Setting the derivative to zero gives $\Delta^{2}-\Gamma^{2}=0$, i.e.

$$
\Gamma^{*}=\Delta.
$$

Substituting $\Gamma^{*}$ back into $k(\Gamma)$:

$$
k^{*}=k(\Gamma^{*})=\frac{2V^{2}\Delta}{\Delta^{2}+\Delta^{2}}=\frac{V^{2}}{\Delta}.
$$

**Numerical range of $k^{*}$.** Evaluating $k^{*}=V^{2}/\Delta$ at the four corners of the reported box:

| Corner | $V$ ($\mathrm{cm^{-1}}$) | $\Delta$ ($\mathrm{cm^{-1}}$) | $k^{*}=V^{2}/\Delta$ ($\mathrm{cm^{-1}}$) |
|--------|-------|-------|---------|
| 1 (min $V$, max $\Delta$) | 50 | 180 | $2500/180=13.8889$ |
| 2 (min $V$, min $\Delta$) | 50 | 110 | $2500/110=22.7273$ |
| 3 (max $V$, max $\Delta$) | 75 | 180 | $5625/180=31.2500$ |
| 4 (max $V$, min $\Delta$) | 75 | 110 | $5625/110=51.1364$ |

Thus

$$
k^{*}\in[13.89,\,51.14]\ \mathrm{cm^{-1}}.
$$

### 4.2 Transfer time $\tau_{T}$

The optimal hopping rate $k^{*}$ has units of wavenumber ($\mathrm{cm^{-1}}$). Converting to angular frequency $\omega^{*}=2\pi c\,k^{*}=2\pi c\,V^{2}/\Delta$, the transfer time is the inverse:

$$
\tau_{T}=\frac{1}{\omega^{*}}=\frac{\Delta}{2\pi cV^{2}}.
$$

**Dimensional check.** $[\Delta]=\mathrm{cm^{-1}}$; $[cV^{2}]=\mathrm{cm\,s^{-1}}\cdot\mathrm{cm^{-2}}=\mathrm{cm^{-1}\,s^{-1}}$; hence $[\Delta/(2\pi cV^{2})]=\mathrm{cm^{-1}}/(\mathrm{cm^{-1}\,s^{-1}})=\mathrm{s}$. The expression is dimensionally a time. The published expression $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$ carries an extra factor of action ($\mathrm{J\,s}$) and is dimensionally inconsistent; it is discarded.

**Extremal transfer times.** Maximum $\tau_{T}$ (smallest $V$, largest $\Delta$): $V=50$, $\Delta=180$:

$$
\begin{aligned}
\tau_{T}^{\max} &= \frac{180}{2\pi c\cdot 50^{2}}
= \frac{180}{2\pi\times2.9979\times10^{10}\times2500}
= \frac{180}{4.70913\times10^{14}} \\
&= 3.8223\times10^{-13}\ \mathrm{s}=0.3822\ \mathrm{ps}.
\end{aligned}
$$

Minimum $\tau_{T}$ (largest $V$, smallest $\Delta$): $V=75$, $\Delta=110$:

$$
\begin{aligned}
\tau_{T}^{\min} &= \frac{110}{2\pi c\cdot 75^{2}}
= \frac{110}{2\pi\times2.9979\times10^{10}\times5625}
= \frac{110}{1.05955\times10^{15}} \\
&= 1.0382\times10^{-13}\ \mathrm{s}=0.1038\ \mathrm{ps}.
\end{aligned}
$$

Hence

$$
\tau_{T}\in[0.1038,\,0.3822]\ \mathrm{ps}.
$$

### 4.3 Trapping-limited efficiency $\eta$

The recombination rate is

$$
\gamma_{\mathrm{rec}}=\frac{1}{\tau_{e}}=\frac{1}{1\ \mathrm{ns}}=10^{-3}\ \mathrm{ps^{-1}}.
$$

The single-hop trapping efficiency for a trap rate $\kappa$ and recombination $\gamma_{\mathrm{rec}}$ is

$$
\eta=\frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}
=\frac{1}{1+10^{-3}}
=\frac{1}{1.001}
=0.999001.
$$

### 4.4 Memory ratio $R$ and regime classification

Using the bounds for $\tau_{T}$:

$$
R_{\mathrm{fast}}=\frac{0.1\ \mathrm{ps}}{\tau_{T}}\in\left[\frac{0.1}{0.3822},\frac{0.1}{0.1038}\right]=[0.2616,\,0.9634],
$$

$$
R_{\mathrm{slow}}=\frac{1\ \mathrm{ps}}{\tau_{T}}\in\left[\frac{1}{0.3822},\frac{1}{0.1038}\right]=[2.6166,\,9.6339].
$$

Rounding to two significant figures gives

$$
R_{\mathrm{fast}}\in[0.26,0.96],\qquad R_{\mathrm{slow}}\in[2.6,9.6].
$$

All $R_{\mathrm{slow}}$ values exceed the 0.5 threshold, placing every realistic slow-mode bath in the non-Markovian sector. Fast baths fall below 0.5 only for the smallest $V$ and largest $\Delta$, leaving a transitional window. Note that the published abstract's claim that $R$ spans 0.17–1.70 is incorrect: it followed from the erroneous $V\in[20,75]\ \mathrm{cm^{-1}}$ box and the dimensionally flawed transfer-time formula. With the reported box $V\in[50,75]\ \mathrm{cm^{-1}}$ [4] and the corrected formula, the windows above are the correct ones.

### 4.5 Sensitivity of the classification to the reported box

Because $R=\tau_{B}\,2\pi cV^{2}/\Delta$ is monotone increasing in $V$ and decreasing in $\Delta$, the extremes of $R$ over the box occur at the corners already evaluated; no interior extremum exists. The classification is therefore robust over the full reported range: $R_{\mathrm{slow}}>0.5$ for every corner, and $R_{\mathrm{fast}}<0.5$ only at the corner $(V,\Delta)=(50,180)$, where $R_{\mathrm{fast}}=0.2616$. Narrowing the box from the erroneous $[20,75]\ \mathrm{cm^{-1}}$ to the reported $[50,75]\ \mathrm{cm^{-1}}$ removes the spurious low-$V$ tail that produced the published claim of $R$ values down to 0.17.

## 5. Results

All numerical values follow directly from the derivations in Section 4.

1. **Optimal dephasing rate:** $\Gamma^{*}=\Delta$, ranging from 110 to 180 $\mathrm{cm^{-1}}$.
2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from 13.89 to 51.14 $\mathrm{cm^{-1}}$.
3. **Transfer time:** $\tau_{T}\in[0.1038,0.3822]\ \mathrm{ps}$, with corner values 0.1038 ps (min) and 0.3822 ps (max).
4. **Single-hop efficiency:** $\eta=0.999001$.
5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$.
6. **Sensitivity:** $R_{\mathrm{slow}}$ always exceeds 0.5; $R_{\mathrm{fast}}$ falls below 0.5 only for $V=50\ \mathrm{cm^{-1}}$ and $\Delta=180\ \mathrm{cm^{-1}}$.

**Hypothesis (projection).** If $R\gtrsim0.5$, the non-Markovian framework is expected to shift the optimal dephasing rate by $\delta\Gamma^{*}$ with

$$
\frac{\delta\Gamma^{*}}{\Gamma^{*}}\approx R,
$$

with a proportionality constant of order unity and an uncertainty factor of two. This is a hypothesis stated for falsification, not a derived result; it is consistent in spirit with the finding that quantum-vibrational corrections to transfer rates are bounded by less than a factor of two in biologically relevant regimes [6], and it can be tested by full-scale non-Markovian simulations of the seven-site FMO Hamiltonian.

## 6. Discussion

### Limitations

- **Two-site abstraction.** Real light-harvesting complexes contain multiple pigments, static disorder, and multiple pathways; the single-hop efficiency $\eta$ therefore represents an upper bound, and the atomistic funneling study shows that full-apparatus transfer converges only on a 10 ps timescale [5], far longer than a single hop.
- **Threshold conventions.** The $R$ thresholds are chosen for falsifiability; alternative thresholds would shift the transitional window but not the qualitative conclusion that slow vibrational modes demand a non-Markovian treatment.
- **Weak-coupling assumption.** The Haken–Strobl rate formula assumes $V\ll\Delta$ and weak system–bath coupling; strong coupling would invalidate the analytic $k(\Gamma)$ expression and require the exact non-Markovian treatment.
- **Assumed bath times.** Both $\tau_{B}=0.1\ \mathrm{ps}$ and $\tau_{B}=1\ \mathrm{ps}$ are assumptions; only the fast value is motivated by analogy with the sub-100-fs relaxation resolved in single complexes [7]. The classification of a given real bath depends directly on these assumed values.
- **Vibronic effects excluded.** The reported 180 $\mathrm{cm^{-1}}$ modes with Huang–Rhys factor 0.03 [4] and the fs-scale vibronic coherences documented for FMO [11] are outside the pure-dephasing model; they could modify $\tau_{T}$ and the thresholds.

### Failure modes

1. **Bimodal baths.** A bath comprising both fast and slow components would invalidate a single $\tau_{B}$; a spectral-density-weighted ratio would be needed.
2. **Strong coupling.** If $V$ approached $\Delta$, the denominator $\Gamma^{2}+\Delta^{2}$ would no longer be dominated by $\Delta^{2}$, breaking the optimality condition $\Gamma^{*}=\Delta$.
3. **Resonant vibronic bridges.** Specific vibrational modes acting as resonant bridges could enhance coherent transport beyond the dephasing-based estimate, as the vibronic-coherence review [11] makes plausible for modes in the 200–500 $\mathrm{cm^{-1}}$ range.

### Falsification condition

The central claim — that the boson-mediated framework is required when $R\gtrsim0.5$ — is falsified if a full non-Markovian simulation of a realistic FMO Hamiltonian yields corrections to populations, trapping currents, or the optimal dephasing rate that are smaller than 1% of the corresponding Markovian predictions for $R\ge0.5$. A secondary falsifier of the numerical classification would be a credible revision of the reported dimer parameters outside $V\in[50,75]\ \mathrm{cm^{-1}}$ or $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ [4]: since $R$ is monotone in both, the classification changes if the box moves enough to push $R_{\mathrm{slow}}$ below 0.5, which requires $\tau_{B}/\tau_{T}<0.5$, i.e. $\tau_{T}>2\ \mathrm{ps}$ at $\tau_{B}=1\ \mathrm{ps}$ — a factor of five beyond the largest derived $\tau_{T}$.

### Self-critique

One could argue that the importance of non-Markovian effects is already established by the nuclear-quantum-effect study [6], which shows transfer-rate corrections up to a factor of two; however, importance does not imply that the specific boson-mediated framework of [10] adds predictive value beyond a Markovian master equation, and our rule is designed to test exactly that. The optimal dephasing condition $\Gamma^{*}=\Delta$ recovers, in the two-site limit, the mechanism identified in the fully connected network analysis of [8], where dephasing suppresses destructive interference; the two-site reduction is the weakest link, since interference effects in larger networks have no two-site analogue.

### Open questions

1. What is the exact prefactor linking $\delta\Gamma^{*}$ to $R$?
2. How does the memory-ratio criterion generalize to multi-site networks with path-dependent $\tau_{T}$?
3. Can single-molecule spectroscopy of the type demonstrated in [7] resolve the predicted backflow signatures in individual complexes?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** The primary users are theoretical chemists, biophysicists, and engineers modeling excitation-energy transfer in natural or artificial light-harvesting systems. The memory-ratio rule provides a quantitative decision point: if $\tau_{B}\gtrsim0.5\,\tau_{T}$, allocate resources to implement the non-Markovian boson-mediated framework; otherwise a Markovian master equation suffices.

**(b) Technology readiness.** This work is purely analytical and has not undergone peer review; it resides at Technology Readiness Level 2. Analytical studies never exceed TRL 3.

**(c) Smallest next experiment or calculation.** A full non-Markovian simulation of the seven-site FMO Hamiltonian, with an assumed spectral density consistent with the reported dimer parameters [4], that computes (i) transient population backflow amplitudes and (ii) the shift in the optimal dephasing rate. The hypothesis is falsified if the computed corrections are below 1% of the Markovian predictions for $R\ge0.5$.

**(d) Engineering and computational constraints.**
- **Spectral-density data.** Accurate $\tau_{B}$ requires high-resolution spectral densities from atomistic simulations or ultrafast spectroscopy of the kind demonstrated in [7]; this is the binding data constraint.
- **Computational load.** A realistic FMO simulation using the non-Markovian framework typically requires on the order of $10^{4}$ CPU-hours (order-of-magnitude estimate).
- **Parameter uncertainty.** Variations in $V$ and $\Delta$ must be propagated; the corner analysis of Section 4.5 shows the classification is robust within the reported box but sensitive to any revision of the box itself.

**(e) Order-of-magnitude cost projection (projection).** Assuming a cloud HPC price of \$0.10 per CPU-hour, the minimal full-scale simulation costs

$$
\text{Cost}\approx10^{4}\ \text{CPU-h}\times\$0.10/\text{CPU-h}=\$1{,}000,
$$

with an uncertainty factor of two due to possible variations in parallel efficiency. Both inputs (the $10^{4}$ CPU-hour estimate and the unit price) are assumptions; this figure is a projection, not a measurement.

**(f) Direct risks or misuse paths.** Over-reliance on the memory-ratio rule without verifying the underlying spectral density could lead to unnecessary deployment of the expensive non-Markovian framework, wasting computational resources. Conversely, misclassifying a slow-mode bath as fast could omit essential memory effects, yielding inaccurate design predictions. Clear documentation of the assumptions (single-exponential bath correlation, weak coupling) mitigates these risks.

## 8. Conclusion

We formulated and applied a quantitative timescale-based re-entry test for the non-Markovian boson-mediated transport framework in photosynthetic light-harvesting, correcting three errors of the published version: the parameter box is the reported $V\in[50,75]\ \mathrm{cm^{-1}}$, $\Delta\in[110,180]\ \mathrm{cm^{-1}}$ [4], not the unsupported $[20,75]\