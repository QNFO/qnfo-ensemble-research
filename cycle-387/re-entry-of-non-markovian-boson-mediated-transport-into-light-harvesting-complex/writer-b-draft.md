# Re‑Entry of Non‑Markovian Boson‑Mediated Transport into Light‑Harvesting Complexes: A Timescale‑Based Applicability Analysis (Revised)

## Abstract

Photosynthetic antennae achieve near‑unity excitation‑energy‑transfer (EET) efficiency on sub‑picosecond timescales, yet modelers must decide whether to allocate expensive non‑Markovian boson‑mediated simulations or inexpensive Markovian dephasing master equations. Earlier applicability tests of this decision suffered from three defects: a coupling range ($V\in[20,75]\;\mathrm{cm^{-1}}$) wider than the experimentally reported values, a dimensionally inconsistent transfer‑time expression, and memory‑ratio windows that followed from those errors. This revision adopts the reported FMO BChl 3–4 dimer parameters $|V|\in[50,75]\;\mathrm{cm^{-1}}$ and $\Delta\in[110,180]\;\mathrm{cm^{-1}}$ [4], uses the dimensionally correct transfer time $\tau_{T}=\Delta/(2\pi cV^{2})$, and replaces a defective dephasing generator with the standard Lindblad pure‑dephasing term. The corrected derivations give $\Gamma^{*}=\Delta$, $k^{*}=V^{2}/\Delta\in[13.89,51.14]\;\mathrm{cm^{-1}}$, $\tau_{T}\in[0.1038,0.3822]\;\mathrm{ps}$, a single‑hop trapping efficiency $\eta=0.999001$, and memory‑ratio windows $R_{\mathrm{fast}}\in[0.26,0.96]$ for $\tau_{B}=0.1\;\mathrm{ps}$ and $R_{\mathrm{slow}}\in[2.6,9.6]$ for $\tau_{B}=1\;\mathrm{ps}$. Every realistic slow‑mode scenario therefore lies in the non‑Markovian sector ($R\gtrsim0.5$), while fast solvent‑like baths occupy a transitional window rather than a uniformly Markovian one. A falsifiable projection $\delta\Gamma^{*}/\Gamma^{*}\approx R$ for the shift of the optimal dephasing rate is stated with its test condition.

## 1. Introduction

Designers of bio‑inspired photovoltaic devices and researchers interpreting ultrafast spectroscopic data both confront a concrete methodological choice: allocate high‑performance‑computing resources to a non‑Markovian boson‑mediated description that retains bath memory, or adopt a Markovian dephasing master equation that discards memory at negligible cost. The former approach can require on the order of $10^{4}$ CPU‑hours (order‑of‑magnitude estimate) for a seven‑site FMO simulation, while the latter can be executed on a laptop in minutes. An incorrect choice either wastes computational budget or yields quantitatively inaccurate transfer rates and optimal dephasing conditions, potentially leading to sub‑optimal device designs or misinterpretation of experimental observables. A decision rule that predicts when memory effects are essential would therefore reduce unnecessary computation and improve the reliability of modelling outcomes.

The published version of this analysis contained errors that materially changed its numerical conclusions, and each is corrected here after verification against the paper's own derivations and its sources. First, the sensitivity analysis claimed that $V\in[20,75]\;\mathrm{cm^{-1}}$ is "the full experimentally reported range"; the atomistic and spectroscopic literature reports excitonic couplings between $-50$ and $-75\;\mathrm{cm^{-1}}$ for the FMO BChl 3–4 dimer [4], so the lower bound $20\;\mathrm{cm^{-1}}$ has no reported support and the box is narrowed to $|V|\in[50,75]\;\mathrm{cm^{-1}}$. Second, Section 4.5 of the published version stated $\tau_{T}=\hbar\Delta/(2\pi cV^{2})$; the factor $\hbar$ is dimensionally inconsistent when $\Delta$ and $V$ are given as wavenumbers, and the corrected expression is $\tau_{T}=\Delta/(2\pi cV^{2})$, verified dimensionally below. Third, the abstract reported a single memory‑ratio span $R=0.17\text{–}1.70$ and described "fast baths in a transitional window" without the two‑bath decomposition; the corrected windows are $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, and the transitional character of fast baths survives but is now quantified corner by corner. Fourth, Section 6.2 cited an urban‑transportation multiplex‑network study [3] as mirroring the $R$‑sensitivity result; that work analyses bicycle, street and rail layers of cities with an overlap‑census method and contains no quantum‑transport content, so the citation is retracted as support and retained only as a documented negative case. Fifth, the Lindblad dephasing term was written as $-(\Gamma/2)(1-\sigma_z^{2}/2)$, which reduces to a multiple of the identity and generates no dephasing; the correct generator is $-(\Gamma/2)[\sigma_z,[\sigma_z,\rho]]$.

Two‑decade‑old theory shows that environmental dephasing can assist transport, raising EET efficiencies above $90\%$ in the FMO complex within a fully Markovian treatment [2]. Ultrafast single‑molecule pump–probe spectroscopy resolves energy relaxation in single light‑harvesting complexes on the sub‑100‑fs scale, motivating the assignment of a fast solvent‑like bath correlation time $\tau_{B}=0.1\;\mathrm{ps}$ [7]. Atomistic and spectroscopic parameter sets report $|V|$ between 50 and $75\;\mathrm{cm^{-1}}$ and $\Delta$ between 110 and $180\;\mathrm{cm^{-1}}$ for the BChl 3–4 dimer [4]. These grounded ranges define a realistic parameter box narrower than the ranges used in the earlier applicability analysis [9]. Transient‑thermal‑grating theory emphasises that forward models must connect energy deposition, transport and detection consistently, motivating our insistence on dimensional consistency in the transfer‑time expression [1].

**Contributions.**
1. Derivation of the optimal dephasing rate $\Gamma^{*}=\Delta$ and optimal hopping rate $k^{*}=V^{2}/\Delta$ for the two‑site Haken–Strobl model with the corrected dephasing generator (Section 4.1).
2. Correction of the transfer‑time formula to $\tau_{T}=\Delta/(2\pi cV^{2})$, dimensional verification, and evaluation at the four corners of the experimental box, yielding $\tau_{T}\in[0.1038,0.3822]\;\mathrm{ps}$ (Section 4.2).
3. Computation of the single‑hop trapping‑limited efficiency $\eta=0.999001$ from assumed trap and recombination rates (Section 4.3).
4. Exhaustive calculation of memory ratios over the corrected experimental box, giving $R_{\mathrm{fast}}\in[0.26,0.96]$ and $R_{\mathrm{slow}}\in[2.6,9.6]$, replacing the erroneous span $0.17\text{–}1.70$ (Section 4.4).
5. A corner‑by‑corner sensitivity analysis showing that the classification is monotone over the reported box, with the single transitional corner identified explicitly (Section 4.5).
6. A falsifiable projection that the non‑Markovian correction to the optimal dephasing rate scales as $\delta\Gamma^{*}/\Gamma^{*}\approx R$ for $R\gtrsim0.5$, together with its refutation condition (Sections 5 and 6).

## 2. Background and Related Work

**Noise‑assisted transport in FMO.** Reference [2] provides physically intuitive mechanisms for dephasing‑assisted transport (DAT) in networks and shows, using a hybrid exciton–site basis, how noise enables energy transfer with efficiencies well above $90\%$ across the FMO complex. Its network model treats the coherent tunnelling amplitudes $v_{j,l}$ as free parameters, and its conclusion states that any noise model that enhances transport must suppress the inefficient pathways and enhance direct relaxation channels. This establishes the practical relevance of dephasing for light harvesting and fixes the Markovian baseline against which a non‑Markovian framework must demonstrate added value.

**Fundamental mechanisms in fully connected networks.** Reference [8] analyses the fully connected network (FCN) with equal hopping strengths $\hbar v_{j,l}=J$ and finds an exact analytical solution for the density matrix of arbitrarily large uniform networks; in the noiseless case the total transferred population is the striking result $p_{\mathrm{sink}}(\infty)=1/(N-1)$, a consequence of destructive interference. Its concluding remarks identify the suppression of destructive interference by dephasing noise and the dephasing‑broadened overlap between sites as the key mechanisms of noise‑assisted transport. In the two‑site limit these mechanisms reduce to the optimality condition $\Gamma^{*}=\Delta$ derived in Section 4.1, so [8] supplies the multi‑site context for our analytic result.

**Vibronic dimer parameters for FMO.** Reference [4] formulates a vibronic heterodimer with parameters chosen to mimic the FMO complex and reports, on the basis of earlier spectroscopic Hamiltonian determinations, that the transition energy difference between BChl 3 and 4 lies between about 110 and $180\;\mathrm{cm^{-1}}$ and that the excitonic coupling is negative with values from about $-50$ to $-75\;\mathrm{cm^{-1}}$. The same source reports vibrational modes near $180\;\mathrm{cm^{-1}}$ in the FMO lowest‑energy BChl with a total Huang–Rhys factor of 0.03. These are the numbers that define the corrected experimental box used throughout this paper, and they directly refute the $V\in[20,75]\;\mathrm{cm^{-1}}$ range of the published version. Reference [4] also finds that for negative coupling most oscillator strength resides in a transition of essentially electronic character, and that Huang–Rhys factors extracted from fluorescence may need corrections as large as $100\%$ — a caution we carry into the limitation on vibronic effects.

**Atomistic energy funneling.** Reference [5] builds an atomistic model of the entire light‑harvesting apparatus of green sulfur bacteria — 3988 pigments spanning chlorosome rolls, a 64‑site baseplate and six FMO trimers — and solves a quantum master equation including coherent, dephasing and relaxation processes. Its conclusion reports that resonant energy transfer is maximised by the multichromophoric excitonic couplings arising from the molecular arrangement, that initial‑condition scenarios differ qualitatively only within 500 fs, and that all scenarios converge within the overall 10 ps funneling timescale. This 10 ps system‑level timescale is two orders of magnitude longer than the single‑hop times derived here, which justifies treating a single dimer hop as the elementary event in the memory‑ratio construction.

**Nuclear quantum effects on rates.** Reference [6] compares classical and quantum treatments of vibrational motion in LH2, FMO and LHCII at $300\;\mathrm{K}$ using a mixed quantum–classical theory. Its discussion concludes that the main difference is not the direction of energy flow but the rate: classical vibrational treatment generally overestimates the transfer rate, the quantum correction is benign (less than a factor of 2) in biologically relevant regimes, and vibronic renormalisation via a VPT captures the effect. This factor‑of‑2 bound is the scale we adopt for the uncertainty of the projected non‑Markovian correction in Section 5, and it also bounds how far a purely classical bath description could mislead the Markovian baseline.

**Ultrafast bath correlation times.** Reference [7] applies a single‑molecule pump–probe (SM2P) technique to LH2 complexes and demonstrates that ultrafast energy relaxation can be observed in individual light‑harvesting complexes, with the fastest processes in the sub‑100‑fs range; the relaxation‑time distribution shifts with excitation wavelength and is explained numerically by energetic disorder of the pigments. The sub‑100‑fs relaxation scale motivates our fast‑bath assignment $\tau_{B}=0.1\;\mathrm{ps}$, and the single‑complex capability suggests the experimental route by which predicted memory signatures could eventually be resolved.

**Transient‑thermal‑grating consistency.** Reference [1] studies transient thermal grating (TTG) dynamics and argues that quantitative interpretation of the measured transient requires a forward model that consistently connects energy deposition, subsequent heat transport, and detection across transport regimes. Although TTG concerns heat rather than excitons, the methodological point transfers directly: a model that mixes units — as the published $\hbar\Delta/(2\pi cV^{2})$ expression did — cannot support a quantitative applicability test. Our dimensional verification in Section 4.2 follows the standard this source sets.

**Urban multiplex networks: a documented negative case.** Reference [3] proposes an overlap‑census method that extracts a multimodal profile from a city's multiplex transportation network, applies it to 15 cities, and finds six k‑means clusters explaining more than $90\%$ of the variance, separating active‑mobility from car‑centric cities. The work contains no quantum dynamics, no bath correlation times and no memory metric; the published version's claim that it "mirrors" the $R$‑sensitivity result is therefore retracted. We retain the citation to document the retraction explicitly, so that the analogy is not silently reintroduced in later versions.

**Prior applicability analysis.** The earlier version of this study [9] employed broader parameter ranges, the dimensionally inconsistent transfer‑time formula, and a single memory‑ratio span; the present work corrects those issues, narrows the parameter box to the reported values of [4], and replaces the defective dephasing generator. Where the earlier conclusions survive the corrections — notably the placement of slow baths in the non‑Markovian sector — they are kept and now rest on correct arithmetic.

**Boson‑mediated non‑Markovian framework.** Reference [10] proposes a "boson–fermion signalling" framework in which structured phonon fields direct excitonic transport through the energy landscape, formulated as a non‑Markovian Hamiltonian dynamics, and reports simulated transfer efficiencies above $95\%$ attributed to resonantly tuned phonon guidance. This is the expensive framework whose applicability the memory‑ratio rule is designed to test: the rule predicts when its retention of bath memory should change predictions relative to a Markovian dephasing master equation, and Section 6 states what simulation outcome would falsify that prediction.

**Vibronic coherence in photosystem II.** Reference [11] reviews quantum coherence in PSII light harvesting and records that 2DES experiments on FMO show oscillatory cross‑peak signals lasting $300\text{–}660$ fs at physiological temperatures, that underdamped intramolecular modes in the $200\text{–}500\;\mathrm{cm^{-1}}$ range can produce similar spectroscopic signatures, and that LHCII coherence lifetimes of about 200 fs at 293 K exceed individual transfer‑step timescales. These coherence lifetimes bracket the $\tau_{T}$ interval derived in Section 4.2 from above, which is precisely the condition under which bath memory can matter; the review also supplies the Förster‑regime scale $k_{B}T\approx200\;\mathrm{cm^{-1}}$ against which the couplings of [4] should be read.

Collectively, these works define the experimentally realistic parameter regime [4], the Markovian DAT baseline [2, 8], the system‑level and single‑complex timescales [5, 7, 11], the quantum‑correction scale [6], the methodological standard for unit consistency [1], the framework under test [10], and the corrected prior [9].

## 3. Methods

### 3.1 Toy model and corrected dephasing dissipator

We consider the two‑site Haken–Strobl Hamiltonian in the single‑excitation manifold

$$
H_{S}= \frac{\Delta}{2}\,\sigma_{z}+V\,\sigma_{x},
$$

where $\sigma_{x},\sigma_{z}$ are Pauli matrices on the two‑site basis, $\Delta$ is the site‑energy difference, and $V$ is the excitonic coupling. Site 2 carries a trap with rate $\kappa$.

The correct pure‑dephasing Lindblad generator with jump operator $\sigma_{z}$ is

$$
\mathcal{L}_{\phi}[\rho]=-\frac{\Gamma}{2}\,[\sigma_{z},[\sigma_{z},\rho]],
$$

which leaves populations invariant and damps the coherence as $\dot{\rho}_{12}=-2\Gamma\,\rho_{12}$. This form replaces the defective term $-(\Gamma/2)(1-\sigma_z^{2}/2)$ of the published version: since $\sigma_z^{2}=\mathbb{1}$, that expression equals $-(\Gamma/4)\mathbb{1}$, a multiple of the identity that generates no dephasing at all. Any optimality analysis built on it was vacuous; all results below use the corrected generator.

### 3.2 Re‑entry criterion

The memory ratio is defined as

$$
R=\frac{\tau_{B}}{\tau_{T}},
$$

with $\tau_{B}$ the bath correlation time and $\tau_{T}$ the intrinsic single‑hop transfer time (Section 4.2). Thresholds are conventions chosen to render the criterion falsifiable:

* $R\lesssim0.1$: Markovian reduction suffices.
* $0.1<R<0.5$: Transitional regime; error estimation required.
* $R\gtrsim0.5$: Non‑Markovian framework required.

### 3.3 Input parameters

| Symbol | Value | Source / status |
|--------|-------|-----------------|
| $V$ | $|V|\in[50,75]\;\mathrm{cm^{-1}}$ | Reported in [4] |
| $\Delta$ | $[110,180]\;\mathrm{cm^{-1}}$ | Reported in [4] |
| $\kappa$ | $1\;\mathrm{ps^{-1}}$ | Assumption of this paper |
| $\tau_{e}$ | $1\;\mathrm{ns}$ | Assumption of this paper |
| $\tau_{B}$ | $0.1\;\mathrm{ps}$ (fast) and $1\;\mathrm{ps}$ (slow) | Fast value motivated by [7]; slow value an assumption |
| $c$ | $2.9979\times10^{10}\;\mathrm{cm\,s^{-1}}$ | Defined constant for unit conversion |

All parameters are either taken directly from the cited literature or explicitly labelled as assumptions. The sign of $V$ is irrelevant to $V^{2}$ in every formula below, so the reported negative couplings of [4] enter through their magnitudes.

## 4. Analysis

### 4.1 Optimal dephasing rate and hopping rate

In the strong‑disorder limit $V\ll\Delta$, adiabatic elimination of the coherences in the Haken–Strobl master equation with the corrected pure‑dephasing generator yields the hopping rate

$$
k(\Gamma)=\frac{2V^{2}\,\Gamma}{\Gamma^{2}+\Delta^{2}}.
$$

Differentiating with respect to $\Gamma$:

$$
\frac{\mathrm{d}k}{\mathrm{d}\Gamma}=2V^{2}\,\frac{(\Gamma^{2}+\Delta^{2})-2\Gamma^{2}}{(\Gamma^{2}+\Delta^{2})^{2}}
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

#### Numerical range of $k^{*}$

Evaluating $k^{*}=V^{2}/\Delta$ at the four corners of the corrected experimental box:

| Corner | $V$ ($\mathrm{cm^{-1}}$) | $\Delta$ ($\mathrm{cm^{-1}}$) | $k^{*}=V^{2}/\Delta$ ($\mathrm{cm^{-1}}$) |
|--------|----------------|----------------------|-----------------------------------|
| 1 (min $V$, max $\Delta$) | $50$ | $180$ | $13.8889$ |
| 2 (min $V$, min $\Delta$) | $50$ | $110$ | $22.7273$ |
| 3 (max $V$, max $\Delta$) | $75$ | $180$ | $31.2500$ |
| 4 (max $V$, min $\Delta$) | $75$ | $110$ | $51.1364$ |

Thus

$$
k^{*}\in[13.89,\,51.14]\;\mathrm{cm^{-1}}.
$$

### 4.2 Transfer time $\tau_{T}$

The optimal hopping rate $k^{*}$ has units of wavenumber ($\mathrm{cm^{-1}}$). Converting to angular frequency $\omega^{*}=2\pi c\,k^{*}=2\pi c\,V^{2}/\Delta$, the transfer time is the inverse:

$$
\tau_{T}= \frac{1}{\omega^{*}} = \frac{\Delta}{2\pi c V^{2}}.
$$

**Dimensional check.** With $\Delta$ and $V$ in $\mathrm{cm^{-1}}$ and $c$ in $\mathrm{cm\,s^{-1}}$, the numerator has units $\mathrm{cm^{-1}}$ and the denominator $2\pi cV^{2}$ has units $\mathrm{cm\,s^{-1}}\times\mathrm{cm^{-2}}=\mathrm{cm^{-1}\,s^{-1}}$, so the ratio has units of seconds. The published expression $\hbar\Delta/(2\pi cV^{2})$ instead carries an extra factor of action ($\mathrm{cm^{-1}\,s}$ in wavenumber units) and yields units of $\mathrm{s^{2}}$; it is dimensionally inconsistent and is discarded.

#### Extremal transfer times

*Maximum* $\tau_{T}$ (smallest $V$, largest $\Delta$): $V=50$, $\Delta=180$

$$
\begin{aligned}
\tau_{T}^{\mathrm{max}} &= \frac{180}{2\pi c \, 50^{2}}\\
&= \frac{180}{2\pi \times 2.9979\times10^{10}\times 2500}\\
&= \frac{180}{4.70912\times10^{14}}\\
&= 3.8223\times10^{-13}\;\mathrm{s}\\
&= 0.3822\;\mathrm{ps}.
\end{aligned}
$$

*Minimum* $\tau_{T}$ (largest $V$, smallest $\Delta$): $V=75$, $\Delta=110$

$$
\begin{aligned}
\tau_{T}^{\mathrm{min}} &= \frac{110}{2\pi c \, 75^{2}}\\
&= \frac{110}{2\pi \times 2.9979\times10^{10}\times 5625}\\
&= \frac{110}{1.05955\times10^{15}}\\
&= 1.0382\times10^{-13}\;\mathrm{s}\\
&= 0.1038\;\mathrm{ps}.
\end{aligned}
$$

Hence

$$
\tau_{T}\in[0.1038,\,0.3822]\;\mathrm{ps}.
$$

### 4.3 Trapping‑limited efficiency $\eta$

The recombination rate is

$$
\gamma_{\mathrm{rec}} = \frac{1}{\tau_{e}} = \frac{1}{1\;\mathrm{ns}} = 10^{-3}\;\mathrm{ps^{-1}}.
$$

The single‑hop trapping efficiency for a trap rate $\kappa$ and recombination $\gamma_{\mathrm{rec}}$ is

$$
\eta = \frac{\kappa}{\kappa+\gamma_{\mathrm{rec}}}
= \frac{1}{1+10^{-3}}
= \frac{1}{1.001}
= 0.999001.
$$

### 4.4 Memory ratio $R$ and regime classification

Using the bounds for $\tau_{T}$:

$$
R_{\mathrm{fast}} = \frac{0.1\;\mathrm{ps}}{\tau_{T}} \in \left[\frac{0.1}{0.3822},\frac{0.1}{0.1038}\right]
= [0.2616,\,0.9634].
$$

$$
R_{\mathrm{slow}} = \frac{1\;\mathrm{ps}}{\tau_{T}} \in \left[\frac{1}{0.3822},\frac{1}{0.1038}\right]
= [2.6165,\,9.6339].
$$

Rounding to two significant figures gives

$$
R_{\mathrm{fast}}\in[0.26,0.96],\qquad
R_{\mathrm{slow}}\in[2.6,9.6].
$$

All $R_{\mathrm{slow}}$ values exceed the $0.5$ threshold, placing every realistic slow‑mode bath in the non‑Markovian sector. Fast baths fall below $0.5$ only for the smallest $V$ and largest $\Delta$, leaving a transitional window rather than a uniformly Markovian sector — the corrected quantitative content of the published abstract's qualitative statement.

### 4.5 Sensitivity of the classification to the reported box

Because $R=\tau_{B}\,2\pi cV^{2}/\Delta$ is monotone increasing in $V$ and decreasing in $\Delta$, the extremes of $R$ over the box occur at the corners already evaluated; no interior extremum exists. The classification is therefore robust over the full reported range $|V|\in[50,75]\;\mathrm{cm^{-1}}$, $\Delta\in[110,180]\;\mathrm{cm^{-1}}$ [4]: $R_{\mathrm{slow}}>0.5$ at every corner, and $R_{\mathrm{fast}}<0.5$ only at the corner $(V,\Delta)=(50,180)$, where $R_{\mathrm{fast}}=0.2616$. The published claim that the box extended down to $V=20\;\mathrm{cm^{-1}}$ would have added a corner with $\tau_{T}=180/(2\pi c\cdot400)=2.389\times10^{-12}\;\mathrm{s}=2.389\;\mathrm{ps}$ and $R_{\mathrm{fast}}=0.0419$ — a genuinely Markovian point — but that corner is not supported by the reported couplings of [4] and is removed.

## 5. Results

All numerical values follow directly from the derivations in Section 4.

1. **Optimal dephasing rate:** $\Gamma^{*}= \Delta$, ranging from $110$ to $180\;\mathrm{cm^{-1}}$.
2. **Optimal hopping rate:** $k^{*}=V^{2}/\Delta$, ranging from $13.89$ to $51.14\;\mathrm{cm^{-1}}$.
3. **Transfer time:** $\tau_{T}=0.1038\text{–}0.3822\;\mathrm{ps}$, with the representative corner values $0.1038\;\mathrm{ps}$ (min) and $0.3822\;\mathrm{ps}$ (max).
4. **Single‑hop efficiency:** $\eta=0.999001$.
5. **Memory ratios:** $R_{\mathrm{fast}}\in[0.26,0.96]$, $R_{\mathrm{slow}}\in[2.6,9.6]$.
6. **Sensitivity:** $R_{\mathrm{slow}}$ always exceeds $0.5$; $R_{\mathrm{fast}}$ falls below $0.5$ only for $V=50\;\mathrm{cm^{-1}}$ and $\Delta=180\;\mathrm{cm^{-1}}$.

**Projection.** If $R\gtrsim0.5$, the non‑Markovian framework predicts a shift of the optimal dephasing rate $\delta\Gamma^{*}$ that scales as

$$
\frac{\delta\Gamma^{*}}{\Gamma^{*}} \approx R,
$$

with a proportionality constant of order unity and an uncertainty factor of two, the latter chosen to match the factor‑of‑2 scale of quantum vibrational corrections reported in [6]. This hypothesis is falsifiable by full‑scale non‑Markovian simulations of the seven‑site FMO Hamiltonian under the condition stated in Section 6.

## 6. Discussion

### Limitations

* **Two‑site abstraction.** Real light‑harvesting complexes contain multiple pigments, static disorder, and multiple pathways; the single‑hop efficiency $\eta$ therefore represents an upper bound. The atomistic study of the full green‑sulfur apparatus [5] shows that system‑level funneling completes on a 10 ps timescale with scenario‑dependent behaviour only within the first 500 fs, so dimer‑level conclusions should not be read as network‑level predictions.
* **Threshold conventions.** The $R$ thresholds are chosen for falsifiability; alternative thresholds would shift the transitional window but not the qualitative conclusion that slow vibrational modes demand a non‑Markovian treatment.
* **Weak‑coupling assumption.** The Haken–Strobl rate formula assumes $V\ll\Delta$ and weak system–bath coupling; strong coupling would invalidate the analytic $k(\Gamma)$ expression and require the exact non‑Markovian treatment. At the box corner $(V,\Delta)=(75,110)$ the ratio $V/\Delta=0.68$ strains this assumption, so the $k^{*}$ and $\tau_{T}$ values there carry the largest model error.
* **Assumed bath times.** Both $\tau_{B}=0.1\;\mathrm{ps}$ and $\tau_{B}=1\;\mathrm{ps}$ are assumptions; only the fast value is motivated by the sub‑100‑fs relaxation resolved in single complexes [7]. The classification of a given real bath depends directly on these assumed values.
* **Vibronic effects excluded.** The reported $180\;\mathrm{cm^{-1}}$ modes with Huang–Rhys factor 0.03 [4] and the fs‑scale vibronic coherences documented for FMO and LHCII [11] are outside the pure‑dephasing model; they could modify $\tau_{T}$ and the